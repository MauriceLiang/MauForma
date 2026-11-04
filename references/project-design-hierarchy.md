# 项目设计系统：MASTER 与页面覆盖

借鉴 UI/UX Pro Max 的 Master + Page Overrides 思想；MauForma 的文件格式和实施规则为独立设计，不复制外部生成器。

## 建议项目输出目录（在用户项目内创建）

`design-system/MASTER.md`：品牌特征、用户已确认的风格、语义色/字体/间距/圆角/动效 Tokens、主组件库、共享组件表、可访问性规范、决策来源与版本。

`design-system/decisions.json`：参照 MauForma `assets/design-brief.schema.json` 记录来源（confirmed/delegated/inherited/unresolved）、风格与参数、用户原话、设计理由与待解决事项。

`design-system/pages/<route>.md`：只记录相对 MASTER 的**例外**（页面模式、主视觉、密度、构图、动效限额、不同于全站的局部需求）。不得复制全量 MASTER 导致两套冲突配置。

## 继承与冲突优先级

1. 用户新近明确确认的页面级指令；
2. 当前页面覆盖文件中的已确认/继承决策；
3. MASTER 的品牌/设计 Tokens/共享组件契约；
4. Agent 基于内容给出的未确认推荐。

若页面例外与全局色彩语义、键盘、对比度或组件可访问性冲突，不能静默覆盖；应解释冲突并征求需要的决定。样式覆盖不应允许页面直接重新定义全局 Token（例如随意用第三种 --primary）。

同一产品可以：首页采用 Premium Showcase 的大图低密度；商品页采用可扫描商品网格；会员管理采用 Functional 高密度。全站仍共享品牌字体/语义颜色/组件状态。

## 多 Agent 开发协作

每次开发前，Agent 读取 MASTER + 相关 page override + 现有组件契约。新页面只提议必要覆盖，修改 MASTER 必须说明影响全站哪些组件；不要在业务页面暗中增加第二套主色/按钮。

每次提交需列出：共享 Tokens 变更、组件契约更改、页面例外、测试与设计依据。变更用户确认的选择应获得新的授权。

## 参考样例

`examples/design-system/MASTER.md` 与 `examples/design-system/pages/home.md`、`examples/design-system/pages/dashboard.md`。这些是演示模板，不是要求用户项目使用完全相同的主题色。

## 可执行的初始化命令

```bash
python3 scripts/init_design_system.py --project-root . --name "Example" --style editorial --page home --mode Persuade
# 默认 PREVIEW ONLY
python3 scripts/init_design_system.py --project-root . --name "Example" --style editorial --source confirmed --page home --mode Persuade --apply
```

`--source confirmed` **仅当用户明确选择该风格**时使用；AI 自行决定使用 delegated。已存在的 MASTER/decisions/页面文件默认拒绝覆盖，只有用户明确授权并传入 `--force --apply` 才可改写。脚本不会替你推断业务事实和素材。

## v6.4 · 页面级构图计划的保存方式

涉及新建页面/重大改版时，在用户项目中另存 `design-system/composition-brief.json`（结构形状见 `assets/composition-brief.schema.json`），列出内容证据、2–3 个有主区域/排序差异的候选、推荐/选择来源、颜色方向与去装饰审查。具体选定方案由 `design-system/pages/<route>.md` 引用而非重复全文。MASTER 继续负责共享品牌角色和组件 Tokens；结构选择不应自动强制各页面使用相同卡片或同样的 Hero。

运行 `scripts/validate_composition_brief.py <brief-path>` 可检查内容引用、差异与未验证数据的处理，但不证明艺术方向优秀或页面已在浏览器运行。

## v6.6 · 配色选择记录必须进入 MASTER，但推荐色不能提前入库

新配色尚待用户确认时使用项目的 `design-system/sidebar-color-decision.json`（参照 `assets/sidebar-color-decision.schema.json`）记录候选与 `status=pending`；真实项目 Tokens **保持既有已批准方案**，或继续完成无颜色依赖的任务。选择后将选定方案、自定义颜色原话、来源（confirmed / delegated / inherited）和 Sidebar/Topbar/Main/Card/Chart 的协调理由写入记录，再更新唯一的 MASTER Token 来源。

如果用户明确指定 `#RRGGBB`，在选色记录 `user_constraints` 中固定目标角色，发布的 `resolved_colors` 必须原样保留；`scripts/validate_sidebar_color_decision.py` 检查不得无授权覆盖。已有已确定配色可直接 `inherited`，只改功能不需要重开主题选择。

## v6.7 · 导航 IA 记录与断点映射

项目可建立 `design-system/navigation-decision.json`，参考 `assets/navigation-decision.schema.json`：记录真实一级目的地 ID、任务/设备/层级、候选架构、用户确认或授权的来源以及 desktop/mobile 的可见+overflow 路由映射。**推荐仍 pending 时不可把候选固化成已确认架构**。MASTER 记录全局导航职责和组件契约，页面 override 只保留有意义的局部 Tab/对象树例外；不在每个路由重复自建一套侧边菜单。跨断点需保存当前页面、过滤条件与对象上下文。可运行 `scripts/validate_navigation_architecture.py <decision-path>` 做静态一致性审查。

## v6.8 · 页面级内容筛选与密度决策

可在用户项目保存 `design-system/pages/content-plan.json`，形状参考 `assets/page-content-plan.schema.json`；按路由记录 primary_task、用户状态、每块内容是 primary/supporting/conditional/deferred/removed、次级入口、页面级 airy/balanced/productive/compact 和实际验证。MASTER 保留共用主题/字级/间距 Token，不强制所有页面复制同一组卡片或固定留白比例。用户选择来源为 confirmed/delegated/inherited/provisional，不将 Agent 推荐冒充批准。真实关键信息不能仅为了留白被删除。

## v6.9 · 每页 Grid/Viewport 结构计划与滚动策略

新建数据看板、主要布局重构可在项目保存 `design-system/pages/layout-integrity.json`（参照 `assets/layout-integrity.schema.json`）：记录目的地、任务、grid pattern、行/列及同级对齐组、移动端阅读顺序、主滚动容器、fixed bar 与末端 padding 策略、浏览器截图证据。MASTER 可共享空间、列轨和滚动安全 Token，但**页面不需要采用完全相同的两列比例**。若是 Agent 推断的临时布局记 provisional，不将其冒充用户确认。真实用户指定的品牌/颜色/导航依旧继承。
