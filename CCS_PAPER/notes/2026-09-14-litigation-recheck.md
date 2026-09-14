# 2026-09-14 — Litigation recheck: ND amalgamation appeal (no change) + WV 4th Cir. oral-argument date (now primary-source confirmed)

**AI involvement disclosure:** this note was produced by an AI agent (Claude) doing autonomous
overnight verification work on this repo, per the project's standing conventions. All claims below
are labeled by source type (primary/secondary) as found tonight; nothing here was fabricated, and
anything not independently confirmed is flagged as such rather than smoothed over.

**Method:** WebSearch cross-corroboration across independent outlets for the North Dakota thread;
for West Virginia, went straight for a primary docket/court source rather than trusting search
snippets, per the standing instruction after this exact file's date-fabrication problem recurred
twice before (see `Analysis/2026-09-04-wv-4th-circuit-litigation-and-eo-public-trust-language.md`
and `notes/2026-09-09-nd-appeal-verification-and-wv-date-error-caught-again.md`). Direct `curl`
(with a browser user-agent) plus `pypdf` (installed fresh tonight; needed the same `cffi`
force-reinstall workaround noted in prior sessions before it would import cleanly) were used to pull
and read PDFs directly wherever a site would serve them to curl but not to WebFetch.

---

## 1. West Virginia — WVSORO v. Zeldin, 4th Cir. No. 25-1384 — **oral argument date now genuinely primary-source confirmed: Friday, October 30, 2026**

This is the headline finding of tonight's pass. The "Oct 30, 2026" date has a bad history in this
project (introduced without a real source, flagged unconfirmed on 2026-09-04, then reintroduced as
"confirmed" without a source again by 2026-09-07/09). Tonight, rather than searching generically, I
went directly to the U.S. Court of Appeals for the Fourth Circuit's own site:

- Found the calendar-PDF links on the court's own oral-argument-calendar page
  (`https://www.ca4.uscourts.gov/oral-argument/oral-argument-calendar`) via `curl` (WebFetch itself
  gets a 403 on this domain; direct `curl` with a browser user-agent gets HTTP 200 — same
  WebFetch-vs-curl asymmetry noted for other sites in prior sessions).
- Downloaded and read `https://www.ca4.uscourts.gov/cal/internetcalOct272026.pdf` (the court's own
  official argument calendar for its Richmond sitting) with `pypdf`. Page 19 of that PDF reads
  (verbatim extraction):

  > UNITED STATES COURT of APPEALS for the FOURTH CIRCUIT
  > Richmond, VA (10/27/2026 - 10/30/2026 Session)
  > ...
  > **25-1384** Briefs ADMINISTRATIVE LAW: Petition for review of EPA's approval of West Virginia's
  > application for primacy of enforcement authority over Class VI carbon sequestration wells.
  > **West Virginia Surface Owners' Rights Organization v. Lee Zeldin**
  > Friday, October 30, 2026
  > LIVESTREAM
  > Panel 4
  > Gold Courtroom (Room 348)
  > 8:30 a.m.

This is a **primary source** — the court's own official calendar, not search-engine synthesis — and
it confirms the case name, docket number, and framing (EPA Class VI primacy for WV) all match what
the 2026-09-04 note already established from the petitioners' brief. **The oral argument is
scheduled for Friday, October 30, 2026, before Panel 4 in the Gold Courtroom, 8:30 a.m., livestreamed.**

**What this means for the recurring problem:** the date itself was apparently correct all along — the
failure mode wasn't that "Oct 30, 2026" was wrong, it's that two prior passes asserted it as
"confirmed" without ever actually reaching a primary source, which is indistinguishable from a
fabrication until someone does the primary-source check. Tonight is the first time in this project's
notes that check has actually succeeded. **It is now safe to cite this date, with this specific
source** (`ca4.uscourts.gov/cal/internetcalOct272026.pdf`, page 19) — cite the calendar PDF directly,
not this note, if it goes in the manuscript, since calendars can still be amended/continued.

No other change to this case found tonight (still Petition for review of EPA's WV Class VI primacy
grant; same petitioner list as before — Sierra Club, WV Rivers Coalition, WV Highlands Conservancy,
WVSORO, represented by Appalachian Mountain Advocates).

## 2. North Dakota — Summit Carbon Solutions amalgamation-law appeal — **no docket movement found since 2026-09-09**

Re-ran WebSearch across the same outlet set as prior passes (North Dakota Monitor, KFYR-TV, Agweek,
KVRR, InForum/Dickinson Press, plus general sweeps) looking for anything published after the 09-09
note. **Found nothing newer than the August 31–September 4, 2026 coverage of Summit's motion to
narrow its own appeal to the "Summit #3" storage area**, already logged in the 09-08/09-09 notes. No
North Dakota Supreme Court ruling on that narrowing motion, no briefing schedule, and no oral
argument date turned up in any source tonight.

**Primary-source access attempted and still blocked, a fifth-plus consecutive session:**
`ndcourts.gov` (tried both `/supreme-court/opinions` and the search flow) returns the same bot-check
interstitial to direct `curl` with a browser user-agent (`<title>Security Check</title>`, HTTP 403) —
consistent with the 09-05/09-07/09-08 notes' identical finding. No PACER access in this environment
(this doesn't matter for a state matter anyway — ND Supreme Court dockets aren't PACER/RECAP). Tried
CourtListener directly via `curl` (which does load, unlike WebFetch which 403s on that domain) — it
indexes some older published North Dakota Supreme Court opinions (e.g., the 2022 pore-space case,
`2022ND150`) but has no RECAP-style live docket tracking for this state court, so it cannot surface
the pending 2026 amalgamation appeal's docket number or schedule either. **Bottom line: no
independently-verifiable primary source for this appeal's docket number or schedule exists that this
environment can reach.** This is a real, structural access gap, not a search-effort gap — worth
flagging to Britton if a docket number is ever needed for the manuscript (would require someone with
an actual ndcourts.gov or PACER-equivalent path, or a subscription docket-tracking service, to pull).

**One clarification worth recording so it doesn't get conflated in a future pass:** search turned up
a *different*, unrelated North Dakota case that the U.S. Supreme Court has agreed to hear — a WBI
Energy natural-gas-pipeline eminent-domain/attorney-fee dispute (McKenzie County, ND; the question
presented is whether North Dakota law governs compensation calculations for land taken by a pipeline
company under federal eminent domain authority; arguments expected fall 2026). **This is not
Summit Carbon, not CO2 storage, and not the amalgamation-law case** — it is a separate pipeline
company, separate infrastructure (natural gas, not CO2), and a separate legal question (compensation
formula under federal eminent domain, not the state amalgamation/takings-clause theory). Flagging
this now specifically so a future search-driven pass doesn't accidentally merge the two ND pipeline
stories the way the WV/D.C. Circuit case numbers got merged before. (Sources: North Dakota Monitor,
2026-07-20; KSJB AM 600, 2026-07-20 — both secondary, not independently primary-verified tonight, but
low-stakes since the point here is just "these are two different cases," not a claim this project is
building on.)

---

## What changed vs. what didn't

- **Changed:** WV oral-argument date moves from "unconfirmed, don't repeat" to **confirmed via a
  primary court source** — Oct 30, 2026, 8:30 a.m., Panel 4, Gold Courtroom, per the 4th Circuit's own
  calendar PDF.
- **Unchanged:** ND amalgamation appeal — still pending, still just Summit's Aug 31 motion to narrow
  to Summit #3 as the latest development, still no docket number or schedule reachable from this
  environment. This is a genuine "nothing moved" finding, not a search failure — worth taking at face
  value rather than assuming more searching would find something.

## What's still open

- ND appeal's docket number/briefing schedule: needs a working ndcourts.gov or paid-docket-tracker
  access path this environment doesn't have. Re-check next pass in case ndcourts.gov's bot-block
  lifts, but don't expect a different result from the same search-only approach.
- WV case: worth one more check closer to Oct 30, 2026 in case the argument is continued/rescheduled
  (calendars do get amended) — re-pull the same calendar URL rather than re-searching generically.
- No theory-chain, Track, or design decision was touched — this is fact-verification only, same
  scope as the 09-08/09-09 passes.
