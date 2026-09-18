# Local residual-gap prioritisation contract — 2026-09-18

The 2022 Geoscience Australia review is useful as a worked example of how residual sonar gaps should be prioritised, but it is local evidence around a proposed location and must not be extrapolated to the full 33–36S corridor.

Within the requested 17,000 km2 review area, about 4,900 km2 had Phase-2 high-resolution data. GA reports 72.79 km2 of holidays/LPD in that reviewed high-resolution footprint:
- additional missing data 1.57 km2
- equipment failure 5.37 km2
- lower probability of detection 48.91 km2
- off-track 0.17 km2
- terrain avoidance 8.44 km2
- shadow zones 8.33 km2

The largest documented holiday/LPD was about 21.7 km2 and was long and narrow. GA states that some holidays are large enough to contain an aircraft debris field and would require new data acquisition to exclude them.

Inference rule: a polygon becomes a high-value residual target only through intersection of (1) authoritative gap/LPD geometry, (2) physics/drift/EOF support, and (3) search non-detection likelihood. Gap area alone is not a ranking criterion.

Priority semantics:
DATA_GAP / EQUIPMENT_FAILURE / OFF_TRACK: unsounded or missing-data mechanisms; Pd cannot be invented from category name alone except where the authoritative search classification explicitly assigns zero confidence.
SHADOW_ZONE / TERRAIN_AVOIDANCE: bathymetry-dependent; require geometry and acquisition context.
LOWER_PD: use source-supported Pd interval/sensitivity, not an exact per-polygon 0.70.

Status: LOCAL_GAP_ACCOUNTING_VERIFIED / AUTHORITATIVE_POLYGON_INTERSECTION_PENDING.
