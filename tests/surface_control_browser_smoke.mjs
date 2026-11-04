/** Chromium visual geometry smoke for generic surfaces and atomic short actions (demo only). */
const {chromium} = require('playwright');
const path = require('path');
const fs = require('fs');
const {pathToFileURL} = require('url');
const assert = require('node:assert/strict');

async function test() {
 const browser=await chromium.launch({headless:true});
 const out=path.resolve('surface-control-browser-artifacts');
 fs.mkdirSync(out,{recursive:true});
 const url=pathToFileURL(path.resolve(__dirname,'../assets/surface-control-layout-lab.html')).href;
 try {
  for (const width of [1280,390,320]) {
   for (const zoom of [100,200]) {
    const page=await browser.newPage({viewport:{width,height:850},deviceScaleFactor:1});
    await page.goto(url);
    await page.evaluate(z=>{ document.documentElement.style.fontSize=z+'%'; },zoom);
    for (const mode of ['flat','panel','cards']) {
     await page.locator('[data-variant="'+mode+'"]').click();
     assert.equal(await page.locator('#sample').getAttribute('class'),mode);
     const result=await page.evaluate(() => {
       const vw=window.innerWidth;
       const problems=[];
       const atomic=[...document.querySelectorAll('[data-mf-atomic-control]')];
       atomic.forEach((btn,index)=>{
         const label=btn.querySelector('[data-mf-control-label]');
         const rect=btn.getBoundingClientRect();
         const range=document.createRange();
         range.selectNodeContents(label);
         const fragmentRects=[...range.getClientRects()].filter(x=>x.width>0 && x.height>0);
         const textRects=fragmentRects.length;
         const lrect=label.getBoundingClientRect();
         if(textRects!==1)problems.push('atomic label wrapped: '+index+' ('+label.textContent.trim()+'), rects '+textRects);
         if(rect.left < -1 || rect.right > vw+1)problems.push('button outside viewport: '+index);
         if(lrect.right > rect.right+0.5 || lrect.left < rect.left-0.5)problems.push('label clipped/exceeds button: '+index);
         if(rect.height<28)problems.push('button too small: '+index);
       });
       if(document.documentElement.scrollWidth > vw+1)problems.push('unexpected horizontal overflow');
       const rows=[...document.querySelectorAll('.entry')];
       for (const row of rows){
         const r=row.getBoundingClientRect();
         if (r.left < -1 || r.right > vw+1)problems.push('record row outside viewport');
         const group=row.querySelector('[data-mf-action-group]');
         const gr=group.getBoundingClientRect();
         if(gr.left < r.left-1 || gr.right > r.right+1)problems.push('action group overflows row');
       }
       return {problems,checked:atomic.length};
     });
     assert.equal(result.problems.length,0,'Geometry issues '+width+'/'+zoom+'/'+mode+': '+result.problems.join('; '));
     assert.ok(result.checked>=5);
     if(zoom===100 || width===320) await page.screenshot({path:path.join(out,width+'-'+zoom+'-'+mode+'.png'),fullPage:true});
    }
    await page.close();
   }
  }
  console.log('Surface/control chromium geometry: PASS (3 widths x 2 font scales x 3 surface modes)');
 } finally {await browser.close();}
}
test().catch(e=>{console.error(e);process.exit(1)});
