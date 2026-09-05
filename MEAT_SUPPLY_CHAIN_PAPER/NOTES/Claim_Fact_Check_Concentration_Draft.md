# Claim Fact-Check — Concentration-Related Claims (Draft, Sections 5 & 13)

Status: draft verdicts from the concentration/structure research pass,
2026-09-03. Covers claims #3, #14, #15 from the brief's Section 13 list.
Merge into the master `NOTES/Claim_Fact_Check.md` when it's assembled;
verdicts here are this fork's best read of the evidence gathered — treat as
a draft input, not final, since a fuller pass (especially getting current
USDA AMS/peer-reviewed HHI figures, and verifying processor 10-K margin
data) could change the nuance.

---

### Claim #3: "Has meatpacking concentration increased, decreased, or
remained stable?"

**Verdict: Supported (increased, long-run 1963-2019) — with commodity-
specific magnitude. 2019-2021 specifically shows flat-to-declining
concentration in the one directly-read official source, not a continued rise.**

**2026-09-05 update — USDA AMS Packers and Stockyards Division (PSD) 2021/2022
Annual Report to Congress obtained and read in full** (direct PDF fetch via
`curl` with a browser user-agent, local `poppler-utils` text extraction —
resolves the "identify but don't fetch" status this source had as of
2026-09-03). This is PSD's own official annual four-firm concentration ratio
table, 2012-2021, methodology stated in the report itself:

| Year | Total Value | Steers & Heifers | Cows & Bulls | Hogs | Sheep & Lambs | Broilers | Turkeys |
|---|---|---|---|---|---|---|---|
| 2019 | 66% | 85% | 50% | 67% | 53% | 53% | 55% |
| 2020 | 65% | 81% | 46% | 64% | 44% | 53% | 55% |
| 2021 | 67% | 81% | 47% | 65% | 42% | 55% | 55% |

PSD attributes the steer/heifer decline (85%→81%) explicitly to "disruptions
in operations at the major packing plants during the COVID-19 pandemic" —
i.e., a temporary capacity-shock effect, not evidence of durable
deconcentration. HHI figures (2017-2021) show steer/heifer slaughter as
"moderately concentrated" per DOJ/FTC merger guidelines (HHI 1,687-1,878),
while cow/bull and sheep/lamb slaughter are "relatively unconcentrated."

**This directly contradicts, and should supersede, this project's own
prior "poultry CR4 = 78% (2019)" figure** (adopted 2026-09-03 via a
Consensus.app AI-search synthesis of "Schaefer et al.," never independently
read). PSD's own official broiler figure for 2019 is 53%, not 78% — a large
enough gap that it cannot be attributed to rounding or a minor methodology
difference. Do not treat this as resolved in favor of either number: PSD is
a directly-read primary regulatory source with stated methodology; Schaefer
et al. is still genuinely unread (paywalled) and may define "concentration"
differently (e.g., plant-level vs. firm-level, a different product-market
definition, or CR4 vs. CR8). **Recommendation: use PSD's 53-55% for poultry
in any manuscript draft until Schaefer et al. is read directly and the
discrepancy is either reconciled or explained; do not average or split the
difference.** This also means poultry should likely revert to being
characterized as the least-concentrated of the three commodities, consistent
with AER-785's original framing, rather than "no longer clearly the least
concentrated" as this project stated as of 2026-09-03.

**Original (2026-09-03) analysis below, retained for the historical
1963-1997 trend, which is unaffected by the above:**

Two independent primary sources, using consistent market definitions,
bracket a 40-year trend:
- USDA/ERS AER-785 (2000), using both Census (shipment-value) and USDA/GIPSA
  (animal-input) concentration ratios, documents concentration rising in all
  four slaughter classes (cattle, hogs, chickens, turkeys) between 1963/1980
  and 1992/1997, with cattle showing by far the steepest rise (steer/heifer
  CR4: 36% in 1980 → 80% in 1997) — a change ERS itself calls unique among
  roughly 1,000 Census product classes tracked back to 1947.
- White House CEA (Sept. 2021) reports the trend continuing through 2021:
  beef CR4 ~82%, pork ~66%, poultry ~54%, each up from a 1970s-80s baseline
  in the 25-35% range.

No evidence found of a reversal or plateau-then-decline in any of the three
commodities. Confidence is high for the *direction* of the trend and for the
1963-1997 figures (directly read from the primary ERS report); confidence is
moderate for the precise current (~2021-2024) *level*, since the most
recent point comes from a White House policy blog rather than a USDA
statistical release or peer-reviewed paper — the peer-reviewed 2024 update
(Schaefer et al.) exists but was not accessible this pass (paywalled /
403 error). Recommend citing the ERS historical series as the anchor and
treating the 2021 CEA figures as "consistent with, and one recent estimate
of the continuation of" that trend, pending verification against the
peer-reviewed source or a USDA AMS Packers and Stockyards annual report.

---

### Claim #14: "Is there evidence processors or retailers benefit
disproportionately from supply disruptions?"

**Verdict: Supported for beef and pork during the 2020-2021 COVID window
specifically (resolved 2026-09-05 via direct SEC-filed audited data) —
commodity-specific, does not extend cleanly to poultry.**

**2026-09-05 update.** The dedicated follow-up recommended below was
completed. Both companies' own SEC filings, read directly:

**Tyson Foods** (10-K, FY2021 filing for FY2019-2021; 10-K, FY2023 filing
for FY2021-2023 — both fetched directly from SEC EDGAR via `curl`, since
WebFetch's summarizer truncated the MD&A section):

| Segment | FY2019 | FY2020 | FY2021 | FY2022 | FY2023 |
|---|---|---|---|---|---|
| Beef operating margin | 6.6% | 10.0% | **18.0%** | 12.6% | -0.5% |
| Pork operating margin | 5.3% | 11.0% | 5.2% | 3.0% | -2.4% |
| Chicken operating margin | 4.7% | 0.9% | -4.6%* | 5.6% | -4.5% |

*Chicken FY2021 driven substantially by a $626M one-time price-fixing
legal-contingency accrual, not market conditions — see below.

Tyson's own MD&A language (not a third party's characterization) for the
FY2020-vs-FY2019 Beef change: "Operating income increased primarily due to
market conditions, including COVID-19 disruptions, which increased the
spread between preexisting contractual agreements and the cost of fed
cattle." Nearly identical language appears for Pork. This is the company
itself, in an audited SEC filing, attributing margin expansion to the
disruption — about as strong a primary-source confirmation as this project
is likely to obtain.

**JBS USA** (SEC Form F-4 registration statement, filed 2023, containing
full-year 2020-2022 segment financials — SEC EDGAR, CIK 1450123; JBS does
not currently file 10-Ks, so this F-4 is the best full-year SEC-filed
segment data located this pass):

| Segment | 2020 | 2021 | 2022 |
|---|---|---|---|
| Beef North America EBITDA margin | ~13.1% | **~21.3%** | ~9.4% |
| Pork USA EBITDA margin | ~10.4% | ~10.5% | n/a (not extracted) |
| Pilgrim's Pride (poultry) EBITDA margin | ~9.5% | ~11.5% | n/a (not extracted) |

JBS's Beef North America Adjusted EBITDA rose 108.8% in 2021 (net revenue
+29.0%, i.e., margin expanded, not just absolute dollars), which JBS's own
filing attributes to "a strong demand in the United States" and a 25.1%
sales-price increase against only a 16.9% rise in operating costs — the same
disproportionate-benefit pattern as Tyson's Beef segment, independently
confirmed at a second major packer. Pork USA's margin was comparatively
flat (proportional revenue/cost growth), and Pilgrim's Pride (poultry) rose
only modestly — poultry again does not show the same dramatic pattern as
beef.

**Independent, non-advocacy corroboration**: the USDA AMS PSD 2021/2022
Annual Report to Congress states in its own voice: "The imbalance between
cattle supply and processing capacity persisted from 2020, and beef packers
continued to earn record profits in 2021. Strong demand for beef helped
maintain high prices at the retail level, and the disparity between live
cattle prices and boxed beef persisted from the prior year." This is a
government regulatory agency's own factual statement, not a political
office's blog post — a materially stronger source type than the White House
CEA blog this project relied on previously.

**Caveat / scope limit, same as Claim #12**: this is strong evidence for the
2020-2021 acute-disruption window specifically. Margins reverted sharply by
FY2022-FY2023 (Tyson Beef fell to -0.5%; JBS Beef NA nearly halved) — do not
generalize to "processors always benefit from disruptions" or treat the
elevated margin as a new permanent baseline.

**Original (2026-09-03) analysis below, retained for the antitrust-
litigation background, which remains accurate and is now expanded in
Claim #15 below:**

The White House CEA blog (Sept. 2021) asserts that "gross profits for some
of the leading beef, poultry, and pork processors are at their highest
levels in history" during the pandemic, and cites specific company
dollar figures (e.g., JBS: $2.3B in dividends/buybacks in 2020; Tyson: $477M
in dividends). These are *directionally* consistent with widely reported
pandemic-era meat-processor profitability, but:
- A political-office blog is advocacy-adjacent even when it cites real
  numbers, and per the brief's Rule 5 ("do not treat political statements or
  industry advocacy as empirical evidence"), these figures need independent
  verification against the underlying SEC filings/10-Ks/earnings-call
  transcripts before being treated as established in this project.
- This fork did not have scope/time to pull JBS, Tyson, National Beef,
  Cargill (private, no public filings), or Smithfield (private, owned by WH
  Group) financial filings directly.
- "Disproportionate" benefit specifically requires a *comparison* — margin
  expansion relative to farm-gate price movement and relative to retail
  price movement in the same period — which is a Section 8 (price
  transmission) analysis this fork did not attempt.

**Recommendation:** This is a high-value, well-defined claim to verify
properly (it's central to the "gouging" narrative and to Study 1's
attribution-coding scheme) — a dedicated research pass pulling actual 10-K
gross/operating margins for Tyson (public) and JBS (public, dual-listed) for
2019-2023, cross-referenced against USDA-published farm-to-retail spreads
for the same period, would let this move to Supported/Partially
Supported/Unsupported rather than sitting at Unresolved.

---

### Claim #15: "Are claims about 'food monopolies' supported by the
empirical literature, or would 'highly concentrated supply chains' be more
defensible terminology?"

**Verdict: Partially supported toward "highly concentrated supply chains"
as the more defensible term — "monopolies" is technically inaccurate but is
established political/advocacy shorthand.**

None of the three sectors shows evidence of monopoly in the technical
economic sense (a single dominant seller/buyer able to unilaterally set
price): all figures found show 3-4 major competing firms per sector with
CR4 well under 100% (beef ~82-85%, pork ~66-70%, poultry ~54%). "Oligopoly"
or "concentrated oligopoly" is the more precise structural descriptor;
"monopsony power" is the more precise term for the buyer-side concern raised
about packers vs. independent cattle producers specifically. "Monopoly" and
"food monopolies" appear to function in public/political discourse (e.g.,
in some advocacy and press usage) as loose shorthand for "a small number of
very large, powerful firms," not as a technically accurate claim of single-
firm dominance.

This is itself a useful and low-risk finding for the paper's marketing
contribution (Section 14): the *gap* between technically precise
industrial-organization terminology (oligopoly, concentrated market,
monopsony) and the looser popular/political terminology ("monopoly," "food
monopolies," "corporate greed") is exactly the kind of attribution/framing
phenomenon Study 1's discourse analysis could examine, rather than something
the paper needs to resolve as a factual matter before it can proceed.

**Recommendation:** In the manuscript, use "concentrated" / "oligopolistic"
/ "monopsony concern" as the paper's own analytic vocabulary, while treating
other actors' use of "monopoly"/"food monopolies" language as *data* (a
framing choice by that speaker) rather than adopting it as the paper's own
descriptive claim.

**2026-09-05 addendum — the anticompetitive-conduct evidence base is
broader and more commodity-differentiated than previously documented.** The
USDA AMS PSD 2021/2022 Annual Report to Congress (read in full this pass)
devotes a section to price-fixing litigation spanning all three commodities,
2020-2022, not just the beef case already in this file:

- **Poultry — criminal, not just civil.** Pilgrim's Pride *pleaded guilty*
  to a federal charge of conspiring to fix chicken prices (Feb. 2021) and
  paid a $107.9M DOJ fine; it separately paid $75M (Jan. 2021) and $110.5M
  (Oct. 2020, restraint-of-competition plea) in related matters. Tyson
  settled turkey price-fixing claims for $4.6M and $1.75M (2021). A related
  criminal case against Koch Foods and Pilgrim's Pride executives ended in
  two mistrials and eventual not-guilty verdicts/dropped charges
  (2021-2022) — the *criminal* prosecution of individuals did not succeed,
  even though Pilgrim's Pride the company pleaded guilty separately.
- **Pork.** Smithfield paid ~$200M combined (2022) across two price-fixing
  settlements; JBS paid $20M (Sept. 2022, pork).
- **Beef.** JBS paid $52.5M (Feb. 2022) in the beef price-fixing suit
  already documented in this file; a related Sysco Corp. suit (June 2022)
  makes the same allegation against Tyson/JBS/Cargill/National Beef.
- **Cross-cutting, different conduct category.** Cargill, Sanderson Farms,
  and Wayne Farms paid $84.8M (2022) to settle a *labor-market* wage-
  suppression conspiracy (improperly sharing worker-wage data via a
  consulting firm) — this is anticompetitive conduct on the *input* (labor)
  side, not output price-fixing, and should not be conflated with the
  price-fixing cases above in the manuscript.

**A guilty plea to a federal criminal antitrust charge (Pilgrim's
Pride/poultry) is categorically stronger evidence than a civil settlement
with an explicit no-wrongdoing statement (the beef case)** — this is a real,
commodity-specific difference in the strength of the anticompetitive-conduct
evidence that the manuscript should preserve rather than treat "meat
industry price-fixing" as one undifferentiated fact pattern across beef,
pork, and poultry.
