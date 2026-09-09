# Threats to Validity

_Compiled 2026-09-04, applies across all candidate designs unless noted otherwise._

## Endogeneity / selection into legalization
States did not adopt sports-betting legalization randomly. States with existing casino industries, budget shortfalls, or particular political compositions selected into legalization (and into mobile specifically) at different rates and times. Any staggered-DiD design needs to address whether the *timing* of adoption correlates with pre-existing trends in the outcome variables (parallel-trends assumption) — several papers in the literature map use event-study designs specifically to check this; ours should too.

## Confounders
- **COVID-era timing overlap**: several states' legalization waves (2020-2021) overlap with pandemic-era financial stimulus, unemployment insurance expansion, and generally disrupted gambling/entertainment substitution patterns. Any design spanning 2020-2021 must control for or exclude this window explicitly.
- **Concurrent vice-policy changes**: marijuana legalization, other gambling-form changes (new casinos, iLottery launches) happening in the same states around the same time as sports-betting legalization risk confounding attribution — flagged explicitly in the brief (Section 9) and confirmed live in our literature map's Category B conflicting cannibalization findings.
- **State-specific economic shocks**: any state-year model needs standard macro controls (Census/ACS/BLS) so a co-occurring recession or boom in a given state doesn't get misattributed to gambling policy.

## Spillovers / contamination
- The NY Fed staff report on cross-border spillovers (flagged UNVERIFIED-detail in the literature map, but the *mechanism* it describes is well-established in the border-county-design literature broadly) means a state's legalization can affect *neighboring* non-legal states' credit/betting outcomes — a classic SUTVA violation. Border-county designs are the standard remedy; worth budgeting for if the final design uses county-level data.
- **Illegal-market betting prior to legalization**: legalization may partly just formalize behavior that was already happening informally/illegally. This attenuates the "true" behavioral effect size relative to a no-betting-at-all counterfactual, and is unmeasurable directly (illegal-market handle isn't observed) — worth an explicit limitations statement rather than an attempted correction.

## Treatment heterogeneity and TWFE bias
Per the literature map (Category A, NY Fed spillover entry, and the general methodology search), naive two-way fixed-effects estimation is now well-documented to produce biased estimates under staggered adoption with heterogeneous treatment effects. Modern estimators (Callaway & Sant'Anna, Borusyak et al. imputation, Sun & Abraham) are the field standard now — several of the anchor papers in our literature map explicitly report using one of these as a robustness check against naive TWFE. Any manuscript from this project needs to do the same, not just run a standard `reghdfe` staggered-DiD and call it done.

## Retail vs. mobile conflation
The brief is correct that mobile/online legalization is very plausibly a distinct, larger treatment than retail legalization (Hollenbeck et al.'s 0.7-point vs. 12-point credit-score gap is direct evidence of this ~17x difference). **Any design that pools retail and mobile legalization into a single "legalized" indicator is likely to badly understate true mobile-specific effects** — this is not a minor design choice, it is probably the single most important specification decision across every candidate design in `candidate_designs.md`.

## Legalization date vs. launch date
Per DATA_SOURCES.md, the legislative legalization date and the actual first-wager date can differ by a year or more. Using the wrong one as the treatment-timing variable will misattribute pre-launch anticipation-period changes to a "before" period that should actually be "after," or vice versa — a coding error, not a deep methodological problem, but one that needs careful hand-verification per state (see policy/ directory, not yet built).

## Measurement problems specific to proposed cost categories
See `literature/social_cost_theory.md` for the full breakdown — the short version: several plausible externality categories (public assistance, productivity loss, uncompensated healthcare) have no dataset that cleanly isolates the gambling-attributable, non-transfer portion. Any design that tries to quantify these needs to either (a) find a better data source than identified this session, or (b) explicitly scope the cost side down to only the categories with defensible measurement (treatment-program costs, bankruptcy administrative costs, IPV response costs) and say so plainly rather than presenting a partial estimate as if it were comprehensive.

## Data-resolution mismatch vs. published anchor papers
As flagged in DATA_SOURCES.md, this project will not have access to the individual-level transaction-panel or credit-bureau data that Hollenbeck et al. and Baker et al. used. Any design competing directly on the same outcome variables (credit scores, bankruptcy, savings) at the same resolution will be judged against those papers and found under-powered. The recommended design (C+D combination, see `candidate_designs.md`) is partly chosen *because* it uses outcome variables (policy variables, heterogeneous-harm patterns) that don't require that same restricted data.

## Likely reviewer criticisms (anticipate these directly)
1. "How is this different from Hollenbeck et al. / Baker et al. / McCarthy et al.?" — needs a one-sentence answer ready before submission, not discovered during review.
2. "Why these specific cost categories and not others?" — answer using the 6-part test in `social_cost_theory.md`, not ad hoc justification.
3. "Is TWFE bias addressed?" — yes, plan for a modern staggered-DiD estimator from the start, not as a revision-stage fix.
4. "Retail and mobile are conflated" — do not let this happen; separate treatment indicators from the design stage.
5. "This is descriptive/correlational, not causal, for the policy-regime design (C/E)" — be upfront in the manuscript about which parts of the design are causal (harm outcomes via DiD) versus associational (policy-regime comparison), rather than overclaiming causal language for the political-economy mechanism.
