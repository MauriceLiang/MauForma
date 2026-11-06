# Spacing Regression Protection Gate · 独立模块间距不可被无意抹除（v6.19）

跨框架、跨网站类型适用。与 `references/semantic-spacing-rhythm-gate.md` 配合：v6.16 规定如何设计空间关系，但过去默认 Agent 会给实际 DOM 加空间标记和执行契约，遗漏时仍能把大区块的 `row-gap` 清零并误称页面“更紧凑”。这版把**现有布局的间距保留与回归检查**提升为更新/优化时的硬门禁。

## Gate SG0 · Preserve by default：设计优化不能擅自消灭既有留白

- 用户要求“优化”“更精致”“清爽”“让首屏装下更多内容”“简约/低密度”等，并不意味着授权把**原本独立的模块**拼接、把 `row-gap` 归零、删掉父 `gap`、或用负 `margin` 收缩视觉分隔。
- 必须在改布局前识别“可保留的组间节奏”（尤其是指标条 → 主图、主图 → 次级统计、并排卡片 → 下一行、分析卡 → 资料摘要、表格 → 独立帮助区）。确定这些区域是否是 `section / peer / inside / connected / anchored`。
- **独立模块的间距是受保护的设计状态**：除非用户要求改变、同一模块职责确实合并（并有结构理由）、或新的布局在用户确认的密度方向下确有更好的视觉层级，否则不得主动大幅收紧，更不能把它们变成零间距；如需改变，说明前后值、影响和依据，而不是将其当“代码简化”。
- 为减小高度，应优先审查重复解释、无效表面、过长图表占位、无价值功能模块、行内密度或可滚动布局；**不能通过删除所有外部 gap 逃避内容/密度设计**。
- 不把某一个具体项目的空隙、像素和模块命名写入全局默认；紧凑风格也需要足够清楚的组间关系。紧邻的连续表头与表体、Tab 与 Panel、分段控件及连续时间轴是合理的零间距例外。

## Gate SG1 · Layout regression checkpoint（优化前和优化后）

1. 在同一应用真实路由、同一数据状态、同一 viewport / 字体比例下，**先拍并观察整页前态**，从真实 DOM 读取主要独立模块的可视间隔。若源项目已有官方 spacing tokens / approval 记录，先继承。不要把新建示例页的正常表现冒充旧页面的基线。
2. 为所有高价值独立模块建立明确的 `section/peer` 关系；若已能写出精确契约继续执行 `scripts/audit_spacing_rhythm.mjs`。若 Agent 未预先添加 `data-mf-space-id`，先执行新增 `scripts/audit_panel_spacing.mjs` 自动扫描实际页面里的主要 bordered/card-like surfaces，**不能以“没有标记”为借口跳过风险评估**。
3. 按相同视口/字体比例保存 `before.json`，完成修改后生成 `after.json`，启用 `--baseline before.json` 对比。失去大量间距（即使新 gap 非零）、出现独立 surface 共边或压叠，视作回归，进入修复循环。
4. 自动扫描是**启发式风险扫描**，不能准确理解所有自定义视觉边界：对透明、开放式、Canvas、position:absolute、CSS transform、跨组件 Portal 等需要补充显式语义关系、全页截图和人类审查。自动扫描找不到 panel pairs / 基线不可比时必须**报告未覆盖**，不能宣称“空间质量通过”。
5. 显式的 `connected` 可用 0 gap，但应说明结构语义与为何共边。例如演示或目标页面中有 `data-mf-connected-reason="Tabs and the immediately associated panel are one continuous control"`；不可给所有父节点都填写“connected”来掩盖零间距。该属性只用于**明确确实为单一结构的容器**，需人工审查。
6. 除几何审查外，仍需完整界面截图（含首屏/中间/滚动末尾）与交互时状态；扫描脚本并不能证明视觉审美、设计意图或完整覆盖。

## Gate SG2 · 典型错误与正确的结构修复

```css
/* 错误：压缩高度时把完整区块的间距一起清除 */
.analysis-stack { display: grid; row-gap: 0; }
.analysis-stack .chart-grid { column-gap: var(--peer-space); row-gap: 0; }

/* 正确方向：维护独立模块关系，由父布局决定真正的 gap */
.analysis-stack {
  display: grid;
  row-gap: var(--section-space);
}
.analysis-stack .chart-grid {
  display: grid;
  grid-template-columns: repeat(2, minmax(0, 1fr));
  column-gap: var(--peer-space);
  row-gap: var(--peer-space);
}
@media (max-width: 48rem) {
  .analysis-stack .chart-grid { grid-template-columns: minmax(0, 1fr); }
}
/* 连续 Tab + 面板可保留零间距：它们不是两个独立分析模块 */
```

CSS 只是关系示例，不代表给所有产品施加固定值。不要用强制 `margin-bottom:16px` 普遍覆盖组件 CSS、`!important`、隐藏溢出或大 `padding` 伪装实际独立间距。

## Gate SG3 · 低开销 Browser 检查用法

在已有项目（装有 Playwright）：

```bash
# 本页例子使用开发服务器 URL，必须由实现者换成当前真实产品页面
node scripts/audit_panel_spacing.mjs --url http://localhost:5173/example --out before.json
# 完成 CSS/布局优化、保持同样页面/视口/数据后再执行
node scripts/audit_panel_spacing.mjs --url http://localhost:5173/example --baseline before.json --out after.json
# 有明确模块关系的页面继续运行更严格的 token/关系契约审查
node scripts/audit_spacing_rhythm.mjs --url http://localhost:5173/example --contract spacing-contract.json
```

- `UNJUSTIFIED_PANEL_CONTACT`：自动发现大尺寸、可见、独立候选 panel 共边。
- `SPACING_REGRESSION`：相比之前的同一 DOM 关系，大幅压缩了原有 gap，不会因新 gap > 0 自动通过。
- `ASYMMETRIC_GRID_SPACING`：同行有 gutter 但行距塌陷的提示，需要结合实际是否存在多行判断。
- `INSUFFICIENT_COVERAGE` / `NO_COMPARABLE_PAIRS`：不能证明通过，需要补充明确的语义契约或人工验证。
- `VERY_TIGHT_PANEL_GAP`：提示人工判断，不强行把所有紧凑设计判成错误。
- `data-mf-connected-reason` 例外不是默认跳过检查的许可证；有意连体必须记录用途和结构原因。

注意：自动脚本只识别有限的**同一 Grid/Flex 父级下，具有明显边框/表面特征的区域**，不会凭空推断所有语义，也不会保存截图。为真实项目提供风险筛查，不是自动审美评分。

## Gate SG4 · 强制交付声明

当用户要求实际页面优化，Agent 交付时必须报告：
- 调整了哪些**独立模块之间的间距关系**，哪些保留不变，哪些有明确授权被压缩；
- 是否对**真实页面**而非 standalone 演示运行浏览器测试，覆盖哪些宽度和字号；是否执行 before/after 对比；
- 是否仍有未覆盖模块、可能的误报或可访问性问题；
- 不能用“调整了 padding”“组件通过”等描述冒充组间间距通过。

## 与其他 Gate 协作

- `references/semantic-spacing-rhythm-gate.md`：决定空间关系与间距角色。
- `references/grid-alignment-and-viewport-safety.md`：Grid 行列、断点、滚动到底安全。
- `references/whitespace-and-surface-composition.md`：留白/视觉权重与 Surface 决定。
- `references/control-geometry-gate.md`：不能因恢复间距导致按钮挤压。
- `references/design-reference-learning-gate.md`：用户提供的参考图像与可识别信息不得进入公开仓库或 CI fixture。
- `tests/panel_spacing_browser_smoke.mjs`：原创合成布局的正/反例，不使用任何用户截图或业务记录。
