# End-to-end BFO forward-model gate — 2026-09-18

All major terms required by the primary Inmarsat/DSTG BFO equation are now represented in code: aircraft/satellite uplink Doppler, satellite/GES downlink Doppler, AES nominal-GEO compensation, measured satellite+EAFC correction, and fixed frequency bias.

A new end-to-end validator is added for the stable 19:41–00:11 Table-9 trajectory. Crucially, it does not embed the published predicted BFO component values; it computes the geometry terms and reads the primary EAFC time series. Satellite state vectors remain an explicit input so that interpolation assumptions are visible and testable.

Acceptance criterion remains the primary example's measured-minus-predicted RMS of about 2.68 Hz. Because the Table-9 aircraft positions, tracks and speeds are rounded, exact equality is neither expected nor a legitimate tuning target. Failure materially above the few-Hz scale blocks descent inference.

The final 00:19:29 point is intentionally excluded from fitting/validation. Only after the stable segment passes will its residual be converted into a vertical-speed likelihood. This prevents circularly calibrating the model on the signal we want to interpret.

Status: END_TO_END_BFO_VALIDATOR_IMPLEMENTED / SATELLITE_STATE_FEED_REQUIRED / EOF_POINT_HELD_OUT.
