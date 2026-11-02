# React / Next.js · 深度支持实施规范

## 1. React 与 Next.js 的角色

React 是 UI 组件/状态模型，TSX 与 hooks 构建可复用界面；Next.js 是 React Web 应用框架，提供路由、服务端渲染、数据获取等能力。已有项目按当前路由方案（Next App Router / React Router / Vite）实施，不能强迫所有 React 工程改用 Next。

## 2. 组件与 UI 原语

| 方案 | 作用 | 适用 | 边界 |
|---|---|---|---|
| shadcn/ui | CLI 将可维护的组件源代码加入项目；提供主题、组件组合及变体 | 需要自有视觉语言的 React | 不是“不受你控制的黑盒组件包”；先核对 primitive base |
| Base UI | 无样式行为、ARIA、交互原语 | 新建高度可定制组件 | `render` 等 API，不能直接照搬 Radix `asChild` |
| Radix UI | 无样式交互原语 | 现有 Radix 项目及可定制控件 | 保留现有实现，不需因为新默认变动而迁移 |
| React Aria | 可访问性和国际化的控件行为 | 表单、选择控件、多语言场景 | 与主组件设计系统做封装 |
| MUI/Mantine/AntD/Chakra | 较完整的 React UI 组件 | 企业业务多、希望开箱即用 | 不要在一个项目到处混用多个视觉系统 |
| Magic UI / Aceternity UI | 高表现力视觉组件、动画区块、落地页效果 | 品牌官网、作品集、少量特定场景 | 不能替代 Dialog/Field/DataTable 基础组件所有权 |

2026-07 官方 shadcn/ui 新项目默认选择 Base UI，仍支持 Radix。已有 Radix 项目**无需迁移**。Base UI 与 Radix 的组件组合语法不完全相同，先查询项目真实安装方式与官方规则。

## 3. 实施目录示例

```text
src/
  styles/tokens.css                 # 全局语义 Tokens
  components/ui/                   # Button/Field/Dialog/Toast 等
  components/composites/           # SearchField/PageHeader/DataTable 工具组件
  components/patterns/             # 通用页面组织结构
  features/users/                  # 页面业务功能、hooks、API 与数据模型
  lib/                              # API client、工具函数
  stores/                           # 如使用 Zustand
  hooks/                            # 共享行为 hooks
  app/ or routes/                  # Next/React Router 特有路由
  tests/
```

## 4. 状态边界

- 局部状态：`useState` / `useReducer`，不要把按钮开关都放全局 store。
- 共享客户端状态：Zustand / Context（已安装项目优先）；例如全局面板选择、UI 草稿、用户偏好。
- 服务端状态：`@tanstack/react-query`（请求缓存、错误重试、失效刷新），或 Next 框架的数据策略；和 Zustand 的职责不同。
- 可调整分栏：`react-resizable-panels`；排序/拖拽：dnd-kit React adapter，具体 API 依当前版本。确认 React StrictMode、卸载、SSR 边界。
- 图表：Recharts 适合 React 数据图表，复杂可视化也可用 ECharts；图表应提供数据含义、单位、图例与可访问表格回退。

## 5. 动画适配

- 交互基线：CSS transitions / Web Animations API。
- React 状态驱动的入场、退出、布局变化、手势：Motion (`motion/react`)；`AnimatePresence` 按官方当前版本。
- SVG/复杂时序：Anime.js v4 或 GSAP；在 React `useEffect` 中作用于 `ref` 范围，卸载和依赖变化时进行 cleanup。
- React 18/19 / Next SSR：不要在 render 或服务端入口读 `document` / `window`；交互动效放 client component 与 effect；必要时动态加载以减少首屏 JS。

## 6. 组件先行验收

- 同一共享组件实现 primary/secondary/ghost/danger 变体；处理 disabled/aria-busy/loading/keyboard。
- 建立 PageHeader、Field、Dialog 以及各状态可观察展示页。
- 页面仅组合组件。查看 `examples/react-web-components.md`。

官方参考：
- https://react.dev/learn
- https://nextjs.org/docs
- https://ui.shadcn.com/docs
- https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default
- https://motion.dev/docs/react
- https://tanstack.com/query/latest/docs/framework/react/overview
