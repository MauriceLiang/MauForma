# v4 推荐新提示词入口

本文件保留早期模板以兼容旧引用；对于 Web/Vue/React 等网页项目请优先使用 `examples/prompt-library-web.md` 与 `references/ai-frontend-prompt-policy.md`。避免旧模板中的原生 macOS 范围与默认绑定 Anime.js。

---

# Agent 可复制任务指令

## 从零开始的新前端（建议优先）

> 使用 `$mauforma` 完成前端设计。**先不要写业务页面**。先盘点技术栈和现成 UI 组件，明确一个与产品定位匹配的视觉方向，设计可创造的主题配色（无需使用原站粉蓝渐变），确定 semantic tokens、间距、圆角、动效与密度配置。接着先建设最小共享 UI 组件集及组件状态展示页，通过 Gate A/B 自查后再实现业务页面。页面只组合组件，禁止重复定义按钮、表单、对话框、导航样式。完成后输出优秀/反面案例对照、截图 QA、100 分量表评分和阻断项。**后台、工具、管理页面默认不要英文装饰小标题、巨型 Hero、宣传口号与重复说明；先完成共享 UiPageHeader。**

## 为已有 Vue/Tauri/React 项目改造外观

> 使用 `$mauforma` 盘点现有组件，优先继承 Reka UI / Radix 等无障碍 primitives。不要改变业务接口与路由。将视觉值迁移到一套 theme/tokens，统一 Button/Input/Dialog/Navigation/Status，并制作组件 gallery。确认组件一致后逐屏重构，消除散落的页面级样式，最后在宽窄窗口与深浅模式下验收。**对于后台页，检查并清理“英文 eyebrow + 大标题 + 套话 + 巨大留白”等模板痕迹，统一 PageHeader。**

## 只审查、不修改

> 按 `$mauforma` 的 good-vs-bad 和 ui-review-rubric 做视觉审查。先分析组件复用度、主题一致性、文本/控件对比、圆角层级、留白节奏、阴影、状态、动画和响应式。对每项问题给出“位置—差的做法—优秀替代方案—修复步骤—验收方式”。先不要写代码；若未实际截图请注明是静态审查。

## 让 Agent 团队分阶段实施

> 负责人先完成主题决策和 token，组件 Agent 独立完成共享组件 + gallery 并交付 Gate B；业务开发 Agent 必须引用共享组件完成页面，禁止私造局部按钮/弹窗；测试 Agent 依据 good-vs-bad、QA 清单和 100 分量表执行视觉与交互验收。每个阶段都需要有可检查的交付物，严禁只上传好看的截图但没有真实功能。
