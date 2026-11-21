# Sidebar Color Discovery — Inspect the Whole Page, Then Let the User Decide

> Synthetic failure: sidebar and main region lack coherent semantic color roles. Color preference requires user authority; a local palette sample is insufficient.

## Color Choice Gate — New sites, major redesigns or explicit color-direction requests

### A. Gather existing evidence first; do not re-ask answered questions

Inspect brand assets, real colors across Main/Topbar/Sidebar/Panel, logo accents, existing design tokens, dark/light variants, **previously explicit user instructions**, and screenshots. Only when the choice genuinely remains unknown and materially affects work, ask **one** question: “What color would you like as the sidebar's primary color? A name or HEX is enough; if you're undecided, I can offer two or three complete whole-page directions.”

- **Already specified** “black sidebar,” “white navigation,” “I like green,” or `#30414C`: adopt this **color requirement** immediately; do not force three options and demand reconfirmation, or silently restore blue/purple.
- **Only says color looks wrong** with no desired choice: inspect product type, main UI and brand. Present 2–3 **meaningfully different whole-page palettes**, concise reasons and tradeoffs; let user select or give another color. A recommendation is **not** approved.
- **“You decide” explicitly delegates color direction:** choose a suitable scheme, record `delegated`. Delegating coding or layout alone does **not** authorize changing inherited colors. Explicitly provided colors outrank general autonomy.
- **Approved brand/design:** Continue as `inherited` or `confirmed`, without re-running the vote. Scoped bugs/functional edits do not require a complete color interview.
- **Exact user HEX:** Never covertly change the numeric HEX or hue. If contrast suffers, adjust surrounding surface, text, selected/focus colors and explain the issue. Seek explicit consent **before** changing the user's fixed value.

### B. Research real design systems; do not copy their look mechanically

Read `references/sidebar-color-reference-cases.md` and `assets/sidebar-color-directions.json`. Compare at least **two distinct methodologies** from evidence, e.g., Linear's reduced navigation noise, Carbon's distinct semantic states, Primer's sidebar/main division, shadcn's sidebar roles or Atlassian's single token source. MauForma example palettes are original concepts, **not screenshots or sampled official brand HEX values**.

Offer 2–3 candidates matching this project, explaining:

1. **Sidebar canvas** (dark/light/neutral/user-selected) and how Main and Topbar relate to it.
2. Selected/default/hover text, icons, edges and focus contrast; where the brand accent is and **is not** used.
3. Which candidate suits the actual product type, why, and its long-session tradeoffs.
4. Coordination with dark/light modes and chart data colors; not merely a sidebar color swatch.

**Required principle:** Compare the **sidebar in the entire page**, not five isolated sidebar images. `assets/sidebar-color-preview.html` contains five *original fictional full-workbench* directions as references, but usually show real users only 2–3 relevant options.

### C. User approval and actual implementation

- Offer “Recommended A (reason), B (tradeoffs), custom color (Chinese/name/HEX/screenshot).” **Agent recommendation is not user confirmation.**
- Save project decision as `design-system/sidebar-color-decision.json` using `assets/sidebar-color-decision.schema.json`. While `status=pending`, a palette has **not** been approved; never apply it as the final site theme.
- After selection record `status=approved`, `source=confirmed`, selected candidate/custom value and the user's actual words. Explicit delegation permits `delegated`; previously approved retained setup can be `inherited`. Never invent a user quotation.
- Integrate through existing theme variables or unified `MASTER`—do not establish a detached second brand palette for the sidebar. Sidebar may have separate semantic roles but derives from the same project theme.
- Inspect **Sidebar ↔ Topbar ↔ Main ↔ Card ↔ Chart** together for temperature, surface hierarchy, boundary transitions, text contrast and chart-series meaning. A lone sidebar edit with other pages untouched is **not** proof of site-wide coordination.
- Review actual wide/narrow browser rendering, light/dark, hover/selected/focus, contrast and 200% text zoom. Static color-value checks **cannot establish visual quality or page-wide harmony**.

## What if the user's requested color is hard to read?

For example, a pure-yellow sidebar is **still the user's specified color**, not permission to silently replace it with dark navy. Offer yellow with dark text and suitable main-region colors and test contrast. If the user additionally requests white on pale yellow and contrast fails, clearly state the conflict: propose retaining yellow while changing text, or getting approval for a darker selected state. Do not override an explicit choice or call an illegible theme verified.

## Decision authority

- **User:** Owns the desired primary color and allowed overall aesthetic.
- **Agent:** Recommends, explains tradeoffs, coordinates accessibility, produces tokens and verifies.
- If the user rejects the Agent's favorite, adapt the whole page to the **user's** direction; do not refuse on “designer taste.”
- Ask only one blocking color question when necessary. Without explicit color authorization, continue layout/structure/component work not dependent on a palette instead of repeatedly surveying the user. **Never promote a recommended example palette into the final theme without approval.**

Sample dialog: `examples/sidebar-color-discovery-dialogues.md`; record and validate with `scripts/validate_sidebar_color_decision.py`.
