# 可直接复制给任何前端 Agent 的提示词

## A. 通用完整提示词（推荐默认）

```text
请使用 MauForma Skill 负责当前 Web 前端的视觉设计、交互体验及实施。

角色：同时拥有高级前端工程能力和成熟 UI/UX 设计判断的开发者。
你需要先理解产品的实际用户和任务，再选择合适的视觉密度、布局和动效。

一、识别现状
1. 检查项目目录、package.json/锁文件、当前框架（Vue、React、Svelte、Angular、Solid、Astro 或原生 HTML/JS）、路由、现有 UI 库、样式组织和动画依赖。
2. 优先复用成熟组件、工具函数与业务逻辑；不要重复造轮子，也不能为追求效果无故更换技术栈。
3. 不将 React 专用库直接安装到 Vue 等框架；所有 API 按现有版本和官方文档核对。

二、先设计统一视觉系统，再开发页面
1. 选择与产品定位匹配的配色。可以创造主题色，不要求复制蓝紫粉渐变。
2. 建立唯一的 Design Tokens：语义色、浅/深主题、字体/字号、间距、圆角、阴影、边框与动效时长/缓动。
3. 先盘点并完成可复用组件：Button、Input/Field、Select、Dialog、PageHeader、Navigation、Table、Status/Feedback 等。
4. 组件必须具备适用的 hover、focus-visible、disabled、loading、error、success 等状态，并集中管理 variants/sizes。
5. 验证共享组件展示页后才批量开发业务页面；页面只负责组合组件和业务功能，不再分别重造按钮、弹窗、表单。

三、页面的视觉质量
1. 首先保证信息层级和功能流程，再追求精致视觉。避免假大空、模板化的营销文案。
2. 后台/列表/表单/设置页不默认使用英文装饰小标题 + 80px 巨型标题 + 大片空白；有意义的面包屑可以保留。
3. 官网/品牌页允许有意图的 Hero、渐变、特殊排版，但必须服从可读性与真实信息。
4. 不允许图标滥用、卡片套娃、随机圆角、多个抢焦点的主按钮和随意改变品牌色。

四、动画与技术选型
1. 动画要表达明确的状态、层级、反馈或空间关系。先选效果，再决定用 CSS、框架内置动画、Motion、Anime.js、GSAP 等。
2. 可参考 Skill 的 114 个原创动效配方与 Anime.js 官方 API；不是每个效果都要上，也不应强迫安装全部引擎。
3. 特效须支持取消/清理、SSR 边界、prefers-reduced-motion、低性能回退；动画加载失败时内容仍可见。
4. 允许参考 Magic UI/Aceternity 等优秀视觉组件，但只采纳对当前框架可维护且具有实际价值的部分。

五、必须保证工程质量
1. 保持现有业务、权限、数据请求和接口契约，不制造虚假的分析结果或交互。
2. 完成加载/错误/空状态、响应式、键盘/触摸、无障碍和性能优化。
3. 实际运行可用的构建、类型检查、测试和浏览器视觉验收。
4. 每项严重问题都给出：具体位置、影响、优秀替代、改动与验收证据。

最终交付：架构选择理由 + 主题 Tokens + 组件复用清单 + 页面成果 + 动效采用表 + 测试结果 + 未通过/未验证项。请直接实施任务，不用先空泛地写一篇设计宣言。
```

## B. Vue / Nuxt 项目专项

```text
使用 $mauforma。当前项目基于 Vue/Nuxt，保留 Vue 组件和现有 UI 库。
先检查 Reka UI/shadcn-vue/Element Plus 等现有组件，复用并统一 CSS Tokens。
优先实现共享 UiButton/UiField/UiPageHeader/UiDialog 与状态展示页，再组合页面。
动画先选 Vue Transition/CSS；需要更丰富的组件动效才考虑 motion-v；SVG 与复杂时序可考虑 Anime.js v4。
不得照搬 React 的 Zustand、Recharts、react-resizable-panels、lucide-react 作为 Vue 直接实现。
完成真实浏览器交互、键盘、响应式、暗色/亮色和 reduced-motion 验收。
```

## C. React / Next.js 项目专项

```text
使用 $mauforma。保持当前 React/Next 项目框架及路由。
先检查 shadcn/ui 的 primitive base（Base UI/Radix/React Aria）、组件目录及主题，已有稳定组件不重装。
按组件优先方式统一 Button/Field/Dialog/PageHeader/Navigation；使用语义 CSS Tokens 和变体。
若需要客户端共享状态才引入/复用 Zustand；有远端缓存/失效需求才使用 TanStack Query；图表/拖拽/可调分栏均按真实需求选。
普通交互优先 CSS，复杂状态动画可用 motion/react，滚动叙事才考虑 GSAP，SVG 时序可用 Anime.js。
测试 Next SSR/hydration、useEffect cleanup、StrictMode、响应式与 reduced-motion。
```

## D. 从设计审查到修复（不换架构）

```text
使用 $mauforma 的正反例评分规则审查当前 Web 前端。
先盘点共用组件、样式 token、页面标题/导航、关键操作、动效和状态，再提供具体问题清单。
按严重程度改造共享层，优先消除重复组件和风格割裂；每次变更不影响已有功能。
用实际浏览器截图/测试证明修复。如果没有测试环境，明确说明未做实测。
```

## E. 营销官网/作品集专项

```text
使用 $mauforma，当前是品牌展示/作品集网站，不要硬套后台系统的紧凑 PageHeader 模板。
可以设计具有辨识度的 Hero、合理渐变、精致排版和内容叙事，但 CTA、可读性与页面性能优先。
优先 CSS/轻量动画，必要时使用 Anime.js/GSAP/Motion；限制同时出现的特效，并为减少动态效果提供回退。
所有重复区块仍应先建立共享组件，页面保持统一 token。
```


## F. 带 React Bits 的 React / Next 产品营销网站

```text
$mauforma
项目是 React/Next 网页。先识别已有主题、共享组件、SEO 与路由。
视觉目标为成熟、精致、有记忆点的品牌官网。先完成可读的静态 Hero、关键内容与 CTA。
随后在 React Bits / Magic UI / Aceternity UI 中选择最匹配的 1–2 个可维护组件，例如短标题 Split Text 和低强度 Aurora；不要盲装整个目录。
核对所选组件官方版本、复制源码方式、依赖、授权与 Next 客户端边界。
检查桌面/手机、触摸、reduced motion、低性能和失败回退；动画不得遮挡 CTA。
只将通用 Button/Navigation/Link 交给自有统一 UI 基础层管理。
完成代码及浏览器测试，并列出选用效果、选型理由、体积变化和未验证项。
```

## G. Vue Bits / Inspira UI 的 Vue / Nuxt 产品官网

```text
$mauforma
这是 Vue 3/Nuxt 项目。保持现有 Vue 组件技术栈，不插入 React TSX。
先完善主题 Tokens、可复用 UI 组件与页面语义，再从 Vue Bits 或 Inspira UI 中逐项评估创意组件。
优先少量 Hero 文案、光感背景与特色卡片；动画需响应 prefers-reduced-motion，移动端提供静态回退。
检查 Vue 组件生命周期、Nuxt SSR/Hydration、Canvas/GSAP/OGL 清理、鼠标与触摸可用性。
浏览器验证官网 CTA、SEO 标题、页面性能与真实功能，不允许只交付截图。
```

## H. React Ant Design / Vue Ant Design Vue 后台

```text
$mauforma
优先使用项目已有后台主 UI 库。如果还没有，React 评估 Ant Design/MUI/Mantine/PrimeReact；Vue 评估 Ant Design Vue/Element Plus/Naive UI/Arco/PrimeVue。
先构建统一 UiButton、UiField、UiDialog、UiPageHeader、UiDataTable、UiFeedback 封装与 ThemeProvider。
主标题必须简洁清楚，不添加重复英文小标签或巨大宣传文字；数据表/筛选/操作一屏可达。
所有组件状态、表单验证、权限、远端数据、loading/empty/error/success、快捷键与键盘焦点应完整。
不因希望“酷炫”而在用户表格和设置页加入粒子/3D/持续背景动效。确有品牌需求时将其隔离到欢迎或空态页面。
完成自定义 Tokens 映射与浏览器、响应式、功能、无障碍回归。
```
