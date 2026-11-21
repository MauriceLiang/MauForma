# Vue 3 / Nuxt — Component Ownership and Reactivity Boundaries

These rules take the *principles* of vuejs-ai Vue Best Practices, but actual implementation must respect the project's Vue/Nuxt versions and inherited Options API constraints.

## Default architecture

- For new Vue 3 components, generally use SFCs with `<script setup lang="ts">`. For substantial existing Options API applications, follow an explicit migration plan instead of requiring a partial unapproved rewrite.
- Props flow down; Emits communicate events upward. Put reusable behavior in composables, not every state in one global Pinia store.
- Keep a **single source of truth** with `ref/computed`. Avoid watchers that write back into each other and reactive loops; do not separately store state that can be derived.
- Shared foundational `UiButton/UiField/UiDialog` components own visuals and primitive behavior. Feature pages own list loading, permissions and business queries.
- Public component APIs declare Props, Emits, Slots, loading/error states and have verifiable examples. Copying CSS across routes is not component reuse.
- Optimize data-heavy components from **measured bottlenecks**; use virtualized Vue lists, async components and caches only with evidence.

## Engineering boundaries

Nuxt SSR must not access `document/window` at module top level. Start imperative animation after mount and clean it up on unmount. Prefer Vue Transition for simple visibility, with complex animation engines selected under `references/animation-engine-selection.md`.

Inherit existing primary libraries such as Element Plus, Ant Design Vue or Reka rather than forcing migration. Use framework-appropriate tests to verify control states and keyboard, focus and touch interactions.

## Quality bar

- Every Prop/Emit type and default has a clear purpose.
- No watcher loops or unnecessary global event buses.
- Empty/error/loading/disabled states are demonstrated and tested.
- Composition honors the project's Master design decisions and current page overrides; individual Vue pages must not each invent a new main color.

Source: https://github.com/vuejs-ai/skills/tree/main/skills/vue-best-practices
