/** Synthetic, style-invariant title-prefix candidate discovery, not semantic auto-deletion. */
import assert from 'node:assert/strict';
import {chromium} from 'playwright';
import {auditTitlePrefixes} from '../scripts/audit_title_prefixes.mjs';

const browser = await chromium.launch({headless: true});
try {
  const signatureSets = [];
  for (const theme of [
    {color: '#2448c9', size: '11px', weight: '400', family: 'monospace'},
    {color: '#121212', size: '26px', weight: '800', family: 'serif'},
    {color: '#a85932', size: '18px', weight: '600', family: 'system-ui'}
  ]) {
    for (const width of [390, 1280]) {
      const page = await browser.newPage({viewport: {width, height: 850}});
      await page.setContent(`<!doctype html><html><head><style>
        body{margin:0;font:16px system-ui}
        main{max-width:680px;margin:auto;padding:20px}
        .prefix{display:block;color:${theme.color};font-size:${theme.size};font-weight:${theme.weight};font-family:${theme.family}}
        article,section,.intro{margin-bottom:32px}
        h1,h2,h3{margin:8px 0 12px}
        </style></head><body><main>
        <div class="intro"><span class="prefix" id="decorative">WORK AREA</span><div><h1>Projects</h1></div></div>
        <article><div class="prefix" id="step">Step 2 of 4</div><h3>Choose source</h3><p>Useful content follows.</p></article>
        <section><nav id="breadcrumb" aria-label="Breadcrumb"><a href="#home">Workspace</a> / Billing</nav><h2>Billing</h2></section>
        <section><span class="prefix" id="status">Offline</span><div role="heading" aria-level="3">Service</div></section>
        <section><h3>Standalone title</h3><p>No prefix here.</p></section>
        <section><span class="prefix">模块分类 · 功能导览</span><h4>Interactive visualizer</h4></section>
        <section><span class="prefix">SECTION CATEGORY</span><div><h5>Component overview</h5></div></section>
        <section><span class="prefix">MODULE CONTEXT</span><h6>Model preview</h6></section>
        </main></body></html>`);
      const report = await auditTitlePrefixes(page);
      const titles = report.candidates.map(x => x.title).sort();
      assert.deepEqual(titles, ['Billing', 'Choose source', 'Component overview', 'Interactive visualizer', 'Model preview', 'Projects', 'Service'], 'Discovered title-group prefixes at ' + width);
      assert.equal(report.inspected_headings, 8);
      assert.ok(report.candidates.every(x => x.semantic_decision === 'UNREVIEWED'),
        'Scanner must never auto-approve or auto-delete content');
      assert.equal(report.verification, 'NOT_VERIFIED');
      assert.equal(report.candidates.find(x => x.title === 'Billing').signals.contains_navigation, true,
        'Real navigation must be surfaced for semantic review, not deleted');
      signatureSets.push(JSON.stringify(titles));
      await page.close();
    }
  }
  assert.equal(new Set(signatureSets).size, 1, 'Candidates must not change across colors, font families, weights, sizes or viewports');
  console.log('Style-invariant title-prefix discovery PASS: 3 unrelated visual styles x 2 widths, H1–H6/role=heading and legitimate semantic examples');
} finally {
  await browser.close();
}
