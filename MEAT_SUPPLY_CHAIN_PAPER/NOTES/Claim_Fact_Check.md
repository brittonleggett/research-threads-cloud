# Claim Fact-Check (Section 13) — Consolidated

Status: consolidated 2026-09-03 from four parallel research passes (concentration/
structure, imports, COOL timeline, price transmission). Verdict scale:
**Supported / Partially supported / Unsupported / Misleading without context
/ Unresolved.** Source detail and full citations for each claim live in the
individual fork drafts (`Claim_Fact_Check_Concentration_Draft.md`,
`Claim_Fact_Check_Imports_Draft.md`, `Claim_Fact_Check_COOL_Draft.md`,
`Claim_Fact_Check_PriceTransmission_Draft.md`, kept as the detailed backing
for each verdict below) and in `SOURCE_VERIFICATION/Evidence_Table.md`. This
file is the short-form summary the rest of the project (especially
`PROJECT_STATUS.md`) should cite.

| # | Claim | Verdict | One-line basis |
|---|---|---|---|
| 1 | Are U.S. cattle producers receiving historically weak returns while consumers face historically high beef prices? | **Partially supported / Misleading without context** (upgraded 2026-09-09 — multi-decade series now pulled) | **2026-09-09: full 1970-present USDA ERS Meat Price Spreads series pulled directly** (`DATA/USDA_ERS_Historical_Meat_Price_Spreads_1970-present.csv`, see `NOTES/2026-09-09-meat-price-spreads-historical-farm-share-analysis.md`). Beef farmers' share of the retail dollar fell from a 1970s decade-average of 63.6% to a 2000s low of 46.1%, then partially recovered (48.1% in the 2010s, 44.4% avg 2020s but with a sharp 2023-2025 rebound to 53.5%) — a real long-run decline, but the *current* period (2023-2025) is the best 3-year run in the 55-year series, the opposite of "increasingly squeezed" right now. Pork's decline is steeper and has not reversed (53.7%→22.6%, 1970s→2020s). Verdict: the long-run "declining farmer share" claim has real historical grounding for both commodities; the "currently/still worsening" version is false for beef specifically (true-ish for pork, which remains flat near its historic low). Not yet inflation-adjusted in absolute-dollar terms — the analysis is share-of-retail-dollar, not real income. |
| 2 | How much of the retail beef dollar goes to farmers/ranchers vs. processors/retailers, and how has that changed? | **Partially supported**, strong "misleading without context" flag (decade-trend context added 2026-09-13) | The popular "~6 cents of the food dollar" figure is real but is an *all-food* statistic (5.9→5.8 cents, 2023→2024); the beef-specific ERS Meat Price Spreads farm share is 49.8→52.2 cents, ~10x higher and rising. Conflating the two is a common, identifiable error. **2026-09-09 full 1970-present pull adds the longer trend** (see `NOTES/2026-09-09-meat-price-spreads-historical-farm-share-analysis.md` and Claim #1 above): beef's decade-average farm share fell 63.6%→46.1% (1970s→2000s) before partially recovering to 44.4% (2020s avg, but 53.5% in 2025 alone — the best 3-year run in the 55-year series). Pork fell further and has not recovered: 53.7%→22.6% (1970s→2020s). So the single-year 2023→2024 uptick this row was originally based on is real but was, on its own, too short a window to characterize the trend — it's the leading edge of a genuine multi-year beef-specific rebound sitting inside a much longer-run decline, not a one-off blip, and pork is not participating in it. |
| 3 | Has meatpacking concentration increased, decreased, or remained stable? | **Supported** (increased over the long run, 1963→2019; but flat-to-slightly-declining 2019→2021 per the single most authoritative source now checked) | **2026-09-05 update — official USDA AMS Packers and Stockyards Division (PSD) Annual Report to Congress (2021/2022, full text read directly) is now the best-verified current-period source and materially revises the picture:** steer/heifer CR4 was **85% (2019) → 81% (2020) → 81% (2021)** — a *decline* from 2019, which PSD attributes to COVID-19 disruption at major plants, not a continued rise; hogs **67% (2019) → 64% (2020) → 65% (2021)**; broilers **53% (2019) → 53% (2020) → 55% (2021)**; turkeys 55%/55%/55%. Beef's *long-run* rise (36%→80%, 1980–1997, AER-785) remains a documented historical outlier and is unaffected by this update. **Unresolved discrepancy, not smoothed over:** the project's prior "poultry 78% (2019)" figure (attributed to Schaefer et al. via an AI-search synthesis, never independently read) is flatly contradicted by PSD's own official 2019 broiler figure of 53%. PSD and Schaefer et al. may use different market/plant definitions, but since Schaefer et al. itself is still unread (paywalled), do not use "78%" for poultry anywhere in the manuscript — use PSD's directly-verified 53-55% instead, and treat poultry as the least-concentrated of the three commodities again, consistent with AER-785's original framing. See `SOURCE_VERIFICATION/Evidence_Table_Concentration.md` for the full table (2012-2021) and HHI figures. |
| 4 | Are processor profit margins unusually high during periods of elevated food inflation? | **Partially supported**, strongest for the 2020 COVID shock specifically, not general inflation periods | Balagtas & Cooper (2021) and Erol & Saghaian (2022) triangulate on margin widening during the 2020 disruption; the broader 2021–2023 inflation episode not separately examined yet. **2026-09-05: now also directly confirmed by both companies' own audited SEC segment data** — Tyson's Beef segment operating margin rose 6.6%→10.0%→18.0% (FY2019→FY2020→FY2021) and Tyson's own 10-K attributes the FY2020 rise explicitly to "COVID-19 disruptions, which increased the spread between preexisting contractual agreements and the cost of fed cattle"; JBS USA's Beef North America segment Adjusted EBITDA margin rose ~13.1%→~21.3% (2020→2021). Margins fell back sharply afterward (Tyson Beef 12.6% FY2022, -0.5% FY2023), consistent with a temporary shock effect, not a permanent margin shift. See Claim #14 and `SOURCE_VERIFICATION/Evidence_Table_Concentration.md`. |
| 5 | Do increases in cattle prices transmit differently to consumers than decreases (asymmetric price transmission)? | **Unresolved / genuinely contested** | Older/BLS-price-based studies find asymmetry; the most methodologically current beef study (Pozo, Bachmeier & Schroeder 2021, scanner data) finds none. Split tracks data source, not just researcher disagreement. **2026-09-05: GAO-02-246 (full text now read directly) independently confirms the contestedness itself is long-standing** — as of 2002, GIPSA's own 1996 literature review was "inconclusive concerning the effects of concentration" on cattle prices, and GAO's 40-expert panel was split on the importance of structural change/imports vs. domestic supply-demand fundamentals. This doesn't resolve the asymmetry question but corroborates, from an independent 2002 government audit, that the mechanism has never been settled — it isn't just a newer-vs-older-data artifact. |
| 6 | Do foreign beef imports actually lower retail beef prices? | **Misleading without context** | 2024 beef imports hit a record (+24% YoY) at the same time cattle herd hit a 1951-low and prices hit records — imports and prices rose together. Imports likely keep prices lower than a no-import counterfactual, but have not produced falling/flat prices in the current period. |
| 7 | Do imports materially suppress domestic cattle prices? | **Unresolved for the current (2020s) import environment; Partially supported / small-magnitude for the historical NAFTA-era (1990s) Canada-specific case, now with real quantitative estimates (upgraded 2026-09-24)** | **2026-09-05: GAO-02-246 full text obtained and read directly** (previously blocked by unreadable PDF stream — resolved by installing local PDF-text-extraction tooling). GAO found that neither USDA's livestock model nor ITC's trade models were designed to isolate the price effect of imports from market concentration/contracting; GIPSA's own 1996 review of the concentration literature was inconclusive; and GAO's expert panel rated domestic supply/demand as more important than international trade for cattle prices, with real disagreement on trade's magnitude. The report states the *theoretical direction* (more beef imports → lower beef prices → lower derived demand for cattle → lower cattle prices) but this is modeled reasoning, not an estimated empirical magnitude for the U.S. Current period (2024) shows imports and cattle/beef prices moving together, the opposite of a simple suppression story. **2026-09-24: a real primary-source econometric estimate now exists, closing part of the "no verified magnitude" gap flagged above** — USITC Publication 3048 ("Cattle and Beef: Impact of the NAFTA and Uruguay Round Agreements on U.S. Trade," Investigation No. 332-371, July 1997) read in full directly (10,761-line extracted text). It cites Marsh & Greer (1994): 1993-94 Canadian LCFS/beef exports lowered U.S. steer prices by ~$2/cwt (<0.3%); a companion study (Marsh & Peck 1996) found a similarly minor feeder-cattle effect. A separate, independently-located working paper by the same MSU research group — Brester & Marsh (1999) — found ~$0.35/cwt of an $8/cwt 1990s price decline (≈4.4%, ≈$4.20/head) attributable to increased Canadian imports (found via RePEc's bibliographic record; the primary PDF itself returned HTTP 202/empty on two access attempts, so this one figure is secondary-sourced, not directly read). All three estimates converge on a small-but-nonzero magnitude (well under 5% of observed price movements) for Canada specifically in the NAFTA era — a real, if dated and geographically narrow, answer to what was previously a total evidence gap. **What remains genuinely unresolved**: none of these estimates cover the current (2020s) import mix, which is now dominated by Australia and Brazil rather than Canada, under a record-low domestic cattle herd — a structurally different situation from the 1990s NAFTA-era Canada/Mexico trade these studies model. No 2020s-era equivalent econometric estimate was found. Treat "imports modestly suppress cattle prices, historically in the low single digits or less, for Canada specifically in the 1990s" as now evidence-backed; treat any claim about the magnitude of today's import effect as still unresolved. See `NOTES/2026-09-24-litigation-recheck-usitc-import-price-effect-schaefer-review.md` and `SOURCE_VERIFICATION/Evidence_Table_Imports.md`. |
| 8 | Why does the U.S. import beef while simultaneously exporting beef? | **Supported** | Intra-industry trade by cut/quality: imports are mostly lean trim (for ground beef); exports are mostly premium marbled cuts to Japan/Korea/Mexico. Not a sign of insufficient aggregate production. |
| 9 | Is imported beef commonly blended into ground beef sold in the United States? | **Supported** | Directly stated by USDA ERS: a majority of beef imports are destined for blending fatty domestic trim with lean imported trim. One of the most solidly verified claims in the project. |
| 10 | Can consumers currently determine whether beef came from an animal born, raised, slaughtered, and processed in the United States? | **Partially supported** (context-dependent) | Only if the package carries a voluntary "Product of USA" claim meeting the post-Jan-1-2026-compliance FSIS standard; no mandatory disclosure exists for beef/pork since Dec. 2015. Absent that claim, no. |
| 11 | How have country-of-origin labeling laws changed? (Is the common belief about current COOL protections accurate?) | **Unsupported**, as commonly believed (verdict unchanged 2026-09-17, but see live legislative-status caveat) | Mandatory COOL for beef/pork was repealed Dec. 2015 (P.L. 114-113) after a WTO loss to Canada/Mexico — over a decade ago. Mandatory COOL persists for lamb, chicken, goat, venison, seafood, and others, so "COOL was repealed" as a blanket statement is also an oversimplification. **2026-09-17: this remains factually correct today — no bill has been enacted — but a bipartisan Senate effort to restore mandatory COOL for beef is actively moving**: Sen. Thune's American Beef Labeling Act (S.421) amendment passed Senate Agriculture Committee markup Aug. 6, 2026 (reported as 17-6 by most trade outlets, 16-7 by one — an unresolved minor discrepancy between sources), and the full Senate farm bill ("Agricultural Act of 2026") containing it was reported out of committee Sept. 16, 2026 on a 12-11 party-line vote, headed to a full Senate floor vote expected after the November 2026 midterms. Secondary-sourced only (multiple consistent trade-press outlets plus one official Thune press release); congress.gov and the Senate Ag Committee's own site both blocked automated fetches, so no primary bill/vote text was independently read. Do not treat this as changed law — it isn't yet — but any manuscript language should be written knowing this could move before publication. See `NOTES/2026-09-17-agristats-broiler-final-approval-mcool-farmbill-scouting.md` for full detail. **2026-09-19 update on the vote-count discrepancy**: still not primary-resolved (agriculture.senate.gov and congress.gov both blocked again on retry), but reading the underlying articles directly (not just search snippets) sharpens it — two independent, contemporaneous (Aug. 6-7, 2026) reports (Capital Press; DTN/Progressive Farmer's own original article) give **17-6** with a named, internally-consistent senator-by-senator breakdown (6 Republicans yes, 6 Republicans no including Chairman Boozman, all Democrats yes), while the sole **16-7** figure traces to one later (Sept. 17, 2026) DTN *Washington Insider* piece with no supporting detail. Evidence now leans clearly toward 17-6, though this remains short of a primary committee-record confirmation. See `NOTES/2026-09-19-pork-mdl-primary-docs-mcool-vote-doj-probe-corroboration.md`. |
| 12 | Is there evidence processors or retailers benefit disproportionately from supply disruptions? | **Supported**, for the 2020 COVID disruption specifically (beef) | Three independent sources (Balagtas & Cooper 2021; Erol & Saghaian 2022; Cooper et al. 2023, confidential USDA plant-level data) triangulate on margin widening during the April–May 2020 shock. Do not generalize beyond that episode. |
| 13 | Are similar dynamics present in pork? | **Supported** (upgraded 2026-09-15 — pork-specific COVID-margin evidence now confirmed) | Pork farm share also rose 2023→2024 (22.1→23.7 cents), paralleling beef. More of the pork price-transmission literature finds asymmetry than the newest beef study does, but findings aren't unanimous within pork either. **2026-09-15: the pork-specific COVID-margin follow-up flagged below is now resolved** — Balagtas & Cooper (2021, *Choices*), re-fetched directly, has a figure explicitly titled "COVID-19 is Associated with a Spike in the Wholesale-Farm Price Margins for Beef **and Pork**," i.e. the margin-widening finding already anchoring the beef claim (#12) is not beef-only in this same primary source. The article's farm-price data also shows the 2020 shock hit hogs at least as hard as cattle: USDA's projected barrow/gilt price fell 20.9% (Jan-May 2020) vs. 11.4% for steers, and pork-packing capacity utilization bottomed at 54% (April 29, 2020) before recovering to ~95% by mid-June. |
| 14 | Is there evidence processors or retailers benefit disproportionately from supply disruptions? *(concentration-fork's general/cross-period read, vs. #12's COVID-specific read)* | **Supported for beef and pork specifically during the 2020-2021 COVID disruption window (upgraded 2026-09-05 with direct SEC-filed audited data); commodity-specific — does not extend cleanly to poultry** | **2026-09-05: resolved via Tyson Foods' own 10-K filings (FY2019-FY2023) and JBS USA's SEC-filed segment data (2020-2022), both read directly from primary filings — no longer resting on the unverified White House CEA figures.** Tyson Beef segment operating margin: 6.6% (FY19) → 10.0% (FY20) → **18.0% (FY21)** → 12.6% (FY22) → -0.5%, loss (FY23); Tyson's own MD&A attributes the FY20-21 rise to COVID-19 disruptions widening "the spread between preexisting contractual agreements and the cost of fed cattle." JBS USA's Beef North America segment: Adjusted EBITDA margin ~13.1% (2020) → **~21.3% (2021)**, then roughly halved in 2022 as cattle costs rose. Tyson Pork showed the same pattern less dramatically (5.3%→11.0%→5.2%, FY19-21); JBS Pork USA's margin was comparatively flat (10.4%→10.5%, 2020-21). **Poultry did not show the same pattern**: Tyson Chicken margin was 4.7% (FY19) → 0.9% (FY20) → -4.6% (FY21, driven substantially by a $626M one-time price-fixing legal-settlement accrual, not market conditions); JBS's Pilgrim's Pride segment rose only modestly (9.5%→11.5%, 2020-21). The official USDA AMS Packers and Stockyards Division Annual Report to Congress independently states, in its own voice (not an advocacy source), that "beef packers continued to earn record profits in 2021." Separately, 2019-2022 saw an extensive wave of DOJ criminal and civil price-fixing actions across beef, pork, AND poultry (Pilgrim's Pride pleaded guilty and paid a $107.9M federal fine in Feb. 2021 for chicken price-fixing; Tyson, JBS, Cargill, National Beef face civil beef-price-fixing suits; Smithfield paid ~$200M in 2022 pork settlements) — see Claim #15 and `SOURCE_VERIFICATION/Evidence_Table_Concentration.md` for the full list. Bolotova (2021, structural pricing-regime shift 2015-2019) and Parcell & Franken (2026, event-study finding little change in price-adjustment speed over the same window) remain a genuine, unreconciled split on a *different* (pre-COVID) question — present both, not just one. |
| 15 | Are claims about "food monopolies" supported by the empirical literature, or would "highly concentrated supply chains" be more defensible terminology? | **Partially supported** toward "highly concentrated" | No sector shows single-firm monopoly in the technical sense; all show 3–4 major competing firms with CR4 well under 100%. "Oligopoly"/"concentrated"/"monopsony concern" are the technically precise terms; "monopoly" functions as political/advocacy shorthand, not a technically accurate claim — itself useful Study 1 framing-analysis material. **Update 2026-09-03:** real Sherman Act §1 collusion litigation (see Claim #14) and a peer-reviewed structural finding of an oligopoly/monopoly-consistent pricing shift in 2015–2019 (Bolotova 2021) mean "oligopoly" specifically — not just "concentrated" — has direct empirical/legal grounding for beef in that period, strengthening the case for precise IO terminology over "monopoly" without needing to invoke the looser popular term at all. **Update 2026-09-05 (USDA AMS PSD Annual Report to Congress, read directly):** the price-fixing evidence is broader than previously documented and spans all three commodities, not just beef — Pilgrim's Pride *pleaded guilty* to a federal criminal charge of chicken-price-fixing conspiracy (Feb. 2021, $107.9M DOJ fine) and separately paid $75M and $110.5M in related settlements; Tyson settled turkey and poultry price-fixing claims (multiple, 2021); JBS agreed to pay $52.5M (beef, 2022) and $20M (pork, 2022); Smithfield agreed to ~$200M combined in pork price-fixing settlements (2022); Cargill/Sanderson Farms/Wayne Farms paid $84.8M (2022) for a labor-market wage-suppression conspiracy (a related but distinct anticompetitive-conduct category, not price-fixing on output). A guilty plea to a federal criminal antitrust charge (Pilgrim's Pride) is categorically stronger evidence of actual anticompetitive conduct than the beef case's civil settlements-with-no-wrongdoing-admission — this is a real commodity-specific asymmetry worth preserving in the manuscript rather than treating "meat industry price-fixing" as a single undifferentiated fact pattern. **2026-09-17 addition, not yet independently verified against a primary document:** a separate, private End-User Consumer pork-antitrust MDL settlement of **$117.065M combined across five processors — Tyson ($85M), Clemens ($13.5M), Seaboard ($10M), Hormel ($4.465M), Triumph ($4.1M)** — was preliminarily approved July 31, 2026, per consistent claims-administrator/trade-press coverage (not independently read in full). This is a *different, later* wave of pork defendants than the already-verified Smithfield (~$200M) and JBS ($20M) pork settlements already in this row — both are real, not duplicates of each other. The same coverage states Agri Stats also has a pork-track settlement, behavioral-only like its chicken/turkey settlements (no cash) — consistent with, not a new fact beyond, the pattern already documented for Agri Stats elsewhere in this project. See `NOTES/2026-09-17-agristats-broiler-final-approval-mcool-farmbill-scouting.md`. **2026-09-19 update — primary court documents read directly, one real correction:** the case is *In re Pork Antitrust Litigation*, No. 18-1776 (JRT/JFD), D. Minn. (Doc. 3436, filed 7/31/26, read in full). July 31, 2026 was **not** the preliminary-approval date — it's when the Court approved sending class notice for five settlements that had each already been preliminarily approved individually, on different dates: Hormel (7/9/24), Seaboard (8/6/24), Clemens (6/13/25), Tyson (11/7/25), Triumph+Agri Stats bundled (5/5/26). The $117.065M total and per-company figures are unaffected and confirmed consistent with the primary order's own class/schedule details. Also: the correct official class name in this MDL is **"Consumer Indirect Purchaser Plaintiffs,"** not "End-User Consumer" (that label belongs to the broiler-chicken MDL's own, differently-named class — a cross-case terminology trap now flagged). **New, not previously tracked**: a *separate* pork-specific **Direct Purchaser Plaintiff** settlement with Agri Stats (Doc. 3472, filed 9/10/26, read in full) reached **final approval on September 10, 2026** — the same day as DOJ's own civil Agri Stats Final Judgment. Agri Stats has now resolved four distinct litigation tracks (DOJ civil case, broiler End-User Consumer, pork Consumer IPP, pork DPP) within about six weeks of each other, all on broadly similar behavioral/no-admission terms as far as directly read — this order itself states no dollar figure, consistent with but not proof of "no cash." See `NOTES/2026-09-19-pork-mdl-primary-docs-mcool-vote-doj-probe-corroboration.md`. |

## Cross-cutting notes for `PROJECT_STATUS.md`

- **Note claims #12 and #14 overlap** (both ask about disruption-period
  processor/retailer benefit) but were researched independently by two
  forks with different evidence bases and landed at different verdicts
  (#12 Supported for COVID-2020 specifically via academic sources; #14
  Unresolved because it rests on unverified political-blog company
  figures). This is not a contradiction — it shows the same underlying
  question can be Supported when tested against peer-reviewed sources and
  Unresolved when tested against a specific advocacy source's specific
  numbers. Keep both rows rather than collapsing them; the gap itself is
  informative about source-quality standards.
- Claim #5 remains genuinely **Unresolved** and should not be used as a
  settled fact in any manuscript draft. Claim #7 was **partially advanced
  2026-09-24** — real quantitative estimates now exist for the historical
  (1990s, Canada-specific) case, but the current-era (2020s, Australia/Brazil-
  dominated) magnitude remains unresolved; see claim #7's row for the split
  verdict.
- The single most load-bearing corrective finding across the whole
  fact-check: **the "~6 cents of the food dollar" statistic is real but is
  not a beef/pork-specific number**, and the actual beef/pork-specific farm
  share is roughly 10x higher and rose, not fell, in the most recent year.
  This alone substantially reframes the brief's motivating tension — see
  `NOTES/Research_Problem_Exploration.md`.

## Follow-ups flagged across all four passes

**Resolved 2026-09-05** (see `NOTES/2026-09-05-primary-source-retry-pass.md`
for full method/detail):
- ~~GAO-02-246 (PDF extraction failed)~~ — resolved by installing
  `poppler-utils` locally and extracting text directly; full report read.
  Bears on claims #1, #5, #7.
- ~~Erol & Saghaian (2022) full text (paywalled, relied on abstract)~~ —
  MDPI itself stayed bot-blocked (403), but the authors' own AAEA 2022
  conference poster (same title, same findings, hosted open-access on
  AgEconSearch) was retrieved via direct `curl` with a browser user-agent
  and read in full. Bears on claims #4, #5, #12, #13.
- ~~Federal Register COOL/labeling rules (bot-blocked)~~ — resolved via
  federalregister.gov's own public JSON/XML API endpoints (bypasses the
  interstitial the HTML page serves to automated fetchers). Full primary
  regulatory text of the 2024-05479 "Product of USA" rule now read directly.
- ~~Pull actual SEC 10-K/earnings-call margin data for Tyson and JBS
  (2019–2023)~~ — Tyson: fully resolved via its own FY2021 and FY2023 10-Ks
  (SEC EDGAR), FY2019-FY2023 segment data for Beef/Pork/Chicken/Prepared
  Foods. JBS: resolved via a 2023 SEC Form F-4 registration statement
  (Beef North America, Pork USA, Pilgrim's Pride segments, 2020-2022) —
  JBS does not currently file 10-Ks (no exact 10-K/20-F equivalent located
  for the full 2019-2023 window; the F-4 covers 2020-2022 only). See Claim
  #14 and the Evidence Table for figures.
- **New primary source pulled and read in full, not previously attempted**:
  USDA AMS Packers and Stockyards Division 2021/2022 Annual Report to
  Congress (PDF, direct `curl` fetch + local text extraction) — supersedes
  the White House CEA blog as the concentration-figure anchor per
  `PROJECT_STATUS.md`'s own instruction, and surfaces a real, unresolved
  discrepancy with the previously-adopted "poultry 78% (2019)" figure (see
  claim #3) plus an extensive list of 2020-2022 DOJ/civil price-fixing
  actions across all three commodities (see claim #15).

**Still open / genuinely blocked:**
- Pull the full USDA ERS Meat Price Spreads historical time series (1970–
  present) directly rather than relying on a two-year secondary summary
  (needed for claim #1's "historically weak" framing). Not attempted this
  pass — out of tonight's scope.
- **Still blocked, but materially advanced 2026-09-07**: Schaefer et al.
  (2024, *Review of Industrial Organization*) itself remains genuinely
  paywalled (Springer login wall; the USDA-hosted preprint mirror that
  worked as recently as it was found is now also 403ing; Wayback/
  archive.org is blocked by this environment's egress policy; ResearchGate
  403s). **However, a 2025 companion paper by the same core author team
  (Saitone, Schaefer, Scheitrum, Arita, Breneman, Nemec Boehm — identical to
  five of the RIO 2024 paper's authors), "Consolidation, productivity, and
  downstream prices in the US poultry industry" (*Agricultural and Resource
  Economics Review* 54, 2025, open-access CC-BY, Cambridge Core), was found
  and read in full, and independently confirms the exact "78%" 2019 broiler
  CR4 figure verbatim** ("In 2019, the CR-4 for the US poultry industry was
  0.78"), plus the "60% absent 1991-2019 consolidation" counterfactual —
  so the number itself is a real, directly-verified figure from this
  author team, not a fabrication or a Consensus.app artifact. Critically,
  this paper's own methodology section states it is built on **NETS
  (National Establishment Time-Series) data — a private, D&B/DUNS-based
  ownership and sales database — not USDA/FSIS federally-inspected
  slaughter-volume data**, whereas the RIO 2024 abstract (independently
  confirmed via multiple search-engine syntheses of its abstract, though
  the abstract itself still hasn't been read primary) states *that* paper
  uses "annual plant-level food safety and inspection service (FSIS) data"
  — the same data family USDA AMS PSD's own official CR4s are built from.
  **Working hypothesis, not yet confirmed by a direct read of RIO 2024
  itself: the "78%" figure may have been correctly reported by Consensus.app
  but mis-attributed to the wrong paper** — i.e., it may belong to this NETS-
  based 2025 poultry-specific companion piece rather than to the FSIS-based
  RIO 2024 meat-processing paper the project actually cited, which would
  mean RIO 2024's own broiler CR4 is plausibly much closer to PSD's 53-55%.
  This would resolve the discrepancy as a citation mix-up rather than a
  genuine factual contradiction between two data sources — but this is
  still a hypothesis, not a resolution, since RIO 2024's own broiler figure
  has still not been independently read. **Do not use "78%" for poultry in
  the manuscript regardless of this finding** — see PROJECT_STATUS.md Open
  Decision #6, updated 2026-09-07, and
  `NOTES/2026-09-07-schaefer-pozo-idea28-followup.md` for the full chain of
  reasoning and every channel attempted.
- Meat Institute rebuttal page (403 all three sessions now, including a
  2026-09-15 retry via both `curl` and WebFetch) — still open, but
  recommend deprioritizing further automated retries on this specific URL
  (persistent bot-block on drovers.com itself, not an intermittent issue).
  Low-value source (industry counter-discourse, not a load-bearing
  empirical claim) — if needed later, search for other outlets covering
  the same Meat Institute statement instead of retrying this one URL.
- **RESOLVED 2026-09-15**: pork-specific figures from Balagtas & Cooper
  (2021) — see Claim #13 above. The article's own Figure 3 explicitly
  covers pork margin-widening, not just beef.
- **RESOLVED 2026-09-07**: Pozo/Bachmeier/Schroeder (2021) full text —
  still paywalled at ScienceDirect itself, but the authors' own K-State
  University working-paper version (KREx institutional repository,
  `krex.k-state.edu`, "revised_bachmeier_pozo_schroeder.pdf") was found and
  read in full directly (44 pages, via `curl` with a browser UA — WebFetch
  itself 403'd). Confirms the 2026-09-03 Consensus.app synthesis's
  conclusions essentially verbatim: scanner-data models fail to reject
  symmetry at monthly or weekly frequency; BLS-data models show statistically
  significant asymmetry (retail responds asymmetrically to farm, wholesale,
  and own-price shocks); counterfactual analysis suggests any undetected
  asymmetry favors consumers, not producers, at the retail level, and is
  ambiguous at the farm level depending on which shock is isolated. This is
  now a directly-verified primary read, not an AI-tool-mediated one — see
  `NOTES/2026-09-07-schaefer-pozo-idea28-followup.md` for detail. Evidence
  Table and this file's Claim #5 row updated accordingly.
- Extract pork-specific figures from Balagtas & Cooper (2021) to confirm or
  disconfirm a pork-specific COVID-margin finding (claim #13). Not
  attempted this pass.
