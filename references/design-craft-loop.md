# Design Craft Loop — Iterative Product Design, Not a One-Pass CSS Beautification

Design quality comes from repeated observation, informed decisions, implementation and real evidence. This guidance applies across marketing, tools, learning, editorial, data and creative experiences. It is not an invitation to redesign unrelated features when a user requested a narrow fix.

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
