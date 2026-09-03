# Price Transmission Literature — Producer vs. Consumer Prices in Beef, Pork, Poultry

Scope: Section 8 of the project brief. Covers farm-to-wholesale-to-retail
price spreads, marketing margins, asymmetric price transmission ("rockets
and feathers"), and processor-margin evidence during supply shocks, for
beef, pork, and poultry separately. See
`SOURCE_VERIFICATION/Evidence_Table_PriceTransmission.md` for the row-level
ledger this memo draws on.

## 1. The core primary data source: USDA ERS Meat Price Spreads / Price
Spreads from Farm to Consumer

- **What it is:** USDA ERS's Meat Price Spreads dataset tracks monthly
  average price values at the farm, wholesale, and retail stages for
  Choice-grade beef and pork and for broilers, plus retail prices for
  turkey, whole chickens, eggs, and dairy. Monthly data since 1970. Combines
  BLS retail price data with USDA AMS livestock/wholesale price data.
  Updated monthly (current release schedule as of this research pass: last
  updated 2026-08-12, next update 2026-09-11; historical files updated
  2026-02-25). https://www.ers.usda.gov/data-products/meat-price-spreads
- **Methodology:** ERS starts from a "standard animal" — a fixed cutting
  yield is used to translate live-animal value into retail-cut-equivalent
  value (2.40 lb of standard steer per lb of retail beef cuts; 1.869 lb of
  hog per lb of retail pork cuts). This is what lets ERS compute a "farmer's
  share of the retail dollar" for beef and pork specifically (distinct from,
  and not comparable to, the broader "farm share of the food dollar" figure
  below, which spans all foods including heavily processed/packaged items).
- **Caution for this project:** ERS's own price-spreads methodology is the
  most-cited but not the only game in town — see the scanner-data critique
  in Section 3 below. Any beef/pork farm-share figure used in this project
  should specify which series (Meat Price Spreads "standard animal" farm
  share vs. USDA ERS Food Dollar Series overall farm/ranch share) it comes
  from; these are frequently conflated in public discourse and that
  conflation is itself a "misleading without context" risk (see Claim #2
  fact-check).

## 2. Farm share of the retail dollar: beef and pork specifically vs. the
"6 cents of the food dollar" figure

Two genuinely different, frequently confused ERS series:

- **USDA ERS Food Dollar Series (all foods, "farm and ranch share"):**
  Farmers/ranchers as a group received about 5.9 cents of the average food
  dollar in 2023 and 5.8 cents in 2024 (i.e., roughly flat, a fractional
  decline). This figure spans the entire U.S. food-at-home *and* food-away-
  from-home basket, most of which (packaged, processed, restaurant food) has
  a much higher labor/processing/marketing cost share than raw meat. This is
  the "less than 6 cents of the food dollar" statistic widely cited in farm-
  advocacy commentary — it is accurate but describes *all food*, not meat
  specifically, and should not be presented as a beef- or pork-specific
  figure. Source: American Farm Bureau Federation Market Intel, "Farmers
  Receive Less Than 6 Cents of the Food Dollar" (2026-03-23), citing USDA
  ERS Food Dollar Series. https://www.fb.org/market-intel/farmers-receive-less-than-6-cents-of-the-food-dollar
- **USDA ERS Meat Price Spreads farm share (beef and pork specifically):**
  Using the "standard animal" methodology above, the beef farm share of the
  retail beef dollar was **49.8 cents in 2023, rising to 52.2 cents in
  2024** (a +4.8% increase, i.e., the farmer's *share* of the beef dollar
  went up, not down, in the most recent year available). Pork farm share
  was **22.1 cents in 2023, rising to 23.7 cents in 2024**. Same AFBF
  Market Intel piece, same ERS-sourced figures.
- **Implication:** the popular narrative "farmers get almost nothing of the
  food dollar" is true for the *food dollar as a whole* but is a
  substantially different — and, for beef in particular, higher and in the
  most recent year *rising* — number when restricted to meat specifically.
  This is exactly the kind of claim that needs the "Partially supported /
  Misleading without context" treatment rather than a flat Supported or
  Unsupported. See `NOTES/Claim_Fact_Check_PriceTransmission_Draft.md`
  Claim #2.
- **Historical caution:** a widely repeated figure — farm share of *all*
  foods was ~31% in 1980, ~24% in 1990, ~21% in 1997 — is from the broader
  food-dollar series, not the meat-specific series, and should not be used
  as a stand-in for a beef/pork historical trend without finding the
  meat-specific historical series (ERS Meat Price Spreads historical data
  back to 1970 should have it; this pass did not extract the full time
  series, only the two most recent years via the secondary AFBF summary —
  **flagged as a follow-up**: pull the actual ERS Meat Price Spreads XLSX/CSV
  historical file directly rather than relying on the AFBF summary alone).

## 3. Asymmetric price transmission ("rockets and feathers") — beef

The literature is genuinely split, and the split tracks the type of retail
price data used:

- **Older/still commonly cited: beef IS asymmetric.** A body of work
  (surveyed in Meyer & von Cramon-Taubadel, "Asymmetric Price Transmission:
  A Survey," *Journal of Agricultural Economics*, 2004) and beef-specific
  studies using BLS-derived retail price series have found retail beef
  prices respond faster to farm-price increases than decreases.
- **Newer, contrary finding using scanner (actual transaction) data: NOT
  asymmetric.** Pozo, V. F., Bachmeier, L. J., & Schroeder, T. C. (2021).
  "Are there price asymmetries in the U.S. beef market?" *Journal of
  Commodity Markets*, 21, 100127. https://doi.org/10.1016/j.jcomm.2020.100127
  — Using retail *scanner data* (actual point-of-sale transaction prices),
  the authors find **no evidence of vertical asymmetric price transmission**
  between farm, wholesale, and retail beef prices. Using the more commonly
  used BLS-derived retail price series (average reported prices, not
  transaction scanner data), the same underlying relationship **does**
  show asymmetric adjustment. The authors' interpretation: because scanner
  prices better reflect what consumers actually pay (capturing sales,
  promotions, etc.), the U.S. beef market may be less inefficient / less
  asymmetric than earlier BLS-based studies suggested.
- **Takeaway for this project:** "beef prices are asymmetric" is a
  defensible but *data-dependent* claim, not a settled fact — the choice of
  retail price series materially changes the answer. Any manuscript claim
  about beef price asymmetry should name which data series it rests on.

### 3.1 Verification upgrade (2026-09-03, via Consensus.app Deep Research —
full text of Pozo et al. read, not just abstract)

Closes the verification gap flagged earlier (ScienceDirect had 403'd
WebFetch). Confirmed details:
- **Method:** Threshold vector error-correction model (TVECM) with
  simulated nonlinear impulse responses, monthly farm/wholesale/BLS-retail/
  scanner-retail beef prices, **January 2001–December 2012**.
- **Core result:** Impulse-response tests fail to reject symmetry in all
  models using scanner retail data. One exception: a slope-based long-run
  asymmetry detected for the farm-to-scanner-retail price pair specifically
  — so the "no asymmetry" finding is not perfectly clean even within this
  paper; it's the *impulse-response* evidence the authors treat as
  decisive (offsetting coefficients across horizons can still net to a
  symmetric cumulative response), not an absence of any asymmetric
  coefficient anywhere in the model.
- **Mechanism claim:** Scanner prices are systematically lower and more
  variable than BLS prices because BLS methodology omits quantity
  weighting, discounted/sale prices, random-weight items, and lower-priced
  outlet formats (e.g., supercenters) — a bias that inflates the *apparent*
  retail price and can manufacture the appearance of asymmetry. Rojas,
  Andino & Purcell (2008), "Retailers' response to wholesale price changes:
  new evidence from scanner-based quantity-weighted beef prices,"
  *Agribusiness*, made the same measurement argument earlier, using
  scanner data to show retailers respond *more* to wholesale price changes
  than BLS series suggest.

**This is a genuinely split literature, not just old-vs-new.** Consensus's
own evidence synthesis across 16 papers on "do U.S. beef prices transmit
asymmetrically" put it at 69% Yes / 13% Mixed / 19% No among papers taking
a position — i.e., most papers in the broader corpus still find *some*
asymmetry; Pozo et al. is the strongest scanner-data challenge to that
majority view, not proof the majority is wrong. Newer nonlinear/
disaggregated studies continue to find asymmetry, often concentrated at the
**wholesale-retail** stage (not farm-wholesale) and stronger for
higher-quality cuts:
- Fousekis, P. et al. (2015). "Vertical price transmission in the US beef
  sector: Evidence from the nonlinear ARDL model." *Economic Modelling* —
  125 citations; NARDL finds asymmetry, strongest at wholesale-retail.
- Panagiotou, D. (2017) — wholesale increases transmit to retail in 5 of 6
  cut-grade pairs; decreases often don't; "rockets and feathers" strongest
  in Choice and sirloin products specifically.
- Surathkal (2017) — similar cut-grade disaggregation finding.
- Hahn (1990) — early asymmetry finding, greater responsiveness to
  increases than decreases (BLS-era).
- Chung (2018) — Mandatory Price Reporting improved *speed* of adjustment
  but left only limited evidence of *greater* asymmetry.
- **Parcell (2026)** — an event-study around the **alleged 2015–2019 beef
  packer collusion/price-fixing litigation** finds only slight and
  economically unimportant changes in price responsiveness around that
  period. **Flag for `SOURCE_VERIFICATION/Evidence_Table.md`'s Market
  Concentration/Antitrust section** — this is a real, findable academic
  study bearing directly on the currently-unverified "beef/broiler
  processors have faced antitrust litigation alleging price-fixing" claim;
  full citation still needs to be pinned down (title/journal), but the
  existence and substantive finding are corroborated by Consensus's
  citation-graph search, not just a single search snippet.
- Luke (2026) — quantity-weighted scanner-based beef demand elasticities
  are higher than USDA/BLS-derived series would suggest (consumers more
  price-sensitive than public data implies) — same BLS-understates-
  responsiveness pattern as the Pozo/Rojas measurement critique, applied to
  demand elasticity rather than price-transmission symmetry specifically.

**Bottom line, sharpened:** Don't state "beef price transmission is
symmetric" or "asymmetric" as a flat fact. The defensible claim is
narrower and more useful for the manuscript: *retail measurement choice
(scanner vs. BLS) materially changes the empirical answer*, asymmetry when
it appears is concentrated at the wholesale-retail stage rather than
farm-wholesale, and it's stronger for higher-quality cuts than commodity
grades — none of which was in the project's evidence base before this
Consensus pass.

## 4. COVID-19 as a natural stress-test of the beef supply chain

- Erol, E., & Saghaian, S. H. (2022). "The COVID-19 Pandemic and Dynamics of
  Price Adjustment in the U.S. Beef Sector." *Sustainability*, 14(8), 4391.
  https://doi.org/10.3390/su14084391 — Using monthly farm/wholesale/retail
  beef prices 1970–2021 with time-series/structural-break methods, finds the
  pandemic shock produced **asymmetric price adjustment along the beef
  chain in both speed and magnitude**, with the historical-decomposition
  analysis showing consumers paying *higher* prices than predicted while
  farmers received *lower* prices than predicted during the disruption —
  i.e., the pandemic widened the farm-to-retail spread, concentrated at the
  retail level.
- Balagtas, J. V., & Cooper, J. (2021). "The Impact of COVID-19 on United
  States Meat and Livestock Markets." *Choices*, Quarter 3, 2021 (AAEA
  outreach magazine; Cooper is USDA Office of the Chief Economist, Balagtas
  is Purdue). Concludes meatpackers exercised market power during the 2020
  plant-shutdown period to **increase price margins** — cattle/hog prices
  fell (reduced processing demand from shuttered/slowed plants) while
  wholesale/retail meat prices rose, widening packer margins.
  https://www.choicesmagazine.org/choices-magazine/theme-articles/agricultural-market-response-to-covid-19/the-impact-of-covid-19-on-united-states-meat-and-livestock-markets
- Cooper, J., Breneman, V., Ma, M., Lusk, J., Maples, W., & Arita, S. (2023).
  Econometric assessment of COVID-19 outbreaks on U.S. meat production and
  plant utilization using confidential USDA plant-level daily slaughter
  data. *Food Policy*. Finding: larger beef and pork plants had
  disproportionately greater capacity underutilization during the April–May
  2020 peak disruption than smaller plants; no equivalent size effect found
  for broiler plants. This is a *supply/capacity* finding, not a margin
  finding directly, but it's the mechanism (concentrated large-plant
  disruption) that the margin studies above point to as the proximate cause
  of the 2020 farm-retail spread widening.
- **Caveat:** COVID-19 is one acute, unusual shock (plant closures from
  worker illness, not a normal demand/supply cycle). It is good evidence
  that packer margins *can* expand sharply during acute disruption; it is
  weaker evidence about "normal" period-to-period price transmission
  behavior. Treat as answering Claim #12/#4 specifically about disruption
  periods, not as general-purpose evidence about baseline price
  transmission.

## 5. Pork: asymmetric transmission literature more consistently finds
asymmetry than beef does, but methodology varies

- Boyd, M. S., & Brorsen, B. W. (1988) — early test of pork marketing-channel
  price adjustment; found **symmetric** responses.
- Goodwin, B. K., & Harper, D. C. (2000) — threshold cointegration model;
  found **asymmetric** adjustment, with information flowing farm → wholesale
  → retail (i.e., retail responds to upstream shocks, not the reverse).
- Miller, D. J., & Hayenga, M. L. (2001); Gervais, J.-P. (2011, smooth
  transition cointegration); Assefa, T. T. et al. (2017) — additional
  studies finding asymmetric long-run transmission between farm and retail
  pork prices.
- Consensus read: more of the pork literature finds asymmetry than the most
  recent beef scanner-data study does, but methodology (threshold
  cointegration vs. simple ARDL vs. scanner vs. BLS data) drives a lot of
  the disagreement across both commodities. No single "the literature says
  X" sentence is defensible without naming the method.

## 6. Poultry: the price-transmission question doesn't map cleanly onto the
beef/pork "farm price" concept

- Structural difference (see also `NOTES/Commodity_Structure_Comparison.md`):
  broilers are raised almost entirely under contract with vertically
  integrated companies ("integrators": Tyson, Pilgrim's, Perdue, etc.).
  Since the 1990s the integrators have paid growers via a **tournament
  system** — a grower's pay depends on their *relative* performance (feed
  conversion, mortality, etc.) against other growers delivering birds to the
  same plant in the same week, not on a market-clearing per-pound "farm
  price" the way cattle or hogs are priced. There is no broiler equivalent
  of "the farm price of chicken" in the commodity-market sense.
- Because of this, "farm-to-retail price spread" analysis for poultry
  typically substitutes **feed cost / live-production-cost ("live cost")**
  as the upstream cost driver rather than a farm price, since integrators —
  not growers — sell wholesale product and set/receive the wholesale price.
  USDA ERS: "Financial Risks and Incomes in Contract Broiler Production,"
  *Amber Waves*, Aug. 2014 (background on the contract-production income
  structure).
- USDA ERS Chart of Note, "Fees paid to growers for raising broiler chickens
  varied widely in 2020" — documents wide grower-to-grower fee dispersion
  under the tournament system. http://www.ers.usda.gov/data-products/charts-of-note/chart-detail?chartId=104642
- **2024 regulatory development, directly relevant to Study 1/fact-check:**
  USDA AMS finalized a rule under the Packers and Stockyards Act — "Poultry
  Grower Payment Systems and Capital Improvement Systems" — published in
  the Federal Register 2024-06-10. https://www.federalregister.gov/documents/2024/06/10/2024-12415/poultry-grower-payment-systems-and-capital-improvement-systems
  This rule directly regulates how tournament-style pay and capital-
  investment demands on growers work; it is itself evidence that USDA
  considers the current grower-payment structure a live regulatory/fairness
  issue, independent of any court or academic finding of anticompetitive
  conduct. **This has not yet been read in full / verified beyond the
  Federal Register listing — flagged as a follow-up** for whoever owns
  Section 7 (COOL)/regulatory-timeline work or a later pass, since it's
  adjacent to but outside this fork's Section 8 scope.
- One study (title/full citation not fully pinned down in this pass —
  **flagged as unverified, do not cite without re-finding it**) reportedly
  finds wholesale broiler price is the "causal center" of the chain, with
  integrator concentration/power cited as the reason — this needs a proper
  WebFetch-verified citation before use; treat as an unconfirmed lead, not
  a citable finding.

## 7. Bottom line for `PROJECT_STATUS.md` synthesis

- The *empirical* consensus on beef/pork asymmetric price transmission is
  **contested, not settled** — methodology (which retail price series;
  which econometric technique) changes the answer, especially for beef.
- What *is* well-supported: during the 2020 COVID plant-disruption shock
  specifically, beef packer margins widened and farm-retail spreads grew
  faster than normal (multiple independent sources agree on this).
- The "farmers get almost nothing" framing is accurate for the *whole food
  dollar* but overstates the case for beef/pork specifically, where farm
  share is roughly half the retail dollar for beef and it *rose* in the
  most recent year (2023→2024) rather than falling.
- Poultry cannot be analyzed with the same farm-price framework at all —
  its structure (tournament grower pay, full vertical integration) means
  the "producer price vs. consumer price disconnect" question has to be
  reframed around grower compensation adequacy/fairness and integrator
  margin, not a market farm price.
