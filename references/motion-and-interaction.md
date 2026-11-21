# Motion and Interaction Standards — v3.0 Entry Point

**Not limited to admin products:** Showcase sites may use richer motion, while editors, workspaces and desktop tools prioritize simple, fast and interruptible behavior.

Read selectively when relevant:

- [motion-governance.md](motion-governance.md) — when to animate, timing, risk, performance and reduced motion.
- [animejs-official-capabilities.md](animejs-official-capabilities.md) — major official Anime.js v4 APIs.
- [animejs-easing-complete.md](animejs-easing-complete.md) — 45 built-in easing names and custom generators.
- [animejs-motion-recipes.md](animejs-motion-recipes.md) — original 114 recipes; expanded catalog of **123** at `assets/motion-effects.json`.
- [animejs-v4-snippets.md](../examples/animejs-v4-snippets.md) — 16 code examples.
- [motion-gallery.html](../assets/motion-gallery.html) — searchable/filterable/playable gallery of 123 recipes; see [expressive-motion-vocabulary.md](expressive-motion-vocabulary.md) for 22 curated expressive concepts.

The historical entrypoint repeated this identical reading list; repetition does not change any rules.

## Historic reference-site observations — inspiration, not mandatory defaults

- Card entrance: opacity 0→1, translateY 24→0, 120ms stagger between siblings, 700ms duration, Anime.js `outBack`.
- Button/link hover: opacity 0.86 over 200ms.
- The source used CDN Anime.js, and components might remain hidden if scripts failed. **Never inherit that defect into production.**

## Motion intensity by context

| Context | Suggested | Not recommended |
| --- | --- | --- |
| Initial showcase entrance | Subtle 8–24px move + fade, 450–700ms with limited stagger | Cards flying in from outside the screen |
| Ordinary controls | 120–240ms background/border/opacity transition | Scaling, spinning or bouncing every hover |
| Frequent desktop-tool operations | 120–180ms, immediate feedback first | Elastic easing on terminal/tree/list scroll |
| Save, error and loading | Clear actual text/state with complete pending feedback | Only a sparkle/spinner without a usable result |
| Navigation | Stable switch or small transition | Replaying every entrance animation on each route |

## Implementation rules

- Explain **state change** or **spatial relationship**, not spectacle alone.
- Prefer appropriate compositable properties such as opacity/transform/color; avoid frequent layout recomputation and heavy blur.
- **Core content is visible by default:** Never rely on `.card { opacity:0 }` and an animation script as the only path to visibility.
- Use `:focus-visible` with `var(--spui-focus)`; never copy the reference's literal `#0071e3` into every theme.
- Under `@media (prefers-reduced-motion: reduce)`, remove nonessential movement/loops while preserving clear state feedback.
- Vue Transition, Motion and Anime.js are options according to the inherited stack; ordinary hover normally needs only CSS.

```css
.ui-interactive {
  transition: background-color var(--spui-motion-ui) ease-out,
              border-color var(--spui-motion-ui) ease-out,
              opacity var(--spui-motion-ui) ease-out;
}
.ui-interactive:focus-visible {outline: 3px solid var(--spui-focus);outline-offset:3px;}
@media (prefers-reduced-motion: reduce) {
  .ui-interactive {transition-duration: .01ms;}
}
```

**Check:** Can rapid button presses trigger duplicate actions? Can dialogs close promptly? Is layout stable with motion off? Does dark mode or a narrow window flicker?
