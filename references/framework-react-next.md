# React / Next.js — Detailed Implementation Guide

## 1. React and Next.js responsibilities

React is the UI component/state model built with TSX and hooks; Next.js is a React Web framework providing routing, server rendering and data-loading capabilities. Implement within the **existing routing strategy** (Next App Router, React Router or Vite). Do not force every React application into Next.js.

## 2. Components and UI primitives

| Option | Purpose | Fits | Boundary |
| --- | --- | --- | --- |
| shadcn/ui | CLI copies maintainable component source into the project, with theme/composition/variants | React with a custom design language | Not an opaque external component package; inspect the selected primitive base |
| Base UI | Unstyled interaction, ARIA and behavior primitives | Highly customizable new UI | Its `render` API does not directly translate to Radix `asChild` |
| Radix UI | Unstyled interaction primitives | Existing Radix and custom-control projects | Preserve existing implementation; don't migrate just because defaults changed |
| React Aria | Accessibility and internationalization behavior | Forms, selection and multilingual products | Integrate into the project's main component system |
| MUI / Mantine / AntD / Chakra | Broader React UI suites | Enterprise products wanting mature controls | Avoid multiple competing visual systems in one application |
| Magic UI / Aceternity UI | Expressive visual and animation components | Brand sites, portfolios and targeted moments | Not a replacement for shared Dialog/Field/DataTable responsibility |

The cited 2026-07 official shadcn/ui default for new projects is Base UI, while Radix remains supported. **Existing Radix projects need not migrate.** Base UI and Radix composition APIs are not identical. Verify actual installed primitives and the applicable official docs.

## 3. Example codebase layers

```text
src/
  styles/tokens.css                 # Global semantic tokens
  components/ui/                   # Button/Field/Dialog/Toast etc
  components/composites/           # SearchField/PageHeader/DataTable
  components/patterns/             # Reusable page compositions
  features/users/                  # Domain features, hooks, API and types
  lib/                              # API client and utilities
  stores/                           # Zustand if used
  hooks/                            # Shared behavior hooks
  app/ or routes/                  # Next / React Router routes
  tests/
```

## 4. State ownership

- Local state: `useState` / `useReducer`; a simple button switch does not belong in a global store.
- Shared client state: Zustand/Context when actually installed or appropriate; e.g. global panel selection, UI drafts or preferences.
- Server state: `@tanstack/react-query` for request cache, retry and invalidation, or Next's own data strategy; distinct responsibility from Zustand.
- Resizable panels: `react-resizable-panels`. Sorting/dragging: dnd-kit React adapter, subject to installed APIs. Check StrictMode, unmount and SSR.
- Charts: Recharts for React data charts, ECharts for complex visuals as needed; explain units, legends and fallback accessible data tables.

## 5. Motion mapping

- Basic feedback: CSS transitions / Web Animations API.
- React state-based presence, layout and gesture motion: Motion (`motion/react`), including `AnimatePresence` under the active official version.
- SVG/complex timelines: Anime.js v4 or GSAP, scoped to React refs inside `useEffect` with cleanup on unmount and dependency changes.
- React 18/19 and Next SSR: Do not access `document/window` during render or server entry. Put interactive animation in Client Components and effects; dynamic load when needed to reduce first-screen JavaScript.

## 6. Component-first acceptance

- Shared components provide primary/secondary/ghost/danger variants with disabled, aria-busy, loading and keyboard states.
- Build observable PageHeader, Field, Dialog and state gallery before multiplying business screens.
- Pages compose those components; see `examples/react-web-components.md`.

## 7. React / Next performance and composition gate — only when relevant

These checks apply to the actual React/Next project; **never automatically apply them to Vue**, and each must follow observed issues or the impact of this change:

- **Request dependencies before micro-optimizations:** Use Network and server logs to identify request waterfalls. Parallelize independent fetches only; never break real business dependencies or cache consistency just to increase concurrency.
- **Bundle and first screen:** Inspect lockfile, production chunk sizes and incremental client JS from new libraries. Dynamically import only appropriate low-frequency expensive components; critical first-screen actions must remain responsive.
- **State and renders:** Separate server data, client drafts and local animation state. Do not memoize every primitive. Optimize demonstrably redundant rendering, costly calculations and event-listener leaks.
- **Server security:** Follow the active React/Next versions for SSR, RSC, Server Actions and hydration. **Authn/authz must be enforced on the real server**, not merely by hiding Buttons.
- **Explicit component variants:** When boolean props allow impossible combinations, use clear variants, compound children and explicit state owners. React Context should not become a dumping ground for the entire enterprise state. **React 19-only APIs/patterns are allowed only after confirming the project actually uses React 19**; React 18, ordinary SPAs and Vue cannot blindly copy them.
- **Motion quality:** Measure real long tasks, CLS, input latency and interruption; cancel imperative animation properly. CSS mentioning `transform` cannot prove 60fps.

Run `scripts/mauforma_check.py` for static candidates on changed files; then reproduce interactions, async errors, focus and smallest supported viewport on **actual pages**. Follow installed versions and official APIs.

Official:
- https://react.dev/learn
- https://nextjs.org/docs
- https://ui.shadcn.com/docs
- https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default
- https://motion.dev/docs/react
- https://tanstack.com/query/latest/docs/framework/react/overview
