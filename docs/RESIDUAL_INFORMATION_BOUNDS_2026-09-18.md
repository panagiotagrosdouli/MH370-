# Residual-area information bounds — 2026-09-18

## Question

What can the verified Table 4.1 residual inventory tell us **before** the authoritative polygons are recovered?

Answer: it cannot locate MH370, but it can quantify how concentrated the residual search problem is and what kinds of geometry matter most.

## Verified inventory

ATSB/Fugro Table 4.1:
- total residual low/no-detection area: 3,078.12 km2
- LPD: 2,510.09 km2
- non-LPD holidays: 568.03 km2
- 12,708 polygons total

Derived shares:
- LPD: 81.5458%
- shadow zones: 10.1666%
- terrain avoidance: 7.1079%
- offtracks: 0.6238%
- equipment failure: 0.5555%

Thus the dominant residual-search problem is not blank seabed; it is seabed with degraded detection confidence.

## Bayesian information bounds

Let prior probability mass over a region R be M(R). If exact residual geometry is unknown, aggregate area alone cannot determine posterior mass.

For a class C with detection probability p, non-detection multiplies prior density inside C by (1-p).

Illustrative class likelihood factors from ATSB definitions:
- Data Gap: 1.0
- Lower Confidence: about 0.30 average residual likelihood
- High Confidence: <0.05 residual likelihood

Therefore, for equal pre-search prior density, a Data Gap cell can retain >20x the posterior density of a cell searched at >95% confidence. An LPD/Lower-Confidence cell at ~70% detection can retain roughly >6x the residual likelihood of a >95%-confidence cell.

These are likelihood-ratio bounds/reference comparisons, not location probabilities.

## Why geometry dominates the next step

The same 3,078.12 km2 produces radically different posterior outcomes depending on whether the polygons:
1. overlap the high physics/drift prior;
2. lie mostly outside it;
3. form many tiny isolated patches;
4. form connected/adjacent clusters large enough to contain a debris field.

Consequently, random spatial allocation of Table 4.1 totals is prohibited as a baseline result.

## Size structure

From the official report's 200m x 200m filtering result:
- most polygon *counts* are small;
- most residual *area* survives filtering.

This implies the high-value target is not simply the largest polygon count. The ranking should use connected residual area, local prior density, class-specific non-detection likelihood, and bathymetric/terrain complexity.

## Ranking statistic once geometry is recovered

For polygon/cluster j:

S_j = integral over A_j of P_physics(x) * L_drift(x) * L_EOF(x) * (1-Pd(x)) dx

Report alongside:
- area;
- class composition;
- maximum/mean prior density;
- connected-component area;
- distance/cross-track relation to official 7th Arc;
- search provenance;
- sensitivity to Pd;
- whether OI 2018/2025-26 geometry overlaps it.

No rank should be published before authoritative spatial geometry passes provenance checks.
