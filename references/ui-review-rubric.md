# Visual and Component Acceptance Rubric (100 Points)

Applies to one page design, a component-system implementation, or a full-site visual refactor. **Check blockers before calculating the total.** Scores support consistent review; they do **not** replace the user's subjective visual acceptance.

## Score allocation

| Dimension | Maximum | Strong result | Common deduction |
| --- | ---: | --- | --- |
| **Component architecture and reuse** | **25** | Inventory inherited components, unified UI layer, complete APIs/states, pages compose rather than reimplement | Every page defines independent Buttons/Inputs and duplicates CSS |
| **Visual coherence** | **20** | Semantic tokens, justified radius hierarchy, shadows, spacing and theme | Inconsistent colors/radii/Button variants across routes |
| **Readability and contrast** | **15** | Scannable type hierarchy, text/control/focus contrast | Pale tiny text, gradients covering body copy |
| **Information hierarchy and whitespace** | **15** | Important actions stand out, density matches product, clear structure | Too many Cards, no focal point, useless blank areas, repetitive English eyebrows, marketing-style giant Hero on operational screens |
| **Interactions and states** | **10** | Clear hover/focus/disabled/loading/empty/error | Pseudo-buttons, invisible keyboard focus, errors conveyed only by a red border |
| **Responsiveness and theme modes** | **10** | Robust wide/narrow windows and light/dark when relevant | Overflow/cropping, crude inverse colors in dark theme |
| **Performance and visual restraint** | **5** | Motion with purpose, stable interactions, controlled cost | Endless animation, heavy blur, blocked workflows |
| **Total** | **100** | | |

## Score interpretation

- **90–100 — Excellent:** Visual quality and component engineering are reliable enough to serve as a baseline for subsequent team pages.
- **85–89 — Deliverable:** Main system complete and no blockers, with a few acceptable details still improvable.
- **70–84 — Needs corrections:** Visible inconsistencies or incomplete details; do not promote as a shared template yet.
- **Below 70 — Does not meet standard:** Return to Gate A/B for structural component and visual fixes.
- **Any blocker:** **Fail regardless of total score.**

## v6.21 — Product Fit precedes the visual score

**Decide product fit as a binary pass/fail before using the 100-point rubric.** The weighted dimensions remain unchanged; add these higher-priority preconditions:

| Product-task problem | Review method | Result |
| --- | --- | --- |
| A learning, consumer, creative or reading screen has no real core task, only generic admin KPIs | Inspect primary user journey, CTA and essential content | Structural FAIL; return to UX |
| Users cannot tell the next action or multiple peer entry points compete for primary importance | Examine IA and shortest task path | Structural FAIL |
| Redesign changes colors/icons/radii only, preserving the original task mismatch | Compare identical viewport/state before/after | Do **not** accept as experience redesign |
| User explicitly requested expressive or children's education design, but Agent forces gray-and-white and deletes emoji | Compare approved brand/content semantics | Does not meet requirements |
| A scoped Button fix changes confirmed navigation or branding without authorization | Compare task authorization | Scope violation |

See product-experience-routing-gate.md and progressive-visual-refinement-gate.md. **Do not award a high score to a core screen that cannot serve the user's task merely because Tokens, alignment and radii are consistent.** A static scan PASS is not real-page visual or business acceptance.

## Immediate blockers / veto conditions

1. Repeated control families still use unrelated Button/Input/Dialog implementations on different routes, causing substantial visual fragmentation.
2. Theme toggling or brand/palette choices make body text, important controls or focus rings difficult or impossible to perceive.
3. Key forms and actions fail or were broken by visual changes (fake save, broken navigation, missing validation/error feedback).
4. Core content remains invisible unless animation/remote CDN succeeds, or reduced-motion users cannot complete the workflow.
5. Critical content disappears, becomes occluded or cannot be operated at required target viewport sizes.
6. The product explicitly calls for native platform conventions, but visual styling destroys native controls or accessibility.

## Acceptance evidence template

~~~text
Project / page:
Visual direction / theme / density:
Inherited component inventory:
Shared components added or changed:
Affected pages:

Gate A (Tokens / Theme): PASS / FAIL
Gate B (Components): PASS / FAIL
Gate C (Screens & QA): PASS / FAIL
Score: components /25, coherence /20, readability /15, hierarchy /15, states /10, responsive /10, performance /5; total /100
Blockers: none / exact findings
Strong examples (screenshot/component/reason):
Weak examples (screenshot/component/violated rule/fix):
Tested viewports / modes:
Build / interaction / accessibility / performance tests:
Unverified cases:
Next recommendation:
~~~

## Reviewer requirements

- Source-only inspection **cannot substantiate an actual visual score of 98**. Useful evidence includes component-showcase screenshots and at least one actual business-page screenshot.
- Every deduction must point to a **specific Token, component or page** with a reproducible reason, not a vague adjective.
- One good theme does not eliminate errors: review both themes, interactive states and real information density.
- For admin/tools, additionally use page-header-antipatterns.md to review titles, semantic repetition, action placement and first-screen content. Count those defects under hierarchy/whitespace and readability, rather than excusing them because other dimensions look good.

## v6.3 — Navigation and frequent-component review

Review within the **original 100-point weights**, not another mechanical scoring scale. Sidebar checks include coherent palette steps, one primary selection signal, and a visual distinction between navigation and historical items. Record issues under visual coherence, hierarchy/whitespace and interactions/states.

Do **not** deduct points merely because there is a vertical Sidebar bar; first determine if it conveys genuine tree hierarchy, chapter navigation or timeline information. If selected items simultaneously carry a bright background, bright rail, glow and meaningless orange dot, require evidence of each cue's value and a new **actual screenshot** after removing duplicated emphasis.

For other controls, see workspace-component-refinement.md. Scores require real screen/state evidence; synthetic examples are not product acceptance.

## v6.4 — Structural failure outranks total score

On an Operate screen, a giant decorative gradient Hero or illustration may occupy most visual space while the important trend chart is empty and a bright insight Card replaces evidence. **First judge whether the user's task and data display are blocked**, rather than letting component reuse and consistent colors produce an excellent score.

Inspect actual structure, headings, primary actions, key data sources and empty states. Structural defects return to composition-first-design.md for comparisons of materially different arrangements; a theme change alone is not a fix.

Keep the 100-point rubric, but **whether the user's task is served is a prior condition**. Without actual screenshots or a runnable product, report hypotheses or static findings—not complete visual acceptance. Detailed critique in visual-critique-loop.md.

## v6.5 — Information and legibility outrank decoration density

Treat ornamental English labels, redundant subtitles, fake section numbers and developer jargon leaking into UI as hierarchy/whitespace problems. Include tiny unreadable KPI labels, chart axes/legends, sample sizes and data limitations in readability/contrast. **Do not give high scores for consistent radii/colors if users cannot read critical chart information.**

Review: Is the loudest H1 also the most valuable information? Can slogans be removed without harming a real task? Are axis labels, legends and sources legible on actual target hardware? Does 200% zoom crop content? Does a retained eyebrow serve valid brand, navigation or chapter purpose? No rendered browser screenshot means typography is not visually verified. See semantic-copy-hygiene.md and typography-hierarchy.md.

## v6.8 — Main task and content burden precede scoring

If an overview simultaneously shows the main task, a three-step tutorial, a feature directory and repetitive instructions, **content priority fails** even if the Cards and Buttons share perfect design Tokens. Ask whether each module belongs on this visit; where secondary information can be found; how first and return visits differ; and whether an overview and a real data-analysis detail deserve different densities.

Higher density can be good for analytical work **when charts, statuses, sample sizes, data sources and interactions remain readable**. Neither "fewer Cards" nor "40% empty space" earns a high score by itself. See page-density-and-content-priority.md.

## v6.9 — Alignment and reachability of final content are blockers

When independent left/right column stacking accidentally creates a misaligned next row on a data page, deduct hierarchy/layout points and recheck Grid even if shadows and colors are polished. This **does not** require equal-width/equal-height Cards everywhere.

If the final data record, interactive action or chart footnote remains invisible at the **actual maximum browser scroll position**, this is a high-priority blocker. One screenshot with a Card touching the window bottom cannot demonstrate whether scrolling works; mark **NOT TESTED**, not automatic PASS or confirmed FAIL. Final acceptance needs desktop/short-window/mobile-end screenshots where supported, plus fixed footer occlusion checks. Optional rendered tool: scripts/audit_rendered_layout.mjs.

## v6.10 — Comparison charts: missing data and plot collisions outweigh tidy Cards

For multi-object comparison, block acceptance when selected entities, legends, plotted series or table columns disagree without explanation; missing measurements are filled with zero; incomparable time windows/units produce an invented "winner"; or important chart labels overlap. Matching outer Card frames does not prove aligned Plot Areas, axes or legends.

Judge whether users can find meaningful differences quickly, not whether four neat Cards fill the screen. Static validators only assess data contracts; test real interactions/screenshots in browsers when feasible.

## v6.11 — Run-monitor information hierarchy and actual actions

For a task center, if status statistics consume most of the width, rows repeat useless stage explanations, or error causes/retry actions are hard to find, classify this as **information-architecture rework**, regardless of cohesive monochrome Cards and row spacing.

Higher-priority blockers include status counts disagreeing with the list, fake progress without a known denominator, unauthorized retry actions, unreachable final records and clicks without meaningful feedback. Mock screenshots or CI alone never prove **real API** acceptance. See task-center-run-monitor-design.md.
