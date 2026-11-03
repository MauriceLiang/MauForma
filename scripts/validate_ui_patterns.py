#!/usr/bin/env python3
"""Validate example sidebar palette contrast and UI-polish reference integrity.

This validates known color pairs and documentation contracts only. It is NOT a
rendering test, not a full WCAG audit, and cannot label any real design "AI-made".
"""
from __future__ import annotations
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PALETTE = ROOT / "assets/sidebar-palette-examples.json"
DOCS = (
    "references/sidebar-navigation-design.md",
    "references/workspace-component-refinement.md",
    "assets/sidebar-refinement-gallery.html",
    "tests/test_ui_patterns.py",
)
REQUIRED_ROLES = {
    "sidebar-bg", "sidebar-surface", "sidebar-hover", "sidebar-selected",
    "sidebar-text", "sidebar-text-muted", "sidebar-icon", "sidebar-border",
    "sidebar-focus", "sidebar-accent", "sidebar-muted-selected",
}


def luminance(color: str) -> float:
    if not re.fullmatch(r"#[0-9A-Fa-f]{6}", color):
        raise ValueError(f"Invalid hex color: {color}")
    values = [int(color[n:n + 2], 16) / 255.0 for n in (1, 3, 5)]
    transformed = [c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
                   for c in values]
    return sum(w * v for w, v in zip((0.2126, 0.7152, 0.0722), transformed))


def contrast(color_a: str, color_b: str) -> float:
    a, b = sorted((luminance(color_a), luminance(color_b)), reverse=True)
    return (a + 0.05) / (b + 0.05)


def validate(data: dict | None = None) -> list[str]:
    issues: list[str] = []
    for path in DOCS:
        if not (ROOT / path).is_file():
            issues.append("Missing UI-polish file: " + path)
    if data is None:
        try:
            data = json.loads(PALETTE.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            return issues + [f"Failed to read palette: {exc}"]
    for mode in ("dark", "light"):
        scheme = data.get("palettes", {}).get(mode)
        if not scheme:
            issues.append("Missing palette mode: " + mode)
            continue
        colors = scheme.get("colors", {})
        missing = REQUIRED_ROLES - colors.keys()
        if missing:
            issues.append(f"{mode}: missing sidebar roles {sorted(missing)}")
        for label, hex_color in colors.items():
            try:
                luminance(hex_color)
            except ValueError as exc:
                issues.append(f"{mode}/{label}: {exc}")
        for pair in scheme.get("test_pairs", []):
            if len(pair) != 3:
                issues.append(f"{mode}: invalid contrast pair {pair}")
                continue
            fg, bg, minimum = pair
            if fg not in colors or bg not in colors:
                issues.append(f"{mode}: unknown contrast role {pair}")
                continue
            try:
                measured = contrast(colors[fg], colors[bg])
                if measured < minimum:
                    issues.append(f"{mode}: {fg}/{bg} contrast {measured:.2f} < {minimum}")
            except ValueError as exc:
                issues.append(f"{mode}: {exc}")
    if (ROOT / "references/sidebar-navigation-design.md").is_file():
        text = (ROOT / "references/sidebar-navigation-design.md").read_text(encoding="utf-8")
        for term in ("aria-current", "focus-visible", "例外", "最近打开", "selected"):
            if term not in text:
                issues.append("Sidebar guide lacks semantic rule: " + term)
    if (ROOT / "assets/sidebar-refinement-gallery.html").is_file():
        gallery = (ROOT / "assets/sidebar-refinement-gallery.html").read_text(encoding="utf-8")
        for term in ("data-scheme", "aria-pressed", "aria-selected",
                     "prefers-reduced-motion", "data-select-group", "role=\"separator\""):
            if term not in gallery:
                issues.append("Gallery missing behavior/accessibility reference: " + term)
        if re.search(r"<script[^>]+\bsrc=", gallery, re.IGNORECASE):
            issues.append("Gallery should work without third-party script dependencies")
    if (ROOT / "SKILL.md").is_file():
        skill = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        for term in ("sidebar-navigation-design.md", "workspace-component-refinement.md"):
            if term not in skill:
                issues.append("SKILL.md missing UI-pattern task route: " + term)
    return issues


if __name__ == "__main__":
    errors = validate()
    for e in errors:
        print("ERROR:", e)
    print("Sidebar pattern validation:", "PASS" if not errors else "FAIL")
    raise SystemExit(bool(errors))
