# 2026-09-16 — Litigation sweep beyond WV/ND: genuine new movement found in IN POET v. Wabash County; ND still blocked; CA/LA/CO unchanged

**AI involvement disclosure:** this note was produced by an AI agent (Claude) doing autonomous
overnight verification work on this repo, per the project's standing conventions. All claims below
are labeled by source type (primary/secondary) as found tonight; nothing here was fabricated, and
anything not independently confirmed is flagged as such rather than smoothed over.

**Orientation:** read `README.md`, `CCS_PAPER/README.md`, and the four most recent `notes/` files
(2026-09-14 litigation recheck, 2026-09-14 implementing-body-constant literature check, 2026-09-09
ND/WV note, 2026-09-08 power-analysis note) plus the two most recent `Analysis/` litigation notes
(2026-09-05, 2026-09-08) to establish the full set of tracked cases before deciding where to spend
tonight's time. Per the 09-14 note, WV's Oct 30, 2026 oral-argument date is already primary-source
confirmed and not due for recheck yet, and the ND amalgamation appeal has been structurally blocked
from primary-source verification for 5+ sessions running. Rather than re-running the same failed ND
approach at length or sitting idle on WV, tonight's pass (a) did one quick, fast ND re-attempt as
instructed, then (b) swept the **other** tracked litigation the 09-05/09-08 `Analysis/` notes
identified but which the 09-09/09-14 `notes/` passes hadn't rechecked: IN POET v. Wabash County, CA
Committee for a Better Shafter v. Kern County, the LA Save My Louisiana eminent-domain suit, and
Colorado's Class VI primacy rulemaking status.

**Method:** direct primary/authoritative-source fetches preferred throughout, per this project's
established practice — `curl` with a browser user-agent against ndcourts.gov (repeat of the standing
approach); CourtListener's RECAP-mirrored PACER docket page for POET v. Wabash County (actual federal
court docket entries, not search-engine synthesis — a step up from the secondary news coverage the
09-05 note relied on for this case); the Federal Register's own API for Colorado Class VI primacy
rulemaking status. WebSearch used only for the two items with no accessible primary docket source
(CA and LA are state-court matters not indexed by CourtListener/PACER).

---

## 1. North Dakota — ndcourts.gov — still blocked, one quick attempt only

Re-tried `curl` with a browser user-agent against `ndcourts.gov/supreme-court/opinions` (HTTP 403,
same "Security Check" interstitial as every prior session since 09-05) and `ndcourts.gov/dockets`
(HTTP 404, soft-404 template). **No change — still structurally blocked, a sixth-plus consecutive
session.** Per the standing instruction not to burn time re-running the same failed approach, this
pass stopped here rather than trying further variations. Nothing new to report on the amalgamation
appeal's docket number or schedule.

## 2. Indiana — POET Biorefining–North Manchester LLC v. Board of Commissioners of Wabash County (3:26-cv-00291-SJF, N.D. Ind.) — **genuine new movement, primary-source (RECAP/PACER docket) confirmed**

This is tonight's real finding. The 09-05 `Analysis/` note had this case as "filed March 5, 2026,
status not reported beyond the filing," sourced only to a March 2026 news article. Tonight I pulled
the actual federal docket via CourtListener's RECAP archive (docket ID 72366283) — this mirrors real
PACER docket entries (dates, party actions, filing categories), not a news summary, so it's treated
as primary/authoritative here even though it's not a direct PACER pull. **The docket was last updated
September 15, 2026, 12:22 p.m. — the day before tonight's session** — with entries the project's
notes don't yet have:

- **April 27, 2026** — Wabash County filed a Motion to Dismiss for Failure to State a Claim (entry
  25) with supporting memorandum (26). No separately-labeled "order on motion to dismiss" entry
  appears in the docket's terse RECAP category tags between then and the next filings, so whether/how
  it was resolved isn't clear from the entry descriptions alone (these are PACER's generic NEF
  category labels, not full docket text — flagging the limits of what this source can tell us rather
  than guessing at the disposition).
- **May 27, 2026** — POET (plaintiff) filed a **Motion for Summary Judgment** (32), Statement (33),
  and Memorandum in Support (34) — not in any prior project note.
- **June 18–29, 2026** — a Motion for Miscellaneous Relief (35), Response (36), Reply (38), and Order
  on that motion (39).
- **July 22 – Aug 28, 2026** — further Response/Reply rounds (40–43) and a Motion/Order for Leave to
  File (44–45), consistent with continued summary-judgment-stage briefing.
- **September 2, 2026** — POET filed an **Amended Complaint** (46).
- **September 15, 2026** — following the amended complaint, a **second round of summary judgment
  filings**: Motion for Summary Judgment (47), Statement (48), Memorandum in Support (49), and a
  Notice (50).

**No secondary/news coverage of the September 15 filing turned up in tonight's WebSearch** — the only
news results found were the original March 2026 filing coverage (WANE, 21Alive, Indiana Lawyer,
Carbon Herald, WBOI). That's expected given the filing is one day old; flagging it here specifically
so a future pass doesn't have to rediscover it from scratch, and because it's a genuinely new,
primary-source-confirmed development this project didn't have before tonight.

**Caveat:** RECAP/CourtListener docket entries are sourced from PACER metadata but the *documents
themselves* (the actual motions/complaint text) were not pulled or read tonight — only the docket's
entry list and dates. If the paper wants to characterize what the amended complaint or the new summary
judgment motion actually argues, that requires buying/pulling the underlying PACER documents (each
entry shows a "Buy on PACER" cost, which appears to be $0 for at least the ones checked, i.e.
free/cheap to retrieve if Britton wants the actual text next).

## 3. Colorado — EPA Class VI primacy rulemaking — no change, primary-confirmed via Federal Register's own API

Queried the Federal Register's public API directly for "Colorado Class VI primacy underground
injection" documents, sorted newest-first. **The only Colorado Class VI item on record is still the
March 19, 2026 Proposed Rule** (`2026-05453`) — no Final Rule has been published as of tonight's
query. This is a direct, authoritative-source confirmation (not a news search) that Colorado's
primacy grant remains unfinalized, consistent with the 09-05 note's "not yet finalized as of Aug 6,
2026" finding — **no movement since then.**

## 4. California — Committee for a Better Shafter v. County of Kern (Kern County Superior Court, BCV-24-104003) — no change found

This is a state-court case not indexed by CourtListener/PACER, so no direct-docket path was available;
WebSearch found nothing dated later than the case's original Nov. 2024 filing and the July 2026
Inside Climate News piece already logged in the 09-05/09-08 notes (Carbon TerraVault 1 operational
since May 2026, suit still pending). **No ruling, no new filing found tonight — unchanged.**

## 5. Louisiana — Save My Louisiana eminent-domain suit (19th JDC, filed Nov. 20, 2025) — no change found

WebSearch found the same set of sources already in the project's notes (Louisiana Illuminator,
Carbon Herald, Business Report, Rapides Parish Journal's April 8, 2026 piece on HB7's rejection).
**No ruling reported since the suit was filed — still pending, unchanged.** LA HB7's exact 12-7
committee vote tally remains the known ASP.NET-gated limitation from prior notes; not re-attempted
tonight (same reasoning as before — a browser-based path, not a fetch-tooling problem).

---

## What changed vs. what didn't

- **Changed:** IN POET v. Wabash County — a real, primary-source (RECAP/PACER docket)-confirmed
  development: an amended complaint (Sept 2, 2026) and a second round of summary-judgment filings
  (Sept 15, 2026, one day before this session), neither previously logged anywhere in this project.
  Also newly confirmed from the same docket pull: POET's own first summary-judgment motion was filed
  May 27, 2026, and Wabash County's motion to dismiss was filed April 27, 2026 — both previously
  unknown to this project's notes (the 09-05 note only had the case as "filed, status not reported").
- **Unchanged:** ND amalgamation appeal (ndcourts.gov still blocked, sixth-plus session); Colorado
  Class VI primacy (still proposed-rule stage, primary-confirmed via Federal Register API); CA
  Shafter (still pending, no ruling); LA Save My Louisiana suit (still pending, no ruling). All four
  are genuine "nothing moved" findings from tonight's checks, not search-effort gaps.
- **Not touched tonight:** WV WVSORO v. Zeldin (per the 09-14 note, already primary-confirmed and not
  due for recheck until closer to Oct 30, 2026); IL Mahomet Aquifer ban's exact effective-date
  confirmation (a minor open item from the 09-08 `Analysis/` note, lower priority than the above and
  not reached tonight).

## What's still open

- **IN POET v. Wabash County:** the actual text of the September 2 amended complaint and the
  September 15 summary-judgment filings hasn't been pulled/read — only docket metadata. Worth a
  follow-up pass to retrieve and read those documents (appears to be free/cheap via PACER per the "0"
  cost shown for entries checked) if this case is going into the comparative-litigation write-up,
  especially since the April 27 motion to dismiss's resolution isn't visible from the docket entry
  labels alone.
- **ND amalgamation appeal:** still structurally blocked from ndcourts.gov; per the 09-14 note, worth
  one more quick check per session rather than a sustained effort, unless a different access path
  (PACER-equivalent, a paid docket tracker) becomes available.
- **IL Mahomet Aquifer effective-date confirmation:** still open from the 09-08 `Analysis/` note (the
  Act's own "Section 99. Effective date" clause wasn't found in the extracted text; secondary sources
  say Jan 1, 2026). Not attempted tonight — lower priority than the above, flagged for a future pass.
- No theory-chain, Track, or design decision was touched — this is fact-verification/litigation-
  tracking only, same scope as the 09-08/09-09/09-14 passes. The POET v. Wabash finding is new raw
  material, not a claim about how or whether it fits the paper's comparative framing — that stays
  Britton's call.
