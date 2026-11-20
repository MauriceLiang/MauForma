# MauForma — 中英文语义边界核对（中文）

本文是**按需查询的解释附录**，不是第二套执行入口。Agent 默认先读英文 SKILL.md；仅在权限、语言、范围、例外或验收有歧义时查看对应 B 编号。英文对照在 semantic-boundaries.en.md；唯一结构化契约为 assets/semantic-boundary-contract.json，修改任一语言须同步回归。

## B01 — Task authority / 任务与授权

- **触发**: 任意设计、实现或评审请求
- **必须**: 优先遵守用户明确要求、已确认设计决策与既有功能契约，仅修改请求涉及的范围。
- **适用例外**: 用户授权的重设计可替换指定范围内的视觉方向，须记录改变了哪些决定。
- **禁止**: 不得把 Skill 默认风格解释成高于用户已确认选择的指令。
- **深入参考**: `SKILL.md`, `references/project-design-hierarchy.md`

## B02 — Language vs product locale / 指令语言与产品语言

- **触发**: Agent 读取英文规范或实现本地化产品
- **必须**: 答复与产品文案遵循用户或现有产品语言，检查真实文字、中英文换行与数字格式。
- **适用例外**: 仅在用户请求翻译或产品明确需要该语言时翻译界面文案。
- **禁止**: 不得仅因为 MauForma 入口是英文，就把已有中文界面擅自改成英文。
- **深入参考**: `SKILL.md`, `references/execution-handbook.en.md`

## B03 — Reference loading / 按需读取

- **触发**: 需要读取专项规范的任何任务
- **必须**: 先读取一份直接相关主文档，仅在发现具体问题时补充专项资料；路由表不是全量必读清单。
- **适用例外**: 复杂实现或已证实阻塞可按实际需要超过三份，但每份增加都应有明确用途。
- **禁止**: 不得默认加载整个 Skill 参考库或运行全部检查器。
- **深入参考**: `SKILL.md`, `references/semantic-boundaries.en.md`

## B04 — Component dependency / 组件与安装权限

- **触发**: 页面需要交互控件
- **必须**: 先盘点并复用现有可访问组件库，将需要的控件映射到实际组件并验证各状态。
- **适用例外**: 没有合适库时，仅在实现授权和依赖策略允许范围内引入兼容依赖；否则优先合格原生控件或说明阻塞。
- **禁止**: 不得擅自安装全局工具，也不得用仅支持点击的 div 伪造 Select 等控件。
- **深入参考**: `references/component-library-first-gate.md`, `references/execution-handbook.en.md`

## B05 — Optional visual effects / 可选视觉特效

- **触发**: 任务涉及液态玻璃、电影化循环动效或实验效果
- **必须**: 仅在用户明确要求或已批准设计方案明确继承时采用，并验证降级与可访问性。
- **适用例外**: 营销插画可以经授权采用强动效；高频操作工作台可以保持静态与紧凑。
- **禁止**: 不得把演示特效或配色预设强加为全站通用样式。
- **深入参考**: `references/liquid-glass-optics.md`, `references/motion-craft-and-continuity.md`

## B06 — Page-header H0 / 页头文字 H0

- **触发**: 创建、修改或审查页头标题，包括已有历史内容
- **必须**: 检查 H1 前文案；任务页移除或移位重复说明，保留真实面包屑、状态及已确认品牌内容。
- **适用例外**: 确有意义的章节标识及有依据的品牌/营销叙事可以保留。
- **禁止**: 不得仅因原页面已有装饰性眉题就保留无意义文案。
- **深入参考**: `references/page-header-antipatterns.md`, `references/semantic-copy-hygiene.md`

## B07 — Surface accent S0 / 卡片贴边彩条 S0

- **触发**: 新建或审查 Card、Panel、Section 容器
- **必须**: 新建及涉及的既有页面都应去除贴着卡片圆角边框的装饰性粗彩条。
- **适用例外**: 真实焦点、图表系列、进度与状态语义不受禁令影响；必要外置标记须与容器留明显间隔。
- **禁止**: 不得用彩色单侧边框、内阴影或伪元素重新制造贴边装饰条。
- **深入参考**: `references/surface-edge-accent-gate.md`, `references/execution-handbook.en.md`

## B08 — Figma authority / Figma 输入权限

- **触发**: 用户要求忠实实现现有 Figma 设计
- **必须**: 在有条件时锁定准确文件、画板节点、授权资产与设计上下文/截图，并以相同视口对照真实实现。
- **适用例外**: 当前选中节点仅在兼容桌面连接可用；远端提供方可能需要明确文件与节点 URL。只有截图时只能做视觉近似。
- **禁止**: 不得虚构 Figma 工具权限、不可见的资产细节或无条件宣称像素级一致。
- **深入参考**: `references/figma-fidelity-workflow.md`, `references/execution-handbook.en.md`

## B09 — Scope of viewport / 支持视口范围

- **触发**: 执行响应式或视口验收
- **必须**: 检查产品实际支持的断点、最小视口、内容可达性及相关文字缩放。
- **适用例外**: 只有产品支持移动端时才要求 390px 手机布局；纯桌面产品仍须验收支持的最小桌面尺寸。
- **禁止**: 不得在无需求时强迫纯桌面项目适配手机或改成移动优先。
- **深入参考**: `references/browser-qa-protocol.md`, `references/product-experience-routing-gate.md`

## B10 — Evidence claim / 验证结论

- **触发**: 汇报任意测试、视觉或业务完成结果
- **必须**: 记录实际测试路由、状态、视口、数据与证据；VERIFIED 仅覆盖明确实测范围。
- **适用例外**: 仅源码审查标记 STATIC CHECK，合成用例标记 DEMO ONLY，条件不足标记 NOT TESTED 或 BLOCKED。
- **禁止**: 不得用截图推断后端真实保存，也不得用启发式帧检测证明动画丝滑。
- **深入参考**: `references/browser-qa-protocol.md`, `references/motion-rehearsal-and-evidence.md`

## B11 — Review vs implement / 评审与实施区分

- **触发**: 仅评审、修复缺陷、重设计或整体精修请求
- **必须**: 仅评审输出问题与证据而不改代码；局部修复需要回归测试；重大重设计应先确认方向并做充分复验。
- **适用例外**: 重大视觉改动适合独立审美评审，但单行 Bug 修复不必召开完整设计评审。
- **禁止**: 不得把仅评审请求当成改代码授权，也不得把小修复扩成多轮无关访谈。
- **深入参考**: `references/design-craft-loop.md`, `SKILL.md`

## B12 — Design drift meaning / 设计漂移含义

- **触发**: 发现 Token、文件格式或设计文档漂移
- **必须**: 区分工具版本、文档格式和设计事实漂移；从代码提取的 Token 观测快照不是已批准设计决策。
- **适用例外**: 格式变迁可以在获授权后机械迁移；设计事实漂移必须结合产品意图和真实渲染证据判断。
- **禁止**: 不得为让漂移检查通过而静默覆盖 MASTER 或用户品牌选择。
- **深入参考**: `references/project-design-hierarchy.md`, `references/skill-gap-workflows.md`

## B13 — Reference research and assets / 参考研究与素材边界

- **触发**: 分析外部网站、借鉴上游规则或使用视觉素材
- **必须**: 仅访问获授权来源，区分实测 WHAT 与推断 WHY，复用素材时核对许可证。
- **适用例外**: 浏览受限或样式搜索没有领域相关结果时，应缩小检索或说明证据不足。
- **禁止**: 不得虚构参考网站的设计意图、伪造设计数据或复制受保护素材。
- **深入参考**: `references/design-dna-protocol.md`, `references/design-reference-learning-gate.md`

## B14 — Browser reconnaissance / 浏览器先观察后操作

- **触发**: 打开运行中的应用进行浏览器测试
- **必须**: 先观察实时 DOM 和页面状态再确定选择器，记录 Console 与相关网络错误，再执行交互和复验。
- **适用例外**: 无法访问浏览器、服务或缺少权限时标记 NOT TESTED/BLOCKED，不得编造选择器或测试结果。
- **禁止**: 不得用合成内存模拟页面替代真实后端业务链路的验收。
- **深入参考**: `references/browser-qa-protocol.md`, `references/execution-handbook.en.md`

## B15 — RTL and locale / RTL 与本地化

- **触发**: 产品包含 RTL 语言、本地化表单或国际化内容
- **必须**: 使用符合语言环境的日期和数字格式，真实检查中日韩文本和已支持的 RTL 布局，必要时使用逻辑方向 CSS 属性。
- **适用例外**: RTL 仅在产品支持对应语言时适用，不要求只支持有限语言的桌面项目新增 RTL。
- **禁止**: 不得仅凭 IP 推断语言，也不得无安全理由禁止用户正常粘贴。
- **深入参考**: `references/browser-qa-protocol.md`, `references/execution-handbook.en.md`


**解释原则**：例外不得抹去禁止事项，禁止事项也不得误伤真正有语义的例外。需求或证据不明确时要说明限制、保留既有产品决定。静态规则一致性通过不等于浏览器或 Agent 实际行为验收通过。
