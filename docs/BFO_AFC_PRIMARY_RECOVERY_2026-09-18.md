# Primary satellite + EAFC time series recovered — 2026-09-18

The ATSB 30 July 2015 Flight Path Analysis Update, Appendix G Table 4, publishes the combined satellite translation plus Perth GES EAFC effect directly. This removes the last major non-geometric blocker in the BFO forward model.

The primary report explains that a fixed-frequency L-band pilot transmitted from Burum through I-3F1 was measured after the Perth receive chain. Comparing measured pilot frequency with expected satellite-motion Doppler directly determined the combined satellite translation and EAFC variation. The approach deliberately removes dependence on assumed internal behaviour of either subsystem.

Recovered values (Hz): 16:30 +29.1; 16:42 +27.6; 16:55 +25.8; 17:07 +24.1; 18:25 +10.7; 19:41 -0.5; 20:41 -1.5; 21:41 -18.0; 22:41 -28.5; 00:11 -37.7; 00:19 -37.8.

This supersedes the need to synthesize AFC from hardware assumptions. Interpolation between primary measured table values may be used only with explicit uncertainty.

The 2014 refinement report additionally states that the EAFC output was sampled every 10 seconds by a separate measurement system and that the improved method used a smoothed transfer function. The full 10-second series is not yet recovered publicly in machine-readable form, so Table 4 remains the evidence-grade public calibration series.

Status: PRIMARY_AFC_SERIES_RECOVERED / FULL_BFO_FORWARD_MODEL_UNBLOCKED / 10_SECOND_RAW_AFC_SERIES_NOT_RECOVERED.
