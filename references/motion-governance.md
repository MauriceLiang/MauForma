# 动效治理规范：动效必须有目的、有边界

## 选择流程

1. 用户发生了什么操作？什么状态改变？需要表达**因果、方向、层级、反馈、进度**中的哪一项？
2. 是否已存在系统原生动效或 CSS transition？够用就不引入 Anime.js。
3. 从 [animejs-motion-recipes.md](animejs-motion-recipes.md) 选 A/B/C 级候选；优先 A，B 需场景支持，C 仅在设计表达收益明确时启用。
4. 建立“动效契约”：触发、目标、起点/终点、持续时间、曲线、重复条件、打断/取消、Reduced Motion、降级、不影响数据真实性、键盘可用。
5. 将动效封装到共享组件或独立 hook/composable；页面不得到处手写不同版本的交互动画。

## 推荐的默认时序（建议值，非 Anime.js 官方常量）

| 场景 | 常见时长 | 建议缓动 | 风险 |
|---|---:|---|---|
| 按钮/开关/标签/焦点 | 100–180ms | `outQuad` / `outCubic` | 延迟感明显时减少时长 |
| 菜单/Popover/Tooltip | 120–200ms | `outCubic` | 延迟遮挡工作流程 |
| Toast / 成功反馈 | 150–240ms | `outCubic` | 无障碍消息需可读 |
| Dialog/Drawer/导航面板 | 180–280ms | `outCubic` / `inOutCubic` | 隐藏焦点和交互 |
| 小范围布局重排 | 180–320ms | `inOutCubic` | 多元素高频重排成本 |
| 展示卡片首屏进入 | 300–600ms | `outCubic` / 少量 `outBack` | 首屏不可用、长时间等待 |
| 品牌展示、SVG、长页面叙事 | 500–1200ms | 内容驱动 | 须支持跳过/减少动态 |

## 性能与无障碍门槛

- 高频事件尽量只做 `opacity` 和 `transform`，避免 `width/height/top/left/box-shadow/filter` 在大面积节点上逐帧改变造成布局/绘制成本；确需时实测。
- 一旦 `prefers-reduced-motion: reduce`，取消位移/缩放/闪动等非必要动画；使用立即切换或极短淡变。
- 对频繁触发事件，必须决定是取消旧动画、覆盖目标、合并新值还是队列排队；默认不允许无限叠加。
- 带循环的动画只用于确实持续的状态，例如等待或录音，停止状态立刻取消并清理。
- 内容默认可见；**不要全局 `.card {opacity:0}` 然后赌 CDN 一定能加载**。应在初始化成功后渐显，或只在初始化期间添加安全类并确保失败回退。
- 数字动效真实数据优先；金额、权限、温度等高敏感数据不能经过无关字符扰动而产生误读。
- 失焦、禁用、键盘 Esc、触屏、切换路由、组件卸载必须正常处理；拖拽应有键盘或等价操作。

## 动效的优秀 / 差劲案例

| 设计决策 | 优秀 | 反面 | 判断标准 |
|---|---|---|---|
| 表格筛选 | 筛选结果就位时 150ms 透明过渡或无动画 | 200 行从底部一张张飞入 | 是否帮助理解变化 |
| 保存成功 | 按钮状态替换 + 一条 Toast | 模态框震动、粒子爆炸 | 是否即时、清晰 |
| 页面加载 | 骨架/进度并行真实请求，加载完直接显示 | 全页先隐藏，等宣传动画结束 | 内容是否可访问 |
| 错误提示 | 有文字原因、聚焦并一次轻摇 | 高速红光闪烁、抖动不止 | 是否让问题可解决 |
| 官网页首 | 短时间精致错峰 + reduced-motion | 文字一字字慢出、不能跳过 | 是否照顾阅读与偏好 |
| 列表/网格 | 动画解释空间位置变化 | 无意义复杂旋转与回弹 | 是否保留对象连续性 |
| 拖拽 | 可吸附、边界明确、有撤销 | 单鼠标可用，释放后丢数据 | 是否可控且可信 |

## API / 配方关系

- 官方能力总表：[animejs-official-capabilities.md](animejs-official-capabilities.md)
- 45 内置缓动完整名称：[animejs-easing-complete.md](animejs-easing-complete.md)
- 114 种组合动效：[animejs-motion-recipes.md](animejs-motion-recipes.md)
- 直接可用示例：[animejs-v4-snippets.md](../examples/animejs-v4-snippets.md)
- 交互目录：`assets/motion-gallery.html`
