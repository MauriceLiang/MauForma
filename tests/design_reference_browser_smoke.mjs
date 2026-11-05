/** Synthetic-only browser proof: selection, icon/typography, dense table, filters, details and responsive safety. */
import {chromium} from 'playwright';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath,pathToFileURL} from 'node:url';

const here=path.dirname(fileURLToPath(import.meta.url));
const url=pathToFileURL(path.join(here,'../examples/clean-enterprise-demo/index.html')).href;

async function run(){
 const browser=await chromium.launch({headless:true});
 const out=path.resolve('reference-learning-browser-artifacts');
 fs.mkdirSync(out,{recursive:true});
 try{
  for(const width of [1280,390,320]){
   for(const fontScale of [100,200]){
    const page=await browser.newPage({viewport:{width,height:820},reducedMotion:'reduce'});
    await page.goto(url);
    await page.evaluate(value=>{document.documentElement.style.fontSize=value+'%';},fontScale);
    assert.equal(await page.locator('[data-demo-source=synthetic]').count(),1,'Only synthetic demo may be shown');
    assert.equal(await page.locator('.navbutton').count(),5);
    assert.equal(await page.locator('.navbutton .iconbox svg path').count()>0,true,'Official SVG glyphs should render');
    assert.equal(await page.locator('.navbutton[aria-current=page]').count(),1);
    await page.locator('[data-nav-id=calendar]').click();
    assert.equal(await page.locator('[data-nav-id=calendar]').getAttribute('aria-current'),'page');
    assert.equal(await page.locator('[data-nav-id=plan]').getAttribute('aria-current'),'false');
    assert.equal(await page.locator('[data-nav-id=calendar]').evaluate(el=>document.activeElement===el),true);
    const navGeom=await page.locator('[data-nav-id=calendar]').evaluate(el=>{
     const svg=el.querySelector('svg').getBoundingClientRect(),r=el.getBoundingClientRect();
     return {square:Math.abs(svg.width-svg.height)<1,within:r.width>svg.width+15};
    });
    assert.ok(navGeom.square&&navGeom.within,'Navigation icon may not distort or crowd its label');

    const initial=await page.locator('#records tr:visible').count();
    assert.equal(initial,8);
    await page.locator('#status-filter').selectOption('done');
    assert.equal(await page.locator('#records tr:visible').count(),3);
    await page.locator('#status-filter').selectOption('all');
    await page.locator('#search-input').fill('测试');
    assert.equal(await page.locator('#records tr:visible').count(),1);
    assert.equal(await page.locator('#result-count').innerText(),'显示 1 条虚构记录');
    await page.locator('#search-input').fill('');
    await page.locator('#records tr:visible').first().locator('.row-action').click();
    assert.ok(await page.locator('#detail-dialog').evaluate(el=>el.open),'Details modal should open');
    assert.match(await page.locator('#dialog-copy').innerText(),/虚构学习专题/);
    await page.keyboard.press('Escape');
    assert.equal(await page.locator('#detail-dialog').evaluate(el=>el.open),false);

    const geom=await page.evaluate(()=>{
      const scroller=document.querySelector('.table-scroller');
      const rect=scroller.getBoundingClientRect();
      const nav=document.querySelector('.navbutton');
      const n=nav.getBoundingClientRect();
      return {viewport:innerWidth,doc:document.documentElement.scrollWidth,
       localScroll:scroller.scrollWidth>scroller.clientWidth+2,
       tableVisible:rect.width>140,
       navHeight:n.height,
       rows:[...document.querySelectorAll('#records tr')].map(x=>x.getBoundingClientRect().height)};
    });
    assert.ok(geom.doc<=geom.viewport+1,'Document-level horizontal overflow');
    assert.ok(geom.tableVisible,'Records region must remain accessible');
    assert.ok(geom.navHeight>=36,'Navigation item usable height');
    assert.ok(geom.rows.every(x=>x>=32),'Table records must not be compressed to tiny heights');
    if(width<=390)assert.ok(geom.localScroll,'Narrow table must use local scroll, not crush content');
    await page.screenshot({path:path.join(out,'synthetic-'+width+'-'+fontScale+'.png'),fullPage:true});
    await page.close();
   }
  }
  console.log('Reference learning browser PASS: original fictional demo, selection/focus, Element Plus icons, search/status, details, 3 widths x 2 font scales');
 } finally {await browser.close();}
}
run().catch(e=>{console.error(e);process.exitCode=1});
