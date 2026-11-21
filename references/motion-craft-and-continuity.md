# Motion Craft & Continuity — High-Quality Movement in Real Products

> Motion must have a cause, frames must tell a coherent story, and the process needs real frame-by-frame review. These are general Web interaction rules for Vue/React/Svelte/Angular and related stacks—not a dependency on any one visual demonstration tool. Apply alongside `references/motion-consent-experience-gate.md` and `references/component-motion-choreography-gate.md`.

## Gate MC0 — Motion quality is design craft, not effect quantity

- For interactive products, **proactively seek continuity that improves real operations** *within existing user authorization and the project's Motion Policy*. Do not reduce all interaction to static states or one route fade merely because the user did not list animation effects for every Tab/Dialog/filter. Without authorization, inherit the choice gate and offer an experience proposal; **do not treat Agent preference as user consent**.
- A motion must support at least one legitimate purpose: **confirm an action** (press/feedback), **maintain spatial relationships** (shared selection indicator/layout reflow), **explain hierarchy** (menu emerging from its trigger), **communicate state** (loading → result), or **provide narrative** (product storytelling). Remove purposeless decoration.
- Important interactions deserve polished feedback, which may be restrained. Frequent actions need quicker, reversible, interruptible behavior than occasional showcase moments. Fewer effects are not proof of poor design; explain which changes benefit from continuity and which should update instantly.
- **A static composition must work first.** Animation cannot repair bad hierarchy, density, whitespace or control placement. Never use perpetual floating, glows, attached decorative color rails or cursor-following noise to hide fundamental defects.

### Creative motion is an opportunity, not a global ban

When a user delegates high-quality creative, branded or immersive design, **proactively explore signature motion specific to the product**. Do not wait for the user to name the technical effect, and do not stop at generic fade/slide. [Expressive Motion Vocabulary](expressive-motion-vocabulary.md) provides combinable mechanisms: hardware close-ups may use scroll zoom + mask reveal; portfolios character reveal + text morph; edition browsing horizontal scroll + scroll snap. Establish real content, a compelling visual subject and an intentional rhythm first. Complex creative sequences are allowed when useful, but tutorial timings are **not** universal constants.

## Gate MC1 — Storyboard the state transition before CSS

For an important real interaction, record a compact storyboard, not an essay for every hover:

`intent → trigger → before → during → after/payoff → interruption/reverse → reduced motion`

1. **Before:** Object identity, selected state, anchor and associated content are discernible.
2. **Trigger:** Real pointer/keyboard/touch/data event. Feedback begins immediately when input occurs.
3. **During:** Specify what moves, makes room, exits or waits, and the causal order/priority.
4. **After:** A complete, operable result; no ghost layers, half opacity, empty placeholders or lost focus.
5. **Interrupt:** Trigger again or reverse around **30% or 70% progress**; movement continues from the *current visible state*, not a sudden jump to the original start.
6. **Reduced:** Remove nonessential motion without losing state, feedback, accurate data or keyboard function.

Only marketing demos, instructional narratives or animation stories normally require 3–5 longer narrative beats, a final payoff, poster frame or optional loop. **Never make production interactions wait for storytelling.**

## Gate MC2 — Continuity: an object must not vanish and reappear as an impostor

- **Identity:** Keep a Submit → Pending → Success button semantically and spatially continuous where possible, preserving component identity, DOM/framework key and focus. Reserve enough width for longest copy or animate the label and neighboring layout consistently. Replacing it with a lookalike new Button that teleports pointer/focus is wrong.
- **Shared geometry:** Tab indicator, nav selection, media and Card→detail can use shared elements, FLIP or layout transitions when one unambiguous object links old and new positions.
- **Neighbor response:** On row insert/delete, filter and sort, neighboring content should make room continuously. Do not show a new Card first and shove the entire list away one frame later. Dense tables or fast live updates may switch instantly; data correctness outranks choreography.
- **Entry/exit:** Meaningful entering and departing content should have coordinated transitions; keep exiting nodes drawable until finished without blocking Escape, close, focus restoration or business response. Check actual support for native `display`, unmount and Transition APIs first.
- **Anchor:** Popover, Tooltip and Dropdown need a stable trigger origin. An open menu should not drift when content changes. Synchronize dialog/drawer layering, backdrop, pointer areas and scroll lock.
- **Morph:** Coordinate size, position, boundaries and content. A container may animate, but **do not scale paragraph text as a fake layout transition**. Prefer width constraints, crossfades and actual layout transitions that avoid stretched/blurred glyphs.
- **Handoff:** When a visual object moves between containers, previous and next instances must align in position/size at handoff. Avoid jumps, double exposure and double selected highlights.
- **Stable chrome / local tracks:** Keep header, main container and action anchors stable while settings, prices and charts change. Move only actual changed regions on bounded paths. Masks manage local entry/exit, **not** full-page blur to conceal incorrect layout. Related data should hand over sensibly rather than replaying an entire screen entrance.

## Gate MC3 — Timing, easing and layering have distinct roles

Do not copy `transition: all 300ms ease` onto every node.

| Motion role | Suggested behavior | Avoid |
| --- | --- | --- |
| Tactile input | Short response beginning on press; focus immediate | Delaying confirmation before revealing it |
| Selection indicator | Smooth travel/size matching, gentle settling | Old location disappearing while a new location abruptly highlights |
| Menu/disclosure | Spatially originate at trigger with content entering in overlap | Empty expanded container that fills with text only later |
| List changes | New item reserves space with coordinated neighbor movement | Entire column flying in on every refresh |
| Status and numbers | Stable anchors and width; animate only true changed parts | Invented numbers, arbitrary rolling, overlapping words |
| Showcase narrative | Staggered main/support layers with actual payoff and rest | Every element endlessly moving in the same direction/speed |

- Stagger related parts by approximately **40–80ms** where helpful. Use different curves for motion versus entrance and overlapping phases rather than strictly serial waits. These are **showcase heuristics, not global thresholds**; buttons are usually faster and input/focus are immediate.
- Natural movement visibly starts, travels, slows and settles. Tune distance, duration and easing together; lengthening duration alone does not fix a sudden movement.
- Link causal changes on an overlapping timeline: click → tactile feedback → main content change → supporting label. Never show “success” before a true result, or delay visible completion after business state is done.
- **Start and rest are designed states.** The pre-motion frame must remain readable; after the result, genuinely stop. Endless pulsing, repeated counts and floating are not substitutes for conveying the result. Optional showcase loops need a recognizable poster and comprehensible reset.
- Use elasticity, overshoot or arc paths sparingly for a few meaningful identity moments. Paragraphs, tables and dangerous actions should not bounce. Avoid site-wide `will-change`, constantly running effects or purposeless loops.

## Gate MC4 — Motion of text, numbers and charts is information design

- Glyphs and icons reveal defects more clearly than their bounding Cards: inspect rasterization, font weight changes, baseline jumps, clipping and stroke jitter before/during/after transforms.
- Reserve label width and alignment before changing long/short copy. Animate only changed words/digits where useful; never present unknown data as a fictional rolling number.
- Chart interpolation must respect corresponding real data, units, time windows and series identities. Initial load and refresh are different contexts; frequent streaming updates do not require complete entrances each time.
- Loading → success/failure copy and accessible states should update promptly. Motion supplements information; it cannot delay screen readers or actual submission.

## Gate MC5 — Pointer, drag, scroll and staged stories, only when applicable

**Real applications:** Respect real pointer/touch/keyboard events. Drag begins at the actual grab point, keeps an origin placeholder, communicates the destination and allows cancellation/reversal. A floating Card with a suddenly reordered list is not sufficient. Scroll-driven effects need stop, reverse and reduced-motion behavior and must not hijack the user's primary scroll.

**Marketing/instructional *simulated* demos only:** A cursor story can show typing/clicking, key hints, camera crops and scene composition, but label it **simulated demo**. Fake clicks and API calls are never real functionality tests. Cursor motion needs a target and genuine causality; derive positions from measured target geometry rather than hard-coded coordinates. A 3–5 beat, **10–16 second** loop is an optional showcase suggestion, never a default application interaction length. A stable initial/poster/thumbnail frame must communicate value independently. Loop resets need a causal transition or an unseen reset; never visibly reverse real business data without reason.

**Transfer principles, not the demonstration frame:** Reuse focal hierarchy, spatial depth, sensible crops and intentional whitespace—not an example's tiny viewport, fake OS shell/phone, placeholder text or fixed camera composition in real business UI.

## Gate MC6 — Implementation and protection

- Reuse existing framework, UI library and motion tokens. CSS/framework Transition for simple changes; FLIP, View Transitions API (with support/fallback checks) or Motion for shared geometry; GSAP/Anime.js only when complex timelines warrant them. Do not transplant framework-specific demo suites or add unnecessary dependencies.
- Own and clean up keys, portals, scroll locks, focus restoration, rAF, observers and timers. Handle unmount, hidden Tabs, route changes and rapid reentry; prioritize actual object identity and usability.
- Respect live changes in `prefers-reduced-motion` and user-selected reduced/no motion. Remove unnecessary displacement/loops while retaining business state and unmistakable feedback.
- Avoid broad layout thrash, full-screen blur, heavy filters and permanent compositor layers. Choose compositable properties when appropriate and measure on the real devices/viewports. Without evidence, **do not claim 60fps, zero CLS or zero memory growth**.
- Users must be able to cancel, repeat or reverse during transitions. Visible focus, keyboard paths and text contrast must remain sound.

## Gate MC7 — Independent fresh-eye visual review

- After complex or signature motion, ask a reviewer to evaluate **without first reading the implementer's rationale**. Supply only a concise user task, target viewport, actual recording/frame evidence, operable page and previously approved constraints. This prevents author explanations from hiding obvious visual defects.
- Review in order: **composition/recognizability → state continuity/timing → typography/icon pixel craft → interaction/reduced-motion**. Each issue needs an exact frame or reproduction step, not an abstract “lacks premium feel” verdict.
- Inspect changing label lengths, local masks, dialog anchors and animated text at actual display dimensions; magnify when needed for clipping, final-frame jitter and ghosting, but also watch at normal playback speed.
- The independent reviewer raises evidenced problems; the implementer repairs and recaptures. Without an independent reviewer, report `NOT REVIEWED`, never convert automated smoke success into an aesthetic sign-off.

## Common rejection criteria

1. Only a page-wide fade was added but all component motion was declared complete.
2. Menu/Tooltip/Dialog loses spatial connection to its trigger or drifts on open/close.
3. Neighbor list/content jumps without reasonable continuity, or a deletion/filter leads to incorrect data.
4. Button/text/icon shows ghosting, jank, cropping, replacement identity or lost focus across a state change.
5. A mid-transition repeat jumps to the original start; hidden/background animation leaks resources indefinitely.
6. Nonstop loops, identical Card float effects, uniform Button bounce or other motion without causal value.
7. Reduced-motion mode hides important content or changes the outcome; animation fakes progress/success.
8. Only static screenshots or synthetic demos were tested, with no real before/during/after interaction verification.

After implementation, execute [Motion Rehearsal](motion-rehearsal-and-evidence.md). External credits and sources remain in README.
