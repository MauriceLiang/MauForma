# 前端项目架构与验收门槛

## v6.17 · Icon Art Direction Gate（语义优先 + 全组视觉一致）

Gate A：在导航架构和信息结构明确后，检查已有图标包/版本、用户已确认风格。为主要导航/高频动作搜索并核实至少两个真实候选，基于任务语义和视觉轮廓进行选择；不要为每个文字标签机械添加图标，也不把 RepoVantage 的例子当全站默认字典。参见 `references/icon-art-direction-gate.md`。

Gate B：共享 `IconBox/NavItem/IconButton/Status` 组件里使用同一个主图标体系；Gallery 展示实际字号、图标/文本/Badge、选中/hover/focus 和主题，不只是单个 SVG。自定义/品牌 glyph 属于合法例外，但要记录来源与许可、视觉边界。

Gate D：图标是否真实加载且可辨识、无多套画风混合、无突然视觉重量变化、无压缩/偏移、图标按钮的文字或 aria-label 可用。显式 DOM 标记可以用 `scripts/audit_icon_consistency.mjs` 检查几何和 style 风险；**脚本无法替代语义辨识或人类审美判断**。

## v6.16 · Semantic Spacing & Rhythm Gate（所有网页类型）

Gate A：在已确定的页面信息结构中，把相邻模块标为 `inside/peer/section/connected/anchored` 等空间关系。根据用户已选视觉方向和业务密度映射 `inline/inside/peer/section/page` 空间 Token；不能因为统一卡片组件就平均间距，也不能因为没要求动画/颜色就忽略空间节奏。参考 `references/semantic-spacing-rhythm-gate.md`。

Gate B：让父级 Grid/Stack/PageSection 管理同级和章节 gap，区分 Card 内边距；同一图表行的 column-gap 与行间 row-gap 都要设计，移动端由横转纵保持相应 peer gap。连续列表、Tab+Panel 等合法连体结构可共边，但必须注明原因，不靠负 margin 掩盖错误。

Gate D：在浏览器含横竖/小视口、200% 字体、异常数据、底部滚动、固定栏情况下查看整页节奏。带 `data-mf-space-id` 的项目可提供独立关系契约给 `scripts/audit_spacing_rhythm.mjs` 实测，正常没有标注时不可编造结果。静态 `scripts/validate_spacing_rhythm.py --repository` 只验证例子的设计完整性。

## v6.15 · Component Motion Coverage 与组合体验

Gate A：完成用户动效选择后，从真实页面识别高频/高价值组件及状态变化；为其决定动效/即时反馈/故意静态的理由，**页面级路由转场不能计入组件动效覆盖**。见 `references/component-motion-choreography-gate.md`。

Gate B：为 Tab/Segment、Accordion/Drawer、Toggle、Row/List、Success/Error/Media 等项目真实存在的组件建立组件 Motion Gallery。不要将所有 `hover` 都写成同一个 scale、所有变化都 fade；根据定位、触觉、空间和状态选择合适机制。并非每个项目都必须存在上述组件。

Gate D：在真实浏览器触发至少关键业务交互的前、中、后状态，检查实际位置/展开高度/组件状态/减少动态效果、快速重复和反向。静态脚本 `scripts/validate_component_motion.py` 只是覆盖契约；独立 Mock 预览不能冒充实际产品 QA。

## v6.14 · Motion Choice Gate：先问，再做动画，最后验证

Gate A（仅新设计/重大动效改版）：查已选品牌/页面动效；未知时推荐 2–3 档有实际视觉差异的交互选择，由用户决定、融合或明确授权 Agent。对话一轮即可、不要重复询问；未回答标 unresolved，**既不能默认全站静态，也不能默认带大量滚动特效**。详见 `references/motion-consent-experience-gate.md`。

Gate B：基于用户确认建立 Motion Tokens 和页面内真实交互列表，必须覆盖其所选强度与 reduced-motion；可以使用已有组件库过渡，不强行引入动画包。基础状态反馈即使无额外动效也必须存在。

Gate D：真实浏览器切换 Tab/弹层/导航/消息/列表与系统 reduced-motion，观察生效的进退场和静态回退，验证快速点击可中断、内容即刻可见、状态与键盘完整。静态决策校验 `scripts/validate_motion_decision.py` 不证明实际动画表现。

## v6.13 · 全类型页面的 Surface / Geometry Gate

Gate A：基于真实用户任务评估 open collection、单层 panel、媒体/商品 cards、editorial flow 或分栏/沉浸 stage；说明所选表面及拒绝候选的理由（`references/surface-architecture-gate.md`）。不把巨型外卡当成后台默认。

Gate B：明确短按钮/Tab/Badge 的 atomic label 与允许语义换行的正文不同；为表格行操作预留自然尺寸预算与 responsive fallback（`references/control-geometry-gate.md`）。`white-space:nowrap` 必须配合 Grid/Flex 父容器策略，否则可能制造横向越界。

Gate D：真实 Chromium 在桌面、390/320px、200% 文字放大和错误状态增加操作时检查短词组不被拆字，点击区域/焦点/最后行可达；可使用 `data-mf-atomic-control` / `data-mf-control-label` 与 `Range.getClientRects()` 测试。独立示例测试不等于业务实现。静态 `scripts/validate_surface_control.py` 只核验结构计划。

## v6.12 · 全类型页面前置条件（Gate A / B / D）

- Gate A：读取 `references/perceptual-hierarchy-gate.md`，按实际用户任务识别 P0–P3、阅读路径、可见信息与密度，**先判重要性、后定字号与组件形式**。不同页面可有不同 P0（例如价格、正文、作品、当前错误）；不是每个数字都是大 KPI。
- Gate B：读取 `references/component-craft-gate.md`，确定共享组件职责/文本层级/形态依据/交互与状态。预览组件本身以及它们组成的真实内容区域，不用统一 pill/描边冒充质量。
- Gate D：整页灰阶三秒扫描、真实正常/异常内容、长文与 200% 放大、宽窄窗口的截图验证。静态优先级计划可由 `scripts/validate_visual_priority.py` 核验**覆盖性**，不能宣称视觉优劣已自动判定。小范围修复按现有页面/组件承诺执行，不强制重复全项目探索。

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

## v6.7 · 新增 Navigation Architecture Gate（构图前、组件实现前）

在重大设计任务里，先盘点一级目的地、栏目深度与频率，区分 global/local/item/actions/tabs。读 `references/navigation-architecture.md`，评估 Top only、Side、Top+Side、Rail/Split、Mobile Bottom、Responsive Side→Bottom、Top+Bottom、Side+Bottom action bar。对未确认架构，展示 2–3 套有实际层级差异的方案，记录用户选择或显式 delegated；明确继承既有导航或局部修复可跳过。之后才建立 UiNavigation 组件契约与 Tokens。浏览器验收必须包含桌面、手机、窄窗和路由可达性、键盘/focus/ARIA、底部遮挡及任务上下文保持。静态脚本 `scripts/validate_navigation_architecture.py` 不能代替真实流程测试。

## v6.8 · Gate A0：内容优先级先于 Card 网格构建

新建/大改版先逐路由列出 primary_task、访问状态、内容主次与条件/延后入口，参照 `assets/page-content-plan.schema.json`。总览页不要同时生成完整教程、功能目录、每个操作的卡片；优先整块删除测试，并确保次级功能可发现。数据分析页允许较高密度展示可比较的图表、指标与筛选，不能因此缩小关键数据来源或藏掉错误。组件 Gate B 不能因为复用 FeatureGrid/Card 就往所有页面额外加介绍区；Gate D 应按总览、分析、首访、回访分别做截图验收。

## v6.9 · Gate A/B/D：Grid 行契约 + 滚动终点证据

**Gate A**：内容筛选后建立同级卡片的内容边界、共同列/行线、合理主次比例与移动阅读顺序；对分析页独立两列的无意瀑布结构执行回退。

**Gate B**：共享 ChartPanel、List、MainScroll、BottomActionBar 的尺寸/滚动契约，优先 CSS Grid 与 `minmax(0,1fr)`、必要的 `min-height:0`、正确的 `overflow-y:auto`；fixed 工具条在真实滚动区末尾预留空间，避免 `overflow:hidden` 全局裁切。不同高度不必强制 equal-height 卡。

**Gate D**：真实浏览器滚到终点，验证最后记录/按钮/图表图例、fixed bar、矮窗口、手机安全区与 200% 放大。若只有截图/声明式脚本则标 `NOT RUN`。可选 `scripts/audit_rendered_layout.mjs` 为浏览器首屏/末端输出几何风险线索，不能替代人工视觉/交互验收。案例见 `references/repovantage-release-alignment-case.md`。

## v6.10 · 比较页面的工程协议

Gate A：选择比较模式前先定义用户的决策问题、对象、共同数据口径和缺失策略，参考 `references/comparison-page-design.md`；不要简单把所有仓库统计图复制并排。

Gate B：RepositoryPicker/Legend/Series/MetricMatrix 共用唯一 ID 与颜色 token；选择、时间窗、过滤、数据来源改变时所有视图同步。表格按对象列/指标行显示，同一指标有单位、sample_size、coverage；缺失值 null 不能自动变成 0。对比首屏强调可信差异，非数据支持的综合赢家禁止。

Gate D：对 Chart Plot 内部坐标、标签碰撞、数据点覆盖和图例绑定做浏览器复核。可用 `scripts/validate_comparison_contract.py` 做声明式数据检查，`scripts/audit_comparison_ui.mjs` 做标注 DOM 的几何风险检查；对 Canvas 内文字未做视觉检查时明确 NOT AUDITED。切换对象和筛选时必须回归数据和表格，不只测试静态页面初始状态。

## v6.11 · Run Monitor 工作台的设计与开发门槛

Gate A：根据 `references/task-center-run-monitor-design.md` 先确定是 `run_monitor/human_tasks/mixed`、最常见操作、状态来源和进度/权限契约。采集任务默认先评估顶部可操作的状态筛选 + 扫描型任务列表 + 按需详情，而不是默认两张大卡片或人工 Kanban。

Gate B：RunRow、StatusFilter、ProgressIndicator、RunDetail、RetryAction 从同一 task/run ID 和 lifecycle state 导出。可计算进度必须有稳定分母和同单位；未知进度不等于 0。需要重试/取消时先确认后端接口、权限及重复请求语义；不能无权限渲染可点击假按钮。

Gate D：`scripts/validate_task_center.py` 检查静态数据/操作契约，`tests/task_center_browser_smoke.mjs` 检查独立 Mock 交互和响应式；目标业务必须验证真实服务端状态、错误/日志与权限、过滤计数、长列表及滚动终点。状态刷新时保留用户选择，不因自动重排强制跳动。
