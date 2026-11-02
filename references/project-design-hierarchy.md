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
