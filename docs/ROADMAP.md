# Research Roadmap

## Phase 1 — Evidence audit

- Re-verify every exact BTO/BFO value against official ATSB/DSTG tables.
- Preserve special handling/corrections for terminal SATCOM bursts.
- Encode radar as an uncertain state rather than inventing coordinates.
- Keep fuel/performance, debris, simulator and WSPR in separate dependency groups.

## Phase 2 — Raw SATCOM reconstruction

- Ingest satellite ephemerides and ground-station parameters.
- Implement BTO likelihood bands.
- Implement BFO Doppler/bias likelihood.
- Reconstruct or validate candidate trajectory families against DSTG outputs.
- Use Monte Carlo / Sequential Monte Carlo with physically constrained B777 state propagation.

## Phase 3 — Fuel and end-of-flight

- Build altitude/Mach/mass-dependent fuel-flow model.
- Propagate fuel uncertainty independently of terminal SATCOM timing.
- Construct separate H1/H2/H3 end-of-flight impact kernels.

## Phase 4 — Debris/ocean inversion

- Ingest discovery dates and coordinates for confirmed/high-confidence debris.
- Use object-specific drift parameters.
- Run forward Lagrangian ensembles using historical currents, winds and Stokes drift.
- Model beaching and non-detection bias.
- Infer `P(debris observations | impact location)`.

## Phase 5 — Search-negative evidence

Highest-priority phase for producing a genuinely new search target.

- Download official Geoscience Australia bathymetry and Phase Two sonar data.
- Reconstruct historical search coverage polygons.
- Encode terrain shadowing, terrain avoidance, LPD geology and sonar gaps.
- Build spatial `P_detection(x,y)` rather than binary searched/unsearched masks.
- Ingest Ocean Infinity 2018 coverage if authoritative geometry can be obtained.
- Ingest 2025/26 coverage only where exact geometry can be verified.

Then compute:

\[
P_{remaining}(L) \propto P_{physical}(L)\prod_k[1-P_{D,k}(L)].
\]

## Phase 6 — Bathymetry and wreckage persistence

- Add seafloor depth, slope and roughness.
- Identify canyons and steep terrain that could reduce detectability or allow downslope redistribution.
- Separate possible movement of small fragments from persistence of the main wreckage field.

## Phase 7 — Sensitivity / falsification

Repeat inference with:

- widened/narrowed SATCOM uncertainty,
- alternative drift models,
- different fuel assumptions,
- different end-of-flight scenarios,
- alternative `P_D` priors,
- removal of each major evidence family.

Report stable regions only.

## Phase 8 — Blind overlays

Only after the physical posterior is frozen:

- compare recovered simulator points spatially,
- overlay WSPR proposals without refitting,
- estimate whether any spatial agreement exceeds chance expectations.

Neither source receives baseline posterior weight without independent physical validation.

## Decision criterion for a proposed new search box

A region should only be promoted as a serious physical-search target when it has:

1. high posterior probability under multiple physically plausible models,
2. low historical cumulative probability of detection,
3. no dependence on a single weak or unvalidated assumption,
4. a credible sonar/AUV search plan given depth and terrain.
