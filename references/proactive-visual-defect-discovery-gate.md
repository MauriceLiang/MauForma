# Proactive Visual Defect Discovery Gate — Vague UI Improvement Requires Finding Existing Problems

MauForma is a design **and implementation** Skill, not a tool that merely converts user-reported symptoms into CSS. When a user says “polish the page,” “make this look professional” or “improve with MauForma,” **inspect the real page first**, establish evidenced defects, prioritize and actually repair the most important ones. The user need not enumerate each flaw. Do not change approved branding, data semantics or motion decisions without authority.

## Diagnose UX causes before visual decoration

For an ambiguous request to “improve the home page” or “remove the AI-template feel,” apply [product experience routing](product-experience-routing-gate.md): admin, consumer, learning, content, creative or another intent—and the user's actual primary task. If that task is missing or the navigation does not serve the product, the problem outranks colors, spacing, emoji or radius. Use [progressive refinement](progressive-visual-refinement-gate.md), **R1 information architecture**, rather than merely recoloring the old layout.

An isolated issue within an approved layout stays scoped under Gate D0; it never automatically authorizes a redesign. The existing five-dimensional visual checklist still matters but does not replace UX diagnosis.

## Gate D0 — Let task semantics select the work mode

| User intent | Default execution | Avoid |
| --- | --- | --- |
| General visual polish / aesthetic refinement | **diagnose → prioritize → repair → verify** the actual page, including inherited defects | Unifying typography/radius/colors and claiming completion |
| One identified visual issue (e.g. touching panels) | Reproduce that issue and directly adjacent area → fix → check regressions | Change one CSS declaration without checking its neighbors |
| Specific functional bug only (e.g. submit failure) | Scoped fix and relevant UI regression | Mandatory site-wide redesign |
| Review/report with no edit permission | Diagnose, rank and report without changing source | Unapproved design-system edits |
| No accessible running page | Source-based structure/style inspection plus user-provided screenshots, explicitly marked as unverified | Pretending to test a browser or treating a demo as the product |

## Gate D1 — Inspect the real page before designing

Examine actual affected routes, states, mid-page content and scroll end, prioritizing:

1. **Structure and spacing:** Are independent Sections, peer data/chart cards or full-width regions unintentionally at zero gap? Identify pre-existing failures rather than protecting them as “the current design.” Card padding does not substitute for a gap *between* cards. A layout with horizontal column gaps but no vertical row gaps is also suspicious.
2. **Hierarchy, typography and title prefixes:** Is important P0/P1 text tiny or low contrast while empty decorative titles dominate? Are chart labels and axes unreadable? On **every page type, color, font and size**, inspect inherited and new pre-title lines across H1–H6, cards, sections, dialogs and custom title components. First recognize structural roles with `references/title-prefix-role-gate.md`, then H-Base/H0 in `references/page-header-antipatterns.md`; decide `keep / merge / move / split / delete`. Valuable content does not automatically justify an ornamental pre-title. Old content is not exempt.
3. **Components, content and attached accent bars:** Are all functions buried in huge nested Cards, unrelated surfaces visually touching, button geometry inappropriate, tables needlessly sparse, or empty data shown as oversized placeholders? Inspect **new and existing** Card/Panel/Section single-edge strips, pseudo-elements, inset shadows and gradients that touch their rounded borders. Remove decorative bars by default; a meaningful indicator must stand **outside** with a visible gap (Gate S0, `references/surface-edge-accent-gate.md`).
4. **Control provenance and expanded-state consistency:** Identify native, vendor, headless and hand-built controls mixed within the same task area. Inspect the *actually opened* Select/Combobox, Dropdown and Dialog as well as typography, density, borders, radius, shadows and focus. Use `references/component-consistency-and-selection-gate.md` to decide whether existing components should be reused or replaced according to product type, not matching CSS strings. `scripts/audit_control_consistency.mjs` can surface DOM candidates but cannot inspect OS-owned menus or identify the component vendor.
5. **Icon and color:** Check icon meaning, shape and optical weight; colors should support brand and state, not gratuitous saturation. Do not silently change a user-approved palette.
6. **Interaction and responsiveness:** Are selected, hover, focus, loading and error states real? Do tabs/dialogs/filters work? Are text zoom, narrow windows and scrolling to the end usable without overflow or occlusion? Respect the approved motion intensity.

Identify the **top three evidenced risks when they exist**; do not invent three problems in a healthy page. Rank by severity and user benefit, not how easily a color can be changed. A concise record is `page | issue | evidence | confidence | impact | severity | proposed fix | verification`. Before a code fix, decide whether two surfaces are independent (gap needed) or intentionally connected (shared edge may be correct). Assigning every gap an arbitrary 16px is not a design decision.

## Gate D2 — Discover inherited failures and protect good existing behavior

The v6.19 `before → after` regression check guards against **new regressions** but cannot reveal a defect already present in the before state. Use both tracks:

- **Baseline-free discovery:** `node scripts/audit_existing_visual_defects.mjs --url <current-page> --out /tmp/visual-audit.json`. Without baseline or DOM annotations, the script can flag likely unintended contact among framed surfaces across block flow, Grid/Flex and simple transparent wrappers. It reuses `audit_panel_spacing` hints and allows justified connected components. It does not prove semantics.
- **Preserve correct spacing (v6.19):** Run `scripts/audit_panel_spacing.mjs --baseline before.json` around changes. Protect good spacing and confirmed spatial roles, but never excuse an inherited zero-gap defect merely because it was in the baseline.
- **Explicit role contract:** If available, `scripts/audit_spacing_rhythm.mjs --contract ...` checks role-specific gaps/tokens. A synthetic annotated demo pass is not evidence about an unannotated real page.
- **Title copy is an independent semantic audit:** Geometry scans cannot judge whether an eyebrow/Logo/Tagline is meaningful. Use `scripts/audit_title_prefixes.mjs` to collect heading-level structural candidates irrespective of color/font/size; verify actual copy, approved brand/navigation roles and placement. Do not auto-delete from CSS keywords.
- **Accent bars require their own visual inspection:** Spacing PASS does not prove attached Card bars are absent. Inspect real border, radius, DOM and computed styles. Neither inherited code nor arbitrary bar removal is acceptable; protect legitimate focus, charts and timelines.
- **Human visual judgment remains essential:** Canvas, transparent frameless areas, portals, sticky elements, animation/scroll, overlays and complex composition may evade DOM heuristics. Small gaps are not universally bad; the target is *accidental contact between unrelated blocks*. A geometric warning needs semantic confirmation; a script PASS does not establish aesthetic quality.
- **Insufficient evidence:** When there are too few visible framed panels or the page is inaccessible, report `NOT AUDITED`, not PASS. Still inspect available screenshots, DOM and CSS, report blind spots and do not demand facts the user already provided.

## Gate D3 — Close the loop by actually fixing defects

1. Attach a real location and root-cause hypothesis to each P0/P1 defect. When evidence and authorization suffice, update the actual layout/styles/components—not just a report. Brand-changing or risky behavior follows existing user-decision gates.
2. Fix structure and spatial roles first, then color, typography details or motion. Change the parent Grid/Stack's gap/relationships where appropriate, not negative margins, `!important` overrides or card padding that hides the problem.
3. Reload the **same real page** and compare the original defect before/after. Recheck inherited title preambles and attached Card strips even if they were not in the changed diff. An unfixed old defect cannot be called verified. Keep valid `connected` exceptions but never add a blanket connected flag to the whole site.
4. Also check responsiveness, 200% text zoom, changed states and scroll-end reachability. A bundled synthetic smoke test proves only its fixture.
5. Report one of `FOUND → FIXED → VERIFIED`, `FOUND → UNFIXED(reason)`, or `NOT AUDITED(reason)`. Running a script alone does not qualify as successful design completion.

## Gate D4 — Scope and privacy

- **Do not infer source ownership.** User screenshots are evidence for the current task. When the user excludes them from the repository, never commit their originals, crops, blurred variants, identifiable content, URLs, PR attachments or test screenshots to a public repository.
- Browser scanners should emit abstract geometry by default; the caller provides the CLI URL. Never automatically upload private/commercial screenshots to public CI artifacts or commit them to the repository.
- The gate does not enforce one UI template across all sites. Operate, Persuade, Read and Experience share diagnosis steps but have different media ratios, spatial expression and density.
- Genuinely separate semantic regions should not accidentally share an edge even in restrained/minimal design; genuinely connected surfaces may use zero gap. The decision is about **relationship**, not a global 16px rule.

## Execution checks

- See `references/spacing-regression-protection-gate.md`, `references/semantic-spacing-rhythm-gate.md`, `references/visual-critique-loop.md` and `references/browser-qa-protocol.md`.
- Ambiguous-intent fixtures: `assets/proactive-audit-trigger-cases.json` and `scripts/validate_proactive_audit.py` (static decisions, never proof of actual Agent compliance).
- Baseline-free browser hints: `scripts/audit_existing_visual_defects.mjs` and `tests/existing_visual_defect_browser_smoke.mjs` (original synthetic DOM only, not user-supplied source).
