# Inmarsat-3F1 state-vector recovery — 2026-09-18

The published Inmarsat paper *The Search for MH370* provides ECEF position and velocity of I-3F1 at eleven key times from 16:30 to 00:20. These are operator-derived satellite states and are preferable to substituting a generic nominal geostationary position.

The table has now been transcribed into machine-readable CSV. It includes position x/y/z in km and velocity components in km/s.

The same source explains that BFO depends on uplink/downlink Doppler, aircraft Doppler compensation, satellite translation, GES AFC and fixed bias. Uplink/downlink frequencies are 1646.6525 MHz and 3615.1525 MHz. Therefore satellite velocity is essential; a fixed satellite at 64.5E is insufficient for evidence-grade BFO reconstruction.

A linear interpolation utility is included only as a transparent validation bridge between the published one-minute/key-time states and handshake timestamps. It must not be represented as Inmarsat's original sub-second ephemeris. Sensitivity to interpolation and comparison with independent fitted ephemerides are required.

Status: OPERATOR_STATE_VECTORS_RECOVERED / BTO_ARC_GEOMETRY_NEXT / FULL_BFO_MODEL_PENDING.
