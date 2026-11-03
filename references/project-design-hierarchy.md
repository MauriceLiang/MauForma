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
