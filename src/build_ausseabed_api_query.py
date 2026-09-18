#!/usr/bin/env python3
"""Build official AusSeabed MH370 API URLs. Network retrieval is external."""
import argparse,urllib.parse
p=argparse.ArgumentParser()
p.add_argument("--base",default="https://mh370-api.ausseabed.gov.au")
p.add_argument("--product",default="Visualisation and Coverage Summaries")
p.add_argument("--wkt")
p.add_argument("--mode",choices=["products","details","features","query","download-url-list"],default="products")
a=p.parse_args()
base=a.base.rstrip("/"); prod=urllib.parse.quote(a.product,safe="")
if a.mode=="products": url=base+"/products"
elif a.mode=="details": url=base+"/products/"+prod
else:
 if not a.wkt: raise SystemExit("--wkt required")
 q=urllib.parse.urlencode({"geom":a.wkt,"pageSize":500,"currentPage":1})
 url=base+"/products/"+prod+"/"+a.mode+"?"+q
print(url)
if a.mode=="features": print("classification=CATALOGUE_INDEX_GEOMETRY_NOT_PD")
if a.mode=="download-url-list": print("classification=SOURCE_URI_ARCHIVE_REQUIRES_SEMANTIC_INSPECTION")
