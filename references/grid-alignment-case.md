# Grid Alignment and Scroll End — Synthetic Failure and Verification

**Nature:** An entirely fictional layout training case.

## Counterexample

A data page builds its left and right columns as two independent vertical Stacks. The differing heights of the first row make the starts of the second row visibly misalign. A fixed action bar at the bottom may obscure the final row of content.

## Transferable rules

- For modules requiring peer comparison, prefer **shared Grid rows/columns** and common content edges.
- Asymmetry and spanning layouts can be valid when supported by information priority and visual anchors. Creative pages do **not** have to make every Card equal height.
- Distinguish **content that normally requires scrolling** from **a genuinely unreachable final item**. A screenshot alone does not prove incorrect `overflow` configuration.
- A fixed bottom action bar needs safe space at scroll end; if it serves no purpose, restore natural document flow.
- Check narrow/tall, wide/short, long copy and 200% text sizing. Do not hide overflow merely to conceal defects.

## Verification

`examples/layout-integrity-demo.json` is a synthetic layout contract. **Real pages** require actual row alignment, bottom-scroll access, occlusion and action-reachability testing.
