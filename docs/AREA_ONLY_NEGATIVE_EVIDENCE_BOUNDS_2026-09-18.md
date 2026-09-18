# Area-only negative-evidence bounds — 2026-09-18

This stage prevents a common inference error: a tiny data-gap area can have high posterior *density* after non-detection without necessarily containing most posterior *mass*.

ATSB's combined 100 m metric reports 97.4% High Confidence, 2.1% Lower Confidence, and 0.5% Data Gaps. High Confidence means >95% detection, Lower Confidence is about 70% on average, and Data Gaps have zero detection confidence.

Under the deliberately artificial assumption of equal prior density over the already-selected searched area, retained mass is proportional to area times (1-Pd). This is a diagnostic bound only, not the MH370 location posterior. Physics, drift, EOF and exact polygon geometry are intentionally absent.

The First Principles report also states that LPD confidence can vary roughly 50–90% with seabed texture/composition, and that about 35% of LPD areas had multiple sonar passes. Therefore 0.70 must remain an aggregate reference/sensitivity value rather than a per-polygon truth.

Key interpretation: negative evidence raises the relative density of genuine gaps/LPD cells, but the enormous High-Confidence area can still retain non-negligible total mass unless Pd is extremely close to one. Do not rank a small gap from Pd alone.

Status: DIAGNOSTIC_BOUND_READY / NOT_A_GEOGRAPHIC_POSTERIOR.
