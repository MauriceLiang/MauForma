# Clean Enterprise · 可选的清爽工作台设计语言（v6.18）

这是一份**可选风格档案**，不是 MauForma 默认 UI 模板、现存产品的还原稿或固定设计 Token 清单。面向需要长时间使用、快速扫描、操作可靠的 Web 工具。主要用于 Operate 工作台，但其他模式可**借用部分原则**，不得强推侧栏或表格。

## 设计的核心不是“全蓝、全白、全圆角”

**目标感受**：清爽、不费力、专业、信息明确、克制但不呆板。真正形成品质的是比例和角色：
- 使用中性大面积背景建立阅读场，主色只承担关键操作与选中状态。状态色与业务语义一一对应，避免所有 badge 有颜色。
- 导航标签应舒适易读，图标辅助而不夺权；选中行通过轻背景和适当的前景强调即可表达归属，必要时才加左侧条/边框，避免同一选择叠加三四种效果。
- 表格根据**扫描任务**设置行高、字重、列宽和对齐。常见信息不被误降成弱灰 11px；重要值和可操作链接有清晰层级。适度密度不等于所有文字小。
- 使用平面 table/list 处理大量同构条目，而不是将每条记录塞进装饰性卡片；独立对象和媒体可使用 Card。
- 让页面标题、工具栏、分区、列标题和行操作自然形成阅读路径，保持段落与数字、数字与单位、图标与文字的光学比例。
- 可以有细腻且有目的的过渡，但不因风格克制就静默省略用户已经选定的组件动效。动效强度由 Motion Choice Gate 单独控制。
- **对比度优先于“浅”**：低饱和不等于低对比度。禁用态、占位符、正文、表头、状态标签应清晰区分；深色主题独立审查。

## 设计语言契约（优先角色，不写死像素）

| 角色 | 风格判断 | 容易失败的情况 |
| --- | --- | --- |
| Base canvas | 柔和中性，减少视觉噪音 | 一切灰到无法分辨结构 |
| Surface | 根据任务采用平面区/单层容器 | 页头+筛选+表格被巨卡重复包围 |
| Accent | 有限强调，用于选中项和主要 CTA | 随意把每个按钮涂成品牌色 |
| Navigation | 标签与 icon 同步读，active 背景清楚 | 字体太小、视觉重量不一、active 过度 |
| Typography | P0/P1 充分可读，说明与元信息弱而不淡 | 大字号口号与小字号重要记录失衡 |
| Records | 数据视线沿列对齐，状态文字明确 | 每行大量多彩 pill、操作挤压折字 |
| Spacing | 行内紧凑、章节有明显呼吸空间 | 卡片内部空洞与外侧零间距并存 |
| Motion | 微交互由用途/用户选择决定 | 页面突然跳变或所有部件一律弹跳 |

### 初始 tokens 仅是项目起点

实际项目先从其现有 tokens 推导。以下并非通用固定值：

`--canvas`、`--surface`、`--ink`、`--muted-ink`、`--accent`、`--accent-soft`、`--line`、`--space-inline/inside/peer/section`、`--radius-control/panel`、`--font-nav/row/meta`。

在真实字体、中文/英文、用户任务密度与视口下调节：同一导航组先看整组，次级信息不能稀释重要文本；图标在真实尺寸下与文字同频，不因 CSS 设置 `20px` 就认定光学一致。历史 UI、品牌配色和用户明确设计方向优先。

## 图标：Element Plus Icons 可以是候选，但不是强制

开源图标库并没有绝对的“高级/低级”之分。Element Plus Icons 常见的是简明轮廓与合适的负空间，适合若干工作台场景；Lucide、Tabler、Phosphor、Heroicons 或本项目既有图标库也可能更适合。

- 选择真实业务图形，而非菜单词语的机械直译。
- UI icon 与品牌 logo 不同；主导航尽量保持一套图形语言及视觉重量。
- 若使用 `@element-plus/icons-vue`，按实际版本核对图标名称、导入方式和当前许可（官方资源：https://github.com/element-plus/element-plus-icons，MIT）；不要因为用户提供参考很喜欢某套图标就宣称原图来源已百分之百确认。
- 主导航 16–24px 只是常见审查区间，是否合适取决于字体比例与图形复杂度。选中态和 normal 态不随意切换风格。

## 四类网站的迁移方式

| 模式 | 可学习什么 | 不该搬什么 |
| --- | --- | --- |
| Operate | 稳定导航、明确选中、紧凑可读的记录、高质量图标 | 所有列表固定表格、所有功能蓝色按钮 |
| Persuade | 中性版式/主色克制、CTA 清晰 | 产品故事缩成后台表格、统一侧栏 |
| Read | 字号可读、低噪阅读、轻量当前章节提示 | 高密度表格行高与多按钮工具栏 |
| Experience | 不打扰作品的控件、节制辅助色、图标语义 | 作品舞台做成工作台，失去视觉个性 |

## 参考实现与限制

仓库里的 `examples/clean-enterprise-demo/index.html` 是**全新虚构场景**，非任何用户页面复刻，使用公开 Element Plus Icons SVG（MIT，独立许可证），通过导航/表格/按钮的可运行实例展示上述原则。它的布局和 token 不该被 Skill 复制成所有项目的必然模板。

额外 QA 需要继续符合 `references/icon-art-direction-gate.md`、`references/perceptual-hierarchy-gate.md`、`references/semantic-spacing-rhythm-gate.md`、`references/surface-architecture-gate.md`、`references/component-motion-choreography-gate.md` 和 `references/visual-qa.md`。

更多公开设计依据：Element Plus https://element-plus.org/zh-CN/component/icon.html；IBM Carbon data table https://carbondesignsystem.com/components/data-table/usage/；Atlassian design tokens https://atlassian.design/foundations/tokens 。
