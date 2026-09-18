# Evidence-grade BTO arc equation implemented — 2026-09-18

The primary Inmarsat calibration definition is now sufficiently explicit to remove the previous arc-equation blocker.

Ashton et al. report 17 known-position KLIA measurements and mean fixed timing bias -495679 us. Their calibration table shows total GES-satellite-AES path length and transmission delay, establishing the convention. The in-flight satellite-to-aircraft range is obtained after removing the satellite-to-Perth-GES leg from the calibrated total path.

Implemented equation:

R_sat-AES = 0.5*c*(BTO - bias) - R_sat-GES

with WGS84 aircraft ECEF at an explicitly assumed altitude (default 10 km), published I-3F1 ECEF state, and published Perth GES ECEF coordinates.

The solver scans latitude and root-solves longitude for the constant satellite-to-aircraft range. It emits a geographic arc, not a posterior. Altitude sensitivity and interpolation of the satellite state remain explicit systematic-error tests.

The source reports that the 17-point calibration had maximum total-path error 17.7 km, corresponding to less than 9 km in satellite-to-aircraft distance. This is a useful independent scale check but is not substituted for the DSTG per-message likelihood model.

Next validation gate: generate the 00:19:29 arc using the interpolated 3F1 state and compare its geometry to an authoritative ATSB/GA seventh-arc line. No wreckage coordinate is inferred from this arc alone.

Status: BTO_ARC_EQUATION_IMPLEMENTED / OFFICIAL_GEOMETRY_COMPARISON_PENDING.
