"""Regression tests for role-driven typography and semantic copy hygiene."""
from __future__ import annotations

import copy
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from audit_readability import analyze, scan, validate_catalog


class ReadabilityRulesTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((ROOT / "assets/typography-role-guidelines.json").read_text("utf-8"))

    def rules(self, text: str) -> set[str]:
        return {item["rule"] for item in analyze(text)}

    def test_role_profiles_validate(self):
        self.assertEqual(validate_catalog(), [])

    def test_workspace_chart_labels_are_explicit_roles(self):
        role_ids = {r["id"] for p in self.catalog["profiles"]
                    if p["id"] == "operate-desktop" for r in p["roles"]}
        self.assertIn("chart-axis", role_ids)
        self.assertIn("chart-legend", role_ids)
        self.assertIn("metric-label", role_ids)
        self.assertIn("metadata", role_ids)

    def test_large_title_role_not_required_for_workbench(self):
        p = next(p for p in self.catalog["profiles"] if p["id"] == "operate-desktop")
        h1 = next(r for r in p["roles"] if r["id"] == "page-title")
        self.assertLessEqual(h1["recommended_px"], 30)

    def test_persuade_has_distinct_hero_role(self):
        p = next(p for p in self.catalog["profiles"] if p["id"] == "persuade-landing")
        self.assertIn("hero-title", [r["id"] for r in p["roles"]])

    def test_small_css_px_is_review_candidate(self):
        self.assertIn("potentially-tiny-text", self.rules(".axis{font-size:10px;}"))

    def test_small_css_rem_is_review_candidate(self):
        self.assertIn("potentially-tiny-text", self.rules(".muted{font-size:0.625rem;}"))

    def test_readable_css_does_not_raise_tiny_warning(self):
        self.assertNotIn("potentially-tiny-text", self.rules(".axis{font-size:13px;}"))

    def test_tailwind_arbitrary_small_size_is_detected(self):
        self.assertIn("potentially-tiny-text", self.rules('<span className="text-[10px]">日期</span>'))

    def test_decorative_section_index_is_flagged(self):
        self.assertIn("decorative-section-index", self.rules("<span>01 / 总览</span>"))

    def test_actual_breadcrumb_does_not_trigger(self):
        self.assertEqual(self.rules("<nav>仓库 / steady-core</nav>"), set())

    def test_brand_strapline_is_advisory(self):
        self.assertIn("generic-brand-subtitle", self.rules("<small>ANALYSIS STUDIO</small>"))

    def test_technical_implementation_note_is_reviewed(self):
        self.assertIn("developer-notes-visible", self.rules("<span>主图保留原生 ECharts tooltip</span>"))

    def test_no_automatic_rewrite_or_deletion(self):
        original = "<span>01 / 总览</span>"
        result = analyze(original)
        self.assertTrue(result)
        self.assertEqual(original, "<span>01 / 总览</span>")

    def test_ignores_node_modules_and_non_source_files(self):
        with tempfile.TemporaryDirectory() as root:
            base = Path(root)
            (base / "src").mkdir()
            (base / "node_modules").mkdir()
            (base / "src" / "Page.vue").write_text("<div style='font-size:10px'>x</div>", "utf-8")
            (base / "node_modules" / "Lib.vue").write_text("<div style='font-size:9px'>y</div>", "utf-8")
            items = scan(base)
            self.assertEqual(len(items), 1)
            self.assertIn("Page.vue", items[0]["file"])

    def test_catalog_rejects_unreasonably_small_start(self):
        data = copy.deepcopy(self.catalog)
        data["profiles"][0]["roles"][0]["recommended_px"] = 7
        self.assertTrue(validate_catalog(data))

    def test_source_guide_preserves_legitimate_small_headings(self):
        text = (ROOT / "references/semantic-copy-hygiene.md").read_text("utf-8")
        for term in ("面包屑", "品牌", "数据来源", "功能性"):
            self.assertIn(term, text)


if __name__ == "__main__":
    unittest.main()
