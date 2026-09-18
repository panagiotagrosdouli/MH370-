# DSTG figure target audit — 2026-09-18

## Primary digitisation target identified

The ATSB-hosted pre-publication draft exposes Fig. 1.1 on printed page 3:
"Probability density function of final location of MH370. Indicative search area (as of November 2015) marked with solid black line."

This is a final-location density product, not merely a BTO arc or trajectory illustration. The indexed PDF representation exposes geographic axes approximately longitude 82–98E and latitude extending to about 41S, plus a quantitative colour bar with values roughly 0.5–2.5.

Chapter 10 (Application to the MH370 Accident, pp. 87–100) is the detailed source chapter and must be inspected for the corresponding end-of-flight construction.

## Critical correction to pipeline semantics

Chapter 10.5 states that the particle-filter output is the aircraft-state PDF at 00:19, while the final-location PDF is produced by applying an ATSB/search-team end-of-flight transition distribution:

p(x_final|Z_K) = integral p(x_final|x_K) p(x_K|Z_K) dx_K.

Therefore Fig. 1.1 is NOT a DSTG-only pre-EOF posterior. It already contains an end-of-flight transition kernel.

Consequences:
- Fig. 1.1 may be digitised as a combined DSTG+EOF physics product.
- It MUST NOT then be multiplied by our separate EOF hypothesis mixture.
- For a modular DSTG-only + explicit H_U/H_G/H_C model, the preferred target is the 00:19 particle-filter state/location distribution before section 10.5's descent transition.

## Additional later product

ATSB's Operational Search report says the November 2016 refined 2-D PDF (Figure 57) incorporated a reduced approximately +/-25 NM end-of-flight descent-kernel width into the DST Group 2-D PDF. This is another combined product and likewise cannot receive a second EOF likelihood.

## Recovery priority

P1: recover/digitise the pre-EOF 00:19 particle-filter location/state distribution from Chapter 10 if a quantitatively interpretable figure is available.
P2: digitise Fig. 1.1 as a combined DSTG+EOF validation/reference product.
P3: digitise ATSB Figure 57 as a later combined DSTG+refined-EOF reference product.

The three products must remain separately labelled and must never be multiplied together.
