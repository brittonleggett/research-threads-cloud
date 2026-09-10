# 2026-09-10 — Citation-accuracy pass (second full pass, after 2026-07-08)

## What this is

Per `SUBMISSION_TRACKER.md`'s own step-6 recommendation ("full citation-accuracy pass
... before submission"), re-checked citations across the manuscript-facing files:
`Introduction_and_Theory_DRAFT_2026-08-12.md`, `Study1_Methods_Section_DRAFT_2026-09-04_
CONSOLIDATED.md`, `Tariff_Manuscript_Working_Draft_2026-09-04.md`, and the scale
citations in `notes/2026-08-04-full-instrument-assembly.md`. This is the second full
pass — the first was `Overnight_Citation_Verification_2026-07-08.md`, which covered the
lit-review docx files, not these manuscript drafts. A partial 2026-09-03 Consensus.app
pass also caught one real error (Xia/Monroe/Cox misattribution) in between.

Every citation below was checked against a primary source directly (a publisher DOI
page, an author's own CV, or a citing paper's own reference list) rather than accepted
because it was already in the file — consistent with academic integrity being the
standing #1 priority on this project.

Most citations in the AI-thematic-analysis methodology section (Xu 2026, Naeem et al.
2025, AlGhamdi 2026, Hill et al. 2026, Goyanes et al. 2025, Misra et al. 2026) were
**not re-derived from scratch** — they're already independently verified, several
"read in full," in `Claude_Knowledge/AI_Thematic_Analysis_Reading_List.csv`. This pass
cross-checked the manuscript's citations against that existing verification and closed
two small gaps it had (Goyanes page range, Misra author list) rather than re-verifying
from zero.

## Results

| Citation | Verdict | Detail |
|---|---|---|
| Campbell, M. C. (2007) | **RESOLVED (bibliographic) / still open (item wording)** | Real title recovered from Campbell's own UCR faculty CV: "Says who?!: How the source of price information and the direction of price change influence perceptions of price fairness," *Journal of Marketing Research*, 44(2), 261–271. Multiple secondary sources (search engines, and Friesen 2020's own reference list) give a *different* subtitle — "...and Affect Influence Perceived Price (Un)fairness" — for what is almost certainly the same paper (identical journal/volume/issue/pages across every source checked). Treated the CV as authoritative since it's the author's own document. **Not resolved**: the specific scale items this project attributes to the paper (a "bad"/"good" motive rating, a "took advantage of you" agreement item) — no source checked this pass confirmed that exact wording. Pull the actual article text before submission if those items are load-bearing as written. |
| Goyanes, Lopezosa, & Jordá (2025) | **RESOLVED** | *Quality & Quantity*, 59(6), 5491–5510. Manuscript had 5493 as the start page — off by 2, now corrected. |
| Misra et al. (2026) | **RESOLVED** | Full author list — Misra, R., Dahal, R., Kirk, B., Khan, R., Dogan, G., Chataut, R., & Gyawali, P. — was already on record in the project's own reading-list CSV, just not carried into this manuscript's reference list. Not independently re-verified against the paper itself this pass. |
| Kahneman & Tversky (1979) | **CONFIRMED** | *Econometrica*, 47(2), 263–291. Exact match (Econometric Society + RePEc/IDEAS). |
| Tversky & Kahneman (1981) | **CONFIRMED** | *Science*, 211(4481), 453–458. Exact match (Science/AAAS DOI record). |
| Chaudhuri & Holbrook (2001) | **CONFIRMED** | *Journal of Marketing*, 65(2), 81–93. Exact match (SAGE DOI jmkg.65.2.81.18255). |
| Braun & Clarke (2006, 2019) | Not re-verified this pass | Canonical, extremely low fabrication risk, confirmed real in the 2026-07-08 pass; still worth one final spot-check before submission per the file's own long-standing flag. |
| Brehm (1966) | Not re-verified this pass | Same as above — foundational book citation, confirmed real 2026-07-08, publisher detail not independently re-checked since. |
| Xu (2026), Naeem, Smith & Thomas (2025), AlGhamdi (2026), Hill et al. (2026) | Cross-checked, not re-derived | Already independently verified (several read in full) in `Claude_Knowledge/AI_Thematic_Analysis_Reading_List.csv`; the specific claims attributed to them in the Methods draft (e.g., Hill et al.'s 93.5%/Gwet's AC1=.93, AlGhamdi's hierarchical-convergence finding) match that existing verification. |
| Dodds, Monroe, & Grewal (1991) / Grewal et al. (1998) | Unchanged | Already tracked as an open item in `SUBMISSION_TRACKER.md` — the Measures section uses the Grewal et al. (1998) secondary-source wording, not the 1991 original, pending Britton's pull of the actual 1991 appendix. Not touched this pass — this is a known, already-flagged gap, not a new finding. |

## Fabrication watch

No new fabricated citations found this pass. One genuine, if minor, factual error
caught and fixed (Goyanes et al.'s start page, 5493 vs. the real 5491) — small, but
exactly the kind of thing a careless final check would let through.

## What's still open

- Campbell (2007)'s exact scale-item wording — the one real remaining gap from this
  pass. If library/database access is handy, worth pulling the full JMR article before
  the item text goes into a submitted manuscript as a direct quote.
- Braun & Clarke (2006, 2019) and Brehm (1966) — low-risk, but not independently
  re-verified this specific pass; still on the "final spot-check before submission"
  list, unchanged from before.
- Everything else flagged as open elsewhere in this project (IRB status, CITI module,
  H3 direction, Purchase Intention item count, grad assistant worksheet) is untouched —
  out of scope for a citation-accuracy pass.
