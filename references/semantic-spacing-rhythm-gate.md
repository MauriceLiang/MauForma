# Semantic Spacing & Spatial Rhythm Gate · 用模块关系决定间距（v6.16）

适用于所有 Web（Operate / Persuade / Read / Experience）、全部框架和视觉风格。**布局对齐 ≠ 模块间距正确**：两个分析图表可以共享边界和行起点，却因纵向 `gap:0` 与上下卡片贴合，导致信息区域像一整块没有节奏的白板。仅修圆角、加阴影或单独给每张 Card 增加 padding 都不能解决“组与组的关系”。

## v6.20 · 默认优化先发现坏的原状，再保护好的间距

如果页面一开始就把两个独立 Section 拼在一起，v6.19 的“保持原有间距”不能证明那种状态合理。泛化优化首先执行 `references/proactive-visual-defect-discovery-gate.md`，对真实页面调用 `scripts/audit_existing_visual_defects.mjs` 无基线/无标记风险发现，区别普通 Block Flow、Grid/Flex 和简单包装层。现有错误应修复；原有良好的 spacing 再由 before/after 保护。脚本识别的主要是明显面板，开放式/Canvas/复杂嵌套仍需视觉审查。

## v6.19 · 已有间距不允许在优化中无意清零

v6.16 的显式契约只在 Agent 标记 DOM 时有效。所有已有产品的视觉重构还必须执行 `references/spacing-regression-protection-gate.md`：先记录真实页面的 before 空间关系，保持独立模块的正常 gap，再在 after 实测。没标记也先用 `scripts/audit_panel_spacing.mjs` 对 Grid/Flex 中明显的 Card/Panel 做启发式扫描（可发现 0 gap 和基线大幅缩水）。不要把“更紧凑”解释为 `row-gap:0`；只用独立样例测试不能交付真实页面，复杂开放式模块未被脚本识别时需说明并人工复核。

## Gate SR0 · Spatial Relationship Map（先辨认空间关系，再分配距离）

对实际页面的可见区域建立简单关系图（不用问用户每一处距离）：明确父级布局、相邻对象、阅读顺序和下列一种关系：

| 关系 | 判定问题 | 典型场景 | 空间策略 |
| --- | --- | --- | --- |
| **inside（内部从属）** | A 是 B 的标签、单位、说明或正文吗？ | 标题与副标题、图表标题与图表、字段与帮助文案 | 近且可感知归属；内部 padding 与内容空隙协调 |
| **peer（同组同级）** | A 与 B 同一网格/功能组，是否等权？ | 并排两张图、功能选项、作品网格 | 同一行/列的节奏稳定，横纵 gap 不因 CSS 嵌套而随机归零 |
| **section（不同功能区）** | 是否跨越独立任务、分析主题或信息章节？ | 指标概览 → 分析图 → 数据质量 → 限制说明 | 清晰的组间区隔，通常大于内部文字间距；可由背景/边界辅助但不机械叠加 |
| **connected（有意连接）** | 两者是否构成单一结构/表面，边界接触有意义？ | Tabs 与面板、表头与表体、连续时间轴、相邻工具条 | **允许 0 gap / 共边**；需要共同表面、边界或交互语义理由 |
| **anchored（锚定/重叠）** | 弹层、徽标或媒体覆层是否明确附着某元素？ | Popover、Tooltip、图片角标 | 由定位与可访问性决定，可重叠；不按普通 sibling gap 报错 |
| **editorial / expressive（叙事性）** | 不规则空间是否有明确的阅读/构图意图？ | 杂志布局、作品展示、大幅主视觉 | 可非等距、非对称；需要可讲清的设计目标，不能用“随机留白有设计感”搪塞 |

**先画出关系，再决定数字。** 项目可以有很紧凑的高频工作台，也可以有宽松的品牌页。不要为了避免 0px 告警就让全部间距变成 32px；“连接”本身也不是错，错误在于没有连接理由的模块贴合。

## Gate SR1 · 三层节奏（语义 Tokens，而不是全站固定 px）

在当前项目已有 spacing scale 上选映射，作为布局契约：

- `space.inline`：图标/文字、Badge 内、单位/数值等；与控件 typography/点击区协同。
- `space.inside`：标题与说明、图表标题与图、卡片内段落/字段；按视觉重心与内容实际高度调整。
- `space.peer`：同一集合的卡片、图表、表单项或对象；同一结构中的水平/垂直间距要有**有意一致或有理由的变化**。
- `space.section`：独立章节/主题/业务区域之间的分隔；通常能明显区别于卡片内部 micro spacing。
- `space.page`：PageHeader → 主体的起始节奏、上下安全空间、主要区块与固定元素边界。

**不规定这些 Token 必须取不同值，更不规定必须按 8px 倍数。** 少数高密度/层叠结构可复用值；需要设计理由。主要结构间距应从父 `gap/row-gap/column-gap`、Stack、Space 组件或布局 Token 控制，不能让每张 Card 自己决定随机 margin。内边距（padding/inset）和同级元素间距（gap）属于不同职责：增加 padding 并不能替代外部 gap。

可选起点（非自动强制值）：紧凑分析可从 4/8/12/20/28 的角色梯度尝试；文档和营销可更大；混合中文字体、数据图表、按钮高度、当前视口和真实密度可改变选择。比例比单一固定数值更重要，**但“section 必须严格为 inside 的 2 倍”也不是法则**。

## Gate SR2 · Spacing Rhythm & Optical Review

1. **纵向检查**：页面标题与描述、摘要/顶部对象块、第一排图表、第二排图表、脚注/限制是否存在有意的节奏？独立模块不能因为容器 `row-gap:0` 或边框接壤变成连续大白块。
2. **横向检查**：同一行双卡、工具栏与主图、列轨之间的 gutter 和左右对齐是否一致？`column-gap` 非零不代表 `row-gap` 自动合理。
3. **视觉权重**：大图表、高彩度图、图片和大标题需要怎样的“呼吸空间”？小表头/注释不能比其所属图表离得更远，导致关系断裂。
4. **边框/背景感知**：相邻白卡同为浅灰细线时，即使物理间距不为零，视感仍可能融在一起；可选择增强父级留白、降低多余边框或改变背景层次，优先保证信息结构而非叠加影子。
5. **不同模式例外**：Dashboard 可以紧但不能同主题“无意粘连”；Editorial 的长文连续段落可以少框；Store 的商品网格 peer spacing 可紧凑，关键商品介绍和购买路径需要有呼吸；作品的非对称空间可服务艺术表达。
6. **动态与状态**：空/加载/错误、展开折叠、Tabs 切换、响应式断点、sticky/固定底栏和文本放大时，组件仍保有合适的语义间隔；**不要强行给错误空态指定大固定高度**。
7. **视觉微调**：先用 Token 保证结构一致，再依据字体/图像的“光学边界”小幅调整。Optical adjustment 不能把组件之间的网格关系打散，也不能通过负 margin 隐藏真实错位。

## Gate SR3 · 可移植实现建议（以下数值仅为演示）

```css
/* 只展示“由父级负责布局”的思想。实际项目沿用现有 token。 */
.research-page {
  --space-inside: 0.5rem;
  --space-peer: 0.875rem;
  --space-section: 1.25rem;
  display: grid;
  gap: var(--space-section);
}
.research-page__chart-row {
  display: grid;
  grid-template-columns: minmax(0, 3fr) minmax(0, 2fr);
  gap: var(--space-peer); /* 同时服务行/列 */
  min-width: 0;
}
.research-page__panel {
  min-width: 0;
  /* 单个 Card 的内边距不负责与下一张卡拉开距离 */
}
.research-page__heading {
  margin-block-end: var(--space-inside);
}
@media (max-width: 48rem) {
  .research-page__chart-row { grid-template-columns: minmax(0, 1fr); }
}
/* 有意一体式 Tab+Panel 可用 connected 模式而非统一加 gap */
```

避免：所有模块堆在 flex column 而未设 `gap`、`row-gap:0` 但 `column-gap:12px`、靠 `:last-child` margin 或绝对定位硬凑、向所有 Card indiscriminately 加 `margin-bottom` 导致 Grid 二次叠加、用 padding 取代外部间距、为使内容“贴齐首屏”压缩全部 gap。

## Gate SR4 · Browser Geometry + Perceptual QA（两者缺一不可）

1. **设计证据**：至少记录主要独立区块/同级卡片/内部标题的关系及各自 spacing token，明确 intentional connected/overlap 的理由；局部修复只针对受影响的关系，不重新访谈。
2. **浏览器检查**：1280×720、1440×900、390×844、320 宽度等可作为候选，重点是真实目标用户屏幕。测量独立区块的边界距离，发现重叠或零间距；宽窄断点需确认横向同行变成纵向堆叠时，**gap 不会突然归零**。
3. **同级节奏和层级**：判断 peer gap 是否合理一致、section 是否能与 inside 区分、父布局是否留有垂直节奏；若页面有意 connected 可以贴边，但须在契约中声明。
4. **全页与末端**：包括首屏、图表后的部分、滚动末端和固定操作条安全距离。不要把正常滚动当 Bug；不能用全局 `overflow:hidden` 遮蔽问题。
5. **静态契约与运行时几何**：`scripts/validate_spacing_rhythm.py --repository` 验证通用设计样例；`scripts/audit_spacing_rhythm.mjs --url ... --contract ...` 可测显式标记的区域。只有有标记的真实页面/契约才能得出有限范围的几何结论；不要声称自动审计证明“审美高级”。独立演示 `assets/spacing-rhythm-lab.html` / `tests/spacing_rhythm_browser_smoke.mjs` 会故意包含贴合反例验证测试能报警。
6. **与已有 Gate 联动**：先审 `references/surface-architecture-gate.md`：一个区域是否需要边框和独立容器；再联动 `references/grid-alignment-and-viewport-safety.md` 确认上下行/列线、`references/perceptual-hierarchy-gate.md` 确保不同组的视觉重要性、`references/control-geometry-gate.md` 防止间距优化后控件被挤压。

## 官方依据及迁移边界

- Carbon Spacing：空间 Token、元素关系、层级和视觉留白；https://www.carbondesignsystem.com/building-blocks/foundations/spacing/overview
- Atlassian Spacing：按相似性/邻近性分组，建立节奏，并允许光学校正；https://atlassian.design/foundations/spacing

上述产品的像素数是各自 Design System 的实现，不是 MauForma 面向所有项目必须照抄的值。
