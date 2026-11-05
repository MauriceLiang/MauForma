#!/usr/bin/env python3
"""Validate Icon Art Direction decisions; static intent, not aesthetic score or upstream freshness proof."""
from __future__ import annotations
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
SAMPLE=ROOT/"assets/icon-curation-patterns.json"
MODES={"Operate","Persuade","Read","Experience"}
REQUIRED=(
 "references/icon-art-direction-gate.md","assets/icon-curation-patterns.json",
 "assets/icon-art-direction-lab.html","scripts/validate_icon_curation.py",
 "scripts/audit_icon_consistency.mjs","tests/test_icon_curation.py",
 "tests/icon_art_direction_browser_smoke.mjs","SKILL.md"
)
def validate_plan(plan:object,require_modes=False)->list[str]:
 errors=[]
 if not isinstance(plan,dict) or plan.get("schema_version")!="1.0":
  return ["Icon plan schema version must be 1.0"]
 profiles=plan.get("profiles")
 if not isinstance(profiles,list) or not profiles:return ["Missing product profiles"]
 ids=set();modes=set()
 for p in profiles:
  if not isinstance(p,dict):errors.append("Invalid profile");continue
  pid=p.get("id")
  if not isinstance(pid,str) or not pid or pid in ids:errors.append("Distinct profile IDs required")
  ids.add(pid)
  if p.get("mode") not in MODES:errors.append(f"{pid}: invalid Web mode")
  else:modes.add(p["mode"])
  for field in ("goal","library","library_source","style","license","icon_size_role"):
   if not isinstance(p.get(field),str) or not p[field].strip():errors.append(f"{pid}: missing {field}")
  if not str(p.get("library_source","")).startswith("https://"):errors.append(f"{pid}: library official URL required")
  icons=p.get("icons")
  if not isinstance(icons,list) or not icons:errors.append(f"{pid}: no icon shortlist");continue
  entries=set();glyphs=set()
  for i in icons:
   if not isinstance(i,dict):errors.append(f"{pid}: invalid icon entry");continue
   key=i.get("id");chosen=i.get("chosen");cands=i.get("candidates",[])
   if not isinstance(key,str) or not key or key in entries:errors.append(f"{pid}: duplicate/missing icon target")
   entries.add(key)
   # UI labels can be one or two CJK characters; require meaning in the separate rationale.
   for field in ("label","semantic_intent","reason"):
    minimum=1 if field=="label" else 6
    if not isinstance(i.get(field),str) or len(i[field].strip())<minimum:
     errors.append(f"{pid}/{key}: missing meaningful {field}")
   if not isinstance(chosen,str) or not chosen:errors.append(f"{pid}/{key}: missing chosen icon")
   if chosen in glyphs:errors.append(f"{pid}/{key}: repeated symbol in distinct navigation item; review semantic collision")
   glyphs.add(chosen)
   if i.get("presentation") not in {"icon-and-text","icon-only","text-only"}:errors.append(f"{pid}/{key}: invalid presentation")
   if not isinstance(cands,list) or len(cands)<2:errors.append(f"{pid}/{key}: compare at least two real semantic candidates");continue
   if chosen not in [c.get("name") for c in cands if isinstance(c,dict)]:errors.append(f"{pid}/{key}: chosen icon not in shortlist")
   if len({c.get("name") for c in cands if isinstance(c,dict)})<2:errors.append(f"{pid}/{key}: no distinct alternative")
   for c in cands:
    if not isinstance(c,dict) or c.get("verified") is not True:
     errors.append(f"{pid}/{key}: candidate must be confirmed in its installed/upstream library");continue
    if not isinstance(c.get("name"),str) or not c["name"] or not str(c.get("source","")).startswith("https://"):
     errors.append(f"{pid}/{key}: candidate missing name or official icon source")
    if not isinstance(c.get("rationale"),str) or len(c["rationale"].strip())<12:
     errors.append(f"{pid}/{key}: candidate needs contextual reasoning")
   if i.get("presentation")=="icon-only" and not i.get("accessible_name"):
    errors.append(f"{pid}/{key}: icon-only action needs accessible name")
 if require_modes and modes!=MODES:errors.append("Generic reference should cover four Web modes")
 return errors

def validate_repository()->list[str]:
 errors=[f"Missing icon resource: {p}" for p in REQUIRED if not (ROOT/p).is_file()]
 if errors:return errors
 skill=(ROOT/"SKILL.md").read_text("utf-8")
 for s in ("icon-art-direction-gate.md","validate_icon_curation.py","audit_icon_consistency.mjs"):
  if s not in skill:errors.append("Missing mandatory icon route: "+s)
 try:errors.extend(validate_plan(json.loads(SAMPLE.read_text("utf8")),require_modes=True))
 except (OSError,ValueError) as e:errors.append(str(e))
 return errors

def main()->int:
 ap=argparse.ArgumentParser(description="Validate selected icon semantics, provenance and design shortlist")
 ap.add_argument("file",nargs="?",type=Path)
 ap.add_argument("--repository",action="store_true")
 ap.add_argument("--json",action="store_true")
 a=ap.parse_args()
 if not a.file and not a.repository:ap.error("Provide --repository or plan JSON")
 issues=validate_repository() if a.repository else []
 if a.file:
  try:issues.extend(validate_plan(json.loads(a.file.read_text("utf8"))))
  except (OSError,ValueError) as e:issues.append(str(e))
 if a.json:print(json.dumps({"passed":not issues,"issues":issues,"scope":"static design-contract only; library versions and human visual judgment require separate verification"},ensure_ascii=False,indent=2))
 else:
  for x in issues:print("ERROR:",x)
  print("Icon curation:", "PASS" if not issues else "FAIL")
 return int(bool(issues))
if __name__=="__main__":raise SystemExit(main())
