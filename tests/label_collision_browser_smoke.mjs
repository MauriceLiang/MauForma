/** Generic rendered collision regression. Synthetic layouts only; no project screenshots. */
import assert from 'node:assert/strict';
import {chromium} from 'playwright';
import {auditLabelCollisions} from '../scripts/audit_label_collisions.mjs';

const browser=await chromium.launch({headless:true});
try {
  for(const width of [1280,390,320]){
    for(const fontScale of [100,200]){
      for(const theme of ['dark','light']){
        const page=await browser.newPage({viewport:{width,height:720}});
        const html='<!doctype html><html><head><meta name="viewport" content="width=device-width, initial-scale=1">'+
          '<style>*{box-sizing:border-box}html{font-size:'+fontScale+'%}body{margin:0;font:1rem/1.35 system-ui;background:#25272d;color:#fafafa}'+
          'body.light{background:#fafafa;color:#222}main{padding:20px;max-width:1100px}'+
          '.labels{display:flex;flex-wrap:nowrap;align-items:center}'+
          '.pill{position:relative;display:inline-flex;align-items:center;flex-shrink:0;padding:.5rem 1rem;border:1px solid #6b768b;border-radius:2rem;white-space:nowrap;background:#293042;color:#fff}'+
          '.pill .dot{display:inline-block;width:.5rem;height:.5rem;border-radius:50%;background:#79f}'+
          '.pill .caption{margin-left:.35rem}'+
          '[data-state=bad] .pill:last-child{margin-left:-4rem}'+
          '[data-state=good]{flex-wrap:wrap;gap:.65rem}'+
          '[data-state=good] .pill:last-child{margin-left:0}'+
          '.paragraph{margin-top:24px}'+
          '</style></head><body class="'+(theme==='light'?'light':'')+'">'+
          '<main><div id="labels" class="labels" data-state="bad">'+
          '<span class="pill"><i class="dot"></i><span class="caption">结构模型展示</span></span>'+
          '<span class="pill">Studio · CC BY 4.0 · 外观定位</span></div>'+
          '<p class="paragraph">Normal content stays readable below the pills.</p>'+
          '</main></body></html>';
        await page.setContent(html);
        const bad=await auditLabelCollisions(page);
        assert.equal(bad.passed,false,'Overlapping pills must be caught '+width+'/'+fontScale+'/'+theme);
        assert.ok(bad.issues.some(x=>x.code==='COMPACT_LABEL_SURFACE_OVERLAP'),
          'Compact surface overlap missing: '+JSON.stringify(bad));
        await page.locator('#labels').evaluate(el=>el.dataset.state='good');
        const good=await auditLabelCollisions(page);
        assert.equal(good.passed,true,'Wrapped pills must pass: '+JSON.stringify(good.issues));
        await page.close();
      }
    }
  }
  const nested=await browser.newPage({viewport:{width:600,height:440}});
  await nested.setContent('<main><button style="padding:10px 20px;background:#ddd;border:1px solid #777"><span>Safe nested</span> <strong>label</strong></button></main>');
  const nestedReport=await auditLabelCollisions(nested);
  assert.equal(nestedReport.passed,true,'Contained text in one control is not independent overlap');
  await nested.close();

  const intersect=await browser.newPage({viewport:{width:650,height:400}});
  await intersect.setContent('<main><div style="position:relative;height:100px"><span id="a" style="position:absolute;left:10px;top:10px">Independent text A</span><span id="b" style="position:absolute;left:45px;top:11px">Independent text B</span></div></main>');
  const collided=await auditLabelCollisions(intersect);
  assert.equal(collided.passed,false);
  assert.ok(collided.issues.some(x=>x.code==='READABLE_TEXT_COLLISION'),'Text must be checked independent of pill styles');
  await intersect.close();

  console.log('Compact label/readability collision QA PASS: dark/light, 3 widths x 2 font scales, repaired wrap, nested control and plain-text collision.');
}finally{await browser.close();}
