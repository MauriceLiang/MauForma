# Surface Edge Accent Gate · 卡片彩色贴边竖条禁用规范

> **适用范围**：所有 Web 产品的新建页面、从零设计、已有页面视觉优化、组件重构与视觉评审；适用于 Card、Panel、Section、信息块、展示卡片、数据卡片和可点击对象。与页面类型、技术框架、主题明暗无关。本规范不要求每个模块增加一根竖条。

## Gate S0 · 贴着容器边框的装饰性彩色竖条一律禁止

**默认：不添加任何装饰性侧边彩条。** 使用清晰的内容层级、正常完整的容器边框、背景、留白和语义文字表达结构。无独立作用时，删除既有彩条，不要为了“精致”“科技感”“卡片不单调”在左边加一条。

**禁止的成品外观**：一根粗彩条沿着 Card/Panel 左边缘延伸，与外框零间距、融合边框或贴着圆角转弯。无论在 CSS 中通过以下何种方式实现，**只要实际视觉效果是贴边彩条，都不通过 Gate S0**：

- `border-left` / `border-inline-start` / `border-image` 将一侧边框染成高饱和强调色；
- 卡片自身的 `::before` / `::after` / 内部子元素绘制的贴边装饰条，甚至跨过圆角；
- `box-shadow: inset ...`、背景线性渐变、多层背景、遮罩、裁切、outline 或绝对定位伪装出同一贴边外观；
- 外侧虽然另设 DOM 节点，但负边距、绝对定位、重叠或容器裁切使它最终**接触/盖住**卡片边框。

对**新生成页面和既有遗留样式采取相同标准**。已有项目的旧代码不是例外；不能只删一根、新页面又生成另一根，或只降低亮度、变细后保留贴边。

## 允许的两种卡片方案（按优先顺序）

**A. 无侧边强调条——首选。** 保留正常一致的边框、圆角、padding；使用标题、正文、状态文字和必要的图标、Badge 区分内容。

**B. 有独立语义且确有必要时的外置指示器——可选。** 将短竖条放在 **Card/Panel 完整 border box 的外侧**，由外层布局容器管理（或由外层容器伪元素实现），留出清楚可见的**正向间隙**；参考起点是 4–10 CSS px，具体依页面密度、缩放与主题选择。它不能作为卡片的一段彩色边框，也不应随圆角弯曲；卡片自身边框、圆角必须完整。

- 若没有**可说明的状态、层级或导览作用**，即使外置也优先删除，不为每张卡片机械复制同一根彩条。
- 可用独立短轨道配合 `display: grid` / `flex` 和 `gap`；在不同窗口、滚动、交互、缩放下验证**正间隙始终存在**，不会遮住内容或被裁切。
- 指示器通常 `aria-hidden="true"`，不能是唯一表达状态的方式；保留可见文字、必要的状态标记和键盘焦点。
- 只有用户要求、现有已确认设计确有明确用途或当前交互确实需要时，才选择外置方案；否则使用 A。

### 合成示例：禁止

```css
/* 错误：贴着卡片边框与圆角的彩色轨道 */
.panel { border-inline-start: 5px solid var(--accent); border-radius: 12px; }

/* 错误：改用伪元素、渐变或内阴影不改变“贴边”的事实 */
.panel::before { content: ""; position: absolute; inset-inline-start: 0; inset-block: 0; width: 5px; background: var(--accent); }
.panel { box-shadow: inset 5px 0 0 var(--accent); }
```

### 合成示例：正确

```html
<!-- 必须有理由才保留外置短标记；不需要时直接渲染 section.panel 即可 -->
<div class="panel-row">
  <span class="panel-indicator" aria-hidden="true"></span>
  <section class="panel">
    <h2>分析摘要</h2>
    <p>近期趋势与范围说明。</p>
  </section>
</div>
```

```css
.panel-row { display: grid; grid-template-columns: 3px minmax(0, 1fr); gap: 8px; align-items: center; }
.panel-indicator { inline-size: 3px; block-size: 22px; border-radius: 3px; background: var(--semantic-accent); }
.panel { min-inline-size: 0; border: 1px solid var(--border); border-radius: 12px; padding: 16px; }
```

上面仅是结构性的合成演示，实际组件样式与标记长度以项目 Token、用途及目标视口为准；不要求所有模块采用这套布局。

## 边界：不要误伤真实语义

- **完整的焦点轮廓**（`focus-visible` / `outline`）是可访问性反馈，不属于单边装饰；不能为了去彩边把键盘焦点隐藏。
- **真实的内容与数据图形**（图表柱、进度条、时间线、引用块、表格行状态和课程步骤轨道）可以按各自语义规范设计；但不要借“状态”一词把一根卡片贴边粗条伪装为必需。若卡片仅需状态提示，先考虑文字、Badge、独立状态点或真正外置的标记。
- **导航选中项**沿用 `references/sidebar-selection-indicator-gate.md` 的专门规范；同样默认无彩条，如确需使用必须位于导航项外部且留有空隙。不要把导航规则的例外扩大到所有卡片。
- **品牌色并不禁止**：Logo、按钮、图表、图像和正式视觉叙事可使用品牌强调色，禁的是卡片边缘的**贴边彩条形态**。

## 对已有页面：发现与清理闭环

1. 在优化前查看首屏与所涉页面的 Card/Panel/Section（包括多个主题和可见状态），记录贴边彩条的**真实渲染外观**；审查组件级 `border-*`、`border-image`、伪元素、渐变、inset shadow、定位和 clip-path 实现。
2. 有贴边彩条则**优先删除**；必须保留的语义强调改成真正独立的外置短标记，有可见正间距。优先在共享 Card/Panel 组件与 Token 处修复，避免单页补丁。
3. 对同一路由、同窗口、同数据状态进行修改前后对比；在目标宽窄视口、深浅主题、200% 文本、hover/focus/selected 下确认边框仍完整、彩条不贴边、状态可读。
4. 若发现贴边彩条仍存在，标记 `FOUND → UNFIXED` 并继续修复；不可声称完成视觉优化。没有真实浏览器证据时应标记 `STATIC CHECK` 或 `NOT TESTED`，不能把规则文档和合成用例的通过当作业务页面通过。

**从零设计**同样执行第 2–4 项：首版不得生成贴边彩条，验收时按真实页面检验。只检查新增代码或旧基线而不检查成品外观，不算通过。

## 检查要点

- [ ] Card/Panel/Section 外框是否完整，未被彩色粗边或贴边伪元素替代？
- [ ] 是否对遗留组件和新建组件都进行了检查，而非只审当前 diff？
- [ ] 是否优先采用无彩条方案？外置标记有明确用途、不重复铺满所有卡片？
- [ ] 如有外置标记，是否确实处于 border box 外侧，与容器保持始终可见的正间隙？
- [ ] 是否避免使用缩小、调淡、负边距或图层覆盖等方式绕过规则？
- [ ] 焦点轮廓、数据状态、内容序号、时间线及可访问性语义是否仍保留？

合成回归案例：`assets/surface-edge-accent-cases.json`。结构契约校验：`scripts/validate_surface_edge_accent.py`。**这些测试只能验证规则与样例的一致性，不自动完成真实 DOM/视觉审美判断。**
