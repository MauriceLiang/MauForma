#!/usr/bin/env python3
"""Prevent the public MauForma entrypoints from drifting into project-specific logs."""
from __future__ import annotations

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
ENTRYPOINTS = (ROOT / "SKILL.md", ROOT / "README.md")

# User-owned application identifiers must never become reusable design rules.
PROJECT_NAMES = (
    "RepoVantage", "GitHubDA", "FinalRace", "LaborQA", "VocaMesh",
    "MauLink", "MauLeaf", "MauQuota", "MauPulse", "Voacfect", "Vocafect",
)
FORBIDDEN_PATH = re.compile(
    r"(?:references|examples|assets)/[^\s\x60)\]]*repovantage", re.IGNORECASE
)
VERSION_HEADING = re.compile(r"^#{1,6}\s+(?:v\d+(?:\.\d+)+)\b", re.MULTILINE)
INCIDENT_LOG = re.compile(
    r"(?:用户|某用户)(?:最新|近期|提供|的)?[^\n]{0,30}(?:项目)?截图(?:表明|显示|揭示|说明)"
)


def validate_entrypoint(name: str, content: str) -> list[str]:
    errors: list[str] = []
    if VERSION_HEADING.search(content):
        errors.append(f"{name}: versioned headings belong in CHANGELOG.md")
    if INCIDENT_LOG.search(content):
        errors.append(f"{name}: incident/screenshot narration belongs outside reusable rules")
    if FORBIDDEN_PATH.search(content):
        errors.append(f"{name}: project-specific case file linked from entrypoint")
    for project in PROJECT_NAMES:
        if re.search(re.escape(project), content, re.IGNORECASE):
            errors.append(f"{name}: user project name must not appear ({project})")
    if name == "SKILL.md":
        if len(content.splitlines()) > 230:
            errors.append(f"{name}: too many lines for a routing entrypoint")
        if len(content.encode("utf-8")) > 35000:
            errors.append(f"{name}: entrypoint exceeds 35 KiB; move details to references")
        if not content.startswith("---\nname: mauforma\n"):
            errors.append(f"{name}: missing Agent Skill frontmatter")
        for key in ("适用范围", "按任务读取", "执行流程", "交付格式"):
            if key not in content:
                errors.append(f"{name}: missing essential section ({key})")
    return errors


def main() -> int:
    problems: list[str] = []
    for path in ENTRYPOINTS:
        if not path.is_file():
            problems.append(f"Missing entrypoint: {path.name}")
            continue
        problems.extend(validate_entrypoint(path.name, path.read_text("utf-8")))
    if problems:
        print("MauForma entrypoint hygiene FAILED:")
        print("\n".join(f" - {p}" for p in problems))
        return 1
    print("MauForma entrypoint hygiene PASS (not a visual or usability test)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
