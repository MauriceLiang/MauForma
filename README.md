<div align="center">

# MauForma

**Design with intent. Build with precision.**

**Framework-agnostic Web UI/UX Design & Frontend Engineering Skill**
面向高品质界面、精致动效与可验证工程交付的 AI Agent Skill。

[English](README.md) · [简体中文](README.zh-CN.md)

[Overview](#overview) · [Capabilities](#capabilities) · [Quick start](#quick-start) · [Reference guide](#reference-guide) · [Quality assurance](#quality-assurance) · [Acknowledgments](#open-source-influences-and-acknowledgments)

</div>

---

## Overview

MauForma is an Agent Skill for designing, implementing and reviewing real Web products. It helps AI agents understand user tasks and actual content before choosing layout, typography, components, design tokens, accessible interactions and motion.

It is **not** a UI library, one-size-fits-all dashboard template, animation-engine installer or automated promise of visual quality. The active design authority is the user and their project, not the Skill.

The primary Agent instruction is **[SKILL.md](SKILL.md)** (English-first and concise). A standalone [English execution handbook](references/execution-handbook.en.md) covers key principles; detailed topic references and reusable validators live under [references](references/) and [scripts](scripts/). A full [Chinese version of the public guide](README.zh-CN.md) and the archived [Chinese skill contract](SKILL.zh-CN.md) support local readers and migration parity. Do **not** load both instruction entrypoints in the same Agent task by default.

## Capabilities

| Area | What MauForma does |
| --- | --- |
| User experience | Audience, user journeys, information architecture, content hierarchy |
| Visual direction | Typography, palettes, spacing, art direction and composition |
| Component engineering | Existing component systems, reusable primitives, interaction states |
| Motion design | Purposeful state transitions, choreography, continuity, interruption and reduced motion |
| Quality assurance | Real-page visual review, accessibility, keyboard behavior, responsive boundaries |
| Evidence workflows | Design DNA, token drift, scoped code review, motion frame evidence and resumable feature tasks |

**Supported interfaces:** Vue/Nuxt, React/Next, Svelte/SvelteKit, Angular, Solid, Astro, standard Web technologies and Web frontends embedded in Electron/Tauri. Native SwiftUI, AppKit and Android views are not direct code targets.

**Product modes:** Operate, Read, Persuade and Experience. A product can use different modes on different pages; none is a mandatory house style. MauForma does not impose mobile layouts on desktop-only tools or require dramatic animation on dense workbenches.

## Design and engineering principles

1. **Respect the existing product.** Preserve approved branding, layout choices, data behavior, navigation and technical stack unless the user requests a change.
2. **Solve information architecture before decoration.** Prioritize actual content, authentic controls and the real primary task.
3. **Component library first where interaction exists.** Inspect existing dependencies, select framework-appropriate accessible primitives, apply tokens and verify open/selected/focus/loading states before duplicating pages.
4. **Text must earn its place.** Review decorative eyebrow/overline/kicker text on **new and existing** screens. Keep real breadcrumbs, approved taglines, statuses and genuinely useful context. On task-oriented pages, redundant pre-H1 explanation is prohibited (Gate H0; [page-header policy](references/page-header-antipatterns.md)).
5. **Do not attach decorative colored edge bars to cards.** For new and existing Card/Panel/Section surfaces, reject colored strips that merge into a rounded edge. A semantic external marker must be separate and visibly spaced; focus, progress and charts retain their real function ([Gate S0](references/surface-edge-accent-gate.md)).
6. **Motion is behavioral craft.** Show immediate response, preserve state continuity, respect reduced motion and allow interruption. Strong effects are valuable when purposeful, not by default ([Motion Craft](references/motion-craft-and-continuity.md); [Motion Rehearsal](references/motion-rehearsal-and-evidence.md)).
7. **Verify, don't merely assert.** Static checks are hints. A synthetic demo is not evidence that the user's real product, API or actual animation passed.

## Quick start

Install this repository as a Skill in your Agent's supported skills directory and invoke **mauforma** for Web product tasks. The actual installation path depends on the Agent host. Most design guidance is reference documentation; **do not install every listed library**.

Example commands (run from the MauForma repository root; target paths are examples):

- Search by real product intent: python3 scripts/search_design_knowledge.py --query "content reading" --mode Read
- Explore suitable visual tools: python3 scripts/search_visual_tech.py --goal "interactive data visualization"
- Audit target frontend source: python3 scripts/audit_frontend.py ./src --format json
- Audit changed files with precise findings: python3 scripts/mauforma_check.py --root ./target-app --changed src/Page.vue --format json
- Inspect design token drift: python3 scripts/check_design_drift.py --root ./target-app --format json
- Capture optional frame evidence (requires a running dev app plus installed Playwright/Chromium): node scripts/motion_rehearsal.mjs --url http://localhost:3000 --scenario ./my-motion-scenario.json
- Run repository checks: python3 scripts/validate_web_skill.py ; python3 scripts/validate_skill_hygiene.py ; python3 -m unittest discover -s tests -v

### Interactive examples

[Motion Continuity Lab](assets/motion-continuity-lab.html) is an **original synthetic demonstration**, showing selected state, spatial transition and input feedback. To inspect motion with Playwright, run a local static HTTP server and the bundled example [scenario](assets/motion-continuity-lab.scenario.json); this proves only the lab behavior and does not verify a real product.

Liquid Glass is an **optional** experimental visual material, not a default product skin. Read [optics guidance](references/liquid-glass-optics.md) and [the isolated optical lab](assets/liquid-glass-layer-lab.html) only when a user requests that visual direction. Respect browser compatibility and accessibility fallbacks.

## Efficient execution and boundaries

The execution entrypoint routes tasks into a small number of relevant reference documents, generally **1–3 groups rather than the whole library**. Use the shortest effective workflow:

| Mode | Typical work | Verification |
| --- | --- | --- |
| shape | New project or major design | Real layout and flows, target viewport |
| polish | Existing interface refinement | Before/after actual page and relevant states |
| review | Independent critique | Findings with evidence, no unrequested code edits |
| fidelity | Authorized Figma implementation | Source design and same-viewport comparison |
| fix | Localized defect | Reproduction, minimal change and targeted regression |

### Evidence boundaries

**VERIFIED** requires direct evidence on the affected real product pages and flows. **STATIC CHECK** is source inspection only. **DEMO ONLY** covers bundled synthetic pages. **NOT TESTED** and **BLOCKED** must be reported honestly. A generated screenshot, heuristic scanner or simulated backend is not a substitute for functional/browser QA.

The agent must not silently install global hooks, change user branding, replace the framework, clone protected design assets, capture private websites or upload customer screenshots. Read [English execution handbook](references/execution-handbook.en.md) and [evidence workflow guide](references/skill-gap-workflows.md) for precise boundaries.

## Reference guide

| Task | Reference |
| --- | --- |
| Design craft and critique | [Design Craft Loop](references/design-craft-loop.md), [visual critique](references/visual-critique-loop.md) |
| Product discovery and direction | [Design discovery](references/design-discovery-interview.md), [page modes](references/product-experience-routing-gate.md) |
| Visual hierarchy and composition | [Composition-first](references/composition-first-design.md), [visual QA](references/visual-qa.md) |
| Components and system design | [Component Library First](references/component-library-first-gate.md), [shared design system](references/design-system.md) |
| Forms and navigation | [Settings/form layout](references/settings-form-layout-gate.md), [navigation architecture](references/navigation-architecture.md) |
| Motion and continuity | [Motion Craft](references/motion-craft-and-continuity.md), [Rehearsal](references/motion-rehearsal-and-evidence.md) |
| Browser and accessibility | [Browser QA](references/browser-qa-protocol.md), [Visual QA](references/visual-qa.md) |
| Figma fidelity | [Figma workflow](references/figma-fidelity-workflow.md) |
| Scripted evidence | [Executable workflows](references/skill-gap-workflows.md), [English handbook](references/execution-handbook.en.md) |

The detailed legacy references are primarily Chinese today; the English entrypoint and English handbook provide a fully usable **English core**. Deep-topic translation is staged separately to protect technical meaning and maintain runnable checks. No false claim of full reference-library translation is made.

## Quality assurance

Checks cover Skill structure, routing, token and UI design contracts, component strategy, visual anti-patterns and browser smoke tests on **synthetic fixtures**. They cannot validate an arbitrary external application without its source, runtime and explicit permissions.

- Repository quality: [GitHub Actions](.github/workflows/skill-quality.yml).
- Test source: [tests](tests/) and [scripts](scripts/).
- Design QA: actual states, focus/keyboard behavior, supported locales, typography, scroll reachability, responsive bounds and motion preferences.
- Locale QA: bilingual README presence and consistent English runtime boundaries, without assuming an English product UI.

## Open source influences and acknowledgments

MauForma is informed by generous public design and frontend engineering work. Special thanks to **Benji Taylor's Stageshow** for its thoughtful treatment of motion narratives, causality, continuity, choreography, frame evidence and independent review. The general principles are adapted into original framework-agnostic guidance for real applications, not copied as a React animation kit or demo code.

### Design Skills and methodology

| Project | Lessons and inspiration |
| --- | --- |
| [Stageshow — Benji Taylor](https://github.com/benjitaylor/skills/tree/main/stageshow) | Motion narrative and frame-based rehearsal |
| [Frontend Design — Anthropic](https://github.com/anthropics/skills/tree/main/skills/frontend-design) | Authorial direction and non-template UI |
| [Impeccable — Paul Bakaus](https://github.com/pbakaus/impeccable) | Systematic visual craft |
| [Taste Skill — senlindesign](https://github.com/senlindesign/taste-skill) | Design DNA, evidence and judgment |
| [Taste Skill — Leonxlnx](https://github.com/Leonxlnx/taste-skill) | Visual variation and verification |
| [Theme Factory — Anthropic](https://github.com/anthropics/skills/tree/main/skills/theme-factory) | Consistent theme selection |
| [Designer Skills — julianoczkowski](https://github.com/julianoczkowski/designer-skills) | Brief-to-task and iterative review |
| [UI/UX Pro Max — nextlevelbuilder](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill) | Searchable direction knowledge and page overrides |
| [Web Design Guidelines — Vercel](https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines) | File/line-specific UI critique |
| [Composition Patterns — Vercel](https://github.com/vercel-labs/agent-skills/tree/main/skills/composition-patterns) | Better component state boundaries |
| [React Best Practices — Vercel](https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices) | React rendering, requests and bundles |
| [Vue Best Practices — vuejs-ai](https://github.com/vuejs-ai/skills/tree/main/skills/vue-best-practices) | Vue component and reactivity contracts |
| [Webapp Testing — Anthropic](https://github.com/anthropics/skills/tree/main/skills/webapp-testing) | Real browser evidence |
| [Figma Implement Design — OpenAI](https://github.com/openai/skills/tree/main/skills/.curated/figma-implement-design) | Faithful design-to-code workflows |

Additional Stageshow references: [Motion](https://github.com/benjitaylor/skills/blob/main/stageshow/references/motion.md), [Choreography](https://github.com/benjitaylor/skills/blob/main/stageshow/references/choreography.md), [Verify](https://github.com/benjitaylor/skills/blob/main/stageshow/references/verify.md), [Rehearse](https://github.com/benjitaylor/skills/blob/main/stageshow/references/rehearse.md), and [Review](https://github.com/benjitaylor/skills/blob/main/stageshow/references/review.md).

### Specifications and design ecosystems

Thanks to [IBM Carbon](https://carbondesignsystem.com/), [Material Design](https://m3.material.io/), [W3C WAI/WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/), [MDN](https://developer.mozilla.org/), [WebKit](https://webkit.org/), [Lucide](https://lucide.dev/), [Tabler Icons](https://tabler.io/icons) and [Phosphor Icons](https://phosphoricons.com/).

Technology ecosystem references include [Motion](https://motion.dev/), [GSAP](https://gsap.com/), [Anime.js](https://animejs.com/), [AutoAnimate](https://auto-animate.formkit.com/), [Rive](https://rive.app/), [LottieFiles](https://lottiefiles.com/), [React Bits](https://reactbits.dev/), [Vue Bits](https://vue-bits.dev/), [Reka UI](https://reka-ui.com/), [Radix](https://www.radix-ui.com/primitives), [shadcn/ui](https://ui.shadcn.com/), [shadcn-vue](https://www.shadcn-vue.com/), [Ant Design](https://ant.design/), [Element Plus](https://element-plus.org/), [Three.js](https://threejs.org/), [PixiJS](https://pixijs.com/) and [ECharts](https://echarts.apache.org/). They are potential references, **not automatic dependencies**.

MauForma does not claim any upstream author's endorsement. This README acknowledgment does not replace third-party licenses when actual code, icons, fonts or assets are reused. The retained [Lucide license notice](assets/icon-art-direction-lucide-license.txt) governs the bundled Lucide sample artwork. Consult the original project's license and API documentation before redistributing anything.

[Release history](CHANGELOG.md) · [简体中文文档](README.zh-CN.md)
