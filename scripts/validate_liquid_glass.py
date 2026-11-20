#!/usr/bin/env python3
"""Check optional liquid-glass knowledge integration, not browser optical fidelity."""
from __future__ import annotations

from pathlib import Path
import argparse
import json
import sys

ROOT = Path(__file__).resolve().parents[1]
FILES = (
    "SKILL.md",
    "README.md",
    "references/liquid-glass-optics.md",
    "references/visual-tech-selection-12.md",
    "references/visual-qa.md",
    "assets/liquid-glass-layer-lab.html",
    "assets/visual-tech-catalog.json",
    "tests/liquid_glass_browser_smoke.mjs",
)
ROUTES = ("SKILL.md", "README.md", "references/visual-tech-selection-12.md", "references/visual-qa.md")
LAYER_MARKERS = ("透明", "折射", "高光", "阴影")
TECH_MARKERS = (
    "feDisplacementMap", "xChannelSelector", "yChannelSelector", "in2",
    "Canvas", "backdrop-filter", "scale", "WebGL", "prefers-reduced-motion",
    "fallback", "NOT TESTED",
)


def validate_repository(root: Path = ROOT) -> list[str]:
    issues = []
    contents = {}
    for item in FILES:
        file = root / item
        if not file.is_file():
            issues.append(f"Missing liquid glass resource: {item}")
            continue
        contents[item] = file.read_text("utf-8")
    if issues:
        return issues
    for route in ROUTES:
        if "references/liquid-glass-optics.md" not in contents[route]:
            issues.append(f"{route}: optional optics guide is not discoverable")
    skill = contents["SKILL.md"]
    if "only on request" not in skill.casefold() or "optional" not in skill.casefold():
        issues.append("Core skill must not turn liquid glass into a mandatory global skin")
    guide = contents["references/liquid-glass-optics.md"]
    for item in LAYER_MARKERS + TECH_MARKERS:
        if item not in guide:
            issues.append(f"Optics guide missing concept: {item}")
    for item in (
        "Safari", "Firefox", "Chromium", "透明", "折射", "高光", "阴影",
        "未自动验证", "data-refraction-attempt",
    ):
        # No requirement for Chromium literal in the demo: compatibility note is in the guide.
        source = guide if item in ("Safari", "Firefox", "Chromium") else contents["assets/liquid-glass-layer-lab.html"]
        if item not in source:
            issues.append(f"Guide/demo missing compatibility or state clue: {item}")
    lab = contents["assets/liquid-glass-layer-lab.html"]
    for item in (
        'id="opacity"', 'id="strength"', 'id="specular"', 'id="elevation"', 'id="blur"',
        'id="refract-toggle"', 'id="lg-displacement-image"',
        'id="lg-displacement"', 'pointer-events:none', 'aria-live="polite"',
    ):
        if item not in lab:
            issues.append(f"Demo lacks layer control/accessible fallback: {item}")
    try:
        data = json.loads(contents["assets/visual-tech-catalog.json"])
        tools = data["tools"]
        if len(tools) != 12:
            issues.append("Do not add a new animation library for optional glass; 12-tool catalog changed")
        native = next(x for x in tools if x["id"] == "svg-filter")
        if not all(t in native["keywords"] for t in ("液态玻璃", "liquid glass", "feDisplacementMap")):
            issues.append("SVG Filter catalog does not discover liquid glass prompts")
        if not any("液态玻璃" in x["goal"] for x in data["scenarios"]):
            issues.append("Visual technology scenarios cannot route liquid-glass user goals")
    except (ValueError, StopIteration, KeyError, TypeError) as exc:
        issues.append(f"Invalid visual-tech catalog integration: {exc}")
    # These tests do not assert actual pixel distortion; that remains browser/device-specific QA.
    return issues


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--repository", action="store_true")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    if not args.repository:
        p.error("Use --repository to validate static Skill integration")
    issues = validate_repository()
    if args.json:
        print(json.dumps({"passed": not issues, "issues": issues,
                          "scope": "documentation and demo-state contract only"}, ensure_ascii=False, indent=2))
    else:
        for err in issues:
            print("ERROR:", err)
        print("Liquid glass Skill integration:", "PASS" if not issues else "FAIL")
    return int(bool(issues))


if __name__ == "__main__":
    sys.exit(main())
