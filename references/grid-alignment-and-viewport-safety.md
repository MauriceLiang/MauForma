# Grid & Viewport Integrity — Shared Alignment and Scroll-End Safety (v6.9)

> Synthetic failure: two independently stacked columns may cause second-row misalignment, while a fixed bottom action bar may hide content. The former needs layout evidence; for the latter, **actually scroll to the bottom in the browser**. A single screenshot cannot prove an obstruction.

## Grid alignment and spatial rhythm are separate checks

A satisfactory horizontal gutter does not authorize zero vertical `row-gap` across rows. Record the pre-edit baseline of independent modules on existing pages and follow `references/spacing-regression-protection-gate.md`, comparing the same route, viewport, font size and data. `scripts/audit_panel_spacing.mjs` can find likely touching panels without DOM annotations; intentionally connected Tab/Panel remains an exception. **Insufficient scan coverage is not a pass**.

## Gate LO — Layout can align while compact labels still overlap

Large-panel gutters, shared Grid lines and global horizontal overflow checks cannot detect a short Badge, status label or attribution pill painting across a neighboring tag. **All new and polished Web interfaces** must review independent visible labels, text and controls for surface-over-surface, text-over-text and text-under-foreign-surface collisions, plus real reading order and visual legibility. Reflow or stack content rather than disguising the collision with `z-index`, clipping or changed colors. Use `references/visual-overlap-and-legibility-gate.md`; the real-browser `scripts/audit_label_collisions.mjs` is also integrated into existing-defect and rendered-layout audits. Its coverage is not a full aesthetic judgment.

## Alignment may pass while gaps fail

Perfect shared row starts/column edges **do not prove inside/peer/section spacing is correct**. Two chart Cards can have a good `column-gap` but `row-gap:0` to the following full-width section, accidentally merging surfaces. New and major redesigns must also execute `references/semantic-spacing-rhythm-gate.md` after Gate G1: distinguish independent chapters from genuinely connected structures, verify roles/row-column rhythm and gap when a layout becomes one column. Scroll-end safety padding is **not** section spacing and cannot replace it.

## Core distinction

**Asymmetry ≠ misalignment.** Data dashboards favor shared column and row tracks, Card edges and comparable plot/axis/header baselines. Different sizes/offsets must have a task/information rationale. Photo masonry and creative editorial layouts may be exceptions; charts, statistics and release histories **do not default to Masonry**.

## Gate G1 — Define an alignment contract before CSS

1. **Shared content edges:** Sidebar/Main/Topbar content regions have a traceable origin. PageHeader, Filters, Sections and charts share main left/right grid lines. Do not give each Card random left margin.
2. **Row starts for peers:** Two charts in one row share the top. Even if their heights differ, the next row begins at one shared next row start. Do not stack the left column independently of the right, creating staggered second rows.
3. **Shared row/column structure:** Prefer a single CSS Grid/shared tracks. 8:4 or 7:5 ratios and full-span Heroes are valid; **neither 50:50 nor equal Card heights are compulsory**. Different widths need a content rationale, not random grids on every row.
4. **Interior chart alignment:** Compare chart titles, units, time ranges, legends and axis labels. Share plot padding/tokens where helpful. **Never fake a common data range or force identical Y axes merely to align surfaces.**
5. **Whitespace is not artificial filler:** When one region is much taller/shorter, reconsider spanning, duplicate charts or a full-width primary plot before stretching rows. `min-height:600px` and fake placeholder Cards are not fixes.
6. **Documented exceptions:** Creative galleries can use Masonry, timelines can stagger, and nested navigation may scroll independently. A deliberately offset professional workspace needs an explanation of how misalignment benefits understanding, not “artistic feeling.”

## Gate G2 — Two valid CSS structures

### A. Shared rows, not independently stacked columns — comparison

```css
.release-dashboard {
  display: grid;
  grid-template-columns: minmax(0, 3fr) minmax(0, 2fr);
  grid-template-areas:
    "timeline intervals"
    "frequency releases";
  gap: var(--space-section, 20px);
  align-items: start;
}
.release-dashboard > * { min-width: 0; }
.timeline { grid-area: timeline; }
.intervals { grid-area: intervals; }
.frequency { grid-area: frequency; }
.releases { grid-area: releases; }
@media (max-width: 900px) {
  .release-dashboard {
    grid-template-columns: minmax(0, 1fr);
    grid-template-areas:
      "timeline" "intervals" "frequency" "releases";
  }
}
```

The second row starts below the taller first-row Card, preserving natural vertical scrolling. This **does not** make all Cards equal-height and may still leave empty area inside row one. If height differences are severe, redesign information hierarchy instead of filling the blank.

### B. Full-width primary chart — when priorities differ

```css
.release-dashboard {
  display: grid;
  grid-template-columns: repeat(12, minmax(0, 1fr));
  gap: var(--space-section, 20px);
}
.timeline { grid-column: 1 / -1; }
.frequency { grid-column: span 7; }
.releases { grid-column: span 5; }
@media (max-width: 900px) {
  .release-dashboard > * { grid-column: 1 / -1; }
}
```

If “interval sequence” and “adjacent release interval” are repetitive for the real task, apply the v6.8 content-reduction test **before** deciding both charts must remain.

## Gate V1 — Scroll safety does not mean everything fits the first screen

**Normal:** Content taller than the viewport scrolls naturally and can be viewed fully. This is **not an overflow bug**.

**Defects:**

- Last actionable row or chart note hidden by `overflow:hidden`, clipped fixed-size container or `clip-path`, **without a way to scroll there**.
- Fixed/floating bottom bar covers the last row/Buttons even at maximum scroll.
- Content runs into the viewport edge, with no appropriate bottom spacing or safe-area room.
- Grid/Flex implicit minimum sizes expand the wrong container, disabling the main scroll area; `100vh` and mobile visual viewport disagree.
- Charts/tables overflow flexible tracks, creating unintended horizontal page scroll.

**Correct behavior:** The page scrolls to its final content in the window or **one clear main scroll owner**. A fixed bottom action bar requires correctly measured scroll-end clearance. Do not hide vertical overflow simultaneously in html/body and main. Fixed-height App Shells may need `min-height:0` and `overflow-y:auto` on the right owner.

### Natural document scrolling

```css
.app-shell { min-height: 100vh; min-height: 100dvh; }
.page-content {
  min-width: 0;
  padding-block-end: calc(var(--space-page-end, 32px) + env(safe-area-inset-bottom, 0px));
}
.chart-panel { min-width: 0; }
```

### Fixed-viewport App Shell with inner main scroll

```css
.app-shell {
  height: 100vh;
  height: 100dvh;
  display: grid;
  grid-template-rows: auto minmax(0, 1fr);
}
.app-body {
  min-height: 0;
  min-width: 0;
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
}
.main-scroll {
  min-height: 0;
  min-width: 0;
  overflow-y: auto;
  overflow-x: clip; /* Only when horizontal content is adapted and no overlays must escape */
  padding-block-end: calc(var(--space-page-end, 32px) + env(safe-area-inset-bottom, 0px));
}
.chart { width: 100%; max-width: 100%; min-width: 0; }
```

**Caution:** `overflow-x:clip` can also clip Popover/Tooltip outside the scroll area. Use Portals, correctly positioned layers or different component structure when necessary. Do **not** globally set `overflow:hidden`; test the architecture in the actual product.

### Fixed bottom bar clearance

Prefer a bar that participates in normal layout. Otherwise reserve end padding equal to its **actual measured height**, including safe-area. Keep `--bottom-action-height` synchronized to real dynamic bar height; never guess and hardcode. A browser/devtools toolbar outside the product DOM is not a product occlusion issue, though its effect on tested viewport should be recorded.

## Gate V2 — Browser acceptance requires scrolling to the very end

On the **actual Web app**, not only illustrative HTML, test:

- Applicable wide desktop, shorter laptop, narrow/mobile and actual user window sizes; e.g. 1440×900, 1280×720 and 390×844 are suggestions, **not required breakpoints**.
- At maximum vertical scroll, last Card border, Buttons, chart X-axis/legend, loading/error notes are fully visible, with reasonable trailing space. Content normally exceeding one screen is not a failure.
- Any fixed bar does not cover the final actionable/important content, which remains interactive at max scroll.
- Long copy/chart axes at 320/390 widths do not create unintended page-wide horizontal scroll. An intentional inner horizontal table scroller must be discoverable and accessible.
- With 200% text: no unreachable clipped material, hidden Buttons or occlusion.
- Capture the **final row and bottom of the actual scroll owner**. An initial-viewport screenshot alone is insufficient for PASS.

In an existing product, optionally run `scripts/audit_rendered_layout.mjs` (Playwright, see tool docs). It captures and reports geometry/scroll-owner/fixed-element candidates. **Heuristics can be wrong and cannot automatically establish visual quality or WCAG compliance.** `data-mf-grid-row`, `data-mf-grid-panel`, `data-mf-bottom-content`, `data-mf-fixed-bar` may mark specific regions but are not required application attributes.

## Gate V3 — Rejected “fixes”

- Only setting `height:100%` on Cards without shared parent Grid/tracks: second-row misalignment remains.
- Global `overflow:hidden` or `height:100vh` hiding truly unscrollable content while appearing compact.
- Shrinking charts, hiding X axes or deleting release records just to fit into 720px height.
- Replacing one natural scroll with multiple tiny nested scrollbars for no clear task reason.
- Invisible filler Cards or arbitrarily huge fixed Card heights.
- Declaring “no overflow” from screenshots **only at the top**.
- **Correct order:** inspect structure/content need → define Grid tracks → choose scroll owner → reserve end clearance → test real scroll-to-end at supported viewports.

## External references

- [IBM Carbon 2x Grid](https://www.carbondesignsystem.com/building-blocks/foundations/2x-grid/guidelines): coherent grids, track/gutter logic and multiple valid layouts.
- [MDN CSS minmax()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax): flexible track minimum constraints such as `minmax(0,1fr)`.
- [web.dev Sizing](https://web.dev/learn/css/sizing): `dvh` and dynamic browser viewport.
- [MDN Viewport concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/CSSOM_view/Viewport_concepts): layout vs visual viewport (zoom/keyboard).

No external standard requires “every pair of Cards must align within 0px.” MauForma thresholds are **review hints conditioned on actual information relationships**.

## Card borders passing does not mean Chart Plot passed

A synthetic-style release-analysis example may have aligned external Card borders but unequal interior plot areas and crowded X-axis/scatter/average labels. Chart pages also need **Chart Header, Plot, Axes, Legend and Footnote** review. Different chart types need not share height, scale or tick ranges; **real labels must not overlap, and time windows/units must be understandable**. Canvas content cannot be fully audited by generic DOM scanning. Inspect the real renderer and, when applicable, ECharts label layout; see `references/chart-interior-alignment.md`.
