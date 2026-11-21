# Design Discovery Interview — Ask Only for Decisions That Matter

This guide supports new products and substantial redesigns when **product purpose, audience, authentic content or the intended visual direction** is genuinely unresolved. It does not require interviews for every small UI bug, already approved design or content-preserving polish.

## Grounding rule: user intent outranks the design questionnaire

Before asking a question, inspect what is already established in the conversation and target project: audience, page goal, current content, approved colors, typography, navigation, motion, density, technical stack, timeline and scope. Do not ask again for an answer already supplied. Distinguish `confirmed / inherited / delegated / proposed / unresolved`. A user's request to implement a feature is not automatically permission to redesign unrelated brand decisions.

Ask **one high-leverage question at a time** when one essential decision is missing. For multiple independent unknowns in a large new-product brief, gather them compactly together only when that genuinely reduces friction. Do not overwhelm users with a long design questionnaire or treat exploratory options as approval.

## Gate DD0 — Minimal product discovery brief

A meaningful first-pass brief usually needs:

| Field | What to learn | Why it affects the design |
| --- | --- | --- |
| Product and audience | What is it and who uses it? First-time/returning/admin/consumer? | Language, density, trust and task priority |
| Core job and success | What must the visitor understand, decide, read or do? | First-screen focal point and CTA |
| Authentic material | Images, product data, source text, brand, real workflows and restrictions | Prevents inventing showcase content and fake metrics |
| Pages/IA | Main routes, navigation depth, object hierarchy and content scope | Structure rather than cosmetic template |
| Visual direction | Existing brand or selected editorial/technical/playful/immersive style | Composition, color, typography and image strategy |
| Motion and behavior | Approved/delegated motion intensity, reduced-motion and critical interactions | Avoids unapproved complexity or inert controls |
| Technical boundaries | Framework, installed library, SSR, platforms, performance, licenses | Feasible components and engineering cost |
| Acceptance | Actual browser support and how to verify outcomes | No promise of unverified delivery |

A short bug fix should read the relevant known fields and proceed; it does **not** need a filled eight-field brief.

## Gate DD1 — Diagnose the actual unknown before proposing style

- If user wants a **local correction** (one misaligned Button, cropped popup or wrong label), inspect related code and affected state, patch and test; never demand a new style direction.
- If an existing product's **brand/direction is confirmed**, inherit it and review the relevant page. Don't offer alternative themes without authorization.
- If user asks **"make it nicer"** with no further detail, inspect page and its task, identify proven flaws and decide whether clarification about a major design choice is essential. Don't fabricate preferences or ask repetitive questions.
- If user requests a **new product / major overhaul** with no direction, propose 2–3 materially distinct options from its actual user job and content. Each must differ in layout/focal mechanism, not just color.
- If user has **explicitly delegated choices**, choose with recorded reasoning; a recommendation remains `delegated`, never mislabel it `confirmed`.
- User not mentioning animation does not mean user chose no animation, nor is it permission for cinematic effects. Follow the Motion Choice Gate for significant visual motion changes.

## Gate DD2 — Present design options with real tradeoffs

For each candidate, keep a short but concrete comparison:
- **First-screen subject and order:** What is central, and what appears before/after?
- **Page grammar:** Editorial flow, product media, dashboard, split editor, guided learning, storefront, canvas or another product-fit composition.
- **Typography and color relationship:** Brand, semantic color, body legibility and distinct type roles; no mandatory blue/purple theme.
- **Media and assets:** Available photography/screenshots/diagrams, quality, licensing and fallback when missing.
- **Interaction and motion:** One purposeful signature where justified, component state feedback, accessibility, interruption, reduced motion and performance cost.
- **What each option sacrifices:** Density versus expressiveness, build complexity versus flexibility, supported devices and maintenance.

Do not show three colored versions of the same Card grid. A project's actual purpose may justify one obvious direction; do not manufacture alternatives or seek reconfirmation merely to satisfy a process template.

## Gate DD3 — Ownership of approval

**The user owns the final decisions.** Present an Agent preference as a recommendation with reasons and limitations; only explicit confirmation or delegated authority allows implementation as selected design. Preserve exact user-selected HEX, navigation type, allowed visual style and declared supported devices.

- `confirmed`: User explicitly approved or selected.
- `inherited`: Established and approved system already exists.
- `delegated`: User explicitly entrusted this decision to the Agent.
- `proposed`: Agent candidate, not yet selected.
- `unresolved`: Evidence missing or a real conflict remains.

If a user's existing decision conflicts with a technical accessibility issue, explain the conflict and propose compatible changes around the protected choice. Do not silently overwrite it. Only ask a blocking clarifying question where the real implementation cannot proceed sensibly without a decision.

## Gate DD4 — Convert choice into an implementable brief

After an authorized decision, capture a concise **design direction record** in the target project, not this public Skill:
- Audience/task/first-screen focus and current page mode (`Operate / Read / Persuade / Experience`);
- Approved/inherited constraints, real assets/data and exclusions;
- Structural composition, navigation strategy, density and accessibility;
- Primary UI library/primitive stack and token roles consistent with actual framework;
- Motion authority and components needing continuity;
- Supported viewports, responsive transformation and browser/real-action tests;
- Explicit unresolved assumptions and what needs further evidence.

A design direction is not complete when only colors and radius are specified. It must connect actual content, actions, layout and verification.

## Gate DD5 — Acceptance and feedback

Use the approved brief to inspect **real target pages**, not synthetic demo pages alone. Confirm first-glance meaning, primary task, copy and media fidelity, proper component states, keyboard/focus, actual responsive scope, reduced-motion behavior and backend outcomes where applicable. Compare user-approved decision versus render; revise with actual feedback.

If user rejects an option, update decision status rather than arguing that an Agent favorite is objectively better. A screenshot or a color palette alone does not establish user satisfaction, platform compatibility or engineering completeness.

## Example questions (adapt, do not quote mechanically)

- For a brand website with genuine missing direction: “Should the first screen highlight a real product photograph, an editorial promise, or an interactive product demonstration? These produce different navigation and media requirements.”
- For a data tool with no approved emphasis: “Which task should be visible without scrolling: filter and inspect current failures, compare several projects, or open an existing analysis?”
- For a major motion overhaul with unknown authorization: “Do you want immediate quiet updates, subtle fluid component changes, or richer storytelling effects? I can recommend one for this product, but the choice remains yours.”

These are **not forms to show indiscriminately**. For established projects, read existing choices and proceed. For review-only requests, deliver critique; do not modify the code.

Related: `references/product-experience-routing-gate.md`, `references/design-style-catalog.md`, `references/art-direction-critique.md`, `references/motion-consent-experience-gate.md`, `references/semantic-boundaries.en.md`.
