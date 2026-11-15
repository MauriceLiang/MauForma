/** Verify the synthetic four-layer liquid-glass lab, not the real-world optical fidelity. */
import { chromium } from 'playwright';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';

const here=path.dirname(fileURLToPath(import.meta.url));
const url=pathToFileURL(path.resolve(here,'../assets/liquid-glass-layer-lab.html')).href;
const output=path.resolve('liquid-glass-browser-artifacts');
async function setRange(page,id,value){
  await page.locator('#'+id).evaluate((el,v)=>{el.value=v;el.dispatchEvent(new Event('input',{bubbles:true}));},value);
}

async function run(){
  const browser=await chromium.launch({headless:true});
  fs.mkdirSync(output,{recursive:true});
  let cases=0;
  try{
    for(const width of [1280,390]){
      for(const reduced of ['reduce','no-preference']){
        const page=await browser.newPage({viewport:{width,height:840},reducedMotion:reduced});
        const errors=[];
        page.on('pageerror',e=>errors.push(e.message));
        await page.goto(url);
        assert.equal(await page.locator('.glass').count(),1);
        assert.equal(await page.locator('.layer.transmission').count(),1);
        assert.equal(await page.locator('.layer.refraction').count(),1);
        assert.equal(await page.locator('.layer.highlight').count(),1);
        assert.equal(await page.locator('#lg-displacement').count(),1);
        assert.ok((await page.locator('#lg-displacement-image').getAttribute('href'))?.startsWith('data:image/png;base64,'),
          'Canvas should generate an independent local displacement map');

        // Transparent, highlight, shadow and optional blur are independently configurable.
        await setRange(page,'opacity','32');
        assert.equal((await page.locator('#glass').evaluate(el=>el.style.getPropertyValue('--lens-tint'))),'0.32');
        await setRange(page,'specular','44');
        assert.equal(await page.locator('#glass').evaluate(el=>el.style.getPropertyValue('--hl')),'0.44');
        await setRange(page,'elevation','12');
        assert.equal(await page.locator('#glass').evaluate(el=>el.style.getPropertyValue('--shadow')),'0.12');
        await setRange(page,'blur','5');
        assert.equal(await page.locator('#blur-label').innerText(),'5px');
        await setRange(page,'strength','26');
        assert.equal(await page.locator('#lg-displacement').getAttribute('scale'),'26');

        // SVG backdrop support is only a candidate; the lab must never claim proven refraction.
        assert.equal(await page.locator('#glass').getAttribute('data-refraction-attempt'),'fallback');
        await page.locator('#refract-toggle').check();
        const attempt=await page.locator('#glass').getAttribute('data-refraction-attempt');
        assert.ok(['attempted','fallback'].includes(attempt));
        const status=await page.locator('#refraction-status').innerText();
        assert.ok(/未自动验证|保持可读的基础材质/.test(status),status);
        await page.locator('#refract-toggle').uncheck();
        assert.equal(await page.locator('#glass').getAttribute('data-refraction-attempt'),'fallback');
        assert.match(await page.locator('#refraction-status').innerText(),/未启用/);

        // The visual effect cannot replace actual readable DOM content.
        assert.equal(await page.locator('.glass-content strong').innerText(),'层次、光与边界');
        assert.equal(await page.locator('.glass-content').evaluate(el=>getComputedStyle(el).pointerEvents),'auto');
        await page.locator('#opacity').focus();
        assert.equal(await page.locator('#opacity').evaluate(el=>document.activeElement===el),true);
        const doc=await page.evaluate(()=>({width:document.documentElement.scrollWidth,viewport:innerWidth}));
        assert.ok(doc.width<=doc.viewport+2,'No unwanted document overflow at '+width);
        assert.deepEqual(errors,[],'No unhandled errors in browser');
        await page.screenshot({
          path:path.join(output,'glass-'+width+'-'+reduced+'.png'),fullPage:true
        });
        cases++;
        await page.close();
      }
    }
    console.log('Liquid glass layer lab PASS: '+cases+' viewport/reduced-motion cases; independent sliders, local displacement map, safe fallback and accessible DOM. Does NOT prove SVG backdrop optical support.');
  } finally {
    await browser.close();
  }
}
run().catch(err=>{console.error(err);process.exitCode=1});
