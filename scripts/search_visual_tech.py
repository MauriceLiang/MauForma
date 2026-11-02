#!/usr/bin/env python3
"""Select specialized Web visual technologies; recommendation only, not package install."""
from __future__ import annotations
import argparse
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "assets" / "visual-tech-catalog.json"


def rank(goal: str, limit: int = 5, db: Path = DATA) -> list[dict]:
    data = json.loads(Path(db).read_text("utf-8"))
    terms = [t for t in re.split(r"[\s,，。；;、/]+", goal.casefold()) if t]
    if not terms:
        return []
    out = []
    for tool in data["tools"]:
        kws = [k.casefold() for k in tool["keywords"]]
        score = 0
        hits = []
        for term in terms:
            if term in kws:
                score += 5
                hits.append(term)
            elif any(term in k or k in term for k in kws if len(k) >= 2):
                score += 2
                hits.append(term)
        if score > 0:
            out.append({
                "id": tool["id"], "name": tool["name"], "kind": tool["kind"],
                "score": score, "matched": hits, "purpose": tool["goal"],
                "avoid_when": tool["avoid"], "lighter_option": tool["lightweight_alternative"],
                "existing_coverage": tool["coverage"], "official_url": tool["api"],
                "status": "recommendation_not_installed"
            })
    return sorted(out, key=lambda x: (-x["score"], x["id"]))[:limit]


def main() -> int:
    p = argparse.ArgumentParser(description="Purpose-first shortlist for 12 animation/visual tools")
    p.add_argument("--goal", required=True, help="Required effect, e.g. '3D 产品模型 可旋转'")
    p.add_argument("--limit", type=int, default=5)
    p.add_argument("--json", action="store_true")
    args = p.parse_args()
    if not 1 <= args.limit <= 12:
        p.error("--limit must be 1..12")
    matches = rank(args.goal, args.limit)
    if args.json:
        print(json.dumps(matches, ensure_ascii=False, indent=2))
    elif matches:
        for m in matches:
            print(f"{m['name']}: {m['purpose']} (score={m['score']})")
            print("  Lightweight alternative:", m["lighter_option"])
            print("  Official:", m["official_url"])
    else:
        print("No specialization indicated. Default to CSS / SVG / framework-native transitions.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
