# MauForma Phase-2 English Runtime — Second-Pass Semantic Review

**Review date:** 2026-11-21  
**Scope:** PR #45, 83 translated references, 4 pre-existing English references, 1 preserved bilingual boundary source.  
**Source baseline:** main at 54a4af62566da1532c2b68d4301b531aee118e81.  
**Review decision:** **PASS — no outstanding identified source-to-English blocking divergence after corrections.** This decision is based on the checks described here, **not a claim of formal proof that arbitrary English prose can never be misunderstood**.

## Review methodology and evidence classes

1. **All 83 translated files, source-to-target structural audit:** For each pair, compare section/headline count, table rows, fenced code blocks, original file-reference paths and quantitative timing/length/percentage clauses. Flag and inspect compressions, missing headings, missing references and normalized-unit differences. This is a **coverage and anomaly screen**, not a semantic oracle.
2. **All 83 source Git blob IDs:** Compare every translation-contract \`source_blob_sha\` against the corresponding actual original file in the baseline \`main\` Git tree. **83/83 exact matches**. The original Chinese source remains recoverable by its Git blob SHA.
3. **High-risk bilingual content review:** Read original and translated normative clauses, especially for component library installation and native-control exceptions, motion consent, surface/card attached-rail prohibition, page-header H0, design discovery and choice provenance, design-craft/evidence classes, composition before palette, Figma source authority, data comparison/known-versus-demo conditions, and multilingual UI locale. Correct missing original sections rather than presenting a rewritten policy as translation.
4. **114 Anime.js motion recipes:** Compare original and translated **114/114 exact recipe IDs**, **114/114 unchanged Tier A/B/C values**, and **114/114 exact or translated-equivalent technical API mappings**. Correct the erroneous typewriter API text. Retain 45 official easing identifiers and the distinction between official Anime.js APIs and user/Skill recipe names.
5. **Regression tests:** Preserve static English semantic anchors and source-to-target Chinese/English examples, original runtime gate tests, and Chromium synthetic browser regression. Recheck the final PR head, not an earlier green run.
6. **Git diff scope:** PR changes were confined to 83 references, the phase-2 inventory/contract, CI and validators/tests, plus this review record; no user-product code is changed. Confirm no unexpected new dependencies or unrelated changes.

## Issues found and resolved in this review

| Area | Finding | Resolution |
| --- | --- | --- |
| Design Discovery Interview | The English version shortened an original 184-line source to 89 lines and omitted real three-product conversation cases, a six-property comparison table and versioned approval boundaries | Restored the original question cadence, two-stage choices, cake/repair-ticket/AI-tool examples, six dimensions, original v6.4/v6.6/v6.7/v6.8 rules and references |
| Design Craft Loop | Five-mode minimum-deliverable table, seven detailed craft-dimension checks and six anti-template critique questions were compressed or omitted | Restored every table, review evidence class, P0–P3 definitions, mode exit flow and external-source privacy boundary |
| Composition First | Original Gate A0–A4, data confidence \`known/demo/unverified\`, 300px Hero exception, example schemas and scroll/Grid links were partly omitted | Restored exact gate responsibilities, examples, versioned technical links, failure conditions and user-decision exceptions |
| Motion & Interaction | “Read first” was weakened to “read selectively” | Restored source reading priority with relevance qualification |
| Semantic spacing and surface examples | Numeric boundary about 0px gaps/32px blanket repair and 1px redundant Card borders lost precision | Restored the examples and valid connected-surface exception |
| Original source cross-references | Several abbreviated references omitted explicit names for navigation, icon and spatial-rhythm governance | Restored them without expanding task authorization |
| Anime.js recipe typewriter | Original \`splitText or text update + timer\` was incorrectly concatenated in English | Fixed formatting and meaning; **Tier and API owner unchanged** |

## Preserved non-negotiable meanings

- **Authority:** A recommendation is not a user-confirmed choice; prior user-approved exact HEX, navigation, density and animation permissions cannot be replaced silently.
- **MUST/SHOULD/MAY and exceptions:** No forced libraries, total product redesign, mobile support or animation without proper task scope. Required interactive controls must actually work; legitimate accessible native controls remain permitted.
- **Data truth:** Missing/null measurements do not become zero, mock values do not become real analysis, no claimed successful backend request based on a screenshot or synthetic demo.
- **Accessibility:** Keyboard/focus, screen-reader semantics, reduced-motion, text zoom, overlay visibility, meaningful semantic status and final-scroll reachability remain binding for applicable platforms.
- **Visual exception boundaries:** Card-attached decorative colored strips remain disallowed; meaningful external or actual hierarchy/status indicators remain permitted. Operational explanatory pre-H1 copy is removed without deleting actual breadcrumbs/brands/chapters.
- **Technical integrity:** Version/API distinctions, 45 easing terms, 114 original recipes, 123 extended catalog total, selector and file-path roles, timing ranges and visual fallback conditions are retained.
- **UI locale:** Translating English runtime instructions does **not** translate a user's existing Chinese product UI to English.

## Limits and merge gate

This is a **second-pass, risk-driven bilingual semantic audit**, supported by a structural comparison of **all 83** translated references. It is **not** a claim that every sentence received a separate certified human translation, nor that visual browser smoke validates a customer application.

**Accept for merge** only if all required GitHub Actions jobs pass on the final exact PR head SHA and there are no unresolved conflicts, review blockers or third-party publication violations. Branch protection remains authoritative. If any subsequent edit changes normative translation content, rerun the relevant source parity and CI checks before release.

**Status terms:** “reviewed_and_approved” means this recorded second-pass review made an explicit bounded acceptance decision; **NOT** an assertion that static CI alone proved perfect semantic equivalence. Further external human bilingual reviews remain welcome and can revise findings.
