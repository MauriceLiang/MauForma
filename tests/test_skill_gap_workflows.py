"""Functional CLI tests for opt-in design workflows (no web access or project mutation)."""
from __future__ import annotations
import json
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SCRIPTS = ROOT / "scripts"

def cli(script, *args, expected=0):
    result = subprocess.run([sys.executable, str(SCRIPTS / script), *map(str, args)],
                            text=True, capture_output=True, timeout=20)
    if result.returncode != expected:
        raise AssertionError(f"{script}: expected {expected} got {result.returncode}\n{result.stdout}\n{result.stderr}")
    return result.stdout

class SkillGapTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)

    def test_drift_baseline_detects_actual_change_without_rewriting_master(self):
        css = self.root / "app.css"
        css.write_text(":root { --brand: #112233; } .b{color:var(--brand)}", encoding="utf-8")
        master = self.root / "design-system" / "MASTER.md"
        master.parent.mkdir(parents=True)
        master.write_text("Confirmed brand must stay untouched\n", encoding="utf-8")
        cli("check_design_drift.py", "--root", self.root, "--write-baseline", "--format", "json")
        baseline = self.root / "design-system" / "observed-tokens.json"
        self.assertTrue(baseline.exists())
        result = json.loads(cli("check_design_drift.py", "--root", self.root, "--format", "json"))
        self.assertFalse(any(x["rule_id"] == "MF-DRIFT-VALUE" for x in result["findings"]))
        css.write_text(":root { --brand: #334455; } .b{color:var(--brand)}", encoding="utf-8")
        result = json.loads(cli("check_design_drift.py", "--root", self.root, "--strict", "--format", "json", expected=1))
        self.assertIn("MF-DRIFT-VALUE", [x["rule_id"] for x in result["findings"]])
        self.assertEqual(master.read_text(encoding="utf-8"), "Confirmed brand must stay untouched\n")
        cli("check_design_drift.py", "--root", self.root, "--write-baseline", expected=2)

    def test_scoped_waiver_and_invalid_waiver(self):
        jsx = self.root / "ui.jsx"
        jsx.write_text("<div onClick={go}>Bad</div>\n", encoding="utf-8")
        out = json.loads(cli("mauforma_check.py", "--root", self.root, "--changed", "ui.jsx", "--strict", "--format", "json", expected=1))
        self.assertEqual(out["findings"][0]["rule_id"], "MF101")
        waivers = self.root / "waivers.json"
        waivers.write_text(json.dumps([{"rule_id": "MF101", "file": "ui.jsx",
                                       "reason": "Reviewed temporary fake UI fixture", "expires": "2099-01-01"}]), encoding="utf-8")
        out = json.loads(cli("mauforma_check.py", "--root", self.root, "--changed", "ui.jsx",
                             "--waivers", waivers, "--strict", "--format", "json"))
        self.assertEqual(out["findings"][0]["status"], "WAIVED")
        self.assertEqual(out["browser_verification"], "NOT_TESTED")
        waivers.write_text(json.dumps([{"rule_id": "MF101", "file": "../outside", "reason": "short", "expires": "2000-01-01"}]), encoding="utf-8")
        cli("mauforma_check.py", "--root", self.root, "--changed", "ui.jsx", "--waivers", waivers, expected=2)

    def test_resumable_workflow_does_not_replace_existing(self):
        preview = json.loads(cli("feature_design_flow.py", "--project-root", self.root,
                                 "--feature", "settings-page", "--action", "init", "--mode", "Operate"))
        self.assertEqual(preview["status"], "PREVIEW_ONLY")
        self.assertFalse((self.root/"design-system").exists())
        result = json.loads(cli("feature_design_flow.py", "--project-root", self.root, "--feature", "settings-page",
                                "--action", "init", "--mode", "Operate", "--apply"))
        self.assertEqual(result["status"], "CREATED")
        path = self.root/"design-system"/"features"/"settings-page"
        before = (path/"BRIEF.md").read_text(encoding="utf-8")
        result = json.loads(cli("feature_design_flow.py", "--project-root", self.root, "--feature", "settings-page", "--action", "init", "--apply"))
        self.assertEqual(result["status"], "ALREADY_EXISTS")
        self.assertEqual((path/"BRIEF.md").read_text(encoding="utf-8"), before)
        result = json.loads(cli("feature_design_flow.py", "--project-root", self.root, "--feature", "settings-page",
                                "--action", "complete", "--task", "F01", "--evidence", "Inspected inherited components and tokens"))
        self.assertEqual(result["next"], "F02")
        self.assertIn("[x] **F01**", (path/"TASKS.md").read_text(encoding="utf-8"))

    def test_variant_preview_html_is_escaped_and_choice_explicit(self):
        source = self.root/"variant.json"
        source.write_text(json.dumps({"title":"<script>attack</script>", "options":[
            {"id":"a", "name":"A", "tokens":{"accent":"#123456"}},
            {"id":"b", "name":"B", "tokens":{"accent":"#654321"}}]}), encoding="utf-8")
        output = self.root/"preview.html"
        cli("preview_design_variants.py", "--input", source, "--output", output)
        self.assertIn("&lt;script&gt;attack&lt;/script&gt;", output.read_text(encoding="utf-8"))
        self.assertFalse((self.root/"decision.json").exists())
        cli("preview_design_variants.py", "--input", source, "--output", output,
            "--choose", "b", "--decision", self.root/"decision.json")
        decision = json.loads((self.root/"decision.json").read_text(encoding="utf-8"))
        self.assertEqual(decision["selection"], "b")
        cli("preview_design_variants.py", "--input", source, "--output", output,
            "--choose", "b", "--decision", self.root/"decision.json", expected=2)

    def test_hardening_scope(self):
        out = self.root/"hardening.json"
        cli("plan_ui_hardening.py", "--out", out, "--include", "rtl")
        report = json.loads(out.read_text(encoding="utf-8"))
        self.assertEqual(report["status"], "PLAN_ONLY")
        self.assertIn("rtl", [x["id"] for x in report["tests"]])
        self.assertNotIn("mobile", [x["id"] for x in report["tests"]])
        self.assertTrue(all(x["status"]=="NOT_TESTED" for x in report["tests"]))

if __name__=="__main__":
    unittest.main()
