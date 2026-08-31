# 2026-08-31 — FAA docket deadline-day check + Boca Chica CWA claim independently verified

Follow-up to `2026-08-30-boca-chica-citation-and-faa-docket-check.md`. Today is the date the FAA
comment period was expected to close. Two tasks: (1) a same-day docket recheck using last night's
documented curl+jina+api.regulations.gov technique, prioritized per tonight's task instructions;
(2) resolving the Boca Chica 2024 Clean Water Act penalty claim against a primary enforcement
record, since three prior notes (08-27, 08-29, 08-30) all left it at "commenters state, not
independently verified." **No theory chain, coding scheme, or Study 1 option (A/B/C) decided or
touched here — still Britton's call**, per standing project rules.

## 1. FAA-2026-8614 — comment period status: NOT YET CLOSED, closes tonight

**This is the single most important finding tonight and updates the framing in the 08-30 note,
which described the deadline as "tomorrow."** Checked directly against the docket's own document
record (`api.regulations.gov/v4/documents?filter[docketId]=FAA-2026-8614`, via the curl+r.jina.ai
technique documented 08-30), which carries structured fields for exactly this:

```
"commentEndDate" : "2026-09-01T03:59:59Z"
"commentStartDate" : "2026-07-30T04:00:00Z"
"openForComment" : true
"withinCommentPeriod" : true
"allowLateComments" : false
```

`2026-09-01T03:59:59Z` is 11:59:59 PM Eastern Time on **2026-08-31** — i.e., the FAA's own system
still shows the docket open, with the close time being end-of-day Eastern tonight, not an earlier
cutoff. `allowLateComments: false` means once that clock hits, filings genuinely stop counting
(no grace window). The r.jina.ai proxy's own server clock, visible in one fetch's error output,
read `Mon Aug 31 05:17:36 GMT 2026` — i.e., this check was run at roughly 05:17 UTC (~12:17 AM
Central) on 2026-08-31, meaning **the docket was still open with roughly 22-23 hours left in the
comment window at the time of this check**, not closed. Anyone reading this note later today
should treat "closed" as not yet true until after ~11:59 PM Eastern / 10:59 PM Central tonight.

**Total comment count: still 1,453** — identical to the 08-30 note's figure, confirmed both via
`meta.aggregations` on an unfiltered docket query and via `meta.totalElements` on the same query.
This is a genuinely informative negative finding: the count has not moved at all between last
night's check and this one.

**Nothing new posted or modified since 08-30's check, confirmed two independent ways:**
- `filter[postedDate][ge]=2026-08-29` on the comments endpoint returns `totalElements: 0`.
- Sorting the full comment set by `-lastModifiedDate` (descending), the most recent item by both
  `postedDate` and `lastModifiedDate` across the entire 1,453-comment docket is still
  `FAA-2026-8614-1454`, timestamped `2026-08-28T23:12:21Z`. No comment newer than that exists in
  the index as of this check.

**141 of 1,453 comments still mention "Vermilion"** — unchanged from the 08-30 count
(`filter[searchTerm]=Vermilion`, `totalElements: 141`).

**Targeted searches, rerun and still empty:** `filter[searchTerm]=StopSpaceX` (0), `filter[searchTerm]=Hensgens`
(0), `filter[searchTerm]="police jury"` (0). No filing from a named Vermilion Parish official, the
StopSpaceX group, or referencing a parish police jury has appeared, same as last night.

**One new-to-the-corpus item surfaced while sorting by most-recent-modified**, dated 08-28 (so it
was technically already indexed as of the 08-30 check, just not individually called out there):
`FAA-2026-8614-1451`, filed by "Airport Concerned Citizens (ACC) of Georgetown, Texas," full text
read directly. It is **not** about Vermilion Parish or Boca Chica — it's a general-aviation-airport
group near Austin, TX, concerned about the same NPRM's waiver framework as applied to Georgetown
Municipal Airport's location over the Edwards Aquifer (a sole-source drinking-water aquifer), and
it formally endorses a separate comment from the "Aviation Impacted Communities Alliance" (AICA,
comment ID FAA-2026-8614-0727, not independently pulled tonight). Noting this only as one more data
point that the NPRM is drawing organized opposition nationally, across unrelated aviation contexts,
not spaceport-specific ones — same pattern as the Merritt Island/Canaveral coalition letter flagged
08-30. Not Louisiana corpus material; don't file it as such.

**Bottom line for Britton**: as of ~05:17 UTC / ~12:17 AM CT on 2026-08-31, the docket is still
open, nothing organizationally new has landed since 08-28, and the true test — whether a
last-minute surge shows up before the actual close (~11 PM Central tonight) — can only be checked
by a pass run after that time. If another overnight or day-of session runs later today or tomorrow
morning, rerunning the same `filter[postedDate][ge]=2026-08-29` and `filter[searchTerm]=Vermilion`
queries via this same technique is the fastest way to catch a late surge.

## 2. Boca Chica 2024 Clean Water Act violation claim — now independently verified against the primary EPA enforcement record

Three prior notes (08-27 via the wildlife letter, 08-29 reading that letter in full, 08-30 finding
a second commenter making the same claim) all correctly declined to treat the Boca Chica CWA
violation as more than "commenters state." Tonight, found and read the actual EPA enforcement
document directly.

**Source**: EPA Region 6 Consent Agreement and Final Order, Docket No. CWA-06-2024-1768, hosted
directly on epa.gov: `epa.gov/system/files/documents/2024-09/spacex_cafo_cwa-06-2024-1768_txu09110_090624__0.pdf`.
Fetched via `curl` (HTTP 200, 263KB), extracted with `pdftotext -layout` (poppler-utils, same
tooling used 08-29) — direct text extraction, not an AI-summarized read, and not routed through a
proxy since epa.gov didn't block the fetch.

**What the CAFO actually says, verified directly from the extracted text:**
- Respondent: Space Exploration Technologies Corp. (SpaceX). Facility: the Starbase Launch Pad
  site, Cameron County, TX (coordinates given in the document: 25.996454, -97.154724).
- **Legal basis**: Class II civil administrative penalty proceeding under CWA Section 309(g), 33
  U.S.C. § 1319(g). SpaceX did not hold a TPDES (Texas Pollutant Discharge Elimination System)
  permit under CWA Section 402 at the time of the discharges, and was therefore not authorized to
  discharge pollutants from the facility into "waters of the United States" — the wetlands
  bordering the launch pad, which the CAFO states have "a continuous surface connection to the Rio
  Grande."
- **Eight specific unauthorized discharges are itemized in the document, by date**, 2022–2024:
  - July 11, 2022 — a liquid oxygen spill, 36,000 gallons, to the wetlands.
  - July 28, 2023 — first full test of the launch-pad water deluge system; ~45,300 of ~114,000
    gallons used discharged to bordering wetlands.
  - August 6, 2023; August 25, 2023; December 29, 2023; May 29, 2024 — four separate Starship
    Super Heavy static-fire tests, each with ~37,000 gallons of deluge water discharged to
    wetlands (out of ~194,500 gallons used per test, with the remainder vaporized or captured).
  - November 18, 2023, and June 6, 2024 — two Starship launches, each with ~34,200 gallons of
    deluge water discharged to wetlands (out of ~180,000 gallons used per launch).
- **Penalty**: SpaceX agreed to a civil penalty of **$148,378**, paid within 30 days of the Final
  Order's filing. (This is the EPA/federal penalty; it is separate from and larger than the $3,750
  TCEQ state-level fine reported by CNBC/Aviation Pros in press coverage — the CAFO document itself
  only speaks to the federal penalty, so the $3,750 figure should still be sourced to state-level
  reporting, not this document, if cited.)
- **Admission status, quoted directly from the document's own terms**: SpaceX "admits the
  jurisdictional allegations set forth in Section III of the CAFO" but "neither admits nor denies
  specific factual allegations set forth in Section IV of the CAFO" (Section IV is the section
  listing the eight discharges above). This is a meaningful nuance for the paper's claim-specificity
  framing: SpaceX accepted the penalty and jurisdiction, but the CAFO's own language is explicit
  that it does not constitute an admission of the specific facts — worth preserving that distinction
  rather than characterizing this as SpaceX admitting to the violations.
- **Compliance steps referenced in the same document**: SpaceX applied for a TPDES individual
  wastewater permit (TX0146251) on July 1, 2024, and signed a separate TCEQ Agreed Order (Docket
  No. 2024-1282-IWD-E) on August 13, 2024, requiring future discharge sampling and effluent limits.
- **Signature date**: the extracted text's own signature-block lines are blank (the actual
  signature/date appears to have been an image or stamp that `pdftotext` didn't capture as text),
  so the precise execution date isn't independently confirmed from the document text itself. The
  filename (`...090624...`) and a WebSearch-surfaced secondary source both point to on/around
  September 5-6, 2024; treat that specific date as secondary-sourced, not primary-verified, if it
  matters for citation precision — everything else above (docket number, penalty amount, discharge
  dates/volumes, admission language) is read directly from the primary document itself.

**This upgrades the paper's evidentiary basis meaningfully**: the Boca Chica CWA claim, which
before tonight rested on "the wildlife groups' letter says so" plus "a second individual commenter
says so," is now backed by the actual federal enforcement record, independently fetched and read —
tier A, not "commenters state." The specific discharge-by-discharge detail (dates, volumes, which
test/launch) is also new material not previously in this project's notes and is exactly the kind
of granular fact that would let a claim-specificity coding scheme code the *company's* Boca Chica
history at the same level of detail the paper already applies to LED's Vermilion figures.

## 3. What's still open (unchanged or updated from prior notes)

- No theory chain, coding scheme, or Study 1 option (A/B/C) decided — unchanged, still Britton's
  call.
- **A true post-deadline docket check is still the single most useful next step for this paper's
  corpus work**, if any session runs after ~11 PM Central tonight (2026-08-31) or tomorrow morning —
  this check confirms the docket was still open and static as of ~12:17 AM CT, not what happened in
  the final hours before close.
- The Exxon-Vermilion-Parish wetland-loss lawsuit detail from the Wesolick FAA comment (flagged
  08-30) is still not independently checked against a court record.
- The exact CAFO signature date (Sept 5 vs. 6, 2024) is secondary-sourced only, not primary-verified
  — low-stakes but worth a quick primary check if the manuscript ever cites the CAFO to the day.
- The $3,750 TCEQ state fine (distinct from the $148,378 federal EPA penalty verified above) is
  still sourced only to news coverage (CNBC, Aviation Pros), not a directly-fetched TCEQ enforcement
  record — a reasonable next Boca Chica corpus item if a future session has time.

## 4. Corpus table update

Updated `Study1_Corpus_and_Coding_DRAFT_2026-08-27.md`, row 9 (previously "Unidentified academic/
ethnographic research program," tier C) with the Palacios thesis citation resolved 08-30, and
upgraded the CWA-violation note in row 4/the Boca Chica section to reflect tonight's primary-source
verification. See that file for the current table; not duplicating the full row text here.
