# Local ↔ Mirror Reconciliation — Tariff Paper (2026-09-11 overnight)

Known recurring failure mode (see memory topic `project_autonomous_research_infrastructure`):
the local `TARIFF_PAPER/` folder (worked from in interactive sessions) and the
`research-threads-cloud/TARIFF_PAPER/` git mirror (worked from by the nightly cloud
routine) had drifted apart again. Reconciled tonight, file by file. **No factual
contradictions found** — every difference was one side having newer/more-complete
content the other lacked, not two sides asserting different facts about the same thing.

## Pure additions (copied, no merge needed)
- Repo → local: `notes/2026-09-10-blocker-briefing-for-britton.md`,
  `notes/2026-09-10-citation-accuracy-pass.md`,
  `notes/2026-09-10-h3-reversal-literature-check.md`,
  `notes/2026-09-10-litigation-recheck-section301-government-response-was-filed-on-time-not-actually-overdue.md`.
- Local → repo: `notes/2026-09-08-choi-chan-fock-2025-reverified.md`,
  `notes/2026-09-09-instrument-build-and-coder-check.md`,
  `notes/2026-09-11-primary-source-corrections-pass.md` (tonight's Insteel-quote fix),
  `GA_Braun_Clarke_Coding_Instructions_2026-08-30.md`, `Literature/` folder,
  `Study1_Consumer_Facing_Supplementary/` folder,
  `Study1_Validation_Pilot_AI_CODES_SEALED_2026-08-13.md`,
  `Study2_Qualtrics_Instrument_READY_2026-09-09.md`, `Study_1_Pilot_Coding-Holden.docx`,
  `Tariff_Data_Collection_Instruments_2026-09-08.docx`, `notes/build_data_collection_instruments.py`.
- Deliberately NOT mirrored: `JPMorgan_EP_Proposal/` (a separate tracked project that
  happens to live inside this local folder), `Overnight_Work_Summary_2026-07-09.docx`
  (unrelated general file), any `.bak.docx` backups, `__pycache__`.

## Real merges (both sides had unique newer content in the same file)
- **`Study1_Corpus_and_Coding_DRAFT_2026-08-21.md`** — local had tonight's Insteel
  freight-vs-profit correction, repo didn't. Local was a strict superset; copied
  local → repo.
- **`SUBMISSION_TRACKER.md`** — local had the 2026-09-08/09 status layer (IRB
  submitted, Study 3 cut, Holden+Jason coders, the live CITI-conflict flag) that repo's
  stale 2026-09-04 copy never received; repo had two 2026-09-10 bullets (Section 301
  litigation-recheck resolved, CITI re-confirmation) local never received. Merged:
  took local as the base and inserted the two repo-only 2026-09-10 bullets into the
  Deadline section in date order. Reconciled version written to both locations.
- **`Introduction_and_Theory_DRAFT_2026-08-12.md`** — repo had Britton's confirmed
  2026-09-10 H3 reversal (compensatory/cue-substitution direction, grounded in Kelley
  1972 + signaling theory); local still had the old open/unresolved H3 placeholder.
  Repo was the strict superset here; copied repo → local. **The substantive H3 decision
  itself was not touched or second-guessed — only synced.**
- **`Tariff_Manuscript_Working_Draft_2026-09-04.md`** — same H3 resolution plus a
  2026-09-10 citation-accuracy pass (Campbell 2007, Connelly et al. 2011, Kelley 1972,
  Kirmani & Rao 2000, and re-verification of 4 existing references) existed only in
  the repo copy. Repo was the strict superset; copied repo → local.
- **`notes/2026-08-04-full-instrument-assembly.md`** — local had the 2026-09-07
  upgrade to the real Dodds, Monroe & Grewal (1991) appendix (superseding the Grewal
  et al. 1998 proxy wording), repo still had the older proxy-only version. Local was
  the strict superset; copied local → repo.

## How to apply
Both trees are now identical (content-wise; a few intentionally-excluded files/folders
listed above aside). No judgment calls were made on any substantive research question —
this was purely a "which copy has the more complete version of the same fact" exercise,
and in every case one side was simply behind, not actually disagreeing. If this drift
recurs, the same file-by-file diff approach worked cleanly and is worth repeating rather
than trusting either copy as automatically authoritative.
