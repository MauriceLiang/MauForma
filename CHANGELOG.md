# Changelog

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
