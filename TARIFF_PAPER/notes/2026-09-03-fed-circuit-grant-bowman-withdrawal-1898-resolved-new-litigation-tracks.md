# 2026-09-03 — Federal Circuit docket recheck: Grant & Bowman withdrawal, 26-1898 identity resolved, three new parallel tariff-litigation tracks, refund-wave story stable

## What this is
Continuation of the nightly Federal Circuit docket-check series (08-29 through 09-02). Read-only
research pass (background agent), findings written up here by the coordinating session. All docket
facts below were read directly from CourtListener's docket-entries tables via `curl` (not just the
capped RECAP search API the prior notes relied on more heavily) — this surfaced the Grant & Bowman
entries the prior search-API technique had missed.

## 0. Framing gap worth flagging: the underlying legality question is already decided

Neither the 09-01 nor 09-02 note states this explicitly, so flagging it now: the constitutional
question — whether IEEPA authorizes the tariffs at all — was **fully resolved by the Supreme Court on
February 20, 2026** in the consolidated *Learning Resources, Inc. v. Trump* / *Trump v. V.O.S.
Selections, Inc.* (Nos. 25-250 & 24-1287), affirming the Federal Circuit's Aug. 29, 2025 en banc
ruling that IEEPA does not authorize the tariffs. Confirmed via SCOTUS's own docket:
https://www.supremecourt.gov/docket/DocketFiles/HTML/public/25-250.html (argued Nov. 5, 2025, decided
Feb. 20, 2026).

**26-1895 (filed June 3, 2026) is a separate, later, post-remand appeal** — the government's appeal of
the CIT's implementation/refund order (the "$175 billion refund reckoning"), not the constitutionality
question. So "ongoing tariff litigation" in the manuscript should be precise: the *legality* of the
IEEPA tariffs is settled (unlawful); what's still being litigated is refund *mechanics and scope*.
Worth checking whether the manuscript's framing already reflects this distinction. Secondary
corroboration: https://patentlyo.com/patent/cafc/2026/03/forthwith-federal-circuit-issues-mandates-in-v-o-s-selections-clearing-the-way-for-175-billion-refund-reckoning.html

## 1. Docket 26-1895 (lead case) — new withdrawal, otherwise stable

- **NEW: Grant & Bowman, Inc. has formally withdrawn.** Docket entry #24 (Sep 2, 2026, 4:41 PM):
  "Official caption revised to remove the Appellee designation for AGS Company Automotive Solutions
  **and Grant & Bowman, Inc.**" (tagged to 26-1895/-1897/-1899). Cross-checked Grant & Bowman's own
  pre-consolidation docket (26-1899, docket_id 73435011) directly: entry #10 (Aug 24, 2026) —
  "Letter from Appellee Grant & Bowman, Inc. ... Notification that Grant & Bowman will not participate
  in these proceedings and, accordingly, will not be filing a brief." Same withdrawal language as
  AGS's Aug 21 letter.
  - This also confirms **Grant & Bowman's original pre-consolidation docket number was 26-1899**
    (previously only inferred by elimination in the 09-02 note; now confirmed directly via that
    docket's own June 4, 2026 consolidation motion naming it).
  - Of the three named parties in this project's working shorthand ("V.O.S. Selections/AGS/Grant &
    Bowman"), **two have now formally exited active litigation** (AGS Aug 21, Grant & Bowman Aug 24).
    Only V.O.S. Selections itself remains confirmed active among that trio. The caption is shrinking
    from its ~20-appellee peak — worth double-checking the manuscript doesn't describe either AGS or
    Grant & Bowman as active litigants (spot-check tonight found no such description anywhere in the
    manuscript-facing files, so likely fine, but flagging since the caption keeps changing).
- Sources (primary, read in full today):
  https://www.courtlistener.com/docket/73433096/vos-selections-inc-v-trump/ and
  https://www.courtlistener.com/docket/73435011/grant-bowman-inc-v-united-states-customs-and-border-protection/

**Stable, unchanged since 09-02:**
- No response/appellee brief filed as of today — last substantive docket entry through Sep 2 is the
  caption revision above.
- No oral argument scheduled. Re-fetched and read in full both the September 2026 calendar (still
  "Revised August 19, 2026," unchanged) and December 2026 calendar (still "Revised August 31, 2026,"
  unchanged, still only one unrelated case). Neither lists 26-1895 or any party name from it. The
  October calendar was **not independently re-verified today** (tooling limitation — no
  `pdftotext`/`pdftoppm` available; last independently verified 09-02) — flag for a future session.
- No cert petition or SCOTUS-adjacent activity found on 26-1895 — unsurprising since Federal Circuit
  briefing isn't even complete.

## 2. Case 26-1898 identity and dismissal reason — now resolved

**Confirmed, not inference:** 26-1898 was ***Euro-Notions Florida, Inc. v. United States Customs and
Border Protection*** (docket_id 73435009) — the government's appeal of the CIT's ruling in
*Euro-Notions Florida, Inc. v. United States* (CIT No. 1:25-cv-00595), which had been **selected as
the lead/test case for the CIT's supervision of the IEEPA tariff-refund process** (the scope question
of whether refunds go to all importers or only those who sued).

**This is unrelated to CBP Commissioner Rodney Scott's testimony** — the 09-02 note's inference tying
26-1898 to "a CBP Commissioner's appearance" appears to be **incorrect**. That was a separate matter:
a mandamus petition, *In re United States* (CAFC No. 26-144, filed June 2, 2026, dismissed June 9,
2026 after DOJ withdrew it), over whether Commissioner Scott personally had to testify. Worth
correcting wherever that inference was carried forward.

**Actual dismissal reason:** Euro-Notions Florida voluntarily dismissed its own underlying CIT case
on **July 16, 2026** (USCIT Rule 41(a)(1)(A)(i), a plaintiff's right to dismiss before the defendant
answers). This mooted the government's Federal Circuit appeal, which the government moved to dismiss
(July 20, confirmed in the lead docket's entry #15) and the court granted (July 28, entry #17). Judge
Eaton named a new lead refund case, ***Freestyle World, Inc. v. United States***, so the broader
refund litigation continues under a different named plaintiff. **Why Euro-Notions itself chose to
dismiss is not reported anywhere, primary or secondary — genuinely unresolved, not guessed at.**
- Primary: CAFC docket entries #15–17 (same lead docket as above).
- Secondary (consistent across independent trade-press sources):
  https://tradelawdaily.com/article/2026/07/17/euronotions-dismisses-case-that-had-been-lead-ieepa-refunds-case-2607160074
  — the Rule 41 mechanism and closed-conference detail are secondary-source only (a linked CIT order
  PDF returned unrenderable), though multiple independent outlets agree.

## 3. Axle of Dearborn (de minimis) — still not appealed

Fetched the full CIT docket (1:25-cv-00091, docket_id 70287201) directly — 79 entries, last entry Aug
25, 2026 (two orders on the reliquidation/stay motion, explicitly preserving the de minimis ruling
"for the avoidance of doubt" as untouched). **No notice-of-appeal entry anywhere.** Nothing has posted
since Aug 25.

Summary judgment for the government (Slip Op. 26-94) issued **Aug 13, 2026**; under the standard
60-day CIT→CAFC appeal window that puts the government's deadline at roughly **October 12, 2026** —
about **39 days remaining** as of today. This is the coordinator's own arithmetic from the primary
ruling date, not a court-stated deadline. No news of a filed appeal found.
Source: https://www.courtlistener.com/docket/70287201/axle-of-dearborn-inc-v-department-of-commerce/

## 4. Tariff-refund consumer pass-through story — stable since ~Aug 19-22, no September developments

Well-covered through late August; nothing found dated after ~Aug 22 despite explicit searches for
September activity. Useful primarily as stable corpus material, not breaking news:

- **Not passing refunds to consumers:** Target ($994M received, CFO says money goes to "invest in
  price" broadly), Amazon ($600–640M Q2, "may offer refunds to only a limited number of customers"),
  Nike (~$302M of ~$986M expected, silent despite consumer lawsuits), Apple ($2.2B, investing in
  domestic manufacturing instead), Walmart (up to $10.2B expected, "will not offer refunds but will
  put that money toward lowering prices").
- **Passing refunds to consumers:** FedEx (~$800M "being held for refunds to customers" — FedEx itself
  sued for the refunds), UPS and DHL (similarly committed), Costco (committed after facing four
  consumer class actions).
- Scale: CBP says >330,000 importers paid IEEPA tariffs, ~$166B total; ~$100B refunded to companies as
  of Aug 4, 2026; widely-cited estimate that only ~15-20% will reach consumers.
- Sen. Elizabeth Warren publicly pressed seven companies (Aug 7 press release, fetched directly:
  https://www.warren.senate.gov/newsroom/press-releases/warren-pushes-giant-corporations-to-give-billions-in-tariff-refunds-back-to-consumers/).
  Rep. Cuellar introduced the "American Consumer Tariff Rebate Act of 2026" (up to $2,040/household) —
  not enacted, WebSearch-summary confidence only.
- Key article (direct-fetch confirmed):
  https://fortune.com/article/fortune-500-companies-billions-tariff-refunds-customers-08-19-2026/
  (Aug 19, 2026, most detailed company-by-company breakdown).

This ties directly to scouting idea 22 (tariff-refund windfall retention) — the corpus is real and
already assemble-able if Britton greenlights it.

## 5. New: three parallel tariff-litigation tracks beyond 26-1895

The manuscript's "ongoing tariff litigation uncertainty" framing, if it currently centers on a single
case, understates the actual legal-uncertainty environment. Three additional, distinct tracks are
active right now:

- **Section 122 tariffs (10% "balance-of-payments" surcharge, imposed after the Feb 2026 IEEPA loss).**
  CIT struck them down 2-1 as unauthorized (https://www.cnbc.com/2026/07/24/trump-tariffs-lawsuit-301-ieepa.html).
  Government appealed — a separate consolidated CAFC appeal captioned *State of Oregon v. Trump*
  (Nos. **26-1804/26-1805**, the latter also styled *Burlap and Barrel, Inc. v. Trump*), filed May 8,
  2026. Existence confirmed directly via CourtListener search. Per a secondary summary (TaxProf Blog,
  Aug 26, 2026, since the underlying Steptoe blog 403'd on direct fetch:
  https://taxprofblog.aals.org/2026/08/26/tariff-litigation-update/): Federal Circuit stayed the CIT
  injunction pending appeal; government's opening brief filed July 21 (corrected July 29); appellee
  responses were due "this week" as of Aug 26 — likely due right around now/early September. Docket
  entries themselves were not independently pulled today.
- **Section 301 "forced-labor" tariffs (10-12.5% on 60 countries, imposed July 2026).** Consolidated
  at CIT as *In re Section 301 Forced Labor Cases*, sample case ***Learning Resources, Inc. v. United
  States*** (a new CIT case, distinct from the SCOTUS case of the same plaintiff name). Per the same
  TaxProf Blog summary: plaintiffs' motion for judgment on the agency record filed Aug 25;
  **government's response due Sep 4** (tomorrow); reply due Sep 18; **oral argument set for Sep 30**
  before Judges Choe-Groves, Reif, and Wang. Corroborated independently (MLex headline, NBC News).
  Worth a follow-up check around Sep 30.
- **Section 338 tariffs on Canada (50% on ~$20B of imports, effective Aug 22, 2026).** Confirmed via
  multiple outlets (PBS, Boston Globe, BNN Bloomberg — all republishing the same AP-style wire piece,
  Aug 29, 2026) that **no lawsuit had been filed as of Aug 29**, though the Liberty Justice Center is
  actively recruiting plaintiffs and trade lawyers consider a challenge "highly likely" ("this law is
  literally a blank canvas because it's never been litigated"). Nothing found suggesting a suit has
  since been filed as of today.

## Summary table: changed vs. stable since 09-02

| Item | Status |
|---|---|
| Response brief in 26-1895 | Stable — still none filed |
| Oral argument scheduling (Sep/Dec calendars) | Stable — unchanged, no listing |
| AGS withdrawal | Already known (09-02) |
| Grant & Bowman withdrawal | **NEW** — Aug 24 letter, Sep 2 caption revision |
| 26-1898 identity/reason | **NEW** — resolved (Euro-Notions Florida's lead refund case; dismissed after Euro-Notions voluntarily dismissed its own CIT case; unrelated to CBP Commissioner Scott) |
| Grant & Bowman's original docket number | **NEW** — confirmed as 26-1899 |
| Axle of Dearborn appeal | Stable — still not filed, ~39 days left |
| Tariff-refund pass-through story | Stable since ~Aug 19-22, no Sep developments |
| Section 122 (State of Oregon v. Trump, 26-1804/-1805) | **NEW to project notes** — briefing likely closing now |
| Section 301 forced-labor (Learning Resources v. US) | **NEW to project notes** — CIT oral argument Sep 30 |
| Section 338 Canada tariffs | **NEW to project notes** — in effect since Aug 22, not yet challenged as of Aug 29 |

## Open items for Britton
- Whether the manuscript's litigation framing should be updated to reflect that IEEPA's illegality is
  settled (SCOTUS, Feb 2026) and what's ongoing is refund mechanics — plus the broader multi-track
  litigation picture (Section 122/301/338) if that level of detail is wanted.
- Refund-wave corpus-scope call (ties to scouting idea 22) — still his, untouched again tonight.
- Everything else here is informational, not blocking.
