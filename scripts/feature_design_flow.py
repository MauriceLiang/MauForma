#!/usr/bin/env python3
"""Opt-in, resumable per-feature design workflow. Never overwrites approved design system."""
from __future__ import annotations
import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path

def feature_dir(root: Path, slug: str) -> Path:
    if not re.fullmatch(r"[a-z0-9][a-z0-9-]{0,63}", slug):
        raise ValueError("Feature must be a lowercase safe slug")
    return root / "design-system" / "features" / slug

DEFAULT_TASKS = [
    {"id": "F01", "name": "Verify product brief, scope and inherited design tokens", "done": False, "acceptance": "Existing system and user decisions identified"},
    {"id": "F02", "name": "Build a risky vertical slice with structure, visual detail and interaction", "done": False, "acceptance": "Working UI + loading/empty/error/keyboard where applicable"},
    {"id": "F03", "name": "Complete remaining slices without introducing duplicate primitives", "done": False, "acceptance": "Routes, states and components implemented according to brief"},
    {"id": "F04", "name": "Review shipped-size visuals and real interactions", "done": False, "acceptance": "Screenshots, reduced motion, edge states and explicit test evidence"},
]

def init(root: Path, slug: str, mode: str, task: str, apply: bool = False) -> dict:
    target = feature_dir(root, slug)
    if target.exists() and any(target.iterdir()):
        return {"status": "ALREADY_EXISTS", "path": str(target), "next": "Use --action status; existing work preserved"}
    docs = {
        "BRIEF.md": f"# Feature Brief: {slug}\n\n- User task: {task or 'UNRESOLVED'}\n- Page mode: {mode or 'UNRESOLVED'}\n- Inherits: ../../MASTER.md and ../../decisions.json (do not copy global tokens)\n- Audience / content / primary action: TO CONFIRM\n- Source of decisions: unresolved until user approves or delegates\n- Visual direction / motion behavior: TO DECIDE\n- Constraints / out of scope: TO DOCUMENT\n",
        "IA.md": "# Information Architecture\n\n- Routes and navigation: TO DEFINE\n- Content priority and reading order: TO DEFINE\n- Primary and secondary flows: TO DEFINE\n- Errors, empty/loading and interrupted states: TO DEFINE\n",
        "TASKS.md": "# Vertical-slice Task Plan\n\n" + "\n".join("- [ ] **"+t["id"]+"** "+t["name"]+" — "+t["acceptance"] for t in DEFAULT_TASKS) + "\n",
        "REVIEW.md": "# Design & Interaction Review\n\n- Status: NOT_TESTED\n- Scope and supported viewports: TO DOCUMENT\n- Real screenshots and interactions: NOT_CAPTURED\n- Findings (file/route/state/evidence): TO REVIEW\n- Reduced motion and interruption: NOT_TESTED\n- Unresolved issues: TO DOCUMENT\n",
        "state.json": json.dumps({"schema":1,"feature":slug,"created_at":datetime.now(timezone.utc).isoformat(),
                                  "phase":"BRIEF", "source":"unresolved", "tasks":DEFAULT_TASKS,
                                  "review_status":"NOT_TESTED","decisions_are_user_approved":False},ensure_ascii=False,indent=2)+"\n"
    }
    if apply:
        target.mkdir(parents=True,exist_ok=False)
        for name,body in docs.items(): (target/name).write_text(body,encoding="utf-8")
    return {"status": "CREATED" if apply else "PREVIEW_ONLY", "path":str(target), "files":list(docs)}

def status(root: Path, slug: str) -> dict:
    target=feature_dir(root,slug)
    if not (target/"state.json").exists():
        return {"status":"NOT_INITIALIZED", "path":str(target)}
    state=json.loads((target/"state.json").read_text(encoding="utf-8"))
    completed=[t["id"] for t in state.get("tasks",[]) if t.get("done")]
    waiting=[t["id"] for t in state.get("tasks",[]) if not t.get("done")]
    return {"status":"IN_PROGRESS" if waiting else "REVIEW_PENDING" if state.get("review_status")!="VERIFIED" else "COMPLETE",
            "path":str(target),"phase":state.get("phase"),"completed":completed,"next":waiting[0] if waiting else "REVIEW",
            "review_status":state.get("review_status"),"decisions_are_user_approved":state.get("decisions_are_user_approved",False)}

def complete(root: Path, slug: str, task: str, evidence: str) -> dict:
    target=feature_dir(root,slug)
    state_path=target/"state.json"
    if not state_path.exists(): raise ValueError("Initialize feature first")
    if len(evidence.strip())<12: raise ValueError("--evidence must identify real implementation/test result (12+ characters)")
    state=json.loads(state_path.read_text(encoding="utf-8"))
    choice=next((t for t in state["tasks"] if t["id"]==task),None)
    if choice is None: raise ValueError("Unknown task ID")
    if choice.get("done"): return {"status":"UNCHANGED", "task":task,"reason":"Already complete"}
    choice["done"]=True; choice["evidence"]=evidence
    state["phase"]="IMPLEMENTATION" if any(not t["done"] for t in state["tasks"]) else "REVIEW"
    state_path.write_text(json.dumps(state,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
    # The Markdown checklist is a view, rebuilt from the state; do not change other files.
    (target/"TASKS.md").write_text("# Vertical-slice Task Plan\n\n"+"\n".join("- ["+("x" if t["done"] else " ")+"] **"+t["id"]+"** "+t["name"]+" — "+t["acceptance"]+(" (Evidence: "+t["evidence"]+")" if "evidence" in t else "") for t in state["tasks"])+"\n",encoding="utf-8")
    return {"status":"TASK_RECORDED", "task":task, "next":status(root,slug)["next"]}

def main() -> int:
    parser=argparse.ArgumentParser()
    parser.add_argument("--project-root",type=Path,required=True)
    parser.add_argument("--feature",required=True)
    parser.add_argument("--action",choices=["init","status","complete"],default="status")
    parser.add_argument("--mode",choices=["","Persuade","Operate","Read","Experience"],default="")
    parser.add_argument("--task",default="")
    parser.add_argument("--evidence",default="")
    parser.add_argument("--apply",action="store_true",help="Explicitly create feature files; init previews by default")
    args=parser.parse_args()
    root=args.project_root.resolve()
    if not root.is_dir(): parser.error("Project root must exist")
    try:
        if args.action=="init": result=init(root,args.feature,args.mode,args.task,args.apply)
        elif args.action=="complete": result=complete(root,args.feature,args.task,args.evidence)
        else: result=status(root,args.feature)
    except (ValueError,FileExistsError) as exc:parser.error(str(exc))
    print(json.dumps(result,ensure_ascii=False,indent=2))
    return 0

if __name__=="__main__":
    sys.exit(main())
