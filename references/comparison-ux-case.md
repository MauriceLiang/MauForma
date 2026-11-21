# Multi-Object Comparison Page — Synthetic Failure and Verification

**Nature:** An entirely fictional design-training scenario, **not** a review of screenshots or a defect finding from any real product.

## Counterexample

A user selects three objects for a comparison. The legend lists three labels, but the main trend chart visibly renders only one series. A very wide object selector remains permanently visible; a methodology explanation consumes substantial area while the difference summary and shared metrics table lack emphasis.

## Transferable rules

- First determine **the question and measures** users need to compare, rather than arranging three charts first.
- Keep the object picker, legend, each actually available data series and comparison matrix in sync. Never show “three selected” without explaining why only one curve appears.
- Clearly identify time window, aggregation granularity, units, sample size and data coverage. Display missing values as **missing**, never as zero or fabricated values.
- Reduce persistent low-value explanations and oversized sidebars. Move details behind discoverable disclosure when appropriate.
- Inspect rendered **plot areas, axis baselines, ticks and labels** inside charts. Equal outer Card frames do not prove interior alignment.

## Verification

Use `examples/comparison-contract-demo.json` to check the synthetic static contract. In the **real product**, verify actual selection, legend, series, matrix columns, missing values and final scroll reachability. Passing a synthetic fixture is **not** proof the real application passed.
