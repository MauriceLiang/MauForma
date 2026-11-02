# MauForma v6.0

**Web Design & Frontend Engineering Skill**  
*统一视觉语言、可复用组件、创意动效与跨框架前端工程规范。*

MauForma 由 Maurice 的品牌前缀 **Mau** 与代表形态/形式的 **Forma** 组合而成。它是此前 Soft Precision UI v5.0 的正式更名版本：**已有设计标准、组件示例、正反案例、动效目录与企业 UI 组件库指南均予以保留**，不改变设计工作的主要执行规则。

## 安装（Codex / Agent Skills）

解压 ZIP，复制完整 `mauforma/` 文件夹至：

- 全局：`~/.agents/skills/mauforma/`
- 项目级：`<项目目录>/.agents/skills/mauforma/`

随后在 Codex 中使用 `$mauforma`。**必须复制整个文件夹**，不能只复制 `SKILL.md`，因为主文件会按任务需要引用 `references/`、`examples/`、`assets/` 与 `scripts/`。

例如：

```text
$mauforma

请先盘点当前 Vue 或 React 项目的组件库和视觉风格；
统一 Design Tokens 与共享组件，通过组件验收后再实现业务页面。
按产品类型选择适当动效，并在浏览器中检查响应式、主题、交互状态和可访问性。
```

## v6.0 · 设计智能与质量工具

此次升级按《MauForma 下一阶段升级方案》的 P0–P3 实施，在原有 Vue/React、组件优先和动效体系上**扩展设计决策能力**，没有替换主框架或修改现有 114 种动画配方。

- **八种风格档案**：每种保留独立审美立场、视觉焦点、构图、适用网站、素材前提、优缺点和出处。见 [风格目录](references/design-style-catalog.md) / [结构化知识](assets/style-knowledge.json)。
- **尊重作者审美**：记录 Impeccable、Anthropic、UI/UX Pro Max、Taste、Vercel/Vue 等设计/工程来源的观点与适用条件，参见 [来源与审美边界](references/aesthetic-authorship.md)。
- **Art Direction**：根据 Persuade/Operate/Read/Experience 模式推荐 2–3 套方案，必须做内容相关的设计批判，见 [艺术指导](references/art-direction-critique.md)。
- **可继承的项目设计系统**：全局 MASTER + 页面差异，确保共享设计语言同时允许不同页面密度，见 [层级规则](references/project-design-hierarchy.md)。
- **Design DNA**：根据实际证据提取参考网站的 WHAT/WHY 与设计权衡；不把推断冒充真实 CSS 数值，见 [协议](references/design-dna-protocol.md)。
- **工程规范与自动验收**：加强 React/Vue 组件 API 与性能规则，增加静态风险扫描、可选浏览器截图采集、回归测试和 GitHub Actions 工作流。

### 常用命令

```bash
python3 scripts/search_design_knowledge.py --query "甜品 摄影 到店" --mode Persuade --json
python3 scripts/init_design_system.py --project-root . --name "Project" --style premium-showcase --page home --mode Persuade
# 上面仅预览；确认后追加 --apply，已有文件不覆盖
python3 scripts/validate_intelligence.py
python3 -m unittest discover -s tests -v
python3 scripts/audit_frontend.py ./src --format json
# 仅在项目已安装 Playwright 时（不会自动安装）：
node scripts/browser_qa.mjs --url http://localhost:3000
```

静态规则仅返回待核实风险；浏览器截图不等于完成了后端业务验证。对于已有明确风格的用户，不允许用自动推荐覆盖其决定。

## v5.2 设计选择能力

新建或整体重设计时，若用户**不知道想要什么风格**，先询问网站用途、主要展示内容及访客最重要的操作；由 Agent 先根据这些内容判断适合的构图、视觉焦点与页面级信息密度，然后给出 2–3 套有清楚区别、可理解的推荐方案。用户选择方向后，才分轮确认更小范围的图片比例、配色氛围、信息密度与动效等属性。已有明确风格则直接沿用，避免重复提问。具体流程见 [`references/design-discovery-interview.md`](references/design-discovery-interview.md)，设计简报结构见 [`assets/design-brief.schema.json`](assets/design-brief.schema.json)。完整对话示例见 [`examples/design-discovery-dialogues.md`](examples/design-discovery-dialogues.md)。不重复询问已明确的项目偏好，也不把展示页的低信息密度机械移植到后台表格。

## 主要能力

- **广泛的 Web 框架**：Vue 3 / Nuxt、React / Next.js；兼顾 Svelte、Angular、Solid、Astro、原生 HTML/CSS/JavaScript。
- **组件优先**：现有组件盘点、主题 Token、共享组件、组件展示、业务组合、浏览器 QA 分阶段执行。
- **视觉设计**：可定制颜色主题、浅/深色、不同布局密度、字体/圆角/间距/阴影与一致性审查。
- **反例审查**：后台功能页的无效 Eyebrow、重复英文与巨型 Hero，以及其他网页形态的常见反面案例。
- **创意动效**：Anime.js 114 种组合配方、45 个缓动名称、16 个代码示例；React Bits、Vue Bits、Inspira UI、Magic UI、Aceternity UI 的创意组件选型。
- **成熟组件库**：Ant Design / Ant Design Vue、Element Plus、Naive UI、MUI、Mantine、PrimeVue 等的选型与统一接入。
- **工程边界**：区分 React/Vue 实现与生命周期；避免重复依赖、过度动画和未测试的交互。

## 核心文件

| 路径 | 作用 |
| --- | --- |
| `references/design-discovery-interview.md` | 网站用途与内容驱动的两阶段访谈 |
| `examples/design-discovery-dialogues.md` | 用户不懂风格时的具体问答示例 |
| `SKILL.md` | 全局指令、阅读路由和强制执行顺序 |
| `references/design-system.md` | 统一视觉规则和 Design Tokens |
| `references/component-first.md` | 共享组件优先规范 |
| `references/framework-vue-nuxt.md` | Vue / Nuxt 实现指导 |
| `references/framework-react-next.md` | React / Next 实现指导 |
| `references/creative-component-libraries.md` | React Bits、Vue Bits 等创意组件指南 |
| `references/enterprise-ui-library-guide.md` | Ant Design 等成熟组件库指南 |
| `references/animejs-motion-recipes.md` | 114 种动效的视觉说明、适用与避雷 |
| `references/animejs-easing-complete.md` | 45 个 Anime.js 内置缓动 |
| `references/quality-antipatterns-by-page-type.md` | 跨页面类型的正反例审查 |
| `examples/prompt-library-web.md` | Web Agent 提示词与使用方式 |
| `assets/creative-effects-gallery.html` | 12 组原创视觉效果演示 |
| `assets/motion-gallery.html` | 114 种动效和缓动的交互演示 |
| `assets/preview.html` | 主题色与密度预览 |
| `scripts/validate_web_skill.py` | 文档、框架和文件关系检查 |

## 保留的兼容性细节

为了避免破坏已使用旧版样式资源的网页，**CSS 的内部技术命名空间保留 `.spui` 和 `--spui-*`**，不作为 Skill 的公开名称。公开调用命令、目录、元数据、示例提示词与展示标题统一为 **MauForma / `mauforma`**。如未来要变更 CSS 变量命名，应单独提供迁移指南，而非在品牌更名时静默破坏代码。

## 验证

```bash
python3 scripts/validate_web_skill.py
python3 scripts/validate_design_system.py
python3 scripts/validate_motion_catalog.py
```

更多版本记录见 `CHANGELOG.md`。
