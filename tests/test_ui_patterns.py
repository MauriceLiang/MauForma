"""Regression checks for high-frequency UI patterns and sidebar color-harmony examples."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_ui_patterns import contrast, validate


class SidebarPaletteTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = json.loads((ROOT / "assets/sidebar-palette-examples.json").read_text("utf-8"))

    def test_complete_contract(self):
        self.assertEqual(validate(), [])

    def test_palette_is_independent_for_light_dark(self):
        a = self.data["palettes"]
        self.assertNotEqual(a["light"]["colors"]["sidebar-bg"], a["dark"]["colors"]["sidebar-bg"])
        self.assertNotEqual(a["light"]["colors"]["sidebar-selected"], a["dark"]["colors"]["sidebar-selected"])

    def test_high_legibility_in_selected_navigation(self):
        for scheme in self.data["palettes"].values():
            colors = scheme["colors"]
            self.assertGreaterEqual(contrast(colors["sidebar-text"], colors["sidebar-selected"]), 4.5)

    def test_keyboard_focus_remains_separate(self):
        for scheme in self.data["palettes"].values():
            colors = scheme["colors"]
            self.assertGreaterEqual(contrast(colors["sidebar-focus"], colors["sidebar-selected"]), 3)

    def test_inaccessible_muted_text_is_detected(self):
        sample = json.loads(json.dumps(self.data))
        sample["palettes"]["dark"]["colors"]["sidebar-text-muted"] = "#283440"
        self.assertTrue(any("contrast" in e for e in validate(sample)))

    def test_rail_is_not_prohibited_universally(self):
        doc = (ROOT / "references/sidebar-navigation-design.md").read_text("utf-8")
        self.assertIn("时间轴", doc)
        self.assertIn("例外", doc)
        self.assertIn("树", doc)

    def test_seven_component_patterns_covered(self):
        s = (ROOT / "references/workspace-component-refinement.md").read_text("utf-8")
        for component in ("Sidebar", "Topbar", "Card", "Data table",
                          "Tabs", "Search", "Split pane"):
            self.assertIn(component, s)

    def test_gallery_switches_states_and_has_reduced_motion(self):
        s = (ROOT / "assets/sidebar-refinement-gallery.html").read_text("utf-8")
        for token in ("data-select-group", "aria-pressed", "aria-selected",
                      "ArrowRight", "prefers-reduced-motion"):
            self.assertIn(token, s)

    def test_primary_selection_does_not_need_extra_rail(self):
        s = (ROOT / "assets/sidebar-refinement-gallery.html").read_text("utf-8")
        self.assertIn(".noisy .item[aria-pressed=true]", s)
        self.assertIn(".item[aria-pressed=true]", s)
        # Highlight rail is intentionally contained in the "before" counterexample.
        self.assertIn("inset 4px 0", s)


if __name__ == "__main__":
    unittest.main()
