#!/usr/bin/env python3
"""Build the standalone offline preview with inlined theme, density and component CSS."""
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "assets"


def render():
    result = (ASSETS / "preview.template.html").read_text(encoding="utf-8")
    for token, filename in (("THEMES", "themes.css"), ("SHOWCASE", "web-tokens.css"), ("DESKTOP", "desktop-tokens.css"), ("COMPONENTS", "components.css")):
        result = result.replace(f"/*__{token}__*/", (ASSETS / filename).read_text(encoding="utf-8"))
    return result

if __name__ == "__main__":
    target = ASSETS / "preview.html"
    target.write_text(render(), encoding="utf-8")
    print(f"Generated {target.relative_to(ROOT)}")
