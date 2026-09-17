# 2026-09-17 — LPSC's Aug 12 order found as a real primary document, Virginia Digital Gateway date conflict resolved, xAI docket recheck, Tier 2 sweep corrections

## What this is

Nightly follow-up to `2026-09-15-xai-docket-recheck-lpsc-evest-confirmed-commission-ruling-found-tier2-sweep.md`,
which left two explicit open items: (1) the Aug 12, 2026 LPSC Commission vote on the Meta
subpoena fight was only sourced to two news outlets, not the Commission's own order/
minutes/transcript; (2) a genuine date conflict across sources on Virginia's "Digital
Gateway" ruling (Aug 2025 vs March/July 2026) needed a primary court-record check. Both
are resolved below with actual primary documents, not just better search summaries. Also
rechecked the xAI/NAACP docket and did a further Tier 2 pass, which surfaced two real
corrections to how 09-15 characterized the Utah and Clinton County items.

## 1. NAACP v. X.AI Corp. (3:26-cv-00074, N.D. Miss.) — still no new entry, but the RECAP mirror finally refreshed

Re-fetched the docket directly (`curl` with a browser User-Agent, same documented
workaround as the last several nights):

- **Highest docket entry: still 122** — read directly again, byte-identical to the last
  four nights' reads (DOJ's Sept. 8, 2026 reply brief). **No entry 123.**
- **RECAP "Last Updated" timestamp: now Sept. 16, 2026, 4:59 p.m.** — this is new. The
  09-15 note flagged this field as stuck at Sept. 11, 2026, 2:57 p.m. for four consecutive
  nights (a stale mirror, not necessarily a quiet case). Tonight it has moved forward five
  days — meaning a RECAP user actually pulled a fresh copy from PACER as of yesterday
  afternoon, **and that fresh pull still shows entry 122 as the highest entry.** This is a
  meaningfully stronger form of "no ruling yet" than the last four nights' checks: it's no
  longer just "the docket hasn't been re-checked," it's "the docket was re-checked
  yesterday and nothing new is there."
- **Fresh WebSearch cross-check tonight** for any ruling on the DOJ intervention/dismissal
  motion, or any other September development, found nothing beyond what's already in the
  corpus (Feb 13 notice, April complaint, May PI motion, June 12 PI denial/DOJ motion to
  intervene-dismiss, Aug 24 evidentiary hearing).

**Bottom line for Britton: still no ruling, and this is now a better-grounded "no ruling"
than the last several nights — the docket mirror itself refreshed and confirmed it, not
just gone stale.**

## 2. LPSC Docket U-37882 — the Aug 12, 2026 Commission vote, now a confirmed primary-source finding

**This closes the open item from 09-15.** The prior note searched the LPSC's document
*portal* (`lpscpubvalence.lpsc.louisiana.gov`) and couldn't locate the order there. The
fix tonight: the Commission's monthly **Business & Executive Session minutes, agenda, and
full court-reporter transcript** live on the LPSC's main public site
(`lpsc.louisiana.gov/docs/minutes/`, `/docs/agenda/`, `/docs/transcripts/`), not the
document-portal search that was tried before — a different part of the same website.
Tonight pulled all three directly:

- `https://lpsc.louisiana.gov/docs/minutes/August_12_2026_Minutes.pdf` (9 pages)
- `https://lpsc.louisiana.gov/docs/agenda/Aug_12_2026_Agenda.pdf` (5 pages)
- `https://lpsc.louisiana.gov/docs/transcripts/August-12-2026-BE.pdf` (138 pages, full
  court-reporter transcript of the entire Aug 12, 2026 Business & Executive Session,
  Baton Rouge)

All three are clean, directly-extractable text (no OCR/font-encoding issues this time).

**What the minutes say, verbatim (Exhibit 20, Docket U-37882):**

> After discussion, on motion of Vice Chairman Coussan, seconded by Chairman Skrmetta,
> with Commissioner Francis concurring, Commissioner Lewis opposing, and Commissioner
> Campbell absent, the Commission voted to reverse the Tribunal's ruling and vacate the
> subpoena, rendering the motion to quash moot. The motion passed 3:1.

This **confirms** the 3-1 vote and Lewis's dissent from the 09-15 note's two news sources,
now from the Commission's own record, and **refines the legal characterization**: the
09-15 note (following WRKF/American Press) framed this as "the Commission voted to reject
an ALJ recommendation that would have made Meta produce documents." The primary record is
more precise: the item before the Commission was **Meta's Motion for Immediate Review of
the ALJ's Aug. 4, 2026 ruling** (which had *denied* Meta's Motion to Quash, i.e., left the
subpoena standing). The Commission's actual action was to **reverse that ALJ ruling and
vacate the subpoena outright**, which mooted Meta's own motion to quash (nothing left to
quash once the subpoena no longer exists). Net practical effect for the paper is the same
as 09-15 already had it — Meta does not have to produce the subpoenaed
investment/job-creation/load-demand documents — but the precise procedural posture is now
right, from the primary source, not inferred from press paraphrase.

**New granular detail not in any prior note**, from the transcript (pp. 9-14): Chairman
Skrmetta initially **moved to defer this item to the September session**; Commissioner
Lewis objected to the deferral; after a back-and-forth, Skrmetta withdrew his own deferral
motion, and Vice Chairman Coussan then made the substitute motion actually voted on. The
exact language of that motion, read into the record by Deputy Executive Counsel Lauren
Evans: *"I move to reverse the Tribunal's ruling and vacate the subpoena, rendering the
Motion to Quash moot."*

**A real correction on the Lewis quote's context.** The 09-15 note (via WRKF) attributed
this quote to Lewis as his dissent statement on the substantive vote:

> "We have found a way ... to find every excuse to not do something when it favors
> Entergy and Meta ..."

The transcript (p. 10) confirms this is a **verbatim, accurate quote** — but it was said
**during the deferral debate**, i.e., Lewis's argument for why the Commission should not
punt the vote to September, not a statement made after the substantive 3-1 vote itself.
He was still on the losing side of the final vote and did still oppose the outcome — this
isn't a case of the quote being fabricated or wrongly attributed to the wrong person — but
if this goes into the manuscript as "Lewis's dissent statement," the more accurate framing
is "Lewis, arguing against delaying the vote, said ..." rather than implying it was said
in explanation of his no-vote on the merits. Small but real precision issue worth fixing
before it's quoted formally.

**Independent third confirmation of "Evest."** The transcript (p. 5) has LPSC counsel
Kathryn Bowman reading the docket into the record aloud: *"Entergy sought the Commission's
approval to add approximately 5,200 megawatts of generation ... to serve Evest ... Evest
is locating a large hyperscale data center in Richland Parish, adjacent to the facility
approved in Commission Order Number U-37425."* This is a third, independent primary
confirmation of the "Evest LLC" name (after the two filings read on 09-15), from the
Commission's own spoken record — fully safe to use now.

**One correction to a Tier 1 figure:** the transcript states the generation addition as
**"approximately 5,200 megawatts,"** slightly different from the "5,278 MW" figure the
09-13 note pulled from the garbled `pdftotext` read of the referral PDF. 5,200 is a
rounded verbal figure from oral argument; 5,278 is from the written application itself —
both are legitimate, but if the manuscript needs one precise figure, the written
application's 5,278 MW is the more authoritative number; the transcript's "approximately
5,200" is consistent with it, not conflicting.

**What's still open on this docket:** per both the minutes and the docket's document list
(pulled fresh tonight — see method note below), there is a **second, separate escalation
still pending**: Meta's and Entergy's own Motions for Immediate Review of the ALJ's Aug 4,
2026 ruling (the one that had denied Meta's Motion to Quash) were filed Aug 11-13, 2026,
and referred to the Commissioners again on **Aug 26, 2026** — LPSC counsel confirmed on
the record (transcript p. 12) that this second question "is not ripe" and is scheduled for
**the September Business & Executive Session**, not yet decided as of Aug 12. Worth a
follow-up check once a September LPSC minutes/agenda file would plausibly exist (the
Commission's regular monthly session; no September date was located or checked tonight —
next session's exact date wasn't confirmed).

**Tooling note (useful beyond this file):** the LPSC document *portal*
(`lpscpubvalence.lpsc.louisiana.gov`) has an unauthenticated JSON API worth knowing about
for future primary-source pulls on this docket family: `POST
https://lpscpubvalence.lpsc.louisiana.gov/portal/PSC/Docket_Documents` with form data
`docketId=<id>&page=1&pageSize=200` (the `docketId` for U-37882 is `32728`, found via the
portal's `DocketDetails?docketId=32728` page) returns the full, clean list of every filed
document in a docket — filer, date, description, and direct `ViewFile?fileId=...` links —
in one call, no login needed. This is much more reliable than the portal's own rendered
search UI and is how tonight confirmed there was no separate "Commission order" document
filed into the docket itself on Aug 12 (the vote lives in the B&E session minutes/
transcript, a separate document series, not a docket filing).

## 3. Virginia "Digital Gateway" date conflict — RESOLVED, not actually a conflict

Pulled the actual Court of Appeals of Virginia opinion directly from the court's own site
(`vacourts.gov/static/opinions/opncavwp/1584254.pdf`, a real, clean 47-page PDF) plus
supporting news for the trial-court dates. **The "Aug 2025 vs March/July 2026" conflict in
the 09-15 note was three different, all-real dates for three different procedural steps in
the same litigation, not a factual contradiction.** Full resolved timeline, primary-source
where noted:

- **June 16-23, 2025** — five-day bench trial, Circuit Court of Prince William County,
  Judge Kimberly A. Irving presiding (consolidated case, CL24-375).
- **August 7, 2025** — Judge Irving's letter opinion, finding the three rezoning
  ordinances (23-57, 23-58, 23-59) **void ab initio** for defective public-hearing
  advertising (news-sourced date — Northern Virginia Mag, Aug. 11, 2025 — not yet
  independently checked against a court filing date-stamp, but this is the "August 2025"
  date prior notes had).
- **September 15, 2025** — the trial court's **final order** made effective (this date is
  a direct primary-source read, straight from the Court of Appeals' own opinion text:
  "The trial court dismissed Counts II through VII without prejudice. The final order was
  made effective September 15, 2025."). This is a new, more precise date than either
  "August 2025" or the appellate dates — the letter opinion and the final order are ~5
  weeks apart, which is a normal and unremarkable gap, not a discrepancy.
- **November 17, 2025** — Court of Appeals partially stayed Judge Irving's judgment
  pending appeal (allowed everything except land-disturbance/construction to proceed).
- **March 31, 2026** — **Court of Appeals of Virginia published consolidated opinion**
  (Record Nos. 1590-25-4, 1584-25-4, 1592-25-4, and 2025-24-4; Judges Beales, Raphael, and
  Bernhard; opinion by Judge Stuart A. Raphael), read directly from the primary PDF.
  Affirms the void-ab-initio ruling on the three Oak Valley/H&H/GW Acquisition appeals;
  separately reverses in the Burke plaintiffs' favor on a related demurrer question
  (Record No. 2025-24-4). News coverage reporting this as a "March 2026" or "April 1,
  2026" ruling is consistent — the opinion is dated the 31st, a Tuesday, and most outlets
  ran it the next day.
- **April 14, 2026** — Prince William County's Board voted not to further appeal to the
  Virginia Supreme Court (news-sourced).
- **April 29, 2026** — Compass Datacenters (the other co-defendant developer) also
  declined to appeal further (news-sourced).
- **April 30, 2026** — QTS (through its affiliate GW Acquisition Co.) filed a petition for
  appeal to the Supreme Court of Virginia (news-sourced; a copy of this actual petition is
  hosted publicly at `protectpwc.org` if a primary read is wanted later).
- **July 2, 2026** — QTS withdrew that Supreme Court petition, "officially" ending the
  project (news-sourced, Virginia Business). This is the "July 2026" date the 09-15 note
  flagged as conflicting — it's real, but it's the *Supreme Court appeal being dropped*,
  a different and later step than the Court of Appeals ruling in March.

**So: "August 2025" = the trial court's original void-ab-initio ruling. "March 2026" =
the Court of Appeals affirming it. "July 2026" = the developer abandoning its last-resort
Supreme Court appeal.** All three are correct references to different points in one
continuous case; the appearance of "conflict" in the 09-15 note came from secondary
sources citing different stages without saying which. Safe to use all three now, cited to
the correct stage.

**One more thing worth flagging so it doesn't get conflated:** there is a *separate*,
smaller Prince William data-center rezoning case — **Caparoula v. Board of County
Supervisors of Prince William County**, Record No. 1137-24-4, an **unpublished** Court of
Appeals memorandum opinion decided **September 16, 2025** (Judge Lisa M. Lorish), about a
different ~270-acre rezoning (Ordinance No. 23-52) and a different developer (Stanley
Martin Homes). Read directly (also pulled from vacourts.gov, a real 15-page PDF). This is
not the Digital Gateway case — don't cite its Sept. 16, 2025 date as if it were a fourth
Digital Gateway date. Flagging only so a future pass doesn't merge the two cases.

## 4. Tier 2 sweep — two real corrections, one negative finding, one non-finding

- **Utah (Stratos Project) — correction to the 09-15 note's framing of the "3,800+
  objections" figure.** 09-15 presented this as a fresh, currently-live number with "no
  ruling yet on the water-rights transfer itself." Tonight's deeper check found the fuller
  picture: the ~3,800-4,000 protests were filed against **Bar H Ranch's original March 25,
  2026 water-right change application** (1,900 acre-feet, agricultural→industrial); that
  application was **withdrawn May 5-7, 2026** after the record-breaking protest volume,
  which nullified those specific objections rather than having them ruled on. **A second,
  separate application** (a smaller change-of-use request tied to a gas-fired power plant)
  drew "hundreds" more protests and was **also withdrawn, May 27, 2026**. Bar H Ranch has
  said publicly it intends to refile "in a timely manner" with more supporting data — no
  refiling was found in tonight's search (most recent coverage located is from mid-May
  2026). **Net correction: the 3,800+ figure is real and citable, but it describes protest
  volume against an application that no longer exists (withdrawn, not ruled on), not a
  live pending application as 09-15's phrasing implied.** Worth stating precisely in the
  corpus: strong evidence of opposition scale, weak/no evidence yet of regulatory outcome.
- **Arizona — one genuinely new item.** Gov. Katie Hobbs publicly rejected AG Kris Mayes'
  statewide data-center moratorium call around Sept. 9, 2026 (azfamily.com), while noting
  she's already secured a three-year pause on the state's data-center tax credit and says
  she'll do more on accountability short of a full moratorium. A Senate Majority Caucus
  spokesperson separately dismissed Mayes' proposal as an "election-year distraction." Not
  in the 09-15 note (which only had the Aug. 31 Mayes call and a Sept. 11 water-framing
  pushback piece) — this is a real escalation showing the moratorium proposal is now
  splitting Arizona's own elected officials, not just facing outside pushback. Good,
  citable evidence that this is a genuine live political fight, not a one-sided narrative.
- **Georgia (Coweta County, Project Sail) — no change.** The Superior Court suit (filed
  ~May 2026) still appears pending; no September ruling or hearing news found tonight,
  consistent with 09-15.
- **Clinton County, IN — dug deeper into the pre-January-2026 history, confirmed no new
  2026 development, and traced the full three-stage backstory that earlier search hits
  had only shown pieces of.** Two search results tonight (a DataCenterDynamics headline
  about an "833-acre... rescinded" rezoning, and a KNS Radio/Clinton County Today "hearing
  set for September 2" story) looked, out of context, like they could be new. Checked
  carefully: both trace to the **same known 2025 saga**, not a new 2026 filing — the full
  sequence is (1) Logix Realty's original **833-acre, 300MW** proposal, filed with the
  **City of Frankfort** (general-business rezoning), scheduled for a July 23, **2025**
  City Plan Commission hearing, **withdrawn by the developer in July 2025** after fierce
  opposition (one search summary initially and incorrectly said "July 2026" — a second,
  more careful search using different terms confirmed **2025** against the primary
  timeline, since it necessarily precedes the county's Sept. 2025 hearing and Jan. 2026
  denial already in the corpus); (2) Logistix then pivoted to the **County** instead of
  the city, filing the ~714.55-acre "Data One" petition; (3) the Clinton County Area Plan
  Commission's Sept. 2, **2025** hearing (the "hearing set for September 2" story) ended
  4-0 "No Recommendation"; (4) the full County Commission denied it 3-0 on **Jan. 20,
  2026** — already in the corpus, with its 12-month refiling bar (through ~Jan. 2027)
  still in effect. **No genuinely new Clinton County item tonight** — but this closes a
  gap in the corpus's own backstory (the city-level 833-acre chapter before the
  county-level 714.55-acre chapter wasn't previously documented in these notes) and is a
  second reminder, after 09-15's near-miss, that headline-level search snippets about this
  saga keep surfacing pre-2026 material that reads as current.

## For Britton — plain summary

- **The LPSC's Aug 12 order is no longer a "news-only" citation.** Pulled the Commission's
  own minutes, agenda, and full 138-page hearing transcript directly from the LPSC's
  website tonight. They confirm the 3-1 vote and Commissioner Lewis's dissent exactly as
  the news reported, plus give the precise legal action (reversing the ALJ and vacating
  the subpoena outright, not just "rejecting a recommendation") and the verbatim Lewis
  quote — though that quote was made while arguing against delaying the vote, not as his
  statement after losing it, a small nuance worth getting right if it's quoted in the
  manuscript. This item is now safe to cite to a primary source.
- **The Virginia "Digital Gateway" date conflict wasn't actually a conflict** — it was
  three real dates for three real stages of the same case (Aug. 2025 trial court ruling,
  March 2026 Court of Appeals affirming it, July 2026 the developer dropping its last
  appeal). Pulled the actual Court of Appeals opinion to confirm this. All three dates are
  now safe to use, each labeled to the right stage.
- **One thing to walk back slightly:** the "3,800+ Utah water-rights objections" figure
  from the 09-15 note is real, but it was against an application that got withdrawn back
  in May, not one still awaiting a ruling — worth phrasing that more precisely if it goes
  in the manuscript, since "no ruling yet" undersold that the application in question no
  longer exists.
- **xAI/NAACP case: still nothing new**, but tonight's check is on firmer ground than the
  last several nights — the docket's own mirror finally refreshed (as of yesterday) and
  still shows no ruling, rather than just being stale.
- **Arizona's moratorium fight has a new development** (the governor publicly rejecting
  it) worth folding in if that section gets touched. **Georgia and Clinton County: no
  change**, though Clinton County's own pre-2026 backstory is now more completely
  documented here.
- No design/theme decisions touched — this is verification and primary-source work only,
  consistent with the design lock. No corpus files were edited; findings are recorded here
  for whoever next updates the Tier 1/Tier 2 corpus.
- Per this task's instructions, no git commit/push was made — the orchestrating session
  handles that.
