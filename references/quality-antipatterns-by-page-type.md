# Cross-Product Web UI Anti-Pattern Catalog — With Valid Exceptions

## Decide by purpose, not by banning visual techniques

**An anti-pattern is not inherently a particular color, CSS value, component or animation.** It is a pattern without information value or user-task justification, or one that damages usability and coherence. For each observed flaw report its **actual location, impact, replacement and verification**, not an aesthetic slogan.

| # | Bad pattern | Why it fails | Better approach | Valid exception |
| --- | --- | --- | --- | --- |
| 1 | Functional H1 preceded by generic "Accounts & Access" microheading | Duplicates meaning without navigation value | Compact PageHeader, one H1 plus necessary explanation | Real breadcrumb |
| 2 | Meaningless English label on a Chinese operational page | USER MANAGEMENT above its exact Chinese translation wastes space | Consistent product locale, explain genuine terms | Multilingual app or official English brand |
| 3 | 80px Hero on an operational screen | Pushes the primary action below the fold | About 24–32px compact title as an illustrative starting range | Marketing site's main Hero |
| 4 | "Make management efficient" slogan repeated on every route | Generic and noninformative | Actual permission boundaries, filters or data context | Confirmed brand promise on product home |
| 5 | Five nested Cards | Eats space and obscures hierarchy | Organize via headings, spacing, separators and meaningful surfaces | A real complex interactive nested object |
| 6 | Every Button filled with primary accent | No visible action priority | One primary, others secondary/ghost/danger | Two genuinely parallel primary flows with explanation |
| 7 | 32px radius everywhere | Wrong proportions in dense data/forms | Radius scale appropriate to density/containment | Strong approved creative brand direction |
| 8 | Meaningless icons/emoji everywhere | Cognitive burden and inconsistent vocabulary | One icon family, icons for real action/status | Legitimate playful/children's content |
| 9 | Several competing saturated gradients | Content loses the focal point | Semantic colors and restrained accents | Art/event experiences with deliberate gradients |
| 10 | A beautiful but static Mock called complete | Real actions unavailable | Real pending/error/empty/permission/success flows | Explicitly labeled static design mock |
| 11 | 700ms fly-in animation for every list item | Slow scanning and scrolling | Brief/no entrances for routine data | Slower portfolio entrances may be justified |
| 12 | Content only appears if animation/CDN succeeds | Accessibility/business failure | Visible content by default, progressively enhanced | None |
| 13 | Motion and Anime.js animate the same property on one element | Competing CSS/transform ownership | One animation owner per property | Different subelements/properties have independent owners |
| 14 | Multiple independent styled UI suites | Divergent Buttons/Fields and interaction states | One primary styled system plus scoped additions | Planned and bounded gradual migration |
| 15 | Huge data table without filter/paging/empty states | Hard to locate and work with data | Real toolbar, paging and state feedback | Tiny static table |
| 16 | Mobile webpage hides core work | Users cannot complete task | Responsive task-preserving layout | Explicit desktop-only support, not fake mobile compatibility |
| 17 | React components pasted directly into Vue | Compile/runtime breakage | Framework-specific component and adapter | None |
| 18 | No reduced-motion path | Motion-sensitive users lose access | prefers-reduced-motion or controllable loop | None |
| 19 | Charts omit units or use misleading truncated axes | Wrong interpretation | Units, range, labels, source | Specialized analysis with explicit disclosure |
| 20 | Pretty components replace keyboard behavior | Mouse-only interaction | Semantics, ARIA, keyboard/focus and proven primitives | None |
| 21 | Excess Magic UI/Aceternity effects | Large bundle and attention theft | A few approved brand-fit effects | Art experiments/portfolio showcase |
| 22 | Stable existing controls rebuilt merely for looks | Doubles maintenance and diverges behavior | Adapt inherited theme/variants first | Real severe accessibility failure may justify replacement |
| 23 | One nav selected item has bright fill, attached bar, glow and highlighted icon | Duplicated emphasis, generic template appearance | One clear primary selected signal; separate keyboard focus | Real tree hierarchy/chapter/timeline information |
| 24 | "Recently opened" objects share the strongest main-route selected style | Current route and historical object become confused | Quieter Recent selection with accurate object context | Current object actually is the sole workspace destination |
| 25 | Dark blue sidebar plus blue fill, cyan rail and unexplained orange dot | Competing cues and unclear status | Coherent neutrals, primary accent and separate semantic states | Actual warning/failure/unread with explanatory meaning |
| 26 | Topbar, Cards and Tabs all have shadows, gradients and ornaments | Everything competes for equal attention | Task context/hierarchy owns boundaries and emphasis | Brand creative narratives with approved direction |
| 27 | Every table row floats as a Card or every cell becomes a colored badge | Harms scan/comparison density | Aligned tabular data, color only for meaningful states | Mobile table-to-card transformation when justified |
| 28 | Selected Tab combines pill, bottom rail and neon ring | Redundant selection cues | One primary selected mechanism, pill OR underline; separate keyboard focus | Two cues represent genuinely different information |
| 29 | Fake Search keyboard shortcut and decorative-only split handle | Functions not actually operable | Search scope/clear/results; split keyboard controls and min size | Explicit static mock, never called complete |

## v6.5 — Repeated copy and typography issues

| # | Anti-pattern | Why | Better approach | Exception |
| --- | --- | --- | --- | --- |
| 30 | Auto-generate ANALYSIS STUDIO below brand | Unofficial English microcopy invents hierarchy | Actual product identity or confirmed subbrand | Genuine tagline/multilingual product line |
| 31 | Generic collaboration pretitle plus giant abstract H1 | Repeats category, hides real task | Functional PageTitle grounded in object | Marketing may need narrative |
| 32 | Add 01 / Overview to every Section | Number is neither a step nor chapter | Direct functional Section title | Real content directory or numbered process |
| 33 | Display ECharts Tooltip implementation terms to end users | Leaks developer implementation into product UI | Truthful instructions users can act on | Developer/debug tutorial |
| 34 | 40–60px generic motto plus tiny chart tick/sample n | Critical information becomes unreadable | Role-based typography and legible data labels | Brand Hero may be big but data must remain readable |
| 35 | Fade sources, UTC and sample limitations into tiny pale text | Hides essential context | Readable contrast, zoom and meaningful metadata role | Truly decorative in-image copy may be removed |

Static typography scripts provide **review candidates only**, not a verdict that all small text or English labels are wrong. See semantic-copy-hygiene.md and typography-hierarchy.md.

## Recommended review format

| Region | Severity | Bad implementation | Replacement | Component owner | Verification |
| --- | --- | --- | --- | --- | --- |
| Account page header | P2 | Microheading + enormous H1 | Compact shared PageHeader | components/composites/PageHeader | Desktop/mobile screenshots, primary action in first screen |
| Confirmation dialogs | P1 | Independent div modal engines | One accessible Dialog | components/ui/Dialog | Tab/Escape/focus return/screen reader |
| Table-row hover | P3 | Heavy shadow and bounce | Brief border/color change | components/ui/Table | Hover/touch/low-powered device |

Detailed operational PageHeader examples: page-header-antipatterns.md and assets/page-header-antipattern-gallery.html.

**v6.3:** For patterns #23–29, see sidebar-navigation-design.md, workspace-component-refinement.md and assets/sidebar-refinement-gallery.html. A CSS border-left alone cannot prove a page was AI-generated or that its navigation is invalid.

## v6.8 — Whitespace and page-density anti-patterns

| Anti-pattern | Why | Corrective approach | Valid exception |
| --- | --- | --- | --- |
| Overview shows "Start from repository", three-step tutorial and three feature Cards | All entrances compete, core task unclear | Current object + one primary action; tutorial on first visit/help; features in navigation | A real educational portal may expose its complete learning pathway |
| Sidebar already has features, home duplicates all as Cards | Redundant content without additional information | Remove/defer duplications; keep genuine high-value summary | Cards contain unique data or direct current task |
| Increase each Card padding only | Page length grows but information burden remains | Prioritize, remove redundant wrappers, then tune layout | Necessary concurrent content may warrant a larger viewport/restructuring |
| Detailed analytics becomes giant empty spacious layout | Metrics/charts cannot be compared | Productive/Compact density, with readable labels | Explicit loading/empty state while data pending |
| Tiny low-contrast type used for density | Hides content | Reduce duplication/group content without sacrificing source, legend and sample size | Pure ornament may be deleted |
| Card inside Card inside giant Card | Borders consume space and confuse hierarchy | Remove surfaces one by one using necessity test | Real nested objects and interactions justify boundaries |
| Huge fixed min-height manufactures premium whitespace | Blank area conveys no relationship, delays main task | Task-driven Macro/Meso/Micro spacing | Large visual Hero may be justified by brand story |

See page-density-and-content-priority.md and whitespace-and-surface-composition.md. **No rigid card-count or blank-space percentage limit applies.**

## v6.9 — Alignment and scroll-end safety anti-patterns

| Anti-pattern | Why it fails | Fix | Valid exception |
| --- | --- | --- | --- |
| Left/right charts stack independently and second row starts misaligned | Peer modules lack shared row identity | Grid rows/areas or full-row key chart | Photo Masonry or intentional editorial composition |
| Every row randomly uses 6:4 / 1:1 / 7:5 without reason | Column tracks are not understandable | Explicit grid contract and purposeful spans | Distinct-content zones with different roles |
| Tall empty Card to align heights | False whitespace distorts content | Recompose, allow natural heights/major chart full row | Plot itself needs a specified height |
| 100vh with overflow:hidden prevents scroll | Last records/actions/chart axes unreachable | Normal document scroll or explicit app-shell scroll owner | True immersive one-screen app **with every item reachable** |
| Fixed action footer occludes last row | Final control remains blocked even at maximum scroll | Reserve true footer height plus safe area in the actual scroller | Footer belongs in normal document flow |
| Screenshot touches viewport bottom, reviewer assumes bug | Screenshot is not scroll-end evidence | Mark candidate and test actual maximum scroll | Actual hard clipping clearly visible supports a provisional risk |
| Shrink charts/delete data to make everything fit first screen | Destroys comparison and source context | Keep legible and permit vertical scroll | Genuine single-screen KPI product may deliberately reduce scope |

See grid-alignment-and-viewport-safety.md.

## v6.10 — Comparison and chart-internal anti-patterns

| Anti-pattern | Problem | Corrective action | Valid exception |
| --- | --- | --- | --- |
| Two outer chart Cards aligned but one plot axis sits lower and the other has blank padding | Card geometry does not imply plot alignment | Audit Plot Region / Axis / Legend; adjust chart type/composition if needed | Different chart semantics do not require identical plot-height |
| Adjacent scatter point label and average marker overlap | Data and conclusion unreadable | Label collision avoidance, tooltip, selective annotations, reposition or redesign | Truly decorative labels can be removed |
| Three repositories selected, three legends but only one series visible without explanation | Missing/hidden/overlapping/loading ambiguity | Synchronize series to IDs, disclose missing data, never silently impute zeros | Real identical series may use differing markers/Tooltip |
| Comparison selector Sidebar consumes most horizontal space, results are verbose Cards | Selecting objects dominates discovering differences | Selected object strip that stays editable; main area for comparative evidence | Real high-dimensional advanced filters may justify sidebar |
| Giant empty definitions Card occupies half row | Noise and blankness | Inline needed methodology, expandable detail | Highly regulated analysis may require full disclosure |
| "Project A wins" when times or sampling differ | Unfair/false inference | Align units/windows/coverage/sample, or say not comparable | Explicit user-approved scoring algorithm with explained rules |

See comparison-page-design.md and chart-interior-alignment.md.

## v6.11 — Task center anti-patterns

| Anti-pattern | Why it fails | Better approach | Valid exception |
| --- | --- | --- | --- |
| Three counters occupy a whole column, task list mostly blank | Area exceeds value; states are not useful filters | Clickable compact status group above integrated tasks | Dense operations monitoring may warrant compact filter sidebar |
| Every row repeats "percentage unknown; showing stage" | Redundant text slows scanning | Show actual stage; show numeric progress when denominator exists | Unique per-task abnormality may justify extra explanation |
| Every unfinished task shows Retry | May be illegal/meaningless for queued/blocked work | Gate by lifecycle, permission and backend capability | Explicitly supported special rerun must be explained |
| progress=null displays 0% and ETA | Fabricates certainty | Honest stage or indeterminate progress; unknown ETA omitted | Percent permitted with stable true denominator |
| Full logs/phases/raw JSON displayed continuously inside task list | Details destroy scan area | One necessary reason in row; full logs/input/output on demand | Dedicated debug page can show full execution trace |
| Filter shows 2 tasks but header claims 7 with no scope | Users misunderstand coverage | "Showing 2 of 7", indicate what aggregates count | Server paging may report total/current-page explicitly |
| Mock retry just changes UI but claims a server job was retried | False result | Label simulation; real API must wait for response and handle rollback | No-backend prototypes may demonstrate intended flow if labeled |

Full run-monitor guidance: task-center-run-monitor-design.md.
