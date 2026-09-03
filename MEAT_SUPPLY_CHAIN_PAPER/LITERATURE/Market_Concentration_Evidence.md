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

## Update 2026-09-03 (via Consensus.app Deep Research) — current 2019
figures found, and a correction to the poultry characterization below

The peer-reviewed successor to AER-785 — Schaefer et al., "Consolidation
and Concentration in U.S. Meat Processing: Updated Measures Using
Plant-Level Data," *Review of Industrial Organization* (2024) — was
previously "Pending" (paywalled). Its figures are now available via
convergent secondary corroboration (Saitone 2023/2025 and MacDonald 2023,
both citing the Schaefer work directly; the original paper itself still
has not been independently WebFetched — see
`SOURCE_VERIFICATION/Evidence_Table.md` for full sourcing detail):

| Commodity | CR4, 2019 (Schaefer et al., FSIS plant-level data) |
|---|---|
| Beef (steer/heifer) | **85%** |
| Pork (hogs) | **67%** |
| Poultry (broilers) | **78%**, up from 48% in the 1980s |

Plant-level detail: the 22 largest beef plants (3.3% of all federally
inspected plants) processed 71.7% of cattle. Decomposition: absent
1991–2019 *consolidation specifically* (M&A activity, as opposed to organic
capacity growth or new entry), poultry CR4 would be an estimated 60%
instead of 78% — i.e., roughly half of poultry's concentration rise since
1991 is attributable to consolidation.

**This corrects the "poultry is not particularly high" framing below.**
That framing came from AER-785's 1992–97 data and a 54% (2021) CEA
estimate. The updated 78% (2019) figure is well above both, and poultry
may now be closer to pork's concentration level than to a genuinely modest
reading — the *direction* of the paper's earlier claim (poultry rose from a
lower base and later than beef) still holds, but the *current magnitude*
claim ("poultry concentration isn't particularly high") no longer holds
without qualification and should not be repeated as-is in the manuscript.

**A methodologically important addition:** national CR4/HHI figures
(including all of the above) can mask much higher **regional/local
procurement-market** concentration — because live animals lose value over
long-distance transport, the actual competitive set a given rancher faces
when selling may be just 2–3 firms even where the national market shows
4+. This regional-market point is arguably the strongest single piece of
evidence in this project's whole evidence base for a genuine monopsony
concern, stronger than any national-level CR4 number, and deserves its own
follow-up pull directly from Schaefer et al.'s regional mapping.

**A counterweight, also newly found:** concentration is not tightly linked
to proven market-power exploitation. Plant-level cost analysis of U.S. beef
packing (Paul, 2001) finds little evidence of market power, with apparent
effects better explained by cost efficiencies (utilization, scope
economies); a bilateral oligopoly model (Tostão, 2005) similarly finds
cost-efficiency gains dominate market-power effects from increased
concentration. Both studies predate the 2015–2019 concentration rise and
litigation below, so don't treat them as settling the current-period
question — but they're a real, citable caution against assuming
concentration automatically implies harm.

**Measurement caution:** CR4 and HHI "lack the value-validity property"
(Kvålseth 2018/2021/2022) — their numeric values aren't directly comparable
as precise representations of real concentration differences, the two
measures have no exact functional relationship, and incomplete
market-share data can distort HHI specifically. Don't treat this project's
various CR4/HHI figures (sourced from AER-785, the CEA blog, and now
Schaefer et al.) as more precisely comparable across sources than they are.

## Poultry is structurally different, and USDA's own framing says so
**(see the 2026-09-03 update above — the magnitude claim in this section is
now superseded by the 78% (2019) CR4 figure; keeping this section for the
historical trajectory and the vertical-integration point, which still
hold)**

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
finding of anticompetitive conduct.

**Update 2026-09-03 (via Consensus.app Deep Research) — partially
resolved.** Real litigation is now confirmed: **2019 antitrust lawsuits
alleged the four largest U.S. beef packers (Tyson, JBS, Cargill, National
Beef) engaged in fed-cattle price-fixing collusion under Sherman Act §1;
the case settled with the packers issuing statements of no wrongdoing.**
Evidence on whether actual collusive *behavior* occurred is genuinely
mixed, not one-sided:
- **For a behavioral/pricing-regime shift:** Bolotova (2021) finds
  wholesale beef pricing shifted from patterns consistent with competitive
  pricing (2010–2014) to patterns consistent with oligopoly/monopoly
  pricing during 2015–2019 specifically — the alleged collusion window —
  with farm sector value share falling and marketing margins rising in
  that period.
- **Against a behavioral shift:** Parcell & Franken (2026), an event-study
  using error-correction VAR on the same period, find only slight,
  economically unimportant change in price-adjustment speed — i.e., no
  strong econometric signature of altered collusive behavior in that
  specific test.
- These are not strictly contradictory (one tests the pricing *regime*,
  the other tests *adjustment speed*), but they point in different
  directions and should be presented together in the manuscript, not
  cherry-picked to support either a "concentration caused collusion" or
  "no real effect" narrative.
- Full citations for Bolotova (2021), Blair (2023, the structural/industry
  review citing ~85% CR4 as facilitating collusion), and Parcell & Franken
  (2026) still need to be independently pinned down and WebFetched before
  manuscript use — currently sourced via Consensus.app's AI synthesis, not
  a direct read of any of the three papers.

## Fact-check verdicts (Section 13, claims #3, #14, #15)

See `NOTES/Claim_Fact_Check_Concentration_Draft.md` for the full write-up.
Summary:
- **#3 (has concentration increased/decreased/stable):** Supported —
  increased, sharply for beef, moderately for pork and poultry, per two
  independent primary sources bracketing 1980–2021.
- **#14 (processors/retailers benefit disproportionately from supply
  disruptions):** Upgraded to **Partially supported** (2026-09-03). The
  White House CEA blog's specific JBS/Tyson dollar figures are still not
  independently verified against SEC filings/10-Ks. But COVID-19 brought
  ~40% of processing capacity offline (Lusk 2020), producing an
  "unprecedented widening" of farm-to-wholesale spreads — corroborating and
  quantifying the existing 2020 packer-margin-widening evidence
  (`LITERATURE/Price_Transmission_Literature.md` §4) with a concrete
  magnitude. Separately, real 2019 antitrust litigation and mixed
  behavioral evidence (Bolotova 2021 vs. Parcell & Franken 2026, above)
  bear on a related but distinct question (collusion, not disruption-period
  margin capture specifically).
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
  search results but was not fetched/verified this pass) — would extend
  past the Schaefer et al. 2019 point estimate.
- Independent full-text read of Schaefer et al. (2024) itself, still not
  directly WebFetched — current 2019 figures are via convergent secondary
  corroboration (Saitone, MacDonald), which is reasonably high-confidence
  but not the same as reading the source.
- Full citations (journal, volume, complete author lists) for Bolotova
  (2021), Blair (2023), and Parcell & Franken (2026) — found via
  Consensus.app Deep Research 2026-09-03 but not yet independently pinned
  down or WebFetched.
- Grocery retail concentration (mentioned as optional in the brief) — not
  researched this pass.
- The regional/local procurement-market concentration mapping (Schaefer et
  al., via MacDonald 2023) — flagged above as the single strongest
  monopsony-relevant finding in the evidence base, worth its own dedicated
  follow-up pull rather than staying at secondary-corroboration confidence.
