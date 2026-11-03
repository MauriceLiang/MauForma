# Navigation Architecture · 由信息架构决定导航位置（v6.7）

**目标**：选导航方式之前，先弄清“去哪里”（destination）、“在当前页做什么”（action）、“当前页内部换视图”（local tabs）、“切换对象/集合”（context picker）。不要因为开发的是 SaaS，就自动画左侧栏；也不能只因为手机宽度小就把七八个入口塞到底部栏。

## 0 · 事实优先，六个问题的取舍

1. **一级目的地有几个？** 记录真实名称、是否同级、是否高频。不能把按钮、筛选器、外链全部算进导航数量。
2. **层级深度如何？** 一级频道、频道内任务、对象/文件树、内容页局部 Tab，分别有不同职责。
3. **切换习惯怎样？** 是持续在栏目间跳转、反复操作/对比，还是浏览一个产品介绍页面？一屏工作时有多少空间要留给数据/画布/摄影？
4. **主要设备及窗口宽度？** 桌面大屏、笔记本窄窗、平板、手机；Web / PWA / Tauri WebView 的实际使用情境和可缩放窗口。
5. **品牌和已确认设计**？继承正式 IA 与视觉方向；若用户明确指定顶部/侧边/底部，不用反复选择。重要可用性冲突先解释再提可行的实现。
6. **是否存在持续显示的次级导航？** 例如项目树、文档目录、仓库对象列表、设置分类，是否需要与全局栏目同时出现？

记录在 `design-system/navigation-decision.json`，参考 `assets/navigation-decision.schema.json`。用户还没决定时，Agent 推荐 `pending/unresolved`，不能把候选偷当已确认。用户授权“整页设计你决定”才可记 `delegated`；仅允许改色不等于允许变更导航位置。

## 1 · 选型地图（不是僵硬的数学公式）

| 方案 | 适合的情况 | 不适合 | 响应式重点 |
| --- | --- | --- | --- |
| **Top only / 顶部主导航** | 品牌官网、作品集、媒体门户，少量宽泛平级栏目；要给主视觉/正文留横向空间 | 类目多、子项需要持续展开、长标签在一行易拥挤 | 窄屏改为菜单抽屉或折叠导航，保证可发现性，不默认“只剩汉堡按钮” |
| **Side only / 持久侧边栏** | 桌面优先的仓库分析、ERP、管理后台，较多功能分区、频繁在分区间切换 | 手机窄屏、沉浸摄影/购物内容、少量简单栏目 | 中屏可收窄为有标签的 rail；窄屏以 drawer 或底部核心导航替代 |
| **Top + Side / 全局顶部 + 局部侧边** | 多产品/工作区或复杂层级：顶部标识全局工作区、通知与搜索；左栏显示当前产品内的功能/目录 | 同一组一级栏目在顶部与左侧无意义重复；占据双重固定空间而无分工 | 小屏顶栏保留对象/全局动作，次导航进入抽屉 |
| **Rail + Detail / 图标轨道 + 列表/详情** | IDE、邮件、文件管理、知识库，需要同时查看两层目录或对象，且空间足够 | 无文字图标难懂，主要内容区被三列挤压 | rail 需提供文本标签/展开提示，窄窗仅保留一层并有返回路径 |
| **Bottom nav / 底部主导航** | 以手机为主且约 3–5 个同级、高频目的地的应用 | 桌面官网、数目很多的导航项、操作按钮被当作目的地 | 注意 safe area、虚拟键盘、屏幕阅读器及手势区域 |
| **Adaptive side → bottom / 桌面侧边、手机底部** | 跨桌面+移动端的应用，桌面入口较多但有 3–5 个稳定的高频手机目的地 | 把一整套侧边栏 7–10 项原样压成 7–10 个底部按钮 | 首选目的地身份、排序和选中状态在断点间保持一致；非核心项可进入更多/抽屉，但不能悄悄消失 |
| **Top + Bottom / 顶部上下文 + 手机底部主导航** | 移动产品：顶部显示当前对象/搜索/返回/通知，底部跨一级模块切换 | 两个区域展示同一组一级入口；顶部工具栏与底部导航争同一功能 | Header 与 bottom nav 权责不同，底部避免被键盘遮挡 |
| **Side + Bottom utility / 侧边导航 + 底部操作区** | 桌面工作台的左侧主导航加页面底部持续的上下文动作/批处理/播放工具条 | 把下方操作按钮称为“底部导航”；顶部/侧边/底部三个地方重复同一目的地 | 底部工具条必须属于当前任务，有清晰关闭/收起机制，避免挡住内容 |

**“侧边加底部”有两种完全不同的含义**：
- **不同设备自适应**：大屏是 sidebar，手机是 3–5 个核心入口的 bottom navigation（不是同一个视口同时显示两套一模一样的主导航）。
- **同一屏同时存在**：sidebar 负责全局/产品内导航，而 bottom 是**操作条**、播放控制、进度与批处理；若底部也是导航，则必须确实属于不同上下文层级且不重复路由，否则不要双层导航。

顶部/侧边/底部都可以无：沉浸式编辑器、支付流程、焦点阅读模式可能只保留 Back、breadcrumb 或临时导航，但仍需退出与恢复上下文路径。

## 2 · 用户可比较的方案，不是组件外观三连

当项目结构未确定且布局会影响体验时，从 `assets/navigation-pattern-catalog.json` 基于项目筛选 **2–3 种主 IA 不同的方案**（例如：Top only / Side only / Top+Side）。每套至少交代：

- 谁是**全局导航、产品内导航、页面内 Tab、上下文动作**；有几项、标签是什么；
- 桌面第一眼能看什么，侧栏占用多少内容宽度（只有必要时用约数），滚动和收起如何影响视线；
- 窄屏变成**哪一种**导航形态，哪几个入口直接可达，其他去哪了；跳转和返回路径是否保留；
- 它对当前项目的优势、代价、适用条件；用户指定模式或明确授权后再定稿。

**不要**为了展示“多方案”把同一侧栏仅改成图标型、暗色型、圆角型。这些是外观变体，不是导航架构差异。参考 `assets/navigation-layout-lab.html` 原创概念实验室；它不是用户真实项目的验收。

## 3 · 跨屏与状态守恒

- **目的地 IDs 唯一且稳定**：`overview`、`issues`、`prs` 在 desktop/tablet/mobile 下同义；不要断点后改名或默认重新排序。手机只显示核心入口时，完整路由必须从抽屉/更多菜单可达。
- **不要在同一视口同时显示重复的同级导航**：例如侧栏有 Overview/Issue/PR，底部又显示同样三个（除非特殊可用性测试要求且用户明确选择）。
- **不要用普通 Tabs 导航跨产品一级路由**：tabs 是同一页面/对象的同级子视图；页面/模块导航使用真正的链接。
- **“底部工具条”不是“底部导航”**：Add/Delete/Apply/Save 等改变当前上下文的按钮只能属于工具或操作区，不能伪造目的地。
- **粘性与遮挡**：sticky header、persistent sidebar、fixed bottom bar 之间的层级、滚动、短窗口和 safe-area inset 需专门检查，避免遮挡焦点与内容。
- **触控与无障碍**：`<nav aria-label="主导航">` 等语义区分；`aria-current="page"` 标真实位置，`aria-selected` 用于真正的 tabs；键盘可达、焦点 visible、主内容 Skip link；不同导航区域给独立名称。不要为了炫酷强迫网页导航使用 application/menubar 角色。
- **状态保留**：导航转换不能导致 filter、搜索词、图表选中、未保存表单或当前对象默默丢失；检测浏览器前后退、深链接、旋转和多窗口 resize。

## 4 · 什么时候应该删掉导航

如果某页面顶部有主导航、左侧又有完全一致的菜单、底部还有同样图标，**先重新定义责任**；将不承担独立任务的导航删去，比重新配色更重要。对无必要的 `WORKSPACE`、`NAVIGATION` 小标题同样执行 `semantic-copy-hygiene.md`。

## 5 · 与用户批准的配色与设计系统协调

导航模式和配色是**两个独立决定**。选择 Side/Top/Bottom 不代表 Agent 可以重选深蓝/蓝紫；延续 v6.6 用户确认的品牌和颜色。候选布局用中性色概念示意，颜色只有用户确认/继承/明确委托才写入 MASTER。每一种模式都要考虑 Sidebar/Topbar/Main/Card/Chart 整页视觉关系与字号密度。

## 6 · 有边界的参考依据

- [IBM Carbon UI Shell](https://www.carbondesignsystem.com/building-blocks/core/patterns/global-header) ：Header only / Header with left panel，导航层级有分工。Carbon 左侧 panel [guidelines](https://www.carbondesignsystem.com/building-blocks/core/components/ui-shell-left-panel/guidelines) 提到次导航项较多或频繁切换时才适合持久侧栏，且不支持无限层级。
- [Android 官方响应式导航](https://developer.android.com/develop/ui/views/layout/build-responsive-navigation)：宽度与目的地数量共同决定 bar/rail/drawer，不能只看设备名称。
- [Android 官方导航组合](https://developer.android.com/design/ui/mobile/guides/layout-and-content/layout-and-nav-patterns)：底部主导航通常约 3–5 个同级目的地，tabs 承担同一内容上下文的次级视图。
- [Apple HIG Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars) / [Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars)：横向空间和信息层级决定持久侧栏或紧凑 tab；在部分平台可自适应。
- [Microsoft NavigationView](https://learn.microsoft.com/windows/uwp/design/controls-and-patterns/navigationview)：少量同级导航可考虑顶部，较多主类别常适合左侧；是原生 WinUI 产品的经验，不能硬套 Web。
- [Atlassian Navigation Layout](https://atlassian.design/components/navigation-system/layout)：顶部全局与侧边上下文可以共存，但必须分工。
- [WAI Navigation landmarks](https://w3c.github.io/wai-website/ARIA/apg/practices/names-and-descriptions/)：多导航区的名称应明确区分用途。

**以上是设计原则与决策参考，不能推导出“6 个入口必须侧栏”之类绝对规则。** 真实网站形态、用户任务和可用性测试可以优先于示例计数。
