# Maintenance Protocol for New Animation Engines

MauForma can incorporate new animation technologies over time, but only after research and validation. Novelty alone is not a reason to upgrade a default dependency.

## Engine evaluation record — all fields required

1. Name, official homepage/documentation, maintenance status, current major version and date checked.
2. Web suitability: DOM/SVG/Canvas/WebGL/design assets and browser compatibility.
3. Frameworks where it works directly (React, Vue, Svelte, Angular, Solid, Astro, Vanilla), with real package names and import paths.
4. Strengths: basic transitions, state-driven layout, timelines, scroll, paths, physics, dragging or complex character animation.
5. API and lifecycle: mount, cancel, destroy, route change, SSR, StrictMode and observer cleanup.
6. Performance/build cost: JavaScript size, tree shaking, frame rate, low-end devices and animation fallbacks.
7. Accessibility: reduced motion, keyboard, focus and pausing loops.
8. Licensing and commercial restrictions; third-party blocks, assets and plugins may have separate licenses.
9. Concrete benefits beyond existing CSS/Motion/Anime.js/GSAP; distinguish new capabilities from duplication.
10. At least one working example, one negative example and one failure/fallback test.

## Adoption rules

- A new engine may enter the **candidate** list; it never automatically becomes a global default.
- Set at most **one principal imperative animation engine per project**. Multiple engines require explicitly separated areas and responsibilities.
- Update `animation-engine-selection.md`, `animation-integration-lifecycle.md`, `examples/prompt-library-web.md` and the validation checklist together when adopting an engine. If a referenced example path is absent in the current repository, reconcile the reference rather than inventing a file.
- Do not claim the catalog covers all possible effects: APIs are finite, but compositions are not.

## v6.2 — Classify specialist rendering capabilities before adoption

Do not misclassify all Canvas/WebGL/physics tools as animation engines. Assign new tools to a suitable category first: **animation orchestration / text splitting / 2D rendering / 3D rendering / DOM–WebGL / charts / hand-drawn SVG / strokes / browser filters / particles / physics**. Compare against `assets/visual-tech-catalog.json`, then add a dependency only after confirming that existing technology cannot meet the actual requirement. For composition, accessibility, mobile GPU limits and failure fallbacks, see `references/visual-tech-selection-12.md`.
