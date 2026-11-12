"""MauForma v6.9 regression: shared row lines and scroll-end reachability."""
import copy
import json
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from validate_layout_integrity import validate_catalog,validate_plan,validate_repository

class LayoutIntegrityTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.catalog=json.loads((ROOT/"assets/layout-integrity-patterns.json").read_text("utf-8"))
        cls.sample=json.loads((ROOT/"examples/layout-integrity-demo.json").read_text("utf-8"))

    def expect(self,plan,fragment):
        errors=validate_plan(plan,self.catalog)
        self.assertTrue(any(fragment in err for err in errors),errors)

    def test_catalog_and_repo(self):
        self.assertEqual(validate_repository(),[])

    def test_example_is_not_fake_browser_pass(self):
        self.assertEqual(self.sample["intent"],"provisional")
        self.assertEqual(self.sample["review"]["browser_status"],"NOT RUN")
        self.assertEqual(validate_plan(self.sample,self.catalog),[])

    def test_shared_rows_are_declared(self):
        g=self.sample["layout"]["align_groups"]
        self.assertEqual({x["id"] for x in g},{"first-row","second-row"})

    def test_top_alignment_rejects_mismatched_rows(self):
        d=copy.deepcopy(self.sample)
        d["layout"]["regions"][3]["row"]=3
        self.expect(d,"Top-aligned peer regions")

    def test_missing_second_row_group_is_blocked(self):
        d=copy.deepcopy(self.sample)
        d["layout"]["align_groups"].pop()
        self.expect(d,"Shared grid row")

    def test_duplicate_grid_cell_rejected(self):
        d=copy.deepcopy(self.sample)
        d["layout"]["regions"][3]["col"]=1
        self.expect(d,"same grid cell")

    def test_duplicate_region_rejected(self):
        d=copy.deepcopy(self.sample)
        d["layout"]["regions"][3]["id"]="timeline"
        self.expect(d,"IDs missing or duplicated")

    def test_mobile_order_does_not_lose_content(self):
        d=copy.deepcopy(self.sample)
        d["layout"]["mobile_order"].remove("release-list")
        self.expect(d,"each content region exactly once")

    def test_bottom_safe_area_required(self):
        d=copy.deepcopy(self.sample)
        d["scroll"]["bottom_safe_area"]=False
        self.expect(d,"bottom safe-area")

    def test_scroll_to_end_required(self):
        d=copy.deepcopy(self.sample)
        d["scroll"]["scroll_to_end_required"]=False
        self.expect(d,"final scroll position")

    def test_last_content_must_exist(self):
        d=copy.deepcopy(self.sample)
        d["scroll"]["last_content_id"]="missing"
        self.expect(d,"Last meaningful content")

    def test_fixed_bar_needs_space(self):
        d=copy.deepcopy(self.sample)
        d["scroll"]["has_fixed_bar"]=True
        d["scroll"]["end_padding_strategy"]="a bit of padding"
        self.expect(d,"Fixed bar requires")

    def test_browser_pass_requires_evidence(self):
        d=copy.deepcopy(self.sample)
        d["review"]["browser_status"]="PASS"
        self.expect(d,"multiple viewports")

    def test_browser_pass_requires_real_scroll_end(self):
        d=copy.deepcopy(self.sample)
        d["review"].update({"browser_status":"PASS","viewports":["1440x900","390x844"],"evidence":["screenshots/1.png"],"scrolled_to_end":False})
        self.expect(d,"actual end-of-scroll")

    def test_confirmed_layout_requires_statement(self):
        d=copy.deepcopy(self.sample)
        d["intent"]="confirmed"
        self.expect(d,"real user statement")

    def test_editorial_masonry_needs_data_page_justification(self):
        d=copy.deepcopy(self.sample)
        d["layout"]["pattern_id"]="masonry"
        d["layout"]["intentional_asymmetry_reason"]="looks cool"
        self.expect(d,"meaningful rationale")

    def test_asymmetry_is_not_universally_banned(self):
        d=copy.deepcopy(self.sample)
        d["layout"]["pattern_id"]="editorial-asymmetry"
        d["layout"]["mode"]="persuade"
        self.assertEqual(validate_plan(d,self.catalog),[])

    def test_lab_has_end_scroller_and_grid_variants(self):
        s=(ROOT/"assets/grid-and-viewport-lab.html").read_text("utf-8")
        for token in ('data-variant="masonry"','data-variant="shared-grid"','data-variant="hero-span"','id="scroll-shell"','id="last-release"'):
            self.assertIn(token,s)

    def test_browser_script_contains_actual_end_screenshot(self):
        s=(ROOT/"scripts/audit_rendered_layout.mjs").read_text("utf-8")
        for token in ("scrollHeight","scrollTop","-end.png","data-mf-grid-row","data-mf-fixed-bar"):
            self.assertIn(token,s)

if __name__=="__main__":
    unittest.main()
