# MauForma — 中文原始规则与英文执行规则语义回归对照

> 用途：用于维护者核查中文设计意图在英文迁移及后续修改中是否被完整保留。本文属于**维护与审计资料**，不是新的 Agent 执行入口；普通产品任务仍由 `SKILL.md` 按需路由。本文不代表自动翻译认证，也不声称覆盖每个自然语言细节。

## 1. 源头、范围与证据等级

- **不可变中文溯源基线**：[Git commit `54a4af62566da1532c2b68d4301b531aee118e81`](https://github.com/MauriceLiang/MauForma/tree/54a4af62566da1532c2b68d4301b531aee118e81)。原中文文件应从该提交下的原始路径读取，而不是用当前英文反向翻译来伪造“原意”。
- **英文执行文本**：当前仓库 `main` 下的 `SKILL.md` 和按需参考文档；新增或调整的规则需要同样记录其批准来源与中英文对应关系。
- **翻译范围**：原中文专项参考文档 83 份，原有英文文档 4 份，保留的中文语义核对文件 1 份。83 份的源 Git blob SHA 见下方索引，也存在 `assets/i18n-phase2-migration-inventory.json`。
- **双语规范**：`references/semantic-boundaries.zh-CN.md` 与 `.en.md` 是 B01–B15 当前版本的两种表述；`assets/semantic-boundary-contract.json` 保存可机检的触发、必须、例外和禁止字段。
- **翻译抽样锚点**：`assets/i18n-phase2-translation-contract.json` 包含 83 份文档的局部中文—英文短语配对。**短语存在性不是整句、整段或整篇语义等价的证明**，尤其不能把否定、授权、量化和例外压缩成关键词匹配。
- **已记录的复核**：`assets/i18n-phase2-semantic-review.md` 记录第二轮有限范围检查及修复；结论只覆盖记录内核查项目，不自动涵盖未来修改或真实 Agent 行为。

### 规则优先级与回归基准

1. 用户最新明确指令、已批准的设计/业务决策始终高于 Skill 解释。翻译不是增加或删除授权的来源。
2. 对于历史中文规则的英文迁移，以不可变中文源文件核对触发条件、行为强度、禁止事项、例外、数值、技术标识及验收标准；**不能只比较两份可能一起出错的翻译文档**。
3. 对于后来明确批准的英文新增规则，不能机械地用旧中文基线否定合法的新范围；必须记录批准依据、中文对应说明和变更原因。
4. 英文正文、中文语义说明、结构化契约发生矛盾时，标记 `REVIEW REQUIRED`，暂停宣布等价；先回查中文源、最新批准决定以及具体变更，再同步修正相关文件。
5. `STATIC CHECK PASS` 仅证明字段、链接、锚点等静态完整性；`BILINGUAL REVIEWED` 需要有原文—译文逐条人工/Agent 复查和记录；`BEHAVIOR VERIFIED` 还需要实际 Agent 任务或真实产品证据。不得互相冒充。

## 2. 重点语义回归风险（实际修订）

| 规则 | 中文语义不可丢失的条件 | 本次英文修正点 | 如回归失败的影响 |
| --- | --- | --- | --- |
| B01 | 设计、实现、**评审**均受用户授权约束 | `Any design, implementation or review request` | 评审任务可能被错误排除 |
| B05 | 营销等强动效必须**经授权** | `When authorized` | 把可选动效误当默认许可 |
| B08 | 设计资产必须来自**授权来源** | `authorized source assets` | 误扩大获取和复用素材的权限 |
| B11 | 重大重设计必须**先确认方向**，再实施与复验 | `requires confirming design direction before implementation` | 将设计建议当作已批准变更 |
| B12 | Schema 机械迁移须**明确授权**，并允许在授权范围内实际迁移 | `With explicit approval, ... may be migrated mechanically` | 将“允许实施”缩成“只能建议”或反向变成“未经批准就修改” |

这五处修订是针对可追溯的中英文条款差异，不应推断其余语句已经自动获得无歧义认证。

## 3. B01–B15 当前中英文逐项对照

下列文字从当前 `assets/semantic-boundary-contract.json` 的正式字段生成。该契约与中、英文对应文档应同步修改；对照本身并不自动证明其与更早的原始中文专项参考文档完全等价。

### B01 — Task authority / 任务与授权

| 对照维度 | 中文规则 | 英文执行含义 |
| --- | --- | --- |
| 触发条件 | 任意设计、实现或评审请求 | Any design, implementation or review request |
| 必须行为 | 优先遵守用户明确要求、已确认设计决策与既有功能契约，仅修改请求涉及的范围。 | Preserve explicit user instructions, approved design decisions and existing functional contracts; scope changes to the asked task. |
| 允许例外 | 用户授权的重设计可替换指定范围内的视觉方向，须记录改变了哪些决定。 | A user-approved redesign may intentionally replace the affected visual direction; record which decisions changed. |
| 禁止行为 | 不得把 Skill 默认风格解释成高于用户已确认选择的指令。 | Never infer that a Skill style override outranks the user's approved choices. |

- 相关文件：`SKILL.md`、`references/project-design-hierarchy.md`。

### B02 — Language vs product locale / 指令语言与产品语言

| 对照维度 | 中文规则 | 英文执行含义 |
| --- | --- | --- |
| 触发条件 | Agent 读取英文规范或实现本地化产品 | An Agent reads English instructions or works on a localized UI |
| 必须行为 | 答复与产品文案遵循用户或现有产品语言，检查真实文字、中英文换行与数字格式。 | Keep replies and product copy in the user's or existing product locale; verify actual text, CJK wrapping and numbers. |
| 允许例外 | 仅在用户请求翻译或产品明确需要该语言时翻译界面文案。 | Translate product copy only if the user requests localization or the product requirements require that locale. |
| 禁止行为 | 不得仅因为 MauForma 入口是英文，就把已有中文界面擅自改成英文。 | Never translate an existing UI to English solely because MauForma's entrypoint is English. |

- 相关文件：`SKILL.md`、`references/execution-handbook.en.md`。

### B03 — Reference loading / 按需读取

| 对照维度 | 中文规则 | 英文执行含义 |
| --- | --- | --- |
| 触发条件 | 需要读取专项规范的任何任务 | Any task using references |
| 必须行为 | 先读取一份直接相关主文档，仅在发现具体问题时补充专项资料；路由表不是全量必读清单。 | Load one primary relevant guide; add secondary guides only for specific identified needs. A reference table lists choices, not mandatory steps. |
| 允许例外 | 复杂实现或已证实阻塞可按实际需要超过三份，但每份增加都应有明确用途。 | Complex implementation or a verified blocker can justify more than three guides when each addition is relevant. |
| 禁止行为 | 不得默认加载整个 Skill 参考库或运行全部检查器。 | Never load the entire Skill reference library or every validator by default. |

- 相关文件：`SKILL.md`、`references/semantic-boundaries.en.md`。

### B04 — Component dependency / 组件与安装权限

| 对照维度 | 中文规则 | 英文执行含义 |
| --- | --- | --- |
| 触发条件 | 页面需要交互控件 | An interactive page needs controls |
| 必须行为 | 先盘点并复用现有可访问组件库，将需要的控件映射到实际组件并验证各状态。 | Inspect and reuse the installed accessible library first; map required controls to real components and test states. |
| 允许例外 | 没有合适库时，仅在实现授权和依赖策略允许范围内引入兼容依赖；否则优先合格原生控件或说明阻塞。 | If none exists, a new compatible dependency may be installed only within the user's delegated implementation and dependency policy; otherwise use sound native controls or report the blocker. |
| 禁止行为 | 不得擅自安装全局工具，也不得用仅支持点击的 div 伪造 Select 等控件。 | Never silently install global tooling or replace real controls with click-only div elements. |

- 相关文件：`references/component-library-first-gate.md`、`references/execution-handbook.en.md`。

### B05 — Optional visual effects / 可选视觉特效

| 对照维度 | 中文规则 | 英文执行含义 |
| --- | --- | --- |
| 触发条件 | 任务涉及液态玻璃、电影化循环动效或实验效果 | Liquid glass, cinematic/looping motion or experimental effects appear in a task |
| 必须行为 | 仅在用户明确要求或已批准设计方案明确继承时采用，并验证降级与可访问性。 | Use such effects only when explicitly requested or clearly inherited from an approved product brief; test fallback and accessibility. |
| 允许例外 | 营销插画可以经授权采用强动效；高频操作工作台可以保持静态与紧凑。 | When authorized, a marketing illustration may be deliberately expressive; a dense workbench may remain static and compact. |
| 禁止行为 | 不得把演示特效或配色预设强加为全站通用样式。 | Never make a demo effect or aesthetic preset a global default for all pages. |

- 相关文件：`references/liquid-glass-optics.md`、`references/motion-craft-and-continuity.md`。

### B06 — Page-header H0 / 页头文字 H0

| 对照维度 | 中文规则 | 英文执行含义 |
| --- | --- | --- |
| 触发条件 | 创建、修改或审查页头标题，包括已有历史内容 | Creating, editing or reviewing a page title, including legacy content |
| 必须行为 | 检查 H1 前文案；任务页移除或移位重复说明，保留真实面包屑、状态及已确认品牌内容。 | Inspect pre-H1 copy; remove or move redundant explanation on task pages; preserve real breadcrumbs, status and approved branding. |
| 允许例外 | 确有意义的章节标识及有依据的品牌/营销叙事可以保留。 | Meaningful chapter labels and intentional brand/marketing narratives may remain when justified. |
| 禁止行为 | 不得仅因原页面已有装饰性眉题就保留无意义文案。 | Never retain meaningless old eyebrow text merely because it already exists. |

- 相关文件：`references/page-header-antipatterns.md`、`references/semantic-copy-hygiene.md`。

### B07 — Surface accent S0 / 卡片贴边彩条 S0

| 对照维度 | 中文规则 | 英文执行含义 |
| --- | --- | --- |
| 触发条件 | 新建或审查 Card、Panel、Section 容器 | Creating or reviewing Card/Panel/Section surfaces |
| 必须行为 | 新建及涉及的既有页面都应去除贴着卡片圆角边框的装饰性粗彩条。 | Remove decorative thick colored strips attached to rounded card borders on both new and affected legacy views. |
| 允许例外 | 真实焦点、图表系列、进度与状态语义不受禁令影响；必要外置标记须与容器留明显间隔。 | Actual focus indicators, chart series, progress and status semantics remain valid; a needed outside marker must have a visible gap. |
| 禁止行为 | 不得用彩色单侧边框、内阴影或伪元素重新制造贴边装饰条。 | Never reintroduce a flush colored border, inset shadow or pseudo-element as a decorative card stripe. |

- 相关文件：`references/surface-edge-accent-gate.md`、`references/execution-handbook.en.md`。

### B08 — Figma authority / Figma 输入权限

| 对照维度 | 中文规则 | 英文执行含义 |
| --- | --- | --- |
| 触发条件 | 用户要求忠实实现现有 Figma 设计 | A user asks to implement an existing Figma design |
| 必须行为 | 在有条件时锁定准确文件、画板节点、授权资产与设计上下文/截图，并以相同视口对照真实实现。 | Identify exact design file, frame/node, authorized source assets, design context and screenshot when available; compare real implementation at the same viewport. |
| 允许例外 | 当前选中节点仅在兼容桌面连接可用；远端提供方可能需要明确文件与节点 URL。只有截图时只能做视觉近似。 | Desktop current-selection is available only with a compatible desktop connection; remote providers may require explicit Figma file and node URL. Screenshot-only work is approximate. |
| 禁止行为 | 不得虚构 Figma 工具权限、不可见的资产细节或无条件宣称像素级一致。 | Never fabricate Figma tool access, unprovided asset details or unconditional pixel-perfect parity. |

- 相关文件：`references/figma-fidelity-workflow.md`、`references/execution-handbook.en.md`。

### B09 — Scope of viewport / 支持视口范围

| 对照维度 | 中文规则 | 英文执行含义 |
| --- | --- | --- |
| 触发条件 | 执行响应式或视口验收 | Responsive or viewport QA |
| 必须行为 | 检查产品实际支持的断点、最小视口、内容可达性及相关文字缩放。 | Test the supported product breakpoints, declared minimum viewport, content reachability and relevant text zoom. |
| 允许例外 | 只有产品支持移动端时才要求 390px 手机布局；纯桌面产品仍须验收支持的最小桌面尺寸。 | Only test a 390px mobile layout when mobile support is in scope; desktop-only products still need their smallest supported desktop view. |
| 禁止行为 | 不得在无需求时强迫纯桌面项目适配手机或改成移动优先。 | Never add mobile support or force a mobile-first redesign without a product requirement. |

- 相关文件：`references/browser-qa-protocol.md`、`references/product-experience-routing-gate.md`。

### B10 — Evidence claim / 验证结论

| 对照维度 | 中文规则 | 英文执行含义 |
| --- | --- | --- |
| 触发条件 | 汇报任意测试、视觉或业务完成结果 | Claiming any test, visual or business result |
| 必须行为 | 记录实际测试路由、状态、视口、数据与证据；VERIFIED 仅覆盖明确实测范围。 | Specify actual route, state, viewport, data and evidence; use VERIFIED only for the tested scope. |
| 允许例外 | 仅源码审查标记 STATIC CHECK，合成用例标记 DEMO ONLY，条件不足标记 NOT TESTED 或 BLOCKED。 | Static code analysis is STATIC CHECK; synthetic fixtures are DEMO ONLY; missing conditions are NOT TESTED or BLOCKED. |
| 禁止行为 | 不得用截图推断后端真实保存，也不得用启发式帧检测证明动画丝滑。 | Never infer backend persistence from screenshots or smooth animation from a heuristic trace. |

- 相关文件：`references/browser-qa-protocol.md`、`references/motion-rehearsal-and-evidence.md`。

### B11 — Review vs implement / 评审与实施区分

| 对照维度 | 中文规则 | 英文执行含义 |
| --- | --- | --- |
| 触发条件 | 仅评审、修复缺陷、重设计或整体精修请求 | Review-only, bug-fix, redesign or general polish request |
| 必须行为 | 仅评审输出问题与证据而不改代码；局部修复需要回归测试；重大重设计应先确认方向并做充分复验。 | Review-only means findings without edits; a scoped fix requires actual regression checks; major redesign requires confirming design direction before implementation and broader QA. |
| 允许例外 | 重大视觉改动适合独立审美评审，但单行 Bug 修复不必召开完整设计评审。 | Independent formal design critique is valuable for substantial visual change but not mandatory for a one-line bug fix. |
| 禁止行为 | 不得把仅评审请求当成改代码授权，也不得把小修复扩成多轮无关访谈。 | Never turn a review request into source edits or a tiny fix into an unrequested interview. |

- 相关文件：`references/design-craft-loop.md`、`SKILL.md`。

### B12 — Design drift meaning / 设计漂移含义

| 对照维度 | 中文规则 | 英文执行含义 |
| --- | --- | --- |
| 触发条件 | 发现 Token、文件格式或设计文档漂移 | An observed token, schema or design-document drift is reported |
| 必须行为 | 区分工具版本、文档格式和设计事实漂移；从代码提取的 Token 观测快照不是已批准设计决策。 | Distinguish tool version drift, schema drift and product truth drift; code-derived token snapshots are observations, not approved design decisions. |
| 允许例外 | 格式变迁可以在获授权后机械迁移；设计事实漂移必须结合产品意图和真实渲染证据判断。 | With explicit approval, schema changes may be migrated mechanically; truth drift requires checking real product intent and rendered evidence. |
| 禁止行为 | 不得为让漂移检查通过而静默覆盖 MASTER 或用户品牌选择。 | Never silently overwrite MASTER or brand decisions to make drift checks green. |

- 相关文件：`references/project-design-hierarchy.md`、`references/skill-gap-workflows.md`。

### B13 — Reference research and assets / 参考研究与素材边界

| 对照维度 | 中文规则 | 英文执行含义 |
| --- | --- | --- |
| 触发条件 | 分析外部网站、借鉴上游规则或使用视觉素材 | Analyzing external websites, adopting upstream rules or borrowing visual assets |
| 必须行为 | 仅访问获授权来源，区分实测 WHAT 与推断 WHY，复用素材时核对许可证。 | Only access authorized sources; distinguish measured WHAT from inferred WHY and check licensing for copied materials. |
| 允许例外 | 浏览受限或样式搜索没有领域相关结果时，应缩小检索或说明证据不足。 | If browsing is blocked or a style query yields no domain-relevant result, refine with available evidence or report missing evidence. |
| 禁止行为 | 不得虚构参考网站的设计意图、伪造设计数据或复制受保护素材。 | Never infer source-site designer intent, invent design data or copy protected assets. |

- 相关文件：`references/design-dna-protocol.md`、`references/design-reference-learning-gate.md`。

### B14 — Browser reconnaissance / 浏览器先观察后操作

| 对照维度 | 中文规则 | 英文执行含义 |
| --- | --- | --- |
| 触发条件 | 打开运行中的应用进行浏览器测试 | Opening a running application for browser tests |
| 必须行为 | 先观察实时 DOM 和页面状态再确定选择器，记录 Console 与相关网络错误，再执行交互和复验。 | Inspect live DOM and current page state before choosing selectors; capture browser console and relevant network errors, then interact and retest. |
| 允许例外 | 无法访问浏览器、服务或缺少权限时标记 NOT TESTED/BLOCKED，不得编造选择器或测试结果。 | When the browser, app server or permissions are unavailable, report NOT TESTED/BLOCKED without manufacturing selectors or expected results. |
| 禁止行为 | 不得用合成内存模拟页面替代真实后端业务链路的验收。 | Never substitute a synthetic in-memory demo for actual server-backed workflow verification. |

- 相关文件：`references/browser-qa-protocol.md`、`references/execution-handbook.en.md`。

### B15 — RTL and locale / RTL 与本地化

| 对照维度 | 中文规则 | 英文执行含义 |
| --- | --- | --- |
| 触发条件 | 产品包含 RTL 语言、本地化表单或国际化内容 | Product includes RTL languages, locale-sensitive inputs or internationalized content |
| 必须行为 | 使用符合语言环境的日期和数字格式，真实检查中日韩文本和已支持的 RTL 布局，必要时使用逻辑方向 CSS 属性。 | Use locale-aware date/number formatting and meaningful CJK/RTL text tests, including logical properties when RTL is supported. |
| 允许例外 | RTL 仅在产品支持对应语言时适用，不要求只支持有限语言的桌面项目新增 RTL。 | RTL is conditional on actual supported locales; do not add a new RTL feature to a locale-limited desktop app. |
| 禁止行为 | 不得仅凭 IP 推断语言，也不得无安全理由禁止用户正常粘贴。 | Never infer locale from user IP or block ordinary paste without a security reason. |

- 相关文件：`references/browser-qa-protocol.md`、`references/execution-handbook.en.md`。

## 4. 83 份原中文资料 → 当前英文资料的可追溯索引

每行的「原中文」链接固定到翻译前的 Git commit；SHA 是该文件当时的 Git blob SHA。英文链接指向当前 `main`，用于未来对比。**这里列的是可检索源头，不是 83 份文件逐行语义验收的证书。**

| # | 文档 | 原中文固定版本 | Git blob SHA | 英文执行版本 |
| ---: | --- | --- | --- | --- |
| 1 | `aesthetic-authorship.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/aesthetic-authorship.md) | `20f2797f08f371ccf7e0d2d6db9e640cd2e0a923` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/aesthetic-authorship.md) |
| 2 | `agent-team-handoff.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/agent-team-handoff.md) | `e7a5f21f35667dff17eb51efc3315a7f61d5ecf3` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/agent-team-handoff.md) |
| 3 | `ai-frontend-prompt-policy.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/ai-frontend-prompt-policy.md) | `c1ee369bdd5a43b7dbd77524c2c6a39a49e25450` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/ai-frontend-prompt-policy.md) |
| 4 | `animation-engine-extension.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/animation-engine-extension.md) | `ac4cda4d9e6985cfd2cf758988cb14382f3234f0` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/animation-engine-extension.md) |
| 5 | `animation-engine-selection.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/animation-engine-selection.md) | `6a044caa593ad26dc62c154fcfc71d9493708277` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/animation-engine-selection.md) |
| 6 | `animation-integration-lifecycle.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/animation-integration-lifecycle.md) | `2a7ecf4b441e89309d8c896fce0a8b9a4e2616ec` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/animation-integration-lifecycle.md) |
| 7 | `animejs-easing-complete.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/animejs-easing-complete.md) | `4e4de154a0c29a1789c57181878f8eaee4d23d8d` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/animejs-easing-complete.md) |
| 8 | `animejs-motion-recipes.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/animejs-motion-recipes.md) | `3e24ad74359f42b1b3977b10391c21539fed67a6` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/animejs-motion-recipes.md) |
| 9 | `animejs-official-capabilities.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/animejs-official-capabilities.md) | `82b72076c5e658ad695329dcce76d14ad28a6d42` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/animejs-official-capabilities.md) |
| 10 | `art-direction-critique.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/art-direction-critique.md) | `441dcfa95aa281238ef7b3acf1cdcc20750b6fc6` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/art-direction-critique.md) |
| 11 | `browser-qa-protocol.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/browser-qa-protocol.md) | `5bb6c97c4271bb25fc1dc904ed5048a6f9e8fdc2` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/browser-qa-protocol.md) |
| 12 | `chart-interior-alignment.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/chart-interior-alignment.md) | `3b22042155e42e15f39800bb10de33153e858b80` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/chart-interior-alignment.md) |
| 13 | `clean-enterprise-design.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/clean-enterprise-design.md) | `61813fa8538a88a1d8b467a1dc6a269f1823d850` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/clean-enterprise-design.md) |
| 14 | `comparison-page-design.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/comparison-page-design.md) | `d524d504160f858774115e850d9218b52a13273d` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/comparison-page-design.md) |
| 15 | `comparison-ux-case.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/comparison-ux-case.md) | `4e7ee45819b6922bb71cba731c3974e21f8f24d1` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/comparison-ux-case.md) |
| 16 | `component-craft-gate.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/component-craft-gate.md) | `96e8b9328a50a7222114c4441b9189e2d2f9bac1` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/component-craft-gate.md) |
| 17 | `component-first.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/component-first.md) | `c823e3de14cd36119f21f0907a5ae91938459c3b` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/component-first.md) |
| 18 | `component-library-first-gate.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/component-library-first-gate.md) | `fe931124ea1e6d07691874af052d1d4a5d8cb0bc` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/component-library-first-gate.md) |
| 19 | `component-motion-choreography-gate.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/component-motion-choreography-gate.md) | `6cf32e2b59d99a3ec4b9063a9a1305b9522a8c09` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/component-motion-choreography-gate.md) |
| 20 | `composition-first-design.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/composition-first-design.md) | `d504dbee1b4ebd8ef739f89636434a345f08bcc3` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/composition-first-design.md) |
| 21 | `control-geometry-gate.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/control-geometry-gate.md) | `417b3c4b7580b5b25a1e96ceccb214e530b1fc75` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/control-geometry-gate.md) |
| 22 | `creative-component-libraries.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/creative-component-libraries.md) | `c5bccc5a3b8c927ced585bf3f70907703b4c98ae` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/creative-component-libraries.md) |
| 23 | `design-craft-loop.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/design-craft-loop.md) | `ab2b6e2ffe6d4d253462504a0c0cf49c5a521266` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/design-craft-loop.md) |
| 24 | `design-discovery-interview.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/design-discovery-interview.md) | `e44159fefd2749ee3f1c47ad1f4948ea6de3d800` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/design-discovery-interview.md) |
| 25 | `design-dna-protocol.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/design-dna-protocol.md) | `74c3a2f3abe8bb993a68276e1cb52cab4c31e74c` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/design-dna-protocol.md) |
| 26 | `design-reference-learning-gate.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/design-reference-learning-gate.md) | `d01c3acb45b0f91872af0049c52616a0d82a407b` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/design-reference-learning-gate.md) |
| 27 | `design-style-catalog.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/design-style-catalog.md) | `3869f05b80313f82faef4afcc0111105dff4dbef` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/design-style-catalog.md) |
| 28 | `design-system.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/design-system.md) | `21d3d767f3e52dc98d1724dd4026d321538d97ea` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/design-system.md) |
| 29 | `enterprise-ui-library-guide.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/enterprise-ui-library-guide.md) | `bca90783d19e2cd96868a4413e17a88c1b5f4f55` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/enterprise-ui-library-guide.md) |
| 30 | `external-design-case-library.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/external-design-case-library.md) | `8ad1438f0f147b7d041e4dacd9135c8af53a73ac` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/external-design-case-library.md) |
| 31 | `figma-fidelity-workflow.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/figma-fidelity-workflow.md) | `a9de5271d035de95530f92e70f55e85cd4e96696` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/figma-fidelity-workflow.md) |
| 32 | `framework-other-web.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/framework-other-web.md) | `c86c7c780c738f431c4da1204e91ea304168e3ec` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/framework-other-web.md) |
| 33 | `framework-react-next.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/framework-react-next.md) | `156a9d32a907293237edcb74be7825504e059dcc` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/framework-react-next.md) |
| 34 | `framework-support-matrix.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/framework-support-matrix.md) | `936c56f90ed3ed3d1ba849074fba65c266a23e57` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/framework-support-matrix.md) |
| 35 | `framework-vue-nuxt.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/framework-vue-nuxt.md) | `7873bfc38a8e2375bde0f22638905aa8cb173ae9` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/framework-vue-nuxt.md) |
| 36 | `frontend-architecture-and-gates.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/frontend-architecture-and-gates.md) | `142c51671bedec7a02d75d5321658dc56f106f9c` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/frontend-architecture-and-gates.md) |
| 37 | `good-vs-bad.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/good-vs-bad.md) | `a34787f431b9c69eafb88267a43b33d778ad4ee5` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/good-vs-bad.md) |
| 38 | `grid-alignment-and-viewport-safety.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/grid-alignment-and-viewport-safety.md) | `1a1e57f4d8044a35a0ca9312ec28938dd3ce125a` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/grid-alignment-and-viewport-safety.md) |
| 39 | `grid-alignment-case.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/grid-alignment-case.md) | `4124a7cef3abcde1afe797a8fec15b970f3019e9` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/grid-alignment-case.md) |
| 40 | `icon-art-direction-gate.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/icon-art-direction-gate.md) | `471a88600dfa4de21cbca6ac50cd573c461a25f0` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/icon-art-direction-gate.md) |
| 41 | `liquid-glass-optics.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/liquid-glass-optics.md) | `5ee5e9eb7fe3793ffe6822fe3139bc86ada984bc` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/liquid-glass-optics.md) |
| 42 | `motion-and-interaction.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/motion-and-interaction.md) | `18f91b1211c64b526730f7b2c9e5b8f0d7ab52bd` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/motion-and-interaction.md) |
| 43 | `motion-consent-experience-gate.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/motion-consent-experience-gate.md) | `883c72333322bbdd365f59d8e9cbae03b50e6929` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/motion-consent-experience-gate.md) |
| 44 | `motion-craft-and-continuity.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/motion-craft-and-continuity.md) | `bb44c8655388042f60ec09ffa51711afcb9ba868` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/motion-craft-and-continuity.md) |
| 45 | `motion-governance.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/motion-governance.md) | `1c80b595b86a231da3a46d4dbcef11e971ea7cf4` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/motion-governance.md) |
| 46 | `motion-rehearsal-and-evidence.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/motion-rehearsal-and-evidence.md) | `889ade88401fdbef8d778ff685a69c9ae9afbf3a` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/motion-rehearsal-and-evidence.md) |
| 47 | `navigation-architecture.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/navigation-architecture.md) | `073e244710bcd1609fbd76f6130da743991e0d2e` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/navigation-architecture.md) |
| 48 | `overview-density-case.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/overview-density-case.md) | `e819742cea8e72a1760c0f43449b58e678e3ff91` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/overview-density-case.md) |
| 49 | `page-density-and-content-priority.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/page-density-and-content-priority.md) | `73eb0f2d57470dc9efed32fdcde45b3cd061b20a` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/page-density-and-content-priority.md) |
| 50 | `page-header-antipatterns.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/page-header-antipatterns.md) | `efe27572e9e8aa16f7410156ba5a080a03c19c2a` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/page-header-antipatterns.md) |
| 51 | `palette-art-direction.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/palette-art-direction.md) | `7b2a3152bde86c6f988a83653c795cbf9cd73969` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/palette-art-direction.md) |
| 52 | `perceptual-hierarchy-gate.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/perceptual-hierarchy-gate.md) | `fa0dbf03f6b354f0a769134b15ab24ab652616ba` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/perceptual-hierarchy-gate.md) |
| 53 | `proactive-visual-defect-discovery-gate.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/proactive-visual-defect-discovery-gate.md) | `3769a2c9c504c57d2f2b707beac5f218b113b5fd` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/proactive-visual-defect-discovery-gate.md) |
| 54 | `product-experience-routing-gate.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/product-experience-routing-gate.md) | `96c5823dc58690c78d152f21a8cf0e3482c828b2` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/product-experience-routing-gate.md) |
| 55 | `progressive-visual-refinement-gate.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/progressive-visual-refinement-gate.md) | `c6371dbdc546008abd443d62962a55b9aa047c83` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/progressive-visual-refinement-gate.md) |
| 56 | `project-design-hierarchy.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/project-design-hierarchy.md) | `43af8915968fc1aef77922facebf8e5c8df11510` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/project-design-hierarchy.md) |
| 57 | `quality-antipatterns-by-page-type.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/quality-antipatterns-by-page-type.md) | `387ccffd94ab8eb7caa6d0737d41210961e80700` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/quality-antipatterns-by-page-type.md) |
| 58 | `react-component-engineering.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/react-component-engineering.md) | `2c43e0d7069499b305cd36b9936675c2f24c9c1a` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/react-component-engineering.md) |
| 59 | `run-monitor-case.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/run-monitor-case.md) | `7782c48f9395e684a5688203d06e11e643ce8c89` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/run-monitor-case.md) |
| 60 | `semantic-boundaries.en.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/semantic-boundaries.en.md) | `429a07ed99df9b571252e6c61e3f04667070470c` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/semantic-boundaries.en.md) |
| 61 | `semantic-copy-hygiene.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/semantic-copy-hygiene.md) | `2d1abca7eab940709bc9a7927f8e2e45be72b078` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/semantic-copy-hygiene.md) |
| 62 | `semantic-spacing-rhythm-gate.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/semantic-spacing-rhythm-gate.md) | `2cbb2a2110490a344cd68069d50e5a630e152d76` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/semantic-spacing-rhythm-gate.md) |
| 63 | `settings-form-layout-gate.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/settings-form-layout-gate.md) | `fae7059ea6f6df0fe60e19ae0c223991e69de720` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/settings-form-layout-gate.md) |
| 64 | `sidebar-color-discovery.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/sidebar-color-discovery.md) | `33879e197ab9e8620957cc91b719ba8aceeb91f4` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/sidebar-color-discovery.md) |
| 65 | `sidebar-color-reference-cases.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/sidebar-color-reference-cases.md) | `30936dc0a62ce02f816cd05252251315b70256ba` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/sidebar-color-reference-cases.md) |
| 66 | `sidebar-navigation-design.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/sidebar-navigation-design.md) | `f42d9c6c9efd856259bfddd62b7f7d2e78b333fa` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/sidebar-navigation-design.md) |
| 67 | `sidebar-selection-indicator-gate.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/sidebar-selection-indicator-gate.md) | `1f13c124d8f497b932f769a5930b558e1305301d` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/sidebar-selection-indicator-gate.md) |
| 68 | `skill-gap-workflows.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/skill-gap-workflows.md) | `f6159cf32d290efbfb43bf285081dbf80319336d` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/skill-gap-workflows.md) |
| 69 | `spacing-regression-protection-gate.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/spacing-regression-protection-gate.md) | `f443e9d37e56ad534d8611fe00d6e54e875c31d3` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/spacing-regression-protection-gate.md) |
| 70 | `stack-guide-11-items.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/stack-guide-11-items.md) | `e274c5d28553ea1ae87d3be0cd6dec75b4a8f29f` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/stack-guide-11-items.md) |
| 71 | `surface-architecture-gate.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/surface-architecture-gate.md) | `3041d77ef06c1c6823a7bf68923e20813d479b74` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/surface-architecture-gate.md) |
| 72 | `surface-edge-accent-gate.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/surface-edge-accent-gate.md) | `ac15e458edcfbff8f25163fe20e22adacb359572` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/surface-edge-accent-gate.md) |
| 73 | `task-center-run-monitor-design.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/task-center-run-monitor-design.md) | `aca03a4c48a098023cc9e68213b7d7489e896ff1` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/task-center-run-monitor-design.md) |
| 74 | `theme-design.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/theme-design.md) | `a900781acce768df8bab0ae1461226c68b78b170` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/theme-design.md) |
| 75 | `typography-hierarchy.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/typography-hierarchy.md) | `03f9eb30b513e5bba9bf2e0b6a33814bf8d93664` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/typography-hierarchy.md) |
| 76 | `ui-review-rubric.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/ui-review-rubric.md) | `6f2838cb1bc91767a93c7eba09748a04731e487b` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/ui-review-rubric.md) |
| 77 | `visual-critique-loop.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/visual-critique-loop.md) | `6bebbebfd12552c11b1f25f0762273e42f44828a` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/visual-critique-loop.md) |
| 78 | `visual-qa.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/visual-qa.md) | `6057f0365bf46114ec02898300661252536844fa` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/visual-qa.md) |
| 79 | `visual-tech-selection-12.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/visual-tech-selection-12.md) | `8dd9131e5db847eab14aa303069e827966e697eb` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/visual-tech-selection-12.md) |
| 80 | `vue-component-engineering.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/vue-component-engineering.md) | `4dc5a92eb495ac4dba096ea92e1341e80bd2e322` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/vue-component-engineering.md) |
| 81 | `web-scope-and-app-types.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/web-scope-and-app-types.md) | `5fe008b7091b3a19fd669138aca0aa87b728e2e9` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/web-scope-and-app-types.md) |
| 82 | `whitespace-and-surface-composition.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/whitespace-and-surface-composition.md) | `f35b192e8eb37bef0042e525ca25fda7ae64bc64` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/whitespace-and-surface-composition.md) |
| 83 | `workspace-component-refinement.md` | [中文源](https://github.com/MauriceLiang/MauForma/blob/54a4af62566da1532c2b68d4301b531aee118e81/references/workspace-component-refinement.md) | `08eabd4a8b86127c3f1bfa14c26a76e43d9afc38` | [英文现行](https://github.com/MauriceLiang/MauForma/blob/main/references/workspace-component-refinement.md) |

### 不属于 83 份翻译范围的资料

- 原有英文专项资料（4 份）：`references/component-consistency-and-selection-gate.md`、`references/execution-handbook.en.md`、`references/expressive-motion-vocabulary.md`、`references/title-prefix-role-gate.md`。
- 有意保留的中文规则核对文档（1 份）：`references/semantic-boundaries.zh-CN.md`。
- 中文 README 是面向开发者的用户文档，不作为第二套 Agent 指令。

## 5. 后续变更的语义回归操作规程

1. **标记范围**：列出发生变化的英文路径、关联 B 编号、受影响的用户权限或技术约束；与 83 份原始资料无关的新功能也要记录新规范的批准来源。
2. **回到中文源头**：对受影响的历史规则打开上述固定提交文件，摘出完整中文上下文，包括紧邻例外、禁令、数据类型、数值、示例和前后依赖；不要只看短语锚点。
3. **逐项核对**：至少检查触发范围、主体责任、`必须/应当/可以/不得` 强度、授权前提、例外条件、时间/数量/平台约束、实际验收口径八类。对否定词、条件分支、隐含主语、排他性和翻译后新增义务尤其谨慎。
4. **处理差异**：只因翻译不准而修英文，不得擅自改变中文原意；如果确为用户批准的规则升级，单独记录审批依据，并同步更新对应的中英文语义描述与结构化契约。不要覆盖固定中文原始基线或其 SHA。
5. **补回归案例**：给高风险语义增加可复现的正例、反例或双语任务场景。应能检测失去禁止项、扩大例外、调换强制程度以及把 `NOT TESTED` 误报 `VERIFIED` 等回归。
6. **测试和复核**：运行仓库文档与语义门禁、单元测试，检查相关链接和 B01–B15 配对；重点由双语审阅者结合完整上下文核查。静态检测通过之后，仍不能宣称真实 Agent 或浏览器已验收。
7. **记录证据**：每次影响规则意义的 PR 写明中文原文定位、英文修改、可能的歧义、审核者/方式、测试范围、尚未覆盖的行为。只更新措辞不改规则也需要明确说明。

### PR 语义变更记录模板

| 项目 | 应填写内容 |
| --- | --- |
| 文件 / 规则 ID | 例如 `references/...`、B04 |
| 中文基线 | 固定 commit + 文件 + 原文段落 / 行定位 |
| 新英文条款 | 完整句子，不能只写一个关键字 |
| 必须 / 例外 / 禁止 | 逐项指出保留或改变的条件 |
| 修改类别 | 仅修复翻译 / 用户批准的规则变更 / 新增概念 |
| 容易误读的反例 | Agent 可能怎样错误执行 |
| 证据与结论 | STATIC CHECK / BILINGUAL REVIEWED / BEHAVIOR VERIFIED；列出实际证据和未测试项 |

**长期原则：保留原中文可追溯性，英文负责执行，双语对照负责防止含义偏移。** 不因英语表达简洁而省略中文里的限制条件，也不因中文版本存在就忽略后续经批准的新规则。

## 6. 2026-11-22 新增规则：主标题自足（Gate H-S）中英语义回归

> **规则来源：**本次用户明确批准的通用设计规则升级，不属于 83 份历史中文原稿的机械翻译。不可变原始 Git 基线及原文件 SHA 保持不变。英文执行入口为 `SKILL.md` 和 `references/title-prefix-role-gate.md`；本节只提供中文语义对照与防曲解检查。

| 中文设计意图（必须保持） | 英文执行契约（含义对应） | 防止的误解 |
| --- | --- | --- |
| 默认仅用一个清晰、能独立说明内容的标题，不主动生成标题前装饰性说明。 | Self-sufficient heading by default; no separate pre-title line. | 不能先生成小标题再找借口保留。 |
| 删除上方文字不会损失**独立的、必要的**用户信息时，应删除。 | If removal loses no independent user information, DELETE. | “有助于理解”“补充上下文”“更精致”本身不是必要信息。 |
| 小标题有独立信息价值，也**不自动取得**放在标题上方的资格。 | Prove independent information **and** above-heading placement independently. | 不能把“有意义”偷换为“应该放在上方”。 |
| 真正的面包屑、章节、步骤、状态、来源、权限、品牌身份不得盲删；优先移到正确语义位置。 | Preserve real navigation, chapter, step, state, source and approved identity; prefer MOVE/MERGE to semantic owner. | 不能一刀切删除、隐藏或误改真实信息。 |
| 所有页面类型和 H1–H6、卡片、分区、弹窗都适用，既有内容不豁免。 | Every page type and heading group, inherited and new content. | 不能只检查任务页 H1 或只修新写的组件。 |
| 对尚未完成语义判断的候选，不得声称视觉验收通过。 | Unreviewed candidates block VERIFIED; before/after closure requires evidence. | 不能以扫描脚本、合成测试或通过 CI 冒充真实产品验证。 |

**回归判定：**若英语表述弱化了默认无前导、信息损失举证、保留位置举证或既有内容整改，应认定为语义漂移并补测。若英语表述导致删除真实导航、章节、信息来源或已批准的品牌叙事，也应认定为错误。

**工具边界：**`scripts/audit_readability.py` 只是静态候选提示；`scripts/audit_title_prefixes.mjs` 发现实际 DOM 候选但不会决定语义；`scripts/validate_title_prefix_review.mjs` 只检查每个候选是否有决策、保留证据及前后关系是否处理，不自动证明保留理由真实、UI 美观或业务行为正确。真实页面仍需人工/Agent 观察与复验，无法运行则标为 STATIC CHECK / NOT TESTED。

