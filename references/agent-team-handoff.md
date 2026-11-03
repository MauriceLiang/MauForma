# 多 Agent / 团队协作规范

## 角色职责与交付顺序

1. **设计负责人 / Lead**：整理产品任务与组件清单、确认视觉方向与主题角色，选择密度，冻结 token；将实现和验收任务拆开，避免前端 Agent 独立发明视觉语言。
2. **组件负责人 / UI Foundation**：先实现/主题化共享组件和状态样板，交付 `tokens/theme + UI primitives + component contracts + component gallery`。提交视觉一致性、键盘、状态报告。
3. **功能前端 / Feature Developer**：复用组件完成页面组装和业务交互。只负责布局与业务差异；新增 UI 需求回归组件层，不能绕开组件规范。
4. **测试 / QA**：在组件 gallery + 实际业务页面对比检查、跑功能和键盘测试，逐项记录优秀/差劲案例，使用评分表，必要时截图标注。
5. **Lead 终审**：检查 Gate A/B/C、重复组件、暗色/窄窗、未完成问题；符合项目原有交付/分支规范后再考虑验收与合并。

## 前端任务拆分示例

- **任务 1 / Foundation**：盘点目前按钮、表单、对话框、导航、卡片的实现。输出 merge/adapt/new 清单和单一源 token，不改业务页面。
- **任务 2 / Component kit**：实现主题适配和 6–10 个本次需要的通用组件；建立可访问状态展示页；通过 Gate B。
- **任务 3 / Feature screens**：逐屏替换现有复用模式；保证行为与接口不变；不新增重复 CSS。
- **任务 4 / Quality**：全屏截图与状态对照、修复反模式、评分报告、性能与可访问性抽检。

## 跨 Agent 的共同约定

- 所有 Agent 只引用同一套 token 和共享组件契约；与现有 UI 库冲突时由负责人明确设计决策。
- 基础组件 API 改动必须说明影响页面，必要时同步修改调用方和组件 gallery。
- 不以“设计图好看”为完成标准；业务逻辑、状态、响应和键盘路径必须可用。
- 组件 owner 不负责替功能团队伪造接口数据；Feature Developer 不负责私自重新定义色系。
- Review 问题用“问题位置—反模式—证据—修复—验收”格式记录。

## v6.3 · 视觉审查任务交接

UI Foundation 为 Sidebar/Topbar/Tabs/RecentItem/Table/Search/SplitPane 提供共用状态规范与可访问性；Feature Developer 不得在工作区页自行给选中态叠加强亮条/无意义橙点；QA 逐一检查暗色背景、hover/selected/focus-visible、最近对象与路由的区别，并引用 `references/sidebar-navigation-design.md` 的具体失败症状。任何主动采用强烈视觉/左侧指示线的决定必须说明它表达什么独立信息；禁止仅以个人“AI 味”主观标签替代证据。
