# Screenshot-Recommended Frontend Stack — 11 Categories, 12 Distinct Technologies

> The screenshot showed **11 rows**: UI components (two), creative visual components (two), icons, motion, styling, layout, drag/drop, state, data fetching and charts. Expanding the first categories gives **12 distinct libraries/technologies**. **Not an installation checklist.** Official information was checked **2026-11-02**; installed lockfile versions and current official documentation take precedence when APIs change.

## Understanding the layers

- **Framework:** Vue/React/Svelte/Angular own components, state and lifecycle.
- **Interaction primitives:** Reka/Radix/Base UI/Bits UI provide keyboard, focus and ARIA behavior.
- **Styled components:** shadcn/ui, shadcn-vue and existing suites combine those primitives with design Tokens.
- **Creative and icons:** Magic UI/Aceternity are expressive visual systems; Lucide supplies ordinary functional icons.
- **Motion:** Motion/Anime.js/GSAP/CSS; choose according to actual needs and ensure **no two systems fight over the same animated property**.
- **Layout/drag:** Resizable splits, reorder and drag/drop are interaction systems, **not synonyms for animation libraries**.
- **State/data:** Zustand-like tools own shared **client** state; TanStack Query-like tools own remote **server** state.
- **Data presentation:** Recharts/ECharts map authentic data to interpretable charts.

## 01 — UI components: shadcn/ui

- **Framework:** React / Next.js; not directly usable as Vue components.
- **Contents:** Components copied into and maintained by the project, theme variables, CLI and composed Button/Dialog/Table/Select/Sidebar; typically built on Base UI, Radix or React Aria primitives.
- **Purpose:** Build a coherent visual component system with accessible behavior and source ownership.
- **Appropriate use:** Inspect existing components.json/primitives, install only needed project components, modify shared variants/CSS Tokens/state, and verify in a component Gallery.
- **Pitfalls:** It is **not** one opaque npm package you must continually depend on; do not paste React TSX into Vue; a project using Radix need not migrate merely because the latest default changed to Base UI.
- **Alternatives:** Vue shadcn-vue (often Reka UI), Svelte shadcn-svelte, other framework-specific ports.
- **Official:** https://ui.shadcn.com/docs

## 02 — Interaction primitives: Radix UI / Base UI

- **Framework:** Separate React primitive ecosystems.
- **Contents:** Dialog, Popover, Select, Dropdown, Tabs, Tooltip, Focus and related accessible behavior. They own focus, ARIA and keyboard handling, **not a product-specific skin**.
- **Purpose:** Build a bespoke visual design without rewriting high-risk interaction engines.
- **Appropriate use:** Wrap inherited primitives as UiDialog/UiSelect/UiPopover, use a single token system and follow official composition APIs.
- **Pitfalls:** Base UI render is **not** Radix asChild. data-* semantics, positioning and event signatures differ; do not follow outdated tutorials blindly.
- **Alternatives:** Vue Reka UI, Svelte Bits UI, Angular CDK, Solid Kobalte/Ark UI.
- **Official:** https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default

## 03 — Creative components: Magic UI

- **Framework:** Mostly React/Next with Tailwind and shadcn ecosystem.
- **Contents:** Installable animated decoration, backgrounds, text effects, promotional components/sections, often using a registry approach.
- **Purpose:** Add selective expressiveness to landing pages, brands, portfolios and focused product presentation.
- **Appropriate use:** Choose **1–2 genuinely justified** visual sections, map colors/spacing/type to the product design system, control scrolling and energy cost.
- **Pitfalls:** Effects never replace basic forms, real Dialog behavior, content or accessibility. Do not let marketing effects spread into administration tables.
- **Vue:** Transfer concepts and implement with Vue-native/Motion Vue/Anime.js; never import React components directly.
- **Official:** https://magicui.design/docs/installation

## 04 — Creative components: Aceternity UI

- **Framework:** Primarily React / Next.
- **Contents:** Copyable visual components for 3D, Card interactions, text/image transitions and animated backgrounds.
- **Purpose:** A small number of signature visual moments for portfolios, brand Heroes or event pages.
- **Appropriate use:** Review specific component source, dependencies and license; isolate creative presentation; keep global tokens coherent and provide reduced-motion fallback.
- **Pitfalls:** Do not stack every effect or assume a decorative demo is an accessible, clickable business component.
- **Other frameworks:** Reimplement with corresponding framework and animation APIs; do not paste TSX into Vue/Svelte/Angular.
- **Official:** https://ui.aceternity.com/components

## 05 — Icons: Lucide

- **Framework:** React, Vue, Svelte, Solid, Angular, Vanilla via different packages.
- **Contents:** A large consistent SVG outline family supporting size, color, stroke width, accessible labeling and selective imports.
- **Purpose:** Share one functional icon language rather than accumulating unrelated libraries.
- **Appropriate use:** Coherent 16/18/20px roles and stroke-width, decorative icons aria-hidden, icon-only buttons aria-label.
- **Pitfalls:** Do not import Vue packages in React; avoid indiscriminate mixing of emoji/3D/outline icons; verify package names for actual installed version.
- **Examples:** React lucide-react; newer Vue @lucide/vue, older Vue projects often lucide-vue-next.
- **Official:** https://lucide.dev/packages

## 06 — Motion (formerly Framer Motion)

- **Framework:** React, Vue and plain JavaScript have distinct entry points.
- **Contents:** Declarative motion components, presence/exit, layout continuity, springs, gestures/dragging and scroll motion; JS can animate DOM/SVG.
- **Purpose:** Press feedback, state-driven transitions, list layout changes and gestures.
- **Appropriate use:** React motion/react; Vue motion-v. Prefer CSS when enough, and clean animation lifecycles when components unmount.
- **Pitfalls:** Do not let Anime.js and Motion animate the **same element's transform** concurrently. Old framer-motion imports are not automatically the new canonical API. Do not add arbitrary spring effects.
- **Other stacks:** Motion's plain JavaScript APIs, CSS or WAAPI.
- **Official:** https://motion.dev/docs

## 07 — Styling: Tailwind CSS

- **Framework:** Vue/React/Svelte/Angular/Astro/Vanilla and more.
- **Contents:** Utility-first CSS, responsive/state variants, themes and design Tokens compiled through build tooling.
- **Purpose:** Rapid coherent spacing/type/responsive styling without duplicating page CSS.
- **Appropriate use:** Define semantic Tokens, type and radius first; then shared component variants. Follow official version-specific Vite/Next setup.
- **Pitfalls:** Repeated raw HEX and arbitrary radii lead to drift; Tailwind **does not implement Dialog focus management**.
- **Alternatives:** CSS Modules, ordinary CSS or UnoCSS where existing solutions suffice; no forced migration.
- **Official:** https://tailwindcss.com/docs/installation

## 08 — Resizable layout: react-resizable-panels

- **Framework:** React-specific.
- **Contents:** Group, Panel and Separator with resize/collapse, size limits, default layouts, keyboard resizing and persistence.
- **Purpose:** Editors, IDE-like workspaces and complex data apps with adjustable split views.
- **Appropriate use:** Visible and keyboard-operable handles, min/max widths, SSR restoration strategy and one shared split-view component.
- **Pitfalls:** Do not introduce for ordinary one/two-column layout; do not omit constraints and crush content; do not install unchanged in Vue.
- **Vue:** Reka UI Splitter; other stacks need compatible accessible split panes or CSS Grid.
- **Official:** https://github.com/bvaughn/react-resizable-panels

## 09 — Drag and drop: dnd-kit

- **Framework:** Recent versions support DOM and adapters for React/Vue/Svelte/Solid; **verify exact version**.
- **Contents:** Sources/targets, sensors, sorting, collision detection, overlays and drag state, wrapped by framework adapters.
- **Purpose:** Kanban reorder, sortable lists and draggable panel arrangements.
- **Appropriate use:** Check whether project uses old packages or new adapters. Support grab handles, drag feedback, touch/keyboard alternatives and undo.
- **Pitfalls:** Animation library is not an accessible drag system. Do not depend solely on mousemove; never mix API examples for old @dnd-kit/core with new @dnd-kit/react.
- **Packages:** Newer @dnd-kit/react, @dnd-kit/vue etc.; older projects may use @dnd-kit/core and @dnd-kit/sortable.
- **Official:** https://github.com/clauderic/dnd-kit

## 10 — Client state: Zustand

- **Framework:** Mainly React with a vanilla store option.
- **Contents:** Store creation, selectors, subscriptions, local state organization and middleware for cross-component client state.
- **Purpose:** Global dialogs, preferences, collapsed Sidebar, editing drafts and filters.
- **Appropriate use:** Keep local state local; reuse Zustand if existing and truly needed across trees. Handle business cache invalidation separately.
- **Pitfalls:** Zustand is **not remote request caching**. Vue apps should not blindly copy React Zustand hooks.
- **Alternatives:** Vue Pinia/composables, Angular Signals, Svelte runes/stores, Solid signals.
- **Official:** https://zustand.docs.pmnd.rs/

## 11 — Server state: TanStack Query

- **Framework:** Separate React, Vue, Solid, Svelte, Angular adapters.
- **Contents:** Query keys/caches, refetch, loading/errors, mutations, invalidation, pagination/infinite scroll, network recovery and devtools.
- **Purpose:** Remote table paging, user details, search results, cross-route caches and refresh after writes.
- **Appropriate use:** Distinguish client vs server state. React @tanstack/react-query; Vue @tanstack/vue-query. Invalidate/update after mutations; account for auth and real failures.
- **Pitfalls:** Query is **not an authorization server**. Do not infinitely retry non-idempotent operations or maintain redundant server-state copies in both Query and Zustand/Pinia.
- **Alternatives:** Framework-specific adapters; when Next/Nuxt already has a data layer, compare roles before adding.
- **Official:** https://tanstack.com/query/latest

## 12 — Charts: Recharts

- **Framework:** React-specific charts.
- **Contents:** Line/Area/Bar/Pie/Scatter/Composed/Radar/Treemap, axes, legends, Tooltip, responsive containers and animation props.
- **Purpose:** Conventional reports, trends, comparisons and metrics in React dashboards.
- **Appropriate use:** Real values, units, zero/error distinctions, coherent color Tokens/legends/Tooltip; avoid misleading truncated scales.
- **Pitfalls:** Do not animate or alter original data to create a better-looking number. React Recharts code does not run directly in Vue.
- **Other frameworks:** Vue/multi-stack Apache ECharts with adapters such as vue-echarts; Chart.js and other current alternatives can also fit; verify APIs/versions.
- **Official:** https://recharts.github.io/en-US/examples/

## Executable Vue/React decision examples

**A — Existing Vue 3 + Reka UI admin:** Keep Vue and Reka. Shared Button/Form/Dialog; add Pinia only for actual shared client state, TanStack Vue Query only for true caching/invalidation, Reka Splitter only for split panels, ECharts only if chart complexity warrants. **Do not install Anime.js, GSAP, Motion and Magic UI solely for one Button hover.**

**B — Existing React + shadcn/ui(Radix) workbench:** Keep the installed Radix stack; do not migrate because a documentation default changed to Base UI. For multi-editor layout evaluate react-resizable-panels; use dnd-kit matching the installed version; simple CSS effects first, Motion for justified layout/state transitions.

**C — Marketing event site:** A small subset of React Magic UI/Aceternity visuals can be appropriate, but **performance, CTA visibility, mobile usability and reduced-motion are hard acceptance requirements**. Astro + CSS + small interactive islands may be significantly lighter.

## Licensing and update obligations

- Before installing/copying anything, check **official license, commercial rights, dependencies, maintenance and component-specific authorization**. Do not assume that every block of every copy-paste creative library is free for commercial use.
- Follow docs for **installed lockfile versions**, not fresh web examples that would break old APIs.
- Recheck fast-changing package names, setup paths, component contracts, branches and SSR compatibility after **three months**.

## v5 extension — Beyond Magic UI and Aceternity UI

- **React Bits:** Copyable React text animation, backgrounds, Cards and micro-interactions; distinguish paid Pro assets from free components.
- **Vue Bits:** Official Vue port of React Bits, Vue 3 + TypeScript + Tailwind, suitable for Vue/Nuxt creative sites.
- **Inspira UI:** Independent Vue/Nuxt creative collection often using shadcn-vue, motion-v and Tailwind.
- **Operational UI:** React Ant Design and Vue Ant Design Vue/Element Plus provide real Form/Table/Select/DatePicker/Feedback; creative animation collections **must not replace** them.

See creative-component-libraries.md and enterprise-ui-library-guide.md by responsibility. **This is not an instruction to install five more dependencies automatically.**
