# Changelog

## v6.15 — 2026-11-04 · Component motion choreography and art direction

- 解决 v6.14 仅要求选择动效强度但 Agent 仍可能只做路由 fade 的缺口。将真实组件状态与动效机制提升到统一 Gate B/QA 覆盖规范，不强制引入无关组件、不盲目增加动画数量。
- 新增 `references/component-motion-choreography-gate.md`：全局真实交互清单、组件级动效/即时反馈/有理由静态、根据用途选择 indicator travel / spatial reveal / state morph / layout continuity / semantic feedback / media continuity，不用一个 fade+slide 套全站。
- 新增 `assets/component-motion-patterns.json`、`scripts/validate_component_motion.py` 与 `tests/test_component_motion.py`：涵盖 Operate/Persuade/Read/Experience、无动效用户选择，拒绝只做 page animation、所有组件同一机制、忽略高价值交互与未说明的静态；静态意图校验不证明体验审美质量。
- 新增原创六组件交互实验页 `assets/component-motion-lab.html` 及 Chromium `tests/component_motion_browser_smoke.mjs`：指示器真实移动、Accordion 尺寸、Toggle 状态形变、列表新增反馈、保存结果、聚焦探索；正常/减少动态效果、桌面/窄屏测试。实验页测试不代表真实产品已通过。
- 将主 Skill、动效选择、技术选型、创意组件、组件审美、工程 Gate、Agent 提示词、README、视觉 QA 与 CI 衔接；旧版强度确认、减少动态效果、页面内容/响应式规则继续有效。

---


## v6.14 — 2026-11-04 · User-owned motion choices and real interaction choreography

- 现有动效规则强调“不要滥用”，却缺乏“**用户可以主动选择是否加入、加入到何种程度**”的硬门禁，容易让 Agent 沉默地把全站做成静态。
- 新增 `references/motion-consent-experience-gate.md`：新项目/重大重设计向用户提出 2–3 档含真实按钮、Tab、弹窗、导航、状态/内容切换的具体体验，提供推荐但不冒充用户确认；继承已有选择、支持混搭/明确委托，局部修复不重复问。
- 定义按业务触发的 `trigger → state → purpose → effect → interrupt/reduced` Motion Coverage、共享 tokens 与可中断/卸载/性能门禁；“无额外动效”仍保留完整状态反馈。
- 新增四类页面的动效决策示例、静态 validator 与回归测试，明确未确认 != `none`，用户授权与减少动效不得省略。
- 新增三档交互 HTML 实验与 Chromium 实测：宽/窄窗口、系统 reduced motion、有/无/强调动效、Tab、Dialog、状态反馈；独立样例通过并不代表真实业务项目通过。
- 接入 SKILL、README、访谈、动画技术选择、动画生命周期、Agent 提示词与视觉 QA；继续保留 v6.13 及此前规则。

---


## v6.13 — 2026-11-04 · Universal surface selection and atomic control geometry

- 新截图暴露“整个筛选/工具栏/连续列表被巨型圆角卡包裹”与中文「查看详情」「重试」被操作列挤为逐字竖排；由此修复**全网站通用的两种设计失败机制**，不再为单个 RepoVantage 页面增补固定配色/尺寸。
- 新增 `references/surface-architecture-gate.md`：open collection / bounded panel / entity cards / editorial flow / split workspace / hero stage 按语义选型，记录拒绝替代方案的原因；允许真实有用的卡片而非强制扁平化。
- 新增 `references/control-geometry-gate.md`：短操作文本原子性、按钮/列宽预算、Flex/Grid shrink 问题、整个控件换行或行重排/菜单回退、CJK/英文/200% 与小屏几何检查。单用 nowrap 而产生屏外溢出不算修复。
- 新增通用设计案例 `assets/surface-control-patterns.json`、静态校验脚本及 Python 反例单测；新增三种表面模式交互实验页和 Chromium 3 宽度×2 字体比例×3 模式 smoke，验证按钮短标签没有折字、溢出、行操作被裁切。
- 接入 Skill 主流程、Component Craft、Component First、Visual QA、Surface/Whitespace、Run Monitor 指南及 CI；保留所有已有能力。此变更未改动真实 RepoVantage 产品工程；browser smoke 只能证明独立样例的几何质量。

---


## v6.12 — 2026-11-04 · Cross-domain perceptual hierarchy and component craft

- 将字号与组件设计的不足从 RepoVantage 单页问题抽象为**所有 Web 页面的通用设计门禁**，适用 Operate / Persuade / Read / Experience；不强制某种 UI 风格、默认尺寸或项目专属命名。
- 新增 `references/perceptual-hierarchy-gate.md`：按真实用户任务建立 P0–P3 信息优先级、灰阶扫读顺序、重要文本不被全局小字号弱化、并防止机械放大所有数字。
- 新增 `references/component-craft-gate.md`：组件职责、内容层级、尺寸理由、视觉状态、交互与边界的六问；覆盖按钮、Tabs、表格/列表、状态、输入、卡片、对话框及导航，强调组合质量而非默认皮肤。
- 增加四种产品模式的可机读示例 `assets/visual-priority-patterns.json`、静态契约校验 `scripts/validate_visual_priority.py` 与单测；接入 Skill Gate A/B/D、现有 Typography/Component-First/Visual QA 与 GitHub Actions。
- 审查约束：静态角色校验不能证明页面美观、可访问性完全达标或真实产品经过 Chromium 检查；现有 v6.11 与此前专项能力不变。

---


## v6.11 — 2026-11-04 · Task center and run monitor UX, verified lifecycle/progress actions

- 用户 RepoVantage「任务中心」截图显示长期大统计侧卡占空间、任务记录行过宽但信息集中左侧、重复“进度百分比未知”文案；判断为任务运行监控信息架构问题，而非再次调卡片 Padding/配色。
- 研究 GitHub Actions workflow runs、GitLab Pipelines/Jobs、Trigger.dev Runs/Inspector、Inngest、Vercel Deployments、Linear List/Filters，区分**机器运行监控**与**人工待办**，保留每个产品的适用边界。
- 新增 `references/task-center-run-monitor-design.md`、`references/repovantage-task-center-case.md`、`assets/task-center-reference-cases.json`。
- 新增 Run lifecycle/Progress/Retry model `assets/task-center-run.schema.json`、`examples/task-center-repovantage.json`、`scripts/validate_task_center.py`，防止未知进度误报零、状态筛选计数错误、重试权限与状态冲突、伪造通过的浏览器证据。
- 新增 `assets/task-center-layout-lab.html` 可交互的独立原创 Mock 示意：顶部状态筛选、任务列表、搜索/排序、真实数量进度与按需详情；只在适合的示例任务出现重试且明确提示**不会执行真实服务端请求**。
- 增加 Python 回归测试和 `tests/task_center_browser_smoke.mjs` 的 Chromium 桌面/手机交互与滚动测试，纳入 GitHub Actions。旧版风格/导航/对齐/数据比较能力保留，本次未修改真实 RepoVantage 业务代码。

---

## v6.10 — 2026-11-04 · Comparison-page UX, chart plot alignment and selection/data integrity

- 针对 RepoVantage 新截图中外框已对齐但图内 Plot Area 与文字重叠、项目比较流程堆积卡片且缺乏差异分析，新增 v6.10 Comparison UX & Chart Integrity Gate。
- 研究 NN/g、RTINGS、Apple Compare、npmcharts、EcosystemPulse、Baymard 和 GitHub Compare 等成熟案例，保留各自适合的设计模式与不能生搬的领域限制。
- 新增 `references/comparison-page-design.md`、`references/chart-interior-alignment.md`、`references/repovantage-comparison-case.md`、`assets/comparison-reference-cases.json`。
- 新增 `assets/comparison-layout-lab.html`：原创响应式比较页，模拟仓库选择同步趋势图图例、series 和指标矩阵；声明示例数据非真实 GitHub 采集。
- 新增 `assets/comparison-contract.schema.json`、`examples/comparison-contract-repovantage.json` 与 `scripts/validate_comparison_contract.py`，静态检查 entity IDs、series/legend/table、时间窗、单位、样本覆盖与 null vs zero。
- 新增 `scripts/audit_comparison_ui.mjs` 可选浏览器几何检查，审计支持标注的 Plot Area、标签交叠、系列身份、横向溢出与底部可达性；Canvas 内标签无结构接口时标 NOT AUDITED。
- 更新 Skill、README、视觉 QA、浏览器/工程规范、反例和 GitHub CI，保留 v6.9 行列对齐/底部安全能力。此更新不直接修改 RepoVantage 业务网站。

---

## v6.9 — 2026-11-04 · Grid alignment, intentional asymmetry and bottom-safe scrolling

- 基于 RepoVantage「版本发布」页面三张截图，识别两个独立问题：左右列独立堆叠导致第二排上边缘错位；卡片靠近视口底部需要验证实际能否滚动到最后一条记录。**截图不能直接证明真实裁切，不能把首屏外的内容都称为 Bug。**
- 新增 `references/grid-alignment-and-viewport-safety.md`：共享网格列线与行起点、ChartPanel 统一分组、不对称合理例外、自然页面滚动与 App Shell 内部滚动、真实 fixed 工具栏和 safe-area 末端占位。
- 新增截图专属 `references/repovantage-release-alignment-case.md`、原创可交互 `assets/grid-and-viewport-lab.html`（独立两列 vs 共享 Grid vs 主图整行，模拟矮窗口和底栏）及 `assets/layout-integrity-patterns.json`。
- 新增 `assets/layout-integrity.schema.json`、`examples/layout-integrity-repovantage.json`、`scripts/validate_layout_integrity.py` 和自动单测，检查是否明确行对齐、移动阅读顺序、滚动末端策略和浏览器证据。
- 新增可选真实浏览器几何审查 `scripts/audit_rendered_layout.mjs`，输出首屏/末端截图、横向溢出、annotated grid 上边缘错列与固定底栏遮挡线索；没有 Playwright 时明确 NOT RUN，不静默安装。
- 更新 MauForma 主 Skill、README、视觉 QA、构图/工程原则与 GitHub CI；保留既有内容密度/导航/配色/字体规则。未直接修改 RepoVantage 业务工程或宣称其底部裁切已经修复。

---

## v6.8 — 2026-11-03 · Page-level density, content curation and intentional whitespace

- 根据 RepoVantage 最新总览截图，发现操作面板 + 三步教程 + 分析功能三卡 + 重复入口同时出现导致内容拥挤；不是配色、圆角或卡片 padding 的单点问题。
- 新增 `references/page-density-and-content-priority.md`：页面主任务和访问状态优先，逐块分 primary/supporting/conditional/deferred/removed，次级内容必须可发现、关键数据不能为留白删除。
- 新增 `references/whitespace-and-surface-composition.md`：macro/meso/micro 组间与组内关系、卡片必要性、反套娃、拒绝固定留白比例。
- 新增四档页面级密度 `assets/page-density-profiles.json`，以及 `assets/page-content-plan.schema.json`、`examples/page-content-plan-repovantage.json` 与截图复盘。
- 新增 `assets/page-density-lab.html` 对比过载总览、精选总览/初访与较密的分析详情；静态脚本 `scripts/validate_page_content_plan.py` 和回归测试用于检查结构和保留来源，不代表视觉审美证明。
- 同步 Skill v6.8、README、设计/QA/Agent 规则及 CI；旧版主题、配色与导航能力保留。未修改 RepoVantage 真实业务源码。

---

## v6.7 — 2026-11-03 · Navigation architecture and responsive shell decisions

- 将“使用侧边还是顶部/底部导航”提升为独立的 Navigation Architecture Gate：先分析真实一级目的地、任务切换频率、层级、屏幕宽度及全局/局部导航分工，后选择组件与颜色。
- 官方参考 Carbon UI Shell、Android/Material 响应式导航、Apple HIG、Microsoft NavigationView、Atlassian 导航系统与 W3C WAI；明确它们是可迁移的决策原则，不是 Web 必须照抄的模板。
- 新增 `references/navigation-architecture.md`、`assets/navigation-pattern-catalog.json`（9 种模式）、`assets/navigation-decision.schema.json`、待确认 RepoVantage 示例、`assets/navigation-layout-lab.html` 交互式桌面/手机预览。
- 解释“Side + Bottom”的两种不同用法：不同断点自适应导航 vs 同屏主导航+底部上下文操作；不同职责不能复制同一套一级路由。
- 新增 `scripts/validate_navigation_architecture.py` 和回归测试，检测重复/丢失目的地、底部导航过载、用户选择来源、断点状态保留与虚构浏览器验收。
- 更新主 Skill v6.7 的阅读路由、设计与组件 Gate、README、项目 MASTER/页面级规则、交互/可访问性 QA 和 CI；保留原有用户选色门槛。
- 此版本只更新 MauForma Skill；未直接修改用户的 RepoVantage 工程或声称真实浏览器功能通过。

---

## v6.6 — 2026-11-03 · User-approved sidebar color & whole-page harmony

- 根据用户新版 RepoVantage 侧边栏截图，将“自选深蓝侧栏”改为 **用户确认后的色彩决策**：Agent 只负责研究、推荐、解释与全页协调，不偷偷覆盖用户指定的颜色/HEX。
- 官方设计来源研究覆盖 Linear、IBM Carbon、GitHub Primer、shadcn/ui、Atlassian；保留来源、适用场景及限制，不把原创示例色值伪称品牌官方色。
- 新增 `references/sidebar-color-discovery.md`、`references/sidebar-color-reference-cases.md`、`assets/sidebar-color-directions.json`、`assets/sidebar-color-preview.html`；预览可切换整页搭配并输入自定义 HEX。
- 新增 `assets/sidebar-color-decision.schema.json`、待确认示例、选择对话和 `scripts/validate_sidebar_color_decision.py`，避免 Agent 推荐被当作用户批准，同时检查用户固定颜色不被擅自覆盖。
- 强化项目 MASTER/Sidebar/Topbar/Main/Chart 的跨区域配色关系，保留状态语义与键盘焦点；静态检查不能证明实际页面美观。
- 新增相关测试与 CI，原有主题、配色案例、动效配方和组件体系保留。
- 未修改 RepoVantage 业务代码，也没有替用户擅自选定新的最终颜色。

---

## v6.5 — 2026-11-03 · Semantic copy and readable typography

- 根据新版 RepoVantage 截图识别无信息增量的英文副标、重复小标题、伪章节编号、开发者术语泄漏，以及大小字号差异不合理、图表和样本信息过小的阅读问题。
- 新增 `references/semantic-copy-hygiene.md` 的 Copy Necessity Gate，区分无用装饰与有意义的面包屑、品牌副标、数据来源和真实流程编号。
- 新增 `references/typography-hierarchy.md` 与 `assets/typography-role-guidelines.json`，按工作台与品牌展示页面分别定义可调整的字号角色建议，不把设计建议冒充 WCAG 强制字号。
- 增加源码静态审查 `scripts/audit_readability.py`、测试与 `assets/typography-reading-lab.html` 概念正反例；静态扫描仅提示人工复核，不自动删文字。
- 将文字必要性/字号层级检查融入 Skill 阅读路由、设计门槛和 QA；不修改用户实际 RepoVantage 代码，不声明实际浏览器验证已完成。

---

## v6.4 — 2026-11-03 · Composition First, palette reasoning and screenshot redesign

- 将内容证据、页面任务、无装饰灰阶构图放到配色和共享组件实现之前；保留已经确认的设计和局部修复免完整访谈例外。
- 强制比较有真实区域结构差异的候选方案，禁止相同 Hero + 四 KPI + 图表模板仅换颜色作为“多方案”。
- 新增针对蓝紫默认 SaaS 配色的语义溯源、颜色角色和审美适用性规则；不武断禁止蓝紫或实验性品牌视觉。
- 新增三种仓库分析页面的构图案例、JSON Schema、可执行结构校验和可切换布局的概念实验室。
- 引入去装饰测试、首屏任务证据、缺数据时空/加载/错误状态和截图结构性返工门槛。
- 新增 12 项构图与决策来源回归测试；本版本没有修改用户 RepoVantage 源码或在其实际网站执行浏览器验收。

---

## v6.3 — 2026-11-03 · Sidebar polish and high-frequency UI patterns

- 根据用户提供的 RepoVantage 侧边栏截图整理真实反例：过度强调、暗色颜色关系不统一、最近打开与导航样式混用、状态点语义不明。
- 新增 `references/sidebar-navigation-design.md` 和 `references/workspace-component-refinement.md`，覆盖 Sidebar、Topbar、Card、Data Table、Tabs、Search、Split Pane 七类高频组件及合理例外。
- 新增浅/深色 `assets/sidebar-palette-examples.json`，保留独立 hover、selected、focus-visible 与业务状态角色。
- 新增可交互 `assets/sidebar-refinement-gallery.html` 正反示例，以及颜色对比度校验脚本与单元测试。
- 强化组件契约、Review、团队交接与 CI 任务路由。**不认定所有左侧轨道线均为错误**，对树形层级、章节进度等保留有依据的使用方式。
- 没有修改用户实际业务仓库的侧边栏，也没有改变六套全局主题与 114 种动效配方。

---

## v6.2 — 2026-11-02 · Animation and visualization selection

- 整合用户提供的 12 项动画与可视化技术指南，与原有 GSAP、Anime.js、Three.js、ECharts/React/Vue 规范去重。
- 新增 `assets/visual-tech-catalog.json`：12 项能力、9 种场景搭配、适用边界、替代与官方链接。
- 新增 `references/visual-tech-selection-12.md`、`scripts/search_visual_tech.py`，按视觉需求推荐技术而非默认安装。
- 澄清 GSAP SplitText 与 anime.js splitText、SVG Filter 原生性质、PixiJS/Matter.js 分工；加强设备性能、生命周期和 reduced-motion 要求。
- 新增回归测试，未安装任何动画/渲染依赖；旧版主题、组件、动效目录保留。

---

## v6.1 — 2026-11-02 · External design case library

- 验证 UI/UX Pro Max 是结构化行业/风格建议库；VoltAgent awesome-design-md 包含 84 个品牌 DESIGN.md 分析文档。
- 新增 84 项可追溯的外部案例轻量索引，含固定上游快照 commit、MIT 来源、风格/用途候选、核验状态。
- 新增 `scripts/search_design_cases.py` 按需检索；先看内容及风格匹配，再打开源 DESIGN.md，严禁冒充品牌官方设计规范。
- 不复制第三方图片、品牌标识、专有字体或整个文档；保留旧版本所有组件和动效功能。

---

## v6.0 — 2026-11-02 · Design intelligence / P0–P3

- P0：建立八种保持作者审美差异的风格档案；按 Persuade/Operate/Read/Experience 模式选择构图；加入 Art Direction 自评。
- P1：新增本地可检索 JSON 风格知识库和推荐 CLI；建立 Design DNA WHAT/WHY/EVIDENCE 协议及全局 Master / 页面差异体系。
- P2：强化 React / Vue 组件架构、状态边界与性能选择原则；保留现有框架、组件库及动画目录。
- P3：新增静态 UI 风险扫描、Playwright 可选浏览器证据采集、unittest 和 GitHub Actions 检查。
- 全部参考均保留来源与适用范围，原创内容独立编写，不复制第三方 Skill 指令或品牌素材。
- 浏览器 QA 工具须由项目拥有 Playwright 环境才能使用；静态扫描不是运行时功能验证。

---

## v5.2 — 2026-11-02 · 设计前访谈与视觉选择

- 增加用户参与的设计方向确认：视觉风格、信息密度、主视觉焦点。
- 用户无法判断风格时，先问网站用途、展示内容、访客首要任务，由 Agent 推导适合的视觉策略。
- 先推荐 2–3 套具体、有真实视觉差异的方向，后让用户选择更小范围的构图、密度、色彩和动效属性；新增多场景对话示例。
- 扩展项目设计简报 Schema，记录内容素材、推荐依据、方案权衡和用户的细化选择。
- 支持按页面内容自适应密度、视觉层级、构图与留白。
- 新增 `references/design-discovery-interview.md` 和 `assets/design-brief.schema.json`。
- 为已有项目、局部修改和用户授权 AI 决定的场景提供免重复提问规则。
- 保留组件优先、跨框架 Web 支持、创意动效和反面案例审查。

---

## v5.1 — 2026-11-02 · 更名为 MauForma

- Skill 正式命名 **MauForma**（Maurice + Forma），slug、安装路径和调用命令统一为 `mauforma` / `$mauforma`。
- 完整继承 Soft Precision UI v5.0 的 114 种动效、45 个缓动、React/Vue 适配、组件体系、正反案例和动画/企业 UI 组件库指南。
- 保留原始 CSS 技术命名空间 `.spui` / `--spui-*`，以避免破坏在旧项目中使用的样式接口。
- 更新示例提示词、主 Skill 元数据和预览页标题，增加品牌安装说明。

---

## v5.0 — 2026-11-02

- Web-first 范围与组件优先的五阶段质量门槛保持不变。
- 增加 React Bits、Vue Bits（React Bits 官方 Vue 移植）、Inspira UI、Magic UI、Aceternity UI 创意组件选型目录；区分免费/Pro 与组件/引擎。
- 增加 Ant Design、Ant Design Vue、Element Plus、MUI、Mantine、Naive UI、Arco Design、PrimeVue/PrimeReact、Angular NG-ZORRO 等企业组件库的职责、框架兼容与主题指导。
- 新增可离线运行的 12 种交互概念展示；**不声称为第三方原版效果**。
- 新增 React/Vue 官方可核验安装示例、Nuxt/Next 生命周期与 SSR/可访问性建议。
- 强化“单主 UI 库 + 可选少量创意组件 + 统一 Design Tokens”，将创意组件的许可/体积/降级列为验收条件。

# Changelog

## v4.0 · 2026-11-02

- 产品定位正式收敛为 Web-first；Vue/Nuxt、React/Next 为一等支持，其他网页框架列入支持矩阵；非 Web 原生 UI 不再是直接实现范围。
- 新增 11 组截图技术栈类别（12 个独立产品）的用途、组件内容、框架兼容、替代方案和反面用法详解。
- 引入基于需要的动画引擎选型：CSS/WAAPI、Motion for React/Vue、Anime.js、GSAP、AutoAnimate、Lottie、Rive 等；保留 v3 的 114 种配方与 45 个 easing。
- 新增跨框架/SSR/生命周期规范、Vue/React 共享组件源码示例、Web Agent 提示词集。
- 建立 Web 组件先行的 Gate A/B/C/D；扩充跨类型网页正反面审查；提供检查脚本。
- 更新 Lucide 与 dnd-kit 新版跨框架适配提示，避免照搬旧 React 技术栈到 Vue。

---

# Change Log

## v3.0 · 2026-11-02

- **通用定位**：面向所有 UI 系统，当前深入研究后台与生产力界面，不再把小标题/大标题禁忌强加给营销、作品展示等其他产品。
- 组件先行、Design Tokens 和反面案例、跨平台模式完整保留。
- **动漫目录**：Anime.js v4.5.0 官方全部主能力类别、45 个官方内置 easing 名称、6 类扩展 easing 生成器/控制方式。
- 新增按目的组织的 **114 个原创可组合动效配方**，逐项写出视觉表现、适用场景、避雷、API 映射和 A/B/C 适用等级。
- 新增交互式 `assets/motion-gallery.html`，支持类别、搜索、重播和 45 缓动列表。
- 新增 16 个 Anime.js v4 ES module 代码示例、动效治理规范和通用系统设计矩阵。
- 说明无法穷尽组合动画，也不把设计配方误写成官方预置特效；Web/Native 区分处理。

## v2.1 · 2026-11-01

- 用户管理页面眉题/巨型 H1/重复英文副标题等反面案例。
- 14 组可视化前后对照、UiPageHeader 规范。

## v2.0 · 2026-11-01

- 组件优先、六套主题、优秀与反例、评分、基础复用组件。
