# MauForma — Component-First Visual QA v2.0

**Scope:** This is a per-task acceptance checklist, not a universal demand to redesign every screen. Inspect only applicable user tasks, routes and states, preserving previously approved direction. Mark missing real-product observation **NOT TESTED / NOT AUDITED / NOT RUN** rather than treating a static or synthetic test as a pass.

## Settings / Form / Hybrid scenario QA

- [ ] Did the Agent classify each area as **individually saved setting / multi-field submission / hybrid** based on save semantics, rather than page title?
- [ ] Do compact preferences put label/explanation left and control right, with tight item spacing and clearly larger group spacing? On narrow screens, do they reflow rather than crush controls?
- [ ] For continuous forms, are labels above inputs, field columns a reasonable width, long error messages completely visible and associated with their fields? Are any multi-column layouts justified?
- [ ] Have meaningless giant outer Cards been reduced while retaining real group boundaries, legitimate single-layer panels, separators and prior section gaps?
- [ ] Are destructive Delete/Clear actions isolated, confirmed and supported by clear risk and permission text?
- [ ] Were **real** setting-save failures, validation errors/success, keyboard focus and last-item scrolling tested? If not, are they labeled NOT TESTED?
- [ ] Is a synthetic browser demo PASS kept distinct from actual user-product verification? See references/settings-form-layout-gate.md.

## Gate LO — Readable layout, independent label collisions and optical feasibility

- [ ] On **every new or affected existing page**, do independent Badge/pills, tags, metadata, links, status labels and controls overlap each other's borders/backgrounds, even where glyphs appear separate? Unintended surface collision is a visible defect.
- [ ] Does any visible text collide with another line or enter a neighboring painted label? Are source/license/long ID and mixed CJK/Latin words fully understandable, not clipped or silently obscured?
- [ ] Do flex/grid peers reflow, wrap or stack with appropriate gaps at the minimum **supported** viewport, 100% and 200% text zoom and realistic longer localized strings? Desktop-only tools need their smallest supported desktop, not invented phone support.
- [ ] Is reading order natural and optical grouping coherent after the collision fix? Check actual screenshot, font contrast, whitespace, clear control boundaries, selected/focus/expanded states, error/loading content and end-of-scroll. A geometry-only PASS cannot establish visual/reading quality.
- [ ] For visual polish, did the Agent inspect and repair **pre-existing** collisions, rather than preserving bad original layout? For new UI, did it verify the first implemented representative group before propagating it?
- [ ] When the real browser is available, was `scripts/audit_label_collisions.mjs` (or the integrated viewport/defect audit) used as candidate evidence, were flagged pairs resolved, and were the same route/state/viewport recaptured? False positives and intentional layers require **specific local reasons**; do not hide independent text with an exception.

See `references/visual-overlap-and-legibility-gate.md` and `references/grid-alignment-and-viewport-safety.md`. Mark inaccessible real-page states NOT TESTED rather than pretending a synthetic browser fixture certifies a product.

## Proactive defect discovery for vague prompts

- [ ] If the user only said "improve/polish this page", did the Agent **proactively inspect existing real-page defects**, rather than waiting for every problem to be listed?
- [ ] Did it check **five areas**: spatial separation, type scale/hierarchy, component density, icon/palette, and interaction/responsiveness? Are key findings evidence-grounded, without inventing defects to hit a quota?
- [ ] Did it use scripts/audit_existing_visual_defects.mjs to detect **pre-existing independent-panel contact**, instead of using only before/after diff and preserving inherited bad states?
- [ ] Was the actually modified page reopened and the original problem confirmed gone (not just a Skill Demo)? If not, is the status UNFIXED or NOT AUDITED?
- [ ] Are semantically connected Tab/Panel boundaries preserved, without mechanically assigning identical margins to every Card?
- [ ] If the user asked only for an assessment, was code left untouched? Did an isolated bug fix avoid unauthorized site/brand redesign?

Source: references/proactive-visual-defect-discovery-gate.md; synthetic smoke: tests/existing_visual_defect_browser_smoke.mjs.

## Real-page panel-spacing regression

- [ ] Before optimization, were meaningful gaps between independent analysis, summaries, charts and metadata identified/preserved? No unauthorized row-gap:0.
- [ ] Were **both** column-gap within rows and row-gap between rows checked, including single-column reflow?
- [ ] Was before evidence captured on the **same real route/data/width/font scale**, then compared with after? A standalone Skill example does not validate the target route.
- [ ] Without DOM markers, was scripts/audit_panel_spacing.mjs used for heuristic large-panel risks, and scripts/audit_spacing_rhythm.mjs used when an explicit relation contract exists? Were unframed/nested cases additionally inspected visually?
- [ ] Did UNJUSTIFIED_PANEL_CONTACT or SPACING_REGRESSION trigger repair rather than blanket connected exemptions or disguising lack of gap with padding?
- [ ] Did genuinely connected Tab/Panel or Table Head/Body preserve valid shared borders?
- [ ] Do spatial relationships remain stable at desktop, **320/390 widths, 200% text**, final scroll position and interactive states?

Reference: references/spacing-regression-protection-gate.md; synthetic regression: tests/panel_spacing_browser_smoke.mjs.

## Reference Learning, Design Transfer & Public Safety Gate

- [ ] Is explicitly claimed user ownership respected rather than inferring "internal" or "third party" from the screenshot?
- [ ] Is the reference **analysis-only**, with **no original image, crop, redaction, re-encoding, data URI or screenshot attachment** published to public repo, PR or Actions artifact?
- [ ] Are insights extracted as **trait → visual effect → task value → applicable condition → exception → transferable rule**, not copied CSS/business fields/whole-page pixels?
- [ ] Do public synthetic examples use a newly invented domain, navigation and fictional data, with **no identifiable source project name, address, logo or business record**?
- [ ] If Clean Enterprise is used, is that suitable for actual product content and user choices, instead of overriding brand, artistic direction or motion in unrelated products?
- [ ] Are icon sources and licenses verified officially for the new demo; were icons/fonts/navigation/data density and primary task/responsiveness tested in the browser?
- [ ] Did publication receive **human review of commits, PR and added files**? Do not treat scripts/validate_design_reference.py PASS as proof of complete privacy/copyright clearance.
- [ ] If the real product was not edited, does the report explicitly say only Skill/original-demo verification occurred?

See references/design-reference-learning-gate.md, references/clean-enterprise-design.md, examples/design-reference-learning/reference-principles.json, tests/design_reference_browser_smoke.mjs.

## Icon Art Direction & Semantic Fit Gate

- [ ] Are icons for primary navigation, frequent actions and critical states **accurate, familiar and immediately understandable**? Are they needed at all, instead of arbitrary brainwave/lightning/star symbols?
- [ ] Were meaningful candidates from a verified icon family/version compared, rationale recorded, and already approved brand choices inherited?
- [ ] Are outlines, filled/stroked style, negative space, complexity and optical weight coherent across the **entire icon set**? Are some extremely dense next to empty/thin ones?
- [ ] Were actual **16/20/24** contextual sizes tested alongside Chinese glyphs, Badges, active/hover/focus and themes? Equal SVG width/height alone does not prove visual coherence.
- [ ] Is one nav/toolbar mixing unrelated emoji, hand-drawn SVG, filled and outline libraries or large icon-fonts causing bundle/flash risks? Document justified brand/logo exceptions.
- [ ] Do actual icons load without compression/cropping, and do icon-only buttons have accessible names? Without a text label, users must not have to guess actions.
- [ ] scripts/audit_icon_consistency.mjs can check **explicitly annotated** groups for geometry/stroke/family/render risks. Actual artistic and semantic judgment still requires the full page or Gallery. If not reviewed by a person, mark **NOT VISUALLY VERIFIED**.

See references/icon-art-direction-gate.md, assets/icon-curation-patterns.json, assets/icon-art-direction-lab.html.

## Semantic Spacing / Visual Rhythm Gate

- [ ] Have separate sections, peer Cards, inside title/content relationships and genuinely connected controls been distinguished? Do gaps communicate task boundaries, and are zero-gap connections justified?
- [ ] Alignment alone is not a pass: even if two peer Cards have column gutter, do **row 1 and row 2 accidentally touch at row-gap:0**? Are gaps preserved on horizontal-to-vertical reflow?
- [ ] Are space.inline/inside/peer/section/page mapped to inherited tokens/density, with parent Grid/Stack owning sibling gap and Card padding owning only internal space? Do not add the same margin to every element to mimic rhythm.
- [ ] Are a subheading and its chart/explanation semantically closer than independent sections? Does the reading flow make sense from header → chart, summary → analysis, chart → data-quality/chapter explanation?
- [ ] Are intentional zero-gap Tab/Panel, Table Head/Body and connected split panes spared false alarms? Are anchored Popover/Overlay positions evaluated by actual usability?
- [ ] Do gaps survive desktop/small-screen, 200% text, error/empty, expansion/collapse, fixed action bars and actual bottom scrolling?
- [ ] In a live browser, scripts/audit_spacing_rhythm.mjs may check **explicitly annotated DOM relations** and horizontal overflow. Without annotations mark NOT AUDITED; script PASS is **not** a human aesthetic score.

See references/semantic-spacing-rhythm-gate.md, assets/spacing-rhythm-patterns.json, assets/spacing-rhythm-lab.html, scripts/validate_spacing_rhythm.py.

## Motion Craft & Frame-by-Frame Rehearsal Gate

- [ ] For changed important interactions, is the sequence **trigger → before → motion → payoff → reverse/interrupt → reduced motion** recorded instead of only CSS properties?
- [ ] Do Buttons, selected indicators and list objects retain identity, while neighboring layouts move coherently, anchors remain stable, and words avoid squeezing/ghosting?
- [ ] Is motion causally meaningful and layered, with immediate input feedback, relevant overlap/stagger, and no arbitrary pauses or long waits?
- [ ] Were first, intermediate, settled and fast-reversal frames captured **on the real page**, and observed at normal playback speed? Is insufficient sampling labeled INCONCLUSIVE?
- [ ] Were light/dark, smallest **supported** viewport, long copy, reduced motion and focus return retested as relevant? Synthetic simulation is not real business evidence.
- [ ] Does the capture tool report only evidence, clearly distinguishing unreviewed visual impressions? Was the **whole interaction recaptured after a repair**?

See references/motion-craft-and-continuity.md, references/motion-rehearsal-and-evidence.md; optional scripts/motion_rehearsal.mjs.

## Component Motion Choreography Gate

- [ ] Which important **actually existing** Button, Tabs/Filters, Accordion/Drawer, Toggle, List/Table, Chart/Media and notifications were inventoried? Is there a Motion Inventory including reasons for **motion / immediate feedback / deliberately static**?
- [ ] If the user chose B/C motion, are there actual component-level transitions? A route crossfade, one Dialog Fade or global Button Hover alone is **not** sufficient.
- [ ] Do mechanisms match behavior—indicator actually travels, disclosure has spatial origin, Toggle state morphs, list changes preserve positional continuity, feedback is immediate/readable? Not every element gets the same fade+offset; do not add effects for quantity.
- [ ] Does the actual Component Showcase cover before/during/after, rapid reversal, touch/keyboard, narrow/zoom/long text? Decoration must not obscure focus/results or cause broken characters or clipped bottom content.
- [ ] Does **none** and prefers-reduced-motion preserve all functionality? A failed motion dependency must not break business state or content.
- [ ] Does the delivery report component, trigger, mechanism, purpose, tests and missing checks? animationDuration>0 and a Mock smoke do not prove target-product experience.

See references/component-motion-choreography-gate.md, assets/component-motion-patterns.json, assets/component-motion-lab.html, scripts/validate_component_motion.py.

## Motion Choice & Interaction Experience Gate

- [ ] Was a genuinely selectable/observable motion experience presented for a **new site or major redesign**? Is authority confirmed/delegated/inherited, otherwise unresolved? Silence must not imply the entire site is permanently static.
- [ ] Were **2–3 actually distinct motion levels** shown through real Buttons, Tab indicator/content, Dialog/Drawer open/exit, status/data and brand moments—not "Hover only" misrepresented as finished interaction design?
- [ ] When the user selects **no extra motion**, are focus, selected and success/error states still immediate? For B/C, are appropriate smooth component transitions actually implemented rather than merely described?
- [ ] Are transitions brief and interruptible under rapid clicks/reversal, without flicker, lost keyboard focus, scroll position, feedback or real submissions? Avoid excessive row staggering, fake loading/progress and state loss.
- [ ] Under prefers-reduced-motion/manual reduction, are states still visible, dialogs operable, keyboard and actual results intact? Honor preference in browser and JS animation.
- [ ] Were actual browser before/during/after, mobile if supported, **200% text**, weak devices and long content examined? Unrun cases must be listed; a static plan or Mock is not real-product verification.

See references/motion-consent-experience-gate.md, assets/motion-choice-layout-lab.html, scripts/validate_motion_decision.py.

## Surface & Control Geometry independent acceptance

- [ ] Does the page-level mega-Card, nested toolbar and row-Card structure each have a real role? If the whole page is framed for decoration, were open collection or single panel considered?
- [ ] Is the chosen container justified against at least one plausible alternative? A Card from the installed library does **not** mean a page needs a border.
- [ ] Do dense homogeneous lists have stable headers, column tracks, separators and scan paths? Media/product Cards, branded Heroes and specialist split panes may remain appropriate by content.
- [ ] Do short Buttons, Tabs, Badges, Nav/Status labels avoid character-by-character vertical Chinese, broken English words, clipping and overflow? Are whole actions readable, clickable and keyboard-operable?
- [ ] Are natural label width + icon + padding budgeted into parent column/action group? white-space:nowrap alone cannot fix a narrow column; narrow views should use control-level wrap, row reflow or accessible overflow action menu.
- [ ] Were errors, varying permissions, more actions, long CJK/English, small supported phone viewport and 200% font tested? Include screenshots of action columns and scroll end; if not, mark **NOT AUDITED**.
- [ ] scripts/validate_surface_control.py --repository only checks synthetic design decisions. A standalone browser-demo PASS does **not** verify the target project.

See references/surface-architecture-gate.md, references/control-geometry-gate.md, assets/surface-control-layout-lab.html.

## All-Web perceptual hierarchy and component-quality gate

- [ ] Are the task and **P0/P1/P2/P3** information priorities clear at the current viewport? Importance comes from decision value—not "every number should be big"; first focus and next action should be identifiable.
- [ ] In grayscale/without decoration, is attention on the important object/state/body/price/artwork rather than a meaningless giant heading or empty panel? Different page modes have different protagonists.
- [ ] Are essential content/fields/status reasons not all reduced to 12px, and not every element oversized? Type roles arise from real font/language/density and project Tokens.
- [ ] Does every frequent-use component have a specific role, primary/secondary text, size/variant/state, operability and long-text behavior? Do composed views align control/status/list baselines, spacing and weight?
- [ ] Do Badge/pills, panel frames, colored status, dotted border and shadow have explained roles? The library's default skin is not a substitute for real art direction.
- [ ] Does **Operate** favor scanning, **Persuade** conversion, **Read** body text, and **Experience** works/media and necessary controls? Do not force all modes into the same dashboard appearance.
- [ ] Were real desktop/narrow, 200% zoom, light/dark if supported, mixed Chinese/English and error/loading/empty reviewed? Explicitly state actual browser usage; a static check is **not** visual PASS.

See references/perceptual-hierarchy-gate.md, references/component-craft-gate.md, assets/visual-priority-patterns.json; scripts/validate_visual_priority.py --repository checks **plan coverage**, not premium aesthetics.

## Same-role control consistency — native / third-party / headless

- [ ] Did existing and newly added UI inventory native controls, third-party libraries, headless primitives, shared wrappers and conflicting skins? Is each same-role different implementation justified with compatibility/target-source reasoning?
- [ ] Does the primary component strategy fit the real product mode and approved design, rather than migrating an entire library by aesthetic preference? If permissions forbid installation, keep appropriate native controls and disclose platform visual limits.
- [ ] Do actual **open** Select/Combobox/DropdownMenu menus match closed triggers and peers? Was native browser/OS options presentation tested on the target platform? If unobservable, mark **NOT TESTED**.
- [ ] Are global Provider/Tokens/shared wrappers active for old and new pages? Do actual functionality, keyboard, selection, disabled/error, long labels and focus still work?

See references/component-consistency-and-selection-gate.md; scripts/audit_control_consistency.mjs only produces DOM candidates, **not aesthetic or semantic verdicts**.

## Gate A — Theme and Tokens before business pages

- [ ] Is the product direction explained in one clear sentence, without forcing a generic pink-blue gradient?
- [ ] Are page/surface/surface-soft/text/accent/on-accent/focus/border/status semantic roles present?
- [ ] Are primary accent and status colors distinct; is centralized theme switching functional, without arbitrary per-page hard-coded colors?
- [ ] Are radius/spacing/type/motion shared Tokens with a deliberate showcase-versus-productivity density?
- [ ] Were contrast and palettes tested in every required light/dark mode?

## Gate B — Components before bulk implementation

- [ ] Were installed libraries inventoried and retain/wrap/add decisions made, rather than rewriting primitives for looks?
- [ ] Are only business-needed Button, Field, Panel, Nav, Dialog and Status/Feedback shared components implemented?
- [ ] Do component APIs define variants, sizes, props/slots/events, relevant states and ownership?
- [ ] Is there a runnable showcase covering applicable normal/hover/focus/disabled/loading/error/empty?
- [ ] Is there no second scattered theme or random radius; do per-page .button rules avoid overriding core shared component appearance?
- [ ] Are Input text, keyboard focus, label relationships and explanatory errors legible and complete?

## Gate C — Actual screen visuals and behavior

- [ ] Is primary/secondary information clear without accent colors pulling attention from content? Are long Chinese headings/numbers intact?
- [ ] Does spacing show relationships, without meaningless large color blocks, nested giant Cards and excessive shadows?
- [ ] Have real save, cancel, delete, navigation, form validation, error/empty/loading flows survived visual changes?
- [ ] Are hover/focus/pressed/disabled/loading visually distinct and not represented solely by color?
- [ ] Were wide + narrow/mobile layouts tested; supported dark mode verified?
- [ ] Is the app usable under Reduced Motion, with core content visible even if third-party animation fails?
- [ ] Are performance and legibility favored over extreme glass, neon and excessive spring effects?

## Review procedure

1. Run the target project's checks/build; when using MauForma's theme package, run scripts/validate_design_system.py.
2. Open the component showcase (or temporary state fixture) for shared controls and states.
3. Open real business routes at least in wide/narrow windows and critical states; inspect high DPI, zoom and long Chinese copy.
4. Compare examples from references/good-vs-bad.md, reporting specific components/pages and repairs.
5. Score per references/ui-review-rubric.md; **fix blockers before acceptance**.
6. Without real browser or screenshot tooling, explicitly state **"static source review only; real rendered result NOT VERIFIED"**.

## Gate H-S — Title self-sufficiency (all pages, not just operational H1)

- [ ] Does each heading communicate the page/section/object on its own, **without an automatic decorative pretitle**? The ordinary outcome is one clear heading.
- [ ] For *every* visible H1–H6, Card, Section, Dialog and equivalent visual heading, do inherited and newly introduced pre-title lines survive a removal test? If deletion loses no independent information, **DELETE** rather than rationalizing "context".
- [ ] If information is lost, was it preferentially MOVED/MERGED into real navigation, chapter/stepper, status, source, scope or below-title explanation? For each exceptional **KEEP**, is there distinct evidence of information value **and why this must stay above the title**?
- [ ] Were all candidates resolved and affected before/after rendered views checked? When feasible run `scripts/audit_title_prefixes.mjs` followed by `scripts/validate_title_prefix_review.mjs`; static/synthetic checks do not certify a real page. No unresolved candidate may be reported as VERIFIED.

## Operational page headings / AI template patterns

- [ ] **Hard first-delivery gate:** Operational management/workbench/settings/data/list/edit H1 has **no explanatory pretitle**, uppercased fake category, ornamental number or letter-spaced overline, even if not an exact repeat of H1.
- [ ] Real breadcrumbs remain **navigation**; necessary status/version/data range appear by their relevant functional area, and explanatory help normally belongs **below H1**.
- [ ] Small labels, English headings and subtitles provide distinct real information; unjustified ornament was removed.
- [ ] Primary action remains beside title and actual list/form appears early in a normal supported viewport.
- [ ] Equivalent task pages use UiPageHeader or existing shared equivalent; preserve real breadcrumbs, technical terminology and essential warnings.
- [ ] Compare references/page-header-antipatterns.md and assets/page-header-antipattern-gallery.html; record before/after and rationale.

## Specialist visual-technology checks

- [ ] Was technology selected for a real effect need, with clear advantage over CSS/SVG/existing dependencies, rather than collecting libraries?
- [ ] Are CSS, GSAP, Motion and Anime.js **not simultaneously controlling the same DOM element/property**?
- [ ] Does SplitText remain accessible and meaningful after font load/breakpoint change, without needless splitting of long prose?
- [ ] Do Three.js/PixiJS/Curtains.js/tsParticles stop and clean up on unmount, hidden/background or failure, with static fallback?
- [ ] Do ECharts plots use truthful data, dispose appropriately and expose important figures through text or accessible tables?
- [ ] Does Matter.js physics avoid replacing actual DOM semantics, keyboard or business operations?
- [ ] Were actual FPS, memory, CPU/GPU, zoom and narrow-screen performance measured on **target devices**, with untested conditions stated?

## Gate E — Shared component refinement (v6.3)

- [ ] Does a desktop dark Sidebar have coherent background/surface/hover/selected/primary-secondary text/icon/focus/border roles with readable text/focus on actual surfaces?
- [ ] A selected accent rail is **optional**. If chosen, is the short rail **outside only the current NavItem** with a visible gap and intact rounded item border? **Prohibit** coloring NavItem's own border-left/border-inline-start/inset shadow as a fake external rail or leaving rails on unselected items.
- [ ] Does the selected NavItem preserve its full radius, padding and distinct hover/focus-visible? Does the external rail follow the one true current route, without crop in narrow/collapsed state? See references/sidebar-selection-indicator-gate.md.
- [ ] Are aria-current, hover and focus-visible distinct, with keyboard focus still visible even without accent rail?
- [ ] Are main Nav, Recently Visited, Help and account areas hierarchically distinct, and business warning dots meaningful with text?
- [ ] Were Topbar, Card, DataTable, Tabs, Search and Split Pane checked against workspace-component-refinement.md for Tokens, interactions and error/empty states?
- [ ] Were component examples and actual light/dark screenshots supplied? assets/sidebar-refinement-gallery.html is a synthetic comparison, **not real-product QA**.

## Page screenshot gate — structural correctness first

- [ ] Is the main user task identifiable on first screen, with the largest area holding primary content rather than meaningless 3D decoration, marketing Hero or giant colored Card? Judge by actual product mode.
- [ ] Does the main Chart/Table show true data or honest loading/error/empty? A source-less Demo must not imply actual measured growth.
- [ ] Without gradients, shadows, colored KPI icons and ornamental illustrations, does information order/reading path/hierarchy still make sense?
- [ ] Was a layout criticism addressed by changing primary/secondary region size, position or grouping—not merely shifting blue-purple to green-gray?
- [ ] Does every strong-color area represent information/brand/status, without multiple large surfaces competing for focus?
- [ ] Were desktop/narrow screenshots from the actual page reviewed? For conceptual or unrun work, label **NOT RUN**.

See references/visual-critique-loop.md. CSS or arbitrary aesthetic scores do not certify visual quality.

## Copy semantics and typographic legibility acceptance

- [ ] For every microheading, English sublabel, chapter number, slogan and explanation, can the reviewer answer **"What information would removal lose?"** Delete pure repetition/ornament; retain meaningful breadcrumb, brand and data source.
- [ ] Across all H1–H6 and Section/Card/Dialog/custom heading groups, apply references/title-prefix-role-gate.md **regardless of color, font, size, weight, language, DOM tag or CSS class**. First identify structural pretitle relationship, then distinguish information value **from validity of presenting it above a title**. Inherited use is no exemption.
- [ ] Are abstract slogans, pseudo-chapter numbers and explanations already expressed by main title repeated without independent value?
- [ ] Are ECharts tooltip internals, React/Vue implementation terms or developer notes leaked to business users? Developer tutorials are valid exceptions.
- [ ] Does H1 → Section → KPI Value/Label → Chart Axis/Legend → sample metadata have a meaningful type scale and reading order, rather than arbitrary huge/tiny text?
- [ ] Are Chart ticks, UTC, n-values and sources legible in dark mode? These are evidence, not mere decoration.
- [ ] At desktop/narrow, with long repository names, mixed Chinese/English/digits and **200% text scaling**, is content complete without crop or occlusion?
- [ ] Check contrast against relevant **WCAG 2.2** guidance. A static scanner's **12px is neither legal nor normative font minimum**, and cannot replace actual visual testing.
- [ ] If large display text, brand subtitle or real chapter number remains, is its product/contextual role explained?

scripts/audit_readability.py <src> --format json only returns **review candidates**, not automatic semantic verdicts or repairs.

## Sidebar global palette and user color authority (Gate A/D)

- [ ] Were explicit color names or HEX respected? If already chosen, was color **not** repeatedly questioned or silently changed?
- [ ] If palette was genuinely undecided and recoloring is in scope, were **2–3 complete Sidebar + Main + Topbar + Card + Chart** scheme candidates shown, rather than three isolated sidebar color swatches?
- [ ] Is Agent recommendation pending/unresolved, never deceptively confirmed? Use delegated only for explicit user authority.
- [ ] Does the final semantic Token preserve exact user HEX? For contrast concerns, explain and adjust supporting text/surfaces without secretly changing user value.
- [ ] Are Sidebar↔Main lightness/temperature and boundary coherent with Topbar/Cards/Chart series/status?
- [ ] Are selection/hover/focus and important text/control/chart contrast distinguishable in actual complete light/dark pages?
- [ ] Do browser screenshots include **whole page and sidebar/main seam**, not only Sidebar? If not tested, mark **NOT RUN**.

scripts/validate_sidebar_color_decision.py --repository tests static values/decisions, **not visual aesthetic merit**. See references/sidebar-color-discovery.md.

## Navigation Architecture and responsive access (Gate A/D)

- [ ] Are top-level count, hierarchy, change frequency and global/current-project/Tabs/context actions explicitly distinguished? Why Top, Side, Rail, Bottom or hybrid instead of defaulting all dashboards to Sidebar?
- [ ] With Top+Side, do they serve genuinely **different navigation scopes**, not duplicate level-one destinations on the same viewport? Does an action bar avoid impersonating navigation?
- [ ] In responsive Side→Bottom, are only appropriate high-frequency destinations visible, with others available through More/Drawer, preserving route IDs/order across breakpoints?
- [ ] Across small/landscape/narrow, resize, back navigation and deep links, are current selection, filters and task context preserved?
- [ ] Can fixed/sticky BottomBar, keyboard, safe area, overlay and Drawer mask occlude focus or primary content?
- [ ] Do multiple nav elements have distinct accessible names; aria-current for actual current page, **aria-selected only for Tabs**, keyboard and Skip to main?
- [ ] Are confirmed navigation architecture/color inherited; no Agent suggestion treated as user approval?
- [ ] Were actual desktop/mobile browser screenshots, menu opens and route changes exercised? Otherwise **NOT RUN**; assets/navigation-layout-lab.html is concept only.

See references/navigation-architecture.md; python3 scripts/validate_navigation_architecture.py --repository is static.

## Per-page content curation, density and whitespace

- [ ] Does Overview contain current task + three-step tutorial + three feature Cards + repeated links simultaneously? Could redundant whole sections be removed/deferred instead of only changing padding?
- [ ] Does each route have a clear primary task without multiple same-priority CTAs fighting?
- [ ] Does the same feature repeat in nav/introduction/help/footer? If deferred, does a clear discoverable path remain?
- [ ] Do first/return visit, real data, empty and failure states show only conditionally relevant content, rather than always pinning beginner tutorials?
- [ ] Does every surface have real interaction/data/grouping role and is decorative outer-Card nesting removed?
- [ ] Can Overview be airy/balanced and Analysis/Management productive/compact **without** hiding Chart labels, sources or errors as tiny 10px text?
- [ ] Do Macro group gaps, meso relationships and micro control spaces communicate hierarchy, instead of manufacturing whitespace via min-height or shrinking every font?
- [ ] Were desktop and supported mobile/narrow, 200% text and actual user states photographed/tested? If not, mark NOT RUN.

See references/page-density-and-content-priority.md, references/whitespace-and-surface-composition.md, references/overview-density-case.md; static scripts do not score "premium feel".

## Grid, Alignment and Scroll-End — visual and runtime acceptance

- [ ] Do PageTitle, filters, main content and peer ChartPanels share traceable content bounds and column gutters?
- [ ] Are peer modules top-aligned; if upper left/right have different heights, does row 2 **still start at one shared row line**, not independent Masonry stacks?
- [ ] Are **3:2 / 8:4 / full-row primary chart** asymmetries justified by evidence hierarchy? Do not force equal width/height where unjustified.
- [ ] Are Chart/List axes, ranges/units, internal baselines and padding clear **without fabricating data scale to align**?
- [ ] Can the actual page/scroll owner reach **the final item border, legend, action and record**? Normal vertical scroll beyond the first screen is **not** a bug.
- [ ] At actual scroll end, is bottom padding enough to avoid overflow:hidden, fixed heights, sticky bottom bars and safe-area occlusion? Account for **actual toolbar height**.
- [ ] In short windows such as **1280×720**, mobile **390×844** and narrower supported widths, are final controls accessible without unexpected horizontal overflow?
- [ ] At 200% zoom, long labels, Chart tooltip, keyboard focus and browser Back, can all content remain accessible?
- [ ] Does report separate screenshot-bottom **suspected risk** from confirmed DOM clipping/unscrollability?
- [ ] Does evidence contain first-screen **and true maximum-scroll** screenshots, including bottom edge? validate_layout_integrity.py alone is **not browser PASS**.

See references/grid-alignment-and-viewport-safety.md, references/grid-alignment-case.md, and optional node scripts/audit_rendered_layout.mjs --url http://127.0.0.1:5173 (requires available Playwright).

## Chart Interior and multi-object comparison QA

- [ ] After aligning outside Cards, were **Plot Area starting points, X-axis/legend baselines, inner margins and date labels** inspected? Equal Card heights do not establish plot alignment.
- [ ] Do bar/scatter values, mean markers, point boundaries actually overlap/crop? Is one value label duplicated unnecessarily?
- [ ] Do selected object IDs equal legends, real series including no_data/partial markers, and table columns? If multiple objects selected but one visible line, is that explained?
- [ ] Are common time windows/buckets, units and metric definitions clear? Missing/insufficient samples remain **null/"—"**, not 0; is coverage fairly disclosed across objects?
- [ ] Can a user see selected objects, key differences, trends and matrix entry early; or does a huge permanent picker or content-poor methodology Card consume main area?
- [ ] Are object columns/metric rows stable and scannable; do selection, difference filtering and detail actions synchronize all views?
- [ ] On phone, can users find at least a two-object comparison or an explicit way to switch objects, without squeezing three columns into tiny text?
- [ ] Were actual browser before/after selection, legend/curves, zoom and both scroll directions captured? Canvas labels uninspected means **NOT AUDITED**, never PASS.

See references/comparison-page-design.md, references/chart-interior-alignment.md, references/comparison-ux-case.md. python3 scripts/validate_comparison_contract.py --repository is **static**, not an actual plotted-series test.

## Task Center / Run Monitor specialist QA

- [ ] Was the product recognized as **automated job monitoring**, not an uncritical copy of human Kanban, comparisons or generic KPIs?
- [ ] Do status summary counts support real filtering/locating, instead of filling a giant low-value sidebar?
- [ ] Can a task row quickly show object, job type, status, progress/current stage, updated time and legitimate actions, without repeated filler and huge blank areas?
- [ ] Are aggregate counts derived from the same data scope, attention classification coherent, and post-filter visible counts/scope clear?
- [ ] Is progress derived from true completed/total/unit? **Never draw fabricated percentage without stable denominator**; show partial completion and error causes honestly.
- [ ] Does Retry appear only with actual capability, authority and valid lifecycle, not as a clickable action for blocked/completed/queued work?
- [ ] Does Detail expose real stages/errors/logs on the actual system? A synthetic demo must not claim a backend Retry succeeded.
- [ ] Does filter/search/sort/refresh preserve user context, with auto-refresh source/time disclosed?
- [ ] On narrow screen, can rows/controls be read and focused, last run scrolled to, long repo names/errors without horizontal overflow?
- [ ] Are real backend integration, authorization and E2E additionally tested? A separate Mock Chromium smoke is **not** production-service acceptance.

See references/task-center-run-monitor-design.md, references/run-monitor-case.md, scripts/validate_task_center.py.

## Foundational interactive controls — first-delivery QA

- [ ] Were existing primary UI packages inventoried; did a new project **actually choose and use** a framework-compatible mature library/accessible primitive rather than merely propose one?
- [ ] Do actual Select/Combobox/DropdownMenu/Checkbox/Radio/Switch/Tabs/Button/Dialog instances have known owners or approved native exceptions, without hand-made fake dropdowns?
- [ ] Are applicable **default/open/selected/hover/focus/disabled/loading/error** and keyboard paths operable, overlays correctly positioned without clip/stacking bugs?
- [ ] Do common themes align heights, padding, typography, radius, selected/focus/status colors, and keep long Chinese labels and narrow windows usable?
- [ ] Can the report distinguish real-route verification from static or synthetic demo, and repair shared components **before copying** faulty patterns?

See references/component-library-first-gate.md.

## Liquid Glass — optional material QA

- [ ] Does the user/confirmed brand genuinely require lens/liquid glass, rather than defaulting all navigation/Cards/Tables to glass?
- [ ] Can **transmission, refraction, specular highlight, elevation/shadow** be inspected separately, blur optional? Ordinary blur is **not** claimed as genuine refraction.
- [ ] Was actual background displacement via Canvas map + SVG feDisplacementMap + backdrop-filter:url(#...) compared in **target browser screenshots with an on/off toggle**? Merely passing CSS syntax is not compatibility proof.
- [ ] Do untested Safari/WebKit/Firefox or other browsers fall back to legible material? No black surfaces, transparent text or disabled controls from filter failure.
- [ ] Is highlight directional and shadow restrained; on complex backgrounds, contrast/focus/disabled/loading/overlays/click areas still work?
- [ ] Were rendered area and refresh costs checked under load, static enhancement used for low motion/low performance, and Observers/textures/shaders cleaned on unmount?
- [ ] Is the isolated lab tagged **DEMO ONLY** and actual route/browser labeled **VERIFIED** only after real test?

See references/liquid-glass-optics.md and assets/liquid-glass-layer-lab.html.

## Art direction and Figma fidelity routing — when applicable

- **New product/major redesign:** Follow references/design-craft-loop.md to define actual task, design thesis, focal objects and rejected template assumptions, honoring inherited system and user constraints. Do not demand decorative effects or exaggerated typography by default.
- **Polish/independent review:** Distinguish UX architecture from visual detail; record **symptom → evidence → root cause hypothesis → affected task → fix → validation**, prioritizing P0/P1/P2/P3 and preserving good inherited work.
- **Seven craft domains:** **Typography, Color & Contrast, Spatial Design, Motion, Interaction States, Responsive, UX Writing**. Check relevant domains; **not every domain must be modified**.
- **Figma implementation:** Follow references/figma-fidelity-workflow.md to obtain authorized node/screenshot/variable/asset evidence, map design components to existing primary UI library, and compare actual same-viewport browser screenshots. Screenshot-only input cannot claim node data or exact Tokens; no MCP connection cannot be fabricated.
- **Acceptance categories:** Aesthetic approval, static PASS, fidelity to source, and real business-flow success must be **reported separately**. One subjective high score is not proof of all of them.
