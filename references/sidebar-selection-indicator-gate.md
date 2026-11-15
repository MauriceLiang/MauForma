# Sidebar Selection Indicator — 外置选中提示条与导航项边界

本规范适用于 Web 侧边主导航、设置目录及其他**已选定使用侧栏**的场景；它不要求所有侧栏都出现选中竖条。新建页面优先考虑柔和背景、文字与图标强调，具体风格继承用户已批准的设计与主题。

## 选中态只有一种清晰、可解释的视觉结构

1. **默认：无竖条**。用低对比背景、字重/图标权重标示当前路由，保留独立的 hover、focus-visible。不得为了“更精致”自动添加彩色竖条。
2. **可选：独立的外置短竖条（external indicator）**。用户指定或设计确实需要时，在**当前选中导航项外侧**单独展示一段竖向细条，通常位于左侧 gutter（RTL 设计按逻辑起始侧处理）；它与导航项的真实边框及底色之间应有可见空隙。导航项保持完整的圆角、背景和文字内边距。**只在实际选中项显示**，不在所有导航行的最左侧重复显示。
3. **禁止：把导航项的左边框涂成品牌色，冒充独立指示条**。不要对 `[aria-current=page]` 的导航链接使用彩色 `border-left` / `border-inline-start`、`box-shadow: inset 3px 0` 或贴在按钮内部左边缘的 `::before` 模拟外置提示。这样的做法改变了选中导航项本身的边框，视觉上与外部指示条不同。
4. **不同职责的轨道不要混淆**：文档目录阅读进度、树形层级连接线、拖拽位置反馈可使用连续线/标记，但它们不是普通页面导航的选中装饰。复杂侧栏中不要将它们全部涂成“活动项颜色”。

## 组件与布局契约

- `SidebarItem` 负责路由链接、选中背景、图标、标签和焦点。外置 `SelectionIndicator` 由**导航项外层的行容器**负责；推荐使用与链接平行的独立装饰节点，或行容器的独立伪元素，而不是按钮/链接自己的彩色左边框。
- 为指示条预留一个稳定 gutter，未选中行也保留一致的对齐空间，避免切换路由时内容左右跳动；避免靠负 margin 或绝对定位超出可裁切的容器来“假装外置”。
- 竖条是短标记，不是贯穿导航项全高的彩色边线。示例可用约 2–4px 宽、12–22px 高，指示条与按钮之间预留约 6–10px 的可见空隙；**数值是设计起点，不是硬性统一尺寸**。它不应占据文字内部 padding。
- 装饰节点使用 `aria-hidden="true"` 且不可交互；不为它增加可 Tab 聚焦元素。真实路由项使用链接及 `aria-current="page"`（示例交互可用按钮和 `aria-pressed`，但不能复制为业务导航）。
- `focus-visible`、hover、selected 是不同状态；不能用竖条取代键盘焦点轮廓，不因 focus 给另一项制造第二根“选中竖条”。单组主导航只能有一个当前页；异步路由切换需从路由真实状态驱动指示条。

## 示意实现（结构与主题均可调整）

```html
<nav aria-label="主导航" data-mf-selection-indicator="external">
  <div class="sidebar-row" data-current="true">
    <span class="sidebar-indicator" data-mf-indicator-rail aria-hidden="true"></span>
    <a class="sidebar-item" data-mf-nav-item href="/overview" aria-current="page">概览</a>
  </div>
  <div class="sidebar-row" data-current="false">
    <span class="sidebar-indicator" data-mf-indicator-rail aria-hidden="true"></span>
    <a class="sidebar-item" data-mf-nav-item href="/activity">活动</a>
  </div>
</nav>
```

```css
.sidebar-row {
  display: grid;
  grid-template-columns: 3px minmax(0, 1fr);
  align-items: center;
  column-gap: 9px;
}
.sidebar-indicator {
  width: 3px;
  height: 18px;
  border-radius: 3px;
  background: var(--sidebar-selection-indicator);
  opacity: 0;
  pointer-events: none;
}
.sidebar-row[data-current="true"] > .sidebar-indicator { opacity: 1; }
.sidebar-item { border-inline-start: 0; box-shadow: none; }
.sidebar-item[aria-current="page"] { background: var(--sidebar-selected); }
.sidebar-item:focus-visible { outline: 2px solid var(--sidebar-focus); outline-offset: 2px; }
```

`data-current` 必须跟随真实路由状态，不可固定硬编码；示例表示结构关系，颜色、字号、尺寸和实际组件 API 应使用当前设计系统。无竖条方案直接不渲染装饰节点，不需要为空占用 gutter。

## 验收与证据

在真实项目中检查桌面、侧栏收起/展开、窄窗口、长中英文、深浅色、键盘焦点、路由前进/后退与 200% 字体；确认：

- 当前项外置标记与导航项**非接触、非重叠**，指标矩形位于 item border box 之外；左右间隙在所有支持视口仍清晰。
- 只有当前路由有可见标记；切换后旧标记消失、新标记正确移动，文字与按钮背景不跳动。
- 链接本身仍有完整边框/圆角和独立焦点；未选中项不应残留彩条。
- 整体视觉不叠加无意义的强底色、彩条、发光和图标强调。若没有明显收益，改用默认无竖条方案。
- 静态检查或概念 Gallery 测试通过不能代表真实页面已验收；未打开目标页面标 `NOT TESTED`。

### 实际页面可选的几何审查

当项目实现了外置短竖条，给侧栏根元素增加 `data-mf-selection-indicator="external"`，给导航链接增加 `data-mf-nav-item`，给与导航项并列的装饰节点增加 `data-mf-indicator-rail`。无竖条方案可标为 `data-mf-selection-indicator="none"`。这些属性仅用于可选择的检查；框架中真实路由仍负责控制 selected。

运行目标开发服务器后可执行：

```bash
node scripts/audit_sidebar_indicator.mjs http://localhost:5173
```

脚本只对**明确标注的导航容器**检查几何、是否贴边、短条是否过高、是否存在内嵌边框、是否错误显示多个选中指示条。未标注或未实际打开页面会返回未通过；它不自动确认导航架构、审美或可访问性，仍需人工复核。

通用概念对比见 `assets/sidebar-refinement-gallery.html`，自动回归测试见 `tests/sidebar_indicator_browser_smoke.mjs`。配色仍以 `references/sidebar-color-discovery.md` 与用户已确认的 Tokens 为准。
