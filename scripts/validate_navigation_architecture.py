#!/usr/bin/env python3
"""Navigation architecture / user-choice validator for MauForma v6.7.

Static checks verify source provenance, known navigation patterns, route-ID
preservation and responsive decisions. They cannot prove usability or browser QA.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "assets/navigation-pattern-catalog.json"
EXAMPLE = ROOT / "examples/navigation-decision.pending.json"
REFERENCES = (
    "references/navigation-architecture.md",
    "assets/navigation-pattern-catalog.json",
    "assets/navigation-decision.schema.json",
    "assets/navigation-layout-lab.html",
    "examples/navigation-decision.pending.json",
    "scripts/validate_navigation_architecture.py",
    "tests/test_navigation_architecture.py",
)
NAV_MODES = {"top", "side", "top-side", "rail-split", "bottom",
             "bottom-drawer", "drawer", "top-drawer", "top-bottom",
             "stack", "focus", "side-bottom-tools", "drawer-bottom-tools"}


def validate_catalog(data: dict | None = None) -> list[str]:
    errors = []
    if data is None:
        try:
            data = json.loads(CATALOG.read_text("utf-8"))
        except (OSError, ValueError) as exc:
            return [f"Cannot read navigation patterns: {exc}"]
    references = data.get("references", [])
    patterns = data.get("patterns", [])
    ref_ids = [r.get("id") for r in references if isinstance(r, dict)]
    pids = [p.get("id") for p in patterns if isinstance(p, dict)]
    if len(references) < 6 or None in ref_ids or len(ref_ids) != len(set(ref_ids)):
        errors.append("Need distinct official references for navigation architecture")
    if len(patterns) < 8 or None in pids or len(pids) != len(set(pids)):
        errors.append("Need distinct, identified navigation architecture patterns")
    for ref in references:
        if not isinstance(ref, dict):
            errors.append("Malformed reference")
            continue
        if not str(ref.get("url", "")).startswith("https://"):
            errors.append(f"{ref.get('id')}: reference URL must be HTTPS")
        if not ref.get("lesson") or not ref.get("limit"):
            errors.append(f"{ref.get('id')}: source must state lesson AND limit")
    for p in patterns:
        if not isinstance(p, dict):
            errors.append("Malformed pattern")
            continue
        pid = p.get("id", "?")
        if not p.get("zones") or not p.get("best_for") or not p.get("why") or not p.get("tradeoff"):
            errors.append(f"{pid}: pattern needs zones, fit, rationale, tradeoff")
        if not set(p.get("reference_ids", [])).issubset(ref_ids):
            errors.append(f"{pid}: unknown official reference")
        if p.get("desktop") not in NAV_MODES or p.get("mobile") not in NAV_MODES:
            errors.append(f"{pid}: unsupported navigation mode")
        if pid == "side-bottom-tools" and "bottom-action-bar" not in p.get("zones", []):
            errors.append("Side + bottom utility is an action bar, not a second primary nav")
    rules = data.get("device_rules", {})
    if rules.get("bottom_primary_heuristic_max") != 5:
        errors.append("Bottom nav must describe the compact 3–5 destination guideline")
    if rules.get("do_not_duplicate_same_primary_destinations_in_one_viewport") is not True:
        errors.append("Same-level nav destinations must not be duplicated in one viewport")
    if rules.get("nav_and_actions_are_distinct") is not True:
        errors.append("Navigation and contextual actions must be distinct")
    return errors


def validate_decision(doc: dict, catalog: dict | None = None) -> list[str]:
    errors = []
    if catalog is None:
        catalog = json.loads(CATALOG.read_text("utf-8"))
    if not isinstance(doc, dict) or doc.get("schema_version") != "1.0":
        return ["Invalid navigation decision schema version"]
    patterns = {p["id"] for p in catalog["patterns"]}
    destinations = doc.get("primary_destinations", [])
    if not isinstance(destinations, list) or not destinations:
        return ["Need actual top-level destination inventory"]
    ids = [d.get("id") for d in destinations if isinstance(d, dict)]
    if len(ids) != len(destinations) or None in ids or len(set(ids)) != len(ids):
        errors.append("Primary destination IDs missing or duplicated")
    dest_set = set(ids)
    context = doc.get("context", {})
    if not isinstance(context, dict) or not context.get("task") or context.get("hierarchy_depth", 0) < 1:
        errors.append("Missing task/hierarchy discovery")
    candidates = doc.get("candidates", [])
    if not isinstance(candidates, list) or not 1 <= len(candidates) <= 3:
        errors.append("Recommend 1–3 relevant architecture alternatives")
        candidates = []
    candidate_ids = [c.get("pattern_id") for c in candidates if isinstance(c, dict)]
    if len(candidate_ids) != len(candidates) or len(set(candidate_ids)) != len(candidate_ids):
        errors.append("Candidate pattern IDs duplicated or missing")
    if not set(candidate_ids).issubset(patterns):
        errors.append("Candidate contains unknown navigation pattern")
    for c in candidates:
        if not isinstance(c, dict) or len(str(c.get("reason", ""))) < 10 or len(str(c.get("tradeoff", ""))) < 10:
            errors.append("Every recommendation needs rationale and tradeoff")
    selection = doc.get("selection", {})
    if not isinstance(selection, dict):
        return errors + ["Selection must be an object"]
    status, chosen, source = (selection.get(k) for k in ("status", "pattern_id", "source"))
    statement = selection.get("user_statement")
    if status == "pending":
        if chosen is not None or source != "unresolved":
            errors.append("Pending navigation recommendation cannot be user-approved")
    elif status == "approved":
        if chosen not in patterns:
            errors.append("Approved navigation layout must name a known pattern")
        if source not in {"confirmed", "delegated", "inherited"}:
            errors.append("Approval requires confirmed/delegated/inherited provenance")
        if source in {"confirmed", "delegated"} and not str(statement or "").strip():
            errors.append("Actual user instruction or explicit delegation required")
    else:
        errors.append("Navigation selection status must be pending/approved")
    resp = doc.get("responsive", {})
    if not isinstance(resp, dict):
        return errors + ["Responsive mapping must be an object"]
    desktop, mobile = resp.get("desktop", {}), resp.get("mobile", {})
    if not isinstance(desktop, dict) or not isinstance(mobile, dict):
        return errors + ["Desktop/mobile mappings must be objects"]
    if desktop.get("mode") not in NAV_MODES or mobile.get("mode") not in NAV_MODES:
        errors.append("Unsupported responsive navigation mode")
    dv, mv, ov = (desktop.get("visible_ids", []), mobile.get("visible_ids", []), mobile.get("overflow_ids", []))
    if not all(isinstance(x, list) for x in (dv, mv, ov)):
        return errors + ["Visible/overflow destinations must be lists"]
    for label, seq in (("desktop", dv), ("mobile", mv), ("mobile overflow", ov)):
        if any(i not in dest_set for i in seq):
            errors.append(f"{label} references unknown destination")
        if len(set(seq)) != len(seq):
            errors.append(f"{label} destination duplicated")
    if set(mv) & set(ov):
        errors.append("A destination cannot be both visible and overflow on mobile")
    if set(dv) != dest_set:
        errors.append("Desktop mapping must make all top-level destinations reachable")
    if set(mv) | set(ov) != dest_set:
        errors.append("Mobile navigation must preserve reachability of every destination")
    if mobile.get("mode") in {"bottom", "bottom-drawer", "top-bottom"}:
        if not 3 <= len(mv) <= 5:
            errors.append("Bottom primary nav should expose 3–5 real destinations, not hide or cram extras")
        if ov and mobile.get("mode") == "bottom":
            errors.append("Overflow destinations require a discoverable drawer/more pattern")
    if resp.get("same_destination_ids") is not True or resp.get("context_preserved") is not True:
        errors.append("Responsive navigation must preserve destination identity and task context")
    if desktop.get("mode") == "side-bottom-tools" and mobile.get("mode") == "bottom":
        errors.append("Bottom action bar must not be treated as primary bottom navigation")
    review = doc.get("review", {})
    if not isinstance(review, dict):
        return errors + ["Review must be an object"]
    if review.get("browser_status") not in {"PASS", "FAIL", "NOT RUN"}:
        errors.append("Browser status must be PASS/FAIL/NOT RUN")
    if review.get("browser_status") == "PASS" and (len(review.get("breakpoints", [])) < 2 or not review.get("evidence")):
        errors.append("Browser PASS requires desktop/mobile breakpoints and evidence")
    return errors


def validate_repository() -> list[str]:
    errors = [f"Missing navigation artifact {p}" for p in REFERENCES if not (ROOT / p).is_file()]
    errors.extend(validate_catalog())
    try:
        errors.extend(validate_decision(json.loads(EXAMPLE.read_text("utf-8"))))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f"Invalid navigation example: {exc}")
    skill = (ROOT / "SKILL.md").read_text("utf-8")
    for required in ("navigation-architecture.md", "navigation-pattern-catalog.json",
                     "validate_navigation_architecture.py"):
        if required not in skill:
            errors.append("SKILL routing missing " + required)
    return errors


def main() -> int:
    p = argparse.ArgumentParser(description="Check navigation pattern and decision integrity; not a visual test")
    p.add_argument("decision", nargs="?", type=Path)
    p.add_argument("--repository", action="store_true")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    issues = validate_repository() if args.repository else validate_catalog() if args.decision is None else []
    if args.decision:
        try:
            issues.extend(validate_decision(json.loads(args.decision.read_text("utf-8"))))
        except (OSError, ValueError) as exc:
            issues.append(str(exc))
    if args.json:
        print(json.dumps({"passed": not issues, "errors": issues, "scope": "static semantics and provenance only"}, ensure_ascii=False, indent=2))
    else:
        for err in issues:
            print("ERROR:", err)
        print("Navigation architecture:", "PASS" if not issues else "FAIL")
    return int(bool(issues))


if __name__ == "__main__":
    raise SystemExit(main())
