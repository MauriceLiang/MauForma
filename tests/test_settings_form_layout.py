"""Mutation tests for independent settings, grouped forms and hybrid layouts."""
from __future__ import annotations

import copy
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from validate_settings_form_layout import validate, validate_repo


class SettingsFormTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cases = json.loads((ROOT / "assets/settings-form-layout-cases.json").read_text("utf-8"))

    def changed(self, cid, key, value):
        data = copy.deepcopy(self.cases)
        next(c for c in data["cases"] if c["id"] == cid)[key] = value
        return validate(data)

    def test_repo_contract(self):
        self.assertEqual(validate_repo(), [])

    def test_valid_synthetic_examples(self):
        self.assertEqual(validate(self.cases), [])

    def test_settings_do_not_become_cramped_forms(self):
        self.assertTrue(any("row layout" in e for e in self.changed("small-settings", "layout", "stacked_field")))

    def test_form_needs_stacked_fields(self):
        self.assertTrue(any("stacked layout" in e for e in self.changed("account-creation", "layout", "horizontal_row")))

    def test_errors_near_fields(self):
        self.assertTrue(any("errors belong below" in e for e in self.changed("order-address", "validation", "none")))

    def test_hybrid_is_segmented(self):
        self.assertTrue(any("hybrid needs" in e for e in self.changed("notification-plus-smtp", "layout", "horizontal_row")))

    def test_danger_isolated(self):
        self.assertTrue(any("dangerous action" in e for e in self.changed("danger-zone", "danger", "inside_preferences")))

    def test_keep_semantic_group_spacing(self):
        self.assertTrue(any("group spacing" in e for e in self.changed("small-settings", "section_rhythm", "equal")))

    def test_no_forced_nested_cards(self):
        self.assertTrue(any("surface" in e for e in self.changed("small-settings", "surface", "nested_cards")))

    def test_mobile_reflows(self):
        self.assertTrue(any("mobile" in e for e in self.changed("small-settings", "mobile", "squeeze_controls")))

    def test_labels_visible(self):
        self.assertTrue(any("visible label" in e for e in self.changed("account-creation", "visible_labels", False)))

    def test_long_setting_requires_justification(self):
        self.assertTrue(any("justified" in e for e in self.changed("long-language-control", "exception_reason", "")))


if __name__ == "__main__":
    unittest.main()
