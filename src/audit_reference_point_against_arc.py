#!/usr/bin/env python3
"""Audit a proposed MH370 reference coordinate against the official seventh arc.

This is a *geometric consistency check*, not a wreckage finder.
Downloads public ATSB-associated ArcGIS geometry. It never synthesizes an arc.
Approximate nearest distance is refined by great-circle segment interpolation.
"""
from __future__ import annotations
import argparse
import json
import math
import urllib.request

URL = ("https://services1.arcgis.com/wfNKYeHsOyaFyPw3/ArcGIS/rest/services/"
       "7thArc_SingleLine/FeatureServer/0/query?where=1%3D1&"
       "outFields=*&returnGeometry=true&outSR=4326&f=geojson")
EARTH_KM = 6371.0088

def vec(lon, lat):
    lo, la = math.radians(lon), math.radians(lat)
    return (math.cos(la)*math.cos(lo), math.cos(la)*math.sin(lo), math.sin(la))

def dot(a,b): return sum(x*y for x,y in zip(a,b))
def angle(a,b): return math.acos(max(-1.,min(1.,dot(a,b))))
def slerp(a,b,t):
    theta=angle(a,b)
    if theta<1e-12: return a
    den=math.sin(theta)
    v=[(math.sin((1-t)*theta)*x+math.sin(t*theta)*y)/den for x,y in zip(a,b)]
    n=math.sqrt(dot(v,v))
    return tuple(x/n for x in v)

def nearest_arc(lat,lon,features):
    point=vec(lon,lat)
    best=(float('inf'),None,None)
    for feature in features:
        geom=feature.get('geometry') or {}
        if geom.get('type')=='LineString': lines=[geom.get('coordinates',[])]
        elif geom.get('type')=='MultiLineString': lines=geom.get('coordinates',[])
        else: continue
        for line in lines:
            for a,b in zip(line,line[1:]):
                va,vb=vec(*a[:2]),vec(*b[:2])
                # Coarse sampling plus golden-section minimization within segment.
                theta=angle(va,vb)
                chunks=max(1,math.ceil(theta*EARTH_KM/8))
                for k in range(chunks):
                    left,right=k/chunks,(k+1)/chunks
                    for _ in range(24):
                        x=left+(right-left)*0.38196601125
                        y=left+(right-left)*0.61803398875
                        if angle(point,slerp(va,vb,x)) < angle(point,slerp(va,vb,y)): right=y
                        else: left=x
                    v=slerp(va,vb,(left+right)/2)
                    distance=EARTH_KM*angle(point,v)
                    if distance<best[0]:
                        near_lat=math.degrees(math.asin(v[2]))
                        near_lon=math.degrees(math.atan2(v[1],v[0]))
                        best=(distance,near_lat,near_lon)
    if not math.isfinite(best[0]): raise ValueError('No valid official arc segments')
    return best

def main():
    p=argparse.ArgumentParser()
    p.add_argument('--lat',type=float,default=-35.6)
    p.add_argument('--lon',type=float,default=92.8)
    p.add_argument('--geojson',help='Local copy of official 7th arc GeoJSON (offline mode)')
    args=p.parse_args()
    if not (-90<=args.lat<=90 and -180<=args.lon<=180): p.error('Invalid coordinate')
    if args.geojson:
        with open(args.geojson,encoding='utf-8') as f: data=json.load(f)
        source=args.geojson
    else:
        req=urllib.request.Request(URL,headers={'User-Agent':'MH370-independent-research/1.0'})
        with urllib.request.urlopen(req,timeout=25) as response: data=json.load(response)
        source=URL
    features=data.get('features')
    if not isinstance(features,list) or not features: raise RuntimeError('Official arc data unavailable or empty')
    km,near_lat,near_lon=nearest_arc(args.lat,args.lon,features)
    print(json.dumps({
        'reference_point':{'lat':args.lat,'lon':args.lon},
        'nearest_official_arc_point':{'lat':round(near_lat,6),'lon':round(near_lon,6)},
        'minimum_distance_km':round(km,3),
        'minimum_distance_nm':round(km/1.852,3),
        'source':source,
        'interpretation':'Geometry check only: NOT a wreckage location or probability estimate'
    },indent=2))

if __name__=='__main__': main()
