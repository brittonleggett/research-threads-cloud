# 2026-08-21 — Overnight session summary

Orientation: read `README.md`, `CLAUDE.md`, `2026-08-16-phase3-theme-review-and-theory-lock.md`,
and the two most recent notes (`2026-08-20-face-validity-review-scale-items.md`,
`2026-08-19-instrument-adaptation-and-manipulation-checks.md`) before starting, plus skimmed the
three top-level drafts and the Tariff Paper IRB materials for format precedent, per the task
brief. Confirmed the two Britton-gated items (archival distributive-surveillance-exposure
moderator feasibility; single-manipulation-vs-factorial and PLS-SEM-vs-PROCESS) remain untouched.

## What got done tonight (three new dated files, plus this summary)

1. **`2026-08-21-irb-application-draft.md`** — first full-content draft of the MSU HSIRB
   application package for this paper (closes the "no IRB draft exists" gap flagged in every note
   since 2026-08-19). Modeled structurally on Tariff Paper's own IRB draft for section-numbering
   consistency, but every substantive claim is fresh and Flock-specific. Covers a Pretest phase
   and Study 2, excludes Study 1 (public-document analysis) from human-subjects review. Explicitly
   presents **both** candidate paths for Moderator 1 (archival vs. self-report) rather than
   picking one, since that's still Britton's call. Includes a draft debriefing statement, an
   AI-use disclosure paragraph, and a risk/benefit section that names — more plainly than Tariff's
   package needed to — that this topic (policing, surveillance, immigration enforcement) is more
   likely to touch personally salient material for some respondents than a corporate-pricing
   vignette would. Sample sizes (Pretest N=150-200, Study 2 N=500-800) are explicit placeholders,
   not power-analyzed. **Not reviewed by Britton, not submission-ready, never submitted or shared
   anywhere.**

2. **`2026-08-21-literature-verification-pass.md`** — WebSearch pass (WebFetch confirmed
   egress-blocked again, 10th straight session) checking the theory-chain citations in the
   Introduction/Theory draft that hadn't already gone through the stronger Ole Miss library
   verification the four scale-source papers got. **Result: seven citations confirmed real**
   (Sunshine & Tyler 2003, Nissenbaum 2010, Tyler 1990, Tyler & Huo 2002, Reisig & Lloyd 2009,
   Bradford et al. 2020, Li 2024, Nhan & Helfers 2026 — author/year/journal all check out).
   **One real problem found and flagged, not fixed silently:** the draft's specific claim that
   Nhan & Helfers's (2026) Flock-funded study had "contractually stipulated researcher
   independence" could not be verified — and search results surfaced real reporting (Techdirt,
   2024) that the same two authors' *earlier* Flock-funded work involved Flock steering which
   departments to interview and researcher pressure toward favorable results. This doesn't prove
   the 2026 study lacks independence, but it means that specific clause in the draft is an
   unverified assertion, not a confirmed fact — flagged for Britton to soften, verify via direct
   fetch, or cut before this goes further. Did not edit the Introduction draft itself, per the
   "new files over overwrites" convention.

3. **`2026-08-21-corpus-addendum-new-evidence.md`** — firmed up two previously
   "WebSearch-confidence only, not re-verified" corpus artifacts (#20 El Cerrito, #21 Appleton)
   with multi-source corroboration, and identified **three strong new candidate corpus artifacts**:
   a Menasha, WI officer convicted (6 months, named, adjudicated) for using Flock to stalk his
   ex-girlfriend; two separate Milwaukee, WI officers criminally charged for similar misuse; and a
   Mountain View, CA case documenting both federal *and* state-level unauthorized access to camera
   data. **This materially changes the evidentiary basis for one Phase-3 judgment call**: Theme 3
   (function creep/individual misuse) was demoted to "reported finding, not primary design" on
   2026-08-16 specifically because it rested on only two thin, single-source artifacts — it no
   longer does. Flagged plainly for Britton's gut-check rather than silently re-opening the
   already-completed, one-time-exception Phase 3 decision myself.

## What wasn't done / explicitly out of scope tonight

- **No piloting was run** — that's human-subjects data collection only Britton can do.
- **The two Britton-gated design questions** (archival-moderator feasibility; factorial/PLS-SEM
  calls) — untouched, as instructed.
- **No participant/survey data added to this repo** — consistent with the standing
  no-human-subjects-data rule; the IRB draft describes a design, it doesn't contain any real
  respondent data.
- **Did not attempt to build a `.docx` version of the IRB package** (Tariff Paper has a
  `build_irb_docx.py` script for that) — the markdown content draft is the deliverable tonight;
  converting to a formatted document is a reasonable next step but wasn't requested and would be
  premature before Britton's first read-through.

## Open items for Britton, collected in one place

1. Read and revise/finish the IRB draft — nothing in it is final, several placeholders need his
   input (CITI number, Path A/B decision, real sample-size targets, timeline).
2. Verify or soften the Nhan & Helfers "contractually stipulated researcher independence" claim in
   the Introduction draft before it goes further.
3. Gut-check whether the new Menasha/Milwaukee/Mountain View evidence changes his view on whether
   Theme 3 (function creep) should be promoted into the primary Study 2 design — not decided here.
4. Everything already open from prior notes remains open and untouched (archival-moderator
   feasibility, factorial-vs-single-manipulation, PLS-SEM-vs-PROCESS, actual instrument piloting).

No files outside `FLOCK_CAMERAS_PAPER/notes/` were modified. No existing draft or note file was
overwritten. Git commit/push is the parent session's responsibility per the task instructions, not
done here.
