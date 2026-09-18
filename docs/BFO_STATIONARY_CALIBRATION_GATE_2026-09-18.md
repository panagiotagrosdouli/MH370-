# BFO ECEF kernel stationary calibration gate — 2026-09-18

ATSB Appendix G and the Inmarsat paper provide a clean 16:30 stationary-aircraft calibration row: aircraft 2.75N, 101.71E, ground speed 0; I-3F1 ECEF position/velocity is published; target uplink Doppler is -6 Hz and target downlink Doppler is -85 Hz. The measured satellite+GES AFC offset is +29 Hz and inferred fixed bias is +150 Hz, yielding measured BFO 88 Hz.

A dedicated executable test now feeds those primary values into our ECEF kernel. This is the first geometry/sign-convention gate. No AFC fitting is involved.

One implementation caveat is now explicit: satellite and GES ECEF velocities must be represented in the same rotating/inertial convention as the source equation. If the stationary calibration misses the -6/-85 Hz targets, the likely first suspect is frame handling rather than an arbitrary bias adjustment. The test must fail visibly; constants must not be tuned to force agreement.

Status: STATIONARY_GEOMETRY_TEST_ADDED / NUMERICAL_EXECUTION_REQUIRED.
