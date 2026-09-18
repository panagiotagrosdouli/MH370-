# BFO component-bookkeeping validation — 2026-09-18

Primary Inmarsat Table 9 is now encoded as a deterministic unit test before geometric Doppler terms are implemented.

For every row, the published predicted BFO is exactly reconstructed by summing:
aircraft uplink contribution + satellite uplink contribution + downlink Doppler + aircraft compensation + combined satellite/AFC term + fixed bias.

For 19:41–00:11 the measured-minus-predicted residuals are +3, -2, -2, +1, -5, 0 Hz, RMS 2.68 Hz. At 00:19:29 the residual is -74 Hz.

This test isolates sign/bookkeeping mistakes from geometry mistakes. The next forward-model stage must independently reproduce each component from ECEF state/velocity and the published compensation/AFC conventions, then pass this exact table test.

ATSB/DSTG Eq. 5.6 independently confirms the same component structure. The Inmarsat paper explicitly warns that the example route is not uniquely valid; it is a validation trajectory, not a wreckage coordinate.

Status: BFO_BOOKKEEPING_UNIT_TEST_READY / GEOMETRIC_COMPONENT_RECONSTRUCTION_NEXT.
