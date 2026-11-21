# Component Motion Choreography Gate — Animate Actual Components, Not Only Page Transitions (v6.15)

**Applies:** All Web products/frameworks, subject to the motion intensity already confirmed, inherited or explicitly delegated under references/motion-consent-experience-gate.md. This gate closes a v6.14 gap: an Agent could implement one route fade or Dialog fade and declare "interaction motion complete" while leaving everyday components with abrupt state changes. **Motion quality is not the number of animations.** It is meaningful local transitions, clear causality, stable tactile feel and interruptible implementation.

## Gate CM0 — Component Interaction Inventory, before page-level effects

Before designing motion, inventory controls and components that **actually exist and are operated by users**. Record interaction frequency, importance and **observable state changes**. Never invent missing controls or add Cards just to have something to animate. Consider each relevant family **only when present**:

- **Button / CTA:** Pointer, press, loading/result; distinguish frequent actions from important confirmations.
- **Tabs / Segmented / Filters / Navigation:** Move selected indicators continuously from previous to next positions while content and focus remain coherent; a full-page fade alone is insufficient.
- **Accordion / Disclosure / Drawer / Popover / Dialog:** Opening/closing from a trigger, spatial relationship of content/backdrop, cancellation and focus restoration; not merely opacity.
- **List / Card / Grid / Table:** Preserve positional relationships when sorting/adding/deleting/filtering, focus/selection and optional detail preview. **Do not fly hundreds of rows in one by one.**
- **Input / Select / Search / Form:** Focus/validation, clear/results and filter transitions; accurate input comes first.
- **Toggle / Checkbox / Radio / Slider:** Thumb/track/check state and touch feedback, respecting native semantics.
- **Data Visualization / Status / Progress:** Moderate interpolation of **true** data, tooltip/crosshair/comparison selection; never invent progress or rising values.
- **Media / Commerce / Learning / Creative:** Media switches, product variants, chapter disclosure, artwork focus or connected narrative. Do not impose one motion treatment across all domains.

**Decision per important real interaction:** Choose **motion / immediate-feedback / intentionally-static**, with an actual reason. A user's **none** choice allows immediate static feedback for all components, but focus, selection and outcome must still be perceptible. For **balanced/expressive**, route-only animation while every important control remains static does not satisfy the selected direction. **Do not add controls that the page lacks; a narrow bug fix must not become a whole-product redesign.**

## Gate CM1 — Motion Art Direction: recognizable component behavior, not a universal fade

Specify for each actual effect:

component → trigger → from/to state → visual mechanism → timing/easing → purpose → cancel/reverse → reduced-mode → implementation owner → evidence.

Choose only mechanisms relevant to the component; **not every component needs every mechanism**:

1. **Indicator travel / continuity:** Tab underline, segmented thumb or selected sidebar background moves from A to B with meaningful position/size continuity. It is **not** simply another opacity 0→1.
2. **Spatial reveal / disclosure:** Accordion height and bounding surface expand smoothly; Drawer has a logical direction/source; focus and exit remain immediately usable.
3. **State morph / tactile feedback:** Toggle thumb, checkbox checkmark, Button press/confirmation—tactility, not indiscriminate bouncing.
4. **Layout continuity:** After filter, delete or sort, surrounding objects **retain spatial identity**. Use FLIP, Motion layout or TransitionGroup when necessary, without delaying actual business results.
5. **Semantic feedback:** Upload/save/error status badge, short tactile feedback and notices; **update semantic text immediately before ornamentation**.
6. **Visual discovery / storytelling:** Product imagery and text, artwork focus, image transitions or a small number of shared elements. Do not use cursor-following light effects on high-frequency data tables; provide equivalent feedback on touch.

**Anti-repetition:** Scaling every Button to 0.98, moving every Card up 4px on hover or fading/sliding every section is **not a complete motion design**. Check that mechanisms reflect different interaction roles, but do **not** add five effects just to meet a quota. Prefer **one or a few signature effects** for identity, while ordinary controls remain restrained and coherent. A genuinely approved expressive brand can justify more. Basic hover color change is valid feedback, **not proof that the component-motion creative brief is finished**.

**Text, usability and accessibility must survive:** Short Button labels must not break character by character; numbers/errors should update promptly; keyboard focus remains visible; never mark essential readable information aria-hidden; important controls must not be discoverable only on hover.

## Gate CM2 — Recommend an experience before implementing it

- For new projects or major interactive redesigns, retain the v6.14 user-choice gate for motion intensity. When the user selects a B/C intensity, the Agent **must also propose product-specific component mechanisms**, not ask the user to specify each Button. A workbench may feature smooth segmented-indicator motion plus local row reflow; learning content may use chapter disclosure and answer feedback; commerce may emphasize continuity between variant images.
- Show a small **Component Motion Showcase** first when warranted: **2–4 high-value actual components** in **none / selected-level / reduced-motion** modes, describing their distinctive behavior and readable static outcomes. A small local repair need not repeat this full showcase.
- For authorized creative work, consult references/creative-component-libraries.md, references/animation-engine-selection.md and the existing 114-recipe catalog in that order when relevant. Transfer technical methods without mechanically copying skins. Confirm actual framework/version, dependencies, licenses, SSR and mobile performance before adopting React Bits, Vue Bits, Inspira, Motion or GSAP. **Ordinary indicators and Accordions do not automatically need an animation library.**
- Project Motion Tokens should describe duration and easing **plus semantic mechanism roles**: interactive-control, selection-indicator, disclosure, layout-change, feedback, spotlight. Do not bind every transition to one global --duration without considering frequency, travel distance and content priority.

## Gate CM3 — When the right motion is no motion

- Decoration without actionable state changes; full stagger on every refresh of long reading content or dense data tables; slow transitions for high-frequency transactions and sensitive tasks that require immediate confirmation.
- Explicit user **no-extra-motion** or prefers-reduced-motion: preserve **immediate static** selected/focus/result state; disable or provide stopping mechanisms for auto-looping backgrounds, parallax and 3D.
- If motion causes CLS, misaligned rows, false-looking values, skipped keyboard focus, narrow-viewport clipping, slow interaction or frame drops on weak devices, fix the behavior, reduce complexity or remove the effect. **Poor performance is not blanket justification to never explore purposeful component motion**; start with a simpler mechanism.
- Honor the confirmed user direction; do not change palette, framework or large-scale layout just because the user did not request additional creative scope.

## Gate CM4 — Real Interaction QA, closing the v6.14 gap

Required evidence is an **actually triggered state change**, not the existence of an animation CSS class.

1. Cross-check the interaction inventory for each high-value real component and document **motion / feedback / static(reason)**. A route transition does **not** count as component coverage.
2. Trigger real Button, Tab, Disclosure, Toggle, List and Feedback interactions where present. Capture **before / during / settled** states, checking geometry, height or interpolated relationship, not only animationDuration > 0.
3. Test rapid repeat, reversal, focus loss, unauthorized/error cases, narrow viewport and **200% text scaling**. The state must not arrive late, the UI must not become obscured/frozen, and engines must not compete for the same property.
4. Compare identical business outcomes and focus in normal versus **reduced-motion** settings. Nonessential movement should immediately reduce or stop. Verify in the **actual target product** under its real framework, not just a standalone synthetic demo.
5. **Evidence boundaries:** JSON structure/coverage validation does not prove aesthetics; CSS declarations do not prove interaction; passing a demo does **not** certify the user's real product.

## Related standards

External systems, implementation sources and accessibility credits are indexed in the repository README. Confirm current official APIs, dependencies and licenses before adopting any implementation library.

Real implementation must additionally use references/motion-craft-and-continuity.md (storyboard, identity, neighboring layout, text/media and anchors) and references/motion-rehearsal-and-evidence.md (full transition, reversing/interrupting, sampling and recapture).

Use together with references/motion-consent-experience-gate.md, references/component-craft-gate.md, references/control-geometry-gate.md and references/animation-integration-lifecycle.md.
