---
name: mauforma
description: MauForma — Web-first, framework-aware, component-first frontend design and implementation Skill for Vue/Nuxt, React/Next, Svelte/SvelteKit, Angular, Solid, Astro and vanilla HTML/CSS/JS. Establish design tokens and reusable components before pages; create coherent visual systems, accessible responsive UI, purposeful motion and detailed good/bad examples. Priority depth: admin/SaaS interfaces, applicable to all websites and web apps. Includes Anime.js v4 catalog, React Bits / Vue Bits / Inspira UI creative components, Ant Design / Ant Design Vue and other enterprise libraries, Motion/GSAP/CSS engine choices, and enforceable agent prompts.
---

# MauForma · Web-first 前端视觉与工程 Skill v5.2

**品牌**：MauForma（Maurice + Forma）。原 Soft Precision UI v5.0 的完整能力保留，本次为品牌与 Skill 调用名更新。

**定位**：网页设计与前端实现（Web-first）。支持所有网页类型，**当前专项深化后台管理/SaaS**，但绝不把其他网站套成后台模板。框架：Vue 3 / Nuxt、React / Next.js、Svelte / SvelteKit、Angular、Solid、Astro、HTML/CSS/JS；若是 Electron/Tauri 的 **Web 前端层**也适用。**不以 SwiftUI、AppKit、原生 Android 等非 Web UI 为直接适用对象**。

**主原则**：审美统一 ≠ 每页一个模板。统一设计语言 + 共用组件 + 符合具体业务的信息架构 + 恰当动效 + 可访问、可测试的功能。允许自主创作主题色，不固定用户参考网站的蓝紫粉渐变。

## 必经设计确认阶段（新增 v5.2）

在新建网站或大规模重设计前，**先检查已有项目、内容和组件，再与用户确认视觉风格、信息密度与主视觉焦点**。对于颜色、动效强度和素材策略，只在确实影响实施且尚不明确时补问。详细依据见 [设计前访谈规范](references/design-discovery-interview.md)，项目决策采用 [设计简报 JSON Schema](assets/design-brief.schema.json)。

明确区分用户确认、AI 受托决定、沿用现有规范和尚未确定的选项。避免对已有设计稿或局部修改重复提问。用户可选混合信息密度，**不同页面应按内容、视觉冲击力和操作效率采用不同展示方式**。

实施流程：项目分析 → 用户设计选择/继承 → 视觉构图与信息层级 → Design Tokens → 共享组件 → 页面实现 → 动效与浏览器验收。后台的高效操作和展示页的大幅主视觉都可以在同一设计体系下共存。

## 阅读路由：只读取与任务有关的参考文件

| 任务 | 必读文件 |
| --- | --- |
| 所有前端实现 | `references/frontend-architecture-and-gates.md`、`references/design-system.md`、`references/component-first.md` |
| 判断网站类型与密度 | `references/web-scope-and-app-types.md`、`references/good-vs-bad.md` |
| Vue / Nuxt | `references/framework-vue-nuxt.md`、`examples/vue3-web-components.md` |
| React / Next | `references/framework-react-next.md`、`examples/react-web-components.md` |
| Svelte、Angular、Solid、Astro、原生 Web | `references/framework-other-web.md` |
| 技术栈选型与截图里的 11 组推荐 | `references/stack-guide-11-items.md`、`references/framework-support-matrix.md` |
| 提示词与 Agent 协作 | `references/ai-frontend-prompt-policy.md`、`examples/prompt-library-web.md` |
| 创意官网、产品宣传与互动视觉 | `references/creative-component-libraries.md`、`examples/creative-library-recipes-react-vue.md`、`assets/creative-effects-gallery.html` |
| Ant Design、Ant Design Vue、Element Plus、MUI 等后台组件库 | `references/enterprise-ui-library-guide.md`、`references/framework-support-matrix.md` |
| 动画选择 | `references/animation-engine-selection.md`、`references/animation-integration-lifecycle.md` |
| Anime.js 动效目录 | `references/animejs-official-capabilities.md`、`references/animejs-motion-recipes.md`、`references/animejs-easing-complete.md` |
| 反例、审查与交付 | `references/quality-antipatterns-by-page-type.md`、`references/page-header-antipatterns.md`、`references/ui-review-rubric.md`、`references/visual-qa.md` |

## 不可跳过的前端执行顺序

1. **Gate 0：侦察**。读取 `package.json`、锁文件、现有路由、框架、UI 库、样式系统、构建命令、页面结构、测试约定，记录技术选择依据；已有项目不能随意换框架。
2. **Gate A：视觉方案**。针对业务类型给出信息架构、视觉密度、色彩角色、Typography、Spacing、Radius、Elevation、Motion Tokens（浅/深色）。在整个项目只有一个真实 Tokens 来源，非每页硬编码颜色。
3. **Gate B：组件优先**。列出复用/改造/新增组件清单，先建立或修正 `UiButton/Field/Dialog/PageHeader/Navigation/Table/Feedback` 等共享组件及各状态，制作组件展示页。**Gate B 未通过，不允许批量铺业务页**。但修复单个故障时不必强制重构全站。
4. **Gate C：业务与动效**。按真实业务组合组件，先保证真实状态、API、权限与数据流程。先确定场景：
   - **官网/品牌/产品介绍/作品集**：允许按需选择 React Bits、Vue Bits、Inspira UI、Magic UI、Aceternity UI 的**单个**创意组件，不能取代原有功能组件；先检查原生框架、许可证、WebGL/GSAP 依赖、动效减弱和移动端回退。
   - **管理后台/工作台/企业表单**：优先复用 Ant Design / Ant Design Vue / Element Plus / MUI / Naive UI / Arco / PrimeVue 等**一套**主组件库，按共享 Ui 契约集中主题，默认轻量 CSS/框架微交互，不将 WebGL 背景批量引入业务工作区。
   - 所有动效优先 CSS/框架原生能力；确有需要才选择 Anime.js/Motion/GSAP。避免同一效果叠用多个引擎。
5. **Gate D：浏览器验收**。检查横向溢出、键盘焦点、屏幕阅读器语义、对比度、浅深主题、长文字、响应式、触摸、错误/加载/空状态、减少动态效果、性能、真实流程回归。把“未实际运行”如实标明。

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

- `assets/creative-effects-gallery.html` — 12 组原创 CSS/JS 交互动效概念预览（**不是** React Bits/Vue Bits 官方源码或精确演示），帮助挑选恰当的创意增强层。
- `references/creative-component-libraries.md` — React Bits/Vue Bits/Inspira UI/Magic UI/Aceternity UI 名称、效果、场景、技术边界和来源。
- `references/enterprise-ui-library-guide.md` — Ant Design、Ant Design Vue 等企业业务组件全景、主题接入、组件职责与选型。
- `assets/motion-gallery.html` — 114 种动效配方索引及 45 种缓动的交互原理演示（不等于全部官方内置特效）。
- `assets/page-header-antipattern-gallery.html` — 后台标题常见问题对照；`assets/preview.html` — 主题与密度样例。
- `assets/framework-decision.json` — 机器可读的框架/工具关系；`scripts/validate_web_skill.py` — 文档引用与覆盖度检查。
- `assets/reference-source/` — 用户提供的原站，仅供视觉设计原理分析；不复制原来的假数据、色盘或过时用法。

## 交付输出要求

必须报告：**产品类型 / 现有框架 / 主业务 UI 库与创意层的选型及理由 / 许可证与依赖核查 / Tokens / 组件复用表 / 页面改动 / 动效及 reduced-motion 降级 / 优秀与反例自检 / 实际测试和未测试项**。先完成工作，再汇报；别用漂亮截图代替真实功能。引用版本易变的 API 时按官方文档复核。

> 官网上的功能/API 会迭代。本次官方资料核对日期：2026-11-02；具体依赖版本以项目锁文件和官方当前文档为准。
