# Satellite-state feed connected to end-to-end BFO validator — 2026-09-18

The published Inmarsat I-3F1 ECEF position/velocity table is now wired into the independent BFO forward model. For each 19:41–00:11 validation timestamp the code linearly interpolates both published position and published velocity between bracketing operator-table epochs, then computes the full BFO from geometry + AES compensation + primary ATSB satellite/EAFC correction + fixed bias.

This is intentionally a transparent baseline interpolation. The previously benchmarked 00:19 position interpolation differed from an independent high-resolution GMAT propagation by only about 0.67 km, but BFO is velocity-sensitive, so velocity interpolation remains a separate systematic-error term.

The 00:19:29 observation remains held out. No final-handshake BFO is used to tune satellite state, AES compensation, AFC correction or bias.

Execution note: repository code is now complete for the stable-segment RMS test, but GitHub connector execution is not a Python runtime. The next numerical execution must run the checked-in scripts in a Python environment; no RMS value is claimed until that execution occurs.

Status: SATELLITE_STATE_FEED_CONNECTED / END_TO_END_CODE_COMPLETE / NUMERICAL_RMS_EXECUTION_PENDING.
