#!/usr/bin/env python3
"""Validate generic surface decisions and atomic control contracts, not visual aesthetics."""
from __future__ import annotations
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXAMPLE = ROOT / "assets/surface-control-patterns.json"
MODES = {"Operate", "Persuade", "Read", "Experience"}
PATTERNS = {"open-collection", "single-panel", "entity-cards", "editorial-flow", "split-workspace", "hero-stage", "mega-card"}
BEHAVIORS = {"atomic", "semantic-wrap"}
FALLBACKS = {"group-wrap", "reflow-row", "overflow-menu", "stack", "accessible-scroll"}
REQUIRED = (
    "references/surface-architecture-gate.md",
    "references/control-geometry-gate.md",
    "assets/surface-control-patterns.json",
    "assets/surface-control-layout-lab.html",
    "scripts/validate_surface_control.py",
    "tests/test_surface_control.py",
    "tests/surface_control_browser_smoke.mjs",
)


def validate_plan(data: object, require_modes: bool = False) -> list[str]:
    errors: list[str] = []
    if not isinstance(data, dict) or data.get("schema_version") != "1.0":
        return ["Unsupported surface/control contract version"]
    profiles = data.get("profiles")
    if not isinstance(profiles, list) or not profiles:
        return ["Need at least one profile"]
    seen: set[str] = set()
    modes: set[str] = set()
    for p in profiles:
        if not isinstance(p, dict):
            errors.append("Invalid profile entry")
            continue
        pid = p.get("id")
        if not isinstance(pid, str) or not pid.strip() or pid in seen:
            errors.append("Profile IDs must be unique and nonempty")
        seen.add(pid)
        if p.get("mode") not in MODES:
            errors.append(f"{pid}: invalid page mode")
        else:
            modes.add(p["mode"])
        if not isinstance(p.get("goal"), str) or len(p["goal"].strip()) < 12:
            errors.append(f"{pid}: must define user decision/task")
        surfaces = p.get("surfaces")
        if not isinstance(surfaces, list) or not surfaces:
            errors.append(f"{pid}: no surface decisions")
            surfaces = []
        surface_ids = {s.get("id") for s in surfaces if isinstance(s, dict)}
        if len(surface_ids) != len(surfaces) or None in surface_ids:
            errors.append(f"{pid}: duplicate or missing surface IDs")
        for s in surfaces:
            if not isinstance(s, dict):
                errors.append(f"{pid}: invalid surface")
                continue
            sid = s.get("id")
            if s.get("pattern") not in PATTERNS or s.get("pattern") == "mega-card":
                errors.append(f"{pid}/{sid}: choose an intentional surface pattern, not 'mega-card' as a default")
            if not s.get("reason") or not s.get("rejected_pattern") or not s.get("rejected_reason"):
                errors.append(f"{pid}/{sid}: explain selected and rejected plausible alternatives")
            nested = s.get("nested_of")
            if nested is not None and (nested == sid or nested not in surface_ids or not s.get("nested_reason")):
                errors.append(f"{pid}/{sid}: nested surface needs a valid parent and independent reason")
        controls = p.get("controls")
        if not isinstance(controls, list) or not controls:
            errors.append(f"{pid}: no control geometry contract")
            controls = []
        for c in controls:
            if not isinstance(c, dict):
                errors.append(f"{pid}: invalid control entry")
                continue
            cid = c.get("id")
            if not cid or not c.get("label") or not c.get("kind"):
                errors.append(f"{pid}: control needs ID, label, and kind")
            if c.get("behavior") not in BEHAVIORS:
                errors.append(f"{pid}/{cid}: behavior must be atomic or semantic-wrap")
            if c.get("fallback") not in FALLBACKS:
                errors.append(f"{pid}/{cid}: specify safe responsive fallback (no clipping/letter stacking)")
            states = c.get("states")
            if not isinstance(states, list) or not {"default", "focus-visible"}.issubset(set(states)):
                errors.append(f"{pid}/{cid}: default and focus-visible states required")
    if require_modes and modes != MODES:
        errors.append("Generic catalog must include all four Web page modes")
    return errors


def validate_repository() -> list[str]:
    errors = [f"Missing resource: {p}" for p in REQUIRED if not (ROOT/p).is_file()]
    if errors:
        return errors
    skill = (ROOT/"SKILL.md").read_text("utf-8")
    for route in ("surface-architecture-gate.md", "control-geometry-gate.md", "validate_surface_control.py"):
        if route not in skill:
            errors.append("SKILL.md missing mandatory route: " + route)
    try:
        errors.extend(validate_plan(json.loads(EXAMPLE.read_text("utf-8")), require_modes=True))
    except (OSError, ValueError) as e:
        errors.append(str(e))
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Surface architecture and atomic control intent review (static only)")
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--repository", action="store_true")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if not args.repository and not args.path:
        parser.error("Provide a JSON plan or --repository")
    errors = validate_repository() if args.repository else []
    if args.path:
        try:
            errors.extend(validate_plan(json.loads(args.path.read_text("utf-8"))))
        except (OSError, ValueError) as e:
            errors.append(str(e))
    if args.json:
        print(json.dumps({"passed": not errors, "issues": errors, "scope": "design intent only; not rendered geometry or aesthetic approval"}, ensure_ascii=False, indent=2))
    else:
        for e in errors: print("ERROR:", e)
        print("Surface/control plan:", "PASS" if not errors else "FAIL")
    return int(bool(errors))


if __name__ == "__main__":
    raise SystemExit(main())
