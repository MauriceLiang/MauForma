# Liquid Glass Optical Effects — Optional Web Material Technique

> **Scope:** A generic Web visual capability, **not** MauForma's default appearance, a UI component library, or an equivalent implementation of Apple's native rendering. Use only when the user requests glass/liquid effects, the confirmed brand direction requires them, or the user authorizes them after comparing options. Readable, performant, degradable **real interactions come first**.

## 1. Four optical layers — blur is not refraction

| Layer | Visual responsibility | Possible implementation | Parameters | Failure signs |
| --- | --- | --- | --- | --- |
| **Transmission** | Let imagery and outlines beneath the panel pass through, creating a base material | Translucent color, single tint/saturation layer | tint, alpha | Too opaque looks like a solid Card; too transparent harms foreground contrast |
| **Refraction** | Offset sampling of the **background image** so straight lines/text bend near curved edges | Displacement map + SVG feDisplacementMap in a backdrop filter (experimental); or WebGL shader | edge falloff, strength/scale, normal direction | Blur without pixel displacement is **frosting, not refraction** |
| **Specular / Fresnel-like highlight** | Nonuniform highlights imply curvature and directional light | Directional radial/linear gradients, masks/overlays; optionally shader normals/view angle | direction, intensity, falloff | Uniform bright outline is just a border; CSS gradients are **not strict Fresnel physics** |
| **Elevation** | Separate panel from backdrop and imply floating | Soft box-shadow/drop-shadow | y-offset, blur, spread, opacity | Too many strong shadows muddy surfaces and reduce contrast |

**Optional background blur:** A small backdrop-filter:blur(...) can soften visual noise, but blur is **not** one of the four layers and is not refraction. Excess blur conceals the edge bending that a refractive treatment should reveal. Never present blur alone as proof of refraction.

### Why does the background bend?

An idealized **design/rendering approximation** assigns near-zero offset to the flat center and progressively stronger X/Y sampling offsets near a rounded-rectangle boundary, with direction estimated from surface curvature and normal. This is **not a complete physical ray-tracing model or a description of Apple's proprietary renderer**.

SVG feDisplacementMap uses two channels of the in2 texture to shift horizontal and vertical sampling of source in. With xChannelSelector=R and yChannelSelector=G:

~~~text
output(x, y) = source(
  x + scale * (R(x, y) / 255 - 0.5),
  y + scale * (G(x, y) / 255 - 0.5)
)
~~~

A neutral value near 127.5 (commonly 128 in 8-bit encoding) yields approximately zero shift. Deviating from neutral increases offset. **scale multiplies map strength**: with a fixed texture, changing scale changes intensity without generating a new map; however, changing **shape, dimensions or edge slope requires regenerating the map**. Source: https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feDisplacementMap.

## 2. Implementation paths, in priority order

### A. Inexpensive translucent fallback — cross-browser baseline

1. Keep real content as normal DOM with real text selection, input and accessibility.
2. Add a separate tint surface, optional mild blur, **directionally varied highlights**, and a soft external shadow.
3. Retain genuine focus-visible, hover, selected and disabled states. Do not trade contrast for ornamentation.
4. Label this **glass-like / translucent fallback**. Do **not** claim that background refraction has been implemented.

Illustrative layering only, **not** a drop-in universal component:

~~~html
<div class="glass-surface">
  <div class="glass-tint" aria-hidden="true"></div>
  <div class="glass-highlight" aria-hidden="true"></div>
  <div class="glass-content">Readable real controls and text</div>
</div>
~~~

~~~css
.glass-surface {
  position: relative; isolation: isolate; overflow: hidden; border-radius: var(--glass-radius);
  box-shadow: 0 12px 35px rgb(0 0 0 / .16);
  background: rgb(255 255 255 / .12);
}
.glass-tint, .glass-highlight { position:absolute; inset:0; pointer-events:none; }
.glass-tint { background: rgb(255 255 255 / .06); backdrop-filter: blur(4px); }
.glass-highlight {
  border: 1px solid rgb(255 255 255 / .5);
  border-radius: inherit;
  background: linear-gradient(135deg, rgb(255 255 255 / .25), transparent 40%, rgb(0 0 0 / .08));
}
.glass-content { position: relative; z-index: 1; }
~~~

The CSS highlight approximates directional lighting; it does **not compute a physical Fresnel reflection**. Its border only delineates an edge, not optical validation. Add decorative glass layers to supported surface/overlay/theme extension points of an existing mature component library. **Do not reimplement Select, Dialog, Popover or keyboard primitives** to gain a glass effect.

### B. Experimental Web optical refraction — Canvas map + SVG Filter + CSS

1. Measure the desired shape dimensions and corner radius. Generate a pixel displacement field with a rounded-rectangle signed-distance function or edge-normal approximation: offsets near zero at center, stronger near edges. Encode X in red, Y in green, blue neutral and alpha=255.
2. Export displacement as a Canvas PNG or Blob URL; feed it to SVG feImage or a compatible SVG image input as **in2**. Use feDisplacementMap with in=SourceGraphic, in2=map, xChannelSelector=R, yChannelSelector=G; adjust scale for intensity.
3. Enable backdrop-filter:url(#...) **only after observing actual refracted background pixels on the target browser**. CSS.supports("backdrop-filter","url(#...)") alone **does not prove** working optical refraction.
4. Regenerate on changes to control width, height or radius; throttle via ResizeObserver, not per-frame ImageData creation. Changing scale alone does not require rebuilding the displacement image. Revoke Object URLs, remove SVG filters/observers on teardown, and give every component instance a unique filter ID.
5. Use test backgrounds with readable stripes/text so displacement can actually be observed. A flat color does not allow visual confirmation.
6. Debug rounding, edge highlight and shadow as **independently switchable layers**. If refraction is unsupported, fall straight back to A; a control must never disappear or become a black rectangle.

**Filter input ownership matters:** CSS filter:url(#...) applied to an element changes that element's **own rendered content**, which is not equivalent to distorting the page **behind** it. Only an SVG filter genuinely applied during backdrop sampling produces a refracted background. Wide availability of feDisplacementMap **does not imply** that the combined CSS+SVG backdrop pipeline works across browsers.

### C. Higher fidelity — WebGL / GLSL when actually needed

WebGL shaders may support dynamic curvature, RGB dispersion, pointer/touch-driven high-frequency distortion, varying radii and volumetric material effects. However:

- Shaders **cannot automatically read arbitrary pixels behind any DOM**. Design a **sampleable background texture** (separate Canvas/texture, prerendered imagery or authorized background capture). Check permissions, cross-origin media and synchronization with updates.
- RGB channel-splitting raises sampling/performance cost; the lightweight SVG example **does not implement chromatic dispersion**. Do not claim "the same dynamic liquid glass as Apple" without an actual rendering implementation.
- Budget GPU/DPR/effected area, including scrolling and low-powered devices. Apply to a few focal surfaces rather than making full-screen WebGL the product's default background.
- In SSR applications, initialize visual processing only on the client; dispose textures, programs, Canvas/renderer and subscriptions when components unmount. Real business controls remain semantic, keyboard-operable DOM.

## 3. Component contexts and roles

| Component / context | Appropriate glass treatment | Discouraged |
| --- | --- | --- |
| Capsule Search / toolbar | Small translucent surface, edge highlight, optional mild refraction | Redrawing a real Input as Canvas and breaking IME/focus |
| Circular thumb / Button handle | Local shadow, highlight and transmission | Conveying status solely by highlight brightness |
| Player controls / floating actions | Limited focus material and elevation | Whole-screen glass covering captions or control labels |
| Notification overlay / promotional Card | Controlled translucency/blur, contrast checks over multiple backgrounds | Turning every data Card into glass and continuous GPU compositing |
| Dense form / long reading / Tables | Usually retain ordinary solid surfaces | Refracting every row or distorting backgrounds behind body text |

**Component Library First still applies:** Choose the existing Button/Select/Popover/Dialog implementation first; add material in approved theme/surface slots or outside decorative layers. Do not duplicate library internals, break native forms or interfere with overlay geometry.

## 4. Browser compatibility and graceful degradation — do not simplify

| Capability | Evidence level | Correct strategy |
| --- | --- | --- |
| Translucent surface, gradient highlight, shadow | Standard CSS primitives | Basic fallback |
| backdrop-filter:blur(...) | Broad modern-browser support, **not all versions/devices** | Optional; readable translucent or solid fallback |
| SVG feDisplacementMap for the image itself | Broadly supported | **Not proof of backdrop use** |
| backdrop-filter:url(#svgFilter) background-refraction pipeline | **Not universally guaranteed**; WebKit/Firefox compatibility risks | Experimental progressive enhancement **only after actual target-browser pixel tests** |
| WebGL shader | Controlled sampled background, GPU budget and lifecycle needed | Optional higher-fidelity route with static fallback |

Do not hide a fallback merely because @supports claims a property exists. **Actual pixel comparison:** screenshot stripe/text background with refraction off and on and confirm meaningful displacement. Test Chromium, Safari/WebKit and Firefox separately **or explicitly mark untested browsers NOT TESTED**.

Official support and issues:
- https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/backdrop-filter
- https://developer.mozilla.org/en-US/docs/Web/SVG/Reference/Element/feDisplacementMap
- https://bugs.webkit.org/show_bug.cgi?id=245510
- https://bugs.webkit.org/show_bug.cgi?id=297770
- https://github.com/mdn/browser-compat-data/issues/24110

## 5. Accessibility, performance, safety and initial acceptance

- **Readability first:** Highlights/refraction cannot obscure titles, input values, placeholders, icons, errors or focus. Test light/dark, high contrast, and worst-case moving backgrounds. Use a more opaque content underlay if needed, rather than sacrificing text to achieve "full translucency".
- **Reduced motion:** Under prefers-reduced-motion, stop looping/pointer-following refraction; static material may remain. Removing transitions must not break business state.
- **Resource budgets:** Limit surface area, redraw frequency, Canvas texture size, DPR and SVG filter count. Pause when backgrounded/invisible; do not apply expensive filters to every nav item, row, dialog and Card by default.
- **Pointer/keyboard:** All decorative layers use pointer-events:none. Preserve semantic DOM, touch targets, overlay stacking and focus.
- **Browser/SSR stability:** Missing filter or image must never yield unreadable transparency/black; no hydration flicker. Actually test inherited library CSS layering and portals.
- **Evidence:** DEMO ONLY = example; STATIC CHECK = source; VERIFIED = tested specific target routes/browsers; NOT TESTED must **not** be recorded as compatible.

### Gate: Should glass be enabled at all?

1. Does the user or confirmed brand direction genuinely require optical glass? Otherwise retain ordinary surfaces.
2. Does the component's role, size and backdrop texture support useful refraction? Skip heavy processing for flat backgrounds and dense data screens.
3. Does the established library expose surface/theme slots? Use them without recreating interaction behavior.
4. Is there a **readable ordinary-material fallback**, target browser evidence and a performance budget? If not, implement **only A**.
5. Can the **four layers toggle independently** for verification? Do not hide blur, highlights and distortion inside an inscrutable CSS blob.

The original teaching demo, assets/liquid-glass-layer-lab.html, lets developers independently inspect transparency, refraction toggle, specular highlight, shadow and blur. It is **not proof** of working SVG backdrop refraction on every browser or real product. All effects must be reversible and context-specific.

**Learning provenance:** The four-layer model and basic implementation order derive from text extracted from a user-supplied liquid-glass educational video, generalized into Web design knowledge. SVG channel formulas, CSS and browser limits are checked separately against MDN/WebKit/browser compatibility records. No user-specific screenshot or business data is included.
