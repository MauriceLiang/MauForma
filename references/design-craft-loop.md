# Design Craft Loop — Iterative Product Design, Not a One-Pass CSS Beautification

Design quality comes from repeated observation, informed decisions, implementation and real evidence. This guidance applies across marketing, tools, learning, editorial, data and creative experiences. It is not an invitation to redesign unrelated features when a user requested a narrow fix.


**Task modes (not interchangeable):** **shape** = new product or major structural design; **polish** = existing UI refinement with inherited design; **review** = evidence-based critique without unrequested edits; **fidelity** = implementation against an authorized reference; **fix** = scoped bug reproduction and repair. A mode does not authorize altering unrelated product behavior.

**Seven required craft domains for applicable screens:** Typography; **Color & Contrast**; **Spatial Design**; Motion; **Interaction States**; Responsive behavior; **UX Writing**. Evaluate each in relation to the real task and its information hierarchy rather than imposing a universal appearance. Findings follow evidence → observed problem → **root cause** hypothesis → severity **P0/P1/P2/P3** → repair → real retest. A claim of visual **fidelity** requires an authorized source and same-viewport comparison; a synthetic demo alone never suffices.

## Design craft is a process, not a preset aesthetic

A refined UI is not automatically minimalist, symmetrical, low saturation or filled with Cards. Strong editorial asymmetry, immersive product visuals, dense professional controls and quiet workspaces can all be correct when intentional. Begin by finding the **actual subject and user's job**, rather than selecting a favorite background color.

### Seven review dimensions

| Dimension | Inspect | Common false shortcut |
| --- | --- | --- |
| Information and task | Correct audience, next action, hierarchy, necessary data and constraints | Adding gradients to wrong content |
| Composition | Dominant region, reading order, grouping, alignment and whitespace | Repeating the same Hero+Cards template |
| Typography and copy | Role-based type, contrast, language fit, readable values, genuine information | Decorative eyebrows and tiny business text |
| Color and surfaces | Actual brand/status roles, accents, optical weight and layering | Uniform saturated badges or nested Cards |
| Components and interaction | Owner, state, keyboard/focus/error/loading/disabled and form outcomes | A static attractive gallery considered complete |
| Motion and continuity | Trigger, spatial cause, rest, interruption and reduced motion | Default fade on every route |
| Responsive/performance/accessibility | Supported widths, zoom, scroll end, content stability, cost, a11y | One desktop screenshot or a synthetic smoke pass |

## Loop 0 — Observe and classify

- Inspect actual page code, main routes, installed stack, approved brand/design system and real content. On an existing UI, capture **before** at the same viewport/state. Distinguish `confirmed / inherited / delegated / proposed / unresolved`.
- Understand which product mode or modes apply: `Operate / Read / Persuade / Experience`; classify page-specific task priority and user journey before tuning visuals.
- For general “polish” requests, proactively inspect beginning/middle/end and main interactive states; find **pre-existing** defects as well as recent regressions. A source diff alone misses bad historical copy, spacing, selection and component mixing.
- A clear narrow functional fix requires scoped reproduction and tests, **not** a brand interview. If source/browser is inaccessible, report observation limits and avoid inventing defects.

## Loop 1 — Frame the problem, not decorative symptoms

Identify the actual primary question/action and what currently blocks it. Sort issues from information architecture/content and key workflow through geometry/typography, component states and decoration.

For a major redesign with missing art direction, propose 2–3 genuinely distinct first-screen directions with content assumptions, benefits and costs. A suggestion becomes an approved direction only after user confirmation or legitimate delegation. Do not silently discard approved navigation, colors, density or interaction decisions.

## Loop 2 — Composition and perceptual hierarchy

1. Inventory real content by `primary/supporting/conditional/deferred/removable`; remove dead/repeated content before polishing it.
2. Build a grayscale composition with clear P0/P1 focal information. Choose open reading flow, chart grid, task list, product stage, split workspace or other content-driven layout.
3. Set inside/peer/section/connected spacing relationships **at the parent layout level**. Don't substitute Card padding for peer gap or erase inherited good separation.
4. Resolve navigation ownership and real scroll-to-end. A visually neat first viewport is not enough when last records or action bars are inaccessible.
5. Audit titles, section/alert copy and actual data semantics; generic pretitle/slogan does not become useful through a new font.

## Loop 3 — Build the coherent system

- Decide from the **actual framework and installed UI libraries**. Reuse stable library/primitive controls, map shared semantic tokens to Button/Field/Select/Dialog/Navigation/Table roles, and document true exceptions. No fake `div + click` Select.
- Component craft includes real states: hover, selected, focus-visible, disabled, pending, error, empty and long content in supported locales. Component Gallery is a useful fixture, not evidence the full product worked.
- Icons express actual objects/actions and form a coherent family; no compulsory Lucide or one hue.
- Preserve confirmed brand. Semantic state colors cannot be replaced by accent for decoration. Don't add attached colored Card border stripes or redundant sidebar rails.

## Loop 4 — Add meaningful motion within authorization

Motion supports input feedback, spatial continuity, status transitions or narrative—not effect quantity. First inherit or clarify the **actual user motion choice**. Respect `prefers-reduced-motion`; a rich marketing experience may justify cinematic sequences while a dense workbench needs restrained interruptions.

For high-value changes specify `trigger → before → during → payoff → interrupt/reverse → reduced`. Verify actual frames, final state, focus and cancellation. A CSS transition declaration is not proof the motion played smoothly. No unauthorized engine installation or large dependency swap.

## Loop 5 — Run the real page and review independently

- Open the **actual affected route** using the project's supported browser/test tooling; inspect rendered DOM before guessing selectors. Capture same-state before/after screenshots where possible, and check initial/middle/end, scroll end, responsive supported sizes, 200% text, light/dark, keyboard, selected/loading/empty/error and permissions.
- Verify actual operations (save/submit/retry) via real backend when available, not a simulated button. Record console/network failures.
- For a major change seek **fresh-eye critique** independent of the implementing agent: first impression, task clarity, typography, spacing, visual identity, motion, accessibility, performance and data truth. Supply evidence rather than the implementer's explanations; reviewers still need to substantiate findings.
- Rework P0/P1 problems and recapture. Do not declare a defect fixed while it remains in inherited components or related routes.

## Loop 6 — Report truthfully and keep boundaries

Use `evidence → issue → likely cause → priority P0–P3 → fix → actual retest`. Distinguish `VERIFIED` (actual tested product and applicable scope), `STATIC CHECK`, `DEMO ONLY`, `NOT TESTED`, `BLOCKED` and `NOT REVIEWED`.

A code review with no running page may still be valuable; clearly say it was static. A passing synthetic Gallery proves the Gallery, not arbitrary user product quality. Avoid dumping screenshots, private Figma data or identifiable project content into public Skill artifacts.

### Exit test

A completed design pass should be able to answer: *What user task improved? What real page/content changed? Why was this composition/component/motion chosen? Which before/after behavior was actually tested? What remains uncertain?* If any important answer is missing, report the gap instead of claiming comprehensive delivery.

Related: `references/design-discovery-interview.md`, `references/composition-first-design.md`, `references/proactive-visual-defect-discovery-gate.md`, `references/visual-critique-loop.md`, `references/browser-qa-protocol.md`.


## Source-parity restoration — Original five task modes and minimum deliverables

**Do not run all modes or seven entire workflows for each task.** Choose the work mode by scope, and preserve the original minimum deliverable and what it does **not** require:

| Mode | Trigger | Minimum deliverable | Unnecessary / unauthorized |
| --- | --- | --- | --- |
| **shape** | New page or visibly misfocused major redesign | Task/content brief, visual direction, shared Tokens and component plan, first implementation and browser recheck | Repeated discovery when requirements are clear |
| **polish** | UI seems plastic, hierarchy unclear, controls coarse | Baseline evidence, root-cause findings, severity-ordered repair, same-condition before/after | Unapproved total navigation/brand rewrite |
| **review** | Independent evaluation only | Evidence-based severity list, strengths, recommendations, untested items | Editing code without request |
| **fidelity** | User supplies Figma and requests faithful reproduction | Authorized design-node context, reference screenshot, asset/Token mapping, implementation and difference retest | Replacing design or composition to personal taste |
| **fix** | Localized interaction/visual bug | Smallest relevant change and regression of related states | Whole-product design discovery |

Operate / Read / Persuade / Experience describe a page's primary product goal, **not fixed layouts**. Explicit user preferences, approved brand, real business tasks and inherited component contracts outrank these mode labels. MauForma authored the process independently; it is **not** another installed Skill or a third-party designer's official scoring standard.

## Original Design Direction Gate — Seven required decisions before a major build

For **new pages or major restructuring**, write a concise Design Intent covering:

1. **Subject and audience** — Who uses the page, which task matters, and what real content/photography exists?
2. **Visual thesis** — One sentence explaining intended experience and how it serves the task. “Premium/minimal/modern” alone is insufficient.
3. **Primary information and composition** — Which headline/media/data/CTA dominates the first screen; which are supporting? Use grayscale sketches where useful.
4. **Optional signature element** — One memorable subject-appropriate photographic crop, type choice, spatial treatment, interaction or color relationship. **Not mandatory for operational Tables**.
5. **Reasoned choice and rejected option** — Explain “A because X, not B because Y”; record confirmed / inherited / delegated / proposed / unresolved authority.
6. **Existing Tokens/components** — Inherit CSS/Figma variables, Provider and primary UI suite; only new projects establish a minimal new token source. See references/component-library-first-gate.md; **do not hand-write fake Select**.
7. **Constraints and fallback** — Supported platform, performance, motion choice, font licensing, themes, breakpoints and necessary devices. A desktop-only product **does not require** a new mobile app.

**Design risk is optional, not a license to impose style:** A purposeful unconventional composition need not mean forced vivid color, serif text, asymmetry or page-entering animations. Inter, Cards, gradients and monochrome are **not inherently AI-looking**; their misuse against user tasks is the issue.

References: references/design-discovery-interview.md, references/composition-first-design.md, references/design-style-catalog.md, references/design-dna-protocol.md.

## Original seven craft domains — All diagnostic dimensions, not seven mandatory modifications

| Domain | Inspect | Common concrete flaw | Evidence to verify |
| --- | --- | --- | --- |
| **Typography** | PageTitle/body/data/axes/legends, CJK/mixed-language, font license, weights/line-height/optical dimensions | Explanatory pre-H1 eyebrow on operational screen, giant heading hiding task, illegible chart ticks | Actual font rendering, long labels, Chinese/digit mixing, **200% text** |
| **Color & Contrast** | Semantic brand/neutral/state, neighboring surfaces, light/dark, focus contrast | Random HEX, faded copy, brand accent confused with error/success, bright surfaces fighting | Foreground/background contrast and real whole-page theme |
| **Spatial Design** | Inside/peer/section gaps, row/column Grid, container necessity, bottom access | Adjacent panels touch, nested Cards, misaligned rows, false min-height whitespace | DOM geometry, **full page and true scroll end** |
| **Motion** | User-authorized timing/easing/stagger/state continuity, reduced motion | Zero visible feedback, meaningless bounces, motion out of sync, multiple engines claiming same property | Real interaction capture, reduced motion, unmount cleanup |
| **Interaction States** | Library Select/Combobox/Dropdown/Button/Tabs/Dialog, selected/hover/focus/disabled/loading/error | Hand-made fake menu, divergent Button radius, lost keyboard focus, clipped overlay | references/component-library-first-gate.md plus **target route state tests** |
| **Responsive** | Required device range, container rules, long copy/reading order | Shrinking font instead of reflow, narrow-height clipping, fixed bottom bar hiding content | Supported viewport matrix and **200% font scaling** |
| **UX Writing** | Informative headings/actions/status/errors, units, source and exceptions | Decorative English, repeated jargon, Mock implementation text exposed, data source/sample deleted | references/semantic-copy-hygiene.md and real task path |

The seven domains are **coverage for review, not a requirement to change every domain**. Fix inaccessible functionality and real operations first on workbenches; prioritize authentic content and composition for brand experiences. Do not generate each Button/Radius/Focus per page to look “unique.”

## Original independent critique requirements

- Evidence class: **OBSERVED** (actual browser or visible screenshot), **CODE ONLY** (source-level risk), **INFERRED** (hypothesis), **NOT TESTED** (insufficient evidence). Subjective “cheap-looking” is **not automatically measurable**.
- Severity: **P0** business unusable/severe accessibility; **P1** primary task or structure wrong; **P2** typography/spacing/components damage use; **P3** local optical fine-tuning.
- Issue entry format: **symptom → evidence → root cause hypothesis → affected task → recommended fix → validation**. Unknown cause remains a hypothesis, not fabricated certainty.
- Keep separate **UX/IA** task/content/path diagnosis and **Visual Craft** type/color/composition/component inspection. Neither successful clicking nor palette changes can substitute for the other.
- Preserve already-good solutions and user-approved decisions; repair **P0/P1 before P2/P3** and compare exactly the **same viewport, data state, theme and zoom**, repeating until key defects are gone or limitations disclosed.
- Team scores from references/ui-review-rubric.md are optional; a high definitive score **cannot be justified without real screenshots and operable evidence**, nor may aesthetics be presented as algorithm-certified.

### Six explicit anti-template critique questions

1. When abstract English overlines and slogans are removed, can users still identify the page's task?
2. Is the most prominent first-screen region the actual task or authentic brand subject?
3. Is the defect in **composition/content**, not just colors/radii? Fix upstream causes first.
4. Are icon families, controls, density and spatial relationships **systemically coherent**, not independent pretty blocks?
5. Is the memorable detail grounded in content/brand, or copied from trendy gradients, giant Cards or particles?
6. After testing light/dark, long Chinese copy, real Select/selected states and true scroll end, does the visual decision still work?

## Original mode-specific exit workflow

- **shape:** Brief / Intent → Composition / Tokens → real component library → implementation → critique → targeted revision → real re-verification.
- **polish:** Actual-product baseline → root-cause priority → structure/content fixes → shared components/Tokens → optical detail → before/after.
- **review:** Available evidence → separate UX + Craft critique → severity and repair suggestions, **without unsolicited edits**.
- **fidelity:** Follow references/figma-fidelity-workflow.md; exact pixel comparison requires actual accessible original design. With inaccessible source, **do not invent a Figma look**.
- **fix:** Strictly bounded change → direct repair → regression of related states; skip irrelevant art-direction tasks.

Every delivery must distinguish **VERIFIED / STATIC CHECK / DEMO ONLY / NOT TESTED / BLOCKED**. Synthetic demonstrations, screenshot critique and real-backend E2E are different evidence classes; none substitutes for another.

**Public-source isolation:** Only original reusable principles and authorized source may be committed to this Skill. Do not copy another Skill's code/commands or protected source material without appropriate rights. Keep real client screenshots, business fields and product-specific design decisions in the actual client/project workspace. External acknowledgements belong in the repository README.
