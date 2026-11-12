# Sidebar Color Reference Study · 真实设计来源与可复用的推理

本文件记录经检查的官方设计文档 / 产品设计说明。**这里提炼“设计原因与机制”，不抄其界面或假装知道品牌配色的每个 HEX**。MauForma 附带的示例色板均为原创概念，与品牌官方主题不是同一回事。

| 参考 | 原始来源 | 可以借鉴什么 | 哪种站点合适 | 不能照搬什么 |
| --- | --- | --- | --- | --- |
| **Linear** | [2024 UI redesign](https://linear.app/now/how-we-redesigned-the-linear-ui) / [后续导航降噪讨论](https://linear.app/now/behind-the-latest-design-refresh) | 侧栏不抢主内容、设计先考虑界面密度与对比度；底色 / 强调色 / 对比构成完整主题 | 任务与项目管理、开发者工具、密集工作台 | 不可得出“Linear 深灰最适合所有网站”的结论 |
| **IBM Carbon** | [UI shell left panel](https://www.carbondesignsystem.com/building-blocks/core/components/ui-shell-left-panel/specifications) / [selected colors](https://www.carbondesignsystem.com/building-blocks/foundations/color/overview) | enabled/hover/active/focus 的语义 Token 分开定义，选中由背景+文字/图标层级表达 | 企业后台、运营系统、复杂的侧栏导航 | 不直接复制 IBM 的 Token 值作为用户品牌色 |
| **GitHub Primer** | [Layout](https://primer.style/product/getting-started/foundations/layout/) / [Color usage](https://primer.style/product/getting-started/foundations/color-usage/) | 侧栏辅助主内容，支持 split page；横跨光/暗模式的语义颜色及响应式布局 | 仓库、代码分析、知识结构与列表/详情系统 | 不把 GitHub 原 UI 的样式机械复制到 示例产品 |
| **shadcn/ui** | [Sidebar theming](https://ui.shadcn.com/docs/components/base/sidebar) | 侧栏拥有 background、foreground、primary、accent、border、ring 等独立角色，同时仍由整体主题协调 | React/Vue 等组件工程与可复用 Theme 方案 | shadcn 颜色样例≠用户已经选择的品牌色 |
| **Atlassian Design** | [Design tokens](https://atlassian.design/components/tokens/all-tokens) | Token 单一来源，selected 状态未必必须使用蓝色；可以用中性状态减低视觉噪声 | 企业协作、项目看板、多主题应用 | 不应把某个特性标志下的表现描述为 Atlassian 永远唯一的做法 |

## 只推荐“有可说明的项目适配性”的组合

对用户的仓库分析工作台（侧栏大面积、主内容数据密集、已有蓝色 Logo）至少可对比：

- **石墨侧栏 + 冷白主内容**：保留较强区域边界，视觉焦点在主内容。适合偏好“暗侧栏、亮正文”的用户；蓝色 Logo 可以保留，但不能让所有状态默认变蓝。
- **浅灰侧栏 + 白色主内容**：整个应用更轻，更像统一色阶，适合长时间浏览、搜索、图表比较。要格外注意灰度对比，不是越浅越好。
- **全深色中性工作台**：侧栏略暗于主内容，让界面统一沉稳；适合明确偏好深色的用户，图表和辅助标签需单独测试。
- **暖纸白 + 砂岩侧栏**：适合品牌确实偏暖、研究/知识阅读导向的产品；若产品已有强冷色品牌，不应硬搬。
- **保留品牌蓝**：用户希望蓝色或项目既有成熟品牌蓝时继续用蓝；约束面积和状态角色，而不是默认反蓝。

这些**不是各品牌的官方复制品**，是 MauForma 结合上述原则设计的可选概念。严格区分两件事：**参考网站提供方法论；用户决定最终颜色**。

## 从某网站的截图学习时的证据级别

- **verified_official_documentation**：官方文档明确谈到的设计机制，可引用链接与对应表述；
- **observed_ui**：在某个时间/主题下实际看见的界面表现，需记录截图、日期、light/dark 条件；
- **mauforma_interpretation**：基于多个设计系统推导的原创色板，不能写成“Linear 官方色板”；
- **unverified**：没读取实际文档/没看到截图或不确定现行版本，不可虚构其具体品牌调色板。

Agent 在用户没指定哪种参考站时，只需精选 2–3 个相近场景，不能把 10 个网站做成无差别潮流拼盘。