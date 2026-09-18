# Evidence-grade residual-ranking engine — 2026-09-18

The ranking engine is now implemented before the missing GIS arrives.

Core update:
P(x|D,ND) ∝ P_physics(x) L_drift(x) L_EOF(x) P(ND|x).

Coverage mapping is deliberately conservative:
- DATA_GAP -> P(ND)=1
- LOWER_CONFIDENCE -> reference P(ND)=0.30
- HIGH_CONFIDENCE -> P(ND)=1-Pd, with Pd sensitivity constrained to >=0.95.

The engine fails closed unless every row carries an accepted authoritative geometry provenance. Catalogue footprints, WMS-derived polygons, vessel tracks, hand-drawn search bands and proxy grids are rejected.

It also fails on unknown coverage classes, missing evidence columns, negative likelihood terms, or zero posterior mass.

This is infrastructure, not a result: no current coordinate is promoted because the authoritative Arc/cell geometry gates remain unmet.

Next run sequence after GIS recovery:
1. intersect authoritative 7th-Arc corridor with Phase-2 coverage/holiday polygons;
2. rasterise/cell-integrate physics, drift and EOF terms;
3. run this engine under Pd sensitivity;
4. repeat ablations with drift/EOF/search-negative terms removed;
5. rank connected residual components, not isolated pixels.
