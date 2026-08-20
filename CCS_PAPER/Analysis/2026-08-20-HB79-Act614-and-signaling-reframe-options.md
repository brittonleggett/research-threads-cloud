# 2026-08-20 — HB79 primary-source status, two reframing options for Britton, and a session-wide legislative pattern that changes the picture again

## 1. WebFetch status — still blocked, 9th consecutive session

Tested against `en.wikipedia.org` (the standing control) before anything else tonight:

```
error_type: EGRESS_BLOCKED
domain: en.wikipedia.org
message: Access to en.wikipedia.org is blocked by the network egress proxy.
```

Same failure mode as every session since 08-13 (now 08-13, 14, 15, 16, 17, 19, 20 — nine
sessions). Did not re-attempt `legis.la.gov/Legis/BillInfo.aspx?i=249698` directly since the
control failure already establishes this is a network-wide egress block, not a domain-specific
one — retrying the actual target would just burn a call for the same known answer. Everything
below is WebSearch-summarized, same standing caveat as every CCS_PAPER note since 08-13.

## 2. HB79 — Act number found (WebSearch/LegiScan confidence, not a direct primary-source read)

Two independent WebSearch queries, both pulling from LegiScan's bill-status summary, agree:

**HB79 was signed by the Governor and is now Act 614, effective 08/01/2026.**

This is a real step up from 08-19's note (which had the House/Senate floor votes but explicitly
flagged the governor's signature and Act number as unconfirmed). It is **not** the primary-
source confirmation the 08-19 note called for, though — that still requires actually reading
`legis.la.gov/Legis/BillInfo.aspx?i=249698` or a legislative-history document, which WebFetch
still cannot do. Treat "Act 614" as search-summary-confidence (two independent hits, consistent,
LegiScan-sourced) rather than a verified primary-source citation. **`legis.la.gov/Legis/
BillInfo.aspx?i=249698` remains the top WebFetch target for this thread** — it would upgrade
"Act 614" from search-confidence to a real citable primary source and confirm the exact
signature date.

**One vote-count discrepancy resolved, not a new error to flag:** 08-19's note cites House
passage 70-25 (May 11). A search tonight separately surfaced "79-18." These are not
contradictory — they're two different House votes: **70-25 was the original floor passage
(May 11); 79-18 was a later House vote to concur in Senate amendments (May 29)**, per the same
search pass. Both numbers are consistent with a bill that passed comfortably twice. Noting this
explicitly so it doesn't look like an unresolved conflict in the corpus record.

## 3. A session-wide pattern that complicates the reframe further: HB804, the "Louisiana Energy Protection Act"

This wasn't in any prior CCS_PAPER note and changes the shape of the reframing question. Same
2026 session, same governor's desk, roughly the same weeks as HB79:

- **HB804 (Rep. Brett Geymann, R-Lake Charles), the "Louisiana Energy Protection Act,"** bars
  civil suits in Louisiana state courts seeking damages tied to greenhouse-gas emissions/climate
  change, unless the defendant violated a specific emissions law, permit, or workplace-safety
  standard, and the plaintiff can prove by clear-and-convincing evidence the defendant caused
  more than 50% of the alleged damages. It also bars claims based on out-of-state emissions.
- **Passed with much wider margins than HB79**: House 92-5 on initial passage, Senate 31-3, then
  House concurrence in Senate amendments 93-4. **Signed by Gov. Landry**, reporting clusters
  around June 13-16, 2026 (American Press, thecentersquare.com, Louisiana Radio Network, AOL/
  wire pickup — consistent across independent outlets).
- Sponsor's own stated purpose, on the record: "to prevent lawsuits against fossil fuel
  companies, against people, against businesses, against government agencies, against
  nonprofits, for a claim for damages related to climate change."
- Sources: [American Press](https://americanpress.com/2026/06/13/landry-signs-law-limiting-climate-change-lawsuits-in-louisiana/), [The Lens (early coverage)](https://thelensnola.org/2026/04/10/louisiana-energy-protection-act-climate-liability-oil-companies/), [LABI (industry association, "Energy Protection Act Clears Legislature")](https://labi.org/804final/), [Louisiana Illuminator (climate-lawsuits framing)](https://lailluminator.com/2026/04/24/climate-change-lawsuits/), [American Press (amendment coverage)](https://americanpress.com/2026/05/28/geymanns-climate-bill-amended-to-allow-legacy-coastal-suits/)

**Why this matters for CCS_PAPER specifically:** HB804 is not CCS-specific — it's a
sector-wide climate-liability shield for Louisiana energy production generally. But it passed
the **same legislature, the same governor's desk, the same session** that also passed HB79
(removing the CCS-specific $250K damages cap) with much narrower margins, while killing the
parish local-option bills (HB5/6/7, see below) outright. Read together, the session did not
uniformly help or hurt industry on liability — it did three different things to three different
liability questions at once. That's the material the reframe below works from.

## 4. Local-option bills (HB5/6 package) — a concrete, quoted rationale for why they died, not just "they died"

New this session: a specific, on-the-record reason for the committee kill, not just the outcome
already known from 08-16/08-19 notes.

- **Louisiana Illuminator, May 20, 2026** ("Local CO2 storage approval rejected in Louisiana
  Legislature"): the six parish-referendum bills failed in the House Natural Resources Committee
  in close votes (HB5, the broadest version, 7-9). **Officials' stated reasoning**: the
  local-control bills would likely cost the state money defending lawsuits, and could risk the
  federal government **revoking Louisiana's Class VI primacy** (granted 2023) — i.e., the
  argument against the bills wasn't "this is bad for the CCS industry," it was "this threatens
  the state's own regulatory authority over CO2 injection wells."
- Source: [Louisiana Illuminator, "Local CO2 storage approval rejected in Louisiana Legislature," May 20, 2026](https://lailluminator.com/2026/05/20/carbon-storage-4/) (also syndicated at [News From The States](https://www.newsfromthestates.com/article/local-co2-storage-approval-rejected-louisiana-legislature) and [Yahoo News](https://www.yahoo.com/news/articles/local-co2-storage-approval-rejected-120804423.html))

This is the load-bearing fact for reframing Option B below: the stated reason the local-option
bills died is about **state regulatory authority/primacy**, not industry protection per se.

## 5. Two reframing options for Britton — not a decision, just well-reasoned alternatives

The 08-19 note flagged that the old framing ("property-rights/liability bills all died except
the tracking measure" as clean signaling-theory evidence of industry tolerating transparency but
blocking teeth) is directly contradicted by HB79's passage. It correctly declined to pick a
replacement. With tonight's HB804 and HB5/6-rationale findings added, here are two concrete,
evidence-grounded alternatives — genuinely different theoretical claims, not just wording
tweaks. **This is Britton's call, not locked in here, no manuscript language touched.**

### Option A — Logrolling / compensatory concession (a political-exchange framing)

**Claim:** The legislature was not broadly hostile to industry on liability this session. It
delivered a much larger, sector-wide liability shield (HB804, wide margins, all energy
production) while conceding a narrower, technology-specific liability rollback (HB79, narrower
margins, CCS only) — plausibly as a release valve for the specific public backlash CCS was
drawing (the EIP report, the Coushatta consultation disputes, Gov. Landry's own Oct. 2025
Class VI application moratorium). The two bills aren't contradictory data points about "does the
legislature favor industry" — they're a bundle: broad protection generally, a targeted give-back
on the one issue generating the most visible public conflict.
- **Theoretical grounding:** classic legislative logrolling/bundled-bargain theory (Buchanan &
  Tullock, *The Calculus of Consent*, 1962 — canonical, not independently re-verified via
  fetch tonight but not a fringe or obscure citation) combined with symbolic-politics/
  compensatory-legitimation framing (a targeted concession that manages public conflict without
  changing the industry's overall regulatory position) — the same conceptual family Britton's
  other papers already draw on for legitimacy-management arguments.
- **What it would require to write up:** framing HB79 explicitly against HB804 as a paired
  finding, not treating HB79 in isolation — a genuinely new move relative to every prior note on
  this thread, which only ever looked at CCS-specific bills.

### Option B — Regulatory-authority/venue-protection framing (a policy-image framing)

**Claim:** The real dividing line this session wasn't "property rights vs. transparency" or
"industry wins vs. loses" — it was whether a bill touched the **state's own regulatory
authority**. Bills that would have devolved CCS permitting power to parishes or removed the
state's Class VI-adjacent eminent-domain framework (HB5/6/7) died specifically because officials
argued they'd jeopardize Louisiana's EPA primacy and invite federal reassertion — a threat to the
state's institutional turf, not to industry per se. HB79, by contrast, adjusted a liability
*standard* — costly to industry, yes, but it left DCE's permitting authority and the primacy
framework completely untouched. HB820 (the tracking/manifest bill, already read by prior notes as
"transparency survives") fits the same pattern: procedural obligations layered *within* the
state's existing regulatory architecture, not a challenge to who holds authority.
- **Theoretical grounding:** Baumgartner & Jones's policy-image/policy-monopoly and punctuated-
  equilibrium framework (*Agendas and Instability in American Politics*, 1993/2009) — the
  question isn't which side an interest group is on, it's whether a proposal threatens the
  institution that currently controls the issue's "venue." Same canonical-citation caveat as
  Option A: well-established, not independently re-verified via fetch tonight.
- **What it would require to write up:** re-coding the bill set on a state-authority-threat axis
  rather than a pro-/anti-industry axis — a bigger analytical lift than Option A, but it directly
  uses the new HB5/6 committee-rationale finding (section 4 above) as its evidentiary anchor
  rather than inferring intent from outcomes alone.

**Which is stronger evidence-wise:** Option B has a more direct evidentiary anchor (an actual
quoted institutional rationale for the bill deaths, not an inference). Option A requires more
interpretive work (reading HB79+HB804 together as a deliberate bundle, which no source states
explicitly — it's a pattern Britton would be naming, not one any source names for him). Neither
is fabricated or overclaimed here; both are offered as candidate lenses, and they aren't mutually
exclusive — a manuscript could use Option B as the mechanism (why specific bills lived/died) and
Option A as the higher-level political-economy reading of the session as a whole.

## 6. Literature/corpus-supplement notes (WebSearch only, nothing fabricated)

- Searched specifically for academic (not just legal-practice) literature on "selective
  liability capture" or "issue-specific regulatory capture" patterns — **did not find a clean
  academic hit**; results were dominated by general regulatory-capture explainers (Stigler) and
  CCS-specific legal/liability-policy literature (law firm alerts, a Global CCS Institute
  liability-framework paper, an MIT sequestration-liability paper) rather than a theory paper
  matching this specific pattern. Flagging as a genuine dead end rather than stretching a weak
  hit to fit — Options A and B above lean on general, well-established theory (logrolling,
  punctuated equilibrium) rather than a CCS-specific precedent, because no CCS-specific one
  surfaced.
- The Oct. 15, 2025 Landry executive order pausing new Class VI applications (45-day DCE review,
  ~33 pending applications not blocked) predates the 2026 legislative session by several months
  and is most likely already represented in `Corpus_1/Department-Directive-Order-No-B-2025-01-
  combined.pdf` (filename/date strongly suggest this is that order, though the text wasn't
  independently re-read tonight to confirm — worth a quick check next pass rather than assuming).
  Not treating this as a "new" 2026 finding; noted here only because it's relevant background for
  Option A (Landry was already managing CCS-specific public backlash before the session started).
- Confirmed `Corpus_1/HB_79_Damages_Threshold.pdf` already exists in the corpus. Its exact
  version (introduced vs. enrolled/Act text) wasn't checked — no PDF text-extraction tool
  (`pdftotext`, `pypdf`) is available in this environment, so this couldn't be verified tonight.
  Worth flagging for whoever next works `Analysis/` scripts: if the pipeline needs the *enrolled*
  Act 614 text rather than the introduced bill, that's a fetch/replacement task, not a given.

## Bottom line / what's still open for Britton

1. **Reframing choice (Option A vs. B vs. some combination) is Britton's call.** Both are
   evidence-grounded, neither fabricated, neither locked into any manuscript file.
2. **HB79 = Act 614 is WebSearch-confidence, not primary-source-confirmed** — `legis.la.gov/
   Legis/BillInfo.aspx?i=249698` is still the right target the moment WebFetch works again.
3. **HB804 is a genuinely new input to this thread** — worth Britton's own read of the American
   Press / Louisiana Illuminator coverage before any framing decision, since it changes what
   "the industry's liability position this session" even means.
4. **No academic citation found for the "selective/issue-specific capture" pattern itself** —
   Options A/B lean on general canonical theory (logrolling, punctuated equilibrium), not a
   CCS-specific precedent. If Britton wants one, that's a job for his own database access, not
   another WebSearch pass — this one came up empty on a real attempt.
5. **WebFetch: 9th straight session down**, same failure signature every time.
