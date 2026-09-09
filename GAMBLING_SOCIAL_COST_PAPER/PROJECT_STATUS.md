# Project Status — Gambling Social Cost Paper

_Last updated: 2026-09-09 evening (RI/WV policy-coding gap closed, coverage expanded to 17 states, one new verified literature entry)_

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
- Whether a credible causal identification strategy exists for the "fiscal dependence → policy laxity" link in the recommended design, or whether it will end up correlational only (see `research_design/threats_to_validity.md`, reviewer-criticism #5). **Still the top open design question.**
- ~~Several health-outcome claims (suicide rate/hotline-call findings)~~ **Resolved 2026-09-04 via Consensus.app**: the suicide/helpline literature has a real, citable contradiction (Ozer/Greenwood/Gopal 2026 peer-reviewed finding a real effect vs. Kavanagh et al. medRxiv preprint finding none) — see `literature/literature_map.md` and `DECISION_LOG.md`.
- ~~The marketing/consumer-research literature (Category F) is under-searched~~ **Meaningfully strengthened 2026-09-04** via Consensus (5 new addiction/behavioral-journal citations) — but a genuinely marketing-journal-specific (JPP&M/JCA) US treatment of sportsbook advertising is still the confirmed real gap, now more precisely characterized rather than just "thin."
- One outstanding manual task for Britton (not a library-access issue): open `peternencka.com/assets/gambling.pdf` directly and skim it — automated extraction of the Coombs/Madonia/Nencka/Smith lottery-cannibalization working paper failed twice.

## What appears novel
The fiscal-dependence/consumer-protection-policy mechanism (Design C), and its pairing with differential-vulnerability outcomes (Design D) — no study located this session tests this political-economy mechanism for sports betting specifically.

## What may already be answered
The core household-finance causal question (does legalization, especially mobile, harm household financial health) is now a crowded, well-answered space (Hollenbeck et al., Baker et al., the Journal of Gambling Studies credit-card-debt paper) — not worth re-litigating as a lead contribution.

## Best available design
Design C+D combined (state revenue-dependence as driver of both policy laxity and vulnerable-consumer harm) — see `research_design/candidate_designs.md` for full scoring.

## Most serious threat
No confirmed causal identification strategy yet for the dependence→policy mechanism specifically — this is the one piece of the recommended design that still needs real design work before it's submission-ready, not just execution.

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
6. **New 2026-09-09 (evening), next concrete step**: the promotional-deduction tax-treatment
   column is now the thinnest dimension across nearly every coded state (the AGA Responsible
   Gaming Guide used this pass is RG/advertising-focused, not reliably comprehensive on tax
   treatment) — needs its own pass through actual state sports-wagering tax statutes. Expanding
   from 17 toward full ~37-40-state coverage is mechanical from here (same AGA guide, more states)
   and lower priority than closing the promo-deduction gap.
7. **New 2026-09-09 (evening)**: one new literature entry added and verified (Obiol-Anaya et al.
   2026, corroborates the paper's novelty claim with international evidence); literature map now
   at ~29 entries. A dedicated JPP&M/JCR/Journal of Macromarketing back-issue search remains the
   best next step to close in on the 30-50 target, not done this pass.
