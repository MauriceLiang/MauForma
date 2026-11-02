# 外部优秀设计案例库：按需复用，不复制品牌素材

MauForma 保留八种自有风格档案（`assets/style-knowledge.json`），并复用两个公开来源。两者服务于不同层次：

| 来源 | 真实内容 | 用途 | 局限 |
| --- | --- | --- | --- |
| [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/main/src/ui-ux-pro-max/data) | 88 风格档案（79 searchable）、192 产品类别/行业策略、配色/字体/布局/UX 数据（2026-11-01 摘要） | 推理适合某行业/任务的设计方向 | 主要是规则/建议，并非 192 个已审查的网站实例 |
| [VoltAgent awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | 84 个品牌站点的 `DESIGN.md` 分析，包含色彩、字体、构图、组件、规则和响应式 | 获得具体网站/品牌的设计案例和具体可借鉴细节 | 来自公开网站的**社区分析**，不是品牌官方发布的 Design System |

目录索引：`assets/external-design-cases.json`（2026-11-02 快照，记录上游 commit SHA 和 84 个外部 DESIGN.md 链接）。不将 84 个完整文档直接粘贴进 Skill：避免上下文膨胀，并可检查上游更新。

## 如何在设计访谈中使用

1. 先根据用户网站用途、内容形态、受众与真实素材，使用 `scripts/search_design_knowledge.py` 选候选设计方向。
2. 用 `python3 scripts/search_design_cases.py --query "甜品 咖啡 门店" --style premium-showcase --limit 5` 查具体品牌案例。
3. **仅对命中的候选**读取上游 `DESIGN.md`；优先从 `review_status=sampled` 的已检查案例开始。`candidate` 是按行业推断的潜在候选；`indexed_unreviewed` 只是收录。
4. 提取可迁移的内容：主体大小、留白逻辑、颜色角色、字体层次、组件状态与响应式。必须说明这是上游文档描述、MauForma 分析还是视觉实测。
5. 若涉及现行品牌视觉，查官方站点或真实浏览器截图核对，不凭旧 DESIGN.md 宣称当前官方精确色值。
6. 给用户 2–3 个可解释的方案和实在的优缺点，不以品牌案例的存在作为用户已确认风格的证据。

## 主要示例（已抽查正文）

- [Apple DESIGN.md](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/apple)：产品摄影优先、浅深展示面交替、精简 UI → 高级产品展示。
- [Tesla DESIGN.md](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/tesla)：全幅汽车画面、极简控件 → 产品展示 / 沉浸式。
- [Linear DESIGN.md](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/linear.app)：深色中性表面、稀少强调色、产品截图 → 开发工具与专业软件。
- [Stripe DESIGN.md](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/stripe)：网格渐变与金融/技术信息层级 → 品牌官网与业务产品组合。
- [Starbucks DESIGN.md](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/starbucks)：门店材料感、绿色色彩角色与产品摄影 → 食品饮品零售。

其他品牌可能通过关键词命中，但在阅读并核验对应文档前不作为已确认的优秀设计范例。README 提及的 `preview.html` 不一定包含于仓库每个案例目录，预览通常应在上游网站查看，不得承诺仓库已包含可运行预览。

## 版权与证据

上游两仓库都以 MIT 发布各自文档/代码，但不代表 Apple、Tesla、Stripe 等公司的商标、图片和专有字体可以自由复制。MauForma 只保存品牌案例的**来源链接和原创筛选注释**，不复制品牌 Logo、图片或专有字体。下游需要再分发上游文档时，保留原许可证/署名，审核品牌资产使用条件。

某些案例文件采用 `version: alpha` 或 `Inspired` 说明，不应将其内容冒充官方网站正式设计规范。