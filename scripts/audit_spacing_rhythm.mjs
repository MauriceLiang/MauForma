#!/usr/bin/env node
/**
 * Measure explicit semantic spacing relationships in a rendered Chromium page.
 * Requires Playwright in the invoking project. This tool never asserts universal px.
 * Usage: node scripts/audit_spacing_rhythm.mjs --url http://localhost:5173/page --contract ./spacing.json
 */
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

export async function auditSpacing(page, contract) {
 if(!contract || contract.schema_version!=='1.0' || !Array.isArray(contract.pairs))
   throw new Error('Expected spacing geometry contract version 1.0 with pairs[]');
 return page.evaluate((plan)=>{
  const problems=[];
  const measurements=[];
  const find=id=>[...document.querySelectorAll('[data-mf-space-id]')].find(el=>el.dataset.mfSpaceId===id);
  const rect=element=>element.getBoundingClientRect();
  for(const pair of plan.pairs){
   const a=find(pair.from),b=find(pair.to);
   if(!a || !b){
    problems.push({id:pair.id,code:'NOT_AUDITED',message:'Missing annotated source/target; cannot assert spacing'});
    continue;
   }
   const ra=rect(a),rb=rect(b);
   const xOverlap=Math.min(ra.right,rb.right)-Math.max(ra.left,rb.left);
   const yOverlap=Math.min(ra.bottom,rb.bottom)-Math.max(ra.top,rb.top);
   let axis=pair.axis||'auto';
   if(axis==='auto'){
    if(yOverlap>Math.min(ra.height,rb.height)*.3) axis='inline';
    else if(xOverlap>Math.min(ra.width,rb.width)*.3)axis='block';
    else {problems.push({id:pair.id,code:'AMBIGUOUS_AXIS',message:'Pairs do not share a clear row/column axis'});continue}
   }
   if(!['inline','block'].includes(axis)){
    problems.push({id:pair.id,code:'INVALID_AXIS',message:'Unsupported axis'});continue;
   }
   const gap=axis==='inline'?rb.left-ra.right:rb.top-ra.bottom;
   const actual=Number(gap.toFixed(2));
   let expected=null;
   if(pair.relation==='separated'){
    if(!pair.token || !pair.token.startsWith('--')){
     problems.push({id:pair.id,code:'MISSING_TOKEN',message:'Separated pair needs a project CSS variable'});continue;
    }
    const raw=getComputedStyle(a).getPropertyValue(pair.token).trim();
    if(!raw){
     problems.push({id:pair.id,code:'MISSING_TOKEN',message:'Token not available to annotated element'});continue;
    }
    const probe=document.createElement('div');
    probe.style.cssText='position:absolute;visibility:hidden;pointer-events:none;inline-size:0;block-size:var('+pair.token+');';
    document.body.appendChild(probe);
    expected=rect(probe).height;
    probe.remove();
    if(!Number.isFinite(expected) || expected<=0){
     problems.push({id:pair.id,code:'INVALID_TOKEN',message:'Cannot resolve nonzero CSS spacing token'});continue;
    }
    const min=expected*(pair.min_factor??.8);
    const max=expected*(pair.max_factor??1.5);
    if(actual<0)problems.push({id:pair.id,code:'OVERLAPPING_REGIONS',actualPx:actual,expectedPx:expected,message:'Separated regions overlap'});
    else if(actual+1<min)problems.push({id:pair.id,code:'INSUFFICIENT_SPACING',actualPx:actual,expectedPx:expected,message:'Gap is below the project role token allowance'});
    else if(actual>max+1)problems.push({id:pair.id,code:'EXCESSIVE_SPACING',actualPx:actual,expectedPx:expected,message:'Gap is beyond the project role token allowance'});
   }else if(pair.relation==='connected'){
    const limit=pair.max_abs_gap_px??1.5;
    if(Math.abs(actual)>limit)
     problems.push({id:pair.id,code:'BROKEN_CONNECTION',actualPx:actual,message:'Intentional connected parts should share an edge'});
   }else{
    problems.push({id:pair.id,code:'UNKNOWN_RELATION',message:'Only separated and connected are measurable; anchored pairs are excluded'});
   }
   measurements.push({id:pair.id,axis,relation:pair.relation,gapPx:actual,expectedPx:expected,group:pair.group||null});
  }
  for(const c of plan.coherence||[]){
   const related=measurements.filter(x=>x.group===c.group && x.relation==='separated');
   if(related.length<2)continue;
   const values=related.map(x=>x.gapPx);
   const high=Math.max(...values),low=Math.min(...values);
   const ratio=high>0?(high-low)/high:0;
   if(ratio>(c.max_difference_ratio??.25))
     problems.push({id:c.group,code:'INCOHERENT_RHYTHM',message:'Equivalent semantic gaps vary beyond contract tolerance',ratio:+ratio.toFixed(3)});
  }
  const overflow=document.documentElement.scrollWidth-window.innerWidth;
  if(overflow>1)problems.push({id:'viewport',code:'HORIZONTAL_OVERFLOW',actualPx:overflow,message:'Unexpected document-wide horizontal overflow'});
  return {passed:problems.length===0,issues:problems,measurements,viewport:{width:innerWidth,height:innerHeight},scope:'annotated DOM regions only; no automatic aesthetic judgment'};
 },contract);
}
async function cli(){
 const args=process.argv.slice(2),opt={};
 for(let i=0;i<args.length;i++){
  if(args[i].startsWith('--'))opt[args[i].slice(2)]=args[i+1],i++;
 }
 if(!opt.url||!opt.contract)throw new Error('Usage: --url URL --contract path/to/contract.json [--out result.json] [--screenshot image.png]');
 const {chromium}=await import('playwright');
 const browser=await chromium.launch({headless:true});
 try{
  const page=await browser.newPage({viewport:{width:1280,height:820}});
  await page.goto(opt.url);
  const plan=JSON.parse(fs.readFileSync(path.resolve(opt.contract),'utf8'));
  const result=await auditSpacing(page,plan);
  if(opt.screenshot)await page.screenshot({path:path.resolve(opt.screenshot),fullPage:true});
  const text=JSON.stringify(result,null,2);
  if(opt.out)fs.writeFileSync(path.resolve(opt.out),text+'\n');
  console.log(text);
  process.exitCode=result.passed?0:1;
 }finally{await browser.close()}
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url)){
 cli().catch(error=>{console.error(error);process.exitCode=2});
}
