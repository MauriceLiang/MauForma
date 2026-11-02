"""Tests that master/page files are preview-first, safe and preserve user decisions."""
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from init_design_system import make_plan, write_plan


class DesignSystemManagerTests(unittest.TestCase):
    def test_preview_does_not_write(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            plan = make_plan(root, "Test brand", style="editorial", source="confirmed", page="home", mode="Persuade")
            self.assertEqual(len(plan), 3)
            write_plan(plan, apply=False)
            self.assertFalse((root / "design-system").exists())

    def test_apply_keeps_original_by_default(self):
        with tempfile.TemporaryDirectory() as d:
            root = Path(d)
            plan = make_plan(root, "Test", style="functional")
            write_plan(plan, apply=True)
            with self.assertRaises(FileExistsError):
                write_plan(plan, apply=True)
            self.assertIn("delegated", (root / "design-system" / "decisions.json").read_text("utf-8"))

    def test_cannot_traverse_from_page_slug(self):
        with tempfile.TemporaryDirectory() as d:
            with self.assertRaises(ValueError):
                make_plan(Path(d), "Test", page="../escape")

    def test_unselected_direction_stays_unresolved(self):
        with tempfile.TemporaryDirectory() as d:
            plan = make_plan(Path(d), "Test")
            contents = next(v for k, v in plan.items() if k.name == "decisions.json")
            self.assertIn('"source": "unresolved"', contents)


if __name__ == "__main__":
    unittest.main()
