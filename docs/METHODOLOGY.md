# Methodology

## 1. Target quantity

We estimate a spatial posterior over the main wreckage field location `L`:

\[
P(L\mid D)
\]

The operational output is a gridded probability surface with credible regions, not a single coordinate.

## 2. Evidence hierarchy

### A. Direct measurements
- Military/civil radar observations.
- Inmarsat BTO/BFO measurements.
- Confirmed debris identifications and discovery locations/dates.

### B. Official model-derived evidence
- DSTG Bayesian trajectory inference.
- ATSB end-of-flight analyses.
- CSIRO debris-drift modelling.
- Official sonar/bathymetry search assessments.

### C. Contextual evidence
- Recovered simulator information.

### D. Experimental / unvalidated
- WSPR-based retrospective aircraft-detection proposals.

C and D are excluded from the baseline posterior and considered only after the physical model is complete.

## 3. Dependency structure

The main risk is double-counting. The DSTG posterior already incorporates SATCOM, aircraft dynamics and meteorology. Therefore a DSTG-derived prior/likelihood must not simply be multiplied again by raw BTO/BFO, aircraft-performance and wind likelihoods unless the model is reconstructed from raw inputs from first principles.

Likewise, CSIRO drift outputs are derived from debris observations and ocean transport assumptions. They should be represented as one conditional evidence family, not decomposed into pseudo-independent factors that reuse the same observations.

## 4. Baseline mathematical structure

A defensible synthesis has the form

\[
P(L\mid D) \propto P_{flight}(L)\,P_{drift}(L)\,P_{EOF}(L)\,P_{search}(ND\mid L),
\]

with explicit checks for conditional dependence.

The search-negative term is

\[
P_{search}(ND\mid L)=\prod_k [1-P_{D,k}(L)]
\]

only when search campaigns can reasonably be treated as conditionally independent given wreckage location and local observability.

## 5. Inmarsat inverse problem

For a raw reconstruction, each handshake contributes

\[
P(BTO_i\mid X_i)
\]

and

\[
P(BFO_i\mid X_i,\dot X_i,S_i),
\]

where `S_i` contains satellite state, oscillator/bias parameters and ground-station compensation effects. Arcs are probability bands, not zero-width curves.

A complete raw model requires satellite ephemerides, calibration terms and a validated BFO compensation model. Until those are fully ingested, the project uses official DSTG/ATSB outputs rather than inventing unavailable parameters.

## 6. Radar state

The last reliable military-radar observation is treated as an uncertain state vector

\[
X(t_0)=[lat,lon,h,V_g,\psi]
\]

with covariance, not a perfect point. If an official source does not publish exact coordinates, the model must not fabricate them.

## 7. Fuel/performance

Fuel is modelled as

\[
f(t+dt)=f(t)-FF(h,M,\text{mass},T,\text{configuration})dt.
\]

No single fixed hourly burn rate is used. Fuel exhaustion time is a distribution and should be compared independently with the terminal SATCOM sequence.

## 8. End-of-flight hypotheses

Separate kernels should be constructed for at least:

- H1: uncontrolled descent after fuel exhaustion,
- H2: aerodynamic glide,
- H3: controlled continuation.

Model probabilities should only be assigned when priors are justified. Otherwise, report scenario-conditional impact kernels.

## 9. Debris drift

Forward Lagrangian transport is preferred over naïve backward advection:

\[
\frac{dx_j}{dt}=U_{current}+\alpha_j U_{wind}+U_{Stokes}+\epsilon_j.
\]

Each debris class needs its own distribution for windage, buoyancy, orientation, degradation and beaching probability.

## 10. Seafloor and elapsed time

Floating-debris transport and underwater wreckage redistribution are separate physical problems. The main wreckage is not advected using surface-current models.

For seabed persistence, assess bathymetry, slope, canyon geometry, sedimentation, bottom currents and plausible turbidity-current transport. Large structural wreckage is expected to remain much closer to the original impact area than floating debris, unless local geomorphology provides a credible downslope transport mechanism.

## 11. Previous search as negative evidence

A searched cell is not automatically probability zero.

For each cell estimate

\[
P_D=P(\text{detection}\mid \text{wreckage present, sensor, terrain, coverage}).
\]

Then update

\[
P(L\mid ND)\propto [1-P_D(L)]P(L).
\]

Important observability factors include sidescan/multibeam resolution, tow/AUV altitude, track spacing, terrain shadowing, terrain avoidance, data gaps and lower-probability-of-detection geology.

## 12. Sensitivity and falsification

Required ablations include removing or widening:

- BFO information,
- BTO information,
- debris/drift evidence,
- fuel constraints,
- EOF assumptions,
- prior-search negative evidence.

A target is robust only if a similar geographic region remains important over a broad range of reasonable assumptions.

## 13. Current proxy model

The current workbook/code uses a deliberately simplified grid proxy anchored to official ATSB/CSIRO constraints. It is a search-prior synthesis, not a fresh raw-DSTG reconstruction. The model must be upgraded with exact sonar/AUV coverage polygons and local `P_D(x,y)` before any claim of a genuinely new search box is justified.
