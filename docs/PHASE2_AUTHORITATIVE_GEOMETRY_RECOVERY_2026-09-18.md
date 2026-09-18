# Authoritative Phase-2 residual-geometry recovery strategy — 2026-09-18

Fresh primary-domain web searches for a publicly indexed machine-readable Phase-2 "data holiday" polygon export returned no result. This negative discovery result does not imply that the geometry is unavailable; it means the exact authoritative polygon file is not discoverable through the current public web index.

The project therefore switches from filename guessing to a provenance-preserving recovery ladder:

1. Preferred: original iy57 Phase-2 GIS geodatabase / holiday feature class from the archived NCI collection.
2. Acceptable: an exact AusSeabed/API export whose source URI resolves to iy57 and whose polygon attributes retain holiday class/mission provenance.
3. Cross-check only: rendered WMS-derived polygons or third-party reproductions.
4. Rejected: schematic rectangles, manually traced coverage, or polygons whose aggregate area/count cannot reproduce ATSB Table 4.1.

Evidence-grade acceptance tests for an imported residual polygon set:
- CRS and geometry validity explicit.
- 12,708 residual polygons total unless the export is a documented subset.
- aggregate area approximately 3,078.12 km2.
- class reconciliation: Equipment Failure 88 / 17.10 km2; Offtracks 8 / 19.20; Shadow 5,026 / 312.94; Terrain Avoidance 146 / 218.79; LPD 7,440 / 2,510.09.
- no automatic assignment of Pd=0.70 to each LPD polygon; 70% is an aggregate lower-confidence calibration anchor.
- original/source URI retained for every feature batch.

Until one of the first two provenance routes passes these checks, the evidence-grade residual ranker remains fail-closed and no cell-level wreckage coordinate is defensible.

Status: PUBLIC_INDEX_SEARCH_NEGATIVE / RECOVERY_LADDER_LOCKED / FINAL_RANKING_FAIL_CLOSED.
