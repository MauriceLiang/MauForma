#!/usr/bin/env python3
"""Check example theme contrast and CSS generation. Advisory only; not a rendering audit."""
import json
import re
import sys
from pathlib import Path
from generate_themes import render
from generate_preview import render as render_preview

ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"


def lum(s):
    if not re.fullmatch(r"#[0-9A-Fa-f]{6}", s):
        raise ValueError(f"Invalid #RRGGBB: {s}")
    rgb = [int(s[i:i+2], 16)/255 for i in (1, 3, 5)]
    vals = [x/12.92 if x <= 0.04045 else ((x+0.055)/1.055)**2.4 for x in rgb]
    return sum(a*b for a,b in zip(vals, (0.2126, 0.7152, 0.0722)))


def contrast(a, b):
    x, y = sorted((lum(a), lum(b)), reverse=True)
    return (x+0.05)/(y+0.05)


def main():
    data = json.loads((ASSETS / "theme-presets.json").read_text(encoding="utf-8"))
    problems = []
    expected = render(data)
    if (ASSETS / "themes.css").read_text(encoding="utf-8") != expected:
        problems.append("themes.css is out of date: run scripts/generate_themes.py")
    if (ASSETS / "preview.html").read_text(encoding="utf-8") != render_preview():
        problems.append("preview.html is out of date: run scripts/generate_preview.py")
    required = {"page-bg","surface","surface-soft","text","text-soft","text-muted", "border","control-border","focus","success","warning","danger","on-accent"}
    for scheme in ("light", "dark"):
        if missing := required - set(data["defaults"][scheme]):
            problems.append(f"Missing default {scheme} tokens: {sorted(missing)}")
    for name, entry in data["themes"].items():
        if not re.fullmatch(r"[a-z][a-z0-9-]*", name):
            problems.append(f"Invalid theme name {name}")
        for scheme in ("light", "dark"):
            palette = data["defaults"][scheme] | entry[scheme]
            for background in ("page-bg","surface","surface-soft"):
                for foreground in ("text","text-soft","text-muted"):
                    ratio = contrast(palette[foreground], palette[background])
                    if ratio < 4.5:
                        problems.append(f"{name}/{scheme}: {foreground} on {background}: {ratio:.2f} < 4.5")
                ratio = contrast(palette["accent"], palette[background])
                if ratio < 4.5:
                    problems.append(f"{name}/{scheme}: text link accent on {background}: {ratio:.2f} < 4.5")
                ratio = contrast(palette["control-border"], palette[background])
                if ratio < 3:
                    problems.append(f"{name}/{scheme}: significant control-border on {background}: {ratio:.2f} < 3")
            ratio = contrast(palette["on-accent"], palette["accent"])
            if ratio < 4.5:
                problems.append(f"{name}/{scheme}: on-accent on accent: {ratio:.2f} < 4.5")
            print(f"{name:8} {scheme:5} | accent contrast against surface {contrast(palette['accent'],palette['surface']):.2f}:1 | button text {ratio:.2f}:1")
    components = json.loads((ASSETS / "component-contracts.json").read_text(encoding="utf-8"))
    for c in components["components"]:
        if not all(c.get(k) for k in ("name", "responsibility", "variants", "states", "api", "a11y")):
            problems.append(f"Incomplete component contract: {c.get('name','unknown')}")
    if problems:
        print("\nFAILED:")
        for p in problems: print(" -", p)
        return 1
    print(f"\nPASS: {len(data['themes'])} themes, light/dark scheme, token CSS sync, component contract schema.")
    print("NOTE: Does not replace browser, keyboard, focus, or rendered visual QA.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
