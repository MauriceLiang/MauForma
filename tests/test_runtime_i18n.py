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

    def test_readmes_reflect_reviewed_migration_and_retain_chinese_semantic_qa(self):
        inventory = json.loads(
            (ROOT / "assets/i18n-phase2-migration-inventory.json").read_text("utf-8")
        )
        statuses = [entry["status"] for entry in inventory["files"]]
        self.assertEqual(inventory["migration_status"], "complete_reviewed")
        self.assertEqual(statuses.count("reviewed_second_pass"), 83)
        self.assertEqual(statuses.count("existing_english_pending_language_audit"), 4)
        self.assertEqual(statuses.count("bilingual_qa_exception"), 1)

        for name in ("README.md", "README.zh-CN.md"):
            readme = (ROOT / name).read_text("utf-8")
            for anchor in ("83", "4", "references/semantic-boundaries.zh-CN.md",
                           "assets/i18n-phase2-translation-contract.json"):
                self.assertIn(anchor, readme, f"{name}: missing {anchor}")

        english_readme = (ROOT / "README.md").read_text("utf-8")
        chinese_readme = (ROOT / "README.zh-CN.md").read_text("utf-8")
        self.assertNotIn("references are primarily Chinese today", english_readme)
        self.assertNotIn("其中部分仍为中文", chinese_readme)

        chinese_boundaries = (ROOT / "references/semantic-boundaries.zh-CN.md").read_text("utf-8")
        self.assertIn("B01", chinese_boundaries)
        self.assertIn("B15", chinese_boundaries)
        self.assertTrue(all(entry.get("semantic_pair_examples")
                            for entry in self.manifest["entries"]))

    def test_chinese_origin_semantic_regression_matrix_is_traceable(self):
        matrix_path = ROOT / "assets/i18n-semantic-regression-matrix.zh-CN.md"
        matrix = matrix_path.read_text("utf-8")
        boundaries = json.loads(
            (ROOT / "assets/semantic-boundary-contract.json").read_text("utf-8")
        )["rules"]
        inventory = json.loads(
            (ROOT / "assets/i18n-phase2-migration-inventory.json").read_text("utf-8")
        )["files"]
        converted = [item for item in inventory
                     if item["status"] == "reviewed_second_pass"]

        self.assertEqual(len(converted), 83)
        self.assertEqual(len(boundaries), 15)
        self.assertEqual(matrix.count(" | [中文源]("), 83)
        self.assertEqual(matrix.count("### B"), 15)
        baseline = self.manifest["source_commit"]
        self.assertIn(baseline, matrix)

        for item in converted:
            self.assertIn(f"/blob/{baseline}/{item['path']}", matrix)
            self.assertIn(item["source_blob_sha"], matrix)
            self.assertIn(f"/blob/main/{item['path']}", matrix)

        for rule in boundaries:
            self.assertIn(f"### {rule['id']} — {rule['topic']}", matrix)
            for field in ("trigger", "require", "exception", "never"):
                for locale in ("en", "zh"):
                    expected = rule[f"{field}_{locale}"].replace("|", "\\|")
                    self.assertIn(expected, matrix,
                                  f"{rule['id']} {field}_{locale} missing")

        for readme in ("README.md", "README.zh-CN.md"):
            self.assertIn(
                "assets/i18n-semantic-regression-matrix.zh-CN.md",
                (ROOT / readme).read_text("utf-8")
            )
        self.assertIn("not a", matrix.lower())
        self.assertIn("STATIC CHECK", matrix)

    def test_semantic_regression_preserves_high_risk_original_conditions(self):
        contract = json.loads(
            (ROOT / "assets/semantic-boundary-contract.json").read_text("utf-8")
        )
        rules = {rule["id"]: rule for rule in contract["rules"]}
        self.assertIn("review request", rules["B01"]["trigger_en"])
        self.assertIn("When authorized", rules["B05"]["exception_en"])
        self.assertIn("authorized source assets", rules["B08"]["require_en"])
        self.assertIn("confirming design direction", rules["B11"]["require_en"])
        self.assertIn("With explicit approval", rules["B12"]["exception_en"])

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
