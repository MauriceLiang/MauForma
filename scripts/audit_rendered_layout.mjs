#!/usr/bin/env node
/**
 * MauForma v6.9 — optional real-browser geometry audit.
 *
 * Usage:
 *   node scripts/audit_rendered_layout.mjs --url http://127.0.0.1:5173/releases --out ./layout-audit
 * Requires Playwright installed in the TARGET project/environment. No install by this script.
 * Instrument optional elements: data-mf-grid-row / data-mf-grid-panel, or
 * data-mf-align-group="row-name", data-mf-bottom-content, data-mf-fixed-bar,
 * data-mf-scroll-region.
 *
 * PASS means no measured clipping/overflow in examined states, NOT aesthetics or WCAG.
 */
import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";
import process from "node:process";

const args=process.argv.slice(2);
const take=(flag,fallback)=>{const i=args.indexOf(flag);return i>=0?args[i+1]:fallback;};
const url=take("--url",null);
const output=take("--out","layout-audit");
const mainSelector=take("--main","main, [role='main']");
const lastSelector=take("--last","[data-mf-bottom-content]");
const widths=take("--viewports","1440x900,1280x720,390x844").split(",").map(x=>x.trim());
if(!url || !/^https?:\/\//.test(url)) {
 console.error("Usage: node scripts/audit_rendered_layout.mjs --url http://127.0.0.1:5173 [--out dir] [--main selector] [--last selector] [--viewports 1440x900,1280x720,390x844]");
 process.exit(2);
}
let chromium;
try { ({ chromium }=await import("playwright")); }
catch(e) { console.error("NOT RUN: Playwright is not installed. Use the existing target project browser QA tooling, or install Playwright only with project authorization."); process.exit(2); }
await mkdir(output,{recursive:true});
const browser=await chromium.launch({headless:true});
const audit={url,generated_at:new Date().toISOString(),scope:"real browser geometry only; NOT visual aesthetics, WCAG or data quality",viewports:[]};
try{
 for(const value of widths){
  const match=/^(\d+)x(\d+)$/.exec(value);
  if(!match){throw new Error("Bad viewport: "+value);}
  const viewport={width:Number(match[1]),height:Number(match[2])};
  const context=await browser.newContext({viewport,deviceScaleFactor:1});
  const page=await context.newPage();
  const run={viewport:value,status:"PASS",issues:[],warnings:[],screenshots:[]};
  try{
   await page.goto(url,{waitUntil:"domcontentloaded",timeout:30000});
   await page.locator("body").waitFor({state:"visible",timeout:10000});
   // Projects with async data should wait explicitly in their own E2E suite.
   await page.screenshot({path:path.join(output,value+"-initial.png")});
   run.screenshots.push(value+"-initial.png");
   const measurement=await page.evaluate(({mainSelector,lastSelector})=>{
     const errors=[],warnings=[];
     const main=document.querySelector(mainSelector);
     if(!main)errors.push("No main landmark matched "+mainSelector);
     const last=document.querySelector(lastSelector) || [...(main?.children||[])].at(-1) || document.body.lastElementChild;
     const viewportWidth=document.documentElement.clientWidth;
     const viewportHeight=window.innerHeight;
     if(document.documentElement.scrollWidth>viewportWidth+3)
       errors.push("Root horizontal overflow: "+(document.documentElement.scrollWidth-viewportWidth).toFixed(1)+"px");
     const isScrollable=(el)=>{
       if(el===document.scrollingElement)return el.scrollHeight>el.clientHeight+2;
       const s=getComputedStyle(el);
       return /(auto|scroll)/.test(s.overflowY)&&el.scrollHeight>el.clientHeight+2;
     };
     let scroller=document.scrollingElement;
     if(main){
       for(let n=last;n&&n!==document.body&&n!==document.documentElement;n=n.parentElement){
         if(isScrollable(n)){scroller=n;break;}
       }
     }
     // Scroll *the container that actually owns the final content*, not only window.
     if(scroller===document.scrollingElement)window.scrollTo(0,document.scrollingElement.scrollHeight);
     else scroller.scrollTop=scroller.scrollHeight;
     const scrollOwner=scroller===document.scrollingElement?"document":(scroller?.getAttribute("data-mf-scroll-region")||scroller?.id||scroller?.tagName||"unknown");
     const rect=last?.getBoundingClientRect();
     const limit=scroller===document.scrollingElement?viewportHeight:scroller.getBoundingClientRect().bottom;
     const bottomGap=rect ? Math.round((limit-rect.bottom)*10)/10 : null;
     if(rect && bottomGap < -3)errors.push("Final content extends below reachable scroll boundary by "+(-bottomGap).toFixed(1)+"px");
     else if(rect && bottomGap<12)warnings.push("Small visible ending gap ("+bottomGap+"px): inspect page-end padding and safe area");
     // Check actual clipped descendants only; a normal scrollable ancestor is allowed.
     if(last){
       for(let p=last.parentElement;p&&p!==document.body;p=p.parentElement){
         const s=getComputedStyle(p),r=p.getBoundingClientRect();
         if((/(hidden|clip)/.test(s.overflowY)||s.clipPath!=="none")&&!isScrollable(p)&&rect&&rect.bottom>r.bottom+3){
           errors.push("Final content clipped by ancestor "+(p.id?"#"+p.id:p.tagName));break;
         }
       }
     }
     const fixed=[...document.querySelectorAll("[data-mf-fixed-bar]")];
     if(!fixed.length) {
      // Heuristic: only fixed elements along the viewport bottom; do not mistake a sticky heading for footer.
      for(const el of document.querySelectorAll("body *")){
       const s=getComputedStyle(el),r=el.getBoundingClientRect();
       if(s.position==="fixed"&&r.width>viewportWidth*.25&&r.height>15&&r.height<viewportHeight*.45&&r.bottom>=viewportHeight-8&&r.top<viewportHeight-12)fixed.push(el);
      }
     }
     for(const bar of fixed){
       const b=bar.getBoundingClientRect();
       if(rect && rect.bottom>b.top+2 && rect.top < b.bottom-2 && rect.right>b.left && rect.left<b.right)
         errors.push("Final content intersects bottom fixed bar "+(bar.id?"#"+bar.id:bar.tagName));
     }
     const near=(a,b)=>Math.abs(a-b)<=3;
     // Each optional annotated group should have same top if at one horizontal row.
     const groups=new Map();
     for(const el of document.querySelectorAll("[data-mf-align-group]")){
       const id=el.getAttribute("data-mf-align-group");
       if(!groups.has(id))groups.set(id,[]);
       groups.get(id).push(el);
     }
     for(const row of document.querySelectorAll("[data-mf-grid-row]")){
       const id=row.getAttribute("data-mf-grid-row")||"unnamed";
       if(!groups.has(id))groups.set(id,[]);
       groups.get(id).push(...row.querySelectorAll("[data-mf-grid-panel]"));
     }
     for(const [name,els] of groups){
       const boxes=els.map(el=>el.getBoundingClientRect()).filter(r=>r.width>0&&r.height>0);
       if(boxes.length<2)continue;
       const cols=[...new Set(boxes.map(b=>Math.round(b.left/4)*4))];
       // On mobile, panels naturally stack in one column: that is not a top misalignment.
       if(cols.length>=2&&Math.max(...boxes.map(b=>b.top))-Math.min(...boxes.map(b=>b.top))>3)
         warnings.push("Grid alignment group '"+name+"' has different row starts; check intentional layout vs unintended masonry");
     }
     return {errors,warnings,scrollOwner,viewportHeight,viewportWidth,endingGap:bottomGap,finalContentTag:last?.tagName||null,finalContentText:last?.textContent?.trim().slice(0,80)||null,annotatedGroups:groups.size};
   },{mainSelector,lastSelector});
   // Browser repaint after scroll before capturing the end.
   await page.waitForTimeout(120);
   await page.screenshot({path:path.join(output,value+"-end.png")});
   run.screenshots.push(value+"-end.png");
   Object.assign(run,measurement);
   run.issues.push(...measurement.errors);
   run.warnings.push(...measurement.warnings);
   run.status=run.issues.length?"FAIL":"PASS";
  }catch(e){run.status="NOT RUN";run.issues.push(e.message);}
  finally{await context.close();}
  audit.viewports.push(run);
 }
}finally{await browser.close();}
const result=path.join(output,"report.json");await writeFile(result,JSON.stringify(audit,null,2));
for(const v of audit.viewports)console.log(v.viewport+": "+v.status+"; issues="+v.issues.length+"; warnings="+v.warnings.length);
console.log("Audit and initial/end screenshots: "+result);
if(audit.viewports.some(x=>x.status!=="PASS"))process.exitCode=1;
