#!/usr/bin/env node
/**
 * Generic, opt-out-by-reason surface adjacency audit for real rendered Web pages.
 * Does not need data-mf-space-id annotations. Unlike the explicit token contract
 * audit, this is a risk triage based on computed layout and visible panel surfaces.
 *
 * CLI:
 *   node scripts/audit_panel_spacing.mjs --url http://localhost:5173/page --out before.json
 *   node scripts/audit_panel_spacing.mjs --url http://localhost:5173/page --baseline before.json
 *
 * Use the same route, viewport and font scale for before/after comparisons.
 * No CSS threshold can prove beauty; human review of full-page screenshots remains required.
 */
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

export async function auditPanelSpacing(page, options={}) {
 const data=await page.evaluate((o)=>{
  const issues=[],observations=[],groups=[];
  const root=document.querySelector(o.selector||'main')||document.querySelector('[role="main"]');
  if(!root)return {passed:false,issues:[{code:'NO_AUDIT_ROOT',severity:'error',detail:'A real content root must be selected'}],observations,groups};
  const css=el=>getComputedStyle(el);
  const rect=el=>el.getBoundingClientRect();
  const isHidden=el=>{
   const s=css(el),r=rect(el);
   return s.display==='none'||s.visibility==='hidden'||Number(s.opacity)===0||r.width<1||r.height<1;
  };
  const blocked=/^(HTML|BODY|NAV|UL|OL|LI|TABLE|TBODY|THEAD|TR|TH|TD|FORM|SELECT|OPTION)$/;
  const panel=(el,depth=0)=>{
   if(blocked.test(el.tagName)||isHidden(el))return false;
   const r=rect(el),s=css(el);
   if(r.width<(o.minWidth??105)||r.height<(o.minHeight??52))return false;
   const border=['Top','Bottom','Left','Right'].some(side=>parseFloat(s['border'+side+'Width'])>=.7 && s['border'+side+'Style']!=='none');
   const shadow=s.boxShadow!=='none';
   const surface=border||shadow;
   if(surface)return true;
   if(depth>0)return false;
   const children=[...el.children].filter(child=>!isHidden(child));
   return children.some(child=>panel(child,1));
  };
  const xpath=el=>{
   const parts=[];
   for(let node=el;node&&node!==root;node=node.parentElement){
    const index=[...node.parentElement.children].indexOf(node);
    parts.unshift(index);
   }
   return parts.join('.');
  };
  const note=(code,severity,info)=>issues.push({code,severity,...info});
  const candidates=[root,...root.querySelectorAll('*')];
  for(const parent of candidates){
   const st=css(parent);
   if(!['grid','flex','inline-grid','inline-flex'].includes(st.display)||blocked.test(parent.tagName)||isHidden(parent))continue;
   const kids=[...parent.children].filter(el=>!isHidden(el)&&panel(el));
   if(kids.length<2)continue;
   const group=xpath(parent);
   const connectedReason=parent.getAttribute('data-mf-connected-reason')||'';
   const justifiedConnection=connectedReason.trim().length>=12;
   let pairs=0,vertical=0,horizontal=0;
   for(let i=0;i<kids.length;i++)for(let j=i+1;j<kids.length;j++){
    let a=kids[i],b=kids[j],ra=rect(a),rb=rect(b);
    const xx=Math.min(ra.right,rb.right)-Math.max(ra.left,rb.left);
    const yy=Math.min(ra.bottom,rb.bottom)-Math.max(ra.top,rb.top);
    let axis,gap;
    if(xx>=Math.min(ra.width,rb.width)*.48 &&
       (ra.top<=rb.top?rb.top>=ra.bottom-2:ra.top>=rb.bottom-2)){
     axis='block';gap=ra.top<=rb.top?rb.top-ra.bottom:ra.top-rb.bottom;vertical++;
    }else if(yy>=Math.min(ra.height,rb.height)*.48 &&
       (ra.left<=rb.left?rb.left>=ra.right-2:ra.left>=rb.right-2)){
     axis='inline';gap=ra.left<=rb.left?rb.left-ra.right:ra.left-rb.right;horizontal++;
    }else continue;
    pairs++;
    const id=group+':'+[...parent.children].indexOf(a)+'-'+[...parent.children].indexOf(b)+':'+axis;
    const actual=+gap.toFixed(2);
    observations.push({id,group,axis,gapPx:actual,connected:justifiedConnection,reason:justifiedConnection?connectedReason:null});
    if(!justifiedConnection && actual<-(o.touchTolerance??1.5)){
     note('PANEL_OVERLAP','error',{id,axis,gapPx:actual,detail:'Independent visible panels overlap'});
    }else if(!justifiedConnection && actual<=(o.touchTolerance??1.5)){
     note('UNJUSTIFIED_PANEL_CONTACT','error',{id,axis,gapPx:actual,detail:'Independent panels touch without a documented connected surface'});
    }else if(!justifiedConnection && actual<Math.max(3,parseFloat(css(document.documentElement).fontSize)*.24)){
     note('VERY_TIGHT_PANEL_GAP','warning',{id,axis,gapPx:actual,detail:'Review whether this unusually small gap expresses the intended grouping'});
    }
   }
   if(pairs){
    groups.push({id:group,pairs,vertical,horizontal,display:st.display,rowGap:st.rowGap,columnGap:st.columnGap,connected:justifiedConnection});
    if(!justifiedConnection && vertical>0 && horizontal>0 && parseFloat(st.rowGap)<2 && parseFloat(st.columnGap)>=6){
     note('ASYMMETRIC_GRID_SPACING','warning',{id:group,rowGap:st.rowGap,columnGap:st.columnGap,detail:'Grid row gap collapsed while columns remain spaced'});
    }
   }
  }
  if(o.requirePairs && observations.length<(o.minPairs||1))
   note('INSUFFICIENT_COVERAGE','error',{detail:'No meaningful panel adjacencies audited; choose a content root or provide an explicit spacing contract'});
  const scrollWidth=document.documentElement.scrollWidth;
  if(scrollWidth>innerWidth+1)note('HORIZONTAL_OVERFLOW','error',{detail:'Document-level horizontal overflow',overflowPx:scrollWidth-innerWidth});
  return {passed:!issues.some(i=>i.severity==='error'),issues,observations,groups,viewport:{width:innerWidth,height:innerHeight,fontSize:css(document.documentElement).fontSize},scope:'Heuristic panel adjacency, not semantic proof or a visual quality score'};
 },options);
 if(options.baseline){
  const old=options.baseline;
  if(!old.viewport||old.viewport.width!==data.viewport?.width||
     old.viewport.fontSize!==data.viewport?.fontSize){
   data.issues.push({code:'INCOMPATIBLE_BASELINE',severity:'error',detail:'Compare the same viewport and font scale'});
  }else{
   const previous=new Map((old.observations||[]).map(p=>[p.id,p]));
   let matched=0;
   for(const now of data.observations){
    const before=previous.get(now.id);
    if(!before || before.axis!==now.axis || before.connected || now.connected)continue;
    matched++;
    if(before.gapPx>=8 && now.gapPx<=before.gapPx*.58 && before.gapPx-now.gapPx>=6){
     data.issues.push({code:'SPACING_REGRESSION',severity:'error',id:now.id,
      beforePx:before.gapPx,afterPx:now.gapPx,detail:'Independent panel gap materially collapsed since the approved baseline'});
    }
   }
   if(options.requirePairs && matched===0)
    data.issues.push({code:'NO_COMPARABLE_PAIRS',severity:'error',detail:'Layout changed or missing baseline matches; manual side-by-side review required'});
   data.baselineMatchedPairs=matched;
  }
 }
 data.passed=!data.issues.some(i=>i.severity==='error');
 return data;
}

async function cli(){
 const args=process.argv.slice(2),config={};
 for(let i=0;i<args.length;i++)if(args[i].startsWith('--'))config[args[i].slice(2)]=args[++i];
 if(!config.url)throw new Error('Required --url. Optional --selector main --baseline before.json --out result.json --width 1280 --font 100');
 const {chromium}=await import('playwright');
 const browser=await chromium.launch({headless:true});
 try{
  const page=await browser.newPage({viewport:{width:Number(config.width||1280),height:800}});
  await page.goto(config.url);
  if(config.font)await page.evaluate(n=>document.documentElement.style.fontSize=n+'%',Number(config.font));
  const baseline=config.baseline?JSON.parse(fs.readFileSync(config.baseline,'utf8')):undefined;
  const result=await auditPanelSpacing(page,{selector:config.selector||'main',baseline,requirePairs:true});
  const output=JSON.stringify(result,null,2);
  if(config.out)fs.writeFileSync(path.resolve(config.out),output+'\n');
  console.log(output);
  process.exitCode=result.passed?0:1;
 }finally{await browser.close()}
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url))
 cli().catch(e=>{console.error(e);process.exitCode=2});
