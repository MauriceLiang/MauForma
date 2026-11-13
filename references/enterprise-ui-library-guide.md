# 成熟 Web 组件库选型与主题集成

> **原则**：当页面需要交互控件时，复用成熟库/可访问原语是默认实施路径；**库的品牌和数量不是强制指定**。优先继承现有主库；新项目由 Agent 自主选择并真正使用。先读 [Component Library First](component-library-first-gate.md)。以下候选列表不是安装清单。

## 1. 框架与生态地图

| 方案 | 框架 | 架构类型 | 特长 | 代价与注意事项 | 官方文档 |
| --- | --- | --- | --- | --- | --- |
| **Ant Design (`antd`)** | React / Next | 完整有样式企业组件库 | 表单校验、Table、DatePicker、Tree、Upload、复杂管理系统、国际化、主题 Tokens | 自带完整设计语言，改造成本要评估，不能和另一套成熟有样式 UI 核心组件随意混用 | https://ant.design/docs/react/introduce |
| **Ant Design Vue (`ant-design-vue`)** | Vue 3 / Nuxt | Ant Design 规范的 Vue 实现 | 表格、表单、弹窗、分页、树、主题与国际化 | 独立 Vue 实现，**不是把 React `antd` 直接安装到 Vue**；SSR 需核查 | https://www.antdv.com/docs/vue/introduce |
| **Element Plus** | Vue 3 | 完整有样式组件库 | 国内后台项目、表格、表单、日期、Tree、主题覆盖 | 主题默认视觉要统一抽象；不要同页再引 AntD 表单样式 | https://element-plus.org/ |
| **Naive UI** | Vue 3 | 全量组件与主题方案 | 企业表单、数据工作台、细粒度主题控制 | 适配目前项目的组件覆盖与生态 | https://www.naiveui.com/ |
| **Arco Design** | React / Vue（分别安装） | 成熟组件库+企业后台生态 | Dashboard/Pro 项目、业务组件、主题一致性 | React/Vue 包与 API 不同；确认现有版本 | https://arco.design/ |
| **PrimeVue** | Vue | 有样式/无样式双模式、设计 tokens | 丰富组件、表格/表单及强定制主题 | Styled/Unstyled 应在架构层确定，不逐页乱切 | https://primevue.org/ |
| **PrimeReact** | React | 有样式/无样式企业组件 | 大量表单与数据展示控件 | 配套风格和现有视觉一致性 | https://primereact.org/ |
| **MUI Material UI** | React | Material Design 完整库 | 复杂中后台、设计语言成熟，生态大 | Material 视觉不一定符合品牌；部分高级 MUI X 产品单独许可 | https://mui.com/material-ui/ |
| **Mantine** | React | 完整组件 + hooks + 定制主题 | 业务页面开发速度、统一主题、丰富 hooks | 属于另一套设计系统，避免和 Ant Design 并列成为“双主库” | https://mantine.dev/ |
| **shadcn/ui** | React | 项目内复制组件 + headless 原语 | 高自由度自建视觉系统、维护源码、可组合组件 | 维护责任在项目；不是完整即装即用的业务框架 | https://ui.shadcn.com/ |
| **shadcn-vue + Reka UI** | Vue 3 | 项目内组件 + 无样式可访问原语 | 高度统一自有设计语言 | 需自行建立业务复合组件，如 DataTable 与 Form | https://www.shadcn-vue.com/ · https://reka-ui.com/ |
| **Angular Material / NG-ZORRO / PrimeNG** | Angular | Angular 原生组件套件 | 企业后台、复杂表单与数据工具 | 不要拿 React/Vue 组件源码套用；遵循 Angular 生态 | https://material.angular.dev/ · https://ng.ant.design/ · https://primeng.org/ |

## 先根据首版交互复杂度选择，而不只是为后台选库

- **开箱即用、视觉规范完整**：按实际框架优先评估 Element Plus / Ant Design / Ant Design Vue / Naive UI / Mantine / MUI / Prime 等有样式主库，能够直接提供 Select、Dropdown、Checkbox、Radio、Button、Switch、Dialog 等完整控件和状态。
- **独特品牌视觉、组件源码可控**：可选 shadcn/ui + Base UI 或 Radix、shadcn-vue + Reka UI。它们允许定制外观但需要项目维护组件代码；不得因为外观灵活，就退回手写 Select 的键盘/焦点逻辑。
- **既有技术栈**：如果主库已安装并真实使用，优先用它解决问题；审美不够时先修改主题 Token、全局 Provider 和公共组件，而不是再引入第二套有样式 UI。
- **只需少量原生操作**：可用原生 button/input/select，但必须是有意选择并实际验收，不是为了跳过组件方案。
- **组件职责区别**：Select 是选择固定数据值；Combobox 是可输入搜索选择；DropdownMenu 是打开动作菜单；不应因为外观都有箭头就互相代用。
- **第一版实施证据**：说明选定的库、真实导入/组件实例、主题接入点，演示所需控件的 default/open/selected/disabled/focus/error/loading 状态；只写推荐方案不算完成。

## 2. Ant Design React：具体包含什么？

- **通用**：Button、Typography、Icon（独立包按需）、Space/Flex/Divider；统一按钮状态、文字层级与操作间距。
- **布局与导航**：Layout、Grid、Menu、Breadcrumb、Tabs、Steps、Pagination；负责菜单层级和页面流程，而不是堆叠重复小标题。
- **数据录入**：Form、Input、Select、AutoComplete、DatePicker、TimePicker、Switch、Checkbox、Radio、Upload；承担校验、禁用、错误提示、提交反馈。
- **数据呈现**：Table、Descriptions、List、Tree、Tag、Badge、Statistic、Calendar、Card；用于复杂数据表达、排序筛选、权限状态与密度管理。
- **反馈/浮层**：Modal、Drawer、Notification、Message、Popconfirm、Tooltip、Popover、Progress、Spin、Skeleton、Empty、Result；必须覆盖真实加载/空/错/成功状态。
- **主题**：`ConfigProvider` 集中统一 `theme.token`，必要时 `theme.components` 细化；可借助官方暗色/紧凑算法；**以项目所用 antd 主版本官方类型为准**。
- **扩展**：Ant Design Pro Components（例如更丰富的业务表格/表单）是另一个层次，先评估功能和体积，不能假定安装 antd 就自动有全部 Pro 功能。

### React 主题接入示意（需根据版本核对）

```tsx
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
```

以上是架构示例，不是规定所有项目必须使用该色值。应用自己的语义 tokens 映射到 antd；统一 Button、PageHeader、DataTable 等封装供业务使用，不要所有页面分别覆盖 `.ant-btn`。

## 3. Ant Design Vue：具体包含什么？

- **同类能力**：`a-form`、`a-input`、`a-table`、`a-select`、`a-date-picker`、`a-tree`、`a-modal`、`a-drawer`、`a-pagination`、`a-config-provider` 等，适合 Vue 企业管理系统。
- **主要作用**：在 Vue 工程中提供成熟的表单、反馈、导航、弹窗、数据表与统一主题，而非为 Vue 安装 React 的 `antd`。
- **Vue 组件状态**：使用 Vue props、slots、`v-model` 与 emits；不能直接照搬 React JSX + hooks。
- **主题配置**：`<a-config-provider :theme="{ token: { colorPrimary, borderRadius } }">`，官方文档有示例；在项目根集中设置，搭配应用 tokens。

### Vue 主题接入示意（需根据版本核对）

```vue
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
```

Nuxt 不一定直接使用 `router-view`，这里展示的是 Vue Router 应用；**在 Nuxt 中将子内容换为 `<NuxtPage />`，并遵循组件 SSR 与样式注入建议**。

## 4. 组件优先：具体组件合同（Contract）

即使选择 AntD/Element Plus 等完整库，也需要设计团队自己的 `Ui` 适配层，**不是重复实现底层交互**：

| 共享组件 | 统一什么 | 不应该做什么 |
| --- | --- | --- |
| `UiButton` | 主要/次要/危险、size、loading、disabled、focus-visible | 每页自行修颜色和 padding |
| `UiField` | label/help/error/required、输入高度与验证反馈 | 禁用真实表单校验改写一个假校验 |
| `UiDialog` | 开闭、焦点回收、遮罩、Esc、尺寸与响应式 | 自己再写一个 DOM dialog 代替成熟库 |
| `UiPageHeader` | 语义标题、必要描述、唯一主操作、面包屑（确有层级时） | “英文 Eyebrow + 80px 中文标题 + 大空白” |
| `UiDataTable` | 列定义、行操作、空态、loading、分页/排序/筛选、虚拟滚动选型 | 所有表格用大卡片包裹或做成无键盘操作的 div |
| `UiFeedback` | Toast/Alert/Confirm/Empty/Result 的语义与文案 | 成功失败都用同一亮色、不显示错误原因 |
| `UiNavigation` | 菜单、Breadcrumb、Tab、Responsive layout、权限过滤 | 同时保留两套不同风格的导航体系 |
| `UiThemeProvider` | 自有 tokens ↔ 库的 theme token 映射 | 为配色引入第二套完整组件库 |

## 5. 如何选一个后台主库（不是越多越好）

1. **已有项目**：优先用现有主库。除非证据显示可访问性、组件覆盖或维护成本无法满足，才考虑换库。
2. **新 React 企业后台**：需要开箱即用复杂 Form/Table/DatePicker，优先评估 Ant Design / MUI / Mantine / PrimeReact；需要自定义视觉与源码控制，选 shadcn/ui + primitives（可能需要额外表格方案）。
3. **新 Vue 企业后台**：优先评估 Ant Design Vue / Element Plus / Naive UI / Arco Design Vue / PrimeVue；需高度自定义视觉时，选 shadcn-vue + Reka UI。
4. **复杂数据网格**：性能、树表、编辑、冻结列、虚拟化、键盘支持等要单独评估 AG Grid / TanStack Table / 主库表格能力；不要为了“更好看”从头重写。
5. **跨端/SSR**：严格核对对应版本的 Next/Nuxt SSR 集成、CSS/样式注入和客户端边界；不要推断所有库同样适用。
6. **允许多库共存的例外**：已有业务逐步迁移、单个专业控件确实不可替代；需有封装、CSS 隔离、主题映射、包体积与迁移计划，禁止简单“看到好看就安装”。

## 6. 与创意动画组件如何组合？

- 后台 **`UiButton`/`UiTable`/`UiForm`**：由稳定企业组件库负责；视觉反馈只轻量 Motion/CSS；**不以 React Bits/Vue Bits 重造业务按钮或表格**。
- SaaS 的 **营销官网** 可以采用 React Bits/Vue Bits 的 Aurora / Hero Text；官网登陆后的 **控制台** 仍使用同一品牌 Tokens，但默认使用高可读、紧凑的企业组件。
- 两个站点可拥有不同的动画密度；品牌色、排版、图标、产品文案保持识别一致。不要因为一个创意库使用 GSAP 就在所有后台路由引入其包。

## 7. 反面案例与红线

- ❌ `antd Button` + `MUI TextField` + `Element Plus Dialog` 跨框架乱混；✅ 框架内选择一套主库，特殊控件有明确理由且统一 Tokens。
- ❌ 每个业务页直接给 AntD 内部 DOM 写 !important 覆盖；✅ ConfigProvider + 自家 Ui 适配组件 + 有作用域的样式。
- ❌ 列表页顶部巨大营销主标题；✅ 紧凑 PageHeader + 搜索/筛选/操作一屏可达。
- ❌ 给每个管理卡片放 Spotlight 或 WebGL 粒子；✅ 功能页动效只表达 hover/focus/状态和层次。
- ❌ 以创意演示按钮代替真实表单 loading/disabled；✅ 状态完整、键盘、错误提示和权限逻辑优先。
- ❌ 把所有布局、滚动、Drawer 和图表都强塞一家库；✅ UI、数据、图表和拖拽边界清楚。

## 8. 官方来源

- React Ant Design: https://ant.design/docs/react/introduce · https://ant.design/docs/react/customize-theme
- Vue Ant Design: https://www.antdv.com/docs/vue/introduce · https://www.antdv.com/components/config-provider
- Element Plus: https://element-plus.org/en-US/guide/design.html
- Arco Vue: https://arco.design/vue/en-US/docs/start
- PrimeVue: https://primevue.dev/theming/styled/ · https://primevue.dev/theming/unstyled/
- MUI: https://mui.com/material-ui/getting-started/
- Mantine: https://mantine.dev/
- Angular NG-ZORRO: https://ng.ant.design/docs/introduce/en
