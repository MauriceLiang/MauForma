# Chart Interior QA · 图表绘图区，而不只是 Card 边缘（v6.10）

> 例子：用户的 RepoVantage 发布间隔柱图与发布节奏散点图，外框顶部、底部差不多，但 Plot Area 高度、日期轴、图中文字以及图例仍然明显不协调。右图高位标签和均值标签接近重叠，说明只用 `getBoundingClientRect()` 审查卡片并不够。

## 对齐不是强行设置每张 canvas 同高

- **框架**：Panel header/title/description → plot viewport → axes/labels/legend → footnote/disclaimer，每层有自己的 spacing role。
- **基线**：相同的时间窗口、同类量纲的多图有可对照的 X 轴/绘图区起点；不同量纲/图型可以有不同 margin，但都应有明确视觉分区。
- **留白**：不能在右图内部放大量完全空白的 plot area，让数据点挤在中间，然后和左图的占满数据区硬凑外框高度。允许增加有用图表高度或改变绘图类型。
- **标签**：重叠时采用库内 `labelLayout`（ECharts 支持时）、`hideOverlap`/formatter/位置偏移/tooltip 等策略，并在实际窗口截图中确认；要避免修掉一个标签导致另一个被图框裁切。
- **状态**：没有真实数据时显式空态，不绘制无限接近 0 的“假曲线”；0 与 null 截然不同。
- **审查证据**：浏览器 geometry + 截图，必要时对 Canvas 使用图表组件的渲染 API/截图审查。无法分析的标签状态记录 NOT AUDITED。

## 自动审核的边界

`scripts/audit_comparison_ui.mjs` 可比较已标注 chart plot 的同组 top/bottom、可读的 SVG/HTML 标注 bounding rect、容器横向溢出及内容底部；但是 Canvas 内数字、tooltip 和遮罩若没有可访问的 DOM，浏览器通用脚本无法推断所有文字。这不是自动化可修复的视觉 Bug 清单，Agent 必须检查真实浏览器截图。
