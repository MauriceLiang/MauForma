# Spacing Regression Protection Gate — Never Erase Independent Section Gaps Unintentionally (v6.19)

Applies across Web frameworks and product modes. Complements `references/semantic-spacing-rhythm-gate.md`: v6.16 defines spatial relationships, but formerly assumed Agents would annotate actual DOM and run explicit contracts. Without annotations a refactor could zero large `row-gap` values yet claim improved compactness. **Preservation and regression inspection of existing good spacing is a hard gate for UI updates/polish.**

## v6.20 — Protect only good inherited gaps, never an already broken baseline

Before/after protects against **new degradation**, not a replacement for initial diagnosis. If two separate large Cards touched **before** editing, the baseline is not proof the user approved that contact. Vague polish must first execute `references/proactive-visual-defect-discovery-gate.md`, using baseline-free `scripts/audit_existing_visual_defects.mjs` on the **actual running page**. Distinguish independent Section/peer surfaces from intentionally connected Tab/Panel structures. Defects requiring repair may not be ignored “to preserve the original.”

Only then compare before/after to protect **already correct** spatial relations. Automated discovery does not replace full screenshots or business semantics. Report unobserved scope.

## Gate SG0 — Preserve by default

- “Improve,” “polish,” “clean,” “put more content above the fold,” “minimal,” or “low density” does **not** authorize joining previously independent regions, setting `row-gap:0`, deleting parent `gap` or using negative margins to collapse separation.
- Before editing, identify group-level rhythm worth preserving (e.g. metric strip → main plot, main plot → supplementary stats, chart row → next row, analysis Card → supporting summary, table → separate Help section). Classify `section/peer/inside/connected/anchored`.
- **Gaps between independent modules are protected design state:** Unless the user requests a change, the modules genuinely merge responsibilities with a structural reason, or a new layout produces a better hierarchy within the user-approved density direction, **do not markedly compress them**, especially not to zero. If modifying, report old/new values, impact and rationale—not “code simplification.”
- Reduce page height by first removing repeated explanations, useless surface shells, oversized chart placeholders, low-value modules, excessive row internal padding or by making content scroll. **Never erase every outside gap to avoid a content-density decision.**
- Do not place one project's gap values or module names into global defaults. Even compact UI needs clear inter-region boundaries. **Valid zero-gap exceptions:** contiguous table header/body, Tabs with their panel, segmented controls and continuous timelines.

## Gate SG1 — Before/after layout regression checkpoint

1. On the same **real application route**, data and viewport/text scale, first capture and **inspect the full existing page**, and measure visible boundaries between meaningful independent regions. Inherit official project tokens and approved decisions. A new synthetic gallery page cannot stand in for the old page baseline.
2. Define `section/peer` relationships for important independent regions. If precise contracts exist, run `scripts/audit_spacing_rhythm.mjs`. Without prior `data-mf-space-id` annotations, use `scripts/audit_panel_spacing.mjs` on actual obvious bordered/surface-like Grid/Flex regions; **missing annotations are not permission to skip risk review**.
3. Save `before.json` at the same viewport/font scale. Edit, produce `after.json`, compare with `--baseline before.json`. Severe gap loss—even if the new gap remains positive—unintended touching and overlapping independent surfaces are regressions requiring repair.
4. This is **heuristic**, and cannot understand every boundary. Transparent/open areas, Canvas, absolute placement, transforms and portals need explicit semantic notes, full-page screenshots and human inspection. With no comparable pairs or insufficient scan coverage, **report uncovered regions**, not a passing spacing score.
5. An intentional `connected` group may use zero gap, but document the reason and shared structure. For example `data-mf-connected-reason="Tabs and the immediately associated panel are one continuous control"`. Do not mark every parent “connected” to hide accidental touching. It belongs only on an actually unified structure and requires human review.
6. Complete-screen screenshots (first/middle/last) and interaction states remain necessary. A geometry scanner does not prove artistic merit, design intent or exhaustive coverage.

## Gate SG2 — Common defect and structural correction

```css
/* Wrong: erase Section spacing to fit more content vertically */
.analysis-stack { display: grid; row-gap: 0; }
.analysis-stack .chart-grid { column-gap: var(--peer-space); row-gap: 0; }

/* Correct direction: parent expresses independent relationships */
.analysis-stack {
  display: grid;
  row-gap: var(--section-space);
}
.analysis-stack .chart-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  column-gap: var(--peer-space);
  row-gap: var(--peer-space);
}
@media (max-width: 48rem) {
  .analysis-stack .chart-grid { grid-template-columns: minmax(0, 1fr); }
}
/* Tab and Panel legitimately connected may remain at zero gap */
```

CSS illustrates relationships, **not universal values**. Do not add `margin-bottom:16px` to every component or use `!important`, clipped overflow or giant padding to fake correct gaps.

## Gate SG3 — Low-cost browser audit commands

For an existing project with Playwright:

```bash
# Replace the demo URL with the actual target page
node scripts/audit_panel_spacing.mjs --url http://localhost:5173/example --out before.json
# After changes, same page, state and viewport
node scripts/audit_panel_spacing.mjs --url http://localhost:5173/example --baseline before.json --out after.json
# When explicit relationships exist
node scripts/audit_spacing_rhythm.mjs --url http://localhost:5173/example --contract spacing-contract.json
```

- `UNJUSTIFIED_PANEL_CONTACT`: Large visible candidate independent panels touching.
- `SPACING_REGRESSION`: Material gap loss relative to prior DOM relationship, even when new gap is above zero.
- `ASYMMETRIC_GRID_SPACING`: A row has gutter while multi-row spacing collapses; confirm actual grid has multiple rows.
- `INSUFFICIENT_COVERAGE` / `NO_COMPARABLE_PAIRS`: Not a pass; add explicit semantics or manual inspection.
- `VERY_TIGHT_PANEL_GAP`: Manual review candidate, not automatic condemnation of all tight UI.
- `data-mf-connected-reason` is **not a global exemption**; intentional shared edge needs structural justification.

The script only recognizes **a limited set of conspicuously framed surfaces under common Grid/Flex parents**. It neither infers all semantics nor saves screenshots. This is a risk hint, not an aesthetic score.

## Gate SG4 — Required delivery statement

For a real UI improvement, report:

- Which **independent-module spacing relationships** changed, remained unchanged or were intentionally compressed with authorization.
- Whether testing covered a **real page**, not a standalone demo; include viewports, text scaling and whether before/after comparison was run.
- Uncovered regions, possible false positives and accessibility concerns.
- “Adjusted padding” or “the component passes” does **not** establish inter-section spacing passed.

## Coordination with other gates

- `references/semantic-spacing-rhythm-gate.md`: Roles and spacing choices.
- `references/grid-alignment-and-viewport-safety.md`: Grid axes, breakpoints, scroll reachability.
- `references/whitespace-and-surface-composition.md`: Whitespace, optical weight and surface decisions.
- `references/control-geometry-gate.md`: Restored gaps must not crush actions.
- `references/design-reference-learning-gate.md`: Never commit user reference screenshots/identifiable content into public repo or CI.
- `tests/panel_spacing_browser_smoke.mjs`: Original synthetic success/failure cases; never user data.
