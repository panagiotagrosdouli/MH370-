# SATCOM noise-semantics resolution — 2026-09-18

The previous log-on uncertainty blocker is now resolved from the primary ATSB-hosted DSTG Bayesian Methods report, Table 10.1.

Authoritative accident-flight BTO measurement classes:
- 18:25:34 anomalous R1200: sigma 43 us; BFO unusable.
- 18:28:05 / 18:28:14 R1200: sigma 29 us; BFO usable.
- 19:41:02, 20:41:04, 21:41:26, 22:41:21 R1200: sigma 29 us; BFO usable.
- 00:10:59 R1200: sigma 29 us; BFO usable.
- 00:19:29 R600: sigma 63 us; BFO unusable.
- 00:19:37 anomalous R1200: sigma 43 us; BFO unusable.

DSTG explicitly states that the two anomalous R1200 messages and the R600 message occurred during transient SATCOM phases; their BFO values cannot be used, and BTO variance is inflated to account for correction uncertainty.

Separately, the Inmarsat Journal of Navigation paper gives the fixed BTO timing bias as -495679 us, estimated from 17 known-position pre-takeoff measurements. This value is now primary-source verified, not merely an external benchmark constant.

Important reconciliation: the signalling-log event timestamp commonly quoted as 18:25:27 is not the exact Table-10.1 measurement row used by the DSTG filter (18:25:34). Likewise hourly timestamps differ by about one second between signalling records and the DSTG measurement table. Downstream likelihood code must preserve the exact measurement product/timestamp instead of silently joining by rounded time.

Status: BTO_BIAS_PRIMARY_VERIFIED / DSTG_BTO_SIGMAS_RESOLVED / EXACT_EVENT_MAPPING_REQUIRED.
