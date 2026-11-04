"""Regression checks for reusable hierarchy and component craft across page categories."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_visual_priority import validate_plan, validate_repository


class UniversalVisualPriorityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sample = json.loads((ROOT / "assets/visual-priority-patterns.json").read_text("utf-8"))

    def test_repository_links_and_four_distinct_modes(self):
        self.assertEqual(validate_repository(), [])

    def test_rejects_important_content_as_caption(self):
        data = copy.deepcopy(self.sample)
        data["pages"][0]["info_items"][1]["type_role"] = "caption"
        self.assertTrue(any("relegated to caption" in x for x in validate_plan(data)))

    def test_rejects_all_information_same_treatment(self):
        data = copy.deepcopy(self.sample)
        for item in data["pages"][0]["info_items"]:
            item["type_role"] = "body"
        self.assertTrue(any("one text treatment" in x for x in validate_plan(data)))

    def test_rejects_many_competing_foci(self):
        data = copy.deepcopy(self.sample)
        for item in data["pages"][0]["info_items"][:3]:
            item["priority"] = "P0"
        self.assertTrue(any("competing P0" in x for x in validate_plan(data)))

    def test_rejects_missing_component_focus_state(self):
        data = copy.deepcopy(self.sample)
        data["pages"][2]["components"][0]["states"].remove("focus-visible")
        self.assertTrue(any("focus-visible" in x for x in validate_plan(data)))

    def test_all_four_modes_have_different_primary_goals(self):
        self.assertEqual({p["mode"] for p in self.sample["pages"]}, {"Operate", "Persuade", "Read", "Experience"})
        self.assertEqual(len({p["user_goal"] for p in self.sample["pages"]}), 4)

    def test_does_not_require_fixed_pixel_values(self):
        self.assertEqual(validate_plan(self.sample), [])
        self.assertNotIn("font_px", json.dumps(self.sample))

    def test_legitimate_supporting_readability_is_preserved(self):
        pages = self.sample["pages"]
        self.assertTrue(any(i["priority"] == "P3" and i["type_role"] == "supporting"
                            for page in pages for i in page["info_items"]))


if __name__ == "__main__":
    unittest.main()
