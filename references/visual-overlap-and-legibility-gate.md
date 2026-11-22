# Gate LO — Label Collision, Readability and Visual Feasibility

> **Scope:** All Web pages and Web-based desktop shells, created from scratch or polished/refactored from existing UI. Applies regardless of framework, theme, language, font, component library, Card or Badge naming. This gate is about **actual rendered readability and spatial relationships**, not matching a screenshot's exact color or pill radius.

## LO0 — Independent information must not visually collide

The default is **zero unintended overlap** among independent readable labels, badges, metadata, links, controls, titles, statuses and their visible backgrounds/borders. Two labels can be separate text strings and still be unusable when one pill background covers the beginning of another. Structural DOM validity, a CSS build, a clean root scrollWidth, and aesthetically rounded components do **not** prove a valid reading surface.

- Distinguish three independently failing cases: **surface–surface overlap** (independent label borders/backgrounds invade each other), **text–text collision** (glyphs are unreadable), and **text–foreign-surface occlusion** (a neighboring chip paints over text). Test all three.
- A short status chip must not hide a long attribution, license, description or timestamp. Never mask data loss with `overflow:hidden`, `text-overflow:ellipsis`, hidden text, an arbitrary `z-index`, reduced opacity, or clipping unless truncation is a **deliberate product requirement** with an accessible full-value route.
- Reading order must remain natural: text should flow in logical groups, remain selectable where applicable, and avoid visually ambiguous combined border outlines, phantom merged pills, cut words, and near-zero unrelated spacing.
- The fact that the **original** product had overlapping UI is no exemption; the fact that a newly generated component is visually attractive in isolation is no exemption either.

## LO1 — Build relationships before styling

For each header, toolbar, chip group, card, metadata row, chart label and overlaid status:
1. Identify whether pieces are **peers**, **contained**, **anchored**, **stacked intentionally**, or **connected single controls**. Define their reading and keyboard/focus order. Separate peers in layout; don't solve overlap with arbitrary `z-index`.
2. Set a coherent parent layout: `display:flex/grid`, intrinsic sizes, explicit `gap`, appropriate `flex-wrap`, `min-width:0` on shrinking children, sensible text wrapping, and stacked layout at the product's supported minimum width. Prefer normal flow and semantic components. Avoid accidental negative margins, absolute offsets and nonwrapping labels that collide at narrow widths or large text.
3. Give attribution/licensing/version/status **their own meaning and room**. If one string is long, allow a new line or a more appropriate metadata position; do not sacrifice information to preserve a single-row look.
4. Check the resulting rendered group, not just token values: borders may intersect before text does, and text may be covered even if two text bounding boxes never intersect.
5. Ensure contrast, target/focus affordances, hierarchy, whitespace, content density, icon alignment and coherent reading order. A collision-free DOM can still look cramped, fragmented or misleading; correct visual feasibility requires human/Agent screenshot review.

## LO2 — Exceptions are narrow and semantic

Some UIs deliberately layer an icon on a card, a badge over media, a Tooltip/Popover over its trigger, a selected indicator under Tabs, or overlapping decoration/motion. **That is not permission for independent readable text or two separate pill outlines to collide.** Anchor real overlays to the owning component and verify their content, hit targets, focus, stacking and closing behavior. Inspect the full interaction state and interrupted/reversed motion. Avoid general-purpose project-level `ignore-overlap` flags; an intentional relationship must be justified **locally** and independently of any accidental text occlusion. A clipped/cropped media image is not the same as clipped explanatory content.

## LO3 — Mandatory real-page verification for new and existing interfaces

- **Before work:** inspect the actual affected routes/components (including historical shared wrappers) for existing collisions. For new pages, establish the supported viewport(s), longest realistic labels, locale mix and interaction states **before bulk building**.
- **During work:** after the first representative section and then after integration, inspect compact labels/metadata rows, headings, form actions, open popovers, tabs, charts and mobile/narrow variants only if supported. Test a declared minimum desktop viewport for desktop-only products.
- **After work:** run `scripts/audit_label_collisions.mjs --url <real-page>` where Playwright is available; also run `scripts/audit_existing_visual_defects.mjs` on pre-existing affected views or `scripts/audit_rendered_layout.mjs` for multi-viewport initial/end evidence. The latter two now include compact-label collision triage. Test 100% and 200% text zoom, original and longest locale labels, initial/focused/selected/expanded/loading/error states where relevant, and scroll to the end. A single full-width initial screenshot is insufficient.
- **Resolve** each collision on the affected page: correct layout, then recapture at the **same state and viewport**. `COMPACT_LABEL_SURFACE_OVERLAP`, `READABLE_TEXT_COLLISION` and `TEXT_OBSCURED_BY_COMPACT_SURFACE` must be assessed as actionable failure candidates; do not silently dismiss them as cosmetic. An incomplete scan cannot be reported as a pass.
- **Report** `route | viewport/zoom/state | element pair | collision or reading defect | fix | before/after visual evidence | remaining uncertainty`. A script PASS means only **no detected geometry risks within the tool's coverage**; Canvas text, SVG charts, image text, OS-owned controls and perceptual quality still require actual observation. When access is missing, report STATIC CHECK/NOT TESTED, never VERIFIED.

## Generic regression cases

- Two painted pills overlap while the labels' glyph boxes remain separated: **FAIL**.
- A second label's text visually enters the first pill's background: **FAIL**.
- Two unframed text lines physically intersect: **FAIL**.
- A long status / licensing / attribution row becomes a nonoverlapping wrapped or stacked group: **PASS candidate**, subject to readability inspection.
- Text inside its own button/badge or a valid icon adjacent to text is **not** independent-label collision.
- An approved icon/media overlay with no obscured content may be intentional; explicit justification does not override actual text or control obstruction.

**Related:** `references/grid-alignment-and-viewport-safety.md`, `references/semantic-spacing-rhythm-gate.md`, `references/control-geometry-gate.md`, `references/browser-qa-protocol.md`, `references/visual-qa.md`.
