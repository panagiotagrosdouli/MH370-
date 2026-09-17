"""Fetch official GA/ATSB ArcGIS geometries used by the MH370 residual-search model.

No synthetic geometry is generated. If a service fails, the script fails closed.
"""
from __future__ import annotations
import json
import urllib.parse
import urllib.request
from pathlib import Path

SERVICES = {
    "seventh_arc": "https://services1.arcgis.com/wfNKYeHsOyaFyPw3/ArcGIS/rest/services/7thArc_SingleLine/FeatureServer/0/query",
    "wide_search_area": "https://services1.arcgis.com/wfNKYeHsOyaFyPw3/ArcGIS/rest/services/WideSearchArea/FeatureServer/0/query",
    "debris": "https://services1.arcgis.com/wfNKYeHsOyaFyPw3/ArcGIS/rest/services/Possible_MH370_Debris_Recovered/FeatureServer/0/query",
}

def query_geojson(endpoint: str) -> dict:
    params = urllib.parse.urlencode({
        "where": "1=1",
        "outFields": "*",
        "returnGeometry": "true",
        "outSR": "4326",
        "f": "geojson",
    })
    req = urllib.request.Request(endpoint + "?" + params, headers={"User-Agent": "MH370-research/1.0"})
    with urllib.request.urlopen(req, timeout=90) as r:
        obj = json.loads(r.read().decode("utf-8"))
    if obj.get("type") != "FeatureCollection" or not obj.get("features"):
        raise RuntimeError(f"No usable features returned from {endpoint}")
    return obj

def main() -> None:
    root = Path("data/derived/official_arcgis")
    root.mkdir(parents=True, exist_ok=True)
    manifest = {}
    for name, endpoint in SERVICES.items():
        data = query_geojson(endpoint)
        path = root / f"{name}.geojson"
        path.write_text(json.dumps(data, indent=2), encoding="utf-8")
        manifest[name] = {"endpoint": endpoint, "features": len(data["features"]), "file": str(path)}
        print(name, len(data["features"]))
    (root / "manifest.json").write_text(json.dumps(manifest, indent=2), encoding="utf-8")

if __name__ == "__main__":
    main()
