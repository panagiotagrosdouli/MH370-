#!/usr/bin/env python3
"""Evidence-anchored EOF cross-arc bands; no fabricated continuous kernel.

Bands encode official qualitative/containment statements only.
They are constraints for sensitivity analysis, not calibrated probabilities.
"""
BANDS_NM=((0,15),(15,25),(25,40),(40,100))
EVIDENCE={
 "BFO_consistent_simulations":{
   "statement":"generally impacted within 15 NM of 7th arc",
   "probability":None},
 "First_Principles":{
   "statement":"probably within 25 NM; closer to arc higher likelihood",
   "probability":None},
 "uncontrolled_simulation_envelope_2016":{
   "statement":"plus/minus 40 NM appropriate to encompass all uncontrolled scenarios in that simulation set",
   "probability":None},
 "historical_glide_sensitivity":{
   "statement":"2015 decreasing-priority extent reached 100 NM",
   "probability":None},
}
def admissible_band(distance_nm):
 d=abs(distance_nm)
 for lo,hi in BANDS_NM:
  if lo <= d < hi or (hi==100 and d==100): return (lo,hi)
 return None
if __name__=="__main__":
 for b in BANDS_NM: print(b)
 for k,v in EVIDENCE.items(): print(k,v["statement"])
