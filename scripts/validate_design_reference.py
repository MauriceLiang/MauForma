#!/usr/bin/env python3
"""Validate abstract, original design reference learning examples and publication boundaries.

This catches declared policy violations and image media accidentally placed in NEW public
example directories. It cannot prove that a page contains no sensitive semantics.
"""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CATALOG=ROOT/"examples/design-reference-learning/reference-principles.json"
DEMO=ROOT/"examples/clean-enterprise-demo/index.html"
DEMO_DIR=DEMO.parent
EXAMPLE_DIR=CATALOG.parent
MODES={"Operate","Persuade","Read","Experience"}
ROLES={"navigation","selection","data-density","color","typography","surface","icons","spacing","motion","feedback"}
FIELDS=("role","observed_trait","visual_effect","task_benefit","applicable_context","tradeoff","transfer_rule","avoid_copying")
FORBIDDEN_MEDIA={".png",".jpg",".jpeg",".webp",".gif",".heic",".bmp",".tif",".tiff",".pdf",".mp4",".mov",".avif",".svg"}
REQUIRED=(
 "SKILL.md","references/design-reference-learning-gate.md",
 "references/clean-enterprise-design.md",
 "examples/design-reference-learning/reference-principles.json",
 "examples/clean-enterprise-demo/index.html",
 "examples/clean-enterprise-demo/element-plus-icons-license.txt",
 "scripts/validate_design_reference.py",
 "tests/test_design_reference.py",
 "tests/design_reference_browser_smoke.mjs"
)

def validate_catalog(data:object,all_modes:bool=False)->list[str]:
    issues=[]
    if not isinstance(data,dict) or data.get("schema_version")!="1.0":
        return ["Unsupported reference-learning catalog version"]
    if data.get("publication_policy")!="synthesized-principles-only":
        issues.append("Public catalog must contain synthesized design principles only")
    if data.get("public_reference_media_allowed") is not False:
        issues.append("Public reference media is forbidden by this catalog policy")
    profiles=data.get("profiles")
    if not isinstance(profiles,list) or not profiles:return issues+["Missing cross-domain profiles"]
    ids=set(); modes=set()
    for p in profiles:
        if not isinstance(p,dict):issues.append("Invalid profile");continue
        pid=p.get("id")
        if not isinstance(pid,str) or not pid or pid in ids:issues.append("Profiles need unique nonempty ids")
        ids.add(pid)
        if p.get("mode") not in MODES:issues.append(f"{pid}: unsupported Web mode")
        else:modes.add(p["mode"])
        if not isinstance(p.get("goal"),str) or len(p["goal"].strip())<12:issues.append(f"{pid}: missing user task")
        insights=p.get("insights")
        if not isinstance(insights,list) or len(insights)<2:issues.append(f"{pid}: at least two transferable insights");continue
        for i in insights:
            if not isinstance(i,dict):issues.append(f"{pid}: invalid insight");continue
            role=i.get("role")
            if role not in ROLES:issues.append(f"{pid}: unsupported design dimension")
            for field in FIELDS[1:]:
                v=i.get(field)
                if not isinstance(v,str) or len(v.strip())<18:
                    issues.append(f"{pid}/{role}: require contextual {field}, not raw style copying")
    if all_modes and modes!=MODES:issues.append("Must cover all four Web product modes")
    demo=data.get("demo")
    if not isinstance(demo,dict):issues.append("Missing independent fictional demo")
    else:
        if demo.get("source_provenance")!="synthetic":
            issues.append("Public demo must be genuinely synthetic, not converted reference media")
        if demo.get("image_policy")!="none":
            issues.append("Public demo must not publish supplied reference images or image variants")
        if len(demo.get("transfer_focus",[]))<3:
            issues.append("Demo must state several transferable design principles")
        if len(demo.get("intentionally_different",[]))<3:
            issues.append("Demo must show independent composition, terminology and data")
    return issues

def validate_public_example_files()->list[str]:
    issues=[]
    for folder in (DEMO_DIR,EXAMPLE_DIR):
        if not folder.exists():continue
        for p in folder.rglob("*"):
            if not p.is_file():continue
            if p.suffix.lower() in FORBIDDEN_MEDIA:
                issues.append(f"Public example includes prohibited media file: {p.relative_to(ROOT)}")
            if p.suffix.lower() in {".html",".css",".js",".json",".md"}:
                t=p.read_text("utf-8")
                if re.search(r"data:image/|<img\b|<picture\b|<canvas\b",t,re.IGNORECASE):
                    issues.append(f"Unexpected embedded/imported image media in example: {p.relative_to(ROOT)}")
    return issues

def validate_repository()->list[str]:
    issues=[f"Missing design-reference resource: {p}" for p in REQUIRED if not (ROOT/p).is_file()]
    if issues:return issues
    skill=(ROOT/"SKILL.md").read_text("utf-8")
    for needle in ("design-reference-learning-gate.md","clean-enterprise-design.md","validate_design_reference.py"):
        if needle not in skill:issues.append("Main Skill missing reference learning route: "+needle)
    try:issues.extend(validate_catalog(json.loads(CATALOG.read_text("utf-8")),all_modes=True))
    except (OSError,ValueError) as e:issues.append(str(e))
    issues.extend(validate_public_example_files())
    html=DEMO.read_text("utf-8")
    if 'data-demo-source="synthetic"' not in html:
        issues.append("Original fictional demo provenance marker absent")
    license=(DEMO_DIR/"element-plus-icons-license.txt").read_text("utf-8")
    if "MIT License" not in license or "Element Plus" not in license:
        issues.append("Embedded open-source icons require their actual license")
    return issues

def main()->int:
    a=argparse.ArgumentParser(description="Validate abstract reference-learning contracts and public example media guard")
    a.add_argument("file",nargs="?",type=Path)
    a.add_argument("--repository",action="store_true")
    a.add_argument("--json",action="store_true")
    args=a.parse_args()
    if not args.repository and not args.file:a.error("Provide JSON catalog or --repository")
    issues=validate_repository() if args.repository else []
    if args.file:
        try:issues.extend(validate_catalog(json.loads(args.file.read_text("utf-8"))))
        except (OSError,ValueError) as e:issues.append(str(e))
    if args.json:
        print(json.dumps({"passed":not issues,"issues":issues,"scope":"static contract/media check, not privacy guarantee or visual aesthetics proof"},ensure_ascii=False,indent=2))
    else:
        for e in issues:print("ERROR:",e)
        print("Design reference learning:", "PASS" if not issues else "FAIL")
    return int(bool(issues))

if __name__=="__main__":raise SystemExit(main())
