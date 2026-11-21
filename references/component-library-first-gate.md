# Component Library First — Reuse Accessible Interaction Components

> **Applies to:** All Web projects with visible interactive controls, whether new pages, refactoring or new feature pages. This gate regulates **actual Agent implementation**, not a merely optional library list. Small static sites, specialist visualizations and explicitly native solutions can qualify for documented exceptions.

## Authority and exception boundaries (B04, EN/ZH-equivalent)

“Component-first” never grants permission to install unapproved dependencies. Inspect existing UI libraries, lockfiles, project conventions and actual control needs first. Apply the policy only to **controls actually required by the current page**, not an entire mandatory library showcase. When implementation and necessary dependency changes are delegated, the Agent can select a compatible primary library and document its rationale, lockfile impact and verification. If dependencies are prohibited or the task is review-only, reuse semantic native controls and report genuine blockers. Never silently install global Agent hooks, alter a global environment or treat cross-framework libraries as interchangeable.

## Core rule: reuse mature controls instead of recreating interaction primitives

**Choose and actually adopt the control implementation strategy before implementing the first business page.** Component-first does not mean authoring a home-grown \`UiButton/UiSelect\` set and patching CSS independently on every route. Prefer established components already in the project; where missing, proactively select a suitable main strategy. Shared \`Ui*\` wrappers are for stable APIs and themes, not rewrites of Select, Combobox, Menu or Dialog focus and keyboard engines.

Do not default to handwritten \`div + click + absolute\` dropdowns merely because the user did not explicitly request a component library. Do not give every page different Select, Button or selected-state implementations. The Agent must act proactively rather than wait for the user to point out a weak first version.

## Gate 0 — Inventory and selection, before the first business page

1. **Existing constraints:** Inspect \`package.json\`, lockfile, actual imports, \`components/ui/\`, providers and theme files. Identify framework, main styled library, headless primitives, wrappers, existing design system and the user's approved library/visual direction.
2. **Required controls for this task:** List only the needed Button, Input, Select, Combobox, MultiSelect, DropdownMenu, Checkbox, Radio, Switch, Tabs, Popover, Dialog, Tooltip, DatePicker, etc. Distinguish data selection, action menus and searchable selection; similar arrows do not imply identical functions.
3. **Decision order:**
   - Reliable existing components → **reuse**. Retain the main library; fix theme/wrapper/visual problems rather than replace it on taste alone.
   - Mature existing library missing a control → check its own offering, official companion or compatible specialist primitive before adding another styled library.
   - New project without a primary library → proactively choose and **actually use one primary solution** for the framework, interaction complexity, visual direction, coverage, maintenance cost and license. A recommendation written in a report without integration is not sufficient.
   - No interactive controls needed (static article, small informational site) → semantic HTML/CSS is valid; do not install a large UI library to satisfy this gate.
4. **Record a concise decision:** framework, reused or selected primary library and reason, complex controls it owns, theme integration and any justified exception. Do not ask the user to complete an unnecessary questionnaire when constraints already suffice. Ask only for conflicts with genuine brand or architecture impact.

### Framework-specific candidates — never transplant components across frameworks

| Framework | Mature pre-styled candidates | Highly custom visual strategy | Boundary |
| --- | --- | --- | --- |
| Vue 3 / Nuxt | Element Plus, Naive UI, Ant Design Vue, PrimeVue, Arco Vue | shadcn-vue + Reka UI | Existing solution first; check Nuxt SSR, themes and coverage |
| React / Next | Ant Design, MUI, Mantine, PrimeReact | shadcn/ui + project's Base UI/Radix or React Aria | Never install a React package as a Vue component; check current primitive APIs |
| Svelte / SvelteKit | Mature, actually supported ecosystem suite | shadcn-svelte / Bits UI | Verify installed versions and feature support |
| Angular | Angular Material, NG-ZORRO, PrimeNG | Angular CDK with custom visual layer | Angular CDK provides primitives, not an automatic styled skin |
| Solid | Compatible UI solution for the active project | Kobalte / Ark UI, after confirming framework support | Do not copy React components unchanged |
| Astro / Vanilla | Current semantic native controls or compatible suite | Accessible components in the selected interactive-island framework, native where sensible | A simple static form is not a reason to install a full SPA stack |

“Mature” never means permission to add arbitrary dependencies. Compare reusability, components and states, styling flexibility, bundle/runtime weight, framework/SSR compatibility, license and maintainability. A project generally uses **one primary styled interaction language**; a headless base plus custom theme is a coherent stack, not two competing styled libraries.

**Mixed controls in existing products must also pass [Component Consistency & Context-Aware Selection](component-consistency-and-selection-gate.md).** Inventory actual imports, shared wrappers and equivalent native \`<select>\` controls and their expanded surfaces—not only installed packages. Decide the inherited design language before unifying roles and tokens; do not replace the whole library for one control. Consider product type, approved aesthetic, accessibility, interaction complexity, dependencies/SSR/bundle size and migration cost. Native option menus may be OS-rendered; CSS on a closed trigger does not prove the popup matches.

## Gate A — Build necessary shared controls before multiplying business pages

Before bulk implementation, create a small component Showcase/development route using the **actual selected library**, covering the high-risk controls needed for this task (e.g. Select, DropdownMenu, Button, Checkbox/Radio, Switch, Dialog):

- **Select:** Value, placeholder, options, selected, disabled, clear when supported, long options, empty options, placement and viewport boundaries.
- **Combobox/MultiSelect:** Search, filtering, selection, multi-value removal, no results, keyboard and async loading. Do not misrepresent ordinary Select as searchable.
- **DropdownMenu:** An *action menu*, not a list of data values. Check open/close, highlight, destructive/disabled actions, Escape, outside click and overflow positioning.
- **Button:** Meaningful primary/secondary/quiet/danger roles; loading, disabled, focus, pressed, icon spacing, long labels and compact layout without character-by-character wrapping.
- **Checkbox/Radio/Switch/Tabs:** Checked/selected/indeterminate where applicable, keyboard focus, distinct hover/selection states, single/multiple-choice behavior.
- **Dialog/Popover/Tooltip:** Keyboard, accessible names, placement, focus entry/exit, closing/returning focus, scrolling and touch viewport bounds.

Use official library components or mature headless primitives for state, ARIA, keyboard, overlays, focus and form associations. The Agent provides a brand theme, composition and needed adapters—not a simplistic handwritten dropdown engine.

### Valid native-control exceptions

\`<button>\`, \`<input>\` and \`<select>\` are not inherently wrong. They may be the best decision for an explicit native-system experience, very simple forms, mobile platform pickers, more reliable native semantics, or strict performance/package-size constraints. But it must be an **intentional product decision**. Verify theme compatibility, focus, error messaging, size, and actual picker appearance/behavior on target devices. Do not use native controls by default just to avoid selecting a library. Do not claim that styling the closed native Select with CSS also produces a fully custom or visually consistent options list.

### Implementations this gate blocks

- Do not substitute \`div + v-if/onClick + position:absolute\` or \`button + ul\` for a mature Select/Menu, unless real platform constraints justify a full accessible focus/keyboard contract.
- Do not reimplement Checkbox/Radio/Switch state and semantics from scratch merely because CSS is convenient.
- Do not vary Button radius, colors, shadows and disabled state on every page. Expose shared variants through the library theme and adapters.
- Do not install two fully styled suites just for the appearance of one Select; theme the existing suite or choose a compatible primitive.
- Do not mistake React Bits/Vue Bits, icon packages or bare Tailwind utilities for a complete accessible form-control library.
- Do not claim a library was adopted when committed code contains no real dependency, import/usage or integration evidence.

## Gate B — Unified theme and component ownership

1. Set typography, dimensions, semantic colors, radius, borders, states, focus, light/dark modes via app-level ThemeProvider/ConfigProvider, CSS variables or the primary library's theme API. Avoid per-page overrides of internal vendor DOM.
2. Only create \`UiButton/UiSelect/UiField/UiDialog\` adapters where shared semantics justify them; forward relevant props/events/slots, controlled values and form submission while preserving library accessibility. **An adapter is not permission to copy the primitive's interaction engine.**
3. Select, Dropdown, Button, Checkbox and Tabs should share coherent heights, typography, horizontal padding, radius systems, icon language and state feedback on a screen. Allow genuine primary/secondary and complexity distinctions; do not make every control an identical pill.
4. Unique interactions not provided by the suite may use a specialist third-party component or a custom implementation only with a recorded reason why reuse does not work, accessibility/performance/permission handling, and a scoped exception. Do not generate unused controls.

**Existing products also require acceptance:** A new component Showcase does not excuse mixed native/vendor controls already in production views. Compare the same-purpose Select/Menu/Field/Dialog in closed/open, selected, keyboard, focus and theme states on actual routes. If native system overlays cannot be inspected, report \`NOT TESTED\`, not a visual pass based on static tokens.

## Gate C — First delivery acceptance, before the user reports defects

Before the first internal review of business pages, **open real feature routes** and interact with the risky controls. Storybook and static screenshots are not sufficient.

| Control | Required visual and behavioral checks |
| --- | --- |
| Select/Combobox | Open width/alignment, stacking, selected vs hover vs focus, long values, clear, arrows/Enter/Esc, keyboard focus, scrolling options |
| DropdownMenu/Popover | Trigger anchor, clipping/edge flipping, width and row height, disabled/danger actions, close/focus return |
| Button/IconButton | Primary/secondary/danger, hit target, icon spacing, duplicate-submission protection during loading, disabled, focus-visible, length and responsive wrapping |
| Checkbox/Radio/Switch/Tabs | Clearly differentiated checked/selected, keyboard path, click target, disabled and error |
| Dialog/DatePicker | Placement, close/focus return, long content, keyboard, unavailable dates/errors, theme and narrow windows |

**Evidence labels:** \`VERIFIED\` requires tests on the actual target route; source/config review is \`STATIC CHECK\`; synthetic gallery-only checks are \`DEMO ONLY\`; unopened pages are \`NOT TESTED\`. Library accessibility claims do not prove integrated application contrast, placement, keyboard behavior or appearance.

**Block first-pass acceptance** while any handwritten fake Select remains, hover and selection cannot be distinguished, Buttons are visually inconsistent across pages, overlays clip, or a core keyboard path is unusable. Fix the primary component and real pages before copying the faulty pattern more widely.

## Maintenance and sources

- \`references/enterprise-ui-library-guide.md\`: Candidates, component coverage and theme integration.
- \`references/framework-support-matrix.md\`: Framework support and library strategy.
- \`references/component-first.md\` and \`references/component-craft-gate.md\`: Component contracts and craft.
- Official Select references: https://reka-ui.com/docs/components/select , https://www.radix-ui.com/primitives/docs/components/select , https://ui.shadcn.com/docs/components/base/select
- UI/primitive APIs evolve. For example, shadcn/ui may offer different implementations using Base UI and Radix. Verify the active project's dependency versions and corresponding official documentation before integrating; do not guess from stale examples.

All examples are generic; no actual user product identifiers or screenshots are embedded.
