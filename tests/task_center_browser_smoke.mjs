#!/usr/bin/env node
/** MauForma standalone demo browser QA (not Synthetic Demo backend E2E). */
import assert from "node:assert/strict";
import path from "node:path";
import { mkdir } from "node:fs/promises";
import { fileURLToPath, pathToFileURL } from "node:url";
import { chromium } from "playwright";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const url=pathToFileURL(path.join(root,"assets/task-center-layout-lab.html")).href;
const output=path.resolve(process.env.CI_TASK_SCREENSHOTS||"task-center-browser-artifacts");
await mkdir(output,{recursive:true});
const browser=await chromium.launch({headless:true});let checks=0;
try{
 for(const viewport of [{width:1440,height:900},{width:390,height:844}]){
  const tag=viewport.width+"x"+viewport.height;
  const context=await browser.newContext({viewport,deviceScaleFactor:1});
  const page=await context.newPage();const errors=[];
  page.on("pageerror",e=>errors.push(e.message));
  await page.goto(url,{waitUntil:"load"});
  const rowCount=()=>page.locator("[data-mf-task-id]").count();
  const count=async(filter,expected)=>{
    const b=page.locator("#status-filter button[data-filter='"+filter+"']");
    const value=await b.locator(".count").textContent();
    assert.equal(Number(value),expected,filter+" aggregate count");checks++;
  };
  const choose=async(filter,expected)=>{
    await page.locator("#status-filter button[data-filter='"+filter+"']").click();
    assert.equal(await rowCount(),expected,filter+" visible rows");checks++;
  };
  assert.equal(await rowCount(),7,"all task rows");checks++;
  await count("all",7);await count("attention",3);await count("running",2);await count("queued",1);await count("completed",1);
  assert.equal(await page.locator("[data-mf-task-action=retry]").count(),2,"retry only eligible partial/failed");checks++;
  assert.equal(await page.locator("[data-mf-task-action=details]").count(),7,"details are accessible");checks++;
  assert.equal(await page.locator("[data-mf-task-state=queued] .bar").count(),0,"queued no made-up progress");checks++;
  assert.equal(await page.locator("[data-mf-task-id=demo-run-006] .bar").count(),0,"stage-only task has no artificial percentage");checks++;
  await page.screenshot({path:path.join(output,tag+"-all.png"),fullPage:true});
  await choose("attention",3);
  assert.equal(await page.locator("[data-mf-task-action=retry]").count(),2,"blocked does not pretend to be retryable");checks++;
  const part=page.locator("[data-mf-task-id=demo-run-003] [data-mf-task-action=details]");
  await part.click();
  assert.equal(await page.locator("#task-detail").evaluate(el=>el.open),true,"details open");checks++;
  assert.match(await page.locator("#detail-data").innerText(),/88 条/,"error reason revealed");checks++;
  await page.keyboard.press("Escape");
  assert.equal(await page.locator("#task-detail").evaluate(el=>el.open),false,"Escape closes detail");checks++;
  await page.locator("#search-tasks").fill("sparse");
  assert.equal(await rowCount(),1,"search combines with active status filter");checks++;
  await page.locator("#search-tasks").fill("");
  await choose("queued",1);
  await choose("all",7);
  const retry=page.locator("[data-mf-task-id=demo-run-004] [data-mf-task-action=retry]");
  await retry.click();
  assert.equal(await page.locator("#retry-dialog").evaluate(el=>el.open),true,"retry asks for confirmation");checks++;
  assert.match(await page.locator("#retry-content").innerText(),/不会调用任何 GitHub/,"no fake server claims");checks++;
  await page.locator("#cancel-retry").click();
  assert.equal(await page.locator("[data-mf-task-id=demo-run-004]").getAttribute("data-mf-task-state"),"failed","cancel changes nothing");checks++;
  await retry.click();
  await page.locator("#confirm-retry").click();
  await count("attention",2);await count("running",3);
  assert.equal(await page.locator("[data-mf-task-id=demo-run-004]").getAttribute("data-mf-task-state"),"running","local simulation changes state");checks++;
  assert.equal(await page.locator("[data-mf-task-action=retry]").count(),1,"retry disappears after synthetic re-run");checks++;
  const bounds=await page.evaluate(()=>{
    const root=document.documentElement;
    const overflow=root.scrollWidth-root.clientWidth;
    window.scrollTo(0,document.scrollingElement.scrollHeight);
    const end=document.querySelector("[data-mf-bottom-content]").getBoundingClientRect();
    return {overflow,end:end.bottom,viewport:innerHeight};
  });
  assert.ok(bounds.overflow<=3,"no horizontal root overflow at "+tag+" (overflow="+bounds.overflow+")");checks++;
  assert.ok(bounds.end<=bounds.viewport+3,"last row/footer reachable after scrolling at "+tag);checks++;
  await page.screenshot({path:path.join(output,tag+"-end.png"),fullPage:false});
  assert.deepEqual(errors,[],"no JS errors");checks++;
  console.log("PASS "+tag+" — state counts, filters, task details, retry confirmation, responsive scroll");
  await context.close();
 }
}finally{await browser.close();}
console.log("Task Center concept QA PASS ("+checks+" assertions). Screenshots: "+output);
