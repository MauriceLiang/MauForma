# 动画与交互规范（v3.0 入口）

**不限于后台系统**：展示型网站可以使用更丰富的动效，编辑器、后台和桌面工具强调简洁、快速与可中断。

优先阅读：

- [motion-governance.md](motion-governance.md) — 什么时候该有动画、速度、风险、性能与 reduced-motion；
- [animejs-official-capabilities.md](animejs-official-capabilities.md) — Anime.js v4 官方主能力 API；
- [animejs-easing-complete.md](animejs-easing-complete.md) — 45 个内置缓动名称 + 自定义生成器；
- [animejs-motion-recipes.md](animejs-motion-recipes.md) — 114 种可组合视觉效果、视觉表现和避雷；
- [animejs-v4-snippets.md](../examples/animejs-v4-snippets.md) — 16 个代码示例；
- [motion-gallery.html](../assets/motion-gallery.html) — 点击重播、搜索、按类别筛选、缓动列表。

---

# 动画与交互规范（v3.0 入口）

**不限于后台系统**：展示型网站可以使用更丰富的动效，编辑器、后台和桌面工具强调简洁、快速与可中断。

优先阅读：

- [motion-governance.md](motion-governance.md) — 什么时候该有动画、速度、风险、性能与 reduced-motion；
- [animejs-official-capabilities.md](animejs-official-capabilities.md) — Anime.js v4 官方主能力 API；
- [animejs-easing-complete.md](animejs-easing-complete.md) — 45 个内置缓动名称 + 自定义生成器；
- [animejs-motion-recipes.md](animejs-motion-recipes.md) — 114 种可组合视觉效果、视觉表现和避雷；
- [animejs-v4-snippets.md](../examples/animejs-v4-snippets.md) — 16 个代码示例；
- [motion-gallery.html](../assets/motion-gallery.html) — 点击重播、搜索、按类别筛选、缓动列表。

---

# 动效与微交互规范

## 原站的事实（灵感，不必原封复制）

- 卡片入场：opacity 0→1、translateY 24→0、相邻错峰 120ms、700ms、Anime.js `outBack`。
- 按钮 / 链接 hover：opacity .86，200ms。
- 原站使用 CDN Anime.js，且组件在脚本失败时可能持续隐藏；正式项目不要继承此缺陷。

## 分层动效决策

| 场景 | 建议 | 不推荐 |
| --- | --- | --- |
| 展示页首次出现 | 8–24px 轻位移 + 淡入，450–700ms，可少量 stagger | 所有卡片从屏幕外飞入 |
| 普通控件 | 120–240ms、轻微背景/边框/opacity 过渡 | 每个 hover 缩放、旋转、弹跳 |
| 桌面工具高频操作 | 120–180ms，优先立即反馈 | 终端/树节点/列表滚动上的弹性缓动 |
| 保存、错误、加载 | 明确文字与状态、异步期间反馈完整 | 只有闪光/转圈，无具体结果 |
| 导航切换 | 稳定切换或小幅过渡 | 每次导航重播所有入场动画 |

## 实施规则

- 动效必须解释“状态变化”或“空间关系”，而非单独追求炫酷。
- 交互只使用 opacity、transform、color 等合适属性；避免高频布局重排与重型模糊。
- **所有核心内容默认可见**：不要将 `.card { opacity:0 }` 写成动效依赖的唯一可见路径。
- `:focus-visible` 使用 `var(--spui-focus)`；不要把原示例的 `#0071e3` 硬编码到各主题。
- `@media (prefers-reduced-motion: reduce)` 下取消非必要位移/循环效果，保留明确状态反馈。
- Vue Transition、Motion、Anime.js 等都可按既有项目选择；多数基础 hover 仅需 CSS，无需引入新动画库。

```css
.ui-interactive {
  transition: background-color var(--spui-motion-ui) ease-out,
              border-color var(--spui-motion-ui) ease-out,
              opacity var(--spui-motion-ui) ease-out;
}
.ui-interactive:focus-visible {outline: 3px solid var(--spui-focus);outline-offset:3px;}
@media (prefers-reduced-motion: reduce) {
  .ui-interactive {transition-duration: .01ms;}
}
```

检查：按钮连点是否误触发？弹窗能否及时关闭？动画关闭后布局是否稳定？暗色和窄窗里是否出现视觉闪烁？
