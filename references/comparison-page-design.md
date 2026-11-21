# Comparison UX & Chart Integrity — Help Compare Differences, Not Just Arrange Charts (v6.10)

## Trigger and observed failure examples

Applies to projects, products, plans, technology selection and other multi-object comparisons. The following are illustrative UI cases and general verification requirements:

- **Interior alignment missed:** Cards for adjacent release intervals and cadence distribution appear to share outer edges, yet plot regions, X-axis baselines, labels and whitespace differ. Dense right-edge labels such as “63/60/67 days” collide. v6.9 exterior Grid integrity does **not** prove the charts are readable.
- **No clear comparative insight:** After selecting three repositories, a large trends chart, collaboration chart, verbose explanation and table occupy space. A methodology Card contains little actual value. Legend names several repositories but it is unclear whether each has a genuine series, and metrics do not compare across chart/table consistently.
- **No unsupported assumptions:** Screenshots do not prove source-data correctness, that all repositories loaded, whether a hidden series is revealed by Tooltip or whether additional interactions exist. Verify real data model and actual browser.

## External research — preserve source and transfer limits

| Site/research | Transferable value | How it informs repository comparison | Do not copy |
| --- | --- | --- | --- |
| [NN/g — Comparison Tables](https://www.nngroup.com/articles/comparison-tables/) | Option columns + aligned attribute rows, scanning and differences, optional properties, reasonable small-set/mobile fallback | Select 2–4 repositories, fixed metric column, highlight differences | Do not force every time-series into a specs table |
| [RTINGS — Headphone Compare](https://www.rtings.com/headphones/tools/compare) | Main differences first, then comparable standardized test details | Start with credible metric differences, expand detail | Consumer scoring/aggregate ranks cannot be imposed on open-source projects |
| [Apple — Mac Compare](https://www.apple.com/mac/compare/) | Few choices, aligned specifications and scannable categories | Repositories as columns, activity/maintenance/Issue/PR as rows | Product spec comparison is not time-series analytics |
| [npmcharts](https://www.npmcharts.com/compare) | Several package trends share time axis, units and legible series labels | Repository trends on one time range with missing points explained | npm downloads ≠ GitHub commits |
| [EcosystemPulse — Comparisons](https://ecosystempulse.dev/comparisons.html) | Comparable public-source metrics | Conclusions only from shared scope/coverage | Never substitute npm numbers for real GitHub data |
| [Baymard — Comparison Examples](https://baymard.com/ecommerce-design-examples/39-comparison-tool) | Study useful and difficult selection/side-by-side patterns | Evaluate entity-picking friction and scan cost | Commerce conversion isn't the same goal |
| [GitHub Docs — Comparing Commits](https://docs.github.com/en/pull-requests/how-tos/commit-changes/comparing-commits) | Clear base/compare selection and diff context | Branch/commit comparisons only | Not a multi-repository trends layout |

NN/g's guidance often favors reducing comparisons to a small set (around 3–4 for dynamic tables). **This is a cognitive-load heuristic, not a hard maximum of four repositories.** More important: scannable standardized attributes, removable items, emphasized differences and access to details. Many columns need a deliberate mobile strategy—switch entities, compare two at once or allow meaningful horizontal scroll.

## Gate C0 — Define the decision before selecting a layout

Establish `decision_question` (what user wants to learn), `entities`, `metrics`, `period`, `context` (comparability across objects) and `output` (how conclusion is supported). Do not place every aggregate, series, collaboration detail and tutorial on the same screen.

| Question | Composition | Suggested use |
| --- | --- | --- |
| Which of A and B fits? | Side-by-side table + meaningful differences | Specs, maintenance, selection; comparable discrete attributes |
| Which project is more active/how do they evolve? | Shared time series + metric matrix | 2–4 repository activity, contributors and issue/PR trends |
| Different scale; how compare pace? | Switch absolute and **explicitly labeled** normalized/per-contributor values | Different repo size and contributor populations |
| Recent state only | Compact metrics, optional charts on disclosure | First-screen decision and frequent switching |
| Comparing reports | Align method, sample n and coverage; preserve incompatibility warning | Research; no invented composite “winner” |

## Gate C1 — Optional multi-object comparison structure

1. **Page header:** Direct “Compare Projects” + one actual decision goal line, such as “Compare commit and collaboration trends over the same time interval,” never generic slogan.
2. **Selected object strip:** 2–4 removable/replacable repository chips in the main content, stable order/colors matching the legend. With 7+ entities use search/Popover/Drawer instead of dedicating one-third of page to permanent selector.
3. **Compact differences:** Choose one primary comparative target and show only 2–3 **genuinely comparable** deltas. If insufficient sample, say “Not comparable/No data”—never fabricate leaders.
4. **One main trend:** Shared X-axis window, aggregation and unit. Every selected object has a real series **or an explicit coverage/no-data state in legend**. For three selected and only one available series, identify the other two as missing, hidden or failed rather than implying all appeared.
5. **Metric table:** Repositories as columns; rows include comparable measures (full weeks, Issue P50, PR P50, coverage). Highlight differences carefully; never rank data from incompatible windows or sample sizes. `null` displays dash/No data, **never 0**.
6. **Optional drilldown:** Link metric/entity to detail; CSV exports include ID, metric, unit, window, n/coverage. Put advanced methodology in discoverable details, not an empty oversized Card.
7. **Empty/error:** With fewer than two repositories, emphasize selecting an object instead of drawing a bogus single-series comparison; identify failures/partial collection/timeouts by entity.
8. **Width and scroll:** Strip, chart and matrix share content edges; full vertical reachability and fixed-footer clearance. Check legends/headers/plot/labels under v6.9 and v6.10.

## Gate C2 — Data contract: truth outranks three colored lines

Record in `examples/comparison-contract-demo.json`:

- `selected_entity_ids` must correspond **one-to-one** with `series[].entity_id`; if observations are absent, explicitly mark `no_data`. **Do not synthesize a nonexistent line just to populate legend.**
- Every `series[].points[].bucket` belongs to common `time_buckets` with consistent unit/granularity/window. Missing buckets use `null` and `missing_reason`, not filled zeros.
- Check each entity's coverage window; uncovered intervals cannot be zero or masquerade as complete.
- Each discrete metric gives `unit`, `direction`, `sample_size`, `coverage_status`. Deltas, ranks or percentages only when definitions are actually comparable.
- A screenshot with three selected objects and one visible line is not proof a multi-object comparison has been completed.

## Gate C3 — Chart interior alignment and label collisions

**Outer Cards aligning is just the first layer.** Review Chart Header, Plot Region, Axis/Legend/Labels and Footnote separately:

1. For comparable neighboring charts, plot top/bottom baselines should be traceable. Different chart kinds (bar vs scatter) may legitimately use different plot height when explained and labels do not compete. Equal outer Card height cannot disguise whitespace/axis drift.
2. Date tick format, bucket count and time window should match for directly compared line/bar plots. If not, label “not directly comparable point by point.” Different Y-axis units do not need identical scale.
3. **Text/data label collision:** Overlapping labels, numbers clipped near edges or multiple nearby values stacking at one coordinate must be repaired. Alternate placement, smart layout, key extrema only, tooltips or plot padding; do not blindly remove all numeric labels.
4. Legend must correspond to actual visible/available or explicitly unavailable objects. Light/dark series colors distinguishable; interactive charts support keyboard toggling.
5. Optional DOM annotations `data-mf-chart-group`, `data-mf-chart-plot`, `data-mf-chart-label` allow limited runtime heuristics. **Canvas chart text often cannot be inspected through DOM geometry**; review chart-engine native layout features, screenshots and Tooltips. No markup means no claim of automated inspection pass.
6. Abbreviations may be valid, but two “85 days” labels must not overlap; unit/sample counts must stay legible.

## Gate C4 — Real browser and data regressions

**Static plan:** `python3 scripts/validate_comparison_contract.py examples/comparison-contract-demo.json --repository` checks synthetic selection/series/window/missing/matrix consistency, **not actual ECharts visual output**.

**Browser option:** `node scripts/audit_comparison_ui.mjs --url http://127.0.0.1:5173/compare --out ./compare-audit`. It provides first/full-page captures and geometry/label collision candidates. If no annotated plot, report `NOT AUDITED`, not invented PASS. On the *real application* check relevant 1440×900 / 1280×720 / 390×844 desktop, low-height and mobile views (as supported):
- Selection changes update legend, series, table and difference summary together.
- Each selected object has a discoverable data state, including no data.
- Matrix rows align same metric; mobile can still compare corresponding values.
- Switching 30/90/180 days updates all views with clear coverage.
- Without real samples, no manufactured “winner.”
- Labels don't collide/clip; final rows/actions reachable through scroll.

v6.8 curates content, v6.9 protects grids/scroll, and v6.10 governs **multi-object comparability, plot alignment and data correctness**. Do not rebuild comparison as four KPI Cards + two huge charts + empty methodology Card. User-approved theme/density remains authoritative.
