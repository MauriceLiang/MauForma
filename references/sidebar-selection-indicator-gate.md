# Sidebar Selection Indicator — External Rail Versus Navigation Item Border

Applies to Web primary sidebars, settings navigation and other contexts **already using sidebar navigation**. It does not require a selection rail anywhere. For a new page, first consider a subtle selected background, text/icon emphasis, and inherit approved styling.

## One clear and explainable selected-state structure

1. **Default: no rail.** A subtle selected background, text/icon weight and independent hover/focus-visible states convey current route. Never add a colored bar automatically for “polish.”
2. **Optional: short, separate external rail.** Only when the user requests it or real design semantics warrant it, show a separate vertical short mark **outside the active nav item**, normally in a left gutter (logical start side for RTL). It must have a **visible gap** from the item's border/fill. Retain complete item radius, background and inner text padding. **Show only on the real selected item**—never one rail on every nav row.
3. **Forbidden: recolor nav item's own left border to impersonate an external rail.** Do not put colored `border-left`, `border-inline-start`, `box-shadow: inset 3px 0`, or attached `::before` on a `[aria-current=page]` link/button. This changes the item's border, which is visually different from a separate external marker.
4. **Distinct tracks have distinct roles.** Reading progress in a TOC, hierarchy connector lines and drag insertion markers can be continuous, but they are not ornamental selection rails for ordinary page navigation. Do not paint all of them with the current-route color.

## Component and layout contract

- `SidebarItem` owns link, selected background, icon, label and focus. A parent row owns `SelectionIndicator`, preferably a sibling decorative element or parent pseudo-element, not the link's single colored border.
- Reserve a stable indicator gutter for alignment even on unselected rows, avoiding horizontal label shifts on route changes. Do not use negative margin or absolute positioning beyond a clipping parent to pretend the mark is external.
- A rail is **short**, not a full-height colored border. Illustrative values: about **2–4px wide, 12–22px high, 6–10px visible gap**. These are **starting values, not mandatory global dimensions**, and cannot consume the link's internal text padding.
- Decorative element is `aria-hidden="true"`, not interactive or in Tab order. Actual route items are links with `aria-current="page"`; a demo may use Buttons and `aria-pressed` but must not be blindly copied as real navigation.
- Focus-visible, hover and selected states differ. A rail never replaces keyboard focus; focusing another item cannot fabricate a second active indicator. Only one main-nav item denotes the current route; asynchronous transitions must derive state from actual router.

## Illustrative implementation (adapt structure and theme)

```html
<nav aria-label="Primary navigation" data-mf-selection-indicator="external">
  <div class="sidebar-row" data-current="true">
    <span class="sidebar-indicator" data-mf-indicator-rail aria-hidden="true"></span>
    <a class="sidebar-item" data-mf-nav-item href="/overview" aria-current="page">Overview</a>
  </div>
  <div class="sidebar-row" data-current="false">
    <span class="sidebar-indicator" data-mf-indicator-rail aria-hidden="true"></span>
    <a class="sidebar-item" data-mf-nav-item href="/activity">Activity</a>
  </div>
</nav>
```

```css
.sidebar-row {
  display: grid;
  grid-template-columns: 3px minmax(0, 1fr);
  align-items: center;
  column-gap: 9px;
}
.sidebar-indicator {
  width: 3px;
  height: 18px;
  border-radius: 3px;
  background: var(--sidebar-selection-indicator);
  opacity: 0;
  pointer-events: none;
}
.sidebar-row[data-current="true"] > .sidebar-indicator { opacity: 1; }
.sidebar-item { border-inline-start: 0; box-shadow: none; }
.sidebar-item[aria-current="page"] { background: var(--sidebar-selected); }
.sidebar-item:focus-visible { outline: 2px solid var(--sidebar-focus); outline-offset: 2px; }
```

`data-current` must follow real router state, never a hardcoded permanent selected row. The example demonstrates structure, not mandated color, font, dimensions or APIs; use current design system. For no-rail mode, render **no decorative node and no reserved gutter**.

## Acceptance and evidence

On the actual product check desktop, collapsed/expanded sidebars, narrow windows, long Chinese/English labels, light/dark, keyboard focus, browser history back/forward and 200% scaling:

- External marker is **non-touching and nonoverlapping**, with rectangle entirely outside the item's border box; retain a visible positive gap at each supported viewport.
- **Only** the active route has a visible marker. After navigation, old marker disappears, new one moves correctly, and labels/backgrounds do not jump.
- Item itself retains whole border/radius and independent focus; unselected rows have no visible leftover colored bars.
- Do not layer loud selected fill, bar, glow and icon treatment without purpose. If no measurable or noticeable benefit, choose default no rail.
- Passing static checks or synthetic gallery does **not** verify real page. If not opened, say `NOT TESTED`.

### Optional geometry audit on actual pages

For an implemented external rail, mark sidebar root `data-mf-selection-indicator="external"`, links `data-mf-nav-item`, and sibling decorative nodes `data-mf-indicator-rail`. For no-rail mode `data-mf-selection-indicator="none"` is optional. The attributes facilitate **optional checks**, not required app architecture; real router still owns selection.

With running dev server:

```bash
node scripts/audit_sidebar_indicator.mjs http://localhost:5173
```

Only annotated nav groups are checked for geometry, contact, excessively tall rails, inset borders and multiple active markers. Unannotated/unopened pages cannot pass this audit. This script does not independently certify navigation structure, aesthetics or accessibility; human review remains necessary.

Concept comparison: `assets/sidebar-refinement-gallery.html`; automated regression `tests/sidebar_indicator_browser_smoke.mjs`. Palette remains subject to `references/sidebar-color-discovery.md` and user-approved tokens.
