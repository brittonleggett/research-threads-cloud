# Research Threads — Cloud Working Copy

This repo is a **mirror** of six local project folders, pushed here specifically so
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
- **`DATA_CENTER_PAPER/`** — public opposition to data center construction. Started
  Louisiana-only (Meta "Hyperion"/Richland Parish, Amazon/Caddo Parish, New Orleans
  East), corpus now at 17 artifacts and primary-source verified. **2026-08-16 scope
  pivot: now deliberately national**, not Louisiana-only — Britton wants
  generalizability, not single-state positioning. A national scan (GA, UT, VA, AZ,
  IN/OH, MS/TN, NY + other moratorium states) is in `notes/2026-08-16-national-scan-beyond-louisiana.md`;
  restructuring the corpus/design around that (region/community-profile as an
  explicit moderator is the current recommendation) is still Britton's open call —
  don't do it without him. Venue: Journal of Public Policy & Marketing leading
  candidate, alongside Journal of Business Ethics/Business & Society/ERSS.
- **`CCS_PAPER/`** — carbon capture/CCS paper, same Study1→Study2 AI-thematic-
  analysis template as the others. Less actively worked recently than Tariff.
- **`FLOCK_CAMERAS_PAPER/`** — newest, added 2026-08-16. Public opposition to Flock
  Safety's ALPR (license-plate-reader) camera networks — ICE/federal data-access
  fights, racial-disparity-in-placement findings, wrongful-stop harms, and a large
  municipal rejection wave. **Venue is public policy, not marketing** (Britton's
  explicit call — the central actors are government bodies, not a company
  marketing to consumers) — think Government Information Quarterly (best-supported
  candidate so far) or Public Administration Review, not JPP&M. **Important: for
  this paper only, Britton granted an explicit one-time exception letting AI run
  Phase 3 (theme review) and lock the primary theory chain** — see
  `notes/2026-08-16-phase3-theme-review-and-theory-lock.md` before touching this
  project's themes/design; don't assume this exception extends to Tariff/Data
  Center/CCS, their Phase 3 stays human-only as normal. A full autonomous build-out
  (literature grounding, verified scales, Study 1/2 drafts) was in progress as of
  2026-08-16 — check `notes/` for the newest dated file before starting new work
  here, so nightly runs build on that rather than duplicating it.
- **`SPACEX_LOUISIANA_PAPER/`** — newest, added 2026-08-27, same day as the real-world
  announcement (SpaceX's $100B Starship spaceport, Vermilion Parish). Economic-benefit
  claim-specificity framing and environmental-commitment/greenwashing framing vs. an
  active FAA regulatory-review-waiver fight, with SpaceX's existing Starbase (Boca
  Chica, TX, operating since 2021) as a built-in comparison case. Britton's explicit
  call: distinct enough from `DATA_CENTER_PAPER` to be its own paper, not a fifth
  anchor case folded into that one — different industry (aerospace vs. data centers),
  different regulator (FAA vs. state utility commissions). Exploratory stage, no
  design-lock yet — see `CLAUDE.md` and `notes/2026-08-27-orientation.md`. **No Phase 3
  exception for this paper** (only `FLOCK_CAMERAS_PAPER` has one) — theme/design-lock
  calls stay Britton's.
- **`Claude_Knowledge/`** — shared methodology, used by all four papers above:
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
- **Thematic-analysis "Phase 3" (theme review) is always human-only, never AI-run —
  except `FLOCK_CAMERAS_PAPER`, where Britton granted an explicit one-time
  exception on 2026-08-16** (see that project's `notes/` for the reasoning and the
  locked chain). Don't extend that exception to Tariff/Data Center/CCS on your own
  judgment — their Phase 3 stays human-only, propose/refine candidates only, same
  as always.
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
- **No copyrighted, non-open-access full-text belongs in this repo — it's public.** Citations,
  abstracts, short quotes for commentary/analysis, and full text of genuinely open-access/CC-BY
  articles are all fine. A downloaded PDF of a paywalled journal article, or an extensive
  verbatim transcription of one, is not — that stays in the local project folders only (outside
  git) and never gets mirrored here. Caught and fixed once already (2026-08-16): a Sage
  journal-article PDF and a long paywalled-article excerpt file almost got committed to this
  public repo before being pulled back out — check before adding any literature file.
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
   one"; (2) `DATA_CENTER_PAPER`; (3) `CCS_PAPER`; (4) `FLOCK_CAMERAS_PAPER` — added
   2026-08-16; (5) `SPACEX_LOUISIANA_PAPER` — added 2026-08-27, same priority tier as
   Data Center/CCS/Flock (not above Tariff). Rotate toward whichever has the most
   open, actionable next-steps in its notes rather than mechanically going in order
   every night — recheck each project's actual state, since prior nights change
   what's "next." For `FLOCK_CAMERAS_PAPER` specifically, remember its Phase 3
   exception above — you can extend/build on its already-locked theory chain and
   finish the autonomous build-out (literature, scales, drafts) without waiting on
   Britton, unlike the other four projects. For `SPACEX_LOUISIANA_PAPER`
   specifically, it has no design-lock yet — useful early-run work is corpus-
   gathering (primary-source verification of the facts in `notes/2026-08-27-
   orientation.md`, expanding the Boca Chica comparison corpus) and literature-gap
   scouting, not picking its Study 1 option (A/B/C) or theory chain — that's
   Britton's call, same as Data Center/CCS/Tariff.
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
