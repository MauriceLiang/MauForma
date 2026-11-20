# Expressive Motion Vocabulary — Curated Effects & Creative Composition

**When to load:** Expressive/premium product websites, portfolios, immersive stories, original visual directions delegated to the Agent, or a request naming a motion effect. **Do not load for every bug fix**. This expands existing craft, choreography, engine-selection and rehearsal guidance without making all effects mandatory.

**Position:** MauForma should expand the Agent's creative vocabulary, not merely warn it away from bold effects. On authorized creative briefs, **propose distinctive motion ideas proactively** based on the real subject. Do not wait for the user to know technical motion names. These are conceptual design names, NOT necessarily official methods in a library. Keep existing assets/motion-effects.json recipes and use IDs to connect ideas to implementations.

## 1. The 22 curated effect terms

“Basic entrance” is counted as one family, although fade/slide/zoom are separate motions. The video’s headline count does not define a hard catalog limit. Sample 300ms and 80ms intervals are illustrations, not universal rules.

| English / 中文 | What to ask the Agent to create | Current MauForma entry / extension | Best-fit and caution |
| --- | --- | --- | --- |
| **Easing 缓动** | Meaningful acceleration, deceleration and settling; tune movement according to action and mass | Existing `animejs-easing-complete.md` and motion craft | Every designed transition; not “ease-out everywhere” |
| **Spring 弹簧** | Tactile press/release with damping, short overshoot and immediate response | **New** `spring-feedback`; distinct from drag-only `spring-release` | Buttons, keys and toggles; avoid business-table bounce |
| **Basic entrance 基础入场** | Fade / slide / scale from a believable source in small doses | Existing `fade-in` / `slide-left` / `zoom-in` | Basic polish, but not the only signature of a brand |
| **Line reveal 按行显现** | Hero lines rise independently while accessible full text remains readable | Existing `line-reveal` | Short hero headings, not long operating instructions |
| **Stagger 交错出现** | Related sibling elements enter in purposeful reading order | Existing `sequential-cards` / `stagger-scroll` | Limited groups; avoid hundreds of list rows |
| **Blur reveal 模糊显现** | Brief focus-like transition from mild blur to sharp content | Existing `blur-reveal` | Media-driven hero; avoid body reading blur |
| **Mask/clip reveal 裁切揭示** | Image, headline or object uncovered through a controlled wipe/crop | Existing `clip-reveal` / `mask-wipe` | Key product moment; content remains accessible |
| **Text shimmer 文字流光** | One bounded beam glides across a short label, then rests | **New** `text-shimmer`; NOT `skeleton-shimmer` | Launch badge; not continuously scanning all headings |
| **Character reveal 字符显现** | Logo/word letters arrive sequentially, with correct CJK handling | Existing `char-reveal` | Short name or phrase; preserve semantics |
| **Scramble text 乱码解码** | Predefined decorative characters resolve to a truthful final string | Existing `text-scramble` | A fictional technology title; never fake real values |
| **Text morphing 文字变形** | Short words visually transform with stable width and atomic accessible label | **New** `text-morph`; NOT `svg-morph` | Brand vocabulary / concept words, not data tables |
| **Typewriter 打字机** | Typed characters and optional *clearly simulated* physical-key feedback | Existing `typewriter` / `cursor-blink` | Short demo; do not delay real user input |
| **Smooth scroll 平滑滚动** | Gentle *intentional anchor* navigation, without taking over wheel/touch scroll | **New** `smooth-scroll` | Chapter/anchor jumps; native behavior preferred |
| **Scroll-triggered 滚动触发** | One finite timed entrance when element becomes visible | Existing `scroll-reveal` | Below-fold introduction; not linked to every pixel |
| **Scroll-linked 跟随滚动** | Progress tracks the scroll position continuously in both directions | Existing `scroll-scrub` / `scroll-progress` | Real product inspection / reading progress |
| **Parallax 视差** | Two or three content planes move at differing scroll speeds | Existing `parallax` | Depth on artistic hero; no form foreground drift |
| **Sticky scrollytelling 固定滚动叙事** | A product object remains pinned while facts/stages change | Existing `sticky-stage` | Multi-step product story with safe exit and focus |
| **Scroll zoom 滚动缩放** | Scrub toward a macro feature then out, preserve object location and crop | **New** `scroll-zoom` | Detail inspection; no violent full-screen scaling |
| **Image sequence 图片序列** | Pre-rendered frames follow scroll; static poster and streaming budget | **New** `image-sequence` | Hardware rotation where assets exist; memory-costly |
| **Horizontal scroll 横向滚动** | Real user-driven sideways variant gallery, not merely a horizontal reveal | **New** `horizontal-scroll`; NOT `horizontal-reveal` | Editions, artworks, version cards |
| **Scroll snap 滚动吸附** | Settle naturally to an item after direct scroll/swipe | **New** `scroll-snap`; NOT `scroll-snap-feedback` | Version galleries; no force-jump traps |
| **Marquee 跑马灯** | Seamless brand/review strip with pause and static fallback | **New** `marquee` | Social proof; no false endorsements |

**Distinctions that matter:** Scroll-triggered is time-based after a trigger; scroll-linked is progress-based and reversible. Text shimmer is NOT loading shimmer. Text morph is a typography transition, not SVG shape morph. Horizontal scroll must remain usable by touch, pointer and keyboard. Scroll snap is the actual landing behavior, not just the indicator animation. Easing/Spring are motion physics; stagger is a timing relationship.

## 2. Creativity-first motion design workflow

1. **Find the subject's personality.** What makes this particular artifact or product recognizable? Think tactile key travel, lens focus, folding paper, fine machining, elastic fabric, evolving data relationships, color mixing, slow camera inspection. Avoid generic “AI-tech neon”.
2. **Sketch two or three different directions** for new products or major redesigns: a bold cinematic direction, an editorial typographic direction and an interaction-driven exploratory direction are examples, not fixed presets. Describe the first still frame, signature moment, controls, cost and user fit. Honor existing approved direction; a small fix needs none of this.
3. **Choose a signature motion** that *reveals an actual insight*, not an arbitrary flourish. Then support it with typography, modest entrance rhythm and tactile real controls. Starting heuristic: **one signature + one or two supporting mechanisms + real state feedback**. A sophisticated authorized piece can use more; never set a universal effect quota.
4. **Storyboard causality:** starting image → user scrolls/clicks → one part transforms/reveals → neighboring content responds → stable payoff → reverses or exits. If an effect does not communicate the product or guide the task, reconsider its role.
5. **Compose the effects deliberately.** Do not play every selected motion at once. Use distinct movement, anticipation, overlap, hold and payoff with readable static frames. 0.3s/0.08s are examples; tune time by travel distance, reading pace and interactivity.
6. **Build and evaluate:** Actual content + original/authorized assets, available framework and users' motion preferences first; then captured browser animation at real playback speed. Rework mismatched rhythm/anchors rather than just adding a new effect.

A premium site **can be cinematic**. MauForma's restraint policy is about preserving product intent, not suppressing creative expression.

## 3. Compositions to invent from (not brand-copy templates)

### A. Mechanical / industrial product

**Scene:** First frame is a strong real product silhouette, not an empty canvas. A short line-reveal heading makes the subject legible. One highlight mask reveals a physical assembly. A scroll-linked zoom or *asset-backed* image sequence exposes the machining/keys. User controls versions via horizontal scroll, snap and a tactile spring. Price/specs update from **real product data**.

**Agent-oriented creative prompt:** “Create a hardware hero with distinct mechanical character. Use a line reveal to introduce one promise, then a scroll-linked macro inspection of the actual mechanism. Make the edition chooser feel like a tactile physical control, while preserving real information and keyboard navigation.”

### B. Experimental portfolio / editorial narrative

**Scene:** One distinctive editorial type composition, short character reveal, then a masked project image passes into a detail surface; mild parallax separates subject from environment. An optional brief text morph changes the central idea, **not** the navigation label. Section progress may be linked to scroll; project entrances trigger only once.

**Agent-oriented creative prompt:** “Give this portfolio a graphic-editorial first frame. Invent one recognizable text transition and an image reveal that feel related to the artist's subject. Keep work visible after settling and maintain a fast route back to the index.”

### C. Product editions / comparison

**Scene:** Featured media arrives softly. Sideways gallery is genuinely scrollable, snaps to a version and carries selected identity across image, real specs and CTA. Short spring feedback expresses selection; layout and labels stay anchored. If motion preference is reduced, selection and facts still update instantly.

**Agent-oriented creative prompt:** “Compose a product edition strip with native horizontal scrolling, useful snap positions, and a continuous selected indicator. The gallery, comparison and CTA must agree on the same real edition.”

### D. Launch / social proof

**Scene:** A subtle shimmer appears **once** on a truthful new-release label; limited headline stagger establishes hierarchy. Supporting brands or real reviews may move in a slow marquee only when paused/readable on interaction, with a static alternative. The main call to action never depends on the loop.

**Agent-oriented creative prompt:** “Build a confident launch page with one elegant highlight and a readable social-proof rhythm. Make all testimonial content inspectable and never fabricate credibility.”

### E. Interactive documentation / education

**Scene:** Real headings and instructions are visible before motion. A scroll-linked progress bar shows position; sticky diagram changes next to explanatory chapters. Triggered figure captions introduce ideas once. Explicit chapter-link clicks may scroll smoothly; a user can always use normal scroll and back navigation.

### F. Desktop productivity / developer workspace

**Scene:** Express craftsmanship through accurate micro-motion: anchored menu origins, control press and a smoothly traveling selection indicator; content swaps preserve identity. An onboarding showcase may use typewriter or a concise reveal if explicitly appropriate. Do not force parallax or sticky stories on high-frequency operations.

## 4. Engineering, accessibility and performance boundaries

- **Source availability:** Image sequences require actual rights and a realistic frame set, or use a still image / limited CSS transform instead. Preload a small directional window, release old frames, measure decode cost and memory. Do not auto-download hundreds of assets.
- **Rendering:** Prefer compositable transforms/opacity for frequent changes when feasible. Filter blur, masks, animated gradients and canvas images can have paint/decode costs. Verify on target devices; do not claim 60 fps or “lightweight” without evidence.
- **Scrolling:** Use CSS sticky, native scroll-snap, overflow-x and native anchors first. Progressive enhancement may use Scroll-driven Animations where supported, IntersectionObserver, existing Motion/Anime.js or GSAP as appropriate. Never hijack wheel/touch just to simulate “smooth inertia”.
- **Text:** Split line/character effects must preserve screen-reader meaning and correctly remeasure on font load/resize/localization. No permanently hidden hero when JS fails. Use one stable accessible label for text morph; changes should be announced appropriately if semantic.
- **Infinite loops:** Marquee/trust strips need pause, clipping without keyboard traps, no duplicate focus targets, and static reduced-motion fallback. Autoplay should not prevent reading.
- **Transitions:** Reverse/interrupt at mid-scroll, resize, tab switch, and quick edition changes; clean listeners, observers, rAF and animations. Disabled / reduced motion preserves state, content and controls.
- **Evidence:** An isolated motion demo is DEMO ONLY. Check real product routes and actual API outcomes separately. See `motion-rehearsal-and-evidence.md`; `CAPTURED_FOR_REVIEW` is not aesthetic or functionality verification.

### Suggested implementation mapping

| Desired motion | Start with | Escalate only if needed |
| --- | --- | --- |
| Tactile press, short spring and entrance | Existing CSS/WAAPI/installed UI transition tools | Motion spring or Anime.js timeline |
| Title/word reveals and shape masks | Native text + CSS clip/transform, stable accessibility | Supported text splitter and choreography library |
| Scroll-trigger once | IntersectionObserver or applicable supported CSS triggers | Existing scroll integration |
| Scroll-linked and zoom | Native sticky / CSS Scroll-driven Animations with feature detection | Motion scroll or GSAP ScrollTrigger |
| Image sequence | Asset loading plan and static poster first | Controlled canvas/image decode and cached frame map |
| Horizontal, snap and anchor scroll | CSS overflow, scroll-snap and scroll-behavior | JS only for real state sync |
| Marquee and shimmer | Pausable bounded CSS + reduced-motion | Higher-level timeline if needed |

Official references: [MDN CSS Scroll-driven Animations](https://developer.mozilla.org/en-US/docs/Web/CSS/Guides/Scroll-driven_animations), [MDN Scroll Snap](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS_scroll_snap), [Motion Scroll](https://motion.dev/docs/react-use-scroll), [Web.dev animation performance](https://web.dev/articles/animations-guide), [Web.dev reduced motion](https://web.dev/articles/prefers-reduced-motion). Check current API/browser support in the actual project.

## 5. Related MauForma references

`assets/motion-effects.json` is the searchable extended recipe catalog. `animejs-motion-recipes.md` documents earlier families and examples; the IDs are **MauForma names, not necessarily official Anime.js API identifiers**. Use `motion-craft-and-continuity.md` for causal continuity, `component-motion-choreography-gate.md` for real controls, `animation-engine-selection.md` for choosing technology, and `motion-rehearsal-and-evidence.md` for genuine frame review. Do not preload all of these just because you opened this guide.
