# Motion Choice & Experience Gate · 动效由用户选择，交互由体验负责（v6.14）

适用于所有 Web 网站与应用：Operate（工作台）、Persuade（品牌/营销）、Read（阅读/教学）、Experience（互动/作品）。动效是**设计决策**，既不能“默认全站无动画”，也不能“默认所有元素动起来”。需要分别处理 **用户意愿、交互反馈、信息连续性、视觉质感、可访问性、性能和回归证据**。

## Gate M0 · 侦察、明确用户选择权（优先于选库/写 CSS）

1. 读取已存在的设计决策、品牌动效、组件库内置 motion、用户在**当前项目**已明确的动效偏好。记录来源：`confirmed`（用户明确选）、`delegated`（用户明确把动效决定权交给 Agent）、`inherited`（继承已有已确认系统）、`unresolved`（未明确）。
2. **新网站、整体重设计、会显著改变动效观感的交互改版**：若动效还未被确认或明确委托，**必须主动询问一次用户**。把选择放在设计方向确定后、Motion Tokens 与组件实现前；允许与一轮设计方向确认合并，避免反复提问。不能把“用户没提动画”“希望简洁”“让你写代码”“页面要快”当成“用户同意全站不做动效”；同样也不能推断用户同意额外滚动/粒子/全屏转场。
3. **有已知答案不要重复问**：用户选了静态、轻柔或更丰富，直接继承并记录，除非要扩展到明显超出授权的动效（如从轻微 hover 到强滚动视差）。
4. **明确全面委托动效**时可代选，并记录选择原因和 `delegated`；不得把 Agent 推荐冒充 `confirmed`。仅“直接开发”“少问问题”不等于对额外动效范围的明确授权。
5. **局部 Bug、非视觉修复、既有组件状态修补**：不重复启动全站设计访谈；沿用既有 motion policy。若尚未作出动效选择，保证即时的静态交互反馈、焦点/状态可见与业务功能，不擅自推出新的视觉动效，标记待定而非“动画永久关闭”。未确认的重大视觉改动应先提出具体选项，不能悄悄决定零动画。
6. 用户选择“无额外动效”是合法结果，但**不可取消交互语义**：按钮按下/选中/焦点、提交 loading、成功/失败通知、展开/收起的最终状态、校验与导航反馈必须可感知。无动效 ≠ 无交互反馈。

## Gate M1 · 面向普通用户的 3 档具体选择

询问时只提出**一个自然语言问题**，提供有实际画面差异的少量方案，附推荐与性能取舍。推荐不等于确认：

> 这个网站的交互切换想要哪种感觉？
>
> **A｜干净利落**：状态即时改变，按钮/焦点仍有明确反馈；不加额外页面或滚动动画。适合高频办公或偏好极低动效。
>
> **B｜细腻流畅（多数普通 Web 产品的建议候选）**：按钮轻微按压、Tabs 指示平滑移动、面板/弹窗短暂淡入淡出、状态/列表变化有连续性；不拖慢操作。
>
> **C｜有表现力**：在 B 的基础上，在少量关键场景加入页面共享元素过渡、主视觉/图像进入或滚动叙事；更突出品牌氛围，也需更多适配与性能预算。
>
> 我推荐 B，因为 [基于该项目的具体理由]；你选 A、B、C，还是想混合/自行描述？

不能机械复制上述话术到每个项目，应使用用户的主要页面与交互描述“看得到什么”。允许“你决定”、只选某一类动效、或不同页面不同强度。**A/B/C 是选择辅助，不是不可修改的等级或全站唯一档位**。如已有明确方向，只问真正未知的一项，避免把动效和配色/字号同时做成一张长问卷。

### 情境差异（同一原则，不同结果）

| 场景 | 建议讨论的可见行为 | 应避免 |
| --- | --- | --- |
| Operate | 筛选/Tab 状态切换、Popover/Dialog 进入、插入删除与状态通知、导航焦点 | 高频列表每一行都飞入；动画阻止用户立即点击 |
| Persuade | 导航与 CTA 反馈、图片/产品切换、适量 Hero 或产品故事转场 | 首屏内容等待长时间动画才能看见 |
| Read | 目录选中、内容锚点、注释/折叠状态、练习反馈 | 文章正文频繁滑移，妨碍连续阅读 |
| Experience | 作品切换、共享视觉元素、定向叙事/画布交互 | 长循环遮挡出口，交互必须等动画播完 |

## Gate M2 · 按功能分类，不是“有无特效”的二元选择

为实际存在的交互（不可虚构）逐项记录 `trigger → from/to state → purpose → visual treatment → cancellation/interrupt → reduced-motion alternative`：

- **Input feedback**：hover、press、selected、focus-visible、字段反馈。反应及时，视觉可辨，focus 不可因动画延时出现。
- **Disclosure & overlays**：Dialog、Drawer、Dropdown、Popover、Accordion 的进退场可缓和突兀切换；关闭、Escape、focus restore 与真实 DOM 状态正确同步。
- **Navigation & continuity**：Tab、侧边栏、路由切换，保留上下文和阅读位置；允许不需要动画的路径，避免双重旋转/空白闪烁。可评估 View Transitions API，需检查实际浏览器支持与回退。
- **Data & status**：列表重排、图表增量、进度、loading/success/error 等。不虚构进度、不要在流式/频繁更新时不断重播，动画不能“掩盖后台没完成”。
- **Story & delight**：营销展示、图片画廊、局部 SVG、滚动叙事、可选复杂动效；须取得与强度匹配的选择，不得因为库里有配方就默认安装使用。

每个效果必须说明“比直接切换更好在哪里”。如果说不出来，保留状态反馈但不加动画；若页面可从动效显著受益，应**主动提出选择而不是默认删掉**。

## Gate M3 · 共享 Motion Tokens、实现与降级

- 把 `fast / normal / deliberate`、`enter / exit / standard` 缓动及 `none / reduced / full` 偏好映射为**项目级 Motion Tokens**。此为角色名示例，不强制所有项目固定 150ms/250ms、固定贝塞尔或使用 Spring。
- 对频繁交互优先短而响应快的 easing；较大位移/品牌重要节点可以更久，但要以阅读、点击、性能和减少动效偏好实测。设计系统中区分 productive 与 expressive，而不是随意给每个 Card 添加同一种弹跳。
- 优先现有组件库内建过渡、CSS / Web Animations API / 框架原生 Transition；复杂布局/编排才引入 Motion、Anime.js 或 GSAP，并确认依赖、许可证、SSR/生命周期、触屏与低性能回退。禁止为普通 hover 安装多个大库。
- **避免“显示内容依赖动画完成”**：初始 HTML/无 JS/低配/禁用动画时，重要文字、表单、按钮、状态与出口保持可见可用；动画无权推迟业务状态提交。
- `prefers-reduced-motion: reduce` 是**独立的可访问性约束**，用户选择 C 也不能覆盖系统减少动效。运动敏感情况下禁用/简化非必要位移、缩放、视差、循环与过渡，保留即时状态反馈；需要 JS 控制的动画也监听偏好及变化并取消已在运行的效果。
- 支持快速反复切换、反向操作、取消、路由卸载、Tab 被隐藏、低端机、滚动中卸载；动画 cleanup 与事件/资源回收参照 `references/animation-integration-lifecycle.md`。
- 尊重触控、键盘和背景任务；不可让页面级 animation 覆盖 focus ring，也不可延长错误信息或确认结果到不可用状态。

## Gate M4 · 验收与证据（不能“写了 CSS 就算有动画”）

- **用户确认**：交付时说明采用哪档、选择的来源和记录原话/明确授权；不能说“你选择了 B”而用户只说“界面好看”。
- **覆盖**：逐项操作验证 Hover/Press、Tabs、Dialog、导航、加载/错误/成功与实际页面存在的交互；如选择 B/C 但关键交互没有任何过渡，需解释特殊情况或修复，不能以“性能优化”为由悄悄全站降为静态。
- **真实过渡**：浏览器在交互前、中、后取证，检查动画确有运行、未闪烁、布局稳定、可中断、焦点可达、最后一步状态正确。仅 DOM/CSS 静态扫描或截图不证明视觉体验优秀；可测场景需实际操控。
- **状态压力**：快速连点/反向切换、输入中弹窗、列表大量更新、长中文/英文、手机窄屏、浅深色、200% 放大。
- **减少动效**：浏览器 emulated reduced motion，确保非必要移动被禁用/缩减、内容仍立即可用、可聚焦与可交互。勿一刀切使用 `* {animation:none!important; transition:none!important}` 作为所有项目唯一实现。
- **性能**：测 FPS/长任务/布局抖动（能力可用时），不要宣称未测的数字；只有弱设备或时间预算无法覆盖时，明确列为未验收而非假定通过。
- **报告**：列出通过和未覆盖的组件、采用的动效与预期价值、预览证据、减少动效策略与问题；禁止从独立 Mock 冒充真实产品 E2E。

### 可核验的官方设计与无障碍资料（来源不代表照抄样式）

- IBM Carbon Motion（productive/expressive、组件与整体转场）：https://www.carbondesignsystem.com/building-blocks/foundations/motion/overview
- W3C WCAG 2.2 Understanding 2.3.3 Animation from Interactions（AAA；交互非必要动画可禁用）：https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions
- W3C C39 技术：https://www.w3.org/WAI/WCAG22/Techniques/css/C39
- MDN prefers-reduced-motion：https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion
- Material Design timing/easing principles：https://m1.material.io/motion/duration-easing.html

继续参阅 `references/animation-engine-selection.md`（技术选型）、`references/animation-integration-lifecycle.md`（清理和回退）、`references/design-discovery-interview.md`（用户选择来源）、`references/visual-qa.md`（整体视觉检查）。