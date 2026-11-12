<div align="center">

# MauForma

**Design with intent. Build with precision.**

面向现代 Web 产品的设计与前端工程 Agent Skill。

[工作方式](#工作方式) · [适用范围](#适用范围) · [快速开始](#快速开始) · [参考资料](#参考资料) · [质量检查](#质量检查)

</div>

---

## 这是什么

MauForma 帮助 Agent 在设计和开发网页时先理解真实用户任务，再处理信息架构、视觉层级、排版、组件、交互、技术选型与验证。它不是一套固定的后台模板，也不会强迫每个网站使用相同的颜色、字体、侧栏和卡片。

**入口只有 [SKILL.md](SKILL.md)**。它是一份稳定的工作规范；具体知识拆分在 `references/`，合成演示位于 `examples/` 和 `assets/`，检查工具位于 `scripts/`。历史改动单独记录在 [CHANGELOG.md](CHANGELOG.md)，不会逐次堆入 Skill 正文。

## 适用范围

| 网站或产品 | 设计重点 |
| --- | --- |
| 品牌官网、营销与产品展示 | 视觉辨识度、叙事、内容与转化 |
| 文章、知识、资讯与阅读 | 排版、导航、阅读顺序与检索 |
| 学习与教育 | 学习任务、内容节奏、练习和反馈 |
| 消费应用与电子商务 | 流程、信任、操作可发现性与移动体验 |
| 艺术、创作与作品展示 | 清晰的艺术方向、媒体表达和动效 |
| 数据、运营与管理工作台 | 信息密度、状态、筛选、表格和图表 |
| 混合型产品 | 按页面任务分别设计，不统一套用后台布局 |

支持 Vue/Nuxt、React/Next、Svelte/SvelteKit、Angular、Solid、Astro、原生 Web，以及 Electron/Tauri 的 Web 界面。原生移动端和原生桌面 UI 不属于直接的组件实现范围。

## 工作方式

1. **了解约束**：判断产品类型、当前页面任务、目标受众、已有设计和工程。对明确的局部修复不重复问卷，也不改动无关部分。
2. **确认 UX**：先处理主要任务、内容取舍、导航、信息架构和视觉中心，再挑选字体、颜色与效果。
3. **建立共用规则**：从现有或新建 Tokens 出发，处理字体角色、间距、栅格、组件状态、图标与交互，保留风格差异。
4. **根据场景实现**：支持操作型、阅读型、说服型与体验型页面；框架与组件库优先沿用项目已有选择。
5. **实际复验**：查看真实渲染页面及关键交互，检查间距、文字、图表、滚动、键盘、深浅色与适用的视口；区分真实通过、仅静态检查与未运行。

设计要有明确原因：删除无意义说明，但保留真正的数据来源；压缩冗余卡片，但不把独立模块拼在一起；允许个性的颜色与动画，但不能牺牲可读性和实际功能。

## 快速开始

将本仓库安装在所使用 Agent 所支持的 Skill 目录中，并在设计或前端开发任务里明确调用 `mauforma`（目录位置依据 Agent 客户端而定）。无需在普通 Web 项目里安装仓库全部技术依赖。

本仓库可独立运行知识库查询和静态检查：

```bash
# 按内容与页面目标检索设计知识
python3 scripts/search_design_knowledge.py --query "阅读 内容 编辑" --mode Read

# 按需求检索技术，而不是一次安装整套库
python3 scripts/search_visual_tech.py --goal "图表 数据交互"

# 针对目标工程做静态审计
python3 scripts/audit_frontend.py ./src --format json

# 验证 Skill 的结构和约束
python3 scripts/validate_web_skill.py
python3 scripts/validate_skill_hygiene.py
python3 -m unittest discover -s tests -v
```

需要验证页面渲染时，可在具有 Playwright 和可访问开发服务器的环境中运行 `scripts/browser_qa.mjs` 及针对相关布局的浏览器脚本。**静态检查、演示页面通过，不等于目标产品已通过视觉、交互和业务验收。**

## 参考资料

只按任务读取必要资料，不把所有文件一并塞进 Agent 上下文。

| 主题 | 主要入口 |
| --- | --- |
| 设计发现与产品 UX | [设计探索](references/design-discovery-interview.md)、[产品体验路由](references/product-experience-routing-gate.md) |
| 艺术方向与视觉风格 | [风格档案](references/design-style-catalog.md)、[构图先行](references/composition-first-design.md) |
| 内容与字体 | [内容密度](references/page-density-and-content-priority.md)、[文案必要性](references/semantic-copy-hygiene.md)、[字体角色](references/typography-hierarchy.md) |
| 空间、布局与组件 | [语义间距](references/semantic-spacing-rhythm-gate.md)、[网格与视口](references/grid-alignment-and-viewport-safety.md)、[组件工程](references/component-first.md) |
| 导航、颜色与图标 | [导航架构](references/navigation-architecture.md)、[配色](references/palette-art-direction.md)、[图标语义](references/icon-art-direction-gate.md) |
| 表单、数据与交互 | [设置/表单](references/settings-form-layout-gate.md)、[图表](references/chart-interior-alignment.md)、[动效](references/motion-consent-experience-gate.md) |
| 技术实现 | [框架支持](references/framework-support-matrix.md)、[业务组件库](references/enterprise-ui-library-guide.md)、[创意组件](references/creative-component-libraries.md) |
| 验证与交付 | [视觉 QA](references/visual-qa.md)、[浏览器检查](references/browser-qa-protocol.md) |

更多专项文档由 [SKILL.md](SKILL.md) 的任务路由表指引。

## 质量检查

主要约束：

- **通用优先**：Skill 不写入用户项目名、原始业务资料、真实截图及可识别来源；示例使用明确的合成内容。
- **按用途设计**：不把所有网站简化为同一套工作台、极简风或演示模板。
- **用户决定优先**：尊重明确的颜色、视觉风格、平台范围与动效选择。
- **工程可验证**：代码能运行、控件真实可用、组件在目标环境复用，不用合成样例冒充真实产品结果。
- **文档不堆版本补丁**：行为规则写在稳定主题章节；修改历史只写 `CHANGELOG.md`。

参考图片及其变体不得未经授权存入公共 Skill。引用第三方技术、图标、字体或资源时核查来源、许可证与依赖版本。

[查看更新历史](CHANGELOG.md)
