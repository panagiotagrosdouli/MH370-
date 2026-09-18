# DSTG Figure 10.3 correction — 2026-09-18

## Correction

A direct inspection of the Chapter 10 text changes the previous target classification.

Figure 10.3 is NOT a two-dimensional geographic density map. The chapter explicitly says it plots the two filter PDFs "as one dimensional curves parameterised by latitude." Its axes are latitude (degrees) and relative frequency.

Therefore Figure 10.3 cannot recover longitude/cross-arc structure and must not be used as a 2-D spatial physics prior.

## What Figure 10.3 can support

It is an evidence-grade target for a one-dimensional along-arc/latitude marginal:
- top panel: no BFO measurements;
- bottom panel: BFO measurements;
- BFO resolves the north/south ambiguity but does not substantially change the southern-mode shape.

A digitised BFO panel may replace the project's Gaussian LATITUDE proxy, but it cannot replace the full 2-D physics distribution.

## Better 2-D target

Figure 10.2 is the pre-EOF BTO+BFO path/PDF representation from 18:02 to 00:19. It is upstream of section 10.5, but the published rendering uses colour-coded paths rather than a simple calibrated raster probability field. It may provide geographic support/shape and particle/path information; probability recovery requires validation of how colour/path weights map to density.

Figure 10.10 is explicitly post-EOF: the 00:19 particle locations were convolved with the section-10.5 descent kernel. It cannot be followed by another EOF likelihood.

## Quantitative EOF kernel recovered

Section 10.5 states the indicative kernel was:
- uniform disc to radius 15 NM;
- Gaussian drop-off beyond 15 NM with standard deviation 30 NM.

It also states uncontrolled-descent simulator studies had high likelihood of reaching zero altitude within 15 NM of beginning of descent, while human-controlled glide could extend farther. Section 10.8 notes simulations predicted a maximum approximately 100 NM glide under human control.

These are historical model assumptions, not direct observations and not current posterior weights.

## Revised pipeline

1. Digitise Fig. 10.3 bottom panel as a 1-D latitude marginal if image quality permits.
2. Use Fig. 10.2 to constrain/validate geographic support, not to invent pixel probabilities.
3. Seek original particles/numerical output or another quantitative pre-EOF 2-D representation before claiming a full DSTG spatial prior.
4. Keep Fig. 10.10/Fig. 1.1 as post-EOF validation products only.

Status: PREVIOUS_2D_TARGET_CLASSIFICATION_RETRACTED.
