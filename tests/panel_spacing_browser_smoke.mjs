/** Regression proof: unannotated card surfaces must keep independent gaps. */
import {chromium} from 'playwright';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {auditPanelSpacing} from '../scripts/audit_panel_spacing.mjs';
const here=path.dirname(fileURLToPath(import.meta.url));
const url=pathToFileURL(path.join(here,'../assets/spacing-rhythm-lab.html')).href;

async function run(){
 const browser=await chromium.launch({headless:true});
 const out=path.resolve('panel-spacing-browser-artifacts');
 fs.mkdirSync(out,{recursive:true});
 try{
  for(const width of [1280,390,320])for(const fontPct of [100,200]){
   const page=await browser.newPage({viewport:{width,height:850}});
   await page.goto(url);
   await page.evaluate(p=>document.documentElement.style.fontSize=p+'%',fontPct);
   // Remove legacy identifiers to prove auto risk scanning does not need opt-in markings.
   await page.evaluate(()=>document.querySelectorAll('[data-mf-space-id]').forEach(el=>el.removeAttribute('data-mf-space-id')));
   const options={selector:'.stack',requirePairs:true,minPairs:4};
   const good=await auditPanelSpacing(page,options);
   assert.equal(good.passed,true,'Healthy independent layout must pass '+width+'/'+fontPct+': '+JSON.stringify(good.issues));
   assert.ok(good.observations.some(x=>x.axis==='block'),'Vertical panel distances must be measured');
   assert.ok(good.observations.some(x=>x.axis==='inline')||width<661,'Wide panels should include horizontal peers');
   await page.screenshot({path:path.join(out,'before-'+width+'-'+fontPct+'.png'),fullPage:true});
   await page.locator('[data-state-option=bad]').click();
   const collapsed=await auditPanelSpacing(page,options);
   assert.equal(collapsed.passed,false,'Zero-gap independent panels must fail without explicit markup '+width+'/'+fontPct);
   assert.ok(collapsed.issues.filter(x=>x.code==='UNJUSTIFIED_PANEL_CONTACT').length>=3,'Detect multiple independent contacts');
   const collapsedAxes=new Set(collapsed.issues.filter(x=>x.code==='UNJUSTIFIED_PANEL_CONTACT').map(x=>x.axis));
   assert.ok(collapsedAxes.has('block'),'Vertical gap collapse must not hide behind horizontal gutter');
   await page.screenshot({path:path.join(out,'after-collapsed-'+width+'-'+fontPct+'.png'),fullPage:true});
   await page.locator('[data-state-option=good]').click();
   const normal=await auditPanelSpacing(page,{...options,baseline:good});
   assert.equal(normal.passed,true,'Restored layout should match approved baseline');
   // Nonzero gaps can still be a severe regression; compare to before screenshot geometry.
   await page.evaluate(()=>{
     const el=document.getElementById('demo-page');
     el.style.setProperty('--demo-space-section','0.55rem');
     el.style.setProperty('--demo-space-peer','0.45rem');
   });
   const compressed=await auditPanelSpacing(page,{...options,baseline:good});
   assert.equal(compressed.passed,false,'Large reductions must fail even if new gap is nonzero');
   assert.ok(compressed.issues.some(x=>x.code==='SPACING_REGRESSION'),'Baseline degradation must be explicitly reported');
   await page.close();
  }
  const page=await browser.newPage({viewport:{width:500,height:500}});
  await page.setContent(`<!doctype html><html><body style="margin:0">
    <main>
     <div id="joined" style="display:grid;gap:0" data-mf-connected-reason="Tab labels and associated panel form one logical surface">
      <section style="width:360px;min-height:70px;border:1px solid #aaa;background:white">Tabs</section>
      <section style="width:360px;min-height:120px;border:1px solid #aaa;background:white">Panel</section>
     </div>
    </main>
   </body></html>`);
  const joined=await auditPanelSpacing(page,{requirePairs:true});
  assert.equal(joined.passed,true,'Documented contiguous component must remain permitted');
  assert.ok(joined.observations.some(x=>x.connected===true),'Connected surfaces still measured');
  await page.locator('#joined').evaluate(el=>el.removeAttribute('data-mf-connected-reason'));
  const undocumented=await auditPanelSpacing(page,{requirePairs:true});
  assert.equal(undocumented.passed,false,'Undocumented contact is not exempt');
  assert.ok(undocumented.issues.some(x=>x.code==='UNJUSTIFIED_PANEL_CONTACT'));
  await page.close();
  console.log('Panel spacing regression PASS: unannotated DOM, 3 widths x 2 font scales, zero-gap/nonzero gap collapse, baseline restore and documented connected exceptions');
 }finally{await browser.close()}
}
run().catch(e=>{console.error(e);process.exitCode=1});
