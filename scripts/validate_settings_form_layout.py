#!/usr/bin/env python3
"""Validate synthetic settings/form layout routing contracts; not a visual UX score."""
from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTEXTS = {"settings", "form", "hybrid"}
LAYOUTS = {"horizontal_row", "stacked_field", "segmented_hybrid"}
SURFACES = {"open_sections", "single_bounded_panel"}
MOBILE = "stacked_responsive"


def validate(data: dict) -> list[str]:
    errors: list[str] = []
    cases = data.get("cases", [])
    if not isinstance(cases, list) or len(cases) < 7:
        return ["insufficient synthetic settings/form cases"]
    seen = set()
    kinds = set()
    for case in cases:
        cid = case.get("id")
        if not isinstance(cid, str) or not cid or cid in seen:
            errors.append("empty or duplicate case id")
        seen.add(cid)
        kind = case.get("context")
        kinds.add(kind)
        layout = case.get("layout")
        if kind not in CONTEXTS:
            errors.append(f"{cid}: invalid context")
        if layout not in LAYOUTS:
            errors.append(f"{cid}: invalid layout")
        if case.get("surface") not in SURFACES:
            errors.append(f"{cid}: nested/unjustified surface")
        if case.get("section_rhythm") != "group_gt_item":
            errors.append(f"{cid}: group spacing must exceed item spacing")
        if case.get("mobile") != MOBILE:
            errors.append(f"{cid}: mobile must reflow without squeezing")
        if case.get("visible_labels") is not True:
            errors.append(f"{cid}: visible label required")
        if case.get("feedback") is not True:
            errors.append(f"{cid}: real save/submit feedback required")
        if case.get("danger") not in {"none", "isolated_confirmed"}:
            errors.append(f"{cid}: dangerous action must be isolated and confirmed")
        if not isinstance(case.get("rationale"), str) or not case["rationale"].strip():
            errors.append(f"{cid}: missing rationale")
        scope = case.get("scope", "new_page")
        if scope not in {"new_page", "scoped_fix"}:
            errors.append(f"{cid}: invalid scope")
        if kind == "settings":
            if case.get("save_scope") != "independent":
                errors.append(f"{cid}: settings require independent save semantics")
            if case.get("field_kind") == "short_control" and layout != "horizontal_row":
                errors.append(f"{cid}: compact settings should use row layout")
            if case.get("field_kind") == "long_input" and (layout != "stacked_field" or not case.get("exception_reason")):
                errors.append(f"{cid}: long settings field needs justified stacked exception")
        elif kind == "form":
            if case.get("save_scope") != "submit_group" or layout != "stacked_field":
                errors.append(f"{cid}: grouped forms require stacked layout and submit scope")
            if case.get("validation") != "inline_below":
                errors.append(f"{cid}: form errors belong below the field")
        elif kind == "hybrid":
            if case.get("save_scope") != "mixed" or layout != "segmented_hybrid":
                errors.append(f"{cid}: hybrid needs per-region row/stack routing")
            if case.get("validation") != "inline_below":
                errors.append(f"{cid}: hybrid subform needs inline errors")
    if not CONTEXTS.issubset(kinds):
        errors.append("missing settings/form/hybrid route")
    if not any(c.get("danger") == "isolated_confirmed" for c in cases):
        errors.append("missing dangerous operation separation")
    if not any(c.get("scope") == "scoped_fix" for c in cases):
        errors.append("missing preserve-approved scoped-fix counterexample")
    if not any(c.get("context") == "settings" and c.get("surface") == "single_bounded_panel" for c in cases):
        errors.append("missing legitimate settings panel exception")
    return errors


def validate_repo() -> list[str]:
    paths = [
        "references/settings-form-layout-gate.md",
        "assets/settings-form-layout-cases.json",
        "examples/settings-form-layout-demo.html",
        "tests/settings_form_browser_smoke.mjs",
    ]
    errors = [f"missing {p}" for p in paths if not (ROOT / p).is_file()]
    if errors:
        return errors
    data = json.loads((ROOT / paths[1]).read_text(encoding="utf-8"))
    errors.extend(validate(data))
    for required in ("SKILL.md", "README.md", "references/product-experience-routing-gate.md", "references/progressive-visual-refinement-gate.md"):
        content = (ROOT / required).read_text(encoding="utf-8")
        if "settings-form-layout-gate.md" not in content:
            errors.append(f"{required}: missing scenario gate link")
    demo = (ROOT / paths[2]).read_text(encoding="utf-8")
    for token in ("data-mf-settings-row", "data-mf-field", "data-mf-danger", "aria-describedby", "data-mf-status"):
        if token not in demo:
            errors.append(f"demo: missing {token}")
    return errors


if __name__ == "__main__":
    errs = validate_repo()
    for err in errs:
        print("ERROR:", err)
    print("Settings/form contract errors:", len(errs))
    sys.exit(bool(errs))
