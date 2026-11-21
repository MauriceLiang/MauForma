"""Runtime-language migration checks: language + fixed source anchors, not semantic proof."""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("validate_runtime_i18n", ROOT / "scripts/validate_runtime_i18n.py")
module = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(module)


class RuntimeEnglishContractTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.manifest = json.loads((ROOT / "assets/i18n-phase2-translation-contract.json").read_text("utf-8"))

    def test_translated_subset_has_clean_english_runtime_prose(self):
        self.assertEqual(module.inspect(self.manifest), [])

    def test_second_pass_review_has_explicit_bounded_evidence(self):
        self.assertEqual(self.manifest["status"], "reviewed_and_approved")
        self.assertEqual(self.manifest["review_record"], "assets/i18n-phase2-semantic-review.md")
        self.assertTrue((ROOT / self.manifest["review_record"]).is_file())
        self.assertEqual(len(self.manifest["entries"]), 83)
        self.assertTrue(all(x["translated_status"] == "reviewed_second_pass"
                            for x in self.manifest["entries"]))

    def test_missing_critical_boundary_is_rejected(self):
        changed = copy.deepcopy(self.manifest)
        changed["entries"][0]["required_english_fragments"] += ["UNTRANSLATED CRITICAL BOUNDARY"]
        self.assertTrue(any("missing English boundary anchor" in x for x in module.inspect(changed)))

    def test_unapproved_chinese_rule_text_cannot_be_added(self):
        entry = self.manifest["entries"][0]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "SKILL.md").write_text("# English entrypoint", "utf-8")
            path = root / entry["path"]
            path.parent.mkdir(parents=True)
            original = (ROOT / entry["path"]).read_text("utf-8")
            path.write_text(original + "\n\n必须删除全部原生控件。", "utf-8")
            minimal = {"schema_version":"1.0","status":"partial_migration","entries":[entry]}
            self.assertTrue(any("explanatory Han script remains" in x
                                for x in module.inspect(minimal, root=root)))

    def test_migration_cannot_claim_independent_verification_from_static_ci(self):
        changed = copy.deepcopy(self.manifest)
        changed["status"] = "fully_verified"
        self.assertTrue(any("cannot assert independent semantic parity" in x
                            for x in module.inspect(changed)))


if __name__ == "__main__":
    unittest.main()
