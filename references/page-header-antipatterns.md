# Page Header Copy Necessity and Functional-Page Anti-Patterns

> **Scope:** Creating, polishing, refactoring and reviewing *any* Web page, especially legacy explanatory text that predates the current change. Task-oriented pages use strict Gate H0; presentation, learning, scientific, reading, marketing and creative pages use universal Gate H-Base. Do not impose one Hero composition or heading density on every product.
>
> **Purpose:** Remove title preambles without information value, while preserving real navigation, approved brand narrative, legitimate chapters, necessary states and sources. Historical presence is not proof of a valid information role. H-Base/H0 focuses primarily on H1: **every H1–H6, Card, Section, Dialog and custom heading group must also pass [Title-Prefix Role Gate](title-prefix-role-gate.md).**

## Gate H-S — Default to one self-sufficient heading

For **all title levels and page modes**, begin with a direct title that tells the reader what the page, section or object is. **Do not add a second pre-title layer by default**, and do not preserve inherited explanatory labels merely because they already exist. Test whether removing the pretitle loses independently necessary information not already supplied by the heading or surrounding navigation, data and controls. If nothing important is lost, DELETE. This is a stronger default than finding a plausible-sounding reason to KEEP. "Provides context", "creates a premium feeling" and "adds visual hierarchy" alone are not sufficient justifications.

If information *is* lost, first move it to the correct owner (breadcrumb, chapter/stepper, status, source, scope, below-title instructions). KEEP above the title only with evidence of both independent information value **and a specific need for that placement**. Intentional approved narrative, legitimate chapters and real navigable hierarchy remain possible. See `references/title-prefix-role-gate.md` (Gate H-S) for the evidence and completion contract, including H2–H6 and Card/Section/Dialog titles.

## Gate H-Base — Mandatory review of existing and new title copy on every page

**Trigger:** Any new page design, visual polish/refactor, heading/Hero-related fix or page review. A vague request to polish an existing product also triggers this audit. A purely functional bug completely unrelated to titles does *not* require site-wide heading cleanup. Examine **actually rendered content first**, then locate its origin in PageHeader props, Hero/Intro components, localization strings or slots; do not depend on a literal `h1` or `eyebrow` class.

**Review candidates:** A short line above or near a main/hero title, below a logo, in English, Chinese or mixed language, widely tracked capital letters, pseudo-category, ornamental index or suspicious subtitle. Include **already present** and **new** instances. “This JSX/Vue component was untouched” and “it was in the original design” are not exemptions.

For each candidate, decide `keep / merge / move / delete` with a reason, using this order; resolve genuine ambiguity from brand/content records rather than removing text based solely on color, capitalization or placement:

1. **Authentic identity and official brand:** Real product name, logo, user-approved tagline or branded series can be kept or moved to a separate identity region. **Split** a mixed “brand name · disposable generic explanation”; never preserve/delete the entire line without separate decisions.
2. **Navigation and state:** A usable breadcrumb, real content hierarchy, course chapter, time range, permission or data status should be kept or moved to the relevant navigation/section/data area. Do not erase necessary meaning.
3. **Content and narrative:** Editorial, marketing, learning, creative and scientific kickers may be kept *when they genuinely establish narrative progression or content positioning*. Be able to explain the added user value. A vague claim of “premium visual style” does not excuse generic function labels.
4. **Duplication/filler:** A repeated H1, literal second-language translation, “this page is for…,” Mock/development label, abstract slogan or invented order number should normally be deleted. Incremental but misplaced information should move below the title or to its owning module; merge if appropriate.

**No cosmetic evasion:** Lower opacity, smaller font, rewritten words, moving the pretitle to the same visual layer, or styling unrelated parts of old code do not fix the underlying issue. Run a **before → decision → after** check on affected pages and states, including a real desktop initial viewport when supported. Without browser access, accurately label `STATIC CHECK` or `NOT TESTED`; do not claim visual verification. This is an **Agent/human semantic review**. Keyword scripts produce candidates, never final brand judgments or automatic mass deletion.

### Synthetic examples across product modes — not actual user products

These examples only express classification decisions. Structured regression fixtures live at `assets/page-header-copy-cases.json` and `scripts/validate_page_header_copy.py`; neither proves actual brand or page correctness.

| Example page | Pre-title → title | Decision | Reason |
| --- | --- | --- | --- |
| Existing learning page | `LEARNING SPACE · Courses` → `Start learning` | delete | Only names the general page category; legacy status grants no exemption |
| Existing scientific visualizer | `VISUAL LAB · Discovery` → `Observe cells` | delete | Repeats domain with no independent information |
| Data workspace | `LIVE INSIGHTS` → `Statistics overview` | delete + Gate H0 | Explanatory label |
| Branded event home | approved `MAKE TOMORROW TANGIBLE` → event name | keep | Documented brand/narrative role |
| Product page | `NOVA · Data visualization` → page title | split / move | Preserve real NOVA identity in brand area, remove generic explanatory part |
| Reading content | `Chapter 03 / Circulatory system` → chapter heading | keep | Genuine chapter sequence |
| Functional page | `Settings / Team` → `Permissions` | keep as nav | Real and usable breadcrumb |
| Data page | `Sample: 2025–2026` → trend title | move | Useful scope information belongs beside relevant data/filter |

## Gate H0 — Default hard prohibition of explanatory pre-H1 eyebrows on task pages

**Applies to:** admin, data, workbench, settings, search, lists, edit and detail pages. During first-pass implementation and existing-page polish/refactor, **do not add or retain** an explanatory eyebrow/overline/kicker, all-caps wide-tracking label, colorful function annotation or decorative number above H1. Even if it does not repeat H1 verbatim, remove it when its only role is to describe the page type, scenario or technology and manufacture an extra title layer. The specific color or font is irrelevant.

**Synthetic violations:** `EXPLORATION MODE · WEEKLY SIGNALS` → `Activity workspace`; `TEAM ACTIVITY / INSIGHT VIEW` → `Project overview`; `01 / OVERVIEW` → `Overview`. The correct version starts from a clear H1.

**Recommended order:** actual breadcrumb (if any) → H1 → necessary *incremental* short explanation and nearby actions (if any) → real page content. Put data versions, time windows, sources, permission and status near their owning filters, charts or indicators; do not disguise them as pre-H1 filler.

**Exceptions:** Actual navigable breadcrumbs, approved official taglines, genuinely meaningful brand/marketing kickers and authentic statuses are not decoration. They do not authorize invented English phrases on routine functional pages. Even when a component exposes `eyebrow`/`overline` props, a task-oriented `UiPageHeader` must not fill or render them by default. Decreasing their color intensity or font size is not a fix.

**Verification:** Check rendered DOM and visual appearance for *every affected task page*, including inherited pre-H1 explanations. Fix and recheck when found; do not wait for the user to identify it or use unchanged source as a defense. Static hints never automatically delete legitimate navigation or necessary state.

## Synthetic first-screen counterexample

A fictional admin header shows a colorful small category label **“Accounts & Permissions”**, then an oversized **“User Management”** H1 and a large gray description **“Manage user accounts and view or change module access permissions.”** The title area consumes nearly the entire first viewport.

- **Defect:** A routine operational screen imitates a marketing Hero; the category and H1 overlap semantically, a self-evident function gets a lengthy description, and actual content/actions are pushed below the fold.
- **Preferred:** A direct “User Management” heading with an optional brief *incremental* description and the “Add User” action nearby; toolbar, filters and list directly below.
- **Allowed exception:** If “Accounts & Permissions” is a real hierarchy, use an actual `Accounts & Permissions / User Management` breadcrumb instead of a decorative colored label. Complex permission logic may justify brief help at its corresponding operation.

## Anti-pattern library: bad → reason → correct

### H01 — False hierarchy: ornamental eyebrow above a heading

- **Bad:** “Accounts & Permissions” in small colored text before a huge “User Management”; no usable path.
- **Good:** One direct “User Management” H1; if a hierarchy actually exists, a breadcrumb such as `Settings / Accounts & Permissions / User Management`.
- **Test:** Does removing the small line lose any orientation information? If not, remove it.

### H02 — Forced second-language translation or invented English slogan

- **Bad:** `USER MANAGEMENT` above a Chinese “用户管理”; or `SMART WORKSPACE / MANAGE EVERYTHING` above a generic list title. These repeat meaning and waste hierarchy.
- **Good:** On a Chinese-language product, show the functional heading directly in Chinese. English is warranted for genuine proper nouns, technical terms or an explicit multilingual requirement.
- **Test:** Does English add distinct identity, branding or professional meaning? Otherwise delete it.

### H03 — Marketing Hero transplanted into a CRUD screen

- **Bad:** An 84px operational heading, 180px vertical whitespace and giant gradient typography; actions appear only after scrolling.
- **Good:** Dense desktop/admin headers are often about 24–32px, *adjusted to actual project and viewport rather than fixed*. Show core actions and some actual content without scrolling.
- **Test:** Are primary actions visible at typical laptop heights?

### H04 — Self-evident and lengthy descriptions

- **Bad:** “Welcome to the User Management Center. Here you can easily manage users and flexibly adjust permissions.”
- **Good:** No description when it adds nothing; “Manage members and module permissions” only if genuinely informative. Link complex rules or present help near relevant operations.
- **Test:** Does the help explain a constraint, scope, dangerous action or otherwise non-obvious rule?

### H05 — Huge distance from title to actions and table

- **Bad:** Heading → empty space → ornamental card → three lines of marketing text → Add User button → actual table.
- **Good:** Main action near `UiPageHeader`, followed closely by search/filter toolbar and list.
- **Test:** How much irrelevant content must be skipped before the primary task?

### H06 — Needless nested giant Cards

- **Bad:** Whole-page white Card containing another header Card, search Card and data Card, each with 32px corners and heavy shadow.
- **Good:** Title directly in content area; use `UiPanel` when a boundary actually aids comprehension. Lists often need only separators and spacing.
- **Test:** Can an outer Card disappear without losing meaningful grouping?

### H07 — Excessive gradient and saturated accent on all titles

- **Bad:** Pink-purple gradient for every settings H1 while nav, breadcrumb, buttons and table headings all demand high attention.
- **Good:** Theme accents convey action and state; task-page heading usually uses the main text color. Brand/showcase pages may intentionally use gradients.
- **Test:** Is accent attention directed to the primary interaction rather than mere words?

### H08 — Identical generic Hero copy on every route

- **Bad:** “Workspace / Make collaboration easier,” “Members / Empower teams,” “Logs / Understand every moment,” all using eyebrow + enormous H1 + empty slogan.
- **Good:** Title states the real task; necessary help varies with each page. Shared components unify look without imposing the same copy arrangement.
- **Test:** Can the template be reused by changing only the page name? If so, the information design is likely generic.

### H09 — Several equal-weight primary actions compete

- **Bad:** “Add,” “Import” and “Export” are equally filled dominant buttons in the title area.
- **Good:** One clear primary action, others secondary or inside a menu; weigh frequency and risk.
- **Test:** Can the user identify the next important action within a second?

### H10 — Arbitrarily extreme title typography in pursuit of “premium” feel

- **Bad:** 84px heading with 24px explanation while real list text falls to 12px.
- **Good:** Type sizes reflect page intent and information density; body text remains readable; analogous task pages share a coherent type scale.
- **Test:** Does purely decorative typography consume all first-screen attention?

### H11 — Repeating the same heading at three nested levels

- **Bad:** Hero “User Management,” Panel “User Management,” Card “User Management,” with no distinct role.
- **Good:** H1 “User Management,” table section “User list,” detail panel “Member information.”
- **Exception:** Breadcrumb terminal item and page H1 (or active sidebar item) may validly share names; do not misclassify genuine navigation.

### H12 — Critical information buried in a long subtitle

- **Bad:** “Access Control” with a paragraph that mentions “Only admins can edit” only at the end.
- **Good:** Make the authorization restriction visible next to the relevant action; e.g., “Admins only” in an actionable location.
- **Test:** Can the user see important restrictions before attempting the action?

### H13 — Icons and badges pretending to add information

- **Bad:** Rockets/stars/lightning and `NEW`, `PRO`, `POWERED BY AI` labels without a real product status.
- **Good:** Icons identify objects, navigation or state. Remove badges without genuine meaning.
- **Test:** Can the icon/badge's function, actual status or deliberate brand purpose be explained?

### H14 — Wrong platform/density assumptions

- **Bad:** A small Mac/Windows settings panel copies a giant Web Hero and pushes options out of its window.
- **Good:** Match the platform and container's density, using a compact `UiPageHeader` and grouped headings. Keep real actions visible in narrow windows.
- **Test:** Does the smaller window preserve reachable controls, full text and sensible focus order?

## Recommended shared component: UiPageHeader

| Input | Purpose | Default policy |
| --- | --- | --- |
| `title` | Actual page task heading | One visible H1, unless the host has already supplied it |
| `eyebrow` / `overline` / `kicker` | Decorative pretitle | **Never auto-render in task-oriented PageHeaders** |
| `description?` | Optional incremental help | Omit if it contains no new information |
| `breadcrumbs?` | Real navigation hierarchy | Breadcrumbs are navigation, not eyebrow decoration |
| `actions` slot | Primary/secondary actions | Position with the title; prefer shared UiButton |
| `density` | compact / comfortable | Admin/desktop often compact, showcase may use a separate Hero |

**Preferred synthetic Vue structure:**

```vue
<UiPageHeader title="User Management" density="compact">
  <template #actions>
    <UiButton variant="primary" @click="createUser">Add User</UiButton>
  </template>
</UiPageHeader>
<SearchToolbar />
<UserTable />
```

**Bad synthetic structure:**

```vue
<div class="huge-gradient-hero">
  <span class="english-eyebrow">USER MANAGEMENT</span>
  <h1>User Management</h1>
  <p>Make every account easier to manage!</p>
</div>
<!-- A long scroll is required to reach the actual list. -->
```

## Agent checklist — Gate H-Base on every page, then H0 on task pages

- [ ] Inspected existing **and** new pre-title copy, not only changed diff lines?
- [ ] Distinguished official brand, real navigation/data status and useful narrative from decorative function labels?
- [ ] Split mixed brand/description lines rather than blindly keeping or removing the entire string?
- [ ] Revisited original findings in real rendered states; labeled static/unavailable cases accurately?
- [ ] Main H1 directly describes the task, with one primary page heading by default?
- [ ] **H0 first-pass blocker:** No explanatory eyebrow, generic English label or invented chapter number before an operational H1, even when wording differs from H1?
- [ ] A smaller line genuinely provides navigation rather than a second headline with different styling?
- [ ] Help copy adds real information rather than repeating the function?
- [ ] First viewport includes important actions and some real data or an accurate state?
- [ ] Title, actions, toolbar and content are ordered closely by task sequence?
- [ ] Analogous functional pages share `UiPageHeader` (or equivalent) and coherent typography?
- [ ] Avoided nested panel shells and arbitrary radius/alignment/spacing drift?
- [ ] Avoided applying marketing Hero rules to administrative screens?
- [ ] Any retained English words, paragraphs, breadcrumbs or oversized titles have a verified product reason?

Multiple H01/H02/H03/H05/H08 symptoms on a task page indicate a **high-priority information architecture defect**, not a trivial aesthetic preference. Never indiscriminately shrink or erase legitimate information; preserve readability, navigation and help.

Visual comparison: `assets/page-header-antipattern-gallery.html` (standalone offline, responsive, 14 synthetic side-by-side examples).

## Additional anti-patterns H15–H20

### H15 — Generated English subheading under a brand name
- **Bad:** `Product / INSIGHT AREA` without a confirmed sub-brand or distinct value.
- **Good:** Keep genuine product name only; official product series and approved taglines may remain.

### H16 — Repeating the same idea at four title levels
- **Bad:** `Repository activity & collaboration · interactive prototype` → `See how projects evolve` → `01 / Overview` → `Start with activity, then follow evidence`, while the real main chart is called “Development activity.”
- **Good:** Choose a clear PageTitle, true repository identity and functional SectionTitle; delete redundant meta-explanations. Actual breadcrumb and data source remain valid.

### H17 — Decorative index without genuine order
- **Bad:** `01 / XX` on every unrelated section for visual rhythm.
- **Good:** Preserve numbering only where documents, steps or timeline items genuinely follow an order.

### H18 — Implementation notes leaking into product copy
- **Bad:** `Main chart retains native ECharts tooltip, zoom and selection`.
- **Good:** Say “Drag to choose the time range” only if that user action truly exists. Keep implementation notes in PRs, tests or technical docs.

### H19 — Huge slogan alongside tiny chart labels
- **Bad:** An abstract 40–60px operational H1 while chart ticks, sample n and KPI labels shrink to faint 10px.
- **Good:** Role-based typography and actual importance determine hierarchy. `typography-hierarchy.md` suggests starting ranges, never universal fixed pixels.

### H20 — “Minimal” taken to mean illegible metadata
- **Bad:** Important source, n, UTC or legend text all rendered at unreadably low contrast.
- **Good:** Keep data limitations legible; check applicable WCAG contrast and zoom on real screens.

Use with [semantic copy hygiene](semantic-copy-hygiene.md) and [typography hierarchy](typography-hierarchy.md). **Static detection supplies candidates only; all pages require H-Base, and task pages additionally require strict H0.**
