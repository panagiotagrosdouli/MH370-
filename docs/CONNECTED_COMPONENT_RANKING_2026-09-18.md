# Connected residual-component ranking — 2026-09-18

The evidence-grade pipeline now ranks contiguous residual regions rather than isolated peak cells.

The component layer aggregates:
- posterior mass;
- physical area (km2);
- posterior mass density;
- cell count;
- cumulative mass.

It deliberately does NOT infer adjacency from latitude/longitude. Component IDs must come from an upstream geometry operation on authoritative polygons/grid topology. This prevents diagonal/grid-resolution artefacts from being mistaken for real contiguous search targets.

Why this matters: ATSB's final operational report explicitly notes that many individual data gaps/LPDs are small, and that filtering by a 200 m x 200 m threshold removes many objects while removing much less total area. Component-level accounting therefore has to preserve raw geometry first and only then assess whether a connected region is physically capable of containing a debris field.

Robust ranking sequence:
authoritative geometry -> connected components -> cell posterior -> component mass/area/density -> Pd sensitivity -> evidence ablations.

No component result is produced until authoritative geometry is available.
