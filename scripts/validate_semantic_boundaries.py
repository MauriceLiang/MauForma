#!/usr/bin/env python3
"""MauForma paired-language *static* boundary and route check.

Enforces inspectable contracts, exceptions, provenance and path existence.
This cannot prove translation meaning, Agent completion quality, or UI runtime
correctness. Never use this tool as a substitute for controlled bilingual
task evaluation or rendered-browser QA.
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTRACT = "assets/semantic-boundary-contract.json"
EN = "references/semantic-boundaries.en.md"
ZH = "references/semantic-boundaries.zh-CN.md"
REVIEW_EN = "references/upstream-reassessment.en.md"
REVIEW_ZH = "references/upstream-reassessment.zh-CN.md"
IDS = tuple(f"B{n:02}" for n in range(1, 16))
FIELDS = (
    "id", "topic", "trigger_en", "trigger_zh", "require_en", "require_zh",
    "exception_en", "exception_zh", "never_en", "never_zh", "docs"
)
UPSTREAM = (
    "Stageshow", "Anthropic Frontend Design", "Impeccable",
    "Senlin Taste", "Leon Taste", "Theme Factory", "Designer Skills",
    "UI/UX Pro Max", "Vercel Web Interface Guidelines",
    "Vercel Composition Patterns", "Vercel React Best Practices",
    "Vue Best Practices", "Anthropic Webapp Testing",
    "OpenAI Figma Implement Design",
)
# These gates need to remain discoverable in the default runtime.
RUNTIME = {
    "SKILL.md": (
        "references/semantic-boundaries.en.md", "references/upstream-reassessment.en.md",
        "one primary guide", "loading budget", "delegated implementation scope",
        "actual rendered DOM", "Gate H-Base / H0", "Gate S0",
        "prefers-reduced-motion", "STATIC CHECK", "DEMO ONLY",
        "NOT TESTED", "BLOCKED",
    ),
    "references/execution-handbook.en.md": (
        "user's preferred language", "one primary guide",
        "delegated implementation scope", "Gate H0", "Gate S0",
        "rendered DOM", "backend", "VERIFIED", "STATIC CHECK",
        "DEMO ONLY", "NOT TESTED", "BLOCKED",
        "references/semantic-boundaries.en.md",
    ),
    "README.md": (
        "README.zh-CN.md", REVIEW_EN, REVIEW_ZH, EN, ZH, CONTRACT,
    ),
    "README.zh-CN.md": (
        "README.md", REVIEW_EN, REVIEW_ZH, EN, ZH, CONTRACT,
    ),
}
# Links in Markdown URLs to upstream sources are not local repository files.
LOCAL_REF = re.compile(
    r"(?<![A-Za-z0-9/_])((?:references|scripts|assets|examples|tests)/"
    r"[A-Za-z0-9._/*-]+)"
)


def validate_repository(root: Path = ROOT) -> list[str]:
    problems: list[str] = []
    sources: dict[str, str] = {}
    for path in (CONTRACT, EN, ZH, REVIEW_EN, REVIEW_ZH, *RUNTIME):
        candidate = root / path
        if not candidate.is_file():
            problems.append(f"Missing semantic source: {path}")
        else:
            sources[path] = candidate.read_text("utf-8")
    if any(path not in sources for path in (CONTRACT, EN, ZH)):
        return problems

    try:
        data = json.loads(sources[CONTRACT])
    except (TypeError, ValueError) as exc:
        return problems + [f"Invalid semantic JSON: {exc}"]
    if not isinstance(data, dict) or data.get("schema") != 1:
        return problems + ["Semantic contract schema must equal 1"]
    rules = data.get("rules")
    if not isinstance(rules, list):
        return problems + ["Semantic contract rules must be a list"]
    ids = [rule.get("id") if isinstance(rule, dict) else None for rule in rules]
    if tuple(ids) != IDS:
        problems.append(f"Boundary IDs must be unique and ordered B01..B15, got {ids}")
    for rule in rules:
        if not isinstance(rule, dict):
            problems.append("Boundary must be a JSON object")
            continue
        label = str(rule.get("id") or "INVALID")
        for field in FIELDS:
            value = rule.get(field)
            if field == "docs":
                if not isinstance(value, list) or not value or not all(
                    isinstance(x, str) and x.startswith(
                        ("references/", "scripts/", "assets/", "SKILL.md")
                    ) for x in value
                ):
                    problems.append(f"{label}: docs must be nonempty local paths")
                else:
                    for link in value:
                        if not (root / link).is_file():
                            problems.append(f"{label}: missing referenced file {link}")
                continue
            if not isinstance(value, str) or len(value.strip()) < (4 if field in {"id", "topic"} else 12):
                if field == "id" and isinstance(value, str) and value in IDS:
                    continue
                problems.append(f"{label}: missing substantive field {field}")
        for language, doc in (("en", EN), ("zh", ZH)):
            body = sources[doc]
            marker = f"## {label} — {rule.get('topic', '')}"
            if body.count(marker) != 1:
                problems.append(f"{doc}: missing or repeated heading {label}")
            for field in ("trigger", "require", "exception", "never"):
                clause = rule.get(f"{field}_{language}")
                if isinstance(clause, str) and clause not in body:
                    problems.append(f"{doc}: {label} missing {field}_{language} clause")

    for file, required in RUNTIME.items():
        body = sources.get(file, "")
        for marker in required:
            if marker not in body:
                problems.append(f"{file}: missing high-risk boundary anchor {marker}")
    for doc in (REVIEW_EN, REVIEW_ZH):
        body = sources.get(doc, "")
        for name in UPSTREAM:
            if name not in body:
                problems.append(f"{doc}: missing reviewed upstream {name}")
    # Do not count github.com references embedded in README as missing local
    # files; the only audited path graph below is the Agent execution entrypoint.
    active = sources.get("SKILL.md", "")
    for match in LOCAL_REF.finditer(active):
        target = match.group(1).rstrip(".,;")
        if "*" in target or target.startswith("references/framework-"):
            continue
        if not (root / target).is_file():
            problems.append(f"SKILL.md: broken runtime reference {target}")
    # Check routing parity without pretending we can decide meaning from tokens.
    for term in ("B01", "B08", "B15"):
        for doc in (EN, ZH):
            if term not in sources[doc]:
                problems.append(f"{doc}: missing crucial paired boundary ID {term}")
    return sorted(set(problems))


def main() -> int:
    issues = validate_repository()
    for issue in issues:
        print("ERROR:", issue)
    if issues:
        print(f"Semantic boundary contract FAILED ({len(issues)} static issues)")
        return 1
    print(f"Semantic boundary contract PASS: {len(IDS)} EN/ZH paired rules, 14 upstream references, local route integrity")
    print("Scope: STATIC CHECK ONLY — this does not prove multilingual model understanding or live UI quality")
    return 0


if __name__ == "__main__":
    sys.exit(main())
