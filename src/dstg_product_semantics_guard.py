#!/usr/bin/env python3
"""Enforce DSTG figure/product semantics before posterior composition."""
import argparse
PRODUCTS={
 "DSTG_0019_PRE_EOF":{"eof_allowed":True},
 "DSTG_FIG1_1_FINAL_LOCATION":{"eof_allowed":False},
 "ATSB_FIG57_REFINED_FINAL_LOCATION":{"eof_allowed":False},
}
def main():
 p=argparse.ArgumentParser();p.add_argument("--product",required=True,choices=PRODUCTS);p.add_argument("--apply-eof",action="store_true");a=p.parse_args()
 if a.apply_eof and not PRODUCTS[a.product]["eof_allowed"]:
  raise SystemExit("FAIL_CLOSED: selected product already contains EOF transition evidence")
 print("PASS",a.product,"apply_eof",a.apply_eof)
if __name__=="__main__":main()
