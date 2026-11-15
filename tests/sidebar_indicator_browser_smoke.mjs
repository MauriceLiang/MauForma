/** Check geometry of optional external active rail against an intentional wrong edge-border. */
import { chromium } from 'playwright';
import assert from 'node:assert/strict';
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath, pathToFileURL } from 'node:url';
import { auditSidebarIndicators } from '../scripts/audit_sidebar_indicator.mjs';

const here = path.dirname(fileURLToPath(import.meta.url));
const url = pathToFileURL(path.resolve(here, '../assets/sidebar-refinement-gallery.html')).href;

async function run() {
  const browser = await chromium.launch({headless:true});
  const output = path.resolve('sidebar-indicator-browser-artifacts');
  fs.mkdirSync(output, { recursive: true });
  let cases = 0;
  try {
    for (const width of [1280, 390, 320]) {
      for (const theme of ['dark', 'light']) {
        for (const scale of [100, 200]) {
          const page = await browser.newPage({viewport:{width,height:860},reducedMotion:'reduce'});
          await page.goto(url);
          await page.evaluate(({theme,scale})=>{
            document.documentElement.dataset.scheme=theme;
            document.documentElement.style.fontSize=scale+'%';
          },{theme,scale});
          const positive = page.locator('[data-mf-indicator-case=external]');
          const negative = page.locator('[data-mf-indicator-case=wrong]');
          const good = await auditSidebarIndicators(page, {
            rootSelector:'[data-mf-indicator-case=external] [data-mf-selection-indicator]'
          });
          assert.equal(good.checkedRoots,1);
          assert.equal(good.passed,true,
            'Separate short rail must pass in '+width+'/'+theme+'/'+scale+': '+JSON.stringify(good.issues));
          const bad = await auditSidebarIndicators(page, {
            rootSelector:'[data-mf-indicator-case=wrong] [data-mf-selection-indicator]'
          });
          assert.equal(bad.passed,false,'Edge-attached stripe must be rejected');
          assert.ok(bad.issues.some(issue=>issue.code==='ITEM_EDGE_BORDER'),
            'Negative case should fail because selected item border itself is colored');

          // On selection change: no stale stripe, new selected rail and stable label x-position.
          const items = positive.locator('[data-mf-nav-item]');
          const beforeX = await items.first().evaluate(el=>el.getBoundingClientRect().x);
          await items.nth(2).click();
          assert.equal(await positive.locator('[data-mf-nav-item][aria-pressed=true]').count(),1);
          assert.equal(await positive.locator('.study-row[data-current=true]').count(),1);
          assert.equal(await positive.locator('.study-row[data-current=false]').count(),2);
          const afterX = await items.first().evaluate(el=>el.getBoundingClientRect().x);
          assert.ok(Math.abs(beforeX-afterX)<1,'Selecting another route must not shift label/item position');
          const moved = await auditSidebarIndicators(page,{
            rootSelector:'[data-mf-indicator-case=external] [data-mf-selection-indicator]'
          });
          assert.equal(moved.passed,true,'External marker must follow selected item: '+JSON.stringify(moved.issues));

          // Genuine keyboard navigation is required to trigger :focus-visible.
          // Programmatic .focus() immediately after a pointer click is not equivalent.
          await page.keyboard.press('Shift+Tab');
          const focused = await items.nth(1).evaluate(el=>({
            active:document.activeElement===el,
            outlineStyle:getComputedStyle(el).outlineStyle,
            outlineWidth:parseFloat(getComputedStyle(el).outlineWidth)
          }));
          assert.equal(focused.active,true,'Tab focus should reach the real control, never decorative rail');
          assert.notEqual(focused.outlineStyle,'none','Focus ring must be independently visible');
          assert.ok(focused.outlineWidth>=2);
          const focusCheck = await auditSidebarIndicators(page,{
            rootSelector:'[data-mf-indicator-case=external] [data-mf-selection-indicator]'
          });
          assert.equal(focusCheck.passed,true,'Focus must not create another selected bar');

          const overflow = await page.evaluate(()=>({
            document:document.documentElement.scrollWidth,viewport:innerWidth
          }));
          assert.ok(overflow.document<=overflow.viewport+2,
            'Sidebar gallery must not cause horizontal root overflow '+width+'/'+scale);
          await page.screenshot({path:path.join(output,`sidebar-indicator-${width}-${theme}-${scale}.png`),fullPage:true});
          await page.close();
          cases++;
        }
      }
    }
    console.log('Sidebar indicator browser QA PASS: '+cases+
      ' cases; external short rail outside item with visible gap, negative item-edge border detected, state/focus verified');
  } finally { await browser.close(); }
}
run().catch(err=>{console.error(err);process.exitCode=1});
