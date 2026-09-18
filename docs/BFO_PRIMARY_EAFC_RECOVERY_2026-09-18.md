# Primary satellite + EAFC time series recovered — 2026-09-18

ATSB Flight Path Analysis Update (30 July 2015), Table 4, publishes the combined satellite translation-frequency variation and Perth GES EAFC correction. Primary values (Hz): 16:30 +29.1; 16:42 +27.6; 16:55 +25.8; 17:07 +24.1; 18:25 +10.7; 19:41 -0.5; 20:41 -1.5; 21:41 -18.0; 22:41 -28.5; 00:11 -37.7; 00:19 -37.8.

ATSB explains that these were recovered from a fixed-frequency L-band Pilot sent from Burum through I-3F1 and measured at Perth after the EAFC-controlled conversion. Thus this is empirical primary calibration, not a term to synthesize from orbital geometry.

The Perth EAFC could not accept negative latitude for a southern-hemisphere GES and therefore only partially removed C-band Doppler. The measured combined satellite+EAFC effect is the correct primary input.

Consequence: the previous full-BFO blocker is removed. We now have geometric uplink/downlink Doppler, reconstructed AES compensation, measured satellite+EAFC correction, and fixed bias. Next gate: reproduce Table-9 total predicted BFO without copying its component outputs.

Status: PRIMARY_EAFC_SERIES_RECOVERED / FULL_BFO_FORWARD_MODEL_UNBLOCKED.
