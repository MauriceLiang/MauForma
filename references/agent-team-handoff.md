# Multi-Agent / Team Collaboration Contract

## Roles, responsibilities, and delivery order

1. **Design Lead:** Consolidate product tasks and component inventory; confirm the visual direction, semantic theme roles, density and design tokens. Separate implementation from acceptance tasks so individual frontend agents cannot independently invent conflicting visual languages.
2. **UI Foundation Owner:** Implement or theme shared components and their state examples first. Deliver `tokens/theme + UI primitives + component contracts + component gallery`, with visual-consistency, keyboard and component-state findings.
3. **Feature Developer:** Compose pages and business interactions using shared components. Own layout and genuine feature differences only; route new shared-UI requirements back to the component layer rather than circumventing it.
4. **QA:** Compare the component gallery with real product pages, run functional and keyboard checks, record good and bad cases item by item using the review rubric, and annotate screenshots when justified.
5. **Lead's final review:** Check Gates A/B/C, duplicate components, dark theme, narrow windows and outstanding issues. Only then consider acceptance and merging under the project's established branch and delivery process.

## Example frontend work split

- **Task 1 / Foundation:** Inventory current buttons, forms, dialogs, navigation and cards. Produce a merge/adapt/new matrix and a single token source. Do not change business pages yet.
- **Task 2 / Component kit:** Implement theme adapters and 6–10 *actually needed* shared components. Provide an accessible state gallery and pass Gate B.
- **Task 3 / Feature screens:** Replace repeated implementations screen by screen, preserving behavior and API contracts without introducing duplicate CSS.
- **Task 4 / Quality:** Capture full-screen and state comparisons, repair visual anti-patterns, produce a rubric-based report, and spot-check performance and accessibility.

## Shared agreements between agents

- Every agent uses the same tokens and shared component contracts. When existing UI-library conventions conflict, the responsible lead must make an explicit design decision.
- Changes to foundational component APIs must identify affected pages and, when necessary, update callers and the component gallery together.
- An attractive mockup is not acceptance: real business logic, states, responsive behavior and keyboard paths must work.
- The component owner must not fabricate API data on the feature team's behalf; a feature developer must not independently redefine the color system.
- Record review findings as **location → anti-pattern → evidence → fix → verification**.

## v6.3 — Visual review handoff

UI Foundation supplies common state and accessibility contracts for Sidebar, Topbar, Tabs, RecentItem, Table, Search and SplitPane. Feature Developers must not add vivid selection bars or meaningless orange dots to workspace pages on their own. QA separately checks dark surfaces, hover/selected/focus-visible, and the difference between the recent item and active route, using the concrete failure modes in `references/sidebar-navigation-design.md`. Any deliberately strong treatment or left selection rail must explain the *independent information* it communicates. Do not replace evidence with a subjective claim that a design merely “looks AI-generated.”
