"""MauForma style ranking and static audit regression tests (stdlib unittest)."""
import json
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from search_design_knowledge import rank_styles
from audit_frontend import scan
from validate_intelligence import validate


class DesignKnowledgeTests(unittest.TestCase):
    def test_style_catalog_valid(self):
        self.assertEqual(validate(), [])

    def test_food_photography_prefers_showcase(self):
        ranked = rank_styles("甜品 食物 产品 摄影", "Persuade")
        self.assertTrue(ranked)
        self.assertEqual(ranked[0]["id"], "premium-showcase")

    def test_admin_task_prefers_functional(self):
        ranked = rank_styles("后台 工单 表格", "Operate")
        self.assertEqual(ranked[0]["id"], "functional")

    def test_docs_prefers_reading(self):
        ranked = rank_styles("文档 文章", "Read")
        self.assertEqual(ranked[0]["id"], "reading-first")

    def test_blank_query_does_not_invent_recommendations(self):
        self.assertEqual(rank_styles(""), [])

    def test_results_not_mislabelled_confirmed(self):
        self.assertTrue(all(r["status"] == "recommendation_not_user_confirmed" for r in rank_styles("摄影")))


class StaticAuditTests(unittest.TestCase):
    def test_detects_common_accessibility_and_motion_risks(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "bad.html"
            p.write_text('<div onClick={go}>Go</div>\n<img src="x.png">\n'
                         '<a href="#">Continue</a><style>.x{transition: all .3s;animation:spin 2s infinite}</style>')
            issues = scan(Path(d))
            codes = {i["code"] for i in issues}
            for expected in ("MF101", "MF102", "MF103", "MF105", "MF107"):
                self.assertIn(expected, codes)

    def test_reduced_motion_included_no_global_warning(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "ok.css"
            p.write_text('@keyframes fade {to{opacity:1}}@media(prefers-reduced-motion:reduce){.x{animation:none}}')
            self.assertNotIn("MF107", {i["code"] for i in scan(Path(d))})

    def test_ignores_node_modules(self):
        with tempfile.TemporaryDirectory() as d:
            p = Path(d) / "node_modules" / "bad.jsx"
            p.parent.mkdir()
            p.write_text('<div onClick={f}>x</div>')
            self.assertEqual(scan(Path(d)), [])


if __name__ == "__main__":
    unittest.main()
