#!/usr/bin/env python3
"""Validate generic visual priority plans. Static intent contract, NOT aesthetic or WCAG proof."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "assets/visual-priority-patterns.json"
MODES = {"Operate", "Persuade", "Read", "Experience"}
PRIORITIES = {"P0", "P1", "P2", "P3"}
TYPE_ROLES = {"display", "page-heading", "section-heading", "primary-content", "strong", "body", "supporting", "caption", "control"}
REQUIRED_STATES = {"default", "focus-visible"}
REQUIRED_DOCS = (
    "references/perceptual-hierarchy-gate.md",
    "references/component-craft-gate.md",
    "references/typography-hierarchy.md",
    "references/component-first.md",
    "references/visual-qa.md",
    "assets/visual-priority-patterns.json",
    "scripts/validate_visual_priority.py",
    "tests/test_visual_priority.py",
)


def validate_plan(data: object, *, all_modes: bool = False) -> list[str]:
    errors = []
    if not isinstance(data, dict) or data.get("schema_version") != "1.0":
        return ["Expected visual priority plan version 1.0"]
    pages = data.get("pages")
    if not isinstance(pages, list) or not pages:
        return ["At least one page is required"]
    ids = set()
    modes_seen = set()
    for page in pages:
        if not isinstance(page, dict):
            errors.append("Invalid page entry")
            continue
        ident = page.get("id")
        if not isinstance(ident, str) or not ident.strip() or ident in ids:
            errors.append("Page ids must be unique non-empty strings")
        ids.add(ident)
        mode = page.get("mode")
        if mode not in MODES:
            errors.append(f"{ident}: unsupported mode")
        else:
            modes_seen.add(mode)
        if not isinstance(page.get("user_goal"), str) or len(page["user_goal"].strip()) < 10:
            errors.append(f"{ident}: missing real user goal")
        items = page.get("info_items", [])
        if not isinstance(items, list) or len(items) < 3:
            errors.append(f"{ident}: need a meaningful salience map")
            continue
        item_ids = [x.get("id") if isinstance(x, dict) else None for x in items]
        if any(not isinstance(x, str) or not x for x in item_ids) or len(set(item_ids)) != len(item_ids):
            errors.append(f"{ident}: info item ids must be unique and non-empty")
        if not any(isinstance(x, dict) and x.get("priority") == "P0" for x in items):
            errors.append(f"{ident}: must name primary decision focus")
        if sum(isinstance(x, dict) and x.get("priority") == "P0" for x in items) > 2:
            errors.append(f"{ident}: too many competing P0 focus items; split or justify")
        type_roles = set()
        for item in items:
            if not isinstance(item, dict):
                errors.append(f"{ident}: invalid info item")
                continue
            name = item.get("id")
            priority = item.get("priority")
            type_role = item.get("type_role")
            if priority not in PRIORITIES or type_role not in TYPE_ROLES:
                errors.append(f"{ident}/{name}: unsupported priority/type role")
            if priority in {"P0", "P1"} and type_role == "caption":
                errors.append(f"{ident}/{name}: essential information relegated to caption")
            if not item.get("role") or not isinstance(item.get("decision_reason"), str) or len(item["decision_reason"].strip()) < 10:
                errors.append(f"{ident}/{name}: explain semantic role and decision impact")
            type_roles.add(type_role)
        if len(type_roles) < 2:
            errors.append(f"{ident}: all information uses one text treatment")
        components = page.get("components")
        if not isinstance(components, list) or not components:
            errors.append(f"{ident}: at least one relevant component contract required")
        else:
            for c in components:
                if not isinstance(c, dict):
                    errors.append(f"{ident}: invalid component")
                    continue
                if not c.get("id") or not c.get("type") or not c.get("purpose"):
                    errors.append(f"{ident}: component needs id, type and purpose")
                if not REQUIRED_STATES.issubset(set(c.get("states", []))):
                    errors.append(f"{ident}/{c.get('id')}: missing default or focus-visible state")
                if not c.get("long_content_strategy"):
                    errors.append(f"{ident}/{c.get('id')}: missing long-content/zoom plan")
                if c.get("reuse_decision") not in {"reuse", "wrap", "build", "defer", "not-needed"}:
                    errors.append(f"{ident}/{c.get('id')}: choose reuse/wrap/build/defer/not-needed")
    if all_modes and modes_seen != MODES:
        errors.append("Reference examples must demonstrate all four Web modes")
    return errors


def validate_repository() -> list[str]:
    errors = [f"Missing artifact: {path}" for path in REQUIRED_DOCS if not (ROOT / path).is_file()]
    if errors:
        return errors
    skill = (ROOT / "SKILL.md").read_text("utf-8")
    for needed in ("perceptual-hierarchy-gate.md", "component-craft-gate.md", "validate_visual_priority.py"):
        if needed not in skill:
            errors.append(f"SKILL.md lacks mandatory generic gate route: {needed}")
    return errors + validate_plan(json.loads(EXAMPLE.read_text("utf-8")), all_modes=True)


def main() -> int:
    p = argparse.ArgumentParser(description="Check generic page salience and component intent; no aesthetic PASS claims")
    p.add_argument("file", nargs="?", type=Path)
    p.add_argument("--repository", action="store_true")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    errors = validate_repository() if args.repository else []
    if args.file:
        try:
            errors.extend(validate_plan(json.loads(args.file.read_text("utf-8"))))
        except (OSError, ValueError) as e:
            errors.append(str(e))
    if not args.repository and args.file is None:
        p.error("Provide a plan JSON or --repository")
    if args.json:
        print(json.dumps({"passed": not errors, "issues": errors, "scope": "static salience/component contract, not visual or accessibility proof"}, ensure_ascii=False, indent=2))
    else:
        for e in errors:
            print("ERROR:", e)
        print("Visual priority plan:", "PASS" if not errors else "FAIL")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
