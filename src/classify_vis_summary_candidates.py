#!/usr/bin/env python3
"""Classify MH370 vis_summary file records without assigning Pd."""
import re
TOKENS=("holiday","coverage","coverages","database","geodatabase","gdb","shp","shape","trackline","tracklines","gis")
def score(name,uri=""):
 s=(name+" "+uri).lower()
 return sum(1 for t in TOKENS if re.search(r"(^|[^a-z])"+re.escape(t)+r"([^a-z]|$)",s))
def classify(name,uri=""):
 n=(name+" "+uri).lower()
 if any(x in n for x in ("holiday","geodatabase",".gdb","database")): return "AUTHORITATIVE_CANDIDATE_HIGH"
 if any(x in n for x in ("coverage",".shp","shape","trackline")): return "AUTHORITATIVE_CANDIDATE_REVIEW"
 return "INDEX_OR_OTHER"
