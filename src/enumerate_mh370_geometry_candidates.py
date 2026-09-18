#!/usr/bin/env python3
"""Generate safe MH370 API discovery requests for authoritative geometry candidates."""
from urllib.parse import urlencode,quote
BASE="https://mh370-api.ausseabed.gov.au"
PRODUCT="Visualisation and Coverage Summaries"
def endpoint(kind,**q):
    return f"{BASE}/{kind}/{quote(PRODUCT,safe='')}?{urlencode(q)}"
if __name__=="__main__":
    print(endpoint("query",pageSize=500,currentPage=1,includeEmptyValues="true"))
    print(endpoint("features"))
    # Do not infer Pd from returned feature geometry.
