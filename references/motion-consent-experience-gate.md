# Motion Choice & Experience Gate — User Chooses Motion; UX Owns Interaction (v6.14)

Applies to all Web sites and apps: Operate (workspaces), Persuade (brand/marketing), Read (reading/learning) and Experience (interactive/media). Motion is a **design decision**: neither “no animation by default” nor “animate everything” is an acceptable universal rule. Consider **user authority, interaction feedback, information continuity, visual craft, accessibility, performance and regression evidence** separately.

## Gate M0 — Discover and respect user motion choice before library/CSS decisions

1. Read existing design decisions, approved brand animation, motion built into the current component library and motion preferences the user has **explicitly expressed for this project**. Label the source: `confirmed` (user selected), `delegated` (user explicitly entrusted the decision to the Agent), `inherited` (existing approved system) or `unresolved` (not settled).
2. **New sites, comprehensive redesigns or interaction overhauls that substantially change the motion feel:** If motion is neither confirmed nor explicitly delegated, **proactively ask the user once**. Ask after agreeing the design direction but before final Motion Tokens/component implementation; combine with a single direction-choice round when possible. The user not mentioning animation, asking for simplicity/speed or delegating coding **does not mean** they agreed to no animations. Nor does it authorize extra scroll effects, particles or full-page transitions.
3. **Do not re-ask settled questions.** Inherit an explicit no/soft/richer motion choice unless the planned effects clearly exceed the approved scope (e.g. upgrading a tiny hover to strong scrolling parallax).
4. If the user **explicitly delegates all motion choices**, the Agent may select and record the rationale as `delegated`. Do not label the Agent's recommendation `confirmed`. “Just build it” or “ask fewer questions” is not, by itself, consent for additional animation scope.
5. **Small bugs, non-visual fixes and maintenance of existing component states:** Do not restart a whole-site design interview. Use the inherited motion policy. If unresolved, preserve immediate semantic feedback, visible focus/state and functionality **without launching unapproved new visual animation**; mark motion choice unresolved, not permanently disabled. Present concrete choices before major new visual motion changes rather than silently choosing a zero-motion site.
6. **No extra motion is a valid user decision**, but **never remove interaction semantics**. Pressed/selected/focus states, loading, success/failure notices, expanded/collapsed final states, validation and navigation feedback must remain perceivable. No motion ≠ no feedback.

## Gate M1 — Three visible options in one natural user question

When a question is necessary, ask **one conversational question**, giving a few choices with visibly different results plus a project-specific recommendation and performance tradeoff. A recommendation is **not** confirmation:

> How should interactions and transitions feel on this site?
>
> **A | Direct and quiet:** State changes happen immediately; buttons and focus still have clear feedback. No extra page or scroll animation. Fits high-frequency work or very low-motion preference.
>
> **B | Subtle and fluid (candidate for many everyday Web products):** Slight button press, smoothly moving Tabs indicator, brief panel/dialog transitions and continuity in lists and state changes, without delaying operations.
>
> **C | Expressive:** Builds on B with limited shared-element transitions, important Hero/media entrances or scroll storytelling where justified. More brand presence, but larger adaptation and performance budget.
>
> I recommend B because [specific reasons grounded in this product]. Would you choose A/B/C, mix them, or describe your own direction?

**Do not copy this script mechanically**. Explain effects in terms of the user's actual pages and tasks. Accept “you decide,” one selected motion class or different intensities across pages. A/B/C is a **choice aid**, not a permanent hierarchy or single required global tier. If an explicit direction already exists, ask only what is genuinely unknown; never combine motion, palette and typography into an unwieldy survey by default.

### Same principles, different visible behavior

| Mode | Interactions worth discussing | Avoid |
| --- | --- | --- |
| Operate | Filter/Tab change, Popover/Dialog entry, insert/delete, status notifications and navigation focus | Flying in every row on a busy list; animation delaying a click |
| Persuade | Navigation/CTA feedback, gallery or product switch, limited Hero/product storytelling | A first viewport that waits for animation before showing actual content |
| Read | Table-of-contents selection, anchors, annotation/disclosure and exercise feedback | Repeatedly sliding article prose so reading is interrupted |
| Experience | Work transitions, shared visual subjects, directed narrative/Canvas interactions | Loops hiding exits and actions that must wait for an animation to end |

## v6.15 — Choosing B or C does not mean component motion is complete

This gate governs **whether and how much motion the user approved**. Actual products must still execute `references/component-motion-choreography-gate.md`: inspect real components/states and give high-value interactions meaningful motion, instant feedback, or an intentionally static treatment. Prioritize in-component indicators, disclosure, status morphing, spatial continuity and actual results. Route transitions alone or generic repeated fades are insufficient. Explicit user `none` and system reduced-motion remain binding; the Agent must not use a richer choice to justify arbitrary extra effects.

## Gate M2 — Classify by purpose, not a yes/no effects toggle

For interactions that **actually exist**, document `trigger → from/to state → purpose → visual treatment → cancellation/interrupt → reduced-motion alternative`:

- **Input feedback:** Hover, press, selected, focus-visible and field response. Timely and legible; focus must never wait for animation.
- **Disclosure and overlays:** Dialog, Drawer, Dropdown, Popover and Accordion can transition gently. Close, Escape, focus return and real DOM state must synchronize.
- **Navigation/continuity:** Tab, sidebar and route switches retain context/reading position; some routes need no animation. Avoid double spinning or blank flashes. Consider View Transitions API only with real support and fallback checks.
- **Data/status:** Reordering, chart updates, progress, loading/success/error. Never fake a progress value or loop an expensive full entrance on frequent/streaming updates. Motion cannot conceal an incomplete backend task.
- **Story/delight:** Marketing product showcases, galleries, selective SVG and scroll stories require matching permission. A recipe's presence in the library does not authorize auto-installation or use.

Every effect needs an answer to **what it improves over an immediate switch**. Without a reason, keep correct state feedback but omit the animation. Where meaningful motion could significantly help, proactively offer the user a choice rather than defaulting to no motion.

## Gate M3 — Shared Motion Tokens, implementation and fallback

- Map role names such as `fast/normal/deliberate`, `enter/exit/standard` easing and `none/reduced/full` preference to **project-specific Motion Tokens**. These are illustrative roles, not mandatory 150/250 ms values, fixed bezier curves or Spring everywhere.
- Prefer short, immediately responsive easing for frequent actions. Larger movement or important brand moments may be longer if confirmed through reading/interaction/performance and accessibility testing. Distinguish productive from expressive motion; do not bounce every Card.
- Start with current component-library transitions, CSS, Web Animations API or framework-native Transition. Add Motion, Anime.js or GSAP for genuinely complex layout/orchestration only after checking dependency permissions, licensing, SSR/lifecycle and touch/low-performance fallback. Do not install multiple heavyweight libraries for simple hover.
- **Business content must not require animation completion to appear.** Important text, forms, buttons, status and exits remain visible/usable in initial HTML, without JS, on low-end devices and with motion disabled. Motion never delays actual state persistence.
- `prefers-reduced-motion: reduce` is an **independent accessibility requirement**; even a user choosing C cannot override an OS/system reduced-motion preference. Eliminate/simplify nonessential movement, scaling, parallax, loops and transitions while preserving immediate feedback. JavaScript motion must observe both initial preference and runtime changes and cancel effects already running.
- Handle quick repeated interactions, reverse/cancel, route unmount, hidden tabs, low-end devices and unmount during scroll. Use lifecycle/cleanup guidance in `references/animation-integration-lifecycle.md`.
- Respect touch, keyboard and background work. Page-level transitions must not mask focus outlines or delay usable errors/confirmed results.

## Gate M4 — Acceptance and evidence; CSS alone is not motion proof

- **User authority:** Report the selected tier, decision source and explicit authorization; do not claim “you chose B” when the user merely asked for better aesthetics.
- **Coverage:** Exercise actual Hover/Press, Tabs, Dialog, navigation, loading/error/success and relevant on-page interactions. If B/C is chosen but important controls have no meaningful continuity, fix or justify; do not quietly downgrade the whole product to static in the name of performance.
- **Real transition evidence:** Capture before/during/after in the browser, confirm movement actually ran, no flicker, stable layout, interruption behavior, reachable focus and correct final state. DOM/CSS scans or a single screenshot cannot prove high visual quality.
- **Stress:** Rapid double clicks/reversal, dialog while typing, many list updates, long CJK/English text, supported narrow/mobile layouts, light/dark modes and 200% zoom.
- **Reduced motion:** Emulate reduced motion and confirm unnecessary movement is removed or reduced while the UI stays immediately usable, focusable and interactive. Avoid using only blanket `* {animation:none!important; transition:none!important}` as the universal solution.
- **Performance:** Measure FPS, long tasks and layout jitter when test capabilities exist; do not invent unmeasured values. Missing low-end/device/time coverage is **not verified**, not implicitly passed.
- **Report:** Give verified/uncovered components, chosen motion, intended benefit, evidence, reduced-motion strategy and open issues. A standalone Mock must not be described as real-product E2E.

### Reference standard

Follow applicable accessibility guidance and platform motion preferences. Official sources are centralized in the repository README. See `references/animation-engine-selection.md` for engine choice, `references/animation-integration-lifecycle.md` for cleanup/fallback, `references/design-discovery-interview.md` for user decision provenance, and `references/visual-qa.md` for full-page QA.
