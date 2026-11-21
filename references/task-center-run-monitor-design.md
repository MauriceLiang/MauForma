# Task Center & Run Monitor UX — An Operations Workspace, Not a Pile of Numbers (v6.11)

**Applies to:** Async jobs, data collection, CI/CD, batch processing, import/export, Agent Runs, deployments and background-job monitoring. If the task is about **human assignment, milestones or Kanban**, Linear patterns may help, but **do not copy a human-task Kanban directly into automated Run monitoring**. All failure scenarios below are entirely fictional; not evidence from real projects.

## Established product research — transfer workflow, not brand skin

| Reference | Useful behavior | Applies when | Do not blindly copy |
| --- | --- | --- | --- |
| [GitHub Actions run history](https://docs.github.com/en/actions/monitoring-and-troubleshooting-workflows/monitoring-workflows/viewing-workflow-run-history) | Run list surfaces status/object/time; click for steps and logs | One-off or recurring jobs | Complex repository/workflow navigation |
| [GitLab Pipelines](https://docs.gitlab.com/ci/pipelines/) / [Jobs](https://docs.gitlab.com/ci/jobs/) | State filtering, stages, failure-first, authorized retries/cancels | Multi-stage collectors/pipelines | A fictitious DAG for a one-step operation |
| [Trigger.dev Runs](https://trigger.dev/changelog/live-runs-page) / [Run Inspector](https://trigger.dev/changelog/run-page-inspector) | Live status, new-run notices, timeline/log/input-output in detail | Frequent async jobs and parent-child work | All developer-debug metadata |
| [Inngest inspect runs](https://www.inngest.com/docs/platform-and-operations/inspect-events-and-runs) | Trace failure to trigger event, step and retry | Diagnosable multi-step workflow | Raw event payload always visible in list |
| [Vercel deployments](https://vercel.com/docs/deployments/managing-deployments) | Clear status/time filtering, run detail, conditionally redeploy | Versioned objects and batch jobs | Treating job retry as equivalent to redeploy |
| [Linear display/filters](https://linear.app/docs/display-options) | Custom displayed fields, grouped statuses, priority/sort/filter | Scanning/locating/batch handling | Human issue management as machine progress model |

**Common principle:** A row should answer “what job, current state, when, next action.” Steps/logs belong in details. State, filtering and density are efficiency features, not decorative Cards. Citing different references does not mean they share an identical layout.

## Gate T0 — Classify work and user job

- `run_monitor`: automated run, queued work, changing status and retry.
- `human_tasks`: assigned people, priorities, due dates, milestones.
- `mixed`: both exist but roles clearly separate.

Run Monitor asks: What failed or stalled? Is it still running? What progress is real? Which action is permitted? Where is failure reason/log? If only 3/3/1 counts are prominent and the failure requires a full screen of scrolling, the design misses the task.

## Gate T1 — Information density and layering

1. **Header:** “Task Center” + necessary repository/workspace scope; one Refresh action at right with last-updated/auto-refresh state where useful. Not long “Mock service handling” copy.
2. **State overview:** Prefer compact Filter Tabs/Segmented (All / Running / Queued / Needs attention / Succeeded), where **counts operate as selectable filters**. Large independent statistics Cards require real trend/health analysis; never dedicate a permanent quarter-screen panel to basic counts.
3. **Main task list:** Own most available width, use **table/compact rows** with readable space. Columns: task/object (including type), state, real progress/current stage, update time, actions. Avoid 110px tall rows stuffed with repeated explanations.
4. **Priority:** Make `requires_attention`, running and waiting easier to find than historical completions by default; allow user-chosen updated-time order. No colored block, warning stripe or invented prefix per row.
5. **Detail:** On demand via Drawer/page/expand according to workflow: trigger, timeline, current step, **actual** logs, failure cause and retry history. Do not show all content in every list row.
6. **State semantics:** `queued`, `running`, dependency `waiting`, `partial`, `failed`, `blocked`, `succeeded`, `canceled` differ. Aggregate for user-friendly filters only when necessary; don't erase meaning into “needs attention” or universal “processing.”
7. **Empty states:** No jobs → legitimate next action; no filter matches → clear filter; loading/API failure is not 0 completed tasks.
8. **Layout:** Desktop aligned columns; on mobile use structured task rows/cards, not five 10px columns. Allow natural scroll to end (v6.9).

## Gate T2 — Data contract for each job row

The backend `task_id` must be unique and not arbitrarily recycled. `repository`, `task_type`, `state`, `started_at`/`updated_at`, `retryable` and `details_route` have defined semantics. Use correct timestamps and actual locale/timezone; do not show fixed Mock timestamps as “just now.”

- **Progress:** Convert `completed / total` to percent only when same units, `total > 0` and **total is a confirmed denominator**. `1200/6800` is ~17.6%; if denominator can grow, label estimated/incomplete. With only a stage string, show “Analyzing” and a valid logs link; **never fabricate 42%, ETA or a fixed progress bar**.
- **Missing:** `progress:null` ≠ 0%; `error:null` ≠ “unknown error”; `updated_at:null` ≠ “just now”.
- **State consistency:** Filter counts derived from same data as list; state and actions agree; `succeeded` alone does not mean complete GitHub dataset coverage.
- **Attention:** Actionable `partial/failed/blocked` may enter Attention. Retry depends on `retryable`, permissions, backend support and cause; no fake buttons for all unusual states. Blocked authentication/metric definition generally needs a repair action first.
- **Retry:** User trigger → check latest Run status/permission → backend request → update after response. Do not fake server success on click. Optimistic feedback requires rollback/error explanation; handle duplicates through backend-supported idempotency or disabled pending action.
- **Cancel/pause:** Offer only when backend and permission support exist. Explain impact if irreversible or affecting subsequent jobs; no decorative actions.
- **Live updates:** Poll/SSE/WebSocket/manual refresh all possible; show last update and disconnected status. Refresh should not jump list to top, clear filters or change active object without cause; new-run prompt can avoid forced reordering.
- **Row detail:** One relevant failure cause or next action near row; do not repeat a paragraph “progress percent unknown; showing stage” everywhere.

## Gate T3 — Interaction, discoverability and sorting

A reasonable default supports status filter, repository/task-type search/filter, clear time/importance sort, detail, authorized retry and cancellation if applicable. **Do not mandate** bulk operations, Kanban, pagination or auto-refresh for every product; volume and permissions matter.

- Filter counts must agree with visible rows, or clarify page versus total scope under pagination/search/server aggregates.
- Entire clickable row and inner action Buttons must not conflict; Tab/Enter/Space reach relevant actions, not hover-only access.
- Returning from details/dialog preserves focus, filter and list context; failures have meaningful recovery path.
- Completed-history remains available without crowding out current failures.

## v6.13 — General surface and control defects, not just a task center

A synthetic UI example shows a giant white rounded outer Card enclosing filters, heading, table header and records. This **might** represent a useful unified data scope, or just generic “every backend page needs a Card.” Compare flat toolbar+table with single bounded panel using `references/surface-architecture-gate.md`, deciding from independent task/state scope. Flat table is not universally correct.

A synthetic row's “View Details” and “Retry” labels wrap **character by character**, a blocking readability defect. Screenshot alone cannot prove whether root cause is `table-layout:fixed`, Grid width, Flex shrink or Button CSS. Inspect **action column width + button intrinsic width + whole-action reflow** per `references/control-geometry-gate.md`; do not just tweak radius or shrink font. When an error adds Retry, both words still need to be complete/reachable. This rule applies to all tables, toolbars and short actions, not one teaching fixture.

## Gate T4 — Layout and visual discipline

Align task identity, status, progress/stage, timestamps and action columns according to actual decision priority. Use one coherent row-height/column track; status color means status, not extra giant colored background and icon wall per row. Peer rows align left edges, text baselines and action columns.

Do not fill available width with duplicated explanation. Appropriate content width and readable columns beat arbitrary stretching. Use spare width for useful filters or genuine progress, not ornamental paragraphs.

**Valid product exceptions:** A dedicated anomaly-investigation center might need a compact persistent filter rail; a single-job flow might need a large progress view. There is no blanket ban on Side Panels. The question is whether the area has independent frequent filter/analysis value.

## Gate T5 — Real browser acceptance

- On supported desktop (e.g. 1440×900, 1280×720) and narrow (e.g. 390×844), assess scan speed, action/status/progress clarity, row/column alignment.
- Filter counts match actual rows; search/pagination scope labels do not mislead.
- `partial/failed/blocked` have distinct permissions/actions; Retry never shows on unauthorized succeeded/queued records.
- Only confirmed progress denominators lead to percentage bars; unknown shows indeterminate/state.
- Detail, logs and expand work without destroying layout; long repo/error copy wraps/truncates with access to full values.
- Small screens retain all tasks and scroll-to-end; fixed bars never cover action Buttons.
- Browser/synthetic automation proves only tested states. **Actual server retry, auth, logs and live data need API/E2E**, not screenshots/Mock.

## Assets and validation

- Sources: `assets/task-center-reference-cases.json`
- Synthetic review: `references/run-monitor-case.md`
- Schema/examples: `assets/task-center-run.schema.json`, `examples/task-center-demo.json`
- Interaction demo: `assets/task-center-layout-lab.html` (filter/search/detail/simulated retry)
- Contract validator: `python3 scripts/validate_task_center.py examples/task-center-demo.json --repository`
- Browser fixture: `tests/task_center_browser_smoke.mjs`. Real products require their own code/browser/API evidence.

v6.8 content selection, v6.9 Grid/scroll safety and v6.10 comparison-data rules remain valid; a Task Center applying Run Monitor rules is **not** a page comparing objects A and B.
