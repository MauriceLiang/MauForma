#!/usr/bin/env node
/**
 * Inspect rendered selection controls for implementation-mix candidates.
 * Never infers a vendor, visual quality or native OS popup appearance.
 * Requires existing Playwright + Chromium in the caller's project.
 * Usage: node scripts/audit_control_consistency.mjs --url http://localhost:3000 --selector main
 * Optional: --out /tmp/control-consistency.json
 * No user-visible labels or text are collected. Do not upload private page paths.
 */
import fs from 'node:fs';
import path from 'node:path';
import {fileURLToPath} from 'node:url';

export async function auditControlConsistency(page, options={}) {
  return page.evaluate(opts => {
    const root = document.querySelector(opts.selector || 'main')
      || document.querySelector('[role="main"]') || document.body;
    const visible = el => {
      if (!el || !el.isConnected || el.closest('[hidden],[inert],[aria-hidden="true"]')) return false;
      const style = getComputedStyle(el);
      const rect = el.getBoundingClientRect();
      return style.display !== 'none' && style.visibility !== 'hidden'
        && Number(style.opacity) > 0 && rect.width > 0 && rect.height > 0;
    };
    const location = el => {
      const nodes = [];
      for (let node=el; node && node!==root && nodes.length<7; node=node.parentElement) {
        if (node.id) { nodes.unshift('#'+node.id); break; }
        const peers = node.parentElement
          ? [...node.parentElement.children].filter(n => n.tagName===node.tagName) : [];
        const nth = peers.length>1 ? ':nth-of-type('+(peers.indexOf(node)+1)+')' : '';
        nodes.unshift(node.tagName.toLowerCase()+nth);
      }
      return nodes.join(' > ');
    };
    const group = el => {
      const ancestor = el.closest('form,fieldset,[role="toolbar"],[data-mf-control-group]');
      return ancestor && root.contains(ancestor) ? location(ancestor) : '(page)';
    };
    const styleOf = el => {
      const style=getComputedStyle(el);
      const rect=el.getBoundingClientRect();
      return {
        fontFamily: style.fontFamily, fontSize: style.fontSize,
        borderRadius: style.borderRadius, backgroundColor: style.backgroundColor,
        color: style.color, height: Math.round(rect.height),
        borderWidth: style.borderWidth
      };
    };
    const nodes=[...root.querySelectorAll('select,[role="combobox"],button[aria-haspopup="listbox"]')].filter(visible);
    const seen=new Set(),controls=[];
    for (const el of nodes) {
      if (seen.has(el)) continue;
      seen.add(el);
      const native=el.tagName==='SELECT';
      const implementation=native?'native_select':'custom_or_library_selection';
      controls.push({path:location(el),group:group(el),role:'value_selection',
        implementation,style:styleOf(el)});
    }
    const native=controls.filter(c=>c.implementation==='native_select');
    const custom=controls.filter(c=>c.implementation==='custom_or_library_selection');
    const candidates=[];
    if (native.length && custom.length) {
      const groups=[...new Set(controls.map(c=>c.group))];
      candidates.push({code:'MIXED_SELECTION_SOURCES',severity:'review',
        scopes:groups,detail:'Native select and custom/ARIA selection controls coexist. Verify their ownership and visual/behavioral consistency; do not auto-migrate.'});
    }
    if (native.length) candidates.push({
      code:'NATIVE_SELECT_POPUP_REVIEW',severity:'info',
      count:native.length,
      detail:'OS/browser may own the expanded select menu. Trigger CSS cannot guarantee matching option popup. Inspect actual target platform open state.'
    });
    return {status:candidates.length?'CANDIDATES_FOR_REVIEW':'NO_MIXED_SELECTION_SOURCES_OBSERVED',
      verified:false,scope:'Rendered selection-control inventory; not full visual/accessibility QA',
      controls,counts:{nativeSelect:native.length,customOrLibrarySelection:custom.length},
      candidates,note:'DOM cannot prove library provenance, open OS popup skin, or that deliberate native controls are inconsistent.'};
  }, options);
}

async function main() {
  const args=process.argv.slice(2),opts={};
  for(let i=0;i<args.length;i++) if(args[i].startsWith('--')) opts[args[i].slice(2)]=args[++i];
  if(!opts.url) throw new Error('Usage: --url URL [--selector main] [--out report.json]');
  const {chromium}=await import('playwright');
  const browser=await chromium.launch({headless:true});
  try {
    const page=await browser.newPage();
    await page.goto(opts.url,{waitUntil:'domcontentloaded'});
    const report=await auditControlConsistency(page,{selector:opts.selector});
    if(opts.out) fs.writeFileSync(path.resolve(opts.out),JSON.stringify(report,null,2)+'\n');
    console.log(JSON.stringify(report,null,2));
  } finally { await browser.close(); }
}
if(process.argv[1] && path.resolve(process.argv[1])===fileURLToPath(import.meta.url))
  main().catch(error=>{console.error(error);process.exitCode=2;});

