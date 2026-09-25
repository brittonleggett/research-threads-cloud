# 2026-09-25 — FAA docket re-check, Aguilar docket procedural update, Starbase 7,133-acre
# annexation, NPR/Gulf States Newsroom find, and a third literature-scouting pass

AI-run background-agent research pass (Claude, via Claude Code). Read-only web research and direct
document/docket fetches only — no design/theory-chain decision made, nothing submitted or
contacted externally, no file touched outside `SPACEX_LOUISIANA_PAPER/`. This is the first pass on
this project since 2026-09-18 (a ~7-day gap; the note-folder listing in the task brief that said
"no pass since 09-23" undercounted — the most recent prior note was actually 09-18, and this
project has had far more work done on it since 08-27 than the task brief's own summary described;
oriented by reading `README.md`, `CLAUDE.md`, and all 18 prior dated notes/literature files before
starting new work, to avoid duplicating anything already resolved).

## Priority order followed
1. Check for FAA/regulatory developments since the last raw check (2026-09-07).
2. Expand the Boca Chica comparison corpus with new verifiable primary-source facts.
3. Literature-gap scouting.
4. Re-attempt the two items already flagged unresolved across multiple prior sessions (the ~$10M
   Aguilar damages figure's origin; the Travis County suit's status) — low priority, time-permitting
   only, given two and three prior sessions respectively already diagnosed these as genuine gaps
   rather than under-searched ones.

## 1. FAA-2026-8614 — re-checked directly, still no final rule, comments essentially flat

First raw re-check since 2026-09-07 (18 days). Checked three independent ways:
- **`api.regulations.gov/v4/dockets/FAA-2026-8614`** (via `r.jina.ai` proxy; direct access to this
  API still 403s from this environment, consistent with every prior session): docket
  `category: "Pending"`, `modifyDate: "2026-09-11T15:57:07Z"` — i.e. the docket record itself hasn't
  moved since Sept. 11, and disposition is still "Pending" (not "final rule issued" or any other
  disposition category).
- **`api.regulations.gov/v4/documents?filter[docketId]=FAA-2026-8614`**: exactly one document
  exists in the docket — the original 2026-07-30 Proposed Rule (`FAA-2026-8614-0001`),
  `openForComment: false`, `withinCommentPeriod: false`, `lastModifiedDate: 2026-09-12`. No final
  rule document has been posted.
- **`federalregister.gov/api/v1/documents.json`**, searched both by RIN (`2120-AM51`, zero results)
  and by agency+keyword (`federal-aviation-administration` + "waiver commercial space launch
  reentry", 77 results): the only FAA document matching this specific action is still the single
  2026-07-30 Proposed Rule (`2026-15415`). No final rule.
- **Comment count**: via `api.regulations.gov/v4/comments?filter[docketId]=FAA-2026-8614`, the
  `agencyId: FAA` aggregation count is **3,203** posted comments, up from 3,201 on 2026-09-07 — a
  net increase of 2 over 18 days. This continues the pattern already flagged 09-07 (flat for five
  consecutive prior readings); recommend continuing to deprioritize this specific check to an
  occasional/monthly cadence rather than nightly, per the 09-07 note's own recommendation, which
  this session is following rather than re-litigating.

**Bottom line: no regulatory movement on the waiver NPRM since the comment period closed
2026-09-01.** The docket is procedurally alive (still "Pending," not withdrawn) but nothing has
been decided.

## 2. Aguilar v. SpaceX (1:26-cv-00485) — a real procedural update, not just a re-read of the
## complaint (row 21 added to the corpus table)

Prior sessions (09-14, 09-16, 09-18) read the original complaint's text closely but never pulled
the docket's own entry list — an oversight this session corrected. Fetched the full CourtListener
docket page directly (`curl` with a browser User-Agent, HTTP 200) and parsed all 35 docket entries
as of 2026-09-25. Findings, all **new** to this project's notes:

- **Plaintiffs filed a First Amended Complaint** (Dkt. 23, filed 2026-07-29). Fetched and read the
  actual PDF (61 pages, up from the original's 59). **Confirms the 09-16/09-18 finding still holds
  in the amended version**: a full-text dollar-sign search found exactly 2 hits, both the same
  "$1.75 trillion" SpaceX IPO-valuation reference from the original complaint. **No damages dollar
  figure was added in the amendment either.**
- **SpaceX filed a second Rule 12(b)(6) motion to dismiss** (Dkt. 29, filed 2026-08-12), superseding
  its first motion to dismiss (Dkt. 13, filed against the original complaint, now moot). Fetched and
  read this motion directly (27 pages). It argues Texas law generally bars property-based
  noneconomic damages absent pleaded malice/ill-will/animus, that plaintiffs' trespass theory
  doesn't independently support such damages, and asks the court to dismiss the noneconomic-damages
  claim **with prejudice**.
- **This motion is now fully briefed**: plaintiffs' Response in Opposition (Dkt. 33, 2026-09-09) and
  SpaceX's Reply in Support (Dkt. 35, **2026-09-23 — two days before this session**) are both
  docketed. Neither has a free RECAP-hosted copy yet (both show "Buy on PACER" only, no
  CourtListener/Internet Archive download link) — this project's convention has been not to spend
  money, so their text is not yet pulled; only their existence/dates are confirmed (docket-entry
  metadata tier, not full-text tier).
- An "Order Resetting Initial Conference" also appears (Dkt. 34, 2026-09-22).
- **No ruling on the dismissal motion yet.**

This is a genuinely live, actively-litigated legal question directly relevant to this paper's
framing: a federal court is about to decide whether Texas property law allows noneconomic damages
in a case whose facts (repeated acoustic/structural harm from routine, licensed rocket operations)
sit somewhere between ordinary negligence and intentional nuisance. A ruling either way would be a
new, citable data point on how the legal system is actually processing the claim-vs-outcome gap
this paper is about — worth a periodic docket check going forward rather than re-reading complaint
text repeatedly, which three prior sessions had already done thoroughly.

Added as **row 21** in `Study1_Corpus_and_Coding_DRAFT_2026-08-27.md`.

## 3. Starbase, TX — 7,133-acre annexation finalized 2026-09-21 (new corpus item, row 22)

Found via a general "Starbase Texas news September 2026" search, not something any prior note had
tracked. Cross-checked across three sources:

- **`starbase.texas.gov/c-4-annexation`** (official city page, fetched directly): the city's own
  framing — a "C-4 annexation" is "consent-based under Texas law," requiring landowner
  petition/agreement, plus public notice/hearings/commission review.
- **San Antonio Express-News / Statesman** (published 2026-02-14, when the annexation was first
  proposed; fetched directly via `r.jina.ai` proxy after a direct 403): a property-records analysis
  of the ~800+ properties in the annexation area found **~3,700 acres federally owned, ~1,000 acres
  Texas Parks & Wildlife Department property, and ~2,400 acres private/corporate (including SpaceX
  and affiliated shell companies)** — much of it inside the **Lower Rio Grande Valley National
  Wildlife Refuge** boundary, though both USFWS and TPWD are quoted stating the annexation itself
  doesn't change land ownership/management. This is a **different** parcel from the 775-acre refuge
  land-exchange proposal already tracked in this corpus (row 14 and its related litigation,
  *Center for Biological Diversity et al. v. FAA*) — flagging explicitly so the two aren't
  conflated.
- **RGV Business Journal** (published 2026-09-23, two days after finalization; fetched directly):
  confirms the annexation finalized 2026-09-21, expanding the city from ~1,000-1,100 acres to
  ~8,100 acres — roughly sevenfold. Describes it as "not requested or voluntary," noting only ~12 of
  280 affected property owners signed in support; city clerk Gretchen Norton disputed this
  characterization, saying an acreage cap that applies to involuntary annexations doesn't apply
  here. **This framing dispute (the city's own "consent-based" description vs. this outlet's
  "not requested or voluntary" characterization) is not reconciled** — the actual annexation
  ordinance/petition-signature record (which the city's own page says is available: "parcel list,
  map, voluntary petition form") was not itself fetched this session. Flagged as open, not resolved.
- **A useful counter-example found in the same Express-News piece, worth keeping for balance**: a
  2024 land-swap proposal (43 acres to SpaceX in exchange for 477 acres near Laguna Atascosa NWR)
  was **abandoned by SpaceX** after public outcry and a lawsuit — a concrete case where organized
  opposition changed an outcome, not just documented harm after the fact. Also notes TPWD approved
  sale of 1.9 acres of state park land within city boundaries in Aug. 2025 "despite heavy public
  criticism" (a smaller, successful land transfer in the same period).

This is directly relevant to the paper's regulatory-venue-shifting/local-capture thread (already
anchored 09-10/09-14 via Coen et al. 2020 and Carpenter & Moss 2013, and concretely instantiated in
row 17's City-of-Starbase-incorporation-by-SpaceX-employees finding) — a sevenfold territorial
expansion of a company-dominated municipal government, including land inside a national wildlife
refuge, is a sharper and more recent instance of the same dynamic.

## 4. NPR / Gulf States Newsroom, 2026-09-20 — new on-record quotes (row 23)

Found via a general Vermilion Parish news search; this is a **different** outlet/byline than the
Gulf States Newsroom NDA-count piece already in the corpus (09-05/09-07 notes, the "54 officials"
figure, syndicated via KPEL/KVKI) — same newsroom, different specific story, worth distinguishing.
Fetched the full transcript directly (`r.jina.ai` proxy after a 503 on direct WebFetch).

New, directly quotable material not previously in this corpus:
- **Gov. Jeff Landry, on-record, asked directly by the reporter why the deal was negotiated under
  NDAs**: *"Well, again, you think I want Texas to steal my thunder? You think I want other states
  to know what we're working on?"* — a first-person justification for the NDA practice, distinct
  from (and more candid than) any statement already in the corpus.
- **Gabe Giffin** ("Gator Gabe," Pecan Island outdoor-education guide), on Mississippi-Flyway
  migratory-bird habitat and on official non-transparency: *"Whether you talk about the federal
  administration or on the state level or the NDAs, whatever it is, the elected leaders aren't
  telling the people what's coming down to them."*
- **Brooke Broussard** (Pecan Island bartender), on place-based/cultural stakes, not just economic
  or environmental ones: *"This is my source in a lot of ways... I find a lot of strength here, and
  I find a lot of strength in my family history here... I don't want the story to just be Elon Musk
  came and conquered."*

The piece also independently re-confirms figures already in the corpus (3,000 new LA jobs over 10
years, the aerospace liability-shield and property-tax legislation, construction starting
"by the end of next year," first launch 2029) via a fully independent reporting chain — useful as
corroboration, not as new information on those specific points.

## 5. Literature-gap scouting — third pass; see `literature/Literature_Scouting_2026-09-25.md` for
## full detail

Two real findings, one negative:
- **New anchor**: Bartik (2020), *Economic Development Quarterly* 34(2), and the broader Upjohn
  Institute "but for" incentive-credibility literature — bibliographically verified via Crossref's
  API, content still secondary-sourced. This fills a real gap the two prior literature passes left:
  both existing anchors (Janssen/Swaen/Du 2022, Delmas & Burbano 2011) are about *environmental*
  claims specifically; nothing in the corpus's literature base addressed the *economic-benefit*
  claim type (jobs/investment numbers) that is this paper's other central framing thread (Musk's
  "10,000" vs. LED's "3,000+8,100"; Cameron County's self-reported "$13B/24,000 jobs"). Bartik's
  research program is the standard public-finance/economic-geography anchor for "incentive-linked
  job-creation claims are usually unaudited and often inflated" — a different discipline reaching a
  parallel conclusion to the marketing/CSR-communication literature already anchored.
- **Negative finding, re-confirmed**: still no peer-reviewed academic literature specifically on the
  2026 FAA environmental-waiver NPRM — re-searched, same conclusion as 09-10 (the policy, implementing
  a July 2026 executive order, is too recent). Carpenter & Moss (2013) remains the right general
  regulatory-capture anchor absent waiver-specific literature.
- **Not done**: citation snowballing from any anchor (flagged as the top open item across all three
  literature sessions now — 09-09, 09-10, 09-25 all recommend it, none have done it).

## 6. Lower-priority re-attempts (time-permitting)

- **The ~$10M Aguilar damages figure's origin**: re-searched for a direct `reuters.com` URL for the
  original story (TheNextWeb/Futurism both cite Reuters for the "$100K foundation repair" figure but
  neither links the original). Same negative result as 09-18 — only secondhand citations of Reuters
  surfaced, no direct Reuters URL. Recommend not re-trying this specific WebSearch approach again;
  it has now failed identically twice.
- **Travis County suit (D-1-GN-24-010020)**: still unresolved, consistent with 09-07's "genuine,
  access-blocked gap" diagnosis. One new hazard found and flagged (not a resolution): a WebSearch
  surfaced a **different** case — *South Texas Environmental Justice Network v. TCEQ*, a Third Court
  of Appeals (Austin) ruling on a natural-gas-terminal permit dismissed for lack of subject-matter
  jurisdiction — that shares a party name (STEJN) with, but is not, the SpaceX wastewater-permit
  suit this project tracks. This is the same false-positive pattern the 09-07 note already caught
  once for an unrelated case pair (the TX Supreme Court beach-closure case); flagging explicitly in
  the corpus file so a future session doesn't mistake this ruling for a resolution.

## What this does not do

Does not pick a Study 1 corpus option, theory frame, or lock any design element — unchanged,
Britton's call per `CLAUDE.md`. Did not contact, submit, or post anything externally. Did not spend
any money (declined to buy the two PACER-only Aguilar docket entries). Did not touch any file
outside `SPACEX_LOUISIANA_PAPER/`.

## Still open / next steps

- Aguilar case: check periodically for a ruling on the fully-briefed motion to dismiss (Dkt. 29);
  pull Dkt. 33/35 text if a free copy ever appears on RECAP.
- Starbase annexation's "consent-based" vs. "not requested/voluntary" framing dispute — the actual
  ordinance/petition-signature record would resolve this directly; not fetched tonight.
- FAA-2026-8614 — recommend continuing to check only occasionally (monthly-ish) rather than nightly,
  per 09-07's recommendation, now reinforced by an 18-day gap showing the same near-zero movement.
- Literature: citation snowballing from the now seven anchors (six from 09-09/09-10 plus Bartik
  2020) is the single most-recommended, least-done next step across three sessions.
- Bartik (2020) and the Upjohn "but for" working paper (#289) — both flagged as directly fetchable
  next-session targets, not yet full-text read.
- Unchanged, genuine gaps (not re-attempted tonight, already well-diagnosed by prior sessions):
  TCEQ Docket 2024-1821-IWD's actual signed Commission order; USFWS's 2025 Amended BCO Addendum #2
  document itself; the Jacob Landry NDA document (DocumentCloud-blocked); Act 343/HB1250's and the
  public-records-exemption bill's enrolled legislative text (still news-sourced, not independently
  fetched).
