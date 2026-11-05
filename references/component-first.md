> v4 范围提示：本 Skill 以 Web 前端为直接适用对象。旧版本个别原生 SwiftUI/AppKit 条目仅供设计语义迁移参考，不用于要求安装或生成原生 UI 源码。

# Component-First：先组件，再业务页面

本 Skill 最重要的工程约束：**产品界面不是由几十个独立设计的页面拼出来的，而是由一套视觉及行为一致的组件组合出来的。**

## v6.17 · Icon 也是组件先行的设计产物

在大量布局复制之前按 `references/icon-art-direction-gate.md` 审阅现有/候选图标库，确认一级导航与高频操作各自的对象/动作语义，再在 Gallery 中展示真实尺寸的整组 Icon 与 Label/Badge/Active/Focus/Theme。优先一个主 UI 图标家族，尺寸/轮廓/光学重量一致；必要时为品牌、插画或特殊领域使用受控例外。图标可以省略，但不能因为有 `Icon` 组件就填充抽象或无关图形。

## v6.16 · 同级组件之间的空间由布局负责

按 `references/semantic-spacing-rhythm-gate.md` 先判断当前组件间属于内部从属、同级并列、跨区章节或连体结构；`Card` 只负责自己内容的 padding，不应该因为缺少 Layout/Stack 规范就让两个独立模块紧贴。共享 `PageSection/PanelGrid/Stack` 负责 spacing tokens 和响应式 gap，且上下/左右都要检查，不能只保证 CSS Grid 对齐；不要把全部同类组件一律加固定 margin。不同产品可有不同密度和艺术留白。

## v6.13 · 结构与尺寸先于视觉皮肤

在为每个页面组合 Card/Table/Button 前按 `references/surface-architecture-gate.md` 选主容器层级；不能把独立内容区全部包在同一巨型 Card 里才算“组件化”。使用 `references/control-geometry-gate.md` 确保按钮、Tab、Badge、工具条及行操作在父容器变化时完整可读；控件短标签不逐字堆叠，窄屏改成整体换行、结构重排或可访问菜单，所有状态须回归。

## v6.12 · 组件实现前必须先做视觉职责设计

所有 Web 项目通用：先读 `references/perceptual-hierarchy-gate.md` 确定真正的主/次信息，再读 `references/component-craft-gate.md`，对高频控件审查职责、结构、交互频率、视觉处理、状态与边界。仅实现一套可复用的 Button/Badge 并不意味着组件具有设计质量，多个“美观”原语组合也可能形成凌乱页面。避免把设计方向变成全站一套圆角/pill；不要在营销与阅读页面套用工作台密度。

## 为什么必须先做组件？

同样的“保存”按钮，如果设置页写 `border-radius:8px`、编辑弹窗写 `12px`、首页写 `999px`，即使每一处单独看来都还行，整体仍会割裂。AI 在每张页面独立写 JSX/Vue/CSS 时尤其容易造成此问题。组件优先能把颜色、间距、圆角、交互状态、键盘行为和修复入口收敛到一个地方。

**不是必须从零造轮子**：如果已有 shadcn/ui、Reka UI、Radix、Ant Design、原生 SwiftUI Control，先评估并主题化其现有实现。只有当功能或视觉不足且确有需求时，再封装或新增。

## 开发门禁（强制）

1. **盘点**：列出页面所需 UI pattern，标记 `reuse / wrap / implement / defer`，识别已有组件、现有状态管理和交互依赖。
2. **冻结 token**：确定字体级差、颜色语义、密度模式、圆角层级、阴影和 motion；建立真实共享 token 文件。
3. **最小组件集**：先完成本轮真正用到的 Button、Input/Field、Panel、Status、导航、弹窗等。创建稳定的 props/events/slots API，避免暴露直接 `style` 作为唯一变体入口。
4. **组件展示 / QA**：有可运行的组件 gallery / story，列出至少 normal、hover、focus、disabled、error、loading 等适用状态，使用长中文、英文、数字、空值测试排版。
5. **页面组合**：只使用共享组件构造业务区域。布局层可自定义 grid/flex，但不在 `.settings button` 或某页 `<style scoped>` 中重复定义按钮颜色/圆角/阴影。
6. **回归修正**：组件视觉问题修一次，所有引用处随之改变；新需求先考虑新增 semantic variant，而不是在某页 `!important` 覆盖。

**可例外**：不进入产品的临时探索原型；一次性特殊可视化；原生系统强制控件。例外必须明确，不能用来绕过成品标准。

## 推荐的组件层次

```
src/
  styles/
    tokens.css              # 单一语义色彩、间距、排版、圆角等设计变量
    themes.css              # 主题映射，允许多个配色，不允许逐页改色
    foundation.css          # reset / 全局字体 / focus / motion
  components/
    ui/                     # 无业务耦合，所有页面复用
      UiButton.vue
      UiField.vue
      UiPanel.vue
      UiDialog.vue
      UiNavItem.vue
      UiStatusBadge.vue
      UiPageHeader.vue         # 用于管理/列表/设置等任务型页面，不是营销 Hero
      UiFeedback.vue
    patterns/               # 由基础组件组合的复合模式
      ConfirmAction.vue
      SearchToolbar.vue
      DataEmptyState.vue
  features/
    servers/
      components/           # 仅服务此功能，但仍从 ui/ 组合
      views/
    settings/
      views/
  playground/               # 本地组件展示或项目已有 Storybook
```

命名和目录可根据项目框架调整；**稳定分层及单一组件所有权**才是强约束。

## API 合同样例

| 组件 | 最低配置 | 必须处理的状态 | 不要做的事 |
| --- | --- | --- | --- |
| `UiButton` | `variant`, `size`, `disabled`, `loading`, `type`, `click` | hover、active、focus-visible、disabled、loading | 在每个页面重新写按钮阴影/圆角 |
| `UiField` | `label`, `id`, `value`, `hint`, `error`, `disabled` | focus、invalid、required、disabled | 只改红色边框不显示错误说明 |
| `UiPanel` | `variant`, `padding`, `header` slot | default、inset、outlined | 把所有内容都装进悬浮大卡片 |
| `UiDialog` | open/title/close/confirm | loading、error、Escape、焦点恢复 | 自己用 `div` 拼弹窗却不处理键盘焦点 |
| `UiNavItem` | to/active/icon/label | hover、active、focus | 只靠颜色暗示所在页面 |
| `UiStatusBadge` | semantic tone/size/label | neutral/success/warning/danger | 用主题强调色代替错误、成功颜色 |
| `UiPageHeader` | title/description?/breadcrumbs?/actions/density | compact/comfortable、长标题、窄屏布局 | 每页重新做“英文小字 + 巨型标题 + 宣传口号” |
| `UiFeedback` | kind/title/action | empty/loading/error/retry | 只显示 spinner 不说明发生了什么 |

可直接使用 `assets/component-contracts.json` 作为这些合同的基础；不要把示例清单误认为每个小项目都需要实现所有组件。

## 页面标题也是一个需要统一的组件模式

当项目包含多个后台、列表、设置或详情页面时，应优先建立/复用 `UiPageHeader`。默认只呈现任务标题、可选增量说明、真实面包屑和关联动作。`UiPageHeader` 不是 marketing Hero；不应该自动生成 eyebrow、小英文、渐变标题、口号和超大留白。

```vue
<UiPageHeader title="用户管理" density="compact">
  <template #actions>
    <UiButton variant="primary" @click="createUser">新增用户</UiButton>
  </template>
</UiPageHeader>
```

详细反面案例与例外规则：[page-header-antipatterns.md](page-header-antipatterns.md)。

## 变体 API（Vue 示例）

**差：每个页面创造自己的按钮样式**

```vue
<button class="save-btn" style="background: #6941c6; border-radius: 12px;">保存</button>
<!-- 另一页面又写 .confirm-btn { background:#0071e3; border-radius:8px } -->
```

**好：统一封装、明确意图**

```vue
<UiButton variant="primary" :loading="saving" @click="save">保存</UiButton>
<UiButton variant="secondary" @click="cancel">取消</UiButton>
<UiButton variant="danger" @click="deleteItem">删除</UiButton>
```

`UiButton` 自己负责 variant → token、focus-visible、disabled/loading 状态。绝不要把 `:loading="true"` 仅做动画却仍能重复点击。

## 推荐组件状态矩阵

| 状态 | 按钮 | 输入控件 | 导航 | 弹窗 |
| --- | --- | --- | --- | --- |
| default / hover | 背景对比与手型 | 细边框/聚焦前后区别 | 活跃行反馈 | 正常结构 |
| keyboard focus | 可见 focus ring | focus ring + 正确 label | 聚焦目标清晰 | 焦点受控 |
| disabled | 不触发 + 标识 | 不可编辑 + 视觉反馈 | 不可操作或不显示 | 禁用主操作 |
| loading | 防重提交 + 明确反馈 | 视场景禁用 | 避免误导航 | 按钮进度/状态 |
| error | 操作结果解释 | 错误文字 + aria-invalid | 必要时显示失败信息 | 保留输入和错误信息 |
| content overflow | 长文换行策略 | 长文本正常显示 | 可截断并有完整提示 | 可滚动而不裁切 |

## 工作量控制

- 组件优先 **不等于第一天制造 50 个原子组件**。按当前页面的真实需求优先化，构建一个稳定的最小集合。
- 有现成 Reka UI / Radix primitives 时，不重写无障碍逻辑；封装主题层即可。
- 出现第二处相同的 UI pattern 时，必须评估抽象成公共组件。最好在**第一处的设计阶段**就识别可复用模式。
- CSS tokens 不等于组件；必须同时有共享样式和规范化交互 API。

## Gate B 自检

- [ ] 组件清单中每个条目都有 reuse / adapt / build 决策。
- [ ] 同类控件只有一个样式所有者；不存在多个非语义重复变体。
- [ ] 组件展示页包含真实文本和状态，至少做过一轮视觉审查。
- [ ] 所有组件使用 token，并为键盘、错误、禁用和动态内容提供路径。
- [ ] 页面不会为了挽救“局部好看”使用大量 `!important` 覆盖基础组件。
- [ ] 任务型页面统一复用 PageHeader 模式，未把营销式 Hero、无意义英文小字、巨大空白变成固定模板。

## 桌面工作台组件（v6.3）

在实际项目需要时优先从现有 UI 库映射/封装 `UiSidebar / UiRecentItem / UiTopbar / UiDataTable / UiTabs / UiSearch / UiSplitPane`，各自职责与交互不同，不要为了统一而将所有对象列表都强行变成与主导航相同的 active 卡片。组件 QA 应分开记录 hover、selected、focus-visible、disabled、long-content、dark/light、collapsed 等状态，尤其不能删除键盘焦点来追求“克制”。参考 `references/sidebar-navigation-design.md`、`references/workspace-component-refinement.md` 与 `assets/sidebar-refinement-gallery.html`。这些是设计规范与概念示例，不是可以直接跨框架复制的生产组件源码。
