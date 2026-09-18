# Audit of derived WMS sonar coverage — 2026-09-18

## Result

A public MH370 analysis repository contains reproducible polygons derived from official AusSeabed WMS sonar imagery. They are useful as an independent discovery/cross-check layer, but they are **not evidence-grade search-negative geometry** and must not be converted directly into probability of detection.

## Recovered layer names

The extraction script identifies these AusSeabed WMS layers:

- `MH370_Phase_2_Sonar_Imagery_Backscatter_Inverse_Autonomous_Underwater_Vehicle__SSS__5m_2018`
- `MH370_Phase_2_Sonar_Imagery_Backscatter_Inverse_Deep_Tow__SSS__5m_2018`
- `MH370_Phase_2_Sonar_Imagery_Backscatter_Wide_DHJ__SAS__5m_2018`
- Phase-1 bathymetry: `Southern_Indian_Ocean__MH370__Bathymetry__150m_2017`

The derived dataset reports 43 AUV polygons, 2 deep-tow polygons and 12 DHJ/SAS polygons.

## Extraction audit

The polygons were produced from a single WMS GetMap image over 85–100E / 42–20S at 1500 x 2200 pixels. Coverage is inferred from non-transparent pixels, then morphologically closed, contours smaller than 50 pixels are removed, and polygons are simplified by 0.02 degrees (~2 km).

Those operations destroy precisely the information needed for cell-level negative evidence:

1. alpha>0 establishes rendered imagery, not documented detection confidence;
2. morphological closing can fill narrow real gaps;
3. the 50-pixel filter can delete small holidays;
4. 0.02-degree simplification can erase/narrow gaps at kilometre scale;
5. a WMS rendering cannot encode the official High/Lower/Gap confidence classes by itself.

Therefore these polygons are classified:

`DERIVED_WMS_CROSSCHECK_ONLY`

They may be used to test gross coverage topology and identify candidate AOIs for authoritative retrieval, but not as `P_D(x)`.

## Important independent observation

The recovered AUV polygon coordinates include a long feature running approximately from 36.3S/91.5E through the mid-35S/92E region toward 34.1S/93.9E. This confirms that the evidence-supported 33–36S corridor intersects real Phase-2 AUV imagery. It does **not** imply complete coverage of that corridor.

The recovered DHJ/SAS polygons also include broad coverage around roughly 35.2–35.8S / 92.0–92.8E.

These are discovery facts from the derived WMS geometry, not candidate wreck coordinates.

## Decision

Do not import these polygons into the Bayesian search-negative term as authoritative coverage.

Use them only to:
- validate that the AusSeabed API/WMS returns expected Phase-2 products;
- target official bundle/URI retrieval;
- compare authoritative coverage geometry once recovered;
- flag disagreements between WMS-derived and official GIS geometry.

The evidence gate remains: obtain authoritative coverage/holiday/LPD semantics before assigning `P_D(x)`.
