#!/usr/bin/env python3
"""Validate component-library-first decision plans.

This is a declarative plan checker, NOT proof of library installation, visual quality,
accessibility or successful browser operation in the target application.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "examples/component-library-decision.demo.json"
REQUIRED = [
    "SKILL.md",
    "README.md",
    "references/component-library-first-gate.md",
    "references/enterprise-ui-library-guide.md",
    "references/component-first.md",
    "references/framework-support-matrix.md",
    "examples/component-library-decision.demo.json",
]
CHOICES = {"existing", "new_selection", "native_exception", "no_interaction"}
SOURCES = {"primary_library", "headless_primitive", "native", "custom_exception"}
BASE_STATES = {
    "Select": {"default", "open", "selected", "focus", "disabled"},
    "Combobox": {"default", "open", "selected", "focus", "disabled"},
    "MultiSelect": {"default", "open", "selected", "focus", "disabled"},
    "DropdownMenu": {"default", "open", "focus", "disabled"},
    "Button": {"default", "focus", "disabled", "loading"},
    "Checkbox": {"default", "selected", "focus", "disabled"},
    "Radio": {"default", "selected", "focus", "disabled"},
    "Switch": {"default", "selected", "focus", "disabled"},
    "Tabs": {"default", "selected", "focus"},
    "Dialog": {"default", "open", "focus"},
}
KNOWN = set(BASE_STATES) | {"Input", "DatePicker", "Popover", "Tooltip", "Textarea"}
PHASES = {"planned", "integrated", "verified"}


def validate(plan: object) -> list[str]:
    issues: list[str] = []
    if not isinstance(plan, dict):
        return ["Plan must be a JSON object"]
    if plan.get("schema_version") != "1.0":
        issues.append("schema_version must be 1.0")
    if not str(plan.get("framework", "")).strip():
        issues.append("Framework must be stated")
    needed = plan.get("interactive_controls_needed")
    if not isinstance(needed, bool):
        issues.append("interactive_controls_needed must be boolean")
        needed = False

    library = plan.get("ui_library")
    if not isinstance(library, dict):
        return issues + ["ui_library decision is missing"]
    choice = library.get("decision")
    if choice not in CHOICES:
        issues.append("Choose a primary component strategy before building business pages")
    if needed and choice == "no_interaction":
        issues.append("Interactive project cannot skip UI library selection")
    if not needed and choice != "no_interaction":
        issues.append("No-interaction page should not force a UI dependency")
    primary = str(library.get("primary") or "").strip()
    reason = str(library.get("reason") or "").strip()
    if needed and choice in {"existing", "new_selection"}:
        if not primary or primary.casefold() in {"none", "tbd", "custom-css", "plain-css"}:
            issues.append("A real primary library or primitive stack must be selected")
        if library.get("framework_compatible") is not True:
            issues.append("Primary library must be framework compatible")
        if not str(library.get("theme_strategy") or "").strip():
            issues.append("Component library must have a shared theme integration strategy")
        if len(reason) < 15:
            issues.append("Primary library selection requires a grounded reason")
    if choice == "native_exception" and len(reason) < 25:
        issues.append("Intentional native-only exception requires a substantive reason")
    if choice == "no_interaction" and needed:
        issues.append("Noninteractive exception cannot hide real controls")

    controls = plan.get("controls", [])
    if not isinstance(controls, list):
        return issues + ["controls must be a list"]
    if needed and not controls:
        issues.append("Interactive page needs explicit control-to-library mapping")
    if not needed and controls:
        issues.append("Noninteractive page must not declare required interactive controls")
    seen: set[str] = set()
    for ctrl in controls:
        if not isinstance(ctrl, dict):
            issues.append("Control mapping must be an object")
            continue
        kind = str(ctrl.get("kind") or "").strip()
        if kind not in KNOWN:
            issues.append(f"Unknown or missing control kind: {kind}")
        if kind in seen:
            issues.append(f"Duplicate control mapping: {kind}")
        seen.add(kind)
        source = ctrl.get("source")
        if source not in SOURCES:
            issues.append(f"{kind}: use a real library/primitive/native source, not hand-written pseudo-controls")
            continue
        if not str(ctrl.get("component") or "").strip():
            issues.append(f"{kind}: specify actual component or semantic HTML element")
        if source in {"custom_exception", "native"}:
            if len(str(ctrl.get("exception_reason") or "").strip()) < 25:
                issues.append(f"{kind}: native/custom exception requires a substantive reason")
        if choice == "native_exception" and source not in {"native", "custom_exception"}:
            issues.append(f"{kind}: native exception cannot be paired with a declared UI library")
        states = ctrl.get("states_to_test", [])
        if not isinstance(states, list) or not all(isinstance(x, str) for x in states):
            issues.append(f"{kind}: states_to_test must be a list of strings")
        else:
            missing = BASE_STATES.get(kind, {"default", "focus"}) - set(states)
            if missing:
                issues.append(f"{kind}: missing first-pass states {', '.join(sorted(missing))}")

    first = plan.get("first_pass")
    if not isinstance(first, dict):
        return issues + ["first_pass evidence and phase are required"]
    phase = first.get("phase")
    if phase not in PHASES:
        issues.append("first_pass phase must be planned/integrated/verified")
    imports = first.get("integration_imports")
    if not isinstance(imports, list):
        issues.append("integration_imports must be a list")
        imports = []
    evidence = first.get("evidence")
    if not isinstance(evidence, list):
        issues.append("evidence must be a list")
        evidence = []
    if phase in {"integrated", "verified"} and needed:
        if not imports or not all(str(x).strip() for x in imports):
            issues.append("Integrated controls need actual import/usage evidence")
        if first.get("theme_applied") is not True and choice != "native_exception":
            issues.append("Integrated library needs project-level theme application")
    if phase == "verified":
        if first.get("real_page_status") != "VERIFIED":
            issues.append("First pass cannot be VERIFIED without real-page browser verification")
        if not evidence:
            issues.append("First pass VERIFIED needs real-page evidence")
        if first.get("showcase_status") not in {"VERIFIED", "DEMO ONLY"}:
            issues.append("First pass VERIFIED requires real controls to have been checked")
    if phase == "planned" and first.get("real_page_status") == "VERIFIED":
        issues.append("A planned library cannot claim real-page verification")
    return issues


def validate_repository() -> list[str]:
    missing = [f"Missing component library resource: {p}" for p in REQUIRED if not (ROOT / p).is_file()]
    if missing:
        return missing
    for file in (ROOT / "SKILL.md", ROOT / "README.md", ROOT / "references/component-first.md"):
        if "component-library-first-gate.md" not in file.read_text("utf-8"):
            missing.append(f"{file.name}: no link to Component Library First gate")
    try:
        missing.extend(validate(json.loads(EXAMPLE.read_text("utf-8"))))
    except (ValueError, OSError, TypeError) as exc:
        missing.append(f"Example decision cannot be read: {exc}")
    return missing


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit UI component-library plans; NOT a browser test")
    parser.add_argument("file", nargs="?", type=Path)
    parser.add_argument("--repository", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    issues = validate_repository() if args.repository else []
    if args.file:
        try:
            issues.extend(validate(json.loads(args.file.read_text("utf-8"))))
        except (ValueError, OSError) as exc:
            issues.append(f"Invalid decision plan: {exc}")
    if not args.repository and args.file is None:
        parser.error("Provide a decision plan JSON or --repository")
    if args.json:
        print(json.dumps({"passed": not issues, "issues": issues,
                          "scope": "static decision and first-pass evidence declaration only"},
                         ensure_ascii=False, indent=2))
    else:
        for issue in issues:
            print("ERROR:", issue)
        print("Component Library First:", "PASS" if not issues else "FAIL")
    return int(bool(issues))


if __name__ == "__main__":
    raise SystemExit(main())
