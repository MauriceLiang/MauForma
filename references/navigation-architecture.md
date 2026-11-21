# Navigation Architecture — Information Architecture Determines Placement (v6.7)

**Goal:** Distinguish “where to go” (destination), “what to do on the current page” (action), “switch subviews within this page” (local tabs), and “switch object/collection” (context picker) before selecting navigation structure. SaaS does not automatically require a sidebar, and small mobile width does not justify squeezing seven or eight destinations into the bottom bar.

## 0 — Fact-first: six tradeoff questions

1. **How many primary destinations?** Record real names, whether peers, and frequency. Do not count buttons, filters or external links as primary navigation destinations.
2. **How deep is hierarchy?** Top-level channels, work within a channel, object/file trees and in-page Tabs each serve different purposes.
3. **How do users switch?** Frequent cross-section navigation and comparison, repeated actions within a workspace, or browsing product storytelling? How much first-screen area is needed for data, canvas or photography?
4. **Primary devices and window widths?** Large monitor, narrow laptop window, tablet, mobile; real Web/PWA/Tauri WebView use and resize constraints.
5. **Brand and approved design?** Inherit actual IA and visual direction. When the user already specified top/side/bottom, don't repeat the selection interview; explain genuine usability conflicts before offering viable alternatives.
6. **Persistent secondary navigation?** Does a project tree, document contents, repository object list or settings category need to coexist with global destinations?

Record decisions in `design-system/navigation-decision.json` following `assets/navigation-decision.schema.json`. An unselected Agent recommendation is `pending/unresolved`, **not confirmed**. Only explicit authority such as “decide the entire page design” grants `delegated`; permission to recolor is not permission to move navigation.

## 1 — Strategy map, not a rigid numeric formula

| Structure | Appropriate | Weak fit | Responsive responsibility |
| --- | --- | --- | --- |
| **Top only** | Brand site, portfolio, media portal; few broad peer destinations; preserve width for Hero/body | Many categories, persistent expanding subitems, labels crowd one row | At narrow widths use accessible Drawer or collapsible menu; not automatically only an unexplained hamburger |
| **Side only** | Desktop-first repository analytics, ERP/admin; several areas and frequent switching | Narrow phones, immersive photography/commerce, very few sections | Medium width may use labeled rail; narrow may use Drawer or bottom primary navigation |
| **Top + Side** | Workspace/multiproduct hierarchy: top handles global workspace, notifications/search; left manages current product's functions/tree | Repeating identical destinations in both, occupying fixed space with no distinct responsibilities | Keep global object/action at top; secondary navigation moves to Drawer |
| **Rail + Detail** | IDE, mail, files and knowledge base with two levels of object navigation, sufficient room | Unlabeled icons unclear; three columns crowd content | Provide text labels/disclosure; narrow view shows one level with return path |
| **Bottom navigation** | Primarily mobile, approximately **3–5** peer high-frequency destinations | Desktop brand site, too many items, action buttons masquerading as destinations | Safe area, keyboard, screen readers and gesture areas |
| **Adaptive side → bottom** | Desktop/mobile product with many desktop choices but 3–5 stable core mobile destinations | Copying 7–10 sidebar routes into 7–10 bottom buttons | Preserve route identity, order and selected state across breakpoints; other entries stay reachable in More/Drawer |
| **Top + Bottom** | Mobile product: top shows current object/search/back/alerts; bottom switches global destinations | Same set of destinations shown in both; top toolbar competes with bottom | Distinct responsibilities and keyboard clearance |
| **Side + bottom utility** | Desktop workspace with side nav plus a persistent contextual action/batch/media toolbar | Calling action buttons “bottom navigation”; triplicate routes on top/side/bottom | Bottom toolstrip belongs to task and can close/collapse without blocking content |

**“Sidebar plus bottom” has two different meanings:**
- **Adapt across devices:** desktop sidebar and mobile 3–5 core-destination bottom navigation; not duplicated simultaneously.
- **Coexist in one viewport:** sidebar navigates globally/within product; bottom is an **action/control strip** for playback, progress or batch operations. If bottom also navigates, it must represent a genuinely different context level, not duplicate routes.

No global top/side/bottom navigation is also possible in an immersive editor, checkout or focus-reading mode; keep Back, breadcrumb or transient navigation and a clear return/exit path.

## 2 — Real IA choices, not three skins of one component

Where structure is unresolved and materially affects UX, select **2–3 different primary IA candidates** from `assets/navigation-pattern-catalog.json` (e.g., Top only / Side only / Top + Side). Each explains:

- Ownership of **global navigation, product navigation, page Tabs and contextual actions**, number and names;
- First-screen desktop content, sidebar space cost where necessary, effects of scrolling/collapse;
- Exactly how narrow-screen navigation transforms, which destinations remain direct, where others go, and how back/navigation works;
- Product-specific benefits, costs and constraints; finalize only after actual user selection or explicit delegation.

Do **not** offer three variants where only icons, darkness or corner radius of the same sidebar changes. These are visual alternatives, **not navigation architecture**. `assets/navigation-layout-lab.html` is an original synthetic conceptual lab, not acceptance of a real user application.

## 3 — Cross-screen conservation of identity and state

- **Destination IDs remain stable:** `overview`, `issues`, `prs` retain their meaning across desktop/tablet/mobile. Do not silently rename or reorder at breakpoints. Non-core routes must still be available in Drawer/More when omitted from mobile bar.
- **Do not simultaneously show duplicate same-level navigation** in a viewport, e.g. the same Overview/Issue/PR list in both sidebar and bottom, unless specific usability evidence and a user-approved exception require it.
- **Tabs are not global route navigation:** Tabs select peer subviews in one page/object; use real links for global modules.
- **Bottom toolstrip is not bottom navigation:** Add/Delete/Apply/Save act on current context, not destinations.
- **Sticky and occlusion:** Verify sticky top, persistent side and fixed bottom layers, scrolling, short windows and safe-area to prevent covering focus or actual content.
- **Touch/accessibility:** Separate semantic `<nav aria-label="Primary navigation">` landmarks, `aria-current="page"` for real route, `aria-selected` for genuine Tabs, visible keyboard focus, Skip to main and distinct accessible names. Do not force application/menubar ARIA roles on ordinary site navigation for visual novelty.
- **State persistence:** Breakpoint changes/navigation must not clear filters, search, chart selection, drafts or active object without reason. Test history back/forward, deep links, orientation changes and resize.

## 4 — When to remove navigation

When top, left and bottom all show the same destinations, **define responsibility again first**. Removing navigation with no unique task value matters more than recoloring it. Apply `semantic-copy-hygiene.md` to redundant `WORKSPACE` and `NAVIGATION` eyebrow labels as well.

## 5 — Coordinate with approved color and design system

Navigation architecture and color are **independent decisions**. Choosing Side/Top/Bottom is not permission to reselect dark navy/blue-purple; inherit v6.6 user-approved brand/color decisions. Show proposed IA in neutral conceptual visuals. Record color in MASTER only when confirmed, inherited or explicitly delegated. Every pattern still needs a coherent Sidebar/Topbar/Main/Card/Chart whole-page visual relationship, typography and density.

## 6 — Bounded external references

- [IBM Carbon UI Shell](https://www.carbondesignsystem.com/building-blocks/core/patterns/global-header): Header only / Header + left panel, each navigation level with distinct responsibility. [Left panel guidance](https://www.carbondesignsystem.com/building-blocks/core/components/ui-shell-left-panel/guidelines) favors persistent side navigation for many or frequently switched secondary choices, not unlimited nesting.
- [Android responsive navigation](https://developer.android.com/develop/ui/views/layout/build-responsive-navigation): Available width and destination count influence bar/rail/drawer, not just device type.
- [Android layout/nav patterns](https://developer.android.com/design/ui/mobile/guides/layout-and-content/layout-and-nav-patterns): Mobile bottom bar commonly ~3–5 high-frequency peer destinations; Tabs select subordinate views in one context.
- [Apple HIG Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars) / [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars): Horizontal space and hierarchy affect sidebar/tab choice; adaptation varies by platform.
- [Microsoft NavigationView](https://learn.microsoft.com/windows/uwp/design/controls-and-patterns/navigationview): Top may fit a few peer sections, left may fit many; this is native WinUI experience, not a Web law.
- [Atlassian Navigation Layout](https://atlassian.design/components/navigation-system/layout): Global top and contextual side can coexist with clearly divided responsibility.
- [WAI Navigation landmarks](https://w3c.github.io/wai-website/ARIA/apg/practices/names-and-descriptions/): Distinct navigation regions require distinct accessible names.

These are principles and decision examples, **not absolute rules such as “six destinations require a sidebar.”** Real product tasks and usability evidence may outweigh example counts.
