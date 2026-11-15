---
name: mauforma
description: Web-first, framework-aware frontend design and implementation skill. Diagnose the real product and page task before choosing a visual direction; build coherent information architecture, typography, components, spacing, interaction and accessible responsive interfaces; verify actual rendered pages. Applicable to marketing sites, consumer products, learning tools, content sites, commerce, creative experiences, enterprise apps and data workspaces. Supports Vue/Nuxt, React/Next, Svelte/SvelteKit, Angular, Solid, Astro and vanilla Web.
---

# MauForma — 通用 Web 设计与前端工程 Skill

> **职责**：从用户任务与真实内容出发，建立有辨识度、可使用、可维护、可验证的 Web 界面。它是 Agent 的工作规范，不是变更日志、某个项目的复盘、固定配色模板或组件库安装清单。

## 1. 适用范围与优先级

- **覆盖**：品牌与营销网站、内容与阅读、教育与学习、消费型应用、电子商务、作品展示、创意体验、数据工具、管理工作台及混合产品。适用于 Vue/Nuxt、React/Next、Svelte/SvelteKit、Angular、Solid、Astro、原生 HTML/CSS/JS，以及桌面容器里的 Web 前端。原生 SwiftUI/AppKit/Android UI 不直接由本 Skill 的代码规范覆盖。
- **核心判断**：先识别**产品类型**，再识别当前页面的**主要行为**。Operate（操作）、Read（阅读）、Persuade（说服/转化）、Experience（体验）是页面目标，不是对产品的排他分类；同一产品的不同页面可以采用不同目标与密度。
- **优先顺序**：当前用户明确要求 > 用户已确认的设计决策与品牌规范 > 现有可运行系统及组件契约 > 本 Skill 的通用原则 > 示例与技术偏好。不要借“统一设计”未经授权改变业务功能、导航、框架、品牌色或已接受的交互。
- **只做需要的事**：新站或重大改版完整走设计流程；局部 UI 故障先定位和修复影响范围；仅需审查时输出证据与建议，不擅自改代码。已有明确需求时不反复让用户填问卷。
- **知识与项目隔离**：本 Skill 正文、通用规范、公开示例不得记录用户的具体项目名、组织、私人截图、业务字段或真实数据。项目诊断留在项目自身工作区；将可复用结论抽象成“问题—原因—适用场景—设计原则—验证方法”。版本历史仅放在 `CHANGELOG.md`，不得按版本把补丁堆进本文件。已有示例中的实体、数据和行为必须明确为合成演示。

## 2. 按任务读取资料，不一次加载全库

`SKILL.md` 只负责路由和决策。具体阈值、范例、JSON 契约、框架 API 和检测脚本以相应参考文件为准。先读取与当前任务有关的 1–3 组资料，发现问题后再扩展，不要让阅读参考成为无限前置工序。

| 任务或证据 | 先读取 |
| --- | --- |
| 新建产品、全面改版、用户没有视觉方向 | `references/design-discovery-interview.md`、`references/product-experience-routing-gate.md`、`references/design-style-catalog.md` |
| 结构与视觉中心、页面变成通用后台模板 | `references/composition-first-design.md`、`references/perceptual-hierarchy-gate.md`、`references/progressive-visual-refinement-gate.md` |
| 模糊指令“优化一下”、审视已有页面 | `references/proactive-visual-defect-discovery-gate.md`、`references/visual-critique-loop.md` |
| 内容重复、空泛文字、信息密度不对 | `references/page-density-and-content-priority.md`、`references/semantic-copy-hygiene.md`、`references/typography-hierarchy.md` |
| 模块贴合、行列错位、底部裁切 | `references/semantic-spacing-rhythm-gate.md`、`references/spacing-regression-protection-gate.md`、`references/grid-alignment-and-viewport-safety.md` |
| 导航职责、位置、层级和跨屏迁移 | `references/navigation-architecture.md`、`references/sidebar-navigation-design.md` |
| 颜色、浅深主题、视觉人格 | `references/palette-art-direction.md`、`references/sidebar-color-discovery.md`、`references/design-system.md` |
| Card 套娃、控件断行、组件精修 | `references/surface-architecture-gate.md`、`references/control-geometry-gate.md`、`references/component-craft-gate.md` |
| 设置页、注册、结账、连续表单 | `references/settings-form-layout-gate.md` |
| 图标含义或同屏风格不协调 | `references/icon-art-direction-gate.md` |
| 数据图表、多对象比较、运行记录 | `references/chart-interior-alignment.md`、`references/comparison-page-design.md`、`references/task-center-run-monitor-design.md`（仅在对应场景阅读） |
| 动效决策、组件级动态反馈 | `references/motion-consent-experience-gate.md`、`references/component-motion-choreography-gate.md`、`references/animation-engine-selection.md` |
| 参考设计、受限素材、外部灵感 | `references/design-reference-learning-gate.md`、`references/design-dna-protocol.md` |
| **新建/重构含交互控件的页面，先选并用组件库** | **`references/component-library-first-gate.md`**、`references/enterprise-ui-library-guide.md`、`references/component-first.md` |
| 组件工程、技术栈、跨框架迁移 | `references/component-first.md`、`references/framework-support-matrix.md`、匹配的 `references/framework-*.md` |
| 浏览器、无障碍、性能与交付复核 | `references/visual-qa.md`、`references/browser-qa-protocol.md`、`references/ui-review-rubric.md` |

其他参考文件、组件画廊与脚本均为**按需工具**。示例通过不代表真实页面通过。不得把某一场景的专项规范自动提升为所有网站的默认布局。

## 3. 执行流程：从实际问题到验证闭环

### A. 探索现状与明确边界

1. 读取用户需求、已有视觉决策、目标受众、页面内容、真实流程、品牌资源与可访问性要求。有现成工程时先检查路由、主要组件、设计 Tokens、UI 库、锁文件及构建脚本；**不擅自换框架**。
2. 将任务归为：**新建/重设计、已有页面优化、明确缺陷修复、仅分析**。已有页面优化应先实际查看页面首屏、中段、末端和关键状态，检查真实 DOM/计算样式及可见问题；证据不足不得编造“必然存在的 bug”。
3. 为页面写出四项最小设计简报：**谁来使用、要完成什么、第一眼应该看到什么、哪些约束必须继承**。同时标明当前页的 Operate/Read/Persuade/Experience 目标。
4. 仅在真正影响方向的关键决策缺失时，给出 2–3 个**具体且不同**的候选：例如内容优先、操作效率优先、视觉体验优先；说明布局、密度、字体/色彩角色和取舍。能从现有产品确定的条件不再追问。**建议不等于用户确认**；清晰区分 `confirmed / inherited / delegated / proposed / unresolved`。

### B. 先修 UX 与内容架构，再画 UI

1. **内容盘点**：标记 `primary / supporting / conditional / deferred / removable`。每个标题、副标题、编号、说明、徽章都应有信息、导航或状态价值；删除后不损失意义的装饰性文案优先移除。真实面包屑、品牌标语、章节编号、数据单位、来源和样本量必须按用途保留。
2. **用户路径**：入口、核心任务、成功/失败反馈、返回与下一步必须成立。学习、消费、内容和创意产品需要体现自己的主要活动，不能把所有产品改名后套入同一组“侧栏 + 四个 KPI + 表格”。
3. **构图先于装饰**：先用灰阶或低保真布局确定区域顺序、主视觉、内容边界、滚动模型，再选择视觉风格。若结构不成立，不得仅换渐变、字体、卡片圆角就称“重新设计”。
4. **导航按任务决定**：比较全局/局部目的地数量、切换频率、层级深度、桌面与窄屏行为，再选 Top、Side、Bottom、混合。不要重复摆三套相同菜单；固定操作栏不能遮挡滚动末端。
5. **不同页面允许不同密度**：引导/展示可以舒展，数据/编辑/工作台可以高密度；但同级模块要有稳定的内部和外部空间节奏，不靠堆卡片制造“高级感”。

### C0. Component Library First — 在写业务页面之前选定并使用组件库

**这是有交互控件页面的首版开发门禁，不是可选建议。** 先读 `references/component-library-first-gate.md`：盘点锁文件和现有 UI 库；已有成熟组件优先继承，缺少时由 Agent **主动为当前框架和视觉风格选择一套主组件方案并真正集成**。用户没有点名库不等于授权从零手写控件。把 Select、Combobox、DropdownMenu、Button、Checkbox、Radio、Switch、Tabs、Dialog 等需要的控件映射到已选库/可访问 headless 原语，先统一主题并试用关键状态，然后再批量开发页面。

**阻断首版低质量实现**：不得用随手拼的 `div + click` 伪 Select/菜单，不得反复手写按钮和选中逻辑，不得“计划采用库但代码未用”。少量静态页面、已确认的原生体验与特殊交互可例外，必须有功能、体积或平台理由。复用成熟组件不免除同屏视觉、焦点、键盘、选中态、悬浮层、长文本和真实业务页面的验收。

### C. 建立设计系统与共享组件

1. 继承已有设计源；新项目建立单一 Tokens 源：颜色角色、字体层级、间距、圆角、边框/阴影、布局断点、图标角色、动效和状态。页面特例要有理由，不要每页独立硬编码同类值。
2. 先确定 `PageTitle / SectionTitle / Body / KPI / Axis / Legend / Metadata` 等**文字角色**，按信息优先级设计字号、字重、行高、字宽与对比。巨大标题不能压过核心任务；图表刻度、表头、单位和样本数不能因“精致”变得难读。排版应同时检查中文、英文、数字混排、长文本和 200% 文本缩放。
3. 根据内容关系选择开放布局、边界面板、单层 Card、表格、列表、分屏或媒体墙。只有信息/交互分组真正独立时才用容器；拒绝无意义外壳与嵌套卡片。**Section 的外部 gap 与 Card 的内部 padding 是两件事**。
4. 空间关系区分 `inside / peer / section / connected`：组内紧密、同级稳定、跨章节更明显、确实连续的 Tab/Panel 可以贴合。纵向 `row-gap` 和横向 `column-gap` 都要检查；不能因新主题把不同业务模块贴在一起，也不能把原本连接的控件强行拆开。
5. **基础交互控件默认使用已选库及其适配层**：先确认 Select、DropdownMenu、Button、Checkbox、Tabs 等实际来源并完成可运行 Showcase；
6. 共享 Button、Field、Dialog、Navigation、Tabs、Table/List、Feedback、Status、PageHeader、Chart 等组件及状态。实现前校验**实际业务动作**、禁用/加载/错误/空状态、键盘操作和组件行为契约。短操作文字不得逐字纵排、裁切或溢出；空间不足时让操作组换行、移位或使用明确的折叠菜单。
7. 图标先检查语义，再检查同屏整组的线条、细节、负空间、视觉重量与字体对齐；不只凭名称导入一个“差不多”的图标。没有清晰符号时可用文字。成熟图标库可按现有技术栈选用，但不能无理由混用多个体系。
8. 配色由用户或品牌决策驱动。可以提出有整体页面依据的候选，但不得默认强加蓝紫渐变、灰白后台或任何单一审美。查看侧栏与主区域、图表、状态、hover/focus 在深浅主题中的整体关系；不以“去 AI 味”为借口禁止合理的强色、插画、emoji 或艺术表达。

### D. 按真实页面类型实施交互

- **操作/数据型**：优先操作可达、状态可辨、筛选与反馈真实。图表需核对绘图区、轴、刻度、单位、图例和表格数据；缺失值不是 0。多对象比较必须让所选对象、图例、系列、矩阵列与共同时间窗对应。运行记录须区分真实进度、未知进度、状态和有权限的操作。
- **阅读/教育/内容型**：优先内容层级、阅读顺序、节奏、检索与回到任务；无需为每段内容套 Card。学习行为、过程反馈与材料呈现应由真实任务驱动。
- **品牌/消费/创意型**：允许大胆排版、摄影、非对称、插画与有意图的动画；不必套“工作台紧凑标题”规范，但主要内容与关键行动仍要可辨、可访问。
- **设置与表单**：独立保存的设置项可采用「左说明、右控件」；整体提交的字段簇通常采用「上标签、下输入」。混合页面按区域判断，不按“设置”标题一刀切。危险操作独立、保存失败可恢复。
- **动效**：用户已确认强度优先；新站或重大视觉重构且尚无动效方向时，提供清晰选择或由用户授权决定。动画应针对 Tab、展开、选择、反馈、排序等真实状态变化，支持中断、卸载清理和 `prefers-reduced-motion`。不因为库存在就添加粒子背景或多个动画引擎。
- **工程**：Vue 使用相应 SFC/组合式 API，React 使用组件与 Hooks，其他框架按各自约定实现。优先复用现有组件库与依赖；引入任何新库前确认兼容版本、许可、包体与运行成本，不照搬另一框架的组件源码。

### E. 真正检查实际渲染结果

1. 在同一路由、同数据状态、同窗口与字号下做修改前后比较；检查首屏、中段、末端、滚动终点，以及选中、hover、focus、loading、empty、error、success 等适用状态。
2. **关键控件首版门禁**：在实际页面打开 Select/Combobox/DropdownMenu，操作 Button、选中项、Checkbox/Radio/Switch、Tabs 和弹窗，检查使用的是已选成熟组件库或有依据的原生实现；在打开、选中、禁用、加载、键盘、长中文、深浅主题中确认统一且可用。
3. 视觉检查至少覆盖：主视觉是否对应主任务、内容是否冗余、字号层级、图表内部标签、图标统一、组件边界、左右/上下间距、共享网格、短按钮与长文本、底部可达性、深浅色。
4. 交互与工程检查至少覆盖：实际点击与状态更新、键盘焦点、语义标签、颜色对比、必要的移动/窄窗口适配、200% 文字缩放、减少动画、加载与错误、性能和构建/测试。响应式范围以用户项目要求为准，**不要强迫仅桌面使用的产品改成手机产品**；仍应避免目标视口出现无意截断。
5. 工具是辅助：静态审计只能产生风险线索；截图只能支持可见观察；浏览器脚本也不能替代审美判断与业务端到端测试。未打开真实页面就不能宣称“已修复视觉问题”；未调用真实后端就不能宣称“已验证保存”。
6. 报告必须使用有证据的状态：`VERIFIED`（在真实产品实测）、`STATIC CHECK`（仅源码/契约）、`DEMO ONLY`（仅合成样例）、`NOT TESTED`（未运行）、`BLOCKED`（条件受限）。视觉问题仍存在时，注明未解决及原因。

## 4. 防止模板化和反复返工的审核题

实施或评审时逐项问：**（1）这一页像不像它真正服务的产品？（2）用户最想完成的动作是否最容易发现？（3）如果删掉某段文字/卡片，会失去什么信息？（4）区域间距表现的是任务关系还是偶然 CSS？（5）标题、KPI、图表刻度、按钮谁该最显眼？（6）同屏图标是否语义正确且统一？（7）互动和状态是否真的可用？（8）是真实页面复验还是只有示例通过？**

出现以下情况应退回相应阶段，而不是叠加补丁：

- 结构错误但仅换配色或圆角 → 返回 **B：内容与构图**。
- 独立模块被挤在一起或右列第二排错位 → 返回 **C：空间关系和共享网格**。
- 删了真实单位/图例/业务说明，却保留空泛英文眉题 → 返回 **B/C：内容必要性与文字角色**。
- 全部页面一个侧栏布局、一个密度、同一组 KPI → 返回 **A/B：产品与页面目标**。
- 动效炫目但控件状态、可访问反馈或低动态模式失效 → 返回 **D/E：交互与验证**。
- 仅在组件 Gallery 或合成案例通过测试 → 返回 **E：真实页面复验**。

## 5. 资源和使用方式

- 设计研究与风格：`references/design-style-catalog.md`、`references/aesthetic-authorship.md`、`assets/style-knowledge.json`。
- 组件与框架：`references/component-library-first-gate.md`、`references/enterprise-ui-library-guide.md`、`references/creative-component-libraries.md`、`references/framework-support-matrix.md`。
- 动画配方：`references/animejs-official-capabilities.md`、`references/animejs-motion-recipes.md`、`assets/motion-gallery.html`。
- 互动原型：`assets/preview.html` 及其他 `assets/*-lab.html`，**只作为独立概念示范**。
- 审核脚本：`scripts/audit_frontend.py`、`scripts/audit_existing_visual_defects.mjs`、`scripts/audit_panel_spacing.mjs`、`scripts/audit_spacing_rhythm.mjs`、`scripts/browser_qa.mjs`。运行前检查依赖与页面可访问性，不能把工具不可用写成通过。

```bash
# 根据网站内容查找风格资料和适用技术
python3 scripts/search_design_knowledge.py --query "内容 阅读 插画" --mode Read
python3 scripts/search_visual_tech.py --goal "图表 趋势 交互"

# 在目标代码库做静态前端审查（替换实际路径）
python3 scripts/audit_frontend.py ./src --format json

# Skill 自身静态质量检查；浏览器 QA 另需实际运行环境
python3 scripts/validate_web_skill.py
python3 scripts/validate_skill_hygiene.py
python3 -m unittest discover -s tests -v
```

### 按需专项资料与检查器

下面是**检索索引，不是所有任务的必执行命令**；只有问题涉及对应领域，才打开资料或运行脚本：

- **设计研究/决策**：`references/art-direction-critique.md`、`references/project-design-hierarchy.md`、`references/external-design-case-library.md`、`references/visual-tech-selection-12.md`、`scripts/search_design_cases.py`。
- **导航/配色/容器**：`references/sidebar-color-reference-cases.md`、`references/workspace-component-refinement.md`、`references/whitespace-and-surface-composition.md`、`references/clean-enterprise-design.md`、`assets/navigation-pattern-catalog.json`。
- **布局与内容**：`scripts/validate_navigation_architecture.py`、`scripts/validate_sidebar_color_decision.py`、`scripts/validate_layout_integrity.py`、`scripts/audit_rendered_layout.mjs`、`scripts/validate_page_content_plan.py`、`scripts/validate_spacing_rhythm.py`。
- **组件与视觉**：`scripts/validate_surface_control.py`、`scripts/validate_visual_priority.py`、`scripts/validate_icon_curation.py`、`scripts/audit_icon_consistency.mjs`、`scripts/validate_design_reference.py`、`scripts/validate_component_motion.py`。
- **内容与交互状态**：`scripts/audit_readability.py`、`scripts/validate_comparison_contract.py`、`scripts/audit_comparison_ui.mjs`、`scripts/validate_task_center.py`、`assets/task-center-layout-lab.html`、`scripts/validate_motion_decision.py`、`scripts/validate_proactive_audit.py`。

## 6. 交付格式

简洁说明：**任务范围与继承约束 → 实际发现的问题/设计依据 → 选定的页面结构与组件/Tokens → 已完成修改 → 真实测试结果及未测项**。大型设计可给出备选与理由；小修复只需要受影响的内容。报告项目变更时使用该项目自己的文档，**不要将其过程与名字追加到 MauForma 通用规范**。

外部工具、依赖和参考产品可能更新；具体 API 和许可证以目标工程锁文件及官方当前文档为准。
