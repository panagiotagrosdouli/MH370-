#!/usr/bin/env python3
"""EOF hypothesis-mixture sensitivity in cross-arc distance bands.
Illustrative branch priors only; not a geographic posterior."""
BANDS=("0-15","15-25","25-50",">50")
# Conditional band masses encode official qualitative constraints, not fitted accident probabilities.
KERNELS={
 "H_U":(0.78,0.17,0.04,0.01), # uncontrolled: BFO-consistent sims generally <=15 NM
 "H_G":(0.20,0.20,0.35,0.25), # controlled glide sensitivity branch
 "H_C":(0.45,0.25,0.20,0.10), # continued-control intermediate sensitivity
}
def mixture(pu,pg,pc):
 assert abs(pu+pg+pc-1)<1e-9
 return tuple(pu*KERNELS["H_U"][i]+pg*KERNELS["H_G"][i]+pc*KERNELS["H_C"][i] for i in range(4))
SCENARIOS={
 "U95_G04_C01":(.95,.04,.01),
 "U90_G08_C02":(.90,.08,.02),
 "U80_G15_C05":(.80,.15,.05),
 "U70_G20_C10":(.70,.20,.10),
}
if __name__=="__main__":
 print("scenario,"+",".join(BANDS))
 for n,w in SCENARIOS.items():
  print(n+","+",".join(f"{x:.4f}" for x in mixture(*w)))
