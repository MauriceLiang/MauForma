# MauForma — Semantic Boundaries (English)

This is a **task-specific interpretation aid**, not a second entrypoint. Start with SKILL.md. Read only the relevant B-code if a question concerns authority, language, scope, exceptions or verification. The paired Chinese source is semantic-boundaries.zh-CN.md. The machine-readable source is assets/semantic-boundary-contract.json; test both versions before changing either.

## B01 — Task authority / 任务与授权

- **Trigger**: Any design or implementation request
- **Required**: Preserve explicit user instructions, approved design decisions and existing functional contracts; scope changes to the asked task.
- **Exception**: A user-approved redesign may intentionally replace the affected visual direction; record which decisions changed.
- **Forbidden**: Never infer that a Skill style override outranks the user's approved choices.
- **Deep references**: `SKILL.md`, `references/project-design-hierarchy.md`

## B02 — Language vs product locale / 指令语言与产品语言

- **Trigger**: An Agent reads English instructions or works on a localized UI
- **Required**: Keep replies and product copy in the user's or existing product locale; verify actual text, CJK wrapping and numbers.
- **Exception**: Translate product copy only if the user requests localization or the product requirements require that locale.
- **Forbidden**: Never translate an existing UI to English solely because MauForma's entrypoint is English.
- **Deep references**: `SKILL.md`, `references/execution-handbook.en.md`

## B03 — Reference loading / 按需读取

- **Trigger**: Any task using references
- **Required**: Load one primary relevant guide; add secondary guides only for specific identified needs. A reference table lists choices, not mandatory steps.
- **Exception**: Complex implementation or a verified blocker can justify more than three guides when each addition is relevant.
- **Forbidden**: Never load the entire Skill reference library or every validator by default.
- **Deep references**: `SKILL.md`, `references/semantic-boundaries.en.md`

## B04 — Component dependency / 组件与安装权限

- **Trigger**: An interactive page needs controls
- **Required**: Inspect and reuse the installed accessible library first; map required controls to real components and test states.
- **Exception**: If none exists, a new compatible dependency may be installed only within the user's delegated implementation and dependency policy; otherwise use sound native controls or report the blocker.
- **Forbidden**: Never silently install global tooling or replace real controls with click-only div elements.
- **Deep references**: `references/component-library-first-gate.md`, `references/execution-handbook.en.md`

## B05 — Optional visual effects / 可选视觉特效

- **Trigger**: Liquid glass, cinematic/looping motion or experimental effects appear in a task
- **Required**: Use such effects only when explicitly requested or clearly inherited from an approved product brief; test fallback and accessibility.
- **Exception**: A marketing illustration may be deliberately expressive; a dense workbench may remain static and compact.
- **Forbidden**: Never make a demo effect or aesthetic preset a global default for all pages.
- **Deep references**: `references/liquid-glass-optics.md`, `references/motion-craft-and-continuity.md`

## B06 — Page-header H0 / 页头文字 H0

- **Trigger**: Creating, editing or reviewing a page title, including legacy content
- **Required**: Inspect pre-H1 copy; remove or move redundant explanation on task pages; preserve real breadcrumbs, status and approved branding.
- **Exception**: Meaningful chapter labels and intentional brand/marketing narratives may remain when justified.
- **Forbidden**: Never retain meaningless old eyebrow text merely because it already exists.
- **Deep references**: `references/page-header-antipatterns.md`, `references/semantic-copy-hygiene.md`

## B07 — Surface accent S0 / 卡片贴边彩条 S0

- **Trigger**: Creating or reviewing Card/Panel/Section surfaces
- **Required**: Remove decorative thick colored strips attached to rounded card borders on both new and affected legacy views.
- **Exception**: Actual focus indicators, chart series, progress and status semantics remain valid; a needed outside marker must have a visible gap.
- **Forbidden**: Never reintroduce a flush colored border, inset shadow or pseudo-element as a decorative card stripe.
- **Deep references**: `references/surface-edge-accent-gate.md`, `references/execution-handbook.en.md`

## B08 — Figma authority / Figma 输入权限

- **Trigger**: A user asks to implement an existing Figma design
- **Required**: Identify exact design file, frame/node, source assets, design context and screenshot when available; compare real implementation at the same viewport.
- **Exception**: Desktop current-selection is available only with a compatible desktop connection; remote providers may require explicit Figma file and node URL. Screenshot-only work is approximate.
- **Forbidden**: Never fabricate Figma tool access, unprovided asset details or unconditional pixel-perfect parity.
- **Deep references**: `references/figma-fidelity-workflow.md`, `references/execution-handbook.en.md`

## B09 — Scope of viewport / 支持视口范围

- **Trigger**: Responsive or viewport QA
- **Required**: Test the supported product breakpoints, declared minimum viewport, content reachability and relevant text zoom.
- **Exception**: Only test a 390px mobile layout when mobile support is in scope; desktop-only products still need their smallest supported desktop view.
- **Forbidden**: Never add mobile support or force a mobile-first redesign without a product requirement.
- **Deep references**: `references/browser-qa-protocol.md`, `references/product-experience-routing-gate.md`

## B10 — Evidence claim / 验证结论

- **Trigger**: Claiming any test, visual or business result
- **Required**: Specify actual route, state, viewport, data and evidence; use VERIFIED only for the tested scope.
- **Exception**: Static code analysis is STATIC CHECK; synthetic fixtures are DEMO ONLY; missing conditions are NOT TESTED or BLOCKED.
- **Forbidden**: Never infer backend persistence from screenshots or smooth animation from a heuristic trace.
- **Deep references**: `references/browser-qa-protocol.md`, `references/motion-rehearsal-and-evidence.md`

## B11 — Review vs implement / 评审与实施区分

- **Trigger**: Review-only, bug-fix, redesign or general polish request
- **Required**: Review-only means findings without edits; a scoped fix requires actual regression checks; major redesign includes design direction and broader QA.
- **Exception**: Independent formal design critique is valuable for substantial visual change but not mandatory for a one-line bug fix.
- **Forbidden**: Never turn a review request into source edits or a tiny fix into an unrequested interview.
- **Deep references**: `references/design-craft-loop.md`, `SKILL.md`

## B12 — Design drift meaning / 设计漂移含义

- **Trigger**: An observed token, schema or design-document drift is reported
- **Required**: Distinguish tool version drift, schema drift and product truth drift; code-derived token snapshots are observations, not approved design decisions.
- **Exception**: Mechanical migration may be suggested for schema changes with explicit approval; truth drift requires checking real product intent and rendered evidence.
- **Forbidden**: Never silently overwrite MASTER or brand decisions to make drift checks green.
- **Deep references**: `references/project-design-hierarchy.md`, `references/skill-gap-workflows.md`

## B13 — Reference research and assets / 参考研究与素材边界

- **Trigger**: Analyzing external websites, adopting upstream rules or borrowing visual assets
- **Required**: Only access authorized sources; distinguish measured WHAT from inferred WHY and check licensing for copied materials.
- **Exception**: If browsing is blocked or a style query yields no domain-relevant result, refine with available evidence or report missing evidence.
- **Forbidden**: Never infer source-site designer intent, invent design data or copy protected assets.
- **Deep references**: `references/design-dna-protocol.md`, `references/design-reference-learning-gate.md`

## B14 — Browser reconnaissance / 浏览器先观察后操作

- **Trigger**: Opening a running application for browser tests
- **Required**: Inspect live DOM and current page state before choosing selectors; capture browser console and relevant network errors, then interact and retest.
- **Exception**: When the browser, app server or permissions are unavailable, report NOT TESTED/BLOCKED without manufacturing selectors or expected results.
- **Forbidden**: Never substitute a synthetic in-memory demo for actual server-backed workflow verification.
- **Deep references**: `references/browser-qa-protocol.md`, `references/execution-handbook.en.md`

## B15 — RTL and locale / RTL 与本地化

- **Trigger**: Product includes RTL languages, locale-sensitive inputs or internationalized content
- **Required**: Use locale-aware date/number formatting and meaningful CJK/RTL text tests, including logical properties when RTL is supported.
- **Exception**: RTL is conditional on actual supported locales; do not add a new RTL feature to a locale-limited desktop app.
- **Forbidden**: Never infer locale from user IP or block ordinary paste without a security reason.
- **Deep references**: `references/browser-qa-protocol.md`, `references/execution-handbook.en.md`


**Interpretation rule:** an exception must not erase a prohibition; a prohibition must not erase genuine semantic exceptions. If task intent and evidence are unresolved, explain the uncertainty and keep the existing product choices. Browser tests and AI behavior scores are separate from this static documentation check.
