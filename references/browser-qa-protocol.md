# Browser QA — Joint Acceptance of Visual Design and Real Interactions

This protocol requires real-browser evidence rather than treating static checks as browser execution. Prefer the target project's existing Playwright/test tooling; if absent, state the limitation before installing anything. Never silently install a browser or remote driver.

## v6.20 — Active browser diagnosis for ambiguous UI polish

For “improve this page,” **start with a baseline-free inspection of the actual page**. Neither a passing before-state spacing baseline nor a built-in Mock is sufficient. Follow `references/proactive-visual-defect-discovery-gate.md`: inspect beginning/middle/end, meaningful states and supported wide/narrow layouts across spacing, hierarchy, control density, icon/color and interaction/responsiveness. Where useful, `node scripts/audit_existing_visual_defects.mjs --url <current-page>` finds pre-existing touching framed panels in Block/Grid/Flex and simple wrapper structures. Compare before/after geometry afterward to protect good regions. Tool coverage is incomplete: never claim browser PASS without opening the actual page. Do not upload private screenshots or user data to public CI.

## Universal title-prefix classification, independent of styling

For creation, authorized visual polish and design review, use `references/title-prefix-role-gate.md` to inspect real heading groups. `node scripts/audit_title_prefixes.mjs --url http://localhost:3000 --selector main` emits `CANDIDATES_FOR_REVIEW` from common H1–H6 and `role=heading` structures. `NO_CANDIDATES_OBSERVED` **does not prove the page has no eyebrows**. The Agent must determine the meaning and correct position of each candidate. Preserve real breadcrumbs, statuses, steps and approved brand stories. Pseudo-elements, Canvas, image-embedded labels and non-semantic visual headings need visual review. **Color, font size and family never define a candidate.** Inspect inherited and new content; recheck the actual page after changes.

## Component provenance and open-state consistency — new and existing UI

Use `references/component-consistency-and-selection-gate.md` to map real imports, theme/tokens, native/headless implementations, shared adapters and **closed plus open states** of same-purpose controls. `node scripts/audit_control_consistency.mjs --url http://localhost:3000 --selector main` may flag native Select and ARIA selection controls coexisting, but cannot identify vendor implementations or all OS-level option popups. Native select menus drawn by the browser/OS need inspection on the actual target platform; if not observed, report `NOT TESTED`. Verify keyboard, selection, errors, focus, dark/light, long labels and viewport boundaries. Styling the trigger is not proof the option popup is consistent.

## Inspect the browser before inventing selectors (B14)

Reuse or start an authorized project server, documenting which process is under test and which processes may be shut down. **Read the current rendered DOM, accessible names, controls and visible states before selecting Playwright locators**; never guess a selector or a live button from a prompt. Record console exceptions and relevant network/server failures. `networkidle` alone is not a sufficient readiness condition for SPAs or streaming apps; combine actual visible semantic readiness with the relevant loading state. Close only resources started for this test; never kill the user's pre-existing service.

## Dynamic Motion Rehearsal

For newly introduced or changed *important* interactions, a CSS transition declaration or final screenshot does not establish quality. Follow `references/motion-craft-and-continuity.md` and `references/motion-rehearsal-and-evidence.md`. Capture before/during/after, real-speed playback, reverse/interruption, the smallest supported viewport and reduced-motion behavior. When appropriate, run `scripts/motion_rehearsal.mjs` to begin rAF/pointer sampling **before** the interaction, then capture frames, geometry and possible positional jumps using selectors read from the real DOM. `CAPTURED_FOR_REVIEW` means evidence was collected, **not** aesthetically or functionally verified. Developer tools do not need promotional fake-mouse animations; a marketing demo cannot stand in for backend E2E.

## Required acceptance matrix — only within the product's actual scope

- **Viewport:** Follow declared support. A desktop app might require 1440px and its minimum desktop width; a mobile-only site may use 390px. Never force phone layouts on desktop-only products. At every supported viewport, check horizontal overflow, visual cropping, line breaks and reflow.
- **Accessibility:** Tab/Shift+Tab, Esc closing, form labels, error focus, focus-visible, semantic controls, contrast and meaningful accessibility state. Never remove focus outlines without an alternative or block normal paste.
- **Themes/settings:** Test supported light/dark, system zoom/text scaling, `prefers-reduced-motion` and lower-end fallback. Only test RTL when the target product supports it. Dates, money and numeric values in multilingual apps need locale-aware formatting; do not guess locale from IP.
- **Real actions:** Input/save/failure/retry/empty/permission/loading. Destructive actions need confirmation or undo; failures must identify and recover the affected operation. A static Mock cannot prove a real server save.
- **Visual comparison:** Compare project MASTER and page overrides, approved plan, component showcase and real screenshots. Check focus, first-screen CTA, whitespace, density and state feedback.
- **Engineering evidence:** Actual build, type checking, unit tests and applicable E2E; inspect browser console and request/server errors.

### Freshness of external frontend standards

Official Web UI guidance changes. Claim “verified against latest guidance” only after authorized research into current rules, with source and date. Otherwise follow the project's pinned versions and known rules, stating limitations. A static `file:line` hint is not WCAG certification. See `references/semantic-boundaries.zh-CN.md` / `references/semantic-boundaries.en.md` for B09/B10/B14/B15 (read only the relevant boundary).

## Review report fields

`page | viewport | light/dark | flow | expected | observed | screenshot-path | code-location | severity | fix | re-tested`.

Status labels: `PASS` (actually executed), `FAIL` (reproduced) and `NOT RUN` (conditions unmet). A planned test is never a pass.

## Severity

- **P0:** Unusable form, inaccessible action, fake data or occluded essential content.
- **P1:** Severe overflow/contrast failure, modal cannot be closed.
- **P2:** Typographic inconsistency, decorative clutter, mild motion defects.

## Tools and boundaries

- Prefer the project's existing Playwright or browser automation. If absent, install only within granted permissions; do not change the business runtime then claim no changes were made.
- Static scanner `python3 scripts/audit_frontend.py path/to/src` emits heuristic hints only. `python3 scripts/mauforma_check.py --root path/to/project --changed src/App.vue --format json` adds scoped findings and expiring waivers; browser coverage still reports `NOT_TESTED` until executed.
- Executable baseline: `python3 -m unittest discover -s tests` plus applicable `scripts/validate_*.py`.

## Invalid evidence

A screenshot does not prove server behavior. One desktop shot does not prove mobile support. Finding a `prefers-reduced-motion` literal does not prove site-wide reduced-motion compliance.

## v6.9 — Final content reachability and shared-grid regression

For lengthy data/release timelines/multi-chart grids, inspect **initial viewport and scroll-to-end**. A first-screen screenshot cannot prove the last item is reachable. `node scripts/audit_rendered_layout.mjs --url http://127.0.0.1:5173/releases --out layout-audit` produces initial/final viewport captures and a report, using the project's installed Playwright or an authorized install. When not run, report `NOT RUN`.

Find the real scroll owner (document vs inner `main-scroll`), verify the last interactive/content item, fixed BottomBar overlap, safe-area/final padding and accidental horizontal scrolling. Inspect shared data cards' top alignment. For third-party components without semantic annotations, use optional `data-mf-bottom-content`, `data-mf-grid-row`, `data-mf-grid-panel`, `data-mf-fixed-bar`. A screenshot near the lower edge is not sufficient evidence of clipping; only a genuinely unreachable endpoint is a major defect.

## v6.10 — Comparison page browser QA beyond cards

Using the user's actually selected objects and sample data, run: select repository → inspect selected IDs, legend, series and table columns → change time window → test missing/partial data → smallest supported mobile layout where applicable → scroll to final row. Optional `data-mf-selected-id`, `data-mf-legend-id`, `data-mf-series-id`, `data-mf-chart-group`, `data-mf-chart-plot`, `data-mf-chart-label` annotations make geometry checks possible in `scripts/audit_comparison_ui.mjs`. Canvas axes/labels are rarely in normal DOM; inspect real chart renders or official engine APIs. Without access, report `NOT AUDITED`. Equal outer Card heights do **not** establish equal plot area/axis alignment or absence of overlapping labels.

## v6.11 — Run-monitor list and details browser QA

Verify that filtered statuses and counts match visible tasks, progress uses genuine numerator/denominator, recovery buttons appear only in legal states, detail navigation shows actual stages/logs, and search/sort preserve context. Check appropriate 1440×900 and 390×844 layouts only when supported, including long IDs, touch/keyboard and final scroll. `tests/task_center_browser_smoke.mjs` uses local Mock data in two viewport screenshots; a real system also needs integration with its real API, permissions, failures, double submissions, background state changes and retries. A local-memory button update does **not** prove actual backend retry. See `references/task-center-run-monitor-design.md`.
