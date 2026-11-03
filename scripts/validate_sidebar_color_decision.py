#!/usr/bin/env python3
"""Check MauForma color references, contrast and user color-decision provenance.

Does NOT select colors for users, rewrite an explicit HEX, or certify aesthetics.
An approved theme requires an actual user choice / explicit delegation / inheritance.
"""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "assets/sidebar-color-directions.json"
PENDING = ROOT / "examples/sidebar-color-decision.pending.json"
HEX = re.compile(r"#[0-9a-fA-F]{6}\Z")
REQUIRED = {
    "main-bg", "main-surface", "main-text", "sidebar-bg", "sidebar-surface",
    "sidebar-selected", "sidebar-hover", "sidebar-text", "sidebar-text-muted",
    "sidebar-focus", "sidebar-border", "brand-accent", "chart-primary",
}
PAIRS = (
    ("main-text", "main-bg", 4.5), ("main-text", "main-surface", 4.5),
    ("sidebar-text", "sidebar-bg", 4.5), ("sidebar-text-muted", "sidebar-bg", 4.5),
    ("sidebar-text", "sidebar-selected", 4.5), ("sidebar-focus", "sidebar-selected", 3.0),
    ("chart-primary", "main-surface", 3.0),
)
REFERENCE_DOCS = (
    "references/sidebar-color-discovery.md",
    "references/sidebar-color-reference-cases.md",
    "examples/sidebar-color-discovery-dialogues.md",
    "assets/sidebar-color-preview.html",
    "assets/sidebar-color-decision.schema.json",
    "tests/test_sidebar_color_choice.py",
)


def luminance(color: str) -> float:
    if not isinstance(color, str) or not HEX.fullmatch(color):
        raise ValueError(f"Expected #RRGGBB, got {color!r}")
    components = [int(color[i:i + 2], 16) / 255 for i in (1, 3, 5)]
    linear = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
              for c in components]
    return 0.2126 * linear[0] + 0.7152 * linear[1] + 0.0722 * linear[2]


def contrast(a: str, b: str) -> float:
    high, low = sorted((luminance(a), luminance(b)), reverse=True)
    return (high + .05) / (low + .05)


def check_colors(colors: dict, label: str) -> list[str]:
    errors: list[str] = []
    if not isinstance(colors, dict):
        return [f"{label}: missing color mapping"]
    missing = REQUIRED - colors.keys()
    if missing:
        errors.append(f"{label}: missing cross-page color roles: {sorted(missing)}")
    for role, color in colors.items():
        try:
            luminance(color)
        except ValueError as exc:
            errors.append(f"{label}/{role}: {exc}")
    for a, b, threshold in PAIRS:
        if a in colors and b in colors:
            try:
                value = contrast(colors[a], colors[b])
                if value < threshold:
                    errors.append(f"{label}: {a} vs {b} contrast {value:.2f} below {threshold}")
            except ValueError:
                pass
    return errors


def validate_catalog(data: dict | None = None) -> list[str]:
    errors = [f"Missing color reference {p}" for p in REFERENCE_DOCS
              if not (ROOT / p).is_file()]
    if data is None:
        try:
            data = json.loads(CATALOG.read_text("utf-8"))
        except (OSError, ValueError) as exc:
            return errors + [f"Cannot read catalog: {exc}"]
    references = data.get("references", [])
    palettes = data.get("palettes", [])
    if len(references) < 5 or len(palettes) < 4:
        errors.append("Provide diverse official references and more than 3 color options")
    ref_ids = {r.get("id") for r in references if isinstance(r, dict)}
    if len(ref_ids) != len(references) or None in ref_ids:
        errors.append("Official reference IDs missing or duplicated")
    for r in references:
        if not isinstance(r, dict) or not str(r.get("url", "")).startswith("https://"):
            errors.append("Each reference requires its official HTTPS link")
        for field in ("observed", "applies", "caveat"):
            if not isinstance(r, dict) or not str(r.get(field, "")).strip():
                errors.append(f"Reference {r.get('id','?') if isinstance(r,dict) else '?'} missing {field}")
    ids = [p.get("id") for p in palettes if isinstance(p, dict)]
    if len(ids) != len(palettes) or len(set(ids)) != len(ids):
        errors.append("Duplicate or missing palette IDs")
    for palette in palettes:
        if not isinstance(palette, dict):
            errors.append("Malformed palette entry")
            continue
        pid = palette.get("id", "?")
        if palette.get("source_type") != "mauforma_original_interpretation_not_official_colors":
            errors.append(f"{pid}: do not represent original palettes as official brand colors")
        if not palette.get("best_for") or not palette.get("tradeoff") or not palette.get("character"):
            errors.append(f"{pid}: missing context, tradeoff or visual identity")
        if not set(palette.get("reference_ids", [])).issubset(ref_ids):
            errors.append(f"{pid}: unknown reference")
        errors.extend(check_colors(palette.get("colors"), pid))
    policy = data.get("selection_policy", {})
    for key in ("recommended_is_approval", "explicit_user_color_priority",
                "full_page_preview_required", "agent_delegation_only_with_explicit_permission"):
        if key not in policy:
            errors.append("Catalog lacks explicit decision rule: " + key)
    if policy.get("recommended_is_approval") is not False:
        errors.append("Recommendations must never be treated as approval")
    if policy.get("explicit_user_color_priority") is not True:
        errors.append("User-specified color must take precedence")
    return errors


def validate_decision(doc: dict, catalog: dict | None = None) -> list[str]:
    errors: list[str] = []
    if catalog is None:
        catalog = json.loads(CATALOG.read_text("utf-8"))
    ids = {p["id"] for p in catalog["palettes"]}
    if not isinstance(doc, dict) or doc.get("schema_version") != "1.0":
        return ["Unsupported sidebar color decision format"]
    status = doc.get("status")
    if status not in {"pending", "approved"}:
        errors.append("status must be pending or approved")
    recommendations = doc.get("recommendations", [])
    if not isinstance(recommendations, list) or not 1 <= len(recommendations) <= 3:
        errors.append("Offer only 1–3 relevant recommendations, not a long template list")
        recommendations = []
    recommended_ids = [x.get("palette_id") for x in recommendations if isinstance(x, dict)]
    if len(recommended_ids) != len(recommendations) or len(set(recommended_ids)) != len(recommended_ids):
        errors.append("Recommendations contain duplicate/invalid IDs")
    if not set(recommended_ids).issubset(ids):
        errors.append("Recommendation references non-existent palette")
    for item in recommendations:
        if not isinstance(item, dict) or len(str(item.get("reason", ""))) < 10 or len(str(item.get("tradeoff", ""))) < 10:
            errors.append("Each recommended palette needs an actual reason and tradeoff")
    selection = doc.get("selection", {})
    if not isinstance(selection, dict):
        return errors + ["selection must be an object"]
    selected = selection.get("palette_id")
    source = selection.get("source")
    statement = selection.get("user_statement")
    resolved = doc.get("resolved_colors")
    constraints = doc.get("user_constraints", [])
    review = doc.get("review", {})
    if status == "pending":
        if selected is not None or source != "unresolved" or resolved not in (None, {}):
            errors.append("Pending recommendation cannot claim a user-selected/approved palette")
    if status == "approved":
        if source not in {"confirmed", "delegated", "inherited"}:
            errors.append("Approved palette requires confirmed/delegated/inherited provenance")
        if selected not in ids | {"custom"}:
            errors.append("Approved choice must reference known palette or custom")
        if source in {"confirmed", "delegated"} and not str(statement or "").strip():
            errors.append("Confirmed/delegated decision requires an actual user statement")
        if selected == "custom" and not constraints:
            errors.append("Custom palette requires concrete user constraints")
        if not isinstance(resolved, dict) or not resolved:
            errors.append("Approved palette requires resolved cross-page tokens")
        else:
            errors.extend(check_colors(resolved, "approved"))
        if not isinstance(review, dict) or review.get("whole_page_preview") is not True:
            errors.append("Approved palette must be considered with a full-page preview")
        if not isinstance(review, dict) or not str(review.get("coordination_rationale", "")).strip():
            errors.append("Approved palette needs sidebar/topbar/main coordination rationale")
    if not isinstance(constraints, list):
        return errors + ["user_constraints must be a list"]
    for fixed in constraints:
        if not isinstance(fixed, dict):
            errors.append("Invalid color constraint")
            continue
        role, color = fixed.get("role"), fixed.get("hex")
        if role not in REQUIRED or not isinstance(color, str) or not HEX.fullmatch(color):
            errors.append("User fixed colors need a valid role and exact #RRGGBB")
        elif status == "approved" and isinstance(resolved, dict):
            if resolved.get(role, "").lower() != color.lower():
                errors.append(f"User color overridden without consent: {role} requested {color}")
        if fixed.get("source") not in {"confirmed", "inherited"} or not str(fixed.get("user_statement", "")).strip():
            errors.append(f"Missing user provenance for exact color: {role}")
    if not isinstance(review, dict):
        return errors + ["review must be an object"]
    if review.get("actual_browser_status") not in {"PASS", "FAIL", "NOT RUN"}:
        errors.append("Browser test status must be PASS/FAIL/NOT RUN")
    if review.get("actual_browser_status") == "PASS":
        required_regions = {"sidebar", "topbar", "main", "cards", "charts", "navigation-states", "focus"}
        if not required_regions.issubset(set(review.get("tested_regions", []))):
            errors.append("Browser PASS requires cross-region visual verification")
        if not str(review.get("evidence", "")).strip():
            errors.append("Browser PASS requires grounded evidence")
    return errors


def validate_repository() -> list[str]:
    errors = validate_catalog()
    try:
        data = json.loads(PENDING.read_text("utf-8"))
        errors.extend(validate_decision(data))
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append("Decision example error: " + str(exc))
    skill = (ROOT / "SKILL.md").read_text("utf-8") if (ROOT / "SKILL.md").is_file() else ""
    for term in ("sidebar-color-discovery.md", "sidebar-color-reference-cases.md",
                 "validate_sidebar_color_decision.py"):
        if term not in skill:
            errors.append("SKILL.md missing color-choice route: " + term)
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Check sidebar/main palette compatibility and user choice provenance")
    parser.add_argument("decision", nargs="?", type=Path)
    parser.add_argument("--repository", action="store_true", help="Check library and examples")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    errors = validate_repository() if args.repository else []
    if args.decision is not None:
        try:
            errors.extend(validate_decision(json.loads(args.decision.read_text("utf-8"))))
        except (OSError, ValueError) as exc:
            errors.append("Cannot load decision: " + str(exc))
    if not args.repository and args.decision is None:
        errors.extend(validate_catalog())
    if args.json:
        print(json.dumps({"passed": not errors, "errors": errors,
                          "scope": "contrast and provenance only; not proof of visual harmony"}, ensure_ascii=False, indent=2))
    else:
        for e in errors:
            print("ERROR:", e)
        print("Sidebar color decisions:", "PASS" if not errors else "FAIL")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
