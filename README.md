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

\`\`\`text
DISCOVER    理解产品用途、展示内容和用户任务
    ↓
DIRECT      推荐设计方向，明确视觉焦点与关键属性
    ↓
SYSTEMIZE   固化项目决策、全局 Tokens 与页面级覆盖
    ↓
BUILD       先构建共享组件，再组合业务页面
    ↓
VERIFY      检查真实交互、视觉实现与响应式表现
\`\`\`

在此过程中，MauForma 会区分**用户确认、委托 Agent 决定、继承既有规范和仍待确认**的选择。推荐不会被冒充为用户决定，也不会在局部修复时重复进行整套设计访谈。

[设计访谈规则](references/design-discovery-interview.md) · [艺术指导与 Critique](references/art-direction-critique.md) · [项目设计系统继承](references/project-design-hierarchy.md)

## 快速开始

### 1. 安装 Skill

将完整仓库放入 Agent Skills 目录，而不是只复制 \`SKILL.md\`。

**全局安装（Codex / Agent Skills）：**

\`\`\`bash
mkdir -p ~/.agents/skills
git clone https://github.com/MauriceLiang/MauForma.git ~/.agents/skills/mauforma
\`\`\`

也可以安装在单个项目中：

\`\`\`bash
mkdir -p .agents/skills
git clone https://github.com/MauriceLiang/MauForma.git .agents/skills/mauforma
\`\`\`

> 以上二选一即可。目录已存在时不要重复克隆；若先前已通过 Git 安装，可进入该目录运行 \`git pull\` 更新。

### 2. 在 Agent 中调用

\`\`\`text
$mauforma

我想为一款新产品设计网站，但还不确定视觉风格。
请先分析网站用途、展示内容与主要用户任务，
给出 2–3 套有具体构图差异的视觉方案供我选择。

确定后建立 Design Tokens 和共享组件，
再开发页面并执行响应式、交互与视觉验收。
\`\`\`

已有设计稿或项目时也可直接要求 MauForma **沿用现有设计语言、审查问题或重构共享组件**，无需重复选择风格。

## 设计知识与视觉技术

<div align="center">

| **8** 种原创风格档案 | **84** 个外部品牌设计参考入口 | **114** 种 Anime.js 动效配方 |
| :--: | :--: | :--: |
| **12** 项动画与可视化技术 | **9** 组场景化技术组合 | **6** 套主题预设 |

</div>

- **风格与案例**：独立保留编辑式、实验性、高级产品展示、活泼趣味、沉浸叙事、克制极简、高效功能型与阅读优先等视觉方向；[查看风格资料库](references/design-style-catalog.md)。外部案例来自 [VoltAgent awesome-design-md](references/external-design-case-library.md) 的来源索引，按需读取，**不是品牌官方设计系统**。
- **动效与可视化**：从 CSS / SVG、Anime.js、GSAP 到 PixiJS、Three.js、ECharts、Matter.js 等，按明确的视觉需求选择，而不是默认安装全部工具；[查看 12 项技术选型指南](references/visual-tech-selection-12.md)。
- **跨框架工程**：优先支持 [Vue / Nuxt](references/framework-vue-nuxt.md) 和 [React / Next.js](references/framework-react-next.md)，同时提供 [其他 Web 框架](references/framework-support-matrix.md) 的适配指引。原生 iOS / Android UI 不在本 Skill 的直接实现范围内。

<details>
<summary><strong>可运行的选型与检查工具</strong></summary>

在 MauForma 仓库根目录执行：

\`\`\`bash
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
python3 -m unittest discover -s tests -v
\`\`\`

浏览器截图工具 \`scripts/browser_qa.mjs\` 需要目标项目已有 Playwright 和可访问的开发服务器；静态扫描或截图**不能单独证明**业务流程与视觉质量已经验收。

</details>

## 参考资料

| 设计与体验 | 前端工程与质量 |
| :-- | :-- |
| [设计发现与用户选择](references/design-discovery-interview.md) | [组件优先开发](references/component-first.md) |
| [风格档案与艺术指导](references/design-style-catalog.md) | [React 组件工程](references/react-component-engineering.md) |
| [外部品牌设计案例](references/external-design-case-library.md) | [Vue 组件工程](references/vue-component-engineering.md) |
| [Design DNA 参考网站分析](references/design-dna-protocol.md) | [动画生命周期与资源清理](references/animation-integration-lifecycle.md) |
| [设计系统 MASTER 与页面覆盖](references/project-design-hierarchy.md) | [前端审查与浏览器 QA](references/browser-qa-protocol.md) |
| [12 项动画与可视化技术选型](references/visual-tech-selection-12.md) | [全局规则与阅读路由](SKILL.md) |

**交互演示资源**：仓库内的 [主题预览](assets/preview.html)、[创意效果展示](assets/creative-effects-gallery.html) 与 [动效目录](assets/motion-gallery.html) 为 HTML 文件，下载或克隆后可在浏览器中打开。

## 项目原则

**Design is a decision. Engineering makes it dependable.**

视觉风格由内容与用户目标决定；组件系统负责统一质量；动效必须有实际价值；所有声称的测试结果都应有可核对的执行证据。

MauForma 借鉴其他优秀设计与工程 Skills 的方法，但不会将其审美主张平均化为一种模板。外部文档与品牌案例保留来源归属；引用第三方源码、字体、图片或商业组件时，应单独核对相应授权。

<details>
<summary>兼容性与版本记录</summary>

MauForma 延续原 Soft Precision UI 的设计资源。为避免破坏已有项目，内部 CSS 命名空间仍保留 \`.spui\` 与 \`--spui-*\`；公开的 Skill 名称与调用命令统一为 \`mauforma\` / \`$mauforma\`。

版本变化及新增能力见 [CHANGELOG.md](CHANGELOG.md)。现有 GitHub Actions 工作流见 [Skill Quality](.github/workflows/skill-quality.yml)。

</details>

---

<div align="center">

**MauForma**

<sub>Thoughtful design. Consistent systems. Reliable interfaces.</sub>

[GitHub](https://github.com/MauriceLiang/MauForma) · [Skill](SKILL.md) · [Changelog](CHANGELOG.md)

</div>
