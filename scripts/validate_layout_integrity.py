#!/usr/bin/env python3
"""MauForma v6.9: validate alignment plans, bottom-reachability intent and reference integrity.

This script checks declarative plans. It does NOT inspect live geometry.
Use scripts/audit_rendered_layout.mjs with the target application's browser to do that.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CATALOG = ROOT/"assets/layout-integrity-patterns.json"
EXAMPLE = ROOT/"examples/layout-integrity-repovantage.json"
REQUIRED = (
 "references/grid-alignment-and-viewport-safety.md",
 "references/repovantage-release-alignment-case.md",
 "assets/layout-integrity-patterns.json",
 "assets/layout-integrity.schema.json",
 "assets/grid-and-viewport-lab.html",
 "examples/layout-integrity-repovantage.json",
 "scripts/validate_layout_integrity.py",
 "scripts/audit_rendered_layout.mjs",
 "tests/test_layout_integrity.py",
)


def validate_catalog(data=None):
    errors=[]
    if data is None:
        try:data=json.loads(CATALOG.read_text("utf-8"))
        except (ValueError,OSError) as ex:return [f"Catalog unreadable: {ex}"]
    patterns=data.get("patterns",[])
    ids=[p.get("id") for p in patterns if isinstance(p,dict)]
    if not {"shared-row-grid","main-feature-span","editorial-asymmetry","masonry"}.issubset(set(ids)):
        errors.append("Need shared grid, main span, editorial and masonry pattern definitions")
    if len(ids)!=len(patterns) or len(ids)!=len(set(ids)):
        errors.append("Invalid/duplicate pattern IDs")
    for p in patterns:
        if not isinstance(p,dict):errors.append("Invalid pattern");continue
        if not p.get("alignment") or not p.get("fit") or not p.get("requires") or not p.get("exception"):
            errors.append(f"Pattern {p.get('id')} lacks fit/rationale/exception")
    refs=data.get("references",[])
    if len(refs)<3 or any(not str(r.get("url","")).startswith("https://") for r in refs):
        errors.append("Need cited official technical/design sources")
    gates=data.get("gates",{})
    required=("must_check_shared_row_alignment","allow_intentional_asymmetry",
              "prefer_natural_scroll_to_clipping","must_test_last_scroll_position",
              "must_test_reachable_last_action","do_not_conflate_below_fold_with_clipping",
              "no_universal_equal_height_rule")
    errors.extend(f"Missing safety gate: {k}" for k in required if gates.get(k) is not True)
    return errors


def validate_plan(data,catalog=None):
    if catalog is None:catalog=json.loads(CATALOG.read_text("utf-8"))
    errors=[]
    if not isinstance(data,dict) or data.get("schema_version")!="1.0":
        return ["Unsupported layout integrity plan version"]
    if not str(data.get("page","")).strip() or not str(data.get("purpose","")).strip():
        errors.append("Page and purpose are required")
    intent=data.get("intent")
    if intent not in {"provisional","confirmed","delegated","inherited"}:
        errors.append("Unknown decision provenance")
    if intent in {"confirmed","delegated"} and not str(data.get("user_statement") or "").strip():
        errors.append("User-confirmed/delegated layout needs real user statement")
    layout=data.get("layout",{})
    if not isinstance(layout,dict):return errors+["layout must be object"]
    patterns={p["id"]:p for p in catalog.get("patterns",[])}
    pat=layout.get("pattern_id")
    if pat not in patterns:errors.append("Unknown layout pattern")
    if layout.get("mode") in {"operate","read"} and pat in {"editorial-asymmetry","masonry"}:
        if len(str(layout.get("intentional_asymmetry_reason","")).strip())<20:
            errors.append("Data/workspace asymmetric or masonry layout requires meaningful rationale")
    regions=layout.get("regions",[])
    if not isinstance(regions,list) or not regions:return errors+["Need actual layout region inventory"]
    ids=[r.get("id") for r in regions if isinstance(r,dict)]
    if len(ids)!=len(regions) or not all(isinstance(i,str) and i for i in ids) or len(set(ids))!=len(ids):
        errors.append("Region IDs missing or duplicated")
    byid={r["id"]:r for r in regions if isinstance(r,dict) and r.get("id")}
    if any(not isinstance(r.get("row"),int) or not isinstance(r.get("col"),int) or r["row"]<1 or r["col"]<1 for r in regions if isinstance(r,dict)):
        errors.append("Regions require positive row and column tracks")
    if len({(r.get("row"),r.get("col")) for r in regions if isinstance(r,dict)})!=len(regions):
        errors.append("Two panels overlap same grid cell without span semantics")
    groups=layout.get("align_groups",[])
    if not isinstance(groups,list):errors.append("align_groups must be array");groups=[]
    for group in groups:
        if not isinstance(group,dict):errors.append("Malformed alignment group");continue
        gp=group.get("ids",[])
        if not isinstance(gp,list) or len(gp)<2 or any(x not in byid for x in gp):
            errors.append("Alignment group references missing/too few regions")
            continue
        if group.get("axis")=="top":
            rows={byid[x].get("row") for x in gp}
            if len(rows)>1:errors.append("Top-aligned peer regions must share the same row in the grid plan")
    order=layout.get("mobile_order",[])
    if not isinstance(order,list) or set(order)!=set(ids) or len(order)!=len(ids):
        errors.append("Mobile reading order must include each content region exactly once")
    if pat=="shared-row-grid" and len(regions)>=4:
        rows={}
        for r in regions:rows.setdefault(r["row"],[]).append(r["id"])
        for row,items in rows.items():
            if len(items)>=2 and not any(set(items).issubset(set(g.get("ids",[]))) and g.get("axis")=="top" for g in groups):
                errors.append(f"Shared grid row {row} requires explicit top alignment group")
    sc=data.get("scroll",{})
    if not isinstance(sc,dict):return errors+["Scroll plan missing"]
    if sc.get("mode") not in {"document","app-shell","fixed-action-bar"}:
        errors.append("Unknown scroll architecture")
    if sc.get("scroll_to_end_required") is not True:
        errors.append("Must validate final scroll position, not only first screen")
    if sc.get("bottom_safe_area") is not True:
        errors.append("Plan must consider bottom safe-area/end padding")
    if not str(sc.get("end_padding_strategy","")).strip():
        errors.append("End-padding strategy missing")
    if sc.get("last_content_id") not in byid:
        errors.append("Last meaningful content must refer to a real region")
    if sc.get("has_fixed_bar") and sc.get("mode")!="fixed-action-bar" and "bar" not in str(sc.get("end_padding_strategy","")).lower():
        errors.append("Fixed bar requires explicit measured-size reserve or normal-flow design")
    review=data.get("review",{})
    if not isinstance(review,dict) or review.get("browser_status") not in {"NOT RUN","PASS","FAIL"}:
        errors.append("Browser status invalid")
    elif review["browser_status"]=="PASS":
        if len(review.get("viewports",[]))<2 or not review.get("evidence"):
            errors.append("Browser PASS requires multiple viewports and real evidence")
        if review.get("scrolled_to_end") is not True:
            errors.append("Browser PASS requires actual end-of-scroll verification")
    return errors


def validate_repository():
    errors=[f"Missing v6.9 file: {p}" for p in REQUIRED if not (ROOT/p).exists()]
    errors.extend(validate_catalog())
    try:errors.extend(validate_plan(json.loads(EXAMPLE.read_text("utf-8"))))
    except (OSError,ValueError,TypeError,KeyError) as ex:errors.append(f"Example invalid: {ex}")
    try:skill=(ROOT/"SKILL.md").read_text("utf-8")
    except OSError:skill=""
    for s in ("grid-alignment-and-viewport-safety.md","validate_layout_integrity.py","audit_rendered_layout.mjs"):
        if s not in skill:errors.append("SKILL.md lacks v6.9 route: "+s)
    return errors


def main():
    p=argparse.ArgumentParser(description="Check layout plans; does NOT replace live browser scrolling QA")
    p.add_argument("plan",nargs="?",type=Path)
    p.add_argument("--repository",action="store_true")
    p.add_argument("--json",action="store_true")
    args=p.parse_args()
    errors=validate_repository() if args.repository else validate_catalog() if args.plan is None else []
    if args.plan:
        try:errors.extend(validate_plan(json.loads(args.plan.read_text("utf-8"))))
        except (ValueError,OSError) as ex:errors.append(str(ex))
    if args.json:print(json.dumps({"passed":not errors,"errors":errors,"scope":"declarative checks, not pixel geometry"},ensure_ascii=False,indent=2))
    else:
        for err in errors:print("ERROR:",err)
        print("Grid & bottom-safety plan:", "PASS" if not errors else "FAIL")
    return 1 if errors else 0


if __name__=="__main__":
    raise SystemExit(main())
