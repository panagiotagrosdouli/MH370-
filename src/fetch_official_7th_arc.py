#!/usr/bin/env python3
"""Fetch the verified official 7th-Arc FeatureServer geometry, fail closed."""
import json, urllib.parse, urllib.request
BASE="https://services1.arcgis.com/wfNKYeHsOyaFyPw3/ArcGIS/rest/services/7thArc_SingleLine/FeatureServer/0/query"
params={"where":"1=1","outFields":"*","returnGeometry":"true","outSR":"4326","f":"geojson"}
url=BASE+"?"+urllib.parse.urlencode(params)
with urllib.request.urlopen(url,timeout=30) as r:
    obj=json.load(r)
if not obj.get("features"):
    raise SystemExit("FAIL_CLOSED: no features returned")
with open("data/derived/official_7th_arc.geojson","w",encoding="utf-8") as f:
    json.dump(obj,f,indent=2)
print("saved",len(obj["features"]),"feature(s)")
