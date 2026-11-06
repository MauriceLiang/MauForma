#!/usr/bin/env python3
"""Validate semantic spacing design decisions; no aesthetic/geometry verdict."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SAMPLE=ROOT/"assets/spacing-rhythm-patterns.json"
MODES={"Operate","Persuade","Read","Experience"}
RELATIONS={"inside","peer","section","connected","anchored","editorial"}
TOKENS={"inside","peer","section","page"}
REQUIRED=(
 "SKILL.md","references/semantic-spacing-rhythm-gate.md",
 "references/whitespace-and-surface-composition.md",
 "references/grid-alignment-and-viewport-safety.md",
 "assets/spacing-rhythm-patterns.json",
 "assets/spacing-rhythm-lab.html","assets/spacing-rhythm-lab-contract.json",
 "scripts/validate_spacing_rhythm.py","scripts/audit_spacing_rhythm.mjs",
 "tests/test_spacing_rhythm.py","tests/spacing_rhythm_browser_smoke.mjs",
 "references/spacing-regression-protection-gate.md",
 "scripts/audit_panel_spacing.mjs","tests/panel_spacing_browser_smoke.mjs"
)

def validate_plan(data:object,require_modes:bool=False)->list[str]:
    errors=[]
    if not isinstance(data,dict) or data.get("schema_version")!="1.0":
        return ["Invalid spacing plan version"]
    profiles=data.get("profiles")
    if not isinstance(profiles,list) or not profiles:return ["Missing spacing profiles"]
    names=set(); modes=set()
    for profile in profiles:
        if not isinstance(profile,dict):errors.append("Invalid spacing profile");continue
        name=profile.get("id")
        if not isinstance(name,str) or not name.strip() or name in names:errors.append("Profile id must be unique and nonempty")
        names.add(name)
        if profile.get("mode") not in MODES:errors.append(f"{name}: unsupported Web mode")
        else:modes.add(profile["mode"])
        if not isinstance(profile.get("goal"),str) or len(profile["goal"].strip())<20:
            errors.append(f"{name}: meaningful user goal required")
        tokens=profile.get("tokens")
        if not isinstance(tokens,dict) or not TOKENS.issubset(tokens):
            errors.append(f"{name}: need semantic inside/peer/section/page tokens")
            tokens={}
        else:
            for key,value in tokens.items():
                if not isinstance(value,str) or not value.strip():
                    errors.append(f"{name}: spacing token '{key}' must map to a project token")
        items=profile.get("relationships")
        if not isinstance(items,list) or not items:errors.append(f"{name}: no spacing relationships");continue
        ids=set()
        for item in items:
            if not isinstance(item,dict):errors.append(f"{name}: invalid relationship");continue
            ident=item.get("id")
            if not isinstance(ident,str) or not ident or ident in ids:
                errors.append(f"{name}: duplicate or missing relationship id")
            ids.add(ident)
            if not item.get("from") or not item.get("to") or item.get("from")==item.get("to"):
                errors.append(f"{name}/{ident}: need two distinct semantic regions")
            relation=item.get("relation")
            if relation not in RELATIONS:errors.append(f"{name}/{ident}: invalid relation")
            if relation in {"inside","peer","section"} and item.get("token")!=relation:
                errors.append(f"{name}/{ident}: relation must have matching semantic spacing token")
            if relation in {"connected","anchored"} and item.get("token") is not None:
                errors.append(f"{name}/{ident}: intentional connected/anchored must not force separation token")
            if not isinstance(item.get("reason"),str) or len(item["reason"].strip())<20:
                errors.append(f"{name}/{ident}: explain visual relationship or intentional adjacency")
    if require_modes and modes!=MODES:errors.append("Need cases across all four Web modes")
    return errors

def validate_repository()->list[str]:
    issues=[f"Missing required resource: {p}" for p in REQUIRED if not (ROOT/p).is_file()]
    if issues:return issues
    skill=(ROOT/"SKILL.md").read_text("utf-8")
    for name in ("semantic-spacing-rhythm-gate.md","validate_spacing_rhythm.py","audit_spacing_rhythm.mjs","spacing-regression-protection-gate.md","audit_panel_spacing.mjs"):
        if name not in skill:issues.append(f"SKILL.md missing spacing gate route: {name}")
    try:issues.extend(validate_plan(json.loads(SAMPLE.read_text("utf-8")),require_modes=True))
    except (OSError,ValueError) as e:issues.append(str(e))
    return issues

def main()->int:
    parser=argparse.ArgumentParser(description="Validate semantic spacing/visual rhythm design contracts")
    parser.add_argument("path",nargs="?",type=Path)
    parser.add_argument("--repository",action="store_true")
    parser.add_argument("--json",action="store_true")
    args=parser.parse_args()
    if args.path is None and not args.repository:parser.error("Give plan JSON or --repository")
    issues=validate_repository() if args.repository else []
    if args.path:
        try:issues.extend(validate_plan(json.loads(args.path.read_text("utf-8"))))
        except (OSError,ValueError) as e:issues.append(str(e))
    if args.json:
        print(json.dumps({"passed":not issues,"issues":issues,"scope":"static semantic design decision only; no visual quality or browser proof"},ensure_ascii=False,indent=2))
    else:
        for e in issues:print("ERROR:",e)
        print("Spacing contract:","PASS" if not issues else "FAIL")
    return int(bool(issues))
if __name__=="__main__":raise SystemExit(main())
