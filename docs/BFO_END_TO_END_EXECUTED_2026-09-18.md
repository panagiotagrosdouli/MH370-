# End-to-end BFO stable-segment execution — 2026-09-18

The independent forward model has now been numerically executed on the held-in stable 19:41–00:11 validation segment using interpolated published I-3F1 state vectors, WGS84 aircraft geometry, the independently validated AES compensation, primary ATSB satellite+EAFC corrections, and 150 Hz fixed bias.

Results (predicted / measured / measured-minus-predicted, Hz):
- 19:41:03: 109.114 / 111 / +1.886
- 20:41:05: 144.015 / 141 / -3.015
- 21:41:27: 170.645 / 168 / -2.645
- 22:41:22: 204.342 / 204 / -0.342
- 00:11:00: 252.528 / 252 / -0.528

Independent residual RMS = 2.002 Hz.

The primary Inmarsat illustrative trajectory has a measured-minus-predicted RMS of about 2.68 Hz over the same stable rows. Our result therefore passes the predeclared few-Hz acceptance gate without fitting the 00:19:29 observation.

Component comparison also exposes remaining rounding/model differences, especially the aircraft uplink term at later latitudes; nevertheless cancellation in the complete physically specified model produces a stable-segment RMS near 2 Hz. This must be treated as validation of the forward calculation on this illustrative trajectory, not proof that the aircraft followed it.

The 00:19:29 BFO remains held out. It may now be evaluated as an EOF vertical-motion observation, with satellite-velocity interpolation and rounded Table-9 trajectory parameters propagated as systematic uncertainty.

Status: END_TO_END_BFO_GATE_PASSED / RMS_2.002_HZ / EOF_HELD_OUT_READY.
