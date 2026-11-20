#!/usr/bin/env python3
"""Safe side-by-side design option preview. Never injects into the running application."""
from __future__ import annotations
import argparse
import html
import json
import re
import sys
from pathlib import Path

HEX=re.compile(r"^#[0-9a-fA-F]{6}$")
FONTS={"system-ui", "sans-serif", "serif", "monospace"}
def options_from_json(source: Path) -> dict:
    obj=json.loads(source.read_text(encoding="utf-8"))
    if not isinstance(obj,dict) or not isinstance(obj.get("options"),list) or not 2<=len(obj["options"])<=4:
        raise ValueError("Expected 2–4 options")
    names=set()
    for item in obj["options"]:
        if not isinstance(item,dict) or not isinstance(item.get("id"),str) or not re.fullmatch(r"[a-zA-Z0-9_-]{1,40}",item["id"]) or item["id"] in names:
            raise ValueError("Option IDs must be unique safe slugs")
        names.add(item["id"])
        tokens=item.get("tokens",{})
        if not isinstance(tokens,dict): raise ValueError("tokens must be object")
        for key,value in tokens.items():
            if key not in {"background","surface","foreground","accent","border"} or not isinstance(value,str) or not HEX.fullmatch(value):
                raise ValueError("Only safe 6-digit color tokens allowed")
        if not isinstance(item.get("radius",8),int) or not 0<=item.get("radius",8)<=32: raise ValueError("radius outside 0..32")
        if item.get("font","system-ui") not in FONTS: raise ValueError("font must be a safe generic CSS family")
    return obj

def build(obj:dict)->str:
    esc=lambda x:html.escape(str(x),quote=True)
    label=esc(obj.get("title","Design variants"))
    parts=[]
    for i,opt in enumerate(obj["options"]):
        tok={"background":"#f5f5f5","surface":"#ffffff","foreground":"#202020","accent":"#343434","border":"#dddddd"}
        tok.update(opt.get("tokens",{}))
        css=";".join("--"+key+":"+val for key,val in tok.items())+f";--radius:{opt.get('radius',8)}px;font-family:{opt.get('font','system-ui')}"
        parts.append(f"""<section class="variant" style="{esc(css)}">
          <header><span class="option-label">{esc(opt['id'])}</span><strong>{esc(opt.get('name',opt['id']))}</strong></header>
          <div class="app">
            <div class="shell"><div class="brand">{esc(obj.get('product','Example product'))}</div><nav>Overview　 Projects　 Settings</nav></div>
            <div class="body"><small>Example · comparable content</small><h2>{esc(obj.get('heading','Your workspace'))}</h2>
            <p>{esc(obj.get('description','This is the same fictional content in every option.'))}</p>
            <details><summary>Show supporting details</summary><p>Reveal state · same content in every variant</p></details>
            <button type="button" onclick="this.textContent=this.textContent==='Done'?'Try action':'Done'">Try action</button>
            </div></div><p class="rationale">{esc(opt.get('reason','No rationale provided'))}</p>
          </section>""")
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta http-equiv="Content-Security-Policy" content="default-src 'none'; style-src 'unsafe-inline'; script-src 'unsafe-inline'; img-src data:;">
<title>{label}</title><style>
*{{box-sizing:border-box}}body{{margin:0;background:#e8e8e8;color:#111;font:15px system-ui;padding:24px}}
h1{{font-size:22px}}.guide{{max-width:85ch;color:#444}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(min(100%,320px),1fr));gap:18px;margin-top:20px}}
.variant{{background:var(--background);color:var(--foreground);border:1px solid #bbb;border-radius:12px;padding:14px}}
.variant>header{{display:flex;gap:12px;align-items:center;padding-bottom:12px}}.option-label{{font:700 12px monospace}}
.app{{border:1px solid var(--border);border-radius:var(--radius);background:var(--surface);overflow:hidden;min-height:350px}}
.shell{{padding:14px 18px;border-bottom:1px solid var(--border)}}.brand{{font-weight:700}}nav{{font-size:12px;margin-top:10px}}
.body{{padding:20px}}.body small{{color:var(--accent)}}.body h2{{font-size:23px;line-height:1.2}}p{{line-height:1.6}}
button{{border:0;border-radius:var(--radius);background:var(--accent);color:#fff;padding:10px 16px;cursor:pointer}}
button:focus-visible,summary:focus-visible{{outline:3px solid var(--foreground);outline-offset:3px}}
details{{border-block:1px solid var(--border);padding:12px 0;margin-bottom:16px}}summary{{cursor:pointer}}
.rationale{{font-size:13px;opacity:.85}}@media(prefers-reduced-motion:reduce){{*,*::before,*::after{{animation:none!important;transition:none!important}}}}
</style></head><body><h1>{label}</h1>
<p class="guide">Isolated preview of identical synthetic UI content. This does not modify real app files, validate backend behavior, or replace production UI QA. Compare hierarchy, colors, contrast and action clarity; choose only after reviewing.</p>
<div class="grid">{''.join(parts)}</div></body></html>"""

def main()->int:
    p=argparse.ArgumentParser()
    p.add_argument("--input",type=Path,required=True)
    p.add_argument("--output",type=Path,default=Path("artifacts/mauforma-variants.html"))
    p.add_argument("--choose",help="Optional explicit decision ID; saves a decision record, never patches UI source")
    p.add_argument("--decision",type=Path,help="Destination of explicit selected option, required with --choose")
    args=p.parse_args()
    if args.choose and not args.decision: p.error("--choose requires --decision")
    try:
        obj=options_from_json(args.input)
        args.output.parent.mkdir(parents=True,exist_ok=True)
        args.output.write_text(build(obj),encoding="utf-8")
        if args.choose:
            selected=next((o for o in obj["options"] if o["id"]==args.choose),None)
            if selected is None: raise ValueError("Unknown selection")
            if args.decision.exists(): raise FileExistsError("Decision exists; refusing silent overwrite")
            args.decision.parent.mkdir(parents=True,exist_ok=True)
            args.decision.write_text(json.dumps({"selection":selected["id"],"decision_source":"explicit_cli_choice",
               "visual_only":True,"requires_real_ui_implementation":True,"tokens":selected.get("tokens",{}),
               "rationale":selected.get("reason","")},ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
        print(json.dumps({"status":"PREVIEW_CREATED","html":str(args.output),"options":len(obj["options"]),"source_modified":False,
                          "choice":args.choose or None},ensure_ascii=False))
    except (OSError,ValueError,json.JSONDecodeError) as e: p.error(str(e))
    return 0
if __name__=="__main__": sys.exit(main())
