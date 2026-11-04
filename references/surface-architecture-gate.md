# Surface Architecture Gate · 先决定是否需要容器，再决定它的外观

适用所有 Web 网站及应用（Operate / Persuade / Read / Experience）。**大圆角框、没有区分层级的多层卡片、到处是边框**是常见机械式生成结果，但“去 AI 味”并不等于删除所有 Card。表面结构应由内容实体、任务边界、对比需求、交互/状态独立性与艺术方向决定；不能从页面模板逆推业务。

## 1. Gate A：Surface Decision Tree（先选形态，后画框）

1. **这些内容是否是同一个可连续扫描或比较的集合？** 若是记录、订单、流水、成员、课程目录、任务等同类条目，优先评估 **open collection / flat table / list**：页头、工具条、表头、行分隔，必要时仅一层轻边界。列表中的每行不是天生一张 Card。
2. **是否存在独立的交互、状态、数据范围或需要视觉隔离的复杂模块？** 若是，可使用 **bounded panel**，但同一表面内的每个标题/筛选/表格不必再套 Card；只保留能解释分组关系的边界。
3. **每个条目是否以独立对象为主，包含异质媒体、图像/商品或独立行动？** 若是可使用 **entity cards / gallery**；允许品牌化图片大卡、不同尺寸/不对称。
4. **是否是长篇阅读或连续叙事？** 优先评估 **open editorial flow**，以行宽、章节节奏、标题、引用组织，不机械用 Card 包每段。
5. **是否是专业工具多区域协作（编辑器/IDE/复杂配置）？** 可采用 **split panes / grouped work areas**；隔断与信息层级优先于漂浮面板。
6. **是否是创意体验/营销主视觉？** 可使用 **hero stage / immersive canvas**；大 Surface 可能是设计主角，但不能覆盖必要操作与内容。

以上是候选，不是自动选项。记录至少一个**被拒绝的合理替代方案及原因**（例如“拒绝全页大卡：过滤工具栏和表格同属一个连续集合、外框无新增语义”）；小范围修复不要求多方案设计汇报。

## 2. 用 Surface Value Test 防止“画框即设计”

对主容器逐个问：

- **范围**：它包围的是独立任务/对象/状态，还是仅把页面全部内容圈起来？
- **区分**：移除外框后能否仍由标题、列、行分隔、背景、间距辨别关系？若能，优先降低或移除表面层。
- **层次**：是否出现 Page background → mega card → toolbar card → list card → row card 等同语义包裹？重叠的外观层级应合并。
- **密度**：容器内可读内容是否与其占地相称？超宽空白、每行额外 padding、空信息小标题不产生专业感。
- **视觉方向**：边框/圆角/阴影是否来自项目 tokens 与真实 Art Direction，而不是“通用 SaaS UI”？
- **响应式**：较窄窗口或 200% 放大时，分组可否自然重排，滚动、最后一项、焦点完整可达？

做两版灰阶 wireframe 对比：**A：开放式分区/直接表格**，**B：单层有界面板**；若媒介主导则比较 **C：实体卡片/画廊**。比较的是**任务完成效率、内容对齐及容器语义**，而不是谁“看起来更高级”。不要求产出所有三个版本，明确有依据选择即可。

## 3. Pattern 选择与适用边界

| 模式 | 有价值的用途 | 不合理的默认 | 注意 |
| --- | --- | --- | --- |
| Open collection / flat table | 大量同构对象、状态扫描、过滤排序 | 所有行继续套圆角卡片 | 列标题、行区分、hover/focus、长字段 |
| Single bounded panel | 真正独立的数据范围、设置分组、分析块 | Page 下再套多层只作装饰的大 Card | 面板标题与子内容同一信息架构 |
| Entity cards / gallery | 商品、作品、课程、独立对象媒体/入口 | 没有差异的记录也按卡片网格 | 内容类型、图像比例与互动 |
| Editorial flow | 文章、文档、教学步骤与例子 | 每段文字单独灰底圆角框 | 正文行宽、插图、引用、导航 |
| Split workspace | 专业编辑器、资源树/详情/预览 | 用多张随机漂浮卡替代稳定工作区 | 真实拖拽/折叠/焦点/尺寸 |
| Hero / immersive stage | 品牌/体验式视觉叙事 | 把业务表格拉到巨型 Hero 中 | 内容可达、对比度、性能 |

任务监控、用户管理、订单记录、分析事件等 `Operate` 页面可从 flat table 起步；**这不是要求所有后台放弃卡片**，而是要求对容器层级提供可检验的理由。局部功能如展开详情、告警、过滤器可有独立表面，但不能无原因堆砌。

## 4. 从成熟设计系统提炼的原则与来源

IBM Carbon Data Table：标题、工具栏、表头、行与分页组成表格结构；表格在主内容区有足够宽度、不要塞在过小容器，行内动作按需组织。借鉴的是**数据集合与动作组织**，非其品牌配色或源码。
- https://www.carbondesignsystem.com/components/data-table/usage/
- https://github.com/carbon-design-system/carbon-website/blob/main/src/pages/components/data-table/usage.mdx

对容器数量、圆角大小、边框轻重**没有通用定量阈值**；机器工具只核验设计方案/标记与示例，不可判断“高级”或用户喜欢哪种设计。

## 5. Gate B / D 验收

Gate B：确定 Table/List/Panel/Card 的共享所有权与 Tokens，区分“页面主要布局”与“真正组件容器”。对表格检查 column sizing、操作布局、状态/行高、交互边界；再读 `references/control-geometry-gate.md` 处理不可拆分的操作标签。

Gate D：真实页面在宽屏、矮屏、窄屏、文字 200% 与异常数据（长文字、空、失败）下对照整体截图；检查视觉焦点、行列节奏和最下方可达性。允许创意或品牌性超大面板，只要有明确内容理由。**静态决策计划 PASS 不代表视觉美学 PASS**。

参考：`references/whitespace-and-surface-composition.md`、`references/component-craft-gate.md`、`references/perceptual-hierarchy-gate.md`。