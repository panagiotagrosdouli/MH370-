#!/usr/bin/env python3
"""Generate direct-NCI GIS recovery targets alongside API discovery."""
TARGETS=("holiday","coverage","geodatabase",".gdb",".shp","trackline","database")
def candidate(path):
 p=path.lower()
 return any(t in p for t in TARGETS)
def rank(path):
 p=path.lower()
 return sum(t in p for t in TARGETS)
