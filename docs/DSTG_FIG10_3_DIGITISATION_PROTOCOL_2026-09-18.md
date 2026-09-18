# DSTG Figure 10.3 digitisation protocol — 2026-09-18

Primary-source text confirms Figure 10.3 is a one-dimensional PDF parameterised by latitude. It compares the particle-filter result without BFO and with BFO. DSTG states that BFO selects the southern mode from the multimodal BTO-only PDF but does not significantly change that southern mode's shape.

This means Figure 10.3 can replace only the project's latitude Gaussian proxy. It cannot supply longitude or cross-arc density.

The new validator accepts explicit curve samples with latitude and relative frequency, selects the BTO+BFO panel, and normalises the curve by trapezoidal integration. It refuses negative values, insufficient points, missing provenance, or zero integral.

No synthetic samples are committed. The next data step requires extraction from the original ATSB-hosted PDF rendering. Until those points exist, the output remains intentionally absent.

Important coordinate caveat from DSTG: latitude is a nonlinear parameterisation of position around the BTO arc, so the plotted PDF is slightly distorted relative to an arc-length density. The digitised curve must therefore be labelled a latitude marginal, not an along-arc metric density.

Status: DIGITISATION_PIPELINE_READY / SOURCE_POINTS_NOT_YET_EXTRACTED.
