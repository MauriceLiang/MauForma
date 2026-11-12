# Page Density & Content Curation · 先筛信息，再设计留白（v6.8）

**触发：** 新站、新增主要页面、首页/总览重构、用户抱怨“卡片太多、信息过满、留白没层次”。对局部修复或已确认的页面不强制再次访谈。

## 核心区别：产品有很多功能 ≠ 这个页面要展示全部功能

同一 Web 产品的 **总览、引导、详情分析、管理、设置、编辑** 可以使用不同内容密度。共享品牌、组件、字级语义和空间 Token，但页面优先级、内容总量、留白及容器呈现按**当前任务**决定。

不要用“更高级”直接定义某一套固定尺寸、百分比留白、最多三卡或卡片宽度。需要判断**少展示哪些内容、为何留下哪些内容**。真实数据、警告、用户已明确要求的信息不能为了留白被隐瞒。

## Gate P0 · 先做 Content Inventory（真实内容盘点）

对当前路由整理页面可见区块、文字、动作与导航：它们是 `critical`（完成主任务必须）、`supporting`（常见但次要）还是 `optional`（偶尔用/有明确二级入口）？分清真实性（真实/Mock/截图可见/未知）、用户状态（新用户/回访、有数据/无数据，加载/错误）和出现条件。**不能只看页面组件列表推断哪个内容有用**：还要参考用户任务和产品流程。

每一块内容必须给出 **placement decision**：
- `primary`：页面第一视线与当前主任务直接相关，例如总览的“选择仓库”、真实分析的趋势或主要筛选。
- `supporting`：确有增量，但不争抢主角，可做紧凑行、文本链接、局部信息。
- `conditional`：只在指定用户状态出现。例如新用户尚无仓库才显示“如何开始”，失败时显示重试，数据缺失时显示空状态。
- `deferred`：放入可发现的“帮助”、详情页、二级操作或展开区域；`accessible_via` 必须明确，不得“为了干净”让功能消失。
- `removed`：无信息增量/导航已直接覆盖/重复描述；需要具体的冗余依据。不可删除必须显示的权限警告、真实数据来源或用户明确指示保留项。

**先做删除测试，再进入布局**：删除某容器后的页面是否更快完成当前任务？如果是且没有损失必要信息，整块下沉或移除，不是换一种更精美的卡片继续占空间。

## Gate P1 · 根据页面而不是根据产品统一设密度

| 页面 | 优先任务 | 推荐起点 | 允许主要内容 | 应主动下沉 |
| --- | --- | --- | --- | --- |
| **Overview / 总览 / 欢迎** | 识别当前状态，找到下一步动作 | `airy` 或 `balanced` | 清楚标题、状态/对象、一个清晰主要操作；必要时简要摘要 | 完整新手教程、功能目录、重复入口、长篇产品说明 |
| **Onboarding / 初次引导** | 只完成眼前第一步 | `airy` 或 `balanced` | 当前一步的必要说明、输入/选择、明确继续/返回 | 同时展开三步长教程及所有高级设置 |
| **Analysis / 数据详情** | 对比证据、筛选、形成判断 | `productive`，复杂时 `compact` | 指标、趋势、图例、来源、筛选和真实状态 | 营销宣言、过多说明/无用大 Hero |
| **Operations / 管理与批处理** | 扫描、编辑、操作 | `productive` 或由用户确定的 `compact` | 表格、查询、筛选、必要状态、批处理工具 | 无用图标卡与过度外层容器 |
| **Marketing / 品牌内容** | 传达品牌、产品与可信信息 | `airy`，视转化任务可 `balanced` | 商品/食品影像、主张、行动入口、证据 | 技术参数长表（可下沉），重复同义卖点 |
| **Reading / 文章与知识** | 连续阅读与理解 | `balanced`（可提供阅读密度选择） | 正文与信息型图、目录按需 | 持久无意义的侧边占位、截断正文的卡片 |

**密度是页面级、可受用户偏好影响的决策**，不是“数据页所有字体都缩小”或“Overview 只剩空白”。`airy` 的文本也必须容易读；`compact` 的表格仍需足够行高、键盘和触摸可用性。

## Gate P2 · 内容呈现与第一视线

确定每页一个`primary_task`，优先检查：
1. 进入页面看到的是什么？能在适合当前用户状态时快速找到下一步吗？
2. 页面是否同时展示相同目的的**介绍卡、步骤卡、功能目录、导航入口、底部重复入口**？保留真正有效的那个。
3. 首屏主要面积是内容/主操作还是卡片边框、空话、重复图标、装饰留白？
4. 是否区分 `first_visit` 与 `returning`：新用户的快速引导不可成为回访用户永远驻留的教程。
5. 页面一旦有数据，是否从 onboarding 自然切换到数据概要/近期任务？不要再强迫用户读使用说明。
6. 用户可能需要的“其他功能”是否可以通过已有导航访问？已经在侧栏的三个分析功能不需要每个都再次做大卡片。

总览“先展示最重要操作和内容”，不代表强制只有一个按钮：仍可保留帮助/查看样例的次级行动，但它们的视觉权重应不同且有业务理由。

## Gate P3 · Macro / Meso / Micro 空间层级

具体留白与容器规范见 `references/whitespace-and-surface-composition.md`：空间应表达语义而不是撑高度。首页允许较大的**模块间**留白，组件内部应更紧凑且对齐；相邻有关信息更靠近。容器只在有必要表明“可交互/独立表面/状态边界”时使用。避免“页面大底卡 → 内部说明卡 → 三个步骤卡 → 末尾功能卡”的套娃结构。

## Gate P4 · 动态信息与分阶段披露

- `first_visit`：只介绍当前需要的启动步骤；可见帮助入口进入详细教程；
- `returning`：显示用户继续工作的对象、最近状态/任务，避免全量重复 onboarding；
- `data_available`：详情分析页优先真实趋势/表格与过滤；按语义附上数据覆盖范围/误差；
- `empty` / `error`：必要说明和下一步操作优先，不能仅为了留白隐藏错误或虚构数据。

把信息移入可发现的明细路由、帮助或展开项，并确保用户能返回当前上下文。隐藏不是删除功能。切换页面状态不应清空已选仓库、筛选条件或未保存内容。

## Gate P5 · 截图复盘：先内容，后美术

审查顺序：`content relevance → primary action → duplicate sections → card necessity → spacing hierarchy → typography → color → responsive`。若信息架构失败，先下沉/删除区域再调 padding 和色板。

全页桌面/手机截图按 `overview` 与 `analysis` **分别判定**，不能用工作台统一密度门槛把首页做得同样密集，也不能把分析页压成只有一个大标题和空白。

执行 `python3 scripts/validate_page_content_plan.py examples/page-content-plan-demo.json --repository` 可检查必要字段、信息分层、用户状态、披露入口与页面密度分配；**通过不等于视觉美感、实际业务功能或 WCAG 验收。**

### 外部设计依据（方法论，不是固定色板与比例）

- [IBM Carbon · Spacing](https://www.carbondesignsystem.com/building-blocks/foundations/spacing/overview)：利用不同尺度间距标示内容关系、层级；页面允许密集区域但整体不应拥堵。
- [IBM Carbon · Productive & expressive typography](https://www.carbondesignsystem.com/building-blocks/foundations/typography/style-strategies)：高效操作与表达性品牌页面在排版目的和密度上不同。
- [Nielsen Norman Group · Progressive Disclosure](https://www.nngroup.com/articles/progressive-disclosure/)：优先展示核心功能，次要内容清楚披露；必须保证用户找得到隐藏内容。
- [GitLab Pajamas · Progressive Disclosure](https://design.gitlab.com/patterns/progressive-disclosure/)：把次要信息转入可发现的二级交互，而不是一次性塞进首屏。
- [Atlassian · Compact density](https://community.atlassian.com/forums/discussion/3189883/new-feature-compact-mode-and-max-width-to-support-information-dense-documentation)：实际产品允许页级紧凑密度设置，不要求全站使用一套密度。

## 密度与对齐、底部安全的关系

高密度数据页不等于两列数据卡片允许无意义独立错列。先做 v6.8 内容删减，再依据 `references/grid-alignment-and-viewport-safety.md` 的共享行/列契约组合相关模块。对于超过当前浏览器高度的真实记录，应允许自然滚动，而非为保持“单屏高级感”截断图表、压缩 Release 或隐藏坐标轴。首屏外的内容不是溢出缺陷；滑不到最后一条记录才需要修复。

## Compare 属于独立的页面任务

比较页通常先让用户知道“比谁、比什么、数据是否可比、差异在哪里”。不应因 Operate 角色就把每张可生成的图表都铺上去。对于典型的多对象分析页面，列表中已选对象可用紧凑可编辑条显示；主要差异与一个共同时序图应比长期的大筛选侧栏/空心口径卡更重要。指标表按对象列和属性行组织；数据不足时不得编造赢家。读 `references/comparison-page-design.md`。

## 任务监控页不等于普通数据概览

后台任务列表的核心目的不是“展示一共多少条任务”，而是让用户快速知道正在执行什么、哪些失败/排队、如何恢复与查看日志。状态统计可以成为顶部紧凑筛选入口，但**不默认要左边一张占半屏高度的大卡片**。任务列表用可扫描的列组织 ID、对象、状态、进度/阶段、更新时间与操作，详情/日志按需打开。不要在每一行重复“进度百分比未知”：进度 null 时展示真实阶段，无可确认分母就不算百分比。人工待办/多阶段作业各有特定 UI。参见 `references/task-center-run-monitor-design.md`。
