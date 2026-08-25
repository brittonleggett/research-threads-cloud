# 2026-08-25 — Texas deep-dive, Coweta Sail/Peach disambiguation resolved, litigation re-check

## WebFetch status — still blocked, 13th+ consecutive session
Tested tonight against `en.wikipedia.org` (standing neutral control): `EGRESS_BLOCKED`, same failure
mode as every prior night. Did not bother re-testing additional domains since the pattern is now
well-established (12-13 straight sessions, confirmed domain-agnostic as of 08-24). Everything below
is WebSearch-summarized only — flagged inline wherever a fact rests on a single source or a
search-engine-generated synthesis rather than a direct read of the underlying article. Recommend,
again, that the proxy/egress config get checked directly rather than continuing to note this nightly.

---

## 1. Texas deep-dive (the flagged priority target) — much bigger than 08-24's shallow pass showed

08-24 flagged Texas as a newly-discovered, uncovered state based on two items (Fort Worth's Aug 11
vote, the statewide ERCOT/PUC audit). Tonight's deeper pass found Texas is a genuinely major,
multi-front national-scope case — more comparable in scale to Georgia or Louisiana than to a
single-item state. Confirmed via grep before starting that none of this is already in the corpus or
prior notes.

### State level: ERCOT/PUC audit, more precisely dated than 08-24 had it
- Gov. Abbott's audit directive: **Aug. 3, 2026**. Follows an earlier **June 10, 2026** Abbott
  directive to PUCT/ERCOT to act on data-center-driven energy-cost concerns — so this is an
  escalation of a months-long state posture, not a one-off. [Texas Tribune](https://www.texastribune.org/2026/08/03/texas-data-center-project-audit-greg-abbott/)
- The 250-300 project figure and audit scope were detailed at a **PUCT open meeting on Aug. 14**
  (not Aug. 20 as 08-24 had it — Aug. 20 was a separate, follow-on meeting). ERCOT separately
  suspended "Batch Zero Large Load classification" notifications that had been scheduled for Aug. 7,
  seeking a "good cause exception" at the Aug. 20 meeting. ERCOT states it intends to complete the
  audit of "hundreds" of projects **by December 10, 2026**. Audit disclosure requirements: tax
  incentives/abatements, power procurement and any self-generation, water source/volume/cooling tech,
  community engagement, and ownership/controlling interests. Well-corroborated: [Texas Tribune](https://www.texastribune.org/2026/08/14/texas-data-center-approval-pause-ercot-power-grid/), [Utility Dive](https://www.utilitydive.com/news/ercot-texas-puc-data-center-audit/828472/), [KERA (Aug 21)](https://www.keranews.org/texas-news/2026-08-21/ercot-says-it-plans-to-complete-governors-data-center-audit-by-december), plus law-firm client alerts from Greenberg Traurig, Gibson Dunn, White & Case, and Troutman Pepper (unusual density of legal-industry coverage — a signal this is seen as a significant regulatory event, not routine).

### Local level: at least five distinct Texas jurisdictions in play, not just Fort Worth
- **Fort Worth** — Aug. 11 vote. Correction/refinement to 08-24's "unanimously (7-0)" framing:
  Fort Worth's council has **10 district members + an at-large mayor**. The vote to *begin the
  moratorium process* was reported as unanimous, but I could not confirm the exact numeric tally
  (10-0? fewer present?) from search snippets alone — **treat "unanimous" as confirmed, the specific
  vote count as not yet nailed down**. A **separate same-meeting vote, 10-1, created the Fort Worth
  Data Center & Infrastructure Commission (DCIC)**; another ordinance (Chapter 14, data-center grid
  interconnection filings) also passed 10-1. If the exact moratorium-process tally matters for the
  write-up, it needs a primary-source pull (council minutes) once WebFetch works. Moratorium would
  take effect ~Feb. 16, 2027 pending required state procedural steps. [Fort Worth Report](https://fortworthreport.org/2026/08/12/data-center-moratorium-takes-first-steps-after-fort-worth-city-councils-unanimous-vote/), [KERA](https://www.keranews.org/news/2026-08-12/data-center-moratorium-takes-first-steps-after-fort-worth-city-councils-unanimous-vote)
- **San Marcos — first Texas city to ban data centers outright, and it's already done, not just
  proposed.** Council voted **4-3 on June 16, 2026** to amend its Land Use Matrix and prohibit data
  centers in **every** zoning district (part of a broader development-code overhaul, Ordinance
  2026-08). Unlike Fort Worth's temporary 90-day process, this is **indefinite**, already in effect,
  and the closer of a 4-3 vote signals real local political division (not unanimous like Fort Worth).
  [Texas Tribune](https://www.texastribune.org/2026/06/30/texas-san-marcos-data-center-ban-zoning-laws/), [Community Impact](https://communityimpact.com/austin/san-marcos-buda-kyle/government/2026/06/17/san-marcos-council-votes-to-prohibit-data-centers-in-all-zoning-districts/)
- **Hill County — the single most theoretically interesting Texas finding tonight: a moratorium
  passed, then reversed under a developer damages lawsuit, with a documented chilling effect on a
  second county.** Hill County (pop. ~35,000, north of Waco) passed a one-year moratorium on
  unincorporated-area data-center construction in **May 2026** — the first Texas *county* to do so.
  Developer **RCM Hill, LLC** filed a federal lawsuit **23 days later** seeking **$100 million** in
  damages, citing ~$1M already spent on 800+ acres for a planned data center. The Commissioners
  Court voted unanimously to **rescind the moratorium on June 4, 2026** (about two weeks after
  passing it) and adopted a "Data Center Development Checklist" (developer disclosure requirements
  on infrastructure/traffic/water/resources) in its place. RCM Hill dismissed its suit with prejudice
  July 9, 2026, after the county agreed to pay **$100,000** in the developer's legal fees. **A
  documented ripple effect: Tom Green County (West Texas) dropped its own planned moratorium as a
  direct result of watching Hill County's lawsuit outcome** — per MultiState's Aug. 19 case-study
  writeup. This is a clean, well-corroborated, concrete instance of a new mechanism not yet in the
  paper's theme vocabulary: **litigation-driven regulatory reversal / inter-jurisdictional chilling
  effect** — a local government's opposition-responsive policy defeated not by the courts ruling
  against it on the merits, but by the *cost exposure of litigation itself* forcing a retreat before
  any ruling, which then deters a neighboring jurisdiction from even trying. Multiple independent
  outlets: [Texas Tribune](https://www.texastribune.org/2026/06/05/texas-hill-county-moratorium-rescinded-data-centers/), [KERA](https://www.keranews.org/energy-environment/2026-06-05/hill-county-drops-data-center-moratorium-after-lawsuit-adopts-new-review-requirements), [Route Fifty](https://www.route-fifty.com/artificial-intelligence/2026/06/texas-county-rescinds-its-data-center-moratorium-after-100-million-lawsuit-developer/414022/), [KWTX (x2, incl. the July dismissal)](https://www.kwtx.com/2026/07/15/hill-county-dropped-its-data-center-ban-after-100-million-lawsuit-now-developer-has-dismissed-case/), FOX 7/26/4 (same AP-style piece across affiliates — count as one source line, not three), [MultiState](https://www.multistate.us/insider/2026/8/19/the-local-fight-over-data-centers-a-texas-case-study).
- **Hood County — a preemption-warning case, opposite outcome.** Commissioners Court **rejected two
  separate attempts to pass a countywide moratorium in February 2026** after state Sen. Paul
  Bettencourt warned the county lacked legal authority to enact one. Useful as a contrast case to
  Hill County: here the chilling came from a state legislator's preemption threat *before* any
  ordinance passed, rather than a developer's lawsuit after. [Texas Tribune](https://www.texastribune.org/2026/02/10/texas-hood-county-rejects-data-center-development-pause-ai/)
- **Austin County (distinct from the city of Austin) — passed a countywide moratorium ordinance in
  July 2026** covering both AI data centers and battery energy storage systems. Found only via the
  MultiState/search-summary route tonight — not independently corroborated beyond that; **flag as
  lower-confidence, needs a second source before citing as fact.**
- **City of Austin — regulation in progress, not yet a moratorium.** Council Member Vanessa Fuentes
  is on record supporting a moratorium pending new rules; as of the Aug. 19-24 coverage window,
  Austin had not yet held a moratorium vote comparable to Fort Worth's — it's in an earlier,
  discussion/pressure stage. [KUT/KERA, Aug 19](https://www.keranews.org/texas-news/2026-08-19/austin-tx-texas-data-centers-regulations-greg-abbott), [KUT, Aug 24](https://www.kut.org/austin/2026-08-24/austin-races-to-regulate-ai-data-centers-before-they-strain-citys-water-and-power)
- **Dallas — also in the pre-vote stage.** Five council members filed a signed memorandum Aug. 11
  requesting a public hearing within 30 days to consider new data-center land-use rules (either
  updating classification or creating a dedicated land-use category), citing gaps on water/
  electricity/noise/light/vibration/air-pollution limits. [Dallas Observer](https://www.dallasobserver.com/news/dallas-data-center-regulations-40704291/), [GovTech](https://www.govtech.com/policy/dallas-council-members-seek-new-rules-around-data-centers), [KERA](https://www.keranews.org/government/2026-08-12/city-of-dallas-could-be-next-in-texas-to-regulate-data-center-land-use)

### Scale statistic (lower confidence — search-synthesis only)
MultiState's Aug. 19 piece states **"at least 100 local ordinances have been considered by Texas
municipalities" since July 1, 2025**. This is a striking number if accurate, but it came through as a
WebSearch AI-summary of the MultiState page rather than something I read directly (WebFetch blocked)
— **flag as needs-direct-verification, don't cite as a hard number yet.**

### Assessment for Britton
Texas is not a one-item addition — it's a multi-jurisdiction case with real internal variation
(outright ban vs. temporary moratorium vs. rejected-under-preemption-threat vs.
passed-then-reversed-under-litigation-threat vs. still-pending), plus a state-level regulatory
freeze layered on top. It's arguably the richest single-state find since the original 08-16 national
scan. Still your call whether/how to fold it into the corpus restructuring, but if a fifth "anchor"
state joins LA/GA/UT/VA/AZ, this is a strong candidate — the Hill County reversal-under-lawsuit
mechanism in particular fills a real gap (every other corpus case so far is opposition *succeeding*
or *pending*; this is the first clean opposition-*defeated* mechanism found).

### Draft candidate corpus rows (NOT added to working corpus — Britton's call per standing rule)
| # | Site/Project | State | Artifact type | Date | Source |
|---|---|---|---|---|---|
| 28 | Statewide ERCOT/PUC interconnection audit | TX (statewide) | State regulatory action (gubernatorial directive + PUCT/ERCOT audit) | 2026-08-03 (directive), ongoing through Dec. 2026 | [Texas Tribune](https://www.texastribune.org/2026/08/14/texas-data-center-approval-pause-ercot-power-grid/), [Utility Dive](https://www.utilitydive.com/news/ercot-texas-puc-data-center-audit/828472/) |
| 29 | Fort Worth moratorium process + DCIC | TX (Fort Worth) | Municipal ordinance/commission (in-process) | 2026-08-11 | [Fort Worth Report](https://fortworthreport.org/2026/08/12/data-center-moratorium-takes-first-steps-after-fort-worth-city-councils-unanimous-vote/) |
| 30 | San Marcos citywide ban | TX (San Marcos) | Municipal ordinance (enacted, indefinite) | 2026-06-16 | [Texas Tribune](https://www.texastribune.org/2026/06/30/texas-san-marcos-data-center-ban-zoning-laws/) |
| 31 | Hill County moratorium + RCM Hill $100M suit + rescission | TX (Hill Co.) | County ordinance + federal litigation (reversed) | 2026-05 (passed), 2026-06-04 (rescinded), 2026-07-09 (suit dismissed) | [Texas Tribune](https://www.texastribune.org/2026/06/05/texas-hill-county-moratorium-rescinded-data-centers/), [KWTX](https://www.kwtx.com/2026/07/15/hill-county-dropped-its-data-center-ban-after-100-million-lawsuit-now-developer-has-dismissed-case/) |
| 32 | Hood County rejected moratorium (preemption threat) | TX (Hood Co.) | County ordinance attempt (failed) | 2026-02 | [Texas Tribune](https://www.texastribune.org/2026/02/10/texas-hood-county-rejects-data-center-development-pause-ai/) |

**Provisional codes:** `regulatory-venue-shifting` doesn't quite fit Hill County — recommend a new
code, something like `litigation-driven-regulatory-reversal` or `chilling-effect-cascade` (the Tom
Green County ripple), distinct from anything currently in the theme map. Hood County fits closer to
an existing `state-preemption-threat` type code if one exists in the national-restructure draft
(didn't verify against the draft's exact code list tonight — check before finalizing).

---

## 2. Coweta County GA — the Project Sail/Project Peach disambiguation is RESOLVED: two real, separate lawsuits

08-24 flagged this as unresolved. Tonight's search confirms **these are two genuinely distinct
projects, two distinct lawsuits, filed the same day (May 5, 2026), by what appear to be different
resident groups — not a search-summarization conflation of one event into two:**

- **Project Sail**: ~800 acres, Prologis/Atlas Development (see 08-24's identity-shifting finding),
  $17B, opposition organized as "Citizens for a Rural Coweta." Lawsuit filed against a rezoning
  approved earlier in 2026.
- **Project Peach**: a **separate** 320-acre site at 300 Johnson Circle in **Palmetto, GA**
  (different geography within Coweta County), $1B, 2.1M sq ft, rezoned from rural-conservation to
  industrial in April 2026. **Also had a Superior Court appeal filed May 5, 2026** — but with
  distinct legal claims: the Peach suit centers on a procedural argument that the county changed its
  data-center zoning ordinance in **December 2025** (shifting the applicable category from "light
  industrial" to "industrial") without requiring a new Development of Regional Impact (DRI) study,
  which plaintiffs argue was required. Opposition here is more Palmetto-city-centered per WABE/Fox5
  coverage, consistent with 08-24's read that it's a geographically and organizationally distinct
  resident group from Project Sail's. [Times-Herald, "Where Coweta's five proposed data centers stand"](https://www.times-herald.com/data_center/where-cowetas-five-proposed-data-centers-stand/article_55ee204a-0e00-43e4-9ad1-78c92b679d06.html), [WABE](https://www.wabe.org/palmetto-residents-unclear-on-project-peach-data-center-as-coweta-commissioners-pauses-data-center-development/), [Fox 5 Atlanta](https://www.fox5atlanta.com/news/coweta-county-concerns-project-peach-data-center-palmetto)

**Practical implication:** the plaintiff-count discrepancies across prior notes (17 vs. 19 vs. "nearly
20" vs. "20") are likely explained, at least partly, by different sources conflating or separating
the two suits' plaintiff counts, not just rounding — as 08-24 suspected. If Britton wants Project
Sail in the corpus (row #27 drafted 08-24), **Project Peach is a legitimate sixth-distinct-mechanism
GA row in its own right** (procedural/DRI-study argument, a species of institutional-rule-change
opposition distinct from Sail's identity-shifting angle and from Stanton Springs/Covington's EJ/
permit-violation angles already in Tier 2). Not drafted as a full corpus row tonight given time
budget on Texas — flagging as ready-to-draft next session if Britton wants it.

---

## 3. NAACP v. SpaceXAI — no new hearing date found; DOJ motion still undecided
Re-checked with several fresh query angles tonight (direct date-range searches, Earthjustice press
page, docket-adjacent terms). **No new hearing date has surfaced anywhere in search results.** DOJ's
motion to intervene/dismiss: still no ruling found, same as every check since 08-21. This remains a
genuine "nothing new to report" rather than a search-technique gap — recommend continuing the
periodic re-check rather than assuming a WebFetch-only fix will resolve it (the docket itself may
simply not have moved).

## 4. Sabey / Decatur Township — still no ruling
Re-confirmed tonight: motion to dismiss (filed June 15) and the June 29 status conference are both
still the most recent confirmable events. No outcome coverage for either the status conference or
the Aug. 20 hearing mentioned in 08-24's note. Genuinely still pending — same read as every note
since 08-20.

---

## What's still open / blocked on Britton
- **Corpus-size and corpus-restructuring calls** — untouched tonight, still Britton's, but tonight's
  Texas findings make this a more live question: if Texas goes in, it's arguably now a fifth anchor
  state alongside LA/GA/UT/VA/AZ, not a minor addition.
- **Texas** — genuinely deep now; candidate rows #28-32 drafted above, not committed. Whether to
  greenlight a formal Texas write-up/corpus addition is the next concrete decision point.
- **Coweta Project Peach** — disambiguation resolved (two real suits); a sixth GA corpus row is
  ready to draft next session if wanted.
- **NAACP v. SpaceXAI** — still no new hearing date; re-check again in a few more days.
- **Sabey/Decatur Township** — still no ruling; re-check again in a few more days.
- **Fort Worth's exact moratorium-process vote tally** — confirmed unanimous, exact number (10-0 or
  otherwise) not nailed down from search alone; minor, needs a primary-source pull if it matters for
  the write-up.
- **Austin County (the county, not the city) countywide ban** — single-source (MultiState synthesis)
  tonight, needs a second corroborating source before treating as confirmed.
- **Kent, OH ordinance PDF + JAPA/Kollar abstract page** — still blocked on WebFetch, unchanged.

## WebFetch status (for the running tally)
13th+ consecutive session `EGRESS_BLOCKED`, tested against the standing Wikipedia control tonight.
No new domains tried tonight given the pattern is well-established. Recommend checking proxy/egress
config directly rather than continuing nightly re-tests indefinitely.
