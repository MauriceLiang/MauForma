#!/usr/bin/env node
/**
 * Optional runtime evidence collector.
 * Requires user project's Playwright package and browser executable.
 * Do not auto-install packages or claim the result is an aesthetic pass.
 */
import fs from "node:fs/promises";
import path from "node:path";

const urlFlag = process.argv.indexOf("--url");
const outFlag = process.argv.indexOf("--out");
const target = urlFlag >= 0 ? process.argv[urlFlag + 1] : "";
if (!/^https?:\/\/.+/i.test(target)) {
  console.error("Usage: node scripts/browser_qa.mjs --url http://localhost:3000 [--out ./artifacts]");
  process.exit(2);
}
let chromium;
try {
  ({ chromium } = await import("playwright"));
} catch {
  console.error("Playwright is not installed in this environment. Run this in an authorized project with Playwright; no packages were installed.");
  process.exit(3);
}
const folder = path.resolve(outFlag >= 0 ? process.argv[outFlag + 1] : "artifacts/mauforma-qa");
await fs.mkdir(folder, { recursive: true });
const report = { target, generated_at: new Date().toISOString(),
  scope: "Browser rendering evidence only; not server-side business validation", screenshots: [], failures: [] };
let browser;
try {
  browser = await chromium.launch({ headless: true });
  for (const config of [{ label: "desktop", width: 1440, height: 900 },
                        { label: "tablet", width: 1024, height: 768 },
                        { label: "mobile", width: 390, height: 844 }]) {
    for (const reducedMotion of ["no-preference", "reduce"]) {
      const context = await browser.newContext({
        viewport: { width: config.width, height: config.height },
        reducedMotion
      });
      const page = await context.newPage();
      const pageErrors = [];
      page.on("pageerror", err => pageErrors.push(String(err)));
      let status = 0;
      try {
        const response = await page.goto(target, { waitUntil: "domcontentloaded", timeout: 30000 });
        status = response?.status() ?? 0;
        await page.evaluate(async () => {
          if (document.fonts?.ready) await Promise.race([
            document.fonts.ready, new Promise(resolve => setTimeout(resolve, 1500))
          ]);
        });
        const metrics = await page.evaluate(() => {
          const root = document.documentElement;
          return { title: document.title,
            horizontalOverflow: root.scrollWidth > innerWidth + 2,
            scrollWidth: root.scrollWidth, viewportWidth: innerWidth,
            mainVisible: !!document.querySelector("main"),
            visibleHeadings: [...document.querySelectorAll("h1,h2")]
              .filter(el => !!el.getClientRects().length).length };
        });
        await page.keyboard.press("Tab");
        const focus = await page.evaluate(() => ({
          tag: document.activeElement?.tagName,
          hasVisibleTarget: document.activeElement !== document.body
        }));
        const screenshot = path.join(folder, config.label + "-" + reducedMotion + ".png");
        await page.screenshot({ path: screenshot, fullPage: true });
        report.screenshots.push({ view: config.label, motion: reducedMotion, file: screenshot,
          status, metrics, focus, pageErrors });
        if (status >= 400 || metrics.horizontalOverflow || pageErrors.length) {
          report.failures.push({ view: config.label, motion: reducedMotion,
            status, horizontalOverflow: metrics.horizontalOverflow, pageErrors });
        }
      } catch (error) {
        report.failures.push({ view: config.label, motion: reducedMotion, error: String(error) });
      } finally {
        await context.close();
      }
    }
  }
} finally {
  if (browser) await browser.close();
}
const output = path.join(folder, "report.json");
await fs.writeFile(output, JSON.stringify(report, null, 2) + "\n", "utf8");
console.log(JSON.stringify({ report: output, captured: report.screenshots.length,
  failures: report.failures.length }, null, 2));
process.exit(report.failures.length ? 1 : 0);
