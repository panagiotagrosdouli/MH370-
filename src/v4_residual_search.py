"""V4 residual-search engine for MH370.

Scientific rule: this program must not manufacture search geometry.
Final ranking requires authoritative GIS layers for sonar coverage / holidays.

The model separates:
  physics prior (prefer published DSTG density when available)
  drift likelihood
  end-of-flight mixture
  search non-detection likelihood

P(L|D) ∝ P_physics * L_drift * L_EOF * product(1-Pd_k)
"""
from __future__ import annotations

from dataclasses import dataclass
import numpy as np


@dataclass(frozen=True)
class EOFMixture:
    glide_prior: float = 0.05
    uncontrolled_sigma_nm: float = 12.5
    glide_scale_nm: float = 45.0
    glide_max_nm: float = 120.0


def uncontrolled_kernel(cross_arc_nm: np.ndarray, sigma_nm: float = 12.5) -> np.ndarray:
    """Proxy only. Replace with published/reconstructed EOF kernel where possible."""
    return np.exp(-0.5 * (cross_arc_nm / sigma_nm) ** 2)


def controlled_glide_kernel(cross_arc_nm: np.ndarray,
                            scale_nm: float = 45.0,
                            max_nm: float = 120.0) -> np.ndarray:
    """Low-prior sensitivity tail, not a claim of pilot control."""
    d = np.abs(cross_arc_nm)
    return np.where(d <= max_nm, np.exp(-d / scale_nm), 0.0)


def eof_mixture(cross_arc_nm: np.ndarray, cfg: EOFMixture) -> np.ndarray:
    if not 0 <= cfg.glide_prior <= 1:
        raise ValueError("glide_prior must be in [0,1]")
    u = uncontrolled_kernel(cross_arc_nm, cfg.uncontrolled_sigma_nm)
    g = controlled_glide_kernel(cross_arc_nm, cfg.glide_scale_nm, cfg.glide_max_nm)
    return (1.0 - cfg.glide_prior) * u + cfg.glide_prior * g


def combine_detection_probabilities(pd_layers: list[np.ndarray]) -> np.ndarray:
    """Combine conditionally independent detection opportunities.

    Do not use this if searches are not conditionally independent; in that case
    implement an explicit joint detection model.
    """
    if not pd_layers:
        raise ValueError("At least one Pd layer is required")
    survival = np.ones_like(pd_layers[0], dtype=float)
    for pd in pd_layers:
        if np.any((pd < 0) | (pd > 1)):
            raise ValueError("Pd values must lie in [0,1]")
        survival *= (1.0 - pd)
    return 1.0 - survival


def posterior(physics: np.ndarray,
              drift: np.ndarray,
              eof: np.ndarray,
              pd_total: np.ndarray) -> np.ndarray:
    arrays = [physics, drift, eof, pd_total]
    if len({a.shape for a in arrays}) != 1:
        raise ValueError("All layers must have identical shape")
    if np.any((pd_total < 0) | (pd_total > 1)):
        raise ValueError("pd_total must lie in [0,1]")
    raw = physics * drift * eof * (1.0 - pd_total)
    z = raw.sum()
    if not np.isfinite(z) or z <= 0:
        raise ValueError("Posterior has zero/non-finite normalizing mass")
    return raw / z


def probability_by_distance_band(p: np.ndarray,
                                 cross_arc_nm: np.ndarray,
                                 bands=((0,25),(25,50),(50,80),(80,120))):
    out = []
    d = np.abs(cross_arc_nm)
    for lo, hi in bands:
        mask = (d >= lo) & (d < hi)
        out.append({"lo_nm": lo, "hi_nm": hi, "mass": float(p[mask].sum())})
    return out


def require_real_search_geometry(metadata: dict) -> None:
    """Fail closed when someone attempts to use area totals as spatial masks."""
    if metadata.get("geometry_source") in (None, "", "area_total_only", "hand_drawn"):
        raise RuntimeError(
            "Authoritative search geometry is required. Area totals or hand-drawn masks "
            "must not be spatially applied to the posterior."
        )


if __name__ == "__main__":
    print("V4 engine loaded. Final localization requires authoritative DSTG/arc and search GIS layers.")
