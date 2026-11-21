# Semantic Copy Hygiene — Necessity and Information Roles

This gate asks whether visible copy adds **real information** on every kind of Web page; it is not a recap of one project's screenshots. Operate and Read contexts commonly prioritize task and data clarity. Brand, marketing and creative contexts can preserve supporting language with a genuine narrative function.

## Synthetic counterexamples and appropriate handling

| Fictional UI copy | Issue | Appropriate action |
| --- | --- | --- |
| \`INSIGHT AREA\` below a logo | No confirmed sub-brand; pure decoration | Remove; genuine official brand sub-labels are an exception |
| \`Content analytics · interactive prototype\` | Development-phase information leaked into product ornament | If samples really are being used, show a truthful “Demo data” state instead |
| \`See the power of change\` as a giant H1 | An operational user cannot identify the task | Name the actual object/task; a marketing home may retain a confirmed brand promise |
| \`01 / Overview\` plus a navigation item with the same meaning | Decorative index duplicates actual navigation | Keep the useful title; a real chapter index remains valid |
| \`Chart retains native tooltip\` | Developer implementation detail, not useful product-facing copy | Move to technical documentation or say “Hover to inspect data” only if genuinely supported |
| Every card repeats \`Demo data\` | Important state becomes noisy when needlessly repeated | Give a clear page-level indicator; keep local warnings where data interpretation requires them |

The examples are original, generic test scenarios, not actual user product material.

## Universal title-copy gate — inherited content is not exempt

When creating, polishing, refactoring or reviewing **any page type**, inspect both inherited and newly introduced pre-H1/hero eyebrow, overline, kicker, Chinese/English/mixed-language prefix, wide-tracking label and ornamental number. Resolve each by \`keep / merge / move / delete\` according to authentic navigation, identity, status, real chapter structure, incremental information or approved brand narrative. “It was there before,” a color change, or a font-size tweak does not excuse a redundant prefix.

Operational pages must not generate or retain explanatory decorative title prefixes. Learning, scientific, reading, marketing, brand and creative pages must also remove *functionless* prefixes, but actual event slogans, chapter numbers and evidenced narrative kickers are not automatically invalid. Split a line combining a genuine brand and generic functional description: preserve the identity in the brand area; remove the redundant text. Put dates, scope, sources, permission and data states near the relevant filters/charts/actions. Put necessary incremental help below the title or next to the corresponding task. See \`references/page-header-antipatterns.md\`, H-Base/H0.

## Title prefix versus real section heading: classify the relationship first

\`references/title-prefix-role-gate.md\` covers all pages and title groups (H1–H6, Card/Section/Dialog, etc.). Whether a line is a title preamble depends on its **structural relationship** to the next title—not on blue versus black, size, weight, letter spacing, language, CSS class or element tag.

Make three separate decisions: (1) find independent preceding text within each title group, including old components and defaults; (2) classify as decoration, real navigation, chapter/step, state, source, brand, independent heading or explanatory copy; (3) even if the text is valuable, decide **independently** whether it belongs in a separate pre-title line. Prefer breadcrumb, stepper, legend, status, below-title description or other appropriate role where applicable. “Meaningful copy” does not automatically justify an ornamental pretitle. Inspect actual rendering and old content.

Static and DOM scans supply **candidates only**. Agents must decide semantics. Never bulk-delete legitimate chapter headings based on appearance.

## Four tests of necessity

1. **Added value:** Would deleting the text lose navigation, identity, status, data scope, source, constraint or brand meaning? Delete words that exist solely to look “premium.”
2. **Duplicated role:** Does it repeat an H1, navigation, breadcrumb, Tab or Card heading? Actual breadcrumb terminal items may validly match a page heading.
3. **Audience:** Is it user-facing information, or a developer note, internal component implementation or Mock terminology?
4. **Page intent:** Reading pages may use chapters, marketing pages may use narrative slogans; operating pages usually need objects, tasks and actions.

Use \`keep / merge / move / delete\` with a short explanation where useful; do not require a formal table for every string.

## Semantic heading roles

- **Product/page identity:** Show real product names and confirmed sub-brand phrases; do not generate generic English slogans.
- **Main heading:** State the actual task, content or brand meaning. Do not arbitrarily inflate or minimize its font size; operational pages do not auto-generate pre-H1 explanatory layers.
- **Section heading:** Introduce information distinct from adjacent content. Chart headings must name actual data.
- **Supporting copy:** Clarify units, sample sizes, time zones, coverage, uncertainty, loading/permission states and other real constraints.
- **Index and breadcrumb:** Only for genuine order or navigation, never invented numbers per paragraph.
- **Bilingual/technical terms:** Retain translated or English duplicates only when the product language strategy, proper noun or a demonstrable user benefit requires them.

## Container-level content audit

Each sentence may be meaningful yet the entire container may be out of place. First classify sections as \`primary/supporting/conditional/deferred/removable\` under \`references/page-density-and-content-priority.md\`. A first-use tutorial need not permanently occupy a familiar task overview; a repeated feature index must not displace core workflows. Maintain a discoverable route to relocated content. **Never discard important data limitations simply to increase whitespace.**

## Verification

- Real data sources, actual states and functional guidance are useful information, not decoration to remove.
- Read actual page copy before deciding. Include historical and added content and a before/after comparison; never batch-delete from a keyword search.
- \`scripts/audit_readability.py <src> --format json\` gives review hints, not an objective verdict about decorative titles.
- Recheck rendered heading hierarchy, mixed-language content, chart sources and help copy. If not executed, report \`NOT TESTED\`.

Related: \`references/typography-hierarchy.md\`, \`references/page-header-antipatterns.md\`, \`references/visual-critique-loop.md\`.
