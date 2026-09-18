# Fuel/performance evidence contract — 2026-09-18

Authoritative ATSB fuel evidence is treated as a temporal feasibility constraint, not an invented cell-level spatial likelihood.

ATSB records the final ACARS transmission at about 17:07 as containing fuel remaining. The 2015 flight-path update states that by 00:19 the aircraft had been airborne 7 h 38 min and fuel exhaustion was a distinct possibility; loss of both engine-driven AC sources followed by APU auto-start was examined as a mechanism for the final SDU log-on.

Modelling rules:
- no constant hourly-burn extrapolation;
- keep fuel/endurance uncertainty explicit;
- do not treat the 00:19 log-on as independent evidence when an EOF/fuel model is conditioned on that event;
- preserve simulator fuel-system limitations noted by ATSB;
- require authoritative performance data before constructing a finer fuel likelihood.

Status: AUTHORITATIVE_CONSTRAINT / FULL_TIME_RESOLVED_PERFORMANCE_MODEL_PENDING.
