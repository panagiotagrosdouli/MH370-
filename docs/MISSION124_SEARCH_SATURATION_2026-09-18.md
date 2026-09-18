# Mission124 exact-path saturation audit — 2026-09-18

## Result

A second, stricter search excluded the known forum index and searched the wider indexed web for the exact basename, Fugro_combined + Mission124, and candidate GDB/LAS-XYI siblings.

No independent mirror, cache, sibling filename, or alternate indexed copy was recovered.

## What remains established

The historical indexed record preserves the literal NCI fileServer path:
iy57/final_processed/mbes/backscatter/Fugro_combined/auv/png/GP1500_6_Mission124_BS_Mosaic_1m_UTM45s.png

The archived official README independently establishes the collection structure and says the AUV backscatter branch had png, las_xyi and gdb representations at collection level.

The official AusSeabed SQL schema independently contains a spatial final_processed table with source URI and EPSG:4326 geometry.

## New conclusion

The public search-engine route for this exact Mission124 artifact is now saturated: repeating basename/sibling searches has low expected value.

The next high-value recovery route is database/catalogue level, not filename level:
1. recover a final_processed catalogue/database export or API response;
2. recover File_Links.txt;
3. recover cached THREDDS catalog XML/HTML;
4. query an official GA/AusSeabed data service capable of returning source-file metadata by AOI.

Until one of those succeeds, Mission124 cannot be spatially placed from its PNG filename alone.

No coordinate and no Pd are inferred.
