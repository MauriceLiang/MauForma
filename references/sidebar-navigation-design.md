# Sidebar — Mature Visual and Interaction Rules for Desktop Navigation

These are verifiable general Web-sidebar principles; all good/bad scenarios are synthetic, **not diagnoses of real user screenshots**. There is no universally correct Sidebar shape, color or selection rail. Actual task and approved user design take precedence.

## Icon-system quality is independent of sidebar color

Even a Sidebar with correct color, row height and text size can fail when arbitrary icon-name matches produce dense Git topology, illegible file-folder detail, abstract laboratory vessels and mismatched optical weights. Begin with `references/icon-art-direction-gate.md`: **determine each navigation item's task → compare two real/verified symbol candidates → review the whole family on one screen → adopt shared SidebarItem**. Identical SVG width/height/stroke is not proof of visual quality.

A “compare projects” operation might use simple opposing arrows rather than a Git-branch topology if it compares project data; if it truly compares Git branches, a Git icon may be right. “Research analysis” with scatter/statistical charts might better use Chart/Scatter than Flask; laboratory administration differs. **These are not mandated icon names.** Check the actual 16–24px render against Chinese weight, icon+Badge+Active background and the group as a whole; brand marks can differ from generic UI symbols. If the group fails, reconsider candidates instead of endlessly adjusting margins/colors.

## Common synthetic failures and corrections

| Observation | Why it matters | Repair |
| --- | --- | --- |
| Deep blue-gray base, bright blue selected fill, cyan left rail, orange dot simultaneously | Multiple emphasis cues compete; orange state meaning unclear | Use one coherent neutral hierarchy and **one dominant selected signal**; every status dot needs business meaning and text/help |
| Repository analysis nav and Recent entries use identical large fill+rail | Active destination vs opened object are confused | Main nav represents current route; Recent list represents an object/focus/working item and can use lighter distinct selection semantics |
| Bottom prototype-note Card looks similar to active nav | Help competes with routine operations | Muted neutral help visually below nav, grouped separately from account/status; keep discoverability if collapsible |
| Massive vertical whitespace plus uniform row heights | Not necessarily an error but may not reflect actual hierarchy | 36–44px nav-row starting range plus group spacing, adjusted to current density and scanability |
| Selected adds bright left rail over already emphasized fill/text | Redundant signals create generic template feel | Default to **selected background + text/icon emphasis**, no extra rail; keyboard focus is a separate state, never remove it |

## 0 — Identify the Sidebar's actual purpose first

A sidebar might be administrative navigation, IDE project tree, file explorer, document contents, creative-scene rail, timeline or mobile Drawer. Do **not** turn “no bars” into a global prohibition on every sidebar line:

- **Operate:** Stable, scannable high-frequency navigation. Prefer subtle selected fill plus text/icon contrast.
- **Read:** TOC hierarchy/progress lines may be meaningful when encoding chapter depth/current position.
- **Experience:** Portfolio/story timeline rails may be a deliberate visual language with accountable meaning.
- **IDE tree:** Connector lines represent parent-child structure, not secondary selected emphasis.
- **Accessibility:** Selected must be visible and semantic: `aria-current="page"` on current route link; keyboard focus remains separately visible.

## 1 — Semantic colors, not arbitrary “premium blues”

Old `assets/sidebar-palette-examples.json` is for **color/state relationship checks**, not a final palette. Whole-page user-led color selection belongs in `references/sidebar-color-discovery.md` and `assets/sidebar-color-directions.json`.

| Token role | Responsibility |
| --- | --- |
| `sidebar-bg` | Overall nav canvas; not competing with main content |
| `sidebar-surface` | Group/footer surface distinct from bg if needed |
| `sidebar-hover` | Temporary pointer hover feedback |
| `sidebar-selected` | Current route fill, **distinct from hover** |
| `sidebar-text` | Primary readable text; typical normal text contrast 4.5:1 |
| `sidebar-text-muted` | Secondary/category labels, not nearly invisible |
| `sidebar-icon` | Icon supports text hierarchy; not a random hue per icon |
| `sidebar-focus` | Keyboard focus-visible **independent** of route selection |
| `sidebar-border` | Container boundaries, not multiple heavy decorative rules |
| `sidebar-accent` | Brand-action emphasis, not every active navigation element |

**Relationships outrank literal colors:** Similar hue or adjacent neutral base → subtle luminance separation for hover/selected → primary/secondary text contrast → restrained brand accents → independent success/warning/error. Orange is not a default “lively” dot, **but actual warning/unread/failure can use orange/red** along with text, shape or Tooltip, not color alone. Dark mode needs its own palette rather than inverted light values; numerical checks of sampled colors cannot verify actual screenshot aesthetics.

## 2 — One dominant visual system for selected state

| Strategy | Implementation | Appropriate use |
| --- | --- | --- |
| **A — Soft inset (default recommendation)** | Low-saturation single background with clear label/icon contrast and moderate weight; no additional left bar | Most admin/workspaces |
| **B — Text emphasis** | No selected Card; font/icon weight and quiet region rhythm, independently visible hover/focus | Minimal desktop/read sidebars |
| **C — External active indicator (optional)** | Short bar in **independent gutter outside nav item**, with visible separation from rounded fill; never use item border/inset shadow as imitation | Routes requiring clear location cue |
| **D — Contextual rail** | Actual structural TOC hierarchy, timeline or Tree guide | Learning chapters, trees, creative timelines |

Avoid stacking a strong selected fill, glowing left bar, gradient outline, heavy shadow and tinted icon for one state. **External indicator and colored nav-item border are different shapes.** If a rail is justified, place it outside the item; `border-left`, `border-inline-start`, inset `box-shadow` and attached pseudo-elements are forbidden as substitute selected rails. Genuine tree/timeline connector lines have distinct semantics. See `references/sidebar-selection-indicator-gate.md`.

State distinctions:
- **Hover:** Temporary pointer feedback, not stronger than selected.
- **Selected:** Current real route or working object with accurate semantics.
- **Focus-visible:** **Separately visible**, even when selected has no rail.
- **Disabled:** Explain nonactionable/permission state, not merely gray.
- **Loading/error:** Reflect real meaning; no arbitrary orange dot.

### External short-rail layout only when chosen

- Nav row owns the indicator, **outside link/Button DOM** as decorative sibling or parent element; reserve uniform gutter without changing NavItem left border, padding, radius or background.
- Show for only the current route, deriving from actual router state. Other rows' indicators are transparent/absent, text starts aligned.
- Keep rail short with visible positive gap; no clipping of icons or rails in collapsed/narrow Sidebar. Focus ring is still separate.
- `assets/sidebar-refinement-gallery.html` compares no rail, valid external rail and invalid attached border. The attached example is a **negative** fixture, not reusable production code.

## 3 — Separate nav / recent / help / account areas

1. **Main navigation:** Core destinations sorted by IA; use `aria-current="page"` for active route.
2. **Recent objects:** Scannable object list; active object may have lighter fill/weight. “Recently opened” does not necessarily equal “current route,” so avoid misleading double-active styles.
3. **Group labels:** Information-free headings get no bright accent; type prominence lower than actual content.
4. **Help/tip:** Usually supporting priority; permanent safety/failure warnings may have higher priority.
5. **Account/settings:** Stable and reachable in collapsed nav; fixed bottom area must not obscure navigation in short windows.
6. **Scroll/collapse:** Main nav may scroll, footer remains accessible, keyboard/screen-reader order matches visual sequence.

## 4 — Component API and visual tests

- `UiSidebar`, `UiNavItem`, `UiRecentItem`, `UiSidebarSection` have distinct responsibilities; one `active` style does not fit all. Optional `SelectionIndicator` lives in outer row, not NavItem border.
- Props: `selected` corresponds to real route/working object; `badgeStatus` means genuine business status. Color derives from semantics.
- Reuse Vue/React RouterLink/NavLink or framework links; `div + onClick` is not a navigation link.
- Gallery/QA: default, hover, selected, focus-visible, disabled, collapsed, long CJK/English, narrow view, light/dark. Record observed and unobserved cases.
- Before adding rail ask **which independent information it encodes**. If no answer, remove it; never ban every colored line merely because of a particular hue.

## 5 — Required positive and negative synthetic comparisons

**Bad:** Current nav link's own left border is heavily colored over bright fill/icons; Recent objects also duplicate it, creating multiple false “current locations.”

**Good for frequent work:** Current route uses restrained background, stronger label/icon; keyboard focus independently appears when navigating. Recent objects have lighter selection; orange dot only for a real “build failed” status with explanation.

**Valid optional:** Short external rail in gutter, visible gap, intact four-sided item border/radius. Other rows have no rail. **Tree exception:** Connector lines encode hierarchy rather than nav item selected border.

`assets/sidebar-refinement-gallery.html` is an original conceptual demo, not a real user app screenshot or tested repair. Actual product QA remains required.

## Sidebar palette and selection are user decisions

Given a Sidebar screenshot, inspect **Sidebar/Main/Topbar/Card/Chart** together, not just a dark sidebar that “looks technical.” For new/redesign without resolved color, read `references/sidebar-color-discovery.md` and `references/sidebar-color-reference-cases.md`, recommend 2–3 coordinated whole-page directions, and let the user decide. Official examples provide semantic color methods, not directly transferable brand HEX values.

Respect explicit black/white/green/purple/blue or specific HEX choices. Where contrast fails, adjust **surrounding** text/selected/hover/focus/main, not secretly rewrite the selected brand color. `assets/sidebar-color-preview.html` is a conceptual whole-page preview; verify on the actual app. Unapproved recommendations cannot be committed as final theme. Existing confirmed colors can be inherited. Sidebar tokens remain owned by global MASTER, not a competing brand theme.

## Decide whether Sidebar is needed before styling it

These rules apply **only after actual navigation architecture calls for a Sidebar**. For new or redesign first read `references/navigation-architecture.md`. A few top-level categories, mobile 3–5 core routes, dual-object lists in wide workbenches, Top+Side or a bottom action bar can need different navigation modes. “Workbench” alone does not mandate left navigation. Do not repeat the same route list in Top, Side and Bottom. Navigation placement is a separate decision from user-approved v6.6 colors.
