# Mature Web Component Libraries — Product-Fit Selection and Theme Integration

> **Rule:** When pages need interactive controls, reuse mature styled components or accessible primitives by default. **No specific library vendor or number of packages is mandatory**. Preserve the established primary solution in an existing project; in a new project, Agent chooses and **actually adopts** an appropriate approach. Start with component-library-first-gate.md. The candidates below are **not an installation checklist**.

## 1. Framework/ecosystem map

| Solution | Framework | Architecture | Strengths | Constraints and tradeoffs | Official docs |
| --- | --- | --- | --- | --- | --- |
| **Ant Design (antd)** | React / Next | Fully styled enterprise components | Form validation, Table, DatePicker, Tree, Upload, complex back offices, localization and Theme Tokens | Strong built-in design language; evaluate migration cost; avoid mixing another styled core UI system | https://ant.design/docs/react/introduce |
| **Ant Design Vue (ant-design-vue)** | Vue 3 / Nuxt | Independent Vue implementation of Ant Design principles | Tables, forms, modal, paging, trees, themes, i18n | **Not React antd installed in Vue**; verify SSR | https://www.antdv.com/docs/vue/introduce |
| **Element Plus** | Vue 3 | Complete styled UI suite | Enterprise/admin forms, tables, dates, Tree, theme customization | Abstract default theme consistently; do not also introduce AntD form styling per page | https://element-plus.org/ |
| **Naive UI** | Vue 3 | Full components and theme system | Forms, data workbenches, fine-grained theming | Check target coverage and ecosystem | https://www.naiveui.com/ |
| **Arco Design** | React / Vue (distinct packages) | Mature styled components and admin ecosystem | Dashboard/Pro tools, business components, visual consistency | React/Vue APIs are not interchangeable; verify versions | https://arco.design/ |
| **PrimeVue** | Vue | Styled/unstyled modes, design tokens | Extensive components, tables/forms and highly adjustable themes | Choose Styled vs Unstyled coherently at architecture level, not differently per route | https://primevue.org/ |
| **PrimeReact** | React | Styled/unstyled enterprise UI | Broad form/data components | Match theme and established visual language | https://primereact.org/ |
| **MUI Material UI** | React | Complete Material Design system | Complex admin products, mature design and large ecosystem | Material style may not fit product; some MUI X advanced packages have separate licenses | https://mui.com/material-ui/ |
| **Mantine** | React | Complete components, hooks and themes | Fast app development, cohesive themes and rich hooks | Separate design system; avoid making it a second primary styled library beside Ant Design | https://mantine.dev/ |
| **shadcn/ui** | React | Project-owned copied components + headless primitives | Highly controllable brand system and composable source | App maintains source; not a full instant business suite | https://ui.shadcn.com/ |
| **shadcn-vue + Reka UI** | Vue 3 | App-owned components + unstyled accessible primitives | Highly consistent bespoke design language | App must build higher-level DataTable/Form patterns | https://www.shadcn-vue.com/ ; https://reka-ui.com/ |
| **Angular Material / NG-ZORRO / PrimeNG** | Angular | Angular-specific suites | Admin work, complex forms and data tools | Do not transplant React/Vue components unchanged | https://material.angular.dev/ ; https://ng.ant.design/ ; https://primeng.org/ |

## Select from first-pass interaction complexity, not "admin" alone

- **Out-of-box styling and complete controls:** Evaluate framework-compatible Element Plus, Ant Design/Ant Design Vue, Naive UI, Mantine, MUI, Prime and peers. Real Select, Dropdown, Checkbox, Radio, Button, Switch and Dialog states come from mature components.
- **Distinctive brand and ownership of source:** Consider shadcn/ui with the selected Base UI or Radix primitives, or shadcn-vue + Reka UI. Flexible appearance means more project maintenance; it does **not** justify reimplementing Select keyboard/focus behavior.
- **Existing stack:** If a primary library is actually installed and used, theme its Tokens/Provider/shared wrappers before introducing a competing styled library.
- **Very few operations:** Semantic native button/input/select may be enough, if intentionally chosen and **tested**; native must not be a shortcut for skipping the component decision.
- **Separate roles:** Select chooses a fixed value; Combobox supports input/search selection; DropdownMenu opens **actions**. Do not substitute based on their similar arrow icon.
- **Evidence of first-pass integration:** Show the selected solution, actual imports/instances, theme entry point and tested default/open/selected/disabled/focus/error/loading states **as applicable**. A written recommendation alone is not implementation.

## Audit inherited consistency and product fit before selection

If the existing app mixes native HTML, a styled library and headless primitives, use component-consistency-and-selection-gate.md to inspect equivalent controls, wrappers and **real open state**. A data-heavy operation tool and a distinctive consumer/brand product can correctly choose different routes; the candidate libraries are tools, **not mandatory visual skins**. Converge on the existing broadly used system and Tokens where possible. For new builds, choose by user task, approved design direction, controls/coverage, framework/SSR, accessibility, runtime weight and maintenance. Platform-native controls may be justified; do not install dependencies merely to eliminate native HTML tags.

## 2. Ant Design React — what the suite provides

- **General:** Button, Typography, Icon (separate package when needed), Space/Flex/Divider; align Button states, type hierarchy and spacing.
- **Layout/navigation:** Layout, Grid, Menu, Breadcrumb, Tabs, Steps, Pagination; convey navigation and flow rather than duplicating decorative eyebrows.
- **Input:** Form, Input, Select, AutoComplete, DatePicker, TimePicker, Switch, Checkbox, Radio, Upload; real validation, disabled/errors and submission feedback.
- **Data:** Table, Descriptions, List, Tree, Tag, Badge, Statistic, Calendar, Card; real sorting/filtering/permission data and content density.
- **Feedback/overlays:** Modal, Drawer, Notification, Message, Popconfirm, Tooltip, Popover, Progress, Spin, Skeleton, Empty, Result; test actual pending/empty/error/success states.
- **Theme:** Centralize with ConfigProvider theme.token and optionally theme.components; use official dark/compact algorithms where appropriate. **Check official types/APIs against the installed antd major version.**
- **Advanced extensions:** Ant Design Pro Components include richer business patterns, potentially with size/behavior cost. Installing antd does **not** mean every Pro component is installed.

### Example React theme adapter — verify against installed version

~~~tsx
import { ConfigProvider, theme, Button } from 'antd'

const brandTheme = {
  token: {
    colorPrimary: '#2665D9',
    borderRadius: 8,
    fontFamily: 'Inter, -apple-system, BlinkMacSystemFont, sans-serif',
  },
  algorithm: theme.defaultAlgorithm,
}

export function UiProvider({ children }: { children: React.ReactNode }) {
  return <ConfigProvider theme={brandTheme}>{children}</ConfigProvider>
}
~~~

This is an **architectural illustration**, not a requirement for the sample HEX in every product. Map the **actual** semantic tokens to Ant Design; share Button/PageHeader/DataTable wrappers instead of patching .ant-btn separately per page.

## 3. Ant Design Vue — component roles and theme

- Representative components: a-form, a-input, a-table, a-select, a-date-picker, a-tree, a-modal, a-drawer, a-pagination, a-config-provider.
- Provides Vue-native enterprise forms, feedback, navigation, dialogs and data display—not React antd installed in a Vue project.
- Vue uses props, slots, v-model and emits; do not copy React JSX/hooks as-is.
- Use a-config-provider theme.token and existing app Tokens at a common root, following documentation for installed version.

### Example Vue theme adapter — verify against installed version

~~~vue
<script setup lang="ts">
const uiTheme = {
  token: {
    colorPrimary: '#2665D9',
    borderRadius: 8,
  },
}
</script>

<template>
  <a-config-provider :theme="uiTheme">
    <router-view />
  </a-config-provider>
</template>
~~~

This snippet assumes **Vue Router**; **Nuxt must replace router-view with NuxtPage** and follow its SSR/component style injection rules.

## 4. Component-first contracts, not primitive reimplementation

Even with a complete suite like Ant Design or Element Plus, a product may need **thin business-oriented Ui adapters**. They must not reimplement the underlying keyboard, focus and overlay engines.

| Shared adapter | What it unifies | What it must not do |
| --- | --- | --- |
| UiButton | Primary/secondary/danger, size, loading/disabled/focus-visible | Each page independently changes padding/color |
| UiField | Label/help/error/required, field height and validation | Replace real validation with fake field feedback |
| UiDialog | Open/close, focus return, overlay, Escape, size and responsive | Invent a second DOM dialog instead of accessible library primitive |
| UiPageHeader | Semantically valid heading, necessary description, one primary action, actual breadcrumbs | Auto-create English eyebrow + giant Chinese title + meaningless blank space |
| UiDataTable | Columns, row actions, empty/pending, paging/sort/filter, virtualization choice | Wrap every table in giant Cards or build inaccessible clickable divs |
| UiFeedback | Semantics/copy for Toast/Alert/Confirm/Empty/Result | Show same bright color for error and success, omit actual reason |
| UiNavigation | Menus, Breadcrumbs, Tabs, responsive navigation and authorization | Keep two competing navigation designs |
| UiThemeProvider | Own project Tokens mapped to library Theme Tokens | Install another complete styled library merely to change colors |

## 5. How to choose the primary library for an enterprise workspace

1. **Existing project:** Prefer established primary suite. Migrate only with evidence that accessibility, component coverage or maintenance cannot meet the task.
2. **New React operations:** For complex Form/Table/DatePicker out of the box, evaluate Ant Design, MUI, Mantine and PrimeReact; for source-controlled brand design, shadcn/ui + compatible primitives (potentially separate table implementation).
3. **New Vue operations:** Evaluate Ant Design Vue, Element Plus, Naive UI, Arco Vue, PrimeVue; for deeply custom style, shadcn-vue + Reka UI.
4. **Complex data grid:** Separately evaluate AG Grid, TanStack Table or primary suite against tree/inline editing/frozen columns/virtualization/keyboard/performance. Do not reimplement a grid solely because it looks more fashionable.
5. **SSR and cross-device:** Check actual Next/Nuxt versions, SSR boundaries, CSS injection and client ownership; not all libraries support the same constraints.
6. **Allowed mixed-library exceptions:** Staged migration of a legacy app or a uniquely necessary specialist control, **with wrapper, style isolation, theme mapping, size impact and migration plan**. Do not install because one option happens to look nice.

## 6. Pair enterprise primitives with creative animation components

- Workbench UiButton/UiTable/UiForm should be owned by a stable enterprise library. Motion/CSS may enhance feedback lightly; **React Bits/Vue Bits are not replacements for foundational business controls**.
- SaaS marketing pages may use React Bits/Vue Bits Aurora or Hero Text, while the signed-in console shares brand Tokens but favors compact, readable operational components.
- Different sections may have different motion intensity; branding, type, icons and copy should remain identifiable. Do not introduce GSAP throughout operational routes just because a creative marketing widget happens to depend on it.

## 7. Anti-patterns and hard prohibitions

- **Bad:** antd Button + MUI TextField + Element Plus Dialog mixed across frameworks. **Good:** a framework-native primary solution with justified specialist exceptions and shared Tokens.
- **Bad:** Every route writes !important against Ant Design internals. **Good:** ConfigProvider, thin Ui adapters and scoped style customization.
- **Bad:** Giant marketing H1 atop a dense list page. **Good:** Compact PageHeader and reachable search/filter/actions.
- **Bad:** Spotlight/WebGL particles on every administrator Card. **Good:** Motion supports meaningful hover/focus/state and hierarchy.
- **Bad:** A creative demonstration Button substitutes for real loading/disabled. **Good:** States, keyboard, errors and permission logic first.
- **Bad:** Forcing one library to own all layout, scroll, drawers, plots and drag behaviors. **Good:** Define UI/data/chart/drag boundaries separately.

## 8. Official references

- React Ant Design: https://ant.design/docs/react/introduce and https://ant.design/docs/react/customize-theme
- Ant Design Vue: https://www.antdv.com/docs/vue/introduce and https://www.antdv.com/components/config-provider
- Element Plus: https://element-plus.org/en-US/guide/design.html
- Arco Vue: https://arco.design/vue/en-US/docs/start
- PrimeVue: https://primevue.dev/theming/styled/ and https://primevue.dev/theming/unstyled/
- MUI: https://mui.com/material-ui/getting-started/
- Mantine: https://mantine.dev/
- Angular NG-ZORRO: https://ng.ant.design/docs/introduce/en
