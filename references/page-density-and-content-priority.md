# Page Density & Content Curation — Select Content Before Designing Whitespace (v6.8)

**Trigger:** New sites, new major pages, home/overview redesigns, or feedback such as “too many cards,” “too much information,” or “whitespace lacks hierarchy.” Do not mandate a fresh discovery interview for a bounded fix or an already approved page.

## Fundamental distinction: many product capabilities ≠ every capability on this page

One Web product's **overview, onboarding, detailed analytics, administration, settings and editor** can each need different densities. Share brand, components, semantic typography and spacing tokens, while deciding page priority, content quantity, whitespace and surface structure from the **current task**.

Do not equate “more premium” with a fixed container width, percent whitespace, three-card cap or universal spacing. Determine **what should not appear** and **why the remaining content is needed**. Do not conceal real data, warnings or information explicitly requested by the user merely to increase whitespace.

## Gate P0 — Inventory genuine page content first

For the current route, inventory visible sections, copy, actions and navigation. Label each as `critical` (required for main task), `supporting` (common but secondary), or `optional` (occasional and reachable through a clear secondary entry). Distinguish whether content is real, Mock, observed only in a screenshot or unknown, and the states in which it appears: new/returning, has/has-no data, loading/error. **A component list alone cannot establish usefulness**; actual task and workflow evidence are necessary.

Every content block requires a **placement decision**:

- `primary`: Immediate focus and current task, e.g. choosing a repository in an overview, actual analysis trend or central filter.
- `supporting`: Adds real meaning without competing for attention, e.g. a compact row, text link or local hint.
- `conditional`: Appears only in the relevant user/data state. First-use “how to start” when no data; retry for failure; explicit empty state for missing data.
- `deferred`: Accessible through discoverable Help, detail page, secondary action or disclosure; document `accessible_via`. “Clean UI” must not make functionality disappear.
- `removed`: No incremental information, already covered by navigation, or duplicated copy; record concrete evidence of redundancy. Never remove required access-control warnings, data sources or content explicitly retained by the user.

**Run the removal test before laying out:** Would relocating or removing this entire block let the user complete the current task faster without losing necessary information? If so, defer or remove it—not rebuild it as a prettier but still useless Card.

## Gate P1 — Density follows the page task, not the product category

| Page | Main task | Starting density | Primary content permitted | Proactively defer |
| --- | --- | --- | --- | --- |
| **Overview / Welcome** | Identify current status and next action | `airy` or `balanced` | Clear title, object/state, one clear primary action; brief summary if useful | Full beginner tutorial, feature directory, duplicate links and long product introductions |
| **Onboarding** | Complete the current first step | `airy` or `balanced` | Necessary step instructions, field/choice and clear Continue/Back | Long explanations for all three steps and every advanced setting |
| **Analysis / Data details** | Compare evidence, filter, form conclusions | `productive`, `compact` if complexity merits | Metrics, trends, legends, sources, filters and real data states | Marketing declarations, wordy explanations and giant unused Heroes |
| **Operations / Batch admin** | Scan, edit and act | `productive` or user-approved `compact` | Tables, search, filters, necessary states and bulk actions | Ornamental icon cards and unnecessary shells |
| **Marketing / Brand** | Express product promise and credible value | `airy`, `balanced` as conversion task requires | Product/food imagery, proposition, CTA and evidence | Long technical specifications that can move elsewhere, repeated claims |
| **Reading / Knowledge** | Read continuously and understand | `balanced` (optional reading-density preference) | Prose, meaningful figures, optional contents navigation | Persistent empty sidebars and Card shells that truncate reading |

**Density is a page-level decision that can reflect a user preference**. It never means “make all data text tiny” or “empty the entire overview.” `airy` copy still must be legible; `compact` tables still need adequate row heights, keyboard access and applicable touch targets.

## Gate P2 — First glance and content presentation

Choose one `primary_task` per page and ask:

1. What is seen on entry? Is the next action easily available in this user's current state?
2. Do intro cards, step cards, feature indexes, navigation links and repeated bottom links express the **same purpose**? Keep the useful one.
3. Is the first viewport mostly genuine content/actions, or borders, generic slogans, repeated icons and decorative emptiness?
4. Are `first_visit` and `returning` distinguished? First-use onboarding must not remain a permanent interruption for existing users.
5. Once real data exists, does the page naturally switch from onboarding to summary/recent work, rather than demanding another tutorial?
6. Are other capabilities already reachable through navigation? Do not repeat three sidebar links as three giant feature Cards.

“Show the main content/action first” does not mean only one Button may exist. Help or “view example” can remain secondary when useful, with appropriate visual hierarchy.

## Gate P3 — Macro / Meso / Micro spatial hierarchy

Use `references/whitespace-and-surface-composition.md` for concrete spacing/surface rules. Whitespace conveys semantic relationships, not empty height. A homepage may have larger **inter-section** spaces while keeping **intra-component** content compact/aligned. Related items should sit closer together. Use a container only when it actually communicates an interactive, independent surface or meaningful state boundary. Avoid “giant page Card → description Card → three step Cards → feature Cards” nesting.

## Gate P4 — Dynamic states and progressive disclosure

- `first_visit`: Explain only the start step required now; make full Help discoverable.
- `returning`: Show the object, recent state and task where the user left off; avoid full repeated onboarding.
- `data_available`: Prioritize actual trends/tables and filtering, with sampling scope/error near their data.
- `empty` / `error`: Present necessary explanation and the next legitimate action. Do not hide errors or invent data to create whitespace.

Use discoverable details, Help or expanded panels **without losing return context**. Hidden content is not deleted functionality. Switching states must not clear a selected repository, filters or unsaved drafts.

## Gate P5 — Screenshot review: content before visual polish

Review in this order: `content relevance → primary action → duplicate sections → card necessity → spacing hierarchy → typography → color → responsive`. When information architecture fails, defer/remove the wrong region *before* adjusting padding and palette.

Judge full-page desktop/mobile screenshots separately for **overview and analysis**. Do not force the homepage to match a dense operating dashboard, or reduce analytical pages to one giant headline over blank space.

`python3 scripts/validate_page_content_plan.py examples/page-content-plan-demo.json --repository` checks required planning fields, content layers, states, disclosure routes and density choices. Passing it **does not verify visual quality, actual business behavior or WCAG conformance**.

### External design research — principles, not fixed palettes or ratios

- [IBM Carbon — Spacing](https://www.carbondesignsystem.com/building-blocks/foundations/spacing/overview): Vary spacing scale to communicate content relationships and hierarchy; dense regions may coexist with an uncluttered page.
- [IBM Carbon — Productive and expressive typography](https://www.carbondesignsystem.com/building-blocks/foundations/typography/style-strategies): Functional work and expressive brand pages require different typographic purposes/densities.
- [Nielsen Norman Group — Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/): Prioritize the core while keeping secondary functionality discoverable.
- [GitLab Pajamas — Progressive Disclosure](https://design.gitlab.com/patterns/progressive-disclosure/): Move supplementary content behind usable secondary interactions rather than filling the first viewport.
- [Atlassian — Compact density](https://community.atlassian.com/forums/discussion/3189883/new-feature-compact-mode-and-max-width-to-support-information-dense-documentation): Real applications can offer compact page-level density, not one global density for every route.

## Relationship to alignment and scroll-end safety

Dense data pages still require coherent alignment for related chart rows; density does not excuse arbitrary misalignment of two independent columns. First curate content using v6.8, then use the shared row/column contracts in `references/grid-alignment-and-viewport-safety.md`. Genuine records extending beyond the viewport should **scroll naturally**. Never clip charts, compress release histories or hide axes merely to project a one-screen “premium” look. Content below the fold is normal; inability to scroll to the final record is a defect.

## Comparison is a distinct page task

A comparison page must first answer **who is being compared, on which measures, whether coverage is comparable and where meaningful differences lie**. Operate mode does not justify every available chart at once. In typical multi-object analysis, show selected objects in a compact editable strip; important differences and a shared time-series chart may outweigh a permanently huge filter sidebar or an empty methodology Card. Organize comparison tables with objects as columns and attributes as rows. Never invent a winner when data is insufficient. See `references/comparison-page-design.md`.

## Task monitoring is not a generic statistics overview

A background run list exists to show what is executing, queued or failed and how to recover or inspect logs—not mainly to show total task count. Status counters can be compact filtering shortcuts, but **do not default to a huge left Card taking half the viewport**. Use scannable ID, object, state, progress/stage, update time and action columns. Open details/logs on demand. Do not repeat “unknown progress percent” on every row. When progress is null, show the **real stage**; without a verified denominator, do not calculate a percentage. Human review tasks and multi-stage jobs may need different UI. See `references/task-center-run-monitor-design.md`.
