# MauForma · 组件优先视觉 QA v2.0

## Gate A — 主题和 tokens（开始业务页面前）
- [ ] 产品视觉方向有一句解释；未强制照搬原站粉蓝渐变。
- [ ] `page/surface/surface-soft/text/accent/on-accent/focus/border/status` 等角色齐全。
- [ ] 主色、状态色职责分开；主题可以集中切换，页面没有无约束的硬编码色。
- [ ] 圆角、空间、字体和动效定义为共享 token；明确 showcase 或 productivity 密度。
- [ ] 浅/深主题在用户要求的模式下完成配色对比检查。

## Gate B — 组件（必须先于大规模页面实施）
- [ ] 盘点现有组件库，判断保留/封装/新增；没有为视觉重新写同一套原语。
- [ ] 按当前业务需要建立共享 Button、Field、Panel、Nav、Dialog、Status/Feedback 等最小组件集。
- [ ] 组件 API 有 variants、sizes、props/slots/events、适用状态和责任边界。
- [ ] 有可运行的组件展示页，覆盖相关 normal/hover/focus/disabled/loading/error/empty。
- [ ] 组件中没有散落的第二套主题颜色和随机圆角；页面的 `.button` 不覆盖基础组件核心外观。
- [ ] 输入可读，键盘焦点、标签关联与错误解释到位。

## Gate C — 业务页面视觉与功能
- [ ] 主次信息清晰，主题色没有抢走内容注意力，长中文标题和数字显示正常。
- [ ] 相邻区域间距表达关联；无无意义彩色大块、嵌套大卡片和阴影泛滥。
- [ ] 真实的保存、取消、删除、导航、表单校验、错误/空/加载状态没有被视觉修改破坏。
- [ ] 组件 hover、focus、pressed、disabled、loading 可辨认；状态不只靠颜色传达。
- [ ] 宽屏 + 窄窗/移动端布局验证；按项目需要完成暗色模式验证。
- [ ] Reduced Motion 下可使用，关键内容不依赖第三方动画库才能显示。
- [ ] 性能与可读性优先于极端玻璃、霓虹、过量弹性动画。

## 审核方法
1. 先运行项目的检查或构建；若使用本包主题，运行 `scripts/validate_design_system.py`。
2. 打开组件展示页（没有则临时制作状态样板）确认每个共享组件及各状态。
3. 打开真实业务页面，至少检查宽/窄窗口与关键状态；注意高 DPI、系统缩放和中文长文。
4. 对照 [good-vs-bad.md](good-vs-bad.md) 寻找反例，输出具体组件/页面/修复方式。
5. 按 [ui-review-rubric.md](ui-review-rubric.md) 打分，阻断项先修复再交付。
6. 如果没有真实浏览器/截图工具，必须说明“仅静态源码审查，未实际渲染验收”。

## 任务型页面标题 / AI 模板味（v2.1）

- [ ] 页面是管理/设置/列表/编辑时，没有默认照搬营销页的 eyebrow + 超大 H1 + 宣传口号。
- [ ] 小字、英文标题和副标题提供了不同的、真实的信息；不能解释价值的装饰文本已删去。
- [ ] 主操作靠近页面标题，核心列表或表单在常见窗口中尽早可见。
- [ ] 同类功能页通过 `UiPageHeader` 或现有等价组件保持一致；真实面包屑、技术术语及必要提醒得以保留。
- [ ] 对照 `references/page-header-antipatterns.md` 与 `assets/page-header-antipattern-gallery.html`，记录修复前后截图和明确理由。

## v6.2 · 复杂视觉技术专项检查

- [ ] 技术是按明确的视觉需求选型，已说明相对 CSS/SVG/已有库的增益，而非为效果堆库。
- [ ] 同一 DOM 元素/属性没有被 CSS、GSAP、Motion、Anime.js 重复控制。
- [ ] SplitText 标题字体加载/断点变化后仍可访问、语义正确，长文没有多余拆字。
- [ ] Three.js / PixiJS / Curtains.js / tsParticles 在卸载、隐藏或失败时停止和回收，提供静态回退。
- [ ] ECharts 图表数据来自真实业务且按需销毁，重要数值可通过文本或可访问表格理解。
- [ ] Matter.js 不负责 UI DOM 本身的交互语义，键盘操作/业务操作没有被物理效果阻碍。
- [ ] 在目标设备实测帧率、内存、CPU/GPU、缩放与窄屏，明确哪些条件未测。
