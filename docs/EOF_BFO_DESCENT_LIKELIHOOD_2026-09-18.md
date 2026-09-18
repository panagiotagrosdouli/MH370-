# Held-out 00:19:29 BFO descent likelihood — 2026-09-18

The stable-segment independent BFO forward model passed at 2.002 Hz RMS without using the 00:19:29 observation. The final log-on request can therefore be treated as held-out EOF evidence.

For the illustrative southbound trajectory, our validated level-flight prediction is approximately 256 Hz and the measured 00:19:29 BFO is 182 Hz, a residual of -74 Hz. ATSB's 2016 EOF analysis gives approximately -1.7 Hz BFO change per 100 ft/min descent at locations consistent with the search area. With zero OCXO warm-up contribution, the central mapping is therefore about 4,350 ft/min downward.

This central value is NOT a standalone descent-rate estimate. ATSB explicitly treats the result as a range because heading, BFO error and OCXO warm-up are uncertain. Its conservative boundary analysis gives approximately 3,800–14,200 ft/min for 00:19:29. For 00:19:37 it gives approximately 14,600–25,000 ft/min, but that second transient observation has different message/model semantics and is not merged blindly into the first likelihood.

The code therefore exposes OCXO warm-up as a nuisance parameter rather than fixing it. BFO measurement scatter is anchored at sigma 4.3 Hz from the 20 previous 9M-MRO flights, while broader systematic uncertainty must be layered separately. The output is an EOF vertical-motion likelihood conditional on the horizontal trajectory, not a geographic posterior.

Search implication: ATSB reports that simulations with descent rates consistent with the final BFO generally impacted within 15 NM of the seventh arc, while some scenarios travelled rearwards about 21 NM and some remained airborne around 20 minutes. Thus this likelihood strengthens the uncontrolled/near-arc branch but does not eliminate controlled-glide sensitivity.

Status: HELD_OUT_EOF_LIKELIHOOD_IMPLEMENTED / CENTRAL_ZERO_WARMUP_4350_FPM / OFFICIAL_BOUND_3800_14200_FPM / GEOGRAPHIC_MIXTURE_NEXT.
