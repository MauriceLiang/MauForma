> v4 范围提示：本 Skill 以 Web 前端为直接适用对象。旧版本个别原生 SwiftUI/AppKit 条目仅供设计语义迁移参考，不用于要求安装或生成原生 UI 源码。

# MauForma · 视觉语言规范 v2.0

> 原站提供了设计品质的基准，而不是唯一色卡。配色机制见 [theme-design.md](theme-design.md)，本篇关注颜色以外的系统级规范。

## A. 风格的共性

- 低噪声背景，明确而柔和的表面层级。
- 通过字号、行高、字重、空间关系组织信息，而非堆积图标、分割线和色块。
- 有规则的圆角与低强度阴影，组件不会因为“可爱”而失去专业性。
- 动效是动作与结果之间的反馈，不是强制的装饰性表演。
- 细节精确且可复用，跨屏幕可延续同一设计语言。

## B. Design Token 架构

组件**只使用语义变量**，页面布局可以引用空间 scale：

| 类型 | 角色 | 反模式 |
| --- | --- | --- |
| 背景 | `--spui-page-bg`, `--spui-surface`, `--spui-surface-soft` | 每页手写新的 `#f6f6f8` |
| 文字 | `--spui-text`, `--spui-text-soft`, `--spui-text-muted` | 通过 `opacity:.25` 模拟辅助信息 |
| 动作 | `--spui-accent`, `--spui-on-accent`, `--spui-focus` | 把主题色和错误色混为一谈 |
| 结构 | `--spui-border`, `--spui-control-border` | 输入边界只有极淡灰且无法辨认 |
| 状态 | `--spui-success`, `--spui-warning`, `--spui-danger` | 图标和操作状态都随品牌色改变 |
| 圆角 | `--spui-radius-panel/inner/control/button/dialog` | 不可控的 9/12/14/19px 随机值 |
| 密度 | `--spui-grid-gap`, `--spui-panel-pad-x/y`, `--spui-control-height` | 页面之间的间距没有共用规则 |
| 动效 | `--spui-motion-ui`, `--spui-motion-entry` | 每个页面随机 130/260/420ms |

## C. 密度模式

| 特性 | `showcase` 展示型 | `desktop` 生产力型 |
| --- | --- | --- |
| 大容器圆角 | 32px | 16px |
| 内部卡片圆角 | 18px | 10px |
| 输入控件圆角 | 16px | 8px |
| 按钮圆角 | 999px | 8px |
| 弹窗圆角 | 24px | 14px |
| 内容最大宽度 | 980px | 1200px（依工作区分栏调整） |
| 面板内边距 | 24px 28px | 14px 16px |
| 栅格间距 | 18px | 12px |
| 控件目标高度 | 44px | 36px（按平台可访问性要求调整） |
| 常规 UI 动效 | 200ms | 160ms |

这是跨项目的推荐值，不是“原站全部数值”。原站展示标题、容器、圆角与动画精确来源见 [source-analysis.md](source-analysis.md)。

## D. 字体排印

**优先使用平台原生字体栈，不随意打包受限字体**：`-apple-system`, `BlinkMacSystemFont`, `SF Pro Text`, `PingFang SC`, `Microsoft YaHei`, `sans-serif`。

- 展示型大标题可用 `clamp(56px,10vw,96px)`、600 字重、`1.04` 行高和适量负字距；中文密集笔画尤其要审查负字距是否影响清晰度。
- 工作台推荐页面标题约 22–30px、分区标题 16–20px、主要正文 14–16px；图表刻度、KPI 标签、重要元数据建议 12–14px 起步并保证对比，具体参照 [字体层级](typography-hierarchy.md)。这些是设计建议，不是 WCAG 强制字号，需在实际屏幕上确认。
- 正文行高通常 1.45–1.65；一行字太宽会增加阅读成本。长正文可加 `max-width` 而不是强行把字号缩小。
- 字体级差、字重、间距都来自统一 scale，不能每个模块自己决定标题样式。
- 重要信息的强调色应来自主题，**标题默认使用高对比实色**；渐变标题是可选强调工具。

## E. 形状与空间

- 原则：父容器更大、子容器更小，保持肉眼可见的内边距。
- 大幅度卡片圆角适合展示页；开发者工具中更小圆角和清楚的分栏更高效。
- 建议以 4px 为间距基元，常用 4/8/12/16/24/32/40，但必须在同一层级统一。
- 留白区分“紧密关联”“一般关联”“独立章节”，绝对不要只用同一个 gap 填充全站。
- 非必要不使用装饰性分隔线；有内容层次时优先靠空间关系分组。
- 表格和列表使用微色差、行高、对齐线组织信息，而不是每条数据一张大卡片。

## F. 阴影与表面

- 展示型源站：`3px 5px 30px rgba(0,0,0,.08)`，非常柔和。
- 桌面型建议：`0 2px 12px rgba(0,0,0,.055)`，可根据暗色/原生平台弱化，优先小边框/色差。
- 浮层应比普通面板更明确，但不应靠纯黑大阴影吓人。
- 玻璃拟态、大面积模糊、霓虹外发光、持续背景动画属于例外，不是默认品质指标。

## G. 组件统一

- Button：primary / secondary / ghost / danger 表达意图，焦点和禁用可辨认。
- Field：label / hint / error / disabled / required 结构固定。
- Panel：仅当信息形成独立块时使用，避免“卡片套卡片套卡片”。
- Status：一套语义色和文案机制，主题变色不改变错误的含义。
- Nav：导航状态除色差之外还要有易识别的焦点/选中形式；**当前路由与键盘焦点是不同状态**。工作台选中项默认用柔和底色 + 文字/图标权重，不额外默认叠加发光竖条；树形层级/时间轴指示线有独立语义时可保留。详见 [侧栏规范](sidebar-navigation-design.md)。
- Dialog：遵守原生或可访问原语，内容/按钮间距统一，避免过大弹窗。

**严格顺序**：组件清单 → tokens → 组件实现与状态 gallery → 业务页面。详细 API 与例子见 [component-first.md](component-first.md)。

## H. 自适应与平台

- 网站和小屏：布局要重排，不能只缩小字号。正文不被裁切，表单按钮不遮挡。
- 桌面：支持窄窗口、侧边栏和多面板，避免把小窗口强行塞入宽屏展示布局。
- SwiftUI/AppKit：优先平台动态色、动态字体、可访问性和系统原生行为，颜色 token 映射即可。
- 常规动画需支持系统 Reduce Motion；对快速重复操作不采用夸张回弹。

## I. 高频工作台组件的精修门槛（v6.3）

在执行 Gate B / 组件状态 Gallery 时，额外检查 [高频组件设计](workspace-component-refinement.md) 的七种模式：功能导航和对象列表不能共用一种强激活视觉；色彩使用统一中性色阶和状态角色，不能无意义地堆叠亮条、彩点、渐变、发光与卡片。实例颜色见 `../assets/sidebar-palette-examples.json`，并在真实浅/深模式截图中评估。此处是桌面工作台默认规则，不替代营销与实验性产品的 Art Direction。

## J. v6.5 · 文案必要性与可读字级

组件不自动给每个标题加 eyebrow、英语副标、伪章节编号或抽象口号。先运行 [文案必要性审查](semantic-copy-hygiene.md)，确认每行可见文案的独立信息价值；再按 [字体层级](typography-hierarchy.md) 与 `assets/typography-role-guidelines.json` 为 PageTitle、Section、Body、Metric、ChartAxis、ChartLegend、Metadata 等角色建立可调整的共享字号。重要数据即使“次级”也要看得清楚。真实工作台截图须检查暗色对比、200% 放大和长中文/英文字段；品牌展示页可拥有不同的字级及强烈艺术构图。

## K. v6.6 · 用户批准、全局协调的导航色彩

对新设计/配色大改，先读取已有品牌与页面全局颜色。用户明确指定色彩/HEX 优先；不明确时，参考官方设计来源后提出 2–3 套**侧栏+主区+顶栏+卡片+数据图**的完整组合供用户选择，不由 Agent 偷偷决定。侧栏可以有独立 tokens，但只能从项目 MASTER 派生，不能作为不同于主内容的独立品牌系统。批准后记录用户原话、来源与精确色值，若需变更已确认品牌色必须取得新许可。

规范：`references/sidebar-color-discovery.md`、`assets/sidebar-color-decision.schema.json`；预览：`assets/sidebar-color-preview.html`；数值对比工具：`scripts/validate_sidebar_color_decision.py`。若工具通过，仅表示所列颜色对有足够数值对比，不代表整页协调性或截图已通过。

## L. v6.8 · MASTER 共用语言，页面密度由真实任务决定

全局保存共用间距尺度、Typography 角色、颜色语义和组件契约；`overview`、`analysis`、`operations` 的内容量、空间组织与容器策略属于 Page Override。见 `references/page-density-and-content-priority.md`：airy/balanced/productive/compact 是可调起点，不应自动将整站渲染为同一套密集卡片。空间应反映分组而非设定空白比例；先删重复模块再使用 `references/whitespace-and-surface-composition.md` 的 macro/meso/micro 规则。用户已定配色/导航/密度不因优化内容被擅自改动。

## M. v6.9 · 网格语义和滚动安全的共享契约

MASTER 中保留 Grid tracks、gutter、页面最大宽度、page-end spacing 与必要的 bottom-bar height/safe-area 语义 Token；各路由在 Page Override 中声明需要的 `shared-row-grid / main-feature-span / editorial-asymmetry` 模式，按任务决定列比例，不强迫统一等高。数据页同级卡片共享行起点；布局变化时更改网格契约而不是零散给 Card 加 margin-top。App Shell 指定唯一可识别的主滚动容器；可滚到底且固定栏不遮挡最后一条记录，按目标浏览器复测。参见 `references/grid-alignment-and-viewport-safety.md`。
