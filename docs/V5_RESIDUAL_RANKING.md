# V5 residual-cell ranking

## Purpose
Produce ranked seabed cells only after authoritative 7th-arc/search geometry is attached. No hand-drawn search polygons are permitted.

## Current evidence gates
- Baseline geographic gate: approximately 33S–36S and close to the 7th arc, following ATSB First Principles Review.
- Practical end-of-flight envelope: about 27.5 NM west / 25 NM east of the arc; far-glide cases remain sensitivity tails.
- Drift gate: CSIRO gives strongest compatibility to 36S–32S, especially near 35S.
- WSPR proposed point is not promoted: GA's 2022 review found it highly unlikely that an aircraft debris field exists in the high-resolution area reviewed around the proposal.

## Search likelihood
For each cell L:

P_residual(L) ∝ P_physics(L) * L_drift(L) * L_EOF(L) * product_k(1-Pd_k(L)).

Missing Ocean Infinity cell geometry is neutral (likelihood 1), not guessed.

## Falsification gates before a candidate polygon may be published
1. Exact official 7th-arc geometry used.
2. Cell lies inside a physically defensible end-of-flight kernel.
3. Drift likelihood is explicitly represented, not merely centered on the CSIRO maximum.
4. ATSB/GA sonar coverage and holidays/LPD are represented cell by cell.
5. Ocean Infinity 2018/2025-26 evidence is applied only where exact geometry is available.
6. Candidate survives Pd sensitivity and controlled-glide prior sensitivity.
7. Candidate is compared with already-reviewed WSPR/GA area to prevent rediscovering a strongly excluded location.
8. Result is reported as a residual search region, never as a wreckage discovery.

## Current status
The ranking engine is implemented in `src/rank_residual_cells.py`. A final ranked polygon is intentionally blocked until authoritative cell-level sonar/search geometry has been ingested. This prevents false precision and boundary artifacts previously observed with synthetic masks.
