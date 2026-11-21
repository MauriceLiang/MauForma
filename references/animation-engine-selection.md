# Animation Engine Selection — Choose by Actual Project Needs

Do not assume “a good-looking Web page must use Anime.js.” Choose an engine from real motion requirements, the current framework, installed dependencies, bundle/performance constraints, reduced-motion accessibility, SSR and lifecycle cleanup. Prefer browser-native CSS/WAAPI for simple effects, and reuse existing engines when they already suffice. This file is a selection guide, not an installation command.

## Decision matrix

| Need | Prefer first | Escalate when needed | Risks and boundary |
| --- | --- | --- | --- |
| Hover/focus/pressed, brief show/hide | CSS transition/animation, framework Transition, WAAPI | None for ordinary controls | Keep focus immediate; no global `transition:all` |
| React state-driven layout, presence, gestures | Existing Motion for React (`motion/react`) | Anime.js/GSAP for independently justified imperative sequences | Follow React keys, cleanup, SSR/StrictMode, installed versions |
| Vue component show/hide and layout | Vue `<Transition>`/`<TransitionGroup>` | Motion for Vue (`motion-v`), Anime.js/GSAP | Don't copy React Motion APIs into Vue |
| Svelte local transitions | Svelte transitions/animate, CSS | Compatible imperative timeline | Respect Svelte lifecycle and version |
| SVG paths, advanced sequencing, text/objects | Anime.js v4 or installed GSAP | Specialist text/SVG/Canvas engine | Check API version, text accessibility, cleanup |
| Scroll storytelling or pin/scrub | Native sticky/scroll behavior where possible | GSAP ScrollTrigger or supported scroll engine | Browser support, reverse, scrolling freedom, reduced motion |
| Large 2D/3D scenes | Purpose-fit Canvas/WebGL/Three/Pixi | Shader/physics specialists | Rendering engine is not a basic UI animation library |
| Animation export/story illustration | Lottie/Rive when actual assets exist | Composable scene tools | Asset licensing, runtime cost, missing-asset fallback |
| Simple brand entrance | CSS or existing framework animation | Sequenced Anime.js if purposefully distinctive | Do not hide H1 until JS loads |

## Selection gate: seven steps

1. **State the actual effect and object.** Identify the trigger (click, hover, route, scroll, data), its semantic outcome and whether it requires continuous progress, sequencing, gestures or simply opacity.
2. **Read the inherited motion policy** from `references/motion-consent-experience-gate.md`. Explicit user `none`/reduced choices and OS `prefers-reduced-motion` outrank the Agent's preferred animation. A user's “make it more polished” does not automatically authorize all effects or library installation.
3. **Inventory versions** in `package.json`/lockfiles and existing component libraries. Avoid redundant imperative engines or two frameworks controlling the same transform.
4. **Try low-cost native solutions** when adequate. A 180ms Button fade does not justify a new animation dependency.
5. **Evaluate candidate capability and cost:** Exact import/API by installed version, tree shaking, SSR, browser/mobile support, focus/keyboard, partial/reverse state, lifecycle destruction, performance and license.
6. **Implement a representative high-value interaction** with a real state and a clear cancel/cleanup path. Measure actual before/during/after and reduced-motion behavior, not just final CSS declarations.
7. **Document choice and exceptions** in project Motion Tokens/decision record. If adding a second engine, explain distinct responsibilities; no default “install everything.”

## Anime.js v4 position

Anime.js v4 is an *optional* high-control animation library, not a mandatory default. Useful capabilities include `animate`, `createTimeline`, `stagger`, `createScope`, `createDraggable`, `createSpring`, SVG motion paths/morphing, easing and a scroll observer. Read official API documentation for the **installed major version**; do not use v3 `anime({...})` syntax as if it were v4. Named MauForma recipes in `assets/motion-effects.json` are concepts, not automatically official Anime.js method identifiers.

- Use local `createScope` or component refs where appropriate; on unmount/re-run, revert or cancel animations, observers and Draggable instances.
- `createTimeline` handles actual sequences; don't replace semantic UI state with a pure animation sequence.
- Match low-level properties with accessibility, text reflow and compositing cost. Do not animate long paragraphs with split letters without preserving accessible text and font/resize behavior.
- If CSS/native or existing Motion solves a control cleanly, **do not introduce Anime.js solely for decorative quality claims**.

## Motion / GSAP / framework boundaries

- Motion React/Vue have framework-specific APIs and lifecycle contracts. Confirm library package paths and versions; shared concepts do not make source APIs interchangeable.
- GSAP is useful for complex timelines and scroll choreography, but not necessary for every hover. ScrollTrigger must not break normal scrolling, back navigation or reduced motion. Check licenses for plugins/assets and actual project permissions.
- Vue/React/Svelte/Angular native transitions can be more reliable for simple component state. Their existing lifecycle often avoids extra imperative synchronization.
- On SSR, don't construct a DOM animation at module top level. Make first-frame content visible without animation support.
- Avoid simultaneous CSS `transform`, Motion layout and Anime.js transform on the **same node** without explicit ownership or nested layers.

## Performance and visual QA

Verify 100%/200% text, CJK/Latin, responsive supported viewports, long values, keyboard and touch. For meaningful motion capture before, interaction, during, settled, reverse/interruption and reduced-motion. A static smoke test or existence of `@keyframes` cannot establish actual frame quality or user experience.

Avoid broad `will-change`, permanent RAF loops and expensive blur/Canvas across entire pages. Never claim “60fps”, “zero CLS” or memory efficiency without measured evidence.

## Related resources and sources

- `references/motion-craft-and-continuity.md`
- `references/component-motion-choreography-gate.md`
- `references/animation-integration-lifecycle.md`
- `references/animejs-official-capabilities.md`
- `references/animejs-easing-complete.md`
- `references/animejs-motion-recipes.md`
- `references/motion-rehearsal-and-evidence.md`
- Official: https://animejs.com/documentation/ , https://motion.dev/docs , https://gsap.com/docs/v3/ , https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API
