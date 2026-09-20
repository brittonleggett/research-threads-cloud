# 2026-09-20 — Study 2 draft documents synced to 4-arm design; new-moderator citations verified

**Disclosure:** This note and the edits below were produced autonomously by an AI system (Claude)
under this project's 2026-08-16 Phase 3/build-out exception
(`notes/2026-08-16-phase3-theme-review-and-theory-lock.md`), not by Britton directly. No locked
theme, hypothesis, mediator, moderator, or the primary theory chain (H1-H6) was touched. None of
the three items reserved for Britton regardless of the exception (archival-moderator feasibility,
PLS-SEM vs. Hayes-PROCESS, and — as of tonight — the now-resolved single-manipulation-vs.-factorial
call, which Britton himself already resolved on 2026-09-08, not decided by this session) were
newly decided here; this session only propagated a decision Britton already made into the documents
that hadn't caught up with it yet.

## Why this task, not the jurisdiction-tracking thread

Per the 2026-09-18 note's explicit flag, this session started by finding the actual next-flagged
step in the literature-verification/scale-sourcing/Study-1-2-draft thread, not the jurisdiction
thread. The most recent note in that thread was `notes/2026-09-08-four-arm-vignette-draft.md`,
whose "still open" item #6 stated plainly: *"Sync this file and the underlying instrument draft to
`research-threads-cloud/`... not yet done for this file's latest edits (only the pre-power-analysis
version was mirrored)."* Checking `Study2_Instrument_DRAFT_2026-08-27.md` and
`Study2_Methods_Section_DRAFT_2026-08-29.md` in this repo confirmed the gap was real: both
documents still described the **original 2-condition disclosure manipulation**, with no trace of
the 4-arm design, the new baseline-trust-in-police moderator, or the 2026-09-08 power analysis.
This was the concrete, already-flagged next step — not a new direction invented tonight.

## What was done

**1. Synced `Study2_Instrument_DRAFT_2026-08-27.md`** to the 4-arm design:
- Section 3 (random assignment): 2-condition → 4-level single-factor equal-probability design.
- Section 4 (vignette text): replaced with the v2, Flesch-Kincaid-checked wording for all four
  conditions (neutral, safety-benefit, broad-network-access, disparate-impact), including the two
  explicit design decisions Britton made 2026-09-08 (dropping ICE-specific wording; "minority and
  lower-income neighborhoods" phrasing) and the still-undrafted exploratory race-composition item.
  Original 2-condition text retained below, clearly marked superseded, for reference.
- Section 5 (manipulation checks): replaced the 2-condition forced-choice item with the new shared
  4-option cross-contamination-check item from the 09-08 note.
- Added a new Section 2b for the baseline-trust-in-police pre-exposure moderator (measured before
  randomization, per the 09-08 design decision) — item wording is explicitly flagged as **not yet
  drafted**, not invented here.
- Rewrote the "what's still needed" list to reflect current status (resolved vs. still-open design
  calls, what's piloted vs. not).

**2. Synced `Study2_Methods_Section_DRAFT_2026-08-29.md`** to match: Design Overview, Participants
(CloudResearch main sample / convenience-sample pilot, replacing the Prolific-only plan), the full
Monte Carlo power-analysis writeup (replacing the old N=500-800 placeholder with the three
test-specific power profiles and the oversampling design for the baseline-trust interaction),
Procedure, Measures, Manipulation/Confound Checks, Pilot Testing, Limitations, and the closing
"still needed" list.

**3. Verified, via Crossref (not WebSearch-only), the citations the 09-08 session introduced for
the new moderator and power-analysis method — none of which had been through this project's own
citation-verification standard yet:**

- **Merola, Lum, & Murphy (2018)** — real, DOI `10.1007/s11292-018-9332-8`, "The impact of license
  plate recognition technology (LPR) on trust in law enforcement: a survey-experiment," *Journal of
  Experimental Criminology*, 15(1), 55–66. Published online 2018-06-02, print issue March 2019 — the
  "(2018)" year in project notes follows the online-first date, consistent with this project's
  established convention (e.g. Schiff et al. 2025). Confirmed via a direct Crossref query and a
  full-record fetch by DOI. Note: the specific "80.79% baseline trust" and "d=.33" figures
  attributed to this paper in the 09-08 note were **not** independently re-verified against the
  article's full text tonight (Springer full-text was not attempted) — flagged as carried over, not
  freshly confirmed, in both synced documents.
- **Preacher, Rucker, MacCallum, & Nicewander (2005)** — real, DOI `10.1037/1082-989x.10.2.178`,
  "Use of the Extreme Groups Approach: A Critical Reexamination and New Recommendations,"
  *Psychological Methods*, 10(2), 178–192. Confirmed via Crossref.
- **McClelland & Judd (1993)** — real, DOI `10.1037/0033-2909.114.2.376`, "Statistical difficulties
  of detecting interactions and moderator effects," *Psychological Bulletin*, 114(2), 376–390.
  Confirmed via Crossref.
- **Pitts (1993)** — **could not be verified tonight.** No matching record found via Crossref
  bibliographic search, and Semantic Scholar/OpenAlex lookups were rate-limited before a result
  could be obtained (OpenAlex: "Insufficient budget," no API key used; Semantic Scholar: HTTP 429).
  This is very likely an unpublished dissertation cited secondhand within Preacher et al. (2005),
  which would explain the absence of a DOI record, but that is an inference, not a confirmation.
  Flagged plainly in both synced documents as unverified rather than treated as confirmed — a
  genuine open item for a future session (retry with an API key, or check Preacher et al.'s own
  reference list directly) rather than something resolved tonight.

## Light verification sweep (kept deliberately brief, per the task's priority order)

Two WebSearch queries only, to avoid crowding out the priority task above:
- **Schulte v. Flock Group Inc.** (federal class action, N.D. Georgia) surfaced prominently in
  current coverage — already in the corpus as item #38, verified in
  `notes/2026-09-08-verification-sweep-and-corpus-expansion.md`. No new information found tonight
  beyond what's already captured.
- A broader municipal-rejection-wave search turned up continuing activity (Lynchburg VA council
  vote to end its contract, Foster RI cancellation, Woonsocket RI council rejecting a proposed ban
  5-1, a Newsweek tracker citing 23 states) but nothing independently confirmed tonight beyond
  headline-level WebSearch summaries — **not directly fetched or added to the corpus**, consistent
  with this project's standing rule that WebSearch-only findings don't get cited without a direct
  fetch. If Britton wants any of these pursued, that's a concrete task for a future jurisdiction-
  focused session, not done here to avoid the exact crowding-out problem the 09-18 note flagged.

## What's still open

1. Baseline-trust-in-police screener item wording — not yet drafted (flagged, not invented).
2. Human pilot of the 4-arm vignette and all scale items — still not run, still the single
   highest-priority step before fielding anything.
3. Pitts (1993) citation — unverified tonight, needs a retry with API keys or a direct check of
   Preacher et al. (2005)'s reference list.
4. The Merola, Lum & Murphy (2018) 80.79%/d=.33 figures — not re-verified against full text.
5. Archival vs. self-report (Moderator 1) and PLS-SEM vs. Hayes-PROCESS — both still Britton's call,
   unchanged.
6. IRB submission for the pilot and CloudResearch main study — still not started (Britton's
   2026-09-08 call to defer).
7. Any further Flock/ALPR jurisdiction or litigation sweep beyond the brief check above — deliberately
   left light tonight; a dedicated jurisdiction-sweep session can pick this back up without
   conflicting with tonight's priority work.

## Files touched

- `Study2_Instrument_DRAFT_2026-08-27.md` — synced to 4-arm design (Sections 2b, 3, 4, 5; "still
  needed" list).
- `Study2_Methods_Section_DRAFT_2026-08-29.md` — synced to 4-arm design (Design Overview,
  Participants, Procedure, Measures, Manipulation/Confound Checks, Pilot Testing, Limitations,
  closing list).
- This note (new).

## Sources used

Crossref REST API (`api.crossref.org`), attempted OpenAlex and Semantic Scholar APIs (both
rate-limited, see above), plus two WebSearch queries for the light sweep.
