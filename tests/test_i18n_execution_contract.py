"""Internationalization contracts that preserve runtime UX constraints."""
from __future__ import annotations

import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class InternationalExecutionContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.en = (ROOT / "SKILL.md").read_text("utf-8")
        cls.en_readme = (ROOT / "README.md").read_text("utf-8")
        cls.zh_readme = (ROOT / "README.zh-CN.md").read_text("utf-8")
        cls.handbook = (ROOT / "references/execution-handbook.en.md").read_text("utf-8")

    def test_frontmatter_and_english_first_execution_sections(self):
        self.assertTrue(self.en.startswith("---\nname: mauforma\n"))
        for marker in (
            "Scope, authority and language",
            "Efficient on-demand reference routing",
            "Execution process",
            "Acceptance and escalation",
            "Opt-in tools",
        ):
            self.assertIn(marker, self.en)
        self.assertLess(len(self.en.encode("utf-8")), 25000)
        self.assertNotIn("\\" + chr(96), self.en, "Do not escape inline Markdown code spans")

    def test_important_design_gates_survive_translation(self):
        for marker in (
            "Gate H-Base / H0", "existing", "eyebrow",
            "surface-edge-accent-gate.md", "Gate S0",
            "Component Library", "prefers-reduced-motion",
            "CAPTURED_FOR_REVIEW", "design-system/MASTER.md",
            "confirmed / inherited / delegated / proposed / unresolved",
            "file", "actual", "frontend",
        ):
            self.assertIn(marker.casefold(), self.en.casefold(), marker)

    def test_execution_boundaries_dont_translate_customer_ui(self):
        for marker in (
            "user's requested language", "English",
            "actual target languages", "brand",
            "do not", "responsive",
            "NOT TESTED", "BLOCKED", "STATIC CHECK",
            "DEMO ONLY", "VERIFIED",
        ):
            self.assertIn(marker.casefold(), self.en.casefold(), marker)
        for marker in ("No arbitrary translation", "200% text scaling",
                       "user's preferred language", "real product",
                       "not an approved decision"):
            self.assertIn(marker.casefold(), self.handbook.casefold(), marker)

    def test_english_reference_handbook_is_self_sufficient(self):
        for marker in ("Operate", "Read", "Persuade", "Experience",
                       "Gate H0", "Gate S0", "React", "Vue",
                       "Motion", "Keyboard", "VERIFIED", "STATIC CHECK"):
            self.assertIn(marker.casefold(), self.handbook.casefold(), marker)
        self.assertIn("Never eagerly load the whole", self.handbook)

    def test_full_language_navigation_and_attribution(self):
        self.assertIn("[English](README.md)", self.en_readme)
        self.assertIn("[简体中文](README.zh-CN.md)", self.en_readme)
        self.assertIn("[English](README.md)", self.zh_readme)
        self.assertIn("[简体中文](README.zh-CN.md)", self.zh_readme)
        for marker in (
            "Overview", "Quick start", "Capabilities", "Quality assurance",
            "Open source influences and acknowledgments", "Stageshow",
            "nextlevelbuilder/ui-ux-pro-max-skill",
            "vuejs-ai/skills", "openai/skills",
            "Lucide", "Motion Continuity Lab", "liquid-glass-optics.md",
        ):
            self.assertIn(marker, self.en_readme)
        for marker in ("这是什么", "工作方式", "快速开始", "开源参考与致谢"):
            self.assertIn(marker, self.zh_readme)

    def test_only_one_active_agent_entrypoint_and_full_chinese_readme(self):
        self.assertFalse((ROOT / "SKILL.zh-CN.md").exists())
        self.assertIn("single active Agent entrypoint", self.en)
        self.assertIn("one primary guide", self.en)
        self.assertIn("中文 README", self.zh_readme)
        self.assertIn("English", self.en_readme)

    def test_runtime_docs_do_not_require_historical_audits(self):
        for text in (self.en, self.handbook, self.en_readme, self.zh_readme):
            self.assertNotIn("upstream-reassessment.en.md", text)
            self.assertNotIn("i18n-runtime-validation.en.md", text)
            self.assertNotIn("SKILL.zh-CN.md", text)
            self.assertNotIn("CHANGELOG.md", text)
        self.assertIn("references/semantic-boundaries.en.md", self.en)
        self.assertIn("README.zh-CN.md", self.en)


if __name__ == "__main__":
    unittest.main()
