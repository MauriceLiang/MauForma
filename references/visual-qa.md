# MauForma · 组件优先视觉 QA v2.0

## v6.13 · Surface & Control Geometry 独立验收

- [ ] 页面外层 mega-card / 内层工具栏 / 行卡层级是否均有独立语义？如果只是为了把所有内容框起来，是否评估过 open collection 或 single panel？
- [ ] 是否记录“为什么选这种容器、为什么不选另一个合理形态”；同一组件库中的 Card 不等于页面必需的外框。
- [ ] 高密度同构列表有稳定表头、列线、行分隔与操作扫描路径；商品/作品媒体卡、品牌 hero、专业分栏仍可根据内容合理保留。
- [ ] 短按钮、Tab、Badge、导航与状态标签没有中文逐字竖排、英文拆词、被裁切或宽度溢出；完整动作仍可读、可点、可键盘操作。
- [ ] 控件的**自然宽度+图标+内边距**和动作组/父列的宽度预算匹配；不要靠纯 CSS nowrap 掩盖固定窄列，窄屏优先整控件换行/row reflow/可访问 overflow menu。
- [ ] 对错误状态、权限不同、动作数量增多、长 CJK/English、手机小视口与 200% 放大在浏览器内验证；截图有操作列和末端滚动证据。未实测标 `NOT AUDITED`。
- [ ] 可运行 `scripts/validate_surface_control.py --repository` 核对设计决策样例；独立浏览器 demo 的 PASS 不能冒充目标项目已修复。

详见 `references/surface-architecture-gate.md`、`references/control-geometry-gate.md` 与 `assets/surface-control-layout-lab.html`。

## v6.12 · 所有 Web 页面通用的感知层级与组件质量门禁

- [ ] 当前视口的用户任务、P0/P1/P2/P3 信息分级明确；P0/P1 由决策价值定义，**不是见数字就放大**；用户第一眼与下一操作真实可辨。
- [ ] 在灰阶/去装饰后，首先读到的是重要对象/状态/正文/价格/作品，而不是非必要大标题或空面板；允许不同页面有不同的主角。
- [ ] 核心内容/必要字段/状态原因并非“全站 12px 小字”，也没有把所有信息统一放大；字体层级来自项目 tokens 与实际字体/语言/密度。
- [ ] 每个高频组件有独立职责、主/次文本、尺寸/变体/状态、可操作性和长内容策略；组合页面里控件、状态标签、列表行的基线、间距与字重协调。
- [ ] Badge/小胶囊、面板外壳、彩色状态、虚线/阴影都有可说明的用途；不能用默认组件皮肤代替真正的 Art Direction。
- [ ] 不同页面模式差异成立：Operate 重扫描，Persuade 重转化，Read 重正文，Experience 重作品和必要控制；不强迫四者采用同一种工作台美学。
- [ ] 检查真实桌面/窄窗、200% 放大、浅深模式、长中文/英文和错误/加载/空态；是否实际打开浏览器应有明确信息，静态校验结果不等于视觉 PASS。

流程与示例：`references/perceptual-hierarchy-gate.md`、`references/component-craft-gate.md`、`assets/visual-priority-patterns.json`；静态意图检查：`python3 scripts/validate_visual_priority.py --repository`（不评分“高级感”）。

## Gate A — 主题和 tokens（开始业务页面前）
- [ ] 产品视觉方向有一句解释；未强制照搬原站粉蓝渐变。
- [ ] `page/surface/surface-soft/text/accent/on-accent/focus/border/status` 等角色齐全。
- [ ] 主色、状态色职责分开；主题可以集中切换，页面没有无约束的硬编码色。
- [ ] 圆角、空间、字体和动效定义为共享 token；明确 showcase 或 productivity 密度。
- [ ] 浅/深主题在用户要求的模式下完成配色对比检查。

## Gate B — 组件（必须先于大规模页面实施）
- [ ] 盘点现有组件库，判断保留/封装/新增；没有为视觉重新写同一套原语。
- [ ] 按当前业务需要建立共享 Button、Field、Panel、Nav、Dialog、Status/Feedback 等最小组件集。
- [ ] 组件 API 有 variants、sizes、props/slots/events、适用状态和责任边界。
- [ ] 有可运行的组件展示页，覆盖相关 normal/hover/focus/disabled/loading/error/empty。
- [ ] 组件中没有散落的第二套主题颜色和随机圆角；页面的 `.button` 不覆盖基础组件核心外观。
- [ ] 输入可读，键盘焦点、标签关联与错误解释到位。

## Gate C — 业务页面视觉与功能
- [ ] 主次信息清晰，主题色没有抢走内容注意力，长中文标题和数字显示正常。
- [ ] 相邻区域间距表达关联；无无意义彩色大块、嵌套大卡片和阴影泛滥。
- [ ] 真实的保存、取消、删除、导航、表单校验、错误/空/加载状态没有被视觉修改破坏。
- [ ] 组件 hover、focus、pressed、disabled、loading 可辨认；状态不只靠颜色传达。
- [ ] 宽屏 + 窄窗/移动端布局验证；按项目需要完成暗色模式验证。
- [ ] Reduced Motion 下可使用，关键内容不依赖第三方动画库才能显示。
- [ ] 性能与可读性优先于极端玻璃、霓虹、过量弹性动画。

## 审核方法
1. 先运行项目的检查或构建；若使用本包主题，运行 `scripts/validate_design_system.py`。
2. 打开组件展示页（没有则临时制作状态样板）确认每个共享组件及各状态。
3. 打开真实业务页面，至少检查宽/窄窗口与关键状态；注意高 DPI、系统缩放和中文长文。
4. 对照 [good-vs-bad.md](good-vs-bad.md) 寻找反例，输出具体组件/页面/修复方式。
5. 按 [ui-review-rubric.md](ui-review-rubric.md) 打分，阻断项先修复再交付。
6. 如果没有真实浏览器/截图工具，必须说明“仅静态源码审查，未实际渲染验收”。

## 任务型页面标题 / AI 模板味（v2.1）

- [ ] 页面是管理/设置/列表/编辑时，没有默认照搬营销页的 eyebrow + 超大 H1 + 宣传口号。
- [ ] 小字、英文标题和副标题提供了不同的、真实的信息；不能解释价值的装饰文本已删去。
- [ ] 主操作靠近页面标题，核心列表或表单在常见窗口中尽早可见。
- [ ] 同类功能页通过 `UiPageHeader` 或现有等价组件保持一致；真实面包屑、技术术语及必要提醒得以保留。
- [ ] 对照 `references/page-header-antipatterns.md` 与 `assets/page-header-antipattern-gallery.html`，记录修复前后截图和明确理由。

## v6.2 · 复杂视觉技术专项检查

- [ ] 技术是按明确的视觉需求选型，已说明相对 CSS/SVG/已有库的增益，而非为效果堆库。
- [ ] 同一 DOM 元素/属性没有被 CSS、GSAP、Motion、Anime.js 重复控制。
- [ ] SplitText 标题字体加载/断点变化后仍可访问、语义正确，长文没有多余拆字。
- [ ] Three.js / PixiJS / Curtains.js / tsParticles 在卸载、隐藏或失败时停止和回收，提供静态回退。
- [ ] ECharts 图表数据来自真实业务且按需销毁，重要数值可通过文本或可访问表格理解。
- [ ] Matter.js 不负责 UI DOM 本身的交互语义，键盘操作/业务操作没有被物理效果阻碍。
- [ ] 在目标设备实测帧率、内存、CPU/GPU、缩放与窄屏，明确哪些条件未测。

## Gate E — 基础组件视觉精修（v6.3）

- [ ] 桌面深色 Sidebar 的背景 / surface / hover / selected / 主次文字 / icon / focus / border 组成可解释的色彩层级，真实文字与焦点对比在其实际背景上可辨认。
- [ ] 活动导航的高亮底、左侧亮条、图标与发光没有重复表达同一状态；若保留条形指示，应解释其独立的结构、时间线或章节语义。
- [ ] `aria-current`、hover、focus-visible 分别传达不同状态；即使去掉亮条也不会失去键盘焦点。
- [ ] 主导航与最近访问对象、帮助提示和账号区域存在清晰职责与视觉层级；业务警告点具备文字或标签。
- [ ] Topbar、Card、Data Table、Tabs、Search、Split Pane 按 `workspace-component-refinement.md` 核对共享 Token、交互与空/异常状态。
- [ ] 提交组件样例与真实浅/深主题截图；`sidebar-refinement-gallery.html` 只是正反概念，不能冒充真实业务页面 QA。

## v6.4 · 页面级截图质量门槛：结构要先过关

- [ ] 用户首要任务是否在首屏可识别？最大区域承载的是主体内容而非没有意义的 3D 装饰、营销 Hero 或彩色巨卡？业务类型适用性要明确。
- [ ] 主要图表/表格有真实数据、加载、错误或空状态；无来源的 Demo 不能被渲染成真实增长结论。
- [ ] 去除渐变、阴影、彩色 KPI 小图标和纯装饰插画后，页面的任务顺序、阅读路径、信息层级仍成立。
- [ ] 对布局类差评，整改是否调整了主/次区域面积、位置或分组，而不是仅把蓝紫替换成绿灰？
- [ ] 强色块是否承担信息/品牌/状态职责？有无多个大色块都争主角？
- [ ] 已在真实页面截图中检查桌面与窄屏；如果只是概念图或尚未运行，应标为 NOT RUN。

具体问题归因与重新构图路径：`references/visual-critique-loop.md`；不要凭 CSS 或随机审美分数断言优秀。

## v6.5 · 文案语义与排版可读性验收

- [ ] 所有小标题、英文副标、章节数字、口号与说明文字能否回答“删除会损失什么信息”？纯重复装饰已删除，真正有语义的面包屑、品牌和数据来源保留。
- [ ] 当前界面是否堆叠“仓库活动与协作”“看见项目如何演进”“01 / 总览”“先看活动”但没有更丰富的实际含义？
- [ ] 是否将 ECharts tooltip、React/Vue 框架术语或开发注释直接呈现给业务用户？技术教程除外。
- [ ] H1 → 区块标题 → KPI 数值/标签 → 图表轴/图例 → 采样说明的字级有真实角色与连续阅读顺序，而非随机超大/超小？
- [ ] 深色下图表刻度、UTC、n 值和数据来源是否无需费力就能阅读？这些是业务证据而非纯装饰。
- [ ] 桌面/窄屏、长仓库名、中文英文数字混排与文字 200% 放大时，信息是否完整且没有裁切/覆盖？
- [ ] 文字对比度参照 WCAG 2.2 相关标准核验；静态提示 12px 并非法定/标准强制下限，也不能替代实际视觉验证。
- [ ] 对于保留大字、品牌副标或正式章节编号，是否说明其内容与页面类型的正当理由？

`python3 scripts/audit_readability.py <src> --format json` 仅返回人工复核候选，不是自动判断或修复。

## v6.6 · SideBar 全局配色与用户确认（Gate A / D）

- [ ] 用户明确说颜色名/HEX 时是否被尊重？若已经选过，是否**没有**重复问颜色或擅自换色？
- [ ] 颜色未定且任务涉及重新配色时是否展示 **2–3 套 Sidebar + Main + Topbar + Card + Chart** 的整体搭配，而不是三张只看侧栏的纯色卡？
- [ ] Agent 推荐是否仍是 `pending/unresolved`，没有把“推荐 A”假写为 `confirmed`？用户明确委托颜色时才可使用 `delegated`。
- [ ] 用户给定的精确 HEX 是否在最终 Token 里完全一致？如因可读性存在风险，是否明确解释并调整文字或辅助表面，不私自换用户目标颜色？
- [ ] 侧栏相对主内容区的色温、亮度与边界有明确理由，是否和顶部栏、卡片、图表序列/状态色协同？
- [ ] 选中态、hover、focus 在完整页面浅/深主题上可辨认；关键文字与控件/图形对比已在实际渲染中验证？
- [ ] 浏览器验证的截图包含**完整页面及 sidebar 与 main 的接缝**，不是仅截图侧栏；若未运行浏览器则标记 NOT RUN。

测试命令：`scripts/validate_sidebar_color_decision.py --repository` 只做静态色值和选择记录检验，不对配色美感自动评分。配色方向详见 `references/sidebar-color-discovery.md`。

## v6.7 · 导航架构与响应式可用性（Gate A / D）

- [ ] 一级导航数目/层级/切换频率及全局、当前项目、页面 Tabs、上下文操作已经分开说明？为何选 Top/Side/Rail/Bottom/组合，而不是“后台自动 Sidebar”？
- [ ] 顶部+侧边时是否**真的不同作用域**；同一视口是否重复同一套一级入口？底部操作按钮是否错误冒充导航？
- [ ] 桌面侧栏→手机底部时只展示合适数量的高频目的地，其他可从 More/drawer 访问？路由 IDs 和顺序在断点前后稳定？
- [ ] 小屏、横屏、窄窗口、窗口 resize、浏览器返回、深链接是否保留当前选择、过滤和任务上下文？
- [ ] fixed/sticky 底栏、键盘、safe area、浮层、抽屉遮罩是否遮挡焦点或主内容？
- [ ] 多个 `nav` 是否用合理而不同的 accessible names，`aria-current` 用于真实当前页，`aria-selected` 只用于 Tabs？是否支持键盘与 Skip to main？
- [ ] 用户明确选择的导航结构和颜色是否保留，Agent 推荐没有被当作用户授权？
- [ ] 真实浏览器桌面/手机截图、菜单开合/导航跳转是否执行？未运行时标 NOT RUN，`assets/navigation-layout-lab.html` 只算概念示例。

规则 `references/navigation-architecture.md`；静态检查 `python3 scripts/validate_navigation_architecture.py --repository`。

## v6.8 · 逐页 Content Curation / Density / Whitespace 验收

- [ ] 总览是不是把“当前任务 + 三步教程 + 功能入口三卡 + 重复链接”全部展现？能否下沉/删除无增量整块内容，而非只调 padding？
- [ ] 每个页面首要任务明确，主操作不和多个同等级 CTA 竞争？
- [ ] 同一功能是否同时在导航、介绍卡、帮助卡与页脚反复出现？下沉后依旧有清晰可达入口？
- [ ] 首访、回访、真实数据、空态、失败时是否按条件展示正确内容，而不是把新手指南永久驻留？
- [ ] 每个容器是否有独立交互/数据/分组意义，装饰性外卡套内卡已去除？
- [ ] Overview 可以 airy/balanced，Analysis/Management 可以 productive/compact；密度增大不代表图表标签/来源/错误信息被隐藏或变成 10px？
- [ ] Macro 组间间距、meso 组内关系、micro 控件间距是否表达真实层级，不靠 min-height 撑空白或一律缩小字体？
- [ ] 真实桌面与移动/窄屏、文字 200% 放大和不同用户状态是否截图检查，未运行是否标 NOT RUN？

详细要求见 `references/page-density-and-content-priority.md`、`references/whitespace-and-surface-composition.md`、`references/repovantage-overview-density-case.md`；静态工具只能检查决策记录，不能自动评定高级感。

## v6.9 · Grid / Alignment / Scroll-End（视觉与运行时双验收）

- [ ] 页面标题、筛选、主内容、同级 ChartPanel 是否使用可追踪的统一内容边界与列 gutter？
- [ ] 同一排模块顶部是否对齐？若上一排左右高度不同，第二排是否仍在共同的行起点开始（而非两列分别堆叠成瀑布流）？
- [ ] 3:2 / 8:4 / 主图整行等不对称是否有数据主次和阅读理由？没有则回到 Grid；不强制等宽等高。
- [ ] 图表、列表轴线、时间范围和单位是否清晰，有共同的内部基线/边距，且没有为了对齐伪造数据尺度？
- [ ] 真实页面/主滚动容器可以滚到**最后一项内容的边框、图例、按钮与记录**；正常跨首屏滚动不算 Bug。
- [ ] 滚到底时末端仍有适当内边距，不能被 `overflow:hidden`、固定高度或固定底栏盖住；safe-area 和真实工具栏高度已计算？
- [ ] 1280×720 等矮窗口、390×844 手机宽度以及更窄视口下没有无法到达的底部控件或非预期横向溢出？
- [ ] 200% 放大、长标签、图表 tooltip、键盘焦点与页面返回时内容完整可达？
- [ ] 审查报告将截图中“卡片靠近底边”的**疑似风险**与真实 DOM 的裁切/不可滚动**已确认问题**分开记录？
- [ ] 实测含首屏截图 + 最大滚动位置截图（含底边）。仅运行 `validate_layout_integrity.py` 不可声明浏览器 PASS。

详细设计 `references/grid-alignment-and-viewport-safety.md`，实例 `references/repovantage-release-alignment-case.md`，可选实测 `node scripts/audit_rendered_layout.mjs --url http://127.0.0.1:5173`（Playwright 需可用）。

## v6.10 · Chart Interior 与多对象比较页专门 QA

- [ ] **外框对齐还要看图内**：Plot Area 的起点、X 轴/图例基线、边距、日期 label 是否协调，不因面板等高而误认为图内已对齐？
- [ ] 柱图/散点图上的数字、均值标注与点、边界有没有真实重叠或被裁切？同一数据点是否重复两处文字？
- [ ] 已选对象 IDs 是否与图例、真实 series（包含 no_data/partial 标记）、表格列完全一致？截图只有一条可见线但选了多个仓库时有没有解释？
- [ ] 共享时间区间、桶、单位和指标口径是否清楚，未采集/样本不足是否用 null/“—”而不是 0？不同仓库覆盖率是否影响公正性？
- [ ] 比较任务是否在一屏内能看到选谁、主要区别、趋势和矩阵入口；是否有长驻过宽的选仓库栏、大块信息稀薄的“口径”卡等无效容器？
- [ ] 表格对象列和指标行稳定、可扫描；用户能切换对比对象/筛选差异/查看详情且全组件同步？
- [ ] 手机端是否可发现至少二项对比或清楚的对象切换，内容不靠超小字挤成三列？
- [ ] 真实浏览器有比较前后选择切换、图例/曲线、放大文字、横向/纵向滚动的截图；Canvas 内标签未实际检查时标 NOT AUDITED 而非 PASS。

参考 `references/comparison-page-design.md`、`references/chart-interior-alignment.md`、`references/repovantage-comparison-case.md`。可用 `python3 scripts/validate_comparison_contract.py --repository`，但静态契约测试不等于真实曲线渲染检查。

## v6.11 · Task Center / Run Monitor 专项 QA

- [ ] 是否识别为自动作业监控，而非把人工 Kanban、比较页或指标仪表盘模板直接复用？
- [ ] 状态概览数字是否有实际用途（筛选、定位）？是否长期占用大面积侧栏却没有独立筛选价值？
- [ ] 任务行能否快速读到：对象、任务类型、状态、进度/当前阶段、更新时间、允许动作；全列表是否充斥重复模板句或大块空白？
- [ ] 统计计数是否从同一数据范围推导，`attention` 归类是否一致，过滤后可见行数/计数口径是否清楚？
- [ ] 进度有真实 completed/total/unit 吗？没有确定分母时是否不绘制虚构百分比；部分完成和错误状态是否明确原因？
- [ ] 重试仅对有实际能力、授权和合适生命周期的作业出现；阻塞/完成/排队不被误当作可直接重试？
- [ ] 点击详情后能够查看真实阶段/错误/日志（真实系统），模拟示例不假装服务端已重试成功？
- [ ] 状态过滤、任务搜索、排序、刷新时不意外丢失用户上下文；自动更新是否说明来源/时点？
- [ ] 窄屏行/卡仍可读、按钮键盘可达、最后一条任务能正常滚动到底，长仓库名/错误原因不会横向溢出？
- [ ] 对真实任务页还需后端数据集成/权限/E2E，独立 Mock 示例的 Chromium 测试不能当真实服务验收。

参见 `references/task-center-run-monitor-design.md`、`references/repovantage-task-center-case.md`、`scripts/validate_task_center.py`。
