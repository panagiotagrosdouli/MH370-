"""Search negative-evidence likelihood for MH370 residual-posterior work.

This module deliberately separates *coverage class* from probability of detection.
It does not infer geometry from area totals. Geometry must come from authoritative
GIS/raster inputs. Unknown Ocean Infinity geometry remains UNKNOWN rather than
being painted onto the map.
"""
from __future__ import annotations
from dataclasses import dataclass
from enum import Enum

class Coverage(Enum):
    HIGH_RES_PHASE2 = "high_res_phase2"
    LPD = "lower_probability_detection"
    HOLIDAY = "holiday_or_gap"
    PHASE1_LOW_RES = "phase1_low_resolution"
    OI_UNKNOWN = "ocean_infinity_geometry_unknown"
    UNSEARCHED = "unsearched"

@dataclass(frozen=True)
class PdScenario:
    name: str
    high_res: float
    lpd: float
    holiday: float
    phase1_low_res: float

# Sensitivity values, not measurements. They are intentionally broad and must
# never be presented as ATSB/GA quoted probabilities.
SCENARIOS = {
    "conservative": PdScenario("conservative", 0.90, 0.50, 0.05, 0.05),
    "central":      PdScenario("central",      0.97, 0.70, 0.02, 0.02),
    "strong":       PdScenario("strong",       0.99, 0.90, 0.01, 0.01),
}

def nondetection_likelihood(coverage: Coverage, scenario: PdScenario) -> float:
    """Return P(no detection | wreckage in cell) for a classified cell."""
    if coverage is Coverage.HIGH_RES_PHASE2:
        pd = scenario.high_res
    elif coverage is Coverage.LPD:
        pd = scenario.lpd
    elif coverage is Coverage.HOLIDAY:
        pd = scenario.holiday
    elif coverage is Coverage.PHASE1_LOW_RES:
        pd = scenario.phase1_low_res
    elif coverage in (Coverage.OI_UNKNOWN, Coverage.UNSEARCHED):
        # Unknown geometry cannot legitimately supply spatial negative evidence.
        pd = 0.0
    else:
        raise ValueError(coverage)
    return 1.0 - pd

def apply_search_evidence(prior: float, coverage: Coverage, scenario: PdScenario) -> float:
    return prior * nondetection_likelihood(coverage, scenario)
