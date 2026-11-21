# Surface Architecture Gate — Decide Whether a Container Is Needed Before Styling It

Applies to all Web products and modes (Operate/Persuade/Read/Experience). Giant rounded frames, nested cards without hierarchy and borders everywhere are common generated patterns. But eliminating “AI-template feel” **does not mean deleting all Cards**. Surface structure follows real content entities, task boundaries, comparison needs, independent interaction/state and art direction—not a page template projected onto business logic.

## v6.18 — Learn grouping principles from strong references, do not clone whole pages

References can teach when a container adds value, when tables should be flat and how sections relate. Extract “compact yet legible, few layers, clear relationships”; never reproduce identifiable reference layouts, original business data or branding page by page. See `references/design-reference-learning-gate.md`. If using `references/clean-enterprise-design.md`, verify the target product actually needs that density/workflow. Project-specific tasks and information architecture outrank a sample workbench template.

## v6.16 — Surface decisions are not spacing decisions

First decide whether the panel exists. Then use `references/semantic-spacing-rhythm-gate.md` to define **inside/peer/section/connected** relationships among container and neighbors. Both inherited and new Card/Panel use `references/surface-edge-accent-gate.md` Gate S0: **no decorative color rail by default, no thick bar flush against rounded borders**; a justified marker must be short, external and visibly separated. Separate chart Cards can still be legitimate, but must not touch vertically merely because they share one parent. Tabs attached to their own Panel may intentionally have a shared edge and **zero gap**; don't blindly add 16px. Card padding cannot substitute for external gap. Do not delete all Cards indiscriminately just because the UI is crowded.

## 1. Gate A — Surface Decision Tree

1. **Are these items one continuous scannable/comparable collection?** Records, orders, transactions, members, course listings and tasks often fit an **open collection / flat table / list** with heading, toolbar, column headers and row separators, perhaps one light boundary. Every list row is not automatically a Card.
2. **Is this an independent interaction, status, data scope or complex block needing separation?** A **bounded panel** can be appropriate, but its heading/filter/table shouldn't each need another Card. Preserve only boundaries that communicate grouping.
3. **Is each entry an independent object with heterogeneous media, product image or independent action?** Consider **entity Cards/gallery**, including branded large media and deliberate asymmetry.
4. **Is this long-form reading or narrative?** Prefer **open editorial flow** with measure, chapter rhythm, headings and quotations rather than boxing every paragraph.
5. **Is this professional multi-area editing (IDE/editor/complex settings)?** Use **split panes/grouped work areas** where stable divisions and ownership matter more than floating cards.
6. **Is this a creative experience or marketing Hero?** A **Hero stage/immersive canvas** may dominate the page, but essential content/actions must remain reachable.

These are **candidates**, not automatic choices. Record at least **one plausible rejected alternative and why** (e.g. “No full-page Card: toolbar and table form one continuous collection, an extra border adds no meaning”). Tiny fixes need no multi-option design presentation.

## 2. Surface Value Test — avoid “drawing a box means designing”

Ask for each major container:

- **Scope:** Does it hold an independent task/object/state or simply enclose everything on the page?
- **Distinction:** Could title, columns, separators, background and spacing preserve comprehension without a frame? If so, reduce or remove the surface.
- **Layers:** Does the UI repeat Page background → mega Card → toolbar Card → list Card → row Card for essentially one logical group? Consolidate redundant shells.
- **Density:** Is the content worth the space occupied? Huge blank regions, row padding and useless mini headings are not professional polish.
- **Art direction:** Do borders/radius/shadows follow project tokens and real art direction rather than generic SaaS? Are borders, pseudo-elements, gradients or inset shadows creating thick colored rails attached to the frame?
- **Responsive:** At narrow viewports/200% text, can relationships reflow without clipping, unreachable focus or loss of final scroll access?

Compare grayscale wireframes: **A — open sections/direct table**, **B — one-layer bounded panel** and, when media-led, **C — independent object Cards/gallery**. Compare **task speed, alignment and grouping semantics**, not which style looks “premium.” Producing all three is unnecessary when one decision is adequately grounded.

## 3. Pattern choices and boundaries

| Pattern | Valuable use | Poor default | Verify |
| --- | --- | --- | --- |
| Open collection / flat table | Many homogeneous records, status scanning, sort/filter | Rounded Card for every row | Columns, separators, hover/focus and long fields |
| Single bounded panel | Independent data range, settings group, analysis module | Giant nested Cards beneath the page frame | Panel heading/content share one IA |
| Entity Cards / gallery | Products, works, courses, separate media/actions | Identical record rows as a Card grid | Types, media ratios and actual interaction |
| Editorial flow | Articles, docs, learning steps and examples | Each paragraph in a gray rounded box | Line width, media, quotes, navigation |
| Split workspace | IDE, resource tree/details/preview | Random floating Cards instead of stable workspace | Drag, collapse, focus and dimensions |
| Hero / immersive stage | Brand/experience storytelling | Business table stuffed into a giant Hero | Reachable content, contrast and performance |

Operate task monitoring, member management, transactions and analytics often start with a flat collection. **This does not forbid Cards in admin products**; it requires a checkable reason for any independent surface. Details, warnings and filters may have separate panels when useful, not by default.

## 4. Principles and sources from established design systems

**IBM Carbon Data Table** organizes title, toolbar, header, rows and pagination as one table structure. Give tables enough main-content width; don't trap them in overly narrow Cards. Design row actions deliberately. Transfer **collection/action organization**, not Carbon's branding or code.

- https://www.carbondesignsystem.com/components/data-table/usage/
- https://github.com/carbon-design-system/carbon-website/blob/main/src/pages/components/data-table/usage.mdx

There are **no universal numeric cutoffs** for container count, radius or border weight. Automated tools can validate authored contracts/fixtures, but cannot score “premium aesthetics” or guess user taste.

## 5. Gate B / D acceptance

**Gate B:** Establish shared Table/List/Panel/Card ownership and tokens; distinguish page composition from actual component surfaces. For tables, check column sizing, action layout, statuses/row heights and behavior; then use `references/control-geometry-gate.md` for atomic action labels.

**Gate D:** Compare full-page **real browser screenshots** across supported wide/short/narrow windows, 200% text and edge data (long labels, empty/error). Confirm focus, rhythm, attached inherited/new accent bars and final scroll access. Large creative or brand panels can remain if actual content justifies them. **A passing static design plan does not prove visual quality.**

Related: `references/whitespace-and-surface-composition.md`, `references/component-craft-gate.md`, `references/perceptual-hierarchy-gate.md`.
