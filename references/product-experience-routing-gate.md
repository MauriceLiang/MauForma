# Product Experience Routing Gate — Identify the Product Before Designing the Experience (v6.21)

MauForma does not infer layout solely from labels (“Dashboard/Home/Table”) or the four `Persuade / Operate / Read / Experience` modes. Keep page modes, but when building a new site, redesigning core pages or responding to vague “optimize product experience” requests, **identify product type, user task and information architecture first**. Do not default every site to an admin dashboard.

## PX0 — Scope, evidence and decision precedence

- New site, whole-site redesign or structurally broken core page: run PX1 → PX2 → PX3 → PX4 before choosing composition, tokens and components.
- Small component, bug or spacing fix in an approved design: inherit the design and gather only necessary context; do not independently redesign information architecture.
- Review/document only: provide grounded findings and recommendations, **without editing source**.
- Decision order: explicit user requirements and approved design > verifiable research/running evidence > actual business materials > Agent proposals. A recommendation is not confirmation.
- Screenshots cannot establish code, framework, brand ownership or user behavioral data. Do not add reference images to repository or recreate an identifiable example without authorization. See `references/design-reference-learning-gate.md`.

## PX1 — Two axes: product experience category × current page task

| Product experience | Main user goal | Content that deserves priority | Common failure |
| --- | --- | --- | --- |
| Admin / Operations | Diagnose anomalies, filter, batch-act, maintain accountability | Real tasks, status, permissions, filters and context | Huge ornamental Hero obscures tasks |
| Consumer Utility | Quickly accomplish personal task, resume recent state | Current action/context and clear outcome | Copying enterprise KPI dashboards |
| Learning / Education | Learn, practice, receive feedback, retain progress | Next learning task, steps, progress and feedback | Admin template with “project” replaced by “course” |
| Content / Media | Discover, select, read/watch | Content, search/recommendations, source and context | Card-only page with no discovery mechanism |
| Commerce | Compare/buy and track orders | Products, price, availability and trust | Every CTA competing equally |
| Creative Tool | Edit, save, preview and publish | Work object, tools and save state | Marketing Cards crowd the canvas |
| Marketing / Portfolio | Understand value, work and reason to act | Portfolio/claim, credible evidence, CTA | Default sidebar + stats Cards |

One product may include multiple types: a learning site's public catalog is Content, its exercise is Learning, personal preferences are Utility, and authorized admin is Operations. **Login or a sidebar does not make the whole product an admin system.**

The second axis remains page modes `Persuade / Operate / Read / Experience`: a consumer learning home can be Learning × Operate/Experience, while admin alerts are Admin × Operate. They can share Buttons and Lists without having identical home-page IA.

### Settings / Form / Hybrid subregions (v6.22)

After product classification, select layout by **actual save/submit unit**. Independent short settings use left-label/right-control rows; multi-field transaction forms use stacked label-above-Input; hybrids divide by subregion. This does not replace product or page mode. Preserve dangerous-operation separation, error messaging, responsiveness and accepted existing design. See `references/settings-form-layout-gate.md`.

## PX2 — UX-first IA gate

Before structuring a new page, prepare a compact **Page Purpose Card**:

| Field | Question that must be answered |
| --- | --- |
| Audience/context | Who uses it? First visit, return, creation, administration or another state? |
| User job | Why open this route now, and which *real* task must be completed? |
| Primary/secondary action | What first, what next? Do actions compete? |
| Needed evidence | Which genuine content, data and state support the decision? |
| Journey/recovery | Where after completion, back, error, empty or insufficient permission? |
| Success | What behavior and feedback prove completion? Which assumptions still need validation? |

Also record first-screen **three likely first-glance elements**, and their relation to the task. Do not invent metrics, badges or arbitrary task counts to fill blank space; content determines whitespace/density.

### Generic-template swap test — heuristic, not a verdict

If replacing “learn/course/review” with “issue/project/task” leaves all priorities/behavior unchanged, the layout **may** lack product-specific content and actions. Inspect task, path and feedback rather than injecting gamification, illustration or flashy Cards merely for differentiation.

## PX3 — Structure before skin

- For new products or **structurally failed** core pages, compare **at least two materially distinct IA candidates**, such as next-task-driven vs content-exploration-driven. Explain audience, first-screen order, navigation, available data, interaction cost and mobile layout.
- Candidates must differ in focal subject, task order or area organization—not just white/blue palettes, radius or icon family.
- An approved layout with a local flaw does not need forced multi-option exploration. Do not overturn a sound workflow without authorization.
- Review UX first; then use `references/composition-first-design.md`, `references/navigation-architecture.md`, `references/page-density-and-content-priority.md`, design tokens and shared components.
- Never automatically require sidebar, large KPI or a four-card grid, but do not universally ban them; decide from content, frequency, focal point and device.

## PX4 — Acceptance and exit

| Dimension | Pass condition |
| --- | --- |
| Primary action | Most important real user task is easy to identify at first glance |
| Product specificity | Content and feedback reflect real domain, not merely renamed generic labels |
| Navigation efficiency | No excessive duplicate equivalent entrypoints; next step discernible |
| State coverage | Empty/loading/error/no-permission/save/exit make sense |
| Visual focal point | First-screen focal region corresponds to user purpose, not ornament |
| Evidence | Screenshot/source/browser/research evidence level honestly labeled |

**Blocker:** If task architecture of a core page fails, recoloring, radius unification or emoji removal does not count as completed UX redesign. If the user rejects the IA, revisit PX2/PX3 rather than reskin the same failed layout.

Coordinate with `references/progressive-visual-refinement-gate.md`; synthetic routing examples are in `assets/product-experience-routes.json`. Automated checks establish authoring consistency, **not real-world UX quality**.
