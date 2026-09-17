# GA Phase 2 data-access verification

## Verified public data path

Geoscience Australia / Research Data Australia identifies the Phase 2 raw and processed collection as DOI `10.4225/25/5B0CD2B84A2DC` (GA dataset 120962). It contains high-resolution raw and processed data acquired September 2014–January 2017 by Fugro Equator, Fugro Supporter, Fugro Discovery, Havila Harmony, Dong Hai Jiu 101 and Go Phoenix, covering >121,000 km².

AusSeabed documentation explicitly states that its **MH370 Database Search** tool can spatially query and download the full Phase 2 collection stored on the National Computational Infrastructure (NCI). The portal also supports GeoTIFF downloads and spatial clipping.

The 5 m visualisation collection (GA dataset 120969, DOI `10.4225/25/5B0CD3B139DEF`) is an overview only. GA recommends the higher-resolution raw/processed collection for detailed interrogation.

## Verified 2022 negative-evidence constraint

GA's 2022 review around the proposed WSPR location examined ~4,900 km² of high-resolution Phase 2 data out of a requested ~17,000 km². It documented 72.79 km² of holidays/LPD, comprising 1.57 additional missing data, 5.37 equipment failure, 48.91 LPD, 0.17 off-track, 8.44 terrain avoidance and 8.33 shadow zones. Some holidays were large enough to contain an aircraft debris field and require new acquisition to exclude.

This is a local constraint around that proposed location; it must not be extrapolated as a spatial mask over the entire 33–36°S corridor.

## Runtime status

The current computation container cannot resolve `warehouse.ausseabed.gov.au` (DNS failure). This is a runtime-network limitation, not evidence that the GA service or data are unavailable. Web-indexed official sources show the AusSeabed portal and MH370 database-search workflow are live.

## Model consequence

No cell-level sonar `P_D` will be fabricated. Until the actual coverage/holiday geometries are retrieved, the residual posterior remains:

`R(L) ∝ P_physics(L) × L_drift(L) × L_EOF(L)`

with search non-detection applied only where geometry and search quality are spatially supported. Ocean Infinity 2025/26 remains unallocated until exact geometry is public.
