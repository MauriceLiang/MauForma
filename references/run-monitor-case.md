# Asynchronous Run Monitor — Synthetic Failure and Verification

**Nature:** Generic teaching counterexample, not material from any actual backend or user screenshot.

## Counterexample

A run-history page permanently devotes a large left section to status counts; every item on the right repeats a lengthy “progress unknown” explanation. Status filtering is awkward, error details are hidden, and short action labels wrap vertically, one character per line, in a narrow column.

## Transferable rules

- Distinguish **asynchronous execution monitoring** from assigning human tasks. A Kanban board is not the right default for every feature called “Tasks.”
- Support troubleshooting with actionable status filters, compact scannable records, and **actual** timestamps and states.
- **Unknown progress is not 0%.** Failed, blocked and completed states determine valid actions and visible feedback.
- Reveal details, logs and retry on demand rather than repeating explanations on every row.
- Reserve usable action-column width; when space is insufficient, reflow the **whole action group**, never wrap individual short actions vertically or clip them.

## Verification

`examples/task-center-demo.json` is a synthetic state example. A **real product** additionally needs API, permission, retry outcome, state consistency, keyboard focus and final-scroll verification.
