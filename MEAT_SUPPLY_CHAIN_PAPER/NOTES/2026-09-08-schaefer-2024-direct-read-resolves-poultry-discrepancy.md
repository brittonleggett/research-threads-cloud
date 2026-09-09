# 2026-09-08 — Schaefer et al. (2024) read directly, poultry-concentration discrepancy (Open Decision #6) RESOLVED

Britton retrieved the actual paper via his institutional library access: Saitone, Schaefer,
Scheitrum, Arita, Breneman, Nemec Boehm & Maples (2024), "Consolidation and Concentration in
U.S. Meat Processing: Updated Measures Using Plant-Level Data," *Review of Industrial
Organization* 64, 35-56. Saved to
`LITERATURE/PDFs/Saitone_Schaefer_et_al_2024_RIO_Consolidation_Concentration_Meat_Processing.pdf`
(kept out of the public `research-threads-cloud` git history — see repo-root `.gitignore`,
added this session, which now blanket-ignores `*.pdf` repo-wide per the standing
no-copyrighted-PDFs-in-a-public-repo rule).

## The actual figures, read directly, not via secondary synthesis

- **Broiler (chicken) CR4, FY2021: 52%** ("FSIS data for CY 2021 indicate that the CR4 in the
  broiler industry is 52%"). No 2019-specific broiler CR4 figure is stated in the body text, but
  the historical trajectory the paper itself reports (32% in 1980 → 51% in 2010, per Crespi et
  al. 2012 → 52% in 2021) leaves no room for a 78% figure at any point in this series.
- **Cattle (steer/heifer) CR4, FY2021: 77%.**
- **Swine CR4, FY2021: 70%** (stated in the intro as "the CR4 for swine processing was 70%" for
  2021).
- **Broiler CR10, FY2021: 77%.** This is the likely real source of the "78%" figure that's been
  circulating in this project since 2026-09-03 — a highly plausible **CR4-vs-CR10 mix-up**:
  broiler CR10 (77%) is nearly identical to the erroneous "broiler CR4 = 78%" figure this project
  picked up from an AI-search synthesis, while broiler CR4 itself (52%) is nothing close. Not
  100% certain (the exact provenance of the original "78%" claim traces to a different, NETS-
  based 2025 companion paper by five of the same authors, per the 2026-09-07 note), but this
  reading adds a second, independent, concrete explanation for how a number in the high-70s could
  plausibly get attached to "broiler concentration" in this literature — worth citing as
  corroboration either way.

## What this resolves

**Open Decision #6 in `PROJECT_STATUS.md` is now closed.** The actually-cited Schaefer et al.
(2024) paper's own broiler CR4 figure (52%, FY2021) is close to USDA PSD's official 53-55%
figure, not 78%. The project should treat "poultry CR4 ≈ 52-55%, FY2021" as the anchor number
going forward, sourced now to a **direct primary read of the actually-cited paper**, not
secondary corroboration. The "78%" figure should not be used as a broiler CR4 figure anywhere in
this project — if it's cited at all, it should be attributed to the 2025 companion paper's NETS-
based measure (a different dataset/methodology), with that distinction stated explicitly.

## Other figures worth cross-checking against the project's existing evidence table

This paper's own FY2021 numbers (cattle CR4 77%, swine CR4 70%, broiler CR4 52%) should be
reconciled against `LITERATURE/Market_Concentration_Evidence.md`'s existing PSD-sourced figures
(cattle 81% for 2020-2021, hog 65% for 2021) — these are two different official/near-official
sources for overlapping years and don't match exactly (77% vs. 81% for cattle is a real, if
modest, gap). Worth a note in that file flagging both sources rather than treating either as
uniquely authoritative — likely a measurement-methodology difference (this paper explicitly notes
its FSIS plant-level data "improve — both with respect to accuracy and granularity — on previous
measures that rely on census information or on data from GIPSA," i.e., it's not claiming to
reproduce PSD's own numbers exactly).

**Regional/monopsony finding, not yet in the project's evidence base:** this paper's Table 2
(spatial competition by USDA NASS region) is a genuinely strong addition to the project's
monopsony-relevant evidence — e.g., cattle-plant "neighbor" competition in the Eastern Mountain
region (KY/TN/WV/VA/NC) fell from 59.9 competing plants within 150 miles (1991) to just 18.2
(2021), and similar sharp regional declines exist for swine in the Northwest and Southern regions
— worth pulling into `Market_Concentration_Evidence.md`'s regional/monopsony section alongside
the existing Schaefer-via-MacDonald regional citation.
