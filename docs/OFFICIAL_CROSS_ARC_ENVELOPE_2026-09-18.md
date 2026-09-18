# Official cross-arc envelope verification — 2026-09-18

## Primary-source result

The ATSB Maps page states that, at the 7th arc, MH370 was considered to have exhausted fuel and to have been descending. The resulting end-of-flight search envelope was:

- no more than 27.5 NM (51 km) west of the 7th arc;
- no more than 25 NM (46 km) east of the 7th arc.

The full 7th arc extends from 20S to 40S, while the First Principles Review narrows the high-value residual latitude band to approximately 33S–36S and describes the likely impact as close to the arc, within about 25 NM.

## Consequence for this repository

The existing geodesic grid defaults:
`cross_min_nm=-27.5`
`cross_max_nm=+25.0`

are now primary-source verified rather than provisional.

This does not imply uniform probability across the envelope. The cross-arc prior must remain concentrated toward the arc, with end-of-flight hypothesis sensitivity.

## Drift anchors

CSIRO Part III gives a model-derived maximum at 35.6S, 92.8E, with nearby alternatives including western-side locations around 34.7S, 92.6E and 35.3S, 91.8E. These are drift-model inferences conditional on uncertain satellite-image debris identification, not wreckage observations.

Therefore 35.6S/92.8E may be used as a drift-model anchor/check, not as a discovered coordinate.

## Geometry implication

The authoritative residual-search domain can now be specified without an arbitrary cross-track width:

D = {x : 33S <= lat(x) <= 36S and -27.5 NM <= cross_arc(x) <= +25 NM}

with sign convention west/east documented by the grid implementation.

The next ranking must distinguish:
- prior probability density within D;
- authoritative search coverage/LPD/gaps within D;
- alternative EOF hypotheses that can put probability outside D as explicit sensitivity mass.

No physical-location claim follows from defining D.
