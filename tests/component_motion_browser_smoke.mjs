/** Real Chromium checks for 5 distinct local component motion mechanisms, not page transitions. */
import {chromium} from 'playwright';
import path from 'node:path';
import fs from 'node:fs';
import {fileURLToPath,pathToFileURL} from 'node:url';
import assert from 'node:assert/strict';
const dir=path.dirname(fileURLToPath(import.meta.url));
const url=pathToFileURL(path.join(dir,'../assets/component-motion-lab.html')).href;
async function run(){
 const browser=await chromium.launch({headless:true});
 const out=path.resolve('component-motion-browser-artifacts');fs.mkdirSync(out,{recursive:true});
 try {
  for(const width of [1280,390]){
   for(const pref of ['no-preference','reduce']){
    const page=await browser.newPage({viewport:{width,height:850},reducedMotion:pref});
    await page.goto(url);
    for(const level of ['none','balanced']){
     await page.locator('[data-level="'+level+'"]').click();
     const moving=level==='balanced' && pref==='no-preference';
     const initial=await page.locator('#indicator').evaluate(x=>x.getBoundingClientRect().left);
     await page.locator('#tab-activity').click();
     assert.equal(await page.locator('#tab-result').innerText(),'展示最近活动');
     assert.equal(await page.locator('#tab-activity').getAttribute('aria-selected'),'true');
     const duration=await page.locator('#indicator').evaluate(x=>parseFloat(getComputedStyle(x).transitionDuration));
     assert.equal(duration>0,moving,'indicator transition mismatch');
     const moved=await page.locator('#indicator').evaluate(x=>x.getBoundingClientRect().left);
     if(moving)assert.ok(moved>=initial-1,'indicator cannot reverse unexpectedly');
     await page.waitForTimeout(320);
     const final=await page.locator('#indicator').evaluate(x=>x.getBoundingClientRect().left);
     assert.ok(final>initial+10,'tab indicator must move to different position');
     await page.locator('#tab-summary').click();
     assert.equal(await page.locator('#tab-result').innerText(),'展示概览信息');
     const a=page.locator('#accordion');
     const panel=page.locator('#reveal');
     assert.equal(await a.getAttribute('aria-expanded'),'false');
     await a.click();
     assert.equal(await a.getAttribute('aria-expanded'),'true');
     const disclosureDuration=await panel.evaluate(x=>parseFloat(getComputedStyle(x).transitionDuration));
     assert.equal(disclosureDuration>0,moving,'accordion transition mismatch');
     await page.waitForTimeout(320);
     assert.ok((await panel.boundingBox()).height>35,'expanded disclosure must take space');
     await a.click();
     await page.waitForTimeout(320);
     assert.ok((await panel.boundingBox()).height<1,'disclosure must collapse');
     const sw=page.locator('#switch'),thumb=page.locator('#thumb');
     await sw.click();
     assert.equal(await sw.getAttribute('aria-checked'),'true');
     assert.equal(await page.locator('#switch-label').innerText(),'自动刷新：开启');
     const thumbDuration=await thumb.evaluate(x=>parseFloat(getComputedStyle(x).transitionDuration));
     assert.equal(thumbDuration>0,moving,'switch motion mismatch');
     await page.waitForTimeout(320);
     assert.ok((await thumb.evaluate(x=>new DOMMatrix(getComputedStyle(x).transform).m41))>15,'thumb must track state');
     await sw.click();
     assert.equal(await sw.getAttribute('aria-checked'),'false');
     const prev=await page.locator('#records li').count();
     await page.locator('#add-record').click();
     assert.equal(await page.locator('#records li').count(),prev+1);
     const row=page.locator('#records li').last();
     const rowDuration=await row.evaluate(x=>parseFloat(getComputedStyle(x).animationDuration));
     assert.equal(rowDuration>0,moving,'record appearance motion mismatch');
     await page.locator('#confirm').click();
     assert.equal(await page.locator('#toast').innerText(),'模拟保存成功');
     const toastDuration=await page.locator('#toast').evaluate(x=>parseFloat(getComputedStyle(x).animationDuration));
     assert.equal(toastDuration>0,moving,'outcome feedback mismatch');
     const widthOverflow=await page.evaluate(()=>document.documentElement.scrollWidth>window.innerWidth+1);
     assert.equal(widthOverflow,false,'Unexpected horizontal overflow');
    }
    if(pref==='no-preference'){
      await page.locator('[data-level=balanced]').click();
      await page.locator('#reduce').check();
      await page.locator('#tab-activity').click();
      assert.equal(await page.locator('#indicator').evaluate(x=>parseFloat(getComputedStyle(x).transitionDuration)),0,'manual reduce motion must disable indicator');
      assert.equal(await page.locator('#tab-result').innerText(),'展示最近活动');
    }
    await page.screenshot({path:path.join(out,width+'-'+pref+'.png'),fullPage:true});
    await page.close();
   }
  }
  console.log('Component motion Chromium PASS: tabs indicator + accordion + toggle + list insertion + status feedback; normal/reduced/none, 1280/390');
 }finally{await browser.close()}
}
run().catch(e=>{console.error(e);process.exit(1)});
