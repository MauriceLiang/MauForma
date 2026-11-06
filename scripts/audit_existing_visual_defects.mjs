#!/usr/bin/env node
/**
 * Defect-first QA for an EXISTING page, including flaws that already existed
 * before the edit. No annotations or before/after baseline are required.
 *
 * Usage: node scripts/audit_existing_visual_defects.mjs --url http://localhost:5173/page
 * Optional: --selector main --width 1280 --font 100 --out /tmp/audit.json
 *
 * This is a structural geometry risk scan, NOT semantic/aesthetic proof.
 * Do not commit screenshots, sensitive page data, or raw URLs to a public repo.
 */
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';
import {auditPanelSpacing} from './audit_panel_spacing.mjs';

export async function auditExistingVisualDefects(page,options={}){
 const broad=await page.evaluate((opt)=>{
  const issues=[],measurements=[];
  const selector=opt.selector||'main';
  const root=document.querySelector(selector) || (selector==='main'?document.querySelector('[role="main"]'):null);
  if(!root)return {issues:[{code:'NO_AUDIT_ROOT',severity:'error',detail:'Missing requested visible content root'}],measurements,candidateCount:0};
  const rs=root.getBoundingClientRect(),computed=el=>getComputedStyle(el);
  const excluded=/^(HTML|BODY|SVG|PATH|CANVAS|BUTTON|INPUT|SELECT|TEXTAREA|NAV|HEADER|FOOTER|UL|OL|LI|TABLE|THEAD|TBODY|TR|TD|TH|FORM)$/;
  const candidates=[];
  for(const el of root.querySelectorAll('*')){
   if(excluded.test(el.tagName))continue;
   const r=el.getBoundingClientRect(),s=computed(el);
   if(s.display==='none'||s.display==='contents'||s.visibility==='hidden'||Number(s.opacity)===0)continue;
   if(['fixed','absolute','sticky'].includes(s.position))continue;
   if(r.width<Math.max(120,opt.minWidth||0)||r.height<Math.max(60,opt.minHeight||0))continue;
   if(r.width>rs.width+4)continue;
   const framed=['Top','Right','Bottom','Left'].some(k=>parseFloat(s['border'+k+'Width'])>=.75 && s['border'+k+'Style']!=='none');
   const shadow=s.boxShadow&&s.boxShadow!=='none';
   // A distinct filled surface without a border also qualifies if sufficiently large.
   const fill=s.backgroundColor;
   const rootFill=computed(root).backgroundColor;
   const filled=fill!=='transparent' && fill!=='rgba(0, 0, 0, 0)' && fill!==rootFill && r.width>=150 && r.height>=90;
   if(!framed&&!shadow&&!filled)continue;
   candidates.push({el,r,id:el.getAttribute('data-mf-space-id')||'',frame:!!(framed||shadow||filled)});
  }
  const ancestry=el=>{
    const p=[];let node=el;
    while(node && node!==root){const parent=node.parentElement;if(!parent)break;p.unshift([...parent.children].indexOf(node));node=parent}
    return p.join('.');
  };
  const connected=(a,b)=>{
   let walk=a.el;
   const chain=new Set();
   while(walk&&walk!==root){chain.add(walk);walk=walk.parentElement}
   walk=b.el;
   let common=null;
   while(walk&&walk!==root){if(chain.has(walk)){common=walk;break}walk=walk.parentElement}
   if(!common)return null;
   const reason=common.getAttribute('data-mf-connected-reason')?.trim();
   if(!reason || reason.length<12)return null;
   // A reason on a generic whole-page wrapper is not permission to join every card.
   const contained=candidates.filter(c=>common.contains(c.el)&&c.el!==common);
   return contained.length<=3?reason:null;
  };
  const overlap=(l1,r1,l2,r2)=>Math.min(r1,r2)-Math.max(l1,l2);
  const threshold=opt.touchTolerance??1.5;
  for(let i=0;i<candidates.length;i++)for(let j=i+1;j<candidates.length;j++){
   const a=candidates[i],b=candidates[j];
   if(a.el.contains(b.el)||b.el.contains(a.el))continue;
   const x=overlap(a.r.left,a.r.right,b.r.left,b.r.right);
   const y=overlap(a.r.top,a.r.bottom,b.r.top,b.r.bottom);
   let axis, gap;
   if(x>=Math.min(a.r.width,b.r.width)*.40){
    gap=Math.max(a.r.top,b.r.top)-Math.min(a.r.bottom,b.r.bottom);
    axis='block';
   }else if(y>=Math.min(a.r.height,b.r.height)*.40){
    gap=Math.max(a.r.left,b.r.left)-Math.min(a.r.right,b.r.right);
    axis='inline';
   }else continue;
   // Only near-contact pairs matter in baseline-free diagnosis.
   // Exclude visibly separate objects and avoid comparing distant rows.
   if(gap>Math.max(5,parseFloat(computed(document.documentElement).fontSize)*.33))continue;
   const reason=connected(a,b);
   const pair={id:ancestry(a.el)+'|'+ancestry(b.el),axis,gapPx:+gap.toFixed(2),connected:!!reason,reason:reason||undefined};
   measurements.push(pair);
   if(reason)continue;
   if(gap< -threshold)
    issues.push({code:'INDEPENDENT_SURFACE_OVERLAP',severity:'error',...pair,detail:'Visible independent surface candidates overlap'});
   else if(gap<=threshold)
    issues.push({code:'EXISTING_SURFACES_TOUCH',severity:'error',...pair,detail:'Candidate panels touch even before any optimization; inspect semantic relationship'});
   else
    issues.push({code:'VERY_TIGHT_SURFACE_RELATION',severity:'warning',...pair,detail:'Panel gap is unusually small for distinct framed surfaces; confirm intent'});
  }
  return {issues,measurements,candidateCount:candidates.length};
 },options);
 const old=await auditPanelSpacing(page,{selector:options.selector||'main',requirePairs:false});
 const issues=[...broad.issues];
 for(const i of old.issues){
  if(['UNJUSTIFIED_PANEL_CONTACT','PANEL_OVERLAP','VERY_TIGHT_PANEL_GAP','ASYMMETRIC_GRID_SPACING','HORIZONTAL_OVERFLOW'].includes(i.code)){
   issues.push({...i,source:'direct-grid-flex-audit'});
  }
 }
 if(broad.candidateCount<2)
  issues.push({code:'LOW_SURFACE_COVERAGE',severity:'warning',detail:'Fewer than two framed surfaces found; audit open layouts manually'});
 // No pair measurements are not proof of a clean layout; flag uncertainty.
 if(broad.measurements.length===0 && old.observations.length===0)
  issues.push({code:'NO_ADJACENCY_EVIDENCE',severity:'warning',detail:'No candidate adjacencies; inspect actual page visually'});
 return{
  passed:!issues.some(x=>x.severity==='error'),
  issues,coverage:{framedCandidates:broad.candidateCount,nearPairs:broad.measurements.length,directGridPairs:old.observations.length},
  measurements:broad.measurements,viewport:old.viewport,
  scope:'baseline-free visual defect triage; not an aesthetic score, semantics or full-page coverage guarantee'
 };
}
async function cli(){
 const args=process.argv.slice(2),opts={};
 for(let i=0;i<args.length;i++)if(args[i].startsWith('--'))opts[args[i].slice(2)]=args[++i];
 if(!opts.url)throw new Error('Usage: --url URL [--selector main] [--width 1280] [--font 100] [--out result.json]');
 const {chromium}=await import('playwright');
 const browser=await chromium.launch({headless:true});
 try{
  const page=await browser.newPage({viewport:{width:Number(opts.width||1280),height:850}});
  await page.goto(opts.url);
  if(opts.font)await page.evaluate(n=>document.documentElement.style.fontSize=n+'%',Number(opts.font));
  const result=await auditExistingVisualDefects(page,{selector:opts.selector||'main'});
  if(opts.out)fs.writeFileSync(path.resolve(opts.out),JSON.stringify(result,null,2)+'\n');
  console.log(JSON.stringify(result,null,2));
  process.exitCode=result.passed?0:1;
 }finally{await browser.close()}
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url))
 cli().catch(e=>{console.error(e);process.exitCode=2});
