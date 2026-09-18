#!/usr/bin/env python3
"""Fail-closed skeleton for calibrated BTO path-delay geometry."""
import math
C_KM_S=299792.458
def norm(a,b): return math.sqrt(sum((x-y)**2 for x,y in zip(a,b)))
def predicted_path_km(aircraft_ecef,sat_ecef,ges_ecef):
    return norm(aircraft_ecef,sat_ecef)+norm(sat_ecef,ges_ecef)
def calibrated_excess_path_km(bto_us,bias_us):
    return (bto_us-bias_us)*1e-6*C_KM_S
def residual_km(aircraft_ecef,sat_ecef,ges_ecef,bto_us,bias_us,reference_path_km):
    # reference_path_km is required explicitly because BTO includes system timing
    # conventions; do not infer it silently.
    obs=reference_path_km+calibrated_excess_path_km(bto_us,bias_us)
    return predicted_path_km(aircraft_ecef,sat_ecef,ges_ecef)-obs
if __name__=="__main__":
    raise SystemExit("FAIL_CLOSED: library only; supply primary-source calibration before solving arcs")
