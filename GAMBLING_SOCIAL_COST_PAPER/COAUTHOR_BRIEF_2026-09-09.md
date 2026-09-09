# Research Proposal: State Fiscal Dependence and Consumer-Protection Policy in Legalized Sports Betting

*Prepared by Britton Leggett — September 2026*

---

## The question

Since *Murphy v. NCAA* (2018) struck down the federal ban on sports betting, states have legalized rapidly and now compete for a share of a market approaching $17B in annual revenue. A growing body of research — mostly in finance and economics — has documented the *consumer harm* side of this: legalization, especially mobile/online, measurably worsens household financial health (credit scores, bankruptcy, credit card debt), concentrated among young men, lower-income households, and Black-headed households.

What hasn't been tested is the **policy side of the same story**: does a state's growing fiscal reliance on gambling tax revenue predict *weaker* consumer-protection regulation — advertising limits, promotional-credit tax treatment, responsible-gambling mandates? In other words, does the state itself, as the fiscal beneficiary of the harm, have a built-in incentive to regulate it lightly?

That link — fiscal dependence → policy laxity — is the paper's core contribution. It sits at the intersection of public policy marketing, consumer vulnerability, and political economy, and a targeted literature search (run twice, a week apart) found no existing study that tests it directly for gambling.

## Why this gap is real, not assumed

The closest existing work is an unpublished working paper (McCarthy, Univ. of Maryland Smith; Taylor, SMU Cox; and a UC San Diego coauthor) using proprietary transaction data on 700,000+ gamblers across 11 states. It juxtaposes state tax revenue (~$0.78/capita/month) against a novel "irresponsible gambling" harm index (+372% post-legalization) — but explicitly stops at reporting the two side by side. It does not test whether fiscal dependence itself predicts policy stringency. That's the space this project occupies.

The literature review (currently ~29 individually source-verified entries, each checked against its publisher/journal record rather than pulled from memory) also confirms two other things worth knowing going in:
- The household-financial-harm question itself is now a **crowded, well-answered space** (Hollenbeck, Larsen & Proserpio, *Management Science* 2026; Baker et al., *Journal of Financial Economics* 2026) — not worth re-litigating as this paper's headline finding.
- A **full dollar-cost/net-benefit calculation is not currently defensible**: the academic social-cost-of-gambling literature has a 25+-year unresolved dispute over what counts as a true externality versus a wealth transfer, and no dataset isolates the gambling-caused, non-transfer portion of costs like public assistance or productivity loss. This project deliberately avoids that trap rather than producing "a dubious aggregate dollar estimate."

## Proposed design

**Study 1 (secondary data, public sources only):** A state-panel design testing whether gambling-revenue fiscal dependence predicts consumer-protection policy stringency.
- **Dependence measure:** total gambling tax revenue (lottery + casino + sports betting) as a share of state tax revenue — sports-betting revenue alone turns out to have almost no cross-state variance (even New York, the highest-grossing state, is under 1% of its tax base), but total gambling dependence has real, usable spread: national average ≈2.2%, with Rhode Island and West Virginia as clear, multi-source-confirmed outliers.
- **Outcome measure:** a hand-coded policy-stringency index (advertising/audience-targeting restrictions, promotional-credit tax treatment, responsible-gambling program mandates), built from primary regulatory sources, now coded for 17 states and counting.
- **Primary specification:** associational (state and year fixed effects, standard fiscal/political controls), explicitly reported as correlational rather than causal.
- **Robustness check:** a shift-share instrument (pre-existing lottery/casino market structure × national sports-betting revenue growth) — no precedent exists for this exact application, so it would be this paper's own methodological contribution, built and defended from first principles rather than borrowed.

**Study 2 (primary data):** A bettor survey measuring perceived promotional/advertising exposure and financial vulnerability, with Study 1's state-level policy-stringency scores used as a moderator — linking the macro (state policy) and micro (individual bettor) halves of the paper.

**Target venue:** *Journal of Public Policy & Marketing* — this design is a substantially better editorial fit there than a pure cost-benefit economics paper would be.

## Where it stands right now

This is a **design-stage project**, not one with results in hand — worth being direct about that. What exists:

- A locked, novelty-checked research question and a defensible Study 1/Study 2 design.
- A real, verified literature base (~29 entries), with the marketing-specific gap this paper fills clearly identified rather than assumed.
- Confirmed public-data feasibility for every Study 1 variable — no restricted or proprietary data required.
- A 37-state sports-betting legalization timeline built.
- Policy-stringency coding underway: 17 of ~38-40 states coded from primary regulatory sources so far, including the two states the whole mechanism depends on (Rhode Island and West Virginia, the clearest high-dependence cases). Preliminary pattern — **not a regression result, n=17, face-validity only** — is at least directionally consistent with the hypothesis: RI and WV currently show the weakest advertising-stringency scores in the table.

What's still open:
- **The identification strategy is the single biggest open intellectual problem**, and honestly the best entry point for a coauthor: the associational design is defensible but not causal, and the shift-share instrument is unprecedented in this application — it needs someone who can stress-test the exclusion restriction and either strengthen it or propose a better identification approach.
- Promotional-credit tax treatment (one of the three policy dimensions) is the least-covered so far and needs a dedicated pass through actual state tax statutes.
- Full 38-40 state coverage is mechanical from here but not yet done.
- No data panel has been assembled and no analysis has been run yet — that's the next phase after coding wraps.

## What a coauthor could bring

The design work above was done to make sure this isn't a paper searching for a contribution — the gap is real, checked twice, and the data path is confirmed feasible. What's genuinely open is the econometric identification problem, and secondarily, capacity to help finish the policy coding and eventually run and interpret the panel model. This is a project that's past the "is this worth doing" stage and into the "how do we do this rigorously" stage — which is a good point to bring someone in.

---

*Happy to walk through the full literature map, the identification-strategy memo, or the coding so far in as much detail as useful.*
