# Motion Rehearsal & Evidence · 动效逐帧质量门禁

> 将录制 → 检查 → 修复 → 重新录制的闭环用于**真实产品**。静态审计、截图数量或自动指标不能替代人类视觉判断。与 `motion-craft-and-continuity.md`、`browser-qa-protocol.md` 和 `visual-qa.md` 联合使用。

## 演示分镜与真实产品验证的差别（B05/B10）

上游展示类动画可采用“poster-first”（静态封面就应表达关键价值）、有限叙事节拍、循环接缝与演示镜头；**这些只在用户任务涉及产品宣传、动态插画或作品展示时有价值**。真正的业务按钮、状态变更、持久化、权限与错误恢复必须另行按真实页面和后端验证，不能把可视化镜头里的假光标或演示状态当成端到端业务结果。即使浏览器截帧没有异常，也仅输出 `CAPTURED_FOR_REVIEW`，不能据此声称审美和流畅度已通过。

## Gate MR0 · 先确定测试对象，区分演示和真实页面

- 只测试用户目标产品**实际存在**的主要交互和本次修改范围；不为满足用例凭空加按钮。
- 在运行前记录 `url / route / data fixture / viewport / device scale / theme / locale / reduced-motion / interaction`。能使用稳定测试数据时用明确标记的 fixture，不能把模拟后端交互冒充真实保存。
- 对当前改动的高价值交互，写出 `before → trigger → during → settled → reverse/interrupted → reduced` 检查清单；这不是要求每个小 hover 都录 20 帧。

## Gate MR1 · 分层验证，而不是一次截图

1. **静态首帧**：在目标交付尺寸看首帧和结果帧。内容层级、控件大小、中文换行、对齐、focus、图标、卡片边界不合格时先修布局。
2. **按节拍采样**：对关键转场采样 start / 25% / 50% / 75% / end，并在短促的出入场、跳变怀疑处增加 40–80ms 采样。采样周期与截图开销必须记录；无法满足预期频率属于 `INCONCLUSIVE`，不是 `PASS`。
3. **真实速度重播**：单看 contact sheet 检不出短暂闪烁、卡顿和不自然 easing；实际看 1x 动画，再慢速看可疑转场。
4. **中断与逆向**：动画约进行到 30% 与 70% 时再点、反向、按 Escape、切路由；检查是否从当前视觉位置连贯衔接，焦点/业务状态没有丢。
5. **动态范围**：按需求覆盖指定桌面宽度、窄窗口/移动端（如项目支持）、深浅主题、200% 字体、长中文/英文、首次加载与稳态。只做桌面项目不强制手机正式适配，但需测最低支持视口。
6. **系统偏好**：在开始时与进行中切换 `prefers-reduced-motion`；业务结果一致，表达方式减少运动；检查可访问名称、聚焦与状态反馈。
7. **循环/长时间**：仅对自循环营销演示检查至少一次完整循环加下一轮起点、重置因果、页签隐藏/恢复；普通后台控件不应为了测试而引入循环。
8. **项目运行**：用真实页面、相同版本的 CSS/JS、实际控件选择器录制。若演示页和实际项目 UI 不一致，不允许互相替代验收。
9. **独立复审**：对高表现力或重要的动态交互，优先让不参与实现的审阅者只根据任务、原有设计约束与真实帧图/录像重新观察，不提供实现者自评结论；每项问题须对应证据帧与操作步骤。无法独立复审须明确标记。

## Gate MR2 · 异常特征与修复动作

| 看到的异常 | 首先检查 | 修复方向 |
| --- | --- | --- |
| 突现/突消 | mount/unmount、display、关键帧开头 | 入/退场与保留节点；必要时即时反馈有依据 |
| 跳位/邻居瞬移 | layout/reflow、key identity、测量时序 | 共享位置过渡、FLIP、占位与邻居同步 |
| 文字最后一帧抖动 | 字体加载、宽度归零、transform layer 清理 | 固定布局约束、只变更必要子段、检查像素 |
| 容器先开空白再装内容 | 数据与动画时间线 | 可读内容随容器进入，loading 必须真实 |
| Popover 一边打开一边漂移 | 锚点、定位更新、内容高度 | 稳定 anchor、位置重算与适当方向 |
| 点击后才慢慢反馈 | delay、动画队列、网络依赖 | pressed/focus 即时、结果晚于触发 |
| 快速反向出现卡顿 | stale target、过时 timer、重复动画 | 取消/retarget、清理旧任务、当前几何续接 |
| 模糊或糊字 | 放大正文、滤镜、大范围 transform | 改为容器/layout transition、保留清晰文本 |
| 不必要重复飞入 | rerender/数据刷新触发 re-entry | 区分首次进入与数据更新、限制动画 |
| 缩减动态时不可用 | 非动效路径缺失或 CSS 只靠动画显隐 | 同步最终 DOM/ARIA 状态、无动效仍完整 |

对每个异常按 `evidence → hypothesis → fix → recapture` 记录；动画问题修复后必须**从真实操作重新拍完整过程**，不能只留修复前帧。

## Gate MR3 · 可执行采样方案（框架无关）

推荐 `scripts/motion_rehearsal.mjs`：传入本地运行的 URL、`scenario` JSON 和明确的视口。它在**触发操作前**开始页面内 rAF 与 pointer 事件采样，和操作并行采集前/中/后截图；输出几何跳变候选、采样间隔、局部 Contact Sheet，必要时使用 `--video` 录制正常速度播放材料。脚本不修改网页、不自动安装浏览器/依赖，也不判定审美合格。

```bash
node scripts/motion_rehearsal.mjs \
  --url http://localhost:3000 \
  --scenario assets/motion-rehearsal-scenario.example.json \
  --out ./artifacts/motion-review
```

示例中的 `data-motion-demo` 选择器仅说明输入格式；**在真实项目使用前必须替换为实际控件选择器**。测试前确保开发服务器与 Playwright 浏览器已安装。报告出现 `INCONCLUSIVE`、`NOT_RUN` 或错误时不能报 `VERIFIED`。`CAPTURED_FOR_REVIEW` 表示证据采集完成，**不是动画已通过质量门禁**。`anchor` 与 `anchorTolerancePx` 可声明固定参照；`allowSnap` 只用于明确合法的快速状态切换。

仓库自带 [原创 Motion Continuity Lab](../assets/motion-continuity-lab.html) 与配套 [可运行场景](../assets/motion-continuity-lab.scenario.json)，可供学习脚本的真实点击/展开/状态采样：

```bash
python3 -m http.server 8000
node scripts/motion_rehearsal.mjs \
  --url http://127.0.0.1:8000/assets/motion-continuity-lab.html \
  --scenario assets/motion-continuity-lab.scenario.json \
  --out ./artifacts/motion-lab
```

演示页面完全合成且不含后端请求；其演示结果只能标 `DEMO ONLY`。复制场景到业务项目时，必须改成该项目的真实控件 selector、实际路由和目标视口。

推荐文件与步骤（每个场景独立保存）：`scenario.json`、`before.png`、`frame-*.png`、`settled.png`、`contact-sheet.html`、包含 rAF 时间序列与候选问题的 `report.json`。自动工具只捕捉证据与潜在运行问题；定性判断必须回看图像与真人播放。

## Gate MR4 · 结果分级与交付

- **VERIFIED**：真实目标页面运行，浏览器及视口明确，关键帧和完整播放由实际观察确认；已检查至少一种中断/反向、减少动效与最小支持尺寸。独立复审另行记录，不能从此状态推断已通过独立美学评审。
- **PARTIAL / INCONCLUSIVE**：帧缺失、采样间隔过大、流程无法稳定重现、目标不可见或部分组合未覆盖；列出确切未覆盖维度，不能说 PASS。
- **DEMO ONLY**：合成动效实验运行，目标产品尚未复验。
- **STATIC CHECK**：只检查代码或设计契约，无运行时动态证据。
- **BLOCKED / NOT TESTED**：没有浏览器、服务器、可操作环境或未实际运行。

交付摘要至少包含：

```md
### Motion Rehearsal
- Scope: <真实交互及路由>
- Decision: <用户确认的强度与来源；或已有继承策略>
- Story: <触发、位置关系、收尾、反向、低动效>
- Captured: <URL、浏览器、viewport、主题、步骤、文件>
- Findings → fixes → recapture: <实际证据>
- Reduced motion / interruption / focus: <结果>
- Independent review: <审阅者、证据及问题；或 NOT REVIEWED>
- Status: VERIFIED | PARTIAL | DEMO ONLY | STATIC CHECK | NOT TESTED | BLOCKED
- Unverified: <未测环境和原因>
```

**不能用自动“没有发现异常”代替美学合格，也不能用随机截图证明动画丝滑。** 推荐在真实设备观察帧率/长任务、页面重排、GPU/内存开销；未测的指标不得宣称达标。

本工具与报告面向真实产品和多框架；不将产品演示场景的模拟动作当成真实业务验证。开源参考与致谢见 README。
