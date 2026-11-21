"""Keep high-frequency Skill guidance concise while retaining attribution and licensing."""
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]


class CreditsAndMotionReviewTests(unittest.TestCase):
    def test_acknowledgements_are_centralized(self):
        readme = (ROOT / "README.md").read_text(encoding="utf-8")
        for term in (
            "## Open source influences and acknowledgments",
            "benjitaylor/skills/tree/main/stageshow",
            "anthropics/skills/tree/main/skills/frontend-design",
            "pbakaus/impeccable",
            "senlindesign/taste-skill",
            "Leonxlnx/taste-skill",
            "anthropics/skills/tree/main/skills/theme-factory",
            "julianoczkowski/designer-skills",
            "nextlevelbuilder/ui-ux-pro-max-skill",
            "vercel-labs/agent-skills/tree/main/skills/web-design-guidelines",
            "vercel-labs/agent-skills/tree/main/skills/composition-patterns",
            "vercel-labs/agent-skills/tree/main/skills/react-best-practices",
            "vuejs-ai/skills/tree/main/skills/vue-best-practices",
            "anthropics/skills/tree/main/skills/webapp-testing",
            "openai/skills/tree/main/skills/.curated/figma-implement-design",
            "React Bits",
            "Vue Bits",
            "Lucide license notice",
        ):
            self.assertIn(term, readme, term)
        self.assertTrue((ROOT / "assets/icon-art-direction-lucide-license.txt").is_file())

    def test_motion_rules_are_not_a_source_bibliography(self):
        for file in (
            "references/motion-craft-and-continuity.md",
            "references/motion-rehearsal-and-evidence.md",
            "references/design-craft-loop.md",
        ):
            body = (ROOT / file).read_text(encoding="utf-8")
            self.assertNotIn("github.com/benjitaylor", body, file)
            self.assertNotIn("https://github.com/anthropics", body, file)
        self.assertNotIn(
            "Stageshow",
            (ROOT / "references/motion-craft-and-continuity.md").read_text(encoding="utf-8"),
        )

    def test_fresh_eye_and_local_track_rules_present(self):
        craft = (ROOT / "references/motion-craft-and-continuity.md").read_text(encoding="utf-8")
        rehearsal = (ROOT / "references/motion-rehearsal-and-evidence.md").read_text(encoding="utf-8")
        self.assertIn("Independent fresh-eye visual review", craft)
        self.assertIn("Stable chrome / local tracks", craft)
        self.assertIn("Independent review:", rehearsal)
        self.assertIn("NOT REVIEWED", rehearsal)

    def test_entrypoint_points_to_readme_without_overloading(self):
        entry = (ROOT / "SKILL.md").read_text(encoding="utf-8")
        self.assertIn("Source acknowledgements are in", entry)
        self.assertNotIn("github.com/benjitaylor", entry)


if __name__ == "__main__":
    unittest.main()
