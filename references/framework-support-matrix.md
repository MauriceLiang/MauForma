# Supported Frontend Framework Matrix

**Rule:** These are **candidate choices**, not required installations. First inspect the target project's `package.json` and lockfile; retain its working solution when feasible. Compatibility in this matrix **does not** imply identical source, props or lifecycle APIs across frameworks.

| Framework | Primary component candidates | Icons | Motion | Client state | Server state | Charts / complex data |
| --- | --- | --- | --- | --- | --- | --- |
| Vue 3 / Nuxt | Reka UI, shadcn-vue, Element Plus, Naive UI, following existing choice | `@lucide/vue` / inherited `lucide-vue-next` | Vue `<Transition>`, Motion for Vue (`motion-v`), Anime.js, GSAP | Pinia / composables | `@tanstack/vue-query` or Nuxt data tools | Apache ECharts with Vue adapter / `@tanstack/vue-table` |
| React / Next.js | shadcn/ui + Base UI or Radix; also Mantine, MUI or AntD | `lucide-react` | Motion for React (`motion/react`), Anime.js, GSAP | Zustand / Context | `@tanstack/react-query` or framework data API | Recharts / ECharts / `@tanstack/react-table` |
| Svelte / SvelteKit | Bits UI, shadcn-svelte | `@lucide/svelte` | Svelte transitions, Anime.js, GSAP, Motion JS | Svelte stores/runes | SvelteKit load / Query adapters | ECharts / Table adapters; verify actual versions |
| Angular | Angular CDK/Material, PrimeNG | `@lucide/angular` | Framework motion / CSS / Anime.js / GSAP | Signals / RxJS | HttpClient / TanStack Query when useful | ECharts / AG Grid |
| Solid | Kobalte / Ark UI | `lucide-solid` / `@lucide/solid`, version-dependent | CSS, Motion JS, Anime.js | Signals / Stores | TanStack Query Solid | ECharts / TanStack Table Solid |
| Astro | Native Astro components + React/Vue/Svelte/Solid Islands | SVG / Lucide for the specific Island framework | CSS, Web Animations, Anime.js | Avoid global client state if unnecessary | Astro data fetching / per-Island tools | ECharts with client hydration when needed |
| HTML/CSS/JS | Semantic native controls, Web Components, limited headless primitives | `lucide` / SVG | CSS, Web Animations, Anime.js | Native module state | Fetch + local caching | ECharts / Canvas/SVG |

> **Implementation priority:** When actual Select, Dropdown, Button, Checkbox and other basic interactive controls are required, start from the **library already used by the current framework/project**. If none is available, proactively select **and actually use** a suitable styled library or accessible mature headless primitives. The matrix is **not permission to handwrite every complex control**. See `references/component-library-first-gate.md`.

## Decision conditions

1. **Existing products: continue with installed frameworks and libraries first.** Do not switch Vue→React or React→Vue without an explicit need.
2. **Complex accessible controls:** For Select, Dialog, Combobox and Menu, prefer mature framework-compatible primitives or suites with verified keyboard/focus behavior.
3. **High visual customization:** Use maintainable project-owned component layers such as shadcn/ui/shadcn-vue or unstyled primitives with the project's own skin.
4. **Large data-dense products:** Mature enterprise component suites, virtualized tables and chart engines can be appropriate; do not blindly favor creative effect packages.
5. **SSR/SEO:** Check Next/Nuxt/SvelteKit/Astro server boundaries and hydration; never access `window`/`document` directly at module top level.
6. **Lightweight marketing sites:** HTML/CSS or Astro plus a few Islands may suffice. Do not force heavy React/Vue state libraries.
7. **Cross-framework reuse:** Design tokens, visual semantics and interaction contracts can transfer; exact source, lifecycle, props and emits must be implemented for the active framework.

> According to the referenced 2026-era Lucide guidance, `@lucide/vue` exists while older projects may use `lucide-vue-next`. Verify the **actual installed version** before migration; do not mix the two packages. Newer dnd-kit versions have adapters including Vue, so an old React-only article cannot prove Vue support is impossible.

Official sources:
- https://lucide.dev/packages
- https://lucide.dev/guide/version-1
- https://github.com/clauderic/dnd-kit
- https://motion.dev/docs
- https://tanstack.com/query/latest/docs/framework/vue/installation
- https://shadcn-vue.com/docs/introduction
- https://ui.shadcn.com/docs

## v5 — Additional creative and enterprise component layers

| Context | React / Next | Vue / Nuxt | Selection rule |
| --- | --- | --- | --- |
| Creative brand site: animated titles, backgrounds, 3D showcases | React Bits, Magic UI, Aceternity UI | Vue Bits (official Vue adaptation of React Bits), Inspira UI | Select only needed compatible pieces; check dependencies/license/SSR. **Not a substitute for foundational UI controls** |
| Enterprise admin with complex tables and forms | Ant Design, MUI, Mantine, PrimeReact; retain existing shadcn/ui when sound | Ant Design Vue, Element Plus, Naive UI, Arco Vue, PrimeVue; retain Reka/shadcn-vue when sound | **One primary styled library**, with additional review of specialist controls |
| Shared visual foundations | CSS/Tailwind design tokens + Ui adapters | CSS/Tailwind design tokens + Ui adapters | Share visual language, not foreign framework code |

See `references/creative-component-libraries.md`, `references/enterprise-ui-library-guide.md` and `examples/creative-library-recipes-react-vue.md`.
