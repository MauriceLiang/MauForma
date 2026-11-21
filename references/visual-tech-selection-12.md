# Twelve Animation and Visualization Technologies — Scenario-Driven Selection (MauForma)

**Source:** A user-provided guide to twelve front-end animation and visualization technologies, cross-checked with the repository's animation-engine-selection.md, animation-integration-lifecycle.md, framework-vue-nuxt.md, framework-react-next.md and stack-guide-11-items.md. The original is technology-selection material, **not a mandatory installation checklist**. The twelve technologies are **not competitors in one single category of animation framework**.

## Do not duplicate established guidance

MauForma already covers GSAP, Anime.js, Three.js, Apache ECharts and basic CSS/SVG. This guide adds distinct responsibilities and composition boundaries for **SplitText, PixiJS, Curtains.js, Rough.js, Vivus, SVG Filter, tsParticles and Matter.js**. Existing 114 Anime.js recipes, React/Vue components and chart standards remain valid.

## Responsibility matrix — all twelve technologies

| Technology | Primary responsibility | Best suited to | Avoid when |
| --- | --- | --- | --- |
| GSAP | Precise choreography of multiple objects, scroll-linked storytelling | Branded product introductions, scrollytelling, expressive first screens | A simple hover |
| anime.js | Local DOM/SVG transitions, stagger, short timelines | Local feedback, SVG illustration, lightweight brand interaction | Replacing an ordinary CSS hover |
| SplitText (GSAP / Anime.js respective implementations) | Split text into lines/words/characters with separate entrances | Brand headings, chapter headings, short text reveals | Animating long body paragraphs character by character |
| PixiJS | High-frequency rendering of many 2D sprites, textures and interactive objects | Interactive 2D posters, 2D games, interactive exhibition walls | Ordinary forms or Cards |
| Three.js | 3D models, lights/materials, camera and spatial interaction | 3D product gallery, rotating device model, immersive scenes | Purely 2D effects |
| Curtains.js | Map DOM-positioned images/videos to WebGL planes and shaders | Creative portfolios, video transitions, image hover ripples | Images with no shader requirement |
| Apache ECharts | Interactive statistical/business charts and dashboards | Enterprise/BI, operations, research data, live monitoring | Decorative animation alone |
| Rough.js | Hand-drawn Canvas/SVG strokes | Learning illustration, whiteboards, sketchy diagrams, playful brands | Every control in a precise enterprise data UI |
| Vivus | Progressively draw SVG stroke paths | Logo entrances, map paths, line-art illustration | Filled-only graphics without drawable strokes |
| SVG Filter | Native browser SVG filtering, **not an npm animation package** | Local ripples, distortion, glow/blur, image warps | Large, frequent full-surface filters |
| tsParticles | Configurable particles for backgrounds and event-driven celebrations | Festivals, task-completion celebrations, purposeful technology scenes | Always-on particles across every page |
| Matter.js | Calculate 2D rigid bodies, gravity, collisions and constraints; **not full Web rendering** | 2D toys, physics education, collision-driven posters | Ordinary list dragging or sorting |

**Important distinctions:**

- GSAP's **SplitText plugin** and Anime.js **splitText()** are different APIs. Choose the implementation matching the inherited engine. Handle responsive re-splitting, screen-reader semantics, font loading and DOM cleanup. Do not split a long article into character animations.
- **SVG Filter is a browser-native SVG feature, not an additional npm dependency.** Check whether a CSS filter already meets the need.
- **Matter.js calculates physics only.** PixiJS renders 2D images. Matter.js must not be described as automatically rendering Web UI elements.
- Three.js, Curtains.js and PixiJS each involve an independent graphics/rendering layer, but they serve **real 3D**, **DOM-positioned image/video shaders**, and **high-density 2D** respectively.
- ECharts is for business data visualization, not a general-purpose animation engine. Vue/React still own UI component state.

## Scenario combinations — conditional, never bundled installs

| Site / content | Baseline recommendation | Conditional enhancement | Do not |
| --- | --- | --- | --- |
| Ordinary enterprise site / SaaS | CSS + anime.js | GSAP | Let marketing effects consume backend work areas |
| Premium brand / scroll narratives | GSAP + corresponding GSAP/Anime.js SplitText | Curtains.js | Split each body paragraph or add WebGL automatically |
| 3D product presentation | Three.js + GSAP | None | Fail without static imagery when the model is unavailable or the device is weak |
| Data wall / admin console | Apache ECharts + CSS | None | Re-create routine line charts in PixiJS |
| Creative 2D poster / mini-game | PixiJS | Matter.js | Call Matter.js a rendering engine |
| Hand-drawn education | Rough.js + SVG | GSAP | Repaint every high-precision enterprise control as a sketch |
| Celebration / particle background | tsParticles + CSS | None | Keep particles running under reduced-motion or consuming performance indefinitely |
| Logo paths / line drawing | Vivus | GSAP | Treat fill-only SVG as drawable stroke paths |
| Liquid/rippled images | SVG Filter | Curtains.js | Use continuous large GPU filters without measurement and static fallback |

**Prove the need before choosing:** When a user merely wants product presentation, image motion or charts, first inspect real content, main visual focus, first-screen objective, installed dependencies, available media and target devices. Prefer CSS/SVG/framework transitions by default; add GSAP/Anime.js only if insufficient; introduce heavier Canvas/WebGL/physics engines only when a specific effect truly needs them. A **conditional enhancement is NOT an invitation to install it together with the baseline**.

## Eight engineering acceptance gates from the source guide

1. **Dependency corresponds to a real effect:** Identify what is missing and why CSS/SVG/existing tools cannot satisfy it.
2. **Animation property ownership:** GSAP, Anime.js, Motion and CSS must not concurrently control the same DOM property. For multiple engines, separate component/property ownership.
3. **Accessibility/reduced motion:** Respect prefers-reduced-motion; preserve screen-reader meaning of split text; ensure content remains visible if animation fails.
4. **Lifecycle cleanup:** Vue mounted/unmounted and React effect cleanup; dispose WebGL textures/renderers, listeners, observers, timers and physics runners.
5. **Demand-driven activation:** Lazily load below-the-fold 3D, particles or charts. Pause unnecessary ongoing rendering when invisible or backgrounded.
6. **GPU/CPU budgets:** Limit pixel ratio, model polygon count, textures, sprites/particles and collision constraints. Supply static/reduced-effect modes for mobile.
7. **Measure, do not infer:** FPS, main-thread blocking, page memory, device load, layout instability and slow-network loading all need actual observation.
8. **Version/license:** Before installing, check lockfiles, current official API, browser support and plugin licensing. A demo does not prove a technology operates in the user's specific product.

## Framework integration and graceful degradation

- **Vue / Nuxt:** Simple enter/leave transitions favor Vue Transition. Create imperative graphics/animations only after onMounted; destroy onUnmounted/onScopeDispose. Guard SSR with ClientOnly or an equivalent client boundary.
- **React / Next.js:** Simple state transitions favor CSS or Motion. Manage instances in useEffect with reentrant cleanup. SSR/RSC must not reference window/document on the server.
- **HTML/CSS/Svelte/Angular etc.:** Follow the applicable mount/destroy contract; do not rewrite an entire product just to introduce Canvas effects.
- **Failure fallback:** Three.js → readable product photography; Curtains.js → original image; particles → static background; ECharts → accessible table or data summary. Essential buttons and body content must remain accessible, interactive DOM elements.

## Selection search

Use: python3 scripts/search_visual_tech.py --goal "3D product presentation with scroll-driven camera" --json

The search script suggests candidate technologies and their applicability. It does **not** install dependencies or prove performance. Catalog data: assets/visual-tech-catalog.json. For animation-engine order, see references/animation-engine-selection.md.

## Optional optical material: four-layer Liquid Glass approximation

Only when the user explicitly requests a lens-like Web glass treatment, consult references/liquid-glass-optics.md. Its layers are **transmission**, **background refraction**, **directional specular/Fresnel-like highlights** and **elevation**, with optional blur. This does **not** introduce a thirteenth standalone JavaScript animation library; existing CSS/SVG/WebGL tools can implement the effect.

- **Ordinary frosted glass:** backdrop-filter: blur(...) is **not refraction**. CSS transmission, gradients and shadows can provide a coherent static fallback.
- **Experimental Web refraction:** Canvas can produce R/G-channel displacement maps, SVG feDisplacementMap can offset a backdrop by channel, and CSS backdrop-filter:url(#filter) may be attempted. **Do not infer Safari/Firefox support** simply because ordinary backdrop-filter and SVG filters each work separately. Verify screenshots in the actual browsers.
- **Higher fidelity:** WebGL shaders require a *sampleable background texture* and may add dispersion and moving highlights. An arbitrary DOM node passed to a shader does not automatically provide its background image as a texture.
- **Appropriate surfaces:** Floating toolbars, players, search capsules and a limited-area material Hero. Do not proactively use this on ordinary forms, tables or long articles.
- **Non-negotiable engineering:** Keep component-library interaction ownership intact; test prefers-reduced-motion, readable light/dark backgrounds, SSR/client lifecycle, measured performance and a fallback without refraction.

The original synthetic four-layer interactive lab is assets/liquid-glass-layer-lab.html. It illustrates layers, controls and enhancement attempts; it **does not prove successful refraction in every browser**.

## Official sources

- GSAP: https://gsap.com/docs/v3/
- Anime.js: https://animejs.com/documentation/
- SplitText (two distinct implementations): https://gsap.com/docs/v3/Plugins/SplitText/ and https://animejs.com/documentation/text/splittext/
- PixiJS: https://pixijs.com/
- Three.js: https://threejs.org/manual/
- Curtains.js: https://www.curtainsjs.com/
- Apache ECharts: https://echarts.apache.org/en/
- Rough.js: https://roughjs.com/
- Vivus: https://github.com/maxwellito/vivus
- SVG Filter: https://developer.mozilla.org/en-US/docs/Web/SVG/Guides/SVG_filters
- tsParticles: https://particles.js.org/
- Matter.js: https://brm.io/matter-js/

**Maintenance boundary:** The suggestions for combinations, learning effort and performance risk are scenario-specific engineering judgments, **not measurements or performance benchmarks for a particular project**. The source requires ongoing version/license review; the actual project version and current official API take precedence.
