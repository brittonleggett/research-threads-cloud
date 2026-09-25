# SpaceX Vermilion Parish Spaceport — Study 1 Corpus (DRAFT, corpus-building only)

**No theory chain, coding scheme, or Study 1 option (A/B/C, see `notes/2026-08-27-orientation.md`)
is decided here — this file only inventories candidate artifacts with sources, so a corpus
exists to code once Britton picks a direction.** Confidence tiers follow the same convention as
TARIFF_PAPER/DATA_CENTER_PAPER: A = primary-fetched, B = search-summarized pending re-fetch,
C = existence-confirmed but content not yet extracted.

## Louisiana side (corporate/official messaging — candidate Option A material)

| # | Source | Type | Date | Tier | Link |
|---|--------|------|------|------|------|
| 1 | Louisiana Economic Development | Official program page (investment/jobs/fiscal terms) | current as of 2026-08-27 | A | [opportunitylouisiana.gov/spacex](https://www.opportunitylouisiana.gov/spacex) |
| 2 | Gov. Jeff Landry | Public quote, via LED page | 2026-08-25 announcement | A | (same LED page above) |
| 3 | Elon Musk | Public quote/video, via LED page + news coverage | 2026-08-25 | A (quote) / B (video itself not directly fetched) | (same LED page above); [TechCrunch](https://techcrunch.com/2026/08/25/spacex-will-build-a-second-100b-starbase-spaceport-in-louisiana/) |

## Louisiana side (opposition/regulatory — candidate Option B material)

| # | Source | Type | Date | Tier | Link |
|---|--------|------|------|------|------|
| 4 | Louisiana Wildlife Federation, National Wildlife Federation, Pontchartrain Conservancy | Joint FAA comment letter (PDF, directly hosted) | 2026-08-24 | **A — UPGRADED 2026-08-29**: full text extracted directly (`curl` + `pdftotext`, poppler-utils installed this session) and cross-checked against an independent extraction path (r.jina.ai reader proxy on the same URL); both agree. See notes/2026-08-29 for full extracted text and summary. | [lawildlifefed.org PDF](https://lawildlifefed.org/wp-content/uploads/FAA-Comment-Letter-8-24-2026-LWF_NWF_PC.pdf) |
| 5 | FAA | NPRM "Waiver of Specified Statutory Requirements for Commercial Space Launch and Reentry Actions," Docket No. FAA-2026-8614, Notice No. 26-11, RIN 2120-AM51 (waives NEPA/ESA/CWA/CAA/NHPA/MMPA + 7 more statutes for commercial launch/reentry licensing) | Federal Register notice 2026-07-30; comments due on or before **2026-08-31** | **A — UPGRADED 2026-08-29**: docket number, notice number, RIN, and comment deadline all confirmed directly from the Federal Register's own PDF (govinfo.gov mirror, fetched via `curl`+`pdftotext` after federalregister.gov and regulations.gov both continued to block WebFetch/bot access). Independently corroborated by the docket number cited in the wildlife groups' own comment letter (#4). | [Federal Register PDF via govinfo.gov](https://www.govinfo.gov/content/pkg/FR-2026-07-30/pdf/2026-15415.pdf) (regulations.gov docket page itself still not directly loadable: [regulations.gov/docket/FAA-2026-8614](https://www.regulations.gov/docket/FAA-2026-8614)) |
| 6 | Louisiana Illuminator | News coverage of the wildlife-groups' opposition | 2026-08-25 | A (news article itself fetched/read) | [lailluminator.com](https://lailluminator.com/2026/08/25/wildlife-spacex/) |
| 6b | Louisiana Illuminator | "Pecan Island residents fight to be heard on SpaceX" — reports LED required elected officials to sign NDAs (State Rep. Jacob Landry signed one in Feb. 2026; State Sen. Bob Hensgens signed then rescinded), residents first noticed survey crews ~Aug. 10, formed "StopSpaceX" group | 2026-08-19 | A — fetched via reader-proxy after direct site 403 (see notes/2026-08-29); content plausible/internally consistent, treat as A-minus pending a second independent confirmation of the NDA detail specifically | [lailluminator.com/2026/08/19/pecan-island-spacex](https://lailluminator.com/2026/08/19/pecan-island-spacex/) |
| 6c | KPLC (Lake Charles CBS affiliate) | "'Landry really stabbed us in the back' — Pecan Island residents still concerned after SpaceX announcement" — direct resident quotes on lack of warning, eminent-domain fear, noise/Boca-Chica comparison, crabbing-business livelihood concern | 2026-08-26 | A (fetched directly) | [kplctv.com](https://www.kplctv.com/2026/08/26/landry-really-stabbed-us-back-pecan-island-residents-still-concerned-after-spacex-announcement/) |
| 6d | Fox 8 Live (WVUE New Orleans) | "Some Pecan Island residents complain they were left in the dark about SpaceX project" — resident Crystal Mhire quote on outreach failure | 2026-08-26 | A (fetched directly) | [fox8live.com](https://www.fox8live.com/2026/08/26/some-pecan-island-residents-complain-they-were-left-dark-about-spacex-project/) |
| 6e | Louisiana Economic Development | Official press release (distinct URL from the /spacex program page, #1 above) — confirms $25M Community Foundation of Acadiana donation, PILOT terms, no coastal-master-plan dollar figure | 2026-08-25 | A (fetched directly) | [opportunitylouisiana.gov/news/...](https://www.opportunitylouisiana.gov/news/spacex-launches-new-era-of-commercial-spaceflight-with-100-billion-louisiana-campus) |
| 6f | The Current (Lafayette) | Live-blog of the Aug. 25 press conference in Abbeville — contemporaneous, timestamped reporting; the only source located that attributes a specific "$100 million coastal master plan" figure to a direct Landry statement to press (see notes/2026-08-29 for the $25M/$100M reconciliation) | 2026-08-25 | A — fetched via reader-proxy after direct site 403 (flagging the proxy-mediated path per repo verification norms) | [thecurrentla.com/2026/live-is-spacex-coming-to-pecan-island](https://thecurrentla.com/2026/live-is-spacex-coming-to-pecan-island/) |
| 6g | State of Louisiana | Act 874 (2026 Reg. Session), HB 1098 (Reps. McFarland/Chassion) — enacts La. R.S. 9:2800.31, a liability shield barring nuisance/trespass/inverse-condemnation/strict-liability claims against any aerospace entity holding 20,000+ contiguous acres; exceptions for gross negligence, intentional injury, FAA-license violations, and excess falling-debris harm | signed 2026, effective on signature | A — enrolled bill text fetched directly (`curl`+r.jina.ai proxy after direct legis.la.gov 403) | [legis.la.gov ViewDocument d=1481505](https://www.legis.la.gov/legis/ViewDocument.aspx?d=1481505) |
| 6h | Louisiana Illuminator | "Louisiana launches immunity law to lure aerospace companies" — HB1098's 33-3 Senate passage; names a 2026-05-01 Texas Tribune-reported Boca Chica-area homeowner lawsuit over rocket-shock home damage as the claim type the bill immunizes against in Louisiana; quotes Sen. Luneau (opposing) and Sen. Connick ("No other state gives immunity away like we just did"); confirms a companion public-records exemption for aerospace company records | 2026-05-29 | A (fetched directly via proxy) | [lailluminator.com/2026/05/29/aerospace-immunity-law](https://lailluminator.com/2026/05/29/aerospace-immunity-law/) |
| 6i | The Current (Lafayette) | "What does SpaceX's legal shield mean for Vermilion Parish residents?" — names Act 874 + companion Act 343 (HB1250, blocks injunctions/enables early dismissal of nuisance suits with fee-shifting); quotes attorney Bill Goodell calling both acts likely unconstitutional and a "double shield" (IDB of Vermilion Parish holds spaceport land under long-term lease); explicitly links the state liability shield's FAA-license-violation exception to the pending federal waiver fight (row 5) | 2026-08-31 | A (fetched directly via proxy) | [thecurrentla.com/.../what-does-spacexs-legal-shield-mean...](https://thecurrentla.com/2026/what-does-spacexs-legal-shield-mean-for-vermilion-parish-residents/) |

## Update — 2026-09-25 (see notes/2026-09-25-regulatory-check-boca-chica-expansion-and-literature.md)

- **New rows 21-23** (Aguilar docket procedural update, Starbase 7,133-acre annexation, NPR/Gulf
  States Newsroom Sept. 20 piece) — see rows below for detail. (Renumbered from this session's own
  20-22 to 21-23 on merge, since row 20 was already taken by the Cards Against Humanity entry added
  in the parallel 2026-09-20/09-23 work below.)
- **FAA-2026-8614 re-checked (first raw re-check since 2026-09-07).** Docket disposition is still
  **"Pending"** (`api.regulations.gov` docket record, `modifyDate: 2026-09-11`), no final rule
  exists (checked both `federalregister.gov`'s API for the RIN and the FAA agency feed — zero
  matching documents beyond the original 2026-07-30 proposed rule). Posted-comment count moved only
  3,201 → 3,203 in 18 days — essentially flat, consistent with the "deprioritize to occasional
  checks" recommendation already made 2026-09-07.
- **What's still needed list below refreshed** to match current state.

## Update — 2026-09-23 (see notes/2026-09-23-sb1198-enrolled-text-cah-docket-and-literature-refresh.md)

- **Row 16 (SB 1198) — enrolled statutory text now directly read, and an important legal-mechanism
  correction.** The enrolled bill text (`capitol.texas.gov/tlodocs/89R/billtext/html/SB01198F.htm`,
  fetched directly via `curl`) confirms SB 1198 amends **Government Code § 424.001** — a chapter
  titled "Damaging or Destroying Critical Infrastructure Facility" (§424.051, third-degree felony)
  and "Impairing or Interrupting Operation of Critical Infrastructure Facility" (§424.052, state
  jail felony) — **not** Penal Code § 30.05, the more commonly-cited misdemeanor criminal-trespass
  statute. Penal Code § 30.05 has its **own, separate** "critical infrastructure facility"
  definition (§30.05(b)(7): chemical plants, refineries, power plants, water/wastewater facilities,
  gas compressor stations, LNG terminals, telecom switching offices, ports/rail/trucking terminals,
  gas processing plants, broadcast transmission facilities) that SB 1198 did **not** amend and that
  does **not** include spaceports. This means SB 1198 raises the criminal exposure specifically for
  **damaging/destroying or impairing/interrupting** a spacecraft launch/landing/recovery/testing
  facility (felony-level), not for the act of mere unauthorized **entry** onto one (which stays
  governed by Penal Code 30.05's unchanged, narrower definition). This is a real nuance for row 16's
  existing note that SOTXEJN's July 2026 post frames this as "entering the town 'could' mean felony
  arrest exposure" — that characterization is not cleanly supported by the amended statute's actual
  mechanism as read tonight; it may rest on a different provision, a broader reading, or context not
  captured in this project's prior notes. Flagging as an open nuance, not a correction of SOTXEJN's
  own statement (their full post was not re-read tonight to check for a fuller explanation). See the
  dated note for the full verbatim enrolled text and the Government Code / Penal Code cross-reference
  chain (423.0045(a)(1-a) as the base list, both fetched directly from FindLaw's codified-statute
  pages).
- **Row 20 (Cards Against Humanity v. SpaceX) UPGRADED A-minus → A.** The actual 21-page Original
  Petition was located and fetched directly (hosted by CAH's own campaign site,
  `cah-sues-elon-musk.s3.amazonaws.com`) and read in full. Confirms: Cause No. **2024-DCL-05445**,
  Cameron County District Clerk (Laura Perez-Reyes), **404th District Court**; filed 9/19/2024 6:36
  PM; plaintiff's counsel Kenneth E. McKay (McKay Law Offices, Bellaire, TX); four causes of action
  (trespass, nuisance, unjust enrichment, tortious interference with existing/prospective business
  relationships) plus a jury demand; damages pleaded "up to" $15,000,000 plus exemplary damages,
  attorney's fees, and a permanent injunction; property legally described as **Lot 11, Block 4,
  Tarpon Haven Subdivision, Cameron County** (matches Bellingcat's satellite-imagery parcel
  identification). The petition itself states SpaceX's use of the property had gone on "for at least
  six (6) months" as of the Sept. 2024 filing (i.e., roughly since spring 2024) — a modest date
  discrepancy worth flagging against Bellingcat's independent finding of construction activity
  beginning around June 2023; not necessarily contradictory (the petition's "six months" describes
  the more intensive construction-storage use CAH is suing over specifically, not first detectable
  activity), but not identical either. The presiding judge (Ricardo M. Adobbati, per a Trellis.law
  case-page WebSearch snippet) and the case's docket entries/settlement-filing date were **not**
  independently verified tonight — Trellis.law, law.justia.com, codes.findlaw.com's case pages, and
  `research.txcourts.gov` (re:SearchTX) all returned Cloudflare/403 blocks to both direct `curl` and
  the `r.jina.ai` proxy; Cameron County's state-court docket remains structurally inaccessible to
  this session's tooling, consistent with every prior session's finding. Treat the judge's name as
  B-tier (search-summary only) pending independent confirmation.
- **New row 21**: City of Starbase's own police department (Ordinance OR 2026-4, "Establishing the
  Starbase Police Department," confirmed directly from the city's own `starbase.texas.gov/ordinances`
  page) — approved by the SpaceX-staffed City Commission Feb. 3, 2026, after a $3.5M/5-year Cameron
  County Sheriff's Office law-enforcement contract broke down (county couldn't recruit deputies
  because the assignment carried no civil-service job protection, per Sheriff Manuel Treviño's own
  on-record quote). City Administrator Kent Myers, on record: "There is a lot of assets here with the
  operations of SpaceX... those assets need to be protected, and so the police department will play a
  critical part in protecting those assets." Directly extends row 17's incorporation-election finding
  (SpaceX employees running the municipal government) into a second, sharper regulatory-capture data
  point: the same company-staffed government now runs its own law enforcement. Tier A (KVEO-TV/
  ValleyCentral news article, published 2026-02-04, fetched via `r.jina.ai` proxy after a direct 403;
  city's own ordinances page fetched directly).
- **New row 22**: SpaceX's own application for Texas's Enterprise Zone Program sales-tax-refund
  incentive (via the City of Starbase, whose three-member Commission includes two SpaceX employees) —
  two projects (GigaBay, a $506M investment, and an unnamed expansion, $480M), each seeking up to
  $3.75M in state sales-tax refunds (up to $7.5M combined), tied to a "Triple Jumbo Project"
  designation requiring $250M+ capital investment. Construction on the GigaBay project began in April
  2025, before the state application was filed — Good Jobs First researchers Kristan Wong Karinen and
  Kasia Tarczynska are quoted directly questioning whether a company already operating in the area,
  already under construction, meets the incentive program's own "would not have happened without it"
  logic ("By already having this company within that town, and then retroactively giving it
  subsidies, it doesn't meet the definition of an incentive"). This is a sharp, directly on-point
  primary source for the paper's economic-benefit-claim-specificity/additionality frame — a named,
  credentialed critique of the incentive's own logic, not just opposition sentiment. Tier A (Texas
  Tribune reporting by Berenice Garcia, republished by KVEO-TV/ValleyCentral 2026-01-29, fetched via
  `r.jina.ai` proxy after a direct 403).
- No theory chain, coding scheme, or Study 1 option decided — same standing rule as before.

## Update — 2026-09-20 (see notes/2026-09-20-reuters-search-exhausted-and-cards-against-humanity-critical-infrastructure-added.md)

- **New row 20**: *Cards Against Humanity v. SpaceX* (Cameron County District Court, 404th District,
  case number not independently located) — land-trespass dispute, distinct from the Aguilar
  acoustic-damage suits (row 18). CAH bought a Cameron County parcel in 2017 as an anti-border-wall
  publicity stunt; sued SpaceX ~Sept. 2024 for using the land for construction storage without
  permission, seeking $15M; settled Oct. 2025 just before trial, with CAH's own statement saying
  "SpaceX admitted during the discovery phase... to trespassing." Tier A-minus: every fact comes
  from a direct fetch of CBS News Texas, TechCrunch, and Bellingcat's own reporting (the last an
  independent satellite-imagery corroboration of the underlying land-use claim), but the underlying
  court filing itself was not located/read — flag this tier distinction if cited.
- **Row 16 (critical-infrastructure designation) — verification resolved.** Previously sourced only
  to SOTXEJN's own petition post. Now primary-verified via `capitol.texas.gov`: **Texas SB 1198,
  89th Legislature Regular Session**, signed June 20, 2025, effective Sept. 1, 2025 — amends the
  state's critical-infrastructure-facility statute to explicitly cover FAA-licensed spacecraft
  launch/landing/testing facilities (Starbase by name in contemporaneous coverage). This is very
  likely the specific statutory basis for SOTXEJN's felony-trespass-exposure concern (timing is
  consistent: SB 1198 took effect before SOTXEJN's July 2026 post). Tier A for the bill's
  history/caption/dates (fetched directly from the Legislature's own site); the enrolled text itself
  not yet read line-by-line.
- **The ~$10 million Aguilar damages figure's origin: search for a direct reuters.com URL is now
  genuinely exhausted** (multiple search engines and approaches tried, all negative) — remains
  unresolved, treat as closed lead barring a new development. See the dated note for full detail,
  including a finding that this environment's `WebFetch` tool is hard-blocked from `www.reuters.com`
  specifically, which would affect any future attempt even if a URL is eventually found.
- No theory chain, coding scheme, or Study 1 option decided — same standing rule as before.

## Update — 2026-09-18 (see notes/2026-09-18-aguilar-address-dedup-and-damages-attribution.md)

- **Row 18 (Aguilar complaint) updated — "53 homes" question RESOLVED, not just narrowed.** A
  systematic, programmatic parse of Section V's 53 named-plaintiff paragraph-groups (¶¶94-252)
  found that 6 of those 53 groups plead two separate street addresses each, and one pleads two
  distinct condo units at one street address — so the complaint's own text supports **58-59
  distinct properties**, not 53. Cross-checked against Texas Tribune's own wording ("53 homes...
  including several couples who shared homes"), which matches the household-group count, not a
  property count. See row 18 and the dated note for full detail and the paragraph-by-paragraph
  address list.
- **Damages-figure attribution resolved for the "$100K foundation repair" figure**: it traces to a
  named plaintiff's on-record interview with **Reuters**, not an attorney statement (correcting
  the 09-16 note's guess). The **~$10M figure's origin remains unresolved** — not found in the
  complaint, not clearly attributable to a specific attorney quote or press release in the outlets
  checked tonight either.
- **New row 19**: TCEQ Docket 2024-1282-IWD-E ($3,750 penalty) — this was actually already
  primary-verified 2026-09-04 but never given its own table row; the "What's still needed" list's
  item 4 incorrectly carried it as open for two weeks. Corrected tonight (same class of
  stale-tracking bug as row 7's tier field, fixed 2026-09-16).
- No theory chain, coding scheme, or Study 1 option decided — same standing rule as before.

## Update — 2026-09-16 (see notes/2026-09-16-aguilar-complaint-damages-read-and-corpus-table-maintenance.md)

- **Row 7 tier corrected B → A.** This row's Tier field had said "B" since the table was first
  built, even though the 2026-09-05 update section below (and notes/2026-09-05) documented the
  upgrade to primary-document tier that same night — a stale-field bug, not a re-verification.
  Corrected tonight per the discrepancy already flagged in notes/2026-09-14.
- **New row 7b**: the 2025/2026 SpaceX-provided economic-impact figures ($13B+ gross output, 24K+
  jobs, $305M+ indirect taxes) — flagged as stuck at search-snippet tier as recently as 09-14 —
  reached primary-document tier tonight via a successful Wayback Machine fetch (see row 7b for the
  exact technique). **These are the same figures reported by five news outlets on 09-14, now
  independently confirmed against the actual SpaceX-branded infographic itself**, with an added
  framing nuance: they are SpaceX's own self-reported numbers, not an independent county audit.
- **New row 17**: City of Starbase incorporation election results (found/verified 2026-09-14, not
  yet folded into this table until tonight).
- **New row 18**: *Aguilar v. SpaceX* complaint (Case 1:26-cv-00485) — full 59-page document read
  tonight. Confirms the 11-test-flights/April 2023-October 2025 date range and >110 dB threshold
  directly from the complaint text (previously only in the 09-14 note's caption/parties/causes-of-
  action read). **Important correction**: the ~$10M damages figure and "$100K foundation repair"
  figure circulating in press coverage do **not** appear anywhere in the complaint itself — the
  Prayer for Relief pleads unspecified "actual damages" and "exemplary damages" only. These two
  figures should not be upgraded to primary tier; if anything, downgrade confidence that they are
  formally part of the legal claim at all (they read as attorney-to-press statements, not pleaded
  amounts). The "53 homes" count also isn't stated as a document total; a rough count of pleaded
  property paragraphs yielded ~46-52, in the right range but not an exact primary confirmation.
- No theory chain, coding scheme, or Study 1 option decided — same standing rule as before.

## Boca Chica, TX comparison corpus (candidate Option C material — the paper's built-in
comparison case)

| # | Source | Type | Date | Tier | Link |
|---|--------|------|------|------|------|
| 7 | Cameron County, TX (hosting SpaceX's own "Starbase Local Impact" report) | Self-released Starbase economic-impact stats (~$800M claim, 2024 period) | released 2024, covering prior period | **A** — UPGRADED B → A 2026-09-05 (county's own PDF directly fetched/read that session; this table row's tier field was left stale until corrected 2026-09-16 — see notes/2026-09-14 and notes/2026-09-16 for the discrepancy). | [MyRGV](https://myrgv.com/publications/the-monitor/2024/06/21/spacex-claims-it-has-800m-impact-in-cameron-county/), [ValleyCentral](https://www.valleycentral.com/spacex/cameron-county-releases-starbase-local-impact-economic-stats/), [Cameron County PR PDF](https://www.cameroncountytx.gov/wp-content/uploads/2024/06/2024.6.18-STARBASE-LOCAL-IMPACT-PR-2.pdf) |
| 7b | Cameron County, TX (hosting SpaceX's own "Starbase Local Impact" infographic) | 2025/2026-period economic-impact infographic: $13B+ gross economic output, 24K+ local jobs supported, $305M+ indirect taxes (all labeled "2024-2026"), plus 350+ local suppliers and $147M+ local supply-chain spend (labeled "2024") | infographic dated Oct. 22, 2025 per accompanying press release; Wayback-captured 2026-03-16 | **A — UPGRADED B → A 2026-09-16.** The live county page/PDF 404s and had been flagged 09-14 as Wayback-unreachable; tonight's session reached the Wayback Machine successfully via `curl` with a browser User-Agent over HTTPS using the exact snapshot URL from the `archive.org/wayback/available` API, with the `if_` (raw HTML) and `im_` (raw image) URL modifiers — a different result from 09-14's attempt, not a contradiction of it (that session may have used a plain `/web/<timestamp>/` URL or hit a transient block; worth retrying this exact recipe first in any future session before assuming the path is closed). The figures are an **embedded JPEG infographic**, not page text — read directly via the Read tool. **Important framing note for the corpus**: the press release text explicitly attributes the report to SpaceX ("the updated Starbase Local Impact report provided by Space Exploration Technologies Corp. (SpaceX)"), and the infographic itself carries the SpaceX logo — this is company-self-reported data redistributed via the county's official channel, not an independent county calculation, despite being commonly reported in press as "Cameron County's" figures. Flag this distinction if cited in the economic-benefit-claim-specificity frame. | [Wayback snapshot](https://web.archive.org/web/20260316233954if_/https://www.cameroncountytx.gov/2026-spacex-economic-impact-release/), [infographic image](https://web.archive.org/web/20260316233954im_/https://www.cameroncountytx.gov/wp-content/uploads/2025/10/10.22.jpeg) |
| 8 | The Conversation | Academic-adjacent commentary on Starbase's landscape/community impact | 2026 | A (article itself fetched earlier tonight, see orientation note) | [theconversation.com](https://theconversation.com/the-starbase-rocket-testing-facility-is-permanently-changing-the-landscape-of-southern-texas-242450) |
| 9 | Jorge Palacios, *Martian Borderlands: Colonizing (Outer) Space in the Lower Rio Grande Valley* | M.A. Thesis, MAPSS, University of Chicago, CC BY 4.0 — ethnographic/participatory-action research on Starbase's impact on Indigenous (Carrizo/Comecrudo) and Latinx Brownsville-area communities | August 2023 (author's continuing PhD research at MIT HASTS confirms this is an active, ongoing research program, not a one-off) | **A — RESOLVED 2026-08-30**: independently confirmed three ways (direct WebFetch of the record page, DOI resolution to a second independent record URL, cross-reference against MIT HASTS's own student-bio page). Thesis-tier, not peer-reviewed-tier — flag that distinction if cited. See notes/2026-08-30 for full verification detail. | [DOI 10.6082/uchicago.7220](https://doi.org/10.6082/uchicago.7220), [knowledge.uchicago.edu/record/7220](https://knowledge.uchicago.edu/record/7220) |
| 10 | U.S. EPA Region 6 | Consent Agreement and Final Order (CAFO), Docket No. CWA-06-2024-1768 — federal Clean Water Act enforcement action against SpaceX for 8 unauthorized discharges (liquid oxygen spill + water deluge system discharges) to wetlands bordering the Starbase Launch Pad, Cameron County, TX, 2022-2024; $148,378 civil penalty; SpaceX "neither admits nor denies" the specific factual allegations | violations 2022-2024, CAFO on/around Sept. 2024 | **A — verified 2026-08-31**: primary document fetched directly (`curl`, HTTP 200) and extracted with `pdftotext -layout`; this is the actual federal enforcement record the FAA-docket wildlife-groups' letter (#4) and the Wesolick FAA comment (see notes/2026-08-30) both cite as "commenters state" — now independently confirmed, not secondhand. See notes/2026-08-31 for full extracted detail (dates/volumes of each discharge, admission language, related TCEQ Agreed Order). | [epa.gov CAFO PDF](https://www.epa.gov/system/files/documents/2024-09/spacex_cafo_cwa-06-2024-1768_txu09110_090624__0.pdf) |
| 17 | Cameron County, TX Elections Department | Official "Unofficial Results Summary Results Report," City of Starbase incorporation election — 212 For/6 Against (97.25%), 283 registered voters, 78.80% turnout; Mayor Bobby Peden unopposed (216 votes); Commissioners Jordan Buss (177) and Jenna Petrzelka (188), both unopposed | election May 3, 2025; document fetched 2026-09-14 | A (county's own official election-results PDF, fetched directly). Search-snippet-tier only (CNBC coverage, not the PDF): Peden is SpaceX's VP of Test and Launch Operations, Buss is SpaceX's Environmental, Health & Safety director, and most of the ~300 eligible voters are SpaceX employees/contractors living on company property. Theoretically relevant as a literal, ex-post regulatory-capture instance (company's own senior staff becoming the municipal government with zoning/permitting authority over the facility they operate) — see notes/2026-09-14 for the fuller framing tie to Coen et al. 2020 / Carpenter & Moss 2013. | [cameroncountytx.gov elections PDF](https://www.cameroncountytx.gov/elections/wp-content/uploads/2025/05/City-of-Starbase-Summary.pdf) |
| 18 | U.S. District Court, S.D. Tex. (Brownsville Div.) | *Aguilar et al. v. Space Exploration Technologies Corp.*, Case No. 1:26-cv-00485 — federal mass-tort complaint (negligence, gross negligence/exemplary damages, trespass) alleging Starship test-flight acoustic energy (sonic booms, launch/landing noise) damaged homes in Port Isabel, South Padre Island, Laguna Vista, and Laguna Heights | filed 04/30/2026; full 59-page complaint directly fetched and read 2026-09-16 and re-fetched/systematically parsed 2026-09-18 (CourtListener/RECAP docket 73273866, `storage.courtlistener.com` PDF, same file: HTTP 200, 1,220,737 bytes) | **A** for: case caption/docket number, ~80 named plaintiffs (individuals, couples, two estates, one family trust), defendant description, jurisdiction (28 U.S.C. §1331 + Commercial Space Launch Act, 51 U.S.C. §50914(g)), all three causes of action, the "eleven fully integrated Starship/Super Heavy test flights between April 2023 and October 2025" count and date range (complaint ¶¶3, 92, with all eleven flight dates and SpaceX's own launch-page citations in footnote 44), and the >110 dB structural-damage threshold cited from independent BYU acoustic researchers. **Not confirmed / corrected from secondary coverage**: the complaint's own Prayer for Relief (¶¶ 269, p.57-58) requests only "actual damages," "exemplary damages," interest, costs, and fees — **no specific dollar figure (e.g. "$10 million") appears anywhere in the 59-page document**, and neither does the word "foundation" (i.e., no "$100K foundation repair" line). **RESOLVED 2026-09-18 (see notes/2026-09-18-aguilar-address-dedup-and-damages-attribution.md): the "53 homes" figure is now a fully explained, primary-document-grounded number, not a loose estimate.** Section V (¶¶94-252) pairs each of exactly **53 named-plaintiff/household paragraph-groups** (summing to exactly 80 named plaintiffs — programmatically verified) with an "owned a home/homes at" sentence. But **6 of those 53 groups plead two separate street addresses each** (Cooney ¶136; Gaviria/Rodriguez ¶160; Ortiz ¶214; Robertson ¶229; Tillman ¶241) and **one (Pena, ¶217) pleads one street address with two distinct condo units** — so the complaint's own text supports **58-59 distinct residential properties** (59 if the two Pena units are counted separately; 58 if treated as one building), not 53. No exact duplicate addresses found among any of the 53 groups (checked programmatically). **"53" is very likely a count of Section V's paragraph-groups/households, not of distinct properties** — Texas Tribune's own May 1, 2026 wording ("The plaintiffs own 53 homes ... including several couples who shared homes") matches this exactly: it explains why 80 plaintiffs collapses to 53, but doesn't account for the 6 groups that own two homes each. Treat "53 homes" as press shorthand for "53 household/plaintiff-groups," and 58-59 as the more defensible distinct-property count if a specific number is needed in manuscript text. **Damages-figure sourcing also resolved 2026-09-18**: the "$100,000 foundation repair" figure traces to a **named plaintiff's own on-record interview with Reuters** ("One plaintiff showed Reuters her home in Port Isabel... She estimates $100,000 in foundation repairs, more than the home is currently worth" — picked up by TheNextWeb and Futurism, both of which cite Reuters as the source) — **not** an attorney statement as the 09-16 note guessed, and not in the complaint. The "~$10 million" damages figure could not be traced to either the complaint or an identifiable attorney quote/press release in the outlets checked (RGV Business Journal states it as unattributed reporter narration: "The plaintiffs are seeking more than $10 million in damages," no source cited in-article); its ultimate origin remains unresolved. Also note: press headcounts for this case are inconsistent across outlets — MyRGV/Texas Tribune say "53 homes," RGV Business Journal says "more than 70 homeowners," TheNextWeb/Futurism/IBTimes say "80 residents/plaintiffs" — only the 80-plaintiff and 53-household-group counts are independently confirmed from the primary document. | [CourtListener docket 73273866](https://www.courtlistener.com/docket/73273866/aguilar-v-space-exploration-technologies-corporation/), [complaint PDF](https://storage.courtlistener.com/recap/gov.uscourts.txsd.2082161/gov.uscourts.txsd.2082161.1.0_1.pdf) |
| 19 | Texas Commission on Environmental Quality (TCEQ) | Agreed Order, Docket No. 2024-1282-IWD-E — state-level enforcement action against SpaceX (Starbase) for discharging industrial wastewater without authorization (30 Tex. Admin. Code §305.42(a)), documented via TCEQ record review July 25-30, 2024; distinct from the $148,378 federal EPA CWA penalty (row 10) | violation documented July 2024; Respondent agreed to Order terms Aug. 13, 2024 | **A — primary-verified 2026-09-04** (see notes/2026-09-04), re-confirmed still resolving 2026-09-18 (HTTP 200, 13,331,483 bytes, same file). **Total administrative penalty: $3,750** ($750 deferred contingent on compliance; $3,000 actually paid) — matches the news-reported $3,750 figure exactly, now primary-document-confirmed rather than search-snippet-tier. Same admission-avoidance language as the EPA CAFO ("entry of this Order shall not constitute an admission... of any violation"). The same multi-document PDF also contains an Oct. 1, 2024 public comment (Save RGV, Carrizo/Comecrudo Nation of Texas, South Texas Environmental Justice Network, Clean Water Action) calling the $3,750 penalty "absurdly low" — same recurring coalition as the 2026 land-exchange suit (row 14) and TCEQ contested-case filing (row 12), useful primary evidence of coalition continuity across years/proceedings. **Correction to the record**: this row did not previously exist in the table despite being fully primary-verified 2026-09-04 — the "What's still needed" list's item 4 wrongly carried this as open through 09-16; a stale-tracking-item bug of the same kind already fixed for row 7's tier field, now fixed here. | [tceq.texas.gov agenda-backup PDF](https://www.tceq.texas.gov/downloads/agency/decisions/agendas/backup/2024/2024-1282-iwd-e.pdf) |
| 16 | Texas Legislature (SB 1198, 89th Leg., Regular Session) | Enacted statute amending Texas's critical-infrastructure-facility law (Gov't Code Ch. 423/424 family) to explicitly cover any FAA-licensed spacecraft launch/landing/recovery/testing facility, or any facility run by a Ch. 507 spaceport development corporation — enhanced criminal/civil trespass liability; covers Starbase by name in contemporaneous coverage, alongside Midland International's spaceport, Houston Spaceport, and Blue Origin's Van Horn site | filed 02/10/2025; signed by Governor 06/20/2025; effective 09/01/2025 | A for bill history/caption/author/dates (fetched directly from capitol.texas.gov's own bill-lookup page 2026-09-20) — resolves this row's prior open item (previously sourced only to SOTXEJN's own petition post, not independently verified against the actual statute). Enrolled bill text itself not yet read line-by-line. Timing is consistent with (not contradicted by) SOTXEJN's July 2026 felony-trespass-exposure concern, since SB 1198 took effect before that post. | [capitol.texas.gov bill history](https://capitol.texas.gov/BillLookup/History.aspx?LegSess=89R&Bill=SB1198) |
| 20 | Cameron County District Court (404th District, TX) | Cards Against Humanity v. SpaceX — land-trespass civil suit; CAH bought a Cameron County parcel in 2017 (anti-border-wall publicity purchase, ~150,000 crowdfunders) and sued SpaceX ~Sept. 2024 alleging unauthorized construction-material/vehicle storage and gravel dumping on the property; sought $15M | filed ~09/19-21/2024; settled 10/20/2025, days before a scheduled 11/03/2025 trial | A-minus — every fact fetched directly from CBS News Texas, TechCrunch, and Bellingcat's own reporting (Bellingcat's satellite-imagery analysis independently corroborates construction activity on the specific parcel, lot 11, 41176 Tarpon Bend Dr., Brownsville, TX, from ~June 2023). CAH's own settlement statement: "SpaceX admitted during the discovery phase of the case to trespassing on its property." Settlement terms otherwise undisclosed (no cash payout to crowdfunders; a novelty card pack instead, per TechCrunch). Underlying court filing/case number not independently located — Cameron County District Court docket was not accessible with this session's tooling; Houston Chronicle's direct account (likely richest primary detail) returned HTTP 403. Distinct from the Aguilar acoustic-damage suits (row 18) — a land-boundary/encroachment dispute, not a noise-nuisance claim, useful for the "does the company respect the property lines it claims to respect" ex-post comparison thread. | [CBS News Texas](https://www.cbsnews.com/texas/news/cards-against-humanity-elon-musk-spacex-settlement-alleged-trespassing-texas/), [TechCrunch](https://techcrunch.com/2025/10/20/cards-against-humanity-settles-trespass-lawsuit-against-spacex/), [Bellingcat](https://www.bellingcat.com/news/2024/10/22/spacex-vs-cards-against-humanity-satellite-imagery-shows-activity-on-land-at-centre-of-legal-case/) |
| 21 | U.S. District Court, S.D. Tex. (Brownsville Div.) | *Aguilar* docket (case 1:26-cv-00485) — procedural update beyond row 18's complaint-text read: full docket entry list fetched directly 2026-09-25 (CourtListener, 35 entries as of that date). Plaintiffs filed a **First Amended Complaint** (Dkt. 23, filed 2026-07-29; fetched and read directly — still **no dollar-figure damages pleaded anywhere**, same "$" search-count of 2, both the "$1.75 trillion" SpaceX IPO-valuation reference, as the original complaint). SpaceX then filed a **second Rule 12(b)(6) motion to dismiss** (Dkt. 29, filed 2026-08-12, fetched and read directly) targeting the amended complaint's non-economic-damages claim specifically, arguing Texas law generally bars property-based noneconomic damages absent pleaded malice/ill-will and that plaintiffs' trespass theory doesn't support such damages either; SpaceX asks for dismissal **with prejudice**. This motion is now **fully briefed**: plaintiffs' Response in Opposition (Dkt. 33, 2026-09-09) and SpaceX's Reply in Support (Dkt. 35, 2026-09-23 — two days before this entry) are both docketed, text not yet extracted (no free RECAP copy uploaded for these two entries; "Buy on PACER" only). An "Order Resetting Initial Conference" (Dkt. 34, 2026-09-22) also appears. **No ruling on the motion to dismiss yet.** | docket entries through 2026-09-23; fetched/read 2026-09-25 | **A** for the amended complaint's text (no dollar figures) and the first MTD's own argument (fetched/read directly); **B** for the existence/dates of the response and reply (docket-entry metadata only, text not yet pulled) | [CourtListener docket 73273866](https://www.courtlistener.com/docket/73273866/aguilar-v-space-exploration-technologies-corporation/), [Amended Complaint PDF](https://storage.courtlistener.com/recap/gov.uscourts.txsd.2082161/gov.uscourts.txsd.2082161.23.0_1.pdf), [Second MTD PDF](https://storage.courtlistener.com/recap/gov.uscourts.txsd.2082161/gov.uscourts.txsd.2082161.29.0.pdf) |
| 22 | City of Starbase, TX (official page) + San Antonio Express-News/Statesman + RGV Business Journal | **7,133-acre annexation**, finalized 2026-09-21 — expands the city's territory roughly sevenfold, from ~1,000-1,100 acres to ~8,100 acres. Land composition per the Express-News's own property-records analysis (published 2026-02-14, when the proposal was first up for a commission vote): ~3,700 acres federally owned, ~1,000 acres Texas Parks & Wildlife Dept. property, ~2,400 acres private/corporate (incl. SpaceX and affiliated shell companies) — much of it falling within the boundaries of the **Lower Rio Grande Valley National Wildlife Refuge** (distinct from the separate 775-acre refuge land-exchange proposal already in this corpus, row 14's related litigation). USFWS and TX Parks & Wildlife both stated the annexation itself doesn't change land ownership/management. City officially frames it as a **"C-4" annexation — consent-based under Texas law**, requiring landowner petition/agreement (per starbase.texas.gov's own C-4 annexation page, fetched directly); RGV Business Journal's finalization coverage (fetched directly, 2026-09-23) describes it as "not requested or voluntary," noting only ~12 of 280 affected property owners signed in support, which the city clerk (Gretchen Norton) disputed, saying an involuntary-annexation acreage cap doesn't apply here. **Relevant precedent found in the same Express-News piece**: a 2024 land-swap proposal (43 acres to SpaceX for 477 acres near Laguna Atascosa NWR) was abandoned by SpaceX after public outcry and a lawsuit — a concrete counter-example to a "opposition never works" reading of this corpus, worth keeping for balance. Also notes TX Parks & Wildlife approved sale of 1.9 acres of state park land within city boundaries in Aug. 2025 "despite heavy public criticism." | proposal first noticed ~2026-02-14; finalized 2026-09-21 | A (official city page + two independently-outletted news accounts fetched directly, one via proxy) for the general facts; **B** for the "not requested or voluntary" vs. "consent-based" framing dispute itself, which rests on the city's own page vs. RGV Business Journal's characterization and hasn't been reconciled against the actual annexation ordinance/petition-signature record | [starbase.texas.gov/c-4-annexation](https://www.starbase.texas.gov/c-4-annexation), [Statesman/Express-News, 2026-02-14](https://www.statesman.com/business/article/spacex-starbase-annexation-wildlife-refuge-21352531.php), [RGV Business Journal, 2026-09-23](https://www.rgvbusinessjournal.com/news/23/09/2026/spacexs-futuristic-city-of-starbase-finalizes-massive-7100-acre-annexation-heres-what-we-know/) |
| 23 | NPR / Gulf States Newsroom (Drew Hawkins, byline) | "SpaceX has big plans for a new Louisiana 'Star Base,' worrying some near there" — broadcast/transcript, direct on-record quote from **Gov. Jeff Landry** explaining the NDA practice when asked by the reporter ("You think I want Texas to steal my thunder? You think I want other states to know what we're working on?"); on-record resident voices not previously in this corpus — **Gabe Giffin** ("Gator Gabe," outdoor-education guide, Pecan Island) on Mississippi-Flyway migratory-bird habitat concerns and on officials "not telling the people what's coming," and **Brooke Broussard** (Pecan Island bartender) on cultural/place-based loss. Independently re-confirms figures already in the corpus (3,000 new LA jobs/10-yr, aerospace liability/tax legislation, NDAs "become common... under Landry," construction end-2027, first launch 2029) via a fully independent outlet/reporting chain, not a re-source of LED's own materials. | published/aired 2026-09-20 | A (full transcript fetched and read directly) | [npr.org/2026/09/20/nx-s1-5974180](https://www.npr.org/2026/09/20/nx-s1-5974180/spacex-musk-landry-louisiana-ndas), [transcript](https://www.npr.org/transcripts/nx-s1-5974180) |

## Update — 2026-09-08 (see notes/2026-09-08-tceq-vote-confirmed-opic-split-boca-chica-expansion-vermilion-rv-ordinance.md)

- **Row 6i (Act 343/HB1250) UPGRADED B → A.** The enrolled bill text was fetched directly from
  `legis.la.gov` and read (`pdftotext`): it creates a "special motion to strike" for claims against
  any "aerospace flight entity" (broadly defined), with automatic discovery stay and attorney-fees
  to the prevailing party on the motion — an anti-SLAPP-style mechanism. Confirms, with the
  statute's own text, the news-sourced characterization already in the corpus.
- **New row 6m** (Vermilion Parish side): Vermilion Parish Police Jury RV-park moratorium/ordinance,
  driven explicitly by anticipated spaceport-worker housing demand — Modern Campground news article
  (2026-09-04, fetched directly) plus the Police Jury's own Aug. 19, 2026 meeting agenda (fetched
  directly from `vppj.org`), which confirms the Finance Committee's moratorium recommendation in the
  parish's own words. Names Parish Administrator Keith Roy and Councilman Scott Broussard; a
  follow-up Police Jury meeting was scheduled for Sept. 16, 2026. Tier A (both the news article and
  the parish's own agenda document). A genuinely new local-governance/second-order-cost angle, not
  previously in the corpus.
- **New row 14** (Boca Chica): **Center for Biological Diversity et al. v. FAA, Case No.
  1:23-cv-01204** (D.D.C., filed May 1, 2023) — a NEPA challenge to FAA's 2022 approval of increased
  Starship/Super Heavy launch cadence at Boca Chica, distinct from the 2026 land-exchange suit
  already in the corpus. Primary-verified via the actual CourtListener docket: Judge Carl J. Nichols
  signed a Memorandum Opinion and Order on Sept. 15, 2025 denying plaintiffs' partial summary
  judgment motion and granting the government's and SpaceX's cross-motions — i.e., the environmental
  groups lost on the NEPA claim's merits (news coverage calls this "dismissed," which is imprecise;
  docket activity continued into Dec. 2025). Save RGV joined this case as a plaintiff via a July
  2025 amended complaint — another point of overlap with the recurring Boca Chica coalition already
  tracked in this corpus. Tier A (primary docket).
- **Row 13 (SOTXEJN v. TCEQ, Travis County) status update**: the actual court portal was identified
  tonight (`odysseyweb.traviscountytx.gov/Portal/`) but is a cookie/JS-gated search application this
  session's tooling cannot query — a more precisely diagnosed access barrier than prior nights'
  generic 502s, still unresolved.
- **New row 15**: SOTXEJN's Sept. 5, 2026 blog post confirming a **formal joint FAA comment** filed
  together with the Vermilion Parish `@stopspacex` group, SouthWings, the Southern Environmental Law
  Center, and the National Parks Conservation Association, opposing the FAA-2026-8614 waiver NPRM —
  direct primary-source evidence that the two sites' opposition coalitions are actively coordinating,
  not just structurally comparable. The underlying joint comment document itself is Google-Drive
  hosted and not yet text-extracted (JS-viewer limitation). Tier A for the fact/framing of the
  partnership (SOTXEJN's own statement); Tier B for the comment's actual text.
- **New row 16**: SOTXEJN's July 15, 2026 petition post, which describes Starbase, TX's designation
  under Texas's Critical Infrastructure law — entering the town "could" mean felony arrest exposure.
  A useful direct comparison to Vermilion Parish's own state-level legal-protection package (Acts
  874/343): one site criminalizes entry, the other shields the company from suit. Tier A (SOTXEJN's
  own statement; the underlying "critical infrastructure" designation itself not independently
  verified against the Texas statute or a state registry tonight).
- **TCEQ Docket 2024-1821-IWD update**: the Commission's 3-0 vote approving the permit (Feb. 13,
  2025) is now confirmed via a directly-fetched San Antonio Current article (byline Sanford Nowlin,
  2026-02-18), not just secondary corroboration. A new nuance: TCEQ's own Office of Public Interest
  Counsel (OPIC) — fetched directly, `2024-1821-iwd-picr.pdf` — recommended the *opposite* of the
  Executive Director, i.e. granting a contested-case hearing to the three organizational requestors;
  the Commission's 3-0 vote followed the ED, not OPIC. The literal signed order document remains
  structurally unlocated (TCEQ's permit-search tool is a JS single-page app this session's tooling
  cannot drive).
- No theory chain, coding scheme, or Study 1 option decided — same standing rule as before.

## Update — 2026-09-05 (see notes/2026-09-05-faa-quiet-nda-document-and-osprey-loi-found.md)

- **Row 7 (Cameron County $800M claim) UPGRADED B → A.** The county's own two-page PR PDF was
  fetched directly (`curl`, HTTP 200) and extracted with `pdftotext`:
  [cameroncountytx.gov PR PDF](https://www.cameroncountytx.gov/wp-content/uploads/2024/06/2024.6.18-STARBASE-LOCAL-IMPACT-PR-2.pdf).
  Confirms $800M+ state/local capital income & indirect business tax figure verbatim, plus a fuller
  stat set (see notes file) not previously in this table: $3B+ SpaceX infrastructure investment,
  $6.5B+ annual gross economic market value, 3,400+ FTE employees/contractors, 21,400+ indirect
  jobs, $99M+ 2025 tourism impact, quote from Cameron County Judge Eddie Treviño Jr.
- **New row 11**: U.S. Fish and Wildlife Service, final Biological and Conference Opinion (BCO),
  Consultation No. 02ETCC00-2012-F-0186-R001, dated May 12, 2022 — the federal ESA Section 7
  review for FAA's permit/license issuance to SpaceX at Boca Chica, covering ocelot, jaguarundi,
  aplomado falcon, four sea turtle species, piping plover, and red knot. Conclusion (read directly):
  "not likely to jeopardize the continued existence of the species." Directly fetched (`curl` +
  `pdftotext`, 5.9MB, HTTP 200) from [fws.gov](https://www.fws.gov/sites/default/files/documents/5-12-2022%20SpaceX%20Final%20BCO_signed%20with%20appendix%20A-D.pdf).
  Tier A. A 2023 addendum and a 2025 "Amended BCO Addendum #2" reportedly exist (per search
  snippets only) — not fetched tonight, a lead for a future session on how the environmental review
  evolved as Starbase's launch cadence increased.
- **New row 12**: SpaceX's own filing, TCEQ Docket No. 2024-1821-IWD ("Space Exploration
  Technology Corporation's Response to Requests for Contested Case Hearing and Requests for
  Reconsideration," filed Jan. 17, 2025) — SpaceX's own legal argument that STEJN, the
  Carrizo/Comecrudo Nation, and Save RGV lack associational/affected-person standing to contest its
  new TPDES wastewater permit (WQ0005462000). This is a distinct TCEQ docket from the
  2024-1282-IWD-E agreed-order penalty already in the corpus (09-04) — same recurring coalition,
  different proceeding. Directly fetched (`curl` + `pdftotext`, HTTP 200, 1724 lines). Tier A.
  [tceq.texas.gov PDF](https://www.tceq.texas.gov/downloads/agency/decisions/agendas/backup/2024/2024-1821-iwd-appr.pdf)
- **New row 13**: South Texas Environmental Justice Network's own press release (its site,
  directly fetched, HTTP 200), Dec. 18, 2024 — announcing a **separate lawsuit**, filed Dec. 16,
  2024 in Travis County (TX) District Court, by SOTXEJN + the Carrizo/Comecrudo Tribe (represented
  by Perales, Allmon & Ice, P.C.) against TCEQ itself (not SpaceX), arguing TCEQ exceeded its
  authority by using an agreed order to authorize continued discharge in lieu of requiring a permit.
  Named: Bekah Hinojosa (SOTXEJN), Juan Mancias (Tribal chairman), Attorney Lauren Ice. A third,
  distinct Boca Chica legal action by the same recurring coalition (alongside the 2026 federal
  land-exchange suit and the TCEQ contested-case-hearing filing above). Case number/docket and
  outcome **not yet independently verified against a Travis County court record** — flag before
  citing. Tier A for the press release itself (org's own statement); B for the underlying suit's
  procedural facts pending a docket check. [sotxejn.org](https://sotxejn.org/2024/12/18/rio-grande-valley-organizations-sue-the-tceq-for-bypassing-permitting-in-favor-of-spacex/)
- **New row 6j** (Vermilion Parish side): Louisiana Economic Development's own "Letter of Intent
  for Project Osprey," dated July 10, 2026, addressed to "Ben Lancaster, Senior Manager,
  Governmental Affairs" — LED's negotiating document, released via public-records request and
  hosted directly by Louisiana Illuminator. States a **Total Potential Value of $27.544 billion**:
  $23.852B PILOT (25-yr property-tax abatement in exchange for $25M/yr + $20M one-time payment,
  matching figures already in the corpus), $3.663B Aerospace Facilities/Activities sales-tax
  rebate, plus smaller HIP/FastStart items. Confirms the $25M charitable donation to the Community
  Foundation of Acadiana (matching LED's public figure) and contains **no line item for a "$100M
  coastal master plan"** — consistent with, and now more strongly evidenced than, the 08-29 note's
  finding that the $100M figure is a separate verbal press-conference commitment, not part of LED's
  written incentive package. This is the single most consequential fiscal find of any night so
  far for the paper's economic-benefit-claim-specificity frame: LED's *own written document* values
  the deal at $27.5B, dwarfing the figures ($25M/yr, $20M, "800M+") emphasized in LED's public
  messaging and most news coverage. Directly fetched (`curl`, HTTP 200, 1.78MB PDF, `pdftotext`
  extraction). Tier A. [lailluminator.com PDF](https://lailluminator.com/wp-content/uploads/2026/09/LOI-Project-Osprey.pdf)
- **New row 6k**: WWNO/Gulf States Newsroom (Drew Hawkins), "Inside Louisiana's $100 billion
  SpaceX deal: NDAs, record tax breaks and a community left out," published 2026-09-02, directly
  fetched (`curl`, HTTP 200, no proxy needed). New named individuals beyond Sagrera/Broussard/
  Miller: **Kim Nehrbass and his wife Libby Smith** (Pecan Island camp owners; Smith held a
  "Sportsman's Paradise" protest sign at the Aug. 25 announcement), **Gabe Giffin** (outdoor
  educator, Mississippi Flyway/bird-habitat concern), and **Hollie Girouard** (named once, in a
  photo caption alongside Broussard and Giffin, role not otherwise described in the fetched text).
  Confirms the SpaceX deal's NDA codename was **"Project Osprey"** and reports "dozens of local and
  state officials" signed NDAs (not just the two — Rep. Jacob Landry, Sen. Bob Hensgens — already
  named in the corpus), traced to the same Gulf States Newsroom NDA-pattern investigation that
  covered the Meta/Richland Parish deal. Tier A. [wwno.org](https://www.wwno.org/economy/2026-09-02/inside-louisianas-100-billion-spacex-deal-ndas-record-tax-breaks-and-a-community-left-out)
- **New row 6l**: the actual Feb. 1, 2026 NDA signed by State Rep. Jacob J. Landry with LED —
  located on DocumentCloud (an 8-page filing). WebFetch confirmed the document's metadata (date,
  parties, page count) directly from the page; full-text extraction was **blocked** — both
  `documentcloud.org` and `assets.documentcloud.org` returned Cloudflare 403s to direct `curl`, and
  the `r.jina.ai` reader proxy used elsewhere tonight returned an "AuthenticationRequiredError...
  bad IP reputation" error specifically for this domain (worked fine for other domains the same
  session) — a new, domain-specific failure mode, not the familiar site-level 403. Tier B (metadata
  confirmed, full text not yet extracted) pending a future session with a different fetch path.
  [documentcloud.org/documents/28476037](https://www.documentcloud.org/documents/28476037-20260201-led-nda-jacob-j-landry-state-representative/)
- No theory chain, coding scheme, or Study 1 option decided — same standing rule as before.

## Update — 2026-09-01 (see notes/2026-09-01-faa-docket-post-deadline-close-and-aerospace-liability-shield-laws.md)

- **FAA docket (#5) — comment period now CLOSED**, confirmed post-deadline (~1h15m after the
  2026-09-01T03:59:59Z close): `openForComment: false`. **Comments posted jumped from 1,453
  (08-30/08-31) to 2,785** — a late-breaking surge, ~1,332 of which posted in the final 72 hours.
  **Comments received (incl. not-yet-posted backlog): 14,669** — do not treat this as a readable/
  codable count; only the 2,785 posted are currently accessible. "Vermilion"-mentioning comments
  rose from 141 to 345. No filing found under "StopSpaceX," "Hensgens," or "police jury" even
  post-surge.
- **New rows 6g-6i added**: Louisiana's 2026 aerospace liability-shield legislative package (Act
  874/HB1098, companion Act 343/HB1250, and a public-records exemption for aerospace company
  records) — directly relevant to the regulatory-venue-shifting frame candidate (a federal review
  waiver paired with a state liability shield whose main carve-out is FAA-license compliance) and
  to the Boca-Chica-precedent-awareness frame candidate (legislators cited an active 2026 Texas
  homeowner lawsuit over Starbase-related home damage as their explicit reason for acting).
- No theory chain, coding scheme, or Study 1 option decided — same standing rule as before.

## What's still needed before this is a workable Study 1 corpus

1. ~~Extract the FAA comment-letter PDF's actual text (#4)~~ — DONE 2026-08-29.
2. ~~Confirm the FAA-2026-8614 docket number directly (#5)~~ — DONE 2026-08-29 (Federal Register
   PDF via govinfo.gov); docket status (open/closed, comment count) re-checked as recently as
   2026-08-31, see notes for that date.
3. ~~Identify the actual Boca Chica community-impact study (#9)~~ — DONE 2026-08-30 (Palacios
   thesis).
4. ~~The $3,750 TCEQ state-level fine~~ — actually already resolved 2026-09-04 (row 19); this list
   item was stale (never updated after that session) and was corrected 2026-09-18.
5. Once Britton picks a Study 1 option (A/B/C from the orientation note), this table's scope
   narrows accordingly — right now it's deliberately broad across both corporate and opposition
   material.
6. ~~Rows 6g-6i (added 2026-09-01): Act 343/HB1250's enrolled text~~ — this item was itself stale;
   row 6i's table entry already shows Tier A (enrolled text fetched directly 2026-09-08), so this
   half of the item is done. The aerospace public-records-exemption bill's enrolled text (a
   separate bill from 6g-6i, mentioned in row 6h's news coverage) was not checked tonight and may
   still be B-tier/news-sourced only — not independently re-verified in this pass, flagging rather
   than assuming either way.
7. The FAA docket's 2,785 posted / 14,669 received comment-surge (2026-09-01) is quantified but
   not yet characterized — a sample read of newly-posted comments (organic vs. form-letter,
   who's filing) is still open.
8. ~~Row 7's stale Tier field~~ — FIXED 2026-09-16.
9. ~~2025/2026 Cameron County/SpaceX economic-impact figures (row 7b)~~ — RESOLVED 2026-09-16 via
   Wayback Machine (see row 7b for the exact fetch recipe).
10. ~~Aguilar v. SpaceX complaint damages/prayer-for-relief section~~ — READ 2026-09-16 (row 18);
    resolved as a correction, not a confirmation — the $10M/foundation-repair figures aren't in the
    complaint itself. ~~The "53 homes" figure~~ — RESOLVED 2026-09-18 (row 18): "53" = household-
    group count (80 plaintiffs, 53 groups), but 58-59 distinct properties by the complaint's own
    text.
11. **The ~$10 million total-damages figure's ultimate source is still unresolved** (carried
    forward from 09-18) — not the complaint, not an identifiable attorney statement in anything
    checked across three sessions now (09-16, 09-18, 09-25). A direct `reuters.com` URL for the
    original story that TheNextWeb/Futurism cite for the "$100K foundation repair" figure still
    hasn't surfaced in WebSearch results (tried again 09-25, same negative result as 09-18) — only
    outlets citing Reuters secondhand. Recommend not re-trying the same WebSearch approach a fourth
    time; if this matters for a manuscript claim, it likely needs a Reuters.com site search or
    subscription access a future session doesn't have.
12. **New 2026-09-25: SpaceX's second motion to dismiss (row 20, Dkt. 29) is fully briefed as of
    2026-09-23 but unruled-on.** Worth a future session pulling the Response in Opposition (Dkt.
    33) and Reply (Dkt. 35) text once a free RECAP copy exists (neither had one as of 09-25; both
    are "Buy on PACER" only, and this project's convention has been not to spend money) — or simply
    re-checking the docket periodically for a ruling, which would be a genuinely new, citable
    development (a federal court's live application of Texas noneconomic-damages law to a
    Starship-litigation fact pattern).
13. **New 2026-09-25: the Starbase 7,133-acre annexation's "consent-based" vs. "not
    requested/voluntary" framing dispute (row 21) is unreconciled** — rests on the city's own
    general description of C-4 annexation law vs. one outlet's characterization of this specific
    annexation's signature count. The actual annexation ordinance/petition record (referenced on
    `starbase.texas.gov/c-4-annexation` as available documentation — "parcel list, map, voluntary
    petition form") was not itself fetched 2026-09-25; would resolve this directly.
14. **Travis County suit (D-1-GN-24-010020, SOTXEJN/Carrizo-Comecrudo v. TCEQ) — still a genuine
    access-blocked gap, re-attempted and re-confirmed unresolved 2026-09-25.** One new hazard
    found and flagged, not resolved: a WebSearch for this case surfaced a **different, unrelated**
    TCEQ case — *South Texas Environmental Justice Network v. TCEQ*, a Third Court of Appeals
    (Austin) ruling on a natural-gas-terminal permit, dismissed for lack of subject-matter
    jurisdiction — that shares a party name (STEJN) but is not the SpaceX wastewater-permit suit
    this project tracks. Flagging explicitly so a future session doesn't mistake that ruling for a
    resolution of this open item, the same false-positive pattern the 09-07 note already caught
    once for a different case pair.

## Update — 2026-08-31 (see notes/2026-08-31-faa-docket-deadline-check-and-boca-chica-cwa-verification.md)

- Row 9 updated with the Palacios thesis citation (resolved 08-30, corpus table not updated until
  now).
- New row 10 added: the actual EPA CWA enforcement record (CAFO, Docket CWA-06-2024-1768) against
  SpaceX's Boca Chica facility — fetched and read directly, upgrading the CWA-violation claim from
  "commenters state" (as it stood in rows 4 and the FAA-docket notes) to independently primary-
  verified.
- FAA docket (#5) re-checked same-day as the (real) comment-period deadline: as of ~05:17 UTC
  2026-08-31, the docket was still open (`commentEndDate: 2026-09-01T03:59:59Z`, i.e. 11:59:59 PM
  ET tonight), total comments still 1,453 (unchanged from 08-30), nothing newly posted since
  2026-08-28. A true post-close check is still outstanding.

## Update — 2026-08-29 primary-source pass

See `notes/2026-08-29-primary-source-pass-and-discrepancy-resolution.md` for full detail. Summary
of what changed in this table:
- **#4 (FAA comment letter) and #5 (FAA docket) both upgraded C/B → A.** Working PDF text
  extraction (poppler-utils `pdftotext`) was available this session; both documents were pulled
  and read in full, not paraphrased from search snippets.
- **New rows 6b-6f added**: local-resident opposition/transparency material (NDAs signed by
  elected officials, "StopSpaceX" group, direct resident quotes) that the earlier corpus pass
  didn't have — this is genuinely new Option-B-relevant material, distinct from the wildlife-group
  filing angle already in the table.
- **The $25M vs. $100M discrepancy flagged on 2026-08-27 is now resolved** (moderate-high
  confidence): both figures are real and distinct. See the dedicated notes file for sourcing and
  reasoning — not restating the full analysis here to avoid the table drifting out of sync with
  the notes file.
- No theory chain, coding scheme, or Study 1 option decided — same standing rule as before.
