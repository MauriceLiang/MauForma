#!/usr/bin/env python3
"""Phase-2 English runtime boundary guard. Static checks do NOT prove translation equivalence."""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = ROOT / "assets/i18n-phase2-translation-contract.json"
HAN = re.compile(r"[\u3400-\u9fff]")
BLOB_SHA = re.compile(r"^[0-9a-f]{40}$")


def inspect(contract: dict, root: Path = ROOT) -> list[str]:
    errors: list[str] = []
    if contract.get("schema_version") != "1.0":
        errors.append("Unsupported i18n phase-2 contract")
    if contract.get("status") not in {"partial_migration", "complete_pending_review", "fully_verified"}:
        errors.append("Explicit migration status is required")
    if contract.get("status") == "fully_verified":
        errors.append("Static contracts cannot assert independent semantic parity verification")
    skill = root / "SKILL.md"
    if not skill.is_file() or HAN.search(skill.read_text("utf-8")):
        errors.append("SKILL.md must remain English-only")
    entries = contract.get("entries", [])
    if not isinstance(entries, list) or not entries:
        return errors + ["Translated runtime file list is required"]
    inventory_file = root / "assets/i18n-phase2-migration-inventory.json"
    if not inventory_file.is_file():
        errors.append("Full reference migration inventory is required")
    else:
        inv = json.loads(inventory_file.read_text("utf-8"))
        records = inv.get("files", [])
        inventory_status = inv.get("migration_status")
        if contract.get("status") == "complete_pending_review":
            if inventory_status != "complete_pending_independent_review":
                errors.append("Completed translation inventory must remain pending independent semantic review")
        elif inventory_status != "partial":
            errors.append("Partial translation must have an explicit partial inventory")
        if not isinstance(records, list):
            errors.append("Reference inventory must list all files")
            records = []
        paths = [r.get("path") for r in records if isinstance(r, dict)]
        if len(paths) != len(set(paths)):
            errors.append("Duplicate files in full migration inventory")
        for entry in entries:
            found = next((r for r in records if isinstance(r, dict) and r.get("path") == entry.get("path")), None)
            if found is None:
                errors.append(f"{entry.get('path')}: missing from full reference inventory")
            elif (found.get("status") != "translated_pending_independent_review"
                  or found.get("source_blob_sha") != entry.get("source_blob_sha")):
                errors.append(f"{entry.get('path')}: inventory and source blob mismatch")
        pending = [r for r in records if isinstance(r, dict) and r.get("status") == "pending_language_and_semantic_audit"]
        if not pending and contract.get("status") == "partial_migration":
            errors.append("No pending inventory documents: verify completion status explicitly")
        if contract.get("status") == "complete_pending_review" and pending:
            errors.append("Completed translation status cannot conceal pending language migrations")
    seen: set[str] = set()
    for entry in entries:
        if not isinstance(entry, dict):
            errors.append("Invalid translation entry")
            continue
        rel = entry.get("path", "")
        if not isinstance(rel, str) or not rel.startswith("references/") or ".." in Path(rel).parts or rel in seen:
            errors.append(f"Invalid/duplicate translation path: {rel}")
            continue
        seen.add(rel)
        sha = entry.get("source_blob_sha", "")
        if not isinstance(sha, str) or not BLOB_SHA.fullmatch(sha):
            errors.append(f"{rel}: original source Git blob SHA is missing")
        if entry.get("translated_status") != "translated_pending_independent_review":
            errors.append(f"{rel}: static validation must not claim independently approved translation")
        path = root / rel
        if not path.is_file():
            errors.append(f"{rel}: translated document missing")
            continue
        source = path.read_text("utf-8")
        if "\\\x60" in source:
            errors.append(f"{rel}: escaped Markdown backtick detected")
        checks = entry.get("required_english_fragments")
        if not isinstance(checks, list) or len(checks) < 3:
            errors.append(f"{rel}: insufficient semantic coverage anchors")
        else:
            for item in checks:
                if not isinstance(item, str) or item.casefold() not in source.casefold():
                    errors.append(f"{rel}: missing English boundary anchor {item!r}")
        paired = entry.get("semantic_pair_examples")
        if not isinstance(paired, list) or len(paired) < 2:
            errors.append(f"{rel}: source/target parity examples required")
        else:
            for p in paired:
                if not isinstance(p, dict) or not p.get("source_zh") or not p.get("target_en"):
                    errors.append(f"{rel}: incomplete bilingual parity example")
                    continue
                if str(p["target_en"]).casefold() not in source.casefold():
                    errors.append(f"{rel}: missing translated meaning for {p['source_zh']!r}")
        allowed = entry.get("allowed_cjk_fragments", [])
        for snippet in allowed:
            if not isinstance(snippet, str):
                errors.append(f"{rel}: invalid locale sample allowance")
            else:
                source = source.replace(snippet, "")
        if HAN.search(source):
            errors.append(f"{rel}: explanatory Han script remains outside permitted locale examples")
    return errors


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repository", action="store_true", help="Validate translated runtime subset")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args()
    if not args.repository:
        parser.error("Use --repository")
    data = json.loads(CONTRACT.read_text("utf-8"))
    issues = inspect(data)
    if args.json:
        print(json.dumps({"passed": not issues, "translated_files": len(data["entries"]), "migration_status": data["status"], "independent_semantic_qa": "NOT VERIFIED", "issues": issues}, ensure_ascii=False, indent=2))
    else:
        for issue in issues:
            print("ERROR:", issue)
        print("Phase-2 English runtime subset:", "PASS" if not issues else "FAIL")
        print("Independent semantic review: NOT VERIFIED; migration:", data["status"])
    return int(bool(issues))


if __name__ == "__main__":
    raise SystemExit(main())
