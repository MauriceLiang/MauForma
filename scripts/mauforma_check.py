#!/usr/bin/env python3
"""Changed-file static UX checks, normalized evidence, scoped waivers and honest exit status.
Does not install hooks or claim browser or aesthetic verification.
"""
from __future__ import annotations
import argparse
import json
import sys
from datetime import date
from pathlib import Path
from audit_frontend import scan, collect_files, EXT
from audit_readability import analyze as analyze_copy

def inspect(root: Path, changed: list[str], waivers: list[dict]) -> dict:
    findings = []
    invalid_waivers = []
    today = date.today()
    for waiver in waivers:
        try:
            if (not isinstance(waiver, dict) or not all(isinstance(waiver.get(k), str) for k in ("rule_id", "file", "reason", "expires")) or
                len(waiver["reason"].strip()) < 12 or date.fromisoformat(waiver["expires"]) < today or
                waiver["file"].startswith("/") or ".." in Path(waiver["file"]).parts):
                raise ValueError("Waiver must specify scoped rule_id/file, meaningful reason and unexpired ISO date")
        except ValueError as exc:
            invalid_waivers.append({"status": "INVALID_WAIVER", "evidence": str(exc), "waiver": waiver})
    accepted = [w for w in waivers if not any(x["waiver"] is w for x in invalid_waivers)]
    paths = changed or [p.relative_to(root).as_posix() for p in collect_files(root)]
    seen = set()
    for relative in paths:
        path = (root / relative).resolve()
        if not path.is_relative_to(root) or not path.is_file() or path.suffix not in EXT:
            continue
        for x in scan(path):
            file = path.relative_to(root).as_posix() if x["path"] != "(project)" else "(project)"
            key = (file, x["line"], x["code"])
            if key in seen: continue
            seen.add(key)
            match = next((w for w in accepted if w["rule_id"] == x["code"] and w["file"] == file), None)
            findings.append({
                "file": file, "line": x["line"], "rule_id": x["code"], "severity": x["severity"],
                "evidence": x["message"], "status": "WAIVED" if match else "STATIC_RISK",
                "waiver_reason": match["reason"] if match else None,
                "needs_browser": True, "confidence": "HEURISTIC"
            })
        # Source-level heading hints are advisory: an actual product reviewer
        # still decides whether information and above-heading placement matter.
        if path.suffix in {".html", ".vue", ".jsx", ".tsx"}:
            for hint in analyze_copy(path.read_text("utf-8", errors="replace"), relative):
                if hint["rule"] not in {"page-header-pretitle-before-h1", "title-prefix-before-heading"}:
                    continue
                file = relative
                key = (file, hint["line"], "MF108")
                if key in seen:
                    continue
                seen.add(key)
                match = next((w for w in accepted if w["rule_id"] == "MF108" and w["file"] == file), None)
                findings.append({
                    "file": file, "line": hint["line"], "rule_id": "MF108",
                    "severity": "medium",
                    "evidence": "Possible title preamble before " + hint.get("heading_level", "heading")
                                + ": " + hint["excerpt"] + ". Check independent information and placement.",
                    "status": "WAIVED" if match else "STATIC_RISK",
                    "waiver_reason": match["reason"] if match else None,
                    "needs_browser": True, "confidence": "HEURISTIC"
                })
    return {
        "status": "BLOCKED" if invalid_waivers else "STATIC_RISKS" if any(x["status"] == "STATIC_RISK" for x in findings) else "STATIC_ONLY",
        "findings": sorted(findings, key=lambda x: (x["file"], x["line"], x["rule_id"])),
        "invalid_waivers": invalid_waivers,
        "browser_verification": "NOT_TESTED",
        "note": "A clean static scan does not prove the target UI visually correct or interactive."
    }

def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--root", required=True, type=Path)
    p.add_argument("--changed", action="append", default=[], help="Project-relative file, repeatable; defaults to all supported UI files")
    p.add_argument("--waivers", type=Path, help="JSON array of {rule_id,file,reason,expires}, no global suppressions")
    p.add_argument("--format", choices=["json", "text"], default="text")
    p.add_argument("--strict", action="store_true", help="Fail on unwaived high severity or invalid waiver")
    args = p.parse_args()
    root = args.root.resolve()
    if not root.is_dir(): p.error("Invalid project root")
    waivers = []
    if args.waivers:
        config = args.waivers.resolve()
        if not config.is_relative_to(root): p.error("Waivers path must remain inside project")
        try:
            waivers = json.loads(config.read_text(encoding="utf-8"))
            if not isinstance(waivers, list): raise ValueError("Waiver configuration must be a JSON array")
        except (OSError, ValueError) as e: p.error(str(e))
    result = inspect(root, args.changed, waivers)
    if args.format == "json": print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        for x in result["findings"]:
            print(f"{x['file']}:{x['line']} {x['rule_id']} [{x['severity']}/{x['status']}] {x['evidence']}")
        for x in result["invalid_waivers"]: print("INVALID WAIVER:", x["evidence"])
        print("Browser verification:", result["browser_verification"])
    if result["invalid_waivers"]: return 2
    if args.strict and any(x["severity"] == "high" and x["status"] == "STATIC_RISK" for x in result["findings"]): return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
