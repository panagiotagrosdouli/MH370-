# Seventh-arc numerical reconstruction — 2026-09-18

The 00:19:29 BTO arc can now be generated from the primary calibration equation rather than copied from a map.

Inputs:
- corrected BTO 18400 us;
- fixed timing bias -495679 us;
- Perth GES ECEF (-2368.8, 4881.1, -3342.0) km;
- I-3F1 ECEF linearly interpolated from the published 00:10 and 00:20 operator states to 00:19:29;
- WGS84 ellipsoid;
- nominal aircraft altitude 10 km.

The source equation is R_sat-AES = c(BTO-bias)/2 - R_sat-GES. ATSB separately reports validation of BTO rings to about +/-10 km.

The script emits the southern arc from 45S to 20S at 0.05-degree latitude spacing and simultaneously evaluates 0, 10 and 12 km altitude assumptions. This is a geometry/systematic test, not a location posterior.

Critical limitation: the satellite state at 00:19:29 is linearly interpolated between published operator states. The generated arc remains RECONSTRUCTED_PRIMARY_INPUTS, not AUTHORITATIVE_ARC, until compared pointwise with the official GA/ATSB 7thArc_SingleLine vertices.

Status: ARC7_NUMERIC_RECONSTRUCTION_READY / OFFICIAL_VERTEX_COMPARISON_PENDING.
