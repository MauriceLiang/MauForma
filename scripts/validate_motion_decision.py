#!/usr/bin/env python3
"""Validate motion decision provenance and experience coverage, NOT visual quality."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
EXAMPLE=ROOT/"assets/motion-decision-patterns.json"
MODES={"Operate","Persuade","Read","Experience"}
SOURCES={"confirmed","delegated","inherited","unresolved"}
LEVELS={"none","balanced","expressive"}
BASELINE={"focus-visible","selected","outcome-feedback"}
REQUIRED_FILES=(
"SKILL.md","references/motion-consent-experience-gate.md",
"references/design-discovery-interview.md","references/animation-engine-selection.md",
"references/visual-qa.md","assets/motion-decision-patterns.json",
"assets/motion-choice-layout-lab.html","scripts/validate_motion_decision.py",
"tests/test_motion_decision.py","tests/motion_choice_browser_smoke.mjs"
)

def validate_plan(data:object, require_modes:bool=False)->list[str]:
    errors=[]
    if not isinstance(data,dict) or data.get("schema_version")!="1.0":
        return ["Unsupported motion decision plan version"]
    profiles=data.get("profiles")
    if not isinstance(profiles,list) or not profiles:return ["Missing page profiles"]
    modes=set(); ids=set()
    for p in profiles:
        if not isinstance(p,dict):errors.append("Invalid profile");continue
        pid=p.get("id")
        if not isinstance(pid,str) or not pid.strip() or pid in ids:errors.append("Profile id must be unique and non-empty")
        ids.add(pid)
        if p.get("mode") not in MODES:errors.append(f"{pid}: invalid mode")
        else:modes.add(p["mode"])
        if not isinstance(p.get("goal"),str) or len(p["goal"].strip())<12:errors.append(f"{pid}: need actual user goal")
        stage=p.get("project_stage")
        if stage not in {"new-site","major-redesign","minor-fix","existing-feature"}:errors.append(f"{pid}: invalid stage")
        d=p.get("decision")
        if not isinstance(d,dict):errors.append(f"{pid}: no motion decision");continue
        source=d.get("source");level=d.get("level")
        if source not in SOURCES:errors.append(f"{pid}: invalid decision source")
        if source=="unresolved":
            if level is not None:errors.append(f"{pid}: unresolved motion cannot silently select a level")
            if d.get("optional_motion_started") is not False:errors.append(f"{pid}: unresolved motion cannot start optional effects")
            if stage in {"new-site","major-redesign"}:
                if d.get("question_asked") is not True:errors.append(f"{pid}: new/major design requires user-facing motion choice")
                options=d.get("proposals",[])
                if not isinstance(options,list) or len(options) not in {2,3}:errors.append(f"{pid}: ask with two or three concrete motion alternatives")
                else:
                    levels=[x.get("level") for x in options if isinstance(x,dict)]
                    if len(levels)!=len(set(levels)) or any(x not in LEVELS for x in levels):errors.append(f"{pid}: options need distinct legitimate motion levels")
                    for o in options:
                        if not isinstance(o,dict) or len(str(o.get("preview","")).strip())<18 or len(str(o.get("tradeoff","")).strip())<12:
                            errors.append(f"{pid}: each motion option needs visible behavior and tradeoff")
        else:
            if level not in LEVELS:errors.append(f"{pid}: selected motion must use valid level")
            if source in {"confirmed","delegated"} and (not isinstance(d.get("user_evidence"),str) or len(d["user_evidence"].strip())<8):
                errors.append(f"{pid}: selection/authorization must cite user's explicit statement")
            if source=="inherited" and not d.get("inherited_from"):errors.append(f"{pid}: inherited motion requires named policy")
            if level=="none" and d.get("optional_motion_started") is True:errors.append(f"{pid}: none policy cannot start optional motion")
            if level in {"balanced","expressive"} and d.get("optional_motion_started") is not True:
                errors.append(f"{pid}: chosen effects missing implementation contract")
        if not isinstance(d.get("rationale"),str) or not d["rationale"].strip():
            errors.append(f"{pid}: record decision rationale")
        if not isinstance(p.get("feedback_baseline"),list) or not BASELINE.issubset(set(p["feedback_baseline"])):
            errors.append(f"{pid}: motion policy cannot remove essential visible feedback")
        interactions=p.get("interactions")
        if not isinstance(interactions,list) or not interactions:errors.append(f"{pid}: enumerate real interactive state changes");continue
        seen=set()
        for item in interactions:
            if not isinstance(item,dict):errors.append(f"{pid}: malformed interaction");continue
            ident=item.get("id")
            if not ident or ident in seen:errors.append(f"{pid}: duplicate/missing interaction id")
            seen.add(ident)
            if not all(isinstance(item.get(key),str) and item[key].strip() for key in ("kind","purpose","effect","reduced_motion")):
                errors.append(f"{pid}/{ident}: missing purpose/effect/reduced-motion state")
            if item.get("interruptible") is not True:errors.append(f"{pid}/{ident}: motion must remain interruptible")
            if source=="unresolved" and item.get("effect")!="unresolved":
                errors.append(f"{pid}/{ident}: unresolved preference must not silently implement optional effect")
            if level=="none" and item.get("effect")!="none":
                errors.append(f"{pid}/{ident}: none policy must not add optional motion")
    if require_modes and modes!=MODES:errors.append("Reference plans must cover all four Web page modes")
    return errors

def validate_repository()->list[str]:
    issues=[f"Missing motion artifact: {p}" for p in REQUIRED_FILES if not (ROOT/p).is_file()]
    if issues:return issues
    skill=(ROOT/"SKILL.md").read_text("utf-8")
    for name in ("motion-consent-experience-gate.md","validate_motion_decision.py"):
        if name not in skill:issues.append("SKILL.md lacks mandatory motion route: "+name)
    try:issues.extend(validate_plan(json.loads(EXAMPLE.read_text("utf-8")),require_modes=True))
    except (ValueError,OSError) as e:issues.append(str(e))
    return issues

def main()->int:
    p=argparse.ArgumentParser(description="Check motion decision provenance and effect contracts; static only")
    p.add_argument("file",nargs="?",type=Path)
    p.add_argument("--repository",action="store_true")
    p.add_argument("--json",action="store_true")
    a=p.parse_args()
    if a.file is None and not a.repository:p.error("Specify file or --repository")
    issues=validate_repository() if a.repository else []
    if a.file:
        try:issues.extend(validate_plan(json.loads(a.file.read_text("utf-8"))))
        except (ValueError,OSError) as e:issues.append(str(e))
    if a.json:print(json.dumps({"passed":not issues,"issues":issues,"scope":"static decision/coverage only, not actual motion QA"},ensure_ascii=False,indent=2))
    else:
        for issue in issues:print("ERROR:",issue)
        print("Motion choice decision:", "PASS" if not issues else "FAIL")
    return int(bool(issues))

if __name__=="__main__":raise SystemExit(main())
