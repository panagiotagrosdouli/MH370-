# Exact Phase-2 source-file recovery — 2026-09-18

## Breakthrough: exact historical file path

A web-indexed 2021 record preserves an exact NCI fileServer path that was successfully downloaded at the time:

`iy57/final_processed/mbes/backscatter/Fugro_combined/auv/png/GP1500_6_Mission124_BS_Mosaic_1m_UTM45s.png`

This is the first recovered exact filename in our audit from the high-resolution `final_processed` AUV branch.

## What the filename establishes

Without interpreting image content, the path/filename itself provides reproducible metadata:
- collection: Phase-2 `final_processed`
- modality: MBES backscatter
- supplier grouping: Fugro_combined
- platform class: AUV
- representation: PNG
- mission token: Mission124
- product: backscatter mosaic
- nominal resolution token: 1m
- projection token: UTM45S

The archived report states that this file was downloadable through the NCI THREDDS fileServer in December 2021.

## Evidentiary limit

This is not a data-holiday polygon and not direct Pd. It is an exact processed AUV sonar-product artifact. A raster footprint/georeference, if the original bytes or sidecar metadata can be recovered, could provide authoritative spatial support for actual AUV product coverage.

The screenshot/forum interpretation is not used as sonar evidence.

## New deterministic search keys

The recovered naming convention gives high-value tokens for archive/mirror searches:
- `GP1500_6_Mission124`
- `BS_Mosaic_1m_UTM45s`
- `final_processed/mbes/backscatter/Fugro_combined/auv/png`

These can now be searched directly instead of guessing generic filenames.

## Next extraction

Search for sibling Mission### products, sidecars/world files, GDB equivalents, and cached THREDDS catalogue pages. If a georeferenced raster/TIFF/GDB is recovered, extract its exact bounds and intersect with the 33–36S residual domain. Do not infer bounds from the PNG alone unless georeferencing metadata is embedded or independently recovered.
