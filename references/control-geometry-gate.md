# Control Geometry Gate — Never Crush Action Labels into Vertical Characters

Applies to all Web controls: Buttons, filter Tabs, state labels, compact navigation, menu items, pagination, toolbars and table row actions. Includes Chinese, English, mixed-language and RTL UI. **When space runs out, reorganize the layout or actions before wrapping a short label character-by-character, squeezing it or clipping it.**

## 1. Decide whether the text is divisible

| Control text role | Default behavior | Legitimate exception |
| --- | --- | --- |
| **Atomic short label** (View details / Retry / Save, short Tab/Badge/status/unit) | Treat phrase as one visual unit; no character-by-character break. Preserve clickable target and icon gap. | Genuine vertical writing system, deliberately designed two-line large CTA or explicitly approved layout |
| **Semantic multiline label** (long field option, paragraph-length Card heading/supporting copy) | Wrap at meaningful phrase/paragraph boundaries with proper leading, rather than overflowing to force one line | Legally required verbatim presentation follows accessibility rules |
| **Content** (table description, error explanation, prose, file/repo name, long path) | Wrap/truncate in content column, with a route to the complete value | Identifiers/code and data tables may use discoverable local scrolling |

**Important:** Apply `nowrap` by default **only to short atomic control labels**, not every string on the site. Global nowrap creates horizontal overflow and lost content. Numbers and units may need grouping; decide meaningful wrap points based on actual business semantics. Test dynamic fonts, CJK and RTL.

## 2. Parent layouts own adequate control space

Diagnose in this order:

1. Inspect local `width`, `max-width`, percentage columns, `grid-template-columns`, `flex-shrink` and `min-width`. A short label wrapped vertically usually indicates the **parent inline-size budget is too narrow**, not an inherently wrong font.
2. Measure the atomic label's natural width + horizontal padding + icon + gap + focus outline as a **space budget** for the chosen control variant. Never blindly shrink fonts to 10px.
3. Desktop inline action groups should **reflow as complete actions**. If they fit, show them together; otherwise wrap the entire Button, use a clear primary action plus an accessible labeled overflow menu, move actions into an expanded row/detail, or reflow the record at a breakpoint.
4. Preserve discoverability and access: do not hide Retry in unreachable hover-only UI; icon-only buttons need accessible names; dangerous actions still need suitable confirmation.
5. Check horizontal/vertical overflow and fixed-bar occlusion. **Do not “fix wrapping” with `overflow:hidden` that clips controls or lets them run offscreen.**

## 3. Portable CSS approach — illustrative, never mandatory everywhere

```css
/* Only short atomic labels: do not copy for long options */
.ui-action {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-control-gap, .375rem);
  white-space: nowrap;
  flex: none;                  /* Keep atomic action from being crushed */
  inline-size: max-content;    /* Pair with an adaptive container */
  max-inline-size: 100%;       /* Do not push outside the viewport */
}
.action-group {
  display: flex;
  flex-wrap: wrap;             /* Wrap whole Buttons, not their characters */
  gap: var(--space-action-gap, .5rem);
}
.data-row {
  display: grid;
  grid-template-columns: minmax(0, 2fr) minmax(0, 1fr) max-content;
}
/* When the entire row no longer fits, change the row layout */
@container (max-width: 38rem) {
  .data-row { grid-template-columns: minmax(0, 1fr); }
  .action-group { justify-content: flex-start; }
}
```

**Do not overapply this example.** The app may use CSS Grid/Flex, `table` with action menus, container queries or explicit breakpoints. If `inline-size:max-content` still exceeds a tiny viewport, change labels/patterns, allow meaningful multiline content or accessible scrolling; never insist on impossible no-overflow geometry. A fixed `table-layout:fixed` action column must fit controls; compress/wrap middle content columns or move actions out of a narrow cell.

Relevant CSS behavior:
- MDN white-space: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space
- MDN flex-shrink: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink
- MDN flex-wrap: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap

## 4. Gate D — Test actual wrapping and reachability, not only source

- **Short labels:** Use actual browser text Range/line rectangles and control bounding boxes. Even a `white-space:nowrap` declaration cannot rule out parent fixed widths, flex shrink, clipping or offscreen content.
- **Geometry:** Labels, icons, focus outline and action columns remain visible; touch/click areas usable; Tabs/toolbars selected and keyboard focus reachable.
- **Stress states:** Appropriate wide/narrow widths (especially 1280, 390 and 320px), 200% type scaling, at least one long Chinese and English example, several actions in a row, extra actions during error states, light/dark modes and RTL where supported.
- **Responsive fallback:** Test whole-Button wrapping, overflow menu, row reflow or local table scrolling. A label must not become characters stacked as “V/i/e/w”.
- **Evidence:** If Canvas/ShadowRoot or required DOM markers are inaccessible, report `NOT AUDITED`. A source CSS rule is **not** a browser PASS. Optionally mark `data-mf-atomic-control` on control roots and `data-mf-control-label` on inner labels for geometry tests; these attributes need not be permanently added to every MauForma target product.

**The difficult question is how layout degrades in narrow spaces**, not whether one rounded Button looks attractive. Pair with `references/surface-architecture-gate.md`, `references/grid-alignment-and-viewport-safety.md` and `references/component-first.md`.
