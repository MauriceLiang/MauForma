"""User color must outrank autonomous recommendations and sidebar must match the page."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_sidebar_color_decision import check_colors, contrast, validate_catalog, validate_decision, validate_repository


class SidebarChoiceTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((ROOT / "assets/sidebar-color-directions.json").read_text("utf-8"))
        cls.pending = json.loads((ROOT / "examples/sidebar-color-decision.pending.json").read_text("utf-8"))

    def approved(self, palette_id="light-unified"):
        doc = copy.deepcopy(self.pending)
        doc["status"] = "approved"
        doc["selection"] = {"palette_id": palette_id, "source": "confirmed",
                            "user_statement": "我选择这一套整体配色"}
        doc["resolved_colors"] = copy.deepcopy(next(p["colors"] for p in self.catalog["palettes"] if p["id"] == palette_id))
        doc["review"]["whole_page_preview"] = True
        doc["review"]["coordination_rationale"] = "侧栏、主区域、顶部栏与卡片共享统一明度和文字对比关系"
        return doc

    def errors_contain(self, doc, needle):
        errors = validate_decision(doc, self.catalog)
        self.assertTrue(any(needle in e for e in errors), errors)

    def test_catalog_and_repository(self):
        self.assertEqual(validate_catalog(), [])
        self.assertEqual(validate_repository(), [])

    def test_pending_is_not_approved(self):
        self.assertEqual(validate_decision(self.pending, self.catalog), [])
        self.assertIsNone(self.pending["selection"]["palette_id"])
        self.assertEqual(self.pending["selection"]["source"], "unresolved")

    def test_distinct_full_page_palettes(self):
        palettes = self.catalog["palettes"]
        self.assertGreaterEqual(len(palettes), 4)
        self.assertGreater(len({p["colors"]["main-bg"] for p in palettes}), 2)
        for p in palettes:
            self.assertIn("sidebar-bg", p["colors"])
            self.assertIn("main-bg", p["colors"])
            self.assertIn("chart-primary", p["colors"])

    def test_exact_user_hex_survives_approval(self):
        doc = self.approved("graphite-split")
        doc["user_constraints"] = [{"role": "sidebar-bg", "hex": "#1C2228", "source": "confirmed",
                                    "user_statement": "侧栏背景必须用 #1C2228"}]
        doc["resolved_colors"]["sidebar-bg"] = "#1C2228"
        self.assertEqual(validate_decision(doc, self.catalog), [])

    def test_prevent_silent_override_of_user_hex(self):
        doc = self.approved()
        doc["user_constraints"] = [{"role": "sidebar-bg", "hex": "#1C2228", "source": "confirmed",
                                    "user_statement": "侧栏背景必须用 #1C2228"}]
        self.errors_contain(doc, "User color overridden")

    def test_user_confirmed_requires_statement(self):
        doc = self.approved()
        doc["selection"]["user_statement"] = None
        self.errors_contain(doc, "actual user statement")

    def test_agent_recommendation_cannot_auto_approve(self):
        doc = copy.deepcopy(self.pending)
        doc["selection"] = {"palette_id": "graphite-split", "source": "confirmed",
                            "user_statement": "AI推荐"}
        self.errors_contain(doc, "Pending recommendation cannot")

    def test_approve_requires_full_page_preview(self):
        doc = self.approved()
        doc["review"]["whole_page_preview"] = False
        self.errors_contain(doc, "full-page preview")

    def test_approve_needs_main_sidebar_rationale(self):
        doc = self.approved()
        doc["review"]["coordination_rationale"] = ""
        self.errors_contain(doc, "coordination rationale")

    def test_delegated_requires_explicit_statement(self):
        doc = self.approved()
        doc["selection"]["source"] = "delegated"
        doc["selection"]["user_statement"] = ""
        self.errors_contain(doc, "actual user statement")

    def test_invalid_color_pair_warns_without_recoloring(self):
        doc = self.approved()
        doc["resolved_colors"]["sidebar-text"] = "#DEE5EA"
        self.errors_contain(doc, "contrast")

    def test_catalog_is_original_not_brand_color_copy(self):
        self.assertTrue(all(p["source_type"] == "mauforma_original_interpretation_not_official_colors"
                            for p in self.catalog["palettes"]))

    def test_custom_palette_must_have_fixed_color(self):
        doc = self.approved()
        doc["selection"] = {"palette_id": "custom", "source": "confirmed",
                            "user_statement": "我想用自定义颜色"}
        self.errors_contain(doc, "requires concrete user constraints")

    def test_unverified_browser_pass_blocked(self):
        doc = self.approved()
        doc["review"]["actual_browser_status"] = "PASS"
        self.errors_contain(doc, "Browser PASS requires")

    def test_related_palette_reference_methods(self):
        ids = {r["id"] for r in self.catalog["references"]}
        self.assertTrue({"linear", "carbon", "primer", "shadcn", "atlassian"}.issubset(ids))

    def test_preview_shows_whole_workbench(self):
        html = (ROOT / "assets/sidebar-color-preview.html").read_text("utf-8")
        for key in ("class=\"sidebar\"", "class=\"app\"", "class=\"top\"", "class=\"metric\"",
                    "class=\"panel\"", "id=\"custom-color\"", "id=\"hex\"", "data", "contrast"):
            self.assertIn(key, html)
        self.assertIn("用户未确认", html)


if __name__ == "__main__":
    unittest.main()
