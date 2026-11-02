# MauForma · 风格档案总览

八种档案由 MauForma 综合外部优秀设计思想独立编写，**不是**外部作者官方风格分类。各档案都保留具体审美意图，允许用户明确选择高实验性或高动效的方向；不把所有项目收敛到极简模板。

| ID | 视觉表现 | 最适合 | 默认使用风险 |
| --- | --- | --- | --- |
| editorial | 如翻阅高质量文化杂志：标题、摄影和内容按叙事节奏交替出现 | architecture / art / photography | 信息结构复杂时需更谨慎的移动端重排 |
| experimental | 大胆的留白、错位与尺度冲突产生难以与通用模板混淆的辨识度 | creative-studio / portfolio / art-exhibition | 高差异布局需额外响应式和无障碍验证 |
| premium-showcase | 一个精心拍摄的产品占据最大视觉面积，其他信息为其服务 | food / car / furniture | 素材低质时大图会放大缺点 |
| playful | 鲜明但组织良好的颜色、插画与富有性格的反馈，营造可探索的轻松氛围 | children-education / games / entertainment | 过度趣味化会削弱专业可信度 |
| cinematic | 舞台式镜头、分镜节奏与沉浸视觉使访客在滚动中逐步理解主题 | gaming / film / digital-art | 高视频/Canvas/WebGL 成本 |
| calm-minimal | 平静、清楚的排版和节制的色彩，让内容而非装饰成为焦点 | developer-tools / professional-software / enterprise-service | 如果所有元素权重完全相等仍会显得乏味 |
| functional | 搜索、筛选、主要任务与状态一眼可达，不用滚动寻找基础操作 | erp / crm / admin | 视觉冲击可低于品牌官网 |
| reading-first | 内容结构在初次浏览时就容易理解，阅读过程没有不必要的干扰 | docs / knowledge-base / news | 视觉实验性适度收敛以换取理解效率 |

## 检索与推荐

运行 `python3 scripts/search_design_knowledge.py --query "蛋糕 店铺 摄影 到店" --mode Persuade --limit 3`。用户已经给出方向时应优先遵守用户决定；程序推荐只是可说明理由的建议，并非设计确认。配置范围和每条档案的作者出处详见 `assets/style-knowledge.json` 与 `references/aesthetic-authorship.md`。

## 解释原则

1. 先获取真实内容、目标用户、素材情况和首要任务；再选风格。
2. 每个方案说明首屏谁最大、图片与文字比例、信息密度、动效、成本和反例。
3. 同一产品不同页面可以在共享品牌 Token 下分别使用 `Persuade`、`Operate`、`Read`、`Experience` 等模式。
4. 风格是审美立场，不是固定组件模板；允许混合，但要说明采用什么、舍弃什么。
