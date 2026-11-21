# Chart Interior QA — Plot Areas, Not Merely Card Borders

> Synthetic anti-pattern: two neighboring chart Cards have matching outside borders, but their plot areas, axes, markers and legends do not share a coherent baseline. Inspect the *chart interior*, not just its containing Card.

## Alignment does not mean forcing every canvas to the same height

- **Layers:** Panel header/title/description → plot viewport → axes/labels/legend → footnote/disclaimer. Each layer has a distinct spacing role.
- **Baselines:** Charts using comparable time windows and dimensions should have comparable X-axis/plot start positions. Different dimensions or chart types may warrant different margins, but each needs a clear visual region.
- **Whitespace:** Do not place a vast empty plot area in one chart, squeezing data points toward the center, merely to match the outside height of a neighboring chart whose plot is full. Increasing useful chart height or choosing a different chart type can be appropriate.
- **Labels:** If labels overlap, use the chart library's supported `labelLayout` (for ECharts, when supported), `hideOverlap`, formatters, positional offsets or tooltips as appropriate; confirm in screenshots at the actual window size. A fix for one label must not clip another against the chart frame.
- **Data states:** With no real data, show an explicit empty state. Never fabricate a near-zero curve. **0 and null have different meanings.**
- **Evidence:** Use browser geometry and screenshots. For Canvas content, consult chart-engine rendering APIs or examine rendered screenshots when necessary. Record `NOT AUDITED` if labels cannot be inspected.

## Automated audit boundaries

`scripts/audit_comparison_ui.mjs` can compare marked plot groups' top/bottom alignment, visible SVG/HTML label bounding rectangles, horizontal container overflow and bottom reachability. Without accessible DOM information, however, generic browser scripts cannot infer all Canvas labels, tooltips or masks. Findings are **not** an automatically repairable list of visual bugs: the Agent must inspect actual browser renderings.
