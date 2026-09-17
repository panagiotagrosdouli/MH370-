# Data and Artifacts

The project currently has two generated spreadsheet artifacts outside GitHub:

- `MH370_Master_Forensic_Dataset.xlsx`
- `MH370_Computational_Search_Model_v3.xlsx`

They contain the structured evidence tables and the current gridded proxy posterior.

## Why the XLSX files are not yet committed here

The connected GitHub action available in this environment writes UTF-8 text files, not arbitrary binary workbook bytes. The repository therefore contains the reproducible text/code layer first. The workbook artifacts should be uploaded separately or exported to CSV/Parquet components before versioning.

## Recommended versioned data layout

```text
data/
  raw/
    official/
      malaysia/
      atsb/
      dstg/
      csiro/
      geoscience_australia/
  processed/
    satcom/
    radar/
    debris/
    search_coverage/
    bathymetry/
  derived/
    posterior/
    sensitivity/
```

## Provenance rules

Every processed observation should preserve at least:

- `source_authority`
- `source_document`
- `source_url`
- `timestamp_UTC` where applicable
- `latitude`, `longitude` where officially available
- `direct_or_inferred`
- `evidence_class`
- `measurement_uncertainty`
- `model_dependent`
- `dependency_group`
- `systematic_error_notes`

## Important current limitation

The 2025/26 Malaysian update provides a total surveyed area of approximately **7,571 km²** within the new defined search area, but the source used in the present model does not provide a machine-readable cell-level AUV coverage polygon. Therefore the current model records the negative evidence but does not invent a spatial mask.

Similarly, full quantitative updating for historical searches requires exact coverage geometry and local probability-of-detection estimates rather than simple binary searched/unsearched labels.
