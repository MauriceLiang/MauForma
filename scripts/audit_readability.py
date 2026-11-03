#!/usr/bin/env python3
"""Advisory audit for user-facing microcopy and typography in frontend source.

This script identifies review candidates, NOT objective design errors or proof
of a WCAG failure. Font sizes in rem assume a 16px root for hints only.
Never automatically delete text based on these results.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT / "assets/typography-role-guidelines.json"
EXTENSIONS = {".css", ".scss", ".sass", ".less", ".html", ".vue", ".jsx", ".tsx", ".svelte", ".astro"}
IGNORE_DIRS = {".git", "node_modules", "dist", "build", ".next", ".nuxt", ".svelte-kit", "coverage"}
PATTERNS = [
    ("decorative-section-index", re.compile(r"(?<!\d)(?:0?[1-9]|[1-9]\d)\s*[/／|]\s*(?:总览|概览|工作台|分析|数据|洞察)(?![\w])", re.I),
     "Check whether this numbered overline encodes a real step, chapter or order."),
    ("generic-brand-subtitle", re.compile(r"\b(?:ANALYSIS\s+STUDIO|SMART\s+DASHBOARD|INSIGHT\s+WORKSPACE|DATA\s+STUDIO)\b", re.I),
     "Check whether this is an approved product name rather than decorative English."),
    ("developer-notes-visible", re.compile(r"(?:ECharts\s*(?:tooltip|brush|zoom)|保留原生.{0,35}(?:tooltip|缩放与点选)|(?:React|Vue)\s*组件(?:库)?)", re.I),
     "Check whether an implementation detail has leaked into user-facing copy."),
]
FONT_DECLARATION = re.compile(r"\bfont-size\s*:\s*(\d+(?:\.\d+)?)\s*(px|rem)\b", re.I)
FONT_TAILWIND = re.compile(r"\btext-\[\s*(\d+(?:\.\d+)?)px\s*\]")
FONT_INLINE = re.compile(r"\bfontSize\s*:\s*(\d+(?:\.\d+)?)\b")
RECOMMEND_REVIEW_BELOW_PX = 12


def analyze(text: str, path: str = "<input>") -> list[dict]:
    findings: list[dict] = []
    for line_num, line in enumerate(text.splitlines(), 1):
        snippet = line.strip()[:190]
        for name, pattern, reason in PATTERNS:
            if pattern.search(line):
                findings.append({"file": path, "line": line_num, "rule": name,
                                 "level": "review", "reason": reason, "excerpt": snippet})
        for match in FONT_DECLARATION.finditer(line):
            px = float(match.group(1)) * (16 if match.group(2).lower() == "rem" else 1)
            if px < RECOMMEND_REVIEW_BELOW_PX:
                findings.append({"file": path, "line": line_num, "rule": "potentially-tiny-text",
                                 "level": "review", "reason": f"Approx. {px:g}px; check role, actual font metrics and zoom. Not an automatic violation.",
                                 "excerpt": snippet})
        for match in FONT_TAILWIND.finditer(line):
            if float(match.group(1)) < RECOMMEND_REVIEW_BELOW_PX:
                findings.append({"file": path, "line": line_num, "rule": "potentially-tiny-text",
                                 "level": "review", "reason": f"Tailwind arbitrary {match.group(1)}px; check actual readability.",
                                 "excerpt": snippet})
        for match in FONT_INLINE.finditer(line):
            if float(match.group(1)) < RECOMMEND_REVIEW_BELOW_PX:
                findings.append({"file": path, "line": line_num, "rule": "potentially-tiny-text",
                                 "level": "review", "reason": f"Inline font size {match.group(1)}px; check actual readability.",
                                 "excerpt": snippet})
    unique: dict[tuple, dict] = {}
    for item in findings:
        unique[item["file"], item["line"], item["rule"]] = item
    return list(unique.values())


def scan(path: Path, max_files: int = 2000) -> list[dict]:
    if not path.exists():
        raise FileNotFoundError(f"Path not found: {path}")
    if path.is_file():
        files = [path] if path.suffix.lower() in EXTENSIONS else []
    else:
        files = sorted(p for p in path.rglob("*") if p.is_file() and p.suffix.lower() in EXTENSIONS
                       and not (set(p.relative_to(path).parts) & IGNORE_DIRS))
    findings: list[dict] = []
    for file in files[:max_files]:
        try:
            content = file.read_text("utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        findings.extend(analyze(content, str(file)))
    return findings


def validate_catalog(data: dict | None = None) -> list[str]:
    errors: list[str] = []
    if data is None:
        try:
            data = json.loads(CATALOG.read_text("utf-8"))
        except (OSError, ValueError) as exc:
            return [f"Could not parse type roles: {exc}"]
    profiles = data.get("profiles", [])
    if len(profiles) < 2:
        errors.append("Need Operate and Persuade profiles")
    ids = [p.get("id") for p in profiles]
    if len(set(ids)) != len(ids):
        errors.append("Duplicate typography profile ID")
    for p in profiles:
        roles = p.get("roles", [])
        role_ids = [r.get("id") for r in roles]
        if len(role_ids) != len(set(role_ids)):
            errors.append(f"{p.get('id')}: duplicate role")
        if not roles:
            errors.append(f"{p.get('id')}: no typography roles")
        for role in roles:
            lo, typical, hi = (role.get(k) for k in ("min_px", "recommended_px", "max_px"))
            if not all(isinstance(v, (int, float)) for v in (lo, typical, hi)) or not 10 <= lo <= typical <= hi <= 120:
                errors.append(f"{p.get('id')}/{role.get('id')}: size range must be ordered")
            line_height = role.get("line_height", 0)
            if not isinstance(line_height, (int, float)) or not 1.0 <= line_height <= 2:
                errors.append(f"{p.get('id')}/{role.get('id')}: invalid line height")
    workspace = next((x for x in profiles if x.get("id") == "operate-desktop"), {})
    required = {"page-title", "section-title", "body", "navigation", "metric-value",
                "metric-label", "chart-axis", "chart-legend", "metadata", "control-label"}
    missing = required - {role.get("id") for role in workspace.get("roles", [])}
    if missing:
        errors.append(f"Missing workspace type roles: {sorted(missing)}")
    for doc in ("references/semantic-copy-hygiene.md", "references/typography-hierarchy.md",
                "assets/typography-reading-lab.html", "scripts/audit_readability.py",
                "tests/test_content_typography.py"):
        if not (ROOT / doc).is_file():
            errors.append(f"Missing typography artifact: {doc}")
    skill = (ROOT / "SKILL.md").read_text("utf-8") if (ROOT / "SKILL.md").is_file() else ""
    for ref in ("semantic-copy-hygiene.md", "typography-hierarchy.md", "audit_readability.py"):
        if ref not in skill:
            errors.append(f"SKILL lacks typography route: {ref}")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser(description="Review candidate tiny text and ornamental labels; no automatic changes")
    parser.add_argument("path", nargs="?", type=Path)
    parser.add_argument("--format", choices=("text", "json"), default="text")
    parser.add_argument("--validate-catalog", action="store_true")
    args = parser.parse_args()
    if args.validate_catalog:
        errors = validate_catalog()
        if args.format == "json":
            print(json.dumps({"passed": not errors, "errors": errors}, ensure_ascii=False, indent=2))
        else:
            for error in errors:
                print("ERROR:", error)
            print("Microcopy / typography references:", "PASS" if not errors else "FAIL")
        return int(bool(errors))
    if args.path is None:
        parser.error("Provide frontend source path, or --validate-catalog")
    try:
        findings = scan(args.path)
    except FileNotFoundError as exc:
        parser.error(str(exc))
    if args.format == "json":
        print(json.dumps({"findings": findings, "count": len(findings),
                          "scope": "Advisory static hints, not WCAG compliance or visual QA"}, ensure_ascii=False, indent=2))
    else:
        for f in findings:
            print(f"{f['file']}:{f['line']}: [{f['rule']}] {f['reason']}")
        print(f"{len(findings)} review candidates. Review manually; do not auto-delete.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
