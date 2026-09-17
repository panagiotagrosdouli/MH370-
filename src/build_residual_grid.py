"""Build a conservative MH370 residual-search grid.

This module is deliberately evidence-limited. It accepts an official 7th-arc
GeoJSON plus optional sonar/search polygons. It NEVER infers missing Ocean
Infinity geometry from total searched area. Unknown coverage stays unknown.

Outputs a CSV suitable for rank_residual_cells.py and records which likelihood
terms are measured/model-derived/proxy.
"""
from __future__ import annotations

import argparse, csv, json, math
from pathlib import Path

NM_KM = 1.852


def gaussian(x, mu, sigma):
    return math.exp(-0.5*((x-mu)/sigma)**2)


def drift_lat_proxy(lat):
    # Explicit proxy only: CSIRO evidence favours roughly 36S-32S, especially
    # near 35S. Replace with digitised/particle likelihood before final result.
    return gaussian(lat, -35.0, 1.15)


def eof_proxy(cross_nm):
    # Concentrates baseline EOF probability close to arc; this is NOT DSTG PDF.
    return gaussian(cross_nm, 0.0, 10.0)


def along_arc_proxy(lat):
    # Broad, intentionally weak placeholder around the evidence-supported
    # 33S-36S corridor. Do not interpret as a reconstructed SATCOM posterior.
    return gaussian(lat, -35.0, 1.25)


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--out', default='data/derived/residual_grid_proxy.csv')
    ap.add_argument('--lat-step', type=float, default=0.05)
    ap.add_argument('--cross-step-nm', type=float, default=1.0)
    args=ap.parse_args()

    rows=[]
    lat=-36.0
    while lat <= -33.0 + 1e-9:
        cross=-27.5
        while cross <= 25.0 + 1e-9:
            physics=along_arc_proxy(lat)
            drift=drift_lat_proxy(lat)
            eof=eof_proxy(cross)
            # Unknown until intersected with authoritative sonar/search GIS.
            pd=None
            pre=physics*drift*eof
            rows.append({
                'lat':round(lat,5), 'cross_arc_nm':round(cross,3),
                'physics_proxy':physics, 'drift_proxy':drift,
                'eof_proxy':eof, 'pd_total':'',
                'pre_search_score':pre,
                'status':'PROXY_ONLY_NO_GIS_PD'
            })
            cross += args.cross_step_nm
        lat += args.lat_step

    s=sum(r['pre_search_score'] for r in rows)
    for r in rows: r['pre_search_score_norm']=r['pre_search_score']/s
    rows.sort(key=lambda r:r['pre_search_score_norm'], reverse=True)
    p=Path(args.out); p.parent.mkdir(parents=True, exist_ok=True)
    with p.open('w', newline='', encoding='utf-8') as f:
        w=csv.DictWriter(f, fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    print(f'wrote {len(rows)} proxy cells; no candidate location may be claimed until GIS P_D is populated')

if __name__=='__main__': main()
