# Browser QA：视觉方案与真实操作的联合验收

借鉴 Anthropic Webapp Testing 的真实浏览器思路，本文件不把静态检查等同于浏览器运行。使用本项目已有 Playwright/浏览器测试设施；没有时先说明限制，不静默安装新浏览器或远程驱动。

## v6.20 · 模糊优化的主动浏览器诊断

用户只说“优化这个页面”时，**先对实际页面做基线无关的缺陷扫描**，不要把运行原有间距基线当作默认通过，也不要只跑 Skill 自带的 Mock。按 `references/proactive-visual-defect-discovery-gate.md` 从实际页面首/中/末、主要状态、宽窄屏检查空间/主次文字/组件/图标配色/交互；可运行 `node scripts/audit_existing_visual_defects.mjs --url <current-page>` 找到 Block/Grid/Flex 或简单包装层中可见面板的既有贴合。再用 v6.19 的 before/after 对比防止引入新问题。工具有覆盖盲点，实际页面未打开不得称为 Browser PASS；含用户隐私的截图和识别信息不得上传公共仓库或 CI artifact。

## 必选验收矩阵（按实际项目选用）

- 视口：桌面 1440px、常见笔记本 1024px、手机 390px 或产品主要断点；检查横向溢出、主视觉裁切、字断行与布局回流。
- 可访问性：Tab / Shift+Tab 焦点路线、Esc 关闭浮层、表单标签、错误信息、可见焦点、语义正确、对比度。
- 主题/设置：浅色/深色（项目支持的）、缩放/系统字体、`prefers-reduced-motion`、低性能回退。
- 真实流程：输入/保存/失败/重试/空状态/权限变化/加载完成；不要用只有静态 Mock 的页面冒充真实服务端。
- 视觉对照：MASTER 与页面 override、当前确认的方案、组件展示页与实际截图；检查焦点、首屏 CTA、留白、信息密度和效果。
- 运行记录：构建、类型检查、UI 单测、E2E（按项目已有命令）；浏览器 Console 与网络错误。

## 审查报告格式

`page | viewport | light/dark | flow | expected | observed | screenshot-path | code-location | severity | fix | re-tested`。

清楚标注三种结果：`PASS`（真运行）、`FAIL`（可复现）、`NOT RUN`（条件不满足），禁止把计划的测试写为已通过。

## 优先级

P0：表单不可用、按钮不可到达、数据不真实、内容被遮挡；P1：严重溢出/对比度/无法关闭模态；P2：排版不一致、无效装饰、轻微动效不合理。

## 可用工具

- 项目自带 Playwright 或相关浏览器工具优先；不自带时按授权安装，禁止修改业务运行环境后宣称“无变化”。
- 静态扫描：`python3 scripts/audit_frontend.py path/to/src` 只提供启发式风险线索；开发者须人工复核。
- 可执行基线：`python3 -m unittest discover -s tests` 与现有 `scripts/validate_*.py`。

## 反面

截图不能证明后端接口实现；一张桌面图不能证明手机断点；grep 到 `prefers-reduced-motion` 字符串也不证明整站真正尊重减少动画设置。

## v6.9 · 页面末端完整性与共享网格复测

新增真实浏览器要求：对有长数据、发布记录、多个 Grid 图表的页面，必须验证**初始视口 + 滚动到最末端**。只截图全页顶端不能证明底部可达。可运行 `node scripts/audit_rendered_layout.mjs --url http://127.0.0.1:5173/releases --out layout-audit`，它输出 viewport 初始/末端截图和报告，需要项目已有 Playwright 或用户授权后安装；脚本没运行时为 NOT RUN。

检查浏览器滚动所有者是 document 还是内部 `main-scroll`、最后可交互/内容项滚动可达、fixed BottomBar 不覆盖、safe-area/page-end padding、无意横向溢出、同排数据卡片起点。对于未打标注的第三方组件，脚本可能无法知道“哪个是最后的有意义的内容”；可以在项目上使用 `data-mf-bottom-content`、`data-mf-grid-row`、`data-mf-grid-panel`、`data-mf-fixed-bar` 辅助判断，不能靠脚本提示直接删除或改组件。截图恰好拍在底边 ≠ 已确认裁切，滚动终点实际仍不可达才是高优先级问题。

## v6.10 · 比较页 Browser QA（覆盖不止 DOM Card）

使用用户实际选定的对象与采样数据，执行选择仓库 → 检查选中对象/legend/series/table columns → 时间窗口变更 → 数据缺失/部分覆盖 → 手机宽度 → 滚动最后一行。标注 `data-mf-selected-id` / `data-mf-legend-id` / `data-mf-series-id` / `data-mf-chart-group` / `data-mf-chart-plot` / `data-mf-chart-label` 能帮助 `scripts/audit_comparison_ui.mjs` 提供几何风险线索，但 Canvas 的轴刻度/标签通常不在普通 DOM 中，必须看真实绘图截图或采用图表引擎内部 API；无结构支持时报告 NOT AUDITED。外框等高 ≠ Plot Area/Axis 等高或标签无重叠。不得以“已跑静态测试”代替浏览器截图。

## v6.11 · 任务列表与详情的浏览器 QA

对 Run Monitor 需实测过滤状态计数及可见任务是否一致、进度是否有实际分子/分母、恢复按钮是否只出现在合法任务、点击详情后是否显示真正阶段/日志、搜索/排序是否保持视图上下文。检查 1440×900 与 390×844 下列表行、长 ID、触摸/键盘和滚动末端。独立概念示例的 `tests/task_center_browser_smoke.mjs` 使用本地 Mock 并对 2 个视口截图；**真实业务**还要集成真实 API、权限、错误、重复操作、后台状态变化与任务重试 E2E，不能因为示例按钮改变了本地内存就称“真实重试完成”。详细规范见 `references/task-center-run-monitor-design.md`。
