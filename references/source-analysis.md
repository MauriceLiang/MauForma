# 源码事实与设计提炼的边界

本 Skill 基于用户提供的 Zero to Tech 静态站点源文件。区分：**原站真实数值**与**为跨项目复用而增加的建议**。不要把后者当成原站代码。

## 原站准确事实（可逐项在 assets/reference-source 中核实）

| 分类 | 原站设置 | 来源 |
| --- | --- | --- |
| 页面底色 | `#f5f5f7` | `css/variables.css` |
| 主卡片 | `#ffffff` | 同上 |
| 次级卡片 | `#fbfbfd` | 同上 |
| 主文字 | `#1d1d1f` | 同上 |
| 次文字 | `rgba(29,29,31,.72)` | 同上 |
| 辅助文字 | `rgba(29,29,31,.56)` | 同上 |
| 品牌高亮 | `#0071e3` | 同上 |
| 淡边框 | `rgba(29,29,31,.08)` | 同上 |
| 投影 | `3px 5px 30px rgba(0,0,0,.08)` | 同上 |
| 展示渐变 | `linear-gradient(294deg,#ff00f7 0%,#1e98fd 100%)` | 同上 |
| 大卡片圆角 | `32px` | 同上 |
| 子卡片圆角 | `18px` | 同上 |
| 主要按钮圆角 | `999px` | `css/lab.css` |
| 内容最大宽 | `980px` | `css/variables.css` |
| 标准卡片留白 | `24px 28px` | `css/cards.css` |
| 栅格 | 12 列，间距 `18px` | `css/layout.css` |
| 展示标题 | `clamp(56px, 10vw, 96px)` / 1.04 行高 / `-.06em` 字距 / 600 字重 | `css/hero.css` |
| 卡片入场 | 透明→实、下移 24px→0、错峰 120ms、700ms、`outBack` | `js/cards.js` |
| 链接和按钮 hover | opacity → 0.86 / 200ms | `css/cards.css`, `css/lab.css` |
| 窄屏适配 | 834px 转单列；640px 时更紧凑、卡片圆角 24px | `css/responsive.css` |

## 原站存在的工程问题（迁移时不要复制）

- `css/cards.css` 将 `.card` 预设为 `opacity: 0`：当 JS 或外链动画依赖失败时可能一直不可见。
- `js/cards.js` 依赖 CDN anime.js v4 并按脚本顺序加载；不应为设计风格强制引入第三方运行时。
- `js/score.js` 按固定值 `0.86` 滚动数字，不是真正的中文情感识别/数据计算。
- 动效没有 `prefers-reduced-motion` 路径；焦点与控件状态不够完整。
- 部分小号浅色文字应按真实背景检查对比度；不能机械照搬任意尺寸。

## 新增建议：不是原站现有实现

- 桌面生产力应用使用较小圆角/间距和更短互动时长。
- 增补 CSS focus-visible、disabled、loading、empty、error 和 reduced-motion 规范。
- 将视觉 token 命名空间化，避免覆盖项目全局变量。
- 提供无需动画 JS 也能显示所有核心内容的渐进增强写法。
