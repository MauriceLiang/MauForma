#!/usr/bin/env node
/**
 * MauForma v6.10 — visual and data-identity QA for comparison pages.
 *
 * Requires Playwright in the TARGET project. No automatic installs.
 *
 * Required annotations for FULL geometry pass:
 *   [data-mf-selected-id], [data-mf-legend-id], [data-mf-series-id]
 *   [data-mf-chart-group] containing >=2 [data-mf-chart-plot]
 *   [data-mf-chart-label] on HTML/SVG text labels that should not collide
 *
 * Canvas/ECharts internal rendered labels cannot be inferred from DOM bounds:
 * those charts are reported NOT AUDITED and require screenshot/engine review.
 *
 * node scripts/audit_comparison_ui.mjs --url http://localhost:5173/compare --out compare-audit
 */
import { mkdir, writeFile } from "node:fs/promises";
import path from "node:path";
import process from "node:process";

const args=process.argv.slice(2),flag=(s,def)=>{const i=args.indexOf(s);return i<0?def:args[i+1];};
const url=flag("--url",null),out=flag("--out","compare-audit");
const sizes=flag("--viewports","1440x900,1280x720,390x844").split(",");
if(!url||!/^https?:\/\/[^/]+/.test(url)){console.error("Usage: node scripts/audit_comparison_ui.mjs --url http://localhost:5173/compare [--out compare-audit]");process.exit(2);}
let chromium;try{({chromium}=await import("playwright"));}catch(e){console.error("NOT RUN: Playwright unavailable in target project; no dependencies installed.");process.exit(2);}
await mkdir(out,{recursive:true});
const browser=await chromium.launch({headless:true});
const report={url,scope:"browser DOM geometry, selection identities, HTML/SVG labels only (Canvas label collision NOT AUDITED)",viewport_reports:[]};
try{
 for(const entry of sizes){
  const m=/^(\d+)x(\d+)$/.exec(entry.trim());
  if(!m)throw new Error("Bad viewport "+entry);
  const ctx=await browser.newContext({viewport:{width:Number(m[1]),height:Number(m[2])}});
  const page=await ctx.newPage();const outRow={viewport:entry,failures:[],warnings:[],not_audited:[],screenshots:[]};
  try{
   await page.goto(url,{waitUntil:"domcontentloaded",timeout:30000});
   await page.locator("body").waitFor({state:"visible",timeout:10000});
   await page.screenshot({path:path.join(out,entry+"-top.png")});
   outRow.screenshots.push(entry+"-top.png");
   const measurement=await page.evaluate(()=>{
    const failure=[],warnings=[],notAudited=[];
    const inView=(el)=>{const r=el.getBoundingClientRect(),s=getComputedStyle(el);return r.width>0&&r.height>0&&s.visibility!=="hidden"&&s.display!=="none";};
    const vals=(attribute)=>[...document.querySelectorAll("["+attribute+"]")].filter(inView).map(el=>el.getAttribute(attribute)).filter(Boolean);
    const selected=vals("data-mf-selected-id");
    const legends=vals("data-mf-legend-id");
    const series=vals("data-mf-series-id");
    const uniq=x=>[...new Set(x)];
    const setsSame=(a,b)=>a.length===b.length&&a.every(x=>b.includes(x));
    if(!selected.length||!legends.length||!series.length)notAudited.push("Selection/legend/series DOM annotations missing; app data contract test still required");
    else{
      if(uniq(selected).length!==selected.length)failure.push("Duplicate selected entity markers");
      if(!setsSame(uniq(selected),uniq(legends)))failure.push("Selected entities and visible legend IDs differ");
      if(!setsSame(uniq(selected),uniq(series)))failure.push("Selected entities and chart series IDs differ; explain partial/no-data");
    }
    const groups=[...document.querySelectorAll("[data-mf-chart-group]")].filter(inView);
    let labeled=0,checkedPlots=0,collisionCount=0;
    if(!groups.length)notAudited.push("No data-mf-chart-group annotations: interior plot alignment NOT AUDITED");
    for(const group of groups){
      const plots=[...group.querySelectorAll("[data-mf-chart-plot]")].filter(inView);
      if(plots.length>1){
       checkedPlots+=1;
       const boxes=plots.map(el=>el.getBoundingClientRect());
       const leftDiff=Math.max(...boxes.map(x=>x.left))-Math.min(...boxes.map(x=>x.left));
       const topDiff=Math.max(...boxes.map(x=>x.top))-Math.min(...boxes.map(x=>x.top));
       const bottomDiff=Math.max(...boxes.map(x=>x.bottom))-Math.min(...boxes.map(x=>x.bottom));
       const sharedAxis=group.dataset.mfSharedAxis==="true";
       if(sharedAxis && (topDiff>6||bottomDiff>6))warnings.push("Shared-axis plot tops/bottoms differ by "+Math.max(topDiff,bottomDiff).toFixed(1)+"px");
       if(sharedAxis && leftDiff>14)warnings.push("Shared-axis plot left edges differ; review margins and labels");
      } else if(!plots.length)notAudited.push("Chart group without accessible data-mf-chart-plot; canvas/SVG internal plot NOT AUDITED");
      const labels=[...group.querySelectorAll("[data-mf-chart-label]")].filter(inView);
      labeled+=labels.length;
      if(labels.length===0)notAudited.push("Chart label collision not measured: no DOM label annotations in "+(group.id||group.dataset.mfChartGroup||"group"));
      for(let i=0;i<labels.length;i++)for(let j=i+1;j<labels.length;j++){
       const a=labels[i].getBoundingClientRect(),b=labels[j].getBoundingClientRect();
       const overlapX=Math.min(a.right,b.right)-Math.max(a.left,b.left);
       const overlapY=Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top);
       if(overlapX>3&&overlapY>3){
        collisionCount++;
        if(collisionCount<8)failure.push("Chart label overlap: "+labels[i].textContent.trim().slice(0,15)+" / "+labels[j].textContent.trim().slice(0,15));
       }
      }
      const boundary=group.getBoundingClientRect();
      for(const el of labels){
        const r=el.getBoundingClientRect();
        if(r.left<boundary.left-2||r.right>boundary.right+2||r.top<boundary.top-2||r.bottom>boundary.bottom+2)
          warnings.push("Chart label exceeds chart group visible bounds");
      }
    }
    if(!labeled)notAudited.push("Canvas/painted text remains NOT AUDITED; human inspection of screenshots required");
    const root=document.documentElement;
    if(root.scrollWidth>root.clientWidth+3)failure.push("Document horizontal overflow "+(root.scrollWidth-root.clientWidth)+"px");
    // Scroll actual main content if marked, otherwise scroll document.
    const scroller=document.querySelector("[data-mf-scroll-region]")||document.scrollingElement;
    if(scroller===document.scrollingElement)window.scrollTo(0,root.scrollHeight);
    else scroller.scrollTop=scroller.scrollHeight;
    const end=document.querySelector("[data-mf-bottom-content]");
    if(end&&inView(end)){
      const r=end.getBoundingClientRect();
      const bottom=scroller===document.scrollingElement?innerHeight:scroller.getBoundingClientRect().bottom;
      if(r.bottom>bottom+3)failure.push("Last comparison content is not reachable after scroll-to-end");
      const bars=[...document.querySelectorAll("[data-mf-fixed-bar]")].filter(inView);
      for(const bar of bars){const b=bar.getBoundingClientRect();if(r.bottom>b.top&&r.top<b.bottom&&r.left<b.right&&r.right>b.left)failure.push("Bottom fixed bar overlaps last comparison content");}
    }else notAudited.push("End-of-content selector missing, full scroll-end audit needs data-mf-bottom-content");
    return {failure,warnings,notAudited,selected,legends,series,groups:groups.length,checkedPlots,labeled,collisionCount};
   });
   Object.assign(outRow,measurement);
   outRow.failures.push(...measurement.failure);outRow.warnings.push(...measurement.warnings);outRow.not_audited.push(...measurement.notAudited);
   await page.waitForTimeout(90);
   await page.screenshot({path:path.join(out,entry+"-end.png")});
   outRow.screenshots.push(entry+"-end.png");
   outRow.status=outRow.failures.length?"FAIL":outRow.not_audited.length?"PARTIAL":"PASS";
  }catch(e){outRow.status="NOT RUN";outRow.failures.push(e.message);}
  finally{await ctx.close();}
  report.viewport_reports.push(outRow);
 }
}finally{await browser.close();}
await writeFile(path.join(out,"comparison-report.json"),JSON.stringify(report,null,2));
for(const r of report.viewport_reports)console.log(r.viewport+" "+r.status+" failures="+r.failures.length+" not-audited="+r.not_audited.length);
console.log("Result: "+path.join(out,"comparison-report.json"));
if(report.viewport_reports.some(r=>r.status==="FAIL"||r.status==="NOT RUN"))process.exitCode=1;
