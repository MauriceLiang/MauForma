> v4 范围提示：本 Skill 以 Web 前端为直接适用对象。旧版本个别原生 SwiftUI/AppKit 条目仅供设计语义迁移参考，不用于要求安装或生成原生 UI 源码。

# Anime.js v4 官方能力全目录（核对日期：2026-11-02）

**重要范围定义**：以下是官网文档的顶层能力、关键入口及其效果，**不是预制 CSS 动画效果名称**。官网将动画定义为属性和时间配置组合；组合结果没有可穷尽的总数。准确区分官方 API 与本 Skill 的 `motion-effects.json` 视觉配方。

采用稳定版 **Anime.js 4.5.0**，不要套用 v3 `anime({targets:...})` 风格。建议 Web/Vue/React 项目 `npm install animejs@4.5.0`，按需 import；非 Web（SwiftUI 等）只转换动效意图，不硬嵌 JS。

| 官网类别 | 关键 API | 可产生的效果/用途 | 官网文档 |
|---|---|---|---|
| Timer / 定时器 | `createTimer` | 精确时序、计数、更新回调 | [官方文档](https://animejs.com/documentation/timer) |
| Animation / 动画 | `animate` | CSS 属性、transform、CSS 变量、DOM/SVG 属性、JS 对象属性的插值 | [官方文档](https://animejs.com/documentation/animation) |
| Timeline / 时间轴 | `createTimeline` | 串行、并行、标签位置、同步与回调 | [官方文档](https://animejs.com/documentation/timeline) |
| Animatable / 高频响应 | `createAnimatable` | 鼠标跟随、连续数据输入、快速更新目标值 | [官方文档](https://animejs.com/documentation/animatable) |
| Draggable / 拖拽 | `createDraggable` | 指针拖拽、轴限制、吸附、速度、回弹 | [官方文档](https://animejs.com/documentation/draggable) |
| Layout / 自动布局 | `createLayout` | 列表/网格切换、排序、容器尺寸或排列变化 | [官方文档](https://animejs.com/documentation/layout) |
| Scope / 作用域 | `createScope` | 组件作用域、响应式媒体条件、清理生命周期 | [官方文档](https://animejs.com/documentation/scope) |
| Events / 滚动事件 | `onScroll` | 滚动触发、阈值控制、滚动同步 | [官方文档](https://animejs.com/documentation/events/onscroll) |
| SVG / 形状变换 | `morphTo` | 两条路径的形状过渡 | [官方文档](https://animejs.com/documentation/svg/morphto) |
| SVG / 路径绘制 | `createDrawable` | SVG 描边逐段绘制与擦除 | [官方文档](https://animejs.com/documentation/svg/createdrawable) |
| SVG / 路径运动 | `createMotionPath` | 沿路径移动及方向跟随 | [官方文档](https://animejs.com/documentation/svg/createmotionpath) |
| Text / 文本拆分 | `splitText` | 按行、词、字拆分供错峰动画 | [官方文档](https://animejs.com/documentation/text/splittext) |
| Text / 字符扰动 | `scrambleText` | 字符随机替换并逐字揭示 | [官方文档](https://animejs.com/documentation/text/scrambletext) |
| Utilities / 错峰 | `stagger` | 依次入场、波浪式分布、网格错峰 | [官方文档](https://animejs.com/documentation/utilities/stagger) |
| Utilities / 其他 | `utils` | get/set、随机、数学插值、范围约束、清理 | [官方文档](https://animejs.com/documentation/utilities) |
| Easings / 缓动 | `eases, cubicBezier, linear, steps, irregular, spring` | 非线性时间曲线与弹簧物理 | [官方文档](https://animejs.com/documentation/easings) |
| WAAPI / 浏览器动画 | `waapi.animate` | 适用于基础视觉变换的轻量浏览器动画路径（能力与 JS 版不完全相同） | [官方文档](https://animejs.com/documentation/web-animation-api) |
| Engine / 引擎 | `engine` | 全局时间精度、速度与动画引擎设置 | [官方文档](https://animejs.com/documentation/engine) |
| Adapters / 外部对象 | `registerAdapter` | 动画驱动 Three.js 等非普通属性对象；官方内置 Three.js adapter | [官方文档](https://animejs.com/documentation/adapters) |


## 属性维度（Animation 文档）

- **CSS**: opacity、colors、尺寸、间距、背景、阴影及其他可插值属性；优先 opacity/transform，避免大面积布局重绘。
- **Transforms**: x/y/translateX/translateY、scale/scaleX/scaleY、rotate/rotateX/rotateY、skew 等，以实际浏览器/Anime.js 支持为准。
- **CSS custom properties**: `--value` 等可被插值的 CSS 变量；用于主题或图表视觉值，需谨慎检查类型兼容。
- **HTML/SVG attributes**: 如 svg `d`、stroke-dasharray 等，使用 SVG 工具更方便。
- **JavaScript object**: `{ value: 0 }` 的真实值插值；适合数字显示、Canvas 数据源。不要伪造业务数据。

## 时间与编排维度

- `from`、`to`；`delay`、`duration`、`ease`；`composition`、`modifier`；`keyframes`；`loop`、`alternate`、`loopDelay`、`autoplay`、`playbackRate`、`reverse`；onBegin/onUpdate/onComplete 等回调（以具体 API 为准）。
- `createTimeline`: `.add()`、`.sync()`、`.call()`、`.label()`；相对定位、标签、同时执行、依次执行；用于需要有意义的连续反馈。
- `stagger`: **时间错峰、值错峰、Timeline 位置错峰**；支持 `from`、`grid`、`axis`、`ease` 等分布配置。
- `onScroll`: 滚动触发、进入/离开阈值、进度同步；严禁劫持原生滚动体验。
- `createDraggable`: 网格吸附、惯性释放、边界、限定轴；释放回弹参数与实际拖拽状态必须一致。
- `createLayout`: 记录前后布局并动画过渡；适用于列表/网格、DOM 顺序和 CSS grid 布局切换。
- `splitText`: 行/词/字；`scrambleText`: 替换字符揭示。无障碍名字、长文字、动态内容应验证。
- `SVG`: `morphTo`/`createDrawable`/`createMotionPath` 分别对应形变、画线、路径移动，不应将它们当作同一个效果。

## 功能 ≠ 动效类型

`Timer`、`Scope`、`Engine`、`Utils`、`Adapters` 主要是实现基础设施，不要给它们杜撰“动画视觉特效”。本目录是对官方文档的归纳，不声称包含今后版本新增的 API，版本升级后须复核。

参考：<https://animejs.com/documentation>、<https://animejs.com/documentation/animation>、<https://animejs.com/documentation/easings/built-in-eases>、<https://animejs.com/documentation/layout>、<https://animejs.com/documentation/adapters>
