> v4 scope notice: MauForma's direct code rules apply to **Web frontends**. Historical SwiftUI/AppKit notes are transferable design semantics only, not instructions to install or generate native UI.

# Component-First — Components Before Business Pages

The central engineering constraint: **A product UI is not dozens of separately designed pages; it is an assembly of components with coherent visuals and behavior.**

## v6.18 — Learn component proportions from examples, not identifiable layouts

User-authored references may help identify useful type size, icon shape, row height, table density, selection backgrounds and container relationships. Never paste user screenshots, fields, logos, domains or real datasets into public component samples/Storybook. Invent synthetic subjects and interactions instead. See `references/design-reference-learning-gate.md`. The clean-workspace language in `references/clean-enterprise-design.md` is an **optional style**, not a default for portfolios, marketing or reading.

## v6.17 — Icons are part of the component-first system

Before multiplying layouts, follow `references/icon-art-direction-gate.md`: identify actual objects/actions for high-frequency controls and top navigation; compare compatible icon sets and review the **whole family** at real size in Gallery with Label/Badge/Active/Focus/Theme. Prefer one coherent UI family for optical stroke/fill weight. Documented brand/illustration/specialist exceptions are allowed. Icons are **optional**; do not fill empty spaces with unrelated symbols merely because an `Icon` component exists.

## v6.16 — Layout owns spacing between peer components

Use `references/semantic-spacing-rhythm-gate.md` to classify inside, peer, section and connected relationships. A Card owns internal padding, **not** arbitrary outside spacing to the next Card. `PageSection/PanelGrid/Stack` should own tokens and responsive gaps on **both** axes. Perfect Grid column alignment cannot compensate for zero vertical gaps. Do not give all identical components a mandatory margin. Different products may need different densities and artistic whitespace.

## v6.13 — Structure and geometry precede component skin

Before combining Card/Table/Button on every page, use `references/surface-architecture-gate.md` to choose appropriate surface levels; componentization does not mean putting all content into a giant outer Card. `references/control-geometry-gate.md` keeps Buttons, Tabs, Badges, toolbars and row actions usable as parents shrink. Short action labels must not stack characters; reflow whole controls, reorganize rows or use accessible menus. Test every affected state.

## v6.12 — Assign visual responsibilities before implementation

For all Web projects, read `references/perceptual-hierarchy-gate.md` to find real primary/secondary information, then `references/component-craft-gate.md` for actual component responsibilities, structure, frequency, appearance, states and edge cases. A reusable Button/Badge set alone does not guarantee good design; individually attractive primitives can form a disjointed page. Do not make rounded pills the one site-wide language or apply admin density to marketing/reading.

## Why components first?

If one “Save” Button has radius 8px in settings, 12px in an edit dialog and 999px on the home page, every instance may look plausible alone yet the product is inconsistent. AI-generated JSX/Vue/CSS especially encourages per-route divergence. Shared components centralize colors, spacing, radius, behavior, keyboard contracts and repair points.

**Do not remake mature primitives by default.** When shadcn/ui, Reka UI, Radix, Ant Design or native SwiftUI controls already exist, evaluate and theme appropriately in their respective technical scopes. Only wrap/add when actual requirements justify it.

## Primitive controls should reuse established libraries, not a new homemade Ui*

Any page with complex controls must first follow `references/component-library-first-gate.md`: inventory installed packages and pick one compatible primary solution when needed, then **actually use it** for required Select, DropdownMenu, Button, Checkbox, Radio, Switch and Dialog. Showcases use real vendor components or mature headless primitives, **not** `div + click` to rebuild overlay, focus, ARIA, keyboard and selection logic.

`UiButton`, `UiSelect` and `UiDialog` are business API/theme adapters, **not permission to reimplement accessible interaction engines**. Expressive visual character comes from tokens and shared components, not random page CSS. Native/custom specialist exceptions require a reason and real-route QA.

## Mandatory implementation gates

1. **Inventory and choose a primary solution:** Enumerate required UI patterns, actual installed library/framework, and decide `reuse / wrap / implement / native-exception / defer`. If no mature solution exists, select and integrate one; do not handwrite first.
2. **Freeze tokens:** Establish typographic roles, semantic colors, density, radius, shadows and motion in one real shared token source.
3. **Minimum needed set:** Build only required Button, Select, DropdownMenu, Input/Field, Checkbox, Dialog, Panel and Status with the chosen library/primitives. Stable props/events/slots API; no direct per-page `style` as the only variant control.
4. **Gallery / QA:** Maintain a working component gallery/story for applicable normal, hover, focus, disabled, error and loading; use long Chinese/English, numbers and empty examples to test layout.
5. **Business composition:** Compose pages from shared components. Grid/Flex layouts may be custom, but per-route `.settings button` or `<style scoped>` must not re-author foundational colors/radius/shadows.
6. **Regression:** Fix a shared component once for all callers. New needs should first consider a semantic variant, not per-page `!important` patching.

**Valid exceptions:** Temporary exploration that will not ship; one-off specialist visualization; platform-mandated native controls. Exceptions must be explicit and cannot bypass product acceptance.

## Suggested component ownership structure

```text
src/
  styles/
    tokens.css              # Semantic color/spacing/type/radius source
    themes.css              # Central theme mapping, multiple palettes allowed
    foundation.css          # Reset / global font / focus / motion
  components/
    ui/                     # Business-neutral reusable controls
      UiButton.vue
      UiField.vue
      UiPanel.vue
      UiDialog.vue
      UiNavItem.vue
      UiStatusBadge.vue
      UiPageHeader.vue       # Operational header, not marketing Hero
      UiFeedback.vue
    patterns/               # Compositions of base primitives
      ConfirmAction.vue
      SearchToolbar.vue
      DataEmptyState.vue
  features/
    servers/
      components/           # Feature-only components composed from ui/
      views/
    settings/
      views/
  playground/               # Local component gallery or existing Storybook
```

Paths/names can vary by framework. **Stable layering and one owner per component role** are the actual requirements.

## Example component API contracts

| Component | Minimum inputs | Required states | Anti-pattern |
| --- | --- | --- | --- |
| `UiButton` | variant, size, disabled, loading, type, click | hover, active, focus-visible, disabled, loading | Repeating shadow/radius CSS per page |
| `UiField` | label, id, value, hint, error, disabled | focus, invalid, required, disabled | Only drawing a red border without explaining error |
| `UiPanel` | variant, padding, header slot | default, inset, outlined | Floating giant Card for all content |
| `UiDialog` | open/title/close/confirm | loading, error, Escape, focus return | Hand-built div modal with missing keyboard behavior |
| `UiNavItem` | to/active/icon/label | hover, active, focus | Active route signaled only by color |
| `UiStatusBadge` | semantic tone/size/label | neutral/success/warning/danger | Using brand accent as success/error semantics |
| `UiPageHeader` | title/description?/breadcrumbs?/actions/density | compact/comfortable, long title, narrow view | Eyebrow + huge title + slogan by default |
| `UiFeedback` | kind/title/action | empty/loading/error/retry | Spinner with no useful outcome/state |

`assets/component-contracts.json` can seed this model; **not every small project needs all these components**.

## Page titles are also a reusable component pattern

For multiple admin/list/settings/detail pages, prefer a shared `UiPageHeader` with direct task title, optional incremental help, authentic breadcrumbs and actions. It is **not a marketing Hero** and must not auto-generate English eyebrows, gradient headlines, slogans or huge whitespace.

```vue
<UiPageHeader title="User Management" density="compact">
  <template #actions>
    <UiButton variant="primary" @click="createUser">Add user</UiButton>
  </template>
</UiPageHeader>
```

For cases and exceptions see [page-header-antipatterns.md](page-header-antipatterns.md).

## Vue API variants — synthetic example

**Bad — each route invents a new Button style:**

```vue
<button class="save-btn" style="background: #6941c6; border-radius: 12px;">Save</button>
<!-- Another route .confirm-btn { background:#0071e3; border-radius:8px } -->
```

**Good — consistent wrapper with explicit role:**

```vue
<UiButton variant="primary" :loading="saving" @click="save">Save</UiButton>
<UiButton variant="secondary" @click="cancel">Cancel</UiButton>
<UiButton variant="danger" @click="deleteItem">Delete</UiButton>
```

`UiButton` owns variant → token, focus-visible and disabled/loading behavior. `:loading="true"` must not be a purely visual animation that still permits duplicate submission.

## Suggested state matrix

| State | Button | Field | Navigation | Dialog |
| --- | --- | --- | --- | --- |
| default / hover | Contrast and pointer affordance | Border and pre/post focus distinction | Active-row feedback | Correct base structure |
| keyboard focus | Visible ring | Ring + correctly associated label | Clear focused target | Managed focus |
| disabled | Does not activate, visibly marked | Not editable with feedback | Not actionable or omitted | Primary action disabled |
| loading | Prevent repeat, clear progress/state | Disable when appropriate | Avoid false navigation | Accurate Button feedback |
| error | Explain outcome | Error copy + aria-invalid | Failure context where relevant | Retain draft and useful error |
| content overflow | Long label strategy | Show full field value | Optional truncation plus full label access | Scroll instead of clipping |

## Scope of component work

- Component-first **does not require creating 50 atomic components on day one**. Build a minimal stable set for the real page needs.
- When mature Reka/Radix primitives exist, do not rewrite keyboard/ARIA; theme them.
- When the **second instance** of an identical UI pattern appears, evaluate shared abstraction; ideally recognize reuse at the first design.
- Tokens alone do not equal a component system: shared visual roles **and** normalized interactive APIs are needed.

## Gate B checklist

- [ ] Every item has a reuse/adapt/build decision.
- [ ] Equivalent controls have one visual owner, not redundant unexplained variants.
- [ ] Gallery contains actual copy and states with at least one visual review.
- [ ] Components reference tokens and support keyboard/error/disabled/dynamic content.
- [ ] Pages avoid `!important` patches to “save” one attractive local control.
- [ ] Operational headers share PageHeader and do not make giant marketing Heros/empty English prefixes universal.

## Desktop workbench components (v6.3)

Where actual needs justify them, map or wrap `UiSidebar / UiRecentItem / UiTopbar / UiDataTable / UiTabs / UiSearch / UiSplitPane` from existing libraries. These have different roles; **do not force all object lists to look like the main active navigation Card**. QA covers hover, selected, focus-visible, disabled, long content, dark/light and collapsed separately. Never erase keyboard focus for “restraint.” See `references/sidebar-navigation-design.md`, `references/workspace-component-refinement.md` and `assets/sidebar-refinement-gallery.html`. These are design examples and contracts, **not production source to paste across frameworks**.
