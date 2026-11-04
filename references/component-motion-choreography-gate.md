# Component Motion Choreography Gate · 让组件动起来，而不只让页面转场（v6.15）

**适用**：所有 Web 项目与框架；遵守 `references/motion-consent-experience-gate.md` 中用户已确认/继承/明确委托的强度。此 Gate 修补了 v6.14 的缺口：Agent 做一个路由 fade、Dialog fade 就自称“交互动效已完成”，却遗漏常用组件的状态变化。**动效质量不是动画数量**，而是足够有记忆点的局部过渡、清楚的因果、稳定的手感和可中断的实现。

## Gate CM0 · Component Interaction Inventory（组件比页面优先）

设计前列出当前产品**真实存在**且用户会操作的控件/组件，标注高频频率、显著性、是否有**可观察状态变化**。不要幻想不存在的组件、只为动效新增卡片。最少覆盖实际有的以下类型：
- Button / CTA：pointer、press、loading/result；区分高频次操作与重要确认。
- Tabs / Segmented / Filter / Navigation：选中指示器从旧位置过渡到新位置，内容与焦点保持连续；不要只做全页淡入。
- Accordion / Disclosure / Drawer / Popover / Dialog：从触发点展开/收拢、遮罩与内容空间、取消、focus restore；不仅单独 opacity。
- List / Card / Grid / Table：排序/增删/筛选前后位置连续性、焦点/选择、按需 detail preview；**不是把上百行逐条飞入**。
- Input / Select / Search / Form：focus/validation、清空与结果、过滤的状态与位置变化；输入准确性优先。
- Toggle / Checkbox / Radio / Slider：滑块/轨道/标记状态映射与触摸反馈，尊重原生语义。
- Data Visualization / Status / Progress：真实数据变化适度插值、tooltip/crosshair/比较选中；绝不捏造进度和“正在增长”的数值。
- Media / Commerce / Learning / Creative：媒体切换、产品变体、课程展开、作品焦点或叙事连接；同一策略不应强加给所有域。

**执行层级**：对每个重要的真实交互，给出 `motion | immediate-feedback | intentionally-static` 三选一，并解释为什么。用户选择 `none` 时允许全部为即时反馈，但焦点、选中、结果必须可感知；`balanced/expressive` 时不能“只有页面动画，组件全是 static”。**没有控件的领域不强制添加控件，局部 Bug 不扩大为全站重做**。

## Gate CM1 · Motion Art Direction（有识别度的组件动效，而非套用同一种 fade）

每个实际动效声明：
`component → trigger → from/to state → visual mechanism → timing/easing → purpose → cancel/reverse → reduced-mode → implementation owner → evidence`。

按用途在不同机制中择其一，**不是所有组件都必须具备所有机制**：
1. **Indicator travel / continuity**：Tab underline、Segment handle、侧栏选中背景从 A 到 B 连续移动（位置/尺寸）；不等于另一个 `opacity:0→1`。
2. **Spatial reveal / disclosure**：Accordion 内容区域高度与边界流畅展开，Drawer 有方向/来源，焦点/出口立即可用。
3. **State morph / tactile response**：Toggle thumb、复选标记、按钮按压/确认；触感而非弹跳大杂烩。
4. **Layout continuity**：筛选/删除/排序时其他对象**保留空间位置关系**，按需 FLIP/Motion layout/TransitionGroup；过渡不打断真实结果。
5. **Semantic feedback**：上传/保存/错误的状态徽记、短促反馈、提示；语义文字必先同步。
6. **Visual discovery / storytelling**：商品图文 hover 质感、作品聚焦、图像切换与少量共享元素；高频表格不做鼠标跟踪光效，触摸设备提供等效反馈。

**防重复模式**：不能把所有按钮都 `scale(.98)`、所有 Card hover 都 `translateY(-4px)`、所有分区都 fade+slide 作为完整动效设计。同一页面至少检查**交互机制是否因角色而不同**；不是为凑数量乱加五种。推荐以**一个或少量标志性动效**建立产品手感，其余高频组件保持连贯、克制；有明确品牌要求可例外。通用 Hover 色变是有效反馈但不能冒充“组件动效创意已完成”。

**动效与文案和可访问性共存**：小按钮文本不得断字、读数/错误及时显示、Keyboard focus 不隐形；不要把 aria-hidden 错加给必读信息。禁止依赖 hover 才能发现核心按钮。

## Gate CM2 · 推荐工作流：先呈现候选体验，后写实现

- 对新项目/重大交互改版，继续执行 v6.14 用户动效强度确认；**用户只选 B/C 等强度，Agent 还要主动挑选适合本产品的组件动效方案**，而非继续追问每个按钮。举例：一个工作台可以主打平滑 segmented indicator + 编辑行的局部布局衔接；课程可主打渐进式章节展开与答案反馈；商品可以主打变体图像连续过渡。
- 先展示小范围 **Component Motion Showcase**：2–4 个最重要的真实组件，在 `none / selected-level / reduced-motion` 下的状态演示，说明独特之处及不用动效时的状态。小修无需再次走完整展示。
- 对创意需求，按顺序查看 `references/creative-component-libraries.md`、`references/animation-engine-selection.md` 和既有 114 配方目录；参考技术方案而非机械复制样式。选择同框架/同版本的实现；使用 React Bits / Vue Bits / Inspira / Motion / GSAP 前核对来源、依赖/许可证、SSR/移动端性能。**不必为常规 indicator/accordion 安装动画库**。
- 项目级 Motion Tokens 既包含时长/曲线，也包含**角色化机制**：`interactive-control`、`selection-indicator`、`disclosure`、`layout-change`、`feedback`、`spotlight`。不要把整站所有动画绑定到一个 `--duration` 而忽视频率、距离与内容优先级。

## Gate CM3 · 什么时候应该不动

- 没有状态变化、用户不可操作的装饰；某些长阅读正文、密集表格每次刷新的全量 stagger；高频交易与敏感操作需要瞬时确认时的长过渡。
- 用户明确选择无额外动效，或 `prefers-reduced-motion: reduce`：保留 selected/focus/结果的**即时静态表现**；背景自动循环/视差/3D 需要禁用或提供可停手段。
- 动效会导致 CLS、重排错列、误导数值、跳过键盘焦点、窄屏裁切、变慢或低端设备掉帧时先修功能、降级或删除。**不能用“性能不好”作为完全不探索组件动效的默认借口**；可以选择更简单的机制。
- 遵守已有确认偏好；用户没有要求超范围创意时不额外改色、换框架或大改布局。

## Gate CM4 · Real Interaction QA（当前 v6.14 的测试缺口）

**必要证据不是“动画 class 存在”，而是实际触发：**
1. 从产品交互清单核对高价值组件有没有 `motion / feedback / static(reason)`，不能拿路由转场算组件覆盖。
2. 浏览器触发 Button、Tab、Disclosure、Toggle、List、Feedback 等实际存在的状态变化，取**交互前/进行中/结束**状态，检查位置或高度/插值行为，而不仅仅 `animationDuration > 0`。
3. 快速反复切换、逆向、失焦、未登录/错误、窄屏和 200% 字体，验证状态不迟到、交互不被遮挡、不会中途冻住或发生多重动画冲突。
4. reduced-motion 开关前后测相同业务结果与焦点，非必要运动立即减弱/关闭。不同框架必须在真实目标页面复核而不是只测 standalone demo。
5. **明确测试边界**：结构/覆盖清单的 JSON 校验不证明美感、CSS 有动画不代表有交互；独立实验页的通过不代表真实项目页面已通过。

## 可核对参考（以当时文档的 API 与许可为准）

- IBM Carbon productive / expressive motion: https://www.carbondesignsystem.com/building-blocks/foundations/motion/overview
- Motion gesture, focus, tap: https://motion.dev/docs/react-animation
- Motion layout and shared elements: https://motion.dev/docs/layout-animations
- W3C WCAG Animation from Interactions (AAA): https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions
- 可选组件选型：`references/creative-component-libraries.md`

本规则必须与 `references/motion-consent-experience-gate.md`、`references/component-craft-gate.md`、`references/control-geometry-gate.md` 和 `references/animation-integration-lifecycle.md` 一起使用。
