# 可执行设计工作流 · 按需加载，不增加常驻 Token

本指南提供针对**用户明确授权的目标项目**的工具入口。所有检查都按真实证据标记状态；只修改 Skill 仓库本身不能证明具体产品已经获得更好的交互体验。来源与致谢统一见根目录 README。

## 触发与选择

| 任务 | 工具 | 证据等级 | 无环境时 |
| --- | --- | --- | --- |
| 分析公开网站的设计 DNA | `scripts/extract_design_dna.mjs` | `OBSERVED`，不是设计意图证据 | `NOT_RUN`，不猜颜色 |
| 检查目标设计 Tokens 漂移 | `scripts/check_design_drift.py` | `STATIC CHECK` | `NOT_BASELINED` |
| 修改 UI 文件后的差量检测 | `scripts/mauforma_check.py` | `STATIC_RISKS` | `NOT_TESTED` |
| 逐帧审视动态交互 | `scripts/motion_rehearsal.mjs` | `CAPTURED_FOR_REVIEW` | `BLOCKED` |
| 设计几个安全候选方案 | `scripts/preview_design_variants.py` | `PREVIEW_ONLY` | 不替换源码 |
| 多次会话持续推进某功能 | `scripts/feature_design_flow.py` | `IN_PROGRESS` | 读取现有设计文件 |
| 长文本、错误与交互的边界清单 | `scripts/plan_ui_hardening.py` | `PLAN_ONLY` | 不宣称通过 |

## P0-1：Design DNA 实测而非猜测

在已获得许可、且有现成 Playwright+Chromium 的开发环境：

```bash
node scripts/extract_design_dna.mjs --url https://example.com --out ./artifacts/design-dna
# 对本机合成测试场景才显式加 --allow-local
```

保存 `report.json`、`report.md`、`page-01.png` 至本地 artifacts。仅输出真实可见 DOM 的计算样式，不采集网页文字或登录信息，截图可能包含个人信息，**不得自动提交到公开 MauForma 仓库**。检查最终 URL、字体状态和证据数量；只在有实际观察和用户确认后，将设计方向转为项目 Token。若第三方页面设置复杂反爬/身份认证，请说明 `BLOCKED`；不得绕过访问控制。网站内部请求按公开网络规则限制，正式安全审计仍需更严格的网络隔离。

## 特殊边界：外部来源与脚本权限

当候选风格搜索返回空结果、低相关结果或不符合用户领域时，先用用户真实内容/页面目的调整少量检索词，再检查返回条目的适用场景；无可靠结果就明确 `NO_GROUNDED_MATCH`，不得把任意高分样式写为用户确认的 MASTER。参考站点分析必须符合页面访问授权，并保留观测 WHAT / 推断 WHY / 未知信息的区分。外部动态规范仅在实际获准联网、检索成功后才可宣称“最新”。

任何现成的 Agent Hook、命令行辅助工具或新的 Playwright 浏览器安装都应区分**项目级授权**与**全局用户环境修改**，默认不自动安装后者。完整触发、例外、禁止中英对照见 `references/semantic-boundaries.zh-CN.md`。

## P0-2：Design Drift Doctor

```bash
python3 scripts/check_design_drift.py --root ./target-project --format json
# 在目标项目内部人工确认后，显式保存「观测基线」；不是用户批准的主题
python3 scripts/check_design_drift.py --root ./target-project --write-baseline
python3 scripts/check_design_drift.py --root ./target-project --strict --format json
```

项目内 `design-system/observed-tokens.json` 仅用于后续差异比对。**它是源码观测，不是 MASTER 真值**。版本漂移、格式漂移、设计事实漂移须分开处理；后者没有仅凭此脚本自动修复的能力。脚本不会更新 `MASTER.md`、用户决定或实际 CSS。对 CSS variables 的新增、删改以及硬编码颜色提供可定位线索；CSS 中的合法主题覆盖和框架内变量应由人审核，不能把静态启发式当作证据确凿的错误。

## P0-3：Motion QA 2.0

```bash
node scripts/motion_rehearsal.mjs --url http://localhost:3000 \
  --scenario assets/motion-rehearsal-scenario.example.json --out ./artifacts/motion --video
```

在点击之前启动 rAF 与 pointerdown/pointerup 采样，同时采集截图，输出候选 `possible-position-jump`、`possible-anchor-drift`、`screenshot-sampling-gap`。每个动作的 `contact-sheet.html` 用于快速复查，`--video` 为可选正常速度回放证据；样本与截图时钟不同，系统调度也会影响结果。

若业务上允许瞬时对齐，在场景步设置 `allowSnap: true`；将固定锚点的 selector 填为 `anchor`，在容许浮动很小的场景启用锚点检查。**候选 ≠ 缺陷证实**，需要把视频、真实帧和代码一起核对；自动测试通过 ≠ 独立美学评审通过。

## P1：增量检查与合理豁免

```bash
python3 scripts/mauforma_check.py --root ./target-project --changed src/App.vue \
  --format json --strict
```

默认检查受支持的 UI 文件，不对全局安装 hooks。若需要豁免，目标项目的 JSON 文件用独立的 `rule_id`、`file`、`reason`（不少于 12 字符）与 `expires`（ISO 日期）限定；脚本返回具体文件、行号、规则、风险以及浏览器未测试事实。无具体理由或过期的豁免视为失败。设计效果仍需浏览器逐页验证。

## P1：变体与可恢复的功能工作流

```bash
python3 scripts/preview_design_variants.py \
  --input assets/design-variant-options.example.json --output ./artifacts/options.html
# 只有用户选定候选后才写选择记录；仍不更改目标产品源码
python3 scripts/preview_design_variants.py --input assets/design-variant-options.example.json \
  --output ./artifacts/options.html --choose calm --decision ./target-project/design-system/features/header/selected-variant.json
python3 scripts/feature_design_flow.py --project-root ./target-project --feature header --action init
python3 scripts/feature_design_flow.py --project-root ./target-project --feature header --action init --apply
python3 scripts/feature_design_flow.py --project-root ./target-project --feature header --action status
python3 scripts/feature_design_flow.py --project-root ./target-project --feature header --action complete \
  --task F01 --evidence "Inherited design tokens reviewed and agreed"
```

在项目内使用 `design-system/features/<slug>/`；只存该功能差异和任务进度，复用 MASTER。已有文件不覆写；未开始的阶段保留 `NOT_TESTED`。预览变体是独立合成示例而非真实业务改版；真实方案采用后必须在目标项目复现并检查。

## P1：健壮性与框架边界

```bash
python3 scripts/plan_ui_hardening.py --out ./artifacts/hardening.json
# 项目需要 RTL、离线或多端时再选择开启
python3 scripts/plan_ui_hardening.py --include rtl --include offline --include mobile
```

始终评估长文本、空状态、失败、慢网络、连续点击、键盘、减少动效；仅在产品需要时增加 RTL、离线、移动端和大数据场景。与实际 API、E2E 和视觉检查结合后才能改为 `VERIFIED`。

Vue/React 的框架专项性能与状态设计要求见 `references/framework-vue-nuxt.md`、`references/framework-react-next.md`。不要让静态工具或模拟页面替代真实产品测试。

## 退出门禁

每项交付须指出：工具版本、目标路由或 URL、作用的文件、真实结果、未检查范围、经人复验的证据，以及是否改变了用户已确认的主题。任何检查失败应修复或说明阻塞后再宣布完成；绝不为了获得“绿色报告”修改品牌决定或删除正常业务内容。
