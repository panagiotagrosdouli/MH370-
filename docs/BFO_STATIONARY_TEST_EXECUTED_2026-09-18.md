# Stationary BFO calibration executed — 2026-09-18

The first-principles ECEF Doppler kernel has now been numerically executed against the ATSB Appendix G 16:30 stationary-aircraft calibration case.

Primary inputs:
- aircraft: 2.75 N, 101.71 E, ground speed 0;
- I-3F1 ECEF: (18122.9, 38080.0, 828.5) km;
- I-3F1 ECEF velocity: (0.00216, -0.00107, 0.06390) km/s;
- Perth GES geodetic: approximately 31.802 S, 115.889 E;
- uplink 1646.6525 MHz; downlink 3615.1525 MHz.

Independent kernel output:
- uplink Doppler = -6.095 Hz, published target -6 Hz;
- downlink Doppler = -84.587 Hz, published target approximately -85 Hz.

Residuals are about -0.095 Hz and +0.413 Hz respectively. No BFO bias or AFC term was fitted to obtain this agreement.

This passes the stationary geometry/sign-convention gate at sub-Hz scale and strongly reduces the risk of a basic LOS sign or ECEF geometry error. It does not yet validate aircraft-velocity Doppler compensation or the time-varying empirical satellite/GES frequency-translation correction.

Primary ATSB Appendix G states that the Perth AFC hardware only partially compensates downlink Doppler and its translation frequency cannot be recovered by simple arithmetic; its effect is measured. Therefore that term remains empirical and will not be synthesized.

Status: STATIONARY_ECEF_DOPPLER_GATE_PASSED / UPLINK_ERROR_0.095_HZ / DOWNLINK_ERROR_0.413_HZ / AIRCRAFT_COMPENSATION_NEXT.
