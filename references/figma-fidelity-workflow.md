# Figma Fidelity Workflow — Implement the Authorized Source, Not an Imagined Design

**Applies when:** User asks to implement or recreate an actual Figma frame, component or page. A screenshot alone may support visual approximation but does **not** prove Figma file access, hidden states or pixel-perfect fidelity.

## Gate F0 — Identify the source and authority

1. Determine the actual Figma **file URL/file key, page, frame/node ID and intended viewport** from user-provided source or connected design tools. If the user gave an accessible source, inspect its dimensions, layers, properties and actual design tokens. Do not fabricate inaccessible Figma metadata.
2. Distinguish **approved source**, inferred design information and Agent-proposed changes. User-specified design fidelity overrides generic MauForma style preferences. Do not silently replace brand colors, typefaces, spacing or visual composition with a preferred library.
3. **Tool-access boundary (B08):** A desktop Figma integration may use current selection only when the supported local connection exists. Remote Figma APIs/tools generally require explicit file and node identification. Do not assert that a screenshot or a browser tab grants Figma MCP access. When unavailable, ask for the necessary Figma URL/node or use clearly labeled screenshot-based approximation.
4. Confirm the source's assets and licenses. Fonts/icons/images cannot be invented or blindly downloaded; use available authorized assets or document the difference.

## Gate F1 — Extract design context before coding

Inspect: page/frame sizes, Auto Layout hierarchy, component instances/variants, Constraints, spacing, padding, typography, fills/strokes/effects, colors/variables, assets, interactions and relevant responsive variants. Derive **Design DNA**, but separate observed Figma properties from interpretation of why designers chose them.

- Map frames to existing routes and component ownership; avoid rebuilding an already mature component differently.
- Prefer installed matching components and theme tokens. A visual screenshot is not a mandate to install an unrelated UI library.
- For unusual layouts/gradients/media, preserve source intention while meeting accessibility; report genuine conflicts rather than redesigning them without authority.
- If a design relies on unprovided font/asset, explicitly mark unavailable and propose a scoped substitute **only with a clear fidelity limitation**.

## Gate F2 — Implementation within project architecture

1. Inspect framework and installed UI primitives, version/SSR constraints and existing components before editing. Reuse where faithful; add wrappers/variants rather than duplicating primitive behavior.
2. Implement frame structure, alignment, typography and visual states using semantic, maintainable tokens. Source values can be mapped to project variables; do not replace exact approved values with a generic predefined palette.
3. Preserve actual functionality and keyboard/focus behavior. A pixel-accurate but non-interactive `div` Select is not faithful to a working product.
4. Implement required variants/responsive frames, not imaginary ones. Do not add mobile layout without source/user scope; if only desktop Figma is available and mobile is required, state the design gap.
5. Respect actual front-end data ownership; no fake backend success merely because the static design contains a “Saved” label.

## Gate F3 — Compare at identical conditions

Use the **same source frame and actual browser viewport**, content and state. Compare:
- Main component bounding rectangles, relative alignment, padding/spacing, typography size/weight/line height and line wrapping;
- Image/icon assets, cropping, colors/gradients, shadows/borders/radius, overflow and responsive behavior;
- Interactive variants: default, hover, focus, selected, disabled, error, loading, modal/overlay and nested scrolling when designed.

Record actual screenshots and visible differences. **Pixel-perfect** is not an honest claim if font load, asset content, Figma source, viewport or browser state differs. Use “approximated” or “unverified” where appropriate.

## Gate F4 — Acceptance and limitations

- Test actual page routing, inputs, keyboard Tab/Shift+Tab/Escape, selected state, responsive scope and real API effects.
- Source-file inspection is **SOURCE INSPECTED**, code-only review is **STATIC CHECK**, synthetic galleries are **DEMO ONLY**, actual matching visual cases can be **VERIFIED** only for the tested states.
- Do not commit user/private Figma screenshots, brand assets or identifiable design snippets into public MauForma examples or CI artifacts unless specifically authorized.
- Final report: source file/frame/node and date, target route/viewport, reused components, intentional deviations, measured differences, actually tested states and remaining blockers.

Related: `references/design-dna-protocol.md`, `references/component-library-first-gate.md`, `references/browser-qa-protocol.md`, `references/semantic-boundaries.en.md` (B08).
