# Aesthetic Positions from External Design Skills — What Can Transfer and Where It Stops

This document records transferable ideas **and explicit limits** from different design approaches. Author preferences are not universal prohibitions. Source authors and acknowledgments live in README. MauForma independently organizes these rules and examples; any actual reuse of upstream code/assets must honor licenses.

| Source | Valuable aesthetic thesis | Best suited to | Do not transplant mechanically into |
| --- | --- | --- | --- |
| Impeccable | Change visual intensity based on whether the user must Persuade, Operate, Read or Experience; be bold when justified or reduce noise when needed | Page-task selection across products | Treating noise reduction as a ban on expressive design |
| Anthropic Frontend Design | A clear visual subject and artistic position; type, copy and content context create identity rather than default templates | Brand, portfolio, culture and product stories | Arbitrarily choosing unusual fonts without actual content |
| UI/UX Pro Max | Multi-style knowledge and product-aware design suggestions; shared Master plus page overrides | Multi-page, multi-industry and evolving sites | Letting automated scores replace the user's final design choice |
| Taste Skill / Leonxlnx | Adjustable `DESIGN_VARIANCE`, `MOTION_INTENSITY`, `VISUAL_DENSITY` encourage asymmetry, experimental whitespace and expressive motion | Creative agencies, fashion, art/portfolio | Applying high variance as the ERP/CRM default |
| Taste Design DNA / Senlin | Record WHY and tradeoffs/evidence/rejected alternatives, not just WHAT (color/font) | Competitive audit, design transfer and source-site research | Claiming original intent without actually observing the site |
| Vercel Web Design Guidelines | File:line review rules, accessibility and interaction quality | Web implementation and code review | Mistaking static source checks for real-browser testing |
| Vercel Composition Patterns | Fewer boolean props, clearer composition and ownership | Complex reusable React components | Copying React Context/Hooks unchanged into Vue |
| Vue Best Practices | Composition API, one-way flow, minimal reactivity state and clear roles | Real Vue 3/Nuxt apps | Copying React code into Vue SFC APIs |
| Vercel React Best Practices | Fix request waterfalls and bundle costs before micro-render changes | React/Next performance work | Letting optimization break existing semantics/usability |
| Anthropic Webapp Testing | Real browser interactions, screenshots and log verification | Visual QA, forms, navigation and responsive testing | Claiming business functions verified from a static page alone |

## Additional workflow influences and verification boundaries

| Source | What was examined | Transferable MauForma idea | Do not copy |
| --- | --- | --- | --- |
| Anthropic theme-factory | Color/type themes for slide/document/HTML outputs, with presets | Token cohesion and **select before applying** | Demo palettes as one universal Web product theme |
| pbakaus Impeccable | Topic guides for type, color, space, motion, interaction, responsive UX copy | Evidence-based refinement across the seven domains in `references/design-craft-loop.md` | Blanket “never use this font/Card” bans |
| julianoczkowski designer-skills | Brief → IA → Tokens → implementation → review stages that may be skipped | Scope process depth to task, separate independent review from implementation | Demanding full interview/project Brief for every small fix |
| OpenAI figma-implement-design | Design context, images, assets, existing components and visual recheck | Fidelity-only mode in `references/figma-fidelity-workflow.md` | Inventing pixel-perfect results without source design or MCP access |
| The video-labeled design-process-pack | Described need to clarify audience, goals and information architecture before design | General discovery inspiration; user-approved constraints prevail | **No uniquely confirmed upstream repository**; do not claim a full code audit was performed |

## Preserving distinct aesthetic viewpoints

- **Distinct styles must not be averaged away:** Experimental design can remain asymmetric, off-grid, oversized and motion-rich; calm minimalism can value clarity and quiet structure.
- **Page task determines suitability:** A brand site may use Persuade while its control panel uses Operate. One product need not have one density everywhere.
- **Dials describe intensity, not mandatory scores:** MauForma's `variance/motion/density` are **suggested 0–10 ranges** inspired by Taste's three controls; do not copy its default values or prohibitions.
- **Source licensing and permissions:** Check license and provenance before adapting external code. This repository provides independently authored guidance/examples; future assets need explicit license clearance.
- **No indiscriminate negative rules:** Large whitespace, all-caps tags, glass effects and dark palettes are **not defects by themselves**. They become problems when they fail to serve genuine content or task.
