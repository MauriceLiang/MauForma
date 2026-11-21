/** Synthetic DOM candidates across unrelated styles; never tests actual vendor or OS popup. */
import assert from 'node:assert/strict';
import {chromium} from 'playwright';
import {auditControlConsistency} from '../scripts/audit_control_consistency.mjs';

const browser=await chromium.launch({headless:true});
try {
  for (const color of ['#25345d','#b28823','#121212']) {
    for (const width of [390,1280]) {
      const page=await browser.newPage({viewport:{width,height:760}});
      await page.setContent('<!doctype html><html><head><style>'+
        'body{font:16px system-ui;background:'+color+';padding:20px}'+
        'select,[role=combobox]{padding:8px 12px;font-size:18px;border:1px solid white;background:white}'+
        '</style></head><body><main>'+
        '<form id="filters"><select id="category" aria-label="Category"><option>A</option></select>'+
        '<button id="custom" type="button" role="combobox" aria-expanded="false" aria-controls="choices">Choose</button>'+
        '<button id="action" type="button" aria-haspopup="menu">Actions</button></form>'+
        '</main></body></html>');
      const mixed=await auditControlConsistency(page);
      assert.deepEqual(mixed.counts,{nativeSelect:1,customOrLibrarySelection:1});
      assert.ok(mixed.candidates.some(c=>c.code==='MIXED_SELECTION_SOURCES'));
      assert.ok(mixed.candidates.some(c=>c.code==='NATIVE_SELECT_POPUP_REVIEW'));
      assert.equal(mixed.verified,false);
      assert.equal(mixed.controls.length,2,'Action menu must not count as value Select');
      await page.locator('#custom').evaluate(el=>el.remove());
      const nativeOnly=await auditControlConsistency(page);
      assert.equal(nativeOnly.counts.customOrLibrarySelection,0);
      assert.ok(!nativeOnly.candidates.some(c=>c.code==='MIXED_SELECTION_SOURCES'));
      await page.locator('#category').evaluate(el=>el.remove());
      const actionOnly=await auditControlConsistency(page);
      assert.equal(actionOnly.controls.length,0);
      assert.equal(actionOnly.status,'NO_MIXED_SELECTION_SOURCES_OBSERVED');
      await page.close();
    }
  }
  console.log('Control consistency candidate QA PASS: mixed/native/action separation across 3 visual styles and 2 viewport widths');
} finally { await browser.close(); }

