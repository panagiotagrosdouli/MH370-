# AES compensation test executed — 2026-09-18

The independently implemented nominal-GEO AES compensation has now been executed against the primary Inmarsat Table 9 stable southbound rows.

Computed versus published compensation, Hz:
- 19:41: -71.453 vs -72; error +0.547.
- 20:41: +142.492 vs +143; error -0.508.
- 21:41: +329.783 vs +331; error -1.217.
- 22:41: +494.859 vs +497; error -2.141.
- 00:11: +688.810 vs +691; error -2.190.

RMS component error = 1.51 Hz; maximum absolute error = 2.19 Hz. No accident BFO values were fitted.

This passes the intended sign-and-magnitude gate. The small systematic growth toward the south is retained as a modelling discrepancy, plausibly attributable to exact AES nominal constants/ellipsoid implementation/rounding of the published Table-9 trajectory. It must not be silently tuned away.

Together with the stationary test, the project now has independently validated sub-Hz LOS Doppler for the calibration case and approximately 1.5-Hz RMS AES compensation agreement on the southbound example.

The remaining full-BFO reconstruction blocker is the time-dependent satellite translation plus Perth GES AFC correction. Primary Inmarsat Table 9 provides this combined term directly (-1, -1, -18, -29, -33, -38 Hz on the late path), but a truly independent model needs the measured AFC history or an accepted primary reconstruction rule.

Status: AES_COMPENSATION_GATE_PASSED / RMS_1.51_HZ / AFC_TIME_SERIES_NEXT.
