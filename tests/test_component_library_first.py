"""Regression tests: agents must choose and actually use suitable UI components."""
import copy
import importlib.util
import json
from pathlib import Path
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location(
    "validate_component_library_first", ROOT / "scripts/validate_component_library_first.py"
)
module = importlib.util.module_from_spec(SPEC)
assert SPEC.loader is not None
SPEC.loader.exec_module(module)


class ComponentLibraryFirstTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example = json.loads(
            (ROOT / "examples/component-library-decision.demo.json").read_text("utf-8")
        )

    def check_issue(self, plan, keyword):
        issues = module.validate(plan)
        self.assertTrue(any(keyword in item for item in issues), issues)

    def test_synthetic_positive_plan(self):
        self.assertEqual(module.validate(self.example), [])

    def test_repository_entrypoint_routes_to_gate(self):
        self.assertEqual(module.validate_repository(), [])

    def test_new_interactive_app_cannot_skip_library(self):
        bad = copy.deepcopy(self.example)
        bad["ui_library"]["decision"] = "no_interaction"
        self.check_issue(bad, "cannot skip")

    def test_new_app_must_choose_real_library(self):
        bad = copy.deepcopy(self.example)
        bad["ui_library"]["primary"] = "none"
        self.check_issue(bad, "real primary library")

    def test_component_choice_must_fit_framework(self):
        bad = copy.deepcopy(self.example)
        bad["ui_library"]["framework_compatible"] = False
        self.check_issue(bad, "framework compatible")

    def test_disallow_handwritten_pseudo_select(self):
        bad = copy.deepcopy(self.example)
        bad["controls"][0]["source"] = "handwritten"
        bad["controls"][0]["component"] = "div + click + absolute"
        self.check_issue(bad, "not hand-written pseudo-controls")

    def test_select_has_open_and_selected_and_focus_states(self):
        bad = copy.deepcopy(self.example)
        bad["controls"][0]["states_to_test"] = ["default", "disabled"]
        self.check_issue(bad, "missing first-pass states")

    def test_source_requires_actual_component(self):
        bad = copy.deepcopy(self.example)
        bad["controls"][0]["component"] = ""
        self.check_issue(bad, "actual component")

    def test_native_exception_needs_reason(self):
        bad = copy.deepcopy(self.example)
        bad["controls"][0]["source"] = "native"
        bad["controls"][0]["component"] = "select"
        self.check_issue(bad, "exception requires")

    def test_integrated_must_show_real_imports(self):
        bad = copy.deepcopy(self.example)
        bad["first_pass"]["phase"] = "integrated"
        self.check_issue(bad, "actual import/usage evidence")

    def test_integrated_must_apply_theme(self):
        bad = copy.deepcopy(self.example)
        bad["first_pass"]["phase"] = "integrated"
        bad["first_pass"]["integration_imports"] = ["ElSelect from element-plus"]
        self.check_issue(bad, "theme application")

    def test_false_verified_claim_rejected(self):
        bad = copy.deepcopy(self.example)
        bad["first_pass"]["phase"] = "verified"
        bad["first_pass"]["integration_imports"] = ["ElSelect from element-plus"]
        bad["first_pass"]["theme_applied"] = True
        self.check_issue(bad, "real-page browser verification")

    def test_static_site_has_valid_no_library_path(self):
        plan = copy.deepcopy(self.example)
        plan["project_type"] = "static-reading-page"
        plan["interactive_controls_needed"] = False
        plan["ui_library"] = {
            "decision": "no_interaction", "primary": None,
            "reason": "Only static prose and navigation links are present."
        }
        plan["controls"] = []
        self.assertEqual(module.validate(plan), [])

    def test_duplicate_controls_rejected(self):
        bad = copy.deepcopy(self.example)
        bad["controls"].append(copy.deepcopy(bad["controls"][0]))
        self.check_issue(bad, "Duplicate control mapping")


if __name__ == "__main__":
    unittest.main()
