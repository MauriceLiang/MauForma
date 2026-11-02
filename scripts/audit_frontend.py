#!/usr/bin/env python3
"""Heuristic static UI risk scanner (not proof of visual quality or runtime accessibility)."""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

EXT = {".html", ".css", ".scss", ".vue", ".jsx", ".tsx"}
EXCLUDE = {"node_modules", "dist", "build", ".next", ".nuxt", ".git", "coverage", ".output"}
FINDINGS = [
    ("MF101", "high", re.compile(r"<(?:div|span)\b[^>]*\bonClick\s*=", re.I | re.S),
     "Clickable non-interactive element; use semantic button or verify keyboard behavior."),
    ("MF102", "medium", re.compile(r"<img\b(?![^>]*\balt\s*=)[^>]*>", re.I | re.S),
     "Image appears to lack alt; decorative images still need alt=\"\"."),
    ("MF103", "medium", re.compile(r"\btransition\s*:\s*all\b", re.I),
     "transition: all can animate unexpected properties; specify transform/opacity."),
    ("MF104", "medium", re.compile(r"\b(?:outline)\s*:\s*(?:none|0)\s*;", re.I),
     "Removed focus outline; verify visible :focus-visible replacement."),
    ("MF105", "low", re.compile(r"""href\s*=\s*["']#["']""", re.I),
     "Placeholder anchor may cause navigation and accessibility problems."),
]


def collect_files(base: Path) -> list[Path]:
    if base.is_file():
        return [base] if base.suffix in EXT else []
    return sorted(p for p in base.rglob("*") if p.is_file() and p.suffix in EXT
                  and not EXCLUDE.intersection(p.parts))


def scan(base: Path) -> list[dict]:
    items = collect_files(base)
    all_source = []
    findings = []
    for p in items:
        content = p.read_text("utf-8", errors="replace")
        all_source.append(content)
        try:
            display = str(p.relative_to(base if base.is_dir() else base.parent))
        except ValueError:
            display = str(p)
        for code, severity, pattern, message in FINDINGS:
            for match in pattern.finditer(content):
                line = content.count("\n", 0, match.start()) + 1
                if "mauforma-ignore" in content.splitlines()[line-1]:
                    continue
                findings.append({"code": code, "severity": severity,
                                 "path": display, "line": line, "message": message})
        if p.suffix in {".css", ".scss", ".vue"} and "tokens" not in p.name.casefold():
            color_matches = list(re.finditer(r"#[0-9a-fA-F]{6}\b", content))
            if len(color_matches) >= 6:
                findings.append({"code": "MF106", "severity": "low", "path": display,
                                 "line": 1, "message": "Many literal hex colors; inspect for duplicated design tokens."})
    if any(re.search(r"\banimation\s*:|@keyframes", src, re.I) for src in all_source):
        if not any("prefers-reduced-motion" in src for src in all_source):
            findings.append({"code": "MF107", "severity": "medium", "path": "(project)",
                             "line": 1, "message": "CSS animations found, but no reduced-motion handling detected in scanned files."})
    return sorted(findings, key=lambda f: (f["path"], f["line"], f["code"]))


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("path", help="Web source directory or file")
    parser.add_argument("--format", choices=["text", "json"], default="text")
    parser.add_argument("--strict", action="store_true", help="Return 1 when high-severity hints exist")
    args = parser.parse_args()
    base = Path(args.path).resolve()
    if not base.exists():
        parser.error(f"Not found: {base}")
    findings = scan(base)
    if args.format == "json":
        print(json.dumps({"count": len(findings), "findings": findings,
                          "scope": "heuristic static analysis only"}, ensure_ascii=False, indent=2))
    else:
        for f in findings:
            print(f"{f['path']}:{f['line']}: {f['code']} [{f['severity']}] {f['message']}")
        print(f"{len(findings)} potential issues. Human/browser review required.")
    return int(args.strict and any(f["severity"] == "high" for f in findings))


if __name__ == "__main__":
    raise SystemExit(main())
