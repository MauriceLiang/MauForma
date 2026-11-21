> v4 scope note: MauForma directly targets Web frontends. A few legacy SwiftUI/AppKit references are for transferring design semantics only; they do not authorize installing or generating native UI code.

# Anime.js v4 Official Capability Catalog (reviewed 2026-11-02)

**Scope:** The following are official top-level capabilities, primary API entrypoints and their intended uses, **not names of preset CSS animation effects**. Official animations are compositions of properties and timing. There is no finite total number of all possible combinations. Distinguish official APIs from MauForma visual recipes in assets/motion-effects.json.

The stable version referenced here is **Anime.js 4.5.0**. Do **not** use the v3 anime({targets:...}) syntax as if it were v4. For Web/Vue/React projects, npm install animejs@4.5.0 and import only what is needed, subject to project authorization. For non-Web contexts (such as SwiftUI), transfer only the motion intention, **not** embedded JavaScript.

| Official category | Main API | Purpose / possible outcome | Official documentation |
| --- | --- | --- | --- |
| Timer | createTimer | Precise timing, counters and update callbacks | https://animejs.com/documentation/timer |
| Animation | animate | Interpolate CSS properties/transforms, variables, DOM/SVG attributes and JavaScript object properties | https://animejs.com/documentation/animation |
| Timeline | createTimeline | Sequential and parallel choreography, label positions, synchronization and callbacks | https://animejs.com/documentation/timeline |
| Animatable | createAnimatable | Pointer following, continuous input and rapid target-value updates | https://animejs.com/documentation/animatable |
| Draggable | createDraggable | Pointer dragging, axis locks, snapping, velocity and rebound | https://animejs.com/documentation/draggable |
| Layout | createLayout | List/grid switching and rearrangement, changes in container geometry | https://animejs.com/documentation/layout |
| Scope | createScope | Component-local scope, reactive media conditions and lifecycle cleanup | https://animejs.com/documentation/scope |
| Events / scroll | onScroll | Scroll triggers, thresholds and scroll-linked synchronization | https://animejs.com/documentation/events/onscroll |
| SVG / morph | morphTo | Shape transition between two paths | https://animejs.com/documentation/svg/morphto |
| SVG / drawing | createDrawable | Incremental drawing/erasing of SVG strokes | https://animejs.com/documentation/svg/createdrawable |
| SVG / motion path | createMotionPath | Movement along a path and rotation following its direction | https://animejs.com/documentation/svg/createmotionpath |
| Text / splitting | splitText | Split lines/words/characters for staggered animation | https://animejs.com/documentation/text/splittext |
| Text / scrambling | scrambleText | Random character substitution resolving into a text reveal | https://animejs.com/documentation/text/scrambletext |
| Utilities / stagger | stagger | Sequential entrances, wave distributions and grid staggering | https://animejs.com/documentation/utilities/stagger |
| Utilities / others | utils | Get/set, randomization, mathematical interpolation, clamping and cleanup | https://animejs.com/documentation/utilities |
| Easings | eases, cubicBezier, linear, steps, irregular, spring | Nonlinear timing curves and spring physics | https://animejs.com/documentation/easings |
| WAAPI | waapi.animate | Lightweight browser-animation path for basic visual transforms; **capabilities differ from the JavaScript implementation** | https://animejs.com/documentation/web-animation-api |
| Engine | engine | Global time precision, speed and animation-engine configuration | https://animejs.com/documentation/engine |
| Adapters | registerAdapter | Animate external object models such as Three.js; an official Three.js adapter exists | https://animejs.com/documentation/adapters |

## Property dimensions (Animation documentation)

- **CSS properties:** Opacity, colors, dimensions, spacing, background, shadows and other interpolable properties. Favor opacity/transform and avoid broad layout repainting.
- **Transforms:** x/y/translateX/translateY, scale/scaleX/scaleY, rotate/rotateX/rotateY and skew, as supported by the installed Anime.js version and browser.
- **CSS custom properties:** Interpolable variables such as --value for visual theme or chart parameters. Verify value-type compatibility.
- **HTML/SVG attributes:** For example SVG d and stroke-dasharray; SVG utility APIs may be more appropriate.
- **JavaScript objects:** Interpolate real values in objects such as { value: 0 }; useful for displayed numbers or Canvas data sources. **Never invent business data.**

## Timing and choreography dimensions

- from/to; delay/duration/ease; composition/modifier; keyframes; loop/alternate/loopDelay/autoplay/playbackRate/reverse; onBegin/onUpdate/onComplete and similar callbacks **only where supported by the specific API**.
- **createTimeline:** .add(), .sync(), .call(), .label(), relative positioning, labels, parallel/sequential arrangements; use for meaningful state-continuity feedback.
- **stagger:** Offset **timing, values and Timeline positions**, including from/grid/axis/ease distribution options.
- **onScroll:** Scroll triggers, entry/exit thresholds, progress synchronization; **never hijack normal scrolling**.
- **createDraggable:** Grid snapping, inertia on release, bounds and axis constraints; release spring configuration must match actual drag state.
- **createLayout:** Capture the previous/next layout and animate between them; useful for reordered lists/grids, DOM order and CSS Grid changes.
- **splitText:** Line/word/character splitting. **scrambleText:** Reveal via temporary character replacement. Verify accessible names, long content and dynamic text.
- **SVG:** morphTo, createDrawable and createMotionPath mean **morphing**, **line drawing** and **path motion** respectively; do not present them as the same effect.

## Capabilities Are Not the Same as Visual Effect Types

Timer, Scope, Engine, Utils and Adapters are mainly implementation infrastructure. Do not invent visual-effect names or results for them. This document summarizes the official documentation as checked; it does **not** claim to cover APIs introduced by future Anime.js versions. Recheck the actual installed major version after upgrades.

Official references:
- https://animejs.com/documentation
- https://animejs.com/documentation/animation
- https://animejs.com/documentation/easings/built-in-eases
- https://animejs.com/documentation/layout
- https://animejs.com/documentation/adapters
