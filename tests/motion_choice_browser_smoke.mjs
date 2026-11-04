/** Chromium checks: user-selectable motion actually runs, and reduced motion preserves usability. */
import {chromium} from 'playwright';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';
import fs from 'node:fs';
import assert from 'node:assert/strict';
const dirname=path.dirname(fileURLToPath(import.meta.url));
const url=pathToFileURL(path.join(dirname,'../assets/motion-choice-layout-lab.html')).href;
async function run(){
 const browser=await chromium.launch({headless:true});
 const out=path.resolve('motion-choice-browser-artifacts');fs.mkdirSync(out,{recursive:true});
 try{
  for(const viewport of [{width:1280,height:900},{width:390,height:844}]){
   for(const reduced of ['no-preference','reduce']){
    const page=await browser.newPage({viewport,reducedMotion:reduced});
    await page.goto(url);
    for(const [mode,shouldRun] of [['none',false],['balanced',reduced==='no-preference'],['expressive',reduced==='no-preference']]){
     await page.locator('[data-motion-option="'+mode+'"]').click();
     assert.equal(await page.locator('[data-motion-option="'+mode+'"]').getAttribute('aria-pressed'),'true');
     await page.locator('#tab-b').click();
     assert.equal(await page.locator('#pane-heading').innerText(),'趋势分析');
     assert.equal(await page.locator('#tab-b').getAttribute('aria-selected'),'true');
     const effect=await page.locator('#pane').evaluate(el=>{
      const style=getComputedStyle(el);
      return {duration:parseFloat(style.animationDuration),hasContent:el.innerText.length>0}
     });
     assert.ok(effect.hasContent,'selected content must stay visible');
     assert.equal(effect.duration>0,shouldRun,'incorrect animation strength '+viewport.width+'/'+reduced+'/'+mode);
     await page.locator('#open-dialog').click();
     assert.ok(await page.locator('#details').evaluate(el=>el.open));
     await page.keyboard.press('Escape');
     assert.ok(!(await page.locator('#details').evaluate(el=>el.open)),'Escape must close immediately');
     await page.locator('#show-result').click();
     assert.equal(await page.locator('#message').innerText(),'模拟操作已完成');
     await page.locator('#tab-a').click();
     assert.equal(await page.locator('#pane-heading').innerText(),'当前概览');
     const overflow=await page.evaluate(()=>document.documentElement.scrollWidth>innerWidth+1);
     assert.equal(overflow,false,'unexpected horizontal overflow');
    }
    if(reduced==='no-preference'){
     await page.locator('[data-motion-option="expressive"]').click();
     await page.locator('#reduce').check();
     await page.locator('#tab-b').click();
     const d=await page.locator('#pane').evaluate(el=>parseFloat(getComputedStyle(el).animationDuration));
     assert.equal(d,0,'explicit reduce motion must disable motion');
     assert.equal(await page.locator('#pane-heading').innerText(),'趋势分析');
    }
    await page.screenshot({path:path.join(out,viewport.width+'-'+reduced+'.png'),fullPage:true});
    await page.close();
   }
  }
  console.log('Motion choice browser smoke PASS: 2 widths × 2 OS preferences × 3 motion levels; dialogs, tabs, feedback, local reduction');
 }finally{await browser.close()}
}
run().catch(e=>{console.error(e);process.exit(1)});
