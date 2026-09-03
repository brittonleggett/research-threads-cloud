# Market Concentration Evidence — Beef, Pork, Poultry Processing

Status: first pass, 2026-09-03. Covers Section 5 of the project brief. All
figures below are traced to primary sources; see
`SOURCE_VERIFICATION/Evidence_Table_Concentration.md` for the row-level
ledger, exact URLs, and verification status.

## Terminology — used carefully, not interchangeably

- **Concentration**: the share of an industry's output/input purchases held
  by the largest firms (e.g., CR4 = top-4 share; HHI = sum of squared market
  shares). A *descriptive* structural measure, not a legal conclusion.
- **Oligopoly**: a market with few enough sellers that each firm's actions
  visibly affect rivals — a structural condition concentration measures can
  indicate but do not, by themselves, prove.
- **Monopsony / monopsony power**: concentration on the *buying* side (few
  buyers facing many sellers) — the specific concern raised about packers
  buying from numerous independent cattle producers. Distinct from
  concentration on the *selling* side.
- **Monopoly power**: a single firm's ability to profitably restrict output
  and raise price above competitive levels. None of the beef/pork/poultry
  processing sectors are monopolies by any figure found so far (CR4 well
  below 100%, multiple large firms).
- **Market power** (general): ability of a firm to influence price
  profitably, whether from the buy or sell side, which does not follow
  automatically from concentration and generally requires additional
  evidence (price-cost margins, conduct evidence, econometric estimation of
  demand/supply elasticities) beyond a CR4/HHI number.
- **Vertical integration**: single-firm ownership across supply-chain stages
  (e.g., broiler integrators owning birds through hatchery-to-processing) —
  a different phenomenon from horizontal concentration among processors,
  though the two interact (see `NOTES/Commodity_Structure_Comparison.md`).
- **Buyer power**: leverage a large buyer (processor over farmers, or
  retailer over processors) can exert on price/terms even short of
  classic monopsony.
- **Anticompetitive conduct**: specific, provable actions (price-fixing,
  bid-rigging, illegal information sharing) — a legal finding, not inferred
  from concentration alone. See the price-fixing litigation note below;
  concentration figures are not themselves evidence of anticompetitive
  conduct.

## Verified CR4 trajectory (four-firm concentration ratio)

Two independent, both-primary data points bracket the modern trend:

| Commodity | Market defined as | 1980 (USDA GIPSA, animal-input basis) | 1997 (USDA GIPSA, animal-input basis) | ~2021 (White House CEA, citing recent data) |
|---|---|---|---|---|
| Beef (steers/heifers) | Share of steer/heifer animals procured for slaughter by top 4 firms | 36% | 80% | 82% (CEA: 25% in 1977 → 82% "today," 2021) |
| Beef (boxed fed beef output) | Share of boxed fed beef output from top 4 steer/heifer slaughter firms | 53% | 83% | not separately re-verified |
| Pork (hogs) | Share of hog animals procured for slaughter by top 4 firms | 34% | 54% | 66% (CEA: 33% in 1976 → 66% "today," 2021) |
| Poultry (chickens, Census shipments basis) | Share of dollar value of shipments, top 4 firms | 32% (1982) | 41% (1992, latest year in that ERS series) | 54% (CEA: 35% in 1986 → 54% "today," 2021) |

**Sources:**
- USDA/ERS, *Consolidation in U.S. Meatpacking* (MacDonald, Ollinger, Nelson,
  Handy, Feb. 2000, AER-785), Chapter 3, Tables 3-1 and 3-2 — verified by
  direct PDF read.
  `https://ers.usda.gov` (AER-785; specific URL in evidence table).
- White House Council of Economic Advisers, "Addressing Concentration in the
  Meat-Processing Industry to Lower Food Prices for American Families,"
  bidenwhitehouse.archives.gov blog, Sept. 8, 2021 (Brian Deese, Sameera
  Fazili, Bharat Ramamurti) — verified by direct fetch. This is a **White
  House policy blog, not a peer-reviewed or agency statistical release**; it
  cites "today" figures without a precise as-of date or full methodology
  note in the fetched text, and without the market-definition footnotes
  AER-785 provides. Treat the ~2021 row as **directionally credible but
  lower-confidence** than the AER-785 rows until cross-checked against a
  USDA AMS Packers and Stockyards annual report or the peer-reviewed
  Schaefer et al. update (see Pending below).

**Verdict on the oft-repeated "four firms control ~80-85% of beef
processing" claim**: **Supported, with a caveat on precision.** The 80–85%
range is consistent across a 1997 USDA/GIPSA figure (80% for steer/heifer
procurement, 83% for boxed beef output) and a 2021 White House figure (82%),
using the same "top four firms' share of steer/heifer slaughter or
procurement" market definition each time. It is **not** a claim about all
beef-industry revenue, retail beef sales, or the full cattle industry
(which includes many small feeders and cow-calf producers upstream who are
not part of the "market" being measured). The specific "four firms" named in
current commentary — JBS, Tyson, Cargill, National Beef — is consistent with
industry-recognized "Big Four" packer identity, though this fork did not
independently re-verify each company's individual share.

## Poultry is structurally different, and USDA's own framing says so

USDA ERS's own historical assessment (AER-785, Chapter 3) is explicit:
*"Market concentration in hog, chicken, and turkey slaughter is not
particularly high when compared with other manufacturing industries... Of
the four classes, only cattle could be described as having unusually high
concentration today, when compared with other manufacturing classes"*
(footnote 11: "About 10 percent of U.S. manufacturing industries are more
concentrated than cattle slaughter, while the other three slaughter classes
are close to the mean for manufacturing" — as of the report's ~1992-1997
data). This is a useful check against loosely combining "beef, pork, and
poultry are all highly concentrated" into one undifferentiated claim — beef
concentration is the outlier in both level and rate of increase; poultry's
~54% CR4 (2021) is a real rise from ~35% (1986) but is a different order of
concentration than beef's ~82-85%, even though poultry is *more* vertically
integrated in the ownership sense (see `NOTES/Commodity_Structure_
Comparison.md`) — concentration among processing firms and vertical
integration of the supply chain are different axes and poultry scores high
on one, moderate on the other, while beef is the reverse.

## Concentration ≠ proven anticompetitive conduct — but there is real
litigation/enforcement history worth tracking separately

Concentration figures describe market structure; they are not themselves a
finding of anticompetitive conduct. Separately and factually, U.S. beef and
pork/chicken processors have faced antitrust litigation and settlements in
recent years (e.g., civil litigation alleging price-fixing/information-
sharing in beef and in broiler chicken production) — this fork did not
verify specific case names, docket numbers, or settlement amounts against
primary court filings; that is flagged as **Pending** and should be picked
up by whichever research pass covers Section 5's "distinguish... from
anticompetitive conduct" instruction in more depth, or Section 13's
claim-by-claim fact-check. Do not cite specific case outcomes from this memo
without independent verification.

## Fact-check verdicts (Section 13, claims #3, #14, #15)

See `NOTES/Claim_Fact_Check_Concentration_Draft.md` for the full write-up.
Summary:
- **#3 (has concentration increased/decreased/stable):** Supported —
  increased, sharply for beef, moderately for pork and poultry, per two
  independent primary sources bracketing 1980–2021.
- **#14 (processors/retailers benefit disproportionately from supply
  disruptions):** Unresolved on the evidence gathered so far — the White
  House CEA blog asserts pandemic-era processor profit increases (with
  specific dollar figures for JBS/Tyson dividends/buybacks) but this fork
  did not independently verify those figures against SEC filings/10-Ks, and
  a political-office blog post is not, by itself, sufficient primary
  verification for a claim this specific. Needs a follow-up pass against
  actual 10-K/earnings-call data (Section 4/Section 13 territory).
- **#15 ("food monopolies" vs. "highly concentrated supply chains"):**
  Partially supported toward "highly concentrated supply chains" as the more
  defensible term — none of the three sectors shows CR4 near 100% or a
  single dominant firm (i.e., not monopoly in the technical sense), and
  "oligopoly" or "concentrated" is the terminologically correct description
  given 3-4 major firms per sector. "Food monopolies" is loose/inaccurate
  as a technical term but is common shorthand in political and advocacy
  discourse — worth noting as a *discourse* fact (how the term gets used) for
  Study 1, separate from whether it's the economically correct term.

## Pending / needs a follow-up research pass
- Current (2022–2024) CR4/HHI directly from a USDA AMS Packers and
  Stockyards Division annual report (a 2021/2022 combined report exists per
  search results but was not fetched/verified this pass).
- The peer-reviewed update: Schaefer, ... et al., "Consolidation and
  Concentration in U.S. Meat Processing: Updated Measures Using Plant-Level
  Data," *Review of Industrial Organization* (2024) — abstract-level
  description found (uses FSIS plant-level data over ~30 years, computes HHI
  and CR ratios by firm share of monetary value), but the article is
  paywalled (Springer redirect to login) and the USDA working-paper PDF
  version returned HTTP 403 on direct fetch. **Do not cite specific HHI
  numbers from this paper until someone with journal/library access pulls
  the actual figures** — right now we only know it exists and roughly what
  it measures, not what it found.
- Grocery retail concentration (mentioned as optional in the brief) — not
  researched this pass.
- Specific antitrust litigation/settlement history (beef price-fixing MDL,
  broiler chicken antitrust litigation) — not verified this pass; treat any
  existing claims about these in other project files as unverified until
  checked against court filings or DOJ/FTC primary releases.
