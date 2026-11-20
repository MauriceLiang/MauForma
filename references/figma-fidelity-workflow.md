# Figma Fidelity Mode — 将给定设计稿忠实实现为 Web UI

> 只在用户明确提供 Figma URL、设计节点/当前选中节点，或要求**精确实现已有设计稿**时触发。此模式与“参考某网站做相似气质”的创意迁移互斥；未经请求，不把 Figma 稿重新设计。

## 一、先判断输入可信度与工具可用性

| 输入和权限 | 可以做什么 | 不能宣称 |
| --- | --- | --- |
| Figma MCP / 兼容设计上下文工具可读取节点 | 取得节点结构、自动布局、变量、组件、真实文本、资产与截图，用于精确实现 | 不经过目标浏览器对照就说“1:1 已完成” |
| 仅有用户提供的设计截图 | 测量可见几何关系、文字层级、色彩、构图并尝试**视觉近似** | 截图能提供精确节点尺寸、Auto Layout、组件变体、字体名称或原始 HEX |
| 只有 URL，但无法访问设计文件 | 说明节点权限/连接受阻，请求可访问素材或允许的截图导出 | 猜测画板内容、伪造 Figma MCP 读取结果 |
| 用户只说“参考这种感觉” | 阅读 `references/design-reference-learning-gate.md`，提炼规律和不应复制的部分 | 把风格参考误当必须像素克隆 |

**工具要求**：优先使用用户明确提供、已连接且有权限的设计源。不同 Figma MCP 提供的 API 可能不同，绝不虚构工具名称、返回结构或“已读取设计稿”的成功状态。

## 二、七步还原流程

1. **锁定源**：确认 file / node / variant / viewport，用户选择的当前帧与版本；若多个页面，列清单并按路由匹配。
2. **设计上下文**：有 MCP 时读取节点树、Auto Layout、constraints、typography、Fill、Stroke、Effects、Variables、Variants 与资产 URL；拿到权威截图作为基准。超长上下文可按 frame/child 节点分段读取，不虚构遗漏内容。
3. **设计 Tokens**：记录值及来源（`source-figma / inherited-project / inferred-from-screenshot / unknown`），将颜色、字体、尺寸、间距、圆角、边框、阴影、断点映射到已有主题。不要为了微小误差复制一堆局部 hardcode；冲突时记录方案和实际差异。
4. **组件映射**：先查现有成熟组件库与共享 UI 组件，建立 `Figma component → project component` 映射。Select、Dropdown、Dialog、Button 仍按 `references/component-library-first-gate.md` 做真实交互；不因视觉还原而重造下拉的键盘/焦点逻辑。确需特别样式时用主题或受控变体。
5. **资产与实现**：只下载/引用授权可用的图片、图标、字体；保留真实文本与合法图片，不用占位图替代可用源。按项目既有框架和路由实施。Figma 里生成的示例 JSX/Tailwind 不是必须照搬的生产代码。
6. **双层验证**：`visual parity` 比较设计截图与真实页面（相同视口、像素比、字体/素材加载状态），先审结构、尺寸、对齐、字体，再核色彩、边缘、阴影；`interaction parity` 单独验证 focus/hover/selected/disabled、键盘、响应式和业务结果。设计未提供的状态，按现有系统与可访问规范补全并标明推导。
7. **差异账本**：列出 `difference → impact → cause → resolution / intentional deviation → evidence`，最后实际浏览器重拍截图、复验已修项。只有图片像素差异的小数点不代表功能好坏；动态素材/反锯齿等环境差异需区分。

## 三、冲突优先级与权限边界

- 用户明确指定“按稿还原”时，设计稿是该范围的**视觉主要基准**，不是 Agent 自行寻找“更漂亮”方案的机会。
- 对已有设计系统/组件库：优先保持代码稳定、业务语义与可访问交互；若与画稿冲突，**必须说明具体差异和对还原度的影响**，不能悄悄把视觉偏移说成“设计规范优化”。
- Figma 与 Web 渲染模型不同，百分比布局/字体抗锯齿/浏览器原生控件可能无法完全等价；不把不可能保证的“百分百像素级”当成无条件承诺。
- 任何 UI 特效如 Liquid Glass 都要以设计稿与用户确认的视觉需要为前提，不能在还原任务里额外增加毛玻璃/大渐变/粒子背景。
- 原图、商业字体、组件与其它资产不得未经授权发布到公共 Skill 仓库。只保留当前项目实际允许的资源。

## 四、验收输出（按项目规模裁剪）

```text
目标：页面/组件/指定节点及设计版本
证据：Figma 可读节点 / 截图 / 仅可见部分
设计约束：主视觉、布局、字号、颜色、资源与交互
组件映射：沿用主库 + 共享组件 + 必要例外
对照检查：同视口截图、版式、字体、颜色、状态、响应式
未实现/偏差：具体点位、原因、是否授权
验证等级：VERIFIED / STATIC CHECK / NOT TESTED / BLOCKED
```

这里的 `VERIFIED` 仅表示列出的**具体环境/页面与测试项目**确实复核，不代表所有设备/视觉与业务百分百一致。

开源 Skill 的出处与谢意集中在根目录 README；Figma 原生 MCP 操作仍须以当前官方文档与实际工具权限为准。

**适用时读取**：`references/design-reference-learning-gate.md`、`references/design-system.md`、`references/component-library-first-gate.md`、`references/browser-qa-protocol.md`。
