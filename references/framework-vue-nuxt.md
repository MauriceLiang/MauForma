# Vue 3 / Nuxt — Detailed Implementation Guide

## 1. Appropriate use of Vue

Vue 3 is a progressive frontend UI framework. Single-file `.vue` components organize templates, state and scoped styles; Composition API with `<script setup lang="ts">` helps reuse behavior; Vue Router handles SPA navigation. Nuxt adds file-based routing, SSR/SSG, server routes and data loading.

**Continue the existing project's architecture first.** Do not unexpectedly migrate it to React or rebuild scaffolding merely to “unify” a frontend.

## 2. Suggested layers — adapt to current structure

```text
src/
  styles/tokens.css                 # Single design token source
  components/ui/                   # Shared UiButton/UiField/UiDialog
  components/composites/           # Domain-neutral PageHeader/SearchField
  components/patterns/             # List/settings/detail page patterns
  features/users/                  # Domain components, requests and types
  composables/                     # useTheme/usePagination/useKeyboardShortcut
  stores/                          # Pinia when shared client state is needed
  services/                        # API client, error mapping, auth
  pages/ or views/                 # Page composition
  tests/                           # Component and feature tests
```

Nuxt projects should follow Nuxt's `pages/`, `components/`, `composables/`, `server/` conventions; do not force them into a Vite/ordinary Vue layout.

## 3. UI technology routes

| Option | Contents / purpose | Fits | Watch for |
| --- | --- | --- | --- |
| Reka UI | Unstyled Select/Dialog/Tabs/Popover/NavigationMenu/Splitter primitives, keyboard/focus | A highly custom visual system | Requires owned style tokens and business variants |
| shadcn-vue | Copyable Vue component source, CLI and Tailwind style, often based on Reka UI | Consistent and maintainable Vue applications | Not React shadcn/ui source; never mix packages |
| Element Plus | Substantial forms, tables, pagination, date and dialog suite | Data-intensive admin systems | Theme the installed library rather than adding another skin |
| Naive UI / Ant Design Vue | Extensive enterprise components | Many mature controls needed | Select **one primary style system** |
| Tailwind CSS / CSS Modules | Styling tools, not interaction engines | Alongside the above | Centralize tokens; avoid per-page colors and radii |

**First:** Audit current Dialog, Button, Input and Table. Reuse established primitives rather than rewriting a DIV-based dialog.

## 4. Data and interaction

- Local transient component state: `ref`, `reactive`, `computed`.
- Shared cross-page client state (sidebar, user preferences, operation drafts): Pinia when appropriate; retain current project solution first. Do not copy all API responses into a global store.
- Remote **server state** (query caching, retry, invalidation, synchronization): `@tanstack/vue-query` or Nuxt's native data-fetching tools. This is **not** synonymous with Pinia.
- Resizable split panes: Prefer `Reka UI Splitter` with keyboard behavior; don't copy React `react-resizable-panels`.
- Charts: Apache ECharts with the existing Vue integration for complex visuals; an existing Chart.js solution may suit lighter cases.
- Drag and drop: Check the installed dnd-kit Vue adapter/version or established Vue drag libraries. Preserve Button clicks, touch scroll and keyboard accessibility.

## 5. Motion mapping

1. Simple show/hide: Vue `<Transition>` / `<TransitionGroup>` plus CSS.
2. Components and layout transitions: Motion for Vue (`motion-v`), using `<motion />` according to its official API.
3. Complex timelines, SVG and physical effects: Anime.js v4 (imperative and scoped through a component ref; start after `onMounted` and cancel/clean before `onUnmounted`) or GSAP.
4. Scroll-led narrative: GSAP + ScrollTrigger, avoiding conflicts with framework-managed layout properties.
5. SSR: Do not access `window` or construct a DOM animation at the top of `setup`; load only on the client when needed.

## 6. Component-first acceptance

- Start with `UiButton`, `UiField`, `UiPageHeader`; demonstrate disabled/loading/focus/error/long-text/dark states.
- Compare the example `examples/vue3-web-components.md`; adapt implementation to actual installed components.
- Business pages compose shared UI with real logic; copying one-off button styles into each page is an anti-pattern.

## 7. Vue 3 / Nuxt reactivity, ownership and performance gate — task-scoped

- **Single source of truth:** Prefer `computed` for derivable local values, not chains of `watch` that mirror each other's state. Side effects belong to named watchers/event handlers. First inspect the component's responsibility, build configuration and data origin. A small fix needs only relevant Vue material; **do not load all framework Skills**.
- **Data flow and API:** Props down, Events up; use `v-model` for genuine two-way contracts, not to modify parent state secretly from children. Use compound patterns for genuinely complex controls, not decomposition for its own sake.
- **Composables lifecycle:** Stop DOM observers, timers, global handlers, network subscriptions and motion instances in their owning component/composable. Do not instantiate browser objects during SSR.
- **Performance evidence:** Inspect large DOM row counts, deep-reactivity costs, duplicate requests, watcher frequency and whether theme changes remount the entire page. Optimize reactivity boundaries when justified rather than adding heavy caching by default.
- **Forms/display:** Reflect real pending/error/retry after actions; long Chinese labels, keyboard, 200% text scaling and reduced motion must work.
- **Target scope:** Desktop-only products require their minimum supported desktop viewport. Add mobile/RTL support only when genuinely in scope.

Use the existing project's component and browser tests. `scripts/mauforma_check.py` collects low-cost static risk candidates; it does not replace Vue type checks or runtime E2E.

Official:
- https://vuejs.org/guide/introduction.html
- https://nuxt.com/docs
- https://reka-ui.com/docs/overview/introduction
- https://reka-ui.com/docs/components/splitter
- https://shadcn-vue.com/docs/introduction
- https://motion.dev/docs/vue
- https://tanstack.com/query/latest/docs/framework/vue/installation
