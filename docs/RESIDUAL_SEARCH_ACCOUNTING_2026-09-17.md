# Residual Search Accounting — 2026-09-17

## New primary-source constraint

ATSB/Fugro Summary Report All Vessels Table 4.1 gives the end-of-search inventory of **remaining** data holidays and Lower Probability of Detection (LPD) polygons across the operational search, including Go Phoenix and Dong Hai Jiu 101.

| Class | polygons | area km² |
|---|---:|---:|
| Equipment failure | 88 | 17.10 |
| Offtracks | 8 | 19.20 |
| Shadow zones | 5,026 | 312.94 |
| Terrain avoidance | 146 | 218.79 |
| LPD | 7,440 | 2,510.09 |
| **Total** | **12,708** | **3,078.12** |

True no/poor-coverage holidays excluding LPD total **568.03 km²**. LPD dominates the residual inventory by area: **81.55%** of the 3,078.12 km² aggregate.

This is materially stronger than using the 72.79 km² figure from the later GA 2022 review as if it described the full historical search. The 72.79 km² value is local to the specific 2022 review footprint; Table 4.1 is the end-of-operational-search aggregate inventory.

## Bayesian consequence

Do not map aggregate areas onto arbitrary cells. For a location L:

    P(L | D, ND) ∝ P0(L) × L_drift(L) × L_EOF(L) × [1 - Pd(L)]

The Table 4.1 totals constrain the *amount* of residual low-detection area but not its position. Spatial negative evidence remains UNALLOCATED until authoritative polygons or a validated derivative are available.

## WMS-derived coverage: useful but not Pd geometry

A public reproducible implementation extracts Phase-2 sonar coverage from the GA/AusSeabed WMS. It identifies these WMS layers:

- AUV SSS 5 m: `ausseabed:MH370_Phase_2_Sonar_Imagery_Backscatter_Inverse_Autonomous_Underwater_Vehicle__SSS__5m_2018`
- Deep Tow SSS 5 m: `ausseabed:MH370_Phase_2_Sonar_Imagery_Backscatter_Inverse_Deep_Tow__SSS__5m_2018`
- DHJ SAS 5 m: `ausseabed:MH370_Phase_2_Sonar_Imagery_Backscatter_Wide_DHJ__SAS__5m_2018`

Its coverage polygons are derived from rendered WMS alpha masks, with morphological closing and ~2 km simplification. They are therefore valid as a REFERENCE coverage envelope / retrieval cross-check, not as authoritative data-holiday or cell-level Pd geometry. In particular, morphological closing can erase exactly the small gaps we are trying to identify.

## Official 7th Arc service verified

The GA ArcGIS service `7thArc_SingleLine` is verified as service item `4c94d33cfc144f7d8b78943dee56e29b`, spatial reference EPSG:4326, with copyright attribution `ATSB. Satellite and aircraft specialists`. The service description states that independent satellite-communications and aircraft-performance analysis places MH370 in close proximity to the 7th Arc.

The current container cannot resolve `services1.arcgis.com`, so direct GeoJSON retrieval failed. This is a runtime DNS limitation, not evidence that the service is unavailable. The indexed ArcGIS REST service is still discoverable.

## Evidence gates after this pass

1. SATCOM/7th-Arc provenance: PASS for official service identity; geometry bytes still to ingest.
2. Full-search residual area accounting: PASS at aggregate level (Table 4.1).
3. WMS sonar layer identity: PASS as reference/retrieval lead.
4. Cell-level sonar Pd: FAIL / UNALLOCATED.
5. Exact remaining holiday/LPD polygons: FAIL / not recovered.
6. OI 2025–26 cell geometry: FAIL / UNALLOCATED.
7. Physical discovery: NOT CLAIMED.

## Immediate computational rule

Until geometry is recovered, any residual ranking must report two separate outputs:

- physics/drift/EOF prior ranking without spatial sonar penalty;
- sensitivity bounds showing what would happen if an unresolved holiday/LPD overlaps a high-prior cell.

No single coordinate may be promoted as an evidence-grade wreckage location from the aggregate Table 4.1 statistics.