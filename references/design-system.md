> v4 scope: MauForma's directly implemented targets are **Web frontends**. Historical native SwiftUI/AppKit details transfer **design semantics only**, not requirements to install or generate native UI source.

# MauForma — Visual Language and Design System v2.0

> General Web-product design-system guidance, **not a visual clone of any reference or fixed default theme**. See [theme-design.md](theme-design.md) for palette mechanisms; actual approved brand and project tokens outrank examples.

## A. Shared qualities

- Low-noise backgrounds and visible but gentle surface hierarchy.
- Organize hierarchy with type scale, leading, weight and spatial relationships—not piles of icons, dividers and decorative fills.
- Coherent radius and quiet shadows; playful components can still be professional.
- Motion expresses actions and outcomes, not compulsory ornament.
- Precision and component reuse let the same visual language survive across viewports.

## B. Design Token architecture

Components use **semantic variables only**. Page layouts can map to a project spacing scale.

| Layer | Role examples | Bad pattern |
| --- | --- | --- |
| Background | `--spui-page-bg`, `--spui-surface`, `--spui-surface-soft` | Random new `#f6f6f8` per route |
| Text | `--spui-text`, `--spui-text-soft`, `--spui-text-muted` | Simulating help text with `opacity:.25` |
| Action | `--spui-accent`, `--spui-on-accent`, `--spui-focus` | Conflating theme accent with error |
| Structure | `--spui-border`, `--spui-control-border` | Input edges so pale they disappear |
| State | `--spui-success`, `--spui-warning`, `--spui-danger` | Every status changes with brand hue |
| Radius | `--spui-radius-panel/inner/control/button/dialog` | Arbitrary 9/12/14/19px per component |
| Density | `--spui-grid-gap`, `--spui-panel-pad-x/y`, `--spui-control-height` | Incoherent margins across pages |
| Motion | `--spui-motion-ui`, `--spui-motion-entry` | Unrelated 130/260/420ms durations per page |

## C. Density profiles — **illustrations only**

| Feature | `showcase` | `desktop` |
| --- | --- | --- |
| Outer panel radius | 32px | 16px |
| Inner Card radius | 18px | 10px |
| Input radius | 16px | 8px |
| Button radius | 999px | 8px |
| Dialog radius | 24px | 14px |
| Content max width | 980px | 1200px, adjusted for workbench columns |
| Panel padding | 24px 28px | 14px 16px |
| Grid gaps | 18px | 12px |
| Target control height | 44px | 36px, adjusted for platform accessibility |
| Ordinary UI motion | 200ms | 160ms |

These are **starting examples**, not mandatory design values or measured results of any real site. Actual tokens follow approved theme, inherited system, density and browser evidence.

## D. Typography

Prefer a suitable **platform font stack**; do not bundle proprietary fonts arbitrarily:
`-apple-system`, `BlinkMacSystemFont`, `SF Pro Text`, `PingFang SC`, `Microsoft YaHei`, `sans-serif`.

- Showcase display can use `clamp(56px,10vw,96px)`, weight 600, 1.04 leading and modest negative tracking. For dense CJK glyphs, check whether negative spacing harms clarity.
- Workbenches often start at H1 22–30px, H2 16–20px, body 14–16px, chart ticks/KPI labels/important metadata 12–14px with sufficient contrast. See [typography hierarchy](typography-hierarchy.md). These are **design suggestions, not WCAG minimum font sizes**; test real screens.
- Body line height often 1.45–1.65. Long measure increases reading cost; constrain width instead of arbitrarily shrinking type.
- Type roles, weights and spacing derive from one shared scale, never independent page-level heading treatment.
- Emphasis color comes from semantic theme. **Titles default to high-contrast solid text**; gradients are optional expressive moments.

## E. Shape and spacing

- Outer surfaces generally have larger radii than their children, with visible padding.
- Larger rounded Cards may suit showrooms; compact controls and clearer splits suit developer tools.
- An illustrative **4px spacing primitive** supports 4/8/12/16/24/32/40, but role-consistent grouping matters more than fixed universal values.
- Space must distinguish closely related, ordinary related and independent sections; don't give everything the same gap.
- Decorative separators are unnecessary unless the content grouping needs them.
- Tables/lists benefit from subtle fills, row height and alignment rather than Card-per-row.

## F. Shadows and surfaces

- Showcase example: `3px 5px 30px rgba(0,0,0,.08)`, a low-intensity candidate **not a default**.
- Desktop example: `0 2px 12px rgba(0,0,0,.055)`; dark/native shells may use even less and favor fine edges.
- Overlays should separate from panels but need not use intimidating pure-black shadows.
- Liquid Glass, huge blurs, neon glow and permanently moving backgrounds are **opt-in exceptions**, not universal quality signals.

## G. Component coherence

- Button: meaningful primary/secondary/ghost/danger; visible focus and disabled.
- Field: fixed label/hint/error/disabled/required structure.
- Panel: only for truly independent blocks; avoid endless nested Cards.
- Status: one semantic color/text system; switching brand theme never changes the meaning of an error.
- Navigation: route selection and keyboard focus are distinct states. Workbench selected items generally use calm fill + label/icon weight; don't add glowing colored rails by default. Genuine tree hierarchy/timeline rails can retain their separate meaning. See [sidebar rules](sidebar-navigation-design.md).
- Dialog: platform/accessible primitives, coherent content/action spacing, appropriate size.

**Strict sequence:** component inventory → tokens → real components and state gallery → business pages. See [component-first.md](component-first.md).

## H. Responsiveness and platforms

- Web/small screen: **reflow**, do not only shrink fonts. Text and form Buttons must not clip.
- Desktop: support narrow windows, sidebars and multiple panes; never squeeze a wide showcase grid into a small app window.
- SwiftUI/AppKit references: prefer platform dynamic color/type, accessibility and native behavior where relevant, transferring token **semantics only**.
- Ordinary motion respects system Reduce Motion; fast repeated actions should not bounce extravagantly.

## I. High-frequency workspace refinement (v6.3)

During Gate B/component state Gallery review, inspect seven patterns in [workspace-component-refinement.md](workspace-component-refinement.md). Functional navigation and recent object lists need distinct selected visuals; coherent neutral/state tones matter more than random bright rails, dots, gradients, glows and Cards. Palette examples at `../assets/sidebar-palette-examples.json` must be evaluated in actual light/dark screenshots. These workspace defaults **do not override marketing/creative art direction**.

## J. v6.5 — Copy necessity and readable roles

Do not auto-attach eyebrows, English subtitles, fake chapter numbers or slogans to every heading. Apply [semantic copy hygiene](semantic-copy-hygiene.md) to check independent value, then [typography hierarchy](typography-hierarchy.md) and `assets/typography-role-guidelines.json` to assign adjustable size roles to PageTitle, Section, Body, Metric, ChartAxis, Legend and Metadata. Real data needs legibility even when “secondary.” Check actual dark-mode contrast, 200% zoom and long CJK/English fields. Brand pages can have stronger art direction and different scales.

## K. v6.6 — User-approved, globally coordinated navigation palette

Before new design or major recoloring, read existing branding and full-page palette. **User-specified HEX/brand decisions prevail**. If unresolved, after official reference research present 2–3 complete **Sidebar + Main + Topbar + Card + Data Chart** combinations for choice, rather than silently deciding. Sidebar may have distinct tokens but inherits from project MASTER, **not a separate unrelated brand system**. Record actual user choice, source and exact value; changing an approved color requires renewed consent.

Rules: `references/sidebar-color-discovery.md`, `assets/sidebar-color-decision.schema.json`; preview: `assets/sidebar-color-preview.html`; numerical contrast: `scripts/validate_sidebar_color_decision.py`. Passing the calculator means the specified pairs have sufficient numerical contrast, **not** whole-page coordination or screenshot verification.

## L. v6.8 — MASTER shared language, per-page density from task

Global MASTER owns spacing, type roles, semantic colors and component contracts. `overview/analysis/operations` content amounts, whitespace and surfaces are page overrides. See `references/page-density-and-content-priority.md`: `airy/balanced/productive/compact` are adjustable starting points, **not orders to render every route as the same dense Cards**. Grouping matters more than any fixed whitespace ratio. First remove duplicated modules, then apply macro/meso/micro rules from `references/whitespace-and-surface-composition.md`. User-approved colors/nav/density cannot be changed without authorization just because content is being optimized.

## M. v6.9 — Grid and scroll safety as shared contracts

MASTER holds Grid tracks, gutters, page max width, page-end space, bottom action bar height/safe-area token roles. Per-route overrides choose `shared-row-grid / main-feature-span / editorial-asymmetry` by actual content—no forced equal heights. Peer data Cards share row starts. Change the Grid contract instead of adding random per-Card margins. App Shell owns one clear main scroll container and reaches the last record without fixed-bar occlusion, verified in target browsers. See `references/grid-alignment-and-viewport-safety.md`.

## N. v6.11 — Run task state semantics and visual roles

Shared Status/Priority/Progress/TaskRow components require accurate lifecycle and permission token mapping. Do not invent a blue-purple fill or left selection rail for every state. Running/completed/warning tones may use restrained accessible brand-compatible semantic colors, with **text/structure carrying meaning instead of hue alone**. Filters, row markers and detail views share the same Task ID, status and count source. Unauthorized recovery actions must be disabled/hidden appropriately. MASTER holds components/semantic tokens; the page task determines whether a left status panel exists.
