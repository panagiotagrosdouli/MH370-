# MH370 V4 — Adversarial hypothesis analysis

## Purpose
This stage deliberately stress-tests the conventional end-of-flight assumptions without assigning probability to unsupported psychological diagnoses or conspiracy claims.

## Findings

### 1. Conventional end-of-flight kernel
ATSB material places the likely fuel-exhaustion/end-of-flight impact close to the 7th arc. The public ATSB map gives an approximate conventional bound of 27.5 NM west and 25 NM east of the arc.

### 2. Controlled-flight sensitivity
The ATSB Operational Search report explicitly discusses an active-control case in which a normal descent from about 40,000 ft could cover approximately 120 NM to sea level. This is not evidence that MH370 actually did so. It is a physically possible sensitivity case that materially expands the cross-arc search envelope.

V4 therefore treats end-of-flight as a mixture:

P(L|D) = (1-pi_g) P(L|H_uncontrolled,D) + pi_g P(L|H_controlled,D)

Sensitivity values for pi_g should be tested rather than asserted, e.g. 0.01, 0.05, 0.10, 0.25.

### 3. WSPR
WSPR receives zero baseline weight. ATSB has not validated WSPR as an aircraft-detection method, and Geoscience Australia re-reviewed high-resolution sonar in the proposed region without identifying an aircraft debris field.

### 4. SATCOM spoofing / Northern Arc
Retained only as a falsification scenario. No positive evidence currently justifies overcoming the combined BTO/BFO, aircraft-performance and debris constraints. A spoofing hypothesis would have to reproduce a coherent multi-hour sequence of BTO and BFO observations.

### 5. Psychological motive
No psychiatric label is used as a numerical prior. Penang overflight and route changes may be tested as observed trajectory facts, but speculative diagnoses or motives cannot defensibly generate coordinates.

### 6. 2025/26 search
Malaysia reports approximately 7,571 km² surveyed under the 2025/26 agreement with no confirmed wreckage location. V4 does not spatially apply this negative evidence until exact survey polygons/AUV tracks or equivalent machine-readable coverage geometry are obtained.

## New falsifiable search question
The useful adversarial question is not whether the entire 7th arc is wrong. It is whether a residual high-probability location survives outside the conventional ±~25 NM corridor under a low-prior controlled-flight hypothesis.

Primary region for testing remains the 33–36°S sector, especially the 35–36°S neighborhood, but V4 expands cross-arc testing out to ~120 NM and then intersects it with real sonar probability-of-detection masks.

Candidate cells must maximize approximately:

P_physics(L) × P_drift(L) × P_EOF(L) × [1 - P_D(L)]

No coordinate should be described as near-certain until physical wreckage is detected.

## Required next data
1. Official/machine-readable 7th-arc geometry.
2. Geoscience Australia Phase One bathymetry.
3. Phase Two sidescan/multibeam sonar coverage and quality metadata.
4. 2018 Ocean Infinity search coverage geometry if publicly recoverable.
5. 2025/26 Ocean Infinity survey geometry if publicly recoverable.
6. DSTG trajectory/posterior representation sufficient to avoid replacing the official Bayesian work with a Gaussian proxy.

## Sources
- ATSB Operational Search for MH370: https://www.atsb.gov.au/sites/default/files/media/5773565/operational-search-for-mh370_final_3oct2017.pdf
- ATSB Maps: https://www.atsb.gov.au/maps
- ATSB Definition of Underwater Search Areas (2015): https://www.atsb.gov.au/sites/default/files/2022-12/AE-2014-054_MH370-Definition%20of%20Underwater%20Search%20Areas_3Dec2015.pdf
- Geoscience Australia MH370 data release: https://www.ga.gov.au/scientific-topics/marine-and-coastal/showcase/mh370-data-release
- Malaysia MOT 2025/26 update: https://www.mot.gov.my/en/Kenyataan%20Media/Year%202026/MH370%20Search%20Operation%202025-2026%20-%20Update%20to%20Families.pdf
