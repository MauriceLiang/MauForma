# Icon Art Direction & Semantic Fit Gate — Choose Icons for Meaning, Shape and Context (v6.17)

Applies to all Web modes and frameworks. An icon is **not a random library match for a menu word**, nor is it visually refined simply because CSS sets every icon to 24px. First decide whether one is needed, then its symbolism and family, finally actual render size, outline, color and states.

## v6.18 — Learn icon direction, never extract screenshot assets

User-supplied original UI can show outline/fill roles, optical weight, type ratios and stylistic cohesion. **Never upload reference screenshots, cropped icons or extracted SVG paths as public demo assets**. Verify actual candidates from official icon libraries and retain project-specific choices. A user liking Element Plus Icons in one project does **not** make them the default across all Web products. For third-party open-source SVG in public examples, retain licenses and omit identifiable user brand/data. See `references/design-reference-learning-gate.md`.

## Gate I0 — Why an icon?

An important navigation/control/status icon needs an actual job:

- **Findability:** Recognizable graphic aids fast scanning and target recognition.
- **Affordance:** Indicates a real action: search, download, filter.
- **Domain identity:** Expresses a known class of object or product with domain consensus.
- **Brand/illustration:** Large marketing graphics/product illustrations are **not** 16–24px UI icons.

For abstract notions (“increase efficiency,” “smart collaboration,” “model insight”), do not invent a brain+lightning+network collage to fill space. Prefer **recognizable familiar symbols**, or **text alone** if no clear symbol exists. User-provided logos, third-party trademarks and generic UI symbols are different categories; never substitute a random outline icon for a real brand mark.

## Gate I1 — Meaning first; candidates must exist

For primary nav, high-frequency actions, destructive actions and core states, compare **at least two real, semantically defensible candidates** before implementation, unless a coherent existing approved system should simply be inherited. Record:

`interface label → intended object/action → real candidate names/library/verified source → selected symbol → recognition rationale → rejected alternative/reason`.

For a generic “compare projects” operation, `arrow-left-right` may be clearer than a complicated Git graph. **If the action actually compares Git branches, `git-compare` may be more accurate.** “Research analysis” might mean scatter statistics, laboratory experiments or document research. Pick from actual task, not the first English dictionary synonym.

Confirm each icon name **actually exists in the installed library version**; illustrative candidates are not import contracts. Avoid:

- Typos or removed aliases causing empty runtime icons.
- Two unrelated adjacent functions sharing one indistinguishable symbol.
- Unreviewed emoji/Unicode decoration or random generated SVG replacing mature icons.
- Inventing an icon for every caption/ordinary state merely for symmetry; no icon is better than a misleading one.
- Destructive/Save actions whose meaning depends on a glyph with no text or accessible name.

## Gate I2 — Choose a coherent *family*, not isolated winners

**Review a group of 6–12 actual icons**, not one impressive isolated screenshot.

Prefer **one inherited main UI family**: Lucide (restrained outlines), Tabler (structured outlines), Phosphor (varied weights), Heroicons, Remix, Carbon, etc. Compare as a group:

- Stroke weight, fill/outline, caps/corners and curve language.
- Complexity, negative space, optical centering and recognizable silhouettes.
- Fit with CJK/Latin typography, palette and density.
- Dependencies, actual package/version/framework binding, tree shaking, licensing and maintenance.

**Family principle:** Do not mix unrelated outline, duotone, filled 3D, icon-font and emoji styles within one navigation/peer control group. Brand logos, data semantics, illustrations and inherited specialist symbols are **controlled exceptions**. Officially paired outline/filled states may work but must not create huge selected weight/shape changes or flicker. **Never choose a semantically wrong icon simply to keep one family**; justify a specialist family, design a coherent custom glyph or omit the icon.

Official sources for comparison:
- Lucide: https://github.com/lucide-icons/lucide/blob/main/docs/how-to/icon-guide.md and https://lucide.dev/icons/
- Tabler: https://docs.tabler.io/icons/design-guide
- Phosphor: https://phosphoricons.com/
- IBM Carbon: https://www.carbondesignsystem.com/building-blocks/foundations/icons/guidelines

Never copy SVG from unverified random sites; check original third-party licenses and preserve required notices. Do not install a huge icon font to display six static nav symbols when on-demand SVG/components suffice.

## Gate I3 — Optical precision: icon and label are one composition

Unify `IconBox` and semantic token roles such as `icon.navigation`, `icon.inline`, `icon.dense-action`, `icon.hero-symbol`. **Size is a contextual role, not one magic global pixel.**

- Coherent visual box, stroke/fill modes and alignment; one list icon must not look dense/bold next to a single thin line.
- Align icons with labels and Badges, center optically when needed, without negative margins hiding faulty geometry. Test mixed CJK/Latin fonts and numeric Badges.
- 16/20/24px are **review examples, not compulsory sizes**. At actual rendered sizes, ensure shape detail and negative space remain visible. Replace overly complex icons before just reducing stroke width.
- `stroke-width:2` is a design choice in some libraries, **not a mandate to rewrite every library as 2px**. Never apply one blanket stroke to Phosphor, Lucide and filled logos.
- Validate icon/label/Badge, selected background, hover/focus-visible/disabled, theme and text scaling; avoid flex-shrink deforming icons or clipping them.
- Animate only within user-approved motion intensity; transitions can belong on the interactive container/state. Do not make every icon spin/bounce or change identity on selection by default.
- Decorative icon duplicated by a visible label may use `aria-hidden="true"`. **Icon-only Buttons require an accessible name and usable hit target**. An `icon` prop does not automatically establish accessibility.

## Gate I4 — Icon shortlist, showcase and real visual acceptance (A/B/D)

**Gate A, before design:** Inventory existing and official libraries → decide the product's icon grammar → verify at least two real candidates for important functions → select by group. When the user already approved a brand/icon family, inherit it rather than switching arbitrarily. For a major new icon direction, offer **2–3 whole-family comparisons** during style approval, not a question per button or a preference-only survey.

**Gate B, implementation:** Create a reusable Icon wrapper/registry. Show actual-sized primary nav, icon Buttons, statuses, empty states and mixed label/icon groups **together**. Verify names, installed versions, license, type scale and semantic mapping. Do not copy and randomly edit every SVG into slightly different styles.

**Gate D, browser:** Test actual 16/20/24px where applicable, CJK/English, selected/hover/focus/disabled, light/dark and zoom. Inspect **blank icons, wrong viewBox, clipping, compression, baseline mismatch, optical weight conflicts and unrelated family mixing**. For abstract concepts, run a quick recognition test with labels hidden; recognition is a bonus, but if unintelligible, don't rely on the glyph alone in icon-only mode. **Whole-group screenshots/human visual review determine aesthetics**; no numeric “looks good” score.

- `assets/icon-curation-patterns.json` and `python3 scripts/validate_icon_curation.py --repository` check mappings, candidate existence markers and family contracts.
- `assets/icon-art-direction-lab.html` and `tests/icon_art_direction_browser_smoke.mjs` verify synthetic SVG rendering, ratios/states and detect intentionally inconsistent combinations.
- `scripts/audit_icon_consistency.mjs` inspects marked `data-mf-icon-group`/`data-mf-ui-icon` geometry/styles. **It only reports technical candidates** for missing, stretched, mismatched size/family, not semantic or subjective taste. Unmarked user products were **not** audited.

Linked gates: `references/perceptual-hierarchy-gate.md`, `references/component-craft-gate.md`, `references/control-geometry-gate.md`, `references/visual-qa.md`, `references/motion-consent-experience-gate.md`.

## Illustrative design failures — not absolute judgments about any icon

- Two 20px glyphs: one path-dense and one simple silhouette. The optical weight differs, so **try a better semantic candidate first**.
- A single nav icon unexpectedly becomes filled/emoji while peers remain outlines; brand logos are an exception.
- A generic two-project metrics comparison uses Git topology so users assume version-control behavior; use accurate comparison semantics.
- “Research analysis” shows a flask even though the page is all statistical charts; consider Chart/Scatter. A real laboratory management screen may actually warrant Flask.
- Icons added beside every ordinary empty-state/caption for decoration. Real status should not rely on icon alone either.

**This Skill supplies a decision process and test guidance. It never mandates Lucide, 20px, outline-only icons, or a single global art style.**
