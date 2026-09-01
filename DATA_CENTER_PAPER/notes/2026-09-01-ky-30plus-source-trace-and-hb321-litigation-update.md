# 2026-09-01 — Kentucky "30+ moratoriums" figure source-traced; HB 321 standing-restriction law found in Simpson County case; pending-item rechecks

Follow-up to `2026-08-31-tx-ky-developer-litigation-pattern-and-open-lead-checks.md`, using the
NC "30+" source-tracing method from `2026-08-29-nc-30plus-claim-resolution-and-greensboro-alamance-verification.md`.
Verification/scouting pass only — nothing added to the working corpus or codebook, no design-lock or
restructuring decisions made. All below are Britton's to act on.

WebFetch worked on most targets tonight (LPM, WDRB, WBKO, Route Fifty, mjbommar.github.io tracker,
Times-Herald-adjacent sources, bgdailynews). Persistent 403s: kentuckylantern.com (every URL tried,
consistent with prior notes' experience), kyrc.org, klc.org, wcluradio.com (one URL 404'd), forwardky.com.
web.archive.org is not fetchable in this environment at all (tool-level restriction, not a site block).

---

## 1. Kentucky's "more than 30 counties/localities" moratorium figure — traced, and it's a different kind of problem than NC's

### Bottom line up front
Unlike NC's "30+" (which traced to one outlet's uncited tally — Carolina Journal, July 31, 2026 — see
08-29 note), Kentucky's figure has a **named, official, on-record source with a described methodology**:
Energy and Environment Cabinet Secretary John Lyons, quoted directly by WDRB (Aug 6, 2026, direct-fetched):
*"We've even started tracking the local ordinances and moratoriums, now numbering over 30."* LPM's
version of the same event (also direct-fetched) attributes the same "more than 30" figure to Lyons.
This is not an anonymous or undocumented press tally — it's a state cabinet secretary describing the
cabinet's own internal tracking effort. **That is a materially stronger provenance than NC's figure.**

**However**, it is still not independently verifiable: no public list or published tracker from the
Cabinet was found (the Cabinet's own website, eec.ky.gov, has no data-center page at all per a direct
fetch tonight), and the number does not match any independent, methodologically-transparent tracker
found tonight — see below.

### Independent tracker check: "Moratorium Nation" (ALEA Institute / Michael J. Bommarito II)
Found via a Green Data Center Guide summary of the nationwide "Moratorium Nation" tracker (533 total
moratorium instruments across 42 states, current through Aug 19, 2026, methodology: ~4,600 primary
documents collected, 348 moratorium texts coded, coordinates verified). Direct-fetched Kentucky's own
page on that tracker (`mjbommar.github.io/moratorium-data-2026/states/kentucky.html`) tonight — it
gives a **specific, dated, sourced table**, not a bare number:

| Jurisdiction | Type | Date Enacted | Status |
|---|---|---|---|
| Bell County | County | 2026-07-02 | 2-year moratorium |
| Boyle County | County | 2026-06-09 | 12-month moratorium |
| Breckinridge County | County | 2025-12-05 | 365-day moratorium |
| Bullitt County | County | 2026-07-21 | 12-month moratorium |
| Cave City | City | 2026-05-21 | 1-year (under legal challenge) |
| Daviess County | County | 2026-05-28 | 1-year moratorium |
| Edmonson County | County | 2026-06-08 | 12-month (covers data centers, AI, crypto mining) |
| Lexington-Fayette | Urban County | 2026-06-09 | Through Oct 31, 2026 |
| Meade County | County | 2026-01-13 | 12-month moratorium |
| Nelson County | County | 2026-07-07 | 12-month moratorium |
| Oldham County | County | 2025-06-26 | Extended indefinitely pending regulations |
| Versailles | City | 2026-06-16 | Through Dec 31, 2026 |
| Mercer County | County (pending) | 2026-07-28 | First reading approved, awaiting second reading |
| Ashland | City (expired) | 2026-02-26 | Replaced by permanent conditional-use ordinance |
| City of La Grange | City (expired) | 2025-06-02 | Expired, no further action |

That's **15 total** (12 active + 1 pending + 2 expired/replaced) as of Aug 19, 2026 — **half of Lyons'
"more than 30"** as of two weeks earlier (Aug 6). If anything the tracker, being more current, should
show *more* than Lyons' figure if his count were accurate, not fewer.

### This tracker is itself demonstrably incomplete — cross-checked against tonight's and 08-31's own direct-fetched facts
The tracker's KY table is **missing** jurisdictions this project has already primary-source-confirmed:
- **Allen County** (Ordinance No. 26-03, 24-month moratorium, ~June 2026 — confirmed via WBKO/WNKY
  tonight, cited in the 08-31 note as a "contagion effect" from Simpson County).
- **London** (city, 2-year moratorium — Kentucky Lantern/Route Fifty, June 8, 2026).
- **Louisville Metro** (24-1 vote, Aug 13, 2026, 6-month interim moratorium — direct-fetched via LPM
  in the 08-30 note).
- **Simpson County's** Dec 2025 ordinance (conditional-use-permit + heavy-industrial-zoning
  requirement — functionally a restriction, arguably not a blanket "moratorium," which may be *why*
  the tracker excludes it, but it's the exact subject of the TenKey litigation covered in 08-31).

So neither number is fully trustworthy on its own: Lyons' "30+" is untraceable to any public list;
the one rigorous, methodologically-documented tracker found is internally consistent and dated but
demonstrably missing at least 4 jurisdictions this project already has primary sources for.

### My own reconstruction from everything checked tonight + 08-31
Combining the tracker's 15 + the 4 primary-confirmed additions above = **19 jurisdictions with
solid, primary-source-level confirmation.** Adding WebSearch-summary-level-only mentions found
tonight but not individually direct-fetched — Jessamine County, Georgetown, Madison County, Greenup
County, Butler County, Scott County (from a WKYT fact-check piece and an Aug 17 Kentucky Lantern
"catch-up" roundup, both WebSearch-summary confidence only) — brings a looser count to **~25**,
still short of "30+."

**Recommendation for Britton, same shape as the NC one:** if this number is used, either (a) drop the
precise "30+" and describe the wave qualitatively (e.g., "a large, ongoing wave; a state cabinet
secretary put the count at over 30 in August 2026, though no public list from that source has been
found and an independent, methodologically-documented tracker counts closer to 15–25 named
jurisdictions as of the same period"), or (b) cite it explicitly as Lyons'/the Cabinet's own
attributed figure, not as an independently confirmed fact. Unlike NC, this isn't a case of an outlet
inventing a number — it's a real government official citing an internal count that simply isn't
public or reconcilable with the best available outside tracker.

### Also worth flagging: the "~30" figure is doing double duty in KY coverage and could get conflated
Separately, multiple KY sources (Kentucky Lantern, May 29, 2026; WKYT fact-check, July 24, 2026) report
that **the Public Service Commission and Kentucky utilities have said "as many as 30 data centers"
are under discussion/in the pipeline in Kentucky** — a completely different figure (proposed *projects*,
not local moratoriums) that happens to also be "~30." Flagging this because it's an easy, plausible
mix-up for anyone skimming KY data-center coverage quickly — a "30 projects" figure and a "30+
moratoriums" figure both circulating about the same state in the same few months are not the same
claim and shouldn't be conflated in the manuscript.

---

## 2. New: a third distinct legal theory in the developer-litigation-countermobilization pattern — Kentucky HB 321 (standing restriction) being used against citizen plaintiffs in the same Simpson County saga

08-31 already covered TenKey LandCo's suit against **Simpson County Fiscal Court** (city-vs-county
jurisdiction theory) and a separate citizens' suit, **Franklin Citizens for Responsible Development v.
TenKey LandCo and Franklin Planning and Zoning Commission**, noting only that oral arguments on
motions to dismiss were heard in July 2026. Chasing that second suit tonight surfaced a genuinely new
detail not in 08-31: TenKey is trying to get the *citizens'* suit dismissed on **standing** grounds
under **Kentucky House Bill 321**.

- **The law:** HB 321, per two independently-fetched sources tonight (Yahoo News syndication and
  Hellbender Newsroom, both republishing the same underlying Kentucky Lantern reporting since the
  Lantern's own URLs 403'd directly) — passed unanimously by Kentucky's Republican-controlled
  legislature, signed by Gov. Beshear (a Democrat), originally framed as a housing-development bill
  (training requirements for planning/zoning officials) but amended late in the session to also
  narrow **KRS 100.347** so that only property owners in the **same zoning classification** as a
  challenged project may sue over a zoning decision.
- **How it's being used:** TenKey's attorneys argue Franklin Citizens for Responsible Development
  lacks standing because its members don't own property in the same zone as the ~200-acre data-center/
  gas-generation project — i.e., a state law meant to speed up housing approvals is being invoked to
  block a citizens' group from challenging a data-center approval.
- **Status:** Judge Mark Thurmond (same judge as the TenKey-vs-Fiscal-Court case) is weighing whether
  HB 321's standing restriction is **constitutional**. At an Aug 24, 2026 hearing he said he had "a
  pretty good idea" of where he was headed but wanted to look more carefully at some issues; another
  hearing is scheduled for **October 2026** (exact date not given in either source — possibly, but not
  confirmed to be, the same Oct 14 status conference already noted for the Fiscal Court case, since
  both are before the same judge in the same overall dispute).
- **On-record opposition:** environmental attorney Tom FitzGerald, representing the citizens' group,
  argues the law unconstitutionally denies Kentuckians "access to the courts where a local government
  decision affects their quality of life."
- **Why this matters for the candidate pattern flagged 08-31:** this is a **third distinct legal
  mechanism** in the developer-litigation-countermobilization pattern, alongside TX's ultra-vires/
  Dillon's-Rule theory and KY's own city-vs-county jurisdiction theory (both already in 08-31) — here
  a state legislature's own recent tort-reform-style law is being repurposed specifically to defeat
  *citizen* (not government) opposition, which is a different target than the other two theories (which
  targeted government authority, not private plaintiffs' standing). Still just flagging the evidence
  base — not proposing to fold this into the candidate `developer-litigation-countermobilization` label
  or any codebook, which stays Britton's call per standing rule.

---

## 3. Cave City — two open items from 08-31 resolved

- **Exact moratorium date:** 08-31 flagged "May 20, 2026" as WebSearch-level only. Direct-fetched
  **WBKO** tonight: *"Cave City implemented a 12-month moratorium on data centers after holding two
  special meetings May 18 and May 20."* Confirms May 20, 2026 as the enactment date (the Moratorium
  Nation tracker's independent entry says May 21 — a one-day gap, same low-stakes pattern as several
  other one-day date slips found in the NC notes; WBKO's direct local-news account naming both meeting
  dates is the better-supported source).
- **Litigation next step:** direct-fetched **Bowling Green Daily News** (Aug 27, 2026): Barren Circuit
  Judge John Alexander confirmed the two consolidated Cave City suits will proceed with the
  **annexation question decided first** (per county attorney Aaron Smith: "if the property was not
  appropriately annexed then the moratorium" wouldn't apply regardless) — discovery on annexation
  begins now, with a **status conference set for November 23, 2026**. This gives a concrete future
  date to re-check, parallel to Simpson County's Oct 14 date.

---

## 4. Pending-item rechecks — all three unchanged, reported plainly as nulls

- **NAACP v. xAI (N.D. Miss.):** WebSearch tonight found nothing past the DOJ's June 16, 2026 motion
  to intervene/dismiss. No new hearing date since the Aug 21 postponement notice already known.
  `courtlistener.com` docket 403'd again on direct fetch — same persistent block as every prior
  attempt, not a resolved gap.
- **Sabey / Decatur Township (Indianapolis):** WebSearch tonight surfaced nothing past the case's
  April 2026 filing status. No ruling on the motion to dismiss or the citizens' judicial-review suit
  found. Genuinely still pending — same null as every check since 08-21/08-22.
- **Louisville Sept 3, 2026 Planning Commission:** confirmed still a future event as of tonight (two
  days out). A fresh WebSearch found the Planning Commission's late-August work session (majority
  vote to keep the hyperscale-data-center ban, and to require most new data centers to go through
  rezoning) — this is the same Aug 20 meeting already fully covered in 08-30/08-31, not new. No
  coverage exists yet of the Sept 3 meeting itself, as expected. Re-check after Sept 3.

---

## What's still open
- **Kentucky's "30+" figure:** now well-characterized (named official source, but no public list; best
  independent tracker gives 15; this project's own reconstruction reaches ~19–25) but still not a
  clean, citable number — same qualitative-framing recommendation as NC's.
- **HB 321 constitutionality ruling** (Franklin Citizens v. TenKey/Franklin Planning Commission): still
  pending, October 2026 hearing, exact date not found.
- **TenKey v. Simpson County Fiscal Court:** unchanged, Oct 14, 2026 status conference (per 08-31).
- **Cave City (Kentucky Industrial Alliance v. Cave City / annexation suit):** now has a concrete next
  date, Nov 23, 2026 status conference on discovery.
- **North State Journal's NC "11 counties/17 towns" figure:** still unread (403'd every attempt across
  multiple sessions) — an archive.org retry isn't possible in this environment (tool-level block, not
  a site block), so this needs either a different fetch path or manual retrieval by Britton.
- **Jessamine County, Georgetown, Madison, Greenup, Butler, Scott counties (KY):** named in passing by
  WebSearch-summary-level sources only tonight, not individually direct-fetched — would need dedicated
  primary-source passes if any of these become corpus rows.
- **NAACP v. xAI and Sabey/Decatur:** both still genuinely pending with no ruling — re-check in a
  future session, no fixed date to anchor to for either.
- Corpus restructuring, the `developer-litigation-countermobilization` candidate code (now with a
  third distinct legal theory in its evidence base), and any codebook additions: untouched tonight,
  all still Britton's call per standing rule.
