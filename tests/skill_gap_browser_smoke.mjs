#!/usr/bin/env node
/** End-to-end checks against synthetic local HTML only; no external source or real product. */
import http from "node:http";
import fs from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import assert from "node:assert/strict";
import {execFile} from "node:child_process";
import {promisify} from "node:util";
const exec=promisify(execFile);
const root=path.resolve(import.meta.dirname,"..");
const tmp=await fs.mkdtemp(path.join(os.tmpdir(),"mauforma-skill-gap-"));
const fixture=[
 "<!doctype html><html><head><style>",
 ":root{--brand:#112233}body{font:16px system-ui;color:rgb(20,30,40);padding:24px}",
 "h1{font-size:30px}button{background:#112233;color:white;padding:12px 16px;border-radius:8px}",
 "#moving{display:block;width:55px;height:40px;background:#556677;margin-top:15px}",
 "</style></head><body><header>Header</header><main><h1>Design fixture</h1>",
 "<p>Public synthetic evidence only.</p><button id='go'>Move box</button><div id='moving'></div></main>",
 "<script>document.querySelector('#go').addEventListener('click',()=>{",
 " const box=document.querySelector('#moving');",
 " box.style.transform=box.style.transform?'':'translateX(85px)';",
 "});</script></body></html>"
].join("");
const server=http.createServer((req,res)=>{res.writeHead(200,{"content-type":"text/html;charset=utf-8"});res.end(fixture);});
await new Promise(resolve=>server.listen(0,"127.0.0.1",resolve));
const address=server.address(),url="http://127.0.0.1:"+address.port+"/";
try{
  const dnaDir=path.join(tmp,"dna");
  await exec(process.execPath,["scripts/extract_design_dna.mjs","--url",url,"--allow-local","--out",dnaDir],{cwd:root,timeout:60000});
  const dna=JSON.parse(await fs.readFile(path.join(dnaDir,"report.json"),"utf8"));
  assert.equal(dna.results[0].status,"OBSERVED");
  assert.ok(dna.results[0].design_map.visible_sample_count>0);
  assert.equal(dna.results[0].design_map.samples.some(x=>"text" in x),false,"Do not store raw content");
  await fs.access(path.join(dnaDir,"page-01.png"));
  const scenario={steps:[{id:"jump",action:"click",selector:"#go",track:["#moving"],intervalMs:70,captureMs:360,settleMs:120}]};
  const scenarioPath=path.join(tmp,"scenario.json");
  await fs.writeFile(scenarioPath,JSON.stringify(scenario));
  const motionDir=path.join(tmp,"motion");
  try{await exec(process.execPath,["scripts/motion_rehearsal.mjs","--url",url,"--scenario",scenarioPath,"--out",motionDir],{cwd:root,timeout:60000});}
  catch(e){if(e.code!==2)throw e;}
  const motion=JSON.parse(await fs.readFile(path.join(motionDir,"report.json"),"utf8"));
  assert.notEqual(motion.status,"BLOCKED");
  const step=motion.steps[0];
  assert.equal(step.raf_metrics.observedPointerdown,true,"Capture must start before click");
  assert.ok(step.raf.events.some(x=>x.type==="pointerup"));
  assert.ok(step.candidates.some(x=>x.kind==="possible-position-jump"),"Must detect abrupt 85px movement");
  await fs.access(path.join(motionDir,"01-jump","contact-sheet.html"));
  console.log("Skill gap browser smoke passed (synthetic fixture): computed styles, click-time rAF, jump candidate, frame evidence");
}finally{
  await new Promise(resolve=>server.close(resolve));
  await fs.rm(tmp,{recursive:true,force:true});
}
