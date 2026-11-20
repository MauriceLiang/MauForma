#!/usr/bin/env node
/**
 * MauForma: framework-agnostic motion evidence collector.
 * Requires an already running site and Playwright/browser installed by the host.
 * Captures real interactions; does NOT rate beauty or prove business correctness.
 */
import fs from "node:fs/promises";
import path from "node:path";
import process from "node:process";

const args = process.argv.slice(2);
const flag = (name, fallback = "") => {
  const i = args.indexOf("--" + name);
  return i === -1 ? fallback : args[i + 1] ?? "";
};
if (args.includes("--help")) {
  console.log("Usage: node scripts/motion_rehearsal.mjs --url http://localhost:3000 --scenario ./scenario.json [--out ./artifacts/motion] [--width 1280 --height 800] [--reduced no-preference|reduce]");
  process.exit(0);
}
const target = flag("url");
const scenarioPath = flag("scenario");
const out = path.resolve(flag("out", "./artifacts/motion-rehearsal"));
if (!/^https?:\/\/.+/i.test(target) || !scenarioPath) {
  console.error("Requires --url and --scenario. Run --help for options.");
  process.exit(2);
}
let playwright;
try {
  playwright = await import("playwright");
} catch {
  console.error("NOT RUN: Playwright is unavailable. Install it in an authorized host project; no packages were installed.");
  process.exit(3);
}
let scenario;
try {
  scenario = JSON.parse(await fs.readFile(path.resolve(scenarioPath), "utf8"));
  if (!Array.isArray(scenario.steps) || !scenario.steps.length) throw new Error("scenario.steps must be a non-empty array");
} catch (error) {
  console.error("Invalid scenario:", String(error));
  process.exit(2);
}
const viewport = {
  width: Number(flag("width", scenario.viewport?.width ?? 1280)),
  height: Number(flag("height", scenario.viewport?.height ?? 800))
};
const reducedMotion = flag("reduced", scenario.reducedMotion ?? "no-preference");
if (!Number.isInteger(viewport.width) || !Number.isInteger(viewport.height) ||
    viewport.width < 240 || viewport.height < 240 ||
    !["reduce", "no-preference"].includes(reducedMotion)) {
  console.error("Invalid viewport or reduced-motion option.");
  process.exit(2);
}
const report = {
  source: "MauForma motion_rehearsal.mjs",
  target, viewport, reducedMotion, scenario: scenarioPath,
  generatedAt: new Date().toISOString(),
  evidenceOnly: true,
  manualReviewRequired: true,
  limitations: [
    "Screenshots are sampled, not a full video or frame-perfect playback.",
    "Capture intervals can be irregular; automatically detected candidates need visual review.",
    "Passing capture is not aesthetic approval, accessibility certification or backend E2E verification."
  ],
  pageErrors: [], steps: [], status: "NOT_RUN"
};
const safe = (value, i) => String(value || "step-" + (i + 1))
  .replace(/[^a-zA-Z0-9_-]/g, "-").slice(0, 64);
const sleep = (ms) => new Promise(resolve => setTimeout(resolve, ms));
let browser;
try {
  browser = await playwright.chromium.launch({ headless: true });
  const context = await browser.newContext({ viewport, reducedMotion });
  const page = await context.newPage();
  page.on("pageerror", error => report.pageErrors.push(String(error)));
  const response = await page.goto(target, { waitUntil: "domcontentloaded", timeout: 30000 });
  report.httpStatus = response?.status() ?? null;
  await page.evaluate(async () => { if (document.fonts?.ready) await document.fonts.ready; });

  const observe = async selectors => page.evaluate((selectors) => {
    const result = {};
    for (const selector of selectors) {
      let node;
      try { node = document.querySelector(selector); }
      catch { result[selector] = { error: "invalid selector" }; continue; }
      if (!node) { result[selector] = { missing: true }; continue; }
      const rect = node.getBoundingClientRect();
      const style = getComputedStyle(node);
      result[selector] = {
        x: +rect.x.toFixed(2), y: +rect.y.toFixed(2),
        width: +rect.width.toFixed(2), height: +rect.height.toFixed(2),
        opacity: style.opacity, transform: style.transform,
        display: style.display, visibility: style.visibility
      };
    }
    return result;
  }, selectors);

  for (let index = 0; index < scenario.steps.length; index += 1) {
    const step = scenario.steps[index];
    const name = safe(step.id, index);
    const folder = path.join(out, String(index + 1).padStart(2, "0") + "-" + name);
    await fs.mkdir(folder, { recursive: true });
    const intervalMs = Math.max(40, Math.min(500, Number(step.intervalMs ?? 80)));
    const captureMs = Math.max(0, Math.min(10000, Number(step.captureMs ?? 600)));
    const settleMs = Math.max(0, Math.min(10000, Number(step.settleMs ?? 250)));
    const selectors = [...new Set([...(step.track ?? []), ...(step.selector ? [step.selector] : [])])];
    const entry = { id: name, action: step.action, selector: step.selector ?? null,
      intervalMs, captureMs, settleMs, frames: [], findings: [], status: "NOT_RUN" };
    report.steps.push(entry);
    const capture = async label => {
      const start = Date.now();
      const filename = label + ".png";
      await page.screenshot({ path: path.join(folder, filename), fullPage: false });
      const geometry = await observe(selectors);
      entry.frames.push({ file: path.relative(out, path.join(folder, filename)),
        timeMs: Date.now(), durationMs: Date.now() - start, geometry });
    };

    try {
      await capture("before");
      const locator = step.selector ? page.locator(step.selector).first() : null;
      switch (step.action) {
        case "click": await locator.click({ timeout: 5000 }); break;
        case "hover": await locator.hover({ timeout: 5000 }); break;
        case "fill": await locator.fill(String(step.value ?? ""), { timeout: 5000 }); break;
        case "press":
          if (locator) await locator.press(String(step.key ?? "Enter"), { timeout: 5000 });
          else await page.keyboard.press(String(step.key ?? "Escape"));
          break;
        case "wait": await sleep(Number(step.ms ?? 100)); break;
        case "reduced-motion":
          if (!["reduce", "no-preference"].includes(step.value)) throw new Error("reduced-motion must be reduce/no-preference");
          await page.emulateMedia({ reducedMotion: step.value });
          break;
        default: throw new Error("Unsupported action: " + step.action);
      }
      const start = Date.now();
      let n = 0;
      while (Date.now() - start < captureMs) {
        const remaining = captureMs - (Date.now() - start);
        const wait = Math.max(0, Math.min(intervalMs, n * intervalMs - (Date.now() - start)));
        if (wait > 0) await sleep(wait);
        await capture("frame-" + String(n).padStart(3, "0"));
        n += 1;
        if (n >= 200 || remaining <= 0) break;
      }
      if (settleMs) await sleep(settleMs);
      await capture("settled");
      const frames = entry.frames;
      for (let i = 2; i < frames.length - 1; i++) {
        const delta = frames[i].timeMs - frames[i - 1].timeMs;
        if (delta > intervalMs * 1.6) {
          entry.findings.push({ kind: "sampling-gap", frame: i, actualMs: delta,
            expectedMs: intervalMs, note: "Coverage inconclusive; do not claim frame-perfect capture" });
        }
      }
      entry.status = entry.findings.length ? "INCONCLUSIVE" : "CAPTURED_FOR_REVIEW";
    } catch (error) {
      entry.status = "BLOCKED";
      entry.findings.push({ kind: "runtime-error", message: String(error) });
    }
  }
  await context.close();
  if (report.pageErrors.length || report.httpStatus >= 400 ||
      report.steps.some(step => step.status === "BLOCKED")) {
    report.status = "BLOCKED";
  } else if (report.steps.some(step => step.status === "INCONCLUSIVE")) {
    report.status = "INCONCLUSIVE";
  } else {
    report.status = "CAPTURED_FOR_REVIEW";
  }
} catch (error) {
  report.status = "BLOCKED";
  report.fatalError = String(error);
} finally {
  if (browser) await browser.close();
  await fs.mkdir(out, { recursive: true });
  await fs.writeFile(path.join(out, "report.json"), JSON.stringify(report, null, 2) + "\n");
  console.log(JSON.stringify({ report: path.join(out, "report.json"),
    status: report.status, steps: report.steps.length, pageErrors: report.pageErrors.length }, null, 2));
}
process.exit(report.status === "BLOCKED" ? 1 : report.status === "INCONCLUSIVE" ? 2 : 0);
