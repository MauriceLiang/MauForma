#!/usr/bin/env python3
"""Static contract checks for universal page-header copy review.

These checks protect authored rules and synthetic expectations. They do not
classify real DOM text or validate a live site's visual correctness.
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
FIXTURES = ROOT / "assets/page-header-copy-cases.json"
ROLE_ACTION = {
    "decorative_explanation": "delete",
    "approved_brand_story": "keep",
    "mixed_brand_description": "split",
    "product_identity": "keep",
    "actual_chapter": "keep",
    "breadcrumb": "keep",
    "data_context": "move",
}
PRODUCT_TYPES = {
    "operate", "learning", "scientific_visualization", "creative",
    "marketing", "content", "data",
}
REQUIRED_SCENARIOS = {
    "legacy-workspace-explanation", "new-workspace-eyebrow",
    "legacy-learning-subtitle", "legacy-science-visualization",
    "legacy-creative-explanation", "marketing-approved-tagline",
    "marketing-unsupported-kicker", "legacy-mixed-brand-description",
    "product-name-in-header", "chapter-numbering",
    "legitimate-breadcrumb", "scope-and-period-label",
}


def validate_cases(data: dict) -> list[str]:
    errors: list[str] = []
    cases = data.get("cases")
    if not isinstance(cases, list):
        return ["cases must be a list"]
    ids: set[str] = set()
    product_types: set[str] = set()
    lifecycles: set[str] = set()
    for case in cases:
        if not isinstance(case, dict):
            errors.append("each case must be an object")
            continue
        cid = case.get("id", "")
        if not isinstance(cid, str) or not cid or cid in ids:
            errors.append("duplicate or missing case id")
            continue
        ids.add(cid)
        kind = case.get("product_type")
        product_types.add(kind)
        if kind not in PRODUCT_TYPES:
            errors.append(f"{cid}: invalid product type")
        lifecycle = case.get("lifecycle")
        lifecycles.add(lifecycle)
        if lifecycle not in {"existing", "new"}:
            errors.append(f"{cid}: invalid lifecycle")
        role = case.get("role")
        if role not in ROLE_ACTION:
            errors.append(f"{cid}: unknown semantic role")
        elif case.get("expected_action") != ROLE_ACTION[role]:
            errors.append(f"{cid}: incorrect expected action for {role}")
        if role in {"approved_brand_story", "product_identity", "mixed_brand_description"}:
            if case.get("approved") is not True:
                errors.append(f"{cid}: brand identity/story needs explicit evidence")
        for field in ("pretitle", "main_title", "reason"):
            if not isinstance(case.get(field), str) or not case[field].strip():
                errors.append(f"{cid}: missing {field}")
    if not REQUIRED_SCENARIOS.issubset(ids):
        errors.append("missing required cross-product scenario")
    if not PRODUCT_TYPES.issubset(product_types):
        errors.append("missing cross-product coverage")
    if lifecycles != {"existing", "new"}:
        errors.append("must cover both existing and new content")
    return errors


def validate_repo() -> list[str]:
    errors: list[str] = []
    if not FIXTURES.is_file():
        return [f"missing {FIXTURES.relative_to(ROOT)}"]
    data = json.loads(FIXTURES.read_text(encoding="utf-8"))
    errors.extend(validate_cases(data))
    required_fragments = {
        "SKILL.md": ("page-header-antipatterns.md", "跨产品页头文案门禁", "现有", "新旧文案验收"),
        "references/page-header-antipatterns.md": ("Gate H-Base", "Gate H0", "历史", "keep / merge / move / delete"),
        "references/proactive-visual-defect-discovery-gate.md": ("Gate H-Base", "原有及新增"),
        "references/semantic-copy-hygiene.md": ("跨产品页头文案门禁", "历史沿用", "Gate H-Base/H0"),
        "README.md": ("页头文案审查", "原有及新增"),
    }
    for path, fragments in required_fragments.items():
        target = ROOT / path
        if not target.is_file():
            errors.append(f"missing policy file: {path}")
            continue
        content = target.read_text(encoding="utf-8")
        for fragment in fragments:
            if fragment not in content:
                errors.append(f"{path}: missing cross-product gate contract: {fragment}")
    return errors


if __name__ == "__main__":
    issues = validate_repo()
    for issue in issues:
        print("ERROR:", issue)
    print("Page-header copy contract errors:", len(issues))
    sys.exit(1 if issues else 0)
