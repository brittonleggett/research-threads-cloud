# Decision Log

Dated record of research/scope decisions and the reasoning behind them.
Newest entries at the top.

---

## 2026-09-03 — First research session used five parallel forked research
passes rather than one long sequential pass
**Decision:** Split Sections 3/5 (concentration & structure), 6 (imports), 7
(COOL timeline), 8 (price transmission), and 9 (theory candidates) across
five parallel background research agents, each with a scoped file-write
mandate and instructions not to touch git. Orchestrator (this session)
handled scaffolding, Study 1-3 planning docs, journal/marketing-contribution
options, and the final consolidation (`NOTES/Claim_Fact_Check.md`,
`SOURCE_VERIFICATION/Evidence_Table.md`, `PROJECT_STATUS.md`) after all five
returned.
**Why:** The brief's evidence-collection scope (Sections 4-13) is large and
the sub-questions are genuinely independent (import data doesn't depend on
COOL regulatory history, etc.), making this a good fit for parallelization.
Each pass self-reported its verification gaps and unresolved items honestly
(several claims — #1, #5, #7 — landed as Unresolved rather than being forced
to a verdict) rather than smoothing over what couldn't be verified this
session.
**What this means for future sessions:** Several primary sources were
blocked by bot-detection or paywalls across multiple independent passes
(Federal Register, FSIS, GAO PDFs, ScienceDirect, MDPI, a Springer
paywall) — this looks like an environment/tooling limitation (no PDF
renderer, WebFetch getting bot-blocked on several government/publisher
domains) rather than these sources being genuinely unavailable. A session
with library-proxy access or better PDF tooling should prioritize the
follow-up list in `PROJECT_STATUS.md` before doing new research passes.
**Reversible:** N/A — describes how the work was done, not a lock-in
decision.

## 2026-09-03 — Project initiated; built in `research-threads-cloud`, not a
loose Desktop folder
**Decision:** Created `MEAT_SUPPLY_CHAIN_PAPER/` inside
`Desktop\Claude Global\research-threads-cloud\` (the git-tracked, actively
synced repo — confirmed current via `git log`/`git status`, last commit
2026-09-03), not inside the loose `Desktop\Claude Global\` folder used for
some earlier project copies (confirmed stale, e.g. the loose
`FLOCK_CAMERAS_PAPER` copy's newest file is dated 2026-08-30 vs. 2026-09-03
in the repo copy).
**Why:** The brief required confirming we're working from the current
repository version. `research-threads-cloud` is the one the nightly
autonomous research routines push to and the one with working-tree parity to
`origin/main`.
**Reversible:** N/A — this is the intended long-term location for the
project.

## 2026-09-03 — Full rigorous scaffold adopted instead of the existing
projects' flatter layout
**Decision:** Built the more elaborate structure this brief specified
(`README.md`, `PROJECT_STATUS.md`, `RESEARCH_QUESTIONS.md`,
`THEORY_CANDIDATES.md`, `LITERATURE/`, `CORPUS/`, `DATA/`, `NOTES/`,
`ANALYSIS/`, `MANUSCRIPT/`, `STUDY1/`, `STUDY2/`, `STUDY3/`,
`SOURCE_VERIFICATION/`, `DECISION_LOG.md`) rather than copying
TARIFF_PAPER/CCS_PAPER/DATA_CENTER_PAPER's flatter, more ad hoc layout
(root-level dated draft files + a single `notes/` folder).
**Why:** Those earlier projects' structure evolved organically; this brief
explicitly asked for the more disciplined scaffold up front, given the
larger and more contested evidence base this topic requires (concentration
measures, import statistics, COOL regulatory history, price-transmission
literature — much more primary-source-heavy than, e.g., FLOCK_CAMERAS_PAPER).
Kept the useful conventions from the other projects: a per-project
`CLAUDE.md` brief, and dated research-pass logs inside `NOTES/` (mirroring
their `notes/` folders).
**Reversible:** Yes — folders can be flattened later if they prove to be
overhead rather than help.
