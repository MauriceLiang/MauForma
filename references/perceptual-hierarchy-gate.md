# Perceptual Hierarchy Gate — Content Importance Comes Before Type Size

Applies to all Web page modes (Operate / Persuade / Read / Experience), frameworks and UI libraries. This gate does **not** mean “increase default font size.” It gives the information the user currently needs to understand, decide or act on enough visual salience. Every size range is a project-level choice, never a universal cross-product pixel mandate.

## 1. Prioritize from actual user tasks, not HTML tag names

Before choosing type size, weight, color or screen area, create a lightweight **Information Salience Map**:

| Level | Definition and test | Typical content | Treatment |
| --- | --- | --- | --- |
| **P0 — Decision focal point** | What must the user immediately understand or act on in this viewport? Without it, the primary task cannot be completed | Current project/product/article, key result, blocking error, primary CTA | Unmistakable focal priority through position, form, size and contrast; not necessarily the largest element |
| **P1 — Required to complete the task** | What must be checked immediately after P0? | Critical status, price and units, task row name, meaningful change, required form label, next action | Stable scan rhythm; usually body-sized or stronger, not automatically faint or tiny |
| **P2 — Supports comprehension** | Helps interpretation but should not displace the task | Secondary explanation, date, category, ordinary detail, relevant navigation | Less prominent but legible; grouped closely with the related information |
| **P3 — Low-frequency context** | Not primary but may be required for truthfulness, traceability or compliance | Data source, footnotes, update time, legal limits, secondary menu | Restrained if appropriate, **never unreadable, unreachable or removed solely due to lower priority** |

**Priority is not a numeric-value detector.** “7 pending” can be a small inline filter count; enlarge it only when it is the decision itself. A product price, article heading, error explanation or Save action may outweigh any number in a statistics card. Mandatory warnings cannot be hidden as P3. P0 does **not** mean the biggest H1: workspaces may prioritize the object/current state, while brand pages may prioritize a Hero.

## 2. Three checkable steps before composing the page

1. **Write the user's real question:** What is the first concrete question on this route? Distinguish new/returning, normal/error and desktop/mobile states when applicable.
2. **Inventory authentic information:** Give each visible text, number, action and status its P0–P3 priority, semantic role and actionable outcome. Remove redundant decoration before shrinking real information to fit.
3. **Rehearse the reading path:** Ignore brand color and shadows; inspect **first glance → second glance → action**. If the dominant feature is a useless huge heading, empty container or uniformly weak copy, fix information order first.

Use only necessary gradations: **most task areas need 2–3 clear major text levels**, with stronger specialized roles for genuinely important KPIs, Heroes or blocking errors. Hierarchy also comes from weight, position, contrast, spacing and rhythm; not only absolute font differences. Body copy must remain comfortable, and 11–12px must not become the site-wide default reading level. Dense specialist tables can offer density controls rather than permanently shrinking every value.

## 3. Project-specific typography contract

- Establish semantic typography tokens such as display, page-heading, section-heading, primary-content, body, supporting, caption, control and critical-value (rename to match the existing system), plus a **real usage map**. Measure actual fonts, CJK/Latin/mixed languages, font metrics, content lengths and supported viewports. A single screenshot cannot dictate site-wide pixel sizes.
- For every P0/P1 element verify that weight, contrast and scale distinguish it from adjacent P2/P3; the headline/metric must justify its footprint through **content value**, not ornament. Keep long values and units grouped and readable.
- Do not “fix” hierarchy by setting every text node to 18px or every number to 28px. At 200% text zoom, narrow screens, system-font fallback and long labels, prefer wrapping, responsive reflow and explicit disclosure rather than endless shrinking.
- Negotiate density **after** removing repeated content and useless outer panels. “One screen” is not a justification for sacrificing P0/P1 readability.
- Apply relevant WCAG 2.2 contrast and scaling checks. This guide sets no universal legal minimum pixel size and does not claim a static scanner proves WCAG compliance. Chart Canvas labels require inspecting actual rendering.

## 4. Same decision method, different results across four modes

| Mode | Likely P0 | Typical AI-generated failure | Better review question |
| --- | --- | --- | --- |
| **Operate** — workspace/data | Current object, actionable state/error, main task row | All text 12–13px; irrelevant giant H1 while task rows fade; every number is an oversized KPI Card | Can users scan task identity, failure cause and executable action without P1 being buried? |
| **Persuade** — marketing/commerce | Product claim, image/name, essential price/CTA | Giant Hero but tiny specs, price or purchase action; every control is a pill | Do expressive typography and the real conversion path coexist without hiding critical terms? |
| **Read** — docs/learning | Article theme, main argument, examples and learning task | Table of contents dominates body; body tiny and too wide; code/comments difficult to read | Does a stable heading–body–note hierarchy support long reading? |
| **Experience** — portfolio/interaction | Work/media or current narrative step; essential controls and exit | Control wall obscures artwork; labels shrink beyond recognition | Is the core experience perceivable while navigation and accessibility remain usable? |

Do not impose Operate's small radii, dense tables or number treatments on every mode. Inherit existing product design decisions rather than silently overriding them through generic advice.

## 5. Gates A/B/D — acceptance evidence

**Gate A (before design):** Identify P0/P1, the first three elements read, token-to-role mapping and likely long-content failures. A tiny isolated button fix does not require a new site-wide plan.

**Gate B (components):** Map salience into slots/variants (primary/secondary label, metric, empty/error, hint). Important text must not require temporary per-page CSS to become readable. Define boundaries for long Chinese and English copy, numbers/units, empty/loading/disabled and 200% scaling.

**Gate D (real screenshots):** Conduct a **three-second scan test** and record what the first glance actually captures and whether that matches the task; repeat without color (grayscale). Check supported desktop/narrow windows, light/dark modes, long content and 200% scaling. Static inference is `NOT VISUALLY VERIFIED`. Do not substitute a fabricated “visual hierarchy score 95” for evidence.

See `references/typography-hierarchy.md` for starting sizes, `references/component-craft-gate.md` for component decisions and `references/visual-qa.md` for acceptance.
