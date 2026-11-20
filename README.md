<div align="center">

# MauForma

**Design with intent. Build with precision.**

面向现代 Web 产品的设计与前端工程 Agent Skill。

[工作方式](#工作方式) · [适用范围](#适用范围) · [快速开始](#快速开始) · [参考资料](#参考资料) · [质量检查](#质量检查) · [开源致谢](#开源参考与致谢)

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

## 按任务选择设计深度

根据需求选择 `shape`（新建/重设计）、`polish`（视觉精修）、`review`（独立审美评审）、`fidelity`（Figma 稿高保真实现）、`fix`（局部缺陷修复），无需同时安装或运行多套外部设计 Skills。详见 [Design Craft Loop](references/design-craft-loop.md) 与 [Figma Fidelity Mode](references/figma-fidelity-workflow.md)。

## 工作方式

1. **了解约束**：判断产品类型、当前页面任务、目标受众、已有设计和工程。对明确的局部修复不重复问卷，也不改动无关部分。
2. **确认 UX**：先处理主要任务、内容取舍、导航、信息架构和视觉中心，再挑选字体、颜色与效果。
3. **建立共用规则**：从现有或新建 Tokens 出发，处理字体角色、间距、栅格、组件状态、图标与交互，保留风格差异。
4. **根据场景实现**：支持操作型、阅读型、说服型与体验型页面；框架与组件库优先沿用项目已有选择。
5. **实际复验**：查看真实渲染页面及关键交互，检查间距、文字、图表、滚动、键盘、深浅色与适用的视口；区分真实通过、仅静态检查与未运行。

设计要有明确原因：删除无意义说明，但保留真正的数据来源；压缩冗余卡片，但不把独立模块拼在一起；允许个性的颜色与动画，但不能牺牲可读性和实际功能。

## 页头文案审查：既有页面也不能漏检

新页面与现有项目的视觉优化、重构或评审，都需要检查主标题上方的**原有及新增**眉题、双语解释标签、装饰编号和功能前缀。只负责重复用途或营造层级的文字按语义删除或移位，不能因为历史存在而保留；工作台、数据、列表、设置等任务型页面的解释性眉题属于硬性否决项。

规则适用于学习、科普、阅读、可视化、创意和品牌/营销页面，但**不是一刀切删除所有 Hero 前导**：真实面包屑、正式产品标识、已确认 Tagline、有效内容章节和必要状态应保留或移到对应角色。审核必须在目标页面复验，不能以静态脚本 PASS 代替。详见 [跨产品 Gate H-Base 与功能页 H0](references/page-header-antipatterns.md)。

## 卡片彩色贴边竖条：新旧页面一律禁止

新建页面、既有项目的视觉优化与组件重构，均**不得生成或保留与 Card/Panel/Section 边框贴合、沿圆角延伸的彩色粗竖条**。默认不使用装饰彩边；确有独立信息用途时，可在模块外侧放置短标记，与卡片完整边框保留可见正向间距。键盘焦点轮廓、真实进度和数据图形仍按语义设计。详见 [Surface Edge Accent Gate S0](references/surface-edge-accent-gate.md)。

## 组件库优先：第一版就要有完整的交互控件

MauForma 在页面开发前会检查项目现有的组件库；如果没有合适的方案，Agent 应**主动为当前前端框架选择并实际采用一套成熟组件库或可访问原语**，优先解决 Select、Combobox、DropdownMenu、Button、Checkbox、Radio、Switch、Dialog 等容易造成视觉和交互返工的控件。

组件优先不等于从零造按钮和下拉菜单。选定组件方案后先统一 Theme/Tokens、完成必要控件的状态检查，再批量编写业务页面。已有主库优先继承，静态页面和合理的原生系统控件不强装大组件库。完整规则见 [Component Library First](references/component-library-first-gate.md)。

## 高级动效：Motion Craft & Rehearsal

MauForma 将动效视为可用性、状态连续性和产品质感的一部分，而不是统一的 Hover 特效或页面淡入。使用分镜、运动因果、缓动节奏、视觉交接和逐帧自查，转化为适用于**真实 Web 产品**的通用规则：

- **先设计状态变化**：触发 → 运动中的关系 → 结果 → 反向/中断 → 低动效；保留按钮、指示器、弹窗、列表等对象的身份和空间锚点。
- **细腻的时间编排**：操作即时响应，相关对象重叠、错峰、连贯让位；文字、数字、布局变化不突然闪跳或糊字。
- **真实页面逐帧验证**：在目标路由录制交互前/中/后、反向与 reduced-motion，逐帧检查跳变、重影、漂移，修复后重录。可选 `scripts/motion_rehearsal.mjs`；脚本只输出证据，不能判定审美通过。
- **保留框架自由**：Vue、React 等均能应用规则；不强制安装 Stageshow React Kit、动画引擎或录制工具。模拟鼠标/宣传动画只用于明确需要展示叙事的场景，不伪装为功能测试。

规范见 [Motion Craft & Continuity](references/motion-craft-and-continuity.md) 与 [Motion Rehearsal & Evidence](references/motion-rehearsal-and-evidence.md)。

仓库包含一份**原创、无需前端框架依赖的可交互实验页** [Motion Continuity Lab](assets/motion-continuity-lab.html)，演示选中指示器、真实位置变化、按钮状态和空间披露。可直接用浏览器打开；若要用自动取证工具录制，启动静态服务器：

```bash
python3 -m http.server 8000
# 另一个终端运行（需要项目中已有 Playwright + Chromium）
node scripts/motion_rehearsal.mjs \
  --url http://127.0.0.1:8000/assets/motion-continuity-lab.html \
  --scenario assets/motion-continuity-lab.scenario.json \
  --out ./artifacts/motion-lab
```

该实验的数据和交互完全为合成模拟。真实项目必须使用实际 UI 路由/选择器再次复验。动画强度仍尊重用户确认选择和系统减少动态效果；高频工作界面强调响应速度，展示型网站可在授权范围内采用更丰富的节奏。

## 可选视觉技术：Liquid Glass

MauForma 可以按需分析和设计液态玻璃的**透明、折射、高光、阴影**四层光学近似，模糊作为可选额外效果，而不是全站默认皮肤。Web 端 SVG 背景折射具有浏览器兼容限制，重要按钮与文字必须保持 DOM 语义与静态降级。详见 [液态玻璃光学规范](references/liquid-glass-optics.md) 与 [独立交互教学实验](assets/liquid-glass-layer-lab.html)。

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

# （可选）在有运行中的真实项目与 Playwright 环境时，录制关键动效
# 先用自己的真实页面选择器替换示例 scenario，再执行：
# node scripts/motion_rehearsal.mjs --url http://localhost:3000 --scenario ./my-motion-scenario.json

# 验证 Skill 的结构和约束
python3 scripts/validate_web_skill.py
python3 scripts/validate_skill_hygiene.py
python3 scripts/validate_page_header_copy.py
python3 scripts/validate_surface_edge_accent.py
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
| 空间、布局与组件 | [语义间距](references/semantic-spacing-rhythm-gate.md)、[网格与视口](references/grid-alignment-and-viewport-safety.md)、[卡片贴边彩条门禁](references/surface-edge-accent-gate.md)、[组件工程](references/component-first.md) |
| 导航、颜色与图标 | [导航架构](references/navigation-architecture.md)、[侧栏选中指示条](references/sidebar-selection-indicator-gate.md)、[配色](references/palette-art-direction.md)、[图标语义](references/icon-art-direction-gate.md) |
| 表单、数据与交互 | [设置/表单](references/settings-form-layout-gate.md)、[图表](references/chart-interior-alignment.md)、[动效偏好](references/motion-consent-experience-gate.md)、[动效工艺](references/motion-craft-and-continuity.md) |
| 技术实现 | [框架支持](references/framework-support-matrix.md)、[业务组件库](references/enterprise-ui-library-guide.md)、[创意组件](references/creative-component-libraries.md) |
| 验证与交付 | [视觉 QA](references/visual-qa.md)、[浏览器检查](references/browser-qa-protocol.md)、[逐帧动效验收](references/motion-rehearsal-and-evidence.md) |

更多专项文档由 [SKILL.md](SKILL.md) 的任务路由表指引。

## 质量检查

主要约束：

- **通用优先**：Skill 不写入用户项目名、原始业务资料、真实截图及可识别来源；示例使用明确的合成内容。
- **按用途设计**：不把所有网站简化为同一套工作台、极简风或演示模板。
- **用户决定优先**：尊重明确的颜色、视觉风格、平台范围与动效选择。
- **工程可验证**：代码能运行、控件真实可用、组件在目标环境复用，不用合成样例冒充真实产品结果。
- **文档不堆版本补丁**：行为规则写在稳定主题章节；修改历史只写 `CHANGELOG.md`。

参考图片及其变体不得未经授权存入公共 Skill。引用第三方技术、图标、字体或资源时核查来源、许可证与依赖版本。

## 开源参考与致谢

MauForma 的设计方法离不开开放的设计知识、工具与社区实践。感谢下列作者、维护者和贡献者公开自己的工作，让我们能够学习、比较和重新思考优秀的产品体验。

**特别感谢 Benji Taylor 的 Stageshow。** 它对动效分镜、运动因果、状态连续性、视觉交接、逐帧检查以及独立复审的实践，为 MauForma 的高级动效规范带来了重要启发。MauForma 将这些思想整理为适用于真实 Web 产品和多种前端框架的通用工作流，而不是直接移植 Stageshow 的 React Kit、演示资产或脚本。

### 设计 Skill 与方法论启发

| 项目及作者 | 主要学习方向 |
| --- | --- |
| [Stageshow — Benji Taylor](https://github.com/benjitaylor/skills/tree/main/stageshow) | 可信的产品界面演示、运动因果、节奏与动效质量复验 |
| [Frontend Design — Anthropic](https://github.com/anthropics/claude-code/tree/main/plugins/frontend-design/skills/frontend-design) | 设计意图、视觉方向与反模板化 |
| [Impeccable — Paul Bakaus](https://github.com/pbakaus/impeccable) | 分维度的视觉精修与设计质量检查 |
| [Taste Skill — senlindesign](https://github.com/senlindesign/taste-skill) | 设计品味与审美判断的讨论 |
| [Taste Skill — Leonxlnx](https://github.com/Leonxlnx/taste-skill) | 不同实现中的视觉判断与验证方式 |
| [Theme Factory — Anthropic](https://github.com/anthropics/skills/tree/main/skills/theme-factory) | 主题与视觉语言的一致性 |
| [Designer Skills — julianoczkowski](https://github.com/julianoczkowski/designer-skills) | 分阶段设计工作流与审查 |

Stageshow 的具体参考包括 [Motion](https://github.com/benjitaylor/skills/blob/main/stageshow/references/motion.md)、[Choreography](https://github.com/benjitaylor/skills/blob/main/stageshow/references/choreography.md)、[Verify](https://github.com/benjitaylor/skills/blob/main/stageshow/references/verify.md)、[Rehearse](https://github.com/benjitaylor/skills/blob/main/stageshow/references/rehearse.md) 和 [Review](https://github.com/benjitaylor/skills/blob/main/stageshow/references/review.md)。这些出处集中保存在 README，避免在 Agent 高频读取的规则文档里重复附上链接和致谢说明。

### 设计体系、可访问性与浏览器规范

感谢以下团队持续公开设计原则和标准：

- [IBM Carbon Design System](https://carbondesignsystem.com/)（动效、图标、组件）、[Material Design](https://m3.material.io/)（交互与动效）、[W3C WAI / WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)（可访问性与减少非必要动画）。
- [MDN Web Docs](https://developer.mozilla.org/)（CSS、Web Animations API、SVG、View Transitions、浏览器兼容性）与 [WebKit](https://webkit.org/) 公开兼容性资料。
- 动效相关原始资料：[Carbon Motion](https://www.carbondesignsystem.com/building-blocks/foundations/motion/overview)、[WCAG Animation from Interactions](https://www.w3.org/WAI/WCAG22/Understanding/animation-from-interactions)、[W3C C39](https://www.w3.org/WAI/WCAG22/Techniques/css/C39)、[MDN prefers-reduced-motion](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-reduced-motion)、[Material Motion Timing](https://m1.material.io/motion/duration-easing.html)、[Motion Layout](https://motion.dev/docs/layout-animations) 与 [Motion Gestures](https://motion.dev/docs/react-animation)。
- [Lucide](https://lucide.dev/)、[Tabler Icons](https://tabler.io/icons)、[Phosphor Icons](https://phosphoricons.com/)（图标设计与资源核对）。

### 动效、组件与可视化生态

以下主要作为**选型、API 或视觉实现参考**，不代表它们是 MauForma 的强制依赖，也不意味着已将其源码整体纳入仓库。

- 动画与交互：[Motion](https://motion.dev/)、[GSAP](https://gsap.com/)、[Anime.js](https://animejs.com/)、[FormKit AutoAnimate](https://auto-animate.formkit.com/)、[Rive](https://rive.app/)、[LottieFiles](https://lottiefiles.com/)。
- 创意组件：[React Bits](https://reactbits.dev/)、[Vue Bits](https://vue-bits.dev/)、[Inspira UI](https://inspira-ui.com/)、[Magic UI](https://magicui.design/)、[Aceternity UI](https://ui.aceternity.com/)。
- 基础及企业 UI：[Reka UI](https://reka-ui.com/)、[Radix Primitives](https://www.radix-ui.com/primitives)、[shadcn/ui](https://ui.shadcn.com/)、[shadcn-vue](https://www.shadcn-vue.com/)、[Ant Design](https://ant.design/)、[Ant Design Vue](https://www.antdv.com/)、[Element Plus](https://element-plus.org/)、[Naive UI](https://www.naiveui.com/)、[Arco Design](https://arco.design/)、[PrimeVue](https://primevue.org/)、[PrimeReact](https://primereact.org/)、[MUI](https://mui.com/)、[Mantine](https://mantine.dev/)、[Angular Material](https://material.angular.dev/)、[NG-ZORRO](https://ng.ant.design/)、[PrimeNG](https://primeng.org/)。
- 可视化与图形：[PixiJS](https://pixijs.com/)、[Three.js](https://threejs.org/)、[Curtains.js](https://www.curtainsjs.com/)、[Apache ECharts](https://echarts.apache.org/)、[Rough.js](https://roughjs.com/)、[Vivus](https://github.com/maxwellito/vivus)、[tsParticles](https://particles.js.org/)、[Matter.js](https://brm.io/matter-js/)。

### 版权与致谢边界

- **学习设计思想不等于复制作品。** 除特别注明的资源外，MauForma 的规则、示例和验证脚本为本项目独立组织的实现；上述项目和作者不因列入参考而对 MauForma 提供背书。
- 如实际使用、修改或再分发第三方代码、图标、字体、图片或其他素材，必须按对应版本的许可证保留必要的版权与许可声明；README 致谢**不能替代**许可证义务。
- 仓库使用的 Lucide 示例 SVG 对应许可文本保留于 [Lucide 许可说明](assets/icon-art-direction-lucide-license.txt)。其他框架或组件的许可证须在实际引入时逐项核对。
- 项目和文档可能更新，涉及 API、兼容性、收费条款或许可证的内容应以各项目当前官方资料为准。

再次感谢开源社区持续分享高质量的设计方法与工程实践。

[查看更新历史](CHANGELOG.md)
