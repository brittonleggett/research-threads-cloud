# 2026-09-07 — WV 4th Cir. oral argument date CONFIRMED, three 09-05 leads vetted via primary source, ND pore-space litigation (new)

## What this is

Follow-up on the 09-05 note's open items: (1) re-check WV 4th Cir. No. 25-1384 status, (2) vet the three
litigation/regulatory leads flagged 09-05 (LA HB7, Indiana POET v. Wabash County, CA Committee for a Better
Shafter v. Kern County) against primary sources, (3) a light national sweep for new Class VI primacy or
CCS-opposition developments. Method: direct pulls from the Fourth Circuit's own oral-argument calendar PDFs,
the Louisiana Legislature's own bill-tracking site, the actual filed court complaints (not summaries), the
EPA's own Class VI primacy page, and WebSearch/WebFetch corroboration where primary sources were blocked.
Every claim below is marked primary or secondary. `pypdf` was installed fresh this session (no PDF extraction
tooling was preinstalled; `cffi`/`cryptography` needed a `pip install --force-reinstall cffi` to work — noting
for whoever runs the next pass) and used to extract text directly from PDFs pulled with `curl`, since WebFetch
could not read the compressed PDF streams itself.

---

## 1. WV 4th Circuit (No. 25-1384) — oral argument date is now CONFIRMED

**This reverses the 09-04 and 09-05 notes' conclusion. "Late October 2026" checks out — it is now on the
court's own published calendar.**

### Primary-source pull

The Fourth Circuit's oral argument calendar page (https://www.ca4.uscourts.gov/oral-argument/oral-argument-calendar)
links PDF calendars for each session. I downloaded the calendar for the **October 27–30, 2026 Richmond, VA
regular session** directly (`internetcalOct272026.pdf`, 19 pages) and extracted the text myself with `pypdf`.
It lists, on the **Friday, October 30, 2026** docket, Panel 4, Gold Courtroom (Room 348), 8:30 a.m.,
livestreamed:

> **25-1384** ADMINISTRATIVE LAW: Petition for review of EPA's approval of West Virginia's application for
> primacy of enforcement authority over Class VI carbon sequestration wells.
> **West Virginia Surface Owners' Rights Organization v. Lee Zeldin**

This is an exact case-number and case-name match for the docket the project has been tracking. I also checked
the **October 14, 2026 special session in Greenville, SC** (`internetcalOct142026.pdf`) — 25-1384 is **not**
on that one, only the October 30 Richmond date.

**One more detail worth flagging:** I checked the HTTP `Last-Modified` header on the Oct 27–30 calendar PDF
before extracting it — **`Mon, 07 Sep 2026 03:05:55 GMT`**, i.e. the file was updated on the court's server
about two hours before this research session started tonight. That's consistent with this being genuinely new
information rather than something the 09-05 pass could have found — the calendar likely wasn't posted yet as
of the last check.

**No panel-judge names are given** — CA4's calendar format lists the case and the *district* judge whose
ruling is under review in parens (not applicable here since this is a petition for review, not an appeal, so
no district judge is listed for this entry) but not the three circuit judges who will hear it. That's normal;
CA4 doesn't publish panel composition this far in advance.

### Bottom line for Britton

**Oral argument in No. 25-1384 (WVSORO v. Zeldin) is scheduled for Friday, October 30, 2026, 8:30 a.m.,
before the Fourth Circuit in Richmond, VA — confirmed directly from the court's own calendar, not a news
summary.** The "late October 2026" figure that two prior nights couldn't substantiate is now correct and
citable, with the court's own PDF as the source. If the manuscript wants a live-argument observation or a
decision-timeline estimate, October 30, 2026 is the anchor date. Recommend Britton or a research assistant
watch for the decision after that date — Fourth Circuit decisions typically follow argument by weeks to
several months, so nothing here estimates when a ruling will issue.

---

## 2. The three 09-05 leads — vetted against primary sources

### 2a. Louisiana HB7 ("Louisiana Landowners Protection Act") — primary-sourced via legis.la.gov, outcome confirmed, vote count still secondary-only

Pulled the bill's own status page directly from the Louisiana Legislature's site
(`legis.la.gov/legis/BillInfo.aspx?s=26RS&b=HB7`). Confirms:

- **HB7, 2026 Regular Session**, title "PROPERTY/EXPROPRIATION — Enacts the Louisiana Landowners Protection
  Act," sponsor **Rep. Mike Johnson**.
- Prefiled 01/12/2026; referred to House Committee on Natural Resources and Environment 03/09/2026.
- **03/31/2026: "Involuntarily deferred in committee."** This is the Louisiana legislature's own official
  status language, pulled from the bill-tracking page's action log — not a paraphrase. In Louisiana
  legislative practice, "involuntary deferral" is the parliamentary mechanism a committee uses to kill a bill
  for the session without a formal "do pass"/"do not pass" vote — functionally equivalent to what the 09-05
  note (drawing on news coverage) called "rejected"/"failed." Also confirmed via the committee's own
  03/31/2026 agenda page (`agenda.aspx?m=25586`), which lists HB7 with the same title and sponsor.
- **The specific "12–7" vote count from the 09-05 note is still not independently confirmed against a primary
  roll-call record.** The bill-status page links to a `Vote.aspx?moi=976506` page, but that page requires
  ASP.NET session/postback state that a direct URL fetch can't supply — it returns a generic "Page Not Found"
  regardless of the underlying data. I could not get past this from here. The 12–7 figure remains
  multiply-corroborated by independent secondary sources (The Advocate, KALB, The Center Square, American
  Press, Rapides Parish Journal — five outlets, none citing each other) but isn't primary-verified to the
  decimal. This is a minor gap, not a substantive uncertainty — the *outcome* (bill did not advance) is now
  primary-confirmed either way.

**Bottom line:** HB7's failure is solid and citable (primary source: the bill's own status page). The 12-7
tally specifically should be attributed to news coverage if used, not treated as court-record-grade.

### 2b. Indiana — POET Biorefining v. Wabash County — primary source obtained (the actual complaint), one correction to the 09-05 note

WANE (a local TV station) hosts the actual filed complaint PDF; I downloaded it directly and extracted the
full 24-page document with `pypdf`. This is the real filed pleading, not a summary. Confirms:

- **Caption:** POET Biorefining – North Manchester, LLC d/b/a POET Bioprocessing – North Manchester v. Board
  of Commissioners of Wabash County, Indiana. **Case No. 3:26-cv-00291-SJF**, U.S. District Court, Northern
  District of Indiana, **South Bend Division**. Filed **03/05/26** (footer stamp on every page: "USDC IN/ND
  case 3:26-cv-00291-SJF document 1 filed 03/05/26"). Jury trial demanded.
- **Three counts, verified by reading them directly:**
  - **Count I — Unconstitutional Taking:** brought under 42 U.S.C. § 1983, citing *Knick v. Township of
    Scott*, 588 U.S. 180 (2019), alleging the county's moratorium ordinance effects a taking of POET's pore
    space (an interest in property) under the Fifth and Fourteenth Amendments without just compensation.
  - **Count II — Violation of Indiana Home Rule Act:** Ind. Code §§ 36-1-3-8(a)(7), 36-1-3-5(a) — the county
    lacks authority to regulate conduct a state agency (IDNR) already regulates.
  - **Count III — State Law Preemption:** Ind. Code § 14-39-2-5 et seq., 312 IAC 30 — the county's ordinance
    conflicts with and is preempted by Indiana's CCS-authorizing statute and IDNR's permitting framework.
- **Correction to the 09-05 note:** it described the theories as including "Fifth/Fourteenth Amendment
  takings/**due-process** claims." Reading the complaint directly, there is **no separate due-process count**
  — Count I is a takings claim only (it invokes the Fourteenth Amendment solely as the vehicle for applying
  the Fifth Amendment's Takings Clause to a county, per standard incorporation doctrine, not as an independent
  due-process theory). Minor correction, doesn't change the substance, but "takings/due-process" overstated it
  slightly.
- **Status:** no ruling found via WebSearch as of tonight (Sept 7, 2026) — consistent with "recently filed,
  still pending."

### 2c. California — Committee for a Better Shafter v. County of Kern — primary source obtained (the actual petition), exact date/case number now confirmed

Center for Biological Diversity (one of the petitioners) hosts the actual filed petition; downloaded directly
and extracted 3 pages with `pypdf` (42-page document total, first few pages sufficient to confirm caption and
filing stamp). Confirms:

- **Case No. BCV-24-104003**, Superior Court of California, County of Kern. **Filed 11/20/2024, 3:24 PM**
  (electronic filing stamp on the document itself, deputy clerk Alexandra Valles) — the 09-05 note had this as
  "~Nov. 2024"; now exact.
- **Petitioners:** Committee for a Better Shafter, Delano Guardians, Comité Progreso de Lamont, Central
  California Environmental Justice Network, Sierra Club, Center for Biological Diversity.
- **Respondents:** County of Kern, Board of Supervisors of the County of Kern.
- **Real Party in Interest:** California Resources Corporation.
- **Claims:** Verified Petition for Writ of Mandate and Complaint for Injunctive Relief under Code Civ. Proc.
  §§ 1085, 1094.5 and Pub. Resources Code § 21000 et seq. (CEQA) — matches the 09-05 note's characterization.
- Cross-checked against the Climate Litigation Database's case tracker (climatecasechart.com), which
  independently lists the same case number, court, and filing date. **Status: active, no ruling or hearing
  date found in either source.**

**Bottom line on all three:** all three 09-05 leads hold up. HB7's failure and case identity for both lawsuits
are now primary-source-confirmed (actual court filings, not summaries); only the LA vote tally remains
secondary-only due to a technical access limitation on the vote-detail page, not a substantive doubt.

---

## 3. National sweep

### Colorado Class VI primacy — unchanged, checked directly against EPA's own page

Fetched EPA's own Class VI primacy status page for Colorado directly
(epa.gov/uic/proposed-rulemaking-colorado-underground-injection-control-class-vi-primacy). Confirms: still
"Proposed Rulemaking," application submitted Oct. 7, 2025, comment period closed May 4, 2026, **no final rule
and no effective date yet** as of tonight. Matches the 09-05 note exactly — no change here.

### New finding, not previously in project notes — North Dakota pore-space "amalgamation" litigation

This surfaced during tonight's general sweep and is a genuinely significant addition: North Dakota (the
*first* state to get Class VI primacy, 2018) has an active, two-track legal fight over the **state-law
mechanism that lets regulators force non-consenting landowners into CO2 pore-space storage** — a fifth legal
theory for the project's comparative-litigation table, distinct from the standing (5th Cir./Deep South
Center), Louisiana eminent-domain, Indiana home-rule/preemption, and California CEQA theories already
catalogued.

**Background (older, for context):** In *Northwest Landowners Association v. State*, No. 20240298, the North
Dakota Supreme Court ruled **August 28, 2025** that plaintiffs had standing to challenge the CO2-storage
pore-space provisions of N.D.C.C. ch. 38-22 (though not other provisions), without yet reaching the merits.
Sourced from statecourtreport.org's case tracker, a nonpartisan legal-tracking site — I could not reach
ndcourts.gov directly (403 on a non-browser request, same pattern as CourtListener's rate-limiting in the
09-05 note) to pull the opinion itself.

**Two subsequent district-court merits rulings, both post-dating that standing decision:**

- ***Northwest Landowners Association & North Dakota Farm Bureau v. [State/Industrial Commission]*** —
  Northeast Judicial District, **Judge Anthony Swain Benson**, ruled **December 2, 2025**: found the
  amalgamation provision (the 60%-landowner-consent rule allowing the state to force the remainder into a CO2
  storage project) unconstitutional under the state constitution's takings clause — no compensation mechanism
  determined by jury trial, and no requirement that compensation be paid *before* the taking.
- ***Swenson v. North Dakota Industrial Commission*** — South Central Judicial District, **Judge Jackson
  Lofgren**, ruled **approximately March 9–10, 2026**: reached the same constitutional conclusion in a case
  specifically challenging Summit Carbon Solutions' Industrial Commission storage permits near Beulah, ND —
  and **voided those specific permits** as a result.
- **Current status (most recent secondary source found, KFGO, dated July 27, 2026):** both cases are now on
  appeal to the North Dakota Supreme Court. The same article reports legal-fee awards against the state —
  roughly $429,000 (Lofgren/Swenson case) and $278,000 (Benson/Northwest Landowners case), for a total
  potential state liability near $975,000 including an older 2022 fee award — and quotes the Attorney
  General's office confirming it is "challenging the attorney fees awards and appealing them as part of our
  broader appeal." No North Dakota Supreme Court ruling on this second appeal round was found as of tonight.

**Sourcing caveat:** this entire item is secondary-sourced tonight — I attempted ndcourts.gov directly and was
blocked (403), the same access pattern noted for CourtListener in the 09-05 note. It is, however, heavily
corroborated: eight independent outlets (North Dakota Monitor, Agweek, TSLN, KFGO, RBN Energy, a Yahoo/AP
wire pickup, KVRR, The Gazette) describe the same case names, judges, and dates consistently, with no
contradictions found across them. Treat as a strong lead, not a verified-and-ready citation — a follow-up pass
that successfully pulls the Benson and Lofgren opinions themselves (or the pending ND Supreme Court briefing)
would upgrade this to primary-verified.

**Why this matters for the paper:** if the project's comparative/national-litigation framing wants a
"landowner forced-participation without compensation" axis, this is the clearest example found so far —
and it's happening in the *original* Class VI primacy state, which is a notable frame (primacy doesn't
insulate CCS development from separate state-constitutional property fights).

### No other new developments found

No new state achieved Class VI primacy since 09-05 (still six: ND, WY, LA, WV, AZ, TX). No new challenge to
Texas's or Arizona's primacy grants found. The Save My Louisiana eminent-domain suit (19th JDC, filed Nov.
2025) remains active with no ruling, per a fresh WebSearch check tonight — unchanged from 09-05.

---

## What's still open / worth Britton's attention

- **WV oral argument: now confirmed for October 30, 2026** — this is a strong, citable, primary-sourced fact
  as of tonight (the court's own calendar PDF, freshly posted). Recommend flagging this date for a manuscript
  update and, if timing allows, watching for the decision afterward.
- **LA HB7, IN POET v. Wabash, CA Committee for a Better Shafter — all three now primary-source-verified**
  against the actual bill-tracking page and the actual filed court documents respectively. Ready to cite with
  confidence; only the LA HB7 committee vote tally (12-7) remains secondary-only due to a page-access
  limitation, not a substantive doubt.
- **New: North Dakota pore-space amalgamation litigation (Northwest Landowners/Farm Bureau v. State; Swenson
  v. ND Industrial Commission)** — strong secondary corroboration (8 outlets), not yet primary-verified
  (ndcourts.gov blocked tonight, same as CourtListener was on 09-05). Worth a dedicated pass to pull the
  actual Benson and Lofgren opinions, and to check whether the ND Supreme Court has ruled on the pending
  appeal by the time of the next research session. A fifth comparative legal theory (forced pore-space
  participation without prior compensation) if Britton wants to expand that table.
- **Tooling note for next pass:** PDF extraction tooling isn't preinstalled in this environment — `pip install
  pypdf` plus `pip install --force-reinstall cffi` was needed to get a working extractor tonight. `pdftotext`/
  poppler-utils (used successfully in the 09-05 note) was not available this session; worth checking what's
  present at the start of the next pass rather than assuming either tool is there.
- **ndcourts.gov and courtlistener.com/northdakotamonitor.com direct access remains blocked** (403s) from
  this environment for non-browser requests — a recurring limitation across multiple nights now. If Britton
  has PACER or a subscription-based legal database, that would resolve both the ND primary-source gap and any
  future WV docket-detail needs faster than this environment can.
- **Unchanged, explicitly not touched tonight per instructions:** McCauley volume-number issue, docx
  "51 vs. 58" reconciliation, Track A/B/C, the date-convention pick, and any theme/Phase-3/design-lock
  decisions all remain Britton's, untouched.
