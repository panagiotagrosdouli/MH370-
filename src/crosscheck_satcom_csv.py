#!/usr/bin/env python3
"""Cross-check two SATCOM CSVs by timestamp/event without silently merging them."""
import argparse,csv
FIELDS=("bto_raw_us","bto_corrected_us","bfo_hz")
def load(p):
 with open(p,newline="",encoding="utf-8") as f:r=list(csv.DictReader(f))
 out={}
 for x in r:
  k=(x.get("time_utc",""),x.get("event",""))
  if k in out:raise SystemExit("FAIL_CLOSED duplicate event "+str(k))
  out[k]=x
 return out
def main():
 p=argparse.ArgumentParser();p.add_argument("primary");p.add_argument("external");a=p.parse_args()
 A,B=load(a.primary),load(a.external); keys=sorted(set(A)|set(B));bad=0
 print("time_utc,event,field,primary,external,status")
 for k in keys:
  if k not in A or k not in B:
   print(*k,"","","","MISSING_SIDE",sep=",");bad+=1;continue
  for f in FIELDS:
   x,y=A[k].get(f,""),B[k].get(f,"")
   s="MATCH" if x==y else "DIFF"
   if s=="DIFF":bad+=1
   print(*k,f,x,y,s,sep=",")
 raise SystemExit(1 if bad else 0)
if __name__=="__main__":main()
