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
