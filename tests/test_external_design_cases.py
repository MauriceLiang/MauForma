"""Regression tests for external brand DESIGN.md index; never fetch upstream during CI."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from search_design_cases import find_cases


class ExternalCaseTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / "assets/external-design-cases.json").read_text("utf-8"))

    def test_count_and_unique_sources(self):
        cases = self.data["cases"]
        self.assertEqual(len(cases), 84)
        self.assertEqual(len(set(c["id"] for c in cases)), 84)
        self.assertTrue(all(c["source_url"].startswith("https://github.com/VoltAgent/")
                            for c in cases))

    def test_community_not_official(self):
        self.assertTrue(all(c["source_type"] == "third_party_design_analysis_not_brand_official"
                            for c in self.data["cases"]))

    def test_food_matches_reviewed_starbucks(self):
        a = find_cases(query="咖啡 门店", style="premium-showcase")
        self.assertTrue(a)
        self.assertEqual(a[0]["id"], "starbucks")
        self.assertEqual(a[0]["status"], "sampled")

    def test_tech_style_matches_linear(self):
        matches = find_cases(query="开发工具", style="calm-minimal")
        self.assertIn("linear.app", [x["id"] for x in matches])

    def test_unreviewed_only_by_explicit_flag(self):
        self.assertEqual(find_cases(query="nvidia"), [])
        matched = find_cases(query="nvidia", include_unreviewed=True)
        self.assertEqual(matched[0]["id"], "nvidia")
        self.assertEqual(matched[0]["status"], "indexed_unreviewed")

    def test_no_blank_query_fake_results(self):
        self.assertEqual(find_cases(""), [])


if __name__ == "__main__":
    unittest.main()
