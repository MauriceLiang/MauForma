#!/usr/bin/env python3
"""Search a provenance-aware, locally indexed library of external DESIGN.md examples."""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "assets/external-design-cases.json"
MODES = ("Persuade", "Operate", "Read", "Experience")


def find_cases(query: str = "", style: str = "", mode: str = "", limit: int = 5,
               include_unreviewed: bool = False, db_path: Path = DATA) -> list[dict]:
    records = json.loads(Path(db_path).read_text("utf-8"))["cases"]
    terms = [t for t in re.split(r"[\s,，、；;/]+", query.casefold()) if t]
    matches = []
    for c in records:
        if c["review_status"] == "indexed_unreviewed" and not include_unreviewed:
            continue
        score = 0
        why = []
        tokens = [t.casefold() for t in c.get("keywords", [])]
        for term in terms:
            if term == c["id"].casefold() or term in tokens:
                score += 5
                why.append("term:" + term)
            elif any(term in x for x in tokens):
                score += 2
                why.append("partial:" + term)
        if style and style in c["styles"]:
            score += 4
            why.append("style:" + style)
        if mode and mode in c["modes"]:
            score += 2
            why.append("mode:" + mode)
        if score == 0:
            continue
        matches.append({"id": c["id"], "source_url": c["source_url"],
                        "status": c["review_status"], "score": score, "evidence": why,
                        "styles": c["styles"], "analysis_note": c["analysis_note"],
                        "not_official_design_system": True})
    matches.sort(key=lambda x: (-x["score"], {"sampled": 0, "candidate": 1, "indexed_unreviewed": 2}[x["status"]], x["id"]))
    return matches[:limit]


def main() -> int:
    p = argparse.ArgumentParser(description="Search real-brand-inspired DESIGN.md references (not brand official)")
    p.add_argument("--query", default="")
    p.add_argument("--style", default="")
    p.add_argument("--mode", default="", choices=["", *MODES])
    p.add_argument("--limit", type=int, default=5)
    p.add_argument("--include-unreviewed", action="store_true", help="Also search name-only entries")
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    if not (args.query.strip() or args.style or args.mode):
        p.error("Provide a site purpose/content query, style or visitor mode")
    if not 1 <= args.limit <= 84:
        p.error("--limit must be between 1 and 84")
    matches = find_cases(args.query, args.style, args.mode, args.limit, args.include_unreviewed)
    if args.json:
        print(json.dumps(matches, ensure_ascii=False, indent=2))
    elif not matches:
        print("No reviewed or candidate match. Refine the website purpose, content or style.")
    else:
        for i, c in enumerate(matches, 1):
            print(f"{i}. {c['id']} ({c['status']}, score {c['score']})")
            print("   ", c["analysis_note"])
            print("   ", c["source_url"])
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
