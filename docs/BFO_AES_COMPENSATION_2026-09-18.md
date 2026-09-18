# AES Doppler compensation implementation — 2026-09-18

The primary Inmarsat description says the aircraft SDU compensates uplink Doppler using aircraft latitude, longitude, track and ground speed, assuming a nominal geostationary satellite position. It does not compensate vertical speed. This term is therefore geometrically reconstructable without fitting the accident BFO.

Implemented an explicit nominal-GEO slant-range derivative at uplink frequency 1646.6525 MHz. Inputs are the Table-9 aircraft state, nominal satellite longitude 64.5E and nominal GEO altitude 35788.12 km. The code intentionally excludes vertical velocity.

Validation target is the published Table-9 aircraft compensation sequence, including approximately -72, +143, +331, +497 and +691 Hz on the stable southbound example. Sign and magnitude must agree before the term is admitted to the complete BFO forward model.

Important distinction: AES compensation is reconstructable physics; the Perth GES AFC plus satellite translation correction remains an empirical measured term and is not inferred from this routine.

Status: AES_COMPENSATION_IMPLEMENTED / TABLE9_NUMERIC_VALIDATION_PENDING.
