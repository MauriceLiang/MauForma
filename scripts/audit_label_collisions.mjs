#!/usr/bin/env node
/**
 * Baseline-free rendered-layout audit for independent compact labels and their
 * readable text. Finds overlapping chips/badges/buttons even when large-panel
 * spacing and document overflow checks pass. No special CSS class is required.
 *
 * Usage: node scripts/audit_label_collisions.mjs --url http://localhost:5173/page
 *        [--selector main] [--width 1280] [--height 800] [--out report.json]
 *
 * This is a geometry-based candidate detector, NOT pixel/aesthetic proof.
 * Inspect visual stacking, screenshot, text legibility and intentional layers
 * before any repair. No source mutation or dependency installation.
 */
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

export async function auditLabelCollisions(page, options = {}) {
  return page.evaluate((opts) => {
    const root = document.querySelector(opts.selector || 'main')
      || ((opts.selector || 'main') === 'main' ? document.querySelector('[role="main"]') : null);
    if (!root) return {
      passed: false, status: 'AUDIT_ROOT_MISSING',
      issues: [{code:'NO_AUDIT_ROOT',severity:'error',detail:'Requested rendered content root not found'}],
      coverage: {compactLabels:0,textFragments:0,pairsChecked:0},
      scope:'Rendered geometry only; real visual and semantic review required'
    };
    const css = el => getComputedStyle(el);
    const rect = el => el.getBoundingClientRect();
    const visible = el => {
      if (!el || !el.isConnected || el.closest('[hidden],[inert],[aria-hidden="true"]')) return false;
      const s=css(el),r=rect(el);
      return s.display!=='none' && s.display!=='contents' && s.visibility==='visible'
        && Number(s.opacity)>0.02 && r.width>2 && r.height>2;
    };
    const locator = el => {
      if (el.id) return '#' + el.id;
      const items=[];
      for(let n=el;n&&n!==root&&items.length<6;n=n.parentElement) {
        if(n.id){items.unshift('#'+n.id);break;}
        const siblings=n.parentElement ? [...n.parentElement.children].filter(k=>k.tagName===n.tagName) : [];
        items.unshift(n.tagName.toLowerCase()+(siblings.length>1?':nth-of-type('+(siblings.indexOf(n)+1)+')':''));
      }
      return items.join(' > ') || root.tagName.toLowerCase();
    };
    const roleLayer = el => el.closest('[role="dialog"],[role="tooltip"],[role="menu"],[role="listbox"],dialog,[popover]') || root;
    const overlap = (a,b) => ({
      x: Math.min(a.right,b.right)-Math.max(a.left,b.left),
      y: Math.min(a.bottom,b.bottom)-Math.max(a.top,b.top)
    });
    const isPainted = el => {
      const s=css(el);
      const border=['Top','Right','Bottom','Left'].some(side=>
        parseFloat(s['border'+side+'Width'])>=0.7 && s['border'+side+'Style']!=='none');
      const bg=s.backgroundColor;
      const filled = bg!=='transparent' && bg!=='rgba(0, 0, 0, 0)' &&
        !/^rgba?\([^)]*,\s*0(?:\.0+)?\)$/.test(bg);
      return border || filled || (s.boxShadow && s.boxShadow!=='none');
    };
    const all=[root,...root.querySelectorAll('*')];
    const candidateLimit=500, textLimit=600;
    const excluded=/^(SCRIPT|STYLE|NOSCRIPT|SVG|PATH|CANVAS|OPTION|OPTGROUP|INPUT|TEXTAREA|VIDEO|IMG)$/;
    const compact=[];
    const textFragments=[];
    for(const el of all) {
      if(excluded.test(el.tagName) || !visible(el))continue;
      const r=rect(el),plain=(el.innerText||'').replace(/\s+/g,' ').trim();
      if(el!==root && plain && plain.length<=180 && r.height>=14 &&
         r.height<=180 && r.width>=20 && r.width<=Math.max(1200,root.clientWidth+5) &&
         isPainted(el) && compact.length<candidateLimit) {
        compact.push({el,r,plain,layer:roleLayer(el),locator:locator(el)});
      }
      // Text fragments belong to their actual text nodes. No parent duplications.
      if(textFragments.length>=textLimit)continue;
      for(const n of el.childNodes) {
        if(n.nodeType!==Node.TEXT_NODE || !n.textContent?.trim())continue;
        if(n.textContent.trim().length>280)continue;
        const range=document.createRange();range.selectNodeContents(n);
        for(const part of range.getClientRects()){
          if(part.width<=2 || part.height<=2)continue;
          if(textFragments.length>=textLimit)break;
          textFragments.push({el,r:part,layer:roleLayer(el),locator:locator(el),
            excerpt:n.textContent.trim().slice(0,70)});
        }
      }
    }
    // Avoid treating a wrapper enclosing genuine chips as an extra chip.
    const labels=compact.filter(a=>!compact.some(b=>b!==a && a.el.contains(b.el)));
    const issues=[],pairKeys=new Set();
    const add=(code,a,b,measure,detail)=>{
      const key=code+'|'+[a.locator,b.locator].sort().join('|');
      if(pairKeys.has(key))return;
      pairKeys.add(key);
      issues.push({code,severity:'error',first:a.locator,second:b.locator,
        firstText:a.plain||a.excerpt||'',secondText:b.plain||b.excerpt||'',
        overlapX:+measure.x.toFixed(1),overlapY:+measure.y.toFixed(1),detail});
    };
    let pairsChecked=0;
    for(let i=0;i<labels.length;i++)for(let j=i+1;j<labels.length;j++){
      const a=labels[i],b=labels[j];
      if(a.layer!==b.layer || a.el.contains(b.el) || b.el.contains(a.el))continue;
      const o=overlap(a.r,b.r);
      pairsChecked++;
      if(o.x>3 && o.y>3 &&
         o.y>=Math.min(a.r.height,b.r.height)*.25) {
        add('COMPACT_LABEL_SURFACE_OVERLAP',a,b,o,
          'Independent compact readable surfaces physically overlap; inspect painted stacking, lost text and accessible hit targets');
      }
    }
    // Catch intersecting visible text even when one/both labels have no painted background.
    for(let i=0;i<textFragments.length;i++){
      const a=textFragments[i];
      for(let j=i+1;j<textFragments.length;j++){
        const b=textFragments[j];
        if(a.el===b.el || a.layer!==b.layer ||
           a.el.contains(b.el) || b.el.contains(a.el))continue;
        const o=overlap(a.r,b.r);
        if(o.x>=3 && o.y>=3 && o.y>=Math.min(a.r.height,b.r.height)*.25)
          add('READABLE_TEXT_COLLISION',a,b,o,
            'Independent rendered text fragments intersect; check occlusion, line breaking and reading order');
      }
    }
    // Text can be hidden under a filled pill even if the two text fragments
    // themselves do not intersect (e.g. left chip paints over right label).
    for(const t of textFragments)for(const label of labels){
      if(t.layer!==label.layer || label.el.contains(t.el) || t.el.contains(label.el))continue;
      const o=overlap(t.r,label.r);
      if(o.x>4 && o.y>4 && o.y>=Math.min(t.r.height,label.r.height)*.25)
        add('TEXT_OBSCURED_BY_COMPACT_SURFACE',t,label,o,
          'Readable text enters an unrelated painted compact surface; the text may be obscured or visually fused');
    }
    const limited=compact.length>=candidateLimit || textFragments.length>=textLimit;
    return {
      passed:!issues.length && !limited,
      status: limited?'INCOMPLETE_COVERAGE':issues.length?'GEOMETRY_RISKS':'NO_COLLISIONS_OBSERVED',
      issues,
      coverage:{compactLabels:labels.length,textFragments:textFragments.length,pairsChecked,limited},
      scope:'Rendered DOM geometry for compact labels and text only; no Canvas/image-text OCR, no proof of correct meaning or visual quality'
    };
  },options);
}
async function cli(){
  const args=process.argv.slice(2),opts={};
  for(let i=0;i<args.length;i++)if(args[i].startsWith('--'))opts[args[i].slice(2)]=args[++i];
  if(!opts.url || !/^https?:\/\//.test(opts.url))
    throw new Error('Usage: --url http://localhost:5173/path [--selector main] [--width 1280] [--height 800] [--out report.json]');
  const {chromium}=await import('playwright');
  const browser=await chromium.launch({headless:true});
  try{
    const page=await browser.newPage({viewport:{width:Number(opts.width||1280),height:Number(opts.height||800)}});
    await page.goto(opts.url,{waitUntil:'domcontentloaded'});
    const report=await auditLabelCollisions(page,{selector:opts.selector||'main'});
    if(opts.out)fs.writeFileSync(path.resolve(opts.out),JSON.stringify(report,null,2)+'\n');
    console.log(JSON.stringify(report,null,2));process.exitCode=report.passed?0:1;
  }finally{await browser.close();}
}
if(process.argv[1] && path.resolve(process.argv[1])===fileURLToPath(import.meta.url))
  cli().catch(error=>{console.error(error);process.exitCode=2;});
