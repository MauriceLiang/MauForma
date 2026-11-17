"""Regression tests for the authored universal page-header review contract."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_page_header_copy import validate_cases, validate_repo


class PageHeaderCopyContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.examples = json.loads(
            (ROOT / "assets/page-header-copy-cases.json").read_text(encoding="utf-8")
        )

    def test_repo_documentation_contract(self) -> None:
        self.assertEqual(validate_repo(), [])

    def test_valid_synthetic_cases(self) -> None:
        self.assertEqual(validate_cases(self.examples), [])

    def test_existing_learning_decoration_cannot_be_grandfathered(self) -> None:
        mutated = copy.deepcopy(self.examples)
        case = next(c for c in mutated["cases"] if c["id"] == "legacy-learning-subtitle")
        case["expected_action"] = "keep"
        self.assertTrue(any("incorrect expected action" in x for x in validate_cases(mutated)))

    def test_unconfirmed_brand_claim_cannot_escape(self) -> None:
        mutated = copy.deepcopy(self.examples)
        case = next(c for c in mutated["cases"] if c["id"] == "marketing-approved-tagline")
        case["approved"] = False
        self.assertTrue(any("explicit evidence" in x for x in validate_cases(mutated)))

    def test_real_chapter_is_not_auto_deleted(self) -> None:
        mutated = copy.deepcopy(self.examples)
        case = next(c for c in mutated["cases"] if c["id"] == "chapter-numbering")
        case["expected_action"] = "delete"
        self.assertTrue(validate_cases(mutated))

    def test_brand_plus_description_requires_separate_decisions(self) -> None:
        mutated = copy.deepcopy(self.examples)
        case = next(c for c in mutated["cases"] if c["id"] == "legacy-mixed-brand-description")
        case["expected_action"] = "keep"
        self.assertTrue(validate_cases(mutated))

    def test_every_page_archetype_must_be_included(self) -> None:
        mutated = copy.deepcopy(self.examples)
        mutated["cases"] = [
            c for c in mutated["cases"] if c["product_type"] != "scientific_visualization"
        ]
        self.assertTrue(validate_cases(mutated))


if __name__ == "__main__":
    unittest.main()
