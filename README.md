<div align="center">

<p><sub>WEB DESIGN&nbsp; / &nbsp;FRONTEND ENGINEERING&nbsp; / &nbsp;AGENT SKILL</sub></p>

# MauForma

**Design with intent. Build with precision.**

让设计从真实内容出发，让体验在精确的工程中成形。

面向现代 Web 的设计与前端工程 Agent Skill。  
从设计方向、视觉语言和组件系统，到动效选型、代码实现与质量验收。

[快速开始](#快速开始) · [核心能力](#核心能力) · [设计方法](#设计方法) · [参考资料](#参考资料)

<sub>Web-first · Framework-aware · Component-first</sub>

</div>

---

## 为有判断力的设计而构建

**好设计不等于塞进更多信息，也不等于在所有页面使用同一套极简模板。**

食物品牌值得让摄影成为主角；创意作品集可以大胆、不对称；复杂工作台则需要让任务、数据和状态一眼可达。MauForma 不预设唯一正确的审美，而是基于**网站用途、展示内容与访问者目标**，帮助 Agent 提出有依据的视觉方向，并由用户作出最终选择。

它不是 UI 组件库，也不会为了“高级感”默认引入渐变、粒子、3D 或额外动画引擎。

## 核心能力

| | 能力 | 如何发挥作用 |
| :-- | :-- | :-- |
| **01** | **Design Discovery** · 设计探索 | 先了解网站做什么、展示什么；当用户不确定风格时，提出 2–3 套具体、可比较的设计方案，而不是要求用户盲选专业名词。 |
| **02** | **Art Direction** · 视觉指导 | 基于 8 种独立风格档案、页面任务模式与外部设计参考，确定构图、排版、留白、视觉焦点、信息密度及动效。保留不同设计流派的鲜明个性。 |
| **03** | **Design System & Engineering** · 设计与实现 | 从全局 Tokens、共享组件和页面级规范开始，兼顾 Vue / React 等前端技术栈的组件契约、状态管理及可维护性。 |
| **04** | **Review & Quality** · 质量验证 | 在源码审查之外，结合浏览器截图、交互、响应式、无障碍与性能约束进行验证。区分“实际通过”与“尚未测试”。 |

### 一致的语言，不相同的页面

MauForma 将页面的核心目标区分为四种模式：

| Persuade · 说服 | Operate · 操作 | Read · 阅读 | Experience · 体验 |
| :-- | :-- | :-- | :-- |
| 产品展示、品牌表达、清晰的转化入口 | 搜索、处理任务、可扫描的数据与状态 | 信息层级、合适行宽、连续阅读 | 沉浸视觉、作品本身、探索与互动 |

同一产品可以拥有强调摄影的首页、便于比较的商品目录，以及紧凑高效的管理后台。**统一的是设计语言和组件质量，而非每一页的布局密度。**

## 设计方法

```text
DISCOVER    理解产品用途、展示内容和用户任务
    ↓
DIRECT      推荐设计方向，明确视觉焦点与关键属性
    ↓
SYSTEMIZE   固化项目决策、全局 Tokens 与页面级覆盖
    ↓
BUILD       先构建共享组件，再组合业务页面
    ↓
VERIFY      检查真实交互、视觉实现与响应式表现
```

在此过程中，MauForma 会区分**用户确认、委托 Agent 决定、继承既有规范和仍待确认**的选择。推荐不会被冒充为用户决定，也不会在局部修复时重复进行整套设计访谈。

[设计访谈规则](references/design-discovery-interview.md) · [构图决策](references/composition-first-design.md) · [艺术指导与 Critique](references/art-direction-critique.md) · [项目设计系统继承](references/project-design-hierarchy.md)

## 快速开始

### 1. 安装 Skill

将完整仓库放入 Agent Skills 目录，而不是只复制 `SKILL.md`。

**全局安装（Codex / Agent Skills）：**

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/MauriceLiang/MauForma.git ~/.agents/skills/mauforma
```

也可以安装在单个项目中：

```bash
mkdir -p .agents/skills
git clone https://github.com/MauriceLiang/MauForma.git .agents/skills/mauforma
```

> 以上二选一即可。目录已存在时不要重复克隆；若先前已通过 Git 安装，可进入该目录运行 `git pull` 更新。

### 2. 在 Agent 中调用

```text
$mauforma

我想为一款新产品设计网站，但还不确定视觉风格。
请先分析网站用途、展示内容与主要用户任务，
给出 2–3 套有具体构图差异的视觉方案供我选择。

确定后建立 Design Tokens 和共享组件，
再开发页面并执行响应式、交互与视觉验收。
```

已有设计稿或项目时也可直接要求 MauForma **沿用现有设计语言、审查问题或重构共享组件**，无需重复选择风格。

## 容器结构与控件宽度：不把所有页面装进圆角巨卡

v6.13 增加 **Surface Architecture Gate** 和 **Control Geometry Gate**：先判断连续列表应直接铺在内容区、使用单层有界面板、还是采用独立商品/作品卡片，禁止以默认 Card 替代设计判断；对短按钮/状态/导航标签要求保持原子完整，窄屏时重排行区、让完整控件换行或转为可访问操作菜单，不允许中文逐字竖排、裁切或出屏。规则适用于营销、阅读、专业工作台、作品展示，而不是针对单个任务中心的 CSS 补丁。

[容器结构选型](references/surface-architecture-gate.md) · [控件宽度与折行](references/control-geometry-gate.md) · [五种跨领域设计计划](assets/surface-control-patterns.json) · [三种结构的交互浏览器示例](assets/surface-control-layout-lab.html)

## 通用层级与组件质感：先判断主角，再选字号与形态

v6.12 新增两项跨领域的基础能力：**Perceptual Hierarchy Gate** 将实际决策任务拆分为 P0–P3，在设计 Token 与组件之前判断哪些文字、数据、对象、反馈与操作值得突出；**Component Craft Gate** 对 Button、Table/List、Tabs/Filter、Badge、Search、Card、Dialog、Navigation 明确职责、内容层级、状态与尺寸理由。反对“所有字都缩到 12px”，也反对“所有数字都变巨型 KPI”。真正的设计质量来自角色与组件组合关系，而非随便堆 pill、浅灰边框和阴影。

这是一套面向 **Operate / Persuade / Read / Experience** 的通用方法，而非 RepoVantage 专用视觉模板；保留项目已有设计和用户已确认选择。静态示例覆盖四种页面，检查工具只能检验角色契约，不能替代实际浏览器截图和审美判断。

[信息显著性与排版](references/perceptual-hierarchy-gate.md) · [跨产品组件设计](references/component-craft-gate.md) · [四种模式的数据样例](assets/visual-priority-patterns.json)

## 任务中心：状态可扫描，异常可定位，执行可追踪

v6.11 新增 **Task Center & Run Monitor Gate**：针对后台采集、作业队列、CI/CD、异步执行与任务日志，借鉴 GitHub Actions、GitLab、Trigger.dev、Inngest、Linear 和 Vercel 的成熟交互逻辑。优先用**可点击的状态计数与过滤、紧凑任务列表、真实进度、合法的恢复操作与按需详情**替代长期占宽的统计大卡和重复说明。人工待办和机器任务需分开选型，不能把两者机械地套同一个模板。

新增静态契约检查，明确“尚无可计算总体进度”不等于 `0%`，“需处理”不是单独的生命周期状态，只有服务端能力允许时才显示重试/取消。在独立模拟页面中可测试状态筛选、搜索、详情、模拟重试与响应式滚动；模拟交互**不代表真实后端操作已经成功**。

[任务中心设计与研究](references/task-center-run-monitor-design.md) · [成熟产品参考目录](assets/task-center-reference-cases.json) · [RepoVantage 截图复盘](references/repovantage-task-center-case.md) · [交互示例](assets/task-center-layout-lab.html)

## 比较页面：先让差异有意义，再画多条线

v6.10 新增 **Comparison UX & Chart Integrity Gate**：参考 NN/g、RTINGS、Apple、npmcharts、EcosystemPulse 等真实比较设计，从使用者的比较问题出发，整理**对象条 → 可信差异摘要 → 共同时间窗趋势图 → 同列指标矩阵 → 可展开口径**。同类指标拥有一致单位和采样范围，未采集的数据不伪装成 0 或综合赢家。

还补上以往遗漏的 **图表绘图区/坐标轴/标签级 QA**：外框对齐不能证明图表可读，必须检查内部 Plot Area 与标签重叠。所选仓库、图例、实际序列、对照表列必须一致；浏览器里看不到的 Canvas 标签不能被静态 DOM 脚本冒充已验收。

[比较页设计研究](references/comparison-page-design.md) · [成熟参考与迁移边界](assets/comparison-reference-cases.json) · [图表内部对齐](references/chart-interior-alignment.md) · [交互式比较页示例](assets/comparison-layout-lab.html) · [RepoVantage 截图复盘](references/repovantage-comparison-case.md)

## 对齐不是让所有卡片一样大

v6.9 加入 **Grid & Viewport Integrity Gate**：数据看板的模块优先共享内容边界和行起点。不同宽度、主图跨行与有业务理由的非对称可以保留；不再将两列数据卡片分别堆叠成无规则的上下错位。摄影、创意、叙事仍然允许合理的 Masonry。

同时明确 **超出首屏可以正常滚动，但页面底部不能被不可达的固定高度或悬浮工具栏裁掉**。在目标浏览器中检查笔记本较矮窗口、手机端与滚动终点，保证最后一个 Release、图表轴/说明与操作按钮完整可达。

[网格对齐与底部安全规范](references/grid-alignment-and-viewport-safety.md) · [RepoVantage 发布页复盘](references/repovantage-release-alignment-case.md) · [三种网格与滚动对照](assets/grid-and-viewport-lab.html)

## 先筛选信息，再设计高级留白

v6.8 新增 **Page Content Curation & Density**：先按真实用户任务决定哪些信息展示在当前页、哪些只在首次使用时出现、哪些移往帮助/明细，再选择 `airy / balanced / productive / compact` 页面级密度。**总览页可以舒展而专注；数据分析页则允许筛选、图表、表格与指标更紧凑**。不再把同一组说明卡片机械复制到所有页面。

基于 RepoVantage 的总览截图，重点删除重复的三步教程、功能介绍卡与伪装高级的外层容器；使用组间/组内层级留白，而不是一味增加 padding。

[内容优先级与密度规则](references/page-density-and-content-priority.md) · [留白/容器必要性](references/whitespace-and-surface-composition.md) · [截图案例复盘](references/repovantage-overview-density-case.md) · [三种布局对照 HTML](assets/page-density-lab.html)

## 导航不是固定的左侧栏

MauForma v6.7 引入 **Navigation Architecture Gate**：先识别一级栏目数量、用户切换任务的频率、信息层级与屏幕宽度，再比较顶部、侧边、顶部+侧边、图标轨道、手机底部及混合式导航。特别区分**桌面侧栏→手机底部**与**侧栏+底部上下文操作条**，避免重复一套主导航、丢失手机端入口或遮挡内容。

[阅读导航架构选型指南](references/navigation-architecture.md) · [9 种导航模式档案](assets/navigation-pattern-catalog.json) · [桌面/手机交互预览](assets/navigation-layout-lab.html)。导航样式与主题颜色分别记录用户决策，不用设计推荐代替用户选择。

## 侧边栏配色：Agent 提建议，用户做决定

针对深蓝侧栏与主区域搭配割裂的问题，MauForma 增加 **Color Choice Gate**：先分析当前品牌和整页配色，再参考 [Linear / Carbon / GitHub Primer / shadcn/ui / Atlassian](references/sidebar-color-reference-cases.md) 的设计方法，筛选 2–3 套适合项目的**完整工作台配色**供用户选择。

支持直接指定颜色名或 HEX，用户指定颜色优先；Agent 不得擅自更换。选定后会一起协调 Sidebar、Topbar、Main、Card 与 Chart，检查文本对比、状态色和暗/亮模式。[查看选色对话规范](references/sidebar-color-discovery.md) · [整页配色预览](assets/sidebar-color-preview.html)。

## 文案克制，排版有层级

新增 [文字必要性检查](references/semantic-copy-hygiene.md) 与 [Typography 角色化设计](references/typography-hierarchy.md)：不再自动添加 `ANALYSIS STUDIO`、`01 / 总览`、抽象标语与不面向用户的工程说明；让页面标题、KPI、图表刻度和数据来源各有适合的字级，保留真正有价值的品牌和导航信息。可查看 [正反对照示例](assets/typography-reading-lab.html)。

## 先决定构图，再讨论配色

从 RepoVantage 等真实页面的失败案例出发，MauForma v6.4 增加 **Composition First** 工作流：先检查真实内容与主要任务，绘制无装饰信息线框，比较 2–3 套**主视觉与区域排序真的不同**的构图，再推导有理由的颜色系统。对于“图表空白却有巨大渐变 Hero”的问题，优先修改页面结构，不再只调整颜色。

[构图优先设计规则](references/composition-first-design.md) · [配色艺术指导](references/palette-art-direction.md) · [截图批判与返工](references/visual-critique-loop.md) · [三种布局的概念对照](assets/composition-layout-lab.html)

## 高频工作台组件的视觉细节

针对实际生成页面中常见的**侧栏配色割裂、重复高亮竖条、主导航与最近对象同级**等问题，增加导航专属颜色角色、状态语义和可访问选中态规范，并扩展到 Topbar、Card、Table、Tabs、Search 与 Split Pane。可查看 [侧边栏规范](references/sidebar-navigation-design.md)、[工作台组件精修规范](references/workspace-component-refinement.md) 及 [可交互正反例](assets/sidebar-refinement-gallery.html)。

该规范是高频工作台的默认设计建议，而不是对创意网站的审美禁令。具有信息含义的树形层级线和时间轴仍可使用。

## 设计知识与视觉技术

| **8** 种原创风格档案 | **84** 个外部品牌设计参考入口 | **114** 种 Anime.js 动效配方 |
| :--: | :--: | :--: |
| **12** 项动画与可视化技术 | **9** 组场景化技术组合 | **6** 套主题预设 |

- **风格与案例**：独立保留编辑式、实验性、高级产品展示、活泼趣味、沉浸叙事、克制极简、高效功能型与阅读优先等视觉方向；[查看风格资料库](references/design-style-catalog.md)。外部案例来自 [VoltAgent awesome-design-md](references/external-design-case-library.md) 的来源索引，按需读取，**不是品牌官方设计系统**。
- **动效与可视化**：从 CSS / SVG、Anime.js、GSAP 到 PixiJS、Three.js、ECharts、Matter.js 等，按明确的视觉需求选择，而不是默认安装全部工具；[查看 12 项技术选型指南](references/visual-tech-selection-12.md)。
- **跨框架工程**：优先支持 [Vue / Nuxt](references/framework-vue-nuxt.md) 和 [React / Next.js](references/framework-react-next.md)，同时提供 [其他 Web 框架](references/framework-support-matrix.md) 的适配指引。原生 iOS / Android UI 不在本 Skill 的直接实现范围内。

<details>
<summary><strong>可运行的选型与检查工具</strong></summary>

在 MauForma 仓库根目录执行：

```bash
# 按内容与访问者目标寻找风格
python3 scripts/search_design_knowledge.py --query "甜品 摄影 到店" --mode Persuade

# 查找适合的品牌设计参考
python3 scripts/search_design_cases.py --query "咖啡 门店" --style premium-showcase

# 按目标视觉效果选择实现技术
python3 scripts/search_visual_tech.py --goal "数据 图表 仪表盘"

# 预览项目级设计系统的文件规划（默认不覆盖已有文件）
python3 scripts/init_design_system.py --project-root . --name "My Website" --style premium-showcase --page home --mode Persuade

# 静态代码风险审查：将 ./src 替换为实际项目的源码路径
python3 scripts/audit_frontend.py ./src --format json

# 校验 Skill 数据及回归测试
python3 scripts/validate_intelligence.py
python3 scripts/audit_readability.py --validate-catalog
python3 scripts/validate_composition_brief.py examples/composition/repo-analysis.json --repository
python3 scripts/validate_ui_patterns.py
python3 scripts/validate_sidebar_color_decision.py --repository
python3 scripts/validate_navigation_architecture.py --repository
python3 scripts/validate_page_content_plan.py examples/page-content-plan-repovantage.json --repository
python3 scripts/validate_layout_integrity.py --repository
python3 scripts/validate_comparison_contract.py examples/comparison-contract-repovantage.json --repository
python3 scripts/validate_task_center.py examples/task-center-repovantage.json --repository
python3 -m unittest discover -s tests -v
```

浏览器截图工具 `scripts/browser_qa.mjs` 需要目标项目已有 Playwright 和可访问的开发服务器；静态扫描或截图**不能单独证明**业务流程与视觉质量已经验收。

</details>

## 参考资料

| 设计与体验 | 前端工程与质量 |
| :-- | :-- |
| [设计发现与用户选择](references/design-discovery-interview.md) | [组件优先开发](references/component-first.md) |
| [风格档案与艺术指导](references/design-style-catalog.md) | [React 组件工程](references/react-component-engineering.md) |
| [外部品牌设计案例](references/external-design-case-library.md) | [Vue 组件工程](references/vue-component-engineering.md) |
| [Design DNA 参考网站分析](references/design-dna-protocol.md) | [动画生命周期与资源清理](references/animation-integration-lifecycle.md) |
| [设计系统 MASTER 与页面覆盖](references/project-design-hierarchy.md) | [侧栏及工作台组件规范](references/workspace-component-refinement.md) |
| [侧栏配色与选中态](references/sidebar-navigation-design.md) | [前端审查与浏览器 QA](references/browser-qa-protocol.md) |
| [12 项动画与可视化技术选型](references/visual-tech-selection-12.md) | [全局规则与阅读路由](SKILL.md) |

**交互演示资源**：仓库内的 [主题预览](assets/preview.html)、[创意效果展示](assets/creative-effects-gallery.html) 与 [动效目录](assets/motion-gallery.html) 为 HTML 文件，下载或克隆后可在浏览器中打开。

## 项目原则

**Design is a decision. Engineering makes it dependable.**

视觉风格由内容与用户目标决定；组件系统负责统一质量；动效必须有实际价值；所有声称的测试结果都应有可核对的执行证据。

MauForma 借鉴其他优秀设计与工程 Skills 的方法，但不会将其审美主张平均化为一种模板。外部文档与品牌案例保留来源归属；引用第三方源码、字体、图片或商业组件时，应单独核对相应授权。

<details>
<summary>兼容性与版本记录</summary>

MauForma 延续原 Soft Precision UI 的设计资源。为避免破坏已有项目，内部 CSS 命名空间仍保留 `.spui` 与 `--spui-*`；公开的 Skill 名称与调用命令统一为 `mauforma` / `$mauforma`。

版本变化及新增能力见 [CHANGELOG.md](CHANGELOG.md)。现有 GitHub Actions 工作流见 [Skill Quality](.github/workflows/skill-quality.yml)。

</details>

---

<div align="center">

**MauForma**

<sub>Thoughtful design. Consistent systems. Reliable interfaces.</sub>

[GitHub](https://github.com/MauriceLiang/MauForma) · [Skill](SKILL.md) · [Changelog](CHANGELOG.md)

</div>
