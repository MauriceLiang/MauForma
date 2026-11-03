"""Composition alternatives must be real structural choices, not palette swaps."""
from __future__ import annotations
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_composition_brief import validate_brief, validate_repository


class CompositionBriefTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.base = json.loads((ROOT / "examples/composition/repo-analysis.json").read_text("utf-8"))

    def check_error(self, bad, contains):
        errors = validate_brief(bad)
        self.assertTrue(any(contains in error for error in errors), errors)

    def test_fixture_and_repository_are_valid(self):
        self.assertEqual(validate_brief(self.base), [])
        self.assertEqual(validate_repository(), [])

    def test_three_layouts_not_three_color_skins(self):
        self.assertEqual(len(self.base["candidates"]), 3)
        primary_contents = []
        for c in self.base["candidates"]:
            x = next(r for r in c["regions"] if r["id"] == c["primary_region"])
            primary_contents.append(tuple(x["content_ids"]))
        self.assertEqual(len(set(primary_contents)), 3)

    def test_palette_swap_cannot_count_as_new_composition(self):
        doc = copy.deepcopy(self.base)
        doc["candidates"][1]["regions"] = copy.deepcopy(doc["candidates"][0]["regions"])
        doc["candidates"][1]["primary_region"] = doc["candidates"][0]["primary_region"]
        doc["candidates"][1]["first_screen"] = list(doc["candidates"][0]["first_screen"])
        self.check_error(doc, "duplicate the same first-screen structure")

    def test_unknown_content_is_rejected(self):
        doc = copy.deepcopy(self.base)
        doc["candidates"][0]["regions"][1]["content_ids"].append("invented-metric")
        self.check_error(doc, "unknown content")

    def test_unverified_chart_needs_data_state_plan(self):
        doc = copy.deepcopy(self.base)
        doc["candidates"][0]["regions"][2]["state_strategy"] = ""
        self.check_error(doc, "no loading/empty/error plan")

    def test_selected_layout_requires_provenance(self):
        doc = copy.deepcopy(self.base)
        doc["comparison"]["selection"] = {"id": "trend-first", "source": "unresolved"}
        self.check_error(doc, "needs a confirmed/delegated/inherited source")

    def test_no_pretend_confirmed_without_selection(self):
        doc = copy.deepcopy(self.base)
        doc["comparison"]["selection"] = {"id": None, "source": "confirmed"}
        self.check_error(doc, "without an ID")

    def test_first_screen_needs_primary_region(self):
        doc = copy.deepcopy(self.base)
        doc["candidates"][0]["first_screen"].remove("trend-main")
        self.check_error(doc, "omits primary region")

    def test_decoration_test_must_have_meaning(self):
        doc = copy.deepcopy(self.base)
        doc["review"]["decoration_removed_test"]["passes"] = False
        self.check_error(doc, "Decoration-removed test")

    def test_browser_pass_requires_evidence(self):
        doc = copy.deepcopy(self.base)
        doc["review"]["browser_status"] = "PASS"
        doc["review"]["evidence"] = ""
        self.check_error(doc, "requires actual evidence")

    def test_palette_must_explain_content_reason(self):
        doc = copy.deepcopy(self.base)
        doc["candidates"][0]["palette"]["rationale"] = ""
        self.check_error(doc, "palette needs a sourced")

    def test_duplicate_inventory_ids_are_blocked(self):
        doc = copy.deepcopy(self.base)
        doc["page"]["content_inventory"][1]["id"] = "repository-context"
        self.check_error(doc, "IDs must be present and unique")


if __name__ == "__main__":
    unittest.main()
