#!/usr/bin/env python3
"""Preview or initialize a page-aware MauForma design system. No overwrite by default."""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "assets/style-knowledge.json"
SOURCES = ("confirmed", "delegated", "inherited", "unresolved")
MODES = ("Persuade", "Operate", "Read", "Experience")


def make_plan(project: Path, name: str, style: str = "", source: str = "delegated",
              page: str = "", mode: str = "", density: str = "") -> dict[Path, str]:
    if not name.strip():
        raise ValueError("Project name is required")
    if source not in SOURCES:
        raise ValueError(f"Unknown source: {source}")
    styles = {s["id"]: s for s in json.loads(DB.read_text("utf-8"))["styles"]}
    if style and style not in styles:
        raise ValueError(f"Unknown style ID: {style}")
    if page and not re.fullmatch(r"[a-zA-Z0-9][a-zA-Z0-9_-]{0,63}", page):
        raise ValueError("Page must be a safe slug (letters, numbers, - and _)")
    if mode and mode not in MODES:
        raise ValueError(f"Unknown page mode: {mode}")
    selected = styles.get(style)
    design_dir = project / "design-system"
    choice_source = source if style else "unresolved"
    decision = lambda value, state: {"value": value, "source": state}
    brief = {
        "project": {"name": name, "kind": "web"},
        "decisions": {
            "visual_style": decision(style or "unresolved", choice_source),
            "information_density": decision(density or "unresolved", source if density else "unresolved"),
            "primary_focus": decision("unresolved", "unresolved"),
            "selected_direction": decision(style or "unresolved", choice_source),
        },
        "constraints": [], "open_questions": ["Confirm content, focal point and user goals"],
    }
    guidance = selected["why"] if selected else "Not selected: first ask about website purpose, content and visitor actions."
    master = (
        f"# {name} · Design System MASTER\n\n"
        f"- **Design direction**: {style or 'pending'} ({choice_source})\n"
        f"- **Reason**: {guidance}\n"
        "- **Scope**: product-wide typography, semantic colors, spacing, radius, motion, component contracts\n"
        "- **Shared components first**: Button / Field / Dialog / PageHeader / Navigation / Feedback\n"
        "- **A11y / reduced-motion**: must work independently of animation libraries\n"
        "- **Page overrides**: only record deviations; do not redefine shared token ownership\n"
        "- **Source tracking**: never convert an AI recommendation into confirmed without user selection\n"
        "\n## Pending design decisions\n\n- Actual content and user tasks\n- Theme colors and typography\n"
        "- User-approved assets\n- Component / framework inventory\n"
    )
    result = {
        design_dir / "MASTER.md": master,
        design_dir / "decisions.json": json.dumps(brief, ensure_ascii=False, indent=2) + "\n",
    }
    if page:
        result[design_dir / "pages" / f"{page}.md"] = (
            f"# Page override: {page}\n\n"
            "- **Inherits**: ../MASTER.md tokens and shared component contracts\n"
            f"- **Primary mode**: {mode or 'not yet decided'}\n"
            f"- **Density**: {density or 'not yet decided'}\n"
            "- **Visual focus / layout / motion**: describe only actual deviations from MASTER\n"
            "- **Decision provenance**: state confirmed/delegated/inherited/unresolved on every choice\n"
            "- **Acceptance**: responsive, keyboard, reduced-motion and actual flow\n"
        )
    return result


def write_plan(plan: dict[Path, str], apply: bool, force: bool = False) -> list[Path]:
    if apply:
        existing = [p for p in plan if p.exists()]
        if existing and not force:
            raise FileExistsError("Existing files preserved; refusing overwrite: " + ", ".join(str(p) for p in existing))
        for p, text in plan.items():
            p.parent.mkdir(parents=True, exist_ok=True)
            p.write_text(text, encoding="utf-8")
    return list(plan)


def main() -> int:
    p = argparse.ArgumentParser(description="Preview-first design-system initializer; does not overwrite by default")
    p.add_argument("--project-root", required=True, type=Path)
    p.add_argument("--name", required=True)
    p.add_argument("--style", default="", help="Chosen profile ID, if known")
    p.add_argument("--source", choices=SOURCES, default="delegated",
                   help="Use confirmed only when the user explicitly selected the direction")
    p.add_argument("--page", default="", help="Optional page slug")
    p.add_argument("--mode", choices=MODES, default="")
    p.add_argument("--density", default="")
    p.add_argument("--apply", action="store_true", help="Write files (otherwise preview only)")
    p.add_argument("--force", action="store_true", help="Explicitly overwrite existing files")
    args = p.parse_args()
    root = args.project_root.resolve()
    if not root.is_dir():
        p.error("Project root must be an existing directory")
    if args.force and not args.apply:
        p.error("--force requires --apply")
    try:
        plan = make_plan(root, args.name, args.style, args.source, args.page, args.mode, args.density)
        paths = write_plan(plan, args.apply, args.force)
    except (ValueError, FileExistsError) as exc:
        p.error(str(exc))
    print(("WROTE" if args.apply else "PREVIEW ONLY") + f" {len(paths)} files")
    for file in paths:
        print("-", file)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
