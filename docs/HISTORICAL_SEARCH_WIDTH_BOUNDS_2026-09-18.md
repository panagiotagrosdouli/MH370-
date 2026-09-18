# Searched-width geometry inside the 33–36S residual band — 2026-09-18

## Primary-source correction

The First Principles Review states that between approximately 32.8S and 36S the historical ATSB-led search did **not** cover the full final 27.5 NM west / 25 NM east envelope.

Within this northern band, the searched widths varied approximately:
- east of the 7th arc: 12–17 NM;
- west of the 7th arc: 10–21 NM.

The final envelope itself is 27.5 NM west and 25 NM east.

## Immediate geometric consequence

Even before individual holiday/LPD polygons are recovered, there is a distinct class of residual seabed:

**OUTSIDE_HISTORICAL_SEARCH_WIDTH_BUT_INSIDE_FINAL_ENVELOPE**

At a given latitude, if the historical searched half-widths are w_W and w_E, the nominal cross-arc strips left outside them are:

west residual width = 27.5 - w_W
east residual width = 25.0 - w_E

Using only the published width ranges, not interpolating latitude-specific widths:
- west residual width ranges from 6.5 to 17.5 NM;
- east residual width ranges from 8 to 13 NM.

Combined, the potentially unsearched cross-arc width inside the final envelope ranges from roughly 14.5 to 30.5 NM depending on latitude/search geometry.

These are width bounds, not areas and not location probabilities.

## Why this matters

The residual problem has two fundamentally different components:

A. seabed inside the historical searched swath but with holiday/LPD/terrain/shadow limitations;
B. seabed inside the final 27.5W/25E envelope but outside the narrower historical search swath.

Component B does not require the 12,708 holiday polygons to exist: it follows from the published search-width geometry itself.

Therefore the residual-grid schema must carry separate states:
- INSIDE_HIGH_CONFIDENCE_SEARCH
- INSIDE_LOWER_CONFIDENCE_OR_HOLIDAY
- OUTSIDE_HISTORICAL_SEARCH_WIDTH
- UNKNOWN_GEOMETRY

Do not collapse B into the Table 4.1 holiday inventory.

## Conservative computation rule

Until latitude-specific search-boundary polygons are recovered, do not assign exact B cells. Instead compute a sensitivity bracket using the published width extrema.

For a cross-track distance d:
- west side definitely outside historical width if |d| > 21 NM;
- west side possibly outside if 10 < |d| <= 21 NM;
- east side definitely outside if d > 17 NM;
- east side possibly outside if 12 < d <= 17 NM.

This bracket is intentionally conservative and must be replaced by actual search polygons.

## Relation to the 2016 residual area

The First Principles Review identified an approximately 25,000 km2 unsearched area between 33S and 36S along the 7th arc as having the highest probability at that time. This is historically important but is not a current unsearched-area figure after Ocean Infinity's later searches.

OI 2018 and 2025–26 exact spatial coverage must be overlaid before any present-day residual area is claimed.

No wreckage coordinate is inferred here.
