# Good vs Bad UI — Cross-Product Design Anti-Pattern Handbook

**Judgment:** Great UI is not simply rounder, brighter or more animated. It communicates information and supports actions quickly through a coherent design system that is maintainable. The examples below are transferable recommendations, **not claims about what an upstream example site already implements**.

## 1. Purposeful colors versus random palette choices

- **Good:** Warm-neutral site surfaces and copper-brown as the primary action accent; success/error/warning have independent semantic colors. Pages inherit one theme mapping with a product rationale.
- **Bad:** A blue Save on Home, purple Save in Settings and green Save in the confirmation dialog, while headings/sidebar/Cards each use unrelated gradients.
- **Fix:** Centralize semantic color roles in Tokens. Themes may change, but not the meaning of a primary action from page to page.
- **Check:** Changing data-theme updates shared components and leaves no stranded hard-coded HEX.

## 2. Radius hierarchy versus 24/32px everywhere

- **Good:** A desktop may use outer 16px, nested fields 8–10px and working Buttons 8px; a promotional page may justify 32/18/pill. The parent/child relationship is clear.
- **Bad:** Tiny labels share the same radius as giant dialogs; every dense list row receives 32px and a heavy shadow.
- **Fix:** Semantic radius-panel/inner/control/button Tokens, coherent within each layer and adapted to actual density.

## 3. Restrained shadows versus everything floating

- **Good:** Subtle surface color/shadow separates Cards; lists primarily use spacing/thin borders. Stronger depth belongs to overlays when warranted.
- **Bad:** Every Table row has 0 18px 48px rgba(0,0,0,.25), Inputs cast heavy shadows and the UI looks like floating stickers.
- **Fix:** Reduce surface levels. Remove shadows from normal lists; use shared shadow Tokens only for meaningful depth.

## 4. Scannable type hierarchy versus equal emphasis everywhere

- **Good:** Page title, section title, body and metadata have intentional relative sizes. Key numbers stand out without metadata competing. Long Chinese and mixed English/numeric strings wrap correctly.
- **Bad:** All headings are 28px bold, auxiliary text is low-contrast 10px, negative tracking crowds short Chinese headings, large paragraphs use saturated colors.
- **Fix:** Use type scales and fewer strong emphases. Preserve readable CJK line height, minimum practical text size and contrast; do not misrepresent advisory sizes as normative WCAG minima.

## 5. Grouping rhythm versus mechanical spacing

- **Good (illustrative values):** 8–12px among related form elements, 16–24px between paragraphs and 24–40px between sections; controls align to common baselines.
- **Bad:** Every region has margin:32px and feels empty without design; another page uses 4px and feels authored by a different team.
- **Fix:** Establish local/global spacing relationships from a 4px/8px scale and adjust by density profile. These numbers are not universal rules.

## 6. One owner for one behavior

- **Good:** UiButton variant=primary behaves the same on Home, dialogs and Settings. Theme changes flow from one shared source.
- **Bad:** HomeButton, SettingsSaveButton, ModalConfirmBlue and BlueBtnV2 implement essentially the same action with separate CSS.
- **Fix:** Reuse primitives and expose meaningful variants instead of cloning components by route names.

~~~css
/* Bad: route-specific styles drift. */
.home-save { border-radius: 20px; background:#0071e3; }
.dialog-save { border-radius: 8px; background:#6941c6; }

/* Good: shared component uses semantic variables. */
.ui-button--primary {
  border-radius: var(--spui-radius-button);
  background: var(--spui-accent);
  color: var(--spui-on-accent);
}
~~~

## 7. Meaningful feedback versus bounce everywhere

- **Good:** Subtle first-visit entrances on promotional pages; 160–200ms Button hover; transitions do not obstruct actual input.
- **Bad:** Cards slide from outside on every refresh, list rows bounce when scrolled, hovered Buttons scale to 1.12 and shake, dialogs refuse to close promptly.
- **Fix:** Remove elastic response from high-frequency controls; respect reduced-motion preferences; keep essential content visible without JavaScript animation.

## 8. Optional accent gradients versus neon on every heading

- **Good:** A promotional headline may use a limited on-brand gradient; controls/body copy remain readable solids. Developer tools may need no gradient at all.
- **Bad:** The same pink/purple/blue is applied to every title, menu, icon, Button and progress bar; white text vanishes on pale gradients.
- **Fix:** Default to no gradient. Use it only with a justified visual role and tested readability.

## 9. Clear navigation state versus tiny color differences

- **Good:** Current item is distinct through background/weight/position/meaningful marker, with visible hover and focus, consistent in the product.
- **Bad:** Selected differs only from #999 to #888; click target is a few letters; navigation is a decorative div without semantics.
- **Fix:** Shared UiNavItem or accessible Tabs primitive; correct aria-current and selection semantics, keyboard/touch targets.

## 10. Real form states versus attractive static boxes

- **Good:** Every Field has label, hint, required (where applicable), focus, error and disabled treatment; errors stay near fields and explain correction.
- **Bad:** Placeholder replaces label, error only changes border to red, focus uses outline:none without alternative.
- **Fix:** Shared UiField; meaningful error text and aria-describedby associations.

## 11. Semantic status feedback versus arbitrary branding

- **Good:** Synced text + green success mark, Connection failed / Retry + error semantics, explicit pending feedback.
- **Bad:** Successful deletion uses error red simply because brand accent is red; only a spinner conveys pending; server disconnection is a nearly invisible gray dot.
- **Fix:** Semantic status separated from brand accent, combining readable words/icons and color.

## 12. Responsive recomposition versus shrinking text

- **Good:** Narrow views reflow Grid and action order; primary CTA remains reachable; long titles wrap; tables scroll or become navigable detail lists.
- **Bad:** Fixed 980px causes overflow, dialog clips at 375px, or changing 18px text to 12px is mistaken for responsiveness.
- **Fix:** Recompose by available space (for example minmax(0,1fr)), verifying long real labels and data.

## 13. True dark-theme palette versus whole-screen inversion

- **Good:** Separate dark surface/border/text/accent/on-accent with coherent semantic contrast and focus.
- **Bad:** Applying filter:invert(1), or preserving white text while Button background changes to an illegibly light purple.
- **Fix:** Define explicit dark Tokens and test regular/focus states in every supported theme.

## 14. Meaningful icons versus decorative clutter

- **Good:** One coherent icon family, consistent strokes/sizes/alignment; icon-only Buttons have accessible names; icons are restrained in dense interfaces.
- **Bad:** Random emoji beside each title; mixed filled/outline icons, arbitrary 12–30px, every label replaced by a mystery symbol.
- **Fix:** Use intentional 16/20/24px icon roles, retain words when helpful, never add an icon merely because an area looks empty.

## 15. True business status versus simulated completion

- **Good:** Show genuine empty/error states; clearly label demonstration interactions.
- **Bad:** An Analyze button animates a fixed 0.86 as if a real model ran; Save turns green without persisting any data.
- **Fix:** Distinguish visual feedback from business results, label demo data and connect production functions to actual state.

## 16. Visual quality and performance versus excessive material effects

- **Good:** Limited shadows, lightweight transforms/opacity, stable low-resource interaction.
- **Bad:** Stacking backdrop-filter glass, noise, floating light orbs and heavy shadows, especially costly on low-end/high-DPI devices.
- **Fix:** Remove effects without information value; prioritize responsive input, scroll, dragging and overlays.

## Reviewer requirement: "looks bad" is not an actionable finding

For each issue: **specific component/page → violated rule → user-facing or maintenance cost → proposed repair → test evidence**. Prefer actual before/after screenshots. Without them, report source-level risks, **not guessed rendered aesthetics**.

## 17. Operational page headings: tasks first, not a marketing Hero

- **Good:** Management/settings/lists/edit pages use one clear H1 (for example a real Account Management task), an optional brief explanation of a genuine constraint/scope, primary action adjacent to the title and toolbar/table close behind. Breadcrumbs represent real navigation.
- **Bad:** Decorative category label above a huge 80px account title and verbose gray filler; or USER MANAGEMENT merely translates the next heading; every task page repeats English pretitle + giant title + slogan + 180px empty space.
- **Fix:** Determine page purpose, then use UiPageHeader or an established equivalent; remove labels lacking new information, forced translations and giant decorative wrappers.
- **Exceptions:** Brand/marketing/portfolio Heroes may legitimately use intentional eyebrows, English and large headings. Breadcrumb terminal label may match H1 without redundancy.
- **Verify:** Core action and at least some real working content visible in typical supported first screen. Every pretitle has an explainable purpose.
- See page-header-antipatterns.md and assets/page-header-antipattern-gallery.html.

## 18. Copy necessity: hierarchy versus decorative pseudo-information (v6.5)

- **Bad:** One analysis page stacks a generic English studio label, vague collaboration phrase, abstract slogan, "01 / Overview" and another instruction line, all repeating "this is an analysis page" without actual navigation value.
- **Good:** Real product identity → actual object/repository identity → clear analysis page heading → meaningful activity/issue sections → real sources and sampling limitations.
- **Preserve:** Verified brand taglines, actual breadcrumbs, legitimate chapter order and data provenance. Do **not** ban all microheadings mechanically.

## 19. Typography: critical content must be readable

- **Bad:** Abstract oversized H1 while real labels become faded 10px and chart ticks/sample n are illegible.
- **Good:** Role-specific PageTitle / Section / Metric / Chart / Metadata sizes, sufficient dark-mode contrast and 200% text scaling. Reduce tick count or restructure groups instead of shrinking all text without limit.
- See typography-hierarchy.md: suggested font ranges are **not mandatory accessibility font-size thresholds**.
