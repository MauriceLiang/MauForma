# Browser QA：视觉方案与真实操作的联合验收

借鉴 Anthropic Webapp Testing 的真实浏览器思路，本文件不把静态检查等同于浏览器运行。使用本项目已有 Playwright/浏览器测试设施；没有时先说明限制，不静默安装新浏览器或远程驱动。

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
