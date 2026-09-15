# Project Status — Gambling Social Cost Paper

_Last updated: 2026-09-15 (promo-deduction tax-treatment gap closed for all 17 coded states via direct statute pass, McCarthy/Taylor/Wilbur author list confirmed via SSRN, 3 new Category F literature entries, identification-strategy precedent found)_

## GO / MODIFY / STOP RECOMMENDATION

### MODIFY

The broad motivating question — does sports-betting tax revenue offset its social/financial costs — is real, publicly important, and not fully answered. But the *specific* framing in the original brief (a monetized Net Public Benefit / Social Cost Ratio calculation) runs into two problems the literature audit surfaced directly:

1. **A working paper already occupies the closest version of this contribution.** McCarthy (UMD Smith, Marketing), Taylor (SMU Cox), and a UC San Diego Rady co-author have a working paper — "The Effects of Sports Betting Legalization on Consumer Behavior, State Finances, and Public Health" — using proprietary transaction data on 700,000+ gamblers across 11 states, explicitly juxtaposing state tax revenue ($0.78/capita/month) against a new "irresponsible gambling" harm metric (+372%). They stop short of full dollar monetization and a formal net-benefit calculation, which is a real gap — but it's a narrow one, and a marketing-department team with much better data is already standing in it.
2. **Full monetization isn't currently defensible with data this project can access.** The classic Walker & Barnett critique and a 2025 scoping review both confirm the field still has no agreed method for what counts as a true externality versus a transfer (see `literature/social_cost_theory.md`). Several plausible cost categories (public assistance, productivity loss, uncompensated healthcare) have no dataset that isolates the gambling-caused, non-transfer portion. Forcing a dollar estimate here would violate the brief's own ground rule against "a dubious aggregate dollar estimate."

**What survives, and is recommended:** a **state fiscal-dependence → consumer-protection-policy-and-vulnerable-consumer-outcomes** design (Design C+D in `research_design/candidate_designs.md`). The literature audit found this specific mechanism — does a state's growing reliance on gambling tax revenue predict weaker consumer-protection rules and worse outcomes for financially vulnerable bettors — genuinely untested, strongly theoretically grounded in existing consumer-vulnerability/marketplace-access literature, buildable entirely from public data, and a much better editorial fit for the stated target venue (Journal of Public Policy & Marketing) than a pure economics cost-benefit paper would be.

## What we know
- Legalization's effects are not uniform: mobile/online legalization produces dramatically larger financial harm than retail-only legalization (roughly 17x larger credit-score effect in the best-identified study, Hollenbeck et al. 2026) — mobile-vs-retail must be treated as a distinct treatment in any design.
- Effects concentrate heavily among young men, lower-income/less-educated households, and Black-headed households across nearly every paper reviewed (household finance, substance use, and credit-debt literatures independently converge on this).
- Cannibalization of lottery/casino revenue is real in some states (NY) but not others (Indiana) — this is genuinely mixed evidence, not a settled fact either direction.
- The social-cost-of-gambling measurement literature has a 25+ year unresolved methodological debate about what counts as an externality — this project cannot sidestep that debate by simply picking a formula.

## What remains uncertain
- Whether a credible causal identification strategy exists for the "fiscal dependence → policy laxity" link in the recommended design, or whether it will end up correlational only (see `research_design/threats_to_validity.md`, reviewer-criticism #5). **Still the top open design question** — but see "What appears novel" note below: a real published precedent for the associational-only approach was found 2026-09-15.
- ~~Several health-outcome claims (suicide rate/hotline-call findings)~~ **Resolved 2026-09-04 via Consensus.app**: the suicide/helpline literature has a real, citable contradiction (Ozer/Greenwood/Gopal 2026 peer-reviewed finding a real effect vs. Kavanagh et al. medRxiv preprint finding none) — see `literature/literature_map.md` and `DECISION_LOG.md`.
- ~~The marketing/consumer-research literature (Category F) is under-searched~~ **Strengthened further 2026-09-15** (3 new fully-verified entries, including a real US-based experimental study on sportsbook-ad celebrity endorsers) — but a genuinely marketing-journal-specific (JPP&M/JCR/JA/Journal of Consumer Affairs) US treatment of sportsbook advertising is still the confirmed real gap. **Honest caveat, now stated explicitly**: both the 09-04 and 09-15 searches for this gap used general web search/Consensus.app, not a systematic database search of those journals' actual back issues — "not found" means "not found by these methods."
- ~~The promotional-deduction tax-treatment column was thin across nearly every coded state~~ **Closed 2026-09-15**: all 9 previously-gapped states (MA, ME, NJ, NC, IL, AZ, MI, PA, TN) now have statute-level promo-deduction sourcing, not AGA-guide inference — see `policy/state_policy_variables.md`. Turned up a real, dated finding worth carrying forward: North Carolina tightened its promotional-credit tax treatment via Session Law 2026-31, effective July 1, 2026 — a mid-sample policy change for a state already in the design.
- One outstanding manual task for Britton (not a library-access issue): open `peternencka.com/assets/gambling.pdf` directly and skim it — automated extraction of the Coombs/Madonia/Nencka/Smith lottery-cannibalization working paper failed twice.

## What appears novel
The fiscal-dependence/consumer-protection-policy mechanism (Design C), and its pairing with differential-vulnerability outcomes (Design D) — no study located this session tests this political-economy mechanism for sports betting specifically.

## What may already be answered
The core household-finance causal question (does legalization, especially mobile, harm household financial health) is now a crowded, well-answered space (Hollenbeck et al., Baker et al., the Journal of Gambling Studies credit-card-debt paper) — not worth re-litigating as a lead contribution.

## Best available design
Design C+D combined (state revenue-dependence as driver of both policy laxity and vulnerable-consumer harm) — see `research_design/candidate_designs.md` for full scoring.

## Most serious threat
No confirmed causal identification strategy yet for the dependence→policy mechanism specifically — this is the one piece of the recommended design that still needs real design work before it's submission-ready, not just execution. **2026-09-15**: a real, structurally-analogous published precedent for the associational (non-causal) version of this design was found — Jayawardhana et al. (2014, PLoS ONE) on tobacco-settlement-revenue dependence predicting weaker tobacco-control regulation, via plain fixed-effects panel regression with an openly-acknowledged, unresolved endogeneity caveat. This doesn't resolve the identification question (that's still Britton's call) but shows a top-tier reviewer process has accepted this exact class of design before — see `research_design/identification_strategy.md`.

## Data currently obtainable
Legalization/launch dates (AGA, state sites), revenue (AGA), bankruptcy (US Courts), suicide (CDC WONDER), substance use (BRFSS), crime/IPV (FBI NIBRS), demographic controls (Census/ACS/BLS) — all public, no restricted access needed. See `data/DATA_SOURCES.md`.

## Data that would require restricted access
Individual-level credit-bureau or financial-transaction-panel data (the data class behind the strongest published anchor papers) — not realistically obtainable for this project; the recommended design was chosen partly to avoid needing it.

## Recommended next action
**Confirmed by Britton, 2026-09-04:** "I like that pivot to looking at state's dependence on gambling funds and their modification of laws as the study 1 here." Design C (fiscal dependence → consumer-protection policy laxity) is locked in as **Study 1**.

**Data sweep, 2026-09-04** (`research_design/study1_data_feasibility_sweep.md`): Britton wants both C and D combined eventually, so a quick public-data feasibility check compared them for the secondary-data Study 1 role. Design C wins clearly — Census QTAX/State Tax Collections has a real, separately-broken-out sports-betting tax revenue series by state-quarter since Q3 2021 (the fiscal-dependence measure), and policy-laxity variables are hand-codeable in days from AGA's Responsible Gaming Regulations Guide + Legal Sports Report's tracker (~38-40 states, 5-8 dimensions). Design D's core predictor — state-level promotional/advertising intensity — has no free data source anywhere (only unusable national totals); its outcome side (BRFSS gambling module) exists but adoption is inconsistent state-to-state. **Study 1 = the full Design C panel, with Design D folded in only as exploratory subgroup outcomes (BRFSS gambling-module states), not a standalone claim.**

This also now answers what Study 2 (primary data) must capture: since promotional/ad exposure can't be measured secondarily, the Study 2 survey should ask bettors directly about perceived promotional/ad exposure, using Study 1's hand-coded state policy-stringency scores as a moderator on individual-level outcomes — linking the macro (Study 1) and micro (Study 2) halves of the paper.

Next concrete deliverables, in order:
1. **DONE 2026-09-09**: `research_design/identification_strategy.md` written — recommends
   associational primary specification (dependence measure broadened to total gambling revenue,
   which has real cross-state variance sports-betting-only revenue lacks) with a shift-share
   instrument as a robustness check, not a headline causal claim (no precedent found for that
   instrument in this exact application — would be this project's own contribution). **Two things
   left for Britton, not decided here**: (a) whether broadening the dependence measure to total
   gambling revenue — which reframes the paper from sports-betting-specific to gambling-dependence-
   general — is acceptable, and (b) whether the associational/robustness-IV framing is acceptable
   or he wants to push harder for a causal headline design first.
2. **DONE 2026-09-09**: `policy/state_legalization_timeline.csv` built — ~37 states + DC, retail
   and mobile launch dates, sourced live from sportsbettingdime.com's tracker plus separate
   verification of the two newest entries (Missouri, Wisconsin). Several states flagged needing
   hand-verification (phased mobile rollouts, ambiguous "launch" dates) before use in analysis.
3. **DONE 2026-09-09 (evening)**: `policy/state_policy_variables.md` — coding expanded from ~10 to
   **17 states**, via direct primary-source pulls (AGA per-state fact sheets + the full AGA
   Responsible Gaming Regulations and Statutes Guide, extracted with `pdftotext` after WebFetch's
   own PDF handling failed). **Rhode Island and West Virginia are now scored — the blocking gap is
   closed.** Result is a real, if preliminary, face-validity match: RI and WV score 2 and 3, the
   two lowest advertising-stringency scores in the table so far. Virginia's promo-deduction note
   was also corrected (was misdated as a mid-2025 policy change; actual mechanism is an older
   per-operator 12-month sunset). See `DECISION_LOG.md`'s 2026-09-09 entries for full detail.
4. Rough out Study 2's survey construct list (perceived promotional/ad exposure, financial vulnerability, marketplace access) once Study 1's panel is underway — the theoretical grounding should come from Category F of the literature map plus whatever Study 1's results actually show.
5. **DONE 2026-09-09 (evening)**: Rhode Island and West Virginia's consumer-protection policy
   stringency coded directly (see #3) — the face-validity test this project needed most is done.
6. **DONE 2026-09-15**: the promotional-deduction tax-treatment column, flagged 09-09 as the
   thinnest dimension across nearly every coded state, is now closed for all 9 states that were
   missing it (MA, ME, NJ, NC, IL, AZ, MI, PA, TN) — sourced directly against actual state
   sports-wagering tax statutes, not the AGA guide. Found the treatment is a genuine 4-category
   variable (no deduction / capped-or-thresholded / uncapped / full disallowance), not a binary,
   plus one dated, real policy change (NC's Session Law 2026-31, effective July 1, 2026, tightening
   promo-credit tax treatment). See `policy/state_policy_variables.md`.
7. **New 2026-09-09 (evening)**: one new literature entry added and verified (Obiol-Anaya et al.
   2026, corroborates the paper's novelty claim with international evidence); literature map now
   at ~29 entries.
8. **DONE 2026-09-15**: Category F strengthened further — 3 new fully-verified entries (Han &
   Saunak 2025 celebrity-endorser experiment, Meiselbach et al. 2026 podcast-ad-spend data, Holbert
   & Holbert 2025 national US media/attitudes survey) plus the existing Di Censo et al. entry
   upgraded from "venue not captured" to fully sourced with exact coefficients (and corrected to
   flag its sample as UK/Australia, not US). Literature map now at ~32 entries. A dedicated
   JPP&M/JCR/Journal of Advertising/Journal of Macromarketing back-issue search via an actual
   licensed database (not general web search) remains the best next step to close the
   marketing-journal-specific gap and approach the 30-50 target — flagged, not done this pass, as
   it needs library-database access beyond what this session's tools provide.
9. **DONE 2026-09-15**: McCarthy/Taylor/Wilbur working paper's full author list confirmed directly
   via SSRN search (`notes/claims_to_verify.md` item 6) — safe to cite as three authors
   (McCarthy, Taylor, Wilbur) now, with a title-versioning caveat noted in the literature map.
10. **DONE 2026-09-15**: a real published precedent (Jayawardhana et al. 2014, PLoS ONE, tobacco
    MSA-revenue-dependence → weaker tobacco control) found for the associational-only version of
    the identification strategy — added to `research_design/identification_strategy.md` and
    cross-referenced from `threats_to_validity.md` reviewer-criticism #5. Does not resolve the
    identification-strategy choice (still Britton's), but meaningfully de-risks the currently-
    recommended approach.
11. **Next up, not done this pass**: rough out Study 2's survey construct list (perceived
    promotional/ad exposure, financial vulnerability, marketplace access) — several strong
    candidate constructs are now available from Category F (Di Censo's "perceived susceptibility
    to inducements," Han & Saunak's endorser-congruence manipulation); expanding policy coding
    beyond 17 toward ~37-40 states using the same two-track (AGA guide for RG/advertising, direct
    statute for tax treatment) method demonstrated this pass; re-verifying the 8 states whose
    promo-deduction entries still come from the 09-09 AGA-guide-era pass (OH, CO, NY, VA, LA, RI,
    WV) against statutes directly for full sourcing consistency.
