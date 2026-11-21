# Creative Interaction Component Sources — React Bits / Vue Bits / Inspira UI / Magic UI / Aceternity UI

> **Verified as of 2026-11-02.** These are **optional creative building blocks**, **not required dependencies**. Version, props, license, pricing and indirect dependencies must be checked against each component's official details and repository version. Online catalogs change: examples below are a **curated set of known capabilities, not an exhaustive live catalog**.

## v6.15 — Creative motion belongs inside components, not only the Hero

See component-motion-choreography-gate.md. Inventory **actual high-value interactions** first: selected indicators, disclosure, state shape changes, layout and content continuity. Only then ask whether React Bits/Vue Bits/Inspira/Magic UI/Aceternity provides an **appropriately scoped individual implementation**. This does not require animated backgrounds on enterprise dashboards or 3D hovering on every Card. Promotional and portfolio sites can justify a few strong moments; routine work values tactile, spatial and outcome feedback. Brand craft is more than one page-level fade.

## 0. Distinguish three layers

- **Functional UI:** Button, Select, Dialog, Form, Table, DatePicker, Tabs, Menu. Must correctly implement focus, keyboard, ARIA, data and states using the project's mature library or accessible primitives. **Never replace with a creative effect component.**
- **Creative UI:** Animated background, text reveal, 3D Card, spotlight, cursor trail and scrollytelling. Most appropriate to product/brand/portfolio/editorial experiences. May selectively enhance onboarding/empty states, not displace the operating workspace.
- **Motion engine:** CSS, Motion, Anime.js, GSAP, WebGL are underlying implementation mechanisms **not themselves complete UI component collections**. A copied effect may **already depend on GSAP/OGL/Motion**; inspect dependencies and avoid duplicate or competing engines.

## 1. Library comparison

| Library | Official | Framework/source type | Typical content | Strong fit | Risk/limits |
| --- | --- | --- | --- | --- | --- |
| **React Bits, free portion** | https://reactbits.dev/ | React/Next; copy source or CLI; TS/JS + CSS/Tailwind | Text animations, backgrounds, other effects, Cards, micro-interactions | Brand Hero, product feature display, portfolio | Some effects use WebGL/GSAP/OGL; check component-specific performance and SSR |
| **React Bits Pro** | https://pro.reactbits.dev/ | React, commercial assets and distinct entitlement tiers | More components, page Blocks, templates, application UI | Budgeted promotions where they actually add value | **Paid: do not copy Pro assets as though they were free.** |
| **Vue Bits** | https://vue-bits.dev/ | Vue 3 + TypeScript + Tailwind, copied Vue components or CLI | Official Vue port of React Bits: text, backgrounds, mouse, Cards, motion | Vue/Nuxt product sites and portfolios | Extra dependencies, SSR/hydration risk; verify the **actual component/repository license** |
| **Inspira UI** | https://inspira-ui.com/docs/ | Vue/Nuxt copyable components, often shadcn-vue, motion-v and Tailwind | Backgrounds, Cards, typography, interactions, visualizations | Vue business sites, AI promotional pages and Heroes | **Not a substitute foundational UI library or Reka interaction engine.** Check dependencies/licenses per item |
| **Magic UI** | https://magicui.design/ | React/Next, Tailwind/Motion depending on specific component | Animated text, decorative backgrounds and promotional components | Restrained brand/marketing motion | A project with a mature primary library need not switch entirely to shadcn |
| **Aceternity UI** | https://ui.aceternity.com/components | React/Next, Tailwind/Motion | 3D Cards, Aurora, spotlight, backgrounds, scroll stories | Bold landing pages and first-screen moments | Distinguish free components from paid Blocks/templates and preserve architectural constraints |

**Framework rule:** React Bits TSX cannot be used directly in Vue, and Vue Bits SFCs cannot run as React components. Find a native equivalent for the active framework or recreate the visual mechanism using that framework's supported APIs.

## 2. React Bits — what named effects do and when to use them

Official catalog: https://reactbits.dev/ ; text: https://reactbits.dev/c/text-animations ; animations: https://reactbits.dev/c/animations ; backgrounds: https://reactbits.dev/c/backgrounds. Names in the tables are catalog names; guidance is MauForma's **selection interpretation**, not claims that the effects are mandatory.

### 2.1 Text/headlines for brand and product introductions

| Component | Perceived motion | Recommended context | Avoid |
| --- | --- | --- | --- |
| Split Text | Split characters/words, stagger entrances | One concise first-screen brand promise | Animating long body copy character by character |
| Blur Text | Text sharpens from mild defocus | Hero titles and short introductions | Low-contrast body text, time-sensitive instructions |
| Text Type | Typing with cursor rhythm | CLI demo or brand slogan excerpt | Forms, contracts, live factual content |
| Rotating Text | Phrases flip or rotate through variants | Secondary selling points | Constantly changing the only important fact |
| Shiny Text | Light glides across words | A few branded terms | Every nav item, header or numeric datum |
| Gradient Text | Soft flowing gradient | A single emphasized phrase in a visual Hero | Multiple competing saturated backgrounds |
| Decrypted Text | Random characters resolve to actual copy | Security/developer marketing narrative | Accounts, CAPTCHA and business-sensitive data |
| Scroll Reveal | Characters/content reveal with scroll | Long-form product storytelling | Breaking reading order or leaving text invisible |
| Count Up | Animate to **a true sourced number** | Real achievement KPI | Fabricated growth or not-yet-loaded numeric data |
| Glitch Text | Brief chromatic distortions | Tech event or game accents | Routine SaaS H1 or incessant loops |
| Particle Text | Particles coalesce into letters | One premium promotional reveal | Low-performance devices, every heading in a product |
| Text Pressure | Cursor-sensitive font distortion | Interactive brand tagline | Long prose and essential action labels |

### 2.2 Backgrounds and scenes, often higher-cost

| Component | Appearance | Suitable context | Risks/fallback |
| --- | --- | --- | --- |
| Aurora / Soft Aurora | Gently flowing aurora-like gradients | Marketing Hero backdrop | Light/dark contrast; static gradient fallback |
| Particles | Floating layers with pointer reactions | Portfolio/innovative product | Cap count/DPR; soften on mobile |
| Waves / Line Waves | Fine lines undulate like fabric | Supporting brand-story layer | Excess movement/vestibular comfort |
| Orb | Glowing sphere with subtle breathing | One focal product feature | Keep apart from CTA; do not obscure type |
| Liquid Chrome | Metallic liquid reflections | Technology/brand texture | GPU budget and static poster |
| Ballpit | Physically interactive 3D balls | Controlled playful creative feature | Isolated region and mobile limits |
| Letter Glitch | Flickering/deforming character matrix | Developer event background | Strong visual stimulus, not always-on workplace UI |
| Grid Distortion | Local image-grid warping | Portfolio media close-up | Preserve actual image meaning; mobile fallback |
| Lightning | Branching pointer-sensitive lightning | Game or specific event | Strong flashes; not default commercial UI |
| Beams / Light Rays | Volumetric animated light | Dark Hero depth | Reduce persistent GPU and light pollution |
| Grainient | Grainy flowing gradient | On-brand landing background | Text/contrast instability |
| Magic Rings | Pulsing rings with mouse response | Single feature panel/CTA ornament | Must not impersonate upload progress or success |

### 2.3 Cards, navigation and content

| Component | Appearance | Good fit | Caution |
| --- | --- | --- | --- |
| Spotlight Card | Pointer-following Card light | Feature or pricing highlight | Touch has no hover; retain readable static style |
| Tilted Card | Mild 3D tilt and sheen | Product imagery or special feature Card | Cap tilt and avoid misclicks/reading disruption |
| Chroma Grid | Local spotlight restores color to grayscale Cards | Project/team portfolio grid | Keep keyboard focus and touch support |
| Carousel | Switch horizontal content frames | Product-story segments | Manual control, autoplay must be pausable |
| Dock | Nearby icons magnify around pointer | Interactive desktop simulation | Do not force Dock navigation into ordinary websites |
| Gooey Nav | Liquid-like active navigation marker | Short creative navigation | Clearly indicate actual current route; keyboard accessible |
| Staggered Menu | Menu items enter in sequence | Brand/mobile menu | Closing and focus cannot wait on animation |
| Masonry | Variable-image grid smoothly rearranges | Portfolio/case collection | Image sizes, CLS and lazy loading |
| Glass Surface | Translucent, refraction-like surface | Select floating/adjacent Hero areas | Text contrast, performance and compatible fallback |
| Model Viewer | Interactive 3D product model | Physical product/hardware | 2D fallback, loading/error, user controls |

### 2.4 Generic animation and microinteraction

Animated Content (scroll reveal/blur/translation), Fade Content (fade on scroll), Electric Border (electric outline), Pixel Swap (pixel-wise change) and Cursor Grid (pointer-linked grid) appear in the official animations catalog. **Most are B/C-level expressive effects**: justify them from the actual task and do **not** apply to every operational Card by default.

## 3. Vue alternatives and adaptation map

### Vue Bits — official Vue port

Home https://vue-bits.dev/ ; install https://vue-bits.dev/get-started/installation ; repository https://github.com/DavidHDev/vue-bits . Official docs describe Vue 3 + TypeScript + Tailwind, per-component copying or CLI installation, with dependencies listed per component. Some examples use GSAP/OGL.

| Intended experience | React reference | Preferred Vue implementation |
| --- | --- | --- |
| Staggered Hero copy | React Bits Split Text | Vue Bits Split Text; check actual props |
| Light/gradient text | Shiny Text, Gradient Text | Vue Bits named equivalent or motion-v + CSS |
| Aurora background | React Bits Aurora | Vue Bits Aurora or Inspira aurora alternative |
| Spotlight product Card | React Bits Spotlight Card | Vue Bits counterpart, Inspira Card or Vue-native implementation |
| WebGL particles/liquid | React Bits Particles / Liquid Chrome | Vue Bits equivalent **if current catalog confirms it** |
| Scroll-triggered entrance | React Bits Animated Content | Vue Transition + IntersectionObserver or motion-v |
| Folded text entrance | React Bits Fold Text | Vue Bits Fold Text; separate official documentation exists |
| Complex 3D/timeline | Selected OGL/GSAP React Bits examples | Vue-native equivalent plus onMounted/onUnmounted cleanup |

**Not a one-to-one API mapping.** Import paths, props and CLI registry URLs must be copied from each corresponding Vue component's official documentation. **Do not guess Vue props from React TSX.**

### Inspira UI — independent Vue creative library

Home https://inspira-ui.com/docs/ ; getting started https://inspira-ui.com/docs/en/getting-started . Documented families include Backgrounds, Cards, Interactions, Text effects and Visualizations, with Vue/Nuxt support and common shadcn-vue/motion-v/Tailwind combinations. Strong for corporate sites, expressive Heroes, AI SaaS marketing and portfolios. Copy **only the actually justified component** into the inherited theme rather than handing the entire product skin to upstream defaults.

### Other React candidates

- **Magic UI:** https://magicui.design/ ; refined shadcn/Motion-aligned marketing text, grids, lighting and small components. Often preferable to hand-authoring a complicated branded decorative element.
- **Aceternity UI:** https://ui.aceternity.com/components ; examples include 3D Card Effect, Background Beams, Tracing Beam, Hero Parallax, Apple Cards Carousel, Animated Testimonials and Aurora Background. Appropriate for high-impact promotion; distinguish free components from paid templates/Blocks.

## 4. Context combinations — fewer deliberate effects, not maximum count

| Page type | Suggested creative layer | Required real content/behavior | Anti-pattern |
| --- | --- | --- | --- |
| Corporate home | Soft Aurora + one headline entrance | Value proposition, actual service, real contact/CTA | Four WebGL scenes simultaneously on first screen |
| SaaS landing | Sectional scroll reveal + feature-Card spotlight | Features, pricing/trial, product screenshots and credible explanations | Flashy motion replaces a real product demo |
| Developer tool website | Brief code typing demo + product UI showcase | Docs, installation, platform support | Typing forever prevents reading the actual command |
| Portfolio | Image Masonry + subtle 3D Card tilt | Filterable work, reachable detail, optimized images | Cursor effect obscures artwork |
| Careers/company | Mild team-profile entrances | Jobs, culture, location and application path | Long scroll locking and forced playback |
| Dashboard / operations | State feedback, limited entrances and light layout changes | Real Tables, fast search and authentic action states | Particle backdrops impair prolonged work |
| First-run guidance/empty state | Optional short Lottie/creative Card | Clear next action | Unstoppable animation or missing content on error |

## 5. Mandatory performance and accessibility acceptance

1. **Static content readable by default:** Hero, CTA, nav, data and body text visible when JS/CDN/effect init fails; do not permanently hide real content with opacity:0.
2. **Reduced motion:** Respect prefers-reduced-motion:reduce; cancel scroll-following glow, dizzying 3D and cursor tracking; provide static posters/gradients.
3. **Load by need:** Split creative bundles by route/section; avoid importing into the main back-office bundle. WebGL/models require a loading poster and error fallback.
4. **Low-powered devices:** Cap DPR, particle counts and Canvas instances. Slow down/stop when measured jank occurs; pause requestAnimationFrame when hidden/backgrounded.
5. **Touch/mobile:** Never rely solely on hover, keep CTA accessible, do not hijack scroll or let Canvas intercept essential gestures.
6. **Lifecycle:** React effect cleanup disposes listeners/engines/WebGL; Vue onUnmounted cleanup. Next/Nuxt SSR cannot instantiate DOM-dependent effects on the server.
7. **Semantics/keyboard:** Decorative wrappers cannot break real anchor/Button semantics. 3D Cards still need focus-visible and actual targets.
8. **User control:** Autoplay Carousels are pausable; entrance effects do not repeatedly interrupt reading; motion never changes factual business outcomes.
9. **Licenses:** Verify license for each component/font/media and commercial entitlements. "Free" on a landing site does **not mean every template, component and business-use license is identical**.
10. **Evidence:** List actual effect inventory, installed libraries, measured performance, narrow-screen/accessibility/SSR tests and unverified cases.

## 6. Selection scorecard — five criteria scored 0–2, consider only if total ≥8

- User task value: helps understanding, orientation or hierarchy?
- Brand fit: matches existing Tokens, type and palette?
- Performance/bundle: route-load only and acceptable on low-end devices/slow networks?
- Accessibility: usable without mouse; reduced motion supported?
- Maintenance: can existing components/engines achieve it more simply? Is source/dependency supportable?

**Immediate veto:** Unclear legal rights; hidden critical content; blocked primary interactions; scroll hijacking; no accessible fallback; clear frame-rate failure; or a second uncontrolled base component skin fragmenting an existing product. **A numerical 8 does not override these blockers.**

## Official references

- React Bits: https://reactbits.dev/ ; https://reactbits.dev/get-started/installation ; https://reactbits.dev/c/text-animations ; https://reactbits.dev/c/backgrounds ; https://reactbits.dev/c/animations
- Vue Bits: https://vue-bits.dev/ ; https://vue-bits.dev/get-started/installation ; https://github.com/DavidHDev/vue-bits
- Inspira UI: https://inspira-ui.com/docs/ ; https://inspira-ui.com/docs/en/getting-started
- Magic UI: https://magicui.design/
- Aceternity UI: https://ui.aceternity.com/components
