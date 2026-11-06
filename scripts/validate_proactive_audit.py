#!/usr/bin/env python3
"""Check that a vague UI optimization prompt routes to defect-first assessment."""
from __future__ import annotations
import argparse,json
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
FILE=ROOT/"assets/proactive-audit-trigger-cases.json"
MODES={"Operate","Persuade","Read","Experience"}
FULL={"spacing","typography","component-fit","icons-color","states-responsive"}
PATHS={"discover-repair-verify","scoped-diagnose-repair-verify","scoped-functional-fix","diagnose-report-only"}
REQUIRED=[
 "SKILL.md","references/proactive-visual-defect-discovery-gate.md",
 "assets/proactive-audit-trigger-cases.json","scripts/validate_proactive_audit.py",
 "scripts/audit_existing_visual_defects.mjs","tests/test_proactive_audit.py",
 "tests/existing_visual_defect_browser_smoke.mjs"
]
def validate(data,require_all=False):
 errors=[]
 if not isinstance(data,dict) or data.get("schema_version")!="1.0":return ["Wrong schema version"]
 cases=data.get("cases",[])
 if not isinstance(cases,list) or not cases:return ["No intent/flow examples"]
 ids=set();modes=set();paths=set()
 for case in cases:
  if not isinstance(case,dict):errors.append("Invalid case");continue
  name=case.get("id")
  if not isinstance(name,str) or not name or name in ids:errors.append("Missing/duplicate case id")
  ids.add(name)
  mode=case.get("mode");flow=case.get("expected_path")
  if mode not in MODES:errors.append(f"{name}: invalid Web mode")
  else:modes.add(mode)
  if flow not in PATHS:errors.append(f"{name}: invalid expected path")
  else:paths.add(flow)
  if not isinstance(case.get("prompt"),str) or len(case["prompt"])<8:errors.append(f"{name}: realistic prompt required")
  if not isinstance(case.get("reason"),str) or len(case["reason"])<25:errors.append(f"{name}: meaningful reasoning required")
  scans=case.get("scan")
  if not isinstance(scans,list) or not scans or any(x not in FULL for x in scans):
   errors.append(f"{name}: unsupported scan dimension")
  if flow=="discover-repair-verify" and set(scans or [])!=FULL:
   errors.append(f"{name}: vague optimization must trigger full visual defect discovery")
  if flow=="diagnose-report-only" and "fix" in case:
   errors.append(f"{name}: analysis-only must not claim code modifications")
 if require_all:
  if modes!=MODES:errors.append("Need four Web modes")
  if paths!=PATHS:errors.append("Need vague, focused, functional and analysis-only paths")
 return errors
def validate_repo():
 missing=[f"Missing artifact: {p}" for p in REQUIRED if not (ROOT/p).is_file()]
 if missing:return missing
 s=(ROOT/"SKILL.md").read_text("utf-8")
 for needle in ("proactive-visual-defect-discovery-gate.md","audit_existing_visual_defects.mjs","validate_proactive_audit.py"):
  if needle not in s:missing.append("SKILL.md missing proactive audit link: "+needle)
 try:missing.extend(validate(json.loads(FILE.read_text("utf-8")),require_all=True))
 except (OSError,ValueError) as err:missing.append(str(err))
 return missing
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument("file",type=Path,nargs="?")
 ap.add_argument("--repository",action="store_true")
 args=ap.parse_args()
 if not args.file and not args.repository:ap.error("Use --repository or case JSON file")
 issues=validate_repo() if args.repository else []
 if args.file:issues.extend(validate(json.loads(args.file.read_text("utf-8"))))
 for issue in issues:print("ERROR:",issue)
 print("Proactive audit intent contracts:","FAIL" if issues else "PASS")
 return int(bool(issues))
if __name__=="__main__":raise SystemExit(main())
