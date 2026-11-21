# Palette Art Direction — Color Needs a Source and a Role

## The problem is not “no blue or purple”; it is unexamined generic SaaS blue-purple choices

Synthetic counterexample: A page combines highly saturated Hero media, sidebar accents and bright KPI highlights with no explanation for each color's product or brand function. It lacks coherent reasoning; **the solution is not automatically black and white**.

## Derive palette choices from content — answer five questions first

1. **Brand:** What confirmed logo/primary colors, history, audience perception and user color preferences exist? Preserve approved choices.
2. **Content character:** Data tools prioritize legibility/credibility, food may need authentic photographic warmth, and art may warrant charged contrast.
3. **Reading context:** Light/dark preference, long sessions, density, device/screen, near-color contrast and color-vision distinguishability.
4. **Functional roles:** Canvas and surface layers, main/support text, primary actions/links, success/warning/error, and distinct data series.
5. **Differentiation:** Would this palette still look exactly the same if all copy became a generic SaaS product? What actual subject-specific clue warrants it?

The Agent must record a **palette rationale** and check whether the brand color is already settled **before** proposing colors. **The final palette belongs to the user's decision.** If the user has given a color or HEX, use it without asking them to choose again; design supporting colors around it. Running a palette-generation tool does not authorize adoption.

## Suggested atmospheres — not compulsory brand tokens

| Mood | Fit and reasoning | Potential limitation |
| --- | --- | --- |
| Warm graphite | Dark neutral with restrained copper/moss accent, tool-like and suitable for extended viewing; developer/analysis workbench candidate | Too subdued for a lively brand |
| Paper & ink | Ivory/deep ink, precise type and low-noise statuses; reports, reading and dense information | Without hierarchy it looks like a plain document |
| Mineral | Natural green, stone white and charcoal; environment, education, research and selected tools | Blindly applying green creates another generic template |
| Bold editorial | High-contrast black/white with one clear identity accent; brand, creative portfolios, content | Needs careful coordination with photography, type and composition |
| Brand inheritance | Preserve approved blue/purple/pink/orange and complete roles around it | A known accent does not mean every Card should be filled with it |

**Do not replace the blue-purple cliché with an equally compulsory moss-green/brown cliché.** MauForma recommends based on evidence, not a new universal default.

## An evidenced palette does not require showing three themes

Establish **one complete semantic system** in MASTER:

- **Neutral:** page/sidebar/panel/hover/selected, without unrelated colors for main versus sidebar.
- **Text:** heading/body/muted/link. Meaningful data cannot be relegated to almost-white faint small text.
- **Action:** primary CTA, secondary and focus. Accent communicates importance, not an invitation to color everything.
- **Semantic:** success/warning/danger/information, separate from data series colors.
- **Charts:** Category colors have stable meaning; green does not automatically mean good or red bad. Curves/bars require accessible legends or labels.
- **Accessibility:** Normal text aims for 4.5:1; important nontext controls/focus for 3:1 as applicable. Test actual overlays/transparency.

## Three signals of failed palette logic

- **Competing primary colors:** Several big saturated regions demand focus without distinct primary versus semantic roles.
- **Decorative image/color overwhelms task:** Large colorful 3D decoration is more salient than actual trend charts in Operate.
- **Recoloring without composition:** Generic Hero + Cards + insight text still dominates after swapping blue→green or purple→orange.

Repair in this order: **composition → area/type hierarchy → semantic color roles → exact palette values → real-browser validation**. Not the reverse.

## Exceptions and decision provenance

A confirmed user brand color/reference outranks other directions (`confirmed`). Explicit autonomous authority is `delegated` with reasons; an inherited product design is `inherited`. Anything unresolved is **not** user-confirmed. Individual status dots and chart series require genuine meaning too.

See `references/theme-design.md` and `references/sidebar-navigation-design.md` for technical token implementation. This file instead answers **why this color atmosphere was selected**.

## Separate the right to recommend from the right to decide

Any user-specified color outranks Agent preference. If the user dislikes a dark-blue sidebar but has not selected another, inspect [Sidebar Color Discovery](sidebar-color-discovery.md) and [Design Reference Cases](sidebar-color-reference-cases.md), then present **2–3 distinct whole-page combinations** with comparison, reasons and tradeoffs. **Recommended ≠ confirmed:** leave `pending/unresolved` until selected. Only explicit delegation permits the Agent to choose independently.

Keep user-supplied HEX unchanged; fix surrounding colors and explain any legibility tradeoffs rather than silently changing a fixed value. Real implementation checks Sidebar/Topbar/Main/Card/Chart color temperatures, hierarchy, data meaning and state contrast. New example palettes are original MauForma concepts, **not official Linear/GitHub brand colors**.
