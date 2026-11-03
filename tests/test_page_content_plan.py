"""Regression tests for content curation, purposeful whitespace and page-level density."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_page_content_plan import validate_catalog, validate_plan, validate_repository


class PageContentPlanTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((ROOT / "assets/page-density-profiles.json").read_text("utf-8"))
        cls.example = json.loads((ROOT / "examples/page-content-plan-repovantage.json").read_text("utf-8"))

    def errors_include(self, doc, fragment):
        errors = validate_plan(doc, self.catalog)
        self.assertTrue(any(fragment in e for e in errors), errors)

    def test_repository_files_and_example(self):
        self.assertEqual(validate_repository(), [])

    def test_four_distinct_density_profiles(self):
        self.assertEqual({p["id"] for p in self.catalog["profiles"]},
                         {"airy", "balanced", "productive", "compact"})

    def test_overview_and_analysis_have_different_density(self):
        p = {x["page_role"]: x["density_profile"] for x in self.example["pages"]}
        self.assertEqual(p["overview"], "airy")
        self.assertEqual(p["analysis"], "productive")

    def test_provisional_is_not_user_confirmed(self):
        self.assertTrue(all(p["density_decision"]["source"] == "provisional"
                            for p in self.example["pages"]))

    def test_content_priority_has_one_first_task(self):
        p = self.example["pages"][0]
        self.assertTrue(p["primary_task"])
        self.assertIn("current-repository", p["layout"]["above_fold"])

    def test_cannot_remove_critical_data_notice(self):
        doc = copy.deepcopy(self.example)
        note = next(x for x in doc["pages"][0]["content"] if x["id"] == "data-disclaimer")
        note["placement"] = "removed"
        note["duplicate_of"] = "page-title"
        self.errors_include(doc, "critical information cannot")

    def test_deferred_content_requires_route_or_trigger(self):
        doc = copy.deepcopy(self.example)
        x = next(c for c in doc["pages"][0]["content"] if c["id"] == "feature-directory")
        x["accessible_via"] = ""
        self.errors_include(doc, "discoverable access")

    def test_conditional_intro_requires_state(self):
        doc = copy.deepcopy(self.example)
        x = next(c for c in doc["pages"][0]["content"] if c["id"] == "full-onboarding")
        x.pop("condition")
        self.errors_include(doc, "needs user state")

    def test_cannot_mark_duplicate_without_basis(self):
        doc = copy.deepcopy(self.example)
        x = next(c for c in doc["pages"][0]["content"] if c["id"] == "repeated-footer-link")
        x["duplicate_of"] = "missing-target"
        self.errors_include(doc, "reference its redundancy")

    def test_no_multiple_competing_primary_buttons(self):
        doc = copy.deepcopy(self.example)
        x = doc["pages"][0]["actions"][1]
        x["priority"] = "primary"
        self.errors_include(doc, "competing primary actions")

    def test_deferred_card_not_above_fold(self):
        doc = copy.deepcopy(self.example)
        doc["pages"][0]["layout"]["above_fold"].append("feature-directory")
        self.errors_include(doc, "removed/deferred content shown above fold")

    def test_primary_content_visible_above_fold(self):
        doc = copy.deepcopy(self.example)
        doc["pages"][0]["layout"]["above_fold"] = ["data-disclaimer"]
        self.errors_include(doc, "primary task is not visible")

    def test_nested_decorative_wrappers_fail(self):
        doc = copy.deepcopy(self.example)
        doc["pages"][0]["layout"]["nested_decorative_cards"] = True
        self.errors_include(doc, "nested decorative cards")

    def test_confirmed_density_requires_real_user_statement(self):
        doc = copy.deepcopy(self.example)
        doc["pages"][0]["density_decision"]["source"] = "confirmed"
        self.errors_include(doc, "actual statement")

    def test_approved_user_density_allowed_with_statement(self):
        doc = copy.deepcopy(self.example)
        doc["pages"][0]["density_decision"]["source"] = "confirmed"
        doc["pages"][0]["density_decision"]["user_statement"] = "我想总览宽松一些"
        self.assertEqual(validate_plan(doc, self.catalog), [])

    def test_browser_pass_without_evidence_rejected(self):
        doc = copy.deepcopy(self.example)
        doc["pages"][0]["review"]["browser_status"] = "PASS"
        self.errors_include(doc, "without evidence")

    def test_unrecognized_density_profile_rejected(self):
        doc = copy.deepcopy(self.example)
        doc["pages"][0]["density_profile"] = "all-pages-tiny-text"
        self.errors_include(doc, "unknown page-level density")

    def test_sources_reference_progressive_disclosure(self):
        links = [x["url"] for x in self.catalog["sources"]]
        self.assertTrue(any("nngroup.com" in x for x in links))
        self.assertTrue(any("carbondesignsystem.com" in x for x in links))

    def test_gallery_contains_overview_and_detail_modes(self):
        html = (ROOT / "assets/page-density-lab.html").read_text("utf-8")
        for text in ('data-variant="overloaded"', 'data-variant="curated"',
                     'data-variant="analysis"', 'id="first-visit"',
                     'id="workbench"', 'id="main-region"'):
            self.assertIn(text, html)


if __name__ == "__main__":
    unittest.main()
