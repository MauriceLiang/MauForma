"""Surface-choice and no-character-stacking contracts, independent of product/project."""
from __future__ import annotations
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from validate_surface_control import validate_plan, validate_repository

class SurfaceControlTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.plan=json.loads((ROOT/"assets/surface-control-patterns.json").read_text("utf-8"))

    def test_repository_artifacts(self):
        self.assertEqual(validate_repository(), [])

    def test_modes_and_multiple_surface_strategies(self):
        self.assertEqual({p["mode"] for p in self.plan["profiles"]}, {"Operate","Persuade","Read","Experience"})
        self.assertGreaterEqual(len({s["pattern"] for p in self.plan["profiles"] for s in p["surfaces"]}), 4)

    def test_rejects_generic_mega_card_default(self):
        p=copy.deepcopy(self.plan)
        p["profiles"][0]["surfaces"][0]["pattern"]="mega-card"
        self.assertTrue(any("mega-card" in e for e in validate_plan(p)))

    def test_requires_rejected_alternative_reason(self):
        p=copy.deepcopy(self.plan)
        p["profiles"][0]["surfaces"][0]["rejected_reason"]=""
        self.assertTrue(any("alternatives" in e for e in validate_plan(p)))

    def test_rejects_unsafe_fallback_that_crops_buttons(self):
        p=copy.deepcopy(self.plan)
        p["profiles"][0]["controls"][0]["fallback"]="clip"
        self.assertTrue(any("responsive fallback" in e for e in validate_plan(p)))

    def test_atomic_labels_are_distinct_from_body_copy(self):
        self.assertIn("atomic", {c["behavior"] for p in self.plan["profiles"] for c in p["controls"]})
        self.assertIn("semantic-wrap", {c["behavior"] for p in self.plan["profiles"] for c in p["controls"]})

    def test_rejects_nested_panels_without_semantic_reason(self):
        p=copy.deepcopy(self.plan)
        s=p["profiles"][0]["surfaces"][0]
        p["profiles"][0]["surfaces"].append({"id":"inner", "pattern":"single-panel",
            "reason":"extra", "rejected_pattern":"open-collection", "rejected_reason":"extra", "nested_of":s["id"]})
        self.assertTrue(any("nested surface" in e for e in validate_plan(p)))

    def test_rejects_missing_focus_state(self):
        p=copy.deepcopy(self.plan)
        p["profiles"][0]["controls"][0]["states"]=["default"]
        self.assertTrue(any("focus-visible" in e for e in validate_plan(p)))

    def test_has_unambiguous_cjk_short_actions(self):
        p=next(p for p in self.plan["profiles"] if p["id"]=="operations-run-list")
        self.assertEqual({c["label"] for c in p["controls"] if c["behavior"]=="atomic"}, {"查看详情","重试"})

if __name__=="__main__":
    unittest.main()
