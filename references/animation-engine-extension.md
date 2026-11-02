# 新增动画引擎时的维护协议

本 Skill 允许持续纳入新动画技术，但需先完成研究与验证，不因“看起来新颖”而无理由升级默认依赖。

## 引擎评估表（每项必填）

1. 名称、官方主页/文档、维护状态、当前主要版本与核对日期。
2. 是否适合 Web：DOM/SVG/Canvas/WebGL/设计师素材；浏览器兼容性。
3. 哪些框架可以直接使用（React、Vue、Svelte、Angular、Solid、Astro、Vanilla），真实包名与导入路径。
4. 专长：基本过渡、状态驱动布局、时间轴、Scroll、路径、物理、拖拽、复杂角色动画等。
5. API 与生命周期：挂载、取消、销毁、route change、SSR、StrictMode、observer 回收。
6. 性能与构建成本：JS 体积、tree shaking、帧率、低端设备、动画退化方案。
7. 可访问性：reduced-motion、键盘、焦点、可暂停循环。
8. 授权与商业使用限制；第三方区块、素材及插件授权可能不同。
9. 对现有 CSS/Motion/Anime.js/GSAP 的实际增益，是否只是重复能力。
10. 至少一个真实示例、一个反面示例、一个失败回退测试。

## 接纳规则

- 新引擎可以成为“候选”，不自动升级为全局默认。
- 同一工程最多设置一个主要命令式动画引擎；多个引擎同时存在必须按独立区域和职责划分。
- 加入时同步更新 `animation-engine-selection.md`、`animation-integration-lifecycle.md`、`examples/prompt-library-web.md` 与验证清单。
- 不要宣称列出了所有可能动效：API 有限，但组合无限。

## v6.2 · 新增专项渲染能力的分类

不能将所有 Canvas/WebGL/物理技术都误记为“动画引擎”。增加新工具时，先分组为动画编排 / 文本拆分 / 2D 渲染 / 3D 渲染 / DOM-WebGL / 图表 / 手绘 SVG / 描边 / 浏览器滤镜 / 粒子 / 物理，再对照 `assets/visual-tech-catalog.json`，确认现有技术无法解决后才新增依赖。关于组合、可访问性、移动端 GPU 限制和失败回退参见 `references/visual-tech-selection-12.md`。
