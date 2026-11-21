# MauForma — Overview of Eight Visual Direction Profiles

These eight profiles are **MauForma's own synthesis** of strong external design ideas, **not** official classifications invented by the external authors. Each profile preserves a distinct aesthetic intent. Users may deliberately choose highly experimental or motion-rich work; do not force every product toward a minimalist template.

| ID | Visual character | Best suited to | Default risk |
| --- | --- | --- | --- |
| editorial | A high-quality cultural magazine: titles, photography and content alternate in a narrative rhythm | architecture / art / photography | Complex information structures require careful mobile reflow |
| experimental | Bold whitespace, displacement and conflicting scales create a recognizable result unlike standard templates | creative studio / portfolio / art exhibition | Unusual compositions need extra responsive and accessibility validation |
| premium-showcase | A carefully photographed product dominates the frame; other information supports it | food / car / furniture | Poor source media becomes more visibly poor when enlarged |
| playful | Vivid but organized color, illustrations and characterful feedback make exploration approachable | children's education / games / entertainment | Excessive playfulness can weaken professional credibility |
| cinematic | Stage-like camera work, storyboard rhythm and immersion progressively reveal the theme while scrolling | gaming / film / digital art | High video/Canvas/WebGL costs |
| calm-minimal | Calm, precise typography and restrained color make content, not decoration, the focal point | developer tools / professional software / enterprise services | Equal visual weight across everything becomes bland |
| functional | Search, filters, primary tasks and status remain immediately reachable, without scrolling to basic operations | ERP / CRM / admin | Less spectacle than a brand landing page |
| reading-first | Content structure is apparent on first glance and remains free of unnecessary interruptions while reading | docs / knowledge base / news | Limit visual experimentation when it harms comprehension |

## Search and recommendation

Run `python3 scripts/search_design_knowledge.py --query "蛋糕 店铺 摄影 到店" --mode Persuade --limit 3`. When the user has specified a direction, **their decision wins**. Script suggestions are reasoned proposals, never proof of approval. Profile metadata and influences are documented in `assets/style-knowledge.json` and `references/aesthetic-authorship.md`.

## Interpretation principles

1. Collect authentic content, target audience, available assets and the primary task **before** selecting a profile.
2. For each proposed direction describe first-screen focal subject, image-to-text relationship, density, motion, implementation cost and failure modes.
3. One product may use Persuade, Operate, Read and Experience on different pages while sharing brand tokens.
4. A profile expresses an aesthetic position, not a fixed component template. Blends are allowed only with an explicit account of what is adopted and what is intentionally rejected.
