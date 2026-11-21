# Design Reference Learning Gate — Learn Principles Without Cloning Identifiable Source

**Applies to:** User-supplied reference images, screenshots, authorized public examples and requested design-learning tasks. A screenshot is evidence for a visual discussion; **it is not automatic permission to copy its exact components, branding, assets or entire layout into a different project**.

## Gate RL0 — Source provenance, authorization and privacy

- Verify what was supplied: screenshot, URL, Figma frame, user-owned mockup or public design document. Identify available resolution and whether source assets can be used legally.
- Separate **observed** visual structure from **inferred** CSS/framework/intent. Never claim a screenshot proves its component library, author intent or exact token values.
- User-supplied screenshot/artifacts may contain identifiers, product data, brand marks and third-party rights. **Do not commit screenshots, pixel crops, extracted icons/logos, source URLs exposing private data, or renamed derivatives into public Skill repository, sample gallery or CI artifacts** without explicit user permission.
- If a source is private or auth-gated, do not bypass access control. Explain what evidence remains available, or request authorized source access.
- General knowledge (proximity, hierarchy, alignment, meaningful icon grammar, interaction patterns) may transfer; copied artwork, brands and proprietary UI source require separate authorization/license.

## Gate RL1 — Extract role and relationship, not a complete skin

For a referenced page, describe:
1. **Content/task:** Who uses the page and what action/reading objective dominates?
2. **Composition:** Where does the main subject sit, how does layout group regions, and what is first-screen information priority?
3. **Typographic roles:** Primary title/body/metadata/control, weight and line lengths at observed size.
4. **Color semantics:** Neutral surfaces, accents, status/focus—not merely memorized HEX values.
5. **Component behavior:** Distinguish observed open/selected/hover from states not visible in a static screenshot.
6. **Adaptability:** Which relationships survive a different product, language or viewport? Which imagery and exact layouts should not be copied?

Make recommendations grounded in **this target user's task**. If reference is a neat developer workspace, do not force it onto an expressive portfolio. Similarly, an experimental brand design need not become a dense administrator UI.

## Gate RL2 — Convert learning into generic, original design decisions

- Name transferable principles such as "one clear selected state," "tables with readable row density," "typography and icon optical weight should align," or "a panel's boundary must convey grouping."
- Use **new fictional content and original examples** in MauForma's own docs/assets/tests, never the user screenshot or text converted into a disguised example.
- Example SVG icons in demos must come from actual licensed open-source sources or original artwork; retain required license notices. Do not infer an icon pack from pixel appearance alone.
- Avoid using identical colors, section order, card proportions or a private page's information architecture as an implicit template for all products.
- An approved Design DNA may document observed traits and project-specific decisions **in the user's own workspace**; do not move them to the general-public Skill.

## Gate RL3 — Visual and functional verification

Use a real rendered target app to compare intended transferable principles and actual functionality. Screenshots/DOM can flag type, spacing, layering and state risks; they cannot alone prove backend actions, accessibility or source-design fidelity.

Record `observed / inferred / approved / not tested` for key aspects. Recheck relevant routes, responsive breakpoints, keyboard and high-value states. If reference comparison was only visual/static, say `NOT TESTED` for hidden interactions.

## Negative cases and legitimate exceptions

- **Bad:** User likes one product's Sidebar, so the Agent clones its colors, icon SVGs, labels and exact menu hierarchy into an unrelated SaaS.
- **Bad:** An attractive screenshot is imported as a permanent demo file in the public MauForma repository without permission.
- **Good:** Adopt the structural principle of a restrained selected background, optical icon alignment and coherent state colors; redesign actual labels and hierarchy for the new product.
- **Valid exception:** The user explicitly owns and authorizes a source design, or grants licensed asset use. Even then, preserve provenance and scope.

Related: `references/design-dna-protocol.md`, `references/icon-art-direction-gate.md`, `references/clean-enterprise-design.md`, `references/browser-qa-protocol.md`.
