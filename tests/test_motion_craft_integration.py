"""Static integration checks for MauForma's motion craft workflow.

These tests do not claim aesthetic quality or actual app E2E coverage.
"""
import json
from pathlib import Path
import re
import shutil
import subprocess
import unittest

ROOT = Path(__file__).resolve().parents[1]


class MotionCraftIntegrationTests(unittest.TestCase):
    def test_entrypoints_route_to_new_rules(self):
        for name in ("SKILL.md", "README.md", "references/visual-qa.md",
                     "references/browser-qa-protocol.md"):
            text = (ROOT / name).read_text(encoding="utf-8")
            self.assertIn("motion-craft-and-continuity.md", text, name)
            self.assertIn("motion-rehearsal-and-evidence.md", text, name)

    def test_contract_documents_and_script_exist(self):
        for name in ("references/motion-craft-and-continuity.md",
                     "references/motion-rehearsal-and-evidence.md",
                     "scripts/motion_rehearsal.mjs",
                     "assets/motion-rehearsal-scenario.example.json",
                     "assets/motion-continuity-lab.html",
                     "assets/motion-continuity-lab.scenario.json"):
            self.assertTrue((ROOT / name).is_file(), name)

    def test_demo_scenario_selectors_exist_in_synthetic_lab(self):
        scenario = json.loads((ROOT / "assets/motion-continuity-lab.scenario.json").read_text(encoding="utf-8"))
        lab = (ROOT / "assets/motion-continuity-lab.html").read_text(encoding="utf-8")
        self.assertTrue(scenario["steps"])
        for step in scenario["steps"]:
            self.assertIn(step["action"], {"click", "hover", "fill", "press", "wait", "reduced-motion"})
            selectors = [step.get("selector", ""), *step.get("track", [])]
            for selector in selectors:
                for value in re.findall(r"data-motion-demo='([^']+)'", selector):
                    self.assertIn('data-motion-demo="' + value + '"', lab)
        self.assertIn("prefers-reduced-motion", lab)

    @unittest.skipUnless(shutil.which("node"), "Node.js is not installed")
    def test_node_script_syntax_and_help(self):
        script = ROOT / "scripts/motion_rehearsal.mjs"
        for command in (["node", "--check", str(script)], ["node", str(script), "--help"]):
            result = subprocess.run(command, text=True, capture_output=True, timeout=15)
            self.assertEqual(result.returncode, 0, result.stderr)
        self.assertIn("Motion", (ROOT / "references/motion-rehearsal-and-evidence.md").read_text(encoding="utf-8"))


if __name__ == "__main__":
    unittest.main()
