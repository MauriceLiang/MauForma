# Progressive Visual Refinement Gate — Staged Improvement Without Template Imitation (v6.21)

This guide describes a transferable **staged diagnosis-and-convergence process**. It does not reproduce another Skill's writing, a user screenshot, enterprise page or real dataset. It applies to enterprise, consumer, educational, content, creative and showcase Web products. It **does not** mandate black-and-white themes, universally small radii or deleting all emoji.

Before beginning, run Product Experience Routing (product-experience-routing-gate.md) to understand the page's actual task and structure. If the structure is wrong, fix UX first; superficial styling is not a substitute.

## Decide between UX restructuring and UI refinement

| Primary finding | Correct path | Not a valid fix |
| --- | --- | --- |
| The product's distinctive main task is missing; page looks like a generic admin template | Return to PX2/PX3, redesign content and primary action | Changing only palette, icons or radius |
| Main workflow is correct, but spacing/hierarchy/color is inconsistent | Progressive R0–R5 refinement | Declaring an entire page done after fixing one Token |
| User requests only a specific button/icon/function bug | Scoped diagnosis, repair and regression | Unapproved navigation and page-architecture changes |
| Brand intentionally calls for playful, game-like or expressive presentation | Refine within the confirmed direction, preserving necessary expression | Forcing a muted enterprise admin skin |

## R0 — Baseline & Diagnosis: record defects and existing strengths

Inspect actual product tasks, established design decisions, installed component library, design Tokens and real pages. Capture beginning, middle, end and critical interactions on **the same route, data state and viewport**. Without browser access, use only provided screenshots/source and explicitly label **NOT VERIFIED**. Separately identify evidenced P0/P1 issues: missing task, wrong visual focus, unrelated panels touching, excessive information density, incoherent icons/color, responsive and accessibility failures.

**Gate:** Each finding must have a location, evidence, impact, priority and authorized scope. Do not invent defects to meet a quota. Record good existing decisions to protect them, but **do not call a bad inherited state a correct baseline**.

## R1 — Experience & Composition: choose the real focal point first

Use PX2's Page Purpose Card to define the main task, secondary actions and content sequence. If the structure is wrong, compare **at least two materially different low-fidelity information arrangements**; tinting a stock “sidebar + four numbers + list” is not an experience redesign.

Identify what should catch attention within the first three seconds. A grayscale glance test may help, but is **not user research**. Prioritize real content and next actions; reject meaningless KPIs, fabricated outcomes, decorative hero slogans and filler cards.

**Gate:** First-screen focus, information priority and primary action must match the user's task. If not, stop cosmetic refinements and return to R1/PX3.

## R2 — Layout & Spacing: relationships, grid and density

**v6.22 settings/form/hybrid check:** On Settings, Form or Hybrid pages, first apply Settings & Form Layout Gate (settings-form-layout-gate.md). Individually saved settings normally place label and short control side by side (stack at narrow breakpoints if needed); consecutive form fields form vertical clusters; hybrid areas divide according to save/submit semantics. Removing a decorative outer Card must **not remove meaningful group spacing or dangerous-operation warnings**. Field errors, crushed controls and save/submit feedback must be retested at R5.

Distinguish inside / peer / section / connected / anchored spatial relationships. Check horizontal/vertical alignment, parent gap versus internal padding, page-end safe space, scroll reachability and narrow-screen reflow. Independent sections must not accidentally touch at zero gap; a genuine Tabs+Panel or table header/body may intentionally share an edge. Reduce redundant titles and needless cards instead of applying a mechanical 16px gap to every container.

Reuse the existing contracts and tools in semantic-spacing-rhythm-gate.md, spacing-regression-protection-gate.md and grid-alignment-and-viewport-safety.md.

**Gate:** Grouping, whitespace, alignment and content access must work at supported viewports. Hiding overflow, negative margins or unrelated local padding are **not acceptable disguises for a structural problem**.

## R3 — Typography, Palette & Icons: clear focus, justified decoration

Assign semantic type roles to titles, key numeric values, body copy, explanations and metadata. Give color explicit responsibilities: brand accent / primary action / success / warning / error / data / background. A new palette remains subordinate to confirmed brand decisions; **do not automatically replace an existing brand with gray-blue or black-and-white**.

- **Emoji are conditional:** Remove decorative emoji that convey no information or conflict with a professional icon family; replace with coherent icons when appropriate. **Retain and harmonize** emoji that are real social content, children's learning material, game feedback or approved brand assets. **Never delete emoji globally.**
- **More icons are not inherently more professional:** Choose by object/action semantics, outline consistency, optical weight and accessible names, preferring existing project icons. Plain text may be better.
- Check whether background, buttons, KPIs and warnings compete for the same first focal point. Color should clarify meaning, not wallpaper a screen with colorful stickers.
- Respect an explicitly established brand identity and intentional art direction.

**Gate:** Core actions remain discoverable in grayscale; semantic color roles are clear; icons have coherent meanings and families; essential content meets contrast requirements.

## R4 — Radius, Surfaces & Component Finish: consistent shape grammar

Use inherited or new semantic Tokens (for example radius-control, radius-panel and radius-overlay) to coordinate corner radii based on size and nesting. **Do not mandate one radius value for every element**. For same-role Buttons, Fields and Dropdowns, unify heights, text baselines, spacing, borders, shadows and hover/focus/disabled/loading states. Remove needless floating shadows, heavy borders, giant pills and Card-inside-Card stacks.

**Gate:** Controls serving the same role have coherent appearances **and complete behaviors**; radius hierarchy is justified; long text, lower-end devices, zoom and dark theme still work. Behavior and accessibility may not be sacrificed.

## R5 — Compare & Verify in the same environment

Compare before/after on the **same page, state, viewport and theme**. Verify the main task and first-screen focus, section spacing, typography, icons, surfaces and actual control states. Inspect beginning, middle, end, final scroll point, narrow supported viewport and **200% text scaling**. Include dark theme, RTL, long labels and error states when applicable to the actual product.

Scripts and DOM scans can identify measurable risks but **an automated PASS is not proof of aesthetic excellence or validated user experience**. Every R0 item must be reported as **FIXED & VERIFIED / UNFIXED(reason) / NOT AUDITED(reason)**. Without a runnable target or with review-only authorization, state the limits; do not claim the real product was repaired.

## What actually makes a screen feel like an AI template?

| Observation | Primary root-cause hypothesis | Phase |
| --- | --- | --- |
| Replacing the product name leaves the entire page generic and unchanged | Task structure may be too generic | R1 |
| Every site starts with Sidebar + numeric Cards + table | Information architecture is templated | R1/R2 |
| Unrelated modules touch or Cards nest needlessly | Incorrect spatial relationships | R2 |
| Decorative emoji, meaningless icons, every color competing | Unclear visual roles | R3 |
| Massive gradients/shadows obscure information | Color/hierarchy and surface choice conflict | R3/R4 |
| Every control is a huge pill; button sizes diverge | Inconsistent shape grammar | R4 |
| Palette changes but real task is still missing | UX was not improved | **Return to R1** |

**Important:** Gradients, emoji, rich colors, radius and playful/game-like design may all be appropriate to the brand and user's actual task. The question is **why**, whether applied coherently, and whether they obstruct work—not a blacklist of individual effects.

## Staged delivery record

| Stage | Required evidence | Output |
| --- | --- | --- |
| R0 | Original screenshot/real page/source, confirmed decisions and findings | PASS / NOT AUDITED |
| R1 | IA, primary/secondary CTAs and meaningful structure comparison | PASS / FAIL / NOT TESTED |
| R2 | Grid/spacing/viewport evidence and risk scans | PASS / FAIL / NOT TESTED |
| R3 | Typeface roles, color and icon rationale with comparisons | PASS / FAIL / NOT TESTED |
| R4 | Radius/surface/control roles and states | PASS / FAIL / NOT TESTED |
| R5 | Real-page or user acceptance evidence; unresolved issues | PASS / FAIL / NOT TESTED |

The workflow may revisit stages or skip irrelevant work for a scoped task, but **SKIPPED IS NOT PASS**. User reference images remain in the current authorized conversation; they must not be uploaded to the public repository. Demonstrations must be independently invented. See assets/refinement-stage-cases.json.
