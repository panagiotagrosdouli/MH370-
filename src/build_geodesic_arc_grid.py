#!/usr/bin/env python3
"""Build real lat/lon cells around an official 7th-Arc GeoJSON.

Fail-closed design:
- requires an actual LineString/MultiLineString GeoJSON;
- never synthesizes the 7th Arc;
- outputs real geographic cells from geodesic cross-track offsets;
- leaves Pd blank for later authoritative sonar overlay.

No third-party probability surface is embedded here.
"""
from __future__ import annotations
import argparse, csv, json, math
from pathlib import Path

EARTH_KM = 6371.0088
NM_KM = 1.852

def haversine_km(lat1, lon1, lat2, lon2):
    p1,p2=map(math.radians,(lat1,lat2))
    dp=math.radians(lat2-lat1); dl=math.radians(lon2-lon1)
    a=math.sin(dp/2)**2+math.cos(p1)*math.cos(p2)*math.sin(dl/2)**2
    return 2*EARTH_KM*math.asin(min(1,math.sqrt(a)))

def bearing_deg(lat1, lon1, lat2, lon2):
    p1,p2=map(math.radians,(lat1,lat2)); dl=math.radians(lon2-lon1)
    y=math.sin(dl)*math.cos(p2)
    x=math.cos(p1)*math.sin(p2)-math.sin(p1)*math.cos(p2)*math.cos(dl)
    return (math.degrees(math.atan2(y,x))+360)%360

def destination(lat, lon, bearing, distance_km):
    p1=math.radians(lat); l1=math.radians(lon)
    b=math.radians(bearing); d=distance_km/EARTH_KM
    p2=math.asin(math.sin(p1)*math.cos(d)+math.cos(p1)*math.sin(d)*math.cos(b))
    l2=l1+math.atan2(math.sin(b)*math.sin(d)*math.cos(p1), math.cos(d)-math.sin(p1)*math.sin(p2))
    return math.degrees(p2), ((math.degrees(l2)+540)%360)-180

def extract_lines(obj):
    lines=[]
    for f in obj.get("features",[]):
        g=f.get("geometry") or {}; t=g.get("type"); c=g.get("coordinates") or []
        if t=="LineString": lines.append(c)
        elif t=="MultiLineString": lines.extend(c)
    if not lines: raise SystemExit("No LineString/MultiLineString in official arc GeoJSON")
    return lines

def densify_segment(a,b,step_km):
    lon1,lat1=a; lon2,lat2=b
    d=haversine_km(lat1,lon1,lat2,lon2)
    n=max(1,int(math.ceil(d/step_km)))
    out=[]
    for i in range(n):
        t=i/n
        out.append((lon1+(lon2-lon1)*t, lat1+(lat2-lat1)*t))
    return out

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("arc_geojson")
    ap.add_argument("--out",default="data/derived/geodesic_arc_grid.csv")
    ap.add_argument("--lat-min",type=float,default=-36.0)
    ap.add_argument("--lat-max",type=float,default=-33.0)
    ap.add_argument("--along-step-km",type=float,default=5.0)
    ap.add_argument("--cross-min-nm",type=float,default=-27.5)
    ap.add_argument("--cross-max-nm",type=float,default=25.0)
    ap.add_argument("--cross-step-nm",type=float,default=1.0)
    args=ap.parse_args()
    obj=json.loads(Path(args.arc_geojson).read_text(encoding="utf-8"))
    lines=extract_lines(obj)
    arc=[]
    for line in lines:
        for a,b in zip(line,line[1:]): arc.extend(densify_segment(a,b,args.along_step_km))
        arc.append(tuple(line[-1]))
    arc=[p for p in arc if args.lat_min-1e-9 <= p[1] <= args.lat_max+1e-9]
    if len(arc)<3: raise SystemExit("Official arc has insufficient points inside requested latitude corridor")
    rows=[]
    for i,(lon,lat) in enumerate(arc):
        if i==0: lon2,lat2=arc[1]; brg=bearing_deg(lat,lon,lat2,lon2)
        elif i==len(arc)-1: lon0,lat0=arc[-2]; brg=bearing_deg(lat0,lon0,lat,lon)
        else:
            lon0,lat0=arc[i-1]; lon2,lat2=arc[i+1]
            brg=bearing_deg(lat0,lon0,lat2,lon2)
        cross=args.cross_min_nm
        while cross <= args.cross_max_nm+1e-9:
            side_brg=(brg+90) % 360 if cross>=0 else (brg-90) % 360
            plat,plon=destination(lat,lon,side_brg,abs(cross)*NM_KM)
            rows.append({
                "arc_index":i,"arc_lat":lat,"arc_lon":lon,
                "lat":plat,"lon":plon,"cross_arc_nm":cross,
                "pd_atsb_ga":"","pd_oi2018":"","pd_oi2025_26":"",
                "status":"REAL_ARC_GEOMETRY_PD_UNALLOCATED"
            })
            cross += args.cross_step_nm
    p=Path(args.out); p.parent.mkdir(parents=True,exist_ok=True)
    with p.open("w",newline="",encoding="utf-8") as h:
        w=csv.DictWriter(h,fieldnames=rows[0].keys()); w.writeheader(); w.writerows(rows)
    print(f"Wrote {len(rows)} real geographic cells from official arc geometry; Pd remains unallocated")

if __name__=="__main__": main()
