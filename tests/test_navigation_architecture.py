"""Navigation IA and responsive invariants; never mistake a button bar for destinations."""
from __future__ import annotations
import copy
import json
import sys
import unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_navigation_architecture import validate_catalog, validate_decision, validate_repository


class NavigationArchitectureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((ROOT / "assets/navigation-pattern-catalog.json").read_text("utf-8"))
        cls.base = json.loads((ROOT / "examples/navigation-decision.pending.json").read_text("utf-8"))

    def check(self, data, needle):
        issues = validate_decision(data, self.catalog)
        self.assertTrue(any(needle in issue for issue in issues), issues)

    def test_repository_and_pending_example(self):
        self.assertEqual(validate_catalog(), [])
        self.assertEqual(validate_repository(), [])

    def test_nine_distinct_patterns(self):
        self.assertGreaterEqual(len(self.catalog["patterns"]), 9)
        self.assertTrue({"top","side","top-side","rail","bottom","adaptive-side-bottom","top-bottom","side-bottom-tools","focus"}.issubset(
            {p["id"] for p in self.catalog["patterns"]}))

    def test_pending_selection_is_not_approval(self):
        self.assertEqual(self.base["selection"]["status"], "pending")
        self.assertIsNone(self.base["selection"]["pattern_id"])
        self.assertEqual(self.base["selection"]["source"], "unresolved")

    def test_unconsented_pattern_is_rejected(self):
        x = copy.deepcopy(self.base)
        x["selection"]["pattern_id"] = "top-side"
        self.check(x, "Pending navigation recommendation")

    def test_user_confirmed_requires_real_statement(self):
        x = copy.deepcopy(self.base)
        x["selection"] = {"status":"approved","pattern_id":"side","source":"confirmed","user_statement":None}
        self.check(x, "Actual user instruction")

    def test_explicit_delegation_is_valid(self):
        x = copy.deepcopy(self.base)
        x["selection"] = {"status":"approved","pattern_id":"side","source":"delegated","user_statement":"导航结构你决定"}
        self.assertEqual(validate_decision(x, self.catalog), [])

    def test_approval_unknown_pattern_rejected(self):
        x = copy.deepcopy(self.base)
        x["selection"] = {"status":"approved","pattern_id":"wizard","source":"confirmed","user_statement":"选这个"}
        self.check(x, "known pattern")

    def test_bottom_more_than_five_rejected(self):
        x = copy.deepcopy(self.base)
        x["responsive"]["mobile"]["visible_ids"] = [d["id"] for d in x["primary_destinations"]]
        x["responsive"]["mobile"]["overflow_ids"] = []
        self.check(x, "3–5")

    def test_bottom_has_reachable_overflow(self):
        x = copy.deepcopy(self.base)
        x["responsive"]["mobile"]["overflow_ids"].remove("research")
        self.check(x, "reachability")

    def test_duplicate_mobile_and_more_rejected(self):
        x = copy.deepcopy(self.base)
        x["responsive"]["mobile"]["overflow_ids"].append("overview")
        self.check(x, "both visible and overflow")

    def test_unknown_route_id_rejected(self):
        x = copy.deepcopy(self.base)
        x["responsive"]["mobile"]["visible_ids"][0] = "ghost"
        self.check(x, "unknown destination")

    def test_mapping_does_not_erase_desktop_destinations(self):
        x = copy.deepcopy(self.base)
        x["responsive"]["desktop"]["visible_ids"].pop()
        self.check(x, "Desktop mapping")

    def test_destination_identity_is_stable(self):
        x = copy.deepcopy(self.base)
        x["responsive"]["same_destination_ids"] = False
        self.check(x, "preserve destination identity")

    def test_context_is_preserved_on_resize(self):
        x = copy.deepcopy(self.base)
        x["responsive"]["context_preserved"] = False
        self.check(x, "preserve destination identity")

    def test_bottom_actions_are_not_bottom_nav(self):
        x = copy.deepcopy(self.base)
        x["responsive"]["desktop"]["mode"] = "side-bottom-tools"
        x["responsive"]["mobile"]["mode"] = "bottom"
        self.check(x, "Bottom action bar")

    def test_browser_pass_requires_two_viewports_and_evidence(self):
        x = copy.deepcopy(self.base)
        x["review"]["browser_status"] = "PASS"
        self.check(x, "breakpoints and evidence")

    def test_official_reference_source_is_not_theme_copy(self):
        self.assertGreaterEqual(len(self.catalog["references"]), 6)
        self.assertTrue(any("Atlassian" in x["title"] for x in self.catalog["references"]))

    def test_preview_preserves_responsive_labels(self):
        html = (ROOT / "assets/navigation-layout-lab.html").read_text("utf-8")
        for token in ("data-pattern","data-viewport","aria-current","bottom-actions","bottom-nav","top-nav","side-nav"):
            self.assertIn(token, html)

    def test_schema_contains_explicit_provenance(self):
        schema = json.loads((ROOT / "assets/navigation-decision.schema.json").read_text("utf-8"))
        self.assertIn("selection", schema["properties"])
        self.assertIn("user_statement", schema["properties"]["selection"]["properties"])


if __name__ == "__main__":
    unittest.main()
