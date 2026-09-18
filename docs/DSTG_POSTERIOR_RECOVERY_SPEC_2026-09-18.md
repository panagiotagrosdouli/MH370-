# DSTG posterior recovery specification — 2026-09-18

## Primary-source recovery target

The DST Group book and ATSB search-area material establish two related but distinct products:

1. DSTG Bayesian flight-path posterior / endpoint distribution.
2. ATSB Figure 1 / Figure 5 style location distribution after combining DSTG analysis with the ATSB end-of-flight scenario.

These must not be silently interchanged.

The DSTG method produced particle samples from a posterior over flight paths. ATSB states that the output was a PDF defining the probable crossing of the 6th arc and that results were extrapolated to the 7th arc. The book's application chapter contains the final-location density/heatmap products.

## Preferred evidence-grade representation

Priority order:
A. original DSTG particle/filter output, if recoverable;
B. numerical/vector data underlying the published figures;
C. reproducible digitisation of the published DSTG/ATSB figure with explicit calibration and uncertainty;
D. no substitute Gaussian.

A raster heatmap digitisation is a measurement of the published graphic, not recovery of the original particle posterior. It must retain that provenance label.

## Digitisation protocol

For a published map figure:
- use the original PDF page, not a screenshot or third-party crop;
- identify map control points/graticule and fit the map transform;
- isolate only the probability layer; exclude basemap, arc lines, labels and search-area outlines;
- preserve the colour bar mapping if recoverable;
- resample onto a documented geographic grid;
- normalize only after masking non-probability pixels;
- quantify georeferencing and colour-class uncertainty;
- validate extracted contours/peak region against the source figure;
- never infer probability from hue where the source legend does not support a quantitative mapping.

## Important distinction

ATSB's 2022 Search Area page says its displayed probability distribution is the DST Group analysis combined with the ATSB end-of-flight scenario. That product is appropriate for a combined physics+EOF route, but using it and then multiplying by a separate EOF likelihood would double count EOF evidence.

Therefore:
- DSTG-only posterior -> may be followed by explicit EOF mixture.
- ATSB combined DSTG+EOF map -> EOF mixture must be disabled.

## Current state

No evidence-grade numeric DSTG density has yet been recovered into the repository.
The previous Gaussian latitude proxy remains prohibited as a substitute.
