# DSTG Chapter 10 pre-EOF target audit — 2026-09-18

Primary-source web audit confirms section 10.5: the particle filter estimates the aircraft-state PDF at 00:19; only afterward is an end-of-flight transition distribution applied.

Figure inventory recovered from the open chapter/index:
- Fig. 10.1: paths 18:02–00:19, BTO-only weighting.
- Fig. 10.2: paths 18:02–00:19, BTO+BFO weighting.
- Fig. 10.3: comparison of filter PDF without vs with BFO.
- Figs. 10.4 onward include posterior diagnostics; Fig. 10.8 is manoeuvre-time posterior.
- Section 10.5 begins after Fig. 10.8.

Therefore Fig. 10.3 is currently the strongest identified published candidate for a PRE-EOF spatial/filter PDF. It is upstream of the section-10.5 descent kernel. Fig. 10.2 is useful as a trajectory/path validation figure, not automatically a quantitative spatial density.

Evidence gate:
1. Obtain the original PDF rendering of Fig. 10.3.
2. Verify geographic axes/control points and legend semantics.
3. If the figure is only qualitative/colour-coded without quantitative density calibration, do not manufacture probabilities. Use it only to validate support/shape.
4. If quantitative mapping is available, digitise with explicit map transform and uncertainty.
5. Keep BTO-only panel as an ablation/reference; baseline physics uses BTO+BFO.
6. Do not combine any pre-EOF extraction with Fig. 1.1 or later final-location PDFs as independent likelihoods.

Status: TARGET_IDENTIFIED_NOT_DIGITISED.
