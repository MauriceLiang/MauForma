"""MauForma v6.10 — selected/series/table integrity & missing data."""
import copy
import json
import sys
import unittest
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from validate_comparison_contract import validate_catalog,validate_contract,validate_repository

class ComparisonTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.example=json.loads((ROOT/"examples/comparison-contract-repovantage.json").read_text("utf-8"))
        cls.catalog=json.loads((ROOT/"assets/comparison-reference-cases.json").read_text("utf-8"))
    def expect(self,data,msg):
        errs=validate_contract(data)
        self.assertTrue(any(msg in e for e in errs),errs)
    def test_repo_ready(self):
        self.assertEqual(validate_repository(),[])
    def test_baseline_contract(self):
        self.assertEqual(validate_contract(self.example),[])
        self.assertEqual(len(self.example["selected_entity_ids"]),3)
    def test_sources_credible(self):
        self.assertGreaterEqual(len(self.catalog["references"]),6)
        self.assertIn("https://www.nngroup.com/articles/comparison-tables/",[r["url"] for r in self.catalog["references"]])
    def test_missing_series_not_silently_dropped(self):
        d=copy.deepcopy(self.example);d["series"].pop()
        self.expect(d,"Selected entities must equal chart series")
    def test_duplicate_series_ids(self):
        d=copy.deepcopy(self.example);d["series"][2]["entity_id"]=d["series"][0]["entity_id"]
        self.expect(d,"Selected entities must equal chart series")
    def test_duplicate_selected_ids(self):
        d=copy.deepcopy(self.example);d["selected_entity_ids"][2]=d["selected_entity_ids"][0]
        self.expect(d,"unique")
    def test_single_selected_is_not_a_comparison(self):
        d=copy.deepcopy(self.example);d["selected_entity_ids"]=d["selected_entity_ids"][:1]
        self.expect(d,"at least 2")
    def test_partial_data_requires_explicit_null(self):
        d=copy.deepcopy(self.example);d["series"][2]["points"][0].pop("missing_reason")
        self.expect(d,"missing value requires explicit reason")
    def test_complete_status_cannot_hide_missing_point(self):
        d=copy.deepcopy(self.example);d["series"][2]["status"]="available"
        self.expect(d,"available requires complete")
    def test_no_data_cannot_have_real_points(self):
        d=copy.deepcopy(self.example);d["series"][2]["status"]="no_data"
        self.expect(d,"no_data status cannot")
    def test_time_buckets_have_shared_window(self):
        d=copy.deepcopy(self.example);d["series"][0]["points"][0]["bucket"]="2027-01-05"
        self.expect(d,"point outside shared timeline")
    def test_time_buckets_must_be_sorted(self):
        d=copy.deepcopy(self.example);d["window"]["time_buckets"].reverse()
        self.expect(d,"ascending")
    def test_duplicate_point_bucket(self):
        d=copy.deepcopy(self.example);d["series"][0]["points"][1]["bucket"]=d["series"][0]["points"][0]["bucket"]
        self.expect(d,"duplicate/malformed")
    def test_table_column_identity(self):
        d=copy.deepcopy(self.example);d["table"]["columns"].reverse()
        self.expect(d,"preserve selected entity")
    def test_table_row_has_every_entity(self):
        d=copy.deepcopy(self.example);d["table"]["metrics"][0]["cells"].pop()
        self.expect(d,"exactly one cell")
    def test_missing_metric_cannot_be_numeric_zero(self):
        d=copy.deepcopy(self.example);d["table"]["metrics"][1]["cells"][0]["value"]=0
        self.expect(d,"cannot be numeric zero")
    def test_numeric_metric_needs_sample(self):
        d=copy.deepcopy(self.example);d["table"]["metrics"][0]["cells"][0]["sample_size"]=0
        self.expect(d,"nonzero sampled evidence")
    def test_null_coverage_cannot_claim_complete(self):
        d=copy.deepcopy(self.example);d["table"]["metrics"][1]["cells"][0]["coverage"]="complete"
        self.expect(d,"null must not pretend")
    def test_no_fabricated_data_overrides(self):
        d=copy.deepcopy(self.example);d["presentation"]["show_critical_coverage_notice"]=False
        self.expect(d,"visible coverage")
    def test_consistent_selected_count(self):
        d=copy.deepcopy(self.example);d["presentation"]["selected_count"]=2
        self.expect(d,"selected count")
    def test_distinct_series_color_tokens(self):
        d=copy.deepcopy(self.example);d["series"][1]["color_token"]="series-1"
        self.expect(d,"stable distinct color")
    def test_user_approval_evidence(self):
        d=copy.deepcopy(self.example);d["status"]="confirmed"
        self.expect(d,"actual statement")
    def test_browser_pass_must_verify_plots(self):
        d=copy.deepcopy(self.example);d["review"]["browser_status"]="PASS"
        d["review"]["viewports"]=["1440x900","390x844"];d["review"]["evidence"]=["one.png"]
        self.expect(d,"plot-label and series-selector")
    def test_gallery_and_browser_script_have_chart_hooks(self):
        html=(ROOT/"assets/comparison-layout-lab.html").read_text("utf-8")
        script=(ROOT/"scripts/audit_comparison_ui.mjs").read_text("utf-8")
        for token in ("data-mf-chart-plot","data-mf-chart-label","data-mf-series-id","data-mf-selected-id","data-mf-legend-id"):
            self.assertIn(token,html)
            self.assertIn(token,script)

if __name__=="__main__":unittest.main()
