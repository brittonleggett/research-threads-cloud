# Overnight Summary — 2026-09-21

## What tonight did

Ran four research passes in parallel (each confined to its own directory; each commit landed
and pushed as soon as that pass's completion report arrived, same process as prior nights).
Rotated toward TARIFF_PAPER (always top priority) and the two projects not touched since 09-18/
09-19 — DATA_CENTER_LEGITIMACY_PAPER and GAMBLING_SOCIAL_COST_PAPER — plus scouting.
DATA_CENTER_PAPER, CCS_PAPER, FLOCK_CAMERAS_PAPER, SPACEX_LOUISIANA_PAPER, and
MEAT_SUPPLY_CHAIN_PAPER weren't touched tonight (all got full passes 09-19 or 09-20).

**TARIFF_PAPER** — second uneventful litigation night running: all four watched dockets (Section
301 forced-labor master docket, Section 122/*State of Oregon v. Trump*, *V.O.S. Selections*, *Axle
of Dearborn*) re-fetched directly from CourtListener and confirmed unchanged entry-for-entry since
09-20, none terminated. Next dates that could actually move something are still weeks out (V.O.S.
Selections' response brief 10/05, Section 122's government brief 11/12). The Campbell (1999 vs.
2007) opportunism-scale citation lead got one more push via Unpaywall's API — confirmed
`oa_status: closed`, i.e. no legitimate open-access copy exists anywhere, not just that individual
sites are blocking it. Still needs Britton's library access; low-stakes either way since the
existing Campbell (2007) items already work. All standing critical-path items (CITI module
conflict, HSIRB turnaround, Jason's coding worksheet, Purchase Intention item count, banked
scales, two Qualtrics decisions) unchanged, still waiting on you or Jason. Detail:
`TARIFF_PAPER/notes/2026-09-21-litigation-recheck-stable-and-campbell-1999-unpaywall-negative-confirmation.md`.

**DATA_CENTER_LEGITIMACY_PAPER** — first pass on this project since 09-18. A novelty-defense scan
found no 2025-2026 publication using "benefit-burden asymmetry" or a close variant as a named
academic construct for infrastructure-siting justice — one WebSearch summary falsely implied a
hit on a non-academic glossary site, checked directly and ruled out. The 09-18 pass's flag on
Acevedo, Fischhoff & Patrício (2026) — whether the paper's justice-dimension ranking is a strict
four-way order or has a "similar" bottom pair — is now corroborated by four independent
abstract/highlights retrievals (still not the full text; ScienceDirect keeps 403ing WebFetch)
pointing to the weaker, non-strict reading. A broader literature-currency sweep surfaced three
genuinely new 2025-2026 items not in any prior audit: Cartwright (2026, a short data-center-EJ
commentary), Ancona et al. (2026, *Nature Cities* — an empirical map of 4,283+ US data center
sites), and Ngata et al. (2025, ACM COMPASS — a Northern Virginia community-impact study). One
widely-syndicated Yale/YPCCC survey statistic was flagged as motivating-color-only, not yet
verifiable (only a press/event page found, not the underlying report). No theory-model or
construct-naming decision made or implied. Detail:
`DATA_CENTER_LEGITIMACY_PAPER/LITERATURE/Literature_Verification_Followup_2026-09-21.md`.

**GAMBLING_SOCIAL_COST_PAPER** — first pass on this project since 09-19, closed three loose ends
from that note. **Correction, not a new finding**: the "Arizona's separate civil case against
Kalshi" read from the 09-19 note appears to have been a misreading of AG Mayes's press release —
re-fetched verbatim, it only references her office's "ongoing litigation with Kalshi," not a
separate civil suit. Reconstructed the real timeline instead: Kalshi sued Arizona preemptively
(March 2026), Arizona filed 20 criminal counts, the CFTC separately sued Arizona (plus CT and IL)
on preemption grounds, a federal judge enjoined Arizona's prosecution in May, and the Ninth
Circuit's Aug 28 ruling in a different (Nevada) case now cuts the other way and may revive
Arizona's case — Arizona is a defendant in the preemption fight, not a civil plaintiff. FTC
non-response to the June 3 Mullin/Vasquez letter: still no response found, now ~3 months past its
requested deadline. Connecticut's 25/20/15% sports-wagering promo-deduction phase-down: now
confirmed via a second independent source (Connecticut's own open-data portal, citing Public Act
21-23 directly) beyond the prior single findlaw mirror — cga.ct.gov itself remains 503-blocked.
H.R. 10357 (gambling-loss-deduction restoration): no movement, still pre-midterm; added that JCT
scores it at ~$2B in federal revenue cost over 2027-2036. Detail:
`GAMBLING_SOCIAL_COST_PAPER/notes/2026-09-21-arizona-kalshi-civil-case-ftc-connecticut-followups.md`.

**Scouting** — one new research-stream idea logged (#43): StubHub concealed-conflict-of-interest
/ "false scarcity" ticket-pricing litigation, anchored by a genuinely fresh (11-day-old at time of
writing) Louisiana filing — The Howlin' Wolf (New Orleans) sued StubHub Sept 10, 2026 in E.D. La.
alleging false-scarcity pricing claims that contradicted the venue's own real-time inventory,
alongside a separate July 2026 class action alleging StubHub's CEO concealed an ownership stake in
a reseller supplying StubHub's own inventory, and an already-verified April 2026 FTC $10M
deceptive-pricing settlement. Scoped narrowly to the platform-neutrality-betrayal/disclosure angle
to avoid overlapping an existing 2023 paper on plain scarcity-messaging perception. Six other
candidates were checked and explicitly ruled out or deferred as corpus material for existing
projects (documented in the log so future passes don't re-check them): cocoa/chocolate tariffs
(same mechanism as an existing idea), GLP-1 telehealth and BNPL regulation (already ruled out),
retail facial-recognition suits (literature-saturated), AI-augmented qualitative tooling (no
controversy hook found), Mid-Barataria coastal funding (lacks a marketing mechanism), and the
Venture Global CP2 LNG seafood suit (corpus-refresh material for an already-logged idea).
`Claude_Knowledge/Research_Stream_Ideas.md`.

## Fabrication/correction watch

No fabricated citations, docket entries, dates, or figures introduced tonight. One real correction
made to an existing project file: the 09-19 GAMBLING note's characterization of a separate
Arizona civil case against Kalshi was checked against the primary source and found not to be
supported by it — corrected in tonight's note rather than carried forward silently. One WebSearch
false-positive caught before being logged (a glossary-site "hit" on the BBA novelty scan that
didn't actually contain the phrase when fetched directly).

## Process note

No git-coordination issues tonight. Each pass's files were left untouched until that pass's own
completion report arrived; commits were staged and pushed sequentially as each of the four agents
finished (TARIFF → DATA_CENTER_LEGITIMACY → scouting → GAMBLING), with a `git fetch origin main`
immediately before each push to confirm a clean fast-forward. No stashing, no interleaving with a
still-running pass's edits.

## What's still open / blocked on you

- **TARIFF_PAPER**: litigation quiet, nothing time-sensitive for weeks. Campbell (1999) citation
  lead is now confirmed closed-access everywhere (no OA copy exists) — needs your library access
  if you want to pursue it, doesn't block anything. Standing items unchanged: CITI
  Comprehensive-vs-Basic module conflict, McNeese HSIRB turnaround, Jason's blind-coding
  worksheet, Purchase Intention item count, banked scales, two Qualtrics-build decisions.
- **DATA_CENTER_LEGITIMACY_PAPER**: no novelty threat found for the BBA construct as of tonight.
  Three new 2025-2026 citations surfaced (Cartwright, Ancona et al., Ngata et al.) — worth a look
  if any strengthen the paper's grounding. Oliveira (2026) full text still needs you to click
  through a Wiley bot-challenge directly; nothing else blocked.
- **GAMBLING_SOCIAL_COST_PAPER**: correction — there is no separate Arizona civil suit against
  Kalshi; Arizona is a defendant in the CFTC/Kalshi preemption fight, and the Ninth Circuit's
  Aug 28 ruling in the Nevada case may revive Arizona's criminal prosecution — worth knowing if
  this project's Kalshi framing assumed otherwise. FTC still hasn't answered the June letter (~3
  months overdue). Connecticut's tax figures now have two independent sources. This project is
  still at the pre-design literature/feasibility stage — no GO/MODIFY/STOP call made, stays yours.
- **Scouting**: one new idea (#43, StubHub) ready for your read if you want to greenlight it.
  Ideas 37-42 still carried forward unchanged.
- **DATA_CENTER_PAPER / CCS_PAPER / FLOCK_CAMERAS_PAPER / SPACEX_LOUISIANA_PAPER /
  MEAT_SUPPLY_CHAIN_PAPER**: not touched tonight — nothing new to report, no new blockers.
