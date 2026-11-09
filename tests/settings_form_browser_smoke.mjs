// Browser checks for a synthetic settings/form layout only; not real product acceptance.
import assert from 'node:assert/strict';
import { fileURLToPath } from 'node:url';
import { join, dirname } from 'node:path';
import { chromium } from 'playwright';

const file = 'file://' + join(dirname(fileURLToPath(import.meta.url)), '..', 'examples', 'settings-form-layout-demo.html');
const browser = await chromium.launch({ headless: true });
let checks = 0;
try {
  for (const [width, zoom] of [[1440, 1], [768, 1], [360, 1], [360, 2]]) {
    const page = await browser.newPage({ viewport: { width, height: 900 }, deviceScaleFactor: 1 });
    await page.goto(file);
    if (zoom === 2) await page.evaluate(() => document.documentElement.style.fontSize = '32px');
    const data = await page.evaluate(() => {
      const rect = el => {const r=el.getBoundingClientRect();return { x:r.x,y:r.y,w:r.width,h:r.height,right:r.right,bottom:r.bottom };};
      const rows=[...document.querySelectorAll('[data-mf-settings-row]')];
      const fields=[...document.querySelectorAll('[data-mf-field]')];
      return {
        docWidth:document.documentElement.scrollWidth,clientWidth:document.documentElement.clientWidth,
        rows:rows.map(e=>({rect:rect(e),title:rect(e.querySelector('.details')),control:rect(e.querySelector('.control'))})),
        fields:fields.map(e=>({label:rect(e.querySelector('label')),input:rect(e.querySelector('input'))})),
        danger:rect(document.querySelector('[data-mf-danger]')),
        groups:[...document.querySelectorAll('.settings-group')].map(rect),
        column:rect(document.querySelector('.form-column'))
      };
    });
    assert.ok(data.docWidth <= data.clientWidth + 1, 'horizontal overflow at ' + width + '/' + zoom);
    assert.equal(data.rows.length, 3);
    assert.equal(data.fields.length, 2);
    for (const row of data.rows) {
      if (width <= 640) assert.ok(row.control.y >= row.title.bottom - 1, 'settings control must wrap below label');
      else assert.ok(row.control.x >= row.title.right - 1, 'desktop settings control must align right');
    }
    for (const field of data.fields) {
      assert.ok(field.input.y >= field.label.bottom, 'form label must be above input');
      assert.ok(field.input.w > 200 || width <= 360, 'input must not be compressed');
    }
    assert.ok(data.danger.y > data.groups.at(-1).y + data.groups.at(-1).h, 'danger zone must be separated');
    assert.ok(data.groups[1].y - (data.groups[0].y + data.groups[0].h) >= 24, 'inter-group gap');
    assert.ok(data.column.w <= 621, 'form uses bounded content column');
    await page.locator('#digest').check();
    assert.match(await page.locator('[data-mf-status]').innerText(), /没有连接服务器/);
    await page.locator('#full-name').fill('示例用户');
    await page.locator('#email').fill('wrong-address');
    await page.getByRole('button',{name:'验证表单'}).click();
    assert.equal(await page.locator('#email').getAttribute('aria-invalid'), 'true');
    assert.ok((await page.locator('#email-error').innerText()).includes('有效的邮箱地址'));
    await page.locator('#email').fill('demo@example.test');
    await page.getByRole('button',{name:'验证表单'}).click();
    assert.match(await page.locator('#form-status').innerText(), /未向服务器发送/);
    page.once('dialog', d => d.dismiss());
    await page.getByRole('button',{name:'演示删除确认'}).click();
    assert.match(await page.locator('[data-mf-status]').innerText(), /取消/);
    checks++;
    await page.close();
  }
  console.log('Settings/form browser smoke PASS (' + checks + ' viewport/scale states)');
} finally { await browser.close(); }
