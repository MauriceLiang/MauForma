"""Guard four-layer glass learning against decorative defaults and false compatibility claims."""
from pathlib import Path
import sys
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from validate_liquid_glass import validate_repository
from search_visual_tech import rank


class LiquidGlassGuideTests(unittest.TestCase):
    def test_repository_integration_complete(self):
        self.assertEqual(validate_repository(), [])

    def test_on_demand_discovery_in_existing_svg_filter_stack(self):
        found = rank("液态玻璃 折射", limit=12)
        self.assertTrue(any(item["id"] == "svg-filter" for item in found), found)

    def test_video_layers_and_optional_blur_are_distinct(self):
        text = (ROOT / "references/liquid-glass-optics.md").read_text("utf-8")
        for word in ("透明", "折射", "高光", "阴影", "可选背景模糊"):
            self.assertIn(word, text)
        self.assertIn("模糊过强", text)

    def test_svg_backdrop_not_assumed_cross_browser(self):
        text = (ROOT / "references/liquid-glass-optics.md").read_text("utf-8")
        for token in ("feDisplacementMap", "Safari", "Firefox", "CSS.supports", "WebKit",
                      "NOT TESTED", "SVG Filter", "WebGL"):
            self.assertIn(token, text)

    def test_demo_never_claims_actual_optical_proof(self):
        demo = (ROOT / "assets/liquid-glass-layer-lab.html").read_text("utf-8")
        self.assertIn('data-refraction-attempt="fallback"', demo)
        self.assertIn("未自动验证", demo)
        self.assertIn("候选语法", demo)
        self.assertIn("CSS.supports", demo)
        self.assertIn("aria-live", demo)

    def test_core_is_task_routed_not_default_theme(self):
        skill = (ROOT / "SKILL.md").read_text("utf-8")
        self.assertIn("用户明确要求液态玻璃", skill)
        self.assertIn("仅按需", skill)
        self.assertIn("references/liquid-glass-optics.md", skill)


if __name__ == "__main__":
    unittest.main()
