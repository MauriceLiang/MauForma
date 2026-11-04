# 可直接复制给任何前端 Agent 的提示词

## 0. 当用户不知道自己喜欢什么风格（优先执行）

```text
使用 $mauforma。用户无法明确描述想要的设计风格，请不要直接抛出“极简/科技风/玻璃拟态”等抽象标签。

第一轮：检查项目已有信息，只问网站用途、希望展示的内容（商品/照片/文章/产品功能/数据等）和访客首要操作中仍缺失的 1–2 项。允许用户用日常语言回答。
第二步：你负责结合内容、用途、受众、真实素材与产品任务进行视觉判断；给出 2–3 个有清楚区别、确实适合该项目的视觉方向，指明首推及理由。每个方向必须用普通语言描述：首屏第一眼看到什么、图片和文字如何摆、同屏展示多少信息、动画是什么感受、有哪些代价。
第三轮：等用户选定方向后，再把问题缩小到此方向相关的关键细节。每轮只问 1–2 个问题，每项提供 2–3 个具体易懂的选项（例：全幅图片 vs 左大图右文字），解释选择后的真实页面效果。
允许混合方案、看样例或委托你决定；未被用户选择的建议不可写成“用户已确认”。汇总设计简报后先统一 Design Tokens 和可复用组件，再进入业务页面开发。
如果用户已经明确给出风格/设计图，或只要求小范围修复，直接沿用已知约束，避免重复询问。
```

## A. 通用完整提示词（推荐默认）

```text
请使用 MauForma Skill 负责当前 Web 前端的视觉设计、交互体验及实施。

角色：同时拥有高级前端工程能力和成熟 UI/UX 设计判断的开发者。
你需要先理解产品的实际用户和任务，再选择合适的视觉密度、布局和动效。
当用户不知道风格时，优先询问网站用途、要展示的内容和访客最主要的操作；由你根据实际内容给出 2–3 套清楚说明首屏布局/视觉焦点/密度/取舍的推荐方案，并在用户选择方向后，才提供更细的配色、图文比例和动效选项。不得用专业术语要求用户盲选。

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

## 专项动画、图表、2D/3D 与物理特效的按需技术选型

```text
使用 $mauforma。先了解网页展示内容、访客操作、现有前端框架与已安装依赖，再判断需要的是普通状态动画、精密时间线、标题拆字、SVG 路径、数据图表、2D 精灵、3D 物体、图像 shader、粒子或真实物理碰撞。
从 references/visual-tech-selection-12.md 和 assets/visual-tech-catalog.json 中选 1–3 个必要的技术候选；说明 CSS/SVG 是否已足够、为什么需要新依赖、与现有动画引擎如何分工、Vue/React 生命周期如何清理、哪些设备需要 reduced-motion/静态回退。
不可把 12 项全部安装，也不可把工具本身当成设计目标。图表/模型需要真实内容，用户确认视觉方向后才实施；上线前核对版本、许可证与目标设备性能。
```

## Composition First / 不使用默认蓝紫 SaaS 布局的自主设计提示词

```text
使用 $mauforma。优先读取项目真实路由、内容、数据来源、现有组件和用户任务。
先独立绘制 2–3 套“灰阶也成立”的不同构图：必须改变主区域内容、首屏顺序、信息分组或图文关系，不能只换配色。
如果用户已选方向或仅修复局部，沿用现有选择并跳过不必要的多方案。
对每个候选解释主要内容面积、首屏操作路径、图表/空状态、适用人群、代价，并标明推荐与用户确认/委托来源。
确定结构之后才推导配色：品牌、内容材质、语义色和可读性，不能用科技/SaaS 默认蓝紫渐变；也不把暖灰/苔绿设为下一种刻板模板。
实施后用真实浏览器截图检查“去装饰测试”和视觉焦点。如果布局错，把时间用于重新构图，而不是继续叠加卡片、光环、渐变或圆角。
```

## 去除装饰性小标题、修正字体层级的针对性请求

```text
使用 $mauforma。根据当前项目、页面截图和真实内容检查：
1) 列出每处面向用户的 PageTitle、Section、英文副标、eyebrow、章节编号、图表说明、KPI 标签与数据来源；只有带来独立语义的保留，删掉没有信息增量的重复小标题/口号。
2) 不要把 ECharts tooltip 等开发者术语显示成业务界面文案；必要操作提示应使用普通用户能理解的语句，且功能真实存在。
3) 重新设计类型角色与比例：页面标题、区块标题、正文、KPI 数值/标签、图表刻度/图例和采样说明都要可读；避免 40–60px 抽象标题搭配 10px 数据标注。
4) 使用 scripts/audit_readability.py <web-src> --format json 找候选问题，但这不是自动裁决。使用实际浏览器截图验证桌面、窄屏、暗色对比、200% 文字放大；没运行则标 NOT RUN。
有正式品牌副标、面包屑、真实章节编号的情况下，保留并说明理由。
```

## 用户选择侧边导航颜色：整站协调而不擅自替换

```text
使用 $mauforma。先检查项目现有 Logo/品牌色、Sidebar、Topbar、Main、卡片和图表的颜色 Tokens。
如果用户已经指定了侧栏主色或精确 HEX，必须照选定值实施，不能因 AI 偏好改色；检查颜色与全站协调，并调整必要的文本/hover/selected/focus 角色以改善对比，若必须更改用户固定值请先征求同意。
如果用户还没有决定颜色，从 references/sidebar-color-reference-cases.md 的真实设计方法中挑选匹配该项目的 2–3 套全页面色彩组合，说明侧栏与主区的关系、适用性、利弊，展示整页预览并请用户选或自定义；推荐不是用户确认。
采用后将用户选定的色值、原话、决策来源和全局协调理由记录到 design-system/sidebar-color-decision.json，保证 Master Tokens 唯一。
真实浏览器检查全页及 Sidebar/Main 接缝、键盘焦点、暗亮模式、图表与重要文字；不能只靠 HEX 静态扫描断言美感。
```

## Navigation Architecture Gate / 用途和设备决定导航位置

```text
使用 $mauforma。先读取项目全部一级目的地、实际导航频率与层级，以及桌面、窄窗、手机的使用路径。区分全局导航、产品内导航、页面 Tabs、对象目录和当前任务操作。
参考 references/navigation-architecture.md 的官方依据和 9 种模式，给出 2–3 套具有真正 IA 差异的方案，解释为什么适合当前项目、牺牲什么、各断点怎么显示、隐藏入口如何访问。
用户明确指定顶部/侧边/底部时按要求实施；未定时展示预览并让用户选择或委托。不因 SaaS 自动侧栏，不在顶部+侧边+底部重复一套菜单。
桌面 Side+手机 Bottom 时，保留所有 route IDs 和状态，手机底部仅展示合适的核心入口，其余保持可发现。Side+Bottom task bar 时，底部是当前页面操作而不是第二套导航。
导航方案确认后才做共用组件和颜色映射；颜色继续遵循用户已选择的主色与 Sidebar/Main 协调规则。真实浏览器测试导航链接、手机抽屉、键盘、焦点、返回、resize 和遮挡，没有运行则写 NOT RUN。
```

## 页面信息过满 / 总览高级留白 / 分析页相对高密度

```text
使用 $mauforma。先检查当前路由真正要完成什么、首次访问与回访/已采集/失败的状态，再完整列出页面上所有教程、介绍卡、功能入口、动作和数据提示。
逐块判断 primary/supporting/conditional/deferred/removed。总览不能把“从仓库开始 + 三步说明 + 分析功能三卡 + 重复页脚入口”同时渲染；移出后确保帮助或详情页仍有入口。保留 Mock/真实数据来源、警告与错误。
将首页设计为舒展清楚的任务入口；数据分析详情允许更高信息密度，紧凑组织图表、指标、筛选而不牺牲轴/图例/样本可读性。
优先删除重复板块与无意义外层容器，再用 macro/meso/micro spacing 表达分组，不用固定 min-height 或大 padding 冒充高级留白。沿用用户确认的导航、配色与密度。
依据 references/page-density-and-content-priority.md、references/whitespace-and-surface-composition.md、assets/page-density-lab.html；浏览器中复核桌面/窄屏、不同用户状态，没跑就标 NOT RUN。
```

## 修复数据页面上下错列、底部贴边或内容不可达

```text
使用 $mauforma。先按页面任务和截图检查 RepoVantage 等工作台：
1. 标出内容区域左右边界、模块列线、每一排卡片的共同顶部。同级模块不使用两列各自上下堆叠造成第二排错位；用共享 CSS Grid 或主图跨全行结构，列宽可 3:2、8:4 且符合实际重要性，不强制所有卡片等高。
2. 检查必要图表/模块是否冗余，若有重复先做内容删减；真正数据、版本记录、图例、X 轴、来源说明保持完整可读。
3. 先区分正常首屏以下内容和无法滚到的裁切。查看 window / main-scroll 的真实滚动，检查 min-height:0、minmax(0,1fr)、fixed 底栏及 safe area 占位。禁止靠 height:100vh + overflow:hidden 假修复。
4. 在实际浏览器中截图首屏 + 滚动到最大位置的终点，分别查看宽屏、低高笔记本窗口和手机；检查最后记录/按钮、横向溢出与 200% 字体放大。
5. references/grid-alignment-and-viewport-safety.md 和 assets/grid-and-viewport-lab.html 仅是设计指导；可选 node scripts/audit_rendered_layout.mjs --url http://localhost:5173 做浏览器几何审查（需本地 Playwright），没执行写 NOT RUN。
沿用用户已确认的导航/配色，Agent 的布局建议与真实修复必须区分。
```
