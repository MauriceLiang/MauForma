# MauForma — English Execution Handbook

This is the standalone English reference for international Agent users and contributors. It contains the operative rules; Chinese detail files remain available for depth and historical parity. It is not a product-specific design system, a style preset, or a claim that any browser test has passed.

## 1. Minimal workflow by task

| Case | Required preparation | Required evidence | Do not |
| --- | --- | --- | --- |
| Fix a UI bug | Scope route, reproduce, inspect code | Reproduce before/after or note blocker | Redesign unrelated screens |
| Polish existing UI | Inspect first, middle, end, main states | Actual screenshots and user flows | Assume an issue from screenshots alone |
| New product | Audience, content, real task, approved choices | Working flows and target viewports | Reuse a generic dashboard template |
| Figma fidelity | Authorized frame/node and design screenshots | Matching viewport comparison + interactions | Claim pixel-perfect without source access |
| Independent review | Capture observations, affected code and severity | Real page or correctly labeled static evidence | Modify source without permission |
| Cinematic marketing | Intentional visual narrative and motion policy | Real-time playback and interruptions | Simulate fake backend success |
| Operational dashboard | Information priorities, real data and permissions | Correct data, actions, keyboard and error | Apply a marketing hero layout by default |

Treat Operate, Read, Persuade and Experience as page modes, not permanent product types. Select the smallest valid set of references from SKILL.md: one primary guide, up to two supporting guides unless evidence justifies more. The table is an index, not a mandate to load every listed file. Never eagerly load the whole reference library.

## 2. Language and internationalization

**No arbitrary translation.** English instructions do not imply an English UI. Preserve the user's preferred language, product locales, approved copy, proper nouns, translation keys and localized messages. Evaluate actual Chinese, English, mixed Latin/CJK, long words, numeric units, bidirectional text when supported, keyboard interaction and 200% text scaling. Do not arbitrarily translate real products.

Respect source licensing and original API names. Store attribution in README rather than repeating it in execution prompts. Distinguish confirmed, inherited, delegated, proposed and unresolved decisions. A design recommendation is not an approved decision.

## 3. Visual authorship and user authority

Start with content and the primary action, then compose the layout, then choose styling. Favor strong typographic roles, intentional information focus and coherent whitespace over cosmetic card proliferation.

Build a single source of truth for semantic tokens: background, surface, text, muted text, accent, focus, state colors, type, spacing, radius, elevation, layer and motion. In existing projects, inherited tokens and accepted brand decisions outrank any Skill recommendation. Do not impose blue-purple gradients, generic white-gray workbenches or arbitrary banned-font lists.

Creative media projects can be cinematic and asymmetric. Dense business UI can be restrained and compact. Quality means visual purpose, not universal minimalism. State colors mean real system state; decorative color does not substitute for hierarchy.

**Gate H-S: self-sufficient heading first.** On every affected H1–H6, card, section, dialog and visual title group, default to one clear heading with **no** preliminary category/explanation. Remove an inherited or generated pretitle when deleting it loses no independent user information; vague "context" or visual-hierarchy claims cannot justify KEEP. If useful information would disappear, move it to its semantic owner by default. Keep a pretitle only with specific evidence for the **information it adds** and **why it must remain immediately above the title**. Treat unresolved candidates as a review blocker, not as an automatic pass; when target browser access exists, record before/after results and use the title-prefix review validator. This is a review-completeness aid, not automatic semantic judgment.

## 4. Page-header copy: H-Base and H0

Inspect every existing and newly introduced microheading, eyebrow, overline, kicker, mixed-language prefix or decorative number placed above the real H1 on affected routes.

- KEEP if an authentic breadcrumb, status, owner-approved label, meaningful chapter marker, verified tagline or intentional brand narrative.
- MERGE when useful information is duplicated with the title.
- MOVE if the information belongs below the title or beside its related content.
- DELETE when it merely repeats screen purpose, adds filler, or manufactures visual hierarchy.

Gate H0: on task-oriented pages, redundant explanatory pre-H1 microheadings must be removed or moved to semantic content. Existing code is not an exemption. Brand/marketing hero storytelling is allowed when it genuinely helps visitors. Always inspect PageHeader defaults and actual page instances, not just the rule text. Never remove legitimate sources, units, breadcrumbs or meaning in pursuit of minimalism.

**Title-prefix recognition is style-agnostic and applies to every heading level, not only the H1.** Identify a subordinate pre-title line by its relationship to the heading in the rendered title group, regardless of color, font, size, weight, language, element/tag or component name. Separate information value from placement: real status, source, chapter, step, brand and navigation may deserve preservation, but not necessarily as a decorative overline. Review existing card/section/dialog preambles as well as new page ones; record KEEP / MERGE / MOVE / SPLIT / DELETE with reasons. Optional `scripts/audit_title_prefixes.mjs` only finds DOM candidates; the Agent must make the semantic decision and verify the real rendered UI. See `references/title-prefix-role-gate.md`.

## 5. Spacing, surfaces and composition

Separate peer spacing from section spacing and card padding from inter-card gaps. Check vertical rhythm AND column alignment, especially for nested charts and toolbars. Use Grid/Flex according to content relationships; aligned cards do not prove aligned chart plot areas.

Avoid needless Card-inside-Card wrappers. Ensure buttons, translated long labels and final scroll items remain reachable at the smallest required viewport and 200% text scaling. A fixed footer cannot obscure final content.

Gate S0: Do not introduce or retain a thick colored strip attached to a Card/Panel/Section frame or merging into its rounded corners. This includes colored single-edge borders, pseudo-elements, inset shadows and gradient overlays. Default to no strip. If a semantic marker is justified, keep it short and OUTSIDE the surface with visible separation. Focus indicators, progress charts, timelines and status glyphs are not prohibited when used meaningfully.

Sidebar navigation: use selected background/text/icon where suitable; any selected indicator rail sits outside its item, with visible separation, and never substitutes for focus. Keep router-selected state, keyboard state and label semantics correct.

## 6. Component library first

Before bulk interactive page development, inspect existing dependencies and select ONE suitable primary component library or accessible primitive stack for the actual framework. Only install an additional library if that change is within the user's delegated implementation scope and dependency policy; otherwise reuse a sound native component or report what is blocked. Map Button, Field, Select, Combobox, DropdownMenu, Checkbox, Radio, Switch, Dialog, Tabs and Popover to real components and test their critical states.

Avoid hand-built click-only div controls. A light static page or genuine native interaction can justify no dependency, but not broken semantics. An authorized implementation does not imply approval to change global Agent configuration or install unrelated host tools. UI libraries cannot replace testing focus, keyboard, disabled/loading/error, popover positioning, theme, text wrapping and actual business results. React primitives cannot be copied into Vue unchanged.

Shared components should have a clear state owner, semantic API, documented variants and a common token source. Do not create multiple styling systems or a boolean-prop maze.

**Mixed-control consistency is mandatory when polishing an existing interactive UI:** inspect real imports and native/custom/library controls; choose the primary implementation from the project's actual page mode, approved visual language, framework, interaction coverage, accessibility, performance and migration constraints. Favor a coherent existing library or primitive stack over adding another styled system. Check both closed and expanded Select/Combobox/Menu surfaces; OS-owned native select popups may not be fully themeable with CSS. Keep deliberate native controls when appropriate and documented. `scripts/audit_control_consistency.mjs` gives candidates, not vendor attribution or real-page verification. See `references/component-consistency-and-selection-gate.md`.

## 7. Motion quality and continuity

For meaningful interactions, specify:

trigger → before → in-motion relationships → payoff → interrupt/reverse → reduced-motion

Preserve object identity and spatial anchors. Coordinate neighboring layout and text/numeric reflow. Show prompt press feedback before async work finishes, while keeping pending/error states honest. Stagger and overlap only when it serves causal understanding; more animation is not automatically better.

Check fonts, wrapping, remount/re-entry, stale promises, listeners and cleanup. The reduced-motion path must keep the same semantics, business results, focus restoration and meaningful feedback.

For high-impact motion capture real target-page before/action/during/settled states; begin evidence sampling before the click, review normal-speed playback plus a frame contact sheet, interrupt transitions and verify reverse/reduced paths. The motion recorder provides heuristic jump/anchor candidates, not an automated taste verdict. Only creative looping interfaces need loop-seam and hidden-tab checks.

A synthetic mouse, device frame or marketing scene cannot count as production interaction testing.

## 8. Data, interaction and framework boundaries

For charts, keep data units, axis legends, plot alignment, sample size and missing-data semantics explicit. Missing data is not automatically zero. Comparison pages must synchronize selected entities, legends, series, time ranges and table columns. Run-monitor screens must expose true statuses, denominator stability and legally available actions, not fake progress.

For settings/forms, distinguish individually saved preferences from grouped submission. Include real input, disabled, pending, success, failure, retry, permission and unsaved-change behavior.

Vue/Nuxt: prefer computed derived state, props-down/events-up, lifecycle cleanup for observers and animations; avoid browser DOM access in SSR.
React/Next: monitor actual request waterfalls, bundle impact, rerenders, server/client boundaries and stale effects; avoid unnecessary memoization or props exploding into invalid combinations.
Other stacks: follow installed framework conventions and baseline browser semantics instead of porting another ecosystem's internals.

Performance claims need actual timing/memory/runtime evidence, never only static CSS analysis.

## 9. Evidence and acceptance

| Outcome | What it really means |
| --- | --- |
| VERIFIED | Affected actual product page and specified interactions, viewports and states were checked with evidence |
| STATIC CHECK | Source/rule/schema inspection only; no browser proof |
| DEMO ONLY | Bundled synthetic example only |
| NOT TESTED | Relevant test was not performed |
| BLOCKED | Missing permission, source, browser, backend or environment |

A screenshot cannot prove backend correctness. A sample gallery cannot prove product usability. A static scanner can only identify possible risks, not guarantee aesthetic, performance or accessibility quality.

For every significant finding record route/selector, viewport/locale, expected versus observed, evidence, file:line, severity, fix and retest. Browser automation must first inspect the rendered DOM and reachable state, not invent a selector from the initial prompt. Separate permission, request, console and server-backend errors. On major changes, review UX/IA separately from visual treatment. For significant motion, prefer a fresh-eye reviewer not involved in the implementation.

## 10. Efficient execution and consent

1. Inspect only applicable route/component and a few relevant references; expand when evidence shows a gap.
2. Preserve existing user decisions and project boundaries. Do not run global hooks, install libraries, scrape unauthorized sites, export project screenshots or rewrite production code without relevant permission.
3. Prefer existing project scripts and browser tooling. Optional MauForma tools include: audit_frontend.py, mauforma_check.py, check_design_drift.py, motion_rehearsal.mjs, extract_design_dna.mjs, feature_design_flow.py and preview_design_variants.py.
4. Report final changes, concrete real test results, scope, non-verified states and blockers. The status CAPTURED_FOR_REVIEW never means VERIFIED.

For a genuine scope, permission, locale or verification ambiguity, read **only the relevant numbered rule** in `references/semantic-boundaries.en.md`. A separate Chinese version and `assets/semantic-boundary-contract.json` support maintenance of translation parity; neither is needed for an ordinary task.

For deeper specifics use the task-specific documents already routed in SKILL.md. The public Chinese `README.zh-CN.md` is an introduction, not a second Agent runtime contract.
