# 主流前端框架支持矩阵

**规则**：列出候选方案，不代表必须安装。先读取当前项目的 `package.json` 与锁文件，现有方案可行就继续用。下表中的适配支持不意味着同一套源代码或 props 可以在不同框架间无改动通用。

| 框架 | 首要组件路线 | 图标 | 动画 | 客户端状态 | 服务端状态 | 图表/复杂数据 |
|---|---|---|---|---|---|---|
| Vue 3 / Nuxt | Reka UI、shadcn-vue、Element Plus、Naive UI（按已有选择） | `@lucide/vue` / 现有 `lucide-vue-next` | Vue `<Transition>`、Motion for Vue (`motion-v`)、Anime.js、GSAP | Pinia / composables | `@tanstack/vue-query` 或 Nuxt 数据工具 | Apache ECharts + Vue 适配 / `@tanstack/vue-table` |
| React / Next.js | shadcn/ui + Base UI 或 Radix；Mantine、MUI、AntD 也可 | `lucide-react` | Motion for React (`motion/react`)、Anime.js、GSAP | Zustand / Context | `@tanstack/react-query` 或框架数据 API | Recharts / ECharts / `@tanstack/react-table` |
| Svelte / SvelteKit | Bits UI、shadcn-svelte | `@lucide/svelte` | Svelte transitions、Anime.js、GSAP、Motion JS | Svelte stores/runes | SvelteKit load / Query 适配 | ECharts / Table 适配（确认版本） |
| Angular | Angular CDK / Material、PrimeNG | `@lucide/angular` | Angular 动画方案 / CSS / Anime.js / GSAP | Signals / RxJS | HttpClient / TanStack Query 按需 | ECharts / AG Grid |
| Solid | Kobalte / Ark UI | `lucide-solid` / `@lucide/solid`（依版本） | CSS、Motion JS、Anime.js | Signals / Stores | TanStack Query Solid | ECharts / TanStack Table Solid |
| Astro | Astro 原生组件 + React/Vue/Svelte/Solid Islands | SVG / 各 Island 框架 Lucide | CSS、Web Animations、Anime.js | 尽量不引入全局状态 | Astro 数据获取/各 Island | ECharts 按需客户端水合 |
| HTML/CSS/JS | 原生语义元素、Web Components，适量 headless 实现 | `lucide` / SVG | CSS、Web Animations、Anime.js | 原生模块状态 | Fetch + 局部缓存 | ECharts / Canvas/SVG |

## 决策的判定条件

1. **旧项目：先延续已安装框架和组件库**。没有明确需求不要 Vue 转 React 或 React 转 Vue。
2. **无障碍复杂控件**（Select、Dialog、Combobox、Menu）优先选择相应框架下经过验证的 headless primitives 或成熟 UI 套件。
3. **设计高自由度**：选可复制可维护的组件层（shadcn/ui、shadcn-vue）或无样式原语 + 自有样式。
4. **大型数据密集型**：可能选择成熟管理型组件套件、虚拟化表格与成熟图表，不迷信特效库。
5. **SSR/SEO**：检查 Next/Nuxt/SvelteKit/Astro 的服务端边界与 hydration，不要在模块顶层直接访问 `window`/`document`。
6. **轻量营销站**：可能只需 HTML/CSS、Astro + 少量 Islands，不强装 React/Vue 大型状态库。
7. **共享组件契约、颜色 token、交互原则可以跨框架统一**；具体源码、生命周期处理、props/emits 需适配本框架。

> 2026 年 Lucide 官网提供新版 `@lucide/vue`，一些旧项目还使用 `lucide-vue-next`。迁移需检查具体版本，不应同时安装并在组件中混用。dnd-kit 的新版有 Vue 等适配层，不能仅靠旧版文章断言“只能 React”。

官方来源：
- https://lucide.dev/packages
- https://lucide.dev/guide/version-1
- https://github.com/clauderic/dnd-kit
- https://motion.dev/docs
- https://tanstack.com/query/latest/docs/framework/vue/installation
- https://shadcn-vue.com/docs/introduction
- https://ui.shadcn.com/docs


## v5 创意组件层与企业组件层补充

| 场景 | React / Next | Vue / Nuxt | 选择原则 |
| --- | --- | --- | --- |
| 创意官网动态标题、背景、3D 展示 | React Bits；Magic UI；Aceternity UI | Vue Bits（React Bits 官方 Vue 移植）；Inspira UI | 只挑选单个适配组件，核对依赖/许可/SSR，不当作基础 UI 库 |
| 企业后台复杂表格与表单 | Ant Design、MUI、Mantine、PrimeReact；已有 shadcn/ui 可继续用 | Ant Design Vue、Element Plus、Naive UI、Arco Vue、PrimeVue；已有 Reka/shadcn-vue 可继续用 | **选择一套主库**，复杂专业控件额外审查 |
| 共用基础视觉 | CSS/Tailwind Design Tokens + Ui 封装 | CSS/Tailwind Design Tokens + Ui 封装 | 风格复用，源代码不跨框架硬移植 |

完整说明见 `references/creative-component-libraries.md`、`references/enterprise-ui-library-guide.md`、`examples/creative-library-recipes-react-vue.md`。
