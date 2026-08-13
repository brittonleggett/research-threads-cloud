# 2026-08-13 — SP500 vs. Study 1: formal statistical comparison (exploratory, first pass)

**Recovery note:** the original write-up from this run was lost when its container couldn't
push (see `OVERNIGHT_SUMMARY_2026-08-13.md`). This is a manual recreation of the actual test
output, which was captured in full in the run log — the numbers below are exact, not
reconstructed from memory. The original file's fuller prose discussion (interpretation,
caveats in the author's own words) was not recoverable and isn't reproduced here.

Addresses the "not yet run" gap flagged in `SP500_Tariff_Filings/STANDALONE_PAPER_OUTLINE_2026-08-04.md`:
a formal test of whether the SEC-filing corpus (audience: investors/regulators) and Study 1's
consumer/press corpus (audience: consumers) differ in how explicitly they attribute price
changes to tariffs. Uses data/codes already in the repo — no new coding was done.

## Results

- SEC filings, realized-impact subset (n=80): **18.8%** name tariffs explicitly as the cause.
- Study 1 consumer/press corpus: **75.0%** name tariffs explicitly as the cause.
- 2×2 Fisher's exact test (explicit vs. not-explicit, table `[[15, 65], [9, 3]]`): odds ratio =
  **0.077**, **p = 0.000193**.
- 2×3 chi-square (descriptive only — some expected cell counts are below 5, so treat as
  suggestive not confirmatory): χ² = 18.711, df = 2, p = 8.6e-05.

## Status — explicitly not citable yet

This is a first pass on top of existing coding, not a validated result. Before it could go in
a draft it needs: a second, independent coder on the causation-attribution scheme (both the SEC
bucket and the Study 1 bucket), and Britton's sign-off that this comparison belongs in the
paper at all — that's a Phase 3 / design call, not something to treat as decided.
