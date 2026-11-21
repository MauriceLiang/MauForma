# Motion Rehearsal & Evidence — Frame-by-Frame Quality Gate

> Apply the **capture → inspect → fix → recapture** loop to the **real product**. Static audits, screenshot counts and automated metrics cannot replace human visual judgment. Combine with motion-craft-and-continuity.md, browser-qa-protocol.md and visual-qa.md.

## Presentation storyboards versus real product verification (B05/B10)

Promotional animation may use **poster-first** communication (the initial still frame already conveys its core value), finite narrative beats, seamless loops and camera choreography. These techniques matter **only** when the user's task involves product marketing, animated illustration or showcasing creative work. Real business controls, state changes, persistence, permissions and error recovery must **separately** be verified on the actual page/backend. Simulated cursors and demo-only states cannot count as end-to-end business evidence. Even when browser frame capture reports no errors, its outcome is only **CAPTURED_FOR_REVIEW**, not a pass for visual quality or fluidity.

## Gate MR0 — Identify what is tested; separate demo from product

- Test only high-value interactions that **actually exist** in the user's product and fall within the current scope. Do not add imaginary buttons to fill the test scenario.
- Before running, record **url / route / data fixture / viewport / device scale / theme / locale / reduced-motion / interaction**. Stable test fixtures must be labeled as fixtures; a mocked backend response cannot be called a real save.
- For significant changed interactions, prepare **before → trigger → during → settled → reverse/interrupted → reduced**. This is **not** an order to record twenty frames for every tiny hover effect.

## Gate MR1 — Layered verification, not one screenshot

1. **Static first/final frames:** Inspect the delivered dimensions for both first and settled frames. If hierarchy, controls, Chinese line wrapping, alignment, focus, icons or Card boundaries are wrong, repair layout before motion.
2. **Sample meaningful beats:** Sample start / 25% / 50% / 75% / end for major transitions. For short entrances/exits and suspected jumps, increase sampling to **40–80 ms** intervals. Record the achieved sampling cadence and screenshot overhead. If the intended cadence was not achieved, label **INCONCLUSIVE**, not PASS.
3. **Replay at real speed:** A contact sheet alone cannot reveal momentary flicker, frame stutter or awkward easing. Watch actual **1× playback** and then inspect suspicious intervals in slow motion.
4. **Interrupt and reverse:** Trigger again near **30% and 70%**, reverse, press Escape or change route. Motion must continue from current rendered geometry, and focus/business state must survive.
5. **Dynamic range:** Cover actual supported desktop sizes and narrow/mobile if relevant, light/dark theme, **200% font scaling**, long Chinese/English labels, first load and steady state. A desktop-only product does not need new mobile support, but its smallest supported viewport must be tested.
6. **System preferences:** Toggle prefers-reduced-motion before and during a transition. Business outcomes must remain the same while motion reduces. Verify accessible names, focus and status feedback.
7. **Loop/long-running states:** For automatic promotional loops only, inspect a full loop plus the start of the next cycle, reset logic and tab hide/resume. Do not introduce loops into ordinary business controls just to test them.
8. **Product execution:** Capture the actual route using the actual product's CSS/JS version and real element selectors. A different demo and the target product **cannot substitute for each other's acceptance**.
9. **Independent review:** For expressive or important motion, prefer a reviewer who did not implement it. Provide only the user task, inherited design constraints and actual captured frames/video—not the author's own quality judgment. Tie each issue to evidence frames and reproduction steps. If independent review was not possible, report it.

## Gate MR2 — Symptoms and repair actions

| Observed issue | Inspect first | Corrective direction |
| --- | --- | --- |
| Abrupt appearing/disappearing | Mount/unmount, display, first keyframe | Coherent enter/exit and node preservation; immediate feedback if justified |
| Position jump / neighbor teleport | Layout/reflow, key identity, measurement timing | Shared position transitions, FLIP, placeholders and synchronized neighbors |
| Text shakes in final frame | Font loading, width collapsing, transform-layer cleanup | Stable layout constraints, animate only necessary substrings, inspect pixels |
| Container opens empty then fills | Data and animation timelines | Reveal readable content with the container; loading must reflect actual state |
| Popover drifts while opening | Anchor, positioning updates, content height | Stable anchors, recompute position and choose correct direction |
| Click receives delayed feedback | Delay, queued animations, network dependency | Pressed/focus feedback immediately; results may follow later |
| Rapid reversal stutters | Stale targets/timers and overlapping animations | Cancel/retarget, clean stale work, continue from current geometry |
| Blur / illegible text | Enlarged body text, filters, broad transform | Animate container/layout, preserve crisp readable text |
| Needless repeat entrances | Rerender or data refresh restarting entry animation | Distinguish first mount from subsequent updates; bound effect frequency |
| Reduced-motion path is unusable | Missing nonanimated path or animation-only CSS visibility | Keep final DOM/ARIA state synchronized and fully usable without movement |

For each anomaly, record **evidence → hypothesis → fix → recapture**. After a motion repair, recapture the **entire actual interaction**, not only a pre-fix frame.

## Gate MR3 — Executable sampling approach, framework-independent

Recommended script: scripts/motion_rehearsal.mjs. Provide the local running URL, scenario JSON and viewport. It begins page-local **requestAnimationFrame and pointer-event sampling BEFORE triggering the action**, captures before/during/after frames in parallel, and reports candidate geometric jumps, sample intervals and contact sheets. Optional --video supplies normal-speed playback evidence. The script **does not modify the page, silently install Playwright/browser dependencies, or certify visual aesthetics**.

~~~bash
node scripts/motion_rehearsal.mjs \
  --url http://localhost:3000 \
  --scenario assets/motion-rehearsal-scenario.example.json \
  --out ./artifacts/motion-review
~~~

The example data-motion-demo selector illustrates the scenario format; **replace it with actual DOM selectors** for the target product. Ensure the development server and Playwright browser already exist before testing. Report outputs of INCONCLUSIVE, NOT_RUN or errors cannot be relabeled VERIFIED. **CAPTURED_FOR_REVIEW only means frames were collected**, not quality approval. A fixed reference can be described through anchor and anchorTolerancePx; allowSnap applies only to explicitly legitimate instantaneous state changes.

The repository provides a newly authored **Motion Continuity Lab** at assets/motion-continuity-lab.html and executable scenario assets/motion-continuity-lab.scenario.json for learning real click/disclosure/state sampling:

~~~bash
python3 -m http.server 8000
node scripts/motion_rehearsal.mjs \
  --url http://127.0.0.1:8000/assets/motion-continuity-lab.html \
  --scenario assets/motion-continuity-lab.scenario.json \
  --out ./artifacts/motion-lab
~~~

The demo is **entirely synthetic** with no real backend requests; its outcome is **DEMO ONLY**. When adapting the scenario to a business product, change selectors, route and target viewport to the actual product.

Recommended per-scenario evidence files: scenario.json, before.png, frame-*.png, settled.png, contact-sheet.html and report.json containing requestAnimationFrame sampling and issue candidates. Automation captures evidence and possible runtime failures; qualitative assessment requires actual image and normal-speed replay.

## Gate MR4 — Outcome levels and delivery

- **VERIFIED:** Actual target page executed at an explicit browser/viewport; real observation confirmed representative frames and full playback; at least one interruption/reverse, reduced-motion and smallest supported size were checked. Independent fresh-eye critique must be recorded separately; VERIFIED alone **does not** imply independent aesthetics review.
- **PARTIAL / INCONCLUSIVE:** Missing frames, excessive sample gaps, unstable reproduction, invisible target or uncovered state combinations. List exactly what remains unverified; never claim PASS.
- **DEMO ONLY:** Synthetic animation lab ran, target product not rechecked.
- **STATIC CHECK:** Code/design contract inspected without runtime motion evidence.
- **BLOCKED / NOT TESTED:** Browser/server/operable environment unavailable, or test was not run.

Minimum delivery summary:

~~~md
### Motion Rehearsal
- Scope: <actual interaction and route>
- Decision: <user-confirmed intensity/provenance or inherited policy>
- Story: <trigger, spatial relationship, settlement, reversal, reduced motion>
- Captured: <URL, browser, viewport, theme, steps and files>
- Findings → fixes → recapture: <actual evidence>
- Reduced motion / interruption / focus: <results>
- Independent review: <reviewer, evidence and issues; or NOT REVIEWED>
- Status: VERIFIED | PARTIAL | DEMO ONLY | STATIC CHECK | NOT TESTED | BLOCKED
- Unverified: <untested environments and reasons>
~~~

**An automated "no anomalies found" is not aesthetic approval, and random screenshots cannot prove fluidity.** Prefer measuring real-device FPS/long tasks, layout shifts, GPU/memory cost; never claim unmeasured metrics are within budget.

This tool/report targets real products across frameworks. Promotional demo choreography must not be passed off as verified business interactions. Open-source credits and upstream references remain in repository README.
