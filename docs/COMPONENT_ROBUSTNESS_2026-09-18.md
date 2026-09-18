# Residual-component robustness — 2026-09-18

The pipeline now measures whether a connected residual component survives the full sensitivity/ablation suite.

For each component it reports:
- median, best and worst rank across scenarios;
- fraction of scenarios in the top 3;
- mean/min/max posterior mass;
- coefficient of variation of posterior mass.

These are stability diagnostics, not a new probability and not an excuse to collapse model uncertainty into an arbitrary composite score.

A component is scientifically more interesting when its prominence is persistent across plausible Pd choices and leave-one-evidence-out runs. The code intentionally reports the diagnostics separately rather than manufacturing a weighted robustness number.

Required input is scenario-level component ranking after authoritative geometry, Pd sensitivity and evidence ablations. Missing scenario coverage fails closed.

No present component can be evaluated yet because the authoritative spatial evidence gates remain open.
