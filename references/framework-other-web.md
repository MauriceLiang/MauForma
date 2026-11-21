# Adapting Other Web Frameworks — Svelte / Angular / Solid / Astro / Vanilla

**Unify design principles and component contracts, not source code.** Reuse existing project components before considering the following libraries.

## Svelte / SvelteKit

- **Core:** Svelte's component/reactivity model; SvelteKit supplies application routing and server capabilities.
- **Components:** Bits UI provides unstyled headless primitives, keyboard behavior and focus management; shadcn-svelte provides a maintainable UI layer. Prefer one primary component system per project.
- **Motion:** Use Svelte built-in `transition`/`animate` or CSS first; for complex DOM use Anime.js, GSAP or Motion JS with proper destruction cleanup.
- **Data:** SvelteKit `load`/actions suit server-mediated flows; global state should follow the project's actual store approach. Do not introduce React Zustand without purpose.
- **Avoid:** Copying React TSX or Vue `<script setup>` into Svelte components.
- Sources: https://svelte.dev/docs/svelte/overview , https://bits-ui.com/docs/introduction

## Angular

- **Core:** Components, templates, dependency injection, Signals/RxJS and Angular Router, appropriate for complex structured applications.
- **Components:** Angular CDK for primitive behavior; Angular Material, PrimeNG or NG-ZORRO for broader suites. Prefer one principal visual system.
- **Motion:** Prefer CSS/platform capabilities and the Angular motion strategy already adopted by the project. For Anime.js/GSAP, account for component lifecycle and change-detection cost.
- **Data:** HttpClient plus services/caching, using the existing Signals/RxJS and state architecture.
- **Avoid:** Calling React hooks in Angular or rebuilding accessible ARIA behaviors already provided.
- Sources: https://angular.dev/overview , https://material.angular.dev/ , https://primeng.org/

## Solid / SolidStart

- **Core:** Fine-grained Signals and composable UI. Solid's state/rendering model differs from React; do not transplant React Hook tutorials.
- **Components:** Kobalte or Ark UI primitives. Apply tokens, variants and focus styles through coherent app-owned component wrappers.
- **Motion:** CSS/WAAPI, Anime.js and GSAP; verify Solid reactivity and DOM update boundaries.
- **Avoid:** Assuming React hooks or `useState` work in Solid just because both use JSX.
- Sources: https://www.solidjs.com/ , https://kobalte.dev/

## Astro

- **Core:** Content-first static/server HTML; hydrate **only genuinely interactive islands**.
- **Components:** Native Astro components and the inherited CSS design system, with official React/Vue/Svelte/Solid framework integrations where justified.
- **Motion:** CSS/WAAPI first; load costly animation engines only inside specific islands and respect `prefers-reduced-motion`.
- **Avoid:** Converting an entirely static home page into React Client Islands merely for visual effects.
- Source: https://docs.astro.build/en/guides/framework-components/

## Plain HTML / CSS / JS

- **Core:** Semantic HTML, CSS tokens and ES modules. Complex reusable UI may justify Web Components; a big framework is not mandatory simply to be “modern.”
- **Components:** Limited `<template>`, ES modules and Web Components. Prefer correctly semantic native Dialog/Popover behavior, including focus management.
- **Motion:** CSS, Web Animations API or Anime.js/GSAP only as needed. Important content must be visible even when JavaScript animation is unavailable.
- **Avoid:** Accumulating permanent event listeners with no unmount/cleanup, or making the whole page transparent by default.

## Minimum acceptance criteria across all frameworks

Semantic HTML, accessible focus, keyboard/touch operation, supported light/dark themes, narrow layout where required, no duplicated control engines, component states, actual API feedback, no-motion fallbacks and observed performance. The admin PageHeader rule is **not an absolute prohibition on marketing Hero composition**.
