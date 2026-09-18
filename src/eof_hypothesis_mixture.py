#!/usr/bin/env python3
"""Mix end-of-flight hypotheses without collapsing them into one cross-arc kernel."""
import argparse,csv,os
H=("H_U","H_G","H_C")
def main():
 ap=argparse.ArgumentParser();ap.add_argument("input");ap.add_argument("--out",default="results/eof_mixture.csv")
 ap.add_argument("--w-u",type=float,default=.85);ap.add_argument("--w-g",type=float,default=.10);ap.add_argument("--w-c",type=float,default=.05);a=ap.parse_args()
 w={"H_U":a.w_u,"H_G":a.w_g,"H_C":a.w_c}
 if any(v<0 for v in w.values()) or abs(sum(w.values())-1)>1e-9:raise SystemExit("FAIL_CLOSED EOF weights must be nonnegative and sum to 1")
 with open(a.input,newline="",encoding="utf-8") as f:
  r=csv.DictReader(f);req={"cell_id",*H}
  if not req<=set(r.fieldnames or []):raise SystemExit("FAIL_CLOSED missing EOF columns")
  rows=list(r)
 out=[];z=0.
 for x in rows:
  vals={h:float(x[h]) for h in H}
  if any(v<0 for v in vals.values()):raise SystemExit("FAIL_CLOSED negative EOF likelihood")
  mix=sum(w[h]*vals[h] for h in H);z+=mix
  out.append({"cell_id":x["cell_id"],**vals,"w_H_U":w["H_U"],"w_H_G":w["H_G"],"w_H_C":w["H_C"],"eof_mixture_raw":mix})
 if z<=0:raise SystemExit("FAIL_CLOSED zero EOF mass")
 for x in out:x["eof_mixture"]=x["eof_mixture_raw"]/z
 os.makedirs(os.path.dirname(a.out) or ".",exist_ok=True)
 with open(a.out,"w",newline="",encoding="utf-8") as f:
  wr=csv.DictWriter(f,fieldnames=out[0]);wr.writeheader();wr.writerows(out)
if __name__=="__main__":main()
