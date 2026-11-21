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


## Source-parity restoration: v6.15 component mechanisms and v6.14 motion authorization

For new projects or major redesigns, respect confirmed motion intensity first; then distinguish indicator travel, spatial reveal, state morph, layout continuity, semantic feedback and media transitions according to the actual component (see component-motion-choreography-gate.md). Start common indicators, toggles and disclosures with CSS/native mechanisms. FLIP/shared-element motion may justify Motion; complex choreography may justify Anime.js or GSAP. **Not every interaction needs a library, and a CSS opacity alone does not establish a refined component.** Do not implement only page-level fades.

Motion-consent-experience-gate.md is the upstream authority: the user may choose (A) no added visual motion, (B) subtle interaction feedback/transitions, or (C) a few expressive effects. Without a confirmed/delegated direction for major changes, present **2–3 concrete choices**; do not quietly decide to add motion or to remove it. Choosing A still requires immediate and clear state feedback; B/C require inventories and verification on actual interactions. **Engine selection is not authority to approve motion on the user's behalf.**

### Original candidate catalog — retain technology categories and exclusions

| Technology | Core capability | Vue | React | Best fit | When not to use |
| --- | --- | --- | --- | --- | --- |
| CSS transitions/keyframes | Hover, focus, opacity/transform, micro-interactions | Native | Native | Buttons, overlays, small in-page transitions | Complex sequencing/fine-grained playback |
| Web Animations API | Element.animate(), pause, cancel, completion | Native | Native | A few controlled imperative effects | Would require building a large custom coordinator |
| Vue Transition/TransitionGroup | Component enter/leave, list movement | Native | — | Vue state-driven changes | Non-Vue apps |
| Svelte transitions | Built-in enter/leave/list transitions | — | — | Svelte sites | Non-Svelte apps |
| Motion | React motion/react, Vue motion-v, Vanilla motion; layouts, springs, gestures, scroll | Official Vue version | Official React version | Component/layout state transitions | Only hover opacity is needed |
| Anime.js v4 | Property/timeline/stagger/SVG/scroll/draggable/easing/utilities | DOM integration | DOM integration | Controlled multi-step DOM/SVG choreography | Declarative framework transitions suffice |
| GSAP | Tweens, Timelines, ScrollTrigger, plugins | DOM integration | DOM integration | Complex timelines and scroll storytelling | Generic admin buttons |
| AutoAnimate | Child insertion/removal/rearrangement | Verify compatible version | Verify compatible version | Natural list reordering | Precise complex choreography |
| Lottie | Playback of authored vector assets | Web runtime | Web runtime | Success/brand illustrations | Basic inputs and data tables |
| Rive | State machine, interactive vector animation | Web runtime | React runtime | Character, progress and brand interaction | States/low-end devices cannot be tested |
| View Transitions API | Browser continuity across views/pages | Browser API | Browser API | Suitable SPA/MPA transitions | Support unverified or transition causes flicker |
| Canvas / WebGL / Three.js | Advanced graphics, particles, 3D | WebGL canvas | WebGL canvas | 3D/visualization/creative scenes | Ordinary DOM forms |

### Original recommended priority order

1. **Common controls** — CSS plus framework transitions, with shared motion tokens; creative experiences should still have subject-specific motion instead of the same generic transitions everywhere.
2. **Declarative layout or gestures** — Motion for Vue/React as appropriate; prefer one principal solution.
3. **Keyframes, SVG and stagger** — Anime.js v4.
4. **Scroll narratives and complex multiple timelines** — GSAP, with performance and license checks.
5. **Complex product illustration** — Lottie/Rive, with explicit asset/runtime ownership.
6. **Experimental content** — Canvas/WebGL, with graceful fallback and frame-rate control.

## Source-parity restoration: three motion quality tiers

- **A / everyday usability:** hover color/shadow, button press, popover/dialog enter/exit, brief state icon, inserted/reordered list rows.
- **B / requires appropriate context:** layout swap, drag snapping, chart transitions, scroll reveal, grouped stagger, partial text reveal.
- **C / brand or creative specialty:** 3D tilt, particles, morph, scrambleText, strong spring elasticity and full-screen transitions.
- **Reject:** effects blocking important actions, forced repeated playback, hidden essential content, fake numeric calculation/success motion, and lack of reduced-motion or performance fallback.

## Source-parity restoration: suggested timing (design defaults, not official standards)

| Effect | Reference duration | Magnitude | Suggested easing |
| --- | --- | --- | --- |
| Hover / Press | 100–180 ms | scale 0.98–1.00 / subtle color | ease-out |
| Tooltip / Dialog | 160–240 ms | 8–16 px + opacity | outCubic / inOutSine |
| List entrance | 180–300 ms | 8–16 px + opacity | outCubic, limited stagger |
| Page / major section | 200–350 ms | 12–24 px | outCubic / outQuint |
| Brand Hero | 300–650 ms if appropriate | Control quantity and occlusion | inOutSine / custom |

**Creative effects are not limited to Fade/Slide/Zoom.** Expressive Motion Vocabulary contains 22 curated terms. assets/motion-effects.json contains **123 recipes** (the earlier 114 plus 9 additional mechanisms), some relying primarily on browser/CSS capabilities and **not** constituting built-in Anime.js APIs. animejs-motion-recipes.md documents 114 prior combinations; animejs-easing-complete.md documents 45 easing terms. Never use a recipe name as though it were an official API method.

Official references retained from the source:
- https://animejs.com/documentation/
- https://motion.dev/docs
- https://gsap.com/docs/v3/
- https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API
- https://auto-animate.formkit.com/
- https://rive.app/docs/
- https://developers.lottiefiles.com/

## v5 — Visual component collections are not a single low-level engine

React Bits, Vue Bits, Inspira UI, Magic UI and Aceternity UI are **optional component/effect source collections**, not competing universal animation engines. Their components may internally rely on GSAP, Motion, OGL/WebGL and other tools. Inspect the actual component dependencies before adding Anime.js/GSAP/Motion; prevent different engines from simultaneously controlling the same DOM property. See creative-component-libraries.md.

## v6.2 — Specialized technologies beyond general-purpose animation engines

The preceding candidate catalog answers which **animation engine** to select. PixiJS, Three.js, Curtains.js, ECharts, Rough.js, Vivus, SVG Filter, tsParticles and Matter.js do not all compete in one category. For specialized graphics, refer to visual-tech-selection-12.md and assets/visual-tech-catalog.json. GSAP SplitText and Anime.js splitText are distinct APIs; **native SVG Filter is not an additional dependency**. If ordinary micro-interactions can use CSS/framework-native mechanisms, none of these specialist libraries is required.

## Related resources and sources

- `references/motion-craft-and-continuity.md`
- `references/component-motion-choreography-gate.md`
- `references/animation-integration-lifecycle.md`
- `references/animejs-official-capabilities.md`
- `references/animejs-easing-complete.md`
- `references/animejs-motion-recipes.md`
- `references/motion-rehearsal-and-evidence.md`
- Official: https://animejs.com/documentation/ , https://motion.dev/docs , https://gsap.com/docs/v3/ , https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API
