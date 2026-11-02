#!/usr/bin/env python3
"""Search MauForma's original aesthetic profiles. Standard library only; no third-party code."""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DB = ROOT / "assets" / "style-knowledge.json"
MODES = ("Persuade", "Operate", "Read", "Experience")


def tokenize(text: str) -> list[str]:
    return [part for part in re.split(r"[\s,;|/，。；、]+", text.casefold()) if part]


def rank_styles(query: str, mode: str | None = None, website_type: str = "",
                limit: int = 3, db_path: Path = DB) -> list[dict]:
    data = json.loads(Path(db_path).read_text(encoding="utf-8"))
    tokens = tokenize(query + " " + website_type)
    results = []
    for s in data["styles"]:
        blob = " ".join(s["keywords"] + s["sites"] + [s["name"], s["first_impression"]]).casefold()
        why = []
        score = 0
        for token in tokens:
            if token in blob:
                score += 3 if token in [k.casefold() for k in s["keywords"]] else 1
                why.append(f"content:{token}")
        if mode and mode in s["modes"]:
            score += 4
            why.append(f"mode:{mode}")
        if website_type and website_type.casefold() in [x.casefold() for x in s["sites"]]:
            score += 6
            why.append(f"site:{website_type}")
        if score:
            results.append({
                "id": s["id"], "name": s["name"], "score": score, "evidence": why,
                "first_screen": s["first_impression"], "layout": s["layout"],
                "rationale": s["why"], "tradeoffs": s["tradeoffs"],
                "required_assets": s["assets"], "dials": s["dials"],
                "source_urls": s["source_urls"],
                "status": "recommendation_not_user_confirmed",
            })
    results.sort(key=lambda x: (-x["score"], x["id"]))
    return results[:limit]


def main() -> int:
    p = argparse.ArgumentParser(description="Context-aware design direction shortlist, not a user decision")
    p.add_argument("--query", default="", help="Website purpose and actual content")
    p.add_argument("--mode", choices=MODES, help="Visitor task mode")
    p.add_argument("--type", default="", dest="website_type", help="Website category, if known")
    p.add_argument("--limit", type=int, default=3)
    p.add_argument("--json", action="store_true")
    p.add_argument("--selected", default="", help="Already-confirmed profile ID: do not override user choice")
    args = p.parse_args()
    if not args.query.strip() and not args.mode and not args.website_type and not args.selected:
        p.error("Provide --query, --mode, --type or a user-confirmed --selected style")
    if args.limit < 1 or args.limit > 8:
        p.error("--limit must be 1..8")
    all_styles = json.loads(DB.read_text("utf-8"))["styles"]
    if args.selected:
        match = next((s for s in all_styles if s["id"] == args.selected), None)
        if not match:
            p.error(f"Unknown style: {args.selected}")
        results = [{"id": match["id"], "name": match["name"],
                    "status": "user_selected_use_as_primary", "rationale": match["why"]}]
    else:
        results = rank_styles(args.query, args.mode, args.website_type, args.limit)
    if args.json:
        print(json.dumps(results, ensure_ascii=False, indent=2))
    elif not results:
        print("No evidence-backed match. Ask what the website does and what it will display.")
    else:
        for i, r in enumerate(results, 1):
            print(f"{i}. {r['name']} ({r['status']})")
            print(f"   Reason: {r['rationale']}")
            if "first_screen" in r:
                print(f"   First screen: {r['first_screen']}")
                print(f"   Tradeoff: {'; '.join(r['tradeoffs'])}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
