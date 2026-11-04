#!/usr/bin/env python3
"""Validate component motion plans, not actual animation quality."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SAMPLE=ROOT/"assets/component-motion-patterns.json"
MODES={"Operate","Persuade","Read","Experience"}
LEVELS={"none","balanced","expressive"}
SOURCES={"confirmed","delegated","inherited","unresolved"}
TREATMENTS={"motion","feedback","static"}
MECHANISMS={"none","indicator-travel","spatial-reveal","state-morph","layout-continuity","semantic-feedback","media-crossfade","depth-shift","shared-element","tactile-press","fade","page-transition","custom"}
REQUIRED=(
    "SKILL.md","references/component-motion-choreography-gate.md",
    "references/motion-consent-experience-gate.md",
    "assets/component-motion-patterns.json","assets/component-motion-lab.html",
    "scripts/validate_component_motion.py","tests/test_component_motion.py",
    "tests/component_motion_browser_smoke.mjs",
)

def validate_plan(data:object,require_modes:bool=False)->list[str]:
    errors=[]
    if not isinstance(data,dict) or data.get("schema_version")!="1.0":
        return ["Unsupported component motion plan version"]
    profiles=data.get("profiles")
    if not isinstance(profiles,list) or not profiles:return ["Missing motion profiles"]
    modes=set();ids=set()
    for profile in profiles:
        if not isinstance(profile,dict):
            errors.append("Invalid profile");continue
        name=profile.get("id")
        if not isinstance(name,str) or not name.strip() or name in ids:errors.append("Profile IDs must be distinct")
        ids.add(name)
        if profile.get("mode") not in MODES:errors.append(f"{name}: unknown Web mode")
        else:modes.add(profile["mode"])
        level=profile.get("motion_level")
        source=profile.get("user_choice_source")
        if level not in LEVELS:errors.append(f"{name}: unresolved motion selection may not silently become none")
        if source not in SOURCES or source=="unresolved":errors.append(f"{name}: selected level needs a known user choice provenance")
        items=profile.get("interactions")
        if not isinstance(items,list) or not items:
            errors.append(f"{name}: component inventory required");continue
        seen=set();component_motion=[];high_eligible=[];all_motions=[]
        for i in items:
            if not isinstance(i,dict):errors.append(f"{name}: invalid interaction");continue
            key=i.get("id")
            if not key or key in seen:errors.append(f"{name}: duplicate or missing interaction id")
            seen.add(key)
            treatment=i.get("mode"); mechanism=i.get("mechanism")
            if treatment not in TREATMENTS or mechanism not in MECHANISMS:errors.append(f"{name}/{key}: invalid treatment or mechanism")
            if not all(isinstance(i.get(k),str) and i[k].strip() for k in ("component","trigger","purpose","priority","alternative")):
                errors.append(f"{name}/{key}: missing component role, trigger, purpose, priority or no-motion alternative")
            if i.get("priority") not in {"high","medium","low"}:errors.append(f"{name}/{key}: invalid priority")
            if treatment=="motion":
                if mechanism=="none":errors.append(f"{name}/{key}: motion missing real mechanism")
                if level=="none":errors.append(f"{name}/{key}: explicitly none policy cannot add optional motion")
                all_motions.append(i)
                if i.get("component")!="page":component_motion.append(i)
            if treatment in {"static","feedback"}:
                if mechanism!="none":errors.append(f"{name}/{key}: static/feedback must not claim animation mechanism")
                if not i.get("reason"):errors.append(f"{name}/{key}: explain intentionally non-animated behavior")
            if i.get("priority")=="high" and i.get("component")!="page" and treatment!="static":
                high_eligible.append(i)
        if level in {"balanced","expressive"}:
            if not component_motion:errors.append(f"{name}: page-only motion does not count as component coverage")
            if len(high_eligible)>=2 and not any(x in component_motion and x.get("priority")=="high" for x in high_eligible):
                errors.append(f"{name}: high-value components lack interactive motion")
            # Restrict repeating fade when several components were chosen for animation.
            if len(component_motion)>=3:
                distinct={x.get("mechanism") for x in component_motion}
                if len(distinct)<2 or distinct=={"fade"}:
                    errors.append(f"{name}: generic single-mechanism motion for many components")
        if level=="none" and all_motions:
            errors.append(f"{name}: none policy must remain feedback-only")
    if require_modes and modes!=MODES:errors.append("Catalog must demonstrate four Web modes")
    return errors

def validate_repository()->list[str]:
    issues=[f"Missing artifact: {p}" for p in REQUIRED if not (ROOT/p).is_file()]
    if issues:return issues
    skill=(ROOT/"SKILL.md").read_text("utf-8")
    for link in ("component-motion-choreography-gate.md","validate_component_motion.py"):
        if link not in skill:issues.append("Missing main Skill route: "+link)
    try:issues.extend(validate_plan(json.loads(SAMPLE.read_text("utf-8")),require_modes=True))
    except (OSError,ValueError) as e:issues.append(str(e))
    return issues

def main()->int:
    p=argparse.ArgumentParser(description="Check component motion coverage and mechanisms")
    p.add_argument("file",type=Path,nargs="?")
    p.add_argument("--repository",action="store_true")
    p.add_argument("--json",action="store_true")
    a=p.parse_args()
    if not a.repository and not a.file:p.error("Provide plan file or --repository")
    issues=validate_repository() if a.repository else []
    if a.file:
        try:issues.extend(validate_plan(json.loads(a.file.read_text("utf-8"))))
        except (OSError,ValueError) as e:issues.append(str(e))
    if a.json:print(json.dumps({"passed":not issues,"issues":issues,"scope":"static design-intent inventory only, not visual motion proof"},ensure_ascii=False,indent=2))
    else:
        for issue in issues:print("ERROR:",issue)
        print("Component motion plan:","PASS" if not issues else "FAIL")
    return int(bool(issues))

if __name__=="__main__":raise SystemExit(main())
