# BFO primary-semantics correction — 2026-09-18

Primary-source review changes an important earlier guard. Ashton et al. state that the first aircraft Logon Request BFO at 18:25:27 and 00:19:29 is consistent and usable; the intervening 18:25:34–18:28:15 values and 00:19:37 should be discounted for their flight-path reconstruction. Thus 00:19:29 BFO=182 Hz must not be globally labelled unusable.

DSTG and later EOF analyses may treat transient messages differently for particular filters/models. Therefore usability is model-specific, not a single Boolean property of the raw observation.

New rule: preserve raw BFO values and attach `use_context`: ASHTON_REFINED_PATH, DSTG_PARTICLE_FILTER, EOF_DESCENT_HYPOTHESIS. Never overwrite the observation with one model's inclusion rule.

Ashton Table 9 example gives, for an illustrative southbound path at 00:19:29, predicted BFO about 256 Hz versus measured 182 Hz, residual -74 Hz. This is evidence for a large vertical-motion contribution under that trajectory assumption, not a unique geographic location.

The BFO model requires satellite motion, aircraft horizontal velocity, aircraft Doppler compensation, GES AFC/satellite correction and frequency bias. The next implementation should reproduce the pre-00:11 low residuals before interpreting the final-handshake residual.

Status: 001929_BFO_RESTORED_AS_CONTEXT_USABLE / MODEL_SPECIFIC_USAGE_REQUIRED / BFO_RECONSTRUCTION_GATE_DEFINED.
