# 2026-09-05 — Sabey case number found, Dougherty resolution full text obtained, MO/NV access still blocked (confirmed structural), national sweep

## What this is
Direct continuation of 09-04's work, five assigned open items. All AI-conducted
research (WebSearch + WebFetch + direct curl/PDF-extraction attempts), disclosed
per repo convention. No fabricated citations — every claim below is sourced to a
specific fetch or search, and one instance where a WebSearch summary appears to
have invented a case number is flagged explicitly as unverified/likely fabricated
rather than carried forward. Every gap is stated as a gap. Read-only pass — no
git commands run, no theme/design decisions made (Phase 3 stays human-only for
this project, per standing rule).

---

## 1. Sabey/Decatur (Indianapolis) — Aug 20 hearing outcome: still no outcome found, but the actual case number and petition are now in hand

Could not find any news coverage, in any outlet, of what happened at or after
the Aug. 20, 2026 virtual hearing. Searched multiple phrasings ("ruling,"
"decision," "judge," "denied," "granted," "upheld") combined with Decatur
Township/Sabey — nothing from after Aug 20 turned up. **This remains an
honest, unresolved gap**, not a search failure — the same conclusion 09-04
reached. Do not infer an outcome.

What *did* move: found and direct-fetched the actual court filing (PDF,
hosted by WTHR, not previously in the corpus):
https://interactive.wthr.com/pdfs/2026_4_17_Verified_Petition_for_Judicial_Review_and_Complaint_for_DJ.pdf

(WebFetch couldn't read the PDF as prose — same binary-stream issue as other
PDFs — so it was extracted directly with `pdfminer.six` after installing it
and a missing `cffi` dependency locally.) Confirmed directly from the
document text:
- **Cause No. 49D05-2604-PL-021609**, Marion Superior Court 5, Marion County,
  Indiana. Filed 4/17/2026 4:52 PM (e-filing clerk stamp visible in the text).
- Full case caption: **Decatur Township Civic Council Inc, Timothy W.
  McWhirter and Janice F. McWhirter (as Trustees), Charles E. Young II,
  Leslie Young, Loueva Gay Young (as Trustee), Patricia C. Andrews, and
  Russell H. Glashan v. Indianapolis Metropolitan Development Commission,
  City-County Council of Indianapolis, Marion County Indiana, Sabey Data
  Center Properties LLC, SCP Decatur Technology Park LLC, and Strategic
  Capital Partners LLC.**
- Relief sought: a judgment declaring invalid, void, and unenforceable the
  MDC's March 18, 2026 final decisions (variances in **MDC Case No.
  2025-CVR-856 (Amended)** and modification of commitments in **MDC Case No.
  2025-CAP-856**), plus the City-County Council's approval of **Rezoning
  Ordinance No. 3, 2021** under MDC Case Nos. 2020-CZN-834/2020-CVR-834.
  Grounds: violation of due process rights under Indiana Constitution Article
  I, Section 12, among other claims (document truncated in the extract at
  this point — the full 2026-04-17 petition is longer than what was quoted
  here; worth a full read if Britton wants the complete claim list).

This is a genuine primary-source upgrade — Britton now has an exact,
citable cause number and the original petition text, not just news paraphrase.
It does not resolve the Aug 20 hearing outcome, which is still unreported
anywhere found.

**Attempted but not completed:** Indiana's public case-search portal,
mycase.in.gov, returned HTTP 200 (unlike Missouri/Louisville — not
structurally blocked), but it is a JavaScript search application, not a
GET-addressable case lookup — pulling the docket sheet for 49D05-2604-PL-021609
would need an interactive/form-based session this environment doesn't have.
Flagging this as a possible next step for a human with a browser, not a
repeat-tool-block like MO/NV/Louisville.

Also newly found, same search: a September 16, 2026 Metropolitan Development
Commission meeting to discuss Sabey's incentive package is confirmed again
across multiple sources — consistent with 09-04's note, just corroborated.

---

## 2. MO/NV — alternate access routes tried, both still blocked; this is now confirmed structural, not tool-specific

### Missouri (Case.net / courts.mo.gov)
Tried, beyond WebFetch: direct `curl` (plain and with a spoofed desktop
User-Agent) — both returned **HTTP 403** on `courts.mo.gov` and
`courts.mo.gov/cnet/welcome.do`. Tried the Wayback Machine's availability API
(`archive.org/wayback/available`) — the courts.mo.gov homepage *has* an
archived snapshot (Aug 11, 2026), but no snapshot exists for any Case.net
search-results page (Case.net results aren't static/crawlable pages, so this
was always unlikely to work). **Conclusion: this is a WAF/bot-detection block
at the network level, unaffected by User-Agent spoofing — not something this
tool environment can route around.** No case/cause number obtained for the
St. Louis Midtown data center suit (Board of Adjustment / David Lambiaso).

New detail from a fresh source today (STLPR, direct-fetched): the two named
plaintiffs are **Daniel Pate and Kerry McCullen** — not previously in the
corpus. STLPR's own article does not give a case number either, and stltoday's
coverage was inaccessible behind a paywall redirect (TollBit token wall).

**Caution — a likely-fabricated detail to explicitly NOT carry forward:** one
WebSearch summary today asserted a case number "26SL-CC03024" and described it
as *"State of Missouri ex rel. Wake Up Jeffco, LLC v. City of Festus."* This
number does not appear in any of the underlying search result titles/links
returned, and Wake Up Jeffco's actual lawsuit (Festus, filed April 2026 — a
different, already-known case in this corpus) is well-documented in multiple
real articles with no case number cited anywhere in them. Treat "26SL-CC03024"
as **unverified and probably invented by the search tool's summarizer** — do
not cite it or attribute it to either the Festus or the St. Louis Midtown
case.

### Nevada (Washoe County / DocumentCloud)
Confirmed the DocumentCloud block is a Cloudflare WAF challenge, not
something specific to WebFetch: direct `curl` to the document page, to
`api.www.documentcloud.org`, and to `assets.documentcloud.org` page-text
endpoints all returned the same **Cloudflare "Attention Required" 403** block
page. Tried `r.jina.ai` as a proxy fetcher (per tonight's instructions) —
it refused with **401 "blocked from performing anonymous queries due to bad
IP reputation"** — this environment's proxy IP is itself flagged by that
service, so that route is closed too, independent of DocumentCloud. Checked
Wayback Machine's availability API for the specific document URL — no
snapshot exists.

**However, real progress on identifying the case itself:** cross-referencing
today's search results confirms the DocumentCloud complaint (filename-dated
26.07.24, i.e. July 24, 2026) is almost certainly **NV Energy v. Tract**,
filed in Washoe County's Second Judicial District Court on Friday, July 28,
2026 (a "Complaint for Declaratory and Injunctive Relief" matches the
DocumentCloud title exactly) — **Judge Scott Freeman is presiding**, per The
Nevada Independent's own reporting (direct-fetched today). This is a new,
useful detail (the presiding judge's name) not in the 09-03/09-04 notes. Also
confirmed via CourtListener's API that this is a **state** case (Nevada
Second Judicial District, not federal) — CourtListener/PACER has no coverage
of it by design, so that specific route in tonight's instructions doesn't
apply here (CourtListener only indexes federal courts and some state
appellate courts with participating clerks; Washoe County District Court is
neither). Still no case/docket number found for the state case itself, and
the complaint's actual text (it is described in reporting as containing
"significant redactions" and having been "filed under seal" in part) remains
unread.

**Bottom line on both:** this looks like a genuinely systematic limitation of
this research environment against government/court web infrastructure
(WAF/bot-detection blocking a shared proxy IP range), confirmed now across
Missouri, Nevada/DocumentCloud, and Louisville over multiple nights with
multiple bypass attempts (UA spoofing, curl, Wayback, a third-party proxy
service). Recommend Britton treat this as a known ceiling for autonomous runs,
not a nightly-retry item, unless a different access method becomes available
(e.g., PACER credentials for federal matters, or Britton pulling a document
himself via a normal browser).

---

## 3. Georgia (Dougherty County) moratorium extension — full resolution text now in hand; no separate "resolution number" exists to find

Located Dougherty County's Municode Meetings portal
(meetings.municode.com, cid=DOUGHERTY) and downloaded the actual **agenda
packet PDF** for the **Special Called Meeting, August 31, 2026** — a genuine
primary government document (5.7MB, extracted via `pdfminer.six` since
WebFetch cannot read raw PDF binary). Full resolution text confirmed:

> **"A RESOLUTION TO IMPOSE, CONTINUE, AND EXTEND THE TEMPORARY REVIEW PERIOD
> AND MORATORIUM ON THE ESTABLISHMENT OF NEW LARGE SCALE DATA CENTERS IN
> DOUGHERTY COUNTY UP TO 180 DAYS; REPEALING RESOLUTIONS OR PARTS OF
> RESOLUTIONS IN CONFLICT HEREWITH; AND FOR OTHER PURPOSES."**

Key facts from the resolution's own text:
- It extends and continues the moratorium originally imposed by a **July 20,
  2026** resolution ("A RESOLUTION TO INITIATE A COUNTY-WIDE REVIEW OF
  LARGE-SCALE DATA CENTER DEVELOPMENT...ESTABLISHING A FORTY-FIVE (45) DAY
  ADMINISTRATIVE REVIEW PERIOD").
- The extension runs **180 days, through and including Saturday, February
  27, 2027, at 11:59 p.m.**, unless ended earlier by Board action or by the
  Albany-Dougherty Zoning Ordinance amendments taking effect first.
- Dated **"This the 31st day of August, 2026,"** signed by **Lorenzo L.
  Heard, Chairman**, attested by the County Clerk.
- Effective immediately upon adoption; repeals any conflicting prior
  resolutions.

**Gap that turns out not to be closeable, not just unfound:** searched the
full extracted text of the packet for any "Resolution No. ___" identifier or
docket-style number — **none exists in the document**. Dougherty County
appears to identify its resolutions by title and adoption date only, not by a
separate sequential resolution number, at least in this packet's format.
This is a meaningfully different finding from "the number is still missing" —
it's now "there is no such number to find in this county's own document," at
least not in the version circulated to commissioners. If Britton needs a
different kind of identifier (e.g., an internal clerk's filing number), it
would have to come from the county clerk's office directly, not from the
public packet.

**Still not resolved from a primary source:** the actual roll-call vote count
on Aug 31. The meeting's minutes were listed as "not yet posted" on the
Municode portal as of tonight. WALB and dmnews's "unanimous" framing (not
re-verified tonight beyond what 09-04 already had) remains news-sourced only.

---

## 4. Louisville — Sept 15 Metro Council check: no movement, as expected

Confirmed via fresh search tonight: nothing has moved up. The Sept 3
Planning Commission 5-3 vote (already confirmed 09-04) is still the latest
event; the Planning and Zoning Committee meeting remains scheduled for
**September 15, 2026, 1:00 PM, City Hall**, per LPM's Sept 3 report and
corroborating whas11/wdrb coverage found tonight. No new primary-source
government document became available (louisvilleky.gov's data-center page
was not re-tested tonight since 09-04 already established the structural
403 block there and nothing suggests that's changed).

---

## 5. General national sweep — several new, real leads found since 09-04

All WebSearch-summary confidence unless noted; flagging for a future
direct-fetch/verification pass rather than treating any of these as
corpus-ready yet.

- **Imperial County, CA — CEQA ruling against a data center, Sept 1, 2026.**
  Direct-fetched KPBS's report: Imperial County Superior Court Judge L.
  Brooks Anderholt issued a **tentative ruling** that the county
  "prejudicially abused its discretion" approving a lot merger for Imperial
  Valley Computer Manufacturing's 950,000-sq-ft data center complex without
  the CEQA environmental review the whole project required — the county had
  approved it "incrementally" (grading, lot merger, road vacation) rather
  than as a unified project. This is a new state (California) for the
  corpus and a notable legal theory (environmental-review segmentation) not
  seen in the other states' litigation so far. Tentative only — worth a
  follow-up for the final order.

- **Middlesex Township, PA ("PAX-1") — a second, distinct Pennsylvania
  legal fight from the Shapiro EO already in the corpus.** A $15B Carlisle
  Development Partners project; opponents ("Stop PAX-1") got Cumberland
  County Judge Matthew P. Smith to issue a show-cause order requiring the
  developer and township to justify why construction shouldn't stop pending
  their suit, with oral arguments set for **Sept. 18, 2026**. WebSearch
  summary only — the direct source (ABC27) returned HTTP 403 on WebFetch
  tonight; cumberlink.com carried related coverage not yet fetched directly.

- **Salem Township, Luzerne County, PA — pro se Sunshine Act win, Aug 26,
  2026.** Direct-fetched (Just The News/Center Square): eight residents
  without a lawyer won a verbal ruling from Luzerne County Judge Lesa Gelb
  that the township violated Pennsylvania's open-meetings law by locking
  attendees out of a data-center-ordinance meeting. Names an AWS data center
  (under construction) and a QTS Data Centers project as the ones at issue —
  both were reportedly on Gov. Shapiro's state "fast track" permit list
  before being removed earlier in August 2026 amid public opposition. This
  connects directly to the EO already in the corpus (the EO itself removed
  data centers from that fast-track program statewide) — a good candidate
  for tying two PA leads together in the write-up later, Britton's call.

- **DeKalb County, GA — a moratorium being challenged from the *pro-
  development* side, filed Aug 5, 2026.** Direct-fetched decaturish.com:
  Shadowbox Studios and Henrico 183 sued DeKalb County (Superior Court)
  arguing the county's data-center moratorium (in effect since July 8, 2025)
  is invalid as applied to their already-in-motion $30M+, 651 MW project,
  seeking a declaration, permission to build, and "just compensation" for an
  alleged ~$200M property-value diminishment. Useful as a counter-example:
  most of this corpus's litigation is opposition-side; this one is a
  developer suing *to overturn* a moratorium, structurally similar to the
  Nashville DC BLOX suit already in the corpus.

- **Spartanburg/Chester County, SC — a live PSC docket plus litigation,
  new state for the corpus.** WebSearch-summary only tonight (direct fetches
  to scdailygazette.com and wspa.com both returned HTTP 403). Picture pieced
  together from search snippets: Valara Holdings' ~$2.8B, 900,000+ sq ft data
  center campus in Spartanburg County is contested on two fronts — (1) the
  Southern Environmental Law Center, representing residents, filed suit July
  6, 2026 in the Seventh Judicial Circuit Court and sought a preliminary
  injunction over the developer's use of a "minor land development" permit
  designation; (2) South Carolina's Public Service Commission ruled **Aug 27,
  2026** that the facility is not subject to public-utility power-plant rules
  because it won't export power to the grid. Separately, **Chester County**
  (adjacent, also tied to the Valara project per some coverage) passed its
  own 6-month data center moratorium at a July 20, 2026 meeting. This is a
  strong utility-PSC-docket lead matching exactly the kind of source type
  the project wants more of — recommend a dedicated primary-source pass on
  this one on a future night (PSC docket number, the actual circuit court
  filing).

- **North Carolina** — a North State Journal piece (WebFetch blocked, HTTP
  403) apparently reports the state's moratorium count still climbing (was
  already tracked heavily in 08-29/08-30 notes) — nothing new enough
  extracted tonight to add facts, flagging only that the count-rising
  framing continues into September.

- **Prince William County, VA "Digital Gateway" rezoning overturned** — found
  via search, but this ruling is dated **August 7, 2025**, over a year
  before tonight's window. Not a "since 09-04" development — flagging only
  in case this project (which per CLAUDE.md already treats VA as one of its
  national-scan states) hasn't logged it yet; Britton/prior notes should be
  checked before assuming it's new information.

---

## For Britton — plain summary of what moved and what didn't

- **Sabey/Decatur:** the Aug 20 hearing's outcome is still not reported
  anywhere — genuinely unresolved, not a search gap. But the actual court
  case is now precisely identified: **Cause No. 49D05-2604-PL-021609, Marion
  Superior Court 5**, and the original petition PDF is in hand with full
  party names and the specific MDC case numbers being challenged.
- **MO/NV:** tried every reasonable alternate route tonight (direct curl,
  User-Agent spoofing, Wayback Machine, a third-party proxy service) — both
  are still blocked, and this now looks like a structural wall (WAF/bot
  detection against this environment's proxy IP), not a one-off failure or
  something specific to WebFetch. Recommend treating it as a known ceiling
  rather than a nightly retry target. Also: caught and flagged (not carried
  forward) a case number a WebSearch summary appears to have invented for the
  Missouri suit — worth knowing that AI search summaries can fabricate
  specific identifiers even when the underlying links don't support them.
- **Georgia:** got the actual county resolution's full text — it turns out
  there's no separate "resolution number" in the document to find; it's
  identified by title and date only. The Aug 31 vote count is still
  news-sourced, not government-document-confirmed (minutes not yet posted).
- **Louisville:** no movement, as expected — Sept 15 committee meeting is
  still the next real date.
- **National sweep:** several solid new leads (Imperial County CA CEQA
  ruling, a second PA fight at Middlesex Township/PAX-1, a PA Sunshine Act
  citizen win tied to the same fast-track list as the EO already in the
  corpus, a developer-side suit against DeKalb County's moratorium, and a
  South Carolina PSC docket + litigation combo) — all at WebSearch-summary or
  partial-direct-fetch confidence, none corpus-verified yet. The SC lead in
  particular looks worth a dedicated pass since it's exactly the utility-PSC
  angle the project wants more of nationally.
