#!/usr/bin/env python3
"""Advisory page content & density plan validator.

Checks explicit task hierarchy, necessary content retention, disclosure routes
and honest screenshot evidence. Does not judge aesthetics or prescribe whitespace
pixel quotas, and never rewrites UI code.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "assets/page-density-profiles.json"
EXAMPLE = ROOT / "examples/page-content-plan-demo.json"
FILES = (
    "references/page-density-and-content-priority.md",
    "references/whitespace-and-surface-composition.md",
    "references/overview-density-case.md",
    "assets/page-density-profiles.json",
    "assets/page-content-plan.schema.json",
    "assets/page-density-lab.html",
    "examples/page-content-plan-demo.json",
    "scripts/validate_page_content_plan.py",
    "tests/test_page_content_plan.py",
)
ROLES = {"overview", "onboarding", "analysis", "management", "marketing", "reading", "editor", "other"}
STATES = {"first_visit", "returning", "data_available", "empty", "loading", "error", "mixed"}
PLACEMENTS = {"primary", "supporting", "conditional", "deferred", "removed"}
IMPORTANCE = {"critical", "supporting", "optional"}
PRIORITY = {"primary", "secondary", "tertiary"}
SOURCES = {"confirmed", "delegated", "inherited", "provisional"}


def validate_catalog(data: dict | None = None) -> list[str]:
    errors: list[str] = []
    if data is None:
        try:
            data = json.loads(CATALOG.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            return [f"Density catalog unreadable: {exc}"]
    profiles = data.get("profiles", [])
    ids = [p.get("id") for p in profiles if isinstance(p, dict)]
    required = {"airy", "balanced", "productive", "compact"}
    if len(ids) != len(profiles) or len(set(ids)) != len(ids) or not required.issubset(ids):
        errors.append("Density catalog must describe four distinct page-level profiles")
    for item in profiles:
        if not isinstance(item, dict):
            errors.append("Malformed density profile")
            continue
        for key in ("label", "fit", "spacing_strategy", "surface_strategy", "content_strategy", "typography_strategy", "exceptions"):
            if not item.get(key):
                errors.append(f"{item.get('id')}: missing {key}")
    policies = data.get("policies", {})
    for key in ("page_level_not_global", "critical_information_never_deleted_for_aesthetics",
                "progressive_disclosure_must_be_discoverable", "no_numeric_whitespace_target",
                "content_removal_before_padding_tuning"):
        if policies.get(key) is not True:
            errors.append(f"Missing density principle: {key}")
    if len(data.get("sources", [])) < 3:
        errors.append("Density guidance requires sourced research")
    return errors


def validate_plan(doc: dict, catalog: dict | None = None) -> list[str]:
    errors: list[str] = []
    if catalog is None:
        catalog = json.loads(CATALOG.read_text(encoding="utf-8"))
    if not isinstance(doc, dict) or doc.get("schema_version") != "1.0":
        return ["Unsupported content plan schema version"]
    pages = doc.get("pages", [])
    if not isinstance(pages, list) or not pages:
        return ["Page content plan requires at least one page"]
    profile_ids = {p["id"] for p in catalog.get("profiles", [])}
    route_ids: list[str] = []
    for page in pages:
        if not isinstance(page, dict):
            errors.append("Malformed page")
            continue
        route = page.get("route")
        route_ids.append(route)
        ctx = str(route)
        if not isinstance(route, str) or not route.startswith("/"):
            errors.append(f"{ctx}: route must start with /")
        if page.get("page_role") not in ROLES or page.get("audience_state") not in STATES:
            errors.append(f"{ctx}: invalid page role / audience state")
        if not str(page.get("primary_task", "")).strip():
            errors.append(f"{ctx}: no primary task")
        if page.get("density_profile") not in profile_ids:
            errors.append(f"{ctx}: unknown page-level density profile")
        decision = page.get("density_decision", {})
        if not isinstance(decision, dict) or decision.get("source") not in SOURCES:
            errors.append(f"{ctx}: missing density decision source")
        elif decision["source"] in {"confirmed", "delegated"} and not str(decision.get("user_statement") or "").strip():
            errors.append(f"{ctx}: cannot assert user confirmed/delegated without actual statement")
        items = page.get("content", [])
        if not isinstance(items, list) or not items:
            errors.append(f"{ctx}: content inventory missing")
            continue
        ids = [x.get("id") for x in items if isinstance(x, dict)]
        if len(ids) != len(items) or any(not isinstance(x, str) or not x for x in ids) or len(set(ids)) != len(ids):
            errors.append(f"{ctx}: duplicate / missing content IDs")
        index = {x["id"]: x for x in items if isinstance(x, dict) and x.get("id")}
        primary = []
        for item in items:
            if not isinstance(item, dict):
                errors.append(f"{ctx}: malformed content inventory entry")
                continue
            name, imp, place = item.get("id"), item.get("importance"), item.get("placement")
            if imp not in IMPORTANCE or place not in PLACEMENTS:
                errors.append(f"{ctx}/{name}: invalid importance or placement")
                continue
            if not str(item.get("reason", "")).strip() or not item.get("source"):
                errors.append(f"{ctx}/{name}: placement requires evidence/reason")
            if place == "primary":
                primary.append(name)
            if imp == "critical" and place in {"removed", "deferred"}:
                errors.append(f"{ctx}/{name}: critical information cannot be removed or deferred")
            if place == "deferred" and not str(item.get("accessible_via", "")).strip():
                errors.append(f"{ctx}/{name}: deferred content requires discoverable access")
            if place == "conditional":
                if not str(item.get("condition", "")).strip() or not str(item.get("accessible_via", "")).strip():
                    errors.append(f"{ctx}/{name}: conditional content needs user state and recovery path")
            if place == "removed":
                dup = item.get("duplicate_of")
                if imp != "optional" or dup not in index or dup == name:
                    errors.append(f"{ctx}/{name}: removed content must be optional and reference its redundancy")
        if not primary:
            errors.append(f"{ctx}: at least one primary content item needed")
        actions = page.get("actions", [])
        if not isinstance(actions, list):
            errors.append(f"{ctx}: actions must be an array")
            actions = []
        if sum(1 for a in actions if isinstance(a, dict) and a.get("priority") == "primary") > 1:
            errors.append(f"{ctx}: too many competing primary actions for the same state")
        for a in actions:
            if not isinstance(a, dict) or a.get("priority") not in PRIORITY or not a.get("id") or not a.get("label"):
                errors.append(f"{ctx}: malformed action/priority")
        layout = page.get("layout", {})
        if not isinstance(layout, dict):
            errors.append(f"{ctx}: missing layout plan")
            continue
        if layout.get("nested_decorative_cards") is not False:
            errors.append(f"{ctx}: nested decorative cards must be removed")
        if not str(layout.get("primary_region", "")).strip() or not str(layout.get("spacing_strategy", "")).strip():
            errors.append(f"{ctx}: missing primary area / whitespace relationships")
        above = layout.get("above_fold", [])
        if not isinstance(above, list):
            errors.append(f"{ctx}: above-fold inventory must be array")
            above = []
        if len(above) != len(set(above)):
            errors.append(f"{ctx}: duplicate above-fold items")
        for id_ in above:
            if id_ not in index:
                errors.append(f"{ctx}: above-fold references missing content {id_}")
            elif index[id_].get("placement") in {"removed", "deferred"}:
                errors.append(f"{ctx}: removed/deferred content shown above fold: {id_}")
        if not set(primary).intersection(above):
            errors.append(f"{ctx}: primary task is not visible in the first view")
        review = page.get("review", {})
        if not isinstance(review, dict) or review.get("browser_status") not in {"PASS", "FAIL", "NOT RUN"}:
            errors.append(f"{ctx}: browser status must be PASS / FAIL / NOT RUN")
        elif review["browser_status"] == "PASS" and not review.get("evidence"):
            errors.append(f"{ctx}: cannot claim browser PASS without evidence")
    if len(set(route_ids)) != len(route_ids):
        errors.append("Page routes duplicated")
    return errors


def validate_repository() -> list[str]:
    errors = [f"Missing page-density asset: {path}" for path in FILES if not (ROOT / path).is_file()]
    errors.extend(validate_catalog())
    try:
        errors.extend(validate_plan(json.loads(EXAMPLE.read_text(encoding="utf-8"))))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f"Invalid Synthetic Demo page content example: {exc}")
    skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    for key in ("page-density-and-content-priority.md", "whitespace-and-surface-composition.md",
                "validate_page_content_plan.py"):
        if key not in skill:
            errors.append("SKILL.md lacks content density routing: " + key)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Check page-level content decisions and disclosure reachability")
    parser.add_argument("file", nargs="?", type=Path)
    parser.add_argument("--repository", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    issues = validate_repository() if args.repository else validate_catalog() if args.file is None else []
    if args.file:
        try:
            issues.extend(validate_plan(json.loads(args.file.read_text(encoding="utf-8"))))
        except (OSError, ValueError) as exc:
            issues.append("Could not parse plan: " + str(exc))
    if args.json:
        print(json.dumps({"passed": not issues, "errors": issues,
                          "scope": "Content decision checks, NOT visual aesthetic or real-browser approval"},
                         ensure_ascii=False, indent=2))
    else:
        for issue in issues:
            print("ERROR:", issue)
        print("Page content priority & density:", "PASS" if not issues else "FAIL")
    return int(bool(issues))


if __name__ == "__main__":
    raise SystemExit(main())
