---
name: mauforma
description: Framework-agnostic Web UI/UX design and frontend engineering Skill. Diagnose the real product and page task before choosing a visual direction; build coherent information architecture, typography, design tokens, accessible components, meaningful motion, responsive interactions and browser-verified results. Apply task-scoped rules across Vue/Nuxt, React/Next, Svelte/SvelteKit, Angular, Solid, Astro and the Web platform. Preserve user intent and existing systems.
---

# MauForma — Web UI/UX Design & Frontend Engineering

> **Purpose**: Design and implement distinctive, usable, maintainable Web interfaces with verifiable outcomes. MauForma is an **Agent Skill**, not a component framework, fixed theme, product-specific playbook, animation-library dependency, or license to redesign unrelated features.

## 1. Scope, authority and language

- **Scope**: Marketing, brand, editorial, education, consumer and commerce, creative experiences, data products, enterprise workspaces, hybrid sites and Web UI embedded in desktop shells. Native SwiftUI/AppKit/Android UI are out of scope for direct implementation rules.
- **Authority**: Explicit current user requirements > confirmed product/brand/design decisions > working project architecture and component contracts > MauForma general guidance > synthetic examples and tool preferences. Do not silently replace a framework, navigation model, domain behavior, visual identity or an approved UI.
- **Page intent**: Choose the task mode per page: **Operate** (complete work), **Read** (consume content), **Persuade** (understand/convert), **Experience** (engage/explore). A multi-page product may mix modes and information densities.
- **Language**: Respond and generate product copy in the user's requested language or the product's established locale. All labels, typography checks, keyboard flows, empty/error states and accessibility checks must support actual target languages. An English Skill is **not** permission to translate a product into English.
- **Provenance**: Distinguish `confirmed / inherited / delegated / proposed / unresolved`. Recommendations do not become approved decisions. Project-specific names, screenshots, private data and generated evidence stay within the **target project's own workspace**; reusable Skill docs contain only generalized rules or explicitly synthetic examples.
- **Minimum work**: A clear bug fix requires a scoped diagnosis/fix/test, not a redesign interview. A new product or major redesign may require discovery and approval. Reviews do not modify source unless asked.
- **Licenses**: Source acknowledgements are in `README.md`; retain third-party licenses and API documentation links where actually required. Do not copy upstream proprietary code or protected artwork.

## 2. Efficient on-demand reference routing

**Read this entrypoint first.** For each task choose **one relevant row**, then load **at most 1–3** appropriate references. Load more only when an identified failure or user instruction warrants it. Use the concise, English `references/execution-handbook.en.md` for cross-cutting gates; detailed legacy topic guides remain available under their original paths. Never load the entire reference folder, all animations, or all scripts as a default. A clean synthetic example is not a product QA pass.

| Trigger / task | Load only when relevant |
| --- | --- |
| New site, visual overhaul, design critique | `references/design-craft-loop.md`, `references/visual-critique-loop.md`; English summary in `references/execution-handbook.en.md` |
| Missing direction or unknown product content | `references/design-discovery-interview.md`, `references/product-experience-routing-gate.md`, `references/design-style-catalog.md` |
| Composition, hierarchy, generic dashboard syndrome | `references/composition-first-design.md`, `references/perceptual-hierarchy-gate.md`, `references/progressive-visual-refinement-gate.md` |
| Existing UI polish / unspecified visual issue | `references/proactive-visual-defect-discovery-gate.md`, `references/visual-critique-loop.md` |
| Existing **and new** page titles, eyebrow/overline/kicker copy | `references/page-header-antipatterns.md` (**Gate H-Base / H0**), `references/semantic-copy-hygiene.md` |
| Content density and typography | `references/page-density-and-content-priority.md`, `references/typography-hierarchy.md`, `references/semantic-copy-hygiene.md` |
| Spacing, row/column alignment, last-item scroll reachability | `references/semantic-spacing-rhythm-gate.md`, `references/spacing-regression-protection-gate.md`, `references/grid-alignment-and-viewport-safety.md` |
| Navigation, sidebar state, responsive information architecture | `references/navigation-architecture.md`, `references/sidebar-navigation-design.md`, `references/sidebar-selection-indicator-gate.md` |
| Colors, themes, product visual personality | `references/palette-art-direction.md`, `references/sidebar-color-discovery.md`, `references/design-system.md` |
| Card/Panel/Section **attached color accent bars**, new or legacy | `references/surface-edge-accent-gate.md` (**Gate S0**) |
| Card nesting, controls, component quality | `references/surface-architecture-gate.md`, `references/control-geometry-gate.md`, `references/component-craft-gate.md` |
| Form, preferences, registration, checkout | `references/settings-form-layout-gate.md` |
| Icon selection and visual consistency | `references/icon-art-direction-gate.md` |
| Charts, comparisons, run-monitor data states | `references/chart-interior-alignment.md`, `references/comparison-page-design.md`, `references/task-center-run-monitor-design.md` |
| Motion policy, continuity and click-time frame evidence | `references/motion-consent-experience-gate.md`, `references/component-motion-choreography-gate.md`, `references/motion-craft-and-continuity.md`, `references/motion-rehearsal-and-evidence.md` |
| Animation engine selection | `references/animation-engine-selection.md`, `references/animejs-motion-recipes.md` |
| **Optional** liquid glass, optics and refraction | `references/liquid-glass-optics.md`, `references/visual-tech-selection-12.md` — **only on request** |
| Authorized reference site / Design DNA | `references/design-reference-learning-gate.md`, `references/design-dna-protocol.md` |
| Figma fidelity with accessible source | `references/figma-fidelity-workflow.md`, `references/component-library-first-gate.md` |
| Interactive forms and controls: component library **first** | `references/component-library-first-gate.md`, `references/enterprise-ui-library-guide.md`, `references/component-first.md` |
| Framework architecture and migration boundaries | `references/framework-support-matrix.md` plus **only the active** `references/framework-*.md` |
| Visual, accessibility and real-browser acceptance | `references/visual-qa.md`, `references/browser-qa-protocol.md`, `references/ui-review-rubric.md` |
| Design Drift, incremental QA, variant preview, resumable work | `references/skill-gap-workflows.md` |

### Optional specialist references (index only; never load as a batch)

The following are **discovery paths**, not additional required reads. Open a specific tool or guide only for its directly matching issue:

- **Visual direction evidence**: `references/art-direction-critique.md`, `references/project-design-hierarchy.md`, `references/external-design-case-library.md`, `scripts/search_design_cases.py`.
- **Container, sidebar and palette**: `references/workspace-component-refinement.md`, `references/sidebar-color-reference-cases.md`, `scripts/validate_sidebar_color_decision.py`, `assets/navigation-pattern-catalog.json`, `scripts/validate_navigation_architecture.py`.
- **Copy, density and whitespace**: `references/whitespace-and-surface-composition.md`, `scripts/audit_readability.py`, `scripts/validate_page_content_plan.py`.
- **Rendered layouts and viewport**: `scripts/validate_layout_integrity.py`, `scripts/audit_rendered_layout.mjs`.
- **Comparison and data charts**: `scripts/validate_comparison_contract.py`, `scripts/audit_comparison_ui.mjs`.
- **Run-monitor and task-center states**: `scripts/validate_task_center.py`, `assets/task-center-layout-lab.html` (synthetic demo only).

## 3. Execution process

### A. Inspect and scope

1. Identify the actual user task, website kind, visitor intent, locale, source content, primary workflow, brand and accepted decisions. In an existing codebase, inspect routes, used UI libraries, package lockfile, shared components, design tokens and build commands **before** proposing changes.
2. Choose `shape / polish / review / fidelity / fix`. Inspect top/middle/bottom of actual affected pages and interaction states before claiming defects. Missing evidence is `NOT TESTED`, not an assumed bug.
3. Make a minimal brief: **audience → primary task → first-screen focus → inherited constraints**. If direction is truly missing, present 2–3 meaningfully different options, their content/visual consequences and tradeoffs, without treating a recommendation as approval.
4. Use an existing, approved design system first. For ongoing work, preserve the project-specific `design-system/MASTER.md`, decisions and page overrides; use `scripts/feature_design_flow.py` only if a feature-level resumable workflow is useful.

### B. Fix content, IA and layout before decoration

1. Audit content by `primary / supporting / conditional / deferred / removable`. A label, badge, section heading or eyebrow needs a **real** information, navigation, status, brand or narrative purpose. Do not delete authentic breadcrumbs, content sources, units, approved taglines or meaningful chapter indicators.
2. **Mandatory new-and-existing page-header check, Gate H-Base / H0**: inspect **every existing and newly introduced** pre-H1 eyebrow/overline/kicker/decorative prefix on affected pages. Decide `keep / merge / move / delete` with reason. On task-oriented pages, **do not retain redundant explanatory pre-H1 copy**; on brand/creative pages, preserve genuine, intentional hero narratives. A prior implementation is not an exemption. Check shared `PageHeader` default props and page-level callers.
3. Match navigation depth, reading order, screen focal point and layout to real tasks. Avoid generic “sidebar + KPI cards + table” when it does not suit the product. A content-first layout must be structurally sound before polishing colors and radius.
4. Use page-appropriate density. Preserve peer alignment, section separation, row gaps, column gaps, stable grids and scroll-to-end access. An internal card padding is not a replacement for inter-section spacing.

### C. Select accessible components and shared tokens **before bulk page implementation**

1. For interactive pages, choose **one suitable primary existing UI library or accessible primitive stack** and **actually integrate** required Select, Combobox, DropdownMenu, Button, Checkbox, Radio, Switch, Tabs and Dialog controls. Prefer the project's existing library. A static site or intentionally native experience may justify no new dependency.
2. Never replace a real select/menu with hand-written `div + click` pseudo controls. A component library is not a waiver for checking keyboard, focus, loading, disabled, dark theme, overflow, popovers and business effects.
3. Centralize semantic color, typography, spacing, radius, layout, state, icon and motion tokens. Share Button/Field/Dialog/Navigation/Tabs/Table/List/Feedback/PageHeader/Chart roles; avoid unrelated nested cards, duplicate wrappers and per-page token drift.
4. **Gate S0 — surface edge accents**: No newly added **or retained** thick colored vertical strip that touches or merges with the rounded border of a Card/Panel/Section, including single-edge borders, pseudo-elements, inset shadows or gradients. Default to no decorative strip; if a short marker has real meaning, position it **outside** the panel with a visible gap. Do not confuse this with legitimate focus rings, charts, status or progress indicators.
5. **Sidebar selection**: Prefer a clear, calm selected background/text/icon. If an indicator rail is intentional, position it *outside* the navigation item with visible separation, not as its own `border-left` or inset shadow. It must follow the current route and remain distinct from focus.
6. Use design-purpose typography: titles, body, KPI, chart axes, legends, table cells and metadata have different roles. Verify real Chinese/English text, numerical values, long labels, units and 200% zoom. Icons need precise semantics and visual consistency. Do not impose a universal blue-purple gradient, a generic white-grey dashboard or a banned-font list.

### D. Implement interactions and motion with restraint and continuity

- **Operate/data**: Functional filters, explicit data ownership, accurate units, honest missing data, consistent chart axes/legends/series and valid retry/permission states.
- **Read/education**: Navigable content hierarchy, readable type, search/learning actions and feedback; no obligatory card around every paragraph.
- **Persuade/creative/consumer**: Genuine brand personality, strong content photography or illustration, intentional asymmetry and more expressive motion where approved, without obscuring actions or accessibility.
- **Settings/forms**: Choose label/control alignment based on individual setting versus batch form; preserve unsaved drafts and recoverable error states.
- **Motion Craft Gate**: For important interactions, design `trigger → before → during → payoff → interrupt/reverse → reduced`. Preserve visual identity, spatial anchors, neighboring layout, text/number continuity, immediate feedback and cancellation/cleanup. **High quality is not high animation quantity**. Respect user motion choice and `prefers-reduced-motion`. Promotional cursor/window simulations are optional demonstrations, not production E2E evidence. Use `scripts/motion_rehearsal.mjs` to collect actual frames when appropriate; `CAPTURED_FOR_REVIEW` never means `VERIFIED`.
- **Engineering**: Apply only the current framework's APIs and existing dependencies. Check versions, license, bundle impact, SSR and event cleanup before adding libraries. Do not port React primitives into Vue as if they were drop-in equivalents.

### E. Verify affected **real** pages and report evidence

1. Compare before/after at the same route, viewport and data state. Inspect beginning, middle, bottom, scroll end, focus, hover, selected, loading, empty, error and success where applicable; test supported locales and smallest **required** viewport (do not force phone support onto desktop-only products).
2. Test actual Select/Dropdown/Dialog/inputs; keyboard Tab/Enter/Escape, focus visibility/return, long text, 200% zoom, semantics, contrast, reduced motion, errors and real API effects. Verify content and header H0, surface S0, sidebar rail, grid alignment, chart internals and bottom reachability on new **and existing** affected screens.
3. For high-value motion: capture before/action/during/settled, reverse/interruption and reduced-motion; review actual 1× playback. Record jump, flicker, anchor drift and resampling gaps. Re-capture after fixes. A sample gallery or synthetic browser fixture verifies only itself.
4. Distinguish **`VERIFIED`** (real product and actual applicable checks), **`STATIC CHECK`** (code/rules only), **`DEMO ONLY`** (synthetic fixture), **`NOT TESTED`** and **`BLOCKED`**. Do not report real backend saves as tested using an in-memory fake, or claim runtime performance from a static script. Escalate actual unfixed findings.
5. Perform an independent critique of UX/IA, typography, spacing, visual identity, iconography, interaction states, motion, accessibility and content. For major design changes prefer a reviewer who did not implement the motion. Record `evidence → root-cause hypothesis → P0–P3 → fix → recapture`.

## 4. Acceptance and escalation

Stop and revisit the correct phase when any of these occurs:

- Wrong content or layout dressed up only with shadows/gradients → **B**.
- Missing component ownership, pseudo-controls, inconsistent state feedback → **C/D**.
- Attached colored Card edge strip, misplaced sidebar rail or redundant old pre-H1 copy → **B/C/E**.
- Animation breaks current task state, focus, reduced-motion or continuity → **D/E**.
- Only a synthetic example or static scanner was tested → **E, real product remains unverified**.

The final response should be concise: **scope and inherited constraints → observed issue/evidence → decisions and changed components/tokens → tests actually run → untested cases and remaining risks**. Do not insert individual user's project names or incident-specific logs into the reusable Skill.

## 5. Opt-in tools

Use only tools needed for the current task; do not automatically run crawling, screenshot capture, browser installation or agent hooks.

- Direction lookup: `scripts/search_design_knowledge.py`, `scripts/search_visual_tech.py`.
- Static review: `scripts/audit_frontend.py`, `scripts/mauforma_check.py`, `scripts/check_design_drift.py`.
- Rendered review: `scripts/browser_qa.mjs`, `scripts/audit_existing_visual_defects.mjs`, `scripts/motion_rehearsal.mjs`.
- Design DNA and feature planning: `scripts/extract_design_dna.mjs`, `scripts/feature_design_flow.py`, `scripts/preview_design_variants.py`, `scripts/plan_ui_hardening.py`.
- Implementation examples are **synthetic demonstrations**, not user project data.
- Skill repository checks: `python3 scripts/validate_web_skill.py`, `python3 scripts/validate_skill_hygiene.py`, `python3 -m unittest discover -s tests -v`.

Detailed reference and script usage: `references/execution-handbook.en.md` and `references/skill-gap-workflows.md`. Version history belongs in `CHANGELOG.md`; external Skills acknowledgments in `README.md`; bilingual public introduction in `README.md` / `README.zh-CN.md`.
