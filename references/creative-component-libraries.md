# 创意交互组件资源库：React Bits / Vue Bits / Inspira UI / Magic UI / Aceternity UI

> 核对日期：2026-11-02。此文件提供**可选视觉积木**，而非必须安装的依赖表；具体版本、props、许可证、付费与依赖以组件详情页和仓库版本为准。**组件目录随官网变化，以下是精选且已核对的典型能力，不宣称穷尽全部组件。**

## 0. 先分清三个层级

- **功能性组件层（Functional UI）**：Button、Select、Dialog、Form、Table、DatePicker、Tabs、Menu 等；必须正确实现焦点、键盘、ARIA、数据与状态。优先已选定的成熟组件库 / headless primitives，禁止用特效组件代替。
- **创意视觉组件层（Creative UI）**：动态背景、文字揭示、3D 卡片、聚光灯、鼠标轨迹、滚动叙事；优先用于官网、产品介绍、作品集、专题页。可用于少数后台欢迎页/空态，但不挤占核心工作区。
- **动效引擎层（Motion Engine）**：CSS、Motion、Anime.js、GSAP、WebGL 等是驱动上述效果的底层技术，不等价于可直接放入页面的组件库；**复制的创意组件可能内部已经依赖 GSAP/OGL/Motion**，安装前盘点，禁止叠加重复引擎。

## 1. 可用库对照

| 库 | 官方入口 | 框架/形态 | 主要内容 | 特别适合 | 风险/边界 |
| --- | --- | --- | --- | --- | --- |
| **React Bits（免费部分）** | https://reactbits.dev/ | React / Next.js；复制源码或 CLI；TS/JS + CSS/Tailwind | 文字动画、动态背景、普通动效、创意组件、微交互 | 品牌 Hero、产品功能展示、作品集、视觉亮点 | 部分背景使用 WebGL、GSAP/OGL；按组件审查性能与 SSR |
| **React Bits Pro** | https://pro.reactbits.dev/ | React；商业内容和不同权益档 | 更多组件、页面区块、模板及应用 UI | 有预算且确实需要营销模块/模板 | **收费，不能将 Pro 资源当免费部分直接复制** |
| **Vue Bits** | https://vue-bits.dev/ | Vue 3 + TypeScript + Tailwind；复制 `.vue` 或 CLI | React Bits 官方 Vue 移植；文字、背景、鼠标、卡片和动画 | Vue / Nuxt 的产品官网、作品集、介绍页 | 组件可能有额外依赖、SSR/水合问题；**核对具体仓库许可证** |
| **Inspira UI** | https://inspira-ui.com/docs/ | Vue / Nuxt；可复制改造源码；常结合 shadcn-vue、motion-v 和 Tailwind | 动态背景、卡片、文字、交互、可视化 | Vue 企业官网、AI 产品展示、创意首屏 | 非基础组件库；逐项核对依赖和许可，别将其当作替代 Reka UI 的实现 |
| **Magic UI** | https://magicui.design/ | React / Next.js + Tailwind/Motion（以官方组件为准） | 动态文字、装饰背景、品牌/营销组件 | 快速制作克制的品牌动画和特色营销段落 | 项目已有基础组件不必整体改装为 shadcn |
| **Aceternity UI** | https://ui.aceternity.com/components | React / Next.js + Tailwind/Motion | 3D 卡片、Aurora、聚光灯、背景、滚动叙事、区块 | 注重冲击力的展示页与产品首屏 | 免费组件、付费 Blocks/模板分开核实；避免样式与工程边界失控 |

**框架适配红线**：React Bits 的 TSX 不能直接复制进 Vue；Vue Bits 的 SFC 也不能直接作为 React 组件。应在同框架找原生等效组件，或借鉴动效原理以本框架重实现。

## 2. React Bits：按官网分类的效果说明与使用建议

官网目录：https://reactbits.dev/；文字：https://reactbits.dev/c/text-animations；动画：https://reactbits.dev/c/animations；背景：https://reactbits.dev/c/backgrounds。组件名称是官方名称；描述为本 Skill 的选型总结。

### 2.1 文字与标题（适合品牌或产品介绍）

| 名称 | 视觉表现 | 推荐使用位置 | 禁忌 |
| --- | --- | --- | --- |
| `Split Text` | 将字词拆分后错峰入场 | 产品首屏一句短主张 | 大段正文逐字动画 |
| `Blur Text` | 文字从失焦逐步清晰 | Hero 标题、副标题入场 | 低对比正文、必须瞬时读取的提示 |
| `Text Type` | 打字与光标节奏 | 展示 CLI、产品口号片段 | 用作表单、条款、实时信息 |
| `Rotating Text` | 词句翻转轮换 | 副标题多个卖点 | 唯一的重要信息反复变动 |
| `Shiny Text` | 光泽扫过文字 | 少量品牌强调词 | 所有导航、表头、数字 |
| `Gradient Text` | 柔和渐变随时间流动 | 主视觉标题中的一句强调 | 与其他高对比背景同屏堆积 |
| `Decrypted Text` | 随机字符逐步还原 | 安全/开发工具发布营销页 | 账号、验证码、真实业务数据 |
| `Scroll Reveal` | 滚动时逐步显字/清晰 | 长篇产品故事叙事 | 影响阅读顺序或使文本不可见 |
| `Count Up` | 数值动态增长到真实值 | 有数据来源的成果指标 | 伪造增长率、未加载的真实数值 |
| `Glitch Text` | 色散与短促错位 | 技术活动、游戏主题点缀 | 普通 SaaS 主标题、频繁循环 |
| `Particle Text` | 粒子聚合为文本 | 高端宣传段落一次性揭示 | 低端机、全站每个标题 |
| `Text Pressure` | 指针附近字体产生形变 | 交互品牌标语 | 长文本和关键操作文本 |

### 2.2 背景与场景（通常最耗资源）

| 名称 | 视觉表现 | 推荐位置 | 风险/降级 |
| --- | --- | --- | --- |
| `Aurora` / `Soft Aurora` | 缓慢流动的极光色带 | 官网 Hero 背景 | 暗色/浅色对比度；静态渐变回退 |
| `Particles` | 多层漂浮粒子，指针响应 | 作品集/创新产品介绍 | 限粒子数和 DPR；移动端减弱 |
| `Waves` / `Line Waves` | 细线像织物般流动 | 品牌故事的次要背景 | 避免高频运动引起眩晕 |
| `Orb` | 发光球体柔和呼吸 | 单个功能重点/视觉中心 | 与 CTA 分离、避免遮挡文字 |
| `Liquid Chrome` | 液态金属反光与流动 | 品牌质感、科技产品展示 | GPU 性能、静态预览备用 |
| `Ballpit` | 带物理交互的立体球群 | 有趣的创意专题 | 仅独立受控展示区，移动端限制 |
| `Letter Glitch` | 字符矩阵闪烁与扰动 | 开发者工具活动背景 | 强刺激、不要放在持续办公界面 |
| `Grid Distortion` | 图片局部格栅扭曲 | 作品集图片特写 | 图片应仍可看清、移动端降级 |
| `Lightning` | 分叉闪电吸附指针 | 游戏、特定活动主题 | 强烈闪烁，默认不用于常规商业产品 |
| `Beams` / `Light Rays` | 具有体积感的光线运动 | 深色 Hero 层次 | 减少持续 GPU 消耗，弱化光污染 |
| `Grainient` | 颗粒质感的流动渐变 | 产品官网品牌背景 | 避免文本/对比度不稳定 |
| `Magic Rings` | 光环脉冲和鼠标回馈 | 单个展示模块、CTA 装饰 | 不能冒充加载进度或成功状态 |

### 2.3 卡片、导航及内容组件

| 名称 | 视觉表现 | 适用 | 注意 |
| --- | --- | --- | --- |
| `Spotlight Card` | 光斑跟随鼠标照亮卡片 | 产品特性卡片、定价亮点 | 触摸设备无 hover：保持可读静态样式 |
| `Tilted Card` | 卡片轻微 3D 倾斜与光泽 | 产品图片或特色卡片 | 限角度，不影响阅读或误触 |
| `Chroma Grid` | 灰阶卡片被局部聚光恢复色彩 | 作品/团队案例陈列 | 保留键盘聚焦与触摸可用性 |
| `Carousel` | 内容片段横向切换 | 产品特性故事 | 尊重手动控制，禁止无法暂停的自动切换 |
| `Dock` | 指针附近图标放大 | 互动作品展示、模拟桌面 | 普通网页导航不强制使用 Dock |
| `Gooey Nav` | 活跃导航指示像液体般位移 | 创意站点短导航 | 当前位置必须明确且键盘可达 |
| `Staggered Menu` | 菜单逐项错峰入场 | 品牌导航 / 手机菜单 | 不妨碍退出和键盘聚焦 |
| `Masonry` | 图片随容器变化顺畅重排 | 作品集、案例图库 | 图片尺寸和 CLS、懒加载 |
| `Glass Surface` | 类玻璃折射的半透明容器 | 少量浮层或 Hero 附属块 | 文字对比度、性能和兼容回退 |
| `Model Viewer` | 可互动产品 3D 模型 | 硬件/实体产品展示 | 提供平面图、加载/失败态和操作说明 |

### 2.4 通用动效和微交互

`Animated Content`（滚动揭示、模糊与位移）、`Fade Content`（滚动淡入）、`Electric Border`（电流边框）、`Pixel Swap`（逐像素切换）、`Cursor Grid`（指针轨迹栅格）等在官网 `/c/animations` 浏览。**多数属于 B/C 级动效**：需要与用户任务相关，不能作为每张功能卡片的默认动画。

## 3. Vue 的同类替代与对应关系

### Vue Bits（官方 Vue 移植）

官网：https://vue-bits.dev/；安装：https://vue-bits.dev/get-started/installation；项目：https://github.com/DavidHDev/vue-bits 。官方文档说明：Vue 3 + TypeScript + Tailwind，每项源代码可独立复制或 CLI 安装，依赖在对应组件详情页列出；某些组件使用 GSAP/OGL。

| 产品体验需求 | React 参考 | Vue 优先路线 |
| --- | --- | --- |
| Hero 文案错峰出现 | React Bits `Split Text` | Vue Bits `Split Text`（核实具体 props） |
| 光感/渐变标题 | React Bits `Shiny Text`, `Gradient Text` | Vue Bits 相应文字组件或 `motion-v` + CSS |
| 背景极光 | React Bits `Aurora` | Vue Bits `Aurora` 或 Inspira UI 极光类组件 |
| 产品卡片指针光照 | React Bits `Spotlight Card` | Vue Bits 同类卡片、Inspira UI 卡片或 Vue 原生实现 |
| WebGL 粒子/液态 | React Bits `Particles` / `Liquid Chrome` | Vue Bits 同类背景（检查对应组件可用性） |
| 滚动入场 | React Bits `Animated Content` | Vue `<Transition>` + IntersectionObserver / `motion-v` |
| 文字折页入场 | React Bits `Fold Text` | Vue Bits `Fold Text`（官方存在独立文档） |
| 3D 与复杂时间轴 | React Bits 某些 OGL/GSAP 组件 | Vue Bits/OGL/GSAP + `onMounted/onUnmounted` 清理 |

**注意**：此表是**功能对照**，不是组件 API 一比一对应。导入、props、CLI registry URL 应从每个对应详情页复制，禁止“凭 React 代码猜 Vue props”。

### Inspira UI（独立 Vue 创意组件路线）

官网：https://inspira-ui.com/docs/；快速开始：https://inspira-ui.com/docs/en/getting-started 。官网列出 Backgrounds、Cards、Interactions、Text effects、Visualizations，整体基于 Vue/Nuxt；项目常使用 shadcn-vue、motion-v、TailwindCSS。适用于企业官网、创意 Hero、AI SaaS 宣传页和作品集。优先复制**单个**有用组件并纳入自有主题，而不是把整个产品视觉交给组件自带样式。

### React 工程中的另外两套候选

- **Magic UI**（https://magicui.design/）：更偏 shadcn + Motion 生态的精致营销交互；适合文字、网格、光线、展示小组件；通常优先于自写复杂造型。
- **Aceternity UI**（https://ui.aceternity.com/components）：3D Card Effect、Background Beams、Tracing Beam、Hero Parallax、Apple Cards Carousel、Animated Testimonials、Aurora Background 等；适合高冲击营销专题，常有免费组件与付费区块/模板之分。

## 4. 应用场景组合（控制数量，而不是追求组件越多越好）

| 页面类型 | 推荐创意层 | 核心不可缺少 | 反面做法 |
| --- | --- | --- | --- |
| 企业官网首页 | 柔和极光背景 + 一次标题入场 | 价值主张、服务内容、真实联系方式/CTA | 首屏 4 个 WebGL 场景同时运行 |
| SaaS 产品落地页 | 分段滚动揭示 + 产品卡片聚光 | 功能、定价/试用、功能截图、可信说明 | 用炫酷动效取代真实产品演示 |
| 开发者工具官网 | 代码打字演示 + 产品界面变化 | 文档入口、安装方式、平台支持 | 一直打字导致用户看不到命令 |
| 品牌作品集 | 图片 Masonry + 微弱 3D 倾斜 | 作品可筛选、详情可达、图片优化 | 鼠标特效遮挡真实作品 |
| 招聘/公司介绍 | 团队介绍柔和浮入 | 职位、文化、地点、应聘路径 | 全页大量滚动锁定与强迫播放 |
| 仪表盘/后台操作页 | 状态反馈、列表进入、轻量布局过渡 | 复杂表格、快捷搜索、真实操作状态 | 放粒子背景影响长时间使用 |
| 后台首次引导/空状态 | 简短 Lottie/创意卡片（可选） | 清楚说明下一步操作 | 动效无法关闭或错误时不显示内容 |

## 5. 按性能与无障碍强制验收

1. **默认静态内容可读**：JS/CDN/动画初始化失败时，Hero、CTA、导航、数据与正文仍可见；内容不能永久设为 `opacity:0`。
2. **减少动态效果**：监听 `prefers-reduced-motion: reduce`；取消滚动跟随、光晕、眩晕性 3D、跟随鼠标，显示静态图/静态渐变。
3. **按需加载**：创意组件分页面、分路由、分区块按需加载，尽可能不进入后台核心 bundle；WebGL/模型需有加载图与失败回退。
4. **低端机**：控制 DPR、粒子数量、canvas 总数；检测卡顿后减速或静止；切换后台和页面不可见时停止 `requestAnimationFrame`。
5. **移动/触摸**：不依赖 hover；支持无 hover 的 CTA；滚动不被劫持；Canvas 不截断关键触摸操作。
6. **受控生命周期**：React 在 effect cleanup 释放监听、实例与 WebGL；Vue 在 `onUnmounted` 释放。Next/Nuxt SSR 只在客户端创建访问 DOM 的实例。
7. **语义/键盘**：效果包裹不能破坏原本的 `<a>` / `<button>`；自定义 3D 卡片依旧有 focus-visible 和可点击区域。
8. **用户控制**：自动轮播可暂停；单次入场不反复打断阅读；动画不改变真正的业务含义。
9. **许可证**：检查选用组件的许可证、字体、图片与付费授权；项目官网“免费可用”并不等于**全部组件/模板和任意商业分发条件相同**。
10. **可测试证据**：页面上有哪些效果、实际安装了哪些库、performance 检测、窄屏/无障碍/SSR 结果、尚未验证事项。

## 6. 选型打分卡（每项 0~2 分，至少 8 分才考虑引入）

- 用户任务价值：是否帮助理解功能、定位和层次？
- 品牌契合：视觉语言是否与已有 Tokens、字体、配色一致？
- 性能与体积：仅此页面按需加载，低端设备/慢网络可接受？
- 可访问：鼠标以外的输入方式可用，支持 reduced motion？
- 可维护：已有组件/引擎不能更简单完成？组件源码与依赖可维护？

一票否决：授权不清、破坏重要内容可见性、阻塞核心交互、劫持滚动、未提供可访问回退、明显帧率问题、在已有产品中引入第二套独立组件基础样式造成割裂。

## 官方引用索引

- React Bits: https://reactbits.dev/ · https://reactbits.dev/get-started/installation · https://reactbits.dev/c/text-animations · https://reactbits.dev/c/backgrounds · https://reactbits.dev/c/animations
- Vue Bits: https://vue-bits.dev/ · https://vue-bits.dev/get-started/installation · https://github.com/DavidHDev/vue-bits
- Inspira UI: https://inspira-ui.com/docs/ · https://inspira-ui.com/docs/en/getting-started
- Magic UI: https://magicui.design/
- Aceternity UI: https://ui.aceternity.com/components
