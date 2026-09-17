# Next computation: residual-search ranking

## Verified geometry constraints

Primary ATSB evidence places the updated SATCOM+drift high-probability region close to the 7th arc, approximately 33S–36S and mostly within ~25 NM. The First Principles Review states that between 32.8S and 36S historical coverage varied from about 12–17 NM east and 10–21 NM west of the arc, rather than covering the complete ±25 NM corridor.

## Official sonar input

Geoscience Australia dataset GA/120969 (DOI 10.4225/25/5B0CD3B139DEF) provides 5 m WGS84 GeoTIFF mosaics of Phase-2 sonar data, separated into Fugro Deep Tow, Fugro AUV, Go Phoenix and Dong Hai Jiu 101 acquisition layers. Detailed interrogation should use the higher-resolution raw/processed Phase-2 data where possible.

## Computation

For each grid cell L in the 33S–36S corridor:

R(L) ∝ P_physics(L) × L_drift(L) × L_EOF(L) × Π_k(1-P_D,k(L)).

No area-total search statistic may be converted into a spatial mask without authoritative geometry.

Required processing sequence:
1. Resolve/download GA Phase-2 WGS84 coverage/sonar tiles.
2. Derive actual surveyed footprint, overlaps, holidays/gaps and terrain-quality indicators.
3. Intersect with a geodesically constructed ±25 NM 7th-arc corridor.
4. Assign conservative cell-level P_D classes using documented sonar quality/LPD evidence rather than binary searched/unsearched labels.
5. Apply DSTG/ATSB physical prior and CSIRO drift likelihood without double-counting SATCOM evidence.
6. Keep controlled-glide 25–120 NM as a low-prior sensitivity tail only.
7. Cluster high residual-score cells and compute posterior mass and area.
8. Falsify each cluster against every available historical search layer.
9. Leave Ocean Infinity 2025/26 negative evidence spatially unallocated until exact public geometry is obtained.

## Evidence gate

Do not publish a final candidate bounding box until steps 1–8 use real machine-readable search geometry. A coordinate generated before that point is a model artefact, not a defensible localization.
