#!/usr/bin/env python3
"""Audit derived WMS coverage before it can enter negative-evidence modelling.

This deliberately does not assign Pd. It checks provenance metadata and marks
WMS-derived footprints as cross-check-only.
"""
import json, sys
from pathlib import Path

REQUIRED={"source_wms","instrument","resolution","phase","extracted_date","attribution"}

def main():
    if len(sys.argv)<2:
        raise SystemExit("usage: audit_wms_coverage.py file.geojson [file.geojson ...]")
    report=[]
    for name in sys.argv[1:]:
        p=Path(name); d=json.loads(p.read_text())
        feats=d.get("features",[])
        missing=set()
        for f in feats:
            missing |= REQUIRED-set(f.get("properties",{}))
        report.append({
            "file":str(p),"features":len(feats),
            "missing_metadata":sorted(missing),
            "classification":"DERIVED_WMS_CROSSCHECK_ONLY",
            "pd_allowed":False
        })
    print(json.dumps(report,indent=2))
if __name__=="__main__": main()
