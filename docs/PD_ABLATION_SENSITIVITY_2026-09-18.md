# Pd sensitivity and ablation layer — 2026-09-18

ATSB Figure 73 provides the official aggregate calibration: combined High Confidence Coverage 97.4%, Lower Confidence Coverage 2.1%, Data Gaps 0.5%. ATSB defines High Confidence as >95% confidence of detection, Lower Confidence as ~70% average confidence, and Data Gaps as zero confidence.

Because ~70% is an aggregate average rather than a universal polygon-specific Pd, the sensitivity runner now evaluates Lower Confidence Pd at 0.50, 0.70 and 0.90. High Confidence is evaluated at 0.95, 0.97 and 0.99.

It also runs leave-one-evidence-out cases:
- drop drift;
- drop EOF;
- drop search non-detection.

The purpose is to expose ranking instability. A residual component that appears only at one Pd choice or collapses when one model-derived evidence term is removed must not be promoted as robust.

This script requires cell-level authoritative inputs produced by the evidence-grade pipeline. It does not make the current proxy grid evidence-grade.
