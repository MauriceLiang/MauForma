# Web 动画引擎选型与候选目录（v4）

## v6.14 · 先确认交互动效体验，再选择工具

`references/motion-consent-experience-gate.md` 是动效的上游规则。用户有权选择不增加视觉运动、细腻反馈/转场或更有表现力的少量场景。重大设计若无已确认/明确委托的动效基调，先用 2–3 个具体体验选项询问，不得因为“默认动画 CSS+框架”就暗自为用户决定无动画或加动画。用户选择“无额外动画”仍必须保留即时、清楚的交互状态反馈；选择 B/C 则对真实交互建立覆盖清单并验收。此页只负责**技术选型**，不负责替用户批准视觉运动。

## 原则：不绑死 Anime.js，也不靠引入库体现设计感

由**视觉目的**驱动选型：状态反馈、层次过渡、布局重排、滚动叙事、SVG 图形、骨骼互动。先判断 CSS / 框架内置动画是否足够，再决定是否引入大型引擎。

| 技术 | 核心功能 | Vue | React | 适用效果 | 何时不选 |
|---|---|---|---|---|---|
| CSS transitions/keyframes | hover、焦点、Opacity/Transform、轻量微交互 | 原生 | 原生 | 默认按钮、浮层、页内轻量变化 | 非常复杂时序、细粒度播放控制 |
| Web Animations API | DOM `Element.animate()`、暂停、取消、完成状态 | 原生 | 原生 | 少量可控命令式动画 | 需求复杂到要自己写大量协调器时 |
| Vue `<Transition>`/`<TransitionGroup>` | Vue 组件进入/离开、列表移动 | 原生 | — | Vue 状态驱动切换 | 非 Vue 项目 |
| Svelte transitions | Svelte 自带进入/离开与列表过渡 | — | — | Svelte 站点的基本过渡 | 非 Svelte |
| Motion | React `motion/react`、Vue `motion-v`、Vanilla `motion`；布局、spring、手势、滚动 | 官方 Vue 版 | 官方 React 版 | 状态驱动的组件/布局转场 | 只需 hover 透明度时 |
| Anime.js v4 | 属性/时间轴/stagger/SVG/scroll/draggable/easings/工具等 | DOM 集成 | DOM 集成 | 高可控 DOM/SVG 多段编排 | 框架纯声明式就够时 |
| GSAP | Tween/Timeline、ScrollTrigger 和各类插件 | DOM 集成 | DOM 集成 | 复杂时间轴、滚动叙事、高度编排 | 普通管理界面的全部按钮 |
| AutoAnimate | 自动感知子元素新增/删除/重排动画 | 需确认适配版本 | 需确认适配版本 | 轻量列表自然过渡 | 需要严格复杂编排时 |
| Lottie | 设计师制作的矢量动效素材播放器 | Web runtime | Web runtime | 成功状态插画、品牌动画 | 数据表格、输入控件基础交互 |
| Rive | 状态机、交互式矢量动画 | Web runtime | React runtime | 人物插画、进度/品牌交互 | 无法覆盖/测试状态与低端设备时 |
| View Transitions API | 浏览器页面/视图间视觉连续性 | 浏览器 API | 浏览器 API | SPA/MPA 场景合适时 | 未验证浏览器支持、产生跨页闪烁时 |
| Canvas / WebGL / Three.js | 高复杂图形、粒子、3D | WebGL canvas | WebGL canvas | 可视化、3D 宣传/创意作品 | 不应替代普通 DOM 表单 |

### 推荐优先级

1. **默认动画**：CSS + 框架转场。所有常规组件一套 motion tokens。
2. **需要声明式布局/手势**：Vue 用 Motion for Vue，React 用 Motion for React；选单一主体系。
3. **需要丰富 keyframes/SVG/stagger**：Anime.js v4。
4. **滚动叙事和复杂多段时间轴**：GSAP；先评估性能与许可证。
5. **复杂产品插画**：Lottie 或 Rive，动画素材与运行时代码责任明确。
6. **实验性内容**：Canvas/WebGL，必须做降级与帧率管理。

## 动效质量等级

- **A级：日常可用**：hover 颜色/阴影、button press、popover/dialog enter/exit、短暂状态图标、行插入重排。
- **B级：上下文明确才用**：布局调换、拖拽吸附、图表 transition、scroll reveal、成组 stagger、部分文字揭示。
- **C级：品牌/创意专项**：3D 倾斜、粒子、形变、scrambleText、强烈弹性、全屏转场。
- **拒绝**：遮挡关键操作、反复强制重播、导致内容不可见、把非真实数字演成“计算完成”、无 reduced-motion 或性能回退。

## 参数建议（设计默认值，非官方标准）

| 效果 | 参考时长 | 幅度 | 建议缓动 |
|---|---|---|---|
| Hover/Press | 100–180ms | scale 0.98–1.00/轻变色 | ease-out |
| 提示/弹窗 | 160–240ms | 8–16px + opacity | outCubic / inOutSine |
| 列表进入 | 180–300ms | 8–16px + opacity | outCubic，少量 stagger |
| 页面/主要区块 | 200–350ms | 12–24px | outCubic/outQuint |
| 品牌展示型 Hero | 300–650ms（按需） | 控制数量与遮挡 | inOutSine/自定义 |

复杂与独特动效优先检索：`animejs-motion-recipes.md`（114 个原创配方）、`animejs-easing-complete.md`（45 个内置 easing）；两者不等同于“Anime.js 所有现成内置效果”。

官方资料：
- https://animejs.com/documentation/
- https://motion.dev/docs
- https://gsap.com/docs/v3/
- https://developer.mozilla.org/en-US/docs/Web/API/Web_Animations_API
- https://auto-animate.formkit.com/
- https://rive.app/docs/
- https://developers.lottiefiles.com/


## v5 视觉组件 ≠ 底层动画引擎

React Bits/Vue Bits/Inspira UI/Magic UI/Aceternity UI 是**可选的组件与效果源码库**，并非新的一套底层统一动画引擎；组件内部可能使用 GSAP、Motion、OGL/WebGL 等。先查组件文件具体依赖，再决定是否仍需 Anime.js、GSAP 或 Motion，避免同一 DOM 属性由多套动画同时操纵。见 `references/creative-component-libraries.md`。

## v6.2 · 超出通用动画库的专项技术

此表主要回答“选哪个**动画引擎**”；PixiJS、Three.js、Curtains.js、ECharts、Rough.js、Vivus、SVG Filter、tsParticles、Matter.js 并非同一类别的竞品。按内容与所需图形特征，参阅 [12 项动画与可视化技术选型](visual-tech-selection-12.md) 与 `assets/visual-tech-catalog.json`。GSAP SplitText 与 anime.js splitText 是不同 API；原生 SVG Filter 不应被当成额外依赖。若日常微交互能用 CSS/框架原生能力完成，则不必引入以上库。
