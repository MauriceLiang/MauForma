# Motion Governance — Every Effect Needs a Purpose and Boundaries

## Selection workflow

1. What did the user do, and what state changed? Which **causality, direction, hierarchy, feedback or progress** should motion communicate?
2. Does native platform behavior or a CSS transition already suffice? If yes, do not introduce Anime.js.
3. Choose candidate effects by A/B/C tier in [animejs-motion-recipes.md](animejs-motion-recipes.md): prefer A, use B for a matching real situation and C only where expressive benefit is justified.
4. Record a **motion contract**: trigger, target, start/end, duration, curve, repetition conditions, interruption/cancellation, reduced motion, fallback, truthful data and keyboard behavior.
5. Put motion in shared components or standalone hooks/composables. Avoid divergent one-off interaction animations across pages.

## Suggested durations — heuristics, not official Anime.js constants

| Context | Typical duration | Suggested easing | Risk |
| --- | ---: | --- | --- |
| Button / switch / tag / focus | 100–180ms | `outQuad` / `outCubic` | Shorten when feedback feels delayed |
| Menu / Popover / Tooltip | 120–200ms | `outCubic` | Blocking the workflow |
| Toast / success feedback | 150–240ms | `outCubic` | Accessibility copy must remain readable |
| Dialog / Drawer / navigation panel | 180–280ms | `outCubic` / `inOutCubic` | Hidden focus/interactions |
| Small layout reflow | 180–320ms | `inOutCubic` | Reflow costs on frequent multi-element changes |
| Showcase card entrance | 300–600ms | `outCubic` / limited `outBack` | First screen unavailable / long waits |
| Brand display / SVG / long-form narrative | 500–1200ms | Content-driven | Requires skip/reduced-motion support |

## Performance and accessibility conditions

- For frequent changes prefer `opacity` and `transform`. Avoid animating large areas of `width/height/top/left/box-shadow/filter` every frame without measurements; layout/paint cost may be high.
- Under `prefers-reduced-motion: reduce`, cancel nonessential movement, scaling and flashing; use immediate state updates or a very short fade.
- For rapid triggers, decide whether to cancel the previous animation, replace its target, merge values or queue. **Never accumulate animations unboundedly by default.**
- Looping effects only for genuinely continuing states such as waiting or recording. Stop the loop and release resources as soon as the state ends.
- Important content must be visible by default: **no global `.card {opacity:0}` that bets on CDN success**. Animate from a safely initialized state and restore visibility if initialization fails.
- **Truthful numbers first:** Amounts, permissions, temperatures and other sensitive values must not pass through arbitrary character scrambling that creates misleading readings.
- Handle blur/focus loss, disabled states, Escape, touch, route changes and component unmount. Dragging needs keyboard or equivalent accessible interaction.

## Positive and negative decisions

| Scenario | Effective | Defective | Decision test |
| --- | --- | --- | --- |
| Table filtering | Result appears with ~150ms opacity or no animation | 200 rows flying in sequentially | Does motion clarify the change? |
| Save success | Button state changes plus one Toast | Modal shaking and particle explosion | Is confirmation clear and immediate? |
| Page loading | Skeleton/progress alongside a real request, then content | Hide all content until promotional animation ends | Is content reachable? |
| Error | Text explaining cause, focus, one subtle shake if appropriate | Endless rapid red flashing | Can users resolve the error? |
| Brand first screen | Brief thoughtful stagger plus reduced-motion mode | Letter-by-letter copy that cannot be skipped | Does it respect reading preferences? |
| List/grid | Motion expresses actual spatial changes | Meaningless spins and bounces | Is object continuity maintained? |
| Drag | Clear snap/bounds/undo | Mouse-only interaction that loses data on drop | Is it controllable and trustworthy? |

## Official APIs and catalog relationship

- [animejs-official-capabilities.md](animejs-official-capabilities.md)
- [animejs-easing-complete.md](animejs-easing-complete.md) — 45 built-in easing names.
- [animejs-motion-recipes.md](animejs-motion-recipes.md) — 114 original composite recipes.
- [animejs-v4-snippets.md](../examples/animejs-v4-snippets.md) — runnable usage examples.
- Interactive gallery: `assets/motion-gallery.html`.
