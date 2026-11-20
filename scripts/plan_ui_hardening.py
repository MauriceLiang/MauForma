#!/usr/bin/env python3
"""Generate a scoped, non-claiming UI resilience test matrix for a real project."""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

BASE=[
 ("long-copy","Long Chinese/English labels, 200% zoom and overflow","text, headings, buttons"),
 ("empty","Empty collection and zero results","primary CTA, recovery"),
 ("error","Validation, API 4xx/5xx, permissions and timeout","error meaning and next action"),
 ("pending","Network latency and repeated submission","disabled/progress and no fake completion"),
 ("motion","Reduced-motion and interrupted transition","same semantic result and focus"),
 ("keyboard","Tab, Escape, Enter, focus restoration","focus visible and control semantics")
]
OPTIONAL={
 "rtl":("rtl","Right-to-left labels, logical spacing and keyboard flow","dir=rtl, layout and icons"),
 "offline":("offline","Disconnected/slow network during action","retry and unsaved state"),
 "mobile":("mobile","Small touch viewport","navigation, 44px target where applicable, input zoom"),
 "large-data":("large-data","1000+ rows or large numbers","virtualization, unit and readable scale")
}
def matrix(flags: list[str]) -> dict:
    rows=[{"id":a,"scenario":b,"assert":c,"status":"NOT_TESTED"} for a,b,c in BASE]
    rows.extend({"id":OPTIONAL[f][0],"scenario":OPTIONAL[f][1],"assert":OPTIONAL[f][2],"status":"NOT_TESTED"} for f in dict.fromkeys(flags))
    return {"status":"PLAN_ONLY","tests":rows,
            "note":"These are test intentions, not evidence of execution. Run real browser/backend scenarios and record outcomes in the feature review."}
def main()->int:
    p=argparse.ArgumentParser()
    p.add_argument("--include",choices=list(OPTIONAL),action="append",default=[])
    p.add_argument("--out",type=Path,default=Path("artifacts/mauforma-hardening.json"))
    args=p.parse_args();report=matrix(args.include)
    args.out.parent.mkdir(parents=True,exist_ok=True)
    args.out.write_text(json.dumps(report,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    print(json.dumps({"status":report["status"],"tests":len(report["tests"]),"out":str(args.out)}))
    return 0
if __name__=="__main__":sys.exit(main())
