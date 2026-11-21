# Design DNA — Reference Site WHAT / WHY / EVIDENCE

Do not merely list colors: explain the trade-offs behind observed design decisions. MauForma uses its own independent review workflow; it does not claim to inspect inaccessible or unverified remote sites. Open-source acknowledgments belong in README.

## Inputs and levels of evidence

- **Accessible URL:** Identify precisely which pages, viewports and dates were observed. Prefer real browser rendering. With HTML/CSS alone, state that external fonts, images and animation could not be verified.
- **User-supplied screenshot:** Describe only visual characteristics observable in pixels. Do not infer exact CSS values or internal frameworks/component libraries from a screenshot.
- **Multi-page reference:** Compare stable patterns shared across pages; record page-specific differences separately.
- **Insufficient fetched content:** Say evidence is insufficient. **Do not invent** real colors, motion stacks or image quality.

## Trigger and scope (B13)

Only trigger when the user wants to **study a real site's visual design**, or authorizes a specified public site as a design reference. A URL supplied for data retrieval, summarization or deployment does **not** authorize automatic Design DNA capture. Screenshots and computed styles establish observable **WHAT** only; an author's motivation, product strategy or rejected alternatives are **evidence-based interpretations**, not facts personally confirmed by the designer. If access is unavailable, fonts have not loaded, or capture is restricted, report `BLOCKED` or `INCONCLUSIVE`. Never write invented variables into the target project's actual tokens.

## Four-step review

1. **Observe WHAT:** Identify the main visual subject, palette hierarchy, typography, whitespace, grid, corner radius, shadows, media ratios and *only actually observed* motion.
2. **Propose WHY:** For example, a low-saturation background paired with high-contrast product photography can make the product the dominant focal point. Label this as **analyst inference**, not the author's public statement.
3. **Evaluate alternatives:** What is lost with uniform three-column cards or uniformly reduced images? Would the reference composition still work if the current user must rapidly scan a table?
4. **Transferable constraints:** Separate reusable principles (subject focus, hierarchy and rhythm) from brand-specific assets that must not be transplanted (logos, photographs and unique illustrations).

## Output fields

`subject`, `reference_url`, `observed_pages`, `viewports`, `date`, `confidence`, `design_map` (type/color/spacing/radius/shadow/grid), and `taste_decisions[]` entries shaped as:

`{trigger, decision, reason, evidence, rejected_alternative, inferred, suitable_sites, risk}`.

Distinguish fact, inference and unknown. See the example `examples/design-dna-record.json`. Respect copyright: do not copy third-party exclusive photography, brand assets or paid component source; general visual principles may be learned.

## Applicability

Design DNA supplies *supporting evidence for a candidate visual direction*. A confirmed user decision outranks an inference that an interface ought to resemble a reference site. Map observed results to MauForma's eight style profiles, and explain their applicability based on the actual site content and user goal.

## Optional executable capture

When authorized and applicable, run `node scripts/extract_design_dna.mjs --url https://example.com --out ./artifacts/design-dna` on a real accessible site to retain computed styles and screenshots as distinct evidence. This tool does not infer the original author's WHY or automatically write reference findings into MASTER. Static-only reviews or unauthorized sites must be labeled unverified. See `references/skill-gap-workflows.md` for execution and network-safety boundaries.
