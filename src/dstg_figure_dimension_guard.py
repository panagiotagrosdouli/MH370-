#!/usr/bin/env python3
"""Guard dimensional semantics of published DSTG figures."""
import argparse
P={
 "DSTG_F10_3":{"dimension":"1D_LATITUDE","pre_eof":True},
 "DSTG_F10_2":{"dimension":"PATH_ENSEMBLE_2D","pre_eof":True},
 "DSTG_F10_10":{"dimension":"FINAL_LOCATION_2D","pre_eof":False},
}
def main():
 p=argparse.ArgumentParser();p.add_argument("--product",required=True,choices=P);p.add_argument("--require-2d-density",action="store_true");p.add_argument("--apply-eof",action="store_true");a=p.parse_args()
 q=P[a.product]
 if a.require_2d_density and q["dimension"]!="FINAL_LOCATION_2D":
  raise SystemExit("FAIL_CLOSED: product is not a calibrated 2-D density")
 if a.apply_eof and not q["pre_eof"]:
  raise SystemExit("FAIL_CLOSED: EOF already incorporated")
 print("PASS",a.product,q)
if __name__=="__main__":main()
