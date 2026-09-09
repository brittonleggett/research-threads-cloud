# 2026-09-08 — Identification strategy feasibility check: fiscal dependence → policy laxity

Executes the Decision Memo's named minimal step for this paper (`Desktop\Decision_Memo_Noncore_
Papers_2026-09-08.md`), which is also `PROJECT_STATUS.md`'s explicitly-named next deliverable #1
(`research_design/identification_strategy.md`). This note answers that question; a formal
identification_strategy.md can be split out from this if Britton wants the permanent version filed
there instead.

## The three questions asked, answered directly

**1. Is state-by-state sports-betting legalization timing clean enough for a staggered DiD/event-
study design?** Yes, for the *legalization → outcome* question specifically — this is exactly the
identification strategy Hollenbeck et al. and Baker et al. (already in this project's literature
map) use for financial-harm outcomes, and it's well-precedented. Confounders are real but
manageable with the controls already flagged in `threats_to_validity.md` (COVID-window exclusion,
concurrent marijuana/iLottery changes, retail-vs-mobile separation, modern staggered-DiD estimators
per the TWFE-bias literature). **But this is not actually the identification strategy this
project's core new mechanism needs** — see finding below.

**2. Is a parallel-trends check feasible?** Yes for legalization timing (multiple pre-treatment
years exist for most outcome variables back to whenever states began tracking them). Not
straightforwardly for the *dependence* variable specifically, because dependence isn't a discrete
treatment date — it's a continuous, slowly-evolving state that emerges gradually after
legalization. A standard event-study design tests "did legalizing cause a change," not "did
becoming more fiscally dependent cause a change" — these are different causal questions requiring
different designs.

**3. Does a plausible instrument exist for fiscal dependence?** The originally-suggested "distance
to a legalized neighboring state" instrument has a real exclusion-restriction problem: state-policy
diffusion research consistently finds neighboring-state proximity affects a state's *own* policy
choices directly (states copy nearby states' regulations), not just through a dependence channel —
this would violate the exclusion restriction, not satisfy it. A cleaner candidate: a **Bartik/
shift-share-style instrument** — predicted sports-betting revenue built from a state's
*pre-existing* gambling-market structure (pre-sports-betting lottery/casino revenue share)
interacted with national sports-betting revenue growth trends, which predicts a state's likely
sports-betting revenue from its market structure rather than its post-legalization policy choices.
This is a standard technique in state-fiscal political economy (analogous to how state reliance on
other volatile revenue sources gets instrumented), but **no published paper applying it to this
exact gambling-dependence question was found this pass** — it would need to be built, not borrowed.

## The bigger, previously-undiagnosed problem: does "fiscal dependence" even have real variance to
identify from?

This is the actual finding worth surfacing, beyond the three questions as posed. The project's
"dependence → policy laxity" design was explicitly motivated by a resource-curse analogy (states
like Alaska deriving up to 90% of budget from oil/gas severance taxes exhibit distinctive
political-economy behavior). **Checked directly this pass, via Tax Foundation's state-by-state
sports-betting tax data: even New York, the single highest-revenue state in the country, collected
$800.1 million in FY2023 — under 1% of New York's total state tax revenue.** South Dakota, the
lowest, collected $94,424. Broadening to *all* gambling revenue combined (lottery + casino + sports
betting), a second source (ITEP) confirms gambling revenue nationally represents only **2.23% of
state budgets on average in FY2025**, and has been *declining* as a budget share over 25 years —
nothing resembling Alaska's severance-tax concentration exists anywhere in gambling revenue
specifically.

**This means the core premise may not have the real-world variance the resource-curse framing
assumed.** A causal design — however well-instrumented — cannot detect an effect of "dependence" if
no state is ever meaningfully dependent in the first place. This is a different, more fundamental
problem than the reverse-causality/endogeneity concern already flagged in `threats_to_validity.md`;
it's a power/construct-validity problem sitting underneath the causal-identification one.

## Verdict: MODIFY, not a clean GO or NO-GO

**For the legalization → outcome question:** GO, using the already-planned staggered-DiD/event-
study approach — well precedented, real data, no new blocker found.

**For the specific dependence → policy-laxity causal claim:** does not clearly GO as originally
scoped. Recommend two changes together, not either alone:

1. **Broaden the dependence measure from sports-betting-specific tax revenue to total gambling/
   gaming tax revenue** (lottery + casino + sports betting combined, all in the same Census
   QTAX/STC data family already identified as feasible) — sports-betting-only dependence is too
   uniformly tiny to work with; total gambling dependence has more real cross-state spread (states
   with major tribal casino compacts or heavy lottery reliance plausibly show meaningfully higher
   shares than 2.23%, worth checking directly against the actual state-level data before assuming
   it's still too thin).
2. **Report the dependence→policy link as explicitly associational/correlational**, exactly as
   `threats_to_validity.md`'s own reviewer-criticism #5 already anticipated and pre-authorized ("be
   upfront in the manuscript about which parts of the design are causal... versus associational...
   rather than overclaiming causal language for the political-economy mechanism") — this doesn't
   kill the paper, it's the honest framing the project's own prior work already said might be
   necessary, now confirmed as the right call rather than a fallback to consider only if a causal
   design fails. The instrument sketched above (shift-share on pre-existing gambling-market
   structure) is worth building as a *robustness check* strengthening the correlational claim, not
   as a requirement for a fully causal headline result.

## What this doesn't touch

No design decision is locked here — Design C remains the recommended Study 1 scope per
`PROJECT_STATUS.md`; this note only resolves the specific causal-identification question that was
the single named blocker. Britton's read on whether the broadened total-gambling-revenue dependence
measure changes the paper's framing (still "sports betting" specifically vs. "gambling generally")
is a real judgment call this note doesn't resolve.
