# 2026-11-20 — Study 2: built an OPTIONAL v2 import with Block 4b + Opportunism flip (Tariff)

Draft-only. The READY spec, the 2026-09-11 import file and its builder were NOT edited.

## What I built
- `build_qualtrics_import_v2_optional.py` reads `Study2_Qualtrics_IMPORT_2026-09-11.txt` and writes `Study2_Qualtrics_IMPORT_OPTIONAL_v2_2026-11-20.txt` (run with `python3 -I`; asserts the insertion points exist exactly once).
- Change (a): new block "Attribution of Responsibility (draft)" between Manipulation Checks and Fairness, with the three items drafted in `2026-11-12-study2-locus-check-gap-and-draft-items.md` (external cause, avoidable, company/government/other responsibility matrix).
- Change (b): `opp_2` anchors flipped to 1 = Strongly disagree ... 7 = Strongly agree (the READY file's own recommendation).
- Result: 17 blocks / 35 questions, vs 16 blocks in the original (the original has 3 fewer questions: the 3 new ones). Verified by counting markers only; **not imported into Qualtrics**, so Advanced Format validity of the matrix question is untested.

## Things Britton must know before using it
1. Flipping opp_2 changes scoring: opp_2 is now scored directly (higher = more opportunism) while opp_1 (Bad=1 ... Good=7) becomes the reverse-keyed item. Check the opportunism composite scoring in the analysis plan.
2. The 4b wording is my own draft, not a validated scale; methods text must say so. The CDSII (McAuley et al. 1992) is the established alternative; item text/licensing not checked.
3. The matrix question has no export tags per row beyond Qualtrics defaults; rename rows after import.
4. Vignette "new tariffs" staleness (11-17 note) is NOT addressed in v2; that is a stimulus wording call and the vignette text lives in the import's vignette blocks.

## Search recheck (secondary only)
A search surfaced the Columbia tariff-itemization study again, this time credited to "Morwitz and coauthors". Earlier notes have credited Gladstone & Bellezza (10-18) and Morwitz & Fitzsimons (10-23). **Author attribution is still unresolved across sources.** No journal or working-paper link found; cite nothing until Britton opens the Columbia page.
