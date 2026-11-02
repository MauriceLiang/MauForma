# 截图推荐技术栈逐项解释：11 个类别 / 12 个独立名称

> 截图中的 11 行类别为：UI 组件（两项）、视觉组件（两项）、图标、动画、样式、布局、拖拽、状态管理、数据请求、图表。本指南把 UI 与视觉类展开后，共详细介绍 **12 个独立产品/技术**。这不是本 Skill 的强制安装清单。2026-11-02 查验官方资料，版本更新请以项目锁文件/官网为准。

## 技术栈层级怎么理解？

- **框架层**：Vue/React/Svelte/Angular 等负责组件、状态和视图生命周期。
- **基础交互层**：Reka/Radix/Base UI/Bits UI 等提供键盘、焦点、ARIA 行为。
- **组件外观层**：shadcn/ui、shadcn-vue、现有 UI 套件将设计 tokens 与原语组合。
- **美术与图标层**：Magic UI/Aceternity 为展示性创意，Lucide 为功能图标。
- **动效层**：Motion/Anime.js/GSAP/CSS，按用途择一或按责任分工（禁止控制同一动画目标互相覆盖）。
- **布局/拖拽层**：可调分栏、排序和拖放是交互系统，不等价于动画库。
- **状态/数据层**：Zustand 等管理共享客户端状态，TanStack Query 等管理远端服务器状态。
- **数据表达层**：Recharts/ECharts 把真实数据映射为可解释图表。

## 01 · UI 组件 — shadcn/ui

**框架范围**：React / Next.js（与 Vue 移植项目不同）

**里面有什么**：可复制并由项目自行维护的组件源码，主题变量、CLI、Button/Dialog/Table/Select/Sidebar 等复合组件；通常建立在 Base UI、Radix 或 React Aria 等可访问基础上。

**主要解决什么问题**：创建统一视觉组件体系，快速获得正确交互/状态并保留代码控制权。

**正确引入与使用**：先查 components.json / 现有 primitives；按项目组件安装；只改共享层 variant、CSS token 和状态；以 gallery 验收。

**不良用法 / 避雷**：不要把 shadcn/ui 当作需长期依赖的整套黑盒组件 npm 包；不要把 React TSX 复制到 Vue；已有 Radix 无需因新默认 Base UI 而迁移。

**Vue / React / 其他框架适配**：Vue：shadcn-vue（常结合 Reka UI）；Svelte：shadcn-svelte；其他框架需采用对应 port。

**官方资料**：https://ui.shadcn.com/docs

## 02 · UI 原语 — Radix UI / Base UI

**框架范围**：React（各自独立原语体系）

**里面有什么**：Dialog、Popover、Select、Dropdown、Tabs、Tooltip、Focus 等行为/可访问性原语；负责焦点管理、ARIA、键盘交互而非产品视觉。

**主要解决什么问题**：在保持自定义视觉的同时避免重复实现高风险复杂交互。

**正确引入与使用**：使用现有原语封装 UiDialog/UiSelect/UiPopover，统一外观 Token，使用官方 composition API。

**不良用法 / 避雷**：Base UI 的 render 不是 Radix 的 asChild；data-*、定位、事件等 API 存在差异；不能盲用旧教程。

**Vue / React / 其他框架适配**：Vue 使用 Reka UI；Svelte Bits UI；Angular CDK；Solid Kobalte/Ark UI。

**官方资料**：https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default

## 03 · 视觉组件 — Magic UI

**框架范围**：以 React / Next.js + Tailwind / shadcn 生态为主

**里面有什么**：可安装的动态装饰、背景、文字效果、展示性组件/区块等，通常使用 shadcn 风格 registry 机制。

**主要解决什么问题**：为登陆页、品牌官网、作品集、定向产品介绍增加表现力。

**正确引入与使用**：仅挑选能服务叙事/功能的 1–2 个视觉区块，提取颜色/间距/字体到设计系统，控制滚动与电量。

**不良用法 / 避雷**：不能让特效替代基础表单、弹窗、真实内容和可访问交互；避免营销组件蔓延到后台表格页。

**Vue / React / 其他框架适配**：Vue：参考视觉原理，用 Vue 原生 / Motion Vue / Anime.js 实现；不能直接 import React 组件。

**官方资料**：https://magicui.design/docs/installation

## 04 · 视觉组件 — Aceternity UI

**框架范围**：React / Next.js 生态为主

**里面有什么**：复制式视觉组件与高冲击展示效果，如 3D、卡片交互、文字或图像变化、动效背景。

**主要解决什么问题**：少量用于作品展示、品牌首屏、活动页的特定视觉焦点。

**正确引入与使用**：先检查组件代码、依赖和许可；放入独立展示层；设计系统保持一致；提供减少动画回退。

**不良用法 / 避雷**：不可成套堆砌所有特效；不能把可视化效果误当成可点击、可访问、真实业务组件。

**Vue / React / 其他框架适配**：Vue/Svelte/Angular 需用本框架的组件和动画组合重实现，不直接搬运 TSX。

**官方资料**：https://ui.aceternity.com/components

## 05 · 图标 — Lucide

**框架范围**：React、Vue、Svelte、Solid、Angular、Vanilla（各有包）

**里面有什么**：大量一致的 SVG 线性图标，支持尺寸、颜色、线宽、无障碍标签和按需引入。

**主要解决什么问题**：确保各页面图标风格统一，不需要为普通动作引入多套图标库。

**正确引入与使用**：统一 16/18/20px 级别和 stroke-width，装饰图标 aria-hidden，独立图标按钮须带 aria-label。

**不良用法 / 避雷**：禁止 React 里混进 Vue 图标包，避免 emoji/3D/线性图标混排；包名随版本变化应核查。

**Vue / React / 其他框架适配**：React `lucide-react`；Vue 新版 `@lucide/vue`，旧项目常为 `lucide-vue-next`；其余见官方 Packages。

**官方资料**：https://lucide.dev/packages

## 06 · 动画 — Motion（原 Framer Motion）

**框架范围**：React、Vue、原生 JavaScript 各有入口

**里面有什么**：声明式 `<motion />`、存在/退出动画、布局过渡、spring、手势/拖动、滚动动画；JS 版支持 DOM/SVG 等。

**主要解决什么问题**：按钮反馈、状态驱动过渡、列表布局变化、手势等现代交互。

**正确引入与使用**：React `motion/react`；Vue `motion-v`；简单 CSS 能满足就不用此库，组件卸载要管理动画生命周期。

**不良用法 / 避雷**：不要在已有页面里与 Anime.js 同时控制同一元素的 transform；不要把旧版 `framer-motion` 导入视为最新标准；不要随意加弹簧。

**Vue / React / 其他框架适配**：React `motion`，Vue `motion-v`，其它框架可以用 `motion` JavaScript API 或原生 CSS/WAAPI。

**官方资料**：https://motion.dev/docs

## 07 · 样式 — Tailwind CSS

**框架范围**：Vue、React、Svelte、Angular、Astro 和 Vanilla 等

**里面有什么**：Utility-first CSS、响应式变体、状态变体、主题/设计 token 管理，配合构建工具生成 CSS。

**主要解决什么问题**：快速可靠地表达统一间距、字体与响应式，而不需要每页复制一长段 CSS。

**正确引入与使用**：先定义语义 token 与字体、圆角，再编写共享组件变体；Vite/Next 等安装方式不同，查对应官方版本文档。

**不良用法 / 避雷**：禁止用几十个裸十六进制颜色反复堆 class；禁止所有元素自定义任意 radius；Tailwind 不负责对话框焦点。

**Vue / React / 其他框架适配**：也可选 CSS Modules、原生 CSS、UnoCSS；已有方案能满足时不强制迁移。

**官方资料**：https://tailwindcss.com/docs/installation

## 08 · 可调布局 — react-resizable-panels

**框架范围**：React 专用组件库

**里面有什么**：Group/Panel/Separator 以及伸缩、折叠、尺寸约束、默认布局、键盘调整、持久化等。

**主要解决什么问题**：编辑器、IDE 风格工作台、复杂数据系统的可调整分屏。

**正确引入与使用**：保证拖动手柄可见/可键盘操作、设置最小宽度和 SSR 恢复策略，优先复用统一分屏组件。

**不良用法 / 避雷**：普通单栏/双栏不必引入；不要无 min/max 约束导致内容挤压；不要在 Vue 项目直接安装。

**Vue / React / 其他框架适配**：Vue：Reka UI Splitter；其他框架选本框架兼容的可访问 split-pane 或 CSS Grid。

**官方资料**：https://github.com/bvaughn/react-resizable-panels

## 09 · 拖拽 — dnd-kit

**框架范围**：新版支持 DOM / React / Vue / Svelte / Solid 适配（具体版本确认）

**里面有什么**：拖放源/目标、传感器、排序、碰撞检测、覆盖层和拖拽状态；框架适配层封装。

**主要解决什么问题**：看板任务卡排序、列表重新排序、组件布局拖动与放置。

**正确引入与使用**：先检查当前 dnd-kit 是旧包还是新版 adapters；提供手柄、拖拽反馈、触摸与键盘替代、操作撤销。

**不良用法 / 避雷**：动画引擎不等于可访问拖拽系统；不能只依赖 mousemove；别混用 @dnd-kit/core 与新版 @dnd-kit/react API。

**Vue / React / 其他框架适配**：新版含 `@dnd-kit/react`、`@dnd-kit/vue` 等；旧项目可能使用 `@dnd-kit/core` / `@dnd-kit/sortable`，不可混抄。

**官方资料**：https://github.com/clauderic/dnd-kit

## 10 · 客户端状态 — Zustand

**框架范围**：React 主要生态；也有 vanilla store

**里面有什么**：create store / selectors / 订阅 / 局部状态组织、中间件等，控制跨组件共享客户端状态。

**主要解决什么问题**：全局弹窗、用户偏好、侧栏折叠、编辑草稿与过滤选项。

**正确引入与使用**：先将局部状态留在组件；跨树共享且已有 Zustand 时复用，避免过度全局化；业务数据需单独考虑缓存失效。

**不良用法 / 避雷**：Zustand 不等于远端请求缓存工具；Vue 项目默认不应照搬 React Zustand hooks。

**Vue / React / 其他框架适配**：Vue 优先 Pinia / composables；Angular Signals；Svelte runes/stores；Solid signals。

**官方资料**：https://zustand.docs.pmnd.rs/

## 11 · 服务端状态 — TanStack Query

**框架范围**：React、Vue、Solid、Svelte、Angular 等有各自适配

**里面有什么**：请求缓存、查询键、后台刷新、错误/加载、mutation、失效、分页/无限列表、网络恢复及开发工具。

**主要解决什么问题**：表格远程分页、用户详情、搜索结果、跨页缓存和更新后失效。

**正确引入与使用**：先区分 client state 与 server state；React `@tanstack/react-query`，Vue `@tanstack/vue-query`；mutation 后失效/更新，处理认证与错误。

**不良用法 / 避雷**：不能拿 Query 充当用户权限服务；不要无限重试非幂等请求；不能把 server state 再复制到 Zustand/Pinia 两边维护。

**Vue / React / 其他框架适配**：各框架用对应 adapter；Next/Nuxt 已有内置数据层时比较职责后再引入。

**官方资料**：https://tanstack.com/query/latest

## 12 · 图表 — Recharts

**框架范围**：React 专用图表组件库

**里面有什么**：Line/Area/Bar/Pie/Scatter/Composed/Radar/Treemap 等组件、轴、图例、Tooltip、响应式容器、动画属性。

**主要解决什么问题**：React 管理后台中的常规数据报表、趋势、对比和指标图表。

**正确引入与使用**：映射真实数据、单位、零值与异常值；统一 token 配色、图例和 Tooltip；敏感数据避免误导性截断。

**不良用法 / 避雷**：不能因视觉效果随意滚动数字或篡改原始值；不可直接用 React Recharts 代码在 Vue 渲染。

**Vue / React / 其他框架适配**：Vue/多框架可用 Apache ECharts（vue-echarts 等适配）；也可根据需求采用 Chart.js 或 TanStack Charts（核查版本）。

**官方资料**：https://recharts.github.io/en-US/examples/

## Vue 与 React 的可执行决策示例

**案例 A：已有 Vue 3 + Reka UI 的管理系统**：保持 Vue、Reka；共享 Button/Form/Dialog + Pinia（仅需要时）+ TanStack Vue Query（确有缓存/失效需求）+ Reka Splitter（确需多面板）+ ECharts（图表复杂时）。只为一个按钮的 hover **不引入** Anime.js、GSAP、Motion、Magic UI 四套依赖。

**案例 B：已有 React + shadcn/ui(Radix) 的工作台**：保留 Radix，不因为官网新增默认 Base UI 而重装；组件使用既有 shadcn；布局为多编辑器时考虑 react-resizable-panels；拖拽按当前版本选择 dnd-kit；简单动画 CSS，复杂有意义的状态转场使用 Motion。

**案例 C：营销活动网站**：可以使用 React + 少量 Magic UI/Aceternity 的部分视觉组件；但访问性能、CTA 可见性、移动端体验和 reduced-motion 一票否决。Astro + CSS + 小型 Island 常常更轻。

## 许可证与更新要求

- 必须在安装/复制前核对官方仓库许可证、商业授权、依赖、更新活跃度和组件自身授权；**不要假定所有复制式特效库的每个区块都免费可商用**。
- 对核心库使用现有锁文件版本的文档；不要用搜索结果中的新 API 覆盖旧项目代码。
- 三个月后复核快速变化的库名、安装路径、组件协议、分支版本以及 SSR 兼容性。


## v5 扩展：创意组件不止 Magic UI 与 Aceternity UI

- React Bits 提供 React 原生的文字动画、背景、卡片和微交互，代码可复制进项目；其 Pro 资源与免费部分应分清。
- Vue Bits 是 React Bits 的官方 Vue 移植，基于 Vue 3 + TypeScript + Tailwind，适用于 Vue/Nuxt 创意官网。
- Inspira UI 是独立 Vue/Nuxt 创意组件集合，常使用 shadcn-vue、motion-v 与 Tailwind。
- 对于真正的业务后台，React 的 Ant Design，Vue 的 Ant Design Vue、Element Plus 等完整套件提供 Form/Table/Select/DatePicker/Feedback，不能用创意动画库替代。

请按用途分别阅读 `references/creative-component-libraries.md` 和 `references/enterprise-ui-library-guide.md`。以上不是自动增加五个依赖的命令。
