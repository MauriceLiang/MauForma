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


## Source-parity requirements from the original RL0–RL4 contract

These conditions refine, and do not weaken, the gates above:

- **Ownership must not be invented.** A user may have supplied their **own original design**, a historical page, a temporary screenshot or a public example. If the user says the work is theirs, respect that description. If ownership is unknown, do not infer that the material is corporate-internal or third-party solely from the screenshot.
- **Do not publish any user's original reference image without explicit consent**, including cropped, blurred, redacted, re-encoded or Base64-embedded derivatives. The prohibition spans commits, branches, PR descriptions, GitHub Actions artifacts, README, examples, test screenshots and release packages. If the user explicitly said "do not commit this", even anonymized versions remain prohibited until that restriction is explicitly withdrawn.
- Never disclose user identity, employer, project name, URL, business data, contact details, logo or uniquely identifiable layout in public examples/commit messages/issues/CI logs. Do not include such information even as deliberately rejected test strings.
- **No proactive reverse sourcing.** Do not OCR the screenshot, download matching images, search Drive or external links for the identifiable original, or upload it again merely to save a good reference. Any future specific permission to save assets still requires confirming publication scope.
- **Licenses:** Review publicly sourced icon versions and license notices separately through official repositories. Do not extract original brands, commercial fonts, artwork or UI components from the reference. Generic public demos using MIT or other licensed icon sets must retain applicable notices.
- **Review-before-publication is a human/Agent responsibility.** A static script cannot prove that all business semantics and identifiable visuals were removed. Inspect all added files **and** PR/commit text before publication. An anonymous-looking screenshot is not proof of authorization.

### RL1 — Reference Insights Matrix (mandatory fields)

For each candidate principle, record:
observed_trait → visual_effect → task_benefit → applicable_context → constraints/tradeoffs → transfer_rule → avoid_copying.

| Transferable dimension | General observable relationship | Must be reconsidered for the new project |
| --- | --- | --- |
| Typography & Hierarchy | Natural scale and weight proportions across navigation, titles and rows; metadata does not overpower primary content | Font metrics, Chinese/English, task density, viewport, user preferences |
| Navigation & Selection | Clear current item through restrained selected background plus text/icon state | Sidebar/top/tabs; hierarchical context and unread counts |
| Icon Art Direction | Coherent contours, negative space and optical weight; matches real actions | Whether an icon is needed, brand, icon family, semantics and accessible names |
| Color Roles | Mostly neutral surfaces, limited accents and meaningful status colors | Approved brand color may not change; restraint does not mean blue or illegible contrast |
| Data Density | Table columns, row rhythm and state distinctions remain clear; avoid excessive Card-per-row patterns | Large datasets, mobile; complex Tables or content-driven Cards may be legitimate |
| Surface & Spacing | Parent layout owns spacing; container count reflects meaning | Real relationships differ among Table/List/Card/editorial sections |
| Motion & Feedback | Immediate interaction feedback; no gratuitous motion | Confirmed motion policy and OS reduced-motion preference |

For each entry, separate a **transferable principle** from an expression that **must not be copied**. For example, a restrained selected background can transfer; exact source HEX, logos, original business sections and records cannot.

### RL2 — Observe → Abstract → Recompose → Compare → Validate

1. **Observe** actual proportions, spacing, icon weight, visual rhythm and density. A screenshot alone cannot establish exact CSS values, the real component library or hidden motion.
2. **Abstract** a domain-independent design constraint; explicitly note where it would **not** apply. Do not universalize a workbench look to marketing, reading and portfolio sites.
3. **Recompose** an original demo with a **different domain, section labels, data fields and interactions**. Transfer general principles, not identifiable navigation, product flow or data layout.
4. **Compare** qualitative target effects (clarity, lightness, restraint) without aiming for pixel similarity. Independently ask whether the result still resembles a single identifiable source; redesign if it does.
5. **Validate** typography, icons, spacing, density, selected state and real-browser behavior. Passing geometry automation **does not prove aesthetic quality**; only user feedback can establish whether the proposed direction is accepted.

### RL3 — Task-scope decisions

- If the user only expresses a preference for a visual feeling, report transferable insights first; when Skill optimization is explicitly requested, contribute general principles **and newly created synthetic examples**, never automatically save the screenshot.
- Existing approved Design Tokens, product identity and UX decisions take priority. Clean Enterprise is an **optional profile**, never the mandatory default.
- Transfer **particular** useful properties across different product types, not the entire workbench composition: readable type for reading; semantic CTA/color hierarchy for commerce; reduced noise for a portfolio; do not force a Sidebar or dense tables.
- Similar visual principles do **not** require the same component library. Element Plus, Ant Design, MUI, shadcn/ui and native components can all implement them as justified by target stack and task.
- If the user authorizes **analysis only**, do not create or modify public source during the analysis.

### RL4 — Pre-publication checklist

- [ ] No original reference image or derivative, source path/data URI or screenshot artifact is introduced.
- [ ] No identifiable person, organization, product or real data; sample names, menus, fields and interactions are newly invented.
- [ ] Principles state where they apply **and do not** apply.
- [ ] Licensed third-party assets come from verified official channels, with required notices; none extracted from a screenshot.
- [ ] README, PR title/body, commits, Issues and CI logs disclose no identifying source data.
- [ ] Inherited Tokens and explicit user color/motion choices remain authoritative.
- [ ] The original synthetic demo was actually checked for reading, navigation, filtering, density, responsive and zoom states on real browser.
- [ ] When the **real target product** was not tested, label any completed checks EXAMPLE VERIFIED ONLY rather than claiming the user's app was optimized.

Source-linked resources: references/clean-enterprise-design.md (optional profile); examples/design-reference-learning/reference-principles.json (independently invented cross-product patterns); examples/clean-enterprise-demo/index.html (original fictional demo); scripts/validate_design_reference.py (static resource/contract checks); tests/design_reference_browser_smoke.mjs (synthetic browser example). 

Related: `references/design-dna-protocol.md`, `references/icon-art-direction-gate.md`, `references/clean-enterprise-design.md`, `references/browser-qa-protocol.md`.
