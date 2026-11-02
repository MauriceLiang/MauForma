# 12 项动画与可视化技术：场景驱动选型（MauForma）

**依据**：用户提供的《12项前端动画与可视化技术选型指南》，并与本仓库既有的 `animation-engine-selection.md`、`animation-integration-lifecycle.md`、`framework-vue-nuxt.md`、`framework-react-next.md`、`stack-guide-11-items.md` 对照。原指南是技术选型资料，**不是强制安装清单**。12 项并非相互竞争的同一种动画框架。

## 不重复既有规范

GSAP、anime.js、Three.js、Apache ECharts 和 CSS/SVG 基础已在 MauForma 中有所覆盖；本页补齐 **SplitText、PixiJS、Curtains.js、Rough.js、Vivus、SVG Filter、tsParticles、Matter.js** 的职责，强化技术之间的组合边界。既有 114 种 Anime.js 配方、React/Vue 组件和图表规范照常保留。

## 12 项职责矩阵

| 技术 | 核心职责 | 最适合 | 何时避免 |
| --- | --- | --- | --- |
| GSAP | 多元素精密编排、滚动驱动叙事 | 品牌产品介绍、滚动叙事、高表现力首屏 | 简单 hover |
| anime.js | DOM/SVG 小范围动画、stagger 与短时间线 | 局部视觉反馈、SVG 插画、轻量品牌交互 | 用其替代纯 CSS hover |
| SplitText（GSAP / anime.js 对应实现） | 按行、词、字拆分文字并分别入场 | 品牌标题、章节标题、短句揭示 | 长篇正文逐字滚动 |
| PixiJS | 大量 2D 精灵、纹理、交互对象的高频渲染 | 2D 互动海报、2D 游戏、展览互动墙 | 普通表单/卡片 |
| Three.js | 3D 模型、光照材质、相机与空间交互 | 3D 产品展厅、设备模型旋转、沉浸式场景 | 纯 2D 特效 |
| Curtains.js | DOM 布局中的图像/视频映射为 WebGL 平面与 shader 特效 | 创意作品集、视频过渡、图片悬停波纹 | 不需要 shader 的普通图片 |
| Apache ECharts | 业务数据的交互式统计图表与仪表盘 | 后台/BI、运营分析、科研数据、实时监控 | 装饰型动画 |
| Rough.js | 画出手绘笔触的 Canvas/SVG 图形 | 教育插画、白板、草图式流程图、活泼品牌 | 精密数据后台的全部 UI |
| Vivus | SVG stroke 路径逐步显现 | Logo 开场、地图路线、线稿插画 | 只有填充没有可绘 stroke 的图 |
| SVG Filter | 浏览器原生 SVG 滤镜图形处理（并非 npm 动画库） | 局部波纹、纹理扭曲、发光/模糊、图像变形 | 大面积高频滤镜 |
| tsParticles | 可配置粒子背景和事件性庆祝视觉 | 节庆页面、完成任务庆祝、有目的的科技视觉背景 | 所有页面常驻粒子 |
| Matter.js | 计算二维刚体、重力、碰撞与约束；不负责完整网页渲染 | 2D 互动玩具、物理实验教学、有碰撞的互动海报 | 普通列表拖拽/排序 |

**特别澄清**：
- GSAP 的 **SplitText 插件**与 anime.js 的 **`splitText()`** 是不同 API；按项目现有引擎选一种。文字拆分时要处理响应式重拆、屏幕阅读器、字体加载和 DOM cleanup；不要将普通长文逐字动画化。
- **SVG Filter 属于浏览器原生 SVG 技术，不是新的 npm 库**。先检查 CSS filter 是否已经足够。
- **Matter.js 仅负责物理计算**，PixiJS 负责 2D 绘制；不要把 Matter.js 误认为会自动渲染网页元素。
- Three.js、Curtains.js 和 PixiJS 都涉及独立的图形渲染/增强层，但 **Three.js 处理真实 3D**、**Curtains.js 倾向网页图片/video 与 shader**、**PixiJS 处理高密度 2D**。
- ECharts 是业务数据可视化而非通用动效；UI 组件状态仍由 Vue/React 管理。

## 按网站/目标组合

| 网站/内容 | 基础建议 | 条件性增强 | 不要做什么 |
| --- | --- | --- | --- |
| 普通企业官网/SaaS | CSS + anime.js | GSAP | 不要以营销特效覆盖后台业务区域 |
| 高品质品牌/滚动叙事 | GSAP + SplitText（GSAP / anime.js 对应实现） | Curtains.js | 不要在每一段正文拆字或默认加入 WebGL |
| 3D 产品展示 | Three.js + GSAP | 无 | 模型不可用或低性能设备应转静态图 |
| 数据大屏/管理后台 | Apache ECharts + CSS | 无 | 不用 PixiJS 来重做日常折线图 |
| 创意 2D 海报/小游戏 | PixiJS | Matter.js | Matter.js 不是渲染引擎 |
| 手绘插画/教育 | Rough.js + SVG | GSAP | 不要强行将精密后台控件全部变成手绘 |
| 庆祝/粒子背景 | tsParticles + CSS | 无 | 减少动画时停止，不让常驻粒子抢占性能 |
| Logo 路线线稿 | Vivus | GSAP | fill-only SVG 不是可描边的 stroke 路径 |
| 波纹/液态图片 | SVG Filter | Curtains.js | 大面积连续 GPU 滤镜必须测性能和做静态降级 |

**选型时先证明需求**：用户只要求产品展示、图片动效或表格图表时，先确认内容、视觉焦点、首屏目标、已有依赖、可用素材和目标设备。默认选择 CSS/SVG/框架转场；只有不足时才引入 GSAP/anime.js；只有清晰的特殊效果需求才引入重型 Canvas/WebGL/物理工具。不要把右侧「条件性增强」理解为推荐一并安装。

## 8 项工程验收门槛（源指南要点）

1. **为确切的视觉需求安装依赖**：说明“缺什么效果”及为何 CSS/SVG/已安装工具不足。
2. **动画属性所有权**：GSAP、Anime.js、Motion、CSS 不可同时控制同一 DOM 属性；有多个引擎时分组件/分属性。
3. **可访问与减少动效**：支持 `prefers-reduced-motion`；文字分拆保留屏幕阅读器语义；动画失败内容仍可见。
4. **生命周期清理**：Vue mounted/unmounted，React effect cleanup；释放 WebGL 纹理/renderer、监听器、Observers、定时器和物理 runner。
5. **按需激活**：3D、粒子、图表非首屏才延迟加载；不可见或后台时暂停不必要的持续渲染。
6. **GPU/CPU 预算**：限制像素比、模型面数、纹理、精灵/粒子数和碰撞约束，移动端提供静态/低特效版本。
7. **实测而不是推断**：测量 FPS、主线程阻塞、页面内存、设备占用、布局抖动和弱网加载。
8. **版本/授权**：安装前查锁文件、官方 API、浏览器兼容和插件许可；演示不能当成已在具体项目运行。

## 框架集成与退化

- **Vue / Nuxt**：简单进出优先 `<Transition>`；命令式图形/动画只在 `onMounted` 后创建，`onUnmounted` / `onScopeDispose` 销毁；SSR 用 `ClientOnly` 或同类保护。
- **React / Next.js**：简单状态动画优先 CSS 或 Motion；实例在 `useEffect` 中管理，清理需可重入；SSR/RSC 不在服务器侧引用 window/document。
- **普通 HTML、CSS、Svelte、Angular 等**：按框架 mount/destroy 生命周期实现；不为获得 Canvas 特效重写所有页面。
- **故障回退**：Three.js 显示可读的产品摄影，Curtains.js 显示原始图片，粒子替换静态背景，ECharts 可给出可访问表格或数据摘要。重要按钮与正文永远在可交互 DOM 内。

## 选型检索

`python3 scripts/search_visual_tech.py --goal "3D 产品展示 滚动镜头" --json`

脚本只检索候选技术、表达适用理由，不替用户安装依赖或认定性能达标。目录原始数据：`assets/visual-tech-catalog.json`。已有动画生态的引擎优先级详见 `references/animation-engine-selection.md`。

## 官方资料

- GSAP：https://gsap.com/docs/v3/
- anime.js：https://animejs.com/documentation/
- SplitText（GSAP / anime.js 对应实现）：https://gsap.com/docs/v3/Plugins/SplitText/；另一实现 https://animejs.com/documentation/text/splittext/
- PixiJS：https://pixijs.com/
- Three.js：https://threejs.org/manual/
- Curtains.js：https://www.curtainsjs.com/
- Apache ECharts：https://echarts.apache.org/en/
- Rough.js：https://roughjs.com/
- Vivus：https://github.com/maxwellito/vivus
- SVG Filter：https://developer.mozilla.org/en-US/docs/Web/SVG/Guides/SVG_filters
- tsParticles：https://particles.js.org/
- Matter.js：https://brm.io/matter-js/

维护原则：本文的“搭配建议”“上手难度”“性能风险”属于场景化工程判断，**并非项目性能基准测试**。来源文档指出需要持续复核版本和授权；如官方 API 更新，应以项目当前版本为准。
