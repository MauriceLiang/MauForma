# High-Frequency Workspace Components — Refine Without Imposing Templates

Applies to **Operate / desktop workbenches** and frequently used product controls. Rejecting template-like visuals does **not** mean banning corners, Cards, colors or icons; determine whether they clarify actual hierarchy and tasks. Marketing/portfolio art direction follows separate rules and must not inherit workspace aesthetics as universal law.

| Component | Template-like failure | Better workspace strategy | Valid exception | Verify |
| --- | --- | --- | --- | --- |
| **Sidebar** | Strong selection fill + bright left bar + colored icon + glowing edge; Recent list duplicates same look | One dominant selected cue, distinct semantics for main navigation versus history objects | Real tree connectors, timeline tracks | Selected/hover/focus/recent item/narrow windows |
| **Topbar** | Huge gradient/glass header, redundant project title, too many icon Buttons | Clear page context, search/common actions, subtle separation aligned with content | Brand/immersive creative topbar | Sticky/scroll states, shadows, keyboard |
| **Card** | Every region a same-sized shadowed Card, nested Cards | Cards only for independent objects; related information grouped by heading/Grid/gaps | Product gallery and portfolio Cards | Interaction, necessity of surface and nesting |
| **Data table** | A floating Card for each row, colored pills in every column, heavy zebra stripes | Aligned columns/widths, simple headings, real sort/filter, quiet hover; colors only for business state | Specialist visual tables, mobile Cards | Long data, empty, selection, keyboard, overflow |
| **Tabs** | Each Tab simultaneously shows pill, underline, glow and icon emphasis | One dominant pill **or** underline, separate hover/focus | Secondary indicator encoding distinct meaning in approved art direction | Selected Tab, tabpanel association, Arrow navigation per primitive |
| **Search** | Huge gradient box, fake shortcut label, substitutes for all actions | Reasonable input, clear scope/results, real clear/shortcut | Search-first products/search engines | Empty, loading, no result, Escape, scope |
| **Split Pane** | Every panel casts shadow, bright resize rail, unbounded resizing | Fine splitter and actual handle/min/max, stable persisted layout | Professional editor needs more apparent drag handles | Bounds, keyboard resizing, collapse, narrow fallback, persistence |

## v6.17 — Choose semantic icons before polishing strokes

Icons in one Sidebar/Topbar/Toolbar must both express real features and form a coherent family. Follow `references/icon-art-direction-gate.md`: candidates must exist in the **installed version**, compare plausible symbols instead of mapping menu words to arbitrary icon names. Inspect silhouettes, negative space, detail density, line/fill family, and optical relation to text and Badge. Verify the **whole group in a real browser gallery**; identical CSS width/stroke does not prove matching appearance.

## v6.13 — Choose collection and surface structure before table skins

For run histories, orders, users and events, apply `references/surface-architecture-gate.md` first. Consider a **flat toolbar + table/rows** instead of one oversized rounded container enclosing filters, heading, header and every record. A single bounded Panel is still valid for an independent data scope/interaction; do not mechanically delete it. Truly independent item Cards may remain. Whatever the surface, short action labels and column widths must pass `references/control-geometry-gate.md`, not stack “View Details” character by character in a narrow cell.

## Shared decisions for colors and states

1. Derive a **neutral tonal scale** from the approved brand tokens, not several arbitrary blue-gray HEX values. In dark tools, the `page/sidebar/surface/hover/selected` luminance order must be explainable.
2. **Accent signals action priority, not decoration on every component**. Danger/warning/success may use independent semantic colors. If an orange dot accompanies blue selected, explain what status versus selection each means; otherwise remove the dot.
3. One main visual cue often suffices for one state. A second rail/glow/gradient on an already selected fill requires **independent meaning**. **If a rail is used, render it separately outside the current NavItem**, never as the item's colored border or on every navigation row (see `references/sidebar-selection-indicator-gate.md`). **Keyboard focus is a different state, not limited by the single-selected-cue rule.**
4. Give a Panel its own surface only when it supports an independent task; flat lists and document prose generally do not need nested containers.
5. Do not communicate states through color alone. Selection needs semantics, status needs text/hint, and important nontext edges/focus require contrast.
6. In screenshots, remove brand blue/purple/orange mentally: are primary tasks still apparent? If all hierarchy relies on arbitrary color/rails, the information architecture is weak.

## Turn vague comments into actionable review

Code reviews should record: visual region, current state signal, business meaning, conflicting reason, viable alternative, shared component/token owner, applicable exception and actual browser verification status.

### QA checklist

- Do active/hover/focus differ in actual light/dark sidebar screenshots?
- Can users recognize distinct roles of main nav, recent objects and help in three seconds?
- Are multiple elements simultaneously emphasized as “selected” without explaining their meanings?
- Do colors have roles and hierarchy? Low saturation is **not** low contrast; are text, icon and focus borders legible?
- Do Tabs, Search, Data Table and Split Pane **work**, or only look polished?
- Which bold designs remain justified by this particular product? Explain instead of treating all “AI style” as objectively wrong.

More sidebar rules: `references/sidebar-navigation-design.md`; synthetic comparison: `assets/sidebar-refinement-gallery.html`.
