#!/usr/bin/env node
/**
 * Framework-agnostic, read-only motion evidence collector.
 * rAF sampling starts BEFORE a Playwright action; screenshots and optional video
 * provide review evidence. Heuristic flags are candidates, not aesthetic verdicts.
 */
import fs from "node:fs/promises";
import path from "node:path";
import process from "node:process";

const args=process.argv.slice(2);
const flag=(name,fallback="")=>{
  const i=args.indexOf("--"+name);
  return i===-1?fallback:args[i+1]??"";
};
if(args.includes("--help")){
  console.log("Usage: node scripts/motion_rehearsal.mjs --url http://localhost:3000 --scenario ./scenario.json [--out ./artifacts/motion] [--width 1280 --height 800] [--reduced no-preference|reduce] [--video]");
  process.exit(0);
}
const target=flag("url"),scenarioPath=flag("scenario");
const out=path.resolve(flag("out","./artifacts/motion-rehearsal"));
if(!/^https?:\/\/.+/i.test(target)||!scenarioPath){console.error("Requires --url and --scenario. Run --help.");process.exit(2);}
let playwright;
try{playwright=await import("playwright");}catch{console.error("NOT RUN: Playwright is unavailable; no packages installed.");process.exit(3);}
let scenario;
try{
  scenario=JSON.parse(await fs.readFile(path.resolve(scenarioPath),"utf8"));
  if(!Array.isArray(scenario.steps)||!scenario.steps.length||scenario.steps.length>50)throw Error("scenario.steps requires 1–50 items");
}catch(error){console.error("Invalid scenario:",String(error));process.exit(2);}
const viewport={width:Number(flag("width",scenario.viewport?.width??1280)),height:Number(flag("height",scenario.viewport?.height??800))};
const reducedMotion=flag("reduced",scenario.reducedMotion??"no-preference");
if(!Number.isInteger(viewport.width)||!Number.isInteger(viewport.height)||viewport.width<240||viewport.height<240||!["reduce","no-preference"].includes(reducedMotion)){
  console.error("Invalid viewport or reduced-motion option");process.exit(2);
}
const report={source:"MauForma motion rehearsal 2.0",target,viewport,reducedMotion,scenario:scenarioPath,
  generatedAt:new Date().toISOString(),evidenceOnly:true,manualReviewRequired:true,
  limitations:["rAF and screenshots measure different sampling clocks","Candidates are heuristics, not proven bugs",
    "No verification of backend correctness, WCAG compliance or 60fps","Review the 1x recording and relevant frames; a static checker cannot rate taste"],
  pageErrors:[],steps:[],status:"NOT_RUN"};
const safe=(value,i)=>String(value||"step-"+(i+1)).replace(/[^a-zA-Z0-9_-]/g,"-").slice(0,64);
const sleep=ms=>new Promise(resolve=>setTimeout(resolve,ms));
const clamp=(x,min,max)=>Math.min(max,Math.max(min,Number(x)));
let browser;
try{
  await fs.mkdir(out,{recursive:true});
  browser=await playwright.chromium.launch({headless:true});
  const context=await browser.newContext({viewport,reducedMotion,
    ...(args.includes("--video")?{recordVideo:{dir:path.join(out,"video"),size:viewport}}:{})});
  const page=await context.newPage();
  page.on("pageerror",e=>report.pageErrors.push(String(e)));
  const response=await page.goto(target,{waitUntil:"domcontentloaded",timeout:30000});
  report.httpStatus=response?.status()??null;
  await page.evaluate(async()=>{if(document.fonts?.ready)await Promise.race([document.fonts.ready,new Promise(r=>setTimeout(r,1800))]);});
  const observe=selectors=>page.evaluate(list=>{
    const map={};
    for(const selector of list){
      let node;
      try{node=document.querySelector(selector);}catch{map[selector]={error:"invalid selector"};continue;}
      if(!node){map[selector]={missing:true};continue;}
      const rect=node.getBoundingClientRect(),style=getComputedStyle(node);
      map[selector]={x:+rect.x.toFixed(2),y:+rect.y.toFixed(2),
        width:+rect.width.toFixed(2),height:+rect.height.toFixed(2),opacity:style.opacity,
        transform:style.transform,display:style.display,visibility:style.visibility,
        textLength:node.textContent?.length??0};
    }
    return map;
  },selectors);
  for(let index=0;index<scenario.steps.length;index++){
    const step=scenario.steps[index],name=safe(step.id,index);
    const folder=path.join(out,String(index+1).padStart(2,"0")+"-"+name);
    await fs.mkdir(folder,{recursive:true});
    const intervalMs=clamp(step.intervalMs??80,40,500),captureMs=clamp(step.captureMs??600,80,10000);
    const settleMs=clamp(step.settleMs??250,0,10000);
    const selectors=[...new Set([...(Array.isArray(step.track)?step.track:[]),...(step.selector?[step.selector]:[]),...(step.anchor?[step.anchor]:[])])];
    const entry={id:name,action:step.action,selector:step.selector??null,anchor:step.anchor??null,
      intervalMs,captureMs,settleMs,frames:[],candidates:[],status:"NOT_RUN",raf:[]};
    report.steps.push(entry);
    const capture=async label=>{
      const begin=Date.now(),file=label+".png";
      await page.screenshot({path:path.join(folder,file),fullPage:false,animations:"allow"});
      entry.frames.push({file:path.relative(out,path.join(folder,file)),timestamp:Date.now(),durationMs:Date.now()-begin,
        geometry:await observe(selectors)});
    };
    try{
      await capture("before");
      // The recorder is armed before the user action. Pointer events are recorded
      // even if the whole pressed state is shorter than a single screenshot.
      await page.evaluate(list=>{
        if(window.__mfMotionRecorder?.stop)window.__mfMotionRecorder.stop();
        const data=[],events=[];
        let running=true,rafId=0,started=performance.now();
        const snap=(kind,t)=>{
          if(data.length>=2500)return;
          const geometry={};
          for(const selector of list){
            let node;try{node=document.querySelector(selector);}catch{continue;}
            if(!node){geometry[selector]={missing:true};continue;}
            const b=node.getBoundingClientRect(),s=getComputedStyle(node);
            geometry[selector]={x:+b.x.toFixed(2),y:+b.y.toFixed(2),width:+b.width.toFixed(2),
              height:+b.height.toFixed(2),opacity:+s.opacity,transform:s.transform,
              visibility:s.visibility,textLength:node.textContent?.length??0};
          }
          data.push({kind,timeMs:+(t-started).toFixed(2),geometry});
        };
        const tick=t=>{if(!running)return;snap("raf",t);rafId=requestAnimationFrame(tick);};
        const pointer=e=>{events.push({type:e.type,timeMs:+(performance.now()-started).toFixed(2)});
          snap(e.type,performance.now());};
        for(const event of ["pointerdown","pointerup","click","keydown","keyup"])document.addEventListener(event,pointer,true);
        rafId=requestAnimationFrame(tick);
        window.__mfMotionRecorder={data,events,stop:()=>{
          running=false;cancelAnimationFrame(rafId);
          for(const event of ["pointerdown","pointerup","click","keydown","keyup"])document.removeEventListener(event,pointer,true);
          return {frames:data.slice(),events:events.slice(),elapsedMs:+(performance.now()-started).toFixed(2)};
        }};
      },selectors);
      const locator=step.selector?page.locator(step.selector).first():null;
      const trigger=async()=>{
        switch(step.action){
          case "click": if(!locator)throw Error("click requires selector");await locator.click({timeout:5000});break;
          case "hover": if(!locator)throw Error("hover requires selector");await locator.hover({timeout:5000});break;
          case "fill": if(!locator)throw Error("fill requires selector");await locator.fill(String(step.value??""),{timeout:5000});break;
          case "press":
            if(locator)await locator.press(String(step.key??"Enter"),{timeout:5000});
            else await page.keyboard.press(String(step.key??"Escape"));
            break;
          case "wait":await sleep(clamp(step.ms??100,0,10000));break;
          case "reduced-motion":
            if(!["reduce","no-preference"].includes(step.value))throw Error("Invalid reduced-motion value");
            await page.emulateMedia({reducedMotion:step.value});break;
          default:throw Error("Unsupported action: "+step.action);
        }
      };
      // Intentionally run action and screenshots concurrently; await both before
      // declaring settled. A promise rejection is converted into a value to avoid
      // an unhandled rejection during image acquisition.
      const actionResult=trigger().then(()=>null,e=>e);
      const captureStarted=Date.now();
      let n=0;
      while(Date.now()-captureStarted<captureMs&&n<150){
        const expected=captureStarted+n*intervalMs;
        if(Date.now()<expected)await sleep(expected-Date.now());
        await capture("frame-"+String(n).padStart(3,"0"));
        n++;
      }
      const actionError=await actionResult;
      if(actionError)throw actionError;
      if(settleMs)await sleep(settleMs);
      await capture("settled");
      entry.raf=await page.evaluate(()=>window.__mfMotionRecorder?.stop?.()??{frames:[],events:[],elapsedMs:0});
      const raf=entry.raf.frames;
      const rafTicks=raf.filter(f=>f.kind==="raf");
      const deltas=rafTicks.slice(1).map((f,i)=>f.timeMs-rafTicks[i].timeMs);
      const sum=deltas.reduce((a,b)=>a+b,0);
      entry.raf_metrics={frames:rafTicks.length,meanIntervalMs:deltas.length?+(sum/deltas.length).toFixed(2):null,
        largestGapMs:deltas.length?+Math.max(...deltas).toFixed(2):null,
        observedPointerdown:entry.raf.events.some(e=>e.type==="pointerdown"),
        observedPointerup:entry.raf.events.some(e=>e.type==="pointerup")};
      for(let i=1;i<raf.length;i++){
        if(raf[i].timeMs-raf[i-1].timeMs>75)continue;
        for(const selector of selectors){
          const p=raf[i-1].geometry[selector],q=raf[i].geometry[selector];
          if(!p||!q||p.missing||q.missing)continue;
          const distance=Math.hypot(q.x-p.x,q.y-p.y);
          // Explicitly declared snaps are allowed; other large one-frame moves
          // are review candidates, never an automatic failure.
          if(distance>Math.max(24,Number(step.jumpThresholdPx??24))&&!step.allowSnap)
            entry.candidates.push({kind:"possible-position-jump",selector,timeMs:raf[i].timeMs,distancePx:+distance.toFixed(1),
              evidence:"successive rAF geometry",needsVisualReview:true});
        }
      }
      if(step.anchor&&raf.length){
        const positions=raf.map(f=>f.geometry[step.anchor]).filter(x=>x&&!x.missing);
        if(positions.length){
          const b=positions[0],maxDrift=Math.max(...positions.map(x=>Math.hypot(x.x-b.x,x.y-b.y)));
          if(maxDrift>Number(step.anchorTolerancePx??3))
            entry.candidates.push({kind:"possible-anchor-drift",selector:step.anchor,maxDriftPx:+maxDrift.toFixed(1),needsVisualReview:true});
        }
      }
      for(let i=2;i<entry.frames.length-1;i++){
        const delta=entry.frames[i].timestamp-entry.frames[i-1].timestamp;
        if(delta>intervalMs*1.6){
          entry.candidates.push({kind:"screenshot-sampling-gap",actualMs:delta,expectedMs:intervalMs,
            status:"INCONCLUSIVE",needsVisualReview:true});
        }
      }
      if(step.action==="click"&&!entry.raf_metrics.observedPointerdown)
        entry.candidates.push({kind:"missing-pointerdown-evidence",status:"INCONCLUSIVE",needsVisualReview:true});
      // Avoid false PASS: even if no candidate appears, normal-speed visual review is required.
      entry.status=entry.candidates.some(c=>c.status==="INCONCLUSIVE")?"INCONCLUSIVE":"CAPTURED_FOR_REVIEW";
      const shots=entry.frames.map(f=>"<figure><img loading='lazy' src='"+path.basename(f.file)+"' alt='"+path.basename(f.file)+"'><figcaption>"+path.basename(f.file)+"</figcaption></figure>").join("");
      const film="<!doctype html><html lang='en'><meta charset='utf-8'><title>Motion frames</title>"+
        "<style>body{font:14px system-ui;background:#eee;margin:20px}main{display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px}figure{margin:0;background:white;padding:10px}img{max-width:100%}</style>"+
        "<h1>Contact sheet: "+name+"</h1><p>Review at 1x speed separately; stills cannot prove motion quality.</p><main>"+shots+"</main></html>";
      await fs.writeFile(path.join(folder,"contact-sheet.html"),film,"utf8");
    }catch(error){
      entry.status="BLOCKED";entry.candidates.push({kind:"runtime-error",message:String(error)});
      try{entry.raf=await page.evaluate(()=>window.__mfMotionRecorder?.stop?.()??null);}catch{}
    }
  }
  if(args.includes("--video")){report.video_status="RECORDED_REVIEW_REQUIRED";report.video_files_are_local=true;}
  await context.close();
  report.status=report.pageErrors.length||report.httpStatus>=400||report.steps.some(x=>x.status==="BLOCKED")?"BLOCKED":
    report.steps.some(x=>x.status==="INCONCLUSIVE")?"INCONCLUSIVE":"CAPTURED_FOR_REVIEW";
}catch(error){
  report.status="BLOCKED";report.fatalError=String(error);
}finally{
  if(browser)await browser.close();
  await fs.mkdir(out,{recursive:true});
  await fs.writeFile(path.join(out,"report.json"),JSON.stringify(report,null,2)+"\n","utf8");
  console.log(JSON.stringify({report:path.join(out,"report.json"),status:report.status,
    steps:report.steps.length,candidates:report.steps.reduce((n,x)=>n+x.candidates.length,0),pageErrors:report.pageErrors.length},null,2));
}
process.exit(report.status==="BLOCKED"?1:report.status==="INCONCLUSIVE"?2:0);
