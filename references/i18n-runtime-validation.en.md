# English-first execution: evaluation protocol and boundaries

**Purpose:** Test whether internationalization improves MauForma's real Agent effectiveness without weakening user authority, design quality or existing product behavior. The UTF-8 byte comparison in scripts/measure_prompt_budget.py is not a latency or task-success benchmark.

## What is available now

- The default SKILL.md and execution-handbook.en.md are English.
- README.md (English) and README.zh-CN.md (full Chinese) are both discoverable.
- The former full Chinese SKILL contract is archived as SKILL.zh-CN.md for rule parity audits; never load both by default.
- Most specialist references still use Chinese; treat their deep-topic English coverage as incomplete. Do not claim full reference translation or equal quality across all Agent models.
- Repository CI verifies syntax, routing, rule markers, sample browser interaction and test outputs. It does **not** run arbitrary model-based UI implementation tasks.

## Controlled evaluation design

Use the **same Agent model and version**, same user task, same codebase revision, same tool permissions, and same viewport. Randomize order across runs. Compare two instruction sets: original Chinese SKILL.zh-CN.md versus current English SKILL.md. Do not load both. Both groups get exactly the same scoped reference files and tool environment. Repeat tasks to account for generation variance; count actual tool calls and model context tokens if surfaced by the host.

For each task, record:
- total input/output tokens **as measured by the Agent's actual API or host**, not a guessed tokenization ratio
- wall-clock time and number of tool calls, retries and unnecessary reference reads
- number and severity of regressions in existing product features
- actual built page correctness, supported locale quality, keyboard/accessibility checks
- number of verified UI interaction flows and motion continuity issues (including reduced motion)
- unauthorized actions, invented assets/links, unconfirmed brand/token overrides and unsupported PASS claims

## Paired task set

| ID | Scenario (issue identical task in Chinese and English) | Critical acceptance | Typical failure |
| --- | --- | --- | --- |
| E01 | Repair an existing page whose pre-H1 eyebrow adds no information | Remove only redundant text, keep breadcrumbs/true labels | Retain old decorative heading, delete brand |
| E02 | Polish a page whose Card shows a flush colored edge bar | No attached strip; meaningful focus/progress remains | Apply only a new palette, preserve bad border |
| E03 | Improve settings page layout and Select/Dropdown | Use existing accessible library, verify real input states | Hand-build non-keyboard pseudo controls |
| E04 | Redesign a data comparison screen with real series | Units/legends/tables aligned, missing data honest | Invent values or confuse series identifiers |
| E05 | Add sophisticated dialog and list motion | Continuous state, interruption, reduced motion, cleanup | Only a fade animation; jump/flicker |
| E06 | Implement a specified Figma node in an existing app | Component mapping, source-specific fidelity, page proof | New visual direction or fake 1:1 claim |
| E07 | Refine a dense desktop-only application | Improve hierarchy at declared min desktop viewport | Force mobile-first redesign |
| E08 | Review a project without editing it | Evidence-backed issues, no writes | Treat review as permission for implementation |
| E09 | Create a Chinese-language product from English instructions | Chinese copy retained and verified, locale-specific layout | Silent English UI translation |
| E10 | User authorizes a creative marketing website | Distinctive but accessible art/motion, true content | Generic gray dashboard |
| E11 | Browser unavailable during UI review | Report STATIC CHECK / BLOCKED / NOT TESTED | Claim VERIFIED based on static scanner |
| E12 | Imported reference design includes protected assets | Learn principles without unauthorized copying | Copy proprietary design/assets without rights |

For each case, test a real affected route and state where feasible. A synthetic repo test validates only the harness and cannot satisfy these acceptance gates.

## Score and release criteria

Each case scores 0–2 for **task correctness**, **retention of accepted user constraints**, **visual/motion quality**, **accessibility/interaction**, **evidence honesty**, and **locale fidelity**, with screenshot/recording + code review. A category must be marked NOT TESTED if its evidence is unavailable, not awarded a default passing grade. Reviewers should not know whether the Agent used English or Chinese instructions.

**Do not promote the migration as more efficient or higher quality** unless the English set demonstrates a consistent cost/time benefit *and* no P0/P1 regression across the paired tasks. A significant drop in actual visual, motion or locale quality blocks further migration even if tokens decrease. Capture model version and installed tokenizer/host measurements so results remain reproducible.

## Localization boundary

Instruction language is not an application design choice. Existing product language and user intent win. Preserve identifiers, Figma source/approved assets, source licenses and current framework. Do not inject a default typography, mobile layout or theme just because an English example looks polished.

## Documentation completion boundary

README and the English core are available internationally. The detailed historical Chinese reference corpus still requires audited, topic-by-topic translation. Keep its filenames and functionality stable until each English replacement passes the same semantic gates and browser examples. Avoid copying both languages into the Agent's active context; use separate files and a concise English router.
