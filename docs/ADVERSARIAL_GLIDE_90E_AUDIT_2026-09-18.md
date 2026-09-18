# Adversarial audit of the 90.8E post-Arc-7 glide hypothesis — 2026-09-18

## Purpose

A public independent MH370 model currently reports an impact estimate near 35.9S, 90.8E. This note audits whether that result is strong enough to alter this repository's baseline posterior.

## Result

**No. Keep it as a sensitivity branch, not as baseline evidence.**

The public model's own documentation separates the result into:
1. a modeled Arc-7 crossing near 34.8S, 92.2E;
2. a post-Arc-7 unpowered-glide extrapolation of roughly 50–79 NM;
3. a final endpoint roughly 90.4–91.8E depending on assumed descent state.

The large westward displacement is therefore not directly measured by BTO/BFO. It is created mainly by the end-of-flight continuation model.

## Assumptions that create the displacement

The public model uses, among other choices:
- an unpowered post-Arc-7 glide;
- glide ratio 15:1;
- altitude at Arc 7 derived from FL350 minus approximately one minute of descent;
- a central pre-Arc-7 descent rate of 4,200 ft/min;
- continuation along the solver's final heading;
- no wind in the glide endpoint calculation.

Changing the end-of-flight state changes the endpoint substantially. Therefore 90.8E must not be described as a satellite-derived coordinate.

## Important evidential correction

The statement that the 00:19 SDU log-on **proves** engine flameout is too strong.

The log-on is evidence of a power interruption/restoration to the SATCOM system and is consistent with the fuel-exhaustion/APU scenario discussed by investigators, but it does not by itself uniquely prove engine flameout or a specific post-Arc-7 aerodynamic state.

This repository will therefore model:
- H_U: uncontrolled/rapid descent;
- H_G: unpowered glide;
- H_C: continued controlled flight;

as separate end-of-flight hypotheses rather than silently conditioning on H_G.

## Internal consistency issue in the external model

Its DSTG-validation document reports a current probability peak near 37.8S and explicitly notes material differences from DSTG:
- fixed BFO bias rather than particle-filter estimation;
- Arc-7 BFO used as a descent-envelope constraint although DSTG excluded it from trajectory inference;
- integrated fuel model rather than DSTG post-censoring;
- wider speed prior;
- free heading/speed at each arc rather than the DSTG autopilot-mode family;
- directional continuation instead of the DSTG descent kernel.

The separate impact-zone note reports a best Arc-7 crossing near 34.8S. This is not necessarily a software contradiction because the documents can refer to different model stages/configurations, but it means the 34.8S crossing cannot be treated as independently reproduced DSTG output.

## Drift cross-check

The same project contains an earlier OSCAR drift experiment that weakly contradicted the 90.8E zone on Reunion timing. A later note says an ERA5-assisted experiment reverses that conclusion and favors the western zone.

That reversal is scientifically important: it shows that the drift Bayes factor is sensitive to forcing/model specification. Until the later ERA5/HYCOM workflow is independently reproduced against the CSIRO methodology and multiple confirmed debris sites, it should not receive a strong likelihood ratio.

## Baseline treatment

For this repository:

`P(L|D) = sum_H P(L|D,H) P(H|D)`

with H including at least uncontrolled descent and glide.

The western 90–92E zone is retained in the glide sensitivity branch. It does **not** replace the evidence-supported close-to-Arc baseline.

No coordinate in this note is a wreckage-location claim.
