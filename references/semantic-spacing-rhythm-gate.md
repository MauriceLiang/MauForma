# Semantic Spacing & Spatial Rhythm Gate — Choose Gaps From Relationships (v6.16)

Applies across all Web modes, frameworks and styles. **Layout alignment ≠ correct spacing**: two chart Cards may share baselines and column edges yet touch at `row-gap:0`, forming an unintended featureless surface. More radius, shadows or internal Card padding cannot repair incorrect group-to-group relationships.

## v6.20 — Discover inherited bad spacing before protecting good spacing

If two independent Sections already touch, v6.19 “preserve existing spacing” is **not** evidence that the arrangement is good. Vague polish must first follow `references/proactive-visual-defect-discovery-gate.md`: inspect the real UI using baseline-free `scripts/audit_existing_visual_defects.mjs`, including ordinary Block Flow, Grid/Flex and simple wrappers. Fix inherited mistakes; use before/after to protect **already good** gaps. Scanners mostly identify obvious framed panels; open compositions/Canvas/complex nesting still need visual review.

## v6.19 — Do not unintentionally collapse inherited spacing

The v6.16 explicit contract depends on real DOM annotations. Existing products also require `references/spacing-regression-protection-gate.md`: record visible **before** relationships, preserve normal gaps between independent modules and compare **after**. Without annotations, `scripts/audit_panel_spacing.mjs` can heuristically flag Grid/Flex Card/Panel zero gaps or large shrinkage. “More compact” is not permission for `row-gap:0`. A synthetic demo pass does not prove a real page passed; report areas the scanner cannot cover.

## Gate SR0 — Spatial Relationship Map before choosing numbers

For meaningful visible areas, define parent layout, neighboring objects and reading order, then classify one relationship:

| Role | Decision question | Examples | Spacing approach |
| --- | --- | --- | --- |
| **inside** | Is A a label/unit/help/body belonging to B? | Heading+description; chart title+plot; field+help | Close and perceptibly grouped; coordinate padding and inner gaps |
| **peer** | Are A and B coequal items of one grid/function group? | Two chart Cards, settings choices, works gallery | Coherent row/column gaps; nesting must not randomly zero one axis |
| **section** | Are they separate tasks/topics/chapters? | Metrics → charts → data quality → limitations | Clear inter-section separation, usually more than inner copy gaps; background/borders may support without piling on |
| **connected** | Are they deliberately one continuous structure/surface? | Tab bar+Panel, table header+rows, timeline, contiguous toolbar | **Zero gap/shared edge permitted** when structural, border or interaction semantics justify it |
| **anchored** | Is overlay/media/badge genuinely positioned relative to a trigger? | Popover, Tooltip, image label | Positioned overlap permitted; ordinary sibling gap rules don't apply |
| **editorial / expressive** | Does irregular spacing serve a meaningful reading/composition strategy? | Magazine, portfolio, full-bleed Hero | Asymmetry allowed if intent can be explained; “random whitespace feels designed” is insufficient |

**Map relationships before picking pixels.** Dense workbenches and spacious brand pages are both allowed. Never inflate all gaps to 32px merely to eliminate warnings. Connecting components is not inherently wrong; **unjustified touching** is the issue.

## Gate SR1 — Five spacing roles, not fixed site-wide pixels

Map semantic tokens to the project's inherited spacing scale:

- `space.inline`: icon/label, Badge internals, number/unit, coordinated with control typography and hit targets.
- `space.inside`: heading/help, chart title/plot, paragraphs/fields inside a Card; tune to optical weight/content height.
- `space.peer`: Cards, plots, fields or objects within one collection; horizontal **and vertical** gaps should be intentionally consistent or explicitly variant.
- `space.section`: independent chapters, topics and workflows; generally distinguishable from local microspacing.
- `space.page`: start rhythm between PageHeader/body, page safe area and fixed elements.

**These tokens need not all have different values or follow an 8px grid.** Dense/connected components may share values with justification. Primary structural gaps belong to parent `gap/row-gap/column-gap`, Stack/Space/layout tokens—not arbitrary margins per Card. Padding and outside gaps are separate responsibilities.

Possible **non-mandatory** starting progression: 4/8/12/20/28 for a compact data site, larger for docs/marketing. Real CJK font metrics, chart size, control height, viewport and content density may change it. Relative rhythm matters more than a constant; **“section must equal twice inside” is not a law**.

## Gate SR2 — Spacing rhythm and optical review

1. **Vertical:** Is there deliberate rhythm across page title/help, summary, chart rows and data limitations? Independent panels must not fuse into a giant blank sheet through `row-gap:0` or joined borders.
2. **Horizontal:** Are peer Card gutters, toolbar/main plot boundaries and columns aligned? A nonzero `column-gap` never proves `row-gap` is adequate.
3. **Visual weight:** Large charts, saturated plots, photography and huge headings need appropriate breathing room. Related chart captions/labels must not sit farther from their plot than from the next unrelated section.
4. **Borders/backgrounds:** Two white Cards with pale edges may visually fuse even with nonzero physical space. Adjust parent gap, remove redundant borders or change surface separation; prioritise information structure over extra shadows.
5. **Modes and exceptions:** Dashboards may be tight but not accidentally fused. Editorial prose may need fewer frames. E-commerce peer product gaps can be compact; key product details/checkout may need more air. Portfolio asymmetry can be an artistic decision.
6. **Dynamic states:** Empty/loading/error, disclosures, Tabs, breakpoints, sticky bars and text zoom must preserve semantic relations. **Do not force empty/error states into giant fixed heights.**
7. **Optical adjustment:** Start from tokens/geometry and adjust for text/image optical bounds. Never use negative margins to conceal genuine misalignment or destroy Grid relationships.

## Gate SR3 — Portable example, numerical values are illustrative

```css
/* Parent layout owns relationships; use actual project tokens */
.research-page {
  --space-inside: 0.5rem;
  --space-peer: 0.875rem;
  --space-section: 1.25rem;
  display: grid;
  gap: var(--space-section);
}
.research-page__chart-row {
  display: grid;
  grid-template-columns: minmax(0, 3fr) minmax(0, 2fr);
  gap: var(--space-peer); /* Both axes */
  min-width: 0;
}
.research-page__panel {
  min-width: 0;
  /* Card's own padding is not its gap to the next Card */
}
.research-page__heading {
  margin-block-end: var(--space-inside);
}
@media (max-width: 48rem) {
  .research-page__chart-row { grid-template-columns: minmax(0, 1fr); }
}
/* A deliberate contiguous Tab+Panel may use connected mode and zero gap */
```

Avoid un-gapped flex columns, `row-gap:0` with `column-gap:12px`, brittle `:last-child` margins/absolute positioning, blanket Card `margin-bottom` that double-counts Grid gaps, padding pretending to be external space, and compressing every gap just to force everything above the fold.

## Gate SR4 — Browser geometry **and** perceptual QA, both required

1. **Design evidence:** Record important independent Section, peer and title-within-panel relationships and their token roles. State why connected/overlap is intentional. A narrow fix reviews only affected relationships; no new interview needed.
2. **Browser:** Candidate viewports may include 1280×720, 1440×900, 390×844 and 320px width, but actual supported user devices decide. Measure boundaries and watch for overlap/touching. When a two-column row stacks vertically, **the gap must not silently become zero**.
3. **Rhythm:** Review peer consistency, section-vs-inside distinction and vertical spacing owned by the parent. Intentional connected regions may touch when declared in the contract.
4. **Full page/scroll end:** Include first screen, below charts, last content item and clearance for fixed bars. Natural scrolling is not a bug. Global `overflow:hidden` cannot hide a defect.
5. **Contract vs runtime geometry:** `scripts/validate_spacing_rhythm.py --repository` verifies general fixtures; `scripts/audit_spacing_rhythm.mjs --url ... --contract ...` audits explicitly marked regions. Only marked **real pages** with relevant contracts permit limited geometric conclusions. No scanner proves “premium art direction.” Synthetic `assets/spacing-rhythm-lab.html` and `tests/spacing_rhythm_browser_smoke.mjs` deliberately include touching failures.
6. **Linked gates:** First ask `references/surface-architecture-gate.md` whether separate surfaces are appropriate; then `references/grid-alignment-and-viewport-safety.md` for row/column/scroll geometry, `references/perceptual-hierarchy-gate.md` for visual importance and `references/control-geometry-gate.md` to avoid squeezed actions.

## External principles and limits

- Carbon Spacing: Semantic tokens, grouping and hierarchy — https://www.carbondesignsystem.com/building-blocks/foundations/spacing/overview
- Atlassian Spacing: Proximity/grouping/rhythm with optical adjustment — https://atlassian.design/foundations/spacing

Their pixel values belong to **their design systems**, not universal MauForma requirements.
