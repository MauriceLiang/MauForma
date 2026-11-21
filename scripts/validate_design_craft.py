#!/usr/bin/env python3
"""Static checks for optional design-craft guidance and sample decision records.

Checks structure and evidence declarations only. It cannot evaluate visual taste.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "examples/design-craft-decision.demo.json"
REQUIRED = (
    "SKILL.md", "README.md",
    "references/design-craft-loop.md",
    "references/figma-fidelity-workflow.md",
    "references/visual-qa.md",
    "examples/design-craft-decision.demo.json",
)
MODES = {"shape", "polish", "review", "fidelity", "fix"}
SOURCES = {"confirmed", "inherited", "delegated", "proposed", "unresolved"}
SEVERITIES = {"P0", "P1", "P2", "P3"}
EVIDENCE = {"OBSERVED", "CODE ONLY", "INFERRED", "NOT TESTED", "DEMO ONLY"}
STATUS = {"VERIFIED", "STATIC CHECK", "DEMO ONLY", "NOT TESTED", "BLOCKED"}
SEVEN_DOMAINS = (
    "Typography", "Color & Contrast", "Spatial Design", "Motion",
    "Interaction States", "Responsive", "UX Writing",
)


def validate_plan(plan: object) -> list[str]:
    errors: list[str] = []
    if not isinstance(plan, dict):
        return ["Design decision must be a JSON object"]
    if plan.get("schema_version") != "1.0":
        errors.append("schema_version must be 1.0")
    if plan.get("mode") not in MODES:
        errors.append("mode must identify shape/polish/review/fidelity/fix")
    if not str(plan.get("scope", "")).strip() or not str(plan.get("user_task", "")).strip():
        errors.append("scope and user_task must be explicit")
    decision = plan.get("design_decision")
    if not isinstance(decision, dict):
        return errors + ["design_decision must be an object"]
    for k in ("visual_direction", "why", "primary_focus", "rejected_alternative"):
        if not str(decision.get(k) or "").strip():
            errors.append("design_decision missing: " + k)
    if decision.get("source") not in SOURCES:
        errors.append("design direction must identify confirmed/inherited/delegated/proposed/unresolved")
    system = plan.get("existing_system")
    if not isinstance(system, dict):
        errors.append("existing_system is missing")
    else:
        for k in ("component_source", "token_source"):
            if not str(system.get(k) or "").strip():
                errors.append("existing_system missing: " + k)
        if not isinstance(system.get("framework_change"), bool):
            errors.append("framework_change must be a boolean")
    review = plan.get("review")
    if not isinstance(review, dict):
        return errors + ["review must be an object"]
    if review.get("evidence_level") not in EVIDENCE:
        errors.append("review evidence_level is unknown")
    if review.get("overall_status") not in STATUS:
        errors.append("overall_status is unknown")
    issues = review.get("issues")
    if not isinstance(issues, list):
        return errors + ["review issues must be a list"]
    for i, issue in enumerate(issues):
        if not isinstance(issue, dict):
            errors.append(f"issues[{i}] must be an object")
            continue
        if issue.get("severity") not in SEVERITIES:
            errors.append(f"issues[{i}]: missing P0/P1/P2/P3 severity")
        if issue.get("evidence_level") not in EVIDENCE:
            errors.append(f"issues[{i}]: evidence source missing")
        for field in ("symptom", "evidence", "root_cause_hypothesis",
                      "affected_task", "recommended_fix", "validation"):
            if not str(issue.get(field) or "").strip():
                errors.append(f"issues[{i}]: missing {field}")
    routes = review.get("verified_routes")
    shots = review.get("screenshots")
    if not isinstance(routes, list) or not isinstance(shots, list):
        errors.append("review requires verified_routes and screenshots arrays")
    if review.get("overall_status") == "VERIFIED":
        if not routes:
            errors.append("Cannot claim VERIFIED without real target routes")
        if not shots:
            errors.append("Cannot claim visual VERIFIED without actual before/after or reference screenshot evidence")
        if review.get("evidence_level") not in {"OBSERVED"}:
            errors.append("VERIFIED visual status must be based on observed browser evidence")
    if plan.get("fixture_type") == "synthetic" and (
        review.get("overall_status") == "VERIFIED" or review.get("evidence_level") == "OBSERVED"
    ):
        errors.append("Synthetic teaching data cannot claim actual product verification")
    return errors


def validate_repository(root: Path = ROOT) -> list[str]:
    errors = []
    text = {}
    for file in REQUIRED:
        p = root / file
        if not p.exists():
            errors.append("Missing design-craft resource: " + file)
            continue
        text[file] = p.read_text("utf-8")
    if errors:
        return errors
    for file in ("SKILL.md", "README.md", "references/visual-qa.md"):
        for guide in ("references/design-craft-loop.md", "references/figma-fidelity-workflow.md"):
            if guide not in text[file]:
                errors.append(f"{file}: missing task routing to {guide}")
    craft = text["references/design-craft-loop.md"]
    for mode in MODES:
        if f"`{mode}`" not in craft and f"**{mode}**" not in craft:
            # some headings use italic mode labels instead of literal code identifiers
            if f"**{mode}**" not in craft and f"`{mode}`" not in craft:
                errors.append("Missing design workflow mode: " + mode)
    for domain in SEVEN_DOMAINS:
        if domain not in craft:
            errors.append("Missing visual craft domain: " + domain)
    for word in ("evidence", "root cause", "P0", "P1", "P2", "P3", "fidelity"):
        if word.casefold() not in craft.casefold():
            errors.append("Missing evidence-led critique principle: " + word)
    figma = text["references/figma-fidelity-workflow.md"]
    # English runtime reference: preserve the same screenshot/difference evidence
    # contract without requiring Chinese literal strings in the translation.
    for token in ("MCP", "node", "screenshot", "difference", "Token", "component-library-first-gate.md"):
        if token.casefold() not in figma.casefold():
            errors.append("Missing Figma fidelity prerequisite: " + token)
    try:
        errors.extend(validate_plan(json.loads(text["examples/design-craft-decision.demo.json"])))
    except (ValueError, TypeError) as exc:
        errors.append(f"Invalid decision JSON: {exc}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Check design-craft contracts, not visual quality")
    parser.add_argument("plan", nargs="?", type=Path)
    parser.add_argument("--repository", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if not args.repository and args.plan is None:
        parser.error("Provide a JSON decision plan or --repository")
    errors = validate_repository() if args.repository else []
    if args.plan:
        try:
            errors.extend(validate_plan(json.loads(args.plan.read_text("utf-8"))))
        except (OSError, ValueError) as exc:
            errors.append(f"Cannot read plan: {exc}")
    if args.json:
        print(json.dumps({"passed": not errors, "issues": errors,
                          "scope": "static decision and evidence contract only"}, ensure_ascii=False, indent=2))
    else:
        for issue in errors:
            print("ERROR:", issue)
        print("Design craft:", "PASS" if not errors else "FAIL")
    return int(bool(errors))


if __name__ == "__main__":
    sys.exit(main())
