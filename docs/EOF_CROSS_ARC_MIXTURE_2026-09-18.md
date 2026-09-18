# EOF cross-arc mixture sensitivity — 2026-09-18

Purpose: translate the held-out final-BFO evidence into a transparent cross-arc sensitivity layer without pretending that ATSB simulator statements provide a calibrated probability distribution.

Official anchors:
- BFO-consistent uncontrolled simulations generally impacted within 15 NM of the seventh arc.
- Some simulated trajectories travelled rearwards about 21 NM.
- Some remained airborne about 20 minutes after second-engine flameout.
- First Principles consequently placed substantially more weight close to the arc and judged the aircraft probably within 25 NM, while earlier work retained lower-probability widths to 40/100 NM.

The script defines three explicitly illustrative conditional kernels over 0–15, 15–25, 25–50 and >50 NM: H_U uncontrolled, H_G controlled glide, H_C continued-control. These numbers are NOT ATSB probabilities and MUST NOT be multiplied into a DSTG final-location product that already contains an EOF kernel. They are sensitivity parameters for a raw-SATCOM route or for ablation studies.

Illustrative mixture outputs:
- U95/G04/C01 -> 0–15 75.25%, 15–25 17.25%, 25–50 5.40%, >50 2.10%.
- U90/G08/C02 -> 0–15 72.50%, 15–25 17.50%, 25–50 6.80%, >50 3.20%.
- U80/G15/C05 -> 0–15 67.55%, 15–25 17.85%, 25–50 9.45%, >50 5.15%.
- U70/G20/C10 -> 0–15 63.10%, 15–25 18.40%, 25–50 11.30%, >50 7.20%.

Interpretation: under every tested mixture dominated by the held-out high-descent branch, most cross-arc mass remains inside 15 NM and roughly 81.5–92.5% remains inside 25 NM. The tail beyond 25 NM is controlled almost entirely by the prior assigned to controlled/continued-control branches, not by the final BFO itself.

These are branch-sensitivity results, not a location claim. Along-arc latitude still comes from the SATCOM/drift physics route, and search non-detection must be applied only after authoritative coverage/Pd geometry is attached.

Status: EOF_MIXTURE_SENSITIVITY_IMPLEMENTED / NO_DOUBLE_COUNTING / AUTHORITATIVE_PD_GEOMETRY_STILL_BLOCKS_FINAL_CELL_RANKING.
