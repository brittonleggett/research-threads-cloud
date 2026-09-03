# Decision Log

Dated record of research/scope decisions and the reasoning behind them.
Newest entries at the top.

---

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
