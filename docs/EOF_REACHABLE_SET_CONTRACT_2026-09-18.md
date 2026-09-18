# EOF cross-arc reachable-set contract — 2026-09-18

The held-out 00:19 BFO result is now translated into an evidence-anchored cross-arc contract without inventing a Gaussian spatial likelihood.

Official ATSB evidence supports nested distance bands:
- 0–15 NM: Boeing simulations whose descent rates were consistent with the final-BFO ranges generally impacted within 15 NM of the 7th arc.
- 15–25 NM: First Principles Review concluded the aircraft was probably within 25 NM, with locations closer to the arc having higher likelihood.
- 25–40 NM: the 2016 simulation report retained ±40 NM as an envelope appropriate to encompass all uncontrolled-descent scenarios in that simulation set.
- 40–100 NM: historical 2015 decreasing-priority/glide sensitivity only; First Principles later gave substantially more weight closer to the arc.

No numerical probability mass is assigned to these bands from these statements alone. “Generally”, “probably”, and “appropriate to encompass” are not converted into arbitrary percentages.

The official map additionally gives an asymmetric final envelope: no more than 27.5 NM west and 25 NM east of the reference 7th arc for the current principal search interpretation. That asymmetry is retained separately from the older ±40 NM uncontrolled-simulation envelope.

The held-out ECEF BFO sweep (central zero-warm-up descent about 4.25k ft/min for the illustrative Table-9 endpoint) selects the class of high-descent EOF scenarios, but does not itself determine along-arc latitude or a unique post-arc trajectory. A true 2-D reachable set requires initial attitude, bank/turn dynamics, altitude, horizontal speed, control/autopilot state and OCXO/systematic uncertainty. Those variables are not identifiable from the single 00:19:29 BFO measurement.

Therefore the evidence-grade implementation uses nested support/sensitivity bands, not a fabricated 2-D density. The next geographic posterior may weight these bands only through a separately documented scenario prior or an official/DSTG EOF kernel.

Status: EOF_BANDS_EVIDENCE_ANCHORED / NO_FAKE_GAUSSIAN / NO_UNIQUE_COORDINATE.
