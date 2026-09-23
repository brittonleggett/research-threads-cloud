# 2026-09-23 — SB 1198 enrolled statutory text pulled directly, Cards Against Humanity's actual
# court petition located and read, and a literature-scouting refresh

AI-run background-agent research pass (Claude, via Claude Code). Read-only web research and direct
document/page fetches only — no design/theory-chain decision made, nothing submitted or contacted
externally, no git operations performed (per this repo's standing convention), no file touched
outside `SPACEX_LOUISIANA_PAPER/` except the shared, append-only `Claude_Knowledge/
Research_Stream_Ideas.md` (per the standing exception for the nightly scouting task). Confirmed
current state first by reading the root README, this project's `CLAUDE.md`, the 09-20 note, the
09-09 literature note, and the corpus table — state matched the task brief's summary; nothing below
duplicates already-logged work.

## 1. Texas SB 1198 — enrolled statutory text pulled directly (resolves the 09-20 note's open item)

The 09-20 note only reached `capitol.texas.gov`'s bill-*history* page. Tonight, `curl` against
`capitol.texas.gov/tlodocs/89R/billtext/html/SB01198F.htm` (the enrolled-version HTML, found via a
plain WebSearch for the URL pattern the task brief suggested) returned the page directly — no
proxy needed, no block encountered. The exact enacted language, **Section 1** of the enrolled Act,
amending **Government Code § 424.001**:

> Sec. 424.001. DEFINITION. In this chapter, "critical infrastructure facility" has the meaning
> assigned by Section 423.0045(a)(1-a) and also includes:
> (1) any pipeline transporting oil or gas or the products or constituents of oil or gas;
> (2) a public or private airport depicted in any current aeronautical chart published by the
> Federal Aviation Administration;
> (3) a military installation owned or operated by or for the federal government, this state, or
> another governmental entity; [and]
> (4) any property, including a temporary hazard area related to the operation of a launch complex
> authorized by the Federal Aviation Administration, or facility used for the launch, landing,
> recovery, or testing of spacecraft, as defined by Section 507.001, Local Government Code; and
> (5) a property, facility, or pipeline described by this section that is under construction and
> all equipment and appurtenances used during that construction.

Effective date confirmed directly from the enrolled text: **September 1, 2025** (Section 4), and
Sections 2-3 confirm it applies only to offenses/causes of action arising on or after that date.
The bill's own certification language (also on this page) gives vote counts not previously in the
corpus: Senate passed 30-1 (March 24, 2025); House passed with amendments 121-17 (two present not
voting) on May 23, 2025; the two chambers then went to a **Conference Committee** (House refused
initial Senate concurrence), with the Conference Committee Report adopted by the Senate 30-1 and
the House 118-14 (two present not voting) on May 30, 2025 — a real, if minor, additional data point
(near-unanimous but not unanimous passage, requiring a conference committee) not previously in this
project's notes.

**An important mechanism correction, found while tracing the statute's actual legal effect**: SB
1198 amends **Government Code Chapter 424**, which (confirmed by directly fetching the current,
codified sections at 424.051 and 424.052 via FindLaw's own pages) criminalizes **damaging or
destroying** a critical infrastructure facility (third-degree felony) and **impairing or
interrupting its operation** (state jail felony) — both require entering *and* intentionally/
knowingly causing one of those specific harms, not mere unauthorized entry. The separate, more
commonly-cited **misdemeanor criminal-trespass enhancement**, Penal Code § 30.05, has **its own,
independent** "critical infrastructure facility" definition (§30.05(b)(7): chemical plants,
refineries, power plants, water/wastewater facilities, gas compressor stations, LNG terminals,
telecom switching offices, ports/rail/trucking terminals, gas-processing plants, and broadcast
transmission facilities — confirmed by directly reading the codified section via a `r.jina.ai`
proxy fetch of FindLaw's page after direct access was blocked). **SB 1198 did not touch Penal Code
30.05's list, and that list does not include spaceports.** So the accurate statement is: SB 1198
raises the *felony* exposure specifically for damaging/destroying or impairing/interrupting a
spacecraft launch/landing/recovery/testing facility — not for simply entering or trespassing on
one, which stays governed by the unchanged, narrower misdemeanor-trespass statute. Row 16's
existing note (via SOTXEJN's July 2026 post) frames this as "entering the town 'could' mean felony
arrest exposure" — that phrasing isn't cleanly supported by what SB 1198 itself actually amended;
it may reflect a different or additional legal basis, a broader/more cautious reading of exposure,
or context in SOTXEJN's fuller post that wasn't re-read tonight. **Flagging this as an open nuance
for row 16, not asserting SOTXEJN's statement is wrong** — a future session re-reading SOTXEJN's
full original post directly would resolve this cleanly.

All of the above (enrolled bill text, Gov't Code 424.001/424.051/424.052, Penal Code 30.05, and
Gov't Code 423.0045(a)(1-a) as the base cross-referenced definition) was fetched and read directly
from primary statutory-text sources (`capitol.texas.gov` directly; FindLaw's codified-statute pages
directly for 424.001 and via `r.jina.ai` proxy for 30.05/424.051/424.052 after direct 403s) — Tier
A throughout, not search-summarized.

## 2. Cards Against Humanity v. SpaceX — the actual court filing located and read

The 09-20 note added this case at A-minus tier (news reporting only; no working Cameron County
docket search found). Tonight:

- **WebSearch surfaced the actual cause number and court** directly: **Cause No. 2024-DCL-05445,
  Cameron County District Clerk, 404th District Court** (via a Trellis.law search-result snippet —
  Trellis's own case page itself returned a Cloudflare 403 to both direct `curl` and a `r.jina.ai`
  proxy attempt, so the docket-entry list/judge name shown in that snippet is **B-tier** (search-
  summary only), not independently confirmed by a direct fetch tonight. The `research.txcourts.gov`
  (re:SearchTX) portal, tried per the task brief's suggestion, returned a flat HTTP 403 to a direct
  `curl` attempt — consistent with every prior session's finding that Cameron County's state-court
  docket search is structurally inaccessible to this environment's tooling.
- **The actual 21-page Original Petition PDF was found and fetched directly** — hosted not by the
  court but by Cards Against Humanity's own campaign site (`cah-sues-elon-musk.s3.amazonaws.com`),
  a hosting detail worth noting (a party-hosted copy of its own filing, not a neutral court-record
  copy, though the content is the actual filed, clerk-stamped document — the PDF's own e-filing
  stamp confirms "FILED - 9/19/2024 6:36 PM, 2024-DCL-05445 / 92247218, LAURA PEREZ-REYES, Cameron
  County District Clerk, By Alejandra Ramos Deputy Clerk, Cameron County - 404th District Court,"
  matching the docket number found via WebSearch independently). `pdftotext`/`poppler-utils` was
  not available in this environment tonight (apt install failed on a 404'd package mirror); text
  was extracted successfully instead with Python's `pypdf` library (`pip install pypdf`), a working
  alternative worth noting for future sessions hitting the same poppler gap already flagged in the
  09-10 literature note.

Reading the petition directly confirms, beyond what news coverage already established:
- **Four causes of action**, not just "trespass": trespass, nuisance, unjust enrichment, and
  tortious interference with existing and prospective contracts/business relationships (the last
  theory specifically pleads that SpaceX's occupation of CAH's land creates a false public
  impression of association between CAH and SpaceX/Musk, damaging CAH's relationship with its
  donor-supporters — a distinct reputational-harm theory beyond simple property-line disregard).
- Damages pleaded: "up to" $15,000,000 (not a fixed $15M demand), plus exemplary damages (pleaded
  as warranted because the conduct was "fraudulent, intentional, malicious, and willful"),
  attorney's fees, and a permanent injunction ordering SpaceX to remove equipment/materials/
  personnel from the property.
- **Property legal description**: Lot 11, Block 4, Tarpon Haven Subdivision, Cameron County — this
  matches Bellingcat's independent satellite-imagery parcel identification (41176 Tarpon Bend Dr.)
  from the 09-20 note, now cross-confirmed from the primary legal document itself rather than only
  from Bellingcat's own analysis.
- **Attorney of record**: Kenneth E. McKay, McKay Law Offices, Bellaire, TX — a different firm from
  the Moore Law Firm representing the Aguilar plaintiffs (row 18), worth noting if the manuscript
  ever compares plaintiffs'-counsel patterns across the Boca Chica litigation corpus.
- **A minor date nuance worth flagging, not smoothing over**: the petition itself states SpaceX had
  "treated the Property as its own for at least six (6) months" as of the September 2024 filing —
  i.e., roughly since spring 2024 — while Bellingcat's independent satellite-imagery analysis (cited
  in the 09-20 note) found construction-related activity on the same parcel beginning around June
  2023, over a year earlier. These aren't necessarily contradictory (the petition's "six months"
  describes the specific construction-storage/vehicle-staging use CAH is suing over, which could
  postdate an earlier, less intensive phase of activity Bellingcat's imagery caught), but they are
  not the same date either — flagging the discrepancy explicitly rather than assuming either source
  resolves it.

**Net effect: row 20 upgrades from A-minus to full Tier A** — the underlying primary legal document
is now read directly, not just secondary news reporting of it, resolving the specific open item the
09-20 note flagged. The judge's identity and the case's later docket history (answer, discovery,
settlement filing) remain unverified beyond news reporting — the actual docket search tool this
would require stays inaccessible to this environment, consistent with every prior attempt.

### Also found while researching this case: two new, real Boca Chica corpus items

Neither was being searched for specifically — both surfaced as directly-linked related coverage
while reading the police-department/tax-incentive news beat for Starbase, TX, and both are
genuinely new, well-documented, and directly relevant to this paper's core framing (not previously
in the corpus table; checked against the table before adding). Full detail and sourcing is in the
corpus table's own 2026-09-23 update section — summarizing here:

- **City of Starbase's own police department** (Ordinance OR 2026-4, confirmed directly from the
  city's own `starbase.texas.gov/ordinances` page), formed after a $3.5M/5-year Cameron County
  Sheriff's Office contract broke down because the county couldn't recruit deputies for a position
  with no civil-service protection (Sheriff Manuel Treviño's own on-record quote, KVEO-TV/
  ValleyCentral, fetched directly via proxy). City Administrator Kent Myers, on record, ties the
  new department explicitly to protecting SpaceX's operations: "There is a lot of assets here with
  the operations of SpaceX... those assets need to be protected." Directly extends the paper's
  existing regulatory-capture thread (row 17, the incorporation election) — the same SpaceX-staffed
  municipal government now runs its own law enforcement.
- **SpaceX's own application, via the City of Starbase, for a Texas Enterprise Zone Program sales-
  tax refund** (up to $7.5M combined across two projects, GigaBay and an unnamed expansion) —
  construction on the GigaBay project began *before* the state application was filed, prompting
  Good Jobs First researchers (a named, credentialed economic-development-accountability nonprofit)
  to directly question whether the incentive meets its own program logic ("retroactively giving it
  subsidies... doesn't meet the definition of an incentive"). This is a sharp, directly on-point,
  named-source primary example for the paper's economic-benefit-claim-specificity/additionality
  frame, found via Texas Tribune reporting (Berenice Garcia byline, republished by KVEO-TV/
  ValleyCentral, fetched directly via proxy after a direct 403).

## 3. Literature-gap scouting refresh (last touched 2026-09-09/09-10)

Full detail in the new `literature/Literature_Refresh_2026-09-23.md` file. Summary:

- **Kudłak (2025)** — the loose-coupling/greenwashing-alternative anchor flagged as unverified on
  09-09 and cross-verified via secondary listings on 09-10 — is now **verified directly against
  Crossref's own API** (title, single author, journal, DOI, and an actual abstract field all
  confirmed from a primary bibliographic registry, not a search snippet or secondary listing). Safe
  to cite the bibliographic details with confidence now; the article's full body text remains
  paywalled and unread.
- **Two new, Crossref-verified 2024-2025 papers** extend the project's existing claim-specificity
  anchor (Janssen, Swaen & Du 2022): **Choubey et al. (2025, *Business Strategy and the
  Environment*)**, a two-phase longitudinal survey (512 + 478 respondents) on green-claim signals
  vs. actual company environmental actions in quick-commerce, finding claim-exposure effects can
  decay with repeated exposure even when the underlying claims stay constant; and **Wang, Zhou,
  Zhang & Wang (2024, *Current Psychology*)**, "claim specificity x message framing" in green
  demarketing ads — a citation-only lead (title/DOI verified, content not yet read), and worth
  noting its actual publication date (Dec. 14, 2024) falls just outside the task's 2025-2026 window,
  flagged precisely rather than rounded up.
- A broader search for a direct marketing/consumer-behavior treatment of "economic-benefit-claim
  framing" specifically in infrastructure-siting contexts (as opposed to green/environmental
  claims) again came up empty, same finding as 09-09/09-10 — the closest real analogs remain the
  claim-specificity green-advertising literature and the greenwashing/loose-coupling/aspirational-
  talk cluster already anchored in this project. This gap appears stable across three separate
  search passes now, not a one-off miss.

## What this does not do

Does not pick a Study 1 corpus option, theory frame, or lock any design element — unchanged,
Britton's call per `CLAUDE.md`. Did not contact, submit, or post anything externally. Did not run
any git commands. Did not touch any file outside `SPACEX_LOUISIANA_PAPER/` except the shared,
append-only `Claude_Knowledge/Research_Stream_Ideas.md` (per the nightly-rotation scouting task,
same standing exception every other project's overnight notes use).

## Still open / next steps

- Row 16 nuance (SB 1198's actual felony-damage/impair mechanism vs. SOTXEJN's "felony arrest for
  entering" framing) — a future session should re-read SOTXEJN's full July 2026 post directly to
  see whether it cites a different provision or a broader legal theory not captured here, rather
  than assuming either source is simply wrong.
- Cards Against Humanity v. SpaceX: the presiding judge's identity and the case's later docket
  history (answer, discovery record, actual settlement/dismissal filing date) remain B-tier
  (news-sourced) or unverified — Cameron County's docket search, re:SearchTX, and Trellis.law's own
  case page all remained inaccessible to this session's tooling (Cloudflare/403 across the board).
  A future session with different tooling (or a human with a browser) could close this.
- Wang et al. (2024)'s actual content (not just its citation) is unread — a lead for a future
  literature pass, not yet citable beyond title/authors/venue.
- Standing broader open items, unchanged from prior notes: the ~$10M Aguilar damages figure's origin
  remains formally unresolved (treat the 09-20 note's exhaustive-search finding as still current);
  `notes/2026-08-27-orientation.md` has still never been rewritten to reflect how many of its
  individual facts have since been independently verified across many sessions — a future session
  could do a dedicated pass closing that specific loop.
