"""Static checks for creative motion vocabulary and catalog/gallery parity."""
import json
import re
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
NEW = {
    "spring-feedback", "text-shimmer", "text-morph", "smooth-scroll",
    "scroll-zoom", "image-sequence", "horizontal-scroll", "scroll-snap", "marquee",
}
CURATED = (
    "Easing", "Spring", "Basic entrance", "Line reveal", "Stagger",
    "Blur reveal", "Mask/clip reveal", "Text shimmer", "Character reveal",
    "Scramble text", "Text morphing", "Typewriter", "Smooth scroll",
    "Scroll-triggered", "Scroll-linked", "Parallax", "Sticky scrollytelling",
    "Scroll zoom", "Image sequence", "Horizontal scroll", "Scroll snap", "Marquee",
)


class ExpressiveMotionVocabularyTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.doc = (ROOT / "references/expressive-motion-vocabulary.md").read_text("utf-8")
        cls.data = json.loads((ROOT / "assets/motion-effects.json").read_text("utf-8"))
        cls.gallery = (ROOT / "assets/motion-gallery.html").read_text("utf-8")
        cls.legacy = (ROOT / "references/animejs-motion-recipes.md").read_text("utf-8")

    def test_twenty_two_curated_terms_are_documented_independently(self):
        rows = [line for line in self.doc.splitlines() if line.startswith("| **")]
        self.assertEqual(len(rows), 22)
        for term in CURATED:
            self.assertEqual(sum(f"| **{term} " in row for row in rows), 1, term)

    def test_all_114_legacy_recipes_remain_plus_exactly_nine_new(self):
        original = re.findall(r"^\|\s*\`([a-z0-9-]+)\`\s*/", self.legacy, re.M)
        self.assertEqual(len(original), 114)
        ids = [e["id"] for e in self.data["effects"]]
        self.assertEqual(len(ids), 123)
        self.assertEqual(len(ids), len(set(ids)))
        self.assertEqual(set(ids) - set(original), NEW)

    def test_new_recipes_are_actionable_not_just_names(self):
        entries = {e["id"]: e for e in self.data["effects"]}
        for key in NEW:
            recipe = entries[key]
            for field in ("name", "effect", "good_for", "avoid", "animejs_mapping",
                          "english_name", "fallback", "category", "preview"):
                self.assertTrue(isinstance(recipe.get(field), str) and recipe[field].strip(), (key, field))
            self.assertIn(recipe["tier"], {"A", "B", "C"})
            self.assertIn(key, self.doc)

    def test_different_mechanisms_are_not_mislabeled(self):
        for term in ("NOT §skeleton-shimmer§", "NOT §svg-morph§",
                     "NOT §horizontal-reveal§", "NOT §scroll-snap-feedback§",
                     "Scroll-triggered is time-based", "scroll-linked is progress-based"):
            self.assertIn(term.replace("§", chr(96)).lower(), self.doc.lower())

    def test_skill_proactively_routes_creative_motion_when_authorized(self):
        skill = (ROOT / "SKILL.md").read_text("utf-8")
        craft = (ROOT / "references/motion-craft-and-continuity.md").read_text("utf-8")
        self.assertIn("expressive-motion-vocabulary.md", skill)
        self.assertIn("proactively propose", skill)
        self.assertIn("标志性动效", craft)
        self.assertIn("Do not wait for the user", self.doc)
        self.assertIn("reduced motion", self.doc.lower())

    def test_gallery_matches_catalog_and_has_concept_demos(self):
        a = self.gallery.index("const EFFECTS=") + len("const EFFECTS=")
        b = self.gallery.index("; const EASINGS=", a)
        self.assertEqual(json.loads(self.gallery[a:b]), self.data["effects"])
        self.assertIn("123 种动效配方", self.gallery)
        self.assertIn("EFFECTS.length", self.gallery)
        for effect in NEW:
            self.assertIn("e.id==='" + effect + "'", self.gallery, effect)

    def test_cross_framework_naming_and_bilingual_discovery(self):
        self.assertIn("not necessarily official", self.doc.lower())
        self.assertIn("不代表 Anime.js", self.data["meta"]["claim"])
        self.assertIn("Scroll-driven Animations", self.doc)
        for name in ("README.md", "README.zh-CN.md"):
            self.assertIn("expressive-motion-vocabulary.md", (ROOT / name).read_text("utf-8"))


if __name__ == "__main__":
    unittest.main()
