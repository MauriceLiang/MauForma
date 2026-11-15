# Design Craft Loop — 从设计意图到审美复核的通用闭环

> **定位**：提升首版 UI 的视觉判断与精修质量。仅在新建页面、重大改版、用户要求“高级/不模板化/优化细节”、或正式视觉验收时按需使用；单个 Bug 修复不需要重新完成整个设计流程。
>
> 本文是 MauForma 独立编写的方法总结，不是安装第三方 Skill、外部设计师的官方评分标准，也不是给所有项目强制套同一种审美。

## 一、按任务选模式，而不是把七个工作流都跑一次

| 模式 | 触发 | 最小交付 | 不需要 |
| --- | --- | --- | --- |
| **shape** · 新页面/重设计 | 从零设计、现有页面明显失焦 | 任务与内容简报、视觉方向、共享 Token/组件方案、首版及浏览器复验 | 为明确需求反复做访谈 |
| **polish** · 视觉精修 | 用户觉得“塑料感”、层级混乱、控件粗糙 | 现状证据、问题根因、分优先级修复、前后同条件对照 | 不经授权重排全部导航/品牌 |
| **review** · 独立评审 | 只要求评审或设计检查 | 有证据的严重性排序、保留优点、建议与未测项 | 未经请求直接改代码 |
| **fidelity** · 严格实现 | 用户提供 Figma 稿并要求还原 | 设计节点上下文、截图基准、资产与 Token 映射、实现及差异复验 | 自作主张替换风格或重新构图 |
| **fix** · 明确局部修复 | 单个交互/视觉错误 | 最小影响范围、直接修正、关联状态回归 | 大而全的设计发现 |

页面可以以 Operate / Read / Persuade / Experience 为主目标，不能把模式标签直接理解成“某种固定布局”。用户的设计意愿、已确认品牌规范、真实业务目标及现有组件契约始终优先。

## 二、Design Direction Gate：代码前说清“为什么这样设计”

首次创建/重大重构时，用简短的 **Design Intent** 决定：

1. **主题与受众**：用户是谁，页面主要帮助他完成什么？真实的内容/素材是什么？
2. **视觉主张**：一句话说明整页要给人的感受，以及视觉策略如何服务任务。不要只写“高级、简约、现代”。
3. **信息焦点与构图**：首屏主视觉、标题/媒体/数据/主要操作谁最大，哪些只是支持信息？必要时做灰阶 wireframe。
4. **签名元素（可选）**：允许一个能被记住的、与主题一致的视觉手法（特别的摄影比例、排版、交互、色彩关系等），但不要求管理表格硬加炫技。
5. **设计选择的依据与舍弃方案**：至少说明“选择 A 因为 X，有意不使用 B 因为 Y”；明确 `confirmed / inherited / delegated / proposed / unresolved` 的来源。
6. **Tokens 与组件接入**：继承已有 CSS variables / Figma variables / UI Provider / 组件主库；新增项目才建立最小单一 Token 源。先按 `references/component-library-first-gate.md` 配置真实控件，不用手写伪 Select 代替完整组件。
7. **限制与降级**：目标平台、性能、动效偏好、字体许可、主题、布局断点、必要的适配范围。仅桌面产品不强制改成移动产品。

**设计风险**：刻意、有理由地尝试非默认构图，不等于为所有项目强制大胆配色、衬线字体、非对称或页面入场动画。也不能把 Inter、卡片、渐变、黑白等单一样式直接标为“AI 味”。只有不匹配内容与任务、缺乏信息价值或导致实际质量损失时才是问题。

参考：`references/design-discovery-interview.md`、`references/composition-first-design.md`、`references/design-style-catalog.md`、`references/design-dna-protocol.md`。

## 三、精修七个域，但只在触发时深入

| 域 | Agent 要看什么 | 易犯的具体问题 | 核验方法 |
| --- | --- | --- | --- |
| **Typography** 排版 | 页面标题、正文、数据、轴/图例、混合语言与可读宽度，字体来源、字重/行高和光学尺寸 | 功能页 H1 上方解释型眉题（不要求与 H1 字面重复才判错）、过大标题压过主体、刻度小到难读 | 真实字体渲染、中文/数字混排、长文与 200% 文字缩放 |
| **Color & Contrast** 色彩 | 角色化品牌色/中性色/语义状态色，深浅主题、相邻表面、焦点对比 | 随机 HEX、浅灰文字、强调色与状态色混用、多个强色争抢视觉中心 | 对真实前景背景计算对比、检查跨区配色和实际环境 |
| **Spatial Design** 空间 | 内外留白、行/列网格、留白节奏、卡片容器必要性、底部可达 | 模块直接拼到一起、Card 套 Card、上下左右未对齐、虚假 min-height 大空洞 | DOM geometry + 整页截图 + 滚动末端 |
| **Motion** 动效 | 状态反馈时长、缓动、先后关系、用户选择与 reduced motion | 全站零动态反馈、杂乱弹跳、动画与业务状态不同步、多个库争抢同属性 | 实际操作状态录制/浏览器测试、低动态模式、卸载清理 |
| **Interaction States** 交互 | Select/Combobox/Dropdown/Button/Tabs/Dialog 等真实库组件、selected/hover/focus/disabled/loading/error | 手写假下拉、按钮不同页不同半径、没有键盘/焦点、浮层被裁切 | `references/component-library-first-gate.md` + 真实路由逐态操作 |
| **Responsive** 适配 | 按目标使用设备调整布局、容器查询、长文本与内容优先顺序 | 只压缩字号、窄高窗口裁切、底部固定栏挡住内容、忽视桌面目标密度 | 用户要求的视口矩阵与 200% 文字放大 |
| **UX Writing** 文案 | 真实标题、操作动词、状态反馈、空/错误文案、单位、来源与例外 | 装饰性英文、用语重复、Mock 术语外露、删除真实来源/样本量 | `references/semantic-copy-hygiene.md` + 真实任务路径 |

七域是**检查范围**，不是每次必须修改的七项。对交互型页面，优先修复不可用的组件/真实任务错误；对品牌表达，优先处理内容与构图。设计系统用语义变量集中实现，不因追求“独特性”让每张页面分别定义 Button、Radius、Focus。

## 四、独立 Critique Gate：先指出根因，再修

- **证据等级**：`OBSERVED`＝真实浏览器/截图明确可见；`CODE ONLY`＝仅源码风险；`INFERRED`＝设计判断或假设；`NOT TESTED`＝缺少验证。不要把“看起来廉价”当成可自动量化的事实。
- **问题等级**：`P0` 业务不可用/严重可访问性、`P1` 主任务不清或结构错误、`P2` 视觉层级/组件/间距破坏使用、`P3` 局部光学与微调。
- **每条问题写成**：`symptom → evidence → root cause hypothesis → affected task → recommended fix → validation`。对未知根因明确标注待验证，禁止声称静态脚本能自动识别所有“审美问题”。
- **两类检查分开**：`UX/IA` 判断业务目标、内容、信息路径；`Visual Craft` 判断字体、配色、构图、组件状态和细节。UX 失败不能靠换主题冒充解决，视觉不协调不能因为功能能点就宣称优秀。
- **保留有效设计**：报告已经做对的部分与原用户确认决策；不要为了换新风格把原有良好元素全部推翻。
- **从严重到次要处理**：先 P0/P1，再 P2/P3。修好后用**相同视口、数据状态、主题与缩放**前后对照；失败继续迭代，直到主要缺陷不再存在或明确受限。
- **分数不是证据**：可以沿用 `references/ui-review-rubric.md` 做团队内部打分，但没有真实页面截图/可操作证据不得给确定性高分，也不得把主观“美感”伪装成算法认证。

### “反模板”审查的六个具体问题

1. 删除标题上的抽象英文和自嗨口号后，还能知道页面做什么吗？
2. 第一眼最显眼的区域，是否真是用户任务/品牌要表达的主体？
3. 让页面难看的是**构图/内容**，还是仅有配色/圆角？先解决上游根因。
4. 图标、控件、信息密度和间距有没有**系统性的**一致性，而不是每块单独漂亮？
5. 有“独特感”的元素是否有内容或品牌依据，还是照抄流行渐变/大卡片/粒子？
6. 深浅主题、长中文、真实下拉和选中态、滚动末端实测后，视觉选择是否仍成立？

## 五、交付流程与出口标准

`shape`：Brief / Intent → Composition / Tokens → Component Library → 实现 → Critique → 定向修改 → 真实复验。

`polish`：真实页面 Baseline → 根因排序 → 优先修结构/内容 → 控件与 Tokens → 微细节 → 前后对照。

`review`：收集可得证据 → UX / Craft 双通道审查 → 问题分级与修复建议，不擅改代码。

`fidelity`：交给 `references/figma-fidelity-workflow.md`，**有可访问的原设计才谈像素对齐**；没有源时不能“猜一个 Figma 风格”。

`fix`：限制改动范围 → 直接修复 → 回归相关状态，跳过无关艺术方向工作。

**交付必须区分** `VERIFIED / STATIC CHECK / DEMO ONLY / NOT TESTED / BLOCKED`。合成演示、截图审查和真实业务 E2E 是不同层级，不互相替代。

## 来源与迁移边界

可借鉴的方法：Anthropic `frontend-design` 的意图明确与设计观点；Impeccable 的七域精修；Taste 系列不同实现的证据化判断；theme-factory 的统一主题原则；designer-skills 的分阶段设计工作流。视频里的 `design-process-pack` 只作为“需求先于绘图”的启发，未核实唯一对应的上游仓库。**没有复制任一第三方 Skill 的说明文字、命令实现或示例资产**。

公开参考：
- <https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design/skills/frontend-design>
- <https://github.com/pbakaus/impeccable>
- <https://github.com/senlindesign/taste-skill>
- <https://github.com/Leonxlnx/taste-skill>
- <https://github.com/anthropics/skills/tree/main/skills/theme-factory>
- <https://github.com/julianoczkowski/designer-skills>

在 MauForma 通用仓库里只存**匿名、合成**的示例。具体网站的私有截图、业务字段、用户项目名与设计决策保存在其自身工作区，不回流到此 Skill。
