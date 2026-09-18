# Official sonar non-detection calibration — 2026-09-18

## Evidence recovered from ATSB Operational Search report

The final search coverage classes are explicitly calibrated:

- High Confidence Coverage: 97.4% of combined area; definition >95% confidence of detection.
- Lower Confidence Coverage: 2.1% of combined area; approximately 70% average confidence of detection.
- Data Gaps: 0.5% of combined area; zero confidence of detection.

These are aggregate coverage statistics using a 100 m x 100 m gap metric. They are not permission to assign the same Pd to every point in a class without the underlying polygons.

The official legend separates Lower Probability Detection, Sonar Coverage, Data Holidays, Equipment Failure, Terrain Avoidance, Shadow Zones and Offtracks.

## AUV holiday infill

Official AUV campaign aggregate:
- Filled with good AUV data: 77.60%
- Converted to LPD: 18.99%
- No change: 2.84%
- Reduced below the 100 m holiday criterion: 0.57%

This matters because a nominal 'AUV revisit' cannot automatically be treated as successful exclusion. Nearly one fifth of the targeted holiday area became LPD after AUV acquisition.

## Small-gap filtering warning

The ATSB report states that filtering gaps/LPDs below 200 m x 200 m removes 78% of individual gap objects and 60% of individual LPD objects, but only 24% and 7% of their respective total areas.

Therefore the residual model must preserve original polygons and attach a size flag rather than deleting sub-200m features during ingestion.

## 2022 local review calibration

For the 40 NM review around the proposed WSPR location, GA reported 72.79 km2 of gaps/LPDs:
- additional missing data 1.57 km2
- equipment failure 5.37
- LPD 48.91
- off-track 0.17
- terrain avoidance 8.44
- shadow zones 8.33

This is a local review, not a global 33–36S calibration.

## Fail-closed modelling rule

Until authoritative class polygons are recovered:

`pd_lower_bound` / `pd_reference` may be attached only to a documented class, never inferred from WMS alpha coverage.

Recommended likelihood representation once polygons exist:
- High Confidence: preserve an interval, Pd > 0.95, rather than silently hard-code 0.95 as exact.
- Lower Confidence / LPD: central reference around 0.70 only where the ATSB class definition applies; sensitivity range required.
- Data Gap: Pd = 0.
- Unclassified catalogue/WMS footprint: Pd = NA.

Search non-detection likelihood remains `1 - Pd(x)`.

No coordinate is produced by this calibration alone.
