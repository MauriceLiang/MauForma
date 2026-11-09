"""Synthetic tests for MauForma product routing and staged refinement contracts."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_product_experience import validate, validate_repo


class ProductExperienceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls) -> None:
        cls.routes = json.loads((ROOT / "assets/product-experience-routes.json").read_text("utf-8"))
        cls.stages = json.loads((ROOT / "assets/refinement-stage-cases.json").read_text("utf-8"))

    def test_repo_contract(self) -> None:
        self.assertEqual(validate_repo(), [])

    def test_valid_synthetic_examples(self) -> None:
        self.assertEqual(validate(self.routes, self.stages), [])

    def test_all_domain_categories(self) -> None:
        self.assertGreaterEqual(len({c["product_type"] for c in self.routes["cases"]}), 7)

    def test_structural_problem_needs_two_directions(self) -> None:
        routes = copy.deepcopy(self.routes)
        routes["cases"][0]["layout_directions"] = ["only-color-change"]
        self.assertTrue(any("distinct layout directions" in e for e in validate(routes, self.stages)))

    def test_scoped_fix_is_not_ux_rewrite(self) -> None:
        self.assertTrue(any(c["requires_ux_restructure"] is False for c in self.routes["cases"]))

    def test_stage_order_cannot_skip_ux(self) -> None:
        stages = copy.deepcopy(self.stages)
        stages["order"] = ["R0", "R2", "R3", "R4", "R5"]
        self.assertTrue(any("stage order" in e for e in validate(self.routes, stages)))

    def test_learning_ux_failure_must_block_reskin(self) -> None:
        stages = copy.deepcopy(self.stages)
        stages["exceptions"] = [
            e for e in stages["exceptions"] if e["id"] != "structural-education-failure"
        ]
        self.assertTrue(any("learning-UX-first" in e for e in validate(self.routes, stages)))

    def test_emoji_are_not_unconditionally_banned(self) -> None:
        stages = copy.deepcopy(self.stages)
        stages["exceptions"] = [
            e for e in stages["exceptions"] if e["id"] != "children-story-learning"
        ]
        self.assertTrue(any("legitimate emoji" in e for e in validate(self.routes, stages)))


if __name__ == "__main__":
    unittest.main()
