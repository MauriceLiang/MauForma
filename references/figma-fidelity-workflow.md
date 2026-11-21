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


## Source-parity requirements: input confidence and connected-tool capabilities

**Trigger only when:** The user supplies an explicit Figma URL, design node/current selection, or asks to **faithfully implement a particular existing design**. This is different from merely learning a site's visual character: do not redesign a specified Figma implementation without authorization.

| Actual input and permission | What the Agent may do | What it must not claim |
| --- | --- | --- |
| Accessible Figma MCP or compatible design-context tool | Obtain node hierarchy, Auto Layout, variables, component variants, actual copy, assets and screenshots to guide high-fidelity implementation | Do not claim “1:1 finished” without checking the target browser |
| Only a user-provided design screenshot | Estimate **visible** geometry, typography, colors and composition for a clearly labeled **visual approximation** | Screenshot proves exact layer sizes, constraints, component variants, font identity or original HEX |
| Figma URL but no design-file access | Explain connection/permissions and request accessible source or permitted exports | Guess the frame, invent MCP returns or claim to have inspected it |
| Only “use this feeling/style as inspiration” | Follow design-reference-learning-gate.md and extract appropriate principles/non-copyable details | Treat the reference as a pixel-clone contract |

**Desktop selection is not remote node access.** A compatible desktop tool's **current selection** and a remote Figma service's **file/node link** are distinct capabilities. Check which actual connected APIs provide selection, node context, screenshots and assets before using them. If unsupported, label the operation unavailable or BLOCKED. Never invent a tool name, response shape or successful read.

## Source-parity requirements: the seven implementation stages

1. **Lock the source:** File, page, node/frame, variant, intended viewport, current selected version; list multiple routes/frames and match them appropriately.
2. **Read design context:** From authorized tools obtain actual node tree, Auto Layout, Constraints, Typography, Fill, Stroke, Effects, Variables, Variants and asset URLs, plus an authoritative screenshot. Split overly long payloads by real frame/child nodes rather than inventing omitted content.
3. **Record token provenance:** Tag each value as **source-figma / inherited-project / inferred-from-screenshot / unknown**. Map colors, fonts, dimensions, spacing, radius, borders, shadows and breakpoints to existing themes. Do not copy dozens of hard-coded overrides for tiny differences; document conflicts and the resulting visual impact.
4. **Map components:** Make an explicit Figma component → existing project component mapping. Reuse mature UI infrastructure. For Select, Dropdown, Dialog and Button follow component-library-first-gate.md; visual fidelity is not permission to recreate a broken keyboard/focus engine. Use themes or controlled variants for special skins.
5. **Use authorized assets:** Only use images/icons/fonts available under valid permission; preserve actual text and available legitimate imagery. Figma-generated demo JSX/Tailwind is not automatically suitable production code. Keep the inherited framework and routing.
6. **Verify both forms of parity:** Compare design screenshot and rendered browser with **matching viewport, device pixel ratio and font/asset loading state**. Inspect structure, bounds, alignment and typography first, then color, borders, shadows and raster details. Separately verify interaction parity (focus/hover/selected/disabled, keyboard, responsiveness and **real business results**). If the design omits states, derive them from the existing system/accessibility guidance and clearly mark them as inferred.
7. **Keep a difference ledger:** difference → impact → cause → resolution/intentional deviation → evidence. Recapture and recheck affected areas in the actual browser after repairs. Small numeric screenshot differences do not establish functionality, and font antialiasing/moving media may explain environment-specific pixel deviations.

## Source-parity requirements: fidelity conflicts and authority

- When the user explicitly requests implementation **according to the provided design**, that design is the **primary visual source within the agreed scope**, not an invitation for the Agent to seek something prettier.
- Preserve existing business semantics, accessible interactions and stable code. If the Figma design conflicts with an inherited design system/component library, **name the exact mismatch and effect on fidelity** instead of silently claiming a redesign is an optimization.
- Figma and the Web render differently; percentage layout, font antialiasing and native browser controls may not match exactly. Never promise unconditional 100% pixel equality.
- Do not add Liquid Glass, frosted glass, large gradients or particles to a fidelity task unless the source design or explicit user approval warrants them.
- Do not publish private design images, commercial fonts, components or other assets to the public Skill repository without authorization. Retain only resources permitted for this target project.

## Source-parity acceptance report template

~~~text
Target: page / component / node and design version
Evidence: readable Figma nodes / screenshot / visible content only
Design constraints: composition, layout, type, color, assets and interactions
Component mapping: inherited primary library + shared components + justified exceptions
Parity checks: same-viewport images, layout, typography, color, states and responsiveness
Missing / intentional differences: location, reason and authorization
Verification status: VERIFIED / STATIC CHECK / NOT TESTED / BLOCKED
~~~

**VERIFIED is scoped to the exact environment, pages and checks performed**; it is not blanket parity for every device, visual state or backend workflow. Screenshot-only input supports approximation, **not** a claim of precise file-node fidelity. When an exact implementation is requested but remote nodes are blocked, do not invent missing property values and call the result 1:1. Reference implementation boundaries: semantic-boundaries.zh-CN.md B08 (bilingual maintenance source), semantic-boundaries.en.md B08 (Agent runtime). Actual Figma MCP operations must follow the real connected tool API and current official documentation.

Only when relevant, load design-reference-learning-gate.md, design-system.md, component-library-first-gate.md and browser-qa-protocol.md. General upstream Skill credits belong in repository README, not task runtime instructions.


Related: `references/design-dna-protocol.md`, `references/component-library-first-gate.md`, `references/browser-qa-protocol.md`, `references/semantic-boundaries.en.md` (B08).
