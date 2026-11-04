#!/usr/bin/env python3
"""MauForma v6.10 comparison data/model quality gate.

Detects selected-vs-series-vs-table mismatch, time and unit incompatibility,
missing-as-zero mistakes and unsupported claims. NOT a visual/Canvas validator.
"""
from __future__ import annotations
import argparse
import json
from datetime import date
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
CATALOG=ROOT/"assets/comparison-reference-cases.json"
EXAMPLE=ROOT/"examples/comparison-contract-repovantage.json"
REQUIRED=(
 "references/comparison-page-design.md",
 "references/chart-interior-alignment.md",
 "references/repovantage-comparison-case.md",
 "assets/comparison-reference-cases.json",
 "assets/comparison-contract.schema.json",
 "assets/comparison-layout-lab.html",
 "examples/comparison-contract-repovantage.json",
 "scripts/validate_comparison_contract.py",
 "scripts/audit_comparison_ui.mjs",
 "tests/test_comparison_contract.py",
)
VALID_COVERAGE={"complete","partial","not-collected","not-applicable","insufficient"}
VALID_STATUS={"available","partial","no_data"}


def validate_catalog(data=None):
    errors=[]
    if data is None:
        try:data=json.loads(CATALOG.read_text("utf-8"))
        except (OSError,ValueError) as e:return [f"Catalog unreadable: {e}"]
    patterns=data.get("patterns",[])
    refs=data.get("references",[])
    ids=[x.get("id") for x in refs if isinstance(x,dict)]
    pids=[x.get("id") for x in patterns if isinstance(x,dict)]
    if len(refs)<5 or len(ids)!=len(refs) or len(set(ids))!=len(ids):errors.append("Need distinct comparison references")
    if len(patterns)<3 or len(pids)!=len(patterns) or len(set(pids))!=len(pids):errors.append("Need distinct comparison patterns")
    for ref in refs:
        if not isinstance(ref,dict):errors.append("Malformed reference");continue
        if not str(ref.get("url","")).startswith("https://") or not ref.get("learn") or not ref.get("limits"):
            errors.append(f"Reference {ref.get('id')} lacks valid URL, lessons or limitations")
    for pattern in patterns:
        if not isinstance(pattern,dict):errors.append("Malformed pattern");continue
        if not pattern.get("fit") or not pattern.get("primary") or not pattern.get("avoid"):
            errors.append(f"Pattern {pattern.get('id')} lacks purpose or counterexample")
    for flag in ("selected_series_legend_consistency","same_period_and_metric_unit","no_null_as_zero",
                 "source_and_sample_coverage","avoid_fabricated_winner","mobile_readability",
                 "chart_plot_alignment_and_label_overlap_review"):
        if data.get("guardrails",{}).get(flag) is not True:errors.append("Missing guardrail: "+flag)
    return errors


def validate_contract(data):
    errors=[]
    if not isinstance(data,dict) or data.get("schema_version")!="1.0":
        return ["Invalid comparison contract schema version"]
    if not str(data.get("decision_question","")).strip():errors.append("Comparison must have a user decision question")
    if data.get("status") in ("confirmed","delegated") and not str(data.get("user_statement") or "").strip():
        errors.append("User confirmed/delegated needs an actual statement")
    entities=data.get("selected_entity_ids",[])
    if not isinstance(entities,list) or not entities or not all(isinstance(x,str) and x for x in entities) or len(set(entities))!=len(entities):
        return errors+["Selected entity IDs must be unique and non-empty"]
    ids=set(entities)
    if len(entities)<2:errors.append("Comparison requires at least 2 entities; one entity is an analysis view")
    win=data.get("window",{})
    if not isinstance(win,dict):return errors+["Window must be object"]
    buckets=win.get("time_buckets",[])
    if not isinstance(buckets,list) or not buckets or len(buckets)!=len(set(buckets)):
        errors.append("Time buckets must be unique and non-empty")
        buckets=[]
    try:
        start=date.fromisoformat(win["start"]);end=date.fromisoformat(win["end"])
        dates=[date.fromisoformat(x) for x in buckets]
        if start>end or dates!=sorted(dates) or any(d<start or d>end for d in dates):
            errors.append("Time buckets must be ascending and inside common window")
    except (KeyError,ValueError,TypeError):
        errors.append("Comparison dates must use valid ISO date windows")
    if win.get("granularity") not in ("day","week","month","year"):
        errors.append("Comparison requires common day/week/month/year aggregation")
    metric=data.get("metric",{})
    if not isinstance(metric,dict) or not metric.get("id") or not metric.get("unit") or not metric.get("aggregation"):
        errors.append("Timeline metric must declare common ID/unit/aggregation")
    series=data.get("series",[])
    if not isinstance(series,list):return errors+["Series must be list"]
    sids=[s.get("entity_id") for s in series if isinstance(s,dict)]
    if len(sids)!=len(series) or len(sids)!=len(set(sids)) or set(sids)!=ids:
        errors.append("Selected entities must equal chart series and legend entity IDs exactly")
    colors=[]
    for s in series:
        if not isinstance(s,dict):errors.append("Malformed chart series");continue
        entity=s.get("entity_id")
        status=s.get("status")
        if status not in VALID_STATUS:errors.append(f"{entity}: unknown data status")
        if not str(s.get("legend","")).strip() or not str(s.get("color_token","")).strip():
            errors.append(f"{entity}: missing legend/color identity")
        colors.append(s.get("color_token"))
        pts=s.get("points",[])
        if not isinstance(pts,list):errors.append(f"{entity}: points must be list");continue
        if not pts and status!="no_data":errors.append(f"{entity}: available series cannot be empty")
        pids=[p.get("bucket") for p in pts if isinstance(p,dict)]
        if len(pids)!=len(pts) or len(set(pids))!=len(pids):
            errors.append(f"{entity}: duplicate/malformed time buckets")
        for p in pts:
            if not isinstance(p,dict):errors.append(f"{entity}: malformed point");continue
            if p.get("bucket") not in buckets:errors.append(f"{entity}: point outside shared timeline")
            value=p.get("value")
            if value is not None and (isinstance(value,bool) or not isinstance(value,(int,float))):
                errors.append(f"{entity}: invalid numeric chart point")
            if value is None and not str(p.get("missing_reason","")).strip():
                errors.append(f"{entity}: missing value requires explicit reason; never coerce to zero")
        numerical=sum(1 for p in pts if isinstance(p,dict) and p.get("value") is not None)
        if status=="no_data" and numerical:errors.append(f"{entity}: no_data status cannot have numeric points")
        if status=="available" and numerical!=len(buckets):
            errors.append(f"{entity}: available requires complete shared-bucket coverage; otherwise mark partial")
        if status=="partial" and numerical==len(buckets):
            errors.append(f"{entity}: partial status must actually have unavailable buckets")
    if len(set(colors))!=len(colors):
        errors.append("Each selected series needs a stable distinct color token")
    table=data.get("table",{})
    if not isinstance(table,dict):return errors+["Table missing"]
    if table.get("columns")!=entities:errors.append("Table columns must preserve selected entity identity and order")
    seen_metrics=set()
    for row in table.get("metrics",[]):
        if not isinstance(row,dict):errors.append("Malformed metric row");continue
        m=row.get("id")
        if m in seen_metrics:errors.append("Duplicate metric row ID")
        seen_metrics.add(m)
        if not row.get("unit") or row.get("direction") not in ("lower","higher","neutral"):
            errors.append(f"{m}: missing metric units/direction")
        cells=row.get("cells",[])
        if not isinstance(cells,list):errors.append(f"{m}: cells must be list");continue
        cell_ids=[c.get("entity_id") for c in cells if isinstance(c,dict)]
        if len(cell_ids)!=len(cells) or len(set(cell_ids))!=len(cell_ids) or cell_ids!=entities:
            errors.append(f"{m}: each selected entity needs exactly one cell, same column order")
        for cell in cells:
            if not isinstance(cell,dict):errors.append(f"{m}: malformed cell");continue
            entity=cell.get("entity_id")
            cov=cell.get("coverage")
            value=cell.get("value")
            n=cell.get("sample_size")
            if cov not in VALID_COVERAGE:errors.append(f"{m}/{entity}: invalid coverage state")
            if not isinstance(n,int) or isinstance(n,bool) or n<0:errors.append(f"{m}/{entity}: invalid sample size")
            if cov in ("not-collected","not-applicable","insufficient") and value is not None:
                errors.append(f"{m}/{entity}: missing/insufficient coverage cannot be numeric zero or winner")
            if value is None and cov in ("complete","partial"):
                errors.append(f"{m}/{entity}: null must not pretend to be available")
            if value is not None and (not isinstance(value,(int,float)) or isinstance(value,bool)):
                errors.append(f"{m}/{entity}: invalid numeric value")
            if value is not None and isinstance(n,int) and n==0:
                errors.append(f"{m}/{entity}: numeric metric requires nonzero sampled evidence")
    presentation=data.get("presentation",{})
    if not isinstance(presentation,dict):return errors+["Presentation missing"]
    if presentation.get("selected_count")!=len(entities):
        errors.append("Displayed selected count must equal selected entity count")
    if presentation.get("show_critical_coverage_notice") is not True or not presentation.get("show_missing_as"):
        errors.append("Comparison requires visible coverage/missing-data explanations")
    review=data.get("review",{})
    if not isinstance(review,dict) or review.get("browser_status") not in ("NOT RUN","PASS","FAIL"):
        errors.append("Browser review status missing")
    elif review["browser_status"]=="PASS":
        if len(review.get("viewports",[]))<2 or not review.get("evidence"):
            errors.append("Browser PASS requires actual viewport/screenshots")
        if review.get("plot_labels_verified") is not True or review.get("selected_series_verified") is not True:
            errors.append("Browser PASS requires real plot-label and series-selector verification")
    return errors


def validate_repository():
    errors=[f"Missing comparison file: {p}" for p in REQUIRED if not (ROOT/p).exists()]
    errors.extend(validate_catalog())
    try:errors.extend(validate_contract(json.loads(EXAMPLE.read_text("utf-8"))))
    except (OSError,ValueError,KeyError) as e:errors.append("Comparison example invalid: "+str(e))
    skill=(ROOT/"SKILL.md").read_text("utf-8")
    for label in ("comparison-page-design.md","chart-interior-alignment.md",
                  "validate_comparison_contract.py","audit_comparison_ui.mjs"):
        if label not in skill:errors.append("SKILL.md lacks comparison routing: "+label)
    return errors


def main():
    p=argparse.ArgumentParser(description="Data contract QA, not ECharts visual QA")
    p.add_argument("file",nargs="?",type=Path)
    p.add_argument("--repository",action="store_true")
    p.add_argument("--json",action="store_true")
    args=p.parse_args()
    errors=validate_repository() if args.repository else validate_catalog() if args.file is None else []
    if args.file:
        try:errors.extend(validate_contract(json.loads(args.file.read_text("utf-8"))))
        except (OSError,ValueError) as e:errors.append(str(e))
    if args.json:print(json.dumps({"passed":not errors,"errors":errors,"scope":"data contract only, NOT chart rendering or visual aesthetics"},ensure_ascii=False,indent=2))
    else:
        for s in errors:print("ERROR:",s)
        print("Comparison contract:", "PASS" if not errors else "FAIL")
    return 1 if errors else 0


if __name__=="__main__":raise SystemExit(main())
