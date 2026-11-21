# Art Direction — Composition, Page Modes and Independent Critique

Read `references/design-discovery-interview.md` and `assets/style-knowledge.json` when relevant. If the user has not chosen a direction, ask about purpose and available showcase content before suggesting **2–3 genuinely different first-screen compositions**. Do not offer ten vague style adjectives instead.

## Visitor success modes — inspired by Impeccable, independently specified by MauForma

| Mode | Visitor's task | Visual strategy | Never misuse |
| --- | --- | --- | --- |
| **Persuade** | Decide, reserve, buy or download | Hero media/strong claim, real trust evidence, clear CTA; first screen may be low density | Hiding price, critical restrictions or next action for visual drama |
| **Operate** | Search, edit, submit, approve or debug | Task-driven density, fast scanning, stable states/actions | Information-free Hero, slow animation and decorative titles |
| **Read** | Read article, docs, tutorial or policy | Reasonable line length, hierarchy, search and contents navigation | Mandatory per-paragraph animations or interruptions to reading |
| **Experience** | View a work or engage with interactive content | Subject first, secondary controls, intentional asymmetry/immersion | Repeatedly covering or obstructing the work itself |

One page can have a principal and secondary mode. Decide **per page**, not by assigning one permanent label to the entire product. Record in `design-system/pages/*.md` when useful.

## Five design decisions before implementation

1. **Subject:** What specific entity/content must draw the first glance? Explain genuinely coequal subjects when present.
2. **Actual assets:** Are there real product photos, quality video, functional screenshots, usable copy and data columns? If missing, propose a workable alternative without manufacturing facts.
3. **Composition:** Full-bleed photography, split columns, offset editorial layout, project gallery, data grid or reading article. Describe meaningful alternatives and tradeoffs.
4. **Expression intensity:** Three 0–10 controls (variance/motion/density), with different acceptable ranges per page; respect reduced-motion.
5. **Component contract:** Shared tokens, baseline styles and states across pages; variation belongs mainly in page composition.

## Decision card for each candidate

- Option ID, source style, visitor mode and homepage focal point.
- Textual sketch of first-screen geometry and media-to-copy proportion.
- Type, color, whitespace, the motion/variance/density dials and purpose.
- **Content-specific** rationale and required media/dependencies.
- Benefits, sacrifices, responsive cost and reduced-motion alternative.
- Decision status: **confirmed by user** versus merely **recommended**.

## Critique before coding — answer specifically

1. **Substitution test:** If this project's content were replaced by any unrelated SaaS, would the layout still make equal sense? If so, is the result insufficiently content-driven?
2. **Focal point:** Is the important first-screen subject visibly prominent? Are multiple focal points intentional?
3. **Truthful copy:** Do headings, minor labels and descriptions add distinct information rather than filler slogans?
4. **Asset quality:** Is the imagery sharp enough, appropriately cropped and licensed? Does its size express real product identity?
5. **Density:** Is the page for viewing, deciding, reading or operating? Does whitespace and control quantity serve this purpose?
6. **Cost:** Is there a real route for mobile, keyboard, slow networks and motion fallback?

If the critique fails, adding a gradient is not “polish.” Revise composition or remove low-value content **before Gate B**.

## Critique after coding

Compare the user-approved direction with **actual browser rendering** at the same viewport. Record:

- Hero/media scale, first-screen CTA visibility, clipped content and surplus whitespace;
- Reflow at supported breakpoints, long Chinese/English copy, light/dark mode and font-load failures;
- Component hover/focus/disabled/error/loading and actual business operations;
- Access to primary content under reduced motion and low-performance conditions;
- **Three aesthetic decisions to preserve and three problems to repair**.

Static review is not screenshot verification. For failures, record exact route/code position, screenshot if available, and resulting fix status.

## Counterexamples — minimalism is not always correct

- Bad: Flatten an expressive experimental portfolio into equal three-column Cards merely for “component consistency.”
- Bad: Add endless parallax to an operations workspace to make it “premium.”
- Good: A portfolio can use offset photography and large whitespace while keeping its filter list a clear grid.
- Good: A food brand can use dominant hero media while its real ordering page keeps price and checkout actions immediately visible.

A user who explicitly approved strong visual art direction keeps that expression unless it violates safety, accessibility, truthfulness or explicit user constraints.

## v6.4 — Composition before style polish

This document's art direction **must not bypass actual content architecture**. For new sites/major redesigns, run [Composition First](composition-first-design.md) before Critique, create grayscale composition and 2–3 candidates that genuinely differ in **dominant region, order or grouping**. Three recolors of one blue/purple/green layout do not count as choices. If an old screenshot shows an oversized gradient Hero or ornamental 3D cube dominating real trends, reconsider region area and evidence; changing color, glow or corners is not a structural fix.

See [Palette Art Direction](palette-art-direction.md) for semantic palette choices and [Visual Critique Loop](visual-critique-loop.md) for real-browser checks. Keep intentional large imagery/unique colors on authorized creative/brand/launch pages; never blindly impose operations rules on the whole site.
