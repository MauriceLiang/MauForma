/**
 * Baseline-free flaw discovery: intentionally broken pages must fail BEFORE any edit.
 * Entirely original synthetic DOM; no screenshots or project-specific content.
 */
import {chromium} from 'playwright';
import assert from 'node:assert/strict';
import {auditExistingVisualDefects} from '../scripts/audit_existing_visual_defects.mjs';

async function run(){
 const browser=await chromium.launch({headless:true});
 try{
  for(const width of [1280,390,320])for(const fontPct of [100,200]){
   const page=await browser.newPage({viewport:{width,height:800}});
   const html=`<!doctype html><html><head><meta name="viewport" content="width=device-width, initial-scale=1">
    <style>
     :root{font:16px system-ui}
     *{box-sizing:border-box}
     body{margin:0;background:#f5f7f8}
     main{max-width:900px;padding:16px;margin:auto}
     .card{background:white;border:1px solid #d5dde1;border-radius:8px;min-height:110px;padding:18px}
     #summary{margin-bottom:0}
     #plot{min-height:170px;margin-bottom:0}
     .row{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));column-gap:0}
     .row>.card{min-height:130px}
     [data-state=good] #summary,[data-state=good] #plot{margin-bottom:20px}
     [data-state=good] .row{column-gap:16px}
     @media(max-width:600px){.row{grid-template-columns:minmax(0,1fr)}.row>.card:first-child{margin-bottom:0}
      [data-state=good] .row>.card:first-child{margin-bottom:16px}}
    </style></head>
    <body><main id="sample" data-state="bad">
      <section id="summary" class="card">Synthetic status summary</section>
      <div class="wrapper"><section id="plot" class="card">Synthetic data plot</section></div>
      <div class="row"><section id="item-a" class="card">A</section><article id="item-b" class="card">B</article></div>
    </main></body></html>`;
   await page.setContent(html);
   await page.evaluate(p=>document.documentElement.style.fontSize=p+'%',fontPct);
   const bad=await auditExistingVisualDefects(page);
   assert.equal(bad.passed,false,'Existing defects must be reported at first scan '+width+'/'+fontPct);
   const found=bad.issues.filter(x=>x.code==='EXISTING_SURFACES_TOUCH');
   assert.ok(found.some(x=>x.axis==='block'),'Block-flow+wrapper contact should not be missed '+JSON.stringify(bad));
   assert.ok(found.length>=2,'Should find multiple offending panel boundaries');
   await page.locator('#sample').evaluate(el=>el.dataset.state='good');
   const good=await auditExistingVisualDefects(page);
   assert.equal(good.passed,true,'After restoring gaps should no longer report contact '+JSON.stringify(good.issues));
   await page.close();
  }

  const page=await browser.newPage({viewport:{width:800,height:640}});
  await page.setContent(`<!doctype html><html><body><main style="display:block">
    <div id="connected" data-mf-connected-reason="Tabs and their own visible panel form one continuous control">
      <section style="border:1px solid gray;min-height:100px;width:500px">Tabs</section>
      <section style="border:1px solid gray;min-height:120px;width:500px">Panel</section>
    </div>
   </main></body></html>`);
  const allowed=await auditExistingVisualDefects(page);
  assert.equal(allowed.passed,true,'Documented contiguous components should not be falsely rejected '+JSON.stringify(allowed.issues));
  assert.ok(allowed.measurements.some(x=>x.connected),'Connected pair must still be inspected');
  await page.locator('#connected').evaluate(el=>el.removeAttribute('data-mf-connected-reason'));
  const illegal=await auditExistingVisualDefects(page);
  assert.equal(illegal.passed,false,'Removal of justification makes a zero-gap pair an issue');
  await page.close();

  // Never treat a generic root-level exemption as authorization to join multiple panels.
  const root=await browser.newPage();
  await root.setContent(`<!doctype html><html><body><main
    data-mf-connected-reason="All panels should become connected with no space anywhere">
    <section style="border:1px solid gray;width:500px;min-height:80px">A</section>
    <section style="border:1px solid gray;width:500px;min-height:80px">B</section>
    <section style="border:1px solid gray;width:500px;min-height:80px">C</section>
    <section style="border:1px solid gray;width:500px;min-height:80px">D</section>
   </main></body></html>`);
  const report=await auditExistingVisualDefects(root);
  assert.equal(report.passed,false,'Generic page-level connected override must not bypass detection');
  await root.close();
  console.log('Baseline-free visual defect browser PASS: 3 widths x 2 font scales, pre-existing block-flow/wrapper/contact, recovered layout, local connected exemption and invalid root exemption');
 }finally{await browser.close()}
}
run().catch(e=>{console.error(e);process.exitCode=1});
