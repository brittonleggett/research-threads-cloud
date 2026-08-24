# 2026-08-24 — Litigation re-check (Sabey, NAACP v. xAI/SpaceXAI), Coweta GA deep-dive, new Texas lead

## WebFetch status — still blocked, 12th+ consecutive session
Tested again tonight against `en.wikipedia.org` (the standing neutral control) and directly against
`courtlistener.com` (wanted the NAACP v. xAI docket) and `newsatomic.com` (a local-notice aggregator
turned up mid-search). All three returned `EGRESS_BLOCKED`. Everything below is WebSearch-summarized
only — same confidence tier as every prior note, flagged inline wherever a fact rests on a single
source or a search-engine-generated summary rather than a direct read of the underlying article.

---

## 1. NAACP v. xAI Corp. (now SpaceXAI) — Aug. 24 evidentiary hearing was POSTPONED, not held

This was tonight's sharpest re-check target (hearing was calendared for today). Real news since 08-22:

- **The Aug. 24 evidentiary hearing on NAACP's preliminary-injunction motion was postponed.**
  Multiple search results (AOL, Yahoo, apparently a shared wire/syndicated piece — likely originating
  from a Memphis-market outlet, possibly *Commercial Appeal* — consistent wording across all copies,
  so treat as **one underlying source, not independent corroboration**) report: "that hearing was
  postponed, according to a Notice filed with the court on Aug. 21." **No new date has surfaced in
  search results, and no reason for the postponement was reported.** [AOL](https://www.aol.com/articles/spacexai-hearing-decide-future-southaven-100436000.html), [Yahoo](https://www.yahoo.com/news/us/articles/spacexai-hearing-decide-future-southaven-100436668.html)
  — **this is a real, if thin, finding: worth a direct docket re-check the moment WebFetch (or PACER/
  CourtListener access) is available**, since I could not confirm the notice's actual text or the
  new date. Case is confirmed to be *NAACP v. X.AI Corp.*, No. 3:26-cv-00074-DMB-JMV, N.D. Miss.,
  Oxford Division, assigned to Chief District Judge **Debra M. Brown** (matches "DMB" in the case
  number) and Magistrate Judge Jane M. Virden. [CourtListener docket](https://www.courtlistener.com/docket/73188848/national-association-for-the-advancement-of-colored-people-v-xai-corp/) (not fetched, WebFetch blocked).
- **DOJ's motion to intervene/dismiss: still no ruling found**, same as 08-22.
- **New corporate-identity fact, well-corroborated across 7+ independent outlets (Daily Beirut,
  Social Media Today, Stocktwits, ThePlanetTools.ai, Teslarati, Digital Applied, Yahoo Finance):
  xAI has been absorbed into SpaceX.** SpaceX acquired xAI in an all-stock deal Feb. 2, 2026; Musk
  confirmed in May the standalone xAI entity would dissolve into SpaceX; the combined AI operation
  rebranded as **"SpaceXAI"** on July 6, 2026 (new logo, X account moved from @xai to @SpaceXAI).
  Grok itself keeps its name — only the corporate/product-line brand changed. **Practical implication
  for the corpus/citations: the defendant in ongoing filings may now be captioned differently
  (SpaceXAI / MZX Tech, not "xAI Corp.") even though the case name itself (filed pre-rebrand) still
  reads *NAACP v. X.AI Corp.*** Flagging so future searches/citations aren't thrown by the name
  change, and so Britton's write-up doesn't cite "xAI" as if it's still the current corporate name
  without a note.
- **New, separate-but-related development: a state-level Agreed Order, NOT part of the federal
  litigation.** SpaceXAI and the Mississippi Department of Environmental Quality (MDEQ) entered an
  Agreed Order setting a fixed removal timeline for the **69** (up from the 27/33/59 figures in
  earlier notes — the count kept growing as discovery/inspection proceeded) temporary, unpermitted
  gas turbines at the Southaven site: removal beginning as early as August 2026, complete by **July
  2027**, to be replaced by a *permitted* 41-turbine, 1.2 GW permanent plant (permit granted March
  2026). Independently corroborated: [Mississippi Today](https://mississippitoday.org/2026/07/31/southaven-xai-turbines-deadline/) (state-agency beat reporter, strongest single
  source), [Memphis Flyer](https://www.memphisflyer.com/environmental-groups-call-out-spacexai-and-mdeq-over-agreed-order/), [TechCrunch](https://techcrunch.com/2026/07/31/spacex-wont-remove-all-of-xais-unpermitted-turbines-for-another-year/). **Earthjustice/environmental groups are
  on record calling MDEQ "complicit in xAI's lawlessness"** for allowing another ~11 months of
  operation — this is a good verbatim-attributed quote for the institutional-capture/regulatory-
  venue-shifting theme if Britton wants it (Laura Thoms, Earthjustice enforcement director).
- **Net status:** federal PI hearing postponed with no new date found; DOJ motion to intervene still
  undecided; separately, a state administrative settlement already extends operation to mid-2027
  regardless of how the federal case comes out — which somewhat lowers the real-world stakes of the
  federal PI hearing (the turbines were already on a removal glidepath before today's hearing was
  even postponed). **Recommend one more re-check in the next several days** for the rescheduled date.

## 2. Sabey Corp. / Decatur Township — still no ruling; but a related, big Marion County development
**No ruling on the June 15 motion to dismiss has surfaced** — same "still pending" status as 08-21/
08-22, re-confirmed with several fresh searches tonight (Marion Superior Court ruling, dismissed/
denied queries, Mirror Indy archive). The Aug. 20 hearing appears to have occurred (it was reported
as scheduled, "virtual hearing... with lawyers from each side"), but **no outcome coverage exists
yet**. Not a search-technique gap — this is a genuine "still waiting on a written order" situation,
consistent with 08-21/08-22's read.

**Separately (already covered in the 08-20 note, not new — flagging only to avoid Britton thinking
it's new tonight): Marion County's data-center moratorium (City-County Council 23-1 on Aug. 10, MDC
final approval 6-0 on Aug. 19) is now fully final.** Confirmed nothing has changed on that since
08-20's note — the three already-approved projects (DC Blox, Metrobloks, Sabey) remain exempt, and
Sabey's Decatur Township site is unaffected by the moratorium either way since it's already approved
and the fight is now purely the judicial-review lawsuit.

## 3. Coweta County, GA "Project Sail" — deepened sourcing, one correction, one live disambiguation flag

### Litigation status: still pending, no update found
Same as 08-22 — no ruling, hearing date, or docket movement surfaced for the May 5, 2026 Superior
Court petition (Coweta County + Atlas Development LLC as defendants). Multiple fresh queries (court
records sites, "motion to dismiss," "status conference," "judge") turned up nothing past the May
filing. Georgia's Superior Court e-filing isn't searchable by WebSearch and CourtListener/PACER-style
direct lookup is blocked by WebFetch, so this is a hard stop, not a shallow check — flagging plainly
as unresolved rather than guessing.

### Correction to 08-22's note: the developer is not just "Atlas Development" — it's Prologis behind a small local front, and that's a good finding in its own right
08-22's note (and every headline) names Atlas Development LLC as the developer. Digging further
tonight (DeSmog's two-part investigation is the strongest source here) found this is materially
incomplete: **Atlas Development LLC — a small, Carrollton, GA-based firm founded 2017, "with no
known record of building data centers, and only a handful of employees" — served as the project's
public face while Prologis (NYSE: PLD, the world's largest industrial real-estate REIT, San
Francisco-based) was the real financial backer, quietly involved from Prologis's first meetings with
county officials in November 2024 but not publicly announced until May 2025.** [DeSmog, "How Data
Center Developers Staked Their Claim in Rural Georgia"](https://www.desmog.com/2026/04/07/how-data-center-developers-staked-their-claim-in-rural-georgia/), [DCD](https://www.datacenterdynamics.com/en/news/prologis-900mw-project-sail-gets-the-go-ahead-in-coweta-county-georgia/), [AJC (2025)](https://www.ajc.com/news/2025/05/a-new-group-steps-in-to-develop-17b-project-sail-data-center-near-atlanta/), [The Real Deal](https://therealdeal.com/national/atlanta/2026/04/10/prologis-wins-approval-for-massive-georgia-data-center/).
**This is a genuinely useful addition, not just trivia** — it's a concrete instance of the
`regulatory-venue-shifting`/institutional-opacity vocabulary already in the restructured thematic
map, this time as "identity-shifting" (a large, out-of-state institutional developer routes a
politically sensitive rezoning through an obscure local shell so residents are negotiating with,
and suing, the wrong-sized opponent). DeSmog also documents a subsequent "charm offensive" — Prologis
reps doing data-center tours and neighborhood barbecues, a mailer using American-flag imagery aimed
at the "conservative-leaning county's sense of patriotism" — and a named resident quote worth keeping:
Connie Lytten (Citizens for Rural Coweta): *"They [Prologis] haven't been transparent from the
get-go."* [DeSmog, "Don't Patronize Us"](https://www.desmog.com/2025/09/10/prologis-project-sail-data-center-charm-offensive-coweta-county-georgia/).

### Correction to 08-22's note: petition signature count was wrong
08-22 flagged a "1,750-signature" petition figure from AtlantaFi.com as lower-confidence. Tonight's
deeper search finds a much better-sourced, much larger figure: **a Change.org petition ("Stop
Project Sail in Coweta County") reached approximately 7,820 signatures**, presented at the public
commission hearing by District 5 resident Melanie Tomlinson before the 3-2 vote — reported
independently as "~8,000" and "7,820" across multiple pieces including a July 23, 2026 Citizen
op-ed. **The 1,750 figure in 08-22's note appears to have been wrong (possibly a stale mid-process
count or a different, smaller petition) — treat 7,820/~8,000 as the better-sourced number going
forward.** [Change.org petition](https://www.change.org/p/stop-project-sail-in-coweta-county), [The Citizen, "A Referendum Could Settle the Project SAIL Debate"](https://thecitizen.com/2026/07/23/a-referendum-could-settle-the-project-sail-debate/).

### New, unresolved disambiguation flag: possibly TWO parallel Coweta lawsuits, not one — needs Britton's or a direct-docket check
Coweta County has **five** data centers in various stages (Project Sail being the largest/most
covered). A second one, **Project Peach** (Atlas/T5-adjacent, 320 acres near Palmetto, GA, $1B,
2.1M sq ft, also rezoned 3-2 in April 2026), **also had residents file a Superior Court appeal on
May 5, 2026** — the same date as Project Sail's suit — per a Times-Herald headline distinct from the
Project Sail one ("Coweta residents file appeal to reverse Project Sail zoning decision" vs. content
describing a separate Project Peach appeal in "Where Coweta's five proposed data centers stand").
**I could not fully disambiguate whether this is (a) two genuinely separate lawsuits filed the same
day by different resident groups (Project Sail's plaintiffs organize under "Citizens for a Rural
Coweta," led in part by Steve Swope; Project Peach's opposition is more Palmetto-city-centered, per
WABE/Fox5 coverage — different geography, different named opponents, so probably a distinct suit) or
(b) a WebSearch-summarization conflation of one event into two apparent stories.** This matters
because the plaintiff-count discrepancy in prior notes (17 vs. 19 vs. "nearly 20" vs. "20") might
partly be different sources describing different suits, not just rounding. **Not resolved tonight —
flagging as a concrete WebFetch-when-available target** (Coweta County Superior Court Clerk, or the
two Times-Herald source articles directly) rather than guessing at which count is right.

### Additional corroborating outlets found tonight (beyond the six in 08-22's note)
WSB-TV, Yahoo/AP syndication, 11Alive, CBS Atlanta, The Cool Down, Hoodline, The Citizen (Newnan's
own paper — several distinct pieces, including a dedicated "data_center" section tag), and DeSmog's
multi-part investigative series (Aug 2025–Apr 2026, four separate pieces). This is now one of the
best-sourced items in the entire candidate pool, LA corpus included.

### Draft ready-to-merge candidate corpus row (NOT added to the working corpus — Britton's call per standing rule)
Formatted to match the Tier 2 table in `Study1_Corpus_and_Coding_DRAFT_2026-08-17_national-restructure.md`
so it can be pasted in directly if/when Britton decides to expand the corpus:

| # | Site/Project | State | Artifact type | Date | Source |
|---|---|---|---|---|---|
| 27 | Project Sail (Prologis/Atlas Development) | GA (Coweta Co.) | Local/national news + litigation (rezoning approval + resident lawsuit) | 2026-04 (approval), 2026-05-05 (suit filed) | [AJC](https://www.ajc.com/business/2026/04/coweta-votes-to-turn-this-800-acre-forest-into-17b-data-center-campus/), [DeSmog (x4, 2025-08 through 2026-04)](https://www.desmog.com/2026/04/07/how-data-center-developers-staked-their-claim-in-rural-georgia/), [CBS Atlanta](https://www.cbsnews.com/atlanta/news/coweta-county-residents-file-appeal-to-stop-massive-data-center-on-protected-rural-land/), [Times-Herald](https://www.times-herald.com/data_center/coweta-residents-file-appeal-to-reverse-project-sail-zoning-decision/article_819c2d7f-7539-4562-84d7-19026b64a832.html), [The Citizen](https://thecitizen.com/2026/05/11/coweta-residents-sue-to-block-project-sail-data-center/) |

**Provisional codes (Britton's Phase 3 call, not locked):** `regulatory-venue-shifting` (extends to
"identity-shifting" — real developer hidden behind a shell entity, a variant not yet in the theme
map), `resource-scarcity-commons` (state-designated "Most Significant Groundwater Recharge Area" —
Middle Chattahoochee basin), procedural-exclusion/institutional-distrust (charm-offensive-as-
distrust-trigger is a nice concrete instance), collective-mobilization-to-litigation (Theme 6/DV
candidate — 7,820-signature petition → PAC pledge to unseat commissioners → lawsuit, a clean
escalation ladder). **Distinct from GA rows #18/#19 already in Tier 2** (Stanton Springs is
EJ/Congressional-hearing-framed; Covington is a permit-violation/formal-complaint case) — Project
Sail is a *litigation-over-an-already-approved-rezoning* case, a third distinct GA mechanism.
**Litigation outcome still unresolved — this row, if added, would join Tier 3 (WebSearch-confidence,
not yet WebFetch-verified) rather than Tier 2 until a primary-source pull is possible.**

## 4. Bounded extra task: new Texas moratorium/pause activity found — not yet in any prior note, flagging for the national scan
Checked for moratorium activity beyond what 08-16's scan covered. Found a substantial, well-corroborated,
**currently entirely absent from this project's notes** development: **Texas**, both state- and
city-level, in just the last three weeks:

- **Statewide: Gov. Greg Abbott ordered a comprehensive audit of every data-center project seeking
  a new Texas grid interconnection**, administered jointly by ERCOT and the PUC — effectively a
  connection-approval freeze on ~250-300 pending projects until each discloses tax incentives/
  abatements received, power draw and any self-generation, water source/volume and cooling tech, and
  noise/traffic mitigation. Announced ~Aug. 3, detailed further through an Aug. 14 Texas Tribune
  piece and an Aug. 20 PUCT Open Meeting where ERCOT was to lay out implementation timing. Audits
  expected to take "several months." [Texas Tribune](https://www.texastribune.org/2026/08/14/texas-data-center-approval-pause-ercot-power-grid/), [Houston Public Media](https://www.houstonpublicmedia.org/articles/news/energy-environment/2026/08/03/558529/gov-greg-abbott-pauses-new-data-centers-until-ercot-puct-audit-energy-water-usage/), [KERA](https://www.keranews.org/texas-news/2026-08-17/texas-will-audit-up-to-300-projects-mostly-data-centers-after-gov-greg-abbotts-order), [Gov. Abbott's office](https://gov.texas.gov/news/post/governor-abbott-directs-comprehensive-data-center-audit).
- **Local: Fort Worth City Council voted 7-0 (unanimously) on Aug. 11, 2026** to begin the process for
  a 90-day data-center construction moratorium (would take effect ~Feb. 2027 pending required state
  procedural steps), plus a new Fort Worth Data Center and Infrastructure Commission chaired by a TCU
  environmental-studies faculty member, evaluating noise/water/land-use impacts. [Fort Worth Report](https://fortworthreport.org/2026/08/12/data-center-moratorium-takes-first-steps-after-fort-worth-city-councils-unanimous-vote/), [KERA](https://www.keranews.org/news/2026-08-12/data-center-moratorium-takes-first-steps-after-fort-worth-city-councils-unanimous-vote), [The Texan](https://thetexan.news/texas-local-news/fort-worth-city-council-begins-process-to-enact-90-day-data-center-moratorium/article_a2a6100b-9576-4370-8679-12dbf7569b9d.html), [CBS Texas](https://www.cbsnews.com/texas/news/fort-worth-data-center-moratorium-neighborhood-impact-debate-august-2026/).

Confirmed via `grep` across all existing `notes/*.md` and both `Study1_Corpus_and_Coding_DRAFT_*.md`
files that **Texas has not been mentioned anywhere in this project before tonight** — it's a real gap
in the 08-16 national scan's state list (GA, UT, VA, AZ, IN/OH, MS/TN, NY), not a duplicate. Given
time budget tonight this was intentionally kept shallow — no corpus candidate drafted, no theme
coding attempted, just flagging that Texas is a live, multi-source, both-state-and-local-level
opposition/regulatory-response case worth a dedicated deep-dive session, the same way GA/UT/VA/AZ
each got one.

## What's still open / blocked on Britton
- **Corpus-size and corpus-restructuring calls** — untouched tonight, unchanged, still Britton's.
- **NAACP v. xAI/SpaceXAI federal PI hearing** — postponed per an Aug. 21 court notice; no new date
  found; re-check again in a few days, and via direct docket read the moment WebFetch/PACER access
  works.
- **Sabey/Decatur Township ruling** — still unknown; Aug. 20 hearing apparently occurred but no
  outcome reported yet; re-check in a few more days, same as prior notes have been saying.
- **Coweta County Project Sail** — litigation outcome unresolved; the Project Sail/Project Peach
  parallel-lawsuit question is a live disambiguation gap that needs either a primary-source docket
  pull or Britton's own read of the two Times-Herald pieces linked above; candidate corpus row
  drafted above, not committed.
- **Texas (Fort Worth + statewide ERCOT/PUC audit)** — brand-new lead, entirely unexplored beyond
  tonight's shallow pass; a real candidate for the next national-scan-style deep dive.
- **Kent, OH ordinance PDF + JAPA/Kollar abstract page** — still blocked on WebFetch specifically,
  unchanged from every prior note; still queued.

## WebFetch status (for the running tally)
12th+ consecutive session `EGRESS_BLOCKED`. Tested tonight against the standing Wikipedia control,
plus two real queued targets (CourtListener's NAACP v. xAI docket, a newsatomic.com local-notice
page) — same failure mode all three times. If it comes back working in a future session, flag
prominently at the top of that session's note per standing instruction. Primary-source pulls still
queued: Kent OH ordinance, JAPA abstract, CCS Paper's legis.la.gov HB79 page, the DOJ.gov filing PDF,
the NAACP/Earthjustice preliminary-injunction brief PDF, and now the NAACP v. xAI CourtListener
docket and the Coweta County Superior Court records for both Project Sail and Project Peach.
