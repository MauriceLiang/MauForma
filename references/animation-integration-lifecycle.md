# Animation Engines and Component Lifecycle — All Web Frameworks

## v6.14 — Motion intensity and animation lifecycle must pass together

First inspect approved/inherited/delegated motion choices under `references/motion-consent-experience-gate.md`. Every new animation must have observable state purpose and a legal exit, reversal and cancellation path. Test rapid Tab/route changes, repeated Dialog open/close, preference changes while animation is running, system reduced-motion settings and lower-performance scenarios. A `prefers-reduced-motion` CSS rule does **not** prove JavaScript animations cancel correctly.

## Technical safety invariants

- **DOM ownership:** Vue/React/Svelte/Angular control rendering. Imperative animation engines should target scoped refs or elements only after mount, not query all global `.card` instances across unrelated components.
- **Cleanup:** Stop and release timelines, listeners, observers, ScrollTrigger and Rive/Lottie instances on unmount, route changes, dialog close or dependency changes.
- **SSR:** Never access `window` or `document` during server execution. Start animation in client hooks; SSR/first-frame HTML must remain visible without JavaScript motion.
- **Property conflicts:** Do not have Tailwind transitions, Motion and Anime.js all control the same element's `transform/opacity`. For deliberate combinations, specify property ownership and nested animation layers.
- **Performance:** Prefer `transform/opacity`; handle frequent changes to `width/height/top/left`, SVG paths, blur and large box shadows cautiously. Avoid excessive forced synchronous layout measurements.
- **Accessibility:** Respect `prefers-reduced-motion`, allow loops to pause, and never obstruct keyboard focus. Required business state updates should occur semantically, not depend on an animation `onComplete`.
- **Tests:** Rapid open/close, unmount while scrolling, route changes, remount, long lists, low-end devices, missing animation dependencies and reduced-motion preferences.

## Vue 3

- Prefer native `<Transition>` and `<TransitionGroup>` first.
- Construct imperative animations inside `onMounted`, scoped to `ref<HTMLElement | null>`.
- Cancel/restore in `onUnmounted` or `onScopeDispose`; stop the old animation when dependencies change.
- In Nuxt, run after client mount or use the official `<ClientOnly>` approach for advanced DOM engines.

## React / Next.js

- Place imperative DOM motion in `useEffect` or, only when justified, `useLayoutEffect`, returning a cleanup function. Never manipulate DOM during render.
- React StrictMode in development may simulate mount/cleanup to expose effects; cleanup must be idempotent.
- Next App Router interactive components belong behind the client boundary; never execute DOM animation at Server Component module top level.
- Declarative Motion components should follow their own presence/layout protocols rather than exposing animation instances as global variables.

## Astro and content-first pages

- Load interactive islands only where needed; do not turn the whole site into a client-rendered app for decoration.
- Prefer CSS/WAAPI. Use IntersectionObserver for complex animation that should run only while visible.

## Acceptance examples

- Closing a dialog does not later trigger a Toast or mutate an unmounted component.
- With reduced-motion enabled, dialogs remain immediately interactive and primary text is visible at once.
- Ten rapid open/close actions do not accumulate ten event listeners.
- List filtering never makes a data-reorder animation look like a change in underlying real values.

## v6.2 — Canvas/WebGL, charts and physics

- **PixiJS / Three.js / Curtains.js:** Release renderers, scene resources, materials, textures, listeners and `requestAnimationFrame` on unmount. Keep semantically meaningful static DOM and replacement imagery. Define pixel-ratio caps and low-performance fallbacks.
- **ECharts:** Separate container resize handling from data flow; call `dispose` on unmount. Charts alone may not provide an accessible data summary/table for screen readers.
- **tsParticles:** Start on demand when visible, pause in the background or with reduced motion, and dispose instances/listeners.
- **Matter.js:** Keep physics world, runner and rendering separate; clear runner, world, mouse constraints and events.
- **SplitText:** Handle font loading, line reflow and re-splitting on narrow screens. Reverse wrappers and animations when cleaning up while preserving screen-reader semantics.
- **SVG Filter:** Browser-native does not mean zero GPU cost; measure large continuous blurs and displacement effects.

Minimum checks: first launch, ten consecutive mount/unmount cycles, viewport-width changes, reduced motion, WebGL failure, missing assets, empty chart and background tab. See `references/visual-tech-selection-12.md` for further technology selection.
