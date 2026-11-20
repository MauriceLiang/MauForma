#!/usr/bin/env python3
"""Compare instruction surface size without inventing model-token efficiency claims.

If tiktoken is already installed, --encoding can measure a specified public
proxy tokenizer; this does NOT represent the private tokenizer of an arbitrary
Agent model. No dependencies are automatically installed.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]


def measure(file: Path, encoding: str = "") -> dict:
    body = file.read_text(encoding="utf-8")
    result = {
        "file": str(file.relative_to(ROOT)) if file.is_relative_to(ROOT) else str(file),
        "utf8_bytes": len(body.encode("utf-8")),
        "codepoints": len(body),
        "lines": len(body.splitlines()),
        "estimated_tokens": None,
        "tokenizer": "NOT_MEASURED",
    }
    if encoding:
        try:
            import tiktoken
        except ImportError:
            result["tokenizer"] = "UNAVAILABLE: tiktoken not installed (no automatic install)"
        else:
            tokenizer = tiktoken.get_encoding(encoding)
            result["estimated_tokens"] = len(tokenizer.encode(body))
            result["tokenizer"] = encoding + " (PROXY, not validated for all Agent models)"
    return result


def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--english", type=Path, default=ROOT / "SKILL.md")
    p.add_argument("--chinese", type=Path, default=ROOT / "SKILL.zh-CN.md")
    p.add_argument("--encoding", default="", help="Optional installed tiktoken encoding name")
    p.add_argument("--max-english-bytes", type=int, default=25000)
    args = p.parse_args()
    if not args.english.is_file() or not args.chinese.is_file():
        p.error("Both English and Chinese baseline files must exist")
    en = measure(args.english, args.encoding)
    zh = measure(args.chinese, args.encoding)
    if args.max_english_bytes <= 0:
        p.error("--max-english-bytes must be positive")
    summary = {
        "english": en,
        "chinese_baseline": zh,
        "utf8_byte_delta_percent": round(100 * (en["utf8_bytes"] - zh["utf8_bytes"]) / zh["utf8_bytes"], 1),
        "token_delta_percent": (
            round(100 * (en["estimated_tokens"] - zh["estimated_tokens"]) / zh["estimated_tokens"], 1)
            if en["estimated_tokens"] is not None and zh["estimated_tokens"] is not None else None
        ),
        "claim_limit": (
            "Byte count is a reproducible storage/transport metric, NOT runtime latency or token cost. "
            "A tokenizer proxy does not measure actual cross-model task completion quality. "
            "Controlled same-task Agent evaluations are required."
        ),
        "core_byte_limit": args.max_english_bytes,
        "within_limit": en["utf8_bytes"] <= args.max_english_bytes,
    }
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return int(not summary["within_limit"])


if __name__ == "__main__":
    raise SystemExit(main())
