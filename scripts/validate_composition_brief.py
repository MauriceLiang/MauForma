#!/usr/bin/env python3
"""MauForma composition-brief semantic validator (standard library only).

Checks evidence references, meaningful alternatives and selected-state provenance.
Passing this script is NOT proof of visual beauty, correct live data, or browser QA.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DEFAULT = ROOT / "examples/composition/repo-analysis.json"
MODES = {"Persuade", "Operate", "Read", "Experience"}
SOURCES = {"confirmed", "delegated", "inherited", "unresolved"}
STATUSES = {"known", "demo", "unverified"}
ROLES = {"context", "primary", "secondary", "control", "evidence", "decorative"}


def validate_brief(data: dict) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict):
        return ["Brief root must be an object"]
    if data.get("schema_version") != "1.0":
        errors.append("Unsupported composition brief schema_version")
    page = data.get("page", {})
    if not isinstance(page, dict) or page.get("mode") not in MODES:
        errors.append("page.mode must be a visitor-task mode")
        return errors
    if not str(page.get("primary_task", "")).strip() or not str(page.get("first_question", "")).strip():
        errors.append("page requires a real primary_task and first_question")
    inventory = page.get("content_inventory", [])
    if not isinstance(inventory, list) or len(inventory) < 2:
        errors.append("page requires at least two content records")
        return errors
    ids = [item.get("id") for item in inventory if isinstance(item, dict)]
    if len(ids) != len(inventory) or any(not x for x in ids) or len(set(ids)) != len(ids):
        errors.append("Content inventory IDs must be present and unique")
    content_map = {x["id"]: x for x in inventory if isinstance(x, dict) and x.get("id")}
    for item in inventory:
        if not isinstance(item, dict) or item.get("status") not in STATUSES:
            errors.append("Every content item must have known/demo/unverified status")
    candidates = data.get("candidates", [])
    if not isinstance(candidates, list) or not 2 <= len(candidates) <= 3:
        errors.append("New/major layout proposals must have 2–3 candidates")
        return errors
    candidate_ids = [x.get("id") for x in candidates if isinstance(x, dict)]
    if len(candidate_ids) != len(candidates) or any(not x for x in candidate_ids) or len(set(candidate_ids)) != len(candidate_ids):
        errors.append("Candidate IDs must be present and unique")
    signatures = []
    for candidate in candidates:
        if not isinstance(candidate, dict):
            errors.append("Candidate must be an object")
            continue
        key = candidate.get("id", "<unknown>")
        palette = candidate.get("palette", {})
        if not isinstance(palette, dict) or palette.get("source") not in SOURCES or len(str(palette.get("rationale", "")).strip()) < 15:
            errors.append(f"{key}: palette needs a sourced, content-grounded rationale")
        for name in ("archetype", "strength", "tradeoff", "why"):
            if not str(candidate.get(name, "")).strip():
                errors.append(f"{key}: missing {name}")
        regions = candidate.get("regions", [])
        if not isinstance(regions, list) or len(regions) < 3:
            errors.append(f"{key}: need at least three described regions")
            continue
        region_by_id = {}
        for region in regions:
            if not isinstance(region, dict) or not region.get("id"):
                errors.append(f"{key}: region missing id")
                continue
            rid = region["id"]
            if rid in region_by_id:
                errors.append(f"{key}: duplicate region {rid}")
            region_by_id[rid] = region
            role = region.get("role")
            if role not in ROLES:
                errors.append(f"{key}: invalid role for {rid}")
            content_ids = region.get("content_ids", [])
            if not isinstance(content_ids, list):
                errors.append(f"{key}: {rid} content_ids must be a list")
                continue
            if not content_ids and role != "decorative":
                errors.append(f"{key}: {rid} has no information content")
            for cid in content_ids:
                if cid not in content_map:
                    errors.append(f"{key}: {rid} references unknown content {cid}")
                elif content_map[cid]["status"] == "unverified" and role in {"primary", "evidence"}:
                    if not str(region.get("state_strategy", "")).strip():
                        errors.append(f"{key}: {rid} uses unverified data but has no loading/empty/error plan")
        focal = candidate.get("primary_region")
        if focal not in region_by_id or region_by_id[focal].get("role") != "primary":
            errors.append(f"{key}: primary_region must refer to a primary role")
        first = candidate.get("first_screen", [])
        if not isinstance(first, list) or not first:
            errors.append(f"{key}: first_screen must specify visible regions")
            continue
        if any(rid not in region_by_id for rid in first):
            errors.append(f"{key}: first_screen references missing region")
        if focal not in first:
            errors.append(f"{key}: first screen omits primary region {focal}")
        if page["mode"] == "Operate" and focal in region_by_id and region_by_id[focal].get("role") == "decorative":
            errors.append(f"{key}: an Operate page cannot use decoration as its main task")
        # Compare content structure, not arbitrary region IDs or palette names.
        signatures.append(tuple(
            (region_by_id[rid].get("role"), tuple(sorted(region_by_id[rid].get("content_ids", []))))
            for rid in first if rid in region_by_id
        ))
        if candidate.get("mobile_order"):
            mobile = candidate["mobile_order"]
            if not isinstance(mobile, list) or any(rid not in region_by_id for rid in mobile):
                errors.append(f"{key}: mobile_order must contain valid region IDs")
    if len(signatures) != len(set(signatures)):
        errors.append("Candidates duplicate the same first-screen structure; colors/text alone are not alternatives")
    comparison = data.get("comparison", {})
    if not isinstance(comparison, dict) or comparison.get("recommended_id") not in candidate_ids:
        errors.append("comparison.recommended_id must match a candidate")
        comparison = {}
    selection = comparison.get("selection", {})
    if not isinstance(selection, dict) or selection.get("source") not in SOURCES:
        errors.append("comparison.selection has invalid provenance")
    else:
        chosen = selection.get("id")
        source = selection.get("source")
        if chosen is not None and chosen not in candidate_ids:
            errors.append("Selected candidate does not exist")
        if chosen is None and source != "unresolved":
            errors.append("Selection cannot be marked confirmed/delegated/inherited without an ID")
        if chosen is not None and source == "unresolved":
            errors.append("A selected layout needs a confirmed/delegated/inherited source")
    if len(comparison.get("structural_differences", [])) < 2:
        errors.append("State at least two meaningful structural distinctions")
    review = data.get("review", {})
    if not isinstance(review, dict):
        errors.append("review must be an object")
        return errors
    decoration = review.get("decoration_removed_test", {})
    if not isinstance(decoration, dict) or decoration.get("passes") is not True or not str(decoration.get("reason", "")).strip():
        errors.append("Decoration-removed test must pass and explain why structure still works")
    if review.get("first_screen_task_visible") is not True:
        errors.append("The first screen must support the main visitor task")
    if not str(review.get("data_states", "")).strip():
        errors.append("Describe loading, empty and demo/real data states")
    browser = review.get("browser_status")
    if browser not in {"PASS", "FAIL", "NOT RUN"}:
        errors.append("browser_status must be PASS / FAIL / NOT RUN")
    if browser == "PASS" and not str(review.get("evidence", "")).strip():
        errors.append("Browser PASS requires actual evidence")
    return errors


def validate_repository() -> list[str]:
    paths = (
        "assets/composition-brief.schema.json",
        "examples/composition/repo-analysis.json",
        "references/composition-first-design.md",
        "references/palette-art-direction.md",
        "references/visual-critique-loop.md",
        "scripts/validate_composition_brief.py",
        "tests/test_composition_brief.py",
    )
    errors = [f"Missing composition reference: {path}" for path in paths if not (ROOT / path).is_file()]
    try:
        schema = json.loads((ROOT / paths[0]).read_text("utf-8"))
        if schema.get("properties", {}).get("candidates", {}).get("minItems") != 2:
            errors.append("Composition schema lacks layout diversity requirement")
        brief = json.loads((ROOT / paths[1]).read_text("utf-8"))
        errors += validate_brief(brief)
    except (OSError, ValueError) as exc:
        errors.append(f"Composition data not readable: {exc}")
    skill = (ROOT / "SKILL.md").read_text("utf-8")
    for keyword in ("composition-first-design.md", "palette-art-direction.md", "visual-critique-loop.md"):
        if keyword not in skill:
            errors.append(f"SKILL.md missing composition task route: {keyword}")
    return errors


def main() -> int:
    p = argparse.ArgumentParser(description="Audit a content-first composition brief, not visual taste")
    p.add_argument("brief", nargs="?", type=Path, default=DEFAULT)
    p.add_argument("--repository", action="store_true", help="Also verify references and Skill routing")
    p.add_argument("--json", action="store_true", help="Machine-readable error list")
    args = p.parse_args()
    try:
        data = json.loads(args.brief.read_text(encoding="utf-8"))
        errors = validate_brief(data)
        if args.repository:
            errors += validate_repository()
    except (OSError, ValueError) as exc:
        errors = [f"Failed to load brief: {exc}"]
    if args.json:
        print(json.dumps({"passed": not errors, "errors": errors, "scope": "structural checks only, not aesthetic or browser validation"}, ensure_ascii=False, indent=2))
    else:
        for error in errors:
            print("ERROR:", error)
        print("Composition brief:", "PASS" if not errors else "FAIL")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
