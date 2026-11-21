# Web-First — Supported Product Types and Their Differences

MauForma is a browser-frontend Skill, not a fixed enterprise-dashboard skin. Route new sites and key pages through [Product Experience Type × Page Task](product-experience-routing-gate.md) before selecting a visual mode. The categories below provide high-level guidance, **not** a substitute for understanding actual business tasks. Design principles are broadly reusable, but page composition, density, hierarchy and motion rhythm depend on product needs.

| Product category | Primary goal/content | Appropriate title and layout | Motion consideration | Common anti-pattern |
| --- | --- | --- | --- | --- |
| Admin and SaaS (current detailed focus) | Rapid location, data scanning, CRUD, access control and status | Compact PageHeader, filters above tables, dense content | ~100–220 ms feedback/dialog/tab transitions; avoid rows flying in | English eyebrow + huge heading + empty slogan + excessive whitespace |
| Operational workspaces / CRM / ERP | Multitasking, efficiency and consistency | Prioritized actions, split view, saving and bulk operations | State transitions and lightweight layout motion | Wall-to-wall cards obstruct navigation |
| Corporate site / product landing | Brand promise, capabilities, CTA and trust | Hero can be large; meaningful sections | Moderate scroll reveal and product demos | Exaggerated motion hides CTAs |
| Portfolio / showcase | Work quality, projects and creator introduction | Freer compositions and expressive typography | Project transitions, fades and parallax | Motion crowds out discoverable projects |
| Commerce / product detail | Search, filter, price, inventory and buying | Product imagery and price first; clear CTA | Gallery and add-to-cart feedback | Conflicting promotion hierarchy and competing buttons |
| Reading / media / docs | Readability and retrieval | Controlled line width, contents navigation and information hierarchy | Less motion; preserve reading position | Overly narrow columns, floating decoration, animated prose |
| Data analytics / chart workspace | Explain metrics and trends | Clear definitions, sampling scope, legends and linked filters | Short transitions without altering real numbers | Unsourced animated fake data |
| Visual editor / IDE / graphics tool | Editing efficiency, file tree and toolbar | Resizable split panes, keyboard actions, dense controls | Snapping and panel motion without layout jitter | Every tool wrapped in a huge rounded Card |
| Education / interactive learning | Feedback, progression and comprehension | Visible progress, exercise feedback and step control | Light gamification may help | Unrelated motion interrupts learning |
| Web app / PWA / mobile Web | Small screens, touch, weak network and recovery | Touch targets, focused single-column flows and bottom actions | Responsive, energy-conscious feedback | Squeezing a desktop sidebar onto phones |

## Framework and shell boundaries

- Browser-rendered Web interfaces built with Vue, React, Svelte, Angular and similar technologies are in scope.
- Web interfaces hosted within Electron/Tauri can follow these rules at the DOM/CSS/component level; they do **not** replace native OS UI standards.
- Do not treat MauForma as a direct implementation guide for native SwiftUI/AppKit/Jetpack Compose controls. For cross-platform branding, transfer the **semantics** of design tokens only.
- Existing detailed anti-pattern references concentrate on admin products; use this document to decide which restrictions should be relaxed for other page types.
