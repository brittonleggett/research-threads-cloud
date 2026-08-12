# Research Threads — Cloud Working Copy

This repo is a **mirror** of four local project folders, pushed here specifically so
a scheduled cloud agent can work on them overnight (the local versions live outside
git, on Britton's machine, and aren't reachable by a cloud agent). It contains no
personal/sensitive material — deliberately scoped to just these research threads.

## Contents

- **`TARIFF_PAPER/`** — first-authored paper, target *Journal of Consumer Marketing*
  special issue (AMS 2026 conference track, deadline ~Oct 15 2026). Currently the
  top-priority paper in the pipeline. See `CLAUDE.md` and `notes/` (most recent
  dated file = current status). Study 1 (AI-assisted thematic analysis of corporate
  tariff-messaging) has a corpus and a manuscript-ready draft methods section
  already; validation pilot and full Phase 3 theme review still outstanding.
- **`DATA_CENTER_PAPER/`** — newer, exploratory. Public opposition to Louisiana data
  center projects (Meta "Hyperion"/Richland Parish, New Orleans East). Not tied to
  JCM — venue TBD, Journal of Public Policy & Marketing is the current leading
  candidate. Study 1 corpus (public discourse, 11 artifacts) built 2026-08-12.
- **`CCS_PAPER/`** — carbon capture/CCS paper, same Study1→Study2 AI-thematic-
  analysis template as the other two. Less actively worked recently than Tariff.
- **`Claude_Knowledge/`** — shared methodology, used by all three papers above:
  - `Thematic Analysis/AI_Assisted_TA_Shared_Method.md` and
    `Study1_AI_Thematic_Analysis_Publishable_Protocol.md` — the six-phase
    AI-assisted thematic analysis workflow, reporting standards, and citation stack.
  - `AI Research Workflows/PLS-SEM Standards Checklist.md` — reliability/validity
    thresholds for any PLS-SEM work (Study 2/3 across these papers).
  - `AI Research Workflows/Response to Reviewers Letter.md` — R&R letter structure.

## Working conventions (apply across all four folders)

- **Work in small, reviewable steps.** Prefer creating new, clearly-dated files for
  drafts/findings over overwriting existing ones — matches the convention already
  established in `TARIFF_PAPER/CLAUDE.md`.
- **Never fabricate citations, statistics, or quotes.** If something can't be
  verified, say so explicitly rather than smoothing it over — see
  `TARIFF_PAPER/OVERNIGHT_SUMMARY.txt` for the tone/rigor level expected (a prior
  overnight citation-verification pass; it names real errors it found, doesn't
  paper over uncertainty).
- **Thematic-analysis "Phase 3" (theme review) is always human-only, never AI-run.**
  This rule is already established across all three papers' Study 1 work — don't
  finalize themes, only propose/refine candidates for Britton's review.
- **Disclose AI involvement** in any methods-section language drafted.
- **Leave a summary.** At the end of any work session on this repo, write or update
  a top-level `OVERNIGHT_SUMMARY_<date>.md` at the repo root (not per-folder)
  describing what was done, what was found, and what's still open — written for
  Britton to read first thing, in plain, direct prose (state uncertain/negative
  findings plainly, don't spin them).

## Who Britton is (for context, not to be repeated back to him)

Marketing professor at McNeese State University. PLS-SEM is his default empirical
toolkit. Recurring theoretical pattern across his work: mediated antecedent →
psychological mediator → outcome chains, often with a moderator. Values getting
published in venues that matter to him and to Louisiana specifically, and is
building a public expert-positioning angle around the Data Center paper in
particular. Not deeply tooling-fluent — write findings in plain, direct language.
