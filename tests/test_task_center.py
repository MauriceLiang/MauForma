"""Task Center run-monitor status, progress and permission regressions."""
import copy
import json
import sys
import unittest
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT/"scripts"))
from validate_task_center import summary_counts,validate_task_model,validate_catalog,validate_repository

class TaskCenterTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.sample=json.loads((ROOT/"examples/task-center-repovantage.json").read_text("utf-8"))
        cls.catalog=json.loads((ROOT/"assets/task-center-reference-cases.json").read_text("utf-8"))

    def rejects(self,doc,substring):
        errors=validate_task_model(doc)
        self.assertTrue(any(substring in e for e in errors),errors)

    def test_example_and_catalog_integrity(self):
        self.assertEqual(validate_repository(),[])
        self.assertEqual(validate_catalog(self.catalog),[])
        self.assertEqual(validate_task_model(self.sample),[])

    def test_counts_derived_from_same_records(self):
        c=summary_counts(self.sample["tasks"])
        self.assertEqual(c,{"all":7,"attention":3,"running":2,"queued":1,"completed":1})
        self.assertEqual(c["all"],sum(c[k] for k in c if k!="all"))

    def test_no_fake_browser_verification(self):
        self.assertEqual(self.sample["review"]["browser_status"],"NOT RUN")
        self.assertEqual(self.sample["view"]["decision_source"],"provisional")

    def test_duplicate_task_id_rejected(self):
        d=copy.deepcopy(self.sample);d["tasks"][1]["id"]=d["tasks"][0]["id"]
        self.rejects(d,"Duplicate task IDs")

    def test_bad_time_zone_rejected(self):
        d=copy.deepcopy(self.sample);d["tasks"][0]["updated_at"]="2026-11-04T07:00:00"
        self.rejects(d,"timestamp must have timezone")

    def test_no_denominator_zero(self):
        d=copy.deepcopy(self.sample);d["tasks"][0]["progress"]["total"]=0
        self.rejects(d,"invalid progress numerator/denominator")

    def test_progress_beyond_total_rejected(self):
        d=copy.deepcopy(self.sample);d["tasks"][0]["progress"]["completed"]=7000
        self.rejects(d,"invalid progress numerator/denominator")

    def test_progress_unit_required(self):
        d=copy.deepcopy(self.sample);d["tasks"][0]["progress"]["unit"]=""
        self.rejects(d,"progress unit required")

    def test_denominator_stability_required(self):
        d=copy.deepcopy(self.sample);d["tasks"][0]["progress"].pop("total_is_stable")
        self.rejects(d,"denominator stability")

    def test_success_not_incomplete(self):
        d=copy.deepcopy(self.sample);d["tasks"][4]["progress"]["completed"]=1
        self.rejects(d,"succeeded task with incomplete")

    def test_unknown_progress_stays_null(self):
        self.assertIsNone(self.sample["tasks"][1]["progress"])
        self.assertIsNone(self.sample["tasks"][5]["progress"])

    def test_attention_cannot_hide_error_reason(self):
        d=copy.deepcopy(self.sample);d["tasks"][2]["error"]=None
        self.rejects(d,"attention requires actionable reason")

    def test_queue_cannot_offer_retry(self):
        d=copy.deepcopy(self.sample);d["tasks"][1]["allowed_actions"].append("retry")
        self.rejects(d,"unauthorized retry")

    def test_done_cannot_offer_retry(self):
        d=copy.deepcopy(self.sample);d["tasks"][4]["allowed_actions"].append("retry")
        self.rejects(d,"unauthorized retry")

    def test_blocked_nonretryable(self):
        d=copy.deepcopy(self.sample);d["tasks"][6]["retryable"]=True
        self.rejects(d,"retryable flag conflicts")

    def test_retry_requires_real_affordance(self):
        d=copy.deepcopy(self.sample);d["tasks"][3]["allowed_actions"]=["details"]
        self.rejects(d,"must expose retry affordance")

    def test_cancel_only_for_active_tasks(self):
        d=copy.deepcopy(self.sample);d["tasks"][4]["allowed_actions"].append("cancel")
        self.rejects(d,"cancel affordance")

    def test_details_available(self):
        d=copy.deepcopy(self.sample);d["tasks"][1]["allowed_actions"]=[]
        self.rejects(d,"include details")

    def test_valid_status_filters_include_all(self):
        d=copy.deepcopy(self.sample);d["view"]["status_filters"].remove("all")
        self.rejects(d,"Filter set must include all")

    def test_server_data_scope_explicit(self):
        d=copy.deepcopy(self.sample);d["view"]["display_counts_scope"]="some totals"
        self.rejects(d,"explicit data scope")

    def test_claiming_user_approval_requires_evidence(self):
        d=copy.deepcopy(self.sample);d["view"]["decision_source"]="confirmed"
        self.rejects(d,"user evidence")

    def test_pass_requires_browser_evidence(self):
        d=copy.deepcopy(self.sample);d["review"]["browser_status"]="PASS"
        self.rejects(d,"real multi-viewport evidence")

    def test_pass_requires_interactive_checks(self):
        d=copy.deepcopy(self.sample)
        d["review"].update({"browser_status":"PASS","viewports":["1440x900","390x844"],"evidence":["images/one.png"]})
        self.rejects(d,"filters, actions")

    def test_catalog_covers_workflow_tools(self):
        names={r["id"] for r in self.catalog["sources"]}
        self.assertTrue({"github-actions","gitlab-pipelines","trigger-runs","inngest","linear"}.issubset(names))

    def test_html_and_browser_script_hooks_exist(self):
        h=(ROOT/"assets/task-center-layout-lab.html").read_text("utf-8")
        b=(ROOT/"tests/task_center_browser_smoke.mjs").read_text("utf-8")
        for key in ("data-mf-task-id","data-mf-task-state","data-mf-task-action","id=\"status-filter\"","id=\"task-detail\""):
            self.assertIn(key,h)
        for key in ("data-mf-task-id","data-mf-task-state","data-mf-task-action","scrollHeight"):
            self.assertIn(key,b)

if __name__=="__main__":unittest.main()
