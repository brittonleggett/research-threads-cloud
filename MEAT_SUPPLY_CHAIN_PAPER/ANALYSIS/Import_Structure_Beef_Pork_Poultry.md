# Import Structure: Beef, Pork, and Poultry

Status: first-pass draft, 2026-09-03 (fork research pass). Primary source for
volumes/trends is USDA ERS "Sector at a Glance" pages, which themselves draw
on USDA FAS's Production, Supply and Distribution (PSD) database and USDA
ERS's Livestock and Meat International Trade Data product. The underlying
ERS trade dataset (`ers.usda.gov/data-products/livestock-and-meat-
international-trade-data`) contains the authoritative country-by-country,
year-by-year figures as downloadable Excel/CSV files back to 1989, but those
files were not machine-readable via WebFetch in this pass — **a follow-up
task is to download and parse those files directly** for exact country-level
tonnage rather than relying on ERS's narrative summaries and trade-press
citations of USDA outlook reports. See the "Follow-up" section at the bottom.

---

## Beef

**U.S. is simultaneously a major importer and a major exporter of beef.**
This is not a contradiction once the product mix is understood — see
"Why the U.S. both imports and exports beef" below.

### Volumes (verified, primary: USDA ERS Cattle & Beef Sector at a Glance)
- **2024 beef imports: 4.635 billion lbs (carcass-weight equivalent)** — a
  new record, more than 24% above the previous record set in 2023.
- **2024 beef exports: 3.003 billion lbs** — about 1% below 2023, and a 15%
  decline from the record set in 2022.
- Data source cited by ERS: USDA FAS Production, Supply and Distribution
  (PSD) database.

### Top source countries (secondary sources tracing USDA FAS/GATS data —
not yet independently re-verified against the raw PSD/GATS tables; treat
as directionally reliable, not exact)
- Brazil: ~387,000 metric tons to the U.S. in 2025 (per trade-data
  aggregator citing USDA data; Brazil's beef export access to the U.S. has
  been a live trade-policy issue in 2025–2026).
- Australia: described by USDA-FAS-sourced trade press as the "structural
  anchor" of U.S. lean processing beef supply, with 2026 export forecasts
  around 2.2 million tons globally (not U.S.-specific).
- Canada, Mexico, New Zealand: also principal suppliers (unquantified in
  this pass).
- Argentina, Paraguay, Nicaragua: imports reported "up significantly" year
  over year in 2025 reporting — needs primary-source quantification.
- **Follow-up needed:** exact 2023–2025 country-by-country volumes from the
  ERS Livestock and Meat International Trade Data Excel/CSV files.

### Product mix — what's actually being imported
Confirmed via USDA ERS (Cattle & Beef Sector at a Glance): **a majority of
U.S. beef imports are destined for blending into ground beef.** The
mechanism (also corroborated by Kansas State University Extension's
"Cattle Chat" series, citing the same USDA dynamic):
- Most U.S. fed cattle are grain-finished, producing well-marbled beef ideal
  for steaks/premium cuts. A byproduct of fabricating retail cuts from fed
  cattle is roughly 50%-fat trim.
- To hit the fat percentages consumers expect in ground beef (typically
  ~73–93% lean), processors blend that fatty domestic trim with **lean**
  trim — sourced either from U.S. cow/bull slaughter (cull dairy and beef
  cows) or from imports, chiefly grass-fed beef from Australia, New Zealand,
  and South American suppliers, which runs much leaner.
- The domestic ground-beef market is the main driver of U.S. beef imports,
  and import demand is "highly correlated with the rate of domestic cow
  slaughter" (ERS) — when the cattle herd contracts and more cull cows are
  slaughtered, more lean domestic trim is available and import demand for
  lean trim eases; when the herd is being rebuilt (fewer cows slaughtered),
  import demand for lean trim rises. This is the mechanism connecting the
  cattle cycle to the import cycle (see "the puzzle" below).

### Why the U.S. both imports and exports beef (claim #8 — Supported)
Two distinct, non-contradictory trade flows:
1. **Imports:** predominantly lower-value **lean trim** for ground beef
   (see above) — a product U.S. fed-cattle production structurally
   under-supplies domestically.
2. **Exports:** predominantly higher-value **premium/marbled cuts** (the
   kind U.S. grain-finished cattle excel at) sold to markets like Japan,
   South Korea, and Mexico that pay a premium for that eating experience.
This is classic intra-industry trade driven by product differentiation
(different cuts/grades serving different demand), not evidence that the
U.S. "needs" foreign beef to meet aggregate volume — the U.S. is a large net
beef producer overall, but has a structural mismatch in the specific
lean/fat composition its own herd produces relative to demand.

### The current empirical puzzle: record imports + record-low herd +
record-high prices, all at once (feeds `NOTES/Claim_Fact_Check.md` #6, #7,
and `NOTES/Research_Problem_Exploration.md`)
- U.S. cattle inventory (USDA NASS Cattle report, via multiple ag-press
  outlets citing the official report): **87.15 million head as of Jan. 1,
  2024** — the smallest U.S. cattle herd since 1951 (some later-2024/2025
  reports put it lower still, ~86.2 million head — needs a clean primary
  NASS citation with exact report date in the follow-up pass).
- At the same time, 2024 set the beef **import** record noted above, AND
  cattle/beef prices reached record or near-record highs (choice-grade beef
  reported above $300/cwt in summer trade press; multiple ag-econ outlets
  describe 2024–2026 as a period of simultaneously record imports and
  record prices).
- **This directly bears on claims #6 and #7 in the fact-check** (does
  import supply lower retail prices / suppress cattle prices): in this
  period, no — imports rose sharply at the same time prices rose sharply,
  because the dominant driver is the domestic herd contraction (drought-
  driven cow culling over 2020–2023), not import competition. Imports here
  read as a *response* to a domestic lean-trim shortage, not a *cause* of
  low prices. This does not settle the general theoretical question (basic
  supply logic still implies imports put some downward pressure on price
  relative to a counterfactual with zero imports) — it settles that the
  simple public claim "imports are lowering/should lower beef prices" is
  not supported by the 2024–2026 U.S. data and is misleading without the
  herd-size context.
- **Caution on sources for this section:** a 2026-02 White House
  presidential action titled "Ensuring Affordable Beef for the American
  Consumer" and advocacy-group commentary (e.g., Coalition for a Prosperous
  America, a protectionist trade-policy advocacy organization) both discuss
  this dynamic but with policy agendas attached — their framing ("imports
  don't lower costs," import quota/tariff proposals) should be treated as
  political/advocacy positioning per the project's research standards, not
  as neutral empirical findings, even where the underlying trade and price
  figures they cite are independently verifiable via USDA.

---

## Pork

**U.S. is a net exporter of pork**, unlike beef, and has been since 1995
(USDA ERS, Hogs & Pork Sector at a Glance — primary).

### Volumes (primary: USDA ERS)
- Exports: 2010–2022 average over 5.6 billion lbs/year (carcass-weight
  equivalent); 2020 peak of 7.3 billion lbs. In 2022 the U.S. ranked #2
  globally in pork exports, behind the EU.
- Top export destinations (2022, ERS Figure 5): Mexico and Japan have
  accounted for about half of U.S. pork exports over the last 10 years;
  South Korea, Canada, and China also significant (China trade volatile due
  to tariffs).
- 2024 (secondary, USMEF trade-group press release, needs primary
  cross-check): pork exports "record-large" in 2024; Mexico $2.58B, Japan
  $1.38B, Canada $852.96M, South Korea $727.9M in export value.
- Imports: last-decade average ~6% of *global* pork import volume; 2020,
  under 4% of global import volume. About 93% of U.S. pork imports
  originate from Canada + the EU combined, with **almost 70% from Canada
  alone**.
- Live hog imports from Canada: ~6.5 million head in 2022 (~5% of U.S.
  federally inspected slaughter), down from a 2007 peak of ~10 million head
  (9% of slaughter).

### Structural note
Pork's cross-border integration is dominated by one relationship — Canada
(live hogs and pork product both) — rather than the more geographically
diverse sourcing pattern seen in beef. This is a meaningfully different
import structure than beef's multi-country lean-trim sourcing and should
not be described with the same "diverse foreign sourcing" language used for
beef.

---

## Poultry (broiler/chicken)

**U.S. is the world's largest poultry producer and the world's second-
largest poultry exporter**, and poultry imports are a rounding error next
to production and exports (USDA ERS, primary for the export-share figure).

### Volumes (primary where cited as ERS; outlook-report figures via trade
press citing ERS Livestock, Dairy & Poultry Outlook — secondary but traced)
- **13.6% of U.S.-produced poultry meat was exported in 2024** (USDA ERS,
  Poultry & Eggs topic page — directly confirmed).
- Broiler imports are small: 2023 total broiler imports ≈131 million lbs,
  with **Chile alone accounting for 68.7%** of that. 2024 import
  projections in ERS's Livestock, Dairy, and Poultry Outlook series moved
  around (an early-2024 projection near 215 million lbs was later revised
  down to ~162 million lbs) — reflects normal within-year forecast revision,
  not a data error; needs the final-actual 2024 figure from the completed-
  year outlook report in the follow-up pass.
- For scale: U.S. broiler production is in the tens of billions of pounds
  annually, so imports in the 130–215 million lb range represent well under
  1% of production — an order of magnitude smaller, relatively, than beef's
  import share.

### Structural note
Poultry's near-total vertical integration (grower contracts with
integrators — see `NOTES/Commodity_Structure_Comparison.md`, being written
in parallel) plus its role as a large net exporter means the "foreign
sourcing" frame that fits beef (and to a lesser extent pork) barely applies
to poultry. Any paper narrative that treats "foreign meat imports" as a
single phenomenon across all three commodities will misrepresent poultry.

---

## Cross-commodity summary table

| | Net trade position | 2024 imports | 2024 (or latest) exports | Import product mix | Top import source(s) |
|---|---|---|---|---|---|
| Beef | Net importer of *volume* despite exporting high-value cuts; imports > exports in carcass-weight lbs | 4.635B lbs (record) | 3.003B lbs | Majority = lean trim for ground beef | Brazil, Australia, Canada, Mexico, New Zealand, Argentina (diversified) |
| Pork | Net exporter since 1995 | Small; ~6% of global import volume | 5.6B lbs/yr avg (2010–22); 7.3B lbs 2020 peak | Live hogs + pork product | ~70% Canada; ~93% Canada+EU combined |
| Poultry | Large net exporter (2nd largest globally) | ~130–215M lbs (2023–24) — <1% of production | 13.6% of production exported (2024) | Broiler meat | Chile (~69% of import volume, 2023) |

---

## Follow-up (not yet done in this pass)
1. Download and parse the actual ERS Livestock and Meat International Trade
   Data Excel/CSV files for exact, primary-source country-by-country annual
   volumes 2015–2025 for beef, pork, and poultry (this pass relied on ERS's
   narrative "Sector at a Glance" summaries and some trade-press citations
   of USDA outlook-report figures, which is "verified, secondary-traced-to-
   primary" rather than fully primary for the country-level numbers).
   Suggested resource: `SOURCE_VERIFICATION/Evidence_Table_Imports.md` log
   of unsuccessful/inconclusive searches.
2. Get a clean, dated primary citation for the USDA NASS Cattle inventory
   report figure(s) (87.15M head Jan 1 2024 vs. 86.2M head in later
   reporting — confirm exact report titles/dates).
3. Cross-check the 2024 pork export figures (currently sourced to a USMEF —
   U.S. Meat Export Federation, an industry trade group — press release)
   against USDA FAS/Census trade data directly.
4. Get the finalized (not mid-year-projected) 2024 poultry import total from
   the completed-year USDA ERS Livestock, Dairy, and Poultry Outlook.
