# BTO arc reconstruction contract — 2026-09-18

The raw-SATCOM branch now advances from measurements and satellite states to range geometry.

The Inmarsat/JN paper defines BTO as a biased timing/range observable whose aircraft-to-satellite contribution cannot be obtained by simply multiplying corrected BTO by c/2. The complete path includes aircraft-satellite and satellite-ground geometry plus terminal/system calibration terms. Therefore a naive spherical radius derived directly from the accident BTO is prohibited.

The official method uses known-position calibration messages to estimate the BTO bias and then solves the geometric path delay with the satellite state and Perth GES position. The published uncertainty is represented as timing error around the calibrated range solution, not as an arbitrary geographic Gaussian.

Implementation gate:
1. use the operator I-3F1 ECEF state at each message time;
2. use authoritative Perth GES coordinates;
3. recover/verify the exact BTO calibration equation and bias convention from primary sources;
4. validate on known-position pre-departure messages before using accident arcs;
5. reconstruct each arc as the Earth-surface locus satisfying the calibrated path equation;
6. compare reconstructed seventh arc against the official GA/ATSB 7thArc_SingleLine geometry when its vertices become retrievable.

No arc coordinates are emitted until the calibration convention passes the known-position test. This prevents a numerically clean but physically wrong arc.

Status: ARC_SOLVER_CONTRACT_READY / CALIBRATION_KNOWN_POSITION_TEST_PENDING.
