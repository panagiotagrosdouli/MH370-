# Phase-2 final_processed finding — 2026-09-18

The archived Phase-2 README describes a final_processed collection containing high-resolution sidescan and multibeam products. Fugro combined sidescan is separated into deep-tow and AUV branches, with XTF, TIFF and 1 m / 5 m GDB products. Go Phoenix and Dong Hai Jiu SAS products are also separated. The README explicitly says visualisation5m is only an image for visualisation and does not contain data.

The official AusSeabed SQL schema independently defines marine_mh370.final_processed with path, name, md5, file size, extension, bundle, vessel, source URI, timestamps and EPSG:4326 geometry, plus final_processed_geoms.

Important: the public MH370 API product configuration does not expose a product named Final Processed.

This reveals a second official recovery route. A recovered final_processed inventory/database export could spatially identify source high-resolution AUV/deep-tow sonar products without relying on rendered WMS masks.

Priority remains: recover iy57/gis coverage/data-holiday objects and, in parallel, recover final_processed rows/source URIs. Neither catalogue geometry nor visualisation5m is Pd by itself.
