# Control Geometry Gate · 可操作文字不得被布局挤成竖排

适用所有 Web 控件：按钮、筛选 Tab、状态标签、紧凑导航、菜单项、分页、工具条、表格行操作；包括中文、英文、混排、RTL 等国际化界面。目标：**当空间不足，优先重排布局/动作，而不是让短标签逐字折行、被压扁或裁切。**

## 1. 先判断文字能否拆分

| 控件文本角色 | 默认行为 | 合法例外 |
| --- | --- | --- |
| Atomic short label：如“查看详情”“重试”“保存”、短 Tab/Badge、短状态/单位 | 标签视为一个视觉整体；文字不在字符间断行（短词/短语 nowrap），保留点击区与图标间距 | 确定为垂直书写系统、专门设计的两行大尺寸 CTA 或产品明确批准的布局 |
| Semantic multi-line label：很长的表单选项/段落型卡片标题/辅助介绍 | 在语义完整的词组或段落边界正常折行，保留适当行高，不强制一行导致溢出 | 文案需要法律原样呈现时按可访问性规则处理 |
| Content：表格描述、错误理由、正文、仓库/文件名、长对象路径 | 允许在内容列换行/截断（提供完整值入口），保留优先级 | 技术标识符、代码行与数据表可用可发现的局部滚动 |

重要：**默认只对短的原子控件标签 `nowrap`，不对全站所有文字全局 `nowrap`**，否则可能制造水平滚动和内容丢失。数字与单位视业务为整体，必要断点可换位；RTL/CJK、动态字体都需实际测量。

## 2. 布局有责任为控件留出尺寸

诊断顺序：
1. 查局部 `width` / `max-width` / 百分比列宽 / `grid-template-columns` / `flex-shrink` / `min-width`。**短标签折成竖排通常是父布局给的 inline-size 太窄**，不是字体本身不正常。
2. 测量原子标签自然宽度 + 左右内边距 + icon + gap + 焦点边界；将其作为控件适用变体的**尺寸预算**。不要通过盲目把字体缩至 10px 缩进一行。
3. 桌面行内动作组应该**整体布局**：能水平容纳就同行；容不下则整个按钮换行、使用单一主操作 + 带明确名称的 overflow menu、放在独立可展开行/详情里，或在响应式断点重排记录。
4. 维持可发现与访问：不是把重试藏进不可触达的 hover；图标按钮必须有可访问名称，危险/不可逆操作仍有合适确认。
5. 最后检查横向/纵向溢出与固定栏遮挡。**不允许“解决断字”后用 `overflow:hidden` 裁掉操作或横向跑出屏幕**。

## 3. 可移植 CSS 策略（仅示意，不作为所有项目强制值）

```css
/* 仅针对短标签；长文本选项不要照抄这个策略 */
.ui-action {
  display: inline-flex;
  align-items: center;
  justify-content: center;
  gap: var(--space-control-gap, .375rem);
  white-space: nowrap;
  flex: none;                  /* 不让一个短操作被挤压成竖排 */
  inline-size: max-content;    /* 需与容器自适应策略成对使用 */
  max-inline-size: 100%;       /* 控件不应直接越出视口 */
}
.action-group {
  display: flex;
  flex-wrap: wrap;             /* 包裹的是完整按钮，不是按钮里的字 */
  gap: var(--space-action-gap, .5rem);
}
.data-row {
  display: grid;
  grid-template-columns: minmax(0, 2fr) minmax(0, 1fr) max-content;
}
/* 当行总宽不够时：重排行区，不继续维持三列挤压 */
@container (max-width: 38rem) {
  .data-row { grid-template-columns: minmax(0, 1fr); }
  .action-group { justify-content: flex-start; }
}
```

**不要误用示例**：项目可用 CSS Grid/Flex、`table` + overflow menu、容器查询、显式断点等不同实现。若 `inline-size:max-content` 仍比小屏宽，应改变文案/模式、允许有语义的换行或可访问滚动，不能坚持强制不溢出。固定表格 `table-layout:fixed` 的 action column 必须容得下控件；连续长列可以优先缩/折中间内容列或将操作移出狭窄列。

参考 CSS 行为与标准：
- MDN white-space: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/white-space
- MDN flex-shrink: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-shrink
- MDN flex-wrap: https://developer.mozilla.org/en-US/docs/Web/CSS/Reference/Properties/flex-wrap

## 4. Gate D · 必须实测断字与可达性（不只审源码）

- **短标签**：通过真实浏览器获取标签的文本 Range/line rects 和控件 bounding box。即使源码有 `white-space:nowrap`，也要排除父级固定宽度、flex shrink、截断和越屏。
- **几何**：动作标签、图标、焦点边界、表格尾列不被裁切；按钮点击区足够，Tab/工具条的选中和键盘焦点都可触及。
- **应力场景**：宽/窄窗口（尤其 1280、390、320px 级别）、文字 200% 放大、至少一组长中文和英文、多个同排操作、异常状态比正常状态多一个动作、浅/深主题；按项目实际语言另测 RTL。
- **Responsive fallback**：每个短操作用什么自适应路径？测试按钮作为整体换行、overflow menu、行重排或局部表格滚动，而不是把字挤成“查/看/详/情”。
- **报告真实证据**：无法读取 Canvas、ShadowRoot 或未提供 DOM 标记则标 `NOT AUDITED`；静态 CSS 检查不等于浏览器 PASS。对浏览器脚本，推荐控件根元素加 `data-mf-atomic-control`，标签内层加 `data-mf-control-label`，脚本可按实际几何审查。不要求所有使用 MauForma 的产品永久添加这些属性。

**审查难点是布局在变窄时如何退化，而不是某一个圆角控件长得够不够美观。** 和 `references/surface-architecture-gate.md`、`references/grid-alignment-and-viewport-safety.md`、`references/component-first.md` 联用。