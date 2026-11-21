# Surface Edge Accent Gate — No Decorative Color Bars Attached to Rounded Cards

> **Scope:** New pages, first-time design, polish of existing products, component refactors and visual reviews across all Web frameworks, product modes and light/dark themes. Applies to Card, Panel, Section, information blocks, showcase/data Cards and clickable entities. **This is not a requirement to add an accent rail to every block.**

## Gate S0 — Ban decorative colored vertical bars flush against surface borders

**Default: add no decorative edge rail.** Express hierarchy through real content, a complete normal border, background, whitespace and semantic copy. Remove inherited rails with no independent function. “Premium,” “techy” and “Cards need decoration” are not valid reasons to add one.

**Rejected rendered appearance:** A thick accent stripe runs down the Card/Panel edge, merges into its border with **zero gap**, or follows the rounded corner. **Implementation details do not override the visual decision**. Gate S0 rejects any final flush rail, including:

- Colorful `border-left`, `border-inline-start` or `border-image` replacing a single side with saturated color.
- `::before`/`::after` or a child strip drawn along the interior/exterior edge, possibly crossing round corners.
- `inset box-shadow`, linear/multiple backgrounds, masks, clipping, outlines or absolute positioning that recreate the same attached appearance.
- A technically separate DOM node whose negative margin, absolute positioning, overlap or container clip ultimately **touches or covers the surface border**.

Apply the **same standard to new and inherited UI**. Legacy code is not exempt; deleting one rail while generating another elsewhere, or making it paler/narrower but still attached, is not a repair.

## Two permitted surface strategies, in priority order

**A. No accent rail — preferred.** Keep a complete and coherent border, radius and padding. Differentiate content with titles, prose, meaningful status text, necessary icons or Badges.

**B. External short indicator for a justified semantic role — optional.** Place it **outside the complete Card/Panel border box**, controlled by the outer layout (or its pseudo-element), with an unambiguously **positive visible gap**. An illustrative start is **4–10 CSS px**, adjusted for page density, zoom and theme. It must not become a side of the Card border or wrap along its radius; the Card's own border/radius remain intact.

- Without a **clear status, hierarchy or navigation function**, prefer removal even when the strip is external; don't clone one on every Card.
- A short external track can use `grid`/`flex` and `gap`. Recheck that the gap stays positive under viewport changes, scrolling, state/interaction and zoom, without clipping content.
- The indicator is generally `aria-hidden="true"` and **cannot be the sole status cue**; preserve visible text, true status indicators and keyboard focus.
- Choose B only when requested by the user, inherited from a genuinely approved meaningful design, or needed by the actual interaction. Otherwise choose A.

### Synthetic invalid examples

```css
/* Incorrect: colored rail attaches to Card edge and rounded corners */
.panel { border-inline-start: 5px solid var(--accent); border-radius: 12px; }

/* Incorrect: pseudo-element or inset shadow does not change flush appearance */
.panel::before { content: ""; position: absolute; inset-inline-start: 0; inset-block: 0; width: 5px; background: var(--accent); }
.panel { box-shadow: inset 5px 0 0 var(--accent); }
```

### Synthetic valid structure

```html
<!-- Keep a justified external short marker only; otherwise render section.panel directly -->
<div class="panel-row">
  <span class="panel-indicator" aria-hidden="true"></span>
  <section class="panel">
    <h2>Analysis summary</h2>
    <p>Recent trends and scope.</p>
  </section>
</div>
```

```css
.panel-row { display: grid; grid-template-columns: 3px minmax(0, 1fr); gap: 8px; align-items: center; }
.panel-indicator { inline-size: 3px; block-size: 22px; border-radius: 3px; background: var(--semantic-accent); }
.panel { min-inline-size: 0; border: 1px solid var(--border); border-radius: 12px; padding: 16px; }
```

These are structural synthetic demos, **not required token values or layouts**. Actual marker length and styles depend on product purpose and target viewport.

## Boundaries — protect genuine semantics

- A **complete focus outline** (`focus-visible`/`outline`) is accessibility feedback, not a one-sided decorative rail. Never remove keyboard focus to eliminate a colored border.
- **Actual information/data graphics**, including chart bars, progress, timelines, quote blocks, row states and course step tracks, have separate semantic roles. But calling a thick attached Card stripe a “status” does not make it necessary. Prefer text, Badge, a distinct dot or genuinely external marker for simple status.
- **Sidebar selection items** follow `references/sidebar-selection-indicator-gate.md`: default to no colored rail; if genuinely needed, put it **outside** the item with a gap. This exception does not grant rails to every Card.
- **Brand colors are allowed** in Logos, Buttons, charts, media and genuine brand narrative. This gate prohibits **the flush colored edge-rail shape**, not branded color generally.

## Existing UI — discovery and repair loop

1. Before polish, inspect actual first viewport and affected Card/Panel/Section instances under relevant themes and visible states. Inspect **rendered appearance** plus `border-*`, `border-image`, pseudo-elements, gradients, inset shadows, absolute positioning and clip paths.
2. **Prefer deleting** flush rails. Convert only a demonstrably necessary semantic accent into a **short, genuinely separate external** marker. Fix at shared Card/Panel/token level instead of route-by-route CSS patches.
3. Compare **same route, viewport and data state** before/after. Verify complete surface edges, no flush stripe and readable states at supported wide/narrow widths, dark/light, 200% text zoom and hover/focus/selected.
4. If a flush rail remains, record `FOUND → UNFIXED` and repair before claiming visual optimization. Without actual browser evidence, report `STATIC CHECK` or `NOT TESTED`; passing authored docs/synthetic cases is not actual product verification.

**New builds** also perform steps 2–4: do not generate flush rails in the first implementation; verify actual rendered output, not only the changed diff or an old baseline.

## Review checklist

- [ ] Are Card/Panel/Section borders complete, without a thick colored edge or attached pseudo-element?
- [ ] Did the review include **inherited and new** instances, not just changed lines?
- [ ] Was no-rail A considered first? Is any external marker genuinely meaningful and not repeated on every Card?
- [ ] Is an external marker truly outside border box with a persistently visible positive gap?
- [ ] Did the implementation avoid shrink/fade/negative margin/overlay evasions?
- [ ] Are focus outlines, data status, numbering, timelines and accessibility semantics preserved?

Synthetic fixtures: `assets/surface-edge-accent-cases.json`. Static rule-contract validation: `scripts/validate_surface_edge_accent.py`. **These verify rule/fixture consistency, not real DOM, rendering or subjective aesthetics.**
