# MauForma v5.1

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
