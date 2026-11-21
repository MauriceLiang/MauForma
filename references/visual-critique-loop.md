# Screenshot Critique Loop — Recompose the Page, Not Just the Details

## Diagnose existing defects when asked for general polish

When users ask to refine/improve an interface, **proactively discover evidence-based defects** across spacing, hierarchy, components, icons/colors, interaction and responsive design. Inherited unrelated surfaces that already touch **do not become acceptable merely because the before/after diff is unchanged**. Optionally use scripts/audit_existing_visual_defects.mjs for unannotated Block/Grid/Flex panels. Recheck that problems were fixed while preserving already-correct spacing (proactive-visual-defect-discovery-gate.md). When browser/scanner access is absent, report **NOT AUDITED**; a passing Mock is not evidence.

Use the full loop for new sites, major redesigns and repeated "looks templated" feedback. One narrowly scoped focus color or Button defect does **not** force a complete redesign.

## Card/Panel edge-accent veto for new and inherited content

Inspect Card/Panel/Section rounded frames. **A thick colored ornamental bar touching, overlaying or merging into a rounded border fails**, including pseudo-elements, unilateral borders, gradients and inset shadows. Default to no bar. A meaningful short external marker may be separated visibly from an intact panel border. Existing components are not exempt. Verify after repair. Do not misclassify real focus, timeline and chart data (surface-edge-accent-gate.md Gate S0).

## Evidence first

Where available, capture actual running target pages at desktop and narrow **supported** viewports. Inspect actual MASTER.md, page overrides, composition-brief.json, component states and confirmed user direction. Without browser access, analyze supplied images/code, explicitly labeling interactions, breakpoints and data states **untested**. Static screenshots cannot prove functionality.

| Defect class | Observed symptom | Correct action |
| --- | --- | --- |
| Structure / IA | Main job missing, large irrelevant chart, vital content buried far down | **Recompose information**, not recolor |
| Hierarchy | Hero/illustration outranks business data; huge headings; faint CTA | Reallocate space/type/position or remove unnecessary regions |
| Palette | Several bright panels compete without distinct roles | Define semantic roles, reduce competition, then tune colors |
| Rhythm | Crowded top and empty bottom, nested Cards or four identical oversized KPIs | Reconsider Grid, grouping, container count and whitespace |
| Detail / components | Buttons, focus, radii and icons differ | Repair shared tokens/components and interactive states |
| Function / data state | Empty chart without loading/error/empty state, dead action, fake demo data | Fix real data/behavior before scoring visual craft |

## Three-part critique

### 1. Grayscale structural test

If possible inspect the page in grayscale or temporarily strip **decorative** gradients/shadows, without removing genuinely meaningful chart/status colors. Evaluate whether information remains recognizable: Can a user identify the object, important change and next step within three seconds? Is blank space tied to real data or state? Does the dominant visual area reflect the user's real task? Does whitespace separate meaningful sections or just imitate "premium" design?

### 2. Color responsibility test

Classify strong colors as brand/action, data series, state/warning, content media or decoration. Reconsider decoration that outweighs primary data; verify primary/secondary text, focus and status contrast. Backgrounds should support key content, not compete with it.

### 3. Recompose and validate

For structural problems, propose **at least one meaningfully different region arrangement or primary focal subject**. Apply composition-first-design.md, reuse shared components, and capture actual page results. Replacing a gradient Hero's blue-purple palette with monochrome while keeping the broken structure is **not** a structural fix.

## Mandatory review record

Include route/real task, screenshot source and viewport; confirmed/delegated design direction; first-look attention relative to task; area priorities and blank/loading/data states; **evidence and severity** across structure, hierarchy, palette, rhythm, function, detail; good inherited design to preserve and redundant decoration to remove; whether edits changed layout or only tokens/components; actual before/after images and responsive/state verification as **PASS / FAIL / NOT RUN**. Do not claim visual browser review with no actual screenshots.

## Rework conditions despite an otherwise good score

- An Operate page's decorative Hero/3D imagery outranks real tasks/data **without a legitimate business reason**.
- A large primary data region lacks an explicit empty/loading/error explanation.
- A dominant saturated decoration interferes with the primary task.
- A reported structural problem receives only palette/border changes but is claimed redesigned.

Decide from task and real evidence, **not** the presence of a linear-gradient property or particular HEX.

## Typography rework driven by screenshots

A synthetic example may combine brand suffix, duplicated page-category eyebrow, huge abstract H1, ornamental "01 / Overview" and another slogan heading, while KPI labels, chart ticks and sample limitations are nearly unreadable. Fix in this order: **delete/merge information-free words → assign PageTitle/Section/Metric/Chart roles → correct contrast and line height → verify 200% zoom in real screenshots**. Tweaking icons/radii/background is not typography repair.

**Exceptions:** Real breadcrumbs, approved brand subtitles, reading chapters and data sources must survive. A 10px CSS declaration alone does not condemn a screen; inspect actual typography, Canvas chart, zoom and task context. See semantic-copy-hygiene.md and typography-hierarchy.md.

## Diagnose palette as a connected page system

If sidebar and main area conflict, **do not adjust one sidebar HEX alone and claim success**. Inventory color across **Sidebar/Topbar/Main/Card/Chart**, examining temperature, lightness and source of accents; read sidebar-color-reference-cases.md for transferable mechanisms. Compare **2–3 distinct whole-page schemes** for user selection.

Preserve explicitly specified black/white/purple/green or **exact user HEX**. Build readable semantic tokens around them; do not revert to blue because of aesthetics. Adjust supporting colors or explain genuine contrast conflicts. Unconfirmed new suggestions remain **pending** and cannot overwrite approved themes. Compare screenshots including real sidebar/main boundaries; after approval, verify narrow layout and charts.

## Navigation is part of composition

When navigation consumes space, duplicates entry points top/side/bottom or compresses mobile content, first revisit IA (global/local/tabs/actions), real destination count and device patterns, not just radius. A sidebar + bottom bar may be **responsive transformation across device sizes**, or **separate navigation/actions on the same screen**; distinguish them. Evidence should include relevant desktop/mobile layout, Drawer open/close, scrolling and fixed occlusion.

## Content overload precedes whitespace tuning

Distinguish **Content overload** (tutorial, feature directory and CTAs all on overview), **Surface overload** (every paragraph has its own Card), **Density mismatch** (overview crowded while analysis detail is mostly Hero), **False whitespace** (min-height creates empty space without removing unnecessary content). Verify task and first/return visit state → defer/remove unnecessary material → ensure needed content remains reachable → then adjust macro/meso/micro spacing and type. Review overview and detail separately; preserve real statuses and sources (page-density-and-content-priority.md).

## Independent alignment and scroll-end passes

On analytical pages, before tuning color/eyebrows/radii mark main content bounds, Card column lines and row tops. When separate left/right column stacks unintentionally produce **Masonry**, use shared Grid rows as a starting point for comparison and allow full-width key charts where justified.

A screenshot stopping at the window bottom cannot establish a scroll bug. **Scroll to the actual end** to inspect final record, action, chart axis/footnote and fixed bar. Hidden final content or horizontal overflow requires repair; hiding overflow is not a fix. See grid-alignment-and-viewport-safety.md.

## Chart interiors and comparison roles

For peer charts inspect **Plot Area**, X-axis baseline and data-label spacing/collisions—not only outer Card/Grid alignment. Equal container height can hide mismatched units, ticks and plot regions. On comparisons verify selected entities, legends, plotted series, table columns and useful first-screen differences. A permanent filter Sidebar plus large metric-definition Card does not automatically create a usable comparison (comparison-page-design.md; chart-interior-alignment.md).

## Task Center: having all features is not task efficiency

If non-actionable status counters become giant Cards, wide task rows repeat descriptions, or actionable errors/retries are buried among completed jobs, classify as **Run Monitor information hierarchy failure**. Recompose into actionable status filters, scannable records and on-demand detail. Verify true progress and legitimate actions; shrinking Card heights alone is insufficient. Screenshots cannot prove retry, logs or API outcomes: the target needs real browser/E2E checks (run-monitor-case.md).

## Original-source cross-reference parity

Navigation structure criteria also rely on references/navigation-architecture.md; this reference is about scope and route ownership, not permission to redesign existing navigation.
