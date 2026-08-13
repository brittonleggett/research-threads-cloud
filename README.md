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
- **Never submit, email, post, or otherwise externally share anything** — no
  contacting journals, editors, coauthors, IRB offices, or anyone else. Draft-only,
  always. Committing to this private repo is not "external" — that's the point of
  the repo — but nothing leaves it.
- **Always end by committing and pushing to `origin/main`**, even if the work is
  partial or you ran out of time partway through something. Uncommitted overnight
  work is invisible to Britton and to the next run. Small, clearly-labeled commits
  per logical chunk beat one giant commit.
- **No participant/human-subjects data belongs in this repo.** It's scoped to
  public-record corpora (corporate statements, news, filings, public comments) on
  purpose. If a task ever seems to call for adding survey data, IRB materials with
  real identifiers, or anything like that, stop and flag it in the summary instead —
  don't add it.

## Nightly rotation

A scheduled cloud routine runs this repo autonomously overnight with very little
per-run guidance from Britton — he wants steady, real progress on all of it without
having to hand-hold each session. Each run should:

1. **Orient first.** Read this README, then the most recent `OVERNIGHT_SUMMARY_*.md`
   files and each project's `notes/` folder (newest file = current status) to see
   what already happened and what's still open. Don't redo finished work.
2. **Work the priority queue**, spending real time on at least one item rather than
   shallow-touching all of them: (1) `TARIFF_PAPER` — top priority, "I need this
   one"; (2) `DATA_CENTER_PAPER`; (3) `CCS_PAPER`. Rotate toward whichever has the
   most open, actionable next-steps in its notes rather than mechanically going in
   order every night — recheck each project's actual state, since prior nights
   change what's "next."
3. **Spend some time scouting new research streams**, not just advancing the three
   existing papers. Use web search to look for near-term paper opportunities
   adjacent to Britton's existing lines (consumer/marketing behavior, tariffs,
   AI-augmented qualitative methods, Louisiana energy/infrastructure controversies).
   Write findings to `Claude_Knowledge/Research_Stream_Ideas.md` (append, dated
   entries, one running file rather than one-per-night) — each idea needs: the
   gap/question, why it's tractable soon, a rough method sketch, and a plausible
   target venue. This is scouting, not commitment — don't spin up a full corpus for
   a new idea unless it's clearly strong; flag it for Britton to greenlight instead.
4. **If blocked on a real judgment call** (something only Britton can decide, a
   citation needing his library access, ambiguous prior instructions), don't guess
   and don't stall the whole run on it — write it plainly as an open question in the
   summary and move to the next queued item.
5. **Commit and push** per the rule above before finishing.

## Who Britton is (for context, not to be repeated back to him)

Marketing professor at McNeese State University. PLS-SEM is his default empirical
toolkit. Recurring theoretical pattern across his work: mediated antecedent →
psychological mediator → outcome chains, often with a moderator. Values getting
published in venues that matter to him and to Louisiana specifically, and is
building a public expert-positioning angle around the Data Center paper in
particular. Not deeply tooling-fluent — write findings in plain, direct language.
