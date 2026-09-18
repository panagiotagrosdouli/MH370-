# BTO calibration audit — 2026-09-18

A public independent reference dataset reports a BTO bias of -495679 us, Perth GES at 31.802S 115.889E, and a 4600 us correction for AES-initiated log-on BTO. These values are useful discovery/benchmark inputs, but the bias is not promoted to AUTHORITATIVE until its exact primary ATSB/DSTG definition and sign convention are recovered.

A key inconsistency was found in that independent dataset: its comments state R600 log-on noise sigma 62 us, but the accident rows at 18:25 and 00:19 are labelled R1200 with sigma 29 us. Our earlier dataset likewise should not infer the channel/noise class from the correction rule. The 4600 us log-on correction and R600-vs-R1200 noise model are separate semantics.

Therefore:
- corrected BTO values 12520 us and 18400 us remain usable as primary-crosschecked timing values;
- message channel/noise sigma for the log-on rows remains UNRESOLVED in our evidence-grade RAW_SATCOM likelihood until checked directly against DSTG Table 10.1 / signalling documentation;
- do not use the external -495679 us bias in the arc solver until the calibration equation is reproduced at a known aircraft position.

This audit prevents a subtle failure mode where a correct BTO number is paired with the wrong measurement variance.

Status: EXTERNAL_CONSTANTS_AUDITED / LOGON_NOISE_SEMANTICS_UNRESOLVED / BIAS_PRIMARY_DEFINITION_PENDING.
