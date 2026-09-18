# SATCOM event cross-check — 2026-09-18

A primary-source cross-check of the core accident-flight signalling rows is now committed.

The ATSB signalling-log update explicitly states that R600 log-on BTO requires subtraction of 4,600 microseconds when comparing with R1200 messages, and says the same correction applies at 18:25:27 and 00:19:29. Thus 18:25:27 is 17,120 raw -> 12,520 corrected, and 00:19:29 is 23,000 raw -> 18,400 corrected.

The published signalling table gives the sequence used here:
19:41:03 11,500 us / 111 Hz;
20:41:05 11,740 / 141;
21:41:27 12,780 / 168;
22:41:22 14,540 / 204;
00:11:00 18,040 / 252;
00:19:29 raw 23,000 / 182;
00:19:37 raw 49,660 / -2.

The 00:19:37 BTO is not treated as a normal seventh-arc range observation. It remains a special log-on acknowledgement value with different correction/interpretation requirements.

ATSB separately states that extrapolating the 18:39–00:11 BFO trend would give roughly 260 Hz at 00:19 under unchanged flight/SATCOM conditions; the measured 182 and -2 Hz values motivated the high-descent-rate analysis.

This file is an input contract, not an independent reconstructed trajectory. Satellite ephemeris/state-vector validation is still required before RAW_SATCOM route B can produce an evidence-grade geographic likelihood.

Status: CORE_BTO_BFO_ROWS_PRIMARY_CROSSCHECKED / EPHEMERIS_RECONSTRUCTION_PENDING.
