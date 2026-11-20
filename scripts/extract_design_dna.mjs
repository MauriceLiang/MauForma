#!/usr/bin/env node
/**
 * Read-only, opt-in browser evidence collector. Requires a preinstalled Playwright.
 * Samples computed styles only: never captures text, cookies, storage or page source.
 * Screenshots are local evidence and must not be committed without authorization.
 */
import fs from "node:fs/promises";
import path from "node:path";
import dns from "node:dns/promises";
import net from "node:net";

const argv=process.argv.slice(2);
const values=key=>argv.flatMap((v,i)=>v==="--"+key?[argv[i+1]]:[]).filter(Boolean);
const get=(key,fallback)=>values(key)[0]??fallback;
if(argv.includes("--help")){
  console.log("Usage: node scripts/extract_design_dna.mjs --url https://example.com [--url https://example.com/page] --out ./artifacts/dna [--allow-local] [--width 1280] [--height 800]");
  process.exit(0);
}
const urls=values("url");
if(!urls.length||urls.length>5){console.error("Specify 1–5 --url values.");process.exit(2);}
const width=Number(get("width","1280")),height=Number(get("height","800"));
if(!Number.isInteger(width)||!Number.isInteger(height)||width<320||width>3840||height<320||height>2160){console.error("Invalid viewport");process.exit(2);}
const allowLocal=argv.includes("--allow-local");
const output=path.resolve(get("out","./artifacts/mauforma-design-dna"));
const blockedHostname=host=>{
 const h=host.toLowerCase().replace(/\.$/,"").replace(/^\[|\]$/g,"");
 if(["localhost","localhost.localdomain"].includes(h)||h.endsWith(".localhost")||h.endsWith(".local")||h.endsWith(".internal")||h.endsWith(".test"))return true;
 const family=net.isIP(h);
 if(family===6){
   if(h==="::1"||h==="::"||h.startsWith("fc")||h.startsWith("fd")||h.startsWith("fe8")||h.startsWith("fe9")||h.startsWith("fea")||h.startsWith("feb"))return true;
   if(h.toLowerCase().startsWith("::ffff:"))return blockedHostname(h.slice(7));
   return false;
 }
 if(family===4){
   const [a,b]=h.split(".").map(Number);
   return a===0||a===10||a===127||a>=224||a===169&&b===254||a===172&&b>=16&&b<=31||a===192&&b===168||a===100&&b>=64&&b<=127||a===192&&b===0||a===198&&(b===18||b===19)||a===198&&b===51||a===203&&b===0;
 }
 return false;
};
const verified=new Map();
async function validateUrl(raw){
 const u=new URL(raw);
 if(!["http:","https:"].includes(u.protocol)||u.username||u.password)throw new Error("Only credential-free HTTP(S) allowed");
 if(!allowLocal){
   if(blockedHostname(u.hostname))throw new Error("Private/local network URL blocked; --allow-local only for explicitly authorized local fixtures");
   if(!verified.has(u.hostname)){
     const ips=await dns.lookup(u.hostname,{all:true,verbatim:true});
     if(!ips.length||ips.some(x=>blockedHostname(x.address)))throw new Error("URL resolves to a private/reserved network address");
     verified.set(u.hostname,ips.map(x=>x.address));
   }
 }
 return u.href;
}
let chromium;
try{({chromium}=await import("playwright"));}catch{console.error("NOT RUN: Playwright is not installed. No packages installed automatically.");process.exit(3);}
const results=[],failures=[];
await fs.mkdir(output,{recursive:true});
const browser=await chromium.launch({headless:true});
try{
 for(let i=0;i<urls.length;i++){
   const item={requested_url:urls[i],index:i+1,status:"NOT_TESTED",observed_at:new Date().toISOString(),viewport:{width,height},design_map:{},taste_decisions:[],source:"rendered DOM + computed styles",limitations:["No author intent can be inferred from computed CSS","Screenshots are not a replacement for visual review"]};
   results.push(item);
   let context;
   try{
     await validateUrl(urls[i]);
     context=await browser.newContext({viewport:{width,height},serviceWorkers:"block",acceptDownloads:false});
     await context.route("**/*",async route=>{
       try{await validateUrl(route.request().url());await route.continue();}catch{await route.abort("blockedbyclient");}
     });
     const page=await context.newPage();
     page.on("pageerror",e=>{(item.page_errors??=[]).push(String(e));});
     const response=await page.goto(urls[i],{waitUntil:"domcontentloaded",timeout:30000});
     item.status_code=response?.status()??null;
     item.final_url=await validateUrl(page.url());
     if(!response||response.status()>=400)throw new Error("Page could not be loaded successfully");
     const fontReady=await Promise.race([page.evaluate(()=>document.fonts.ready.then(()=>true)),new Promise(resolve=>setTimeout(()=>resolve(false),4000))]);
     item.font_status=fontReady?"ready":"timeout";
     item.design_map=await page.evaluate(()=>{
       const counts={};
       const selectors="body,header,main,section,h1,h2,h3,p,button,a,input,[role='button'],[class*='card']";
       const samples=[];
       function record(map,key,value){
         if(!value||value==="none"||value==="normal"||value==="0px")return;
         const normalized=String(value).trim();
         const counter=map[key]??(map[key]={});counter[normalized]=(counter[normalized]??0)+1;
       }
       const list=[...document.querySelectorAll(selectors)].slice(0,250);
       for(const el of list){
         const r=el.getBoundingClientRect();
         if(!r.width||!r.height||r.bottom<0||r.top>innerHeight||getComputedStyle(el).visibility==="hidden")continue;
         const s=getComputedStyle(el);
         for(const key of ["color","backgroundColor","fontFamily","fontSize","fontWeight","lineHeight","borderRadius","boxShadow","gap","paddingTop","paddingLeft","marginTop"]){record(counts,key,s[key]);}
         if(samples.length<35)samples.push({selector:el.tagName.toLowerCase(),role:el.getAttribute("role")??null,rect:{x:Math.round(r.x),y:Math.round(r.y),width:Math.round(r.width),height:Math.round(r.height)},styles:{color:s.color,backgroundColor:s.backgroundColor,fontFamily:s.fontFamily,fontSize:s.fontSize,fontWeight:s.fontWeight,lineHeight:s.lineHeight,borderRadius:s.borderRadius,gap:s.gap}});
       }
       return {properties:Object.fromEntries(Object.entries(counts).map(([key,entries])=>[key,Object.entries(entries).sort((a,b)=>b[1]-a[1]).slice(0,10).map(([value,count])=>({value,count,evidence:"computed-style"}))])),samples,visible_sample_count:samples.length,document_title_length:document.title.length};
     });
     const filename="page-"+String(i+1).padStart(2,"0")+".png";
     await page.screenshot({path:path.join(output,filename),fullPage:false});
     item.screenshot=filename;
     item.status=item.font_status==="ready"&&item.design_map.visible_sample_count>0?"OBSERVED":"INCONCLUSIVE";
   }catch(e){item.status="BLOCKED";item.error=String(e);failures.push({url:urls[i],error:String(e)});}
   finally{await context?.close();}
 }
}finally{await browser.close();}
const normalize=s=>String(s).replace(/\|/g,"\\|").replace(/\n/g," ");
const markdown=[
 "# Design DNA — observed evidence","",
 "> Computed browser styles, not verified design tokens or the original designer's intention.","",
 ...results.flatMap((item)=>[
  "## Page "+item.index,"",
  "- URL: "+normalize(item.requested_url),
  "- Final URL: "+normalize(item.final_url??"UNKNOWN"),
  "- Status: "+item.status+"; fonts: "+(item.font_status??"UNKNOWN"),
  "- Viewport: "+width+" × "+height,
  "- Screenshot: "+(item.screenshot??"not captured"),
  ...(item.error?["- Error: "+normalize(item.error)]:[]),"",
  "| Property | Observed common values |",
  "| --- | --- |",
  ...Object.entries(item.design_map.properties??{}).map(([k,values])=>"| "+k+" | "+normalize(values.slice(0,4).map(x=>x.value+" ("+x.count+")").join(", "))+" |"),
  "","**Inferred motivations and transfer decisions:** NOT REVIEWED. A human must explain rationale, competing choices, and suitability using real screenshots.",""
 ])
];
const report={status:failures.length?"PARTIAL_OR_BLOCKED":results.some(x=>x.status!=="OBSERVED")?"INCONCLUSIVE":"OBSERVED_NOT_APPROVED",results,failures,notes:["No third-party screenshots or extracted content were added to the Skill repository","Explicit confirmation required before adopting any inferred tokens"]};
await Promise.all([
fs.writeFile(path.join(output,"report.json"),JSON.stringify(report,null,2)+"\n"),
fs.writeFile(path.join(output,"report.md"),markdown.join("\n")+"\n")
]);
console.log(JSON.stringify({status:report.status,output,pages:results.map(x=>({status:x.status,url:x.final_url??x.requested_url,samples:x.design_map.visible_sample_count??0}))},null,2));
process.exit(failures.length?1:results.some(x=>x.status!=="OBSERVED")?2:0);
