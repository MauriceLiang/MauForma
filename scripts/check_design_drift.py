#!/usr/bin/env python3
"""Read-only design token inventory and drift diagnosis. Baselines describe code, NOT approval."""
from __future__ import annotations
import argparse
import hashlib
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

EXT = {".css", ".scss", ".less", ".vue", ".jsx", ".tsx", ".ts", ".js"}
SKIP = {"node_modules", "dist", "build", ".git", ".next", ".nuxt", "coverage", ".output", "vendor", "artifacts"}
DEFINITION = re.compile(r"(?<![\w-])(--[a-zA-Z][\w-]*)\s*:\s*([^;{}\n]+)\s*;")
USE = re.compile(r"var\(\s*(--[a-zA-Z][\w-]*)")
HEX = re.compile(r"(?<![\w-])#[0-9a-fA-F]{6}(?:[0-9a-fA-F]{2})?\b")


def inventory(root: Path) -> dict:
    definitions, uses, raw_colors, files = {}, {}, [], {}
    for p in sorted(root.rglob("*")):
        if not p.is_file() or p.suffix not in EXT or any(part in SKIP or part.startswith(".venv") for part in p.relative_to(root).parts):
            continue
        rel = p.relative_to(root).as_posix()
        body = p.read_text(encoding="utf-8", errors="replace")
        files[rel] = hashlib.sha256(body.encode("utf-8")).hexdigest()
        for match in DEFINITION.finditer(body):
            name, value = match.groups()
            definitions.setdefault(name, []).append({"file": rel, "line": body.count("\n", 0, match.start()) + 1, "value": " ".join(value.split())})
        for match in USE.finditer(body):
            uses.setdefault(match.group(1), []).append({"file": rel, "line": body.count("\n", 0, match.start()) + 1})
        if p.suffix in {".css", ".scss", ".vue", ".jsx", ".tsx"} and not re.search(r"token|theme|palette", p.stem, re.I):
            for match in HEX.finditer(body):
                raw_colors.append({"file": rel, "line": body.count("\n", 0, match.start()) + 1, "value": match.group()})
    return {"schema": 1, "source": "OBSERVED_CODE_NOT_USER_APPROVAL", "files": files,
            "definitions": definitions, "uses": uses, "raw_colors": raw_colors[:300]}


def diagnose(current: dict, baseline: dict | None) -> list[dict]:
    findings = []
    def add(rule, severity, file, line, evidence, status="REVIEW"):
        findings.append({"rule_id": rule, "severity": severity, "file": file, "line": line,
                         "evidence": evidence, "status": status, "needs_human_review": True})
    if baseline is None:
        add("MF-DRIFT-NO-BASELINE", "info", "design-system/observed-tokens.json", 0,
            "No observed-code snapshot; run --write-baseline explicitly", "NOT_BASELINED")
    else:
        if baseline.get("schema") != 1:
            add("MF-DRIFT-SCHEMA", "high", "design-system/observed-tokens.json", 0, "Unsupported baseline schema")
        for name, old in baseline.get("definitions", {}).items():
            newer = current["definitions"].get(name, [])
            if not newer:
                point = old[0] if old else {}
                add("MF-DRIFT-REMOVED", "high", point.get("file", "?"), point.get("line", 0), name + " no longer defined")
            elif sorted(x["value"] for x in old) != sorted(x["value"] for x in newer):
                point = newer[0]
                add("MF-DRIFT-VALUE", "medium", point["file"], point["line"],
                    name + " changed from " + repr([x["value"] for x in old]) + " to " + repr([x["value"] for x in newer]))
        for name, newer in current["definitions"].items():
            if name not in baseline.get("definitions", {}):
                point = newer[0]
                add("MF-DRIFT-NEW", "info", point["file"], point["line"], name + " added since baseline")
    for name, origins in current["uses"].items():
        if name not in current["definitions"]:
            point = origins[0]
            add("MF-TOKEN-UNDEFINED", "medium", point["file"], point["line"], "var("+name+") has no project-local definition; may be supplied by external library")
    for entry in current["raw_colors"]:
        add("MF-COLOR-LITERAL", "info", entry["file"], entry["line"],
            entry["value"] + " outside a theme/token-named file; verify against approved palette")
    return sorted(findings, key=lambda x: (x["file"], x["line"], x["rule_id"]))


def run(root: Path, baseline_path: Path, write: bool = False, force: bool = False) -> dict:
    current = inventory(root)
    baseline = json.loads(baseline_path.read_text("utf-8")) if baseline_path.exists() else None
    if write:
        if baseline is not None and not force:
            raise FileExistsError("Baseline exists: refusing overwrite without --force")
        baseline_path.parent.mkdir(parents=True, exist_ok=True)
        payload = dict(current, created_at=datetime.now(timezone.utc).isoformat())
        baseline_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        baseline = payload
    findings = diagnose(current, baseline)
    return {"status": "OBSERVED_NOT_APPROVED" if baseline is not None else "NOT_BASELINED",
            "baseline": str(baseline_path), "source_files": len(current["files"]), "tokens": len(current["definitions"]),
            "findings": findings, "scope": "static evidence, not proof that design matches product or user decisions",
            "human_review_required": True}


def main() -> int:
    cli = argparse.ArgumentParser()
    cli.add_argument("--root", type=Path, required=True)
    cli.add_argument("--baseline", type=Path)
    cli.add_argument("--write-baseline", action="store_true")
    cli.add_argument("--force", action="store_true", help="Explicitly replace existing observed snapshot, not MASTER or decisions")
    cli.add_argument("--strict", action="store_true")
    cli.add_argument("--format", choices=["json", "text"], default="text")
    args = cli.parse_args()
    root = args.root.resolve()
    if not root.is_dir(): cli.error("--root must be an existing directory")
    baseline = (args.baseline or root / "design-system" / "observed-tokens.json").resolve()
    if not baseline.is_relative_to(root): cli.error("Baseline must remain inside the project root")
    if args.force and not args.write_baseline: cli.error("--force requires --write-baseline")
    try: result = run(root, baseline, args.write_baseline, args.force)
    except (FileExistsError, ValueError, json.JSONDecodeError) as exc: cli.error(str(exc))
    if args.format == "json": print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(result["status"] + ": " + str(result["tokens"]) + " observed token names")
        for x in result["findings"]:
            print(f"{x['file']}:{x['line']} [{x['rule_id']}/{x['severity']}] {x['evidence']}")
    if args.strict and any(x["severity"] in {"high", "medium"} for x in result["findings"]): return 1
    return 0

if __name__ == "__main__":
    sys.exit(main())
