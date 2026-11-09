#!/usr/bin/env python3
"""Static integrity checks for product-type routing and staged design review.

This validator checks the skill's authored contracts, not real UI quality.
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
TYPES = {
    "Admin / Operations",
    "Consumer Utility",
    "Learning / Education",
    "Content / Media",
    "Commerce",
    "Creative Tool",
    "Marketing / Portfolio",
}
MODES = {"Persuade", "Operate", "Read", "Experience"}
STAGES = ["R0", "R1", "R2", "R3", "R4", "R5"]


def validate(routes: dict, stages: dict) -> list[str]:
    errors: list[str] = []
    cases = routes.get("cases", [])
    if len(cases) < len(TYPES):
        errors.append("insufficient cross-product experience cases")
    seen: set[str] = set()
    types_seen: set[str] = set()
    for case in cases:
        cid = case.get("id", "")
        if not cid or cid in seen:
            errors.append("duplicate or empty case id")
        seen.add(cid)
        kind = case.get("product_type")
        types_seen.add(kind)
        if kind not in TYPES:
            errors.append(f"{cid}: invalid product type")
        if case.get("page_mode") not in MODES:
            errors.append(f"{cid}: invalid page mode")
        for field in ("audience", "user_job", "primary_action", "anti_pattern"):
            if not isinstance(case.get(field), str) or not case[field].strip():
                errors.append(f"{cid}: missing {field}")
        if len(case.get("priority_content", [])) < 2:
            errors.append(f"{cid}: too little task content")
        if case.get("requires_ux_restructure") and len(set(case.get("layout_directions", []))) < 2:
            errors.append(f"{cid}: structural failures require distinct layout directions")
    if not TYPES.issubset(types_seen):
        errors.append("missing product archetype")
    if not any(not c.get("requires_ux_restructure", True) for c in cases):
        errors.append("missing scoped-fix counterexample")

    if stages.get("order") != STAGES:
        errors.append("stage order must be R0-R5")
    gates = stages.get("gates", [])
    if [g.get("id") for g in gates] != STAGES:
        errors.append("gate list must match stage order")
    for gate in gates:
        if len(gate.get("must_check", [])) < 2 or not gate.get("stop_if"):
            errors.append(f"{gate.get('id')}: missing stage criteria")
    exceptions = stages.get("exceptions", [])
    decisions = {e.get("decision") for e in exceptions}
    for required in ("preserve_brand_expression", "allow_connected_zero_gap", "scoped_repair", "return_to_R1"):
        if required not in decisions:
            errors.append(f"missing exception: {required}")
    if not any(e.get("product_type") == "Learning / Education"
               and e.get("decision") == "return_to_R1" for e in exceptions):
        errors.append("missing learning-UX-first counterexample")
    if not any("emoji" in e.get("situation", "").lower()
               and e.get("decision") == "preserve_brand_expression" for e in exceptions):
        errors.append("no legitimate emoji-content exception")
    return errors


def validate_repo() -> list[str]:
    expected = [
        "references/product-experience-routing-gate.md",
        "references/progressive-visual-refinement-gate.md",
        "assets/product-experience-routes.json",
        "assets/refinement-stage-cases.json",
    ]
    errors = [f"missing file {p}" for p in expected if not (ROOT / p).is_file()]
    if errors:
        return errors
    routes = json.loads((ROOT / expected[2]).read_text(encoding="utf-8"))
    stages = json.loads((ROOT / expected[3]).read_text(encoding="utf-8"))
    errors.extend(validate(routes, stages))
    primary = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    for required in expected[:2]:
        if required not in primary:
            errors.append(f"SKILL.md missing routing link: {required}")
    return errors


if __name__ == "__main__":
    errors = validate_repo()
    for error in errors:
        print("ERROR:", error)
    print("Product experience routing errors:", len(errors))
    sys.exit(1 if errors else 0)
