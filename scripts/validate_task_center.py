#!/usr/bin/env python3
"""MauForma v6.11: task-run data, action, and summary semantics.

Static contract validation only. Real UI actions, server status, permissions,
and browser scroll reachability require actual E2E/integration testing.
"""
from __future__ import annotations
import argparse
import json
from datetime import datetime
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CATALOG=ROOT/"assets/task-center-reference-cases.json"
EXAMPLE=ROOT/"examples/task-center-repovantage.json"
REQUIRED=(
"references/task-center-run-monitor-design.md",
"references/repovantage-task-center-case.md",
"assets/task-center-reference-cases.json",
"assets/task-center-run.schema.json",
"assets/task-center-layout-lab.html",
"examples/task-center-repovantage.json",
"scripts/validate_task_center.py",
"tests/test_task_center.py",
"tests/task_center_browser_smoke.mjs",
)
STATES={"running","queued","waiting","partial","failed","blocked","succeeded","canceled"}
ATTENTION={"partial","failed","blocked"}
ACTIVE={"running"}
QUEUED={"queued","waiting"}
COMPLETE={"succeeded"}
ACTIONS={"details","retry","cancel","resolve"}
VALID_FILTERS={"all","attention","running","queued","completed"}


def summary_counts(tasks):
    """Derived counts: attention excludes running/queued and includes partial/failed/blocked."""
    return {
      "all":len(tasks),
      "attention":sum(t["state"] in ATTENTION for t in tasks),
      "running":sum(t["state"] in ACTIVE for t in tasks),
      "queued":sum(t["state"] in QUEUED for t in tasks),
      "completed":sum(t["state"] in COMPLETE for t in tasks),
    }


def validate_catalog(data=None):
    issues=[]
    if data is None:
        try:data=json.loads(CATALOG.read_text("utf-8"))
        except (ValueError,OSError) as exc:return ["Reference catalog unreadable: "+str(exc)]
    refs=data.get("sources",[])
    if len(refs)<5:issues.append("Task run monitor needs mature reference cases")
    names=[x.get("id") for x in refs if isinstance(x,dict)]
    if len(names)!=len(refs) or len(names)!=len(set(names)):
        issues.append("Duplicate or missing reference IDs")
    for item in refs:
        if not isinstance(item,dict) or not str(item.get("url","")).startswith("https://") or not item.get("use") or not item.get("avoid"):
            issues.append("Task reference needs URL, lessons and limitations")
    patterns=data.get("patterns",[])
    if not any(p.get("id")=="run-list" for p in patterns if isinstance(p,dict)):
        issues.append("Missing run-monitor list pattern")
    for key in ("no_permanent_stat_column_without_distinct_task","no_repeated_progress_unavailable_sentence",
                "counts_derived_from_visible_data","unknown_progress_is_not_zero",
                "retry_requires_explicit_capability","log_details_progressively_disclosed",
                "real_api_not_inferred_from_mock","focusable_controls"):
        if data.get("guards",{}).get(key) is not True:issues.append("Missing run-monitor guard: "+key)
    return issues


def validate_task_model(doc):
    issues=[]
    if not isinstance(doc,dict) or doc.get("schema_version")!="1.0":
        return ["Unsupported run monitor schema version"]
    view=doc.get("view",{})
    if not isinstance(view,dict):return ["View missing"]
    if view.get("page_type") not in {"run_monitor","human_tasks","mixed"}:
        issues.append("View role missing")
    if view.get("decision_source") in ("confirmed","delegated") and not view.get("user_statement"):
        issues.append("Cannot claim confirmed/delegated style without user evidence")
    filters=view.get("status_filters",[])
    if not isinstance(filters,list) or "all" not in filters or len(filters)!=len(set(filters)) or set(filters)-VALID_FILTERS:
        issues.append("Filter set must include all and valid nonduplicated states")
    if view.get("display_counts_scope") not in {"all_loaded_records","filtered_records","server_total"}:
        issues.append("Status counters need explicit data scope")
    if view.get("default_sort") not in {"attention_then_recent","recent_first","oldest_first"}:
        issues.append("Sort order needs explicit rule")
    if view.get("refresh_mode") not in {"manual","poll","sse","websocket"}:
        issues.append("Refresh mode must be implemented, not guessed")
    sync=view.get("last_synced_at")
    if sync is not None:
        try:
            dt=datetime.fromisoformat(sync)
            if dt.utcoffset() is None:raise ValueError("naive")
        except (ValueError,TypeError):issues.append("Last sync timestamp must include time-zone offset")
    tasks=doc.get("tasks",[])
    if not isinstance(tasks,list):return issues+["Task records must be array"]
    ids=[]
    for t in tasks:
        if not isinstance(t,dict):
            issues.append("Malformed task record");continue
        task_id=t.get("id")
        ids.append(task_id)
        state=t.get("state")
        if not isinstance(task_id,str) or not task_id:
            issues.append("Missing task id")
        if state not in STATES:
            issues.append(f"{task_id}: unknown task lifecycle state")
        for key in ("object","type","phase","details_route"):
            if not isinstance(t.get(key),str) or not t[key].strip():
                issues.append(f"{task_id}: missing {key}")
        stamp=t.get("updated_at")
        try:
            dt=datetime.fromisoformat(stamp)
            if dt.utcoffset() is None:raise ValueError("naive")
        except (TypeError,ValueError):issues.append(f"{task_id}: timestamp must have timezone")
        steps=t.get("steps")
        if not isinstance(steps,list) or not steps or any(not isinstance(x,str) or not x.strip() for x in steps):
            issues.append(f"{task_id}: provide real stage/step context for details")
        progress=t.get("progress")
        if progress is not None:
            if not isinstance(progress,dict):
                issues.append(f"{task_id}: progress must be object or null")
            else:
                completed=progress.get("completed");total=progress.get("total")
                if (not isinstance(completed,int) or isinstance(completed,bool) or
                    not isinstance(total,int) or isinstance(total,bool) or total<=0 or not 0<=completed<=total):
                    issues.append(f"{task_id}: invalid progress numerator/denominator")
                if not isinstance(progress.get("unit"),str) or not progress["unit"]:
                    issues.append(f"{task_id}: progress unit required")
                if not isinstance(progress.get("total_is_stable"),bool):
                    issues.append(f"{task_id}: denominator stability must be explicit")
                if state=="succeeded" and isinstance(completed,int) and isinstance(total,int) and completed!=total:
                    issues.append(f"{task_id}: succeeded task with incomplete known progress")
        err=t.get("error")
        if state in ATTENTION and (not isinstance(err,str) or not err.strip()):
            issues.append(f"{task_id}: attention requires actionable reason")
        if state in {"queued","waiting","succeeded"} and err not in (None,""):
            issues.append(f"{task_id}: unexpected error on non-error lifecycle state")
        retryable=t.get("retryable")
        actions=t.get("allowed_actions")
        if not isinstance(retryable,bool):issues.append(f"{task_id}: retryable must be explicit boolean")
        if not isinstance(actions,list) or len(actions)!=len(set(actions)) or set(actions)-ACTIONS or "details" not in actions:
            issues.append(f"{task_id}: action set must be valid, nonduplicated and include details")
            actions=[]
        if "retry" in actions and (not retryable or state not in {"partial","failed"}):
            issues.append(f"{task_id}: unauthorized retry action for lifecycle state")
        if retryable and state not in {"partial","failed"}:
            issues.append(f"{task_id}: retryable flag conflicts with lifecycle state")
        if retryable and "retry" not in actions:
            issues.append(f"{task_id}: retryable task must expose retry affordance")
        if "cancel" in actions and state not in {"running","queued","waiting"}:
            issues.append(f"{task_id}: cancel affordance on non-active/non-queued state")
    if len(set(ids))!=len(ids):
        issues.append("Duplicate task IDs")
    review=doc.get("review",{})
    if not isinstance(review,dict) or review.get("browser_status") not in {"NOT RUN","PASS","FAIL"}:
        issues.append("Browser review status missing")
    elif review["browser_status"]=="PASS":
        if len(review.get("viewports",[]))<2 or not review.get("evidence"):
            issues.append("Browser PASS requires real multi-viewport evidence")
        if review.get("filters_verified") is not True or review.get("actions_verified") is not True or review.get("scrolled_to_end") is not True:
            issues.append("Browser PASS requires filters, actions, and end scroll verified")
    return issues


def validate_repository():
    issues=[f"Missing task center resource: {p}" for p in REQUIRED if not (ROOT/p).is_file()]
    issues.extend(validate_catalog())
    try:issues.extend(validate_task_model(json.loads(EXAMPLE.read_text("utf-8"))))
    except (ValueError,OSError,KeyError,TypeError) as exc:issues.append("Task center example invalid: "+str(exc))
    try:skill=(ROOT/"SKILL.md").read_text("utf-8")
    except OSError:skill=""
    for name in ("task-center-run-monitor-design.md","validate_task_center.py","task-center-layout-lab.html"):
        if name not in skill:issues.append("SKILL.md needs run-monitor routing: "+name)
    return issues


def main():
    parser=argparse.ArgumentParser(description="Task center model QA; not server/browser verification")
    parser.add_argument("file",nargs="?",type=Path)
    parser.add_argument("--repository",action="store_true")
    parser.add_argument("--json",action="store_true")
    args=parser.parse_args()
    issues=validate_repository() if args.repository else validate_catalog() if args.file is None else []
    if args.file:
        try:issues.extend(validate_task_model(json.loads(args.file.read_text("utf-8"))))
        except (OSError,ValueError) as exc:issues.append(str(exc))
    if args.json:print(json.dumps({"passed":not issues,"issues":issues,"scope":"static data/interaction plan, not live server or aesthetic QA"},ensure_ascii=False,indent=2))
    else:
        for issue in issues:print("ERROR:",issue)
        print("Task Center Run Contract:","PASS" if not issues else "FAIL")
    return int(bool(issues))


if __name__=="__main__":raise SystemExit(main())
