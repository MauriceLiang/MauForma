# Typography Hierarchy — Type Size, Weight, Leading, and Readability First

> v6.5 example: A huge abstract title combined with tiny section indices, chart axes and notes, plus visually weak key metrics, produces the wrong proportions. The answer is not to make everything 14px; **actual task importance determines type scale**.

## v6.12 prerequisite — Perceptual Hierarchy Gate first

**Read `references/perceptual-hierarchy-gate.md` before using the size table.** Determine the real P0–P3 reading/task priorities and the path **first glance → second glance → action**. Whether a number, heading, error or body paragraph deserves emphasis depends on user intent, not whether it happens to be a number, column label or gray text.

The older Operate and Persuade figures below are **project starting points**, not universal rules. Read and Experience modes require their own criteria. If critical list rows, body, price or error copy is buried at 12–13px, it fails hierarchy QA **even if each item passes a static tiny-text lower-bound test**. Conversely, enlarging every number or all text indiscriminately also fails. For weight, baseline and state coordination, see `references/component-craft-gate.md`.

## Choose purpose first, size second

Identify `Operate / Persuade / Read / Experience`, then construct a **role-driven type system**. The table is an *optional starting point for desktop workspaces* in CSS pixels—not a WCAG-recommended type scale or a fixed cross-device requirement. Font metrics, zoom, language and viewport may require different values.

| Role | Suggested range | Common start | Suggested weight / line height | Information purpose |
| --- | --- | --- | --- | --- |
| Page title / H1 | **22–30px** | 26px | 600–700 / 1.25–1.35 | Orient the user, not make an operational page a poster |
| Section title / H2 | **16–20px** | 18px | 600–650 / 1.35–1.45 | Separate genuine task regions |
| Body / key explanation | **14–16px** | 15px | 400–500 / 1.55–1.7 | Read important information as prose, not as a footnote |
| Navigation / link | **13–16px** | 14px | 500–600 / 1.4–1.6 | Frequently scanned routes |
| KPI value | **22–32px** | 26px | 600–700 / 1.1–1.3 | Meaningful figures ahead of decoration |
| KPI label / secondary data | **12–14px** | 13px | 400–550 / 1.45–1.6 | Explain metrics legibly |
| Chart axes / legend | **12–14px** | 13px | 400–500 / 1.4–1.55 | Real time/value/series content |
| Metadata / source / sample | **12–14px** | 13px | 400–500 / 1.5–1.6 | Secondary but legible; sampling, n and UTC must not disappear |
| Button / control label | **13–16px** | 14px | 500–600 / 1.35–1.5 | Action clarity and usable control dimensions |

**A suggested range is not a mandatory accessibility font-size minimum.** Very small labels are not categorically forbidden, but text containing important business information should use an appropriately stronger role, contrast and scalable layout. Do not make 10–11px the default for explanations and chart axes. Dense professional tables can provide a user density setting while retaining a readable mode.

## Hierarchy is not achieved through extreme type sizes

- Prefer **one clear H1** per task page and **2–3 main text levels** for a usable reading path. Do not default to a 40–60px declaration over a workbench with 10px axes.
- **Relative salience:** If a giant heading is several times larger than real content, question whether it deserves the viewport. This ratio is *not* a universal threshold. A genuinely important KPI may be larger than body text; every KPI need not be enormous.
- **Metric labels stay adjacent:** For a metric like “3.4 days” with “Issue close P50,” keep context readable and nearby; `n=198` is a real coverage limitation, not decorative fine print.
- Do not make real chart coordinates, legends or tooltips illegible to save space. On smaller charts first reduce tick count, adjust layout, enable appropriate scrolling or wrapping—do not shrink type without limit.
- Weight supports task hierarchy. Body often uses 400–500, headings and necessary emphasis 600–700. Do not bold every paragraph or fade everything to uniform gray. Avoid arbitrary wide letter spacing on Chinese CJK labels, such as `letter-spacing:.16em`.
- Test mixed Chinese/English/numeral widths, thousands separators, decimals and units. Date ranges, repo names and long IDs need intentional wrapping/truncation with tooltip or full-value access, not microscopic fonts just to prevent wraps.
- Match line height to role: dense numeric values can be tighter; body copy needs breathing room. Avoid the combination of tight line height and low contrast for long CJK text. Desktop navigation and chart axes need density **and** clarity.

## Page-level priority scan

Mark attention in actual task order:

1. Current object and page purpose;
2. Most actionable data or evidence;
3. Available trends/detail and corresponding chart labels;
4. Supporting source, methodology and constraints.

A vague “See how projects evolve” slogan should not overpower the true project identity, data and trends. Decorative `01 / Overview` and `ANALYSIS STUDIO` layers should not manufacture a hierarchy of their own.

## WCAG 2.2 requirements — distinguish standards from suggestions

The following are relevant **WCAG 2.2 AA** checks, **not** recommended fixed pixel sizes:

- Normal text and images of text generally require at least **4.5:1** contrast; text qualifying as large-scale may use **3:1**. Passing contrast alone does not make 10px fine print comfortable.
- Except for applicable exceptions, text resized to **200%** must not lose content or functionality.
- **Text Spacing 1.4.12** addresses user overrides of line spacing and related properties without loss of content/functionality. It does **not** require every initial CSS rule to use 1.5 leading or 0.12em letter spacing. Evaluate Chinese text according to applicable writing and layout properties.
- Important chart axes, legends and sample explanations are not decoration to exclude from readability review; contrast should be tested against their actual rendered backgrounds. For Canvas charts, examine actual drawing, device pixel ratio and browser scaling, not CSS alone.
- Do not claim WCAG conformance based only on static token checks; verify rendered contrast, focus, zoom and high-contrast contexts.

Official: https://www.w3.org/TR/WCAG22/#contrast-minimum , https://www.w3.org/TR/WCAG22/#resize-text , https://www.w3.org/TR/WCAG22/#text-spacing .

## Why “make everything larger” also fails

- **Persuade:** A launch, photography or branding page may use artistic 48–80px+ type; descriptions, price, CTA and material legal constraints must still be legible.
- **Read:** Long text requires comfortable measure and leading, not tiny high-density admin text.
- **Operate:** Dense charts/tables are valid, but dense content does **not** mean every font is 11px. Remove repetitive filler before reducing important text.
- **Experience:** Media/art can dominate while secondary tool labels retreat, but necessary controls remain readable.

Starting roles live in `assets/typography-role-guidelines.json`. This helps Agents choose and review roles; it is not a theme to force-install into users' projects and does not prove visual quality automatically.

## Gate D — Typography acceptance

- Check real proportions and scan order **H1 → H2 → body → metrics → chart ticks/legend** at the supported desktop width and any supported phone/narrow-window layout.
- Test **100% and 200%** text zoom, long Chinese, English repo names, numbers/units, user font overrides and dark mode. Use scalable `rem/em` or equivalent techniques so zoom does not clip content.
- Flag `too large` (overshadows tasks), `too small` (uncomfortable on real device), `duplicate` (no extra meaning), `low contrast` and `zoom clipping`.
- Inspect **actual chart rendering**. ECharts/Chart.js configuration alone does not prove axes are readable.
- Without a real-browser run, report **static recommendations** rather than claiming acceptance on an actual screen.

`assets/typography-reading-lab.html` is a synthetic demonstration, not the user's product source. For copy necessity, see `references/semantic-copy-hygiene.md`.
