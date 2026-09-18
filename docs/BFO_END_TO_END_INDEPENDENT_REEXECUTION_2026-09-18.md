# Independent BFO end-to-end re-execution — 2026-09-18

The repository BFO forward model was independently re-executed from the current source equations and the committed Inmarsat 3F1 ECEF state table, rather than accepting the earlier recorded result.

Stable pre-EOF validation results (predicted, measured, residual measured-predicted), Hz:
- 19:41:03: 109.113, 111, +1.887
- 20:41:05: 143.992, 141, -2.992
- 21:41:27: 170.566, 168, -2.566
- 22:41:22: 204.305, 204, -0.305
- 00:11:00: 252.529, 252, -0.529

Independent RMS residual: 1.973 Hz.

This closely confirms the earlier repository claim (~2.0 Hz) but not every previously rounded number exactly. The discrepancy is small and attributable to exact reproduction/rounding details; the evidence-grade statement should therefore be “approximately 2 Hz stable-path RMS,” with this re-execution as the current numerical audit.

No parameter was fitted to these five residuals during this re-execution. The 00:19:29 point remains held out from stable-path validation and is reserved for EOF/descent testing.

Consequence: the BFO forward-model implementation is no longer an unexecuted verification debt. It reproduces the published illustrative stable path at ~2 Hz RMS using the committed satellite-state table, AES compensation, primary sat+EAFC correction series, and fixed 150 Hz bias.

Status: BFO_END_TO_END_REEXECUTED / STABLE_RMS_1.973_HZ / 0019_HELD_OUT.
