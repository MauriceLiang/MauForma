#!/usr/bin/env python3
"""Validate original MauForma style knowledge, provenance and required task routes."""
from __future__ import annotations
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NEEDED = [
    "assets/style-knowledge.json", "references/design-style-catalog.md",
    "references/comparison-page-design.md", "references/chart-interior-alignment.md",
    "references/repovantage-comparison-case.md", "assets/comparison-reference-cases.json",
    "assets/comparison-contract.schema.json", "assets/comparison-layout-lab.html",
    "examples/comparison-contract-repovantage.json", "scripts/validate_comparison_contract.py",
    "scripts/audit_comparison_ui.mjs", "tests/test_comparison_contract.py",
    "references/grid-alignment-and-viewport-safety.md",
    "references/repovantage-release-alignment-case.md",
    "assets/layout-integrity-patterns.json", "assets/layout-integrity.schema.json",
    "examples/layout-integrity-repovantage.json", "assets/grid-and-viewport-lab.html",
    "scripts/validate_layout_integrity.py", "scripts/audit_rendered_layout.mjs",
    "tests/test_layout_integrity.py",
    "references/page-density-and-content-priority.md", "references/whitespace-and-surface-composition.md",
    "references/repovantage-overview-density-case.md", "assets/page-density-profiles.json",
    "assets/page-content-plan.schema.json", "assets/page-density-lab.html",
    "examples/page-content-plan-repovantage.json", "scripts/validate_page_content_plan.py",
    "tests/test_page_content_plan.py",
    "references/navigation-architecture.md", "assets/navigation-pattern-catalog.json",
    "assets/navigation-decision.schema.json", "assets/navigation-layout-lab.html",
    "examples/navigation-decision.pending.json",
    "scripts/validate_navigation_architecture.py", "tests/test_navigation_architecture.py",
    "references/sidebar-color-discovery.md", "references/sidebar-color-reference-cases.md",
    "examples/sidebar-color-discovery-dialogues.md", "assets/sidebar-color-directions.json",
    "assets/sidebar-color-preview.html", "assets/sidebar-color-decision.schema.json",
    "examples/sidebar-color-decision.pending.json",
    "scripts/validate_sidebar_color_decision.py", "tests/test_sidebar_color_choice.py",
    "references/semantic-copy-hygiene.md", "references/typography-hierarchy.md",
    "assets/typography-role-guidelines.json", "assets/typography-reading-lab.html",
    "scripts/audit_readability.py", "tests/test_content_typography.py",
    "assets/composition-brief.schema.json", "examples/composition/repo-analysis.json",
    "assets/composition-layout-lab.html", "references/composition-first-design.md",
    "references/palette-art-direction.md", "references/visual-critique-loop.md",
    "scripts/validate_composition_brief.py", "tests/test_composition_brief.py",
    "references/aesthetic-authorship.md", "references/art-direction-critique.md",
    "references/design-dna-protocol.md", "references/project-design-hierarchy.md",
    "references/react-component-engineering.md", "references/vue-component-engineering.md",
    "references/browser-qa-protocol.md", "scripts/search_design_knowledge.py",
    "scripts/audit_frontend.py", "tests/test_design_intelligence.py",
    "scripts/init_design_system.py", "tests/test_design_system_manager.py",
    "scripts/browser_qa.mjs",
    "scripts/search_design_cases.py", "references/external-design-case-library.md",
    "assets/external-design-cases.json", "tests/test_external_design_cases.py",
    "references/sidebar-navigation-design.md", "references/workspace-component-refinement.md",
    "assets/sidebar-palette-examples.json", "assets/sidebar-refinement-gallery.html",
    "scripts/validate_ui_patterns.py", "tests/test_ui_patterns.py",
    "assets/visual-tech-catalog.json", "references/visual-tech-selection-12.md",
    "scripts/search_visual_tech.py", "tests/test_visual_tech_selection.py",
]
REQUIRED_FIELDS = {
    "id", "name", "modes", "sites", "keywords", "first_impression",
    "layout", "typography", "palette", "motion", "dials", "assets",
    "why", "tradeoffs", "good_case", "bad_case", "source_urls", "origin",
}


def validate() -> list[str]:
    errors = [f"Missing {p}" for p in NEEDED if not (ROOT / p).is_file()]
    try:
        data = json.loads((ROOT / "assets/style-knowledge.json").read_text("utf-8"))
        styles = data["styles"]
        if len(styles) != 8:
            errors.append(f"Expected 8 independent styles, got {len(styles)}")
        ids = [s["id"] for s in styles]
        if len(ids) != len(set(ids)):
            errors.append("Duplicate style ID")
        for s in styles:
            missing = REQUIRED_FIELDS - s.keys()
            if missing:
                errors.append(f"{s.get('id','?')} missing {sorted(missing)}")
                continue
            if not s["why"] or not s["good_case"] or not s["bad_case"] or not s["source_urls"]:
                errors.append(f"Missing why/examples/provenance for {s['id']}")
            for dial, bounds in s["dials"].items():
                if dial not in ("variance", "motion", "density") or len(bounds) != 2 or not 0 <= bounds[0] <= bounds[1] <= 10:
                    errors.append(f"Invalid {dial} for {s['id']}")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f"Invalid knowledge data: {exc}")
    try:
        external = json.loads((ROOT / "assets/external-design-cases.json").read_text("utf-8"))
        examples = external["cases"]
        if len(examples) != 84:
            errors.append(f"External source index expected 84 records, got {len(examples)}")
        if len({x["id"] for x in examples}) != len(examples):
            errors.append("Duplicate external design case id")
        for case in examples:
            if case["review_status"] not in ("sampled", "candidate", "indexed_unreviewed"):
                errors.append("Bad external review status: " + case["id"])
            if not case["source_url"].startswith(
                "https://github.com/VoltAgent/awesome-design-md/blob/" + external["source_snapshot_sha"] + "/design-md/"
            ):
                errors.append("Unpinned or unexpected source: " + case["id"])
            if case["source_type"] != "third_party_design_analysis_not_brand_official":
                errors.append("Official-brand confusion: " + case["id"])
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f"External case index error: {exc}")
    try:
        visual = json.loads((ROOT / "assets/visual-tech-catalog.json").read_text("utf-8"))
        tools = visual["tools"]
        if len(tools) != 12 or len({t["id"] for t in tools}) != 12:
            errors.append("Expected 12 distinct visual technologies")
        required = {"id", "name", "kind", "keywords", "goal", "best_for", "avoid", "combines_with",
                    "lightweight_alternative", "frameworks", "perf", "api", "coverage"}
        for tool in tools:
            if not required.issubset(tool):
                errors.append("Incomplete visual technology: " + str(tool.get("id")))
            if not tool["api"].startswith("https://"):
                errors.append("Missing official HTTPS source: " + tool["id"])
        ids = {t["id"] for t in tools} | {"native-css", "native-svg"}
        if len(visual["scenarios"]) != 9:
            errors.append("Expected 9 scenario combinations")
        for combo in visual["scenarios"]:
            if not set(combo["recommended"] + combo["optional"]).issubset(ids):
                errors.append("Unknown technology in scenario " + combo["id"])
        native = next((t for t in tools if t["id"] == "svg-filter"), {})
        if native.get("kind") != "browser-native":
            errors.append("SVG Filter must remain a native browser technique")
    except (OSError, ValueError, KeyError, TypeError) as exc:
        errors.append(f"Visual technology catalog error: {exc}")
    try:
        from validate_ui_patterns import validate as validate_ui
        errors.extend(validate_ui())
    except (ImportError, OSError, ValueError) as exc:
        errors.append(f"UI-pattern validation unavailable: {exc}")
    try:
        from validate_composition_brief import validate_repository as validate_composition
        errors.extend(validate_composition())
    except (ImportError, OSError, ValueError) as exc:
        errors.append(f"Composition validation unavailable: {exc}")
    try:
        from audit_readability import validate_catalog as validate_typography
        errors.extend(validate_typography())
    except (ImportError, OSError, ValueError) as exc:
        errors.append(f"Typography validation unavailable: {exc}")
    try:
        from validate_sidebar_color_decision import validate_repository as validate_sidebar_colors
        errors.extend(validate_sidebar_colors())
    except (ImportError, OSError, ValueError) as exc:
        errors.append(f"Sidebar user color choice validation unavailable: {exc}")
    try:
        from validate_navigation_architecture import validate_repository as validate_navigation
        errors.extend(validate_navigation())
    except (ImportError, OSError, ValueError) as exc:
        errors.append(f"Navigation architecture validation unavailable: {exc}")
    try:
        from validate_page_content_plan import validate_repository as validate_page_content
        errors.extend(validate_page_content())
    except (ImportError, OSError, ValueError) as exc:
        errors.append(f"Page content priority validation unavailable: {exc}")
    try:
        from validate_layout_integrity import validate_repository as validate_alignment
        errors.extend(validate_alignment())
    except (ImportError, OSError, ValueError) as exc:
        errors.append(f"Grid and scroll-end safety validation unavailable: {exc}")
    try:
        from validate_comparison_contract import validate_repository as validate_comparison
        errors.extend(validate_comparison())
    except (ImportError, OSError, ValueError) as exc:
        errors.append(f"Comparison data and plot integrity validation unavailable: {exc}")
    skill = (ROOT / "SKILL.md").read_text("utf-8")
    for needed in ("search_design_knowledge.py", "art-direction-critique.md", "browser-qa-protocol.md", "project-design-hierarchy.md", "search_design_cases.py", "external-design-case-library.md", "search_visual_tech.py", "visual-tech-selection-12.md"):
        if needed not in skill:
            errors.append(f"SKILL.md missing task route: {needed}")
    return errors


if __name__ == "__main__":
    errors = validate()
    for issue in errors:
        print("ERROR:", issue)
    print("MauForma design intelligence:", "PASS" if not errors else "FAIL")
    raise SystemExit(bool(errors))
