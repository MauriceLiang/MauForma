# Vue 3 / Nuxt · 深度支持实施规范

## 1. Vue 适合做什么？

Vue 3 是渐进式前端 UI 框架。以单文件组件 `.vue` 组织模板、状态和局部样式；Composition API + `<script setup lang="ts">` 适合复用逻辑；Vue Router 处理 SPA 页面导航；Nuxt 提供基于 Vue 的 Web 应用框架能力，例如文件路由、SSR/SSG、服务端路由和数据加载。

**已有项目优先沿用现有工程结构**，不为了“统一”突然切换到 React 或重建脚手架。

## 2. 建议代码分层（可根据现有目录调整）

```text
src/
  styles/tokens.css                 # 单一 Design Tokens 来源
  components/ui/                   # 基础共享组件：UiButton/UiField/UiDialog
  components/composites/           # 复合业务无关组件：PageHeader/SearchField
  components/patterns/             # 列表页/设置页/详情页结构模板
  features/users/                  # 按业务域组织组件/请求/类型
  composables/                     # useTheme/usePagination/useKeyboardShortcut
  stores/                          # 如需要，用 Pinia 维护客户端共享状态
  services/                        # API 客户端、错误映射、鉴权
  pages/ or views/                 # 页面组合逻辑
  tests/                            # 组件与业务测试
```

Nuxt 项目遵循 Nuxt 的 `pages/`、`components/`、`composables/`、`server/` 等约定，不强行塞入普通 Vue Vite 工程结构。

## 3. UI 技术路线

| 可选方案 | 包含内容/作用 | 适用 | 注意 |
|---|---|---|---|
| Reka UI | Select/Dialog/Tabs/Popover/Navigation Menu/Splitter 等无样式行为原语、键盘与焦点管理 | 自建视觉体系，高可定制 | 需要自己封装风格 Tokens 与业务变体 |
| shadcn-vue | 可复制的 Vue 组件源码、CLI、统一 Tailwind 风格，常以 Reka UI 构建 | 追求可维护和一致视觉的 Vue 应用 | 不是 React 的 shadcn/ui 组件源码，不混装 |
| Element Plus | 表单、表格、分页、日期、弹窗等较完整的产品组件 | 数据密集型管理系统 | 先主题化而非叠另一套组件外观 |
| Naive UI / Ant Design Vue | 业务丰富的组件套件 | 需要大量成熟控件 | 只选择一家作为主体系，避免风格割裂 |
| Tailwind CSS / CSS Modules | 样式能力，不提供组件行为 | 可配合上述方案 | Tokens 集中，避免各页任意颜色/圆角 |

**优先做**：审查现有 Dialog、Button、Input、Table；已有原语可用时复用，不重新写 div 弹窗。

## 4. 数据与交互

- 组件局部临时状态：`ref` / `reactive` / `computed`。
- 多页面共享的客户端状态（侧边栏、偏好设置、操作草稿）：Pinia（项目已用的优先）。不要把所有 API 响应复制进全局 store。
- 远端服务端状态（查询缓存、重试、失效与同步）：`@tanstack/vue-query`，或 Nuxt 原生数据获取机制；不是 Pinia 的同义替代。
- 分栏：优先 `Reka UI Splitter`，支持键盘操作，不需照搬 React `react-resizable-panels`。
- 图表：Apache ECharts（配合项目 Vue 集成）适合复杂数据可视化；较轻场景也可以选择已有 Chart.js 方案。
- 拖拽：检查 dnd-kit 对应 Vue adapter 的具体版本，或已有的 Vue 拖拽库；与按钮点击、触摸滚动、键盘行为兼容。

## 5. 动画适配

1. 简单显示/隐藏：Vue `<Transition>` / `<TransitionGroup>` + CSS。
2. 组件与布局动效：Motion for Vue（`motion-v`），按官方文档使用 `<motion />`。
3. 复杂时序、SVG、物理特效：Anime.js v4（命令式，用 `ref` 指向组件 DOM；`onMounted` 后启动，`onUnmounted` 前取消/清理）或 GSAP。
4. 滚动演示与复杂叙事：GSAP + ScrollTrigger，防止与框架渲染互相篡改布局属性。
5. SSR：不要在 `setup` 顶层访问 `window` 或创建 DOM 动画，必要时仅客户端加载。

## 6. 组件先行验收

- 先实现 `UiButton`、`UiField`、`UiPageHeader`，演示 disabled/loading/focus/error/long-text/dark。
- 对齐 `examples/vue3-web-components.md` 的示范；真实项目根据已有库更改实现。
- 业务页面应当组合共享组件和真实逻辑；仅为单个页面临时复制按钮 style 属于反例。

官方参考：
- https://vuejs.org/guide/introduction.html
- https://nuxt.com/docs
- https://reka-ui.com/docs/overview/introduction
- https://reka-ui.com/docs/components/splitter
- https://shadcn-vue.com/docs/introduction
- https://motion.dev/docs/vue
- https://tanstack.com/query/latest/docs/framework/vue/installation
