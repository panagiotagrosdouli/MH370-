# Mission124 sibling-recovery audit — 2026-09-18

## Exact-file search

Targeted exact-string searches were run for the recovered AUV product:
GP1500_6_Mission124_BS_Mosaic_1m_UTM45s.png

Sibling searches covered TIFF, GDB, LAS/XYI, neighbouring Mission123/Mission125 naming, and shortened Mission124 tokens.

## Result

No indexed sibling TIFF/GDB/LAS/XYI file and no neighbouring Mission123/Mission125 product was recovered in this pass.

The exact PNG path remains independently visible in a web-indexed historical record, which says it was downloaded from the NCI THREDDS fileServer on 6 Dec 2021.

## Stronger structural inference, not file recovery

The archived official README states that final_processed MBES backscatter for Fugro_combined/AUV was organised into:
- png
- las_xyi
- gdb

Therefore Mission124 likely belonged to a product family for which alternate representations existed at collection level. This does NOT establish that an identically named Mission124 GDB or LAS/XYI sibling existed. Filename substitution is prohibited.

## New recovery rule

For each exact recovered source path:
1. preserve the literal filename/path;
2. search exact basename and stable mission token;
3. search collection-level sibling directories;
4. accept sibling only if its exact filename/path is independently recovered;
5. never synthesize a sibling filename by extension or directory replacement.

## Current evidence state

Mission124 PNG path: EXACT.
Mission124 georeferenced sibling: NOT RECOVERED.
Mission124 footprint: UNKNOWN.
Mission124 Pd contribution: NONE.

This prevents an apparently plausible but unsupported georeferencing shortcut.
