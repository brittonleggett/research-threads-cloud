# 2026-09-09 — USDA ERS historical Meat Price Spreads pull: full-history farm-share trend

Closes the top un-started next-action flagged repeatedly in `PROJECT_STATUS.md` since 2026-09-03
("test Claim #1/#2's 'historically weak returns' framing against the full 1970-present series" —
never actually attempted until now).

## What was pulled

Downloaded USDA ERS's own historical monthly meat price spreads file directly:
[Meat Price Spreads](https://www.ers.usda.gov/data-products/meat-price-spreads) →
`historical-monthly-price-spread-data-for-beef-pork-broilers.csv` (13,081 rows, monthly,
1970-2026), saved to `DATA/USDA_ERS_Historical_Meat_Price_Spreads_1970-present.csv`. Also pulled
the companion `summary-of-retail-prices-and-price-spreads.csv` (USDA's own published "farmers'
share" percentage, but only covers the trailing ~2 years) as a methodology check, saved to
`DATA/USDA_ERS_Summary_Retail_Prices_and_Spreads.csv`. Analysis script:
`DATA/analyze_farm_share.py`.

## Method

The historical file has no pre-computed "farmers' share %" column, only raw cents-per-pound
series (`Choice beef net farm value`, `Choice beef retail value`, `Pork net farm value`,
`Pork retail value`). Computed farm share = net farm value ÷ retail value × 100, annual average
of the monthly series, for beef and pork separately (broiler data in this file has no comparable
farm-value series, so poultry isn't included here). Validated the ratio methodology against
USDA's own directly-published "farmers' share" figures in the summary file: my derived 2025 beef
share (53.5%) is close to USDA's own published 2026 monthly figures (51.1-55.6%, avg 53.8%) —
good agreement, not an exact replication (likely a retail-value-series definitional difference,
e.g. "Choice beef retail value" vs. "All fresh beef retail value"), so treat my full-history
series as directionally solid but not identical in every decimal to any single official USDA
percentage cited elsewhere in this project.

## Finding: a real, undocumented-in-this-project secular decline, with beef's recent rebound now in historical context

**Decade averages, farmers' share of the retail dollar:**

| Decade | Beef | Pork |
|---|---|---|
| 1970s | 63.6% | 53.7% |
| 1980s | 58.7% | 49.4% |
| 1990s | 52.2% | 37.0% |
| 2000s | 46.1% | 28.5% |
| 2010s | 48.1% | 26.7% |
| 2020s (through 2025) | 44.4% | 22.6% |

- **Beef**: farmers' share fell by roughly 20 percentage points from the early 1970s (peak
  ~68% in 1973) to a 2020-2021 trough (~37%), then **rebounded sharply to 47.8% (2023), 50.2%
  (2024), 53.5% (2025)** — the recent rise already documented in `PROJECT_STATUS.md` and Claim
  #2 is real and is now the *largest 3-year gain in the full 55-year series*, driven by the
  herd-contraction/record-cattle-price dynamic already established elsewhere in this project. But
  it is a partial recovery within a much longer decline, not evidence the long-run trend has
  reversed — 2025's 53.5% is still below every decade average from the 1970s-1990s.
- **Pork**: the decline is steeper and has **not** reversed. From a 1970s average of 53.7%
  (peaking near 62% in 1973) to a 2020s average of 22.6% — less than half the 1970s share — with
  2025 (24.0%) still near the historical floor, not participating in beef's rebound. This
  matches the project's existing note that pork's contract/tournament production system (see
  `NOTES/Commodity_Structure_Comparison.md`) differs structurally from beef's more open market —
  worth stating explicitly as a beef/pork divergence in the manuscript, not folding pork into
  beef's "farm share is recovering" narrative.

## How this changes Claim #2 (and the broader "historically weak returns" question)

Previous verdict (Claim #2, `NOTES/Claim_Fact_Check.md`) was based on a single 2023→2024
data point (49.8¢→52.2¢) and correctly rebutted the "6 cents of the food dollar" conflation, but
made no claim about the longer historical trend. This pull adds the missing context:

- The popular narrative error isn't just "conflating the whole food dollar with meat" — there's a
  **second, more defensible version of a "farmers get a shrinking share" claim that IS supported
  by real data**, just not the version usually stated. Beef and pork farmers' shares of the
  retail dollar really have fallen substantially since the 1970s (a genuine structural fact,
  consistent with the concentration-history literature already in this project, AER-785 etc.).
  The error is in treating this as still-currently-declining or as "6 cents on the dollar" — the
  real number is much higher (roughly 45-55% for beef even now) and, for beef specifically, has
  been *recovering* for three years, not worsening.
- This is good Study 1 framing material: a case where the popular claim gets the *direction*
  wrong for the current period (says "worsening," reality says "beef: recovering; pork: still at
  a historic low but flat, not falling further") while still being right about the *long-run*
  structural change (both did fall substantially since the 1970s) — a more nuanced
  fact-vs-narrative gap than a simple "true/false," and arguably a stronger empirical hook than
  the flatter "$0.50 not $0.06" framing alone.

**Recommend updating Claim #2's row in `NOTES/Claim_Fact_Check.md`** to reference this fuller
history (leaving the verdict as "Partially supported / misleading without context," now with
much stronger evidentiary grounding) rather than resting on one year-over-year comparison. Not
done in this pass to keep this note the single source of the new numbers; a follow-up pass should
fold this into the ledger and `SOURCE_VERIFICATION/Evidence_Table.md` proper.

## Not done / caveats

- Broiler/poultry farm share not computed here — this file's broiler series has no comparable
  farm-value line item; would need a different USDA source (possibly the PSD Annual Report
  already used for concentration figures, or ERS's poultry-specific price-spread product if one
  exists) — worth a future pass, not urgent given poultry's ~99.5% contract structure makes "farm
  share of the retail dollar" a less meaningful frame there anyway (see `Commodity_Structure_Comparison.md`).
- This is my own derived ratio, not a copy-paste of an official USDA percentage — flagged
  explicitly above so it's never mistaken for a directly-quoted USDA statistic in the manuscript.
  Cite as "USDA ERS Meat Price Spreads historical data, farm share calculated as net farm value
  ÷ retail value" if used.

No design decisions touched. No external contact. No money spent.
