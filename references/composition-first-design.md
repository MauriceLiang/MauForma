# Composition First — Solve Layout, Content and Information Priority Before Decoration

This gate governs new Web products, major visual redesigns, and pages whose information hierarchy is structurally wrong. **Do not apply a full composition exercise to a narrowly scoped functional bug or overwrite an approved design without authorization.**

## Why composition comes first

A familiar AI-generated result is a centered heading with decorative category text, four equivalent statistic Cards, two unrelated chart Cards and a large empty Hero or footer. Recoloring, adding blur/glow or changing radius produces variations of **the same layout failure**. Composition addresses **what occupies the viewport, its size and order, how regions relate, and why**.

The framework or component library does not determine composition. A page can use Vue/React, Ant Design or headless primitives while still choosing its own information priority. Do not impose the same sidebar+KPI template across Work, Read, Persuade and Experience.

## Gate C0 — Establish the actual first-screen subject

Before CSS, record a short composition brief:

| Question | Required answer |
| --- | --- |
| Audience and page mode | Who is this for, and is the job to Operate, Read, Persuade or Experience? |
| First-screen subject | Which real product, article, data result, task or artwork deserves attention? |
| Primary action | What should the user do next? Where does it appear? |
| Authentic content | Which data, images, text and constraints exist? Which are unknown or missing? |
| Page structure | Which regions need to be side-by-side, grouped, sequential or revealed later? |
| Inherited constraints | Approved brand, navigation, density, target viewport, actual component stack |
| Evidence | What comes from real code/content, screenshots, approved decisions or unverified assumptions? |

Do not invent hero images, KPI numbers, positive findings, sample sizes or user testimonials solely to fill a concept. A missing authentic asset can justify a different composition or an explicit placeholder **labeled as such**, not a fake success claim.

## Gate C1 — Region map before visual skin

1. Make a **grayscale wireframe** of major regions. For each, specify real purpose, approximate relative visual area, alignment, reading order and primary/secondary action.
2. Classify content `primary / supporting / conditional / deferred / removable` using `references/page-density-and-content-priority.md`. Remove redundant explanatory categories and decorative wrappers before allocating space.
3. Identify **one principal focal region** unless multiple coequal tasks have a real reason. A massive ornamental H1 can be less important than the object, filter, error or product photo; do not assume semantic HTML `h1` must be the biggest shape.
4. Choose a layout grammar suited to content: open editorial flow, full-bleed media, split stage, task-first workspace, aligned data grid, comparison matrix, object gallery, deliberate asymmetry or another justified form.
5. Organize **actual relationships**: Inside, Peer, Section, Connected, Anchored or editorial variants from Semantic Spacing Rhythm. Do not treat a Card around every block as design.
6. Check first, middle and end of the page. A strong Hero with broken scroll, clipped final content or unrelated lower sections is not a successful page.

## Gate C2 — Truly different design directions when needed

For an unresolved new product or authorized **major** redesign, offer **2–3 materially different** directions. A different color/gradient/font on the same Card grid is **not** a different direction.

For each candidate, explain:

- **Dominant region and geometry:** Is it media-led, typographic, task-first or data-first? How much space is used for navigation, actual content, utility and intentional rest?
- **Reading/action order:** What does the user see in the first three seconds and do next?
- **Real assets/content:** Which input makes this design credible? What remains when media/JavaScript/data is missing?
- **Navigation and responsive transformation:** What becomes a column, drawer, scroll region or lower-priority entry at the actual supported breakpoints?
- **Visual treatment only after structure:** Type role, surface hierarchy, brand accents and approved motion.
- **Tradeoffs:** Accessibility, complexity, performance, maintenance, density and what each alternative deliberately rejects.

Approved existing designs need no fake multi-choice exercise; a precise local fix can preserve the established composition. An Agent suggestion is `proposed`, not `confirmed`.

## Gate C3 — Distinguish product modes by task, not template

- **Operate:** Current object, filters, actionable records and error/retry may deserve the first viewport. Dense is allowed, illegible is not. Do not erect a marketing Hero over a data table.
- **Read:** Readable prose, chapter/navigation and visual examples determine rhythm. White space helps comprehension; Cards are not required per paragraph.
- **Persuade:** Real product photography/media, claim, trust, price/spec restrictions and CTA form an intentional story. A bold Hero is legitimate when it supports truth and conversion.
- **Experience:** Art/media and user-controlled exploration may lead. Keep accessible controls and an exit; expressive asymmetry and signature motion may be appropriate with approval.

One product can mix modes across routes with shared tokens. Do not carry Operate's panel density into a creative portfolio or impose cinematic scroll on every admin dialog.

## Gate C4 — Composition quality review, then detailed craft

Run a **content/grayscale substitution test**: Temporarily remove gradients, shadows and saturated accent. Is the task subject still clear? If all copy could be replaced with unrelated SaaS terms without affecting layout, reconsider whether architecture is generic.

Before coding or bulk component duplication, reject:
- A decorative label + oversized heading that pushes true interaction away;
- Giant empty panel wrappers, Card-inside-Card scaffolding and repeated navigation links;
- Multiple equally dominant regions with no actual priority;
- Tiny key chart labels or data beside oversized decorative copy;
- Random two-column geometry with no shared grid/tracks or deliberately justified asymmetry;
- Missing content, unsupported Mock data, hidden important states or non-scrollable final items.

Then pass to component ownership, semantic Tokens, typography and motion. A visually attractive screenshot does not prove backend save, accessibility or interaction behavior. Verify actual routes/states at consistent viewport and data.

## Acceptance record

Use a concise record: `page | user task | source/evidence | first-screen focus | primary action | content disposition | chosen structure | rejected alternative | actual browser verification`.

A synthetic wireframe, variant preview or screenshot-only inference is **not** `VERIFIED`. For real modifications, compare before/after on the actual app, including relevant responsive/dark/light, focus and scroll-end states.

Related: `references/product-experience-routing-gate.md`, `references/perceptual-hierarchy-gate.md`, `references/page-density-and-content-priority.md`, `references/visual-critique-loop.md`, `references/design-system.md`.


## Original Gate A0 — Required content evidence ledger for new/major layout work

This supplements Gate C0 above, **not optional for a new page or major layout redesign**:

| Source field | Question that must be answered |
| --- | --- |
| **Task** | What is the primary purpose of this **specific route**: learn the product, read trends, filter or decide? |
| **Actual content** | Which real features, titles, charts, Tables, metrics, media and explanations exist now? |
| **Data confidence** | For each value record **known** (grounded), **demo** (explicitly labeled), or **unverified** (**never presented as measured fact**) |
| **Main visual** | Which content itself deserves area: photography, artwork, **true data trend**, task queue or article? |
| **Constraints** | Existing components/brand, media quality, supported viewport, keyboard, responsive and performance limits |

Do not decide composition solely because the product is called SaaS. For example, a repository-analysis detail page is mainly Operate/Read, while its marketing homepage may be Persuade with a valid Hero and illustration.

## Original Gate A1 — Five grayscale-wireframe duties

1. Identify the primary read/action path, e.g. **repository → significant change → trend evidence → issue/PR detail**.
2. Build a **no-color, no-illustration, no-shadow** text wireframe or grayscale HTML first.
3. Tag **each visible region** with real content ID, primary/secondary status, above-fold visibility, expected area/density and **loading/empty states**.
4. Explain visual rhythm: where density is needed, where data needs breathing space, and why Sidebars, Cards or columns exist.
5. Only after structure works choose **color, type, detail and motion**.

**Removal-of-decoration test:** If gradients, glowing orbs, 3D art, shadows and colored statistic icons vanish, can the user still understand and complete the main first-screen task quickly? If not, **return to composition**, not another gradient.

## Original Gate A2 — Distinct comparison patterns and decision ownership

For new or major visual redesign, **prefer 2–3 genuinely distinct compositions** and record them at **design-system/composition-brief.json**. Original illustrative directions:

- **Trend-first** — Primary trend takes the stage; four **necessary** metrics form a compact row, insight is attached to trend or below.
- **Investigation-first** — Relevant Issue/PR changes and investigation list lead, with curves as secondary evidence.
- **Summary-first** — Critical changes and segmented summaries first; chart and list become the next drill-down path.

For each candidate record **first visible subject, primary region location/size, above-fold content, interaction starting point, media/data relationship, cost, mobile reading order and why it fits the actual content**. Recoloring an unchanged layout/radius/shadow/icon/Hero copy does not create a new composition.

**Exception:** Existing approved composition or localized repair need not present three alternatives. Explicit “design freely” is a **delegated** choice: Agent compares alternatives internally and selects with evidence, rather than stopping for endless confirmation. When the user explicitly wants to choose, show options with differences and rationale before recording their decision.

## Original Gate A3 — Product/data truth before proportional aesthetics

- On Operate views, keep page identity, object selection, refresh and title in compact task context; **do not automatically add a 300px-tall brand Hero**.
- A huge chart region without real data must show an **explicit loading / failed / no-data state**. A blank white panel cannot count as completed visualization.
- Insights belong near or linked to actual data evidence. A bright-blue marketing Card is **not** a substitute for analysis.
- First-screen area should prioritize actionable content. Explain the value of any enormous region instead of filling it with illustration.
- Keep true data, Mock/demo and textual inference separate. A claimed **92% coverage** without a source is not a measured fact.
- Do not force equal-sized dashboard Cards. Depending on the actual question, fewer Cards, no Cards or a compact metrics row may be right.

## Original Gate A4 — Style after composition, never “SaaS implies blue-purple”

Read references/palette-art-direction.md for brand-semantic color roles and **why the palette serves this product**. Blue/purple is valid **if inherited from brand, suited to an actual technological identity, explicitly chosen by the user, or justified by the design strategy**. A component library's default theme, a purple reference site or a common generated template **is not sufficient reason**. The rule does **not** ban distinctive, experimental, colorful sites or all Heroes; adapt to actual **Persuade / Operate / Read / Experience** subject.

## Original structured deliverables, tests and blocking conditions

- **assets/composition-brief.schema.json** defines plan records and evidence; passing its schema does **not** certify design quality.
- **examples/composition/repo-analysis.json** contains **three genuinely distinct** repository-analysis arrangements; all simulated values are marked **demo**.
- **scripts/validate_composition_brief.py** provides dependency-free checks of content citation, candidate differentiation, decision provenance and certain structural anomalies; **cannot replace expert screenshot critique**.
- **assets/composition-layout-lab.html** is a static concept comparison with **no real backend**; never claim that running it proves the user's app works.
- Example command to understand the contract, **not to copy demo values into business charts**: python3 scripts/validate_composition_brief.py examples/composition/repo-analysis.json.
- Recommended procedure: inspect the example, then create a **separate brief in the user's project**.

**Gate A fails:** An Operate first screen devotes materially more area to decorative Hero/illustrations than its main data, displays an empty primary chart without visible state, or relies on color instead of a coherent task structure. **Rebalance actual regions first**, then write theme/component code. See references/visual-critique-loop.md.

## Original content-curation and Grid/scroll-end extensions

**Before grayscale layout, ask whether a section belongs on this route at all.** Via references/page-density-and-content-priority.md, classify each whole section as primary/supporting/conditional/deferred/removed. Remove or defer repeated tutorials, feature directory and competing CTAs **before** dressing them with prettier Cards. Overview may be spacious while analysis/management are denser, **without hiding charts, sources or statuses**. See references/whitespace-and-surface-composition.md.

On the grayscale design identify **shared container bounds, columns and common starting row for peer Panels**. For analytical layouts, do not default to independent left/right vertical stacks that cause row two to start at different heights. Proportions like **3:2, 8:4 or a full-width primary chart** may be justified by data priority; Masonry is for fitting photo/editorial tasks. Specify **actual scroll owner, final padding and fixed toolbar** during design. Content **must be reachable at the last row**, not forced entirely above the fold. See references/grid-alignment-and-viewport-safety.md.
