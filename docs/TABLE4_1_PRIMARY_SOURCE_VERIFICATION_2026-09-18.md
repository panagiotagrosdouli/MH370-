# Primary-source verification of end-of-search residual inventory — 2026-09-18

## Status: VERIFIED

The ATSB-hosted *Operational Search for MH370* contains the embedded Fugro document **SEARCH FOR MH370 – SUMMARY REPORT ALL VESSELS**. Section 4.1.1 / Table 4.1 directly reports the remaining data holidays and Lower Probability of Detection (LPD) inventory.

Official Table 4.1 values:

| Class | Polygon count | Area km2 |
|---|---:|---:|
| Equipment Failure | 88 | 17.10 |
| Offtracks | 8 | 19.20 |
| Shadow Zones | 5,026 | 312.94 |
| Terrain Avoidance | 146 | 218.79 |
| Lower Probability of Detection | 7,440 | 2,510.09 |

The table explicitly notes that the totals include Go Phoenix and DJ101.

Derived arithmetic, not a separately quoted ATSB row:
- total polygon count = 12,708
- total area = 3,078.12 km2
- non-LPD holiday count = 5,268
- non-LPD holiday area = 568.03 km2
- LPD share of residual area = 81.5458%

## Interpretation

This is the strongest verified aggregate accounting currently in the repository. It establishes the amount and composition of residual low/no-detection area at the end of the ATSB-led search.

It does **not** locate those 12,708 polygons.

Therefore these totals constrain residual-area mass but cannot be spatially distributed across the 33–36S corridor without authoritative geometry.

## Relationship to Figure 73

The same ATSB report gives combined coverage:
- High Confidence Coverage 97.4%
- Lower Confidence Coverage 2.1%
- Data Gaps 0.5%

and defines High Confidence as >95% detection confidence, Lower Confidence as approximately 70% average detection confidence, and Data Gaps as zero confidence.

These are compatible but conceptually different summaries:
- Table 4.1 counts/areas the remaining holiday/LPD polygon inventory.
- Figure 73 summarizes coverage-confidence fractions over the search area using the 100 m x 100 m metric.

Do not force Table 4.1 classes into Figure 73 percentages cell-by-cell.

## Size-filter consequence

The report states that filtering gaps and LPDs smaller than 200 m x 200 m removes 78% of individual gap objects and 60% of individual LPD objects, while reducing total gap area by 24% and LPD area by 7%.

Thus polygon count is dominated by small objects, while residual area is much less dominated by them.

For wreckage-search ranking:
1. retain all authoritative polygons;
2. compute polygon area and maximum inscribed / characteristic dimension where possible;
3. flag polygons incapable of fully containing a typical aircraft debris field;
4. do not simply delete them before spatial union/intersection, because clusters or adjacency can matter.

## Evidence gate update

Aggregate residual accounting: PASS / PRIMARY SOURCE VERIFIED.

Spatial allocation: FAIL / authoritative polygon geometry still required.

Physical location claim: NOT MADE.
