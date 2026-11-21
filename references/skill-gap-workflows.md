# Executable Design Workflows — Load on Demand, Do Not Inflate Default Context

This guide provides entrypoints for tools operating on the **user-authorized target project**. Label every finding by real evidence. Updating the Skill repository alone cannot prove a user's application has better interactive behavior. Sources and acknowledgments live in the root README.

## Trigger and tool selection

| Task | Tool | Evidence level | Without environment |
| --- | --- | --- | --- |
| Analyze public site Design DNA | `scripts/extract_design_dna.mjs` | `OBSERVED`, not proof of design intent | `NOT_RUN`; do not invent colors |
| Detect project design-token drift | `scripts/check_design_drift.py` | `STATIC CHECK` | `NOT_BASELINED` |
| Differential check after modifying UI files | `scripts/mauforma_check.py` | `STATIC_RISKS` | `NOT_TESTED` |
| Inspect motion frame by frame | `scripts/motion_rehearsal.mjs` | `CAPTURED_FOR_REVIEW` | `BLOCKED` |
| Preview design variants | `scripts/preview_design_variants.py` | `PREVIEW_ONLY` | Does not replace source |
| Resume feature work across sessions | `scripts/feature_design_flow.py` | `IN_PROGRESS` | Read existing design files |
| Plan long-copy/errors/interaction resilience | `scripts/plan_ui_hardening.py` | `PLAN_ONLY` | Never claim a pass |

## P0-1 — Measure Design DNA rather than guessing

In an authorized development environment with installed Playwright/Chromium:

```bash
node scripts/extract_design_dna.mjs --url https://example.com --out ./artifacts/design-dna
# Add --allow-local only for synthetic local test scenarios
```

Save `report.json`, `report.md`, `page-01.png` to local artifacts. The structured observation only includes computed styles from visible DOM (not page copy or credentials), but screenshots may still contain private data: **never automatically commit them to the public MauForma repo**. Check final URL, font readiness and evidence count. Convert observations into project Tokens only after real inspection and user confirmation. If a third-party site requires authentication or enforces anti-automation, report `BLOCKED`; **do not circumvent access controls**. Restrict internal requests by public network-safety rules; a formal security audit requires stronger network isolation.

## Boundary — External references and script installation permissions

When a style search returns empty/low-relevance/out-of-domain results, refine a small number of terms based on actual content and page intent. Check applicability of returned cases. With no grounded result say `NO_GROUNDED_MATCH`, not that an arbitrary high-scoring style is approved MASTER. For site references distinguish observed WHAT, inferred WHY and unknown intent. Claim “latest” external specification only if browsing was authorized and completed.

Distinguish **per-project authorization** from **global user environment changes** for Agent hooks, CLI helpers and installing Playwright browsers. Never silently install global tools. Complete bilingual trigger/exception/prohibition guidance is paired in `references/semantic-boundaries.en.md` and `references/semantic-boundaries.zh-CN.md`; read only relevant boundaries.

## P0-2 — Design Drift Doctor

```bash
python3 scripts/check_design_drift.py --root ./target-project --format json
# Save an observed baseline only after reviewing it within the target project; this is not an approved theme
python3 scripts/check_design_drift.py --root ./target-project --write-baseline
python3 scripts/check_design_drift.py --root ./target-project --strict --format json
```

`design-system/observed-tokens.json` is for comparing subsequent changes. **It reflects source observations, not MASTER truth.** Distinguish tool-version, schema-format and product design-truth drift; the script cannot autonomously repair the latter. It never updates `MASTER.md`, approved choices or product CSS. Added/deleted/changed CSS variables and literal colors create locatable clues; human review must distinguish legitimate theme overrides and framework variables from actual errors.

## P0-3 — Motion QA 2.0

```bash
node scripts/motion_rehearsal.mjs --url http://localhost:3000 \
  --scenario assets/motion-rehearsal-scenario.example.json --out ./artifacts/motion --video
```

Start rAF and pointerdown/pointerup sampling **before clicking**; collect screenshots and emit possible `possible-position-jump`, `possible-anchor-drift` and `screenshot-sampling-gap` candidates. Use each step's `contact-sheet.html` for quick review; `--video` supplies optional normal-speed playback evidence. Screenshot and sample clocks differ, and system scheduling affects results.

If the business interaction allows instantaneous alignment, set `allowSnap: true` on that scenario step. Specify stable anchor's selector as `anchor` and enable anchor checks for low-tolerance drift. **Candidate ≠ confirmed defect**: compare videos, real frames and source together. Automated PASS ≠ independent aesthetic review.

## P1 — Incremental checks with scoped waivers

```bash
python3 scripts/mauforma_check.py --root ./target-project --changed src/App.vue \
  --format json --strict
```

Default to supported UI source files; no global hooks installed. An exception JSON inside the **target project** must identify specific `rule_id`, `file`, `reason` (at least 12 characters) and `expires` (ISO date). The result specifies file/line/rule/risk and untested-browser status. An expired waiver or one without substantive reason fails. Verify actual design in a browser separately.

## P1 — Design variants and resumable feature work

```bash
python3 scripts/preview_design_variants.py \
  --input assets/design-variant-options.example.json --output ./artifacts/options.html
# Only record selection when user has chosen; source remains unchanged
python3 scripts/preview_design_variants.py --input assets/design-variant-options.example.json \
  --output ./artifacts/options.html --choose calm --decision ./target-project/design-system/features/header/selected-variant.json
python3 scripts/feature_design_flow.py --project-root ./target-project --feature header --action init
python3 scripts/feature_design_flow.py --project-root ./target-project --feature header --action init --apply
python3 scripts/feature_design_flow.py --project-root ./target-project --feature header --action status
python3 scripts/feature_design_flow.py --project-root ./target-project --feature header --action complete \
  --task F01 --evidence "Inherited design tokens reviewed and agreed"
```

Inside project use `design-system/features/<slug>/`; keep only feature deltas/progress and reuse MASTER. Do not overwrite existing files; unstarted stages remain `NOT_TESTED`. Variants are isolated synthetic previews, not live business redesign. When a variant is approved and applied, reproduce and verify it in the actual target application.

## P1 — Resilience and framework boundaries

```bash
python3 scripts/plan_ui_hardening.py --out ./artifacts/hardening.json
# Only enable RTL, offline or mobile if the target product needs them
python3 scripts/plan_ui_hardening.py --include rtl --include offline --include mobile
```

Always evaluate long copy, empty state, failure, slow network, rapid repeated clicks, keyboard and reduced motion. RTL, offline, mobile and huge-data scenarios apply only when the product requires them. `VERIFIED` requires matching real API/E2E/visual checks.

Vue/React performance and state specifics are in `references/framework-vue-nuxt.md` and `references/framework-react-next.md`. Static tooling and fake pages cannot replace real-product tests.

## Completion gate

Report tool version, target route/URL, affected files, actual results, untested scope, independently rechecked evidence and whether user-approved themes changed. Repair a failed check or disclose the blocker **before** declaring completion. Never change brand decisions or remove real business data solely to make checks green.
