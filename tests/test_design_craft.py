"""Regression checks for scoped design workflows and honest review evidence."""
from pathlib import Path
import copy
import json
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_design_craft import validate_plan, validate_repository


class DesignCraftTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan = json.loads(
            (ROOT / "examples/design-craft-decision.demo.json").read_text("utf-8")
        )

    def test_repository_is_routed(self):
        self.assertEqual(validate_repository(), [])

    def test_synthetic_plan_is_valid_without_claiming_proof(self):
        self.assertEqual(validate_plan(self.plan), [])

    def test_mode_must_be_explicit(self):
        bad = copy.deepcopy(self.plan)
        bad["mode"] = "all-seven-skills"
        self.assertTrue(any("mode" in e for e in validate_plan(bad)))

    def test_cannot_skip_design_reason(self):
        bad = copy.deepcopy(self.plan)
        bad["design_decision"]["rejected_alternative"] = ""
        self.assertTrue(any("rejected_alternative" in e for e in validate_plan(bad)))

    def test_prior_decision_source_is_required(self):
        bad = copy.deepcopy(self.plan)
        bad["design_decision"]["source"] = "agent-guessed"
        self.assertTrue(any("source" in e or "direction" in e for e in validate_plan(bad)))

    def test_review_issue_needs_impact(self):
        bad = copy.deepcopy(self.plan)
        bad["review"]["issues"][0]["affected_task"] = ""
        self.assertTrue(any("affected_task" in e for e in validate_plan(bad)))

    def test_severity_is_not_a_vague_adjective(self):
        bad = copy.deepcopy(self.plan)
        bad["review"]["issues"][0]["severity"] = "ugly"
        self.assertTrue(any("severity" in e for e in validate_plan(bad)))

    def test_cannot_claim_verified_on_synthetic_fixture(self):
        bad = copy.deepcopy(self.plan)
        bad["review"]["overall_status"] = "VERIFIED"
        bad["review"]["evidence_level"] = "OBSERVED"
        bad["review"]["verified_routes"] = ["/settings"]
        bad["review"]["screenshots"] = ["before.png", "after.png"]
        self.assertTrue(any("Synthetic" in e for e in validate_plan(bad)))

    def test_real_visual_claim_requires_source(self):
        bad = copy.deepcopy(self.plan)
        bad["fixture_type"] = "project"
        bad["review"]["overall_status"] = "VERIFIED"
        bad["review"]["evidence_level"] = "OBSERVED"
        self.assertTrue(any("real target routes" in e for e in validate_plan(bad)))
        self.assertTrue(any("screenshot" in e for e in validate_plan(bad)))

    def test_scoped_fix_mode_is_allowed(self):
        good = copy.deepcopy(self.plan)
        good["mode"] = "fix"
        self.assertEqual(validate_plan(good), [])


if __name__ == "__main__":
    unittest.main()
