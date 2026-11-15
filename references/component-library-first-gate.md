# Component Library First — 基础交互组件优先复用门禁

> **适用**：所有有可见交互控件的 Web 项目（新建、重构、页面新增）。本规范约束 Agent 的**实际实现行为**，不是一个“可选的组件库推荐目录”。小型静态站、特殊可视化、用户明确要求原生方案等有例外，但需要说明。

## 核心规则：能复用成熟组件，就不要重新造基础交互控件

**在编写第一个业务页面之前，必须完成组件来源决策并实际采用选定方案。** “组件优先”不等于先写自己的 `UiButton/UiSelect` 再在每个页面里覆盖 CSS；应优先复用项目已有的成熟组件，缺少时为当前技术栈主动选择一套主组件方案。共享 `Ui*` 只是封装与统一 theme 的适配层，不能重新实现 Select、Combobox、Menu、Dialog 的焦点与键盘引擎。

不可以因为用户没有主动说“用组件库”，就默认用手写的 `div + click + absolute` 下拉列表，或者让不同页面的选择框、按钮、选中状态各自实现。Agent 必须主动行动，不等待用户在第一版完成后指出控件粗糙。

## Gate 0 · 盘点与选择（先于第一张业务页面）

1. **识别已有约束**：从 `package.json`、锁文件、实际 import、`components/ui/`、Provider、theme 文件查明框架、UI 主库、headless 原语、既有封装和是否已形成设计体系；检查用户明确指定的库与视觉方向。
2. **列出本轮控件清单**：`Button / Input / Select / Combobox / MultiSelect / DropdownMenu / Checkbox / Radio / Switch / Tabs / Popover / Dialog / Tooltip / DatePicker` 等，只列实际需要的，不为没有用到的功能强装全套库。明确选项选择 vs 操作菜单 vs 可搜索组合框，避免仅凭图形相似就都当作 Dropdown。
3. **按优先级自动决定**：
   - **已有可靠组件** → `reuse`。继承原主库，修复主题/封装/视觉缺陷。不因审美偏好随意换库。
   - **已有成熟主库但缺少某控件** → 查主库对应组件、官方配套或兼容的专业原语；先考虑局部补充，而不是第二套有样式主库。
   - **新项目且没有主库** → Agent 主动根据框架、交互复杂度、视觉方向、组件覆盖度、维护成本与许可证选出**一套主方案**，并开始使用；不要把“建议 Element Plus/shadcn/ui”写在报告后却仍手写控件。
   - **确实不需要交互控件**（静态文章、简洁介绍页）→ 可使用语义 HTML/CSS，不因本门禁引入大 UI 依赖。
4. **选择结果简单记录**：框架、现有主库/是否新选、为什么选它、哪些复杂控件由它承担、主题接入点，以及偏离该主方案的例外。不是让用户填组件库问卷；已有约束足够时直接实施，只有影响品牌或技术方向的真实冲突才征询。

### 框架与组件路线（候选，不能跨框架照搬）

| 框架 | 优先考虑的**完整有样式**方案 | 高度定制视觉时的组件/原语方案 | 选型边界 |
| --- | --- | --- | --- |
| Vue 3 / Nuxt | Element Plus、Naive UI、Ant Design Vue、PrimeVue、Arco Vue | shadcn-vue + Reka UI | 既有库优先；需检查 Nuxt SSR、theme、组件覆盖 |
| React / Next | Ant Design、MUI、Mantine、PrimeReact | shadcn/ui + 当前项目采用的 Base UI 或 Radix、React Aria | React 方案不可安装成 Vue 包；确认当前组件原语 API |
| Svelte / SvelteKit | 已有生态成熟 UI 套件 | shadcn-svelte / Bits UI | 按实际依赖版本和组件能力核对 |
| Angular | Angular Material、NG-ZORRO、PrimeNG | Angular CDK + 自有视觉层 | Angular CDK 为原语而非现成皮肤 |
| Solid | 与现有框架兼容的 UI 方案 | Kobalte / Ark UI（确认框架支持） | 检查支持状态，不能把 React 组件直接拿来用 |
| Astro / Vanilla | 已用的原生语义控件或兼容组件 | 按交互岛框架选成熟原语/组件，必要时原生 | 少量静态表单不能无理由引入整套 SPA 框架 |

**“成熟”不是任意引库的借口**：比较现有方案的复用性、控件与状态覆盖、样式可控程度、依赖大小、框架/SSR 兼容性、许可证和可维护性。一个项目通常只选一套主**有样式组件语言**；headless 底座与自有样式层是合理的一组，不是“双主库”。

## Gate A · 第一版先完成基础组件，再铺业务页面

在批量开发前，先用真实将要采用的主库完成一个小型组件 Showcase/开发路由，至少包含**本轮需要的**高风险控件（例如 Select、DropdownMenu、Button、Checkbox/Radio、Switch、Dialog）：

- **Select**：值、placeholder、选项列表、selected、disabled、clear（若支持）、长选项、无数据、方向与可视区域。
- **Combobox / MultiSelect**：搜索、过滤、选中、多项移除、空结果、键盘与异步时的 loading；不能拿普通 Select 假装支持搜索。
- **DropdownMenu**：这是“操作菜单”而不是数据选项；检查打开/关闭、当前高亮、危险动作、禁用项、键盘 Esc、外部点击和溢出定位。
- **Button**：primary/secondary/quiet/danger 的真正语义，loading/disabled/focus/pressed 与图标间距，正常与紧凑布局下不逐字折行。
- **Checkbox/Radio/Switch/Tabs**：checked/selected/indeterminate（适用时）、键盘焦点、状态区别、单选/多选行为，不能用同一个 Hover 样式冒充选中态。
- **Dialog/Popover/Tooltip**：键盘操作、可访问名称、浮层定位、焦点进出、关闭/恢复、滚动区与触屏边界。

使用**组件库正式提供的组件或 headless 原语**处理状态、ARIA、键盘、浮层、焦点和表单关联；Agent 的工作是做品牌 theme、组合与必要的适配层，而不是造一套简陋的下拉交互引擎。

### 合理原生控件例外

`<button>`、`<input>`、`<select>` 本身不是错误。用户明确要求系统原生体验、表单极简、移动设备平台选择器更合适、原生语义更可靠或性能/体积限制严格时，可以选择原生。**但必须是有意识的产品决策**：主题兼容、焦点、错误提示、尺寸、目标设备上的选择器外观和操作状态仍需实际检查。原生控件不应成为“没有选择库”的默认借口。不要仅靠 CSS 将原生 Select 强制画成伪自定义下拉而不保证列表一致性。

### 明确阻断的实现

- 不得用 `div + v-if/onClick + position:absolute` 或 `button + ul` 冒充成熟 Select/Menu，除非确有平台约束且实现可访问的完整键盘/焦点契约。
- 不得在新业务页面把 Checkbox/Radio/Switch 的语义和状态从零写一遍，只因为纯 CSS 写得快。
- 不得给每个业务页重新指定按钮圆角、颜色、阴影与 disabled 样式；统一从主库主题和共享适配层暴露变体。
- 不得安装两套完整有样式组件库仅为了某个 Select 的外观；应先主题化现有库或选兼容原语。
- 不得把 React Bits/Vue Bits、图标库或纯 Tailwind 工具类当成已经具备表单基础组件的证明。
- 不得只在计划里写“采用某组件库”，但提交代码实际没有引用、安装、集成或组件使用证据。

## Gate B · 主题统一与组件所有权

1. 通过应用级 ThemeProvider/ConfigProvider、CSS 变量或主库主题 API 配置字体、尺寸、语义颜色、圆角、边框、状态色、焦点与深浅模式；不要在业务页逐个覆盖主库内部 DOM。
2. 只对需要共享语义的控件写 `UiButton/UiSelect/UiField/UiDialog` 等适配层，透传业务所需 props/events/slots，尊重受控值、表单提交和官方可访问能力。**适配不等于把库原语复制重写**。
3. Select、Dropdown、Button、Checkbox、Tabs 等同屏控件要满足统一的控件高度、行高、左右内边距、圆角系统、图标风格和状态视觉语言；但允许主次不同、复杂度不同，不做“全部一样的胶囊”。
4. 对组件库不能覆盖的独特交互可选第三方专业组件或自研，须写出“为什么不复用”、处理可访问性/性能/权限，并把它作为受控例外。项目不需要的组件不强制生成。

## Gate C · 首版交付验收（不能等用户反馈后再补）

在业务页上线首轮内部评审前，必须用**真实业务路由**打开和操作高风险控件，而不只看 Storybook 或静态截图：

| 控件 | 必须观察的视觉和行为 |
| --- | --- |
| Select / Combobox | 展开时宽度和容器、菜单层级、选中/hover/focus 区别、长值、清空、箭头/回车/Esc、键盘焦点、选项滚动 |
| DropdownMenu / Popover | 触发器位置、遮挡/边缘翻转、菜单宽度与行高、禁用/危险动作、关闭和焦点恢复 |
| Button / IconButton | 主次/危险级、点击区域、图标间距、loading 防重复、disabled、focus-visible、长度和响应式 |
| Checkbox / Radio / Switch / Tabs | checked/selected 是否足够清晰、是否有键盘操作、点击目标、禁用与错误状态 |
| Dialog / DatePicker | 浮层位置、关闭/恢复、长内容、键盘、禁用日期/错误、主题与窄窗口 |

**验收结论分层**：实际在目标路由实测才可写 `VERIFIED`；只查组件配置/源码属于 `STATIC CHECK`；仅合成 Gallery 是 `DEMO ONLY`；没打开页面是 `NOT TESTED`。不能因为“库本身可访问”就宣称应用集成的对比度、位置、键盘和视觉已验收。

**阻断条件**：第一版仍出现手写假下拉、选中/hover 不可区分、按钮风格跨页割裂、浮层被裁切或无法键盘完成核心路径时，先修复主组件与真实页面，再批量复制相同模式。

## 维护与来源

- `references/enterprise-ui-library-guide.md`：候选库的定位、组件覆盖和主题接入。
- `references/framework-support-matrix.md`：框架兼容性与组件路线。
- `references/component-first.md`、`references/component-craft-gate.md`：共享组件合同和视觉精修。
- 官方 Select 行为说明：https://reka-ui.com/docs/components/select ，https://www.radix-ui.com/primitives/docs/components/select ，https://ui.shadcn.com/docs/components/base/select
- 官方 UI/原语 API 会变化，例如 shadcn/ui 目前对 Base UI 与 Radix 提供不同实现。集成前必须核对项目依赖版本和对应文档；不能凭旧示例猜 API。

所有例子均为通用规范，不含任何用户产品的专有名称或截图。
