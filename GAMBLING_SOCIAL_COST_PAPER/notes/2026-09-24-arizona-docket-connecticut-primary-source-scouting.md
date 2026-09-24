# 2026-09-24 — Arizona/Kalshi docket read directly (major correction), Connecticut fully closed via primary statute text, FTC/H.R. 10357 rechecks, Illinois per-wager tax flagged

This pass works the four items the 09-21 note left open, in the same priority order, plus a general
policy-staleness scan of `policy/state_policy_variables.md`. No design or scope decisions made — all
findings below are flags for Britton, same as every prior pass.

## 1. Arizona/Kalshi litigation — direct court-docket read finds the 09-19/09-21 characterization needs correction, not just confirmation

The 09-21 note's top open item was: "Arizona's actual *KalshiEX v. Johnson* docket has not been read
directly (PACER/court-site access, not this session's tools)." This pass got there — not via PACER, but
via **CourtListener's free RECAP mirror**, which turned out to be reachable this session via a direct
`curl` fetch (WebFetch itself 403'd on courtlistener.com; plain `curl` without any special flags returned
a clean HTTP 200 and the full docket HTML, ~540KB). This is a genuinely different and more complete
picture than the secondary-reporting reconstruction in the 09-19/09-21 notes.

**Case identity, confirmed directly from the docket header**: *KalshiEX LLC v. Johnson*, No.
**CV-26-1715-PHX-MTL** (D. Ariz.), filed March 12, 2026, assigned to **Judge Michael T. Liburdi** (after
two recusals — first Judge David G. Campbell, then Senior Judge James A. Teilborg). Last docket activity
as of this pass: Sept. 23, 2026 (administrative "mail returned" notices only — see below).

**What actually happened, reading the docket entries themselves rather than secondary press coverage**:

- **Apr 8, 2026 (docket #51)**: the order discharging the Younger-abstention show-cause order also
  **DENIED Kalshi's own Motion for Preliminary Injunction (Doc. 11) and Motion for Immediate TRO
  (Doc. 42)**. Kalshi lost its own bid for injunctive relief at this stage. Kalshi appealed this denial
  to the Ninth Circuit the same week (Notice of Interlocutory Appeal, docket #98, May 8, 2026 — **Ninth
  Circuit No. 26-2978**).
- Separately, the **CFTC and United States** — who had joined/intervened as "Consolidated Plaintiffs" —
  filed their **own** Motion for TRO and Preliminary Injunction the same day, April 8 (docket #49). This
  is a distinct motion from Kalshi's, not the same one.
- **May 5, 2026 (docket #96)**, verbatim: *"IT IS ORDERED the Temporary Restraining Order (Doc. 65) is
  DISSOLVED. FURTHER ORDERED that the CFTC's Motion for Preliminary Injunction (part of Doc. 49) is
  GRANTED."* This is a **preliminary injunction, not a permanent one**, and it was **won by the CFTC/US
  suit, not by Kalshi** (whose own request for the same relief had already been denied a month earlier).
  Arizona (Kristin Mayes, Jackie Johnson) appealed this grant on Jul 6, 2026 (docket #107 — **Ninth
  Circuit No. 26-4281**).
- **May 18, 2026 (docket #104)**: the district case was **stayed** by stipulation, pending a Ninth
  Circuit decision in the cases consolidated for the April 16, 2026 oral argument — confirmed by name
  and number: **North American Derivatives Exchange, Inc. v. Nevada, No. 25-7187; KalshiEX, LLC v.
  Assad, No. 25-7516; Robinhood Derivatives, LLC v. Dreitzer, No. 25-7831.** All pending deadlines
  (including Arizona's time to answer Kalshi's complaint) were vacated.
- **No substantive docket entries between Jul 10, 2026 (docket #108, the Ninth Circuit case-number
  notice for Arizona's appeal) and Sept 21/23, 2026** — the only entries in that gap are two purely
  administrative "mail returned as undeliverable" notices (docket #109, #110). **As of this pass (Sept
  24, 2026), nearly a month after the Ninth Circuit's Aug 28, 2026 ruling in the consolidated *KalshiEX
  v. Assad* (Nevada) case — which went the opposite direction, against CEA preemption — neither party has
  moved to lift the stay or asked for a status conference in the Arizona district case.** This is itself
  a real, citable fact (the case is procedurally dormant despite a directly relevant appellate ruling
  having issued), not something this pass is speculating about.
- The CFTC's own parallel suit against Arizona — which the 09-21 note could not get a clean caption for
  from its own PDF and only guessed "captioned around Katie Hobbs" from secondary reporting — is
  confirmed directly from the docket text (a April 2, 2026 status-conference order referencing it) as
  **"United States, et al. v. Arizona, No. 2:26-cv-02246-DMF (D. Ariz. 2026)."** This resolves that
  specific uncertainty flag; the docket for *that* case itself was not separately pulled this pass.

**Corrected bottom line**: the 09-19/09-21 notes' description — "Liburdi converted [Kalshi's] TRO into a
permanent injunction... ruling federal law preempts Arizona's gambling law" — is not a fabrication (it
tracked reputable secondary reporting faithfully) but **conflates two different things**: Kalshi's own
requested relief was actually denied in April; the relief that succeeded in May was the CFTC's separate
motion, and it was preliminary, not permanent. If this ever surfaces in manuscript background text, use
the docket-sourced version above, not the 09-19/09-21 summary. This remains background/prediction-market
context, not core sports-betting-operator policy-stringency data — same relevance tier as before.

**Item now closed**: no PACER access was needed — CourtListener's free RECAP archive had everything.
Future passes checking federal-court status should try CourtListener via direct `curl` (not WebFetch,
which 403'd) before assuming PACER access is required.

## 2. FTC non-response — rechecked, still no response found

Fresh search of ftc.gov's press-release listing and targeted queries turns up nothing new. No FTC
response to the June 3, 2026 Mullin/Vasquez letter (9 House members, response requested by June 29, 2026)
has been found as of this pass — now nearly three months past the requested deadline. Same status as
09-19 and 09-21: genuinely unresolved, not a new finding. Worth another check in a few weeks; continued
silence approaching 90+ days past deadline is itself becoming a more citable fact over time.

## 3. Connecticut §12-867 / Public Act 21-23 — fully resolved via direct primary-statute-text read; item closed

The 09-21 note's cga.ct.gov PDF fetch (the enrolled Public Act 21-23 at
`cga.ct.gov/2021/ACT/PA/pdf/2021PA-00023-R00HB-06451-PA.pdf`) had 503'd on three consecutive prior
passes. Re-tried it this pass and it **returned cleanly (HTTP 200, ~334KB)** — confirming those earlier
503s were transient/server-side for those specific sessions, not a standing block on the domain.

Extracted and read **Sec. 18 of the enrolled Public Act 21-23** (Substitute House Bill No. 6451)
directly. Verbatim, Sec. 18(a): a master wagering licensee "shall pay to the state for deposit in the
General Fund: Thirteen and three-quarters per cent of the gross gaming revenue from online or retail
sports wagering." Sec. 18(b)(2), on the promotional-coupon carve-out: coupons/credits issued "for the
sole purpose of sports wagering" and "linked to sports wagering in a documented way as part of a
promotional program and actually played by the patrons" are excluded from gross gaming revenue *unless*
the aggregate monthly amount exceeds **25% of GGR in the first year of operation, 20% in the second
year, or 15% in the third year and thereafter** — in which case the excess above the threshold is taxed.

This **exactly matches** both prior secondary sources this project used (the codes.findlaw.com statute
mirror from 09-19, and Connecticut's own open-data portal metadata from 09-21) — no discrepancy found
anywhere across the three sources. The item is now closed at the strongest sourcing tier this project
uses (primary enrolled-bill text), not resting on secondary confirmation. Updated
`policy/state_policy_variables.md`'s Connecticut row accordingly.

**Technical note, worth carrying forward**: this session's usual PDF-extraction tools both failed —
`pypdf` and `pdfminer.six` both crashed on a broken system `cryptography` package (a Rust-binding panic,
`ModuleNotFoundError: No module named '_cffi_backend'`), and `apt-get install poppler-utils` 404'd again
on the security-archive mirror (same failure this project's 09-21 note flagged). **Worked around this
time with PyMuPDF** (`pip install pymupdf`, imported as `fitz`), which does not depend on the broken
`cryptography` package and extracted all 65 pages cleanly. Future sessions hitting the same
pypdf/pdfminer failure should try PyMuPDF first.

## 4. H.R. 10357 — rechecked, no material change since 09-21

Confirmed again via fresh search: cleared House Ways & Means 38-5 on Sept 16, 2026 as part of the
broader Digital Asset Tax Certainty Act package (the wagering-loss-deduction piece is the bipartisan
"Full House Act," Reps. Horsford D-NV and Miller R-OH), now headed to the House floor, with **no floor
vote expected until after the November 2026 midterms** — same status as 09-21, just reconfirmed with
newer (mid-to-late Sept 2026) sourcing. No new figures found beyond the JCT's ~$2B/2027-2036 revenue-cost
estimate already logged 09-21.

## 5. Policy-file staleness scan — one informational flag, not core to the current design

Per the assignment to check `policy/state_policy_variables.md` for staleness against current news: spot
searches on several already-coded states (Illinois, Ohio, Massachusetts) turned up nothing that
contradicts existing entries, **with one exception worth flagging, not coding in**: Illinois adopted a
**separate per-wager excise tax** (25¢ on each of the first 20 million bets/fiscal-year, 50¢ thereafter)
effective July 1, 2025 — a different tax mechanism layered on top of the GGR tax this project already
has coded (230 ILCS 45/25-10, no promotional deduction). A repeal bill (HB 5143, Rep. Didech) cleared the
Revenue and Finance Committee with bipartisan support and an April 17, 2026 crossover deadline, but this
pass could not confirm final passage/signature status as of late Sept 2026 — genuinely unresolved, not
just unchecked. **Not adding this to the coded table**: it's a tax-rate/mechanism variable, not a
promotional-deduction or advertising-stringency variable, and doesn't cleanly fit any of the project's
current coded dimensions — flagging for Britton's judgment on whether a future pass should add a
separate "special/excise tax structure" column, rather than assuming it belongs in the existing ones.

## What's still open / unresolved after tonight

- **FTC non-response** — recheck again in a few weeks; approaching 90+ days past the requested deadline
  makes continued silence itself more citable over time.
- **Connecticut** — closed; no further action needed on this specific item.
- **Arizona** — the district case is stayed and procedurally dormant; the cleanest next check-in point is
  whenever the Ninth Circuit issues mandates in the three consolidated cases (NADEX v. Nevada 25-7187,
  KalshiEX v. Assad 25-7516, Robinhood v. Dreitzer 25-7831), which would let the stay be lifted.
- **H.R. 10357** — no floor vote expected before the November midterms; next natural check-in point is
  after the midterms.
- **Illinois per-wager tax (HB 5143)** — final passage/signature status unresolved as of this pass; a
  quick recheck in a few weeks would likely resolve it either way. Also an open design question for
  Britton (not decided here): does this tax mechanism belong in the coded policy table at all, and if so,
  as what kind of variable?
- Everything else flagged as open in `PROJECT_STATUS.md`, `DECISION_LOG.md`, and
  `notes/open_questions.md` remains open — this pass was scoped to the four 09-21 follow-ups plus a
  staleness scan, not a full project review.

No fabricated citations, case names, dockets, statute text, or figures were introduced this pass. Where a
route was genuinely blocked (courtlistener.com via WebFetch, HB 5143's final status), that is stated
plainly above rather than worked around with an unverified guess.
