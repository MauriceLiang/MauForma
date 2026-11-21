# Project Design Hierarchy — One Approved System, Context-Specific Overrides

**Purpose:** Distinguish the user's authoritative design decisions from Agent proposals, observed code, synthetic examples and external references. Multi-page products should have coherent foundations without forcing the same page density or composition everywhere.

## Authority levels

1. **Explicit user requirement:** Latest specific instruction, requested product behavior, confirmed color, component/navigation direction and constraints.
2. **Confirmed project design:** Approved `design-system/MASTER.md`, decisions and signed-off page variants.
3. **Actual working architecture:** Existing framework, component APIs, installed packages, data flow and routes.
4. **MauForma guidance:** General reusable principles and conditional gates.
5. **Synthetic samples/external trends:** Inspiration, never binding project truth.

If a newer explicit instruction contradicts an older generic preference, follow the newer instruction for the affected scope. Do not infer blanket authorization to rewrite unrelated decisions.

## Source-of-truth structure — adaptable, not a required directory dump

```text
design-system/
  MASTER.md                 # Approved shared tokens and component roles
  decisions/                # Confirmed/delegated records with rationale
  pages/                    # Page-specific purpose, layout and density overrides
  features/                 # Resumable task-specific design records when useful
  observed-tokens.json      # Code-derived observations, NOT user approval
```

Use the existing project's established folders when available. These paths are illustrative; **do not create empty documentation trees for every small patch**.

## Decision provenance and language

Record `confirmed / inherited / delegated / proposed / unresolved` as separate states. “The Agent recommends” remains `proposed`, not `confirmed`. Silence or a request to write code is not broad permission to redefine branding, install dependencies or add cinematic motion.

Retain the actual product locale. An English Agent instruction file **never means the user's UI must be translated to English**. On bilingual products, check real translated copy and layout rather than setting a global English default.

## Global MASTER versus page override

MASTER should hold shared colors, type roles, spacing scales, radius, interaction/state semantics, icon and Motion Tokens, component contracts and navigation responsibilities. Each page can choose its task-specific density, content hierarchy, layout, editorial rhythm, media emphasis or allowed motion intensity. A marketing landing can be expressive, while settings/operations remain compact under the same product branding.

Do not let page-local CSS silently redefine global brand tokens. Conversely, do not erase a justified page exception merely because MASTER is more compact.

## Design drift categories

- **Tool drift:** Dependency/formatter/browser version behavior changes.
- **Schema drift:** Token/decision document structure changes.
- **Design truth drift:** Source/UI diverges from actually approved choices or real task meaning.

`scripts/check_design_drift.py` records code-observed variables and compares versions; a generated observed baseline is **not MASTER truth**. Do not overwrite `MASTER.md` or approved design decisions merely to make a static drift report green. Design truth requires user/brand authority and real rendered evidence.

## Multi-agent and resumable work

Component/design lead owns shared tokens; feature agents compose using them. Changes to foundational components should identify all affected callers and reverify. Feature-level records may be created as needed with `scripts/feature_design_flow.py`, but are not mandatory for every tiny task.

## Quality evidence and escalation

For significant change, record scope, approved/inherited constraints, observed defect, proposed fix, actually modified components and verified route/state/viewport. Static checks and synthetic examples remain separately labeled; a complete green CI on Skill examples is not a substitute for the target product's real user workflows.

**Escalate** real conflicts over a fixed user HEX, approved navigation type, licenses, explicit performance limits or interaction state rather than silently choosing whichever design looks prettier. Genuine unknowns remain `unresolved`, not a fabricated user decision.
