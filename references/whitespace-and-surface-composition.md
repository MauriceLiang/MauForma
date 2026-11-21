# Whitespace & Surface Restraint — Space Should Express Relationships, Not Emptiness

## v6.19 — Preserve by default

When a user asks only to polish the aesthetics/density of an existing UI, **do not independently erase outside gaps between already separate Sections/peers**. Parent Grid/Stack gaps and Card padding are different responsibilities. Before attaching the next row to the previous one, reduce meaningless copy, duplicate panels and flawed information structure. `references/spacing-regression-protection-gate.md` is the protection gate; real-browser before/after and `scripts/audit_panel_spacing.mjs` supply evidence—not a subjective observation that code looks compact.

## v6.16 — Universal Spatial Relationship Map and rhythm acceptance

Earlier macro/meso/micro guidance described “larger between groups, smaller inside” but did not require checking **real inter-module distance**. First read `references/semantic-spacing-rhythm-gate.md`, assign spacing tokens to `inside/peer/section/connected/anchored` relationships, and let the parent Grid/Stack own gaps. Card padding cannot stand in for section gaps. Inspect same-row `column-gap`, next-row `row-gap` and rhythm when the layout stacks on narrow screens. Touching Cards are not always bad: Tab/Panel and table header/body may intentionally share an edge. Two unrelated charts/data blocks accidentally fused by `row-gap:0` must be repaired.

Use real browser screenshots to assess visual weight/optical whitespace. `scripts/audit_spacing_rhythm.mjs` with explicit `data-mf-space-id` and project contracts can inspect limited geometry. A static spacing table does not prove beauty. Repair structure, parent gap and information grouping **before** adding `margin` to every Card; blanket margins break nested/peer/mobile arrangements.

## Avoid

- Forcing huge top/bottom margins onto every page “for premium feel,” pushing the main action below the first screen.
- A page title and a line of description, followed by a huge wrapper containing three explanatory feature Cards, plus another Card duplicating navigation.
- Putting a **1px border** around every small heading, KPI and action and calling it a coherent Card system confuses repeated decoration with actual hierarchy.
- Shrinking body text to 12px and help to 10px to fit more. Remove low-value material instead of shrinking real task text.
- Treating whitespace as a rigid `min-height:400px` filler or empty first screen without usable primary content.
- Editing only Card padding while preserving redundant content and claiming density was optimized.

## Meaningful whitespace at three scales

**Macro:** Stable separation among distinct tasks; the first viewport should have a clear primary task region, not several equal visual competitors. Welcome/brand pages may be airy; analysis/admin can be denser without losing section relationships.

**Meso:** Related heading, explanation, input, action and state sit close within one workflow. A title should be nearer to **its own content** than to an unrelated sibling Section.

**Micro:** Icons, labels, Badges and rows use shared tokens for readable text and usable targets. Respect approved theme/type, visible focus and contrast. Dense tables may use compact measurements but never near-invisible text or untappable controls.

These are **not fixed universal 8/16/24/32/48 px requirements**. Ratios should cohere within the real design system, adapting to font, page mode, viewport and content.

## v6.13 — Surface choice precedes polishing a box

Earlier Surface Necessity checked whether a border was useful, but did not compare the **whole page's information organization**. For real pages/major redesigns, run `references/surface-architecture-gate.md`: continuous records may become flat collections, independently scoped modules may use one Panel, products/works may use Cards, while reading/immersive UI needs another spatial grammar. **No mandatory global Card deletion.** Then run `references/control-geometry-gate.md` for narrow controls so labels do not stack character by character to preserve an outer frame.

## Surface Necessity Test

For each Panel/Card/outline ask:

1. Does it define a distinct interactive object, a coherent data group, a genuine state or a useful visual boundary?
2. Without border/background, would spacing and alignment still convey the relationship? If yes, **prefer removing the outer surface** while keeping necessary inner structure.
3. Are nested Cards merely two decorative layers? Merge or replace with flat list rows.
4. Do three feature Cards duplicate existing navigation? Delete the row or replace with one actually useful secondary entry.
5. Is a giant homepage Card genuinely needed or only filling the viewport? A library having a `Card` component does not justify wrapping everything.

**Independent interactive objects, multi-state modules and analysis charts may validly use Cards.** The rule opposes pointless wrappers, not Cards themselves.

## Suitable spatial structures

### Overview — low to medium density

- Clear top title with necessary context, not a second slogan.
- Main object/entry such as current repository plus a single primary action; secondary actions as links/quiet Buttons.
- Limited real status/recent work only when it meaningfully shortens the next action.
- Tutorials/all-feature lists may be conditional, deferred to nav/help or detailed routes.
- Section whitespace signals where the user is; no need to fill the entire screen vertically.

### Analytics detail — medium to high density

- Object, time window and filters stay near relevant charts and metrics.
- Important numbers, plots and records can use a comparable shared grid.
- Chart titles, axes, units and limits stay legible without nested Card shells.
- Missing data gets explicit empty/loading/error states, never fabricated trends for prettier charts.

### Brand showcase — may be airy

- Authentic quality media can warrant a giant Hero, whitespace and experimental type. Essential comparison, price and conversion details remain readable and discoverable.
- Admin-review limits on number of Cards do **not** automatically apply to brand sites.

## Quality checks

- **Grayscale/no-border test:** Temporarily remove shadows/gradients/unnecessary borders. Do task order and primary action still make sense?
- **Content-removal test:** Would deleting one whole duplicate explanation make the current task clearer? Defer/remove the block instead of merely changing its CSS.
- **Spacing-hierarchy check:** Inside a group is generally closer than between groups; are equal-weight blocks truly equally important?
- **User states:** Compare new, returning, populated and empty/error UI. Each may need different whitespace.
- **Real screenshot evidence:** Check actual supported desktop/mobile, 200% text zoom, keyboard focus and light/dark. If not run, mark `NOT RUN`.

Related: `references/page-density-and-content-priority.md`, `references/typography-hierarchy.md`, `references/semantic-copy-hygiene.md`.

## v6.9 — Spacing hierarchy does not excuse arbitrary column misalignment

Macro/meso/micro gaps still need **shared Grid lines and row starts**. A primary plot can be wider and peer Cards can differ in height, but two independent column Stacks can make the second row misalign like a masonry flow. If row alignment produces huge wasted space, use a full-width main plot or rethink the data groups—not invisible filler Cards. End padding allows natural scrolling to the last item, **not** a mandate to make all content fit the first screen. See `references/grid-alignment-and-viewport-safety.md`.

## v6.11 — Whitespace in task lists should support scanning

In high-frequency run monitors, empty area alone is not sophistication. If a huge status counter Card has no separate analytical purpose, turn it into clickable compact filters near the list. Let object, state, stage, time and action form a scannable column grid, not paragraph-heavy rows with decorative icons. Use space to distinguish tasks and exceptional groups, not repeat “progress percent unknown” on every record. On mobile, reflow into reasonable two-line/layered task cards instead of shrinking a desktop five-column table to microscopic text. See `references/task-center-run-monitor-design.md`.
