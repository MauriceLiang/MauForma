# React / Next — Reusable Components and Performance Review

These rules draw on the *intent* of Vercel Composition Patterns and React Best Practices. Implement using the actual project's React/Next versions and installed primitives; **never copy APIs from an incompatible version**.

## Component structure and APIs

- Avoid giant components with a maze of mutually exclusive boolean props such as `isCompact/isDark/isPrimary/isEditable`. Express roles through explicit `variant/size` enums or appropriate compound components.
- A compound component may use a shared Provider to coordinate cross-child state with clear ownership. Do not impose complex Context on a simple Button.
- Separate presentation primitives from data/business logic. `components/ui` owns coherent visuals, focus/keyboard and fundamental states; features own fields, permissions and APIs.
- Make controlled and uncontrolled API modes explicit. Avoid untraceable mixes of render props, children and Context.
- Build a runnable component showcase/tests for variants, states and keyboard behavior before duplicating UI across business pages.
- **React 19 rules cannot be applied automatically to React 18.** Account for Next SSR/RSC; declare Client Components only where interaction actually requires them.

## Performance priorities

1. **Real perceived bottlenecks:** Network request waterfalls, serialized server blocks, duplicate fetches.
2. **Bundle size:** Dynamically load expensive below-the-fold effects; never inject a site-wide animation engine into every page without need.
3. **Rendering stability:** Unnecessary whole-tree state propagation, redundant renders and virtualizing truly large lists.
4. **Micro-optimizations last:** Do not wrap every text node in memo.

## Interaction with visual rules

- Concentrate expressive motion in high-value regions. Do not have an animation library and React state code directly fight over the same DOM property.
- Clean up animations, observers and timers on unmount.
- Avoid browser-only APIs during SSR render. Optimize image loading and provide appropriate fallbacks.
- Third-party defaults are not an accessibility waiver: test actual focus and keyboard interactions.

## Pull request acceptance

Report the mapping of reused components, variant/state evidence, version/dependency changes, measured bottlenecks and actual tests. **Untested performance claims are only risk hypotheses, never proof that optimization succeeded.**

Official references: https://github.com/vercel-labs/agent-skills/tree/main/skills/composition-patterns and https://github.com/vercel-labs/agent-skills/tree/main/skills/react-best-practices
