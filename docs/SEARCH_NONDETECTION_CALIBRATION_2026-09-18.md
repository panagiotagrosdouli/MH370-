# Search non-detection calibration — 2026-09-18

Official ATSB final-search calibration (100 m x 100 m gap metric):
- HIGH_CONFIDENCE: 97.4% of combined area; probability of detection >95%.
- LOWER_CONFIDENCE: 2.1%; average probability of detection about 70%.
- DATA_GAP: 0.5%; probability of detection 0%.

The lower-confidence 70% value is an aggregate average, not a defensible exact Pd for every LPD polygon. Evidence-grade inference must therefore sweep LPD Pd rather than hard-code 0.70 cell by cell. Likewise >95% does not identify a unique High-Confidence Pd; sensitivity values must be labelled assumptions.

AUV infill is not equivalent to erasing all holidays. ATSB reports the combined AUV outcome as 77.60% successfully filled, 18.99% converted to LPD, 2.84% no change, and 0.57% reduced below the holiday-size criterion.

ATSB also notes that filtering gaps/LPDs below 200 m x 200 m removes many polygon counts but much less total area. This is relevant to debris-field containment, but must not be used to delete small polygons before the authoritative geometry is available.

Inference contract:
P(ND|x)=1-Pd(x).
DATA_GAP uses Pd=0.
LOWER_CONFIDENCE uses a sensitivity family, not exact 0.70 per polygon.
HIGH_CONFIDENCE uses a sensitivity family constrained to >0.95.
UNKNOWN remains NA and cannot be silently promoted to a searched class.

The 2022 GA review around a proposed location is local evidence only: about 4,900 km2 of the 17,000 km2 requested review area had Phase-2 high-resolution data; documented/additional holidays and LPDs totalled 72.79 km2. It must not be extrapolated to the full 33–36S corridor.

Status: OFFICIAL_PD_CALIBRATION_VERIFIED / CELL_GEOMETRY_STILL_REQUIRED.
