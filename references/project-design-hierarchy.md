# Project Design Hierarchy — One Approved System, Context-Specific Overrides

**Purpose:** Distinguish the user's authoritative design decisions from Agent proposals, observed code, synthetic examples and external references. Multi-page products should have coherent foundations without forcing the same page density or composition everywhere.

## Authority levels

1. **Explicit user requirement:** Latest specific instruction, requested product behavior, confirmed color, component/navigation direction and constraints.
2. **Confirmed project design:** Approved `design-system/MASTER.md`, decisions and signed-off page variants.
3. **Actual working architecture:** Existing framework, component APIs, installed packages, data flow and routes.
4. **MauForma guidance:** General reusable principles and conditional gates.
5. **Synthetic samples/external trends:** Inspiration, never binding project truth.

If a newer explicit instruction contradicts an older generic preference, follow the newer instruction for the affected scope. Do not infer blanket authorization to rewrite unrelated decisions.

## Source-of-truth structure — adaptable, not a required directory dump

```text
design-system/
  MASTER.md                 # Approved shared tokens and component roles
  decisions/                # Confirmed/delegated records with rationale
  pages/                    # Page-specific purpose, layout and density overrides
  features/                 # Resumable task-specific design records when useful
  observed-tokens.json      # Code-derived observations, NOT user approval
```

Use the existing project's established folders when available. These paths are illustrative; **do not create empty documentation trees for every small patch**.

## Decision provenance and language

Record `confirmed / inherited / delegated / proposed / unresolved` as separate states. “The Agent recommends” remains `proposed`, not `confirmed`. Silence or a request to write code is not broad permission to redefine branding, install dependencies or add cinematic motion.

Retain the actual product locale. An English Agent instruction file **never means the user's UI must be translated to English**. On bilingual products, check real translated copy and layout rather than setting a global English default.

## Global MASTER versus page override

MASTER should hold shared colors, type roles, spacing scales, radius, interaction/state semantics, icon and Motion Tokens, component contracts and navigation responsibilities. Each page can choose its task-specific density, content hierarchy, layout, editorial rhythm, media emphasis or allowed motion intensity. A marketing landing can be expressive, while settings/operations remain compact under the same product branding.

Do not let page-local CSS silently redefine global brand tokens. Conversely, do not erase a justified page exception merely because MASTER is more compact.

## Design drift categories

- **Tool drift:** Dependency/formatter/browser version behavior changes.
- **Schema drift:** Token/decision document structure changes.
- **Design truth drift:** Source/UI diverges from actually approved choices or real task meaning.

`scripts/check_design_drift.py` records code-observed variables and compares versions; a generated observed baseline is **not MASTER truth**. Do not overwrite `MASTER.md` or approved design decisions merely to make a static drift report green. Design truth requires user/brand authority and real rendered evidence.

## Multi-agent and resumable work

Component/design lead owns shared tokens; feature agents compose using them. Changes to foundational components should identify all affected callers and reverify. Feature-level records may be created as needed with `scripts/feature_design_flow.py`, but are not mandatory for every tiny task.


## Source-parity: original file structure and page conflict precedence

Recommended outputs **inside the user's project**:

- design-system/MASTER.md: brand, confirmed style, semantic color/type/spacing/radius/motion tokens, primary UI library, shared components, accessibility rules, provenance, version.
- design-system/decisions.json (assets/design-brief.schema.json): confirmed/delegated/inherited/unresolved origin, style parameters, actual user wording, reasoning and unresolved questions.
- design-system/pages/<route>.md: only genuine differences from MASTER (page type, focal point, density, composition, motion allowance and page-specific requirements). **Never copy the whole MASTER** into every page and create conflicting configurations.

**Conflict order:** (1) latest explicit page-level instruction; (2) confirmed/inherited page override; (3) MASTER branding/tokens/shared component contracts; (4) unapproved Agent recommendation. If a page override conflicts with global color semantics, keyboard access, contrast or component accessibility, **explain and escalate**; never silently replace global tokens with an arbitrary new --primary. The same product can use a spacious expressive home, scannable product grid and compact management tool while sharing branding and component states.

In multi-Agent work, read MASTER, relevant page override and current component contracts before implementation. A global MASTER change must identify every affected component. Each commit reports shared token changes, component-contract changes, page exceptions, tests and design grounds. A new authorization is required to change user-confirmed choices.

## Source-parity: initialization and write safety

Example templates: examples/design-system/MASTER.md; examples/design-system/pages/home.md; examples/design-system/pages/dashboard.md. They are illustrative, not mandatory themes.

~~~bash
python3 scripts/init_design_system.py --project-root . --name "Example" --style editorial --page home --mode Persuade
# PREVIEW ONLY by default
python3 scripts/init_design_system.py --project-root . --name "Example" --style editorial --source confirmed --page home --mode Persuade --apply
~~~

Use --source confirmed **only when the user explicitly selected that style**; an authorized Agent choice uses delegated. Existing MASTER/decisions/page files refuse overwrite by default; explicit authorization together with --force --apply is required to replace them. A script cannot infer real business facts or design assets.

## v6.4 — Per-page composition plan

For new pages/major redesigns, a project-local design-system/composition-brief.json (assets/composition-brief.schema.json) may record content evidence; **2–3 meaningfully different candidates** for main region/order; the recommendation and selection authority; color direction; and a remove-decoration critique. The selected page override references, rather than duplicates, the brief. MASTER owns brand/component tokens; choosing one composition does not impose identical Cards/Heroes across pages.

scripts/validate_composition_brief.py <brief-path> may check source references, candidate differences and handling of unverified data. It **cannot establish art direction quality or a live-page pass**.

## v6.6 — Color choice must not enter MASTER before authorization

When a new color proposal is unconfirmed, save candidates to design-system/sidebar-color-decision.json (assets/sidebar-color-decision.schema.json) with status=pending. **Keep previously approved product tokens unchanged**, or work only on tasks independent of the unresolved color choice. After approval, record the chosen option, original user wording for custom colors, confirmed/delegated/inherited provenance and coordinated Sidebar/Topbar/Main/Card/Chart color rationale; only then change the **single** MASTER token source.

An exact user-provided #RRGGBB must be fixed for its specified role under user_constraints; resolved_colors **must preserve it exactly**. scripts/validate_sidebar_color_decision.py checks unauthorized replacement. Approved palettes may simply be inherited; a functional bugfix should not automatically reopen a theme choice.

## v6.7 — Navigation IA decision and breakpoint map

The project may use design-system/navigation-decision.json (assets/navigation-decision.schema.json) to record actual destination IDs, task/device/hierarchy, alternative navigation architectures, approval/delegation provenance, and desktop/mobile visible plus overflow route maps. **A pending recommendation may not become an approved IA.** MASTER owns global navigation responsibilities; page overrides only meaningful local Tabs/object-tree exceptions. Do not create a fresh sidebar on each route. Across breakpoint changes retain current route, filters and object selection. Static contract: scripts/validate_navigation_architecture.py <decision-path>.

## v6.8 — Page content curation and density decision

Per-route design-system/pages/content-plan.json (assets/page-content-plan.schema.json) may record primary_task, user states, each group as primary/supporting/conditional/deferred/removed, the secondary navigation path, local density as airy/balanced/productive/compact, and real testing. Shared theme/type/spacing tokens live in MASTER; pages are **not** required to use identical Cards or fixed whitespace ratios. Decision status is confirmed/delegated/inherited/provisional; an Agent suggestion is **not approval**, and actual critical information cannot be removed merely for blank space.

## v6.9 — Grid, viewport and scrolling strategy

For dashboards or major layout redesigns, design-system/pages/layout-integrity.json (assets/layout-integrity.schema.json) may describe route/task, grid pattern, aligned row/column peers, mobile reading order, primary scrolling container, fixed-bar and end-padding strategies, and browser evidence. MASTER may share spacing/grid/scroll-safety tokens but **must not require identical two-column ratios**. Inferred interim designs are provisional, not user-confirmed. Keep explicit brand/color/navigation decisions.

## v6.10 — Comparison data and visualization alignment contract

For product, project or plan comparisons, design-system/pages/comparison-contract.json (assets/comparison-contract.schema.json) records object IDs, metric definitions, time windows/buckets, series/legend, table columns, data coverage and real browser QA. Data must be grounded in the actual source; never populate business charts from synthetic Skill demo numbers. Real E2E verifies object selection and time-window linkage. Targeted data-mf-* browser hooks are allowed where useful, **without renaming an entire application's component architecture**.

## v6.11 — Run Monitor state contract

The project may save design-system/pages/task-run-contract.json (assets/task-center-run.schema.json) recording run IDs, status aggregation, progress units/stable denominator, retry permissions, detail routes, update frequency and E2E evidence. MASTER owns shared status colors, list typography and alignment. Whether to show a statistic sidebar, compact rows or details drawer depends on the actual task and is **not globally mandatory**. Never pass synthetic Mock run records off as genuine production tasks.

## B12 — Distinguish three types of design drift

- **Tool/version drift:** Skill/script/tool version changes may require checking commands and schemas; they do **not** automatically imply a product palette error.
- **Schema drift:** MASTER/decision field or location changes may be migrated **with authorization**; a structural migration is not renewed permission to change brand colors.
- **Truth drift:** Documentation and actual source/rendered UI conflict. Resolve via current user intent, provenance, target page and visual evidence; **a static snapshot alone cannot decide which side is correct**.

observed-tokens.json is code observation, **not user-approved canonical Tokens**. Never rewrite MASTER, accepted brand decisions or page exceptions to make a static report green. See references/semantic-boundaries.en.md B12.

## Runtime drift check and resumable features

- Inspect actual source and confirmed MASTER/decisions before modifying tokens. scripts/check_design_drift.py writes an **observational baseline only with explicit --write-baseline**. Then inspect CSS-variable changes and local hardcoded colors. Observed baselines are **not equivalent to approval** and cannot authorize rewriting MASTER.
- For larger features, use project design-system/features/<slug>/ with scripts/feature_design_flow.py (defaults to preview) to record steps, evidence and progress. Reference MASTER rather than duplicating brand/visual settings.
- When resuming a session, inspect saved feature state and completion evidence. Without actual acceptance testing, do not mark it VERIFIED. See references/skill-gap-workflows.md.


## Quality evidence and escalation

For significant change, record scope, approved/inherited constraints, observed defect, proposed fix, actually modified components and verified route/state/viewport. Static checks and synthetic examples remain separately labeled; a complete green CI on Skill examples is not a substitute for the target product's real user workflows.

**Escalate** real conflicts over a fixed user HEX, approved navigation type, licenses, explicit performance limits or interaction state rather than silently choosing whichever design looks prettier. Genuine unknowns remain `unresolved`, not a fabricated user decision.
