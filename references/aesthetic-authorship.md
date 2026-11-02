# 外部优秀 Skills 的审美立场与吸收边界

本页记录**来源实际强调的思想**与 MauForma 的独立推导，不将其他作者的个人审美选择改写成普遍禁令。作者仓库会演进，引用时以当时版本为准。我们只参考方法和思想，MauForma 的示例、选型器及文案独立编写，未复制第三方素材、Pro 组件或安装脚本。

| 来源 | 源地址 | 值得保留的审美主张 | 最适合 | 不应机械移植到 |
| --- | --- | --- | --- | --- |
| Impeccable | https://github.com/pbakaus/impeccable | Persuade / Operate / Read / Experience 根据访客成功目标变换视觉尺度；可以主动变大胆也可以降噪 | 全类型网站的页面任务选择 | 把“降噪”当成禁止大胆视觉 |
| Anthropic Frontend Design | https://github.com/anthropics/skills/tree/main/skills/frontend-design | 设计有明确主体与艺术观点，字体、文案和内容语境共同塑造身份，不靠自动套模板 | 品牌、作品集、文化、产品介绍 | 不根据真实内容就随意选奇特字体 |
| UI/UX Pro Max | https://github.com/nextlevelbuilder/ui-ux-pro-max-skill | 多风格知识资料与按产品分类的设计推荐；全局 Master 与页面差异覆盖 | 多页面、多行业、持续迭代的网站 | 让自动评分代替用户最终选择 |
| Taste Skill / Leonxlnx | https://github.com/Leonxlnx/taste-skill | DESIGN_VARIANCE、MOTION_INTENSITY、VISUAL_DENSITY 可调，鼓励非对称、实验性留白和动态视觉 | 创意机构、潮流、艺术展、作品展示 | ERP/CRM 高频操作区默认高变化度 |
| Taste Design DNA / Senlin | https://github.com/senlindesign/taste-skill | 不止提取 WHAT（颜色/字体），还要写 WHY（特定权衡、证据、拒绝的替代） | 竞品分析、视觉迁移、参考网站研究 | 无页面证据却声称复刻原创意图 |
| Vercel Web Design Guidelines | https://github.com/vercel-labs/agent-skills/tree/main/skills/web-design-guidelines | file:line 规则审查、可访问性与交互质量 | 所有 Web 业务实现与 Code Review | 把静态代码扫描当成已做浏览器验收 |
| Vercel Composition Patterns | https://github.com/vercel-labs/agent-skills/tree/main/skills/composition-patterns | 更少布尔 Props、更明确的组件组合和状态边界 | React 复杂可复用组件 | Vue 无差别照抄 React Context/Hooks |
| Vue Best Practices | https://github.com/vuejs-ai/skills/tree/main/skills/vue-best-practices | Composition API、单向数据流、最小响应式状态、清晰组件职责 | Vue 3/Nuxt 的实际工程 | React 代码直接套 Vue 的 SFC 接口 |
| Vercel React Best Practices | https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices | 优先消除请求瀑布和包体积问题，再优化渲染微细节 | React/Next 性能治理 | 性能优化破坏既有语义和可用性 |
| Anthropic Webapp Testing | https://github.com/anthropics/skills/tree/main/skills/webapp-testing | 真实浏览器交互、页面截图与日志核对 | 视觉验收、表单/导航/响应式测试 | 只有静态页面就宣称所有业务功能验证 |

## 审美主张如何被保留

- **独立风格，不被均值化**：实验性风格保留非对称、错位、形态夸张、强动效的权利；克制极简保留安静结构的价值。
- **以任务模式决定适用性**：同一网站的官网属于 Persuade，而其管理后台可能属于 Operate；不用全站套相同密度。
- **参数是表达强度，不是强制评分**：MauForma 的 `variance/motion/density` 是**0–10 的建议区间**，沿用 Taste 三旋钮的思路，不复制它的默认值和强制禁令。
- **源代码与数据权限**：改编外部代码前逐项核对许可证和出处；本包只提供自编规则和示例，未来引入素材必须明确许可证。
- **不滥用负面规则**：大量留白、全大写标签、玻璃拟态、暗黑配色都不是“错误本身”。只有当这些设计和内容/任务不匹配时才构成反例。
