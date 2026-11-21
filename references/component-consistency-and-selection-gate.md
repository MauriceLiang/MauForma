# Component Consistency & Context-Aware Selection Gate

**Use for:** New interactive Web products, existing product polish/refactoring, cross-page UI inconsistencies, control-library selection, and visual QA. This gate complements Component Library First; it is not a requirement to install a new library.

## Non-negotiable goal: one coherent interaction language

A project can contain library components, semantic native HTML and specialized widgets. This is not intrinsically wrong: libraries themselves often render native HTML. The defect is **unjustified inconsistency among controls with the same user-facing role**: mismatched typography, density, shape, focus, disabled/error treatment, overlay/menu surface, keyboard interaction, or state feedback. Compare the *whole control experience* and its peers, not just CSS classes, source tags, or library count.

**Native select caveat:** A browser/OS may render the open native select options popup outside the stylable document UI (especially desktop browsers). Styling the closed select via CSS does not guarantee matching options fonts, background, radius, selected state or menu dimensions. Do not promise exact native popup parity from CSS. For a custom-designed product where open-menu consistency is required, prefer an appropriate accessible Select/Listbox/Combobox from the project's primary component strategy. Preserve native controls when deliberate platform behavior or constraints justify them.

## Gate C0 — Investigate the *existing* project before choosing anything

1. Identify product/page modes (Operate / Read / Persuade / Experience), target browsers/devices, visual identity, density, accessibility/localization, performance and dependency constraints, user-approved choices and existing design system. A page can mix modes without mixing arbitrary control skins.
2. Inventory the **real source**, not package.json alone: installed UI dependencies/versions and lockfile; actual imports/usage; providers; token/variable sources; shared wrappers; raw HTML elements; independent CSS controls; headless primitives; custom overlay implementations; and duplicated component families. Categorize by function: value Select, search Combobox, action DropdownMenu, Button, Field, Check/Switch, Dialog/Popover, date picker, etc.
3. Audit the actual rendered UI on affected routes **before any modification**, sampling repeated controls across header, panel, form, dialog and overlay. Check open popups and selected, hover, focus, disabled, error, empty, long-label, dark/light and supported viewport states. UI controls may be styled consistently when closed but diverge when expanded. Do not call an unobserved system popup verified.
4. Map each control family to an actual owner/implementation and source locations. If identical roles have different implementations, classify them as **intentional exception** or **inconsistent drift** using both code and the final user experience. Historical existence is not approval.
5. Optional: use scripts/audit_control_consistency.mjs to find rendered native selects, ARIA selection controls and mixed-source **candidates**. The script cannot identify the actual library, inspect all OS-level option popups, or determine aesthetic quality; it must not auto-migrate controls.

## Gate C1 — Choose the component strategy **for this product**

**Priority order:** explicit user decisions > established coherent design system + real usage > existing primary library/primitive stack > tested compatible additions > new solution. Do not migrate a working project to another library merely because an alternative looks fashionable.

| Context and verified needs | Preferred strategy | Avoid |
| --- | --- | --- |
| Existing project with a broadly adopted compatible styled library | Reuse its components and provider/theme for equivalent controls; replace legacy raw equivalents where allowed | Adding another full styled library for one dropdown |
| Existing project built on headless primitives and bespoke brand tokens | Reuse primitives and shared wrappers, complete missing behaviors with compatible primitives | Mixing in pre-styled enterprise components that break the visual system |
| New/weakly established data-heavy operations, complex forms and tables | Evaluate a framework-compatible complete styled library for coverage, states, i18n, theme and accessibility | Creating every form control from raw clickable elements |
| New consumer, editorial or premium brand experience with custom art direction | Evaluate compatible accessible headless/unstyled components and original token-driven presentation | Imposing a default enterprise skin everywhere |
| Small static page or a few simple fields, performance-sensitive or intentionally platform-native product | Consistent semantic native controls, tested on real target OS/browser, with explicit limitations | Installing a large UI framework by default |
| Existing product with two conflicting styled libraries or unresolved migration | Choose one target design language based on installed usage, control coverage and change risk; migrate scoped families incrementally and isolate interim styles | Deleting working routes or bulk framework migration without authorization |

For each feasible candidate, evaluate **framework and version/SSR support, component and state coverage, approved visual fit, theme customization, accessibility and keyboard behavior, i18n, license, bundle/runtime cost, maintenance and migration effort**. If two options remain equally plausible, explain trade-offs; do not invent numeric compatibility scores. Only use libraries/version APIs confirmed in project dependencies or current official docs. A choice is an implementation decision, not a justification for unapproved redesign/dependency installation.

A project normally has one **primary styled component language**, but multiple specialized or headless building blocks can coexist with a shared theme. Raw HTML for simple semantics is often desirable; making all HTML elements third-party components is **not** the goal. Each exception requires a real user/technical reason.

## Gate C2 — Converge mixed controls without breaking behavior

1. For the *same semantic role*, choose a common source and shared API: reuse primary component, wrap a compatible headless primitive, or deliberately use consistent native controls. Mark each legacy instance as reuse, theme, wrap, replace, or justified exception; avoid changing unrelated routes.
2. Apply **one semantic token layer** to all relevant controls (type, dimensions/density, border, radius, padding, surface, focus, hover, selected, disabled, error and motion), plus consistent label/help/error positioning. Distinct semantic variants are permitted; identical pixel dimensions are not required.
3. Audit **open surfaces** separately from triggers: option rows, checkmarks, option density/typography, popover width, overlay clipping/stacking/scroll, surface colors, focus/keyboard navigation, Escape/Enter, long options and virtualized lists. Do not use a CSS-only imitation of native select options to claim parity.
4. Preserve controlled value, form submission, async filtering, multi-select, a11y names, touch target and real business effects. Select, Combobox and action DropdownMenu are different interaction patterns; do not substitute by visual resemblance.
5. If a library is insufficient, justify a compatible specialist primitive/adapter and its theme integration; do not introduce a competing full styled library by convenience. When permissions prohibit new dependencies, use the best allowed accessible control, document the visible platform limitation, and do not claim visual uniformity that cannot be achieved.
6. When a shared wrapper or theme changes, inspect every affected instance (including existing pages). Do not claim completion after updating one screenshot. Record any explicitly deferred migration and its scope.

## Gate C3 — Real UI verification and truthful reporting

Before declaring a mixed-control design fixed, compare same-function controls at the same viewport/data/state on actual routes. Verify **closed + expanded** state, selected/hover/focus/disabled/error, keyboard and pointer, overlay stacking/scroll, localization, zoom and dark/light modes supported by the app. Native OS popups may require actual interactive device-level inspection beyond DOM screenshots; if inaccessible, report NOT TESTED.

Final compact evidence: product mode/constraints → existing sources and inconsistency → chosen strategy and rejected options → affected controls/files → real-page outcomes → exceptions and untested limitations.

Do **not** pass on a prettified trigger if its open menu still breaks the product's visual or behavioral contract. Static import checks or a synthetic lab are not real-page verification.

Related: references/component-library-first-gate.md, references/enterprise-ui-library-guide.md, references/component-first.md, references/browser-qa-protocol.md.
