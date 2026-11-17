#!/usr/bin/env python3
"""Verify MauForma's authored card edge-accent gate with synthetic cases.

This validator checks the rule contract and fixture expectations, NOT actual
image pixels, DOM geometry or project-specific artistic judgment.
"""
from __future__ import annotations

import json
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]
CASES_FILE = ROOT / "assets/surface-edge-accent-cases.json"
SURFACES = {"card", "panel", "section", "timeline", "chart"}
CARD_SURFACES = {"card", "panel", "section"}
FLUSH = {"flush_border", "flush_pseudo", "flush_gradient", "flush_inset_shadow", "flush_mask", "overlapping_rail"}
ALLOWED = {"none", "external_rail", "focus_outline", "data_track"}
REQUIRED = {
    "new-card-left-border", "legacy-panel-left-border", "new-card-pseudo-before",
    "legacy-card-pseudo-after", "new-section-gradient",
    "legacy-card-inset-shadow", "new-card-mask", "legacy-panel-external-node-overlap",
    "new-card-external-no-gap", "legacy-card-too-small-gap",
    "legacy-card-redundant-rail", "new-panel-neutral", "legacy-card-neutral",
    "new-card-external-gap", "legacy-section-external-gap", "new-card-focus-outline",
    "semantic-timeline-track", "semantic-chart-bar", "new-panel-status-flush",
}


def expected_decision(case: dict) -> str:
    pattern = case.get("pattern")
    surface = case.get("surface")
    if pattern in FLUSH:
        return "reject"
    if pattern == "none":
        return "accept"
    if pattern == "focus_outline":
        return "accept" if case.get("meaningful") is True else "reject"
    if pattern == "data_track":
        return "accept" if surface in {"timeline", "chart"} and case.get("meaningful") is True else "reject"
    if pattern == "external_rail":
        gap = case.get("gap_px")
        return "accept" if (surface in CARD_SURFACES and case.get("meaningful") is True
                            and isinstance(gap, (int, float)) and not isinstance(gap, bool)
                            and gap >= 4) else "reject"
    return "reject"


def validate_cases(data: dict) -> list[str]:
    problems: list[str] = []
    cases = data.get("cases")
    if not isinstance(cases, list):
        return ["cases must be a list"]
    seen: set[str] = set()
    types: set[str] = set()
    lifecycles: set[str] = set()
    patterns: set[str] = set()
    for c in cases:
        if not isinstance(c, dict):
            problems.append("invalid case object")
            continue
        cid = c.get("id")
        if not isinstance(cid, str) or not cid or cid in seen:
            problems.append("duplicate or missing case ID")
            continue
        seen.add(cid)
        surface = c.get("surface")
        types.add(surface)
        if surface not in SURFACES:
            problems.append(f"{cid}: unknown surface")
        lifecycle = c.get("lifecycle")
        lifecycles.add(lifecycle)
        if lifecycle not in {"new", "existing"}:
            problems.append(f"{cid}: invalid lifecycle")
        pattern = c.get("pattern")
        patterns.add(pattern)
        if pattern not in FLUSH | ALLOWED:
            problems.append(f"{cid}: unknown pattern")
        if not isinstance(c.get("meaningful"), bool):
            problems.append(f"{cid}: missing meaningful boolean")
        for key in ("reason",):
            if not isinstance(c.get(key), str) or not c[key].strip():
                problems.append(f"{cid}: missing {key}")
        if c.get("expected") != expected_decision(c):
            problems.append(f"{cid}: incorrect expected decision for {pattern}")
    if not REQUIRED.issubset(seen):
        problems.append("missing required positive/negative synthetic cases")
    if not CARD_SURFACES.issubset(types):
        problems.append("missing Card/Panel/Section coverage")
    if lifecycles != {"new", "existing"}:
        problems.append("both new and existing page coverage required")
    if not FLUSH.issubset(patterns):
        problems.append("missing attached accent implementation")
    return problems


def validate_repo() -> list[str]:
    if not CASES_FILE.exists():
        return ["missing synthetic accent cases"]
    errors = validate_cases(json.loads(CASES_FILE.read_text(encoding="utf-8")))
    expected = {
        "SKILL.md": ("surface-edge-accent-gate.md", "卡片彩色贴边条否决项", "新建/优化"),
        "references/surface-edge-accent-gate.md": ("Gate S0", "默认", "已有", "边框", "外置"),
        "references/surface-architecture-gate.md": ("surface-edge-accent-gate.md", "彩色"),
        "references/proactive-visual-defect-discovery-gate.md": ("surface-edge-accent-gate.md", "原有和新增"),
        "references/component-craft-gate.md": ("surface-edge-accent-gate.md",),
        "references/visual-critique-loop.md": ("surface-edge-accent-gate.md",),
        "README.md": ("surface-edge-accent-gate.md", "新建页面", "既有"),
    }
    for name, fragments in expected.items():
        p = ROOT / name
        if not p.is_file():
            errors.append(f"missing policy file: {name}")
            continue
        content = p.read_text(encoding="utf-8")
        for f in fragments:
            if f not in content:
                errors.append(f"{name}: missing surface edge-accent contract: {f}")
    return errors


if __name__ == "__main__":
    errors = validate_repo()
    for error in errors:
        print("ERROR:", error)
    print("Surface edge-accent contract errors:", len(errors))
    sys.exit(1 if errors else 0)
