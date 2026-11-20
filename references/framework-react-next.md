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

## 7. React / Next 性能与组合架构专项门禁（按需）

这些检查用于 React/Next 真实项目，**不**自动应用到 Vue，且每项都须有实际症状或本次修改影响：

- **请求关系先于微优化**：通过 Network/Server log 标识串行依赖的请求瀑布，将独立请求并发化；不能为追求并发改变业务依赖或缓存一致性。
- **包体与首屏**：检查依赖锁文件、生产构建的 chunk 大小和新库增加的客户端 JS；只对低频、重组件考虑动态导入；首屏关键操作不能因懒加载而失去响应。
- **状态与渲染**：区分服务端数据、客户端草稿与本地动画状态。不要为所有 primitive 一律 memo；对已证实的重复重渲染、昂贵计算和监听器泄漏再采取优化。
- **服务端安全**：遵循当前 React/Next 版本的 SSR、RSC、Server Actions 与 hydration 规则；任何认证与授权必须在服务端真实验证，不靠隐藏按钮。
- **显式组件变体**：当 bool Props 组合导致不可能状态时，优先清晰的 variant API、组合式子组件和明确的状态所有权。React Context 不应变成存储整个后台业务对象的垃圾桶。
- **动态质量**：记录真实设备下的 long task、CLS、input latency 与动画中断；命令式动画正确取消；不能凭 CSS 中含 `transform` 断言 60fps。

可用 `scripts/mauforma_check.py` 对本次改动先做静态风险收集，再对真实页面复现交互、异步错误、焦点和最小支持视口。具体 API 以锁文件与官方当前文档为准。

官方参考：
- https://react.dev/learn
- https://nextjs.org/docs
- https://ui.shadcn.com/docs
- https://ui.shadcn.com/docs/changelog/2026-07-base-ui-default
- https://motion.dev/docs/react
- https://tanstack.com/query/latest/docs/framework/react/overview
