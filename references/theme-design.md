> v4 scope notice: MauForma directly targets **Web frontends**. A few historical SwiftUI/AppKit items transfer only design semantics; they do not instruct the Agent to install or generate native UI code.

# Theme Design — Creative Freedom With Coherent Roles

## 1. What stays consistent, and what can vary?

**Semantic relationships are fixed; blue/purple/pink choices are not.** The useful part of a polished reference is its coordination of neutral colors, readable type, whitespace, radius hierarchy, quiet shadows and motion—not one HEX on a heading.

- **Candidates may vary:** Brand/accent colors, whether and where gradients exist, cool/warm tone, subtle page background hues, dark theme, illustration/icon direction. Actually adopt only a **confirmed, explicitly delegated or soundly inherited** choice; an Agent recommendation is not approval.
- **Must remain consistent:** Semantic color roles, contrast, component states, hierarchy, spacing/radius scales, Button semantics, keyboard focus and status-color meaning. One product shares a token system across its pages.
- **Prohibited:** Arbitrary pink primary Button on one route, green on another, blue in a dialog solely because each looked attractive. Multi-theme support must use a centralized mechanism.

## 2. Theme decision workflow

1. Establish product type (admin, SSH tool, content product), emotional direction (calm/warm/playful/serious) and usage frequency (long daily sessions vs occasional showcase).
2. Build a **low-saturation neutral base**. In light mode, page background, main surface and soft surface are nearby but distinguishable. Dark-mode values need their own deliberate selection—not a simple inversion of white.
3. **Respect any user-selected primary color first.** If color remains undecided, present 2–3 coherent full-page palette candidates for choice rather than silently imposing dark blue or any default. Map the selected accent to meaningful UI roles. Neighboring/complementary colors may be proposed, **not** distributed as mandatory ornament. Success/warning/error are independent from brand accent.
4. Define roles such as `accent`, `on-accent`, `focus`, `text`, `text-soft`, `text-muted`, `control-border`, `surface`, `surface-soft`, `page-bg`, `success/warning/danger`.
5. Test readable text and meaningful control edges **on each real background**. Preview hover, pressed, focus, disabled and loading; adjust luminance/saturation as needed.
6. Inspect dark mode separately. Accents often require adjusted luminance; shadows cannot be the only separator; light-theme white-on-accent assumptions may fail.
7. Compare screenshots: Is the reading path clear? Does theme color overpower content? Does this design need a gradient at all?

## 3. Six editable starting palettes

| Theme ID | Direction | Light accent | May fit |
| --- | --- | --- | --- |
| `ocean` | Clear blue | `#175CD3` | Reliable system/developer tools |
| `forest` | Misty pine green | `#147D64` | Calm creator tools |
| `copper` | Warm terracotta | `#A14B20` | Editorial content and brand work |
| `violet` | Twilight violet | `#6941C6` | Expressive workspaces |
| `slate` | Graphite gray | `#344054` | Dense developer tools and restraint |
| `rose` | Deep rose | `#B42349` | Energetic without excessive sweetness |

These are **structurally valid examples, not the only six allowed themes**. If creating a seventh, save it in `theme-presets.json` or the actual project's shared theme configuration, not scattered page CSS.

## 4. Accent and gradients

**Good:** `--spui-accent` governs important Buttons, usable links, focus and selection. A decorative gradient can be limited to a Hero, data-specific chart usage or onboarding moment when contrast remains sufficient. Marketing pages may use **no gradients at all**. Gradient colors should share a coherent palette logic rather than jumping among three unrelated saturated hues.

**Bad:** Blue buttons, pink badges, green navigation, purple dialog and random orange-red charts; white body text on a pale pink→yellow gradient; gradient body text; or wall-to-wall saturated backgrounds that tire readers.

## 5. Contrast — WCAG 2.2 AA baseline

- Ordinary text against its **actual** background: **at least 4.5:1**. Qualifying large text: **3:1**.
- Meaningful UI boundaries/icons/status visuals: typically **at least 3:1** under applicable standards. Purely decorative borders may be exempt but cannot be the only accessibility cue.
- Disabled must not become an indistinguishable “disappeared” state; distinguish disabled from pending.
- Focus indicators need to be clearly visible and not clipped by overflow/shadows. Contrast-test colored rings on their real backgrounds.
- `scripts/validate_design_system.py` only checks **numeric relationships in the palette**; it does not test actual DOM, overlays, opacity, font size, animation or complete WCAG conformance.

Standard: https://www.w3.org/TR/WCAG22/

## 6. CSS integration

```html
<link rel="stylesheet" href="themes.css">
<link rel="stylesheet" href="desktop-tokens.css">
<link rel="stylesheet" href="components.css">
<div class="spui spui--desktop" data-theme="forest" data-scheme="light">
  <!-- components and business screens -->
</div>
```

Switch theme via root `data-theme`; switch light/dark via `data-scheme`. Components use semantic references like `var(--spui-accent)`, **not** hard-coded “green theme” constants.

## 7. Integrate with inherited theme architecture

If the app already uses Tailwind CSS variables, CSS Modules, UnoCSS, themed Reka wrappers or SwiftUI Color assets, map the **semantic roles** to its existing system. The invariant is **one source of truth + component reuse + verifiability**, not specific stylesheet filenames.

## 8. Sidebar semantic color scale and color quality (v6.3)

Dark navigation should not become “navy background + three inconsistent blues + orange dots.” Choose a coherent neutral hierarchy: **navigation canvas → soft surface → hover → selected**, then map primary/secondary labels, icons, focus, edges and accents. Neutral and blue-gray may coexist when they have clear roles. Warning/failure/unread status colors remain distinct from brand accent. Orange dots represent **real states only**, with visible labels/text as appropriate.

See two **non-mandatory** light/dark examples at `assets/sidebar-palette-examples.json` and color-contrast checks in `scripts/validate_ui_patterns.py`. This does not verify translucent overlays, screenshot pixels, image intersections, actual focus shapes or artistic color quality. Test in the real browser. A sidebar selection rail is appropriate only when it communicates a genuine chapter/timeline/hierarchy role or separately justified information, **not universally right or wrong**. See [Sidebar Navigation](sidebar-navigation-design.md).

## 9. v6.6 — Sidebar + Main is one coordinated user color decision

For new projects or major redesigns, first inspect `references/sidebar-color-discovery.md`, existing user color decisions, brand and the **actual main-content background**. Preview Sidebar, Topbar, Main, Panel and Chart **together**. The sidebar may be materially darker or lighter with a justified hierarchy, but `--sidebar-primary` must not silently replace a global brand accent without authorization. Keep a user-specified HEX exactly; when contrast fails, first adjust surrounding text/surfaces and discuss necessary design decisions.

Old `assets/sidebar-palette-examples.json` shows state relationships; it is **not permission for Agent-default blue-gray sidebars**. `assets/sidebar-color-directions.json` includes five original full-page directions, but usually present 2–3 relevant options. Actual approval/provenance follows `assets/sidebar-color-decision.schema.json`; `pending` is **not** approved.
