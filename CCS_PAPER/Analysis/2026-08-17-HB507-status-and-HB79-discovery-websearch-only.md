# HB507 status check + HB79 discovery (WebSearch-only)

**Tooling note:** WebSearch worked tonight (unlike the last 5 sessions) but WebFetch is still
`EGRESS_BLOCKED` on every domain tested (including a non-Louisiana one, `en.wikipedia.org`, to
rule out a Louisiana-specific block). So this is still a WebSearch-summarized pass, not a
primary-source read of the actual bill-status page — flagging per the repo's usual convention.

## HB507 (liability-cap repeal) — still not conclusively resolved

This was the one open thread flagged in `2026-08-16-corpus-supplement-fleshed-out-websearch-only.md`.
What search surfaced tonight:

- Introduced 2026-02-26, referred to House Civil Law and Procedure 2026-03-09 (legiscan showing
  "25% progression" as of that referral — this looks like a stale/cached snapshot, not a live
  read of current status).
- No search result confirms a committee vote, floor vote, or "died"/"failed" outcome specifically
  for HB507.
- The 2026 regular session adjourned **June 1, 2026** (fiscal-only session, consistent with
  Louisiana's even-year session pattern). Louisiana bills don't carry over between sessions, so
  if HB507 never got a floor vote, it's dead by sine die regardless of whether any outlet wrote
  an explicit "HB507 failed" story — quiet committee deaths usually don't get their own coverage.
- **Best inference, not confirmed:** HB507 most likely died in committee like HB5/6/7, given no
  evidence anywhere of it clearing committee or reaching the floor. But this is an inference from
  absence of coverage, not a direct primary-source confirmation — treat it as provisional until a
  working WebFetch pass can pull the actual bill-status page.

## New find: HB79 complicates the "all liability/property-rights bills died" narrative

Search surfaced a second liability-cap bill not previously in the CCS corpus or any prior note:

- **HB79** (Rep. Robby Carter, D-Greensburg) — also targets the carbon-capture liability cap.
  Per Livingston Parish News (businessreport.com corroborates), it **advanced without opposition
  from the House Civil Law and Procedure Committee in late April 2026** — i.e., it got further
  than HB507, HB5, HB6, or HB7 did.
- This matters for the 08-16 note's framing ("local-control and property-rights bills all died;
  an accountability/tracking measure [HB820] survived" as a clean signaling-theory pattern). A
  second liability-related bill clearing committee complicates that clean binary — worth Britton
  knowing before that framing gets written into a draft. Notably `CCS_PAPER/Corpus_1/` already
  has a `HB_79_Damages_Threshold.pdf` on file (from the original corpus build), so this bill was
  already known to the project — it just hadn't been cross-referenced against the 08-16
  legislative-sweep narrative until tonight.
- HB79's final floor outcome (post-committee) is also not confirmed by tonight's search — same
  caveat as HB507.

## Recommendation

Don't lock in the "property-rights bills uniformly died" framing until a working WebFetch/curl
pass can pull actual final-status pages for HB507, HB79, and the others. This is now the 6th
consecutive session with WebFetch blocked — the CCS legislative-sweep narrative specifically
needs primary-source bill-status confirmation before it goes into a manuscript, not just search
summaries.
