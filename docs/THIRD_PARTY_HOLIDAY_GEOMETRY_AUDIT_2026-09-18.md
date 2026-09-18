# Third-party holiday geometry audit — 2026-09-18

A newly discovered public MH370 analysis repository contains a four-feature `data_holidays.geojson` and derived WMS sonar-coverage polygons. This is useful as an adversarial cross-check, not authoritative search geometry.

## Holiday geometry rejection

The four holiday features are coarse axis-aligned rectangles with declared areas 12, 28, 18 and 8 km2. Their coordinate extents are vastly larger than those declared areas. For example, the feature declared as 12 km2 spans 93.6–94.1E and 34.7–35.0S: roughly 0.5 degrees longitude by 0.3 degrees latitude, i.e. on the order of 1,500 km2 at that latitude. Therefore these polygons cannot represent the stated holiday areas literally.

The repository itself attributes the holidays to ATSB reports, but report attribution does not make hand-encoded/coarse geometry authoritative. These features are rejected from evidence-grade ranking.

## WMS-derived coverage

The same repository documents a reproducible WMS extraction:
- alpha-mask from GA/AusSeabed rendered sonar imagery;
- morphological closing;
- contour tracing;
- minimum-area filtering;
- polygon simplification of about 0.02 degrees for sonar.

This can be useful for independent visual/coverage cross-checking. It cannot preserve small holidays reliably because closing, filtering and kilometre-scale simplification alter precisely the gaps we need to rank. It remains DERIVED_REFERENCE_ONLY, not a substitute for the original Phase-2 holiday/coverage geodatabase.

## Consequence

This discovery does not unblock authoritative polygon ranking. It does strengthen the stop rule: do not import attractive third-party GeoJSON merely because it has source labels. Validate geometric area against attributes before use.

Status: THIRD_PARTY_GEOMETRY_AUDITED_AND_REJECTED_FOR_BASELINE.
