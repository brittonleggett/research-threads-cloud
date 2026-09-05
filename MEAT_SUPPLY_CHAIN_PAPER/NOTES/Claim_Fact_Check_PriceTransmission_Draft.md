# Claim Fact-Check — Price Transmission Fork (draft for claims #1, #2, #4, #5, #12, #13)

Draft verdicts only — to be merged into the master `NOTES/Claim_Fact_Check.md`
by the project orchestrator alongside the other forks' claims. Verdicts:
Supported / Partially supported / Unsupported / Misleading without context /
Unresolved. See `LITERATURE/Price_Transmission_Literature.md` and
`SOURCE_VERIFICATION/Evidence_Table_PriceTransmission.md` for full sourcing.

---

### Claim #1 — Are U.S. cattle producers receiving historically weak returns
while consumers face historically high beef prices?

**Verdict: Unresolved (leaning Partially supported / Misleading without
context, pending better historical data).**

The most recent year-over-year data available (2023→2024) shows the *opposite*
of "historically weak" in relative-share terms: beef farm share of the retail
dollar rose from 49.8 to 52.2 cents, a real increase, not a decline. That
contradicts a simple "producers are being squeezed more than ever" framing
for that specific year. However, this fork could not pull the full ERS Meat
Price Spreads historical time series (1970–present) needed to properly judge
"historically weak" against multi-decade context, only a single two-year
comparison from a secondary summary. It's entirely possible farm-gate cattle
prices *in absolute/inflation-adjusted terms* are historically weak even
while the *share* of the retail dollar rose (share and absolute return are
different questions, and this project should not conflate them). **Do not
use this claim in the manuscript until someone pulls the actual ERS
historical series and, separately, inflation-adjusted cattle price data
(e.g., from USDA AMS or the St. Louis Fed/FRED).**

### Claim #2 — How much of the retail beef dollar goes to farmers/ranchers
versus processors/retailers, and how has that changed?

**Verdict: Partially supported, with a strong "misleading without context"
flag on how this figure is typically used in public discourse.**

Two genuinely different ERS statistics get conflated in public discourse:
(a) the overall "farm/ranch share of the food dollar" (all foods combined) —
5.9 cents (2023) → 5.8 cents (2024), roughly flat, low because it includes
heavily processed/packaged/restaurant food; and (b) the beef-specific
"Meat Price Spreads" farm share — 49.8 cents (2023) → 52.2 cents (2024),
much higher because beef requires comparatively little processing between
farm and retail cut. Advocacy material citing "farmers get less than 6 cents
of every dollar" is accurate for (a) but actively misleading if implicitly
applied to beef specifically, where the real figure is roughly ten times
higher and moving in the opposite direction in the most recent year. Pork
farm share (22.1 → 23.7 cents, 2023→2024) sits between these two extremes.
**This is likely one of the most important individual findings for
`PROJECT_STATUS.md` — a common public claim does not hold up as stated for
beef and pork specifically, though it is accurate for food overall.**

### Claim #4 — Are processor profit margins unusually high during periods of
elevated food inflation?

**Verdict: Partially supported, but evidence is strongest for the specific
2020 COVID-19 acute-disruption episode, not for "elevated food inflation"
generally (e.g., the broader 2021–2023 inflation period was not separately
examined in this pass).**

Two independent lines of evidence for the COVID-19 2020 shock specifically:
Balagtas & Cooper (2021, Choices) conclude packers used market power to
widen margins as cattle/hog prices fell while wholesale/retail prices rose;
Erol & Saghaian (2022, Sustainability) find the pandemic period produced
asymmetric adjustment with farmers receiving less and consumers paying more
than model-predicted values, consistent with a widened, retail/processor-
concentrated spread. This is reasonably strong triangulated evidence *for
that specific shock*. It should not be generalized to "food inflation
periods" broadly without separately checking margin data for, e.g., the
2021–2023 general inflation episode — **flagged as an open follow-up**,
not yet done in this pass.

**2026-09-05 update: Erol & Saghaian (2022) now read in full (not just
abstract), and Tyson/JBS SEC segment data pulled directly — both confirm
and refine, but also add an important nuance, this claim.** The Erol &
Saghaian working paper (an open-access AAEA 2022 conference poster by the
same authors, same title, hosted on AgEconSearch — MDPI itself stayed
bot-blocked) states its finding precisely: **"The COVID-19 pandemic caused
retailers and wholesalers to have higher prices, while farmers received
lower prices than their predicted values,"** and **"Price spreads are
widened due to the COVID-19 shock in favor of wholesalers and retailers."**
Note the mechanism identified is wholesale/retail-level, not narrowly
"meat packers/processors" — the paper's background section separately
asserts "Meat packers and processors have market power" as motivating
context, but the VEC/historical-decomposition result itself is about price
levels at the farm/wholesale/retail stages, not a direct measurement of
packer margins. The direct packer-margin evidence for Claim #4/#12 now
comes from Tyson's and JBS's own SEC filings instead (see Claim #12 and
`NOTES/Claim_Fact_Check_Concentration_Draft.md` Claim #14) — both sources
point the same direction but are not the same measurement, and should be
cited for what each actually shows. See
`SOURCE_VERIFICATION/Evidence_Table_PriceTransmission.md` for the full
extracted findings (speed-of-adjustment coefficients, structural breaks,
etc.).

### Claim #5 — Do increases in cattle prices transmit differently to
consumers than decreases (asymmetric price transmission)?

**Verdict: Unresolved / genuinely contested in the peer-reviewed literature
— do not state as settled either way.**

Older studies and studies using BLS-derived retail price series generally
find asymmetry (rockets-and-feathers pattern). The most methodologically
current study identified in this pass — Pozo, Bachmeier & Schroeder (2021,
*Journal of Commodity Markets*) — using retail scanner (actual transaction)
data specifically, finds **no evidence** of vertical asymmetric price
transmission in the beef chain, and attributes earlier asymmetry findings
partly to the retail-price data source used (BLS averages vs. scanner
data). The honest answer is that the literature is split and the split
correlates with data source/methodology, not that one side is simply wrong.
Caveat: this fork could not get past a paywall to read the Pozo et al. full
text directly (403 on ScienceDirect); findings here rely on a search-engine-
summarized abstract, confirmed only at the citation-exists level via
RePEc/EconPapers. Recommend a library-proxy full-text pull before any
manuscript claim leaning on this paper specifically. (Not attempted again
2026-09-05 — outside that session's three targeted items; still open.)

**2026-09-05 note relevant to this claim**: GAO-02-246 ("Economic Models of
Cattle Prices," March 2002 — now read in full, see Claim #7 discussion in
the concentration fork / master fact-check) independently corroborates that
this contestedness is long-standing and not merely a function of newer vs.
older data: as of 2002, GAO's own 40-expert panel disagreed on how much
weight structural change and imports deserve relative to domestic
supply/demand fundamentals, and GIPSA's internal 1996 literature review of
concentration's price effects was itself "inconclusive." This is background
corroboration for the *general contestedness* of vertical/structural price
effects in cattle markets, not a direct test of asymmetric transmission
specifically — file alongside, not instead of, the Pozo/older-literature
split above.

### Claim #12 — Is there evidence processors or retailers benefit
disproportionately from supply disruptions?

**Verdict: Supported, for the 2020 COVID-19 disruption specifically (beef).**

Same evidence as Claim #4 above (Balagtas & Cooper 2021; Erol & Saghaian
2022), plus Cooper et al. (2023, *Food Policy*) showing larger beef/pork
plants had disproportionately greater capacity underutilization during the
April–May 2020 peak — the supply-side mechanism that plausibly drove the
margin widening. Three independent sources triangulate on the same period
and direction (packer/retail margin widened while farm price fell during
acute 2020 disruption). This is the single best-supported claim in this
fork's scope. **Scope limit: this is evidence about one acute historical
shock (COVID plant closures), not a general claim that disruptions always
benefit intermediaries — do not overgeneralize in the manuscript.**

**2026-09-05: now also confirmed directly at the individual-company level.**
Tyson Foods' own FY2020 and FY2021 10-Ks (SEC EDGAR, read directly) state
that Beef segment operating income increased because COVID-19 disruptions
"increased the spread between preexisting contractual agreements and the
cost of fed cattle" (nearly identical language for Pork). Tyson's Beef
operating margin: 6.6% (FY19) → 10.0% (FY20) → 18.0% (FY21), reverting to
12.6% (FY22) and a loss (-0.5%, FY23) — confirming both the disruption-era
widening and its temporariness. JBS USA's Beef North America segment shows
the same pattern independently (Adjusted EBITDA margin ~13.1%→~21.3%,
2020→2021, SEC Form F-4). Poultry did not show the same pattern at either
company (Tyson Chicken margin fell during 2020-2021; see the master
fact-check Claim #14 for the full breakdown) — this strengthens the
"beef/pork specifically, not a blanket meat-industry pattern" framing of
this claim's scope limit. Full detail:
`NOTES/Claim_Fact_Check_Concentration_Draft.md` Claim #14 and
`SOURCE_VERIFICATION/Evidence_Table_Concentration.md`.

### Claim #13 — Are similar dynamics (producer/consumer price divergence)
present in pork?

**Verdict: Partially supported — directionally similar structure, weaker
COVID-specific evidence base found in this pass than for beef.**

Pork farm share of the retail dollar also rose 2023→2024 (22.1 → 23.7
cents), paralleling beef's increase — so the "historically squeezed"
framing is equally complicated for pork as for beef in the most recent
year. On price-transmission asymmetry specifically, more of the *pork*
literature identified in this pass (Goodwin & Harper 2000; Miller & Hayenga
2001; Gervais 2011; Assefa et al. 2017) finds asymmetric transmission than
the most recent beef scanner-data study does — though an early pork study
(Boyd & Brorsen 1988) found symmetric adjustment, so even within pork the
literature isn't unanimous. This fork did **not** find a pork-specific
equivalent to the beef COVID-margin papers (Balagtas & Cooper covers "meat
and livestock markets" generally and likely includes pork/hog data, but
this pass did not extract pork-specific figures from it) — **flagged as a
follow-up**: read the Balagtas & Cooper (2021) full text for hog-specific
figures before treating pork's COVID-disruption margin story as separately
confirmed.
