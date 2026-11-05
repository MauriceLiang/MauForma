/** Cross-viewport semantic spacing regression: intentionally broken examples MUST be caught. */
import {chromium} from 'playwright';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import {auditSpacing} from '../scripts/audit_spacing_rhythm.mjs';
const dir=path.dirname(fileURLToPath(import.meta.url));
const url=pathToFileURL(path.join(dir,'../assets/spacing-rhythm-lab.html')).href;
const contract=JSON.parse(fs.readFileSync(path.join(dir,'../assets/spacing-rhythm-lab-contract.json'),'utf8'));
async function run(){
 const browser=await chromium.launch({headless:true});
 const output=path.resolve('spacing-rhythm-browser-artifacts');
 fs.mkdirSync(output,{recursive:true});
 try{
  for(const width of [1280,390,320]){
   for(const fontPct of [100,200]){
    const page=await browser.newPage({viewport:{width,height:760}});
    await page.goto(url);
    await page.evaluate(p=>{document.documentElement.style.fontSize=p+'%';},fontPct);
    const good=await auditSpacing(page,contract);
    assert.equal(good.passed,true,'Well-spaced layout should pass '+width+'/'+fontPct+': '+JSON.stringify(good.issues));
    assert.equal(good.measurements.length,contract.pairs.length);
    const joined=good.measurements.find(x=>x.id==='tabs-to-panel');
    assert.ok(Math.abs(joined.gapPx)<=1.5,'Intentional joined surfaces may have zero gap');
    const peers=good.measurements.find(x=>x.id==='language-to-scatter');
    assert.equal(peers.axis,width>=661?'inline':'block','Responsive peers should change layout orientation, not disappear');
    await page.screenshot({path:path.join(output,width+'-'+fontPct+'-good.png'),fullPage:true});
    await page.locator('[data-state-option=bad]').click();
    const bad=await auditSpacing(page,contract);
    assert.equal(bad.passed,false,'Intentionally touching independent panels must fail');
    const failures=bad.issues.filter(x=>x.code==='INSUFFICIENT_SPACING').map(x=>x.id);
    for(const required of ['overview-to-charts','language-to-scatter','charts-to-quality','quality-to-limits','chart-heading-to-plot']){
      assert.ok(failures.includes(required),'Missing under-spacing diagnosis for '+required+': '+JSON.stringify(bad.issues));
    }
    assert.ok(!bad.issues.some(x=>x.id==='tabs-to-panel'),'Connected surface must not be a false positive');
    await page.locator('[data-state-option=good]').click();
    const recovered=await auditSpacing(page,contract);
    assert.equal(recovered.passed,true,'Restored spacing must recover');
    await page.close();
   }
  }
  console.log('Semantic spacing browser PASS: 3 widths × 2 font scales; distinct/inside/peer gaps, intentionally connected zero-gap, bad-case detection and recovery');
 }finally{await browser.close()}
}
run().catch(e=>{console.error(e);process.exit(1)});
