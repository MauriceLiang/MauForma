#!/usr/bin/env node
/**
 * Annotated icon-group geometry/style risk audit.
 * Measures objective risks only. Does NOT grade attractiveness or semantic correctness.
 * CLI: node scripts/audit_icon_consistency.mjs --url http://localhost:5173 --out icon-audit.json
 */
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

export async function auditIcons(page) {
 return page.evaluate(()=>{
  const issues=[],groups=[];
  const range=(v,base,tolerance=.12)=>Math.abs(v-base)<=Math.max(1,base*tolerance);
  for(const group of document.querySelectorAll('[data-mf-icon-group]')){
   const icons=[...group.querySelectorAll('[data-mf-ui-icon]')];
   const id=group.getAttribute('data-mf-icon-group');
   if(icons.length===0){
    issues.push({id,code:'EMPTY_ICON_GROUP',detail:'No explicitly annotated UI icons'});continue;
   }
   const records=[];
   for(const svg of icons){
    const name=svg.getAttribute('data-mf-icon-name')||'';
    const pack=svg.getAttribute('data-mf-icon-pack')||'';
    const r=svg.getBoundingClientRect(),style=getComputedStyle(svg);
    const view=svg.getAttribute('viewBox'),stroke=parseFloat(style.strokeWidth);
    const label=svg.closest('.navitem')?.querySelector('.label');
    let opticalDelta=0;
    if(label){
     const lr=label.getBoundingClientRect();
     opticalDelta=Math.abs((r.top+r.height/2)-(lr.top+lr.height/2));
     if(opticalDelta>2.5)
      issues.push({id,code:'ICON_LABEL_MISALIGNMENT',icon:name,deltaPx:+opticalDelta.toFixed(2)});
    }
    if(!name||!pack)
     issues.push({id,code:'UNVERIFIED_ICON_SOURCE',detail:'Icon source/name must be tracked'});
    if(svg.children.length===0||r.width<1||r.height<1)
     issues.push({id,code:'EMPTY_ICON',icon:name});
    if(view!=='0 0 24 24')
     issues.push({id,code:'NONSTANDARD_ARTBOARD',icon:name,detail:'Mismatch within this group; other libraries may use valid different artboards'});
    if(!range(r.width,r.height,.05))
     issues.push({id,code:'DISTORTED_ICON',icon:name,width:r.width,height:r.height});
    if(svg.getAttribute('aria-hidden')!=='true' && label)
     issues.push({id,code:'REDUNDANT_SCREENREADER_ICON',icon:name});
    records.push({name,pack,width:r.width,height:r.height,stroke,view,alignmentPx:opticalDelta});
   }
   const base=records[0];
   for(const rec of records.slice(1)){
    if(!range(rec.width,base.width,.12))
     issues.push({id,code:'INCONSISTENT_ICON_SIZE',icon:rec.name,referencePx:base.width,actualPx:rec.width});
    if(Number.isFinite(rec.stroke)&&Number.isFinite(base.stroke)&&Math.abs(rec.stroke-base.stroke)>.35)
     issues.push({id,code:'INCONSISTENT_STROKE',icon:rec.name,reference:base.stroke,actual:rec.stroke});
    if(rec.pack!==base.pack)
     issues.push({id,code:'MIXED_ICON_PACK',icon:rec.name,reference:base.pack,actual:rec.pack});
   }
   groups.push({id,iconCount:icons.length,icons:records});
  }
  if(document.documentElement.scrollWidth>innerWidth+1)
   issues.push({code:'UNEXPECTED_HORIZONTAL_OVERFLOW',width:innerWidth,scrollWidth:document.documentElement.scrollWidth});
  return {passed:issues.length===0,issues,groups,scope:'Annotated icon group geometry and identity only. Human semantic/visual assessment still required.'};
 });
}

async function cli(){
 const args=process.argv.slice(2),opt={};
 for(let i=0;i<args.length;i++)if(args[i].startsWith('--'))opt[args[i].slice(2)]=args[++i];
 if(!opt.url)throw new Error('Required: --url URL. Optional: --out path.json');
 const {chromium}=await import('playwright');
 const browser=await chromium.launch({headless:true});
 try{
  const page=await browser.newPage({viewport:{width:1280,height:800}});
  await page.goto(opt.url);
  const result=await auditIcons(page);
  const text=JSON.stringify(result,null,2);
  if(opt.out)fs.writeFileSync(path.resolve(opt.out),text+'\n');
  console.log(text);
  process.exitCode=result.passed?0:1;
 }finally{await browser.close()}
}
if(process.argv[1]&&path.resolve(process.argv[1])===fileURLToPath(import.meta.url)){
 cli().catch(err=>{console.error(err);process.exitCode=2});
}
