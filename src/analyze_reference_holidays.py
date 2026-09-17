#!/usr/bin/env python3
"""Audit a reference holiday GeoJSON without treating it as evidence-grade geometry.

The script intentionally refuses to emit a posterior ranking. It reports geometry
bounds and geodesic areas so approximate/debug layers can be detected before use.
"""
import argparse, json, math
from pathlib import Path

R = 6371.0088

def ring_area_km2(ring):
    # Spherical approximation adequate for auditing gross rectangle/area mismatch.
    if len(ring) < 4:
        return 0.0
    s = 0.0
    for (lon1, lat1), (lon2, lat2) in zip(ring, ring[1:]):
        p1, p2 = math.radians(lat1), math.radians(lat2)
        dl = math.radians(lon2-lon1)
        s += dl * (2 + math.sin(p1) + math.sin(p2))
    return abs(s) * R * R / 2.0

def polygon_area(coords):
    if not coords: return 0.0
    return max(0.0, ring_area_km2(coords[0]) - sum(ring_area_km2(r) for r in coords[1:]))

def geom_area(g):
    if g['type'] == 'Polygon': return polygon_area(g['coordinates'])
    if g['type'] == 'MultiPolygon': return sum(polygon_area(p) for p in g['coordinates'])
    return 0.0

def points(g):
    def walk(x):
        if isinstance(x, list) and len(x) >= 2 and all(isinstance(v,(int,float)) for v in x[:2]):
            yield x[0], x[1]
        elif isinstance(x, list):
            for y in x: yield from walk(y)
    yield from walk(g['coordinates'])

def main():
    ap=argparse.ArgumentParser(); ap.add_argument('geojson'); args=ap.parse_args()
    fc=json.loads(Path(args.geojson).read_text())
    print('id,declared_km2,geometry_km2,min_lon,min_lat,max_lon,max_lat,ratio_geometry_to_declared')
    for i,f in enumerate(fc.get('features', []),1):
        ps=list(points(f['geometry'])); xs=[p[0] for p in ps]; ys=[p[1] for p in ps]
        a=geom_area(f['geometry']); d=f.get('properties',{}).get('area_km2')
        ratio=(a/d) if isinstance(d,(int,float)) and d else ''
        ident=f.get('properties',{}).get('id',i)
        print(f'{ident},{d},{a:.3f},{min(xs):.6f},{min(ys):.6f},{max(xs):.6f},{max(ys):.6f},{ratio}')

if __name__ == '__main__': main()
