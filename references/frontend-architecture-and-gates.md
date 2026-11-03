# 前端项目架构与验收门槛

## Phase 0：项目现状盘点

- 从 `package.json` / 锁文件 / `vite.config.*` / `next.config.*` / `nuxt.config.*` / `angular.json` 等判断现有架构。
- 列出路由、权限、i18n、数据请求、表单、测试与样式工具；对现有组件做实例检索：button/input/dialog/table/toast/sidebar。
- 报告：已有 / 可复用 / 有缺陷需改造 / 需要新增。不要因为截图里推荐某个库就改变依赖。

## Phase A：设计语言与 Design Tokens

单一来源定义：`--color-bg/surface/surface-muted/text/text-muted/accent/on-accent/border/focus/success/warning/danger`，以及 `--font-*`、`--space-*`、`--radius-*`、`--shadow-*`、`--motion-*`。用语义 token 替换页面级硬编码，浅色/深色各有明确对比度和层级。

**门槛 A**：提供至少两张“组件状态 + 页面主要区域”的预览或可运行展示；没有主题定义，不进入多个页面开发。

## Phase B：组件系统先行

- 原语组件（UI primitives）：Button、Input、Textarea、Checkbox、Select、Dialog、Popover、Tooltip、Tabs、Toast、Loader、Icon。
- 复合组件（composites）：Field + Error、SearchField、DataTable、FilterBar、Pagination、EmptyState、ConfirmDialog、PageHeader、Sidebar、FormActions。
- 页面模板（patterns）：列表筛选页、详情页、创建/编辑页、设置页、向导、内容页、展示型 Hero、商品详情。
- 组件契约：稳定的 props/variants/size/state/slots(or children)/events；视觉 token 集中处理；键盘/焦点/ARIA 语义明确。
- 状态覆盖：normal、hover、pressed、focus-visible、disabled、loading、success、error、empty；重要业务还需 pending/offline/permission denied。
- 组件示例页：至少能查看基础组件的尺寸、变体、状态、长中英文内容，以及暗色主题。

**门槛 B**：业务页不直接重造基础按钮、弹窗、表单字段；多个页面统一依赖共享组件。对于小修小补任务可局部适用，不要求先重建全项目。

## Phase C：真实页面开发

- 页面标题按照产品类型处理：后台优先紧凑、营销首屏可大幅排版。
- 带真实数据口径；提交按钮有 loading、错误、成功、重复提交保护；删除/权限操作处理确认。
- 接口数据与本地状态分离；SSR 页面避免 hydration 失配；图表/编辑器只在需要时客户端加载。
- 动效先选择需要表达的信息：反馈、层级、状态、重排、方向；再选择引擎。交互应可中断且回退可用。

## Phase D：测试与审查

- 单元/组件（Vitest/Testing Library，按项目）与 E2E（Playwright/Cypress，按项目）结合；至少覆盖主线业务。
- 浏览器实际检查：360/390/768/1024/1440 等代表视口（不是固定唯一断点）、深浅模式、触摸、键盘、放大、长文本、错误/加载/空状态。
- 视觉 QA：标题层级、颜色、边界、圆角、间距、图标、按钮优先级、图表标签、表格可读性。
- 动效 QA：prefers-reduced-motion、组件卸载清理、路由快速切换、低性能设备、无动画时核心内容可见。
- 交付：变更清单、设计 Token、组件复用映射、动效选型理由、真实测试证据及未测项。

## 依赖准入门槛（每安装一个库回答）

| 问题 | 说明 |
|---|---|
| 需要解决什么具体缺口？ | 不能只说更炫酷 |
| 原生 CSS / 现有库为什么不够？ | 简单按钮过渡不应额外装 GSAP |
| 是否支持当前框架/SSR/版本？ | Vue 和 React 包不同；确认准确导入与 lifecycle |
| 是否有可访问性、性能、许可证与安全风险？ | 动效不可制造闪烁和可读性问题 |
| 是否有替换与清理方案？ | 组件 ownership 与依赖数尽量收敛 |

## v6.4 · Gate A 的构图先行前置条件

新建页面或重大视觉重设计必须先读取 `references/composition-first-design.md`，登记真实内容与主任务，构思 2–3 种**信息排序或主内容位置真正不同**的灰阶构图，然后才讨论主题 Token 与组件。用户明确参考图、已有确认布局或局部修复可沿用原样并跳过候选比较。工作台若图表空白且无数据状态，不应标记实现完成。Gate D 中如果截图暴露主视觉与任务不匹配，重新进入 Gate A 调整信息架构，而不是持续微调特效。推荐颜色须有来源与语义职责，见 `references/palette-art-direction.md`。

## v6.5 · Gate A 后、Gate B 前确认文字与排版

构图确定后先完成 `references/semantic-copy-hygiene.md` 删除测试，并按 `references/typography-hierarchy.md` 为页面标题、正文、指标、图表轴/图例和辅助来源建立可调整的角色化 Typography Tokens。PageHeader 的 kicker/description/英语副标必须是可选插槽，没信息增量时默认不渲染。Gate D 检查目标浏览器的暗色文字、中文/数字/仓库名混排以及 200% 文本放大与裁切；只有源码扫描时不得声称视觉可读性已实测。

## v6.6 · Color Choice Gate 不属于 Agent 的任意审美推断

颜色重设计时先盘点全站已有 Tokens、用户确定的品牌色和侧栏/主内容的实际搭配；无色彩约束时提出 2–3 套完整工作台的推荐，等待用户选定或明确授权 Agent 代选。**不得因为开始开发就假定用户批准 Agent 最喜欢的颜色**。如果用户直接说 HEX，保证最终项目角色色精确一致，遇对比问题调整周边颜色并解释。只修改纯功能/保留已确认品牌主题时不强制重问。详见 `references/sidebar-color-discovery.md` 和项目 `design-system/sidebar-color-decision.json`，在浏览器截图里检查 Sidebar、Topbar、Main、Card 和 Chart 一起搭配。
