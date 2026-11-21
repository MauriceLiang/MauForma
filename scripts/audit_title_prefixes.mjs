#!/usr/bin/env node
/**
 * Style-agnostic rendered DOM candidate discovery for title preambles.
 * It reports nearby text appearing before H1-H6/role=heading in the same
 * grouping. It DOES NOT make semantic deletion decisions or guarantee all
 * visible non-semantic/canvas/pseudo-element titles have been inspected.
 * No color, font, font-size, weight or letter-spacing based classification.
 *
 * Usage (requires project's already-available Playwright + Chromium):
 *   node scripts/audit_title_prefixes.mjs --url http://localhost:3000 --selector main
 * Optional: --out /tmp/title-prefix-candidates.json
 * Do not publish outputs containing private target-page text.
 */
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

export async function auditTitlePrefixes(page, options = {}) {
  return page.evaluate((opts) => {
    const root = document.querySelector(opts.selector || 'main')
      || document.querySelector('[role="main"]') || document.body;
    const isVisible = el => {
      if (!el || !el.isConnected || el.closest('[hidden],[inert],[aria-hidden="true"]')) return false;
      const css = getComputedStyle(el);
      if (css.display === 'none' || css.visibility !== 'visible' || Number(css.opacity) === 0) return false;
      const rect = el.getBoundingClientRect();
      return rect.width > 0 && rect.height > 0;
    };
    const pathFor = el => {
      const parts = [];
      for (let cur = el; cur && cur !== root && parts.length < 7; cur = cur.parentElement) {
        if (cur.id) { parts.unshift('#' + cur.id); break; }
        const siblings = cur.parentElement
          ? [...cur.parentElement.children].filter(e => e.tagName === cur.tagName) : [];
        parts.unshift(cur.tagName.toLowerCase() + (siblings.length > 1 ? ':nth-of-type(' + ([...cur.parentElement.children].filter(e => e.tagName === cur.tagName).indexOf(cur) + 1) + ')' : ''));
      }
      return parts.join(' > ');
    };
    const headings = [...root.querySelectorAll('h1,h2,h3,h4,h5,h6,[role="heading"]')]
      .filter(isVisible).slice(0, 250);
    const candidates = [];
    const seen = new Set();
    for (const title of headings) {
      const titleText = (title.innerText || title.textContent || '').replace(/\s+/g, ' ').trim();
      if (!titleText) continue;
      const t = title.getBoundingClientRect();
      let branch = title;
      let parent = title.parentElement;
      for (let depth = 0; parent && parent !== root && parent !== document.body && depth < 5; depth++) {
        if (/^(NAV|FOOTER|MAIN|BODY|HTML)$/.test(parent.tagName)) break;
        // Don't mistake a previous content section for the pretitle of the next section.
        if (depth > 0 && [...parent.querySelectorAll('h1,h2,h3,h4,h5,h6,[role="heading"]')].filter(isVisible).length > 1) break;
        let sibling = branch.previousElementSibling;
        for (let count = 0; sibling && count < 3; count++, sibling = sibling.previousElementSibling) {
          if (!isVisible(sibling)) continue;
          if (sibling.matches('h1,h2,h3,h4,h5,h6,[role="heading"]')
              || sibling.querySelector('h1,h2,h3,h4,h5,h6,[role="heading"]')) continue;
          const raw = (sibling.innerText || sibling.textContent || '').replace(/\s+/g, ' ').trim();
          if (!raw || raw.length > 180) continue;
          const r = sibling.getBoundingClientRect();
          // Visually before/above the title and within its heading group's nearby area.
          const gap = t.top - r.bottom;
          const xOverlap = Math.min(t.right, r.right) - Math.max(t.left, r.left);
          if (gap < -Math.max(12, t.height * 0.25) || gap > Math.max(144, t.height * 4)
              || xOverlap <= 0) continue;
          const key = pathFor(title) + '|' + pathFor(sibling);
          if (seen.has(key)) continue;
          seen.add(key);
          candidates.push({
            code: 'TITLE_PREFIX_CANDIDATE',
            title: titleText.slice(0, 180),
            title_level: title.getAttribute('aria-level') || (/^H[1-6]$/.test(title.tagName) ? Number(title.tagName[1]) : null),
            title_path: pathFor(title),
            prefix: raw,
            prefix_path: pathFor(sibling),
            signals: {
              preceding_in_group: true,
              near_title: true,
              contains_navigation: sibling.matches('nav,[role="navigation"]')
                || !!sibling.querySelector('nav,[role="navigation"]'),
              contains_link: !!sibling.querySelector('a[href]'),
              depth
            },
            semantic_decision: 'UNREVIEWED',
            note: 'Review information value AND whether a separate pre-title line is justified. Never auto-delete.'
          });
        }
        branch = parent;
        parent = parent.parentElement;
      }
    }
    return {
      status: candidates.length ? 'CANDIDATES_FOR_REVIEW' : 'NO_CANDIDATES_OBSERVED',
      verification: 'NOT_VERIFIED',
      inspected_headings: headings.length,
      candidates,
      scope: 'Rendered DOM structural hints; style-independent, not semantic classification or full visual coverage'
    };
  }, options);
}

async function cli() {
  const args = process.argv.slice(2);
  const opts = {};
  for (let i = 0; i < args.length; i++) {
    if (args[i].startsWith('--')) opts[args[i].slice(2)] = args[++i];
  }
  if (!opts.url) throw new Error('Usage: --url URL [--selector main] [--out filename]');
  const {chromium} = await import('playwright');
  const browser = await chromium.launch({headless: true});
  try {
    const page = await browser.newPage();
    await page.goto(opts.url, {waitUntil: 'domcontentloaded'});
    const report = await auditTitlePrefixes(page, {selector: opts.selector});
    if (opts.out) fs.writeFileSync(path.resolve(opts.out), JSON.stringify(report, null, 2) + '\n');
    console.log(JSON.stringify(report, null, 2));
  } finally {
    await browser.close();
  }
}
if (process.argv[1] && path.resolve(process.argv[1]) === fileURLToPath(import.meta.url))
  cli().catch(err => { console.error(err); process.exitCode = 2; });
