# 2026-09-08 — ND Supreme Court appeal narrows (Summit forfeits 2 of 3 permits), Illinois Mahomet Aquifer ban primary-verified, CA Shafter project now operational, light recheck of other tracked items

## What this is

Follow-up on the 09-07 note's open items, focused per tonight's assignment on: (1) tracking the North Dakota
Supreme Court appeal of the amalgamation-law rulings (flagged 09-07 as a live, fast-moving thread), (2) a light
recheck of WV 4th Cir., LA HB7, IN POET v. Wabash, and CA Committee for a Better Shafter for anything new since
09-07, (3) a fresh national sweep for CCS-opposition/regulatory developments not yet in the corpus. Method:
WebSearch for leads, WebFetch/curl + `pdftotext` (poppler-utils, already installed in this environment tonight —
no install needed, unlike 09-07's `pypdf` workaround) to pull and read primary documents directly wherever
possible. Every claim below is marked primary or secondary; ndcourts.gov remains fully blocked to both WebFetch
(403 on every URL pattern tried, including the plain `/supreme-court` landing page) and direct `curl` with a
browser user-agent (curl gets HTTP 200 but the body is the court site's own soft-404 "Page no longer exists"
template) — same access pattern flagged on 09-05 and 09-07, now confirmed a third night running. No PACER
access in this environment.

---

## 1. North Dakota pore-space amalgamation litigation — genuine movement, still secondary-sourced

**Summit Carbon Solutions itself has now moved to narrow the pending North Dakota Supreme Court appeal**, a
significant new development not in the 09-07 note (which only had the Attorney General's office confirming it
would appeal as of a July 27, 2026 article). This is well-corroborated across independent outlets published
**August 31–September 4, 2026** (KFYR-TV, KVRR, Agweek, Carbon Herald, RBN-adjacent trade coverage, and two
regional radio-affiliate pickups — six-plus independent outlets, consistent details, no contradictions found):

- **Summit forfeited two of its three North Dakota CO2 storage permits** (informally "Summit #1" and "Summit
  #2," in Mercer/Oliver/Morton counties). In a filing with the North Dakota Supreme Court, the company stated
  it "determined as a matter of business judgment that they will not proceed with development, construction,
  operation, or implementation of either proposed storage facility." The state Industrial Commission approved
  the cancellations.
- **Summit is now asking the state Supreme Court to limit its own appeal to the single remaining storage area,
  "Summit #3,"** where the company says it has secured roughly 98% of the necessary pore-space storage rights
  and where landowner litigation is less concentrated than the other two areas.
- Recall the underlying posture (per the 09-07 note): a district court voided **all three** storage permits
  earlier in 2026 (the Benson/Northwest Landowners ruling, Dec. 2, 2025, and the Lofgren/Swenson ruling,
  ~March 9–10, 2026, both on state-constitutional-takings grounds), and **both Summit and the state appealed**
  that outcome to the ND Supreme Court — this is the first confirmation found that Summit itself (not just the
  state) is an appellant, which the 09-07 note hadn't established.
- Coverage frames the forfeiture as **"a victory for most opposing landowners"** in the two abandoned areas,
  though only one litigant in the case reportedly owns property within the remaining Summit #3 area — i.e.,
  narrowing the appeal may also narrow who has standing to keep contesting it.

**Sourcing caveat, same limitation as 09-07:** everything above is secondary-sourced tonight. ndcourts.gov
remains blocked (see header note); no docket number, exact filing date of Summit's forfeiture notice, or
briefing/argument schedule was found in any source, primary or secondary. This upgrades the "on appeal" status
from 09-07 (which only had the state's appeal confirmed) to "Summit is now actively litigating the scope of its
own appeal," but the appeal's procedural posture (docket number, schedule) is still not independently verified.

**No new North Dakota Supreme Court ruling on the merits appeal was found** — as of tonight, the case is still
pending; only the scope-narrowing filing is new.

**Why this matters for the paper:** if Britton pursues the ND amalgamation-law theory the 09-07 note flagged as
a potential fifth comparative-litigation axis, this is a live update worth folding in — it shows the litigation
pressure is already reshaping the underlying project (a 2-of-3 permit forfeiture), not just producing court
rulings in the abstract. Worth another check next pass for whether the Supreme Court grants Summit's request to
narrow its own appeal, and for the actual docket number if a working ndcourts.gov access path is ever found.

---

## 2. Other tracked litigation — recheck since 09-07 (one day, so light-touch as expected)

- **WV 4th Cir. No. 25-1384 (WVSORO v. Zeldin):** no change found. The October 30, 2026 Richmond oral-argument
  date confirmed 09-07 stands; searched for any cancellation, rescheduling, or new amicus activity tonight and
  found nothing to contradict it. (Incidentally found a hosted copy of the petitioners' own opening brief PDF,
  via climatepolicyradar.org, confirming the petitioner list — Sierra Club, West Virginia Rivers Coalition,
  West Virginia Highlands Conservancy, represented by Appalachian Mountain Advocates — consistent with the West
  Virginia Highlands Conservancy's own case-announcement page. Not previously itemized in project notes; minor
  addition, not a new development.)
- **LA HB7:** no change since 09-07 (already primary-confirmed dead via the Legislature's own tracker). Did not
  re-attempt the Vote.aspx workaround for the 12-7 committee tally — 09-07 already documented that page requires
  ASP.NET session/postback state a direct fetch can't supply; no reason to expect that's changed in one day, and
  re-trying it tonight wouldn't be a good use of time. Still open for whoever has a browser-based way in.
- **IN POET Biorefining v. Wabash County (3:26-cv-00291-SJF):** no ruling found; still pending, consistent with
  "recently filed" (complaint filed March 5, 2026). One useful secondary find: a Justia PACER-tracker page for
  this docket confirms it's still an active N.D. Ind. South Bend Division case as of a page-generation date
  in the search index; no new entries beyond what 09-07 already established. Local coverage (21Alive, WANE)
  shows continued grassroots organizing around the case (a Wabash County residents' group invited North
  Dakota attorney Derrick Braaten — the same attorney representing landowners in the ND amalgamation cases
  above — to a public meeting on landowner rights), which is a notable cross-state-network detail if the
  paper's comparative framing wants to note that the same plaintiffs'-side counsel network is active in both
  the Indiana and North Dakota fights. Secondary-sourced, not independently confirmed beyond the local TV
  coverage.
- **CA Committee for a Better Shafter v. County of Kern (BCV-24-104003):** no ruling found; still active. **New
  detail, not in prior project notes:** the underlying project, Carbon TerraVault 1 (California Resources
  Corp.), **became operational in May 2026** — began actually injecting CO2 underground — while the lawsuit
  remains pending, per Inside Climate News reporting (republished via Maven's Notebook, July 4, 2026;
  secondary source). This is now California's first operational CCS project, per that reporting. The
  litigation itself hasn't produced a ruling that would have paused construction/operation. Earthjustice
  attorney Michelle Ghafar (representing the petitioners) is quoted arguing Kern County didn't properly
  evaluate pollution/environmental impacts from "speculative industrial projects that may be built to take
  advantage of TerraVault's storage space" — a slightly different framing angle than the CEQA-adequacy summary
  in the 09-05/09-07 notes (adds a "downstream speculative buildout" theory to the existing CEQA-adequacy
  characterization; both are consistent, not contradictory). **Pattern worth flagging for the paper:** this is
  now a second case (alongside ND's Summit #3) where CCS opposition litigation is running in parallel with,
  not ahead of, project construction/operation — a "litigation doesn't necessarily stop the bulldozers" dynamic
  that could be its own comparative dimension if Britton wants one.

---

## 3. National sweep — one genuinely new item, primary-verified

### Illinois — Mahomet Aquifer carbon-sequestration ban (SB1723 / Public Act 104-0119) — primary-verified, not previously in project notes

This is distinct from the Illinois SAFE CCS Act (SB1289, a CO2-pipeline moratorium tied to PHMSA rulemaking)
already logged in the 09-03 note — **SB1723 is a separate bill**, specifically about sole-source aquifers, and
wasn't in the corpus before tonight.

**Primary-source pull:** downloaded the actual Public Act PDF directly from the Illinois General Assembly's own
site (`ilga.gov/Documents/Legislation/PublicActs/104/PDF/104-0119.pdf`) and extracted all 9 pages with
`pdftotext`. Confirms:

- **Public Act 104-0119 (SB1723 Enrolled)**, amending the Illinois Environmental Protection Act (415 ILCS 5).
  The PDF's own metadata shows a creation date of **August 4, 2025** (consistent with secondary reports of an
  August 1, 2025 gubernatorial signature — I could not find an explicit "Section 99. Effective date" clause in
  the extracted text to independently confirm the exact effective date; secondary sources, e.g. the Illinois
  State Bar Association's own daily legal news post, say it took effect **January 1, 2026**. Flagging this as
  not independently primary-confirmed on the effective-date specifically, though the substance of the Act
  itself is primary-confirmed.)
- **The operative prohibition, quoted directly from the amended Sec. 59.5(g):** *"No person shall conduct a
  carbon sequestration activity within a sequestration facility that overlies, underlies, or passes through a
  sole source aquifer. Nothing in this subsection deprives the Agency of authority to deny a carbon
  sequestration permit."* This is **broader than a Mahomet-specific ban** on its face — it applies to any
  sole-source aquifer in Illinois — though the bill's findings section and the rest of the Act are written
  specifically around the Mahomet Aquifer (central Illinois' sole source of drinking water for the region) and
  a real corrosion/CO2-migration leak incident at ADM's Class VI well in Decatur, IL that the findings section
  explicitly cites as motivating context.
- **Creates a "Mahomet Aquifer Advisory Study Commission"** (new Sec. 59.18): 21 legislatively-appointed
  members, must hold its first meeting within 90 days of the Act's effective date, meetings must be held within
  the Mahomet Aquifer region or within 25 miles of it and open to the public. The University of Illinois's
  Prairie Research Institute must submit a final safety/risk assessment report (covering effects on human,
  animal, and environmental health, and comparison to how other states' CCS projects have affected aquifers) no
  later than **December 31, 2030**, with annual status reports starting **December 31, 2027**. The Commission
  itself dissolves and the section repeals on **January 1, 2032**.
- Secondary sources (Illinois State Bar Association, Daily Illini, Capitol News Illinois) confirm strong
  bipartisan passage: **Senate 55-0** (one secondary source), **House 91-19**, signed by Gov. Pritzker.

**Why this matters for the paper:** this is a genuinely different regulatory posture than anything else in the
project's national-comparison table — not litigation (courts striking something down after the fact) and not a
moratorium tied to a federal rulemaking timeline (like Illinois's own SB1289), but a **legislature imposing a
categorical, geography-defined ban** directly in response to a documented leak incident, paired with a
multi-year state-funded science-review commission running through 2032. If the paper's national/comparative
framing wants a "legislative preemption via categorical geographic ban" axis distinct from the standing
(5th Cir.), eminent-domain (LA), home-rule/preemption (IN), CEQA (CA), and forced-pore-space-taking (ND)
theories already catalogued, this is a clean sixth example — and it's the only one in the current set that
succeeded through the legislature rather than the courts.

### No other new litigation/regulatory items found

Checked Colorado's Class VI primacy status (still "proposed," comment period closed May 4, 2026, no final rule
found as of tonight — unchanged from 09-05/09-07) and ran several general sweeps for "carbon capture opposition"
news from the last few days; nothing else surfaced that wasn't already in the project's notes or covered above.

---

## What's still open / worth Britton's attention

- **North Dakota: Summit is now actively trying to narrow its own Supreme Court appeal** to just the Summit #3
  storage area, having forfeited the other two permits — a live update to the 09-07 "fifth comparative-theory"
  lead, still not primary-source-verified (ndcourts.gov blocked a third night running; no PACER access here).
  Worth a dedicated pass whenever a working access path to ndcourts.gov or PACER is available, and worth
  checking again next session for whether the court has ruled on Summit's narrowing request.
- **New: Illinois SB1723 / Public Act 104-0119 (Mahomet Aquifer sole-source-aquifer ban)** — primary-verified
  from the Act's own text, ready to cite. Only the exact effective date (Jan 1, 2026 per secondary sources)
  isn't independently confirmed against the primary document's own effective-date clause; everything else about
  the Act's substance is confirmed directly. Not yet vetted for fit into any specific theory chain — that's
  Britton's call, same as the ND/IN/CA/LA leads already flagged.
- **CA Committee for a Better Shafter:** Carbon TerraVault 1 is now operational (May 2026) despite the pending
  lawsuit — worth noting if the paper discusses whether litigation actually delays CCS buildout in practice.
  Same now true, differently, for ND's Summit #3 (litigation reshaping scope, not stopping the underlying
  project).
- **LA HB7's exact 12-7 committee vote tally remains secondary-only** (ASP.NET-gated Vote.aspx page); not
  re-attempted tonight, unchanged limitation from 09-07.
- **Cross-project note (not this paper, but relevant to sourcing rigor):** attorney Derrick Braaten appears as
  counsel or a cited resource in both the Indiana POET v. Wabash County grassroots organizing and the North
  Dakota amalgamation litigation — a real plaintiffs'-side network detail across two of this project's tracked
  cases, secondary-sourced (local TV coverage), not independently verified against a bar-admission or
  appearance filing.
- **Tooling note for next pass:** `pdftotext`/poppler-utils was already installed in this environment tonight —
  no `pip install` workaround needed this time (contrast with 09-07, which needed a fresh `pypdf` +
  `cffi`-reinstall). Whether PDF tooling is preinstalled appears to vary session to session; worth checking at
  the start of each pass rather than assuming either way.
- **Unchanged, explicitly not touched tonight per instructions:** McCauley volume-number issue, docx "51 vs.
  58" reconciliation, Track A/B/C, the date-convention pick, and any theme/Phase-3/design-lock decisions all
  remain Britton's, untouched. No new theory chain, Track choice, or theme was locked — the North Dakota,
  Illinois, and "litigation vs. operational reality" observations above are proposed additions/leads only.
