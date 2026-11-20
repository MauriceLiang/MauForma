"""Maintain usable task documentation after removing non-runtime historical artifacts.

Checks local Markdown links; it does not judge the aesthetic usefulness of a
design guide or the actual quality of Agent-generated UI.
"""
from __future__ import annotations

import re
import unittest
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
LINK = re.compile(r"!?(?:\[[^\]]*\])\(([^)]+)\)")
FENCE = re.compile(r"^\s*`{3,}|^\s*~{3,}")
REMOVED = (
    "CHANGELOG.md",
    "SKILL.zh-CN.md",
    "references/upstream-reassessment.en.md",
    "references/upstream-reassessment.zh-CN.md",
    "references/i18n-runtime-validation.en.md",
    "references/source-analysis.md",
    "references/framework-mapping.md",
    "references/universal-applications.md",
    "examples/prompts.md",
    "scripts/measure_prompt_budget.py",
)


def linked_paths(document: Path):
    inside_fence = False
    for line in document.read_text(encoding="utf-8").splitlines():
        if FENCE.match(line):
            inside_fence = not inside_fence
            continue
        if inside_fence:
            continue
        for raw in LINK.findall(line):
            address = raw.split("#", 1)[0].strip().strip("<>").split(" ", 1)[0]
            if not address or re.match(r"^(?:[a-zA-Z][a-zA-Z0-9+.-]*:|//)", address):
                continue
            yield unquote(address)


class ActiveDocumentationTests(unittest.TestCase):
    def test_historical_artifacts_are_absent(self):
        for item in REMOVED:
            with self.subTest(item=item):
                self.assertFalse((ROOT / item).exists(), item)
        self.assertFalse((ROOT / "assets/reference-source").exists())

    def test_all_local_markdown_links_point_to_existing_targets(self):
        # A preview/sample is still allowed, but its links must remain valid.
        broken = []
        for doc in sorted(ROOT.glob("*.md")) + sorted((ROOT / "references").rglob("*.md")) + sorted((ROOT / "examples").rglob("*.md")):
            for ref in linked_paths(doc):
                target = (doc.parent / ref).resolve()
                if not target.is_relative_to(ROOT):
                    continue  # cross-repository reference rather than owned asset
                if not target.exists():
                    broken.append(f"{doc.relative_to(ROOT)} -> {ref}")
        self.assertEqual(broken, [], "\n".join(broken))

    def test_runtime_entrypoint_does_not_route_to_audit_logs(self):
        entry = (ROOT / "SKILL.md").read_text("utf-8")
        handbook = (ROOT / "references/execution-handbook.en.md").read_text("utf-8")
        for text in (entry, handbook):
            for item in REMOVED:
                self.assertNotIn(item, text, item)
        self.assertIn("references/semantic-boundaries.en.md", entry)
        self.assertIn("references/component-library-first-gate.md", entry)
        self.assertIn("references/browser-qa-protocol.md", entry)


if __name__ == "__main__":
    unittest.main()
