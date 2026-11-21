# Frontend Project Architecture & Acceptance Gates

## Defect-first default for vague optimization

- **Gate 0:** Interpret scope. "Improve this page" implies proactive inspection and repair, not just CSS token adjustment. A single functional bug does **not** require redesigning every page. Review-only requests do not authorize source edits. Read proactive-visual-defect-discovery-gate.md.
- **Gate A:** Inspect the **running target page** for spacing, typography, component, icon/palette and interaction/responsive flaws. If independent Sections already touched in the inherited layout, discover and assess that flaw; preserve-baseline is **not an approval**. scripts/audit_existing_visual_defects.mjs may provide baseline-free heuristic signals.
- **Gate B/C:** Repair high-value user-task and readability defects first while preserving correct structure, brand, motion and confirmed choices. Audit Block, Grid/Flex and nested wrapper gaps; **internal padding does not substitute for between-panel gap**.
- **Gate D:** Reopen the changed **real page**, confirm the original defect is fixed, then compare before/after to protect sound spacing, supplemented by actual screenshots and narrow supported widths. A Skill-only demo smoke test is **not business-page visual acceptance**.

## Spacing preservation and real-page verification

- **Gate 0/A:** On existing layouts, record meaningful section/peer/connected gaps before edits; simplicity/one-screen goals do **not** authorize accidentally joining independent modules. See spacing-regression-protection-gate.md.
- **Gate B:** Parent Grid/Stack semantic tokens own independent surface gaps. Compact design does **not automatically authorize removing row-gap**; region boundaries must remain perceptible with a reason.
- **Gate D:** Compare before/after surface geometry and full screenshots on actual routes. Use scripts/audit_panel_spacing.mjs for unannotated risk scanning; where a precise relation contract exists, use scripts/audit_spacing_rhythm.mjs. If only demo, no coverage or incomparable baseline, state it honestly rather than claiming passed.

## Design Reference Learning Gate — transfer principles, protect sources

- **Gate 0:** Respect user's stated ownership and authorization; without permission do not save/upload the reference, its variants or identifiable business details. Read design-reference-learning-gate.md. Source imagery is used for **current-task insight extraction**; public reusable output contains generalized rules and newly invented fictional examples only. No original material in PR/commit/CI screenshot artifacts.
- **Gate A:** Write observed_trait → task_benefit → applicable_context → transfer_rule → avoid_copying. Test where cross-domain principles do/don't apply. Clean Enterprise (clean-enterprise-design.md) is a **candidate**, not global default; confirmed identity and user choices outrank it.
- **Gate B:** Recompose genuine new navigation/components/information for the target product. Do not copy source field names, project identity, actual data or identifiable layout. Official icons can be used only under their own rights.
- **Gate D:** Review every published file and text for unauthorized reference images/identifiers. Test synthetic examples with Chromium keyboard, responsive and interaction checks. scripts/validate_design_reference.py --repository is **static-only**; it cannot replace privacy/aesthetic review or prove the real product was changed.

## Icon Art Direction Gate — semantic fit and whole-set coherence

- **Gate A:** Once IA is known, inspect inherited icon package/version and approved design. For important navigation and frequent actions, research at least **two real icon candidates** and choose by task meaning and visual contour; do not mechanically add an icon to every text label or turn a synthetic example into product-specific icon rules.
- **Gate B:** Use one principal icon language in shared IconBox/NavItem/IconButton/Status components. Gallery demonstrates actual icon size, text alignment, Badges, active/hover/focus and themes, not isolated SVG thumbnails. Brand/custom symbols may be justified exceptions with source/license and visual-role boundaries.
- **Gate D:** On the real page ensure icons actually render recognizably, avoid mixed styles and mismatched optical weights, compression and baseline drift; ensure icon-only actions have visible text/aria-label. scripts/audit_icon_consistency.mjs can inspect annotated geometry/style risks; **it cannot judge semantic accuracy or human art direction**.

## Semantic Spacing & Rhythm Gate — all Web page types

- **Gate A:** Assign inside/peer/section/connected/anchored relationships after IA, and map them to inline/inside/peer/section/page spacing tokens based on user-approved density. Shared Cards do not justify equal gaps; absence of color/motion requests does not remove spacing quality duties.
- **Gate B:** Parent Grid/Stack/PageSection owns peer and section gaps independently of Card padding. **Design both column-gap and row-gap**; reflow from horizontal to vertical must retain appropriate peer separation. Lists and genuinely connected Tabs+Panel can share edges with reasons; do not fake layout using negative margin.
- **Gate D:** Inspect full page at wide/narrow and 200% text, unusual data, actual scroll end and fixed bars. Explicit data-mf-space-id plus contract can enable scripts/audit_spacing_rhythm.mjs; unannotated pages **cannot claim measured results**. scripts/validate_spacing_rhythm.py --repository checks synthetic contract consistency, not aesthetic quality.

## Component Motion Coverage — real components, real state relationships

- **Gate A:** After the user's motion direction is known, inventory actual high-frequency/high-value component changes and choose motion/immediate-feedback/intentionally-static(reason). **Page-route transition is not component motion coverage.** See component-motion-choreography-gate.md.
- **Gate B:** When those components exist, create a Component Motion Gallery for Tabs/Segments, Accordion/Drawer, Toggles, Row/List, Success/Error and Media. Avoid applying identical hover scale/fade to every interaction. Select mechanism by spatial anchor, tactile response and meaning. The list does **not** require creating missing controls.
- **Gate D:** Trigger actual important business interactions in browser and inspect before/during/after, layout position/expanded height, normal/reduced motion, repeated rapid clicks and interruption/reversal. scripts/validate_component_motion.py checks static contracts; standalone Mock motion is not target-product QA.

## Motion Choice Gate — user authority before engines

- **Gate A, new/major motion redesign only:** Inspect inherited motion choices. If undecided, offer **2–3 materially distinct observable experiences** for selection, combination or explicit delegation. Ask once, avoid repeated questioning. Unanswered direction remains unresolved; **neither all-static nor excessive scroll effects are authorized by silence**. See motion-consent-experience-gate.md.
- **Gate B:** On confirmed selection, establish Motion Tokens and inventory actual on-page interactions covering chosen strength/reduced-motion. Reuse framework/native transitions where adequate; do not force installing an engine. Immediate state feedback remains necessary even with no added animation.
- **Gate D:** Exercise real Tab, overlays, navigation, notifications and lists under normal/reduced-motion, checking true enter/exit/static fallback, rapid-interruption continuity, immediate content, keyboard and semantic state. scripts/validate_motion_decision.py cannot certify actual animation.

## Settings/Form layout follows saving semantics

- **Gate A:** For Settings, registration, checkout, grouped data entry and hybrid configuration, consult settings-form-layout-gate.md. Independently saved settings get setting rows; grouped submissions get vertically associated fields; isolate destructive controls and preserve current IA/library.
- **Gate B:** group-gap must be perceptibly greater than item-gap. Left descriptions cannot crush controls; Form labels/help/errors belong to a bounded readable field column. Keep meaningful surfaces; removing a decorative wrapper does not remove group spacing.
- **Gate D:** Test real wide/narrow routes with long localization, 200% zoom, save/submit failure and final scroll access. Synthetic fixtures/Chromium smokes do not verify user-specific product behavior.

## Surface & Atomic Control Geometry Gate — all page types

- **Gate A:** Match real task with an open collection, single panel, media/product Cards, editorial flow or split/immersive stage, describing why selected and what alternatives were rejected (surface-architecture-gate.md). Giant outer Card is not the default enterprise wrapper.
- **Gate B:** Short Button/Tab/Badge atomic labels are unlike body prose that may wrap. Budget row actions at natural size with responsive fallback (control-geometry-gate.md). white-space:nowrap **requires** sound parent Grid/Flex handling, otherwise it creates horizontal overflow.
- **Gate D:** On real Chromium supported desktop and when in scope 390/320px, 200% text, error-added actions, verify atomic labels don't split character-by-character; targets, focus and final rows remain accessible. Optional data-mf-atomic-control/data-mf-control-label and Range.getClientRects() provide risk checks. Synthetic examples are not business implementation; scripts/validate_surface_control.py only checks structural plans.

## All-page prerequisite gates A/B/D

- **A:** Read perceptual-hierarchy-gate.md, identify P0–P3 per user task, reading path, visible content and density. **Rank importance before setting type and components.** Different pages may prioritize a price, prose, artwork or current error; not every number needs huge KPI typography.
- **B:** Read component-craft-gate.md; define shared component responsibilities, text hierarchy, visual-form rationale, interaction and state. Preview components **and their actual composed content**; uniform pills and outlines do not equal quality.
- **D:** Inspect grayscale three-second hierarchy, true normal/error content, long text, 200% zoom and wide/narrow screenshots. scripts/validate_visual_priority.py tests priority-plan **coverage**, not visual superiority. Small patches stay scoped and need not repeat whole-project discovery.

## Component Library First — mandatory before bulk page phase B

- **Gate A:** Inventory inherited actual UI library usage. If a new interactive project lacks a primary system for Select, DropdownMenu, Button, Checkbox, Radio, Switch and Dialog, **Agent selects a suitable mature framework-compatible solution** (component-library-first-gate.md). No manual pseudo-Select/Buttons just because user didn't name a vendor.
- **Gate B:** Actually integrate required components, common theme and real Showcase; verify selection dropdown open/selected, action menus, primary/secondary/danger Buttons, focus/disabled and forms. Shared Ui wrappers **adapt**, not recreate accessible primitives; a narrow repair does not force whole-library migration.
- **Gate D:** Real-page Select/Dropdown/multi-select/Button keyboard, focus, overlay placement and theme consistency. Unjustified hand-made div dropdown, fake selected state or cross-page Button drift means **first delivery is not acceptable**. Synthetic demo gives design hints, not product verification.

## Phase 0 — Inspect existing architecture

- Read package.json, lockfile, vite.config.*, next.config.*, nuxt.config.*, angular.json or matching framework build sources.
- Inventory routes, permissions, i18n, remote data, forms, tests and styling; search instances of button/input/dialog/table/toast/sidebar.
- Classify **existing / reusable / defective-needs-repair / genuinely missing**. A screenshot suggesting one vendor does not authorize dependency changes.

## Phase A — Design language and semantic Tokens

Single token source for --color-bg/surface/surface-muted/text/text-muted/accent/on-accent/border/focus/success/warning/danger and --font-*, --space-*, --radius-*, --shadow-*, --motion-*. Replace unrelated per-page literals with semantic roles; light and dark each have correct contrast and hierarchy.

**Gate A:** Provide at least **two preview screenshots or executable examples** showing component states + main page regions. Without a coherent theme, do not multiply page development.

## Phase B — Build the component system

- **Primitives:** Button, Input, Textarea, Checkbox, Select, Dialog, Popover, Tooltip, Tabs, Toast, Loader, Icon.
- **Composites:** Field+Error, SearchField, DataTable, FilterBar, Pagination, EmptyState, ConfirmDialog, PageHeader, Sidebar, FormActions.
- **Patterns:** Filterable lists, detail view, create/edit, Settings, wizard, article, branded Hero, product detail.
- **Contract:** Stable props/variants/size/state/slots(or children)/events, shared Tokens and correct keyboard/focus/ARIA.
- **States:** normal, hover, pressed, focus-visible, disabled, loading, success, error, empty; business-critical pending/offline/permission denied.
- **Showcase:** Dimensions, variants, states, long Chinese/English/numeric content and supported dark mode.

**Gate B:** Business pages must reuse, not recreate Buttons, Dialogs and Fields. A minor scoped change need only apply this contract where relevant.

## Phase C — Implement real pages

- Page heading density follows task: compact operations, expressive Hero only where appropriate.
- Real data semantics; submissions need loading/error/success/duplicate protection; dangerous or permission actions need confirmation.
- Separate remote server data from local UI state; avoid SSR hydration mismatch; lazy-load chart/editor clients when appropriate.
- Choose motion purpose first (feedback, hierarchy, state, reflow, direction), then engine. Keep interruption and static fallback.

## Phase D — Real tests, review and delivery

- Appropriate unit/component (Vitest/Testing Library) plus E2E (Playwright/Cypress) test coverage of primary workflows.
- Real representative viewports, e.g. **360/390/768/1024/1440** according to supported devices, not forced breakpoints; check light/dark, touch/keyboard, zoom, long text and error/loading/empty.
- Visual QA: headings, semantic colors/boundaries/radii/gaps, icons, action hierarchy, chart labels and table readability.
- Motion QA: prefers-reduced-motion, unmount cleanup, rapid route changes, lower-spec devices, content visibility with animations disabled.
- Report changed files, Tokens, component reuse mapping, motion rationale, **actual test evidence and untested cases**.

## Dependency admission gate — answer for each new package

| Required question | Evaluation |
| --- | --- |
| What specific missing behavior requires the dependency? | "Looks cooler" is insufficient |
| Why are native CSS or current dependencies insufficient? | Do not install GSAP for a simple Button transition |
| Current framework/SSR/version support? | Vue/React packages differ; inspect correct imports and lifecycles |
| Accessibility/performance/license/security risk? | No induced flashing or illegibility |
| Migration/cleanup/replacement plan? | Converge interaction ownership and dependency count |

## Composition-first prerequisite to Gate A

For new pages and major redesigns, consult composition-first-design.md first. Inventory authentic content and task, sketch **2–3 actually different grayscale layouts** by information ordering or primary focal position before selecting colors/components. An explicit reference, approved layout or local fix may keep its structure and skip comparisons. An empty chart without truthful data state cannot be considered complete. At D, if screenshot reveals task/focal mismatch, **return to A** rather than repeatedly tuning effects. Palette decisions require source and semantic role (palette-art-direction.md).

## Text/typography check between A and B

After composition, run semantic-copy-hygiene.md deletion/necessity reasoning. Use typography-hierarchy.md to define role Tokens for PageTitle, body, metrics, chart axes/legends and source metadata. PageHeader kicker/description/English prefix remain **optional slots** that default to absent when no information is gained. In Gate D, inspect real browser dark text, Chinese/digits/repo-name mixing, 200% zoom and clipping; static source scanning cannot claim readability verified.

## Color Choice Gate — approval is not an Agent aesthetic default

Before recoloring, inventory confirmed colors and current Sidebar/Main system. When undecided, present **2–3 genuinely different whole-workspace palettes** for user selection or explicit delegated choice. Never infer that starting development confirms the Agent's favorite color. For an exact HEX, retain assigned role **exactly** and adjust surrounding contrast with explanation. Functional fixes and approved inherited colors do not require new questioning. See sidebar-color-discovery.md, design-system/sidebar-color-decision.json. Actual screenshots should compare Sidebar/Topbar/Main/Card/Chart together.

## Navigation Architecture Gate — before composition/components

For major tasks, list top-level destination count, nesting/frequency and devices; separate global/local/object/actions/Tabs. Consider Top only, Side, Top+Side, Rail/Split, Mobile Bottom, Responsive Side→Bottom, Top+Bottom and Side+Bottom action bar (navigation-architecture.md). For undecided IA, present **2–3 meaningful architectural alternatives**, record actual user selection or explicit delegated authority. Existing confirmed navigation or scoped repair may skip. Then set UiNavigation contracts/Tokens. Browser verification must include supported desktop/mobile/narrow, route reachability, keyboard/focus/ARIA, bottom occlusion and task context. scripts/validate_navigation_architecture.py does **not** replace real flow testing.

## Gate A0 — Content priority before building Card grids

On new/major pages, per route inventory primary_task, visit state, content roles and conditional/deferred navigation (assets/page-content-plan.schema.json). Overview should **not simultaneously** generate full tutorial, feature directory and Cards for every action. Apply whole-block deletion reasoning, keeping secondary features findable. Analytical detail can be denser and include comparable charts/metrics/filters, but **never hide sources/errors**. Reusable FeatureGrid/Card is not justification to create extra intros everywhere. Gate D tests overview/detail and first/return visits separately.

## Gate A/B/D — Shared Grid rows and scroll-end evidence

- **A:** Establish peer content boundaries, shared column/row tracks, purposeful proportional emphasis and mobile reading sequence; avoid accidental independent two-column Masonry on analytical pages.
- **B:** ChartPanel/List/MainScroll/BottomActionBar share sizing and scroll contracts. Prefer CSS Grid and minmax(0,1fr), min-height:0 where needed, correct overflow-y:auto. Fixed bar reserves space at the actual scroller end; avoid global overflow:hidden clipping. Different Cards need not all have equal heights.
- **D:** Actually scroll to final record/Button/chart legend, inspect fixed bar, short windows, mobile safe area and 200% text. Only screenshot/declarative scripts means **NOT RUN**. scripts/audit_rendered_layout.mjs can surface initial/final DOM geometry risks; it does **not** replace manual interaction/visual acceptance. See grid-alignment-case.md.

## Comparison page engineering contract

- **A:** Before choosing layout define user decision question, compared objects, common definitions and missing-data policy; do not merely tile all repository statistics (comparison-page-design.md).
- **B:** RepositoryPicker/Legend/Series/MetricMatrix synchronize one object ID and color token. Selection/time/filter/source updates must change every view coherently. Matrix uses object columns and metric rows with units/sample_size/coverage. **null is not 0**. First screen highlights evidence-grounded differences; ban unsupported composite "winner" labels.
- **D:** Inspect Plot Area, axes, labels, collision, point coverage and legend bindings on actual rendered charts. scripts/validate_comparison_contract.py checks declared data rules; scripts/audit_comparison_ui.mjs checks annotated DOM geometry; Canvas text not visually inspected is **NOT AUDITED**. Test changing object and filters against real data and matrix, not just the initial static view.

## Run Monitor workspace engineering contract

- **A:** Determine run_monitor/human_tasks/mixed, frequent user action, lifecycle source and progress/permission rules (task-center-run-monitor-design.md). For crawler/Agent runs, first consider actionable status filter + scannable run list + on-demand detail, **not** automatic giant KPIs or a Kanban.
- **B:** RunRow, StatusFilter, ProgressIndicator, RunDetail and RetryAction derive from the **same run ID and lifecycle state**. Percentage requires a stable denominator with matching units; **unknown is not zero**. Check backend and user permission before showing retry/cancel, including duplicate requests. Do not render fake clickable action without authority.
- **D:** scripts/validate_task_center.py checks static data/action contracts; tests/task_center_browser_smoke.mjs checks a **synthetic Mock**. Target app still requires real server status, error/log/permission, counts, long lists and last-record scrolling. Keep user's selected filter/context during refresh; avoid involuntary jumping/reordering.
