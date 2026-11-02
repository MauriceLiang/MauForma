# 示例：设计决策与审查报告

- 用户任务：展示甜品照片，吸引访客到店；素材尚未核实
- Agent 推荐：Premium Showcase 和 Editorial 两套方向（**推荐 ≠ 已确认**）
- 项目模式：品牌首页 Persuade；商品列表 Operate/Persuade 混合
- 页面预览：高质量食物摄影可作单主体，否则采用强排版 + 适量商品图片
- 构图自我批判：是否只因“美食”就套暖色？是否在没有实际摄影素材时过度放大？
- UI 组件：统一 Button / Field / Navigation 的外观、状态、键盘行为
- 渲染证据：NOT RUN（仅文档示例，不声明浏览器测试）
- 来源：MauForma 原创综合，参考 `references/aesthetic-authorship.md`

## 如何改成可执行项目

使用 `scripts/search_design_knowledge.py` 推荐方案；用户决定后保存 MASTER 与页面 override，然后以 `scripts/audit_frontend.py` 和 `scripts/browser_qa.mjs` 收集风险和实际渲染报告；最后按照 `references/browser-qa-protocol.md` 对照截图逐条审查。
