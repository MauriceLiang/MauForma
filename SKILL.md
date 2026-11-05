---
name: mauforma
description: MauForma — Web-first, framework-aware, component-first frontend design and implementation Skill for Vue/Nuxt, React/Next, Svelte/SvelteKit, Angular, Solid, Astro and vanilla HTML/CSS/JS. Establish design tokens and reusable components before pages; create coherent visual systems, accessible responsive UI, purposeful motion and detailed good/bad examples. Priority depth: admin/SaaS interfaces, applicable to all websites and web apps. Includes Anime.js v4 catalog, React Bits / Vue Bits / Inspira UI creative components, Ant Design / Ant Design Vue and other enterprise libraries, Motion/GSAP/CSS engine choices, and enforceable agent prompts.
---

# MauForma · Web-first 前端视觉与工程 Skill v6.16

**品牌**：MauForma（Maurice + Forma）。原 Soft Precision UI v5.0 的完整能力保留，现已扩充为内容驱动艺术指导、设计知识库、项目级设计规范、组件工程与 QA 的综合 Web Skill。

**定位**：网页设计与前端实现（Web-first）。支持所有网页类型，**当前专项深化后台管理/SaaS**，但绝不把其他网站套成后台模板。框架：Vue 3 / Nuxt、React / Next.js、Svelte / SvelteKit、Angular、Solid、Astro、HTML/CSS/JS；若是 Electron/Tauri 的 **Web 前端层**也适用。**不以 SwiftUI、AppKit、原生 Android 等非 Web UI 为直接适用对象**。

**主原则**：审美统一 ≠ 每页一个模板。统一设计语言 + 共用组件 + 符合具体业务的信息架构 + 恰当动效 + 可访问、可测试的功能。可以自主**提案**主题色，但新配色进入正式实施前须尊重用户明确选择与决策来源，不自行固定用户未认可的蓝紫粉或其他颜色。

## v6.16 · Semantic Spacing & Spatial Rhythm Gate（间距服务关系，而非堆数字）

**组件对齐、字体正确、容器合理，仍可能因为“独立模块贴合 / 同级横纵 gap 不一致 / 卡片内部过空而外部拥挤”使整个页面廉价。** v6.16 将**语义空间关系**提升为独立设计与浏览器验收门禁；适用于所有 Web 产品，不规定统一 8/16/24、统一卡片间隔或强制把所有边界分开。

- **先做空间关系图**：实际页面按 `inside`（标题/图表内）、`peer`（同级卡片/图表）、`section`（独立任务区）、`connected`（Tab 与同一面板/表头与表体）、`anchored`（弹层/叠置媒体）识别相邻关系。独立 Section 不应因父 `row-gap:0` 贴合；`connected` 允许共边/0 gap，必须有语义理由。编辑式艺术排版也可刻意非等距，但不能随机。
- **建立项目级空间层级**：`space.inline / inside / peer / section / page`，从既有 design tokens、字体、业务密度、视口与视觉权重推导，而非强迫所有项目采用一组数值。父级 Grid/Stack 负责 sibling gap；单个 Card padding 不代替外部间隔，且注意图表行内 `column-gap` 与行间 `row-gap` 是两个独立维度。
- **Gate A/B/D**：设计前标记主要模块之间的分组关系与空间角色 → 共享布局组件设置 gap/padding 与断点策略 → 浏览器真实测量同级横纵距离、组间/组内节奏、零间隙与 intentional adjacency、320/390/1280 宽度、200% 字体、最底部/悬浮工具栏。没有真实 DOM 标注时报告 NOT AUDITED，不能从静态截图冒充几何测量。详见 `references/semantic-spacing-rhythm-gate.md`。
- **可执行审查**：四域例子 `assets/spacing-rhythm-patterns.json`、静态角色检查 `python3 scripts/validate_spacing_rhythm.py --repository`、可切换合理/不合理间距的原创实验 `assets/spacing-rhythm-lab.html`、基于显式标记与项目 Token 的 `scripts/audit_spacing_rhythm.mjs` 和 Chromium 反例回归 `tests/spacing_rhythm_browser_smoke.mjs`。独立样例通过不代表外部项目已经修复。

## v6.15 · Component Motion Choreography & Art Direction Gate（不能只做页面切换）

v6.14 解决了**用户有权选择动效强度**，但 Agent 仍可能只完成路由 Fade / Dialog Fade，忽略组件内部动效，造成页面普通、无活力。新 Gate 适用于所有 Web 产品，不强制增加不相关组件，不为动画而动画，也不覆盖用户确认的 `none / balanced / expressive`。

- **组件清单先于页面转场**：在 Gate A/B 梳理页面真实存在的 Button/CTA、Tabs/Filter、Accordion/Drawer/Dialog、Toggle/Checkbox/Slider、List/Table/Card、Search/Form、Status/Chart/Media，按高频程度和任务重要性标记 `motion / immediate-feedback / intentionally-static(reason)`。**路由动效不能计作组件动效覆盖**；B/C 选择下的关键交互如果都静止，必须纠正或提供可验证的理由。
- **动效艺术指导与组合**：不再所有组件只用 `fade+slide` 或全局 `scale(.98)`。优先针对交互用途选择 **indicator-travel（选中指示器移动）/ spatial-reveal（内容按空间关系展开）/ state-morph（滑块或状态形态变化）/ layout-continuity（增删/排序保持位置连续）/ semantic-feedback（结果确认）/ media-continuity（图片和作品切换）**。一个产品选一两项标志性手感，其他高频操作简洁一致；不是给所有卡片加特效。参阅 `references/component-motion-choreography-gate.md`。
- **先预览真实组件，再铺页面**：重要改版须为 2–4 个高价值、实际存在的组件做动效对照，并解释机制/用户价值/静态回退，继承 v6.14 的用户选择，不要反复问每一个按钮。按需参考 `references/creative-component-libraries.md`、`references/animation-engine-selection.md`、114 种 Anime.js 配方；不因有库就安装，不复制同一套效果到所有项目。
- **逐状态浏览器验收**：选中指示器位置、Accordion 尺寸、Toggle thumb、列表插入/重排、结果反馈等需要在浏览器中触发并检验初始/中间/最终状态；`animationDuration>0` 不是审美及动态正确性的证明。要支持快速反向、低性能与 `prefers-reduced-motion`，不要丢焦点或让重要信息迟到。
- **规则与测试**：跨领域交互契约 `assets/component-motion-patterns.json`、静态脚本 `python3 scripts/validate_component_motion.py --repository`，原创交互预览 `assets/component-motion-lab.html`、Chromium 回归 `tests/component_motion_browser_smoke.mjs`；独立样例通过不能冒充用户真实工程通过。

## v6.14 · Motion Choice & Experience Gate（重大设计必须询问，而非默认没有动画）

**交互动效是用户可选择的设计维度，不是 Agent 在“加满花哨特效”和“全部静止”之间悄悄做决定。** 本 Gate 适用于 Operate / Persuade / Read / Experience 与所有 Web 框架；新建、整体改版或显著改变动效的交互重构时，用户没有明确动效偏好且没有授权 Agent 决定，**必须在确定视觉方向后、制作 Motion Tokens 与组件前提出一次具体的动效选择问题**。不能把“简洁”“性能优先”“直接开发”或沉默解释成永久零动画。已有 `confirmed/inherited/delegated` 选择、单点 Bug 与无关修复不重复询问。

- **用户能理解的方案**：提供 2–3 种具体现实体验（A 直接切换但有明确状态反馈，B 细腻的按压/Tab/弹层/列表过渡，C 少量更有表现力的共享元素/主视觉/叙事），解释使用感、性能/可访问性取舍并给推荐理由。接受混搭、明确“无额外动效”、以及用户将动效裁决权委托给 Agent。推荐 `recommended` 不等于用户 `confirmed`；未答复保持 `unresolved`，不要把其当成选择了 A。
- **交互全覆盖而非单个 Hover**：实际存在的按钮/Tab/导航/Popover/Dialog/Accordion/加载成功失败/列表重排及品牌叙事分别建立 `trigger → 状态 → 目的 → 视觉处理 → 中断/反向 → 减少动效` 契约。功能反馈即使选择 A 也不可消失；B/C 的核心交互若完全静态，必须补全或解释边界。
- **动效性能与真实可用性**：使用项目级 Motion Tokens，优先复用现有 CSS / 框架原生机制，再按复杂度选择 Motion、Anime.js 或 GSAP。不能以引入库代替有目的的动画，不得遮挡操作、卡住导航、重复闪烁、虚构数据进度。尊重 `prefers-reduced-motion`（也适用于已选 C），支持取消/卸载/快速重复操作，静态降级保留内容、焦点和结果。
- **可执行验收**：静态决策计划 `assets/motion-decision-patterns.json`、`python3 scripts/validate_motion_decision.py --repository`；可交互选择预览 `assets/motion-choice-layout-lab.html`，Chromium `tests/motion_choice_browser_smoke.mjs` 分别验证 A/B/C、桌面/手机、系统减少动效、Tab/Dialog/反馈。**Mock 测试不证明业务产品动效已验收**。详见 `references/motion-consent-experience-gate.md`。

## v6.13 · Surface Architecture & Control Geometry（全网站通用；不可让短操作竖排）

**组件“长什么样”之前，应先回答“是否需要外层容器”；控件“能否放进去”必须看真实尺寸，不能靠缩小字号/逐字折行解决。** 这属于任何 Web 类型的基础规则，而非任务中心专用模板。

- **Surface Architecture Gate（选结构，不默认 Mega Card）**：先以真实内容、对象独立性、扫描/比较需求、交互/数据边界和 Art Direction 决定 open collection / single bounded panel / entity cards / editorial flow / split workspace / immersive stage。对主要页面至少说明所选形态以及一项有理的替代被拒绝的原因。表格/连续记录常适合平面行与轻分隔，而媒体/商品卡、编辑器面板、品牌大画面则有其合法用途。**不能只因现有组件库有 Card 就把筛选、标题、表头、记录全部包进大圆角卡片**。读取 `references/surface-architecture-gate.md`。
- **Control Geometry Gate（短标签不可逐字竖排）**：对 Button、Tabs、Badge、导航/分页和表格行操作，明确 atomic short labels vs semantic multiline content。短标签必须作为完整文本显示，不允许把「查看详情」「重试」「保存」挤成上下单字，亦不可省略文字、被裁切或跑出屏幕。先检查父列宽、flex shrink、min-content、图标与 padding；优先让**整个控件**换行、列表行改布局、溢出操作菜单/可访问横向滚动，不能只加 `white-space:nowrap` 却制造溢出。读取 `references/control-geometry-gate.md`。
- **Gate A → B → D**：选 surface、确定每类控件文字折行契约与宽度预算 → 组件画廊/组合页面检查对齐与 responsive fallback → 浏览器宽/窄/200% 放大及长中文英文、异常状态检查标签 `Range.getClientRects()` 和按钮 bounding box。静态计划可运行 `python3 scripts/validate_surface_control.py --repository`；可查看 `assets/surface-control-layout-lab.html`，CI 独立 Chromium 演示烟测不等于真实业务系统通过。
- **与 v6.12 共存**：信息 P0/P1 仍决定视觉权重；组件质量既包含内容层级，也包含表面结构、控件固有尺寸和可用交互。不可将开放表格“模板化”成所有项目必选，也不可不顾用户已确认的设计方向。

## v6.12 · Universal Visual Hierarchy & Component Craft Gate（所有 Web 页面必读）

**先回答“谁值得被看见”，再决定“字体该多大、组件该长什么样”。** 过去的字级区间与组件清单不足以防止“重要内容被一片小字号埋没、漂亮组件各自堆成低质页面”。本 Gate **不是后台专用模板，不把所有数值变大，也不统一圆角、固定配色或强制某一套字体**。

- **信息显著性先于字号**：新设计/大改版对各页面真实任务建立 P0（立即判断/主动作）、P1（必读信息）、P2（支持）、P3（低频上下文）清单；按对象、内容、风险和决策价值而不是元素标签/是否为数字来给权重。标题、商品价格、文章正文、任务错误或作品本身都可能是 P0/P1；辅助数字并非必然 KPI。详见 `references/perceptual-hierarchy-gate.md` 与原有 `references/typography-hierarchy.md`。
- **实际阅读路径与视觉反差**：先做灰阶/去装饰快扫；明确用户第一眼、第二眼、接下来会点击哪里。禁止为了适配一屏平均缩到 12–13px，禁止把所有数字统一放大，不能让低价值巨大标题/装饰区抢走任务主体。按项目语义 tokens 决定类型尺度、对比、字重和空间。
- **组件审美是设计决策不是 UI 库默认皮肤**：对高频 Button、Tabs/Filter、RecordList/Table、Badge/Status、Search、Card、Navigation、Dialog 逐一说明职责、主/次内容、交互频率、尺寸/表面理由、状态与边界，再决定 reuse/wrap/build。检查页面里组件之间的字号、间距、基线、密度、焦点与状态语义是否互相协调；不能靠批量 pill/阴影/描边制造“高级感”。详见 `references/component-craft-gate.md`。
- **跨领域应用**：Operate 工作台可紧凑，但任务/错误必须清晰；Persuade 营销页可大胆，但产品/价格/CTA 不可淹没；Read 教育/文档重正文舒适度；Experience 作品/互动不压过作品也不能丢控制。用户已确认风格与真实业务优先。
- **执行顺序与证据**：Gate A 建立优先级 → Gate B 共享组件与内容/状态 gallery → Gate D 整页快扫、局部组件与长文本、桌面/窄屏、200% 放大实测。可用 `assets/visual-priority-patterns.json` 作为四种页面模式的通用样例，并运行 `python3 scripts/validate_visual_priority.py --repository` 做**静态契约**检查；它不能客观评分美感，也不能替代浏览器。修单个 Bug 可精简映射，不要求重新设计整站。

## v6.11 · Task Center / Run Monitor Gate（状态可筛选、执行可诊断、操作有依据）

用户最新 RepoVantage「任务中心」截图仍采用**左侧大统计卡 + 右侧巨大任务记录列**，每条记录重复“进度百分比未知，当前显示阶段状态”，真正的异常、作业进度和合法操作反而不醒目。这是**信息架构与任务类型选型**问题，不能仅凭 v6.9 网格对齐或 v6.10 比较页模板修复。

- **识别任务类型**：若是后台采集、部署、导入、Agent Runs，按 `run_monitor` 设计；若是人工待办/指派，按 `human_tasks`，混合场景先区分。不要把技术执行任务一律做成 Kanban，更不能错误地套用多对象比较页。专用规范：`references/task-center-run-monitor-design.md`。
- **研究成熟的执行工作台**：`assets/task-center-reference-cases.json` 梳理 GitHub Actions、GitLab Pipelines、Trigger.dev、Inngest、Vercel、Linear 的官方参考，借用**状态筛选、紧凑运行列表、按需详情/日志、错误恢复、实时更新和合理列显示**；每项都有适用边界，**不复制它们的配色/商标/布局源码**。
- **页级信息优先级**：默认倾向 **轻量状态筛选（可操作且与数据计数一致）→ 搜索/排序 → 对齐的任务列表（任务、状态、真实进展/阶段、更新时间、操作）→ 按需的执行详情**，而非一个永久占 1/4 宽度的统计卡。行高按信息量和可读性决定，避免反复使用空话撑高度。侧栏只有服务大量高频独立筛选时才推荐。
- **生命周期 & 真实进度**：queued、running、waiting、partial、failed、blocked、succeeded、canceled 各有语义，attention 是可解释的**筛选聚合**，不能滥用为状态。只有同单位的有效 `completed/total` 且分母有依据才能显示数字进度；`null` 不是 0，阶段未知不捏造百分比/ETA。计数从同一实际任务集推导或说明服务端汇总的范围。
- **操作权限 & 详情**：`retry`、`cancel` 按当前生命周期、真实后端支持、授权、业务前置条件决定。失败/部分覆盖可在具备能力时重试，阻塞任务可能必须先修复数据/认证，完成/排队任务不能随意提供重试。列表一行简洁呈现状态/原因；复杂阶段、输入输出、日志、错误和重试历史进入可打开的详情。
- **验证与对照**：`references/repovantage-task-center-case.md` 是截图分析，`assets/task-center-layout-lab.html` 是独立原创的可交互 Mock 示例；`examples/task-center-repovantage.json`、`assets/task-center-run.schema.json`、`scripts/validate_task_center.py` 检查状态/进度/授权/汇总语义。运行 `python3 scripts/validate_task_center.py examples/task-center-repovantage.json --repository` 做静态 QA；`tests/task_center_browser_smoke.mjs` 在 Chromium 中核对筛选、搜索、详情、模拟重试、手机适配和滚动终点。**这些不代表真实 RepoVantage 的重试/API 已通过测试。**

与 v6.8 页面密度、v6.9 网格/滚动、v6.10 可比性数据规则配合使用。重设计时继承用户已确定的色板、导航与真实业务权限。

## v6.10 · Comparison UX & Chart Integrity Gate（从“多张图”升级为“真正可比较”）

用户的 RepoVantage 新截图显示两类问题：**发布间隔柱图与散点图外框对齐，但绘图区/X 轴基线和标签布局仍不协调甚至重叠；项目比较页选择了三个仓库，却只有一条突出趋势、长驻大型对象列表和信息稀薄的「比较口径」面板，难以快速发现真正差异。** 截图不能证明源码已漏画其他线，必须在数据/浏览器中检查。

- **按任务选择成熟比较模式**：读取 `references/comparison-page-design.md`、`assets/comparison-reference-cases.json`。参考 NN/g comparison tables、RTINGS、Apple Mac Compare、npmcharts、EcosystemPulse、Baymard 与 GitHub commits compare，从“同列同指标的矩阵”“共享时间窗叠加趋势”“先差异摘要再证据”“两版本 Diff”中**挑与当前用户问题相关的模式**；不是对所有数据页照搬商品比较模板，也不随意生成综合赢家。
- **精简比较流程**：优先明确比较问题 → 2–4 个常见比较对象（仅经验起点，非强制上限）→ 可比性/关键差异 → 一张共同单位时间轴的主趋势图 → 指标矩阵 → 可发现的详细口径和钻取。对象选择与图例保持近邻，可移除/替换。大型“比较口径”空卡、重复图与过长选择侧栏应通过 v6.8 内容筛选，而不是单纯缩小。
- **数据/视图契约必检**：所选 IDs、图例、每条真实系列、表格列必须一一对应；若无数据，系列明确 `no_data/partial`、空缺按 `null` 显示，不得填 0、假设其他线已画出。单位、聚合粒度、时间窗、采集覆盖与样本量必须一致或明确解释不可比。运行 `python3 scripts/validate_comparison_contract.py examples/comparison-contract-repovantage.json --repository` 检查声明式契约，不能替代真实页面数据流 E2E。
- **图表内部也要查对齐**：读取 `references/chart-interior-alignment.md`；比外框多检查 Plot Region、X 轴与图例/辅助文本布局、坐标轴单位、数据标签碰撞和边缘裁切。不同图型不强制同高/相同 Y 量程，但**禁止标签重叠、不可读及误导性比较**。Canvas 内文字无法仅凭通用 DOM 几何脚本自动确认，需图库能力及截图人工复核。
- **运行时检查不可省**：可选 `node scripts/audit_comparison_ui.mjs --url http://127.0.0.1:5173/compare --out compare-audit`（目标项目有 Playwright 才能运行）；支持 `data-mf-selected-id`、`data-mf-legend-id`、`data-mf-series-id`、`data-mf-chart-group`、`data-mf-chart-plot`、`data-mf-chart-label` 等检查钩子。没有标注/Canvas 内绘图不可测时明确报 `NOT AUDITED/PARTIAL`，不伪造自动视觉 PASS。真实 QA 至少覆盖选择变更、图例/图表/矩阵联动、标签、滚动终点和手机可读性。
- **证据和对照**：`references/repovantage-comparison-case.md` 是基于截图的复盘；`assets/comparison-layout-lab.html` 是独立原创的三仓库模拟数据交互示例，图表/表格数据均明确标模拟，**不是实际 RepoVantage 源码改造**。

继续执行 v6.9 外部网格与底部安全、v6.8 页面信息筛选、v6.6 用户选色；比较 UX 以可验证的数据口径和决策效率为优先目标。

## v6.9 · Grid & Viewport Integrity Gate（对齐有秩序、内容可滚到底）

用户的 RepoVantage「版本发布」页与局部截图表明：**左右两列独立堆叠导致第二排顶部错位**，且发布明细接近页面下沿。截图不足以证明页面真的不可滚动或内容被裁切，因此**对齐属于可见视觉问题；底部是否真实溢出必须运行浏览器并滚到终点检查**。

- **先定 Grid 契约**：新数据看板/主要页面重排时读 `references/grid-alignment-and-viewport-safety.md`。同级模块优先共享内容边界、列线、同一排顶部和分组 gutter；若上一排卡片高度不等，下一排仍使用**共同的新行起点**。切勿默认左列一串、右列一串各自 flex 纵排。可用 3:2、8:4、主图跨全行等有依据的宽度关系，**无需所有卡片等宽、等高**。
- **不对称有理由、不是随机错位**：商业图表、统计、表格等 Operate/Read 任务以稳定可比较的网格为默认；创意作品/摄影图库允许刻意 Masonry 或错列，但必须有阅读/内容/叙事理由。对图表内部的单位、时间轴、标签保留必要一致性，不用强行统一量纲。
- **底部不能不可达或被盖住**：允许页面高度大于视口并正常滚动。禁止用 `height:100vh;overflow:hidden`、过短容器或底部 fixed 栏把最后一条记录、X 轴或按钮裁掉。明确 window 还是 `main-scroll` 为真实滚动容器，核查 `min-height:0`、Grid `minmax(0,1fr)`、末端 padding、safe area 与固定工具条真实占位。
- **实际滚动终点验收**：桌面、低高度笔记本、窄屏下从首屏**真正滚到底**，最后一行/按钮/完整卡片底部应可达、无遮挡；若有固定操作条必须为其预留空间。图表/表格有合法局部滚动时应能发现与操作；尽量避免无理由的多级滚动。检查 200% 文字放大与横向溢出。
- **文档与校验**：参考 `references/repovantage-release-alignment-case.md`、`assets/grid-and-viewport-lab.html`（错列/共享网格/主图全宽 + 矮窗口与底部工具条模拟）。结构计划格式 `assets/layout-integrity.schema.json`，案例 `examples/layout-integrity-repovantage.json`，用 分别运行 `python3 scripts/validate_layout_integrity.py --repository` 与 `python3 scripts/validate_comparison_contract.py examples/comparison-contract-repovantage.json --repository` 检查声明式行/列/末端策略。可选 `node scripts/audit_rendered_layout.mjs --url http://127.0.0.1:5173` 运行**真实浏览器**几何审计并保存首屏/末端截图；需要目标工程已有 Playwright 或明确授权安装，静态检查不是浏览器 PASS 证明。

**验收失败应优先回到构图/容器滚动架构，不是随意调小卡片/文字、增加空面板或全局隐藏超出内容。** 保留 v6.8 按页面区分信息密度、v6.7 导航决策与 v6.6 用户颜色选择。

## v6.8 · Page Content Curation & Density Gate（总览留白、数据页高效）

用户的 RepoVantage 总览截图包含“从一个仓库开始”“三步使用说明”“三张分析功能卡”、多个近似主操作及重复的底部链接。**这些内容全部出现在总览，造成信息拥挤与留白失衡；仅靠增加 Card padding、换字体/颜色无法修复。**

**Page Content Curation Gate（新建页面/主要改版先于构图执行，局部 Bug 免重复访谈）：**

1. **每页先盘点主任务与访问状态**：读取 `references/page-density-and-content-priority.md`，按 overview / onboarding / analysis / operations / marketing / reading 识别角色，并区分 first_visit / returning / data_available / empty / error。不是把整个产品所有功能放进首页。
2. **先筛信息、再留白**：内容划分 `primary / supporting / conditional / deferred / removed`；次级/延后内容必须有可发现入口，重要警告、真实数据来源和用户要求不得为了美观删除。对教程、功能入口与重复操作做**整块删除测试**，而不是只调整文字、边框和卡片内边距。
3. **按页面而非全站设密度**：`assets/page-density-profiles.json` 包含 `airy / balanced / productive / compact` 四种可调整起点。**总览/欢迎页通常更舒展，数据分析和管理操作页面可以显著更高密度**；但图表刻度、图例、样本量和操作控件仍需可读。已有用户选择优先；Agent 仅推荐时记 `provisional`，不能冒充 confirmed。
4. **有意义的空间关系**：读取 `references/whitespace-and-surface-composition.md`。不同任务区之间可有充分留白，同组相关数据/操作靠近，卡片容器只服务明确的分组/交互/状态。不能凭固定 min-height、强行留白百分比或套娃卡片追求高级感。
5. **用户状态动态呈现**：首次使用只引导当前一步，回访展示继续工作/现有对象，不再反复展示完整新手教程；真实分析页呈现图表/表格/筛选与必要来源；空/错误态明确，不编造数据。
6. **质量与案例**：见 `references/repovantage-overview-density-case.md`、`assets/page-density-lab.html`（过载总览/精选总览/较密分析页）和 `examples/page-content-plan-repovantage.json`。运行 分别运行 `python3 scripts/validate_page_content_plan.py examples/page-content-plan-repovantage.json --repository` 与 `python3 scripts/validate_layout_integrity.py --repository` 核对信息保留、延后可达、主操作、状态与来源，**不能证明高级感或真实浏览器验收**。

v6.7 导航架构、v6.6 用户选色、v6.5 字体和 v6.4 构图仍有效；新的内容筛选决定**展示什么**，后续构图决定**怎么摆**。不同路由允许不同密度，但不随意改变用户已确认的颜色或导航。

## v6.7 · Navigation Architecture Gate（位置由任务、层级与屏幕决定）

**不能把“现在做的是 SaaS / 管理台”直接等同于使用左侧导航**；也不能在手机上原封不动塞入一整条 7–10 项的底部导航。导航属于信息架构和交互决策，应当在样式与导航组件实现之前决定。

1. **盘点信息架构**：数清真正的一级目的地及切换频率、栏目层级、页面 Tabs、上下文对象树、全局动作/搜索；区分“导航去哪”和“对当前内容执行什么操作”。看桌面/手机/可缩放窗口的真实使用习惯、内容需要的横向空间与用户已有明确要求。
2. **基于官方设计方法推荐**：读取 `references/navigation-architecture.md`、`assets/navigation-pattern-catalog.json`，从 Top only、Sidebar、Top+Side、Rail+Split、Mobile Bottom、Desktop Side→Mobile Bottom、Top+Bottom、Side+Bottom Actions、Focus/Minimal 等模式中挑选适合项目的 **2–3 个有实际结构差异**的方案，解释适用理由、局限与移动端变化。不按“网页一律顶部、后台一律侧边”的伪公式选择。
3. **用户选定/继承**：已有明确导航要求直接遵从；未指定时请用户选或明确委托，Agent 的首推仍为 `pending/unresolved`，不能悄悄固化为用户已确认。已有用户确认的成熟 IA 可继承，局部 Bug 不重复设计访谈。决策模板：`assets/navigation-decision.schema.json`，待确认示例：`examples/navigation-decision.pending.json`。
4. **解释“侧边+底部”含义**：桌面侧栏 → 手机底部属于**同一导航的自适应位置变更**；桌面侧栏 + 底部批处理/播放操作条属于**导航+上下文动作**，不能把底栏的操作按钮当成另一套全局导航。若 Top+Side 同屏，必须区分顶部全局与左侧局部职责，不得重复整套一级入口。
5. **响应式路线完整**：底部主导航通常适合 3–5 个同级高频入口；更多目的地应有可发现的 drawer/More 路径，不能删丢。跨断点稳定 route IDs/selected、滚动与任务状态，检验窄窗、旋转、返回、焦点、sticky/fixed 遮挡与安全区。
6. **真实验收**：参考原创交互式 `assets/navigation-layout-lab.html` 对比桌面/手机架构；用 `python3 scripts/validate_navigation_architecture.py --repository` 做静态校验，**它不是导航可用性或视觉审美通过证明**。真实浏览器仍需验证键盘、路由、深链接、窄屏与实际交互。

导航架构决策和 **v6.6 配色选择是分开的**：选择 Sidebar 不代表允许 Agent 重选深蓝主题。只能使用用户已确定或明确委托的颜色，并保持整个页面协调。原生 Android/Apple/Windows 的官方规范提供设计参考，不能逐条当成 Web 强制尺寸标准。

## v6.6 · 用户主导配色：Sidebar 必须与整个页面一起设计

用户提供的新 RepoVantage 截图表明：即使导航布局和选中态已经克制，侧栏的**深蓝背景 / 蓝色选中块 / Logo 蓝色**仍可能与旁边的主内容区缺少协调。**颜色是用户的选择，不是 Agent 的最终决定；Agent 提供基于真实设计案例的推荐和整页验证。**

**Color Choice Gate**（新建网站、重设计、用户对颜色提出要求时执行）：

1. **先继承用户意图**：核查已有品牌、用户明确的颜色/HEX、全站 Main/Topbar/Panel/Chart tokens 与真实截图；用户已指定颜色直接采纳，不再反复问，不得以“高级感”擅自换色。仅功能修复无需重开配色讨论。
2. **未知颜色才推荐**：读取 `references/sidebar-color-discovery.md`、`references/sidebar-color-reference-cases.md` 和 `assets/sidebar-color-directions.json`。基于项目用途、品牌、暗/亮模式与长期使用密度，向用户展示**2–3 组有理由的整页颜色组合**及权衡；不要只展示侧栏色块，也不要把参考品牌色直接当成自己的主题。可使用 `assets/sidebar-color-preview.html` 切换整页示例和直接输入 HEX。
3. **等待真实决定**：Agent 的首推只是 `recommended`，不是 `confirmed`。用户选择、自定义颜色或**明确授权** Agent 决定后，才能将配色写成 `approved`；分别标记 `confirmed` / `delegated` / `inherited`。若用户只委托布局设计，不等于授权更改品牌色。
4. **固定用户指定色**：若指定 `#RRGGBB`，对应角色必须原样保留；若和文字/状态对比冲突，应调整周围的文字、hover/selected、主区表面与边界，并向用户解释，不能悄悄改成 AI 偏好的蓝、绿、灰或另外一串 HEX。
5. **整页协调而非局部换肤**：把 **Sidebar ↔ Topbar ↔ Main ↔ Card ↔ Chart** 作为一个体系设计，验证色温、色彩权重、区域边界、图表序列与用户操作状态。主题 Token 仍以项目 MASTER 为唯一来源，侧栏角色可独立但不能独立成另一个品牌系统。
6. **证据与验收**：决策记录形状见 `assets/sidebar-color-decision.schema.json`，未确认示例为 `examples/sidebar-color-decision.pending.json`；用 分别运行 `python3 scripts/validate_sidebar_color_decision.py --repository` 与 `python3 scripts/validate_navigation_architecture.py --repository` 检查色板/来源/部分对比度与用户 HEX 不被覆盖。真实浏览器需要整页、不同状态与窄屏截图；脚本**不能客观判定美感**。

注意：用户确认的蓝、紫、粉、黑、白乃至自定义颜色都可以使用；禁止的是**Agent 在未征求意见时私自套常见模板**，不是任何一种具体颜色。真实品牌副色、警告、成功和数据序列必须保留其独立语义。

## v6.5 · 文案必要性与角色化字体层级

新的 RepoVantage 截图揭示了两个独立问题：`ANALYSIS STUDIO`、`仓库活动与协作 · 交互原型`、`01 / 总览`、`先看活动，再沿证据往下读` 等**没有信息增量的装饰文字**，以及过大的抽象 H1 与难以阅读的图表刻度、KPI 标签、样本数等之间的字级失衡。**这是内容架构和阅读层级问题，不是简单再换一个字体或颜色。**

- **Copy Necessity Gate**：读取 `references/semantic-copy-hygiene.md`。每个 eyebrow、英文副标、编号、口号和解释文字必须回答“删去会损失什么信息？”没有真实导航、状态、品牌或业务增量时合并/删除，开发者实现备注（如 `ECharts tooltip`）移到技术文档。**正常面包屑、正式品牌 Tagline、真实章节编号、图表单位/来源应保留。**
- **Type Role Gate**：读取 `references/typography-hierarchy.md` 和 `assets/typography-role-guidelines.json`。按 PageTitle / SectionTitle / Body / KPI / ChartAxis / Legend / Metadata 等角色设计字号、行高、字重和对比，别让工作台巨型口号压过极小的数据标注。所列 px 仅为设计起点，不是 WCAG 的统一字体尺寸规定。
- **审查与验证**：`python3 scripts/audit_readability.py <web-src> --format json` 只能给出人工复核线索，**不可自动删文案或宣称审美、WCAG 合格**。`assets/typography-reading-lab.html` 是原创正反对照示例。实际验收检查深/浅模式、中文数字混排、长文本、图表真实渲染与 **200% 字体放大**；没有浏览器证据则记为 NOT RUN。
- **适用范围**：主要针对 Operate/Read 工作台；Persuade/Experience 可在有品牌/叙事理由时使用大标题、英文小字或艺术排版，不能将工作台约束变成所有网站的统一模板。

## v6.4 · Composition First（从内容证据先决定页面结构）

**默认不从 SaaS 模板或调色板开始设计。** 用户提供的仓库分析截图表明：即使实现了组件复用、圆角和状态色，页面仍可能因为“巨大渐变 Hero + 蓝紫立方体 + 同宽指标卡 + 空白图表 + 高饱和洞察卡”的组合而缺乏实际设计判断。此类问题属于**布局与信息主次**，不能仅靠换色或减少竖条修复。

新网站 / 重大视觉改版依次执行：

1. **内容证据**：先标记当前页面真实的任务、主数据、重要操作、素材质量，区分 known/demo/unverified；完整规则见 `references/composition-first-design.md`。
2. **灰阶线框**：在挑选蓝/紫/绿、动画与组件之前，确定主视觉**到底是什么内容**，并说明哪些区域应该占据首屏面积；大型数据区无数据必须给空/加载/错误状态。
3. **真正不同的候选**：优先提出 **2–3 套在主区域、顺序、比例或信息分组上不同的构图**，不能把同一 Hero + 四指标 + 图表模板换三种颜色冒充选择。用户已确认布局、局部修复可跳过；用户“你自由发挥”意味着 Agent 自行比较并记录 `delegated`，而不是停在问卷里。
4. **配色有理由**：按品牌、受众、内容质感和颜色职责推导，见 `references/palette-art-direction.md`；不能把“技术/SaaS”自动映射到蓝紫色渐变，也不能机械换成所谓高级的苔绿/暖灰。
5. **去装饰与截图复盘**：先临时移除装饰渐变、阴影和无意义插画，判断首屏主任务能否成立；真实浏览器截图按结构/层级/配色/节奏/功能/组件细节分类审查。结构失败须回到构图，不准只调颜色宣称重设计。详见 `references/visual-critique-loop.md`。

结构计划模板：`assets/composition-brief.schema.json`，三种仓库分析方案：`examples/composition/repo-analysis.json`，可切换结构与去装饰的概念演示：`assets/composition-layout-lab.html`。运行 `python3 scripts/validate_composition_brief.py examples/composition/repo-analysis.json --repository` 只验证结构合理性和引用，**不能宣称自动鉴定审美优秀**。Operate 页面装饰占主导或图表空白却无数据状态属于返工信号；但作品集/品牌营销存在合理的大 Hero 与实验性审美，不做统一禁令。

## v6.3 · 高频工作台组件精修（截图反馈驱动）

用户提交过的侧边栏显示了一类实际反例：暗色蓝灰配色缺少明确秩序，导航选中同时叠加**大面积高亮底、侧边亮条、图标强调与不明含义的橙点**，主导航与“最近打开”对象还复用了相同的强激活样式。**不得把这一套组合自动作为默认导航模板**。但左侧指示线本身不是绝对错误——阅读目录、树形层级、时间轴等存在独立语义时可保留，并应说明理由。

- 侧边栏任务：必须加载 `references/sidebar-navigation-design.md` 和 `assets/sidebar-palette-examples.json`；先核对现有组件与色阶，分清 current route、recent object、hover、focus-visible 和业务状态。
- 高频工作台设计：加载 `references/workspace-component-refinement.md`，覆盖 Sidebar、Topbar、Card、Data Table、Tabs、Search 和 Split Pane 七类；默认通过**一种主要选中信号 + 清楚的语义与字级**表达层次，不堆积线条、强阴影、额外卡片与假装饰。
- 视觉对照：`assets/sidebar-refinement-gallery.html` 是独立可交互正反概念示例（浅/深主题、状态选择、Tab 与分栏键盘交互），不是用户实际项目修复证据。先使用 分别运行 `python3 scripts/validate_ui_patterns.py` 和 `python3 scripts/validate_sidebar_color_decision.py --repository` 检查色板/引用/示例状态，再在真实业务浏览器截图中验收。
- **审美例外**：有品牌叙事、IDE 树形结构、章节进度或用户明确要求时，轨道线、强视觉配色和创造性构图可以合理存在；不把“AI 味”当成可用正则量化的通用结论。任何例外都应保留独立业务含义、对比度与键盘焦点。

## v6.2 · 动画与可视化技术按场景选型

针对用户提供的《12 项前端动画与可视化技术选型指南》，**先明确视觉或数据目标，再选择技术，不因为想让页面酷炫就安装 12 项依赖**。这 12 项分属动画控制、文本拆分、2D/3D 渲染、WebGL 图像、业务图表、手绘、SVG 滤镜、粒子和物理引擎，不是 12 个相互替代的动画库。

- 查 `references/visual-tech-selection-12.md`，或使用 `python3 scripts/search_visual_tech.py --goal "商品 3D 产品旋转" --json` 查询候选。数据索引 `assets/visual-tech-catalog.json` 包含 12 项定位、场景、避雷、替代方案与 9 种组合。
- **默认** HTML/CSS/SVG + 框架原生动画；短时间线才选 Anime.js 或 GSAP；特殊文本、图表、2D/3D、shader、粒子和物理需求明确后才引入专项库。
- SplitText 可能指 GSAP 插件，也可能是 anime.js `splitText`：两套 API 独立，优先复用项目现有动画栈；SVG Filter 是浏览器原生能力而非 npm 库；Matter.js 物理计算不替代 PixiJS 绘制。
- 不允许同时让 CSS/GSAP/Motion/Anime.js 控制同一元素同一属性；Vue/React 卸载时释放时间线、Canvas/WebGL、图表、物理 runner、观察器和事件监听器。
- 强制 reduced-motion、失败静态回退、按需加载和目标设备实测，不以工具存在证明当前项目性能或动效已验收。用户明确选择的风格优先于自动技术推荐。

## v6.1 · 真实案例库按需复用

**优先复用已有的外部优秀案例，不重新编造品牌设计细节**：行业/风格规则参考 UI/UX Pro Max；真实品牌 `DESIGN.md` 案例参考 VoltAgent 的 84 个文档。前者是设计策略库，不等同于真实品牌案例；后者是社区分析/启发式转译，不是品牌官方 Design System。

设计访谈中应先根据真实用途和内容使用 `scripts/search_design_knowledge.py` 收敛方向，再运行：

```bash
python3 scripts/search_design_cases.py --query "咖啡 门店 食物" --style premium-showcase --limit 5
```

仅对命中的案例按需打开对应上游 `DESIGN.md`；**不能只根据案例名称或索引就声称掌握该品牌的实际设计**。`sampled` 表示本次读取过相关正文；`candidate` 表示尚待核验的候选；`indexed_unreviewed` 只是外部来源登记。遇到过时或不可靠的数据，重新检查原始网站/真实截图，并标注推断或未知。严禁无许可复制品牌图片、商标、专有字体或 Pro 内容。

文档与索引：`references/external-design-case-library.md`、`assets/external-design-cases.json`。保留上游仓库的 MIT 许可和出处说明，但其许可证不赋予第三方品牌资产使用权。用户已确定风格时不得被案例推荐覆盖。

## v6.0 · 设计能力与工程审查的任务路由

MauForma 不是固定的“极简皮肤”，也不是默认全站都用大图/卡片。**保留各作者审美立场的理由和适用性**，详见 `references/aesthetic-authorship.md`。禁止直接复制外部 Skill 指令、图片和受限资源；本包的八种风格资料均为 MauForma 独立编写。

1. **页面模式先行**：按访问目的确定 `Persuade / Operate / Read / Experience`（可有主次），再依据内容和素材推荐 2–3 个真正不同的风格方向。调用 `python3 scripts/search_design_knowledge.py --query "网站用途 展示内容" --mode Persuade --limit 3`；返回结果是**推荐，不是用户确认**，不能覆盖已确认的选择。
2. **Art Direction / Critique**：推荐时给出首屏视觉焦点、图文比例、构图、字体、信息密度、动效、优缺点、素材前提；进入组件开发前先做一次自我批判。详见 `references/art-direction-critique.md`。
3. **风格与原作者个性**：八种独立风格及适用/反例在 `assets/style-knowledge.json`、`references/design-style-catalog.md`。允许非对称、大留白、大胆排版、强动效，前提是内容、页面目标和性能许可；也允许高密度功能型工作台。三旋钮 `variance/motion/density` 建议范围为 0–10，不是限制上限。
4. **可持续的设计决定**：在用户项目中建立 `design-system/MASTER.md` 和按页面差异记录的 `design-system/pages/*.md`，并保存含 confirmed/delegated/inherited/unresolved 来源的决策记录。参见 `references/project-design-hierarchy.md`；页面例外不得破坏全局组件行为、品牌 Token 和无障碍。
5. **项目文件落地**：`python3 scripts/init_design_system.py --project-root ./ --name "My Product" --style premium-showcase --page home --mode Persuade` 默认仅预览；经用户确认后加 `--apply` 才写文件，默认禁止覆盖现有文件。选择来源必须正确标记，详见 `references/project-design-hierarchy.md`。
6. **Design DNA**：用户给出参考网站/截图时，记录观察 WHAT、解释 WHY（明确区分推断）、证据、放弃的替代布局、可迁移设计原则。详见 `references/design-dna-protocol.md`。
7. **工程审查与浏览器证据**：Vue/React 使用各自组件契约和性能规则；`python3 scripts/audit_frontend.py <web-src> --format json` 为**静态启发式风险检测**，不能替代真实视觉验收。若项目已有 Playwright，可运行 `node scripts/browser_qa.mjs --url http://localhost:3000` 收集截图/页面错误/溢出线索；未运行必须标记 NOT RUN。详见 `references/browser-qa-protocol.md`。
8. **只加载需要的知识**：局部修复直接读相关组件与审查规则；完整新网站依次执行内容发现 → **导航 IA 与响应式模式比较/确认** → 风格方案推荐 → 用户选择 → Master/页面设计规范 → Tokens → 共享组件 → 业务页面 → Browser QA。组件先行 Gate B 仍是强制门槛，不能被创意动效跳过。

## 必经设计确认阶段（新增 v5.2）

在新建网站或大规模重设计前，**先检查已有项目、内容和组件，再与用户确认视觉风格、信息密度与主视觉焦点**。对于颜色、动效强度和素材策略，只在确实影响实施且尚不明确时补问。详细依据见 [设计前访谈规范](references/design-discovery-interview.md)，项目决策采用 [设计简报 JSON Schema](assets/design-brief.schema.json)。

明确区分用户确认、AI 受托决定、沿用现有规范和尚未确定的选项。避免对已有设计稿或局部修改重复提问。用户可选混合信息密度，**不同页面应按内容、视觉冲击力和操作效率采用不同展示方式**。

实施流程：项目分析 → 用户设计选择/继承 → 视觉构图与信息层级 → Design Tokens → 共享组件 → 页面实现 → 动效与浏览器验收。后台的高效操作和展示页的大幅主视觉都可以在同一设计体系下共存。

### 用户不确定风格时：先问内容，再让用户选择（强制分支）

**不得让不知道设计术语的用户直接从“极简/科技/编辑式”等抽象风格词中盲选。** 若用户说“不知道、没想法、你推荐”，按如下顺序：

1. **内容发现**：检查已有项目；仅询问缺失的网站用途、要展示的内容（产品图片、作品、文字、商品、数据或功能）及用户最希望访客完成的操作。优先自然语言、每轮 1–2 个问题，不问已知信息。
2. **Agent 自行分析**：基于业务目标、内容形态、素材质量与目标用户推导首要视觉焦点、合适构图、各页面的信息密度、动效必要性。不要要求用户先掌握设计知识。
3. **给出 2–3 个具体方案**：每套用用户能想象的语言说明首屏第一眼看到什么、图文比例与布局、显示多少信息、色彩气质、动画行为和利弊；标明有依据的首推方案。避免只给抽象名称。
4. **用户选方向后再缩小范围**：按所选方案，仅就关键而未知的属性每轮提供 2–3 个细化选项（例如“全幅商品大图”或“左大图右文案”），解释视觉与体验差异，允许融合或委托 Agent 决定。不要一次抛出十项专业问题。
5. **记录真实决策来源**：Agent 推荐不等于用户已确认。保留 `confirmed/delegated/inherited/unresolved` 来源标记。已有品牌规范、明确偏好或小范围修复跳过完整流程。

详细规则与场景判断：`references/design-discovery-interview.md`；可直接模仿的逐轮对话：`examples/design-discovery-dialogues.md`。主题色、圆角、Anime.js/React Bits 等是视觉方向明确后才评估的实施细节，不应成为首次提问的负担。

## 阅读路由：只读取与任务有关的参考文件

| 任务 | 必读文件 |
| --- | --- |
| 任务中心/作业记录堆叠卡片、状态不可筛选、进度不可信、重试无授权 | `references/task-center-run-monitor-design.md`、`assets/task-center-reference-cases.json`、`assets/task-center-layout-lab.html`、`scripts/validate_task_center.py` |
| 多仓库/产品/技术对比页难用、只堆图、图表内部错位/标签重叠 | `references/comparison-page-design.md`、`references/chart-interior-alignment.md`、`assets/comparison-reference-cases.json`、`scripts/audit_comparison_ui.mjs` |
| 独立模块贴合 / 同级图表横纵间距失衡 / 内边距与组间留白混淆 / 间距节奏紊乱 | `references/semantic-spacing-rhythm-gate.md`、`assets/spacing-rhythm-patterns.json`、`scripts/validate_spacing_rhythm.py`、`scripts/audit_spacing_rhythm.mjs` |
| 模块上下/左右错列、第二排起点不同、底部卡片接近边界/无法滚动到底 | `references/grid-alignment-and-viewport-safety.md`、`references/repovantage-release-alignment-case.md`、`assets/grid-and-viewport-lab.html`、`scripts/audit_rendered_layout.mjs` |
| 总览信息过多 / 多层卡片 / 高级留白 / 数据页可更密 | `references/page-density-and-content-priority.md`、`references/whitespace-and-surface-composition.md`、`assets/page-density-profiles.json`、`assets/page-density-lab.html` |
| 多余小标题 / 伪章节编号 / 自动英文副标 / 开发者文案泄露 | `references/semantic-copy-hygiene.md`、`references/page-header-antipatterns.md`、`scripts/audit_readability.py` |
| 重要信息被小字淹没 / 字号平均化 / 视觉焦点错误 | `references/perceptual-hierarchy-gate.md`、`references/typography-hierarchy.md`、`assets/visual-priority-patterns.json`、`scripts/validate_visual_priority.py` |
| 整页大圆角框 / 连续记录过度卡片化 / 页面容器选型 | `references/surface-architecture-gate.md`、`assets/surface-control-patterns.json`、`assets/surface-control-layout-lab.html` |
| 中文按钮竖排 / 操作列挤压 / 控件文字断裂或裁切 | `references/control-geometry-gate.md`、`scripts/validate_surface_control.py`、`tests/surface_control_browser_smoke.mjs` |
| 组件默认化 / pill 泛滥 / 按钮或表格缺少质量 / 组合气质割裂 | `references/component-craft-gate.md`、`references/component-first.md`、`references/visual-qa.md` |
| 字号失衡 / 图表刻度难读 / KPI 标签 / 字体层级 | `references/typography-hierarchy.md`、`assets/typography-role-guidelines.json`、`assets/typography-reading-lab.html` |
| 新网站 / 大改版构图、空间布局和视觉焦点 | `references/composition-first-design.md`、`references/palette-art-direction.md`、`assets/composition-brief.schema.json`、`assets/composition-layout-lab.html` |
| 用户反馈页面模板化、配色糟糕或截图缺乏美感 | `references/visual-critique-loop.md`、`references/art-direction-critique.md`、`references/visual-qa.md` |
| 用户不确定视觉风格 / 需要设计访谈 | `references/design-discovery-interview.md`、`examples/design-discovery-dialogues.md` |
| 导航位置选型：顶部、侧边、底部、混合导航、手机自适应 | `references/navigation-architecture.md`、`assets/navigation-pattern-catalog.json`、`assets/navigation-layout-lab.html`、`assets/navigation-decision.schema.json` |
| 用户希望选择侧栏颜色 / 侧栏与主内容配色不搭 | `references/sidebar-color-discovery.md`、`references/sidebar-color-reference-cases.md`、`assets/sidebar-color-directions.json`、`assets/sidebar-color-preview.html` |
| 侧边栏 / 导航选中态 / 配色协调 | `references/sidebar-navigation-design.md`、`assets/sidebar-palette-examples.json`、`assets/sidebar-refinement-gallery.html` |
| 顶部导航 / 卡片 / 表格 / Tabs / Search / 分栏 | `references/workspace-component-refinement.md`、`references/visual-qa.md` |
| 真实品牌优秀案例 / DESIGN.md 参考 | `references/external-design-case-library.md`、`assets/external-design-cases.json`、`scripts/search_design_cases.py` |
| 风格知识库 / 艺术指导 / 作者审美 | `references/aesthetic-authorship.md`、`references/design-style-catalog.md`、`references/art-direction-critique.md`、`assets/style-knowledge.json`、`scripts/search_design_knowledge.py` |
| 参考网页/截图提取设计 DNA | `references/design-dna-protocol.md`、`examples/design-dna-record.json` |
| 项目 Master 与页面差异 | `references/project-design-hierarchy.md`、`examples/design-system/MASTER.md` |
| React 组件 API 与性能 | `references/react-component-engineering.md` |
| Vue 组件 API 与响应式 | `references/vue-component-engineering.md` |
| 前端静态审查 / 浏览器 QA | `references/browser-qa-protocol.md`、`scripts/audit_frontend.py`、`scripts/browser_qa.mjs` |
| 所有前端实现 | `references/frontend-architecture-and-gates.md`、`references/design-system.md`、`references/component-first.md` |
| 判断网站类型与密度 | `references/web-scope-and-app-types.md`、`references/good-vs-bad.md` |
| Vue / Nuxt | `references/framework-vue-nuxt.md`、`examples/vue3-web-components.md` |
| React / Next | `references/framework-react-next.md`、`examples/react-web-components.md` |
| Svelte、Angular、Solid、Astro、原生 Web | `references/framework-other-web.md` |
| 技术栈选型与截图里的 11 组推荐 | `references/stack-guide-11-items.md`、`references/framework-support-matrix.md` |
| 提示词与 Agent 协作 | `references/ai-frontend-prompt-policy.md`、`examples/prompt-library-web.md` |
| 创意官网、产品宣传与互动视觉 | `references/creative-component-libraries.md`、`examples/creative-library-recipes-react-vue.md`、`assets/creative-effects-gallery.html` |
| Ant Design、Ant Design Vue、Element Plus、MUI 等后台组件库 | `references/enterprise-ui-library-guide.md`、`references/framework-support-matrix.md` |
| 12 项动画/可视化技术选型 | `references/visual-tech-selection-12.md`、`assets/visual-tech-catalog.json`、`scripts/search_visual_tech.py` |
| 用户是否希望交互/页面切换动画、动效强度尚未确认、动效缺失或突然跳变 | `references/motion-consent-experience-gate.md`、`assets/motion-decision-patterns.json`、`scripts/validate_motion_decision.py`、`assets/motion-choice-layout-lab.html` |
| 仅页面切换有动画 / 组件动效缺失 / 所有效果只有 fade | `references/component-motion-choreography-gate.md`、`assets/component-motion-patterns.json`、`scripts/validate_component_motion.py`、`assets/component-motion-lab.html` |
| 动画选择 | `references/animation-engine-selection.md`、`references/animation-integration-lifecycle.md` |
| Anime.js 动效目录 | `references/animejs-official-capabilities.md`、`references/animejs-motion-recipes.md`、`references/animejs-easing-complete.md` |
| 反例、审查与交付 | `references/quality-antipatterns-by-page-type.md`、`references/page-header-antipatterns.md`、`references/ui-review-rubric.md`、`references/visual-qa.md` |

## 不可跳过的前端执行顺序

0. **通用视觉前置条件**：所有新设计/重大页面改版必须为主要相邻区块先确定 `inside/peer/section/connected` 的关系与空间 token，读取 `references/semantic-spacing-rhythm-gate.md`。CSS 能对齐并不代表间距合理；独立功能区贴合应被识别，真正连接的组件不应强制拉开。重大设计前同时判断 `references/surface-architecture-gate.md` 中的容器选型、`references/control-geometry-gate.md` 的控件尺寸与断行策略。不要用巨型 Card 代替页面信息结构，不得生成会把短操作中文字逐字堆叠的按钮。所有新设计和重要重构均先阅读 `references/perceptual-hierarchy-gate.md` 与 `references/component-craft-gate.md`。不要将其变成新的问卷；基于已有产品信息直接判定，不需要用户重复选择。已有设计系统/单点修复仅复核受影响的内容与组件。可用 `scripts/validate_visual_priority.py` 辅助检查计划，静态检查不等于美感验收。
1. **Gate 0：侦察、Design Discovery 和模式识别**。在新网站/重大视觉重构中将动效偏好视为独立决策：先读取历史确认，未知则明确提出体验级选项，不能默默定零动画；读 `references/motion-consent-experience-gate.md`。读取既有设计决策（Master/页面例外）；读取 `package.json`、锁文件、现有路由、框架、UI 库、样式系统、构建命令、页面结构、测试约定，记录技术选择依据；已有项目不能随意换框架。
2. **Gate A：先内容筛选、任务类型/比较数据契约、导航架构和 Grid 对齐，再谈主题**。对 run_monitor 页面必须先判断状态、进度、需处理动作和筛选流程。统计数字能成为状态过滤就不必长期占左侧整列；不按“后台页面固定左右两个大卡”构图。对 compare 页面继续使用 v6.10 数据契约。若是“项目比较/多对象对比”页面，v6.10 优先定义决策问题、选中对象与实际系列/表格、共同时间窗、指标单位、缺失覆盖，再选择矩阵/趋势/差异摘要结构；不能仅用卡片排版替代比较任务。进入排版前读取 v6.9 Grid & Viewport Integrity：明确共享网格的行/列边界、非对称的用途、目标滚动容器与页面底部可达性。数据页不能让两列各自独立向下堆叠，造成同级模块第二排错位。每个页面先执行 v6.8 Content Inventory：确认主任务和用户状态，标记 primary/supporting/conditional/deferred/removed。总览不要同时铺开重复教程和功能目录；分析详情保留完整且可读的证据。再进入导航 IA、灰阶构图和配色。新站/重大改版先评估全局与局部目的地数量、切换频率和手机/桌面层级；参考 `references/navigation-architecture.md` 的 Navigation Architecture Gate 选择 Top/Side/Bottom/组合与响应式方式，记录用户真实决策。先执行 `references/composition-first-design.md` 的 A0 内容证据 → A1 无装饰构图 → A2 真正不同的区域布局备选 → A3 数据状态 → A4 配色理由；用户自选/授权决定后再进入 Design Tokens。参考 `examples/composition/repo-analysis.json`，可用 `scripts/validate_composition_brief.py` 检查方案是否只是换色。保存用户确认的方向及推荐理由；运行 Art Direction Critique，不把未确认的建议记为用户确认。如果用户不确定风格，先按“用途/内容发现 → Agent 推荐少量具体方案 → 用户选择 → 细化属性”的流程确认设计方向；针对业务类型给出信息架构、视觉密度、色彩角色、Typography、Spacing、Radius、Elevation、Motion Tokens（浅/深色）。在整个项目只有一个真实 Tokens 来源，非每页硬编码颜色。**对侧边栏先分析中性色阶与选中/悬停/焦点的关系，不能把多套蓝色和装饰性状态点随意拼接。**
3. **Gate B：组件优先**。共享 Stack/Grid/PageSection 负责同级/章节的 gap，Card 内 padding 只负责内容；检查横向 column-gap、纵向 row-gap、响应式单列后 peer gap 是否保留，不可凭组件默认 margin 使页面区块随机粘连。在组件库基础形态/状态 Gallery 中增加真实的 Component Motion Showcase（选中指示器、局部展开、状态形态/反馈等具体机制）；要对所有高价值真实交互作选择，不许把路由转场作为组件完成的证据。建立共享 Motion Tokens 和各组件实际存在交互的微动效契约：即使选择无额外动效也必须保留可见状态，B/C 要有真正的进退场/状态连续性；不能只做一个 Button hover 就宣称完成全部交互过渡。组件画廊与组合页应含必要的 Surface 变体、原子短操作标签在窄屏/放大时的完整显示及动作分组 fallback；需预留操作列的固有宽度，单独的 `white-space:nowrap` 并不保证布局可用。RunList/RunStatus/Progress/RunDetail/RetryAction 要从同一状态模型中得出标签、进度、计数及可执行操作；不要每条都生成重复“百分比未知”文案；TaskCenter 的详情优先使用可访问的弹层/独立页/展开行。复杂 log 不默认全部塞主列表。比较页需复用 RepositoryPicker/ChartLegend/MetricMatrix 等关联组件的统一 entity ID 和颜色 Token，确保选择变更正确刷新图例、系列、指标列。所有图表组件增加 Plot Region/Axis/Label 视觉检查，不只验证 Card 边框；Canvas 标签需要实际浏览器复核。共享 ChartPanel/Table/RecordList 必须有可追踪的共同内容边界与 row/column 约束；不能让内部 canvas 或长标签撑破 `minmax(0,1fr)`。BottomActionBar 若固定必须预留滚动结束空间，或优先进入正常布局。创建 Card / FeatureGrid / Onboarding / DataPanel 前先判断容器是否有独立业务、交互、数据或状态意义；无信息增量则合并/移除，不为了组件复用而增加套娃卡片与重复功能导览。实现导航组件前必须根据 v6.7 选定架构明确全局/局部/页面内 Tab/底部操作职责，避免把顶部+侧边+底部做成三套相同主菜单；检查自适应路由保留。如果涉及侧栏/全站颜色变更，先通过 v6.6 Color Choice Gate：已有明确颜色直接继承或按指定 HEX 处理；未知时先展示 2–3 套含主内容的对照，取得用户选择或明确委托后再覆盖全局 Tokens。开发共享 PageHeader/Chart/Table 之前需完成 v6.5 文案与字级检查：不自动注入 kicker、抽象口号、数字章节；重要图表刻度、n 值、单位和来源不能做成不可读的小字。列出复用/改造/新增组件清单，先建立或修正 `UiButton/Field/Dialog/PageHeader/Navigation/Table/Feedback` 等共享组件及各状态，制作组件展示页。工作台需要进一步区分 Sidebar / RecentItem / Tabs / Table / Search / SplitPane 的**状态与行为契约**，不能全部借用同一种 Active 卡片。**Gate B 未通过，不允许批量铺业务页**。但修复单个故障时不必强制重构全站。
4. **Gate C：业务与动效**。先对组件的 `trigger/from-to/mechanism/interrupt/reduced` 作覆盖设计与实现，再考虑页面级转场；组件需要根据职责选择不同机制、优先已有基础库。遵守已确认或明确委托的动效范围，设计过渡来自真实触发/状态变化，避免自作主张只给全站静态或额外引入夸张的滚动动画。按真实业务组合组件，先保证真实状态、API、权限与数据流程。先确定场景：
   - **官网/品牌/产品介绍/作品集**：允许按需选择 React Bits、Vue Bits、Inspira UI、Magic UI、Aceternity UI 的**单个**创意组件，不能取代原有功能组件；先检查原生框架、许可证、WebGL/GSAP 依赖、动效减弱和移动端回退。
   - **管理后台/工作台/企业表单**：优先复用 Ant Design / Ant Design Vue / Element Plus / MUI / Naive UI / Arco / PrimeVue 等**一套**主组件库，按共享 Ui 契约集中主题，默认轻量 CSS/框架微交互，不将 WebGL 背景批量引入业务工作区。
   - 所有动效优先 CSS/框架原生能力；确有需要才选择 Anime.js/Motion/GSAP。避免同一效果叠用多个引擎。
5. **Gate D：静态风险审查 + 浏览器证据 + 视觉验收**。整体截图必须审查独立模块的上下/左右间距、同级节奏、内部标题归属及有意共边，发现无语义的零间距/无规律留白不能直接通过。若可给目标 DOM 添加关系标记与 token 契约，运行 `scripts/audit_spacing_rhythm.mjs` 测几何；未标记不得假装自动完成。检查真实组件级 Tab/Toggle/Accordion/List/Feedback 等可见变化，不只检查页面切换/弹层 fade；真实操作的动效需前中后、快速中断、减少动态效果和最终交互状态证据。对用户所选动效级别用真实浏览器操作检查动画有无、前中后状态、快速反复触发/取消、键盘焦点、减少动态效果以及组件卸载；未执行浏览器检查不可声称视觉动画已通过。必须实际验证重要控件短标签为完整的水平词组、无逐字折行/裁切/出屏，操作组根据宽度整体重排；整体查看外部容器是否有独立分组价值、行/列是否仍易读。先做全页面 P0/P1 扫读检查并与灰阶截图对比；在组件 gallery 检查主次内容、状态、交互与尺寸节奏，在整页检验不同组件是否和谐；重点查重要文字被过度弱化和“所有数字都巨型”两种相反错误。后台任务页新增状态筛选/计数一致性、未知进度与 0 的区分、失败/阻塞/已完成的按钮权限、详情焦点、窄屏列表与滚动终点检查。Mock 重试只能标“演示模拟”；要证明真实后端能力需实际 API/E2E。比较页必须验证已选对象与图例、可见或明确缺失的序列、矩阵列一致；图内 X 轴/绘图区基线及标签不碰撞，缺失不是零；所选对象切换、不同窗口和移动端比较结构能用。v6.10 可用 `audit_comparison_ui.mjs` 收集浏览器 DOM 风险，无法读 Canvas 内标签时标 NOT AUDITED，并人工看截图。对有图表/多卡片的页面新增**共享网格对齐检查与滚动终点检查**：实测内容超出视口能否正常滚动，最后图表轴、Release 行和按钮是否可见；固定栏是否遮挡，窗口 1280×720/390×844 等低高视口下是否仍可达。不要把“正常需要滚动”误报为 overflow，也不要在未打开浏览器时声称已修复底部裁切。对 Overview、Analytics、Operations 等路由分别审查：总览先减少重复信息和并列 CTA，分析详情保持较高密度且不隐藏数据来源。先筛选内容再调整留白，不允许只加 padding 宣称信息减负。导航结构变更还必须验证真实桌面/手机/窄窗口和断点前后相同的目的地 ID、主导航可达性、顶部/侧边/底部是否互相重复、返回与上下文状态、键盘焦点、fixed bottom 遮挡。色彩变更必须查看侧栏与主内容的整页截图，包含 Topbar、Card、Chart 和 hover/selected/focus；检查用户固定 HEX 是否原样保留。必须检查“小标题删除测试”、标题与 KPI/图例的阅读优先级、暗色文字对比与 200% 字体放大；字级不应简单全部放大或统一缩小。先进行去装饰/灰阶信息结构测试；若页面最大面积与主任务不一致，应回到 Gate A 改布局，而不是调渐变颜色。优先在现有测试环境完成构建和组件/流程测试，静态扫描只是提示；检查横向溢出、键盘焦点、屏幕阅读器语义、对比度、浅深主题、长文字、响应式、触摸、错误/加载/空状态、减少动态效果、性能、真实流程回归。**暗色导航需用真实截图检查重复强调色、左侧竖条是否有独立语义、最近打开与主导航是否混淆；本规则不机械禁止层级线。**把“未实际运行”如实标明。

## 框架隔离强制规则

- **视觉契约可移植，组件源码不能跨框架复制**；Vue 写 SFC + Composition API，React 写 TSX + hooks，其他框架按自身语法。
- 创意视觉与业务交互分层：React Bits/Vue Bits **不是 AntD 的替代品**；Ant Design React 与 Ant Design Vue 不共享源码。前者美术层可用在营销官网，后者业务层承担真实表单、表格、选择器和弹窗。
- **企业 UI 主库尽量只选一种**：React 可评估 Ant Design/MUI/Mantine/PrimeReact；Vue 可评估 Ant Design Vue/Element Plus/Naive UI/Arco Vue/PrimeVue；已有项目以原有库为准，不强制换库。
- 无论截图推荐什么：`lucide-react`、`Recharts`、`Zustand`、`react-resizable-panels` **不能被默认当成 Vue 项目依赖**。应查询 `references/stack-guide-11-items.md` 的真实框架支持。
- 2026 年官方源中 shadcn/ui 新项目默认 Base UI，但已有 Radix 项目仍保留 Radix，不自动迁移。`shadcn-vue` 与 React 的 `shadcn/ui` 是不同技术实现。
- dnd-kit 有新旧 API/适配层差异；Lucide Vue 的包名也存在版本迁移。**安装前根据项目依赖和官方 API 确认**，禁止拼凑旧版代码。
- 首选既有库与现有测试；禁止未经理由一次安装整套截图技术栈。**每一项外部库都必须回答：现有方案为何不够、引入成本如何、能否复用、是否经版本与许可证确认。**

## 视觉红线与允许的例外

- 后台/设置/表单页：默认紧凑页面标题，避免无用 Eyebrow、重复英文、80px Hero、空泛口号、无意义大留白；真实面包屑和必要的页面描述是例外。
- 展示型网站/作品集/活动首页：可以有大标题、创意渐变、舞台式动效，但不得掩盖关键信息、降低可访问性或造成性能问题。
- 避免“页面看起来很美但没有加载、错误、空状态和可点击逻辑”。**视觉完成不等于产品完成**。
- 所有动画有目的、可中断、可清理；优先 transform/opacity；支持 `prefers-reduced-motion`；动画资源加载失败不隐藏主要内容。

## 资源

- `assets/sidebar-refinement-gallery.html` — 七类高频工作台组件（包含侧栏正反例）的原创可交互概念对照；`scripts/validate_ui_patterns.py` — 色板对比度与结构校验，不能代替真实视觉验收。

- `assets/creative-effects-gallery.html` — 12 组原创 CSS/JS 交互动效概念预览（**不是** React Bits/Vue Bits 官方源码或精确演示），帮助挑选恰当的创意增强层。
- `references/creative-component-libraries.md` — React Bits/Vue Bits/Inspira UI/Magic UI/Aceternity UI 名称、效果、场景、技术边界和来源。
- `references/enterprise-ui-library-guide.md` — Ant Design、Ant Design Vue 等企业业务组件全景、主题接入、组件职责与选型。
- `assets/motion-gallery.html` — 114 种动效配方索引及 45 种缓动的交互原理演示（不等于全部官方内置特效）。
- `assets/page-header-antipattern-gallery.html` — 后台标题常见问题对照；`assets/preview.html` — 主题与密度样例。
- `assets/framework-decision.json` — 机器可读的框架/工具关系；`scripts/validate_web_skill.py` — 文档引用与覆盖度检查。
- `assets/reference-source/` — 用户提供的原站，仅供视觉设计原理分析；不复制原来的假数据、色盘或过时用法。

## v6.0 新增运行入口

```bash
python3 scripts/search_design_knowledge.py --query "甜品 食物 产品 摄影" --mode Persuade --json
python3 scripts/search_visual_tech.py --goal "手绘 插画" --json
python3 scripts/search_design_cases.py --query "甜品 咖啡 门店" --style premium-showcase --json
python3 scripts/init_design_system.py --project-root ./ --name "Project" --style functional --page dashboard --mode Operate
# 审核选择之后加 --apply 写入；已有文件不会覆盖
python3 scripts/validate_intelligence.py
python3 scripts/audit_readability.py --validate-catalog
python3 scripts/validate_composition_brief.py examples/composition/repo-analysis.json --repository
python3 scripts/validate_ui_patterns.py
python3 -m unittest discover -s tests -v
python3 scripts/audit_frontend.py ./src --format json
# 只有在项目已安装 Playwright 且允许访问开发服务器时：
node scripts/browser_qa.mjs --url http://localhost:3000 --out ./artifacts/mauforma
```

推荐结果不能自动转为 confirmed；真实浏览器渲染必须与静态审查区别标注。新增参考来源、原创风格表和样例在 `references/aesthetic-authorship.md`、`assets/style-knowledge.json` 与 `examples/project-design-review.md`。

## 交付输出要求

必须说明用户的动效决定来源 `confirmed/delegated/inherited/unresolved` 及实际实现的交互状态范围；未确认时不写“用户已选择无动画”。必须报告：**产品类型 / 现有框架 / 主业务 UI 库与创意层的选型及理由 / 许可证与依赖核查 / Tokens / 组件复用表 / 页面改动 / 动效及 reduced-motion 降级 / 优秀与反例自检 / 实际测试和未测试项**。先完成工作，再汇报；别用漂亮截图代替真实功能。引用版本易变的 API 时按官方文档复核。

> 官网上的功能/API 会迭代。本次官方资料核对日期：2026-11-02；具体依赖版本以项目锁文件和官方当前文档为准。
