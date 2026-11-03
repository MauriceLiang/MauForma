---
name: mauforma
description: MauForma — Web-first, framework-aware, component-first frontend design and implementation Skill for Vue/Nuxt, React/Next, Svelte/SvelteKit, Angular, Solid, Astro and vanilla HTML/CSS/JS. Establish design tokens and reusable components before pages; create coherent visual systems, accessible responsive UI, purposeful motion and detailed good/bad examples. Priority depth: admin/SaaS interfaces, applicable to all websites and web apps. Includes Anime.js v4 catalog, React Bits / Vue Bits / Inspira UI creative components, Ant Design / Ant Design Vue and other enterprise libraries, Motion/GSAP/CSS engine choices, and enforceable agent prompts.
---

# MauForma · Web-first 前端视觉与工程 Skill v6.5

**品牌**：MauForma（Maurice + Forma）。原 Soft Precision UI v5.0 的完整能力保留，现已扩充为内容驱动艺术指导、设计知识库、项目级设计规范、组件工程与 QA 的综合 Web Skill。

**定位**：网页设计与前端实现（Web-first）。支持所有网页类型，**当前专项深化后台管理/SaaS**，但绝不把其他网站套成后台模板。框架：Vue 3 / Nuxt、React / Next.js、Svelte / SvelteKit、Angular、Solid、Astro、HTML/CSS/JS；若是 Electron/Tauri 的 **Web 前端层**也适用。**不以 SwiftUI、AppKit、原生 Android 等非 Web UI 为直接适用对象**。

**主原则**：审美统一 ≠ 每页一个模板。统一设计语言 + 共用组件 + 符合具体业务的信息架构 + 恰当动效 + 可访问、可测试的功能。允许自主创作主题色，不固定用户参考网站的蓝紫粉渐变。

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
- 视觉对照：`assets/sidebar-refinement-gallery.html` 是独立可交互正反概念示例（浅/深主题、状态选择、Tab 与分栏键盘交互），不是用户实际项目修复证据。先使用 `python3 scripts/validate_ui_patterns.py` 检查色板/引用/示例状态，再在真实业务浏览器截图中验收。
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
8. **只加载需要的知识**：局部修复直接读相关组件与审查规则；完整新网站依次执行内容发现 → 风格方案推荐 → 用户选择 → Master/页面设计规范 → Tokens → 共享组件 → 业务页面 → Browser QA。组件先行 Gate B 仍是强制门槛，不能被创意动效跳过。

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
| 多余小标题 / 伪章节编号 / 自动英文副标 / 开发者文案泄露 | `references/semantic-copy-hygiene.md`、`references/page-header-antipatterns.md`、`scripts/audit_readability.py` |
| 字号失衡 / 图表刻度难读 / KPI 标签 / 字体层级 | `references/typography-hierarchy.md`、`assets/typography-role-guidelines.json`、`assets/typography-reading-lab.html` |
| 新网站 / 大改版构图、空间布局和视觉焦点 | `references/composition-first-design.md`、`references/palette-art-direction.md`、`assets/composition-brief.schema.json`、`assets/composition-layout-lab.html` |
| 用户反馈页面模板化、配色糟糕或截图缺乏美感 | `references/visual-critique-loop.md`、`references/art-direction-critique.md`、`references/visual-qa.md` |
| 用户不确定视觉风格 / 需要设计访谈 | `references/design-discovery-interview.md`、`examples/design-discovery-dialogues.md` |
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
| 动画选择 | `references/animation-engine-selection.md`、`references/animation-integration-lifecycle.md` |
| Anime.js 动效目录 | `references/animejs-official-capabilities.md`、`references/animejs-motion-recipes.md`、`references/animejs-easing-complete.md` |
| 反例、审查与交付 | `references/quality-antipatterns-by-page-type.md`、`references/page-header-antipatterns.md`、`references/ui-review-rubric.md`、`references/visual-qa.md` |

## 不可跳过的前端执行顺序

1. **Gate 0：侦察、Design Discovery 和模式识别**。读取既有设计决策（Master/页面例外）；读取 `package.json`、锁文件、现有路由、框架、UI 库、样式系统、构建命令、页面结构、测试约定，记录技术选择依据；已有项目不能随意换框架。
2. **Gate A：先构图，后艺术指导与配色**。先执行 `references/composition-first-design.md` 的 A0 内容证据 → A1 无装饰构图 → A2 真正不同的区域布局备选 → A3 数据状态 → A4 配色理由；用户自选/授权决定后再进入 Design Tokens。参考 `examples/composition/repo-analysis.json`，可用 `scripts/validate_composition_brief.py` 检查方案是否只是换色。保存用户确认的方向及推荐理由；运行 Art Direction Critique，不把未确认的建议记为用户确认。如果用户不确定风格，先按“用途/内容发现 → Agent 推荐少量具体方案 → 用户选择 → 细化属性”的流程确认设计方向；针对业务类型给出信息架构、视觉密度、色彩角色、Typography、Spacing、Radius、Elevation、Motion Tokens（浅/深色）。在整个项目只有一个真实 Tokens 来源，非每页硬编码颜色。**对侧边栏先分析中性色阶与选中/悬停/焦点的关系，不能把多套蓝色和装饰性状态点随意拼接。**
3. **Gate B：组件优先**。开发共享 PageHeader/Chart/Table 之前需完成 v6.5 文案与字级检查：不自动注入 kicker、抽象口号、数字章节；重要图表刻度、n 值、单位和来源不能做成不可读的小字。列出复用/改造/新增组件清单，先建立或修正 `UiButton/Field/Dialog/PageHeader/Navigation/Table/Feedback` 等共享组件及各状态，制作组件展示页。工作台需要进一步区分 Sidebar / RecentItem / Tabs / Table / Search / SplitPane 的**状态与行为契约**，不能全部借用同一种 Active 卡片。**Gate B 未通过，不允许批量铺业务页**。但修复单个故障时不必强制重构全站。
4. **Gate C：业务与动效**。按真实业务组合组件，先保证真实状态、API、权限与数据流程。先确定场景：
   - **官网/品牌/产品介绍/作品集**：允许按需选择 React Bits、Vue Bits、Inspira UI、Magic UI、Aceternity UI 的**单个**创意组件，不能取代原有功能组件；先检查原生框架、许可证、WebGL/GSAP 依赖、动效减弱和移动端回退。
   - **管理后台/工作台/企业表单**：优先复用 Ant Design / Ant Design Vue / Element Plus / MUI / Naive UI / Arco / PrimeVue 等**一套**主组件库，按共享 Ui 契约集中主题，默认轻量 CSS/框架微交互，不将 WebGL 背景批量引入业务工作区。
   - 所有动效优先 CSS/框架原生能力；确有需要才选择 Anime.js/Motion/GSAP。避免同一效果叠用多个引擎。
5. **Gate D：静态风险审查 + 浏览器证据 + 视觉验收**。必须检查“小标题删除测试”、标题与 KPI/图例的阅读优先级、暗色文字对比与 200% 字体放大；字级不应简单全部放大或统一缩小。先进行去装饰/灰阶信息结构测试；若页面最大面积与主任务不一致，应回到 Gate A 改布局，而不是调渐变颜色。优先在现有测试环境完成构建和组件/流程测试，静态扫描只是提示；检查横向溢出、键盘焦点、屏幕阅读器语义、对比度、浅深主题、长文字、响应式、触摸、错误/加载/空状态、减少动态效果、性能、真实流程回归。**暗色导航需用真实截图检查重复强调色、左侧竖条是否有独立语义、最近打开与主导航是否混淆；本规则不机械禁止层级线。**把“未实际运行”如实标明。

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

必须报告：**产品类型 / 现有框架 / 主业务 UI 库与创意层的选型及理由 / 许可证与依赖核查 / Tokens / 组件复用表 / 页面改动 / 动效及 reduced-motion 降级 / 优秀与反例自检 / 实际测试和未测试项**。先完成工作，再汇报；别用漂亮截图代替真实功能。引用版本易变的 API 时按官方文档复核。

> 官网上的功能/API 会迭代。本次官方资料核对日期：2026-11-02；具体依赖版本以项目锁文件和官方当前文档为准。
