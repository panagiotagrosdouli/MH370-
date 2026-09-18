#!/usr/bin/env python3
"""Held-out 00:19:29 descent-rate likelihood from BFO residual."""
import math
MEASURED=182.0
LEVEL_PRED=256.0
SENS_HZ_PER_100FPM=1.7
SIGMA_BFO=4.3
def descent_from_residual(measured=MEASURED,pred=LEVEL_PRED,warmup_hz=0.0):
 # positive fpm denotes downward speed
 return (pred-(measured-warmup_hz))/SENS_HZ_PER_100FPM*100.0
def likelihood(descent_fpm,warmup_hz=0.0,sigma=SIGMA_BFO):
 pred=LEVEL_PRED-SENS_HZ_PER_100FPM*descent_fpm/100.0+warmup_hz
 z=(MEASURED-pred)/sigma
 return math.exp(-0.5*z*z)
if __name__=="__main__":
 print("central_no_warmup_fpm",descent_from_residual())
 for w in (0,25,50,100,130):
  print("warmup_hz",w,"descent_fpm",round(descent_from_residual(warmup_hz=w)))
