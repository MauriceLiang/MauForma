"""Regression checks for paired-language policy clauses and source coverage.

These tests validate document consistency, not LLM comprehension or a real UI.
"""
from __future__ import annotations

import json
import shutil
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_semantic_boundaries import validate_repository


class SemanticBoundaryContractTests(unittest.TestCase):
    def test_every_runtime_pair_and_route_pass(self):
        self.assertEqual(validate_repository(ROOT), [])

    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / "repo"
        shutil.copytree(
            ROOT, self.root,
            ignore=shutil.ignore_patterns(".git", ".venv", "node_modules", "__pycache__", "artifacts", "*.png")
        )

    def test_chinese_prohibition_drift_is_caught(self):
        file = self.root / "references/semantic-boundaries.zh-CN.md"
        current = file.read_text("utf-8")
        original = "不得仅因为 MauForma 入口是英文，就把已有中文界面擅自改成英文。"
        self.assertIn(original, current)
        file.write_text(current.replace(original, "默认把中文界面翻成英文。"), "utf-8")
        failures = validate_repository(self.root)
        self.assertTrue(any("B02 missing never_zh clause" in x for x in failures), failures)

    def test_english_exception_drift_is_caught(self):
        file = self.root / "references/semantic-boundaries.en.md"
        content = file.read_text("utf-8")
        original = "Only test a 390px mobile layout when mobile support is in scope"
        self.assertIn(original, content)
        file.write_text(content.replace(original, "Always require 390px mobile on every project"), "utf-8")
        self.assertTrue(any("B09 missing exception_en clause" in x for x in validate_repository(self.root)))

    def test_new_contract_without_chinese_pair_is_blocked(self):
        file = self.root / "assets/semantic-boundary-contract.json"
        data = json.loads(file.read_text("utf-8"))
        data["rules"][0]["never_zh"] = "不得在任何时候忽略已批准的视觉方案而不说明原因。"
        file.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        self.assertTrue(any("B01 missing never_zh clause" in x for x in validate_repository(self.root)))

    def test_deleted_source_reference_is_blocked(self):
        (self.root / "references" / "design-dna-protocol.md").unlink()
        self.assertTrue(any("missing referenced file" in x or "broken runtime reference" in x for x in validate_repository(self.root)))

    def test_runtime_scope_and_reference_routing_are_checked(self):
        file = self.root / "SKILL.md"
        original = file.read_text("utf-8")
        self.assertIn("one primary guide", original)
        file.write_text(
            original.replace("one primary guide", "all the references"),
            encoding="utf-8",
        )
        self.assertTrue(any(
            "missing high-risk boundary anchor one primary guide" in x
            for x in validate_repository(self.root)
        ))

    def test_runtime_boundary_docs_survive_without_audit_reports(self):
        for path in (
            "references/upstream-reassessment.en.md",
            "references/upstream-reassessment.zh-CN.md",
            "references/i18n-runtime-validation.en.md",
            "SKILL.zh-CN.md",
            "CHANGELOG.md",
        ):
            self.assertFalse((self.root / path).exists(), path)
        english = (self.root / "references/semantic-boundaries.en.md").read_text("utf-8")
        chinese = (self.root / "references/semantic-boundaries.zh-CN.md").read_text("utf-8")
        for token in ("B01", "B08", "B15"):
            self.assertIn(token, english)
            self.assertIn(token, chinese)
        self.assertEqual(validate_repository(self.root), [])


if __name__ == "__main__":
    unittest.main()
