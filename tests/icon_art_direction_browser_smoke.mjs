/** Test visually measurable icon consistency; counterexample must fail. */
import {chromium} from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import assert from 'node:assert/strict';
import {auditIcons} from '../scripts/audit_icon_consistency.mjs';
const dir=path.dirname(fileURLToPath(import.meta.url));
const url=pathToFileURL(path.join(dir,'../assets/icon-art-direction-lab.html')).href;
async function run(){
 const browser=await chromium.launch({headless:true});
 const out=path.resolve('icon-art-direction-browser-artifacts');fs.mkdirSync(out,{recursive:true});
 try{
  for(const width of [1280,390,320]){
   for(const size of [20,16]){
    const page=await browser.newPage({viewport:{width,height:790}});
    await page.goto(url);
    await page.locator('[data-scale="'+size+'"]').click();
    await page.locator('[data-mode=good]').click();
    const good=await auditIcons(page);
    assert.equal(good.passed,true,'Curated icons must render consistently: '+width+'/'+size+': '+JSON.stringify(good.issues));
    assert.equal(good.groups[0].iconCount,6);
    assert.equal(new Set(good.groups[0].icons.map(x=>x.name)).size,6,'Distinct navigation labels need distinct glyphs');
    assert.ok(good.groups[0].icons.every(x=>x.pack==='lucide'));
    await page.locator('[data-nav-id=analysis]').click();
    assert.equal(await page.locator('[data-nav-id=analysis]').getAttribute('aria-current'),'page');
    assert.equal(await page.locator('[data-nav-id=settings]').getAttribute('aria-current'),'false');
    const current=await page.locator('[data-nav-id=analysis] [data-mf-ui-icon]').getAttribute('data-mf-icon-name');
    assert.equal(current,'chart-scatter','Selected nav should retain the chosen identity');
    await page.locator('[data-nav-id=settings]').focus();
    assert.equal(await page.locator('[data-nav-id=settings]').evaluate(x=>document.activeElement===x),true);
    await page.screenshot({path:path.join(out,'curated-'+width+'-'+size+'.png'),fullPage:true});
    await page.locator('[data-mode=bad]').click();
    const bad=await auditIcons(page);
    assert.equal(bad.passed,false,'Unreviewed inconsistent set should fail objective risk checks');
    const codes=new Set(bad.issues.map(x=>x.code));
    for(const expected of ['MIXED_ICON_PACK','INCONSISTENT_ICON_SIZE','INCONSISTENT_STROKE','ICON_LABEL_MISALIGNMENT'])
     assert.ok(codes.has(expected),'Missing icon risk diagnosis: '+expected+' '+JSON.stringify(bad.issues));
    await page.locator('[data-mode=good]').click();
    assert.equal((await auditIcons(page)).passed,true,'Returning to curated set must recover');
    await page.close();
   }
  }
  console.log('Icon art-direction browser PASS: 3 widths × 2 icon sizes; real SVG rendering, selection/focus, incorrect set detection and recovery');
 } finally{await browser.close()}
}
run().catch(e=>{console.error(e);process.exit(1)});
