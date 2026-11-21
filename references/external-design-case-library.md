# External Design Case Library — On-Demand Principles, No Brand Asset Copying

MauForma maintains eight independent style profiles in `assets/style-knowledge.json` and selectively references two public sources that serve **different** purposes:

| Source | Actual corpus | Use | Limitation |
| --- | --- | --- | --- |
| [UI/UX Pro Max](https://github.com/nextlevelbuilder/ui-ux-pro-max-skill/tree/main/src/ui-ux-pro-max/data) | 88 style profiles (79 searchable), 192 product/industry strategy classes, palette/type/layout/UX data (**summary checked 2026-11-01**) | Suggest design directions appropriate to specific industry/tasks | Rules and recommendations, **not 192 individually reviewed real websites** |
| [VoltAgent awesome-design-md](https://github.com/VoltAgent/awesome-design-md) | 84 community analyses of brand websites in `DESIGN.md`, covering color, type, composition, components, rules and responsiveness | Concrete sites and transferable patterns | **Community analysis** of publicly available sites, **not an official brand Design System** |

Catalog: `assets/external-design-cases.json`, a 2026-11-02 snapshot with upstream commit SHA and 84 links. Do not paste all 84 documents into MauForma: they inflate context and prevent checking upstream changes.

## Use during product discovery

1. Begin from the user's website purpose, authentic content, audience and available assets. Use `scripts/search_design_knowledge.py` to identify candidates.
2. Search specific site cases with `python3 scripts/search_design_cases.py --query "甜品 咖啡 门店" --style premium-showcase --limit 5`.
3. Read upstream `DESIGN.md` **only for matching candidates**. Prefer `review_status=sampled` reviewed records. `candidate` is a domain-inferred potential match; `indexed_unreviewed` means indexed only.
4. Extract transferable subject scale, whitespace, color semantics, typography hierarchy, states and responsive choices. Label whether evidence comes from upstream author's document, MauForma inference or **actual rendered observation**.
5. When current brand visuals matter, cross-check official site or current browser screenshots; older `DESIGN.md` text cannot certify latest official exact palette.
6. Offer **2–3 defensible distinct options** with tangible advantages and costs; an indexed brand does not constitute user approval.

## Sampled examples

- [Apple DESIGN.md](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/apple): Product imagery first, alternating light/dark presentation and concise UI → premium showcase.
- [Tesla DESIGN.md](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/tesla): Full-bleed cars and minimal controls → product/immersive presentation.
- [Linear DESIGN.md](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/linear.app): Dark neutral surfaces, restrained accent, product screenshots → developer/professional software.
- [Stripe DESIGN.md](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/stripe): Grid gradients and financial/technical hierarchy → brand and product.
- [Starbucks DESIGN.md](https://github.com/VoltAgent/awesome-design-md/tree/main/design-md/starbucks): Retail materiality, meaningful green roles and photography → food/drink retail.

Other brands may appear in search, but are not approved exemplars before reading/verifying their actual documents. A README mentioning `preview.html` does not guarantee it exists in every case's folder. Previews generally need to be viewed on the upstream website; do not promise a runnable preview inside the repository.

## Copyright and evidence

Both upstream repositories release *their documents/code* under MIT; this does **not** grant rights to reproduce Apple/Tesla/Stripe trademarks, photography or proprietary fonts. MauForma stores **source links plus original selection commentary**, not brand Logos/images/fonts. Redistribution of upstream documents requires preserving the license/attribution and checking terms for brand assets.

Files marked `version: alpha` or `Inspired` must **not** be described as official brand design standards.
