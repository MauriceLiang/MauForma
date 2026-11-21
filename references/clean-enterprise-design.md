# Clean Enterprise — Optional Clear Workspace Design Language (v6.18)

This is an **optional style profile**, **not** MauForma's default UI template, an exact recreation of any product, or a fixed token list. It fits Web tools used for long periods, fast scanning and reliable operations. Operate products are primary candidates; other modes may selectively borrow principles. Never force a sidebar or table onto unrelated sites.

## Quality is not “all blue, all white, all rounded”

**Desired character:** Clear, effortless, professional, informative, restrained but not flat. Proportion and roles create quality:

- Use large neutral surfaces to support reading. Accent belongs to important actions/selection. Business statuses have consistent semantics; not every Badge needs color.
- Navigation labels should be legible with icons in a supporting role. A subtle selected background and appropriate foreground emphasis usually suffice; add rails/borders only when justified, avoiding three or four redundant selection treatments.
- Set table row heights, weights, widths and alignment from the **scanning task**. Frequent information must not become faint 11px copy. Critical values and actionable links need clear hierarchy. Density does not mean tiny text.
- Use flat tables/lists for repeated homogeneous records, not a decorated Card for every row. Cards are suitable for distinct objects and media.
- Page title, toolbar, sections, headers and row actions form a natural reading path, with optical proportion between paragraphs, digits/units and icons/labels.
- Allow detailed purposeful transitions; a restrained visual style does **not** erase component motion already chosen by the user. The Motion Choice Gate independently governs intensity.
- **Contrast outranks pale appearance:** Muted saturation is not low contrast. Disabled, placeholder, body, headers and statuses remain distinguishable; inspect dark themes separately.

## Design-language contract — semantic roles before fixed pixels

| Role | Desired treatment | Failure mode |
| --- | --- | --- |
| Base canvas | Quiet neutral reading field | Gray so uniform that structure disappears |
| Surface | Flat regions or one-layer containers as task needs | Giant nested Cards around title+filters+table |
| Accent | Limited emphasis on selection and primary CTA | Every Button randomly gets brand fill |
| Navigation | Icon+label as one readable group; clear active background | Tiny text, inconsistent weight, exaggerated active |
| Typography | P0/P1 fully legible; weaker but visible explanation/metadata | Giant slogan alongside tiny critical records |
| Records | Column-aligned scanning, meaningful status copy | Many colored pills per row; clipped actions |
| Spacing | Tight internal relationships, clear inter-section gaps | Empty interior padding coexists with touching Cards |
| Motion | Microinteractions by purpose/user decision | Sudden jumps or universal bounce |

### Starting tokens are project-specific proposals

Derive tokens from the **existing** project. Illustrative roles (not fixed values):

`--canvas`, `--surface`, `--ink`, `--muted-ink`, `--accent`, `--accent-soft`, `--line`, `--space-inline/inside/peer/section`, `--radius-control/panel`, `--font-nav/row/meta`.

Tune using the real font, Chinese/English text, target scanning density and viewport. Review entire nav groups, not isolated icons. Secondary labels must not wash out critical text. Optical icon/text alignment at actual size is not proven by specifying `20px`. Existing UI, approved brand and explicit user choices take priority.

## Icons: Element Plus Icons is a candidate, not a requirement

No open-source icon family is objectively “premium” or “cheap.” Element Plus Icons has concise outlines and usable negative space for some workbenches; Lucide, Tabler, Phosphor, Heroicons or the project's existing icons may fit better.

- Choose icons for actual business meaning, not literal translations of menu wording.
- UI icons differ from logos. Main navigation generally shares a consistent line language and optical weight.
- When using `@element-plus/icons-vue`, verify icon name/import/license for the installed version (official: https://github.com/element-plus/element-plus-icons, MIT). A liked reference icon set is not proof of its origin.
- Main-nav 16–24px is only a common review range, not a mandate. Align with actual type and visual complexity; do not change icon family between active and normal states.

## Transfer across four page modes

| Mode | What transfers | What does not |
| --- | --- | --- |
| Operate | Stable nav, clear selected state, compact readable records, consistent icons | Forcing tables for every list or branded Buttons on every action |
| Persuade | Neutral balance, disciplined accent, clear CTA | Turning a product story into an admin table/sidebar |
| Read | Readable sizes, quiet prose, subtle chapter position | Dense table row height and toolbars full of Buttons |
| Experience | Unobtrusive controls, limited secondary colors and meaningful icons | Replacing an artwork stage with a workbench |

## Reference implementation and limits

`examples/clean-enterprise-demo/index.html` is an **original fictional scenario**, not a recreation of user UI. It uses public Element Plus Icons SVG (MIT, separate license) to demonstrate Nav/Table/Button behavior. Its layout and token values must **never become compulsory defaults** for other products.

Follow additional QA in `references/icon-art-direction-gate.md`, `references/perceptual-hierarchy-gate.md`, `references/semantic-spacing-rhythm-gate.md`, `references/surface-architecture-gate.md`, `references/component-motion-choreography-gate.md` and `references/visual-qa.md`.

Public references: Element Plus https://element-plus.org/zh-CN/component/icon.html ; IBM Carbon Table https://carbondesignsystem.com/components/data-table/usage/ ; Atlassian Tokens https://atlassian.design/foundations/tokens .
