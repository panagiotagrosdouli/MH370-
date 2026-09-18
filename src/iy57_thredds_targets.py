#!/usr/bin/env python3
"""Generate non-guessing THREDDS catalogue traversal targets for historical iy57."""
from urllib.parse import urljoin
ROOT="https://dapds00.nci.org.au/thredds/catalog/iy57/"
TARGETS=[
 "catalog.html",
 "catalog.xml",
 "gis/catalog.html",
 "gis/catalog.xml",
]
if __name__=="__main__":
 for x in TARGETS: print(urljoin(ROOT,x))
