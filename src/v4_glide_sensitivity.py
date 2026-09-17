"""MH370 V4: controlled-glide sensitivity layer.

This module deliberately does NOT claim a new wreck coordinate. It defines the
cross-arc end-of-flight mixture to be combined with an official/DSTG along-arc
prior, CSIRO drift likelihood, and measured sonar probability-of-detection.

Evidence basis:
- ATSB First Principles Review: later evidence strongly weights impact closer to
  the 7th arc, probably within ~25 NM.
- ATSB Operational Search report: an actively controlled normal descent from
  ~40,000 ft could theoretically travel ~120 NM before sea level.

The 120-NM case is therefore a sensitivity hypothesis, not the baseline.
"""

from __future__ import annotations

import math
from dataclasses import dataclass


@dataclass(frozen=True)
class EOFModel:
    sigma_uncontrolled_nm: float = 10.0
    conventional_limit_nm: float = 25.0
    glide_max_nm: float = 120.0
    glide_scale_nm: float = 45.0


def gaussian(x: float, sigma: float) -> float:
    return math.exp(-0.5 * (x / sigma) ** 2)


def uncontrolled_kernel(cross_arc_nm: float, cfg: EOFModel = EOFModel()) -> float:
    """Symmetric near-arc proxy for uncontrolled/high-rate descent."""
    return gaussian(cross_arc_nm, cfg.sigma_uncontrolled_nm)


def controlled_glide_kernel(cross_arc_nm: float, cfg: EOFModel = EOFModel()) -> float:
    """Conservative sensitivity kernel for active control.

    The kernel is nonzero out to 120 NM and decreases with distance. It is NOT a
    statement that MH370 glided 120 NM. Directional/meteorological constraints
    should be added once the exact 7th-arc geometry and 00:19 winds are ingested.
    """
    d = abs(cross_arc_nm)
    if d > cfg.glide_max_nm:
        return 0.0
    return math.exp(-d / cfg.glide_scale_nm)


def eof_mixture(cross_arc_nm: float, glide_prior: float, cfg: EOFModel = EOFModel()) -> float:
    if not 0.0 <= glide_prior <= 1.0:
        raise ValueError("glide_prior must be in [0, 1]")
    u = uncontrolled_kernel(cross_arc_nm, cfg)
    g = controlled_glide_kernel(cross_arc_nm, cfg)
    return (1.0 - glide_prior) * u + glide_prior * g


def residual_score(
    physics_prior: float,
    drift_likelihood: float,
    cross_arc_nm: float,
    detection_probability: float,
    glide_prior: float,
) -> float:
    """Unnormalised residual posterior score.

    P_residual ∝ P_physics * L_drift * L_EOF * (1 - P_D)

    `physics_prior` must not separately multiply evidence already included in a
    DSTG posterior (e.g. raw BTO/BFO again), otherwise evidence is double-counted.
    """
    if not 0.0 <= detection_probability <= 1.0:
        raise ValueError("detection_probability must be in [0, 1]")
    return (
        physics_prior
        * drift_likelihood
        * eof_mixture(cross_arc_nm, glide_prior)
        * (1.0 - detection_probability)
    )


def sensitivity_grid():
    """Return scenario weights for inspection before geospatial ingestion."""
    priors = (0.01, 0.05, 0.10, 0.25)
    distances = (0, 10, 25, 40, 60, 80, 100, 120)
    return [
        {
            "glide_prior": p,
            "cross_arc_nm": d,
            "eof_weight": eof_mixture(d, p),
        }
        for p in priors
        for d in distances
    ]


if __name__ == "__main__":
    for row in sensitivity_grid():
        print(row)
