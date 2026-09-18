# End-of-flight hypothesis mixture — 2026-09-18

The pipeline now keeps three end-of-flight branches separate:
- H_U: uncontrolled / rapid descent after the final SATCOM event;
- H_G: unpowered glide branch;
- H_C: continued-control branch.

The location likelihood is mixed only after each branch has its own spatial likelihood:
P(L|D_EOF) = sum_H P(L|D_EOF,H) P(H|D).

This prevents a long-glide tail from being hidden inside a single arbitrary cross-arc Gaussian.

The default numerical weights in the command-line tool are illustrative engineering defaults, not evidence-derived posterior probabilities. They must be swept in sensitivity analysis and must not be cited as factual probabilities of pilot/control scenarios.

Official ATSB end-of-flight work is the primary evidence source for constructing H_U. H_G and H_C are sensitivity branches and require explicit aerodynamic/state assumptions. The western 90–92E scenario remains in H_G/H_C sensitivity space unless independent evidence increases its support.

The script fail-closes on missing branch likelihoods, negative likelihoods, invalid mixture weights or zero mass.
