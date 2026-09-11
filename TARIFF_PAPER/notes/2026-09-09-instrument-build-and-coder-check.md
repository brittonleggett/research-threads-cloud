# 2026-09-09 — Study 2 instrument build + coder-status check

**Task:** while Tariff Paper is blocked on HSIRB turnaround, (1) assemble the
fully-specified Study 2 content from `2026-08-04-full-instrument-assembly.md`
into a build-ready Qualtrics spec, and (2) check Holden/Jason validation-pilot
coding completion status. No design decisions made — H3 direction and any
other design-lock question left untouched, per standing rule.

## 1. Qualtrics instrument spec
Built: `TARIFF_PAPER/Study2_Qualtrics_Instrument_READY_2026-09-09.md` — full
block-by-block flow (Consent → Screener → Randomizer/Vignette → Manipulation
Checks → Fairness → Opportunism → Trust → Purchase Intention → WOM →
Demographics → Debriefing), exact item wording, response scales, skip/branch
logic, and embedded-data fields to capture condition assignment. Two small
items flagged for Britton's confirm-or-override (not decided here): whether
to flip the Opportunism item 2 anchors (it's the one item in the instrument
running backward from the rest) vs. reverse-score in analysis, and whether
attention-check failure should flag-only or hard-terminate. Everything else
in the assembly note was already locked as of 2026-09-07 and is just
formatted into build order here. No live Qualtrics build attempted — judged
higher-risk to attempt multi-step Qualtrics UI automation unsupervised than
to hand over a complete, unambiguous spec; someone with Qualtrics access can
build the live survey from the spec in well under an hour.

## 2. Coder status
- **Holden: confirmed complete.** `Study_1_Pilot_Coding-Holden.docx` has all
  15 artifacts filled in with real inductive codes (spot-checked several —
  e.g. Artifact 1/Nike: "[External Impact] [Precise Financials] [Limited
  Impact] [Production Relocation] [Operational Change] [China]"). Matches
  the 2026-09-08 memory note that Holden was done.
- **Jason: no worksheet file found at all.** Searched the entire
  `TARIFF_PAPER` folder recursively for anything Jason-named — nothing
  exists. Either he hasn't started, or his copy lives somewhere outside this
  folder (e.g., emailed directly, a separate Google Doc, his own machine).
  Did not compute or attempt Gwet's AC1 — there's nothing to compare Holden's
  codes against yet.

## What's still open
- Jason's coding status needs a direct check with Britton (or Jason) — not
  resolvable from the files in this folder.
- The two flagged instrument items above need his call before fielding.
- Live Qualtrics build itself still needs someone with account access.
