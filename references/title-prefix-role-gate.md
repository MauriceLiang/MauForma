# Title-Prefix Role Gate — Structure and Semantics Before Styling

**Applies to:** New Web pages, existing UI polish, component refactors and relevant design reviews. Every page type (Operate, Read, Persuade, Experience) and every visible heading level (H1–H6 or equivalent visual headings), including Card, Section, Panel, Hero, Dialog and embedded Web UI. This is **not** a ban on useful section titles, status, chapters or brand narrative.

## The principle

An **eyebrow / overline / kicker / pretitle** is a *relationship*, not a CSS class, font size, color or English phrase: a short subordinate text layer placed before or above a neighboring title to label, introduce or decorate that title. It may be black, colorful, bold, small, large, monospace, handwritten, uppercase, Chinese, numerical, icon-backed, or split across nested components. Do **not** define its identity by a blue color, letter spacing, a fixed number of pixels, a text regex or a literal `eyebrow` prop.

Determine the element's **structural relationship** first, its **information role** second and its **presentation role** third. The meaning of its words and the appropriateness of the *preamble presentation* are separate decisions. Meaningful content may still be incorrectly presented as a decorative title prefix.

## Gate H-S — Self-sufficient heading by default (all page types)

**Default: write a clear, self-sufficient heading and no separate pre-title line.** Most category labels, dual-language explanations, rhetorical overlines, feature introductions and visual-rhythm indices merely restate what the heading or nearby interface already tells the reader. The burden of proof is on **retaining or introducing** a pretitle, not on deleting one. This applies equally to inherited UI and new work, H1–H6, and functional, scientific, learning, editorial, brand and creative contexts; genuine meaning is protected, but a page type alone is not an exemption.

Run these three counterfactual tests **in order**:

1. **Remove the line mentally.** Can users still identify the content or action from the heading and nearby UI *without losing independent navigation, status, scope, source, chapter order or approved identity*? If yes, **DELETE the redundant line**. Merely saying it "provides context," "looks polished," "adds hierarchy," "improves UX" or "explains the area" is not evidence of information loss.
2. **Demand specific added information.** If removing it loses something real, state exactly *what* is lost, *who* needs it, and where that information is supported by the product. A category word, loose synonym, generic explanatory translation or repeated mode name does not automatically add value.
3. **Prove why the text belongs above the heading.** Even genuinely valuable information should normally move to its owner: breadcrumbs/navigation, a stepper, a status or version badge, data scope/source beside relevant data, or concise below-title help. **KEEP as a separate pretitle only if this exact placement has a justified, nonduplicated role**, including explicit approved editorial/brand narrative. Do not turn real progress or a verified state into ornamental small type.

**Default decisions:** no extra pretitle in new UI; DELETE inherited filler; MOVE legitimate but misplaced data; MERGE a useful qualifier into the heading; SPLIT brand/status from generic filler; KEEP only with two distinct concrete reasons (independent information **and** above-heading placement). Do not remove actual structured navigation, course chapters, sources, permissions or safety information to make a page superficially sparse.

**Completion gate for scoped UI polish:** every candidate from affected real routes must have a reviewed decision and, for KEEP, a substantiated semantic role, information-loss explanation, placement reason and evidence. Re-check the rendered result after implementing DELETE/MOVE/MERGE/SPLIT. Unreviewed candidates, vague KEEP rationales or still-present unjustified prefixes **block a claim of VERIFIED**. Use `scripts/audit_title_prefixes.mjs` for candidate discovery and `scripts/validate_title_prefix_review.mjs` for a mechanical **review-completeness** check when the target project and Playwright are available. The validator cannot judge true brand meaning or replace human/Agent visual inspection; otherwise report STATIC CHECK or NOT TESTED instead of inventing evidence.

## Mandatory three-pass decision

### Pass A — Discover potential title prefixes, not just H1

1. Inspect the actual rendered page at the target viewport(s). Find title/heading groups, including headings rendered through reusable components, slots, fragments, React/Vue templates, translated content, CSS pseudo-content and visible non-semantic wrappers. Do not assume `h1`, `.eyebrow` or an adjacent sibling structure.
2. For every visible main/page, section, card, step, chart, dialog or feature title, look for **independent subordinate text immediately before/above it in the same title group**. Ask whether it reads as a prelude to the title rather than a separate content block. Look at DOM/rendered order, grouping, proximity, repetition across peers and the relationship to downstream content. **Do not use color, font, weight, case, language or absolute size as a gate.**
3. Explicitly inspect existing *and* added content; inspect shared header components, default props, slot fallbacks, data-driven title arrays, localization strings and CSS `::before`/`::after`. A change to unrelated styling never grants legacy text an exemption.
4. A source or DOM scanner is an **optional candidate generator**. It cannot verify purpose, brand approval or visual appropriateness by itself. Canvas, image-baked labels, portals and unusual layouts may need human visual review.

### Pass B — Classify meaning and ownership

For each candidate, answer: **What information does this specific element add? Who needs it? Is it already conveyed by the title or nearby UI? Would removing it lose valid information?**

| Role | Examples (fictional) | Default action |
| --- | --- | --- |
| Decorative pretitle, generic category or duplicate translation | `WORK AREA` above `Projects`; `VISUAL VIEW` above `Explore` | **DELETE**, regardless of presentation |
| Unsupported ornamental number / meaningless sequence | `02 / FEATURES` used purely for rhythm | **DELETE** the decorative part |
| Real page path / breadcrumb | `Workspace / Billing` as navigable path | **KEEP** as navigation, not an eyebrow |
| Real ordered instruction, chapter or timeline step | `Step 2 of 4`, `Chapter 3` with real structure | **KEEP or MOVE** into stepper/chapter/navigation semantics |
| Actual status, classification, source, unit, scope or time range | `Offline`, `Updated 09:00`, `Sample n=42` | **KEEP or MOVE** beside affected object, status, legend or data source |
| Confirmed product identity or approved brand narrative | Real brand name, documented editorial kicker | **KEEP or MOVE** when genuinely needed, with appropriate presentation |
| Mixed identity plus generic description | `ATLAS · Analysis Workspace` | **SPLIT**: preserve genuine identity; delete or move unsupported filler |
| Necessary distinct section heading or explanatory paragraph | A heading introduces its own content, or a paragraph explains a real constraint | **KEEP** as its own semantic block; do not mislabel it a prefix |

An actual step number or semantic label is **not blanket permission** to place it above every heading with eye-catching pretitle styling. If its relationship is step progress, show it as progress; if it is data metadata, place it near the data; if it is a useful description, consider below-title help copy. Brand/editorial storytelling can intentionally use an eyebrow when approved and contextually useful.

### Pass C — Evaluate presentation independently

Even if the candidate text is worth keeping, decide whether the **separate pre-title line** is necessary. Prefer a clear standalone title. Use `KEEP / MERGE / MOVE / SPLIT / DELETE` with a one-sentence reason:

- **KEEP** only if both meaning and title-prefix placement are justified by product information architecture, actual narrative or explicit design approval.
- **MERGE** when text adds a useful modifier to the title but need not occupy another line.
- **MOVE** when the text is legitimate but belongs in a breadcrumb, stepper, tag, chart legend, status area, metadata row or below-title description.
- **SPLIT** when legitimate identity/state is combined with decorative explanations.
- **DELETE** when no content is lost, or the prefix is added only to imitate visual complexity, an AI template or a supposedly premium style.

**Hard default for task-oriented product surfaces:** do not invent a second decorative title layer above a title at *any* level. Functional headings are direct. For reading, learning, scientific, marketing and creative experiences, real chapters, guided steps, editorial contexts and accepted narratives may be justified; do not flatten them mechanically.

**Styling-invariance test:** Would you reach the same semantic decision if the candidate used a different color, font family, scale, weight or language? If not, reconsider the classification. A CSS-only change that leaves the same unjustified pretitle relationship is **not a fix**.

## Verify on the user's real product

1. For UI improvement/overhaul tasks, enumerate affected rendered title groups and classify likely prefixes (not just H1, not just changed files). The reviewer must inspect each exposed route/panel state or report scope limitations.
2. Use `scripts/audit_title_prefixes.mjs` when a real page and available Playwright make it useful. Its style-independent DOM traversal generates **CANDIDATES_FOR_REVIEW**, not semantic verdicts, and cannot guarantee coverage for canvas/pseudo-content or non-heading typography. The Agent must resolve candidate roles from context.
3. Compare the same rendered regions **before → after**, including component instances that retain old prefixes. If an unjustified prefix remains, do not mark the design review verified. Preserve legitimate navigational and data content.
4. Report compactly: `route | title/region | candidate | semantic role | decision/reason | result | evidence`. Use `VERIFIED` only after actual page review; `STATIC CHECK` for code-only review; `NOT TESTED` for no render access. Never claim a synthetic demo proves the user's product passed.

## Boundaries and negative cases

- **Do not** automatically delete every line above a heading, every uppercase or CJK label, all badges, every number, or all subtitles. Meaning and owner authorization outrank aesthetic heuristics.
- **Do not** infer or change the user's brand, language, taxonomy or approved editorial hierarchy from a screenshot-only guess.
- **Do not** create a fixed style blacklist (specific hex colors, font sizes, letter-spacing values, theme or framework names). Such blacklists cause false negatives and break unrelated products.
- **Do not** turn this into a full-site redesign for an isolated non-visual bug. Apply to affected routes and shared components when title/content work or UI-polish scope calls for it.
- Preserve useful visible status even if its visual placement must change; do not hide critical accessibility content solely to satisfy an aesthetic preference.

**Related:** `references/page-header-antipatterns.md` (H-Base/H0), `references/semantic-copy-hygiene.md`, `references/proactive-visual-defect-discovery-gate.md`, `references/browser-qa-protocol.md`.
