# Sidebar Color Reference Study — Real Design Sources and Transferable Reasoning

This document records inspected official design guides and product design explanations. **Extract the reasons and mechanisms, not the interface itself or supposedly exact brand HEX values.** MauForma's included example palettes are original concepts, not official brand themes.

| Reference | Original source | Transferable idea | Appropriate contexts | Do not copy |
| --- | --- | --- | --- | --- |
| **Linear** | [2024 UI redesign](https://linear.app/now/how-we-redesigned-the-linear-ui) / [subsequent navigation-noise discussion](https://linear.app/now/behind-the-latest-design-refresh) | Sidebar does not compete with main content; choose density and contrast before decoration; background/accent/contrast form one theme | Tasks/projects, developer tools, dense workbenches | Do not conclude that Linear's dark gray is best for every site |
| **IBM Carbon** | [UI Shell left panel](https://www.carbondesignsystem.com/building-blocks/core/components/ui-shell-left-panel/specifications) / [selected colors](https://www.carbondesignsystem.com/building-blocks/foundations/color/overview) | Separate enabled, hover, active, focus semantic tokens; express selection through background + text/icon hierarchy | Enterprise administration and complex navigation | Do not transplant IBM's token values as the user's brand color |
| **GitHub Primer** | [Layout](https://primer.style/product/getting-started/foundations/layout/) / [Color usage](https://primer.style/product/getting-started/foundations/color-usage/) | Sidebar supports main content and split pages; semantic colors across light/dark and responsive layouts | Repository/code analysis, knowledge/list/detail systems | Do not copy GitHub UI onto an illustrative product |
| **shadcn/ui** | [Sidebar theming](https://ui.shadcn.com/docs/components/base/sidebar) | Independent background, foreground, primary, accent, border and ring roles for sidebar, coordinated with the whole theme | Component-based React/Vue projects and reusable theme strategies | Sample shadcn colors are not the user's selected brand |
| **Atlassian Design** | [Design tokens](https://atlassian.design/components/tokens/all-tokens) | One token source; selected need not be blue and can use calm neutral treatments | Enterprise collaboration, project boards, multi-theme apps | Do not describe a feature-flagged treatment as Atlassian's sole permanent design |

## Recommend only combinations with explainable project fit

For a hypothetical repository-analysis workbench with a large sidebar, dense charts and an established blue logo, possible comparisons include:

- **Graphite sidebar + cool-white main:** Stronger region boundary, focal point in the main data area; fits those preferring dark navigation and light content. Keep the real logo blue, but do not make every state blue.
- **Light-gray sidebar + white main:** Lighter unified tonal system for prolonged reading, search and chart comparison. Verify gray contrast; paler is not always better.
- **Full dark neutral workbench:** Sidebar slightly darker than main, for users deliberately preferring dark mode. Chart and supporting-label contrast needs separate testing.
- **Warm paper white + sandstone sidebar:** Could suit truly warm brands, research or knowledge reading; do not force into an established cool brand.
- **Keep brand blue:** Preserve blue when selected by the user or inherited from a mature brand system; constrain colored area and status roles, rather than reflexively rejecting blue.

These are **not official copies of those brands**, but optional MauForma compositions informed by their principles. Distinguish clearly: **the reference offers reasoning; the user decides final colors.**

## Evidence levels when learning from a site screenshot

- **verified_official_documentation:** Mechanism stated by official documentation, cited to the exact source.
- **observed_ui:** Interface actually observed in a given date/theme; record screenshot, date and light/dark setting.
- **mauforma_interpretation:** Original palette inferred from more than one design system; never label as “Linear official palette.”
- **unverified:** Documentation not read, screenshot not observed or current version uncertain; do not invent brand palettes.

When the user has not chosen a reference site, select only 2–3 relevant cases rather than presenting ten sites as a directionless trend collage.
