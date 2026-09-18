# First-principles BFO geometry kernel — 2026-09-18

Primary Inmarsat documentation confirms uplink 1646.6525 MHz and downlink 3615.1525 MHz, with Doppler determined from relative aircraft/satellite/GES motion. The AES compensation is not a generic correction: it is computed from aircraft latitude, longitude, track and ground speed against a nominal satellite location over the equator, and it does not compensate vertical motion.

Implemented a WGS84/ECEF Doppler kernel with aircraft horizontal/vertical velocity decomposition and explicit uplink/downlink line-of-sight terms. This is deliberately lower-level than the Table-9 bookkeeping test.

Important validation rule: the kernel is not yet accepted merely because its equations look correct. It must reproduce the primary Table-9 component values. AFC plus satellite-translation correction remains empirical/tabulated in the Inmarsat treatment and must not be fabricated from orbital geometry.

The primary source also documents a stationary-aircraft calibration example at 16:30: uplink Doppler -6 Hz, downlink Doppler -85 Hz, satellite plus GES AFC offset +29 Hz, measured BFO 88 Hz and inferred fixed bias 150 Hz. This becomes an additional pre-flight unit-test target.

Status: ECEF_DOPPLER_KERNEL_IMPLEMENTED / TABLE9_COMPONENT_VALIDATION_PENDING / AFC_EMPIRICAL_TERM_NOT_SYNTHESIZED.
