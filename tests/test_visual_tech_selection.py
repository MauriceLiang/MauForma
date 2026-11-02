"""Regression tests for the 12-item, role-aware visual technology selection guide."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from search_visual_tech import rank


class VisualTechTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog = json.loads((ROOT / "assets/visual-tech-catalog.json").read_text("utf-8"))

    def test_12_distinct_entries(self):
        self.assertEqual(len(self.catalog["tools"]), 12)
        self.assertEqual(len({x["id"] for x in self.catalog["tools"]}), 12)

    def test_native_filter_not_npm_package(self):
        entry = next(x for x in self.catalog["tools"] if x["id"] == "svg-filter")
        self.assertEqual(entry["kind"], "browser-native")

    def test_splittext_is_not_just_one_library(self):
        t = next(x for x in self.catalog["tools"] if x["id"] == "splittext")
        self.assertIn("animejs", t["combines_with"])
        self.assertIn("gsap", t["combines_with"])
        self.assertIn("alternate_api", t)

    def test_user_goal_2d_physics(self):
        items = rank("刚体 碰撞 重力", limit=4)
        self.assertTrue(items)
        self.assertEqual(items[0]["id"], "matterjs")

    def test_3d_is_not_default_for_chart(self):
        items = rank("数据 图表 仪表盘")
        self.assertTrue(items)
        self.assertEqual(items[0]["id"], "echarts")
        self.assertNotIn("threejs", [x["id"] for x in items])

    def test_handdrawn_vs_pixi(self):
        self.assertEqual(rank("手绘 插画")[0]["id"], "roughjs")

    def test_no_fake_recommendation(self):
        self.assertEqual(rank(""), [])
        self.assertEqual(rank(" completely-unrelated-999999 "), [])

    def test_scenarios_link_known_technologies(self):
        ids = {t["id"] for t in self.catalog["tools"]} | {"native-css", "native-svg"}
        self.assertEqual(len(self.catalog["scenarios"]), 9)
        for s in self.catalog["scenarios"]:
            self.assertTrue(set(s["recommended"]).issubset(ids))
            self.assertTrue(set(s["optional"]).issubset(ids))

    def test_all_entries_have_avoid_and_fallback(self):
        for t in self.catalog["tools"]:
            self.assertTrue(t["avoid"] and t["lightweight_alternative"] and t["api"])


if __name__ == "__main__":
    unittest.main()
