# Grid & Viewport Integrity · 统一对齐与底部安全（v6.9）

> 合成反例：左右独立纵向堆叠的模块可能出现第二排错位，固定底栏可能遮挡内容。前者需查看布局证据；后者必须在真实浏览器中滚动到底验证，不能仅凭截图断言。

## Grid 对齐与空间节奏是不同的验收项

横向列 gutter 合理，不代表纵向同行/跨行 `row-gap` 可以取消。更新已有页面前应保存独立模块的基线，参照 `references/spacing-regression-protection-gate.md`，在相同视口/字号/数据下比对后态。无 DOM 标记可用 `scripts/audit_panel_spacing.mjs` 发现常见面板共边；合法的 Tab/Panel 连接除外。没有足够检测覆盖时不能宣布已通过。

## 对齐通过但间距不通过的独立判定

同一 Grid 的行起点、列线完美对齐，并不代表模块的**组内/组间间距**正确。尤其是并排双图表拥有 `column-gap`，但图表行与后续全宽模块之间 `row-gap:0`，会让页面形成大片无意贴合面板。新设计与大改版在通过 Gate G1 之后还必须执行 `references/semantic-spacing-rhythm-gate.md`：区分相邻独立章节和有意连接的同一结构，验证空间角色、同级横纵节奏与移动单列后的 gap。滚动末端安全 padding 不等于“章节间距”，不要互相替代。

## 核心判断

**不对称（asymmetry）≠ 不对齐（misalignment）。** 数据看板优先共享列线、行线、卡片边界及可比较对象的轴/表头基线。不同宽度/高度/错列仅在信息重要性、阅读顺序和内容比例有明确理由时采用。摄影瀑布流/创意刊物可以例外；分析图表、统计表、发布记录不默认 Masonry。

## Gate G1 · 先定义「对齐契约」，再决定 CSS

1. **统一内容边界**：Side/Main/Topbar 间的内容区域有一个起点；PageHeader、Filters、Section、Charts 的主左/右边缘共享可追踪列线。不要每个卡片单独设左 margin 使横向边界漂移。
2. **同级模块行起点**：两张同级图表同排时共同 top；若上一排高低不同，下一排仍从同一个新的行起点开始。不要「左列连续向下排、右列连续向下排」造成第二行交错。
3. **统一跨行列结构**：首选单个 CSS Grid、共用列轨/行轨；可以 8:4/7:5、主图跨全行，**不强制 50:50 或所有卡片等高**。对不同用途的内容允许宽度有差异，但理由应从业务出发，不能每排重新随机分栏。
4. **图表内部对齐**：同主题图表的标题、单位、时间范围、图例、轴标签可比较，必要时做相同 plot padding 或组件 Token。**不要为了对齐强制所有图表具有同一 y 轴刻度或伪造同一数据范围**。
5. **留白不是空白填充**：如果单个区域特别高/短，先考虑更合理的跨行重组、合并重复图表、全宽主图，再考虑行拉伸；不能靠 `min-height: 600px` 和无意义占位硬凑行高。
6. **例外理由必须可见**：艺术画廊可采用 Masonry、时间线可错位、嵌套导航可独立滚动；对专业工作台，若选择刻意错列，需要记录它如何帮助理解，而非仅“设计感”。

## Gate G2 · 两类合法的布局结构

### A. 分行而非分列独立堆叠（适合对比模块）

```css
.release-dashboard {
  display: grid;
  grid-template-columns: minmax(0, 3fr) minmax(0, 2fr);
  grid-template-areas:
    "timeline intervals"
    "frequency releases";
  gap: var(--space-section, 20px);
  align-items: start;
}
.release-dashboard > * { min-width: 0; }
.timeline { grid-area: timeline; }
.intervals { grid-area: intervals; }
.frequency { grid-area: frequency; }
.releases { grid-area: releases; }
@media (max-width: 900px) {
  .release-dashboard {
    grid-template-columns: minmax(0, 1fr);
    grid-template-areas:
      "timeline" "intervals" "frequency" "releases";
  }
}
```

**说明**：这会让第二行统一从第一行中更高卡片的下方开始，并保留自然的垂直滚动。它不保证每张卡片等高，也不保证第一行内部不会出现多余空白；高度差明显时，应当重构信息层级，而非强行填充。

### B. 主要图表跨全行（适合重要性明显不同的模块）

```css
.release-dashboard {
  display: grid;
  grid-template-columns: repeat(12, minmax(0, 1fr));
  gap: var(--space-section, 20px);
}
.timeline { grid-column: 1 / -1; }
.frequency { grid-column: span 7; }
.releases { grid-column: span 5; }
@media (max-width: 900px) {
  .release-dashboard > * { grid-column: 1 / -1; }
}
```

如果“间隔顺序”与“相邻发布间隔”在用户任务中高度重复，应先进行 v6.8 内容删减测试，再考虑它们是否真的需要两张图。

## Gate V1 · 滚动安全不是“全部必须首屏显示”

**正常情况**：内容高度超过视口，用户可以自然地滚动看到完整记录。这不算溢出 Bug。

**问题情况**：
- 最后一个可交互行/图表脚注被 `overflow:hidden`、固定高度容器或 `clip-path` 隐藏，且**滚不到**；
- 固定/悬浮底栏挡住卡片最后一行或按钮，滚到最大位置也无法露出；
- 主区底部紧贴窗口，缺乏可见结束空间；边框/文字可能贴边或被系统安全区域覆盖；
- Grid/Flex 的隐式最小尺寸使外层撑大，主滚动区失效；`100vh` 与移动浏览器可视视口不一致造成遮挡；
- 图表或表格宽度撑破列轨，页面出现非预期横向滚动。

**合规做法**：页面级内容应当能在 window 或**唯一且可辨认的主滚动容器**内滚动到底；如果底部有固定操作条，应量得高度并预留滚动末端空间，避免按钮被盖住。不要在 `html/body` 和主区域同时藏起纵向溢出。复杂 App Shell 若依赖内部滚动，需确保 `min-height:0` 和正确的 `overflow-y:auto`。

### 文档整体滚动（非锁定工作台）

```css
.app-shell { min-height: 100vh; min-height: 100dvh; }
.page-content {
  min-width: 0;
  padding-block-end: calc(var(--space-page-end, 32px) + env(safe-area-inset-bottom, 0px));
}
.chart-panel { min-width: 0; }
```

### App Shell 固定视口 / 主区内部滚动（例如桌面工作台）

```css
.app-shell {
  height: 100vh;
  height: 100dvh;
  display: grid;
  grid-template-rows: auto minmax(0, 1fr);
}
.app-body {
  min-height: 0;
  min-width: 0;
  display: grid;
  grid-template-columns: auto minmax(0, 1fr);
}
.main-scroll {
  min-height: 0;
  min-width: 0;
  overflow-y: auto;
  overflow-x: clip; /* 仅当横向内容已响应式适配且没有要展示的弹出层 */
  padding-block-end: calc(var(--space-page-end, 32px) + env(safe-area-inset-bottom, 0px));
}
.chart { width: 100%; max-width: 100%; min-width: 0; }
```

**注意**：如果 Popover、Tooltip 等溢出主滚动区边界，`overflow-x:clip` 也可能裁掉内容；必要时通过 Portal、定位层或组件结构正确处理，不能简单全站设置 `overflow:hidden`。以上 CSS 是架构示例，仍要在实际项目试验。

### 固定底栏的遮挡处理

优先使底栏参与正常布局，或按它**实际尺寸**为 scroll content 预留末端填充（包括 safe-area）。`--bottom-action-height` 必须与真实动作条高度同步，变化时更新，不能死写一个猜测值。如果工具栏属于浏览器/开发环境而非产品 DOM，不应误报为产品级遮挡，但视觉验收仍要记录。

## Gate V2 · 浏览器级验收：必须真实滚到最底部

在真实网页（非仅示意 HTML）检查：
- 至少宽屏、常用笔记本较矮窗口、窄屏/移动端，以及用户实际使用窗口；建议包含 1440×900、1280×720、390×844，**不是产品必须采用的标准断点**。
- 最大纵向滚动后：最后一张卡片的边框、底部按钮、图表 X 轴/图例、加载/错误说明均能看见；结束内容与滚动视口底部有合理内边距。页面正常超出一屏不算失败。
- 有固定栏时：它与最后一个真实可交互/重要信息区域不遮挡；滚动最大位置仍可交互。
- 320/390 窄窗长文本与图表坐标轴不会导致非预期横向滚动；合法独立横向表格 scroller 必须有可见提示与可访问方式。
- 文字放大到 200%：不能出现不可滚动的截断、无法到达按钮或遮挡。
- 截图要包含**最后一行和滚动容器底边**；仅首屏截图不足以给出 PASS。

对已有应用，运行浏览器脚本 `scripts/audit_rendered_layout.mjs`（可选 Playwright，见工具说明）；它会截图和报告滚动容器/固定栏/可见元素几何风险。**启发式检查可能误报，也不会自动认定“很好看”或 WCAG 合格。** 可以用 `data-mf-grid-row`、`data-mf-grid-panel`、`data-mf-bottom-content`、`data-mf-fixed-bar` 声明需要验证的区域；标签不是运行应用的必要条件。

## Gate V3 · 不应采用的“修复”

- ❌ 仅给各卡片加 `height:100%`；没统一父 Grid/行轨，错位仍然存在。
- ❌ 给全站设置 `overflow:hidden` 或 `height:100vh`，让页面看似“不会超出底部”，但真实内容无法滚动。
- ❌ 强行缩小图表、隐藏 X 轴、减少 Release 记录来让全部信息塞进一个 720px 高窗口。
- ❌ 把原本滚动的内容改成内嵌小滚动条，制造多个竞争滚动容器，却没有明确理由。
- ❌ 用透明伪卡片填补不等高空间，或者把每块卡片指定超大固定高度。
- ❌ 自动截图只拍首屏就宣布“没有溢出”；必须检查最大滚动位置的终点。
- ✅ 先检查布局结构和信息必要性 → 明确 Grid 行/列契约 → 选择正确的滚动容器 → 预留底部空间 → 实际多视口滚到底验证。

## 参考来源

- [IBM Carbon 2x Grid](https://www.carbondesignsystem.com/building-blocks/foundations/2x-grid/guidelines)：信息型产品使用统一网格、列线与 gutter，允许有意义的不同布局模型。
- [MDN CSS minmax()](https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Values/minmax)：`minmax(0,1fr)` 等可控制弹性网格项的最小约束。
- [web.dev Sizing](https://web.dev/learn/css/sizing)：`dvh` 与动态浏览器可视区域。
- [MDN Viewport concepts](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/CSSOM_view/Viewport_concepts)：layout viewport 与 visual viewport（含软键盘、缩放）差异。

**外部文档提供技术和设计依据，不存在“任何两张卡片必须对齐到 0px 差”的通用 Web 法规；本 Skill 的对齐阈值仅供风险审查并应与页面语义一起使用。**

## Grid 外框合格不等于 Chart Plot 合格

用户新的发布分析截图显示两个外框上下边缘比较整齐，但 Plot Area 不同、X 轴/数据标签不协调，右侧散点与平均值标注挤在一起。对于图表页面，加查内部 Chart Header、Plot Region、Axis、Legend 与 Footnote。不同类型图不要求强行统一绘图区高度/量程，**要确保图表中真实文字没有重叠、数据时间窗口和单位可理解**。Canvas 文字不能由通用 DOM 自动审计；检查 ECharts 等图表库的 label 布局与真实截图，详见 `references/chart-interior-alignment.md`。
