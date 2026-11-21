# Settings & Form Layout Gate — Choose Layout by Save Semantics (v6.22)

> This gate belongs to the **page-task layer of Product Experience Routing**, not a separate replacement for product type or Operate/Persuade/Read/Experience. Settings exist in learning, consumer, admin and creative tools. A page named “Settings” **does not imply every field must use a horizontal row layout**.

## SF0 — Identify save and interaction units before R1/R2

Inspect each region: Does each setting **take effect independently** or do fields **submit as one transaction**? Short option vs long free text? Validation/error states? Irreversible actions? Available control width at narrow viewports?

| Pattern | How to recognize | Recommended structure | Failure |
| --- | --- | --- | --- |
| Settings / independent | Notification toggle, theme, language: one item changes without cross-field validation | Section heading + one setting per row; desktop label/help on left and compact control on right | All toggles in nested giant Cards or misaligned controls |
| Form / submit group | Registration, checkout, creation or editing: several fields entered and committed together | Label above Field, appropriate bounded content column, field width matching content | Label in left column and tiny Input too narrow for value/errors |
| Hybrid | Settings contain SMTP config, token handling, complex address or password form | Individual rows remain rows; multi-field subforms use **stacked form** | Forcing entire page horizontal because its title says “Settings” |
| Compact exception | Side-by-side control/translated help would be cramped | Stack that item or reflow on narrow screens | Preserving two columns by crushing field/error text |

First establish each region's true persistence semantics. For a narrow fix to an approved control, preserve inherited IA and tokens; do not restructure the full Settings page without authorization.

## SF1 — Independent setting rows

- One identifiable setting normally occupies one row: left content has **visible label** and optional help; right side has Switch, Select, compact Button, status or navigation entry. Text, control and state share stable alignment.
- Independently persisted settings need immediate or explicit feedback (pending, success, failure/recovery). If a Save action is required, **do not pretend the value auto-saves**. Async failure cannot merely leave a toggle visually enabled.
- Group related settings. Items within a group are close/scannable, while group boundaries are **noticeably larger** than row gaps. Each row label/control should feel closer than adjacent groups.
- Use subtle dividers, space and typography as needed. Audit whether giant outer Cards or nested surfaces add real task boundaries; prefer open sections if not. **Single bounded panels remain valid** for permission boundaries, pinned settings or complex configurations.
- Destructive actions (delete account, permanently clear data, reset all configuration) require separate grouping, explicit consequences and appropriate confirmation, permission checks or second verification; never mingle with ordinary notification toggles.
- Reflow on narrow screens: text above, control below/right-below, with legible tap targets. Do not rely on severe flex shrinking, hidden full labels or clipped overflow to keep two columns.

## SF2 — Multi-field submitted forms

- Default to **label above, Input below** for each field. Help and field errors near the Input, usually beneath, never confused with the next label.
- “Full width” means the **sensible bounded form content column**, not every field stretching to the entire 1440px page. Short fields may stay short; addresses and longer errors need enough room.
- Use multiple columns only when fields genuinely form a meaningful set (e.g. city/postal code in one address), there is sufficient space and visual/keyboard reading order remains clear. Stack to one column at narrow widths.
- Placeholder is **not a substitute for visible label**. Preserve htmlFor/id association, required/optional text, disabled reasons, visible focus, keyboard order and autofill support.
- Errors need intelligible text and association with their Field (e.g. `aria-describedby`). Whole-form submission failures also need discoverable summary/navigation. Never clip long error text with fixed heights.
- Save/Cancel/Back actions match the actual transaction boundary. Prevent duplicate submission and implement genuine success/failure/recovery. Mock animation is not evidence a backend save succeeded.

## SF3 — Spacing, surface and responsive acceptance

1. Inherit project spacing tokens, **not universal pixels**. Confirm group-gap > item-gap. Removing a giant Card is **not permission to erase independent section gaps**.
2. Horizontal setting rows align text baseline and control optical center when space permits; long help wraps instead of crushing controls. Switch has a clear text association.
3. Stacked forms treat label, Field, help/error as **one Field cluster**. Gaps between Fields should exceed local error/help spacing; error text must naturally expand layout.
4. Test actually supported widths (e.g. 320/360/768/1440), 200% text, long translations, errors, disabled/loading/success, dark mode and scroll end. If not tested, report `NOT TESTED`.
5. When removing Card shells, compare real before/after grouping; unrelated content must not touch and destructive warnings remain.
6. Screenshots, DOM and rule scans show geometry/contract risks—not automatically aesthetic quality or actual save reliability. Unobserved components cannot be marked PASS.

## SF4 — Integration with MauForma phases/gates

- **PX1/PX2:** Determine product type, then each Settings/Form/Hybrid subregion's independent versus grouped submit model; Page Purpose Card records task and save model.
- **R0:** Capture actual field states, long text, responsiveness and good inherited layout *before* removing any shells.
- **R1:** Establish grouped sections and separate destructive actions; distinguish Row versus Stacked regions in hybrid pages.
- **R2:** Apply row/stack decisions, surface necessity, inter/intra-group space and control width; reuse Semantic Spacing, Surface Architecture and Control Geometry gates.
- **R3/R4:** Refine label hierarchy, component states, semantic danger color and coherent controls without overwriting approved brand.
- **R5:** Compare same data/error/viewport before/after. Test real save, failure and undo paths. Status must be `FIXED & VERIFIED / UNFIXED / NOT AUDITED`.

## SF5 — Scenario matrix (complements source scans)

| Must test | Pass criteria |
| --- | --- |
| Routing | Independent setting Row, multi-field Form Stacked, hybrid divided; exceptions justified |
| Labels | Visible, not crushed, correctly associated with genuine control |
| Field/error | Long inputs have space, complete errors are shown and owned by proper Field |
| Surface | Remove needless giant Cards but preserve necessary sections/panels/gaps |
| Destructive action | Separate, consequences clear, appropriate confirmation and permission protection |
| State | Pending/success/failure match real persistence, not only Mock |
| Responsive | Stack at narrow sizes, usable controls, no overflow or hidden final content |

Synthetic examples: `assets/settings-form-layout-cases.json`, `examples/settings-form-layout-demo.html`. Validators: `python3 scripts/validate_settings_form_layout.py --repository` and `node tests/settings_form_browser_smoke.mjs` (with the project/CI Playwright installed). **Synthetic passes do not certify real product UI.**
