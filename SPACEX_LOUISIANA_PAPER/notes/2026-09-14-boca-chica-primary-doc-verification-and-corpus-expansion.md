# 2026-09-14 — Direct-fetch verification of the two items flagged 09-09, plus Boca Chica corpus
# expansion (Starbase incorporation)

AI-run background-agent research pass (Claude, via Claude Code). Read-only web research and direct
document fetches only — no design/theory-chain decision made, nothing submitted or contacted
externally, no git operations performed. Executes the two specific follow-ups flagged as open in
`2026-09-09-boca-chica-claim-verification-forced-paragraph.md` (search-snippet tier only, not yet
direct-fetched) and continues general Boca Chica ex-ante-vs-ex-post corpus building per this
project's standing early-stage instructions (corpus-gathering/primary-source verification only — no
Study 1 option or theory-chain choice made, unchanged, still Britton's call).

## 1. Cameron County's escalating economic-impact claims ($800M → $13B/24,000 jobs)

### 2024 figure ($800M+): re-confirmed at PRIMARY-DOCUMENT tier — and a correction to the record

Direct `curl` fetch tonight of Cameron County's own hosted PDF succeeded again:
`https://www.cameroncountytx.gov/wp-content/uploads/2024/06/2024.6.18-STARBASE-LOCAL-IMPACT-PR-2.pdf`
(HTTP 200, 3.87MB). This reconfirms the same document already fetched and read on 2026-09-05 (see
`2026-09-05-faa-quiet-nda-document-and-osprey-loi-found.md`, section 2a) — **the 2024 $800M+ figure
has actually been at primary-document tier since 09-05**, not search-snippet tier. The 09-09 note's
framing ("not yet via a direct fetch... worth a follow-up direct pull") appears to be an oversight —
that session's forced-paragraph exercise cited the 09-04 corpus note but didn't cross-check the 09-05
note four days later in the same notes folder. Correcting the record here rather than silently
re-doing already-finished work: **the $800M figure was already primary-tier; tonight only
re-validates it still resolves (HTTP 200, same file).**

### 2025/2026 figure ($13B economic output / 24,000 jobs): genuine direct-fetch attempt made, stays at SEARCH-SNIPPET tier

Tried multiple direct-fetch paths tonight, all documented rather than skipped:
- The live Cameron County page found via search, `cameroncountytx.gov/2026-spacex-economic-impact-
  release/`, returns **HTTP 404** on both `curl` and WebFetch — the page appears to have been
  removed or restructured since the report's October 22, 2025 release.
- Guessed PDF paths following the 2024 file's naming convention
  (`wp-content/uploads/2025/10/2025.10.22-STARBASE-LOCAL-IMPACT-PR*.pdf` and variants) all return
  HTTP 404 — no equivalent standalone PDF found at a guessable URL.
- The Wayback Machine has an archived snapshot of the missing page
  (`web.archive.org/web/20260316233954/...`), but this environment cannot reach it: WebFetch
  explicitly refuses `web.archive.org`, and a direct `curl` (including with a browser user-agent)
  returns HTTP 403. This is a genuine environment/tooling limitation, not a skipped step.
- `texasborderbusiness.com`'s coverage says an image of the full press release is embedded in their
  article, but the page provides no extractable figures or a standalone document link.

**Net result: still search-snippet tier**, but meaningfully strengthened — now corroborated
consistently across **five** independent outlets (up from three on 09-09): Spectrum News,
Yahoo Finance/RGV Business Journal (same wire content), ValleyCentral, and Texas Border Business,
all attributing the same figures to Cameron County's October 22, 2025 "Starbase Local Impact
Report" release and consistently quoting Judge Eddie Treviño Jr. The figures themselves, consistent
across all five: **$13 billion** gross economic output and **~24,000** local jobs supported "through
2026"/"over the past two years," **$305 million** in indirect tax revenue, **$147 million** in local
supply-chain spending, employment rising from 3,400 (2024) to an expected ~8,000 in 2026. Do not cite
as primary-document-verified in any manuscript text — cite as multiply-corroborated news reporting of
a county release, same caveat as before, just with more outlets behind it.

## 2. Resident property-damage lawsuit (previously sourced only via eciks.org) — UPGRADED to PRIMARY-DOCUMENT tier

This is a real, confirmed lawsuit, not an eciks.org-only claim. Found the actual case name and
number via news search (`Aguilar et al. v. Space Exploration Technologies Corp.`, No.
**1:26-cv-00485**, filed in the **U.S. District Court, Southern District of Texas, Brownsville
Division**) and then located the real complaint's RECAP/CourtListener storage URL. **Fetched the
actual 59-page federal complaint directly** (`storage.courtlistener.com/recap/...`, HTTP 200,
1.22MB PDF) and read it with `pypdf` (this environment's `pdftotext`/poppler CLI is not installed
this session — same recurring gap other recent notes flagged; `pypdf`, already present, worked
fine).

**Confirmed directly from the complaint itself:**
- Case caption, docket header, and case number match exactly: "Case 1:26-cv-00485 Document 1
  Filed 04/30/26 in TXSD Page 1 of 59," Southern District of Texas, Brownsville Division.
- **80 named plaintiffs** (individuals, married couples, two estates, and one family trust),
  all Texas citizens residing in Cameron County except one Washington-state plaintiff, versus
  defendant **Space Exploration Technologies Corp.**, described in the complaint as a Delaware-
  incorporated, Texas-domiciled for-profit corporation headquartered at its Starbase facility,
  1 Rocket Road, Brownsville, TX.
- Jurisdiction invoked: 28 U.S.C. § 1331 and the **Commercial Space Launch Act, 51 U.S.C. §
  50914(g)** (exclusive federal jurisdiction over third-party property-damage claims from
  licensed commercial launch activity).
- Core factual allegation, direct from the complaint's own text: "As a result of SpaceX's
  Starship operations, Plaintiffs' homes have been subjected to repeated intense and damaging
  acoustic events."
- Three causes of action (confirmed via a targeted extraction of the complaint's claims
  sections): negligence, gross negligence (seeking exemplary damages, citing the April 2023 test
  that destroyed SpaceX's own launch pad as evidence of known risk), and trespass (intentional
  direction of acoustic energy onto plaintiffs' properties).

**Not independently confirmed from my own read of the PDF** (only from secondary news coverage,
so flagging the tier distinction honestly): the ~$10M total damages figure, the specific "$100K
foundation repair" claim for one plaintiff, and the 53-homes/11-test-flights counts — these come
from MyRGV.com, RGV Business Journal, TheNextWeb, and Futurism coverage, not from the specific
complaint pages read tonight (the full 59 pages were not read end-to-end; the caption, parties,
jurisdiction/venue, and opening factual-allegations sections were, plus the causes-of-action
section via a separate extraction). Treat the case's existence, parties, causes of action, and
core factual theory as primary-document-verified; treat the specific dollar figures and headline
counts as still search-snippet tier pending a full read of the damages/prayer-for-relief sections.

**Bottom line: this claim is real, not fabricated or exaggerated by eciks.org** — an actual federal
mass-tort complaint exists, filed nine days before eciks.org's characterization implies. This is a
strong, citable addition to the ex-post outcomes side of the Boca Chica comparison.

## 3. Corpus expansion: City of Starbase incorporation (May 2025) — new PRIMARY-DOCUMENT-tier item

Not previously in this project's notes (checked: no prior mention of "City of Starbase" or
"incorporation" anywhere in the project). Found via this session's economic-impact search and
independently verified.

**Fetched Cameron County's own official election-results PDF directly**
(`cameroncountytx.gov/elections/wp-content/uploads/2025/05/City-of-Starbase-Summary.pdf`, HTTP 200).
Confirmed directly from the document (an official "Unofficial Results Summary Results Report,"
May 3, 2025, Cameron County Elections Dept.):
- Incorporation vote: **212 For / 6 Against (97.25%)**, 283 registered voters, 78.80% turnout.
- Mayor, City of Starbase: **Bobby Peden**, unopposed, 216 votes (100%).
- Commissioners (vote for 2): **Jordan Buss** (177 votes, 48.49%) and **Jenna Petrzelka** (188
  votes, 51.51%), both unopposed for the two seats.

**Search-snippet tier only** (from CNBC's contemporaneous coverage, not the election PDF itself,
which lists names/votes with no employer information): Bobby Peden is SpaceX's VP of Test and
Launch Operations; Jordan Buss is SpaceX's Environmental, Health & Safety director. Most of the
~300 eligible voters are SpaceX employees or contractors living on company property.

**Why this belongs in the corpus**: this is a concrete, primary-document-verified instance of the
regulatory-venue-shifting/regulatory-capture theoretical thread already anchored in this project's
literature (Coen et al. 2020 venue-shopping; Carpenter & Moss 2013 capture-theory definition, per
`literature/Literature_Deepening_2026-09-10.md`) — not a company routing around an existing
regulator, but a company's own senior employees *becoming* the municipal government with zoning,
permitting, and local-ordinance authority over the facility they operate. It is a sharper, more
literal ex-post outcome than anything currently in the corpus for the "does the same playbook look
different once you know how the last site actually played out" moderator candidate from the
08-27 orientation note.

## What this does not do

Does not pick a Study 1 corpus option, theory frame, or lock any design element — unchanged,
Britton's call per `CLAUDE.md`. Did not contact, submit, or post anything externally. Did not run
any git commands (add/commit/push) — per tonight's explicit instruction, left for whoever
integrates all of tonight's parallel work. Did not touch any file outside
`SPACEX_LOUISIANA_PAPER/`.

## Still open / next steps

- The 2025/2026 Cameron County economic-impact figures ($13B/24,000 jobs) remain uncitable as
  primary-document tier — the county's own hosted page/PDF for that release could not be located
  live or via Wayback in this environment. A human with a real browser (or a future session with
  Wayback access) could likely resolve this in minutes; not worth further automated attempts
  tonight.
- The Aguilar v. SpaceX complaint's damages/prayer-for-relief sections (pages beyond what was
  read tonight) should be read directly before citing the ~$10M/foundation-repair figures as
  primary-verified rather than news-sourced.
- The City of Starbase incorporation is a strong new corpus item; worth folding into
  `Study1_Corpus_and_Coding_DRAFT_2026-08-27.md`'s inventory table alongside the other primary
  Boca Chica documents once Britton's design-lock conversation happens (not done here — that
  file wasn't touched tonight to keep this a small, reviewable step; flagging instead of editing
  it unprompted).
- Corpus table maintenance: whoever next touches `Study1_Corpus_and_Coding_DRAFT_2026-08-27.md`
  should correct the 2024 $800M row's tier (already Tier A/primary since 09-05, not Tier B) if it
  hasn't been corrected already — tonight's note above documents the discrepancy but doesn't edit
  that file directly.
