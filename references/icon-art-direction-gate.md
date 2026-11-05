# Icon Art Direction & Semantic Fit Gate · 图标必须“选得对、看着好、搭得上”（v6.17）

适用于所有 Web 站点/应用（Operate / Persuade / Read / Experience），Vue、React、HTML 等均有效。**Icon 不是“根据菜单名从一个库中随机挑一个词”，也不是 CSS 统一 24px 后就有视觉质量。** 先判断是否需要，再决定视觉符号和图标体系，最后确认尺寸/轮廓/色彩/状态、浏览器真实渲染。

## Gate I0 · 先确认“为什么要有图标”

每个重要导航、操作或状态中的 icon 必须有明确目的：

- **Findability**：熟悉图形辅助用户快速扫描与定位目标；
- **Affordance**：帮助表达可执行动作（搜索、下载、过滤等）；
- **Domain identity**：表达产品或物件类别，具有领域共识；
- **Brand / illustrative**：大型营销图形/产品插图属于不同图形层级，不当作 16–24px UI icon。

如果概念抽象（例如“提升效能”“智慧协作”“模型洞察”），不能凭空创作“脑袋+闪电+连线”凑图标；**优先可辨认的常见符号，无法清晰表达时可只用文字**。用户提供的品牌 Logo、第三方商标与通用 UI 图标独立管理，不用 outline 库图标冒充品牌标识。

## Gate I1 · 语义优先，候选是真实可选的资源

对一级导航、高频按钮、危险操作、核心状态，要在实现前比较 **至少两个真实存在、语义可解释** 的图标候选（有明确成熟既有设计时可继承，不强行更换）。记录：

`interface label → intended object/action → candidate names + library + verified source → chosen symbol → why easier to recognize → rejected alternative and reason`。

例如“项目比较”若表达两个对象间横向对照，`arrow-left-right` 可能比复杂 Git 分叉节点更直观；但**如果实际功能是 Git 分支比较，git-compare 反而可能更准确**。同理“研究分析”可以指散点统计、实验室实验或文档研究，图标选择需以真实任务为准，不机械统一用烧瓶。不要从英文词典的第一个图标命名直接推断语义。

检索时确认 icon 名称在**当前使用的包版本**真实存在；示意候选不是安装/导入契约。要防止:
- 代码导入一个拼错/旧版本别名的图标，运行时渲染空白；
- 相邻两个不同功能使用相同符号造成导航辨识冲突；
- 设计/代码使用未审核的 Emoji、Unicode 文字装饰、随机 AI 自绘 SVG 代替成熟图形；
- 因为“每行都要带 icon”而为说明/普通状态加噪音；宁可无 icon，也别用错 icon；
- 删除、保存等高风险动作单凭图标暗示而没有明确的文字或 accessible name。

## Gate I2 · 选整套 Icon Family 的视觉语言（先看同屏，再看单个）

**视觉统一的判断对象是一组 6–12 个真实图标，不是一个孤立 icon 的精致截图。**

优先从项目已有**一个主 UI 图标家族**出发：如 Lucide（克制线条）、Tabler Icons（轮廓/专业感）、Phosphor（可选权重/更柔和）、Heroicons、Remix Icon、Carbon Icons 等。逐个对比：
- 线条 weight、fill/stroke、端点/转角、曲线语言；
- 图形复杂度、负空间、光学居中、轮廓辨识度；
- 与产品排版（CJK/拉丁）、色彩与密度的契合；
- 项目依赖/版本、框架包、Tree Shaking、许可证、可维护性。

**主家族原则**：同一个导航/同级控制组不得混用线描、双色、实心 3D、图标字体等不相关风格；品牌 Logo、数据语义符号、插画或产品既有图形属于可以记录的例外。允许同一套具有官方配套的 outline/filled 状态变体，但需验证 selected 的光学重量不会突然变大、变形或“闪跳”。不为追求风格统一硬选一个语义错误的图标：可有受控的替代家族、经过系统化绘制的自定义图标，或干脆去掉图标。

可比的正式来源：
- Lucide icon selection & design: https://lucide.dev/guide/lucide/icon-guide 和 https://lucide.dev/icons/
- Tabler design specification: https://docs.tabler.io/icons/design-guide
- Phosphor: https://phosphoricons.com/
- IBM Carbon UI Icon Guidelines: https://www.carbondesignsystem.com/building-blocks/foundations/icons/guidelines

不要从未知随机网站复制 SVG；第三方图标必须核对原始许可证并按规定保留声明。不要为六个静态导航图标引入一整套巨大图标字体（按需 SVG/组件）。

## Gate I3 · 光学精度（icon 与字体是组合设计）

统一 `IconBox` 及语义 tokens（例如 `icon.navigation`、`icon.inline`、`icon.dense-action`、`icon.hero-symbol`）；**尺寸是场景角色，而非全站一个神奇 px**。

- 统一视觉盒子、stroke/fill 模式、对齐基准，避免同一列表某个图标又粗又密另一个只有一条线；
- 同一组 icon 与标签比例协调、共同居中（必要时光学微调，不靠负 margin 修错位）；测试 CJK 与英文文本、混合字体、数值 Badge；
- 16/20/24px 等只是常见评估档位，不是强制统一；在实际渲染目标尺寸下看清图形细节、留白与主体面积；过密图标应换更简洁的候选，而不总是缩小 stroke；
- `stroke-width:2` 是某些图标库源设计，**不是所有库都必须修改为 2px**。不能粗暴用全局 CSS 把 Phosphor、Lucide 和实心 Logo 拉成同一个描边；
- 图标/标签、图标/Badge、Active 背景、focus-visible、hover、disabled、深浅色、系统缩放后都应保持视觉稳定；图标不能因 flex-shrink 被压成椭圆或被裁切；
- 交互动画只使用已获用户同意的动效强度；尽量把过渡施加到可交互容器/状态，不默认让所有图标旋转、弹跳或替换导致辨识中断。
- 装饰性图标与可见标签同义时可 `aria-hidden=true`；无可见文案的按钮必须有完整可访问名称和可触达点击区（遵循目标平台/组件规范）。不要把 icon 属性自动视为无障碍语义。

## Gate I4 · Icon Shortlist Showcase & 真实视觉验收（Gate A / B / D）

**Gate A**（设计前）：审已有系统与第三方库 → 定产品图标语言 → 为主要真实功能列出至少两个语义候选并核实包中存在、从整组里选择；用户已确定图标风格/品牌规范时继承，不能无故替换。对于新设计/有显著观感差异的全站 icon 方案，可在风格确认阶段展示 2–3 套整体对照供用户选择，不要逐个按钮发问或仅靠偏好问卷。

**Gate B**（实现）：创建一个可复用 Icon 组件/注册表，在同一示例页放出真实大小的一级导航、图标按钮、状态/空态和混排图标；比较整体形态。确保引用的名字、包版本、许可、字级、字号与语义映射可信。不要复制每个 SVG 再手工改出不同画风。

**Gate D**（浏览器）：实测渲染真实大小（如小 16 / 标准 20 / 仅在必要时 24）、CJK/英文、选中/hover/focus/disabled、深浅色与缩放；**检查空白图标、画布不符、裁切、压缩变形、基线错位、重量悬殊、不同风格混用**。若内容是抽象概念做可用性快速识别测试：遮住标签，能辨识是加分；遮住标签仍不懂，不能在只图标模式依赖它。视觉优劣必须看整组截图/适当的人类评审，不能用数学分数判“好看”。

- 可机读方案 `assets/icon-curation-patterns.json` 与 `python3 scripts/validate_icon_curation.py --repository` 检查映射、候选存在验证标记与家族原则；
- 真实 SVG 实验 `assets/icon-art-direction-lab.html`、浏览器回归 `tests/icon_art_direction_browser_smoke.mjs` 验证示例正常渲染/比例/状态/不合理混搭可检测；
- `scripts/audit_icon_consistency.mjs` 对显式 `data-mf-icon-group` 和 `data-mf-ui-icon` 组件做几何与样式检查：**只能指出尺寸/家族/缺失/拉伸等技术风险**，不会自动替人判断语义/审美。未标记的用户项目不得声称已审计。

原有 Gate 关系：`references/perceptual-hierarchy-gate.md`（文本主次）、`references/component-craft-gate.md`（组件表现）、`references/control-geometry-gate.md`（按钮宽度）、`references/visual-qa.md`（整页 QA）以及 `references/motion-consent-experience-gate.md`（动效决定权）。

## 设计缺陷范例（示例只讲风险，不把任何图标宣告“天生丑”）

- 同样是 20px 的图标，一项路径密集、一项是简单闭合轮廓：视觉重量与细节反差大，**先换更合适的图标候选**；
- 导航某一个 icon 突然切换为 filled/emoji，视觉系统断裂；品牌标识不在此限；
- “项目比较”用 Git 网络拓扑但功能只是两个项目的数据对比，用户误认成版本控制操作；不要凭功能名“项目”就匹配 Git；
- “研究分析”使用实验烧瓶，但页面实际上全是图表统计。可以更准确地尝试 Chart/Scatter；真正的实验管理反之可用 Flask；
- 空态/普通文案每个标签都加图标，制造噪音；真正的状态信息也不能只靠图标传递。

**本 Skill 提供决策流程、实例与技术检查，绝不强制所有产品使用 Lucide、全部 20px、全部 Outline，或只允许一种艺术风格。**