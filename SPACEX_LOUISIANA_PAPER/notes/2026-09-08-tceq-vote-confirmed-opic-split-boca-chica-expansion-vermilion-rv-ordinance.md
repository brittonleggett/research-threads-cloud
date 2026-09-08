# 2026-09-08 — TCEQ's 3-0 vote confirmed via a directly-fetched news source (signed order PDF
# itself still unlocated), a genuinely new finding that TCEQ's own Public Interest Counsel
# recommended the opposite of the Executive Director, Travis County suit remains a documented
# access barrier (found the real portal, still blocked), FAA docket flat for a sixth check, and a
# substantial Boca Chica corpus expansion (a second, primary-verified federal lawsuit; a
# cross-state coalition solidarity filing; a land-exchange case hearing with no ruling yet) plus a
# new Vermilion Parish local-governance angle (RV-park moratorium tied directly to anticipated
# spaceport worker housing demand)

Follow-up to `2026-09-07-tceq-permit-resolved-and-100m-coastal-figure-clarified.md`. Read-only
research pass (background agent). **No theory chain, coding scheme, or Study 1 option (A/B/C)
decided or touched here — still Britton's call**, per standing project rules. Tooling:
`poppler-utils` reinstalled again this session (not persisted between sessions, same as every
prior night); PDFs fetched with `curl` + read with `pdftotext -layout` where flagged as primary;
several sources required the `r.jina.ai` proxy after direct `curl`/WebFetch hit 403s — flagged
inline per this project's tiering convention.

## 1. TCEQ Docket 2024-1821-IWD — the vote is now confirmed via a directly-fetched news source; the
## signed order PDF itself remains genuinely unlocated after a real second attempt

09-07 left this open: "the actual signed Commission order/vote record itself" was not found, only
inferred from a related federal suit's dismissal and news convergence. Tonight, two separate
efforts:

**a) Searched TCEQ's own agenda-backup package for docket 2024-1821-IWD more completely** — the
09-05/09-07 notes had only pulled two of the ten filed items (`-appr.pdf`, `-edr.pdf`). Tonight,
found and fetched all remaining backup filings directly from TCEQ's own site (all `curl`, HTTP
200, `pdftotext -layout`): the **backup index** (`2024-1821-iwd-index.pdf`, confirms the full list
of ten filed items — Agenda Setting Letter, Request(s), Comment(s), ED's Response to Comment,
Draft Permit, Applicant's Response, ED's Response to Requests, **OPIC's Response to Requests**,
and two coalition replies), the **Agenda Setting Letter** (`-set.pdf`, dated Jan. 3, 2025, confirms
the Feb. 13, 2025 meeting date and location), and **Save RGV/Carrizo-Comecrudo's Reply to
Responses** (`-pror1.pdf`, filed by Requestors urging the Commission to grant reconsideration or,
alternatively, refer to SOAH for a contested hearing).

**This confirms directly, and importantly**: TCEQ's agenda-backup packages contain only
**pre-meeting** filings (everything submitted before Feb. 13, 2025) — there is no "final order" or
"vote record" document in this package by design; TCEQ does not post the signed Commission order
in the same backup folder as the pre-meeting filings. This explains, rather than just repeats,
why five nights of URL-pattern-guessing (`-final.pdf`, `-order.pdf`, `-cofo.pdf`, `-cor.pdf`,
`-io.pdf`, `-commord.pdf`, `-vote.pdf`, etc. — all 404) never found it: it was never going to be
there.

**b) The genuinely new document found tonight: the Office of Public Interest Counsel's (OPIC)
Response, `2024-1821-iwd-picr.pdf`** (fetched directly, `curl`, HTTP 200, 1,411 lines). OPIC is a
statutorily independent office within TCEQ, distinct from both the Executive Director and the
Commissioners — this is the first time this project has that office's position on this docket.
**Quoted directly, verbatim**:

> "OPIC respectfully recommends that the Commission find that the Carrizo/Comecrudo Nation of
> Texas, Inc., Save RGV, and South Texas Environmental Justice Network are affected persons, grant
> their hearing requests, and refer this application for a 180-day hearing at the State Office of
> Administrative Hearings (SOAH) on Issue nos. 1-8... Additionally, OPIC recommends denial of the
> remaining hearing requests and all requests for reconsideration."

**This is the opposite recommendation from the Executive Director** (already primary-confirmed
09-07: ED recommended denying *all* hearing requests). This is a genuinely new nuance not found in
five prior nights on this docket: **TCEQ's own internal offices split** — the ED said deny
everything; the Public Interest Counsel said grant a contested-case hearing to the three
organizational parties specifically. The Commission's ultimate 3-0 vote (below) sided with the ED,
not OPIC — a fact worth having in the corpus regardless of which framing Britton picks, since "did
the regulator's own public-interest office disagree with staff, and did the Commission follow
staff over its own watchdog office anyway" is a sharper venue-capture data point than "staff
recommended denial and the Commission agreed."

**c) The vote itself, now confirmed via a directly-fetched (not WebSearch-summarized) news
article.** Searching specifically for TCEQ vote/outcome language surfaced San Antonio Current's
own coverage; **fetched directly** (WebFetch, not a search snippet):
https://www.sacurrent.com/news/state-regulators-approve-elon-musks-spacex-to-release-wastewater-into-south-texas-wetlands-36790995/
— byline Sanford Nowlin, published **Feb. 18, 2025**. Confirms: **the Texas Commission on
Environmental Quality voted 3-0 on Thursday (Feb. 13, 2025) to approve SpaceX's wastewater
discharge permit**, ruling that opponents offered no "new factual information or an error" that
could alter the decision; no public comment was allowed at the meeting; environmental engineer
Eric Roesch is quoted submitting a written statement proactively requesting a contested hearing.
Three commissioners sat on TCEQ at the time (Paup, Janecka, Gonzales — named on the letterhead of
every backup filing above), consistent with a 3-0 vote.

**Net position, stated plainly**: the vote count, date, and outcome (3-0, Feb. 13, 2025, permit
approved / hearing requests denied) are now confirmed via a directly-fetched primary-tier news
article, a meaningfully stronger basis than 09-07's "secondary corroboration via a related federal
suit's dismissal." **What remains genuinely unlocated, after a real second attempt tonight**: the
actual signed Commission order document itself. TCEQ's Plone-based backup-file system only holds
pre-meeting filings (confirmed above, not merely re-asserted); TCEQ's permit-search web app
(`permit-search.tceq.texas.gov`) is a client-side JavaScript single-page application that returns
the same empty app shell to every URL and API guess tried (confirmed by testing both a real path
and a fabricated API endpoint — both returned identical shell HTML), which this session's tooling
cannot drive without a JS-capable browser. **Recommend treating this as a structurally blocked gap
for this environment's tooling specifically** (would likely resolve in one query by a human using
the actual web app, or via a TCEQ records request), not a search-effort gap — do not keep
re-guessing PDF filenames on future nights.

## 2. Travis County suit (D-1-GN-24-010020) — found the real court portal for the first time,
## confirmed it's genuinely inaccessible to this session's tooling, not just mis-targeted

Prior nights hit 502s against guessed subdomains (`judicial-search.traviscountytx.gov`,
`publicaccess.traviscountytx.gov`, etc.) that may not have even been the right portal. Tonight,
found the *actual* link by fetching Travis County's own District Clerk case-information page
directly (`traviscountytx.gov/district-clerk/case-information-records`, HTTP 200) and reading its
own outbound link: **`https://odysseyweb.traviscountytx.gov/Portal/`** — a Tyler Technologies
Odyssey court-records portal, the same platform family many Texas counties use. Direct `curl`
returns **403**. Via the `r.jina.ai` proxy, the portal loads far enough to reveal *why*: it is a
stateful, cookie- and JavaScript-dependent search application ("Cookies must be allowed... your
browser must allow cookies before you can use this application") — not a page that exposes case
data through a plain URL or query string the way TCEQ's static PDF backups do. This is a genuine,
now-more-precisely-diagnosed access barrier (a JS-driven session-based search UI, not a network
block), not a wrong-URL problem. Two additional targeted news searches tonight (specific to this
case number and the named coalition) turned up nothing published after the Dec. 2024 filing
coverage. **Restating 09-07's recommendation with more confidence now that the actual portal is
identified**: this needs either a human using a real browser against
`odysseyweb.traviscountytx.gov/Portal/`, or a direct District Clerk records request — not further
automated search.

## 3. FAA docket (FAA-2026-8614) — sixth consecutive identical reading, confirms 09-07's
## deprioritization call

Per the task's instruction to spend no more than a quick confirmation check: re-fetched via
`r.jina.ai` proxy (direct still 403s). **Posted: 3,201. Received: 14,670.** Identical to every
reading since 09-02 — now six consecutive nights (with one intentional skip) at the exact same two
numbers. No further action taken tonight beyond this one check; continuing to recommend
deprioritizing to news-only or a weekly cadence, per 09-07.

## 4. Boca Chica comparison corpus — substantial expansion, four genuinely new items

### 4a. A second, primary-verified federal lawsuit against the FAA (2023-2025), distinct from the
### 2026 land-exchange suit already in the corpus

Chasing a stocktwits/Deccan Herald pair of articles headlined "court rejects environmental
challenge to SpaceX's expanded launch site" (dated by their own bylines to March 5, 2026 — a
detail that turned out to be an article-update timestamp, not the ruling date; flagging this
explicitly since it's exactly the kind of date confusion the project has been warned to check
rather than repeat) led to a **different, older, and previously-untracked Boca Chica legal
action**: **Center for Biological Diversity et al. v. FAA**, Case No. **1:23-cv-01204**, U.S.
District Court for the District of Columbia — filed **May 1, 2023** by the Center for Biological
Diversity, American Bird Conservancy, Surfrider Foundation, and the Carrizo/Comecrudo Nation of
Texas, challenging FAA's 2022 approval of increased Starship/Super Heavy launch cadence at Boca
Chica (the same FAA licensing action underlying the FWS Biological and Conference Opinion already
in the corpus, row 11) on NEPA grounds — arguing FAA should have required a full Environmental
Impact Statement rather than accepting SpaceX's Programmatic Environmental Assessment.

**Verified directly from the actual CourtListener docket** (fetched via `r.jina.ai` proxy after a
direct 403, not a WebSearch summary): on **September 15, 2025**, Judge Carl J. Nichols signed a
Memorandum Opinion and an Order **denying Plaintiffs' Motion for Partial Summary Judgment; granting
the government's and SpaceX's Cross-Motions for Partial Summary Judgment**. News coverage (Texas
Tribune, 2025-09-17, WebFetch-confirmed directly) quotes the opinion: "Most of the [assessment's]
conclusions were well-reasoned and supported by the record," citing recent Supreme Court precedent
that courts should avoid micromanaging agency environmental reviews within reasonable bounds.
**One precision correction on how to describe this**: news coverage characterizes this as the
"lawsuit dismissed" — the primary docket entry itself is a partial-summary-judgment ruling *for*
the government and SpaceX on the motions actually before the court that day, and the docket shows
continued activity into December 2025 (a status report, further orders) — so "the environmental
groups lost on the merits of their NEPA claim" is the more precise description than "dismissed,"
even though the practical effect (FAA's licensing stands) is the same. **A genuinely useful
connective detail**: an amended complaint filed July 2025 in this same case added **Save RGV** as
a plaintiff — meaning Save RGV, already tracked in this corpus across three other Boca Chica
actions, is also a party here, reinforcing how small and recurring the opposition-coalition
membership is across every distinct Boca Chica legal front found so far.

### 4b. The land-exchange case (1:26-cv-02053) — a hearing happened Sept. 3, 2026; no ruling found
### yet, a genuinely open item rather than a stalled search

09-05's note primary-verified this case's caption from the actual stamped complaint. Tonight,
found (via SOTXEJN's own site, directly fetched, HTTP 200 — the plaintiff coalition's own
announcement, Tier A for the event's occurrence) that a **court hearing on this case was held
Thursday, September 3, 2026**, livestreamed by SOTXEJN from its Brownsville office:
https://sotxejn.org/2026/08/25/rsvp-the-people-v-spacex/. Searched specifically for any ruling or
outcome from that hearing (multiple query angles, avoiding conflation with the unrelated
2023-cv-01204 case above) — **found nothing**, including no newer press release on Center for
Biological Diversity's own site (its press-release index was checked directly and currently runs
through Sept. 4, 2026 with no SpaceX land-exchange entry after the July 20 emergency-injunction
motion). **Stated plainly: a hearing occurred five days ago; no ruling has surfaced yet** — a
genuinely current open item worth a check on a near-future night, not a gap this session failed to
find.

### 4c. Direct, primary-source evidence of cross-site coalition coordination between Boca Chica and
### Vermilion Parish opposition groups — a new finding relevant regardless of framing

Sweeping SOTXEJN's own site for anything posted since the corpus was last checked turned up
**https://sotxejn.org/2026/09/05/louisiana-rgv-solidarity-stop-spacex/** (fetched directly, HTTP
200), posted by SOTXEJN organizer Bekah Hinojosa. **Quoted in full, it is short enough to
reproduce**:

> "We partnered with the Louisiana Vermillion Parish community group impacted by SpaceX
> @stopspacex, & organizations @southwings, @southernenvironment, and @npcapics to submit comments
> opposing the Federal Government @faa's plans to eliminate 13 environmental laws to fast-track
> permits for dangerous, polluting SpaceX."

The linked comment document itself (a bit.ly link resolving to a Google Drive file) could not be
extracted tonight — Google Drive's viewer is a JS application, same limitation as the TCEQ permit
app above; located and dated but not text-read, Tier B. **Why this matters beyond either site's
own corpus**: this is the first primary-source confirmation this project has found that the two
sites' opposition coalitions are not just structurally similar cases for comparison, but are
**actually coordinating** — the RGV-based coalition formally joined the Vermilion Parish
`@stopspacex` group, plus SouthWings, the Southern Environmental Law Center, and the National
Parks Conservation Association, in a single joint FAA comment on the Vermilion Parish waiver
docket (FAA-2026-8614) itself. This closes some distance on the "broader Stop SpaceX coalition"
gap flagged closed-but-unresolved on 09-05 — it's not a fully separate finding, but it is concrete
evidence of the multi-organization coalition acting jointly, with named partner organizations,
which prior nights hadn't found.

### 4d. Minor additions from the same SOTXEJN sweep — Starbase's "critical infrastructure" felony
### law and continued on-the-ground documentation

Two more items worth having in the corpus, both from SOTXEJN's own site (Tier A for their own
statements):
- **"Petition: Stop Elon Musk's Land Grab in South Texas!"** (2026-07-15) — describes Starbase, TX
  (the company town incorporated May 2025, already known to this project) as designated under
  Texas's Critical Infrastructure law, such that "anyone entering the town could be arrested
  immediately and potentially face felony charges." This is a striking, directly comparable data
  point to Vermilion Parish's own state-level legal-protection package (Act 874/HB1098's liability
  shield, Act 343/HB1250's special-motion-to-strike, both already in the corpus) — one site
  criminalizes entry, the other shields the company from suit; both are state-level legal
  architecture built around the same company's operations, a useful direct comparison regardless
  of framing.
- **"May 22, 2026 SpaceX Starship V3 Explosion Debris on Boca Chica Beach"** — SOTXEJN's own
  on-the-ground photo-documentation post of rocket debris on the beach after a Starship V3
  explosion, continuing the pattern of self-documented environmental-harm evidence from the
  opposition side (distinct from, and a useful complement to, the federal CWA/CAFO enforcement
  record already in the corpus).

## 5. Vermilion Parish side — Act 343 (HB1250) enrolled text now primary-fetched (was B-tier), and
## a new local-governance finding: an RV-park moratorium tied directly to anticipated spaceport
## housing demand

### 5a. Act 343 / HB1250 — upgraded from news-sourced to directly-fetched primary text

The corpus (`Study1_Corpus_and_Coding_DRAFT_2026-08-27.md`, row 6i) has carried Act 343's substance
as news-sourced only since 09-01. Tonight, found the actual enrolled bill on `legis.la.gov` — a
direct `curl` fetch of the bill's own info page succeeded without a proxy this time (HTTP 200,
unlike some prior nights' 403s on this domain; access appears intermittent rather than
permanently blocked), which linked directly to the "HB1250 Act 343" document
(`https://www.legis.la.gov/legis/ViewDocument.aspx?d=1479644`, HTTP 200, 3-page PDF, `pdftotext`
extraction). **Confirmed directly from the enacted text** (enacting La. R.S. 9:2800.31): it creates
a **"special motion to strike"** for any cause of action against an "aerospace flight entity"
(defined broadly — the company, its employees/contractors/vendors, any landowner leasing to it,
and any public entity with an operational relationship to it) arising from a "public issue," unless
the plaintiff can show a probability of success; **all discovery is automatically stayed** upon the
motion's filing; and the **prevailing party on the motion is awarded attorney fees and costs** —
i.e., an anti-SLAPP-style mechanism, structurally similar to media/speech anti-SLAPP statutes but
purpose-built for aerospace companies, that both accelerates dismissal of weak claims *and*
imposes a real cost risk on filing a claim against SpaceX that doesn't clear the bar. This
confirms, with the statute's own text rather than a paraphrase, The Current LA's 08-31-sourced
characterization already in the corpus ("blocks injunctions/enables early dismissal... with
fee-shifting").

### 5b. New: Vermilion Parish Police Jury considering an RV-park moratorium/ordinance explicitly
### tied to anticipated spaceport worker housing demand — a genuinely new local-governance angle

A general Vermilion Parish news sweep surfaced **Modern Campground's "Vermilion Parish Considers
New RV Park Rules as SpaceX Spaceport Plans Advance"** (byline Jhareyna Pagao, published
**2026-09-04** — after the 09-07 note's cutoff), fetched directly. Confirms: the parish is
considering an ordinance requiring privacy fencing (at operator expense) and capping new RV parks
at 50 lots, driven explicitly by anticipated construction-worker and permanent-worker housing
demand tied to the spaceport. **Parish Administrator Keith Roy**, quoted: "Do you really want
hundreds of RVs next to your house?" **Councilman Scott Broussard** opposed the ordinance as
currently drafted (questioning why RV operators specifically bear fencing costs rather than
residential developers generally) but flagged the parish's **one-person permit office** as a
capacity risk that needs addressing "now" if construction accelerates. **The Vermilion Parish
Police Jury was scheduled to take this up further on September 16, 2026** — a concrete, dated
future-check item.

**Independently corroborated with a primary government document tonight, not just the news
article**: fetched the Vermilion Parish Police Jury's own **August 19, 2026 meeting agenda**
directly from the parish's own site (`vppj.org`, HTTP 200, `pdftotext` extraction) — confirms, in
the parish's own words, a Finance Committee recommendation "to approve to put a moratorium on any
new RV Parks until Ordinance is in place," acted on by the full Jury that same meeting. This
establishes the moratorium recommendation predates the news article by about two weeks and gives a
primary-document anchor point (Aug. 5, 2026 committee meeting → Aug. 19, 2026 Jury action → Sept.
4, 2026 news coverage → Sept. 16, 2026 scheduled follow-up) rather than relying on the news article
alone. **This is a genuinely new local-impact/regulatory-response angle for the corpus** — direct
evidence of local government proactively responding to anticipated economic-benefit-driven
population inflow, useful regardless of which Study 1 framing Britton eventually picks (it's
concrete "second-order local cost of the promised jobs" material, adjacent to but distinct from
the NDA/liability-shield material already in the corpus).

### 5c. General Vermilion-side news sweep — otherwise quiet

Beyond 5b, no other Vermilion-Parish-specific developments dated after 09-07 were found across
several search angles (litigation against the project directly, parish council/permitting actions,
state legislative activity, coalition activity). The Verite News piece behind 09-07's "$100M
coastal figure" finding (`veritenews.org/2026/09/04/spacex-promises-coastal-restoration/`) was
confirmed as the original of the story 09-07 read via its Louisiana Illuminator republication — no
new content beyond what 09-07 already extracted, just noting the original-outlet URL exists and
matches, for citation-source-of-record purposes.

## 6. What's still open

- TCEQ Docket 2024-1821-IWD's signed Commission order — the vote (3-0, Feb. 13, 2025) and outcome
  are now primary-tier-news-confirmed; the literal order document is structurally inaccessible to
  this session's tooling (a JS-driven permit-search app, not a static file), not merely unfound —
  recommend a human check the live web app, or a records request, rather than more automated
  guessing.
- Travis County suit (D-1-GN-24-010020) — the actual portal (`odysseyweb.traviscountytx.gov`) is
  now identified but confirmed cookie/JS-gated; same recommendation as above.
- FAA docket — sixth consecutive flat reading (3,201/14,670); continue deprioritizing.
- The land-exchange case (1:26-cv-02053) — a Sept. 3, 2026 hearing occurred; no ruling found as of
  tonight (Sept. 8) — worth a check in a few days, this is live and current, not stale.
- The Louisiana-RGV joint FAA comment letter's full text — located (Google Drive link) but not
  text-extracted; a JS-viewer limitation, same as the TCEQ permit app.
- USFWS's 2025 "Amended BCO Addendum #2" itself (cited via FAA's EA, per 09-07) — still not
  independently fetched.
- Unchanged from prior nights: the Exxon-to-state settlement's own terms (reportedly sealed); the
  original Gulf States Newsroom/Type Investigations "54 officials" piece (syndicated version only);
  the Jacob Landry NDA document (still Cloudflare-blocked at DocumentCloud); "Golden Eagles'
  Conservation Society" (FAA filer name) still unverified — none of these were re-attempted tonight
  given diminishing returns already logged across multiple prior nights; flagging them here rather
  than re-running the same searches.
- No theory chain, coding scheme, or Study 1 option (A/B/C) decided — unchanged, still Britton's
  call.

## Summary: what's new vs. stable since 09-07

| Item | Status |
|---|---|
| TCEQ Docket 2024-1821-IWD vote | **Confirmed** — 3-0, Feb. 13, 2025, via directly-fetched San Antonio Current article; signed order PDF confirmed structurally unreachable by this session's tooling (JS app), not just unfound |
| TCEQ OPIC position | **New finding** — Public Interest Counsel recommended granting a contested hearing to the 3 organizational parties, opposite the ED; Commission followed the ED |
| Travis County suit | Real portal identified (`odysseyweb.traviscountytx.gov`); confirmed cookie/JS-gated, same status (unresolved) with a more precise diagnosis |
| FAA docket | Flat, 3,201/14,670, sixth consecutive reading |
| Boca Chica: 2023 NEPA suit (1:23-cv-01204) | **New to corpus** — Center for Biological Diversity et al. v. FAA; partial summary judgment for government/SpaceX, Sept. 15, 2025, primary-docket-confirmed |
| Boca Chica: land-exchange case (1:26-cv-02053) | Hearing held Sept. 3, 2026; no ruling yet |
| Boca Chica ↔ Vermilion coalition coordination | **New finding** — SOTXEJN + Vermilion's @stopspacex + 3 national/regional orgs filed a joint FAA comment together, Sept. 2026 |
| Vermilion: Act 343/HB1250 | Upgraded B → A, enrolled text fetched and read directly |
| Vermilion: RV-park moratorium | **New finding** — parish-level housing-capacity response to anticipated spaceport population, primary-document-corroborated (parish's own Aug. 19 agenda) |

All claims above are labeled by tier inline: primary document directly fetched and text-extracted
(TCEQ index/set/picr/pror1, Act 343 enrolled text, VPPJ Aug. 19 agenda) vs. primary court docket
directly read via proxy (CourtListener, both cases) vs. news article directly fetched, not
AI-search-synthesized (San Antonio Current, Texas Tribune, Modern Campground) vs. organizational
press release/blog directly fetched (SOTXEJN, Center for Biological Diversity) vs. located-but-not-
text-extracted (the Google Drive-hosted joint FAA comment) — nothing load-bearing above relies on
a bare WebSearch snippet without saying so.
