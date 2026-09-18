# Held-out 00:19:29 ECEF vertical-speed sweep — 2026-09-18

The verified BFO forward model has now been extended to the held-out 00:19:29 log-on request without using that measurement in the stable-path validation.

Conditioning geometry is the published illustrative Ashton Table-9 endpoint: 34.7 S, 93.0 E, track 180 deg, groundspeed 829 km/h, with 10 km altitude and linearly interpolated published I-3F1 ECEF state at 00:19:29.

Numerical result:
- level-flight prediction: 256.800 Hz;
- measured BFO: 182 Hz;
- exact local vertical sensitivity from the ECEF uplink geometry: 1.75853 Hz per 100 ft/min downward;
- zero-warm-up central descent matching 182 Hz: 4253.5 ft/min.

This independently recovers the same scale as the ATSB approximation of -1.7 Hz per 100 ft/min. The earlier simple repository mapping (~4350 ft/min using 256 Hz and 1.7) is therefore directionally correct; the first-principles kernel gives ~4254 ft/min for this specific illustrative geometry.

The ATSB boundary analysis remains broader: approximately 3,800–14,200 ft/min for the 00:19:29 message after allowing heading, ±3 sigma BFO error and OCXO warm-up. The central 4254 ft/min result must not replace those uncertainty bounds.

This is an EOF state constraint, not a crash coordinate. It is conditional on the illustrative endpoint geometry and does not justify multiplying an EOF kernel into DSTG products that already incorporate EOF assumptions.

Status: HELD_OUT_0019_EXECUTED / CENTRAL_ZERO_WARMUP_4254_FPM / ATSB_BOUNDS_RETAINED.
