# 2026-09-07 — Five 09-05 leads verification pass, SC PSC docket directly confirmed, a second fabricated case number caught, Sabey/Louisville/MO-NV rechecked

## What this is
Direct continuation of 09-05's assigned five open leads, plus the standing
Sabey/Louisville/MO-NV checks and a light national sweep. All AI-conducted
research (WebSearch + WebFetch + direct curl + local `pdftotext` extraction on
fetched PDFs), disclosed per repo convention. Every claim below is sourced to
a specific fetch; two instances where a search-tool synthesis asserted a case
number not supported by the underlying documents are flagged explicitly and
NOT carried forward, per the README's standing warning about this exact
failure mode (caught once already 9/5 on a Missouri case number). Nothing
added to the actual corpus files — this is a verification/gathering pass
only, per this project's standing rule that corpus/design restructuring stays
Britton's call. Read-only otherwise; no git commands run.

---

## 1. Imperial County, CA — CEQA ruling: REAL, well-documented, still tentative; a second fabricated case number caught and rejected

Confirmed via two independent direct fetches (KPBS's Sept 1 report and
KESQ's Sept 1 report) plus corroborating WebSearch hits from ivpressonline,
Beyond Borders News, Courthouse News, thedesertreview, and datacenterknowledge.com:

- **Imperial County Superior Court Judge L. Brooks Anderholt** issued a
  **tentative decision Aug. 31, 2026** in a CEQA suit brought by the **City of
  Imperial and the Sierra Club** against **Imperial County**, over the
  county's approval of Imperial Valley Computer Manufacturing LLC's
  ~950,000-sq-ft, 330 MW "Hyperscale AI Data Center Project" (Aten/Clark Roads).
- Holding (direct quote via KPBS): "The court finds the county prejudicially
  abused its discretion by approving the lot merger without first completing
  the CEQA review required for the whole project." The county had treated
  grading, lot merger, road vacation, electrical, and water infrastructure as
  separate ministerial approvals rather than one project — a project-
  segmentation theory, not seen elsewhere in this corpus's litigation so far.
- Remedy as reported: the county must identify the whole project and prepare
  an EIR before further permits/construction. **Still tentative as of
  tonight** — both KPBS and KESQ describe a comment period; a "20 days after
  service of notice of entry" writ/judgment process was mentioned in one
  WebSearch synthesis (unconfirmed against a primary doc, flagged not
  verified). No finalization found as of 9/7.
- **Important complication for the write-up**: this is NOT the only Imperial
  County ruling in play. A **separate judge, Jeffrey B. Jones**, issued his
  own **Aug. 21 tentative ruling in a different case** — brought by the same
  developer, Imperial Valley Computer Manufacturing LLC, *against* the
  county — striking down the county's own data-center moratorium ordinances
  for failing to show a public-health/safety threat. So Imperial County
  currently has two parallel, opposite-valence tentative rulings: one
  favoring the opposition (Anderholt/CEQA), one favoring the developer
  (Jones/moratorium). Don't conflate them in the corpus — they're genuinely
  two different cases with two different judges and two different theories.
  Also found (not requested, background only): the same developer
  successfully used California's anti-SLAPP statute to get its own
  defamation suits against a resident, an advocacy group, and KPBS itself
  dismissed in July 2026 — relevant context if this becomes the CA anchor
  case (a developer that both sues critics and gets sued back).

**Caught and rejected — do not carry forward:** a WebSearch synthesis
confidently supplied **"Case No. ECU004457"** for the City of
Imperial/Sierra Club v. Imperial County suit. Direct-fetching the actual
underlying source it was drawing from (KPBS's original May 27, 2026 filing
article) shows **no case number anywhere in the article's text** — "filed in
Imperial County Superior Court" is as specific as the primary source gets.
This is the same fabrication pattern the README already flags from 9/5
(the Missouri "26SL-CC03024" number): treat "ECU004457" as unverified and
likely invented by the search tool's summarizer, not as a real citable case
number.

**Bottom line:** real, strong, corpus-ready material once Britton decides
whether/how CA fits the national design — but flag the case number as
missing/unconfirmed, not "ECU004457," and flag that there are two separate
Imperial County cases in play, not one.

---

## 2. Middlesex Township, PA ("PAX-1") — REAL, more active than 09-05 knew; ABC27 still hard-blocked

Corroborated across the Stop PAX-1 organization's own site (direct-fetched),
WITF (direct-fetched, Sept 3), and multiple WebSearch hits (ABC27, cumberlink,
fox43) that ABC27/cumberlink themselves remain unfetchable tonight (ABC27:
403 again; cumberlink: redirects to a TollBit paywall token-gate, confirmed
by direct fetch to return only an authorization-error page, not article
text — a different, harder wall than a normal 403).

Confirmed real (Stop PAX-1's own site, direct-fetched):
- Three separate legal challenges filed by the "Stop PAX-1" opposition group
  against **Carlisle Development Partners'** $15B "PAX-1" project (16
  buildings across three campuses, each with its own 450 MW substation) and
  **Middlesex Township**: (1) a spot-zoning challenge filed in county court
  **Aug. 6, 2026** (694 acres rezoned for one company); (2) a land-development-
  approvals challenge in county court; (3) a stormwater-permit appeal to the
  **PA Environmental Hearing Board**, filed **Aug. 13, 2026** (permit was
  reportedly written for 58 houses, not a hyperscale data center campus).
- Confirmed via WITF direct fetch (Sept 3): Middlesex Township supervisors
  **voted to approve the first phase of PAX-1** after 3 hours of public
  comment, with the group's Environmental Hearing Board matter set for a
  **first hearing Sept. 16**.
- Via WebSearch only (ABC27/cumberlink content, not directly fetchable):
  **Cumberland County Judge Matthew P. Smith** issued a **show-cause order**
  requiring Carlisle Development Partners and the township to justify why a
  construction stay shouldn't be granted, with **oral arguments set for Sept.
  18**. This is a separate proceeding from the Sept. 16 Environmental Hearing
  Board date, not a conflicting date for the same hearing — but the Sept. 18
  detail specifically remains WebSearch-summary-sourced only; I could not get
  a direct primary/news-outlet fetch to confirm it tonight, same as 09-05.

**Bottom line:** upgraded from 09-05 (which had this as WebSearch-summary
only) to partially direct-source-confirmed (the org's own site, WITF), with
one specific date (Sept. 18 show-cause hearing) still resting on
WebSearch-summary confidence only. Recommend a future pass try the PA
Environmental Hearing Board's own docket search directly for the stormwater
appeal, since that's a state administrative body that may not carry the
same paywall/WAF blocks as the news outlets.

---

## 3. Salem Township / Luzerne County, PA — Sunshine Act win: REAL and has since escalated into a live compliance fight

Direct-fetched Times Leader and Brushwood Media Network (a Center
Square/Just The News syndication partner), corroborating each other and the
09-05 note's original facts, plus adding real new developments:

- **Judge Lesa Gelb** (Luzerne County Court of Common Pleas, Wilkes-Barre)
  verbally ruled **Aug. 25, 2026** that the Salem Township Planning
  Commission violated PA's Sunshine Act at its meeting on the data-center
  zoning overlay (locked doors, "many people turned away" per the civil
  complaint filed by eight self-represented residents: Nate Eachus, Karla
  Puterbaugh, Anne Vinatier, Jason Oldenbuttel, Teri Barren, Gabby Malencore,
  Kenneth Fatula, John Oldenbuttel). Gelb ordered the commission to redo the
  meeting.
- **New since 09-05 — this did not stay resolved:** the commission held a
  second vote **Aug. 27** and approved the overlay again (2-1). On **Aug.
  31**, a reporter obtained the written copy of Gelb's order and found it had
  actually **stayed** action on the overlay — the township only learned the
  full contents of its own court order on **Sept. 1**. Township Solicitor
  Anthony McDonald: "We are taking that to mean it has been invalidated." The
  township has now rescheduled a **third vote for Sept. 24, 5:30 p.m., at
  Berwick Assembly of God church.**
- **Discrepancy worth flagging, not resolved:** Times Leader (direct-fetched)
  gives the original disputed meeting date as **July 13**; Brushwood Media
  Network (also direct-fetched) gives it as **July 23**. Both are otherwise
  consistent on every other fact (judge, plaintiffs, ruling date, outcome).
  Didn't find a way to adjudicate which date is correct tonight — flag for
  whoever eventually writes this up to re-check against the original civil
  complaint if precision on that date matters.
- Confirms the 09-05 note's context: Salem Township hosts an under-
  construction **Amazon** data center and a planned **QTS** data center, both
  reportedly on Gov. Shapiro's state "fast-track" list before being pulled
  in August — the same statewide fast-track program the EO already in this
  corpus addresses. Real candidate for tying the two PA leads together later.

**Bottom line:** real, now direct-source-confirmed, and meaningfully more
interesting than 09-05 knew — a citizen legal win that the township itself
apparently tried to route around before being caught, with a third public
vote now pending Sept. 24 (a genuine future event worth a follow-up check).

---

## 4. DeKalb County, GA — developer-side moratorium suit: REAL, direct-confirmed, with a concrete near-term date

Direct-fetched decaturish.com's original filing report and Atlanta News
First's Sept. 2 follow-up (WABE itself returned 403 tonight, unlike 09-05
where it was apparently accessible — inconsistent, not chasing further):

- **Shadowbox Studios and Henrico 183 v. DeKalb County**, filed **Aug. 5,
  2026** in **DeKalb County Superior Court**. Plaintiffs argue county
  planning officials told them (in emails/letters June 2023–Feb 2025) a data
  center would be permitted on their ~200-acre site (3600 International Park
  Drive, Ellenwood) as a "communication utility" or "warehouse" use, then the
  county's data-center moratorium (in effect since July 2025) blocked them
  after they'd invested over $30M. Seeking a declaration the moratorium is
  invalid, permission to build, "just compensation" for an alleged ~$200M
  property-value loss, and attorney's fees.
- **New since 09-05:** a parallel, more immediate track — the **DeKalb County
  Zoning Board of Appeals heard Shadowbox's separate appeal on Sept. 9,
  2026** of the board's prior denial of the data-center application (public
  comment period closed Sept. 3). Commissioner Ted Terry is separately
  pushing a third-party environmental-health study on data-center impacts.
  So there are now two live tracks (the Superior Court suit and the ZBA
  appeal) — worth distinguishing in any future write-up, since a ZBA reversal
  could moot part of the lawsuit's relief request.

**Bottom line:** real, well-sourced, corpus-ready as a developer-side
counter-example (structurally similar to the already-corpused Nashville DC
BLOX suit against that city's moratorium). No case number found in any
outlet fetched tonight.

---

## 5. South Carolina — Valara/Spartanburg PSC docket + Chester County moratorium: REAL, now GOVERNMENT-PRIMARY-SOURCE CONFIRMED — best-verified lead of the five

This is the strongest upgrade of the night. 09-05 had this at WebSearch-
summary-only confidence (direct fetches to scdailygazette.com and wspa.com
both still return 403 tonight, unchanged). Instead of retrying those, I
found and directly fetched the actual government primary sources:

- **PSC Docket No. 2026-158-E**, South Carolina Public Service Commission —
  confirmed directly from the **PSC's own docket detail page**
  (dms.psc.sc.gov/Web/Dockets/Detail/119739), fetched successfully tonight.
  Caption per the docket page itself: **"Concerned Citizens of Spartanburg
  County and Southern Alliance for Clean Energy, Complainants/Petitioners v.
  Valara Holdings, LLC, Defendant/Respondent."** Opened **June 19, 2026**,
  status **Open**, industry **Electric**.
- Also directly obtained and text-extracted (via `pdftotext`, not WebFetch,
  which can't read raw PDF binary) the actual filed petition from SELC's own
  site: **"Petition for Declaratory Order, Petition for Rule to Show Cause
  Order, Request for Expedited Relief,"** filed by Concerned Citizens of
  Spartanburg County and the Southern Alliance for Clean Energy, represented
  by SELC. Confirms the legal theory directly from the document: Valara's
  proposed 450 MW gas-fired power plant (to power its ~900,000+ sq ft data
  center at 4000 South Pine Street, Spartanburg) is a "major utility
  facility" under SC's Utility Facility Siting and Environmental Protection
  Act and needs a CECPCN (certificate of environmental compatibility and
  public convenience and necessity) before construction can lawfully
  continue. Note: the petition document's own caption shows the docket
  number blank ("2026-___-E") because it predates docket assignment — the
  158-E number was assigned after filing, confirmed via the docket page
  itself, not the petition PDF.
- **The docket page's own order log confirms the Aug. 27 ruling reported in
  the news actually happened, directly from the government source, not just
  news paraphrase**: a **"Special Commission Business Meeting Directive —
  Staff Presents for Commission Consideration Disposition of Initial
  Threshold Issue and Oral Arguments," dated Aug. 27, 2026**, appears in the
  docket's own record — matching the WebSearch-summarized news reporting
  (SC regulators ruling the facility isn't subject to Siting Act power-plant
  rules because it won't export power to the grid) almost exactly in timing.
  This is about as close to full primary-source confirmation as this kind of
  claim can get without reading the order text itself (still not extracted —
  worth a follow-up to pull the actual order PDF from the docket page).
- **Docket is still active**: most recent entries are **Sept. 3, 2026**
  Directive Orders 2026-520 and 2026-522 granting pro hac vice admission to
  out-of-state counsel (including Jeremy Fielding) for Valara — i.e., this
  is not over, litigation/regulatory activity is ongoing into this month.
- **Chester County's separate 6-month moratorium** (adjacent county, also
  tied to the Valara project in coverage): confirmed directly via WBTV
  (fetched tonight) — **unanimous** vote **July 20, 2026**, moratorium text
  quoted directly ("a temporary, countywide pause on the acceptance,
  processing, and approval of applications regarding data centers..."), two
  expert workshops scheduled **Aug. 13 and Sept. 28** (both 5 p.m.). Council
  Chair Pete Wilson noted no data center is currently proposed *in* Chester
  County itself — this is a preemptive/precautionary moratorium, a distinct
  pattern from most of this corpus's reactive moratoria.

**Bottom line:** fully verified via direct government-agency and direct
advocacy-org-hosted-legal-filing sources. This is exactly the utility-PSC-
docket angle the 09-05 note flagged as wanted — recommend Britton treat this
as ready for corpus consideration (his call on timing/restructuring), the
best-sourced of tonight's five leads by a clear margin.

---

## 6. Sabey/Decatur (Indianapolis) — Aug 20 hearing outcome: still genuinely unresolved

Re-searched with fresh phrasing tonight (ruling, decision, judge, order,
outcome, "August 20" / "Aug. 20" combined with Decatur Township/Sabey/MDC).
Nothing from after Aug. 20 turned up in any outlet. Direct-fetched Mirror
Indy's dedicated "Indianapolis data centers" tracker page (mirrorindy.org/
data-centers/, appears to be their rolling explainer, most recently touched
after the March 18 MDC approval) — it does not mention an Aug. 20 hearing
outcome either. **This is now confirmed unresolved across three consecutive
nightly passes (09-04, 09-05, tonight)** — treat as a standing information
gap, not a search failure, until something surfaces.

Confirmed still on the calendar: the **Sept. 16, 2026 MDC meeting** on
Sabey's incentive package is corroborated again tonight.

**Incidental finding, not part of tonight's assigned scope, flagged briefly
because it surfaced while checking Mirror Indy's tracker:** Indianapolis's
other two exempted data center projects (DC Blox/Irvington, Metrobloks/
Martindale-Brightwood) each also have their own separate judicial-review
suits against MDC approvals — DC Blox opponents preparing/filing an appeal
after a 6-1 MDC vote, and Metrobloks facing a petition filed May 1 by
residents and the Hoosier Environmental Council alleging "environmental
racism." Both appear to predate tonight's window and may already be
implicitly known from the 08-20 note (which named the three projects but,
re-reading it, only as "approved projects," not as active litigation) — not
verified against the full corpus tonight, just flagging that Marion County
now has three parallel data-center judicial-review suits running at once
(DC Blox, Metrobloks, Sabey), which could be a self-contained mini-
comparative case if Britton ever wants that granularity. Not a recommendation
to add it — just noting the pattern is bigger than "Sabey" alone.

---

## 7. Missouri / Nevada court-record access — still blocked, confirmed unchanged; did not re-attempt bypasses

Per tonight's instructions, did not burn time re-trying the same blocked
routes. Quick spot-checks only:
- `courts.mo.gov` — direct curl tonight returned **HTTP 500** (previously
  403 on 09-05) — a different error code, but still not a working access
  path either way. Not investigating further; consistent with "structural
  block" conclusion from 09-05.
- `documentcloud.org` (general domain, not the specific Washoe County
  document) — direct curl returned **HTTP 403**, consistent with the
  Cloudflare WAF block already documented 09-05.

No new information gathered on either the St. Louis Midtown (Pate/McCullen)
case number or the NV Energy v. Tract docket number. Treating both as still
at the ceiling 09-05 already documented — not a nightly retry target per
that note's own recommendation, which tonight's instructions echoed.

---

## 8. Louisville — Sept 15 committee hearing: confirmed no change

Direct-fetched LPM's Sept. 3 report again tonight (still accessible): the
Planning Commission's **5-3 vote** recommending stricter zoning (near-
universal rezoning requirement, 500,000 sq ft size cap, closed-loop cooling
mandate, quarter-mile facility-spacing rule) is unchanged from 09-04/09-05.
Metro Council's **Planning and Zoning Committee still meets Sept. 15, 1 p.m.,
City Hall**, chaired by Andrew Owen, who's signaled the process may run to a
second committee meeting rather than a quick vote. `louisvilleky.gov`'s
data-center page is still a **403** (WAF), unchanged from prior nights — not
re-investigating, consistent with the standing structural-block conclusion.

One item search surfaced but did not confirm: a "Councilwoman Chappell
reintroduces temporary moratorium" headline from louisvilleky.gov (title
only, page itself blocked). The LPM article directly fetched tonight makes
no mention of a Chappell moratorium reintroduction. Flagging as an unverified
loose end rather than asserting it — worth a look on a future pass once/if
louisvilleky.gov becomes fetchable.

---

## 9. Light national sweep — one genuinely new state-level thread found

Time-boxed per tonight's instructions ("if time allows, a light sweep").
One clearly new, real item found and directly verified:

- **New Hampshire — Gov. Kelly Ayotte** has taken a public position
  **opposing all data centers in the state**, citing ISO-New England
  guidance that large data centers will raise regional energy prices.
  Direct-fetched NHPR (Sept. 2, 2026): she plans to include a **multi-year
  moratorium in her upcoming state budget proposal** (earliest effective
  date **July 2027**, i.e., not immediate — though she could act sooner via
  executive order per the article) aimed at studying energy/water/noise
  impacts. Trigger: a proposed hyperscale data center in **Bow, NH**, tied to
  **Granite Shore Power LLC**'s idle former coal plant site and an
  **Eversource Energy** feasibility study (per FERC filings). Separately,
  NH House Democrats have announced their own 2027-session bill for a
  24-month moratorium. This is a genuinely new state for the corpus/scan —
  notable as a **governor-level** (not just county/city-level) opposition
  voice, and for the "old fossil plant site repurposed for a data center"
  framing, which hasn't shown up elsewhere in this corpus yet.
- Ran a general sweep for "Hill County, TX $100M moratorium lawsuit" out of
  curiosity while searching — confirmed real (RCM Hill LLC sued, county
  rescinded its moratorium, developer then dropped the suit, county paid
  $100k in the developer's fees) but this is already very likely covered by
  the 08-24/08-25/08-31 Texas-lead notes (titles reference "texas lead" and
  "tx-ky developer litigation pattern" explicitly) — not re-verifying or
  re-adding, just confirming it's a real, closed case in case cross-
  referencing is useful later.
- Did not find any other clearly new (post-9/5) moratorium votes, lawsuits,
  or contested hearings beyond what's captured above and what the existing
  notes already track (NC's rising moratorium count, already flagged in
  08-29/08-30, continues per a North State Journal headline that remained
  paywalled tonight — nothing new extracted).

---

## For Britton — plain summary of what moved and what didn't

- **Best news of the night: the South Carolina PSC docket lead is now fully
  verified from the government's own docket page** (2026-158-E, Concerned
  Citizens of Spartanburg County & Southern Alliance for Clean Energy v.
  Valara Holdings) plus the actual petition PDF, and it's still an active,
  ongoing matter as of Sept. 3. This is exactly the "regulatory docket, not
  just news coverage" kind of source the project wants more of.
- **Imperial County CA CEQA ruling**: real, but more complicated than 09-05
  knew — there are two separate tentative rulings by two different judges
  (one for the opposition on CEQA grounds, one for the developer against the
  county's own moratorium), both still tentative, neither final yet. Also
  caught a second instance of a search tool inventing a specific case number
  ("ECU004457") that the actual underlying article doesn't support — same
  pattern as the Missouri fabrication from 9/5, now confirmed to recur, so
  worth treating as a standing risk with this kind of tool, not a one-off.
- **Middlesex Township PA (PAX-1)** and **DeKalb County GA**: both real,
  both now better-sourced than 09-05 (direct org/outlet fetches instead of
  WebSearch-summary-only), both have concrete near-term dates worth watching
  (PAX-1: Sept. 16 EHB hearing, Sept. 18 show-cause oral arguments per
  WebSearch only; DeKalb: Sept. 9 zoning board of appeals hearing).
- **Luzerne County PA Sunshine Act win**: real, and it turns out the story
  didn't end with the Aug. 26 win — the township tried a second vote, got
  caught having violated its own court order, and is now doing a third vote
  Sept. 24. Good material if this becomes part of the write-up.
- **Sabey/Decatur Aug. 20 outcome**: still genuinely unresolved after three
  nights of checking — treat as a real information gap, not a search
  failure, until it surfaces.
- **MO/NV court access**: still blocked, didn't waste time re-trying per
  tonight's instructions — no change from 09-05's "structural ceiling"
  conclusion.
- **Louisville**: no change, Sept. 15 committee hearing is still the next
  real date.
- **One new state-level thread**: New Hampshire's governor has taken a
  public anti-data-center position and is planning a state budget moratorium
  proposal (earliest effective mid-2027) — a genuinely new, governor-level
  voice for the corpus/scan to know about whenever the national-scope
  restructuring conversation happens.
