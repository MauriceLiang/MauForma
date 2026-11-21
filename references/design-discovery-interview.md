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


## Source-parity restoration — Explicit content-first priority and two-stage conversation

The original normative order is **website purpose and actual content → attention/visual focus → recommended visual directions → direction selected by user → targeted refinements → Design Tokens/shared components → real page implementation and acceptance**. Do not replace the user's plain-language concerns with a designer-style questionnaire.

### v6.18 — Original ownership and publication exception

If the user states the reference is their own design, respect that statement without inferring “internal corporate” or “third-party” status from its appearance. A reference supplied for analysis **does not grant consent to store or republish the image**. If the user says no image may enter the repository, forbid **originals, crops, redactions, anonymized variants, recognizable data, brands and domains** in public Skill material, examples, screenshots, PRs and commits. Extract only transferable principles via references/design-reference-learning-gate.md. Create an unrelated fictional demo. **Analysis only does not authorize edits**.

### v6.14 — Motion must have an independent user decision

For a new website, full-page redesign or substantial motion changes, if neither an inherited confirmed choice nor explicit delegation exists, **show 2–3 tangible interaction experiences and ask once**. Describe immediate static feedback, refined Buttons/Tabs/overlays and selective visual storytelling with cost and mobile/performance consequences. A request for minimal visuals **does not mean no animation**. “Develop directly” **does not mean every interaction was approved as static**. Respect confirmed/delegated/inherited; unanswered = unresolved, not “zero animation confirmed.” Even no extra motion retains selected/focus/loading/error/success feedback. Read references/motion-consent-experience-gate.md.

### Step 0 — Inspect known facts before interviewing

Read installed project routes, content, code, components, Design Tokens, actual imagery, brand rules and existing preferences. Existing approved design → ask only for truly missing constraints. Uncertain style → content-led two-stage flow. Only vague “premium / cool / minimal” → explain real compositions, not automatically glass, gradients or large radii. Explicitly delegated → choose and record provenance. Local bug or small nonvisual change → skip interview.

### Step 1 — Ask ordinary content questions, not designer jargon

Prioritize **(1) purpose and audience, (2) real content/media quality and quantity, (3) first visitor action**. One round should usually have **1–2 short natural-language questions**. When only content is missing, ask only about content. If only one essential detail is missing, ask only one. Accept conversational answers such as “coffee shop homepage with drink photos and address”; do not demand a brand-strategy form. Offer understandable content prompts only if users cannot describe their site; never invent facts.

### Step 2 — Derive the content–goal–presentation matrix

The Agent derives: main subject (photo/brand text/screenshot/operations/data/long reading), main task (attract/compare/read/operate), first focal point (image/claim/CTA/task/metric), **page-dependent** density, known media quality/quantity, motion value (advisory only) and weak-network/mobile/readability/reduced-motion constraints. Recommending “warm for all food” or “blue for all technology” without product evidence is prohibited.

Present **2–3 different suitable directions** (or a clearly best direction and meaningful alternative) and identify a grounded recommendation. Each must explicitly cover all six observable dimensions:

| Dimension required from source | Explanation for an ordinary user |
| --- | --- |
| First visual focus | The **first thing** visible: food photograph, promise, search box or task data |
| Primary composition | Full-width image, left/right split, editorial, grouped list or data grid |
| Information density | One first-screen focus or many task entries; cost of scrolling/search |
| Color/type mood | Bright/warm, calm/neutral or dark/focused without forcing a HEX |
| Motion | Quiet/static feedback, subtle controls or narrative animation and what they do |
| Tradeoffs | Visual impact vs scanning speed; motion vs performance/build cost |

Merely labeling A “premium,” B “technology,” C “minimal” **does not constitute meaningful options**.

### Step 3 — First choice is a direction, not ten parameter decisions

Offer **2–3 small candidates with genuinely different first-screen organization**. Accept “combine A and B”, “show examples”, or “choose for me.” If needed, show a short **text-only first-screen sketch**; use preview/prototype tools when available, but never claim an uncreated preview. Borrow layout/atmosphere from user references without cloning them. **Do not require primary color, 12px/16px radius or animation function selection before a direction is chosen.**

### Step 4 — Only targeted follow-up decisions after direction selection

Per round, ask **at most 1–2 necessary decisions**, with **2–3 meaningful choices** for each, and only if the result would change implementation:

- **Page-dependent density:** main image roughly two-thirds plus headline/one CTA, image-left/text-right with 2–3 advantages, or many search/filter tasks. Explain what appears first and after scrolling.
- **Composition:** single product close-up, image/text split, comparable product grid; or metric panel, compact table and task-priority navigation.
- **Color mood:** a few real product-fit combinations (cream/wood, white/fruit accent or dark/high contrast) as examples, **not mandatory brand colors**.
- **Motion:** quiet immediate states, small entrances/hover, or disciplined scroll story. Explain what visibly happens and load/mobile cost; **do not default to full-screen particles**.
- **Typography/whitespace:** controlled headline size, media-to-copy ratio and paragraph measure, not vague claims of elegance.
- **Media feasibility:** confirm actually available quality and mobile crop/readability; if missing, choose a different presentation.

Allow custom ideas, “use the recommended choice” and “you decide.” The latter must be recorded as **delegated, not confirmed**.

### Step 5 — Record choices without inventing consent

Produce a short design-confirmation summary including purpose, audience, actual assets, chosen direction, **per-page** density, focal subject, color and motion baseline, tradeoffs and unresolved issues. Record in the user's project using assets/design-brief.schema.json. The original allowed source values are **confirmed / delegated / inherited / unresolved**. The Agent's suggestion alone **must not become confirmed**; “proposed” is an internal option, not an authorized final selection.

The downstream sequence is content reconnaissance → real option selection → visual hierarchy/composition → unified Tokens → component/state showcase → business pages → motion and actual browser acceptance. A large airy brand homepage can coexist with a compact catalog and productive operations page without imposing one template across all pages.

## Source examples — full comparable decision walkthroughs

### Example A — Cake-shop brand website

- **User:** “I want a cake shop site, but don't know the visual style.”
- **First Agent question:** “Is the priority cake photos, the brand story or online ordering? Do you already have your own product photographs?”
- **User:** “I have many beautiful cake photos; I want visitors to come to the shop.”
- **Direction A (recommended, photography-led):** One nearly full-screen cake photograph, short title and **View store** CTA; spacious and visually striking, but new-product catalog does **not** all appear above the fold.
- **Direction B (editorial narrative):** Alternating large cake photos and handcraft stories, magazine-like headings; needs more substantial text.
- **Direction C (ordering-led):** Product categories, bestsellers and store/order actions up front; easier shopping but lower immediate visual impact than A.
- **After choosing A only:** Ask whether one close-up should fill the screen or occupy the **left approximately two-thirds**, with brand text on the right. Discuss color/motion later **only if necessary**.

### Example B — Repair-ticket management website

- **User:** “We need a repair-ticket admin interface and cannot name a style.”
- **Agent:** “Who uses it daily, and do they mainly check statuses, assign tickets or review performance?”
- **User:** “Support staff search every day; managers only occasionally review numbers.”
- **Derived recommendation:** **Task-first workbench**, compact search and status filter at top, actual ticket table as primary area, management analytics on a separate route. Offer **compact-efficient** and **comfortable-readable** density, explaining per-screen ticket and column differences. **Do not push an oversized marketing Hero**.

### Example C — AI coding-tool marketing site

With real terminal screenshots, feature comparisons and downloads, compare **product-screenshot-first** (real first-screen screenshot, restrained motion) against **narrative-demo-first** (scroll through workflows with greater engineering/performance cost). Explain mobile fallback and visual consequences before requesting a choice. More dialogue: examples/design-discovery-dialogues.md.

## Source anti-patterns and plain-language glossary

**Wrong:** Ask users to choose Nordic Minimal / Cyber Technology / Neumorphism / Neo-Brutalism without first explaining actual outcome; build full-screen food video without real media; offer the same big-radius Card template three times; ask twenty specialist questions at once; give an operations workbench an impractically low-density marketing Hero; or label “you decide” as “user confirmed warm colors.” **Right:** Explain actual content composition and tradeoffs, then request only genuine missing decisions. **When content and objective are already sufficient and the user requests direct execution, recommend a grounded default and proceed rather than blocking the task with interviews.**

| Design jargon | User-understandable meaning |
| --- | --- |
| Low density / generous whitespace | One main image and title on the first screen; remaining sections below scroll |
| Editorial visuals | Magazine-like large images, type contrasts and offset image/copy layout |
| Technology look | Precise lines, useful screenshots/demos, neutrals; **not automatically neon and particles** |
| Card layout | Independent blocks for scanning; too many fragment reading and work |
| Strong motion | Scroll reveals/short title entrance/image changes; explain possible performance cost |
| Mixed density | Airy homepage, denser comparable catalog, productive management screen |

### v6.4 — The user chooses distinct **layouts**, not alternative skins

After purpose/content/task discovery, sketch content priority and grayscale composition (references/composition-first-design.md). **2–3 genuinely different first-screen arrangements, primary regions or groupings** are necessary when alternatives are called for. Recoloring identical Hero + KPI Cards + Charts blue-purple, warm gray and moss green **does not count**. Explicit delegation permits internal comparison and documented delegated choice; do not force another questionnaire.

### v6.6 — User color authority remains separate

Do **not** default SaaS Sidebars to navy or gray-green. Read the approved palette across Main/Topbar. An explicit user color name or HEX must be used **as given without re-asking**. Otherwise compare **2–3 whole-page Sidebar + Main color systems**, not three isolated Sidebar swatches. An explicit “choose the colors” permits delegated choice; freedom on layout **does not grant color-change authority**, and previously confirmed HEX cannot be quietly overwritten. See references/sidebar-color-discovery.md and assets/sidebar-color-decision.schema.json.

### v6.7 — Decide navigation architecture by tasks before placement

For new/major redesigns, read top-level destinations, frequent tasks, hierarchy and main device sizes. Offer **2–3 actual architecture options** such as Top, Side, Top+Side or mobile Bottom, explaining discoverability cost and hidden-route counts. “SaaS” alone does not mandate a permanent Sidebar. Inherit specified navigation; unresolved choices require a selection or explicit delegation. **Changing navigation does not authorize a color change.** See references/navigation-architecture.md.

### v6.8 — Curate content before using whitespace as decoration

Do not ask for a global density percentage. Distinguish content retained, first-visit-only, moved to details/help and removed, explaining how each affects real tasks. A lower-density overview can coexist with denser comparison, tables and batch actions **without hiding data sources or error notices**. Reuse known constraints; density candidates may be **provisional**, not confirmed. See references/page-density-and-content-priority.md.
