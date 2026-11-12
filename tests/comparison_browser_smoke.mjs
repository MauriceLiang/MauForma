#!/usr/bin/env node
/**
 * Real Chromium smoke test for the *MauForma example only*, NOT Synthetic Demo.
 * Renders local HTML, selects/deselects entities, checks legends/series/table,
 * scroll-end reachability and narrow-screen root overflow, saves screenshots.
 */
import assert from "node:assert/strict";
import path from "node:path";
import { mkdir } from "node:fs/promises";
import { fileURLToPath, pathToFileURL } from "node:url";
import { chromium } from "playwright";

const root=path.resolve(path.dirname(fileURLToPath(import.meta.url)),"..");
const url=pathToFileURL(path.join(root,"assets/comparison-layout-lab.html")).href;
const output=path.resolve(process.env.CI_SCREENSHOT_DIR||"comparison-browser-artifacts");
await mkdir(output,{recursive:true});
const browser=await chromium.launch({headless:true});
let checks=0;
try{
 for(const viewport of [{width:1440,height:900},{width:390,height:844}]){
  const tag=viewport.width+"x"+viewport.height;
  const context=await browser.newContext({viewport,deviceScaleFactor:1});
  const page=await context.newPage();
  const errors=[];
  page.on("pageerror",x=>errors.push(x.message));
  await page.goto(url,{waitUntil:"load"});
  const ids=async(selector,attr)=>page.locator(selector).evaluateAll((els,name)=>els.map(el=>el.getAttribute(name)).filter(Boolean),attr);
  const allEqual=(a,b)=>a.length===b.length&&a.every(x=>b.includes(x));
  const check=async(expected)=>{
   const selected=await ids("[data-mf-selected-id]","data-mf-selected-id");
   const legends=await ids("[data-mf-legend-id]","data-mf-legend-id");
   const series=await ids("[data-mf-series-id]","data-mf-series-id");
   assert.equal(selected.length,expected,"selected inputs");
   assert.ok(allEqual(selected,legends),"selection matches legend");
   assert.ok(allEqual(selected,series),"selection matches chart series");
   assert.equal(await page.locator("#table-head th").count(),expected+1,"matrix columns");
   checks+=4;
  };
  await check(3);
  assert.equal(await page.locator("data-mf-chart-plot").count(),0,"use explicit attribute selector instead");
  assert.equal(await page.locator("[data-mf-chart-plot]").count(),1);
  const labels=await page.locator("[data-mf-chart-label]").evaluateAll(els=>els.map(e=>{
   const r=e.getBoundingClientRect();return {left:r.left,right:r.right,top:r.top,bottom:r.bottom};
  }));
  for(let i=0;i<labels.length;i++)for(let j=i+1;j<labels.length;j++){
   const a=labels[i],b=labels[j];
   assert.ok(Math.min(a.right,b.right)-Math.max(a.left,b.left)<=3||
             Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top)<=3,"SVG axis labels should not overlap");
  }
  checks+=2;
  await page.screenshot({path:path.join(output,tag+"-initial.png"),fullPage:true});
  await page.locator(".repo input").nth(2).uncheck();
  await check(2);
  await page.locator(".repo input").nth(2).check();
  await check(3);
  await page.locator("#differences").check();
  assert.equal(await page.locator("#table-body tr").count(),2,"difference-only filter works");
  await page.locator("#differences").uncheck();
  assert.equal(await page.locator("#table-body tr").count(),3,"full table restores");
  checks+=2;
  // Extra-wide SVG canvas is deliberately horizontally scrollable *inside* plot
  // on mobile; the document itself must not develop horizontal overflow.
  const end=await page.evaluate(()=>{
   const root=document.documentElement;
   const widthOverflow=root.scrollWidth-root.clientWidth;
   window.scrollTo(0,document.scrollingElement.scrollHeight);
   const last=document.querySelector("[data-mf-bottom-content]").getBoundingClientRect();
   return {widthOverflow,lastBottom:last.bottom,viewportHeight:innerHeight};
  });
  assert.ok(end.widthOverflow<=3,"no root horizontal overflow at "+tag);
  assert.ok(end.lastBottom<=viewport.height+3,"last comparison content reachable at "+tag);
  checks+=2;
  await page.screenshot({path:path.join(output,tag+"-scrolled-end.png"),fullPage:false});
  assert.deepEqual(errors,[],"no browser JS page errors");
  checks+=1;
  console.log("PASS "+tag+" selection/series/matrix, chart labels, viewport, scroll end");
  await context.close();
 }
}finally{await browser.close();}
console.log("MauForma comparison concept browser smoke PASS ("+checks+" assertions), screenshots "+output);
