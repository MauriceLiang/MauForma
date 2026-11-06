# Proactive Visual Defect Discovery Gate · 模糊优化请求必须主动找问题（v6.20）

MauForma 是设计与实现 Skill，不只是把用户明确指出的问题翻译成 CSS。**当用户只说“优化一下页面 / 打磨视觉 / 看起来更专业 / 用 MauForma 改进”时，Agent 必须先主动检查真实页面，建立缺陷清单，再选择并完成最有价值的修复。** 不得以用户没有逐条指出问题为由跳过页面整体审查；也不得未经授权改变既定品牌、数据含义或动效决定。

## Gate D0 · 任务语义决定默认模式

| 用户表达 | 默认路径 | 避免 |
| --- | --- | --- |
| 模糊的视觉优化、精修、提升观感、改好看 | **diagnose → prioritize → repair → verify**；整页主动审查，优先真实缺陷 | 只统一字号/圆角/配色然后宣布成功 |
| 用户指出一个视觉问题（如模块贴合） | 先诊断该问题和直接相关邻接区域 → 修复 → 检查是否带来新问题 | 仅改一段 CSS 不看相邻布局 |
| 只要求具体 Bug（如修复搜索提交报错） | 有边界的局部修复与相关 UI 回归 | 为此强制整个网站重设计 |
| 只请求评估/报告，不授权改代码 | 诊断与排序，报告问题和原因，不改仓库 | 自动动用设计系统改动 |
| 没有可访问的运行页面 | 静态样式/布局结构审查 + 用户提供的截图分析；准确标注未验证范围 | 假装跑过浏览器或只展示演示页结果 |

## Gate D1 · First inspect, then design：缺陷清单不是装饰性流程

启动页面优化时按优先级扫 **真实页面**（当前路由 + 相关状态 + 滚动中部/底部）：

1. **结构/空间**：独立 Section、同级数据卡/图表行与相邻全宽区块是否意外零间距？先从当前页面识别已存在的缺陷；保持良好间距，但不能因为“保留现状”而保护已经错误的零间距。卡片内 padding 无法代替外部 gap。检查横纵分离：同排有列间距而下一排完全贴上去也是错误信号。
2. **层级/文字**：P0/P1 是否过小或太淡？有没有大字体无信息量装饰占主次、正文难读、数据标签和图轴模糊？
3. **组件/内容**：是否所有功能都包巨卡、多个独立卡片视觉粘连、按钮尺寸与用途不符、表格/列表密度不适合业务、空数据却用大占位？
4. **图标/色彩**：图标语义、轮廓、光学重量和文字是否协调？色彩是否服务品牌/状态，而不是无理由铺强饱和块？注意用户已有配色选择不得擅改。
5. **交互/响应式**：选中、hover、focus、加载与错误状态是否有效？Tab/弹窗/筛选是否真实可用？文本放大、窄屏和滚动到底是否不溢出、不遮挡？动效遵循已选强度。

至少挑出能够从运行页面或可信源码佐证的 **Top 3 风险项**；没有真实缺陷不能硬凑三个“为了设计而设计”的问题。按严重性/用户收益排序，不只挑容易改颜色的低价值项。

输出精简审查记录可用 `page | issue | evidence | confidence | impact | severity | proposed fix | verification`；代码修复前确认**语义关系**：独立的应分开，真正连体的可共边。仅把所有 gap 变成固定 16px 不算设计。

## Gate D2 · 先发现已存在的问题，再做前后回归

v6.19 的 `before → after` 检查防止**引入新的退化**，但无法检测 before 中已经存在的缺陷（如原本两个独立 Card 就粘在一起）。因此必须双路径：

- **发现当前缺陷（本版新增）**：`node scripts/audit_existing_visual_defects.mjs --url <current-page> --out /tmp/visual-audit.json`。它**不需要 before 基线，也不需要添加 DOM 标记**，能在实际渲染的普通 Block 流、Grid/Flex 和透明包装层内寻找明显边框 panel 的相互贴合。它复用原有 `audit_panel_spacing` 风险扫描，对可见的连体结构提供有理由的例外。
- **保护已正确的部分（v6.19）**：修改前后用 `scripts/audit_panel_spacing.mjs --baseline before.json`，防止正常间距大幅缩小。默认保留**良好设计和已经确认的空间角色**，但不能把“保留历史坏状态”作为忽略缺陷的理由。
- **有业务语义契约时**：`scripts/audit_spacing_rhythm.mjs --contract ...` 继续负责明确的间距角色/Token。无标记真实页面不能只报告这个脚本的 Demo PASS。
- **重点补充人眼判断**：Canvas 绘图、背景透明无边框区块、portal、sticky、动画/滚动、叠层、复杂布局不一定被 DOM 启发式识别。少量距离不是所有场景都有错，错误主要是**无意且不相干的模块接触**。几何工具报错应先确认语义再修，工具 PASS 也不证明审美合格。
- **主动判断异常结果**：如果扫描没发现有意义的 panel 或缺乏访问权限，结果是 `NOT AUDITED` 而不是 `PASS`。仍然尽力审已有截图、DOM 与 CSS，报告盲区；不借机要求用户提供重复信息。

## Gate D3 · 修复闭环：不只是在报告中列出问题

1. 给每个 P0/P1 缺陷附上实际位置与具体原因；如果证据充分且在授权范围内，应真正修改样式/布局/组件代码；需要改变品牌/高风险行为的方案需遵循现有用户决策门禁。
2. 先修结构和空间角色，再调色、字体细节或动效。空间问题优先修改父 Grid/Stack 的 gap/布局关系，而不是在每张卡片用负 margin、`!important` 或内部 padding 伪装。
3. 修后重载**同一个真实页面**，对原问题重新诊断，比较视觉效果；旧问题仍然存在不得宣布验收完成。保留合法 `connected` 例外，且不允许通过把全站统一标记为 connected 绕过问题。
4. 同时检查响应式、200% 字体、状态变更与滚动终点。只跑独立演示页的 smoke 测试不能证明目标应用已修复。
5. 交付结果区分 `FOUND → FIXED → VERIFIED`、`FOUND → UNFIXED(reason)`、`NOT AUDITED(reason)`。可以给出持续性问题，但不能将“跑了一条脚本”直接称为完成设计。

## Gate D4 · 限制与隐私

- **不推断来源归属**。用户提供的设计截图仅用于当前分析；明确不入仓时，不得把截图、裁剪、模糊处理后的图、可识别数据、URL、PR 附件或测试截图提交到公共仓库。
- 浏览器脚本默认只输出抽象几何，CLI URL 由使用者提供；对于含私人/商业信息的真实应用，不应自动把原始截图上传 CI artifact 或写到公共仓库。
- 本 Gate 不是全站强制一个 UI 模板；Operate、Persuade、Read、Experience 四类页面均使用同一诊断流程，但有不同的图文比例、空间表达和密度。
- 语义明确的不同模块即使处于“克制/极简”风格，也不应无意共边；真正组合表面可以继续 0 gap。判断的是**关系**，不是“一刀切所有模块 16px”。

## 执行检查

- 参考：`references/spacing-regression-protection-gate.md`、`references/semantic-spacing-rhythm-gate.md`、`references/visual-critique-loop.md`、`references/browser-qa-protocol.md`。
- 模糊意图触发示例：`assets/proactive-audit-trigger-cases.json`、`scripts/validate_proactive_audit.py`（静态决策，不证明 AI 必然执行）。
- 不依赖基线的浏览器风险检查：`scripts/audit_existing_visual_defects.mjs`、`tests/existing_visual_defect_browser_smoke.mjs`（原创合成 DOM，非用户源图）。
