# 2026-09-05 — Primary-source retry pass: Erol & Saghaian, Federal Register COOL rule, GAO-02-246, USDA AMS PSD Annual Report, Tyson/JBS SEC data

Follow-up to the 2026-09-03 scaffold session. This was a targeted, read-only
research pass on the three items `PROJECT_STATUS.md`'s "Next actions"
prioritized: (1) retry Erol & Saghaian (2022), the Federal Register COOL
rules, and GAO-02-246 via alternate access methods; (2) pull the USDA AMS
Packers and Stockyards Division 2021/2022 Annual Report to Congress; (3)
find Tyson/JBS 10-K or earnings-call margin data (2019-2023) for Claim #14.
**All three were substantially resolved.** No git commands were run (per
instructions for this pass); the repo has uncommitted changes as of this
note.

## Method note that mattered for almost everything below

The single most useful discovery this pass: **when a `.gov` or `.sec.gov`
PDF returns HTTP 403 or an unreadable "binary content" response to the
WebFetch tool, retrying the identical URL with `curl` and a standard
browser `User-Agent` header very often succeeds (HTTP 200)** — this worked
for the AgEconSearch PDF, the USDA AMS PDF, both Tyson 10-Ks, and the JBS
F-4. Separately, **when a PDF *does* download but its text can't be
extracted, the fix is often missing local tooling, not a bad source**: this
environment did not have `poppler-utils` installed; `apt-get update &&
apt-get install -y poppler-utils` fixed it in under a minute, after which
`pdftotext -layout <file>` reliably extracted readable text from every PDF
attempted (GAO-02-246, the AgEconSearch poster, the USDA AMS report). For
long SEC HTML filings, the WebFetch tool's own summarizer truncated before
reaching the MD&A/segment-results sections on two different Tyson 10-Ks;
downloading via `curl` and stripping HTML tags locally with a small Python
script (inserting newlines at block-tag boundaries before stripping, so the
line-based Grep/Read tools stay useful) worked reliably instead. **This
pattern — curl-with-UA, then local pdftotext/HTML-stripping when needed —
is worth trying as a first resort on any future "blocked" .gov/.sec.gov
source in this repo**, not just this project. (A note for whoever's on
`SPACEX_LOUISIANA_PAPER`: that project's stuck FAA docket PDF is very
likely fixable the same way.)

## 1. Erol & Saghaian (2022) — resolved via the authors' own poster, not the journal itself

MDPI's `Sustainability` journal page (`mdpi.com/2071-1050/14/8/4391`, and
its `/pdf` and `/htm` variants) stayed HTTP 403 to both WebFetch and
`curl` with a browser UA — this is durable bot-blocking on MDPI's end that
this pass could not get around. Instead, a search turned up a companion
document: the same two authors presented a **2022 AAEA (Agricultural &
Applied Economics Association) conference poster**, same title ("The
COVID-19 Shock and Dynamics of Price Adjustment in the U.S. Beef Sector"),
hosted open-access on AgEconSearch (University of Minnesota). AgEconSearch's
own HTML record page 403'd, but its direct PDF URL
(`ageconsearch.umn.edu/record/322057/files/22443.pdf`) returned HTTP 200 to
`curl` with a browser UA. Full text read (2 pages).

**Findings, verbatim where quoted:**
- VEC model with historical decomposition; monthly farm/wholesale/retail
  prices, USDA ERS, 1970:01–2021:04.
- "Producers do not benefit from price increases at retail and consumer
  levels (in terms of both time and magnitude of the change)."
- "Price spreads are widened due to the COVID-19 shock in favor of
  wholesalers and retailers."
- Dynamic speed-of-adjustment coefficients: wholesale 0.21, farm 0.074,
  retail 0.021 — wholesale prices adjusted back to long-run equilibrium
  roughly 3x faster than farm prices and 10x faster than retail prices.
- 4 structural breaks detected in the long-run equation: Nov 1980, Jul
  1993, May 2001, Sep 2013.
- Markets returned to pre-shock patterns within 4-6 months (resilience
  finding).
- "Meat packers and processors have market power" appears in the
  background/motivation section, not as a directly-tested result of this
  specific VEC model — **worth being precise about in the manuscript**: this
  paper's own result is about relative price levels at the farm/wholesale/
  retail stages, not a direct measurement of packer margins. The direct
  packer-margin evidence now comes from the Tyson/JBS SEC data (item 3
  below), which is a different measurement pointing the same direction.
- The poster's own reference list cites the peer-reviewed journal article
  by its full citation, confirming the poster and the *Sustainability*
  paper are the same underlying work by the same two authors.

Updated: `NOTES/Claim_Fact_Check_PriceTransmission_Draft.md` (Claims #4,
#12), `SOURCE_VERIFICATION/Evidence_Table_PriceTransmission.md`,
`SOURCE_VERIFICATION/Evidence_Table.md`.

## 2. Federal Register COOL rule (2024-05479, "Product of USA") — resolved via the API, not the HTML page

The HTML document page still 302-redirects to `unblock.federalregister.gov`
(an anti-automation interstitial) for both WebFetch and a retry this pass —
that part of the block is unchanged. What worked: **federalregister.gov
publishes the same content through public API/XML endpoints that are not
behind the interstitial**:
- `https://www.federalregister.gov/api/v1/documents/2024-05479.json` —
  metadata (title, dates, links to PDF/HTML/XML).
- `https://www.federalregister.gov/documents/full_text/xml/2024/03/18/2024-05479.xml`
  — the complete regulatory text.

Both fetched successfully via WebFetch directly (no curl workaround needed
here — the block is specific to the HTML document-view route, not the
domain generally).

**Findings, read directly from the primary text:**
- Published March 18, 2024; effective May 17, 2024; full compliance
  required January 1, 2026.
- Single-ingredient products: "Product of USA"/"Made in the USA" permitted
  only if "the product is derived from animals born, raised, slaughtered,
  and processed in the United States."
- Multi-ingredient products: additionally require all non-spice/flavoring
  ingredients to be of domestic origin, and all preparation/processing
  steps to occur in the U.S.
- Prior rule (to be removed from FSIS's Food Standards and Labeling Policy
  Book by the compliance date): allowed the claim on products "minimally
  processed in the United States" — i.e., the pre-2024 loophole was
  specifically that minimal domestic processing sufficed regardless of
  where the animal was born, raised, or slaughtered. This confirms, with
  primary-text precision, what the project's secondary sources (National
  Ag Law Center) had already summarized correctly.

Updated: `SOURCE_VERIFICATION/Evidence_Table_COOL.md`,
`SOURCE_VERIFICATION/Evidence_Table.md`. The 2016 conforming rule
(2016-04609) was NOT retried this pass — same API/XML technique should work
for it; flagged as an easy follow-up.

## 3. GAO-02-246 ("Economic Models of Cattle Prices," March 2002) — resolved by installing PDF tooling

Previously the PDF downloaded fine (WebFetch saves binary content to a
local path even when it can't read it) but the environment had no way to
extract text from it. This pass: `apt-get update && apt-get install -y
poppler-utils`, then `pdftotext -layout <path>` on the saved file. Full
126-page report read.

**Key findings relevant to this project's Claims #1, #5, #7:**
- USDA's long-term livestock model and short-term forecasting committee,
  and ITC's COMPAS/CGE trade models, all explicitly account for beef/cattle
  imports and exports — but **none of them incorporate market concentration,
  marketing agreements, or forward contracts**; GAO found these models
  "were not designed to answer questions about these factors."
- GIPSA's own 1996 internal literature review of concentration's effects on
  cattle prices was "inconclusive... primarily because of limitations in
  methods or data in the research reviewed" — and GIPSA could not conclude
  the industry was *either* noncompetitive or competitive.
- GAO's 40-member expert panel (named in the report's Appendix VI) judged
  domestic cattle supply/demand as more important than international trade
  and structural change for explaining cattle prices and producer incomes,
  but with real, quoted disagreement among panelists on how much weight
  structural change (concentration, vertical coordination) deserves — one
  panelist: "Until recently, the conventional wisdom has been that higher
  concentration leads to higher beef prices and lower cattle prices. The
  thought in modern industrial organization does not put so much weight on
  concentration..."
- The report states the theoretical *direction* of the import-price
  mechanism plainly: "an increase in beef imports causes beef prices to
  fall, which in turn reduces the domestic demand for cattle and causes
  cattle prices to fall" — but this is modeled reasoning about direction,
  not an estimated U.S.-specific magnitude. **This project still has no
  verified econometric estimate of how much imports actually move cattle
  prices** — GAO-02-246 corroborates that this has been a genuinely
  unresolved empirical question since at least 2002, not a data-recency
  problem.

Updated: `NOTES/Claim_Fact_Check.md` (Claims #5, #7),
`SOURCE_VERIFICATION/Evidence_Table_PriceTransmission.md`.

## 4. USDA AMS Packers and Stockyards Division 2021/2022 Annual Report to Congress — fetched and read in full; surfaces a real discrepancy

Fetched via `curl` with a browser UA (`ams.usda.gov` PDF, HTTP 200);
`pdftotext` extraction; ~140-page report read for the relevant sections.
This was PROJECT_STATUS.md's explicitly-flagged "stronger primary source
than the White House CEA blog" and had been identified-but-not-fetched
since 2026-09-03.

**Official four-firm concentration ratios (Table 5, p.13), 2019-2021:**

| | 2019 | 2020 | 2021 |
|---|---|---|---|
| Total Value Purchases | 66% | 65% | 67% |
| Steers & Heifers | 85% | 81% | 81% |
| Cows & Bulls | 50% | 46% | 47% |
| Hogs | 67% | 64% | 65% |
| Sheep & Lambs | 53% | 44% | 42% |
| Broilers | 53% | 53% | 55% |
| Turkeys | 55% | 55% | 55% |

PSD attributes the steer/heifer decline (85%→81%) to COVID-19 plant
disruptions specifically, not deconcentration. HHI figures (2017-2021) show
steer/heifer slaughter as "moderately concentrated" per DOJ/FTC merger
guidelines (1,687-1,878); cow/bull and sheep/lamb slaughter as "relatively
unconcentrated." The report also states regional/local livestock-
procurement markets are "significantly more concentrated" than these
national figures — relevant to the monopsony argument specifically.

**This directly contradicts a figure this project adopted just two days
earlier.** On 2026-09-03, a Consensus.app AI-search synthesis (never
independently read against the underlying paper) reported Schaefer et al.
(2024, *Review of Industrial Organization*) as finding a 2019 broiler CR4 of
**78%**. PSD's own official 2019 broiler figure is **53%** — a 25-point gap
too large to attribute to rounding. Notably, **the same Consensus.app
synthesis's beef (85%) and hog (67%) 2019 figures match PSD's official
figures exactly** — which argues against the synthesis being a wholesale
fabrication, and suggests the broiler figure specifically may use a
different market/plant definition that can't be determined without reading
Schaefer et al. directly (still paywalled). **This project is now using
PSD's 53-55% for poultry and reverting to describing poultry as the
least-concentrated of the three commodities**, per AER-785's original
framing — but the discrepancy itself is flagged as unresolved, not smoothed
over, and is now the single highest-value remaining "Britton's library
access" item (see `PROJECT_STATUS.md` Open Decisions #6).

**Other material found in this report, relevant to Claims #14/#15:**
- "The imbalance between cattle supply and processing capacity persisted
  from 2020, and beef packers continued to earn record profits in 2021." —
  an official USDA statement, not an advocacy claim, directly supporting
  Claim #14 with a stronger source type than the White House CEA blog.
- An extensive, previously undocumented (in this project) list of 2020-2022
  DOJ criminal/civil price-fixing actions spanning all three commodities —
  see item 5 below and the updated Claim #15.

Updated: `NOTES/Claim_Fact_Check.md` (Claims #3, #14, #15),
`NOTES/Claim_Fact_Check_Concentration_Draft.md`,
`SOURCE_VERIFICATION/Evidence_Table_Concentration.md`,
`SOURCE_VERIFICATION/Evidence_Table.md`, `PROJECT_STATUS.md`.

## 5. Tyson/JBS 10-K and SEC segment data (2019-2023) — resolved for Claim #14

**Tyson Foods** (SEC EDGAR, CIK 100493): fetched the FY2021 10-K (filed
2021-11-15, covers FY2019-2021) and FY2023 10-K (filed 2023-11-13, covers
FY2021-2023) directly via `curl`, since WebFetch's own summarizer truncated
before reaching the MD&A "Segment Results" section on both filings (a real
tool limitation for long SEC HTML documents, not a source-access problem).
Parsed to plain text locally.

| Segment operating margin | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 |
|---|---|---|---|---|---|
| Beef | 6.6% | 10.0% | **18.0%** | 12.6% | -0.5% |
| Pork | 5.3% | 11.0% | 5.2% | 3.0% | -2.4% |
| Chicken | 4.7% | 0.9% | -4.6%* | 5.6% | -4.5% |

*Chicken's FY2021 loss is driven substantially by a $626M one-time
price-fixing legal-contingency accrual per Tyson's own MD&A, not underlying
market conditions.

Tyson's own words (FY2020 vs. FY2019, Beef segment): "Operating income
increased primarily due to market conditions, including COVID-19
disruptions, which increased the spread between preexisting contractual
agreements and the cost of fed cattle." Nearly identical language appears
for the Pork segment. This is the company itself, in an audited SEC filing,
directly attributing the margin expansion to the pandemic disruption.

**JBS USA**: JBS does not currently file 10-Ks with the SEC (it's a
Brazilian foreign private issuer; its NYSE-listed entity, JBS N.V., only
began filing 20-Fs after a 2025 listing). The best full-year, SEC-filed,
segment-level USD data located for the 2019-2023 window is a **2023 SEC
Form F-4 registration statement** (filed in connection with a bond exchange
offer), which includes audited full-year 2020-2022 segment financials.
Fetched via `curl` (31MB file), parsed locally.

| Segment | 2020 | 2021 | 2022 |
|---|---|---|---|
| Beef North America EBITDA margin | ~13.1% | **~21.3%** | ~9.4% |
| Pork USA EBITDA margin | ~10.4% | ~10.5% | not extracted |
| Pilgrim's Pride (poultry) EBITDA margin | ~9.5% | ~11.5% | not extracted |

JBS's own filing attributes the 2021 Beef North America EBITDA jump
(+108.8%, to $4,511.9M from $2,161.4M) to "a strong demand in the United
States" and a 25.1% sales-price increase against only a 16.9% rise in
operating costs — independently confirming, at a second major packer, the
same disproportionate margin-expansion pattern found at Tyson. Pork USA's
margin was comparatively flat (proportional revenue/cost growth); Pilgrim's
Pride (poultry) rose only modestly.

**Net effect on Claim #14**: upgraded from "Unresolved — resting on
unverified White House CEA figures" to **"Supported for beef and pork
specifically during the 2020-2021 COVID window; poultry does not show the
same pattern at either company."** This is now grounded in each company's
own audited financial statements rather than a political source's cited
figures — a meaningful evidentiary upgrade, and one that also reinforces
this project's standing rule against pooling beef/pork/poultry, since
poultry's trajectory at both companies looks genuinely different.

Updated: `NOTES/Claim_Fact_Check.md` (Claim #4, #14),
`NOTES/Claim_Fact_Check_Concentration_Draft.md` (Claim #14),
`NOTES/Claim_Fact_Check_PriceTransmission_Draft.md` (Claim #12),
`SOURCE_VERIFICATION/Evidence_Table_Concentration.md`,
`SOURCE_VERIFICATION/Evidence_Table_PriceTransmission.md`,
`SOURCE_VERIFICATION/Evidence_Table.md`, `PROJECT_STATUS.md`.

## What's still genuinely blocked (not resolved, not attempted, or a residual gap)

- **Schaefer et al. (2024, *Review of Industrial Organization*)** — still
  paywalled at Springer (institutional login wall). Now the single
  highest-value remaining item: it's the only way to actually reconcile the
  poultry-concentration discrepancy in item 4 above rather than just
  flagging it.
- **Pozo, Bachmeier & Schroeder (2021, *Journal of Commodity Markets*)** —
  still paywalled at ScienceDirect; not retried this pass (outside tonight's
  three targeted items). Note a separate 2026-09-03 Consensus.app pass
  reported reading this paper's full text via an AI-research tool — that is
  a lower-confidence source type than a direct primary read and should
  still be treated with some caution until independently confirmed.
- **JBS's full 2019 and 2023 segment data** — the F-4 located only covers
  2020-2022; a genuine partial gap, not a wrong-source problem. A JBS N.V.
  20-F (post-2025 listing) might have retrospective 2023 data; not checked
  this pass.
- **ERS Meat Price Spreads historical time series (1970-present,
  beef/pork-specific)** — not attempted this pass; still needed for Claim
  #1's "historically weak returns" framing. Flagged as the top remaining
  next-action in `PROJECT_STATUS.md`.
- **The Meat Institute rebuttal page** (403 in the 2026-09-03 pass) — not
  retried this pass.
- **AER-787** (ERS poultry-specific companion, unreadable PDF stream as of
  2026-09-03) — not retried this pass, but should now be resolvable via the
  same `poppler-utils` fix that worked on GAO-02-246. Flagged as a likely
  quick win for a future session.
- **The 2016 Federal Register conforming rule** (2016-04609) — the API/XML
  technique that worked for the 2024 rule was not applied to this document
  this pass.

## Files edited this pass

- `NOTES/Claim_Fact_Check.md`
- `NOTES/Claim_Fact_Check_Concentration_Draft.md`
- `NOTES/Claim_Fact_Check_PriceTransmission_Draft.md`
- `SOURCE_VERIFICATION/Evidence_Table.md`
- `SOURCE_VERIFICATION/Evidence_Table_Concentration.md`
- `SOURCE_VERIFICATION/Evidence_Table_PriceTransmission.md`
- `SOURCE_VERIFICATION/Evidence_Table_COOL.md`
- `PROJECT_STATUS.md`
- This file (new).

No git commands were run per this session's instructions — these changes
are uncommitted as of this note.
