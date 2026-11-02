# Design System MASTER（项目级示例，不代表已确认的真实用户选择）

- **项目**：示例复合品牌网站
- **用途**：产品介绍、商品浏览与运营后台
- **决策状态**：全部 delegated（演示用的 Agent 建议），用户真实确认前不得视为 confirmed
- **品牌语言**：质感突出、清晰文案、节制状态色；允许展示页与工作台不同密度
- **全局 Tokens**：`--surface`、`--text`、`--muted`、`--accent`、`--border`、`--focus-ring`，避免各页硬编码主色
- **排版**：统一字体家族和语义层级（display/h1/h2/body/caption），具体字号可按页面用途覆盖
- **组件**：UiButton、UiField、UiDialog、UiPageHeader、UiFeedback 等共享外观及键盘/状态
- **动效**：默认简短状态过渡，展示首页可追加受控章节动效；必须支持 reduced-motion
- **检查**：用户选择 → 视觉方案自评 → Tokens → 组件展示 → 页面 → 浏览器 QA

页面例外见 `pages/home.md` 与 `pages/dashboard.md`。请勿将本文件的示例参数直接复制为实际项目的已确认选择。
