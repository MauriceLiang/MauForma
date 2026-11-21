# Component Craft Gate — A Component Is Not a Random Styled Box

This is a **cross-project, cross-framework component-design decision workflow**, not a mandatory “minimalist recipe.” Independent art directions may be editorial, playful, restrained, luxurious or experimental. Components must follow content, usage frequency, state and accessible interaction—not receive a passing grade just because they use pills and pale borders.

## v6.17 — Review icon quality together with Button/navigation composition

An icon is part of the control, not an empty space to fill after every Button/Sidebar/Menu/Table has been implemented. Apply `references/icon-art-direction-gate.md`: explain actual action/object semantics, compare real icon candidates, choose coherent outline/fill style as a group and evaluate optical weight against nearby text. Avoid similarly sized but very different visual weights, half-outline/half-filled navigation and icons overpowering labels. Icon-only Buttons need an accessible name. **Text-only UI is valid where an icon adds nothing.**

## v6.13 — Component geometry depends on surface architecture and parent width

First run `references/surface-architecture-gate.md`: continuous records often merit a flat list/table versus a giant rounded Card containing smaller Cards. Then `references/control-geometry-gate.md`: short action labels are atomic; parent table columns/action groups must reserve intrinsic space and reflow whole controls when needed, not break text character-by-character or clip Buttons. This is a general rule that does **not** prohibit legitimate media Cards or portfolios.

## v6.15 — Interaction-state craft is part of component appearance

When the user **confirmed or delegated** meaningful interaction motion, judge not just static type/size but real transitions across **Hover/Press/Selected/Expand/Insert/Success**. See `references/component-motion-choreography-gate.md`: Buttons/Tabs need not all fade; indicators can travel, Disclosures expand spatially, states morph and lists preserve spatial continuity. But do **not animate every frequent table row or inert Card** merely to meet a motion requirement. Respect `none` and reduced-motion; preserve visible focus and correct outcome. A Gallery needs real interaction demos, not CSS declarations asserted to be validated.

## Reuse foundational controls before polishing them

Interactive implementation first follows `references/component-library-first-gate.md` to select the control source. For Select, Combobox, DropdownMenu, Checkbox, Radio, Switch, Button, Tabs and Dialog, start with the existing main library or compatible primitives. **Do not improvise complex behavior for a first-pass visual design.** Refine actual components for consistent dimensions, radius, backgrounds, borders, weight, icon proportions and selected/hover/focus/disabled. A gallery of only static default states does not establish first-pass quality.

## 1. Six questions before high-frequency component design (Gate B)

1. **Purpose:** Which object/action/status? Is a separate surface needed? Navigation, selection, filtering, status or action?
2. **Reading:** What is the most important content (Perceptual Hierarchy Gate)? Is primary/secondary meaning visible through size, weight and spacing?
3. **Usage:** Trigger frequency, risk, keyboard/touch, feedback and confirmation need. Does hit area/action emphasis match?
4. **Shape:** Which established tokens (dimensions, borders, space, radius, colors, typography)? Why not reuse an existing variant?
5. **States:** Do default/hover/active/focus-visible/disabled/loading/error/empty/selected produce distinct, noncontradictory feedback?
6. **Boundaries:** Narrow view, long Chinese/English, 200% zoom, light/dark, empty/errors and real content density. Will text clip or break the parent?

Decide `reuse / wrap / add / do not componentize`. Remove redundant outer Cards, repeated status labels and non-functional decorative Buttons when they have no independent meaning; prettier fills cannot solve missing purpose.

## 2. Replace vague “premium” adjectives with checkable decisions

| Component | Common AI-template failure | Quality bar | Legitimate exception |
| --- | --- | --- | --- |
| Button / CTA | Every Button is the same outline pill, multiple filled primaries per row | Primary/secondary/destructive weight based on **semantics and frequency**; clear label, hit target, feedback and long-copy handling | Brand may use rounded/exaggerated CTAs while retaining usability |
| Tabs / Segmented / Filter | Capsules simultaneously represent filtering, navigation, counts and warnings; tiny count labels | Determine nav vs filter first. Emphasize counts only if central. Proper selected, hover, keyboard and content state | Underline, colored taxonomy and Card switches are valid when justified |
| Table / List / Item | All rows tiny and equal; floating Cards, failure reason buried | Scan object/primary → progress/result → secondary metadata → permitted action; coherent columns and long/filtered/error states | Product/portfolio imagery may use Cards instead of tables |
| Badge / Status | Every ordinary label a colored pill; colors without readable state | Semantic color plus text/icon, consistent size/baseline, Badge only when it shortens scanning | Characterful brand categories if not confused with error/success |
| Input / Search | Oversized round shell with tiny typed text; decorative search | Label/scope/placeholder, focus, clear/error/keyboard, type proportional to field size | Search-first sites may emphasize search |
| Card / Section | Nested borders/shadows/backgrounds, page Card wrapping table and row Cards, **thick colored edge stripe touching Card border** | Every surface explains its independent purpose. Default no rail; justified short marker **outside** with gap (Gate S0) | Deliberate showcase Cards allowed, **flush color rail still prohibited** |
| Dialog / Drawer / Popover | Giant dialog regardless of task; Buttons floating in corners | Match content/risk, managed focus, exit, feedback, scroll, long content | Complex wizard may be page or wide Dialog |
| Navigation | Main nav, recent objects and Tabs share identical active pills | Distinguish route, object, option, status and keyboard focus; preserve discoverability across devices | Immersive nav may be subtle but must remain accessible |

**A design system aligns components; vendor default skins do not replace art direction.** Reka/Radix/AntD/MUI/native may all work when appropriately integrated. Careful typography, optical alignment, sufficient but not excessive padding, clear boundaries and states produce refinement—not globally enlarging every radius or shadow.

## 3. Component composition determines page quality

- An excellent isolated Button can still form a weak page when paired with incoherent Tabs/Table/Badge dimensions, baselines, icon gaps, row density and status tones.
- Gallery should show base treatment + at least two legitimate variants, important interaction states, P0/P1 copy, long Chinese/English, numbers with units, empty/error/loading, narrow window and zoom. **Not every tiny control needs 30 variants.**
- Fix existing tokens/shared components first; do not produce N route-local “premium Button” styles. A scoped patch is fine when it preserves established behavior.
- Reuse **does not** imply identical appearance: Button has primary/quiet/danger; data lists may prioritize price, stock or failure differently by task.

## 4. “Anti-AI-look” is not a ban on legitimate creativity

Never reject a useful artistic choice solely with “it looks AI-made.” State **observable failures**: critical values unreadable at faint 12px, failure reason treated like update timestamp, multiple competing primaries, surfaces without grouping value, illegible action labels, absent states or bottom clipping.

Repair order: **task semantics → information hierarchy → component purpose → type/space/surface → motion/decoration**. If business data or layout is wrong, colors and shadows cannot make it correct.

## 5. Delivery and verification

**Gate A:** Identify actual product type, necessary components and confirmed visual direction. **Gate B:** Provide at least one shared component gallery and contract (purpose, states, tokens, edge cases). **Gate D:** Inspect the component *and its real composed page* in screenshots and interactive states. Different products may choose different shapes; never treat synthetic examples as actual source. Without real browser evidence report **RULE REVIEW ONLY / NOT VISUALLY VERIFIED**, not a finished quality claim.

Use with `references/component-first.md`, `references/workspace-component-refinement.md`, `references/perceptual-hierarchy-gate.md`, `references/visual-qa.md`.
