# Identification Strategy — Fiscal Dependence → Consumer-Protection Policy Laxity

_Formalizes the finding in `notes/2026-09-08-identification-strategy-feasibility.md`, per
`PROJECT_STATUS.md` next-deliverable #1. Extended 2026-09-09 with real state-level data checks
and a literature/instrument search. This is a recommendation, not a lock — the final choice among
the options below is Britton's, especially the framing question in the last section._

## The two causal questions this design actually contains

1. **Legalization → financial-harm outcomes.** Well-precedented (Hollenbeck et al., Baker et al.
   already use this). Staggered-DiD/event-study, modern estimator (Callaway & Sant'Anna or
   Borusyak et al.) to avoid TWFE bias, retail/mobile as separate treatments. **No open
   identification problem here — GO as planned.**
2. **Fiscal dependence → policy laxity.** This is the paper's actual novel contribution and the
   one with a real identification problem: dependence is a continuous, slowly-evolving state, not
   a discrete treatment date, so the event-study toolkit for (1) doesn't transfer directly.

## Does "dependence" have real variance to identify from? (checked directly, 2026-09-09)

The original resource-curse framing (states like Alaska deriving up to ~90% of budget from
severance taxes) does not transfer to **sports-betting-specific** revenue: even New York, the
highest-revenue state, collected $800.1M in FY2023 — under 1% of state tax revenue (Tax
Foundation data, per the 09-08 note). That finding holds.

But broadening to **total gambling tax revenue** (lottery + casino + sports betting), real
cross-state variance does exist and is large enough to be worth building a design around:

- National average: gambling revenue ≈ **2.23% of state budgets** (Massachusetts FY2025 figure,
  which happens to match the national ITEP average cited in the 09-08 note — Mass Budget and
  Policy Center, "Payouts and Risks in Massachusetts's Gambling Revenue," Sept. 2025).
- **Rhode Island and West Virginia are genuine outliers, not just marginally above average.**
  Multiple sources converge: Rockefeller Institute of Government put Rhode Island's lottery share
  of total state revenue at ~4.4% (a widely-cited FY2013 figure) and West Virginia at ~3.9%;
  more recent reporting puts Rhode Island lottery revenue at ~3.0% of general revenue (vs. a
  ~1.0% national average in that same source) with RI's two casinos separately contributing
  roughly another ~10% of total state revenue in an earlier accounting (the video-lottery-terminal
  revenue-sharing agreement gives the state 61% of VLT revenue at one casino). A sin-tax-specific
  ranking (Tax Foundation-style analysis) separately names Rhode Island the single most
  sin-tax-dependent state in the country, at 15.9% of total tax revenue (this figure blends
  gambling with tobacco/alcohol, so it's directional corroboration, not a standalone gambling
  number).
- **This is a real, meaningful, multi-source-confirmed spread** — call it roughly 1%-4%+ of state
  revenue across states, with RI and WV as clear high-dependence cases and most other states
  clustered near the ~1-2% national average. That's a usable range for a continuous-dependence
  design; sports-betting-only revenue is not.

**Recommendation: use total gambling tax revenue as % of state tax revenue as the dependence
measure, not sports-betting-specific revenue alone.** This changes the paper's framing question
from "does sports-betting dependence..." to "does gambling-revenue dependence generally...", with
sports betting treated as the newest, fastest-growing, most policy-active component within that
broader dependence measure — worth flagging as a framing choice, not a data-availability
afterthought (see final section).

## Instrument search (this pass)

Two candidates were checked; neither is a clean, published, directly-applicable instrument:

1. **Neighboring-state legalization/proximity** (originally suggested) — rejected per the 09-08
   note: state-policy-diffusion research finds neighboring-state proximity affects a state's own
   policy choices directly, not just through a dependence channel. Violates the exclusion
   restriction.
2. **Shift-share / Bartik-style instrument** (pre-existing lottery/casino revenue share ×
   national sports-betting revenue growth) — this pass searched specifically for precedent
   applying shift-share designs to state vice-tax or gambling-revenue dependence and **found
   none**. The technique is standard in state-fiscal political economy generally (e.g., profit-
   shifting/corporate-tax-base literature, Tax Notes 2025) and in labor/regional economics broadly,
   but not in this specific gambling-dependence application — it would need to be built as this
   project's own contribution, not borrowed from a precedent paper. This raises the bar for
   defending it (a reviewer will ask why this instrument is valid here specifically) but doesn't
   rule it out.
3. **A genuinely useful adjacent finding**: the sin-tax political-economy literature confirms
   states treat sin-tax increases (including, implicitly, gambling-adjacent revenue) as a
   politically easier substitute for raising income/property/sales taxes during budget pressure
   (125 state cigarette-tax increases vs. 21 sales-tax increases since 2000, per this pass's
   search) — this is corroborating *mechanism* evidence for why fiscal dependence could plausibly
   drive policy behavior, useful for the manuscript's motivation section, but it is not itself an
   identification strategy.

**No academic paper doing exactly "gambling-revenue fiscal dependence → consumer-protection
policy stringency" was found in this or the 09-08 pass.** This is good news for novelty (matches
`PROJECT_STATUS.md`'s "what appears novel" section) and bad news for borrowing a ready-made
identification strategy — there isn't one to borrow.

## Recommendation

**Do not force a fully causal design onto the dependence→policy-laxity link.** Two things
together, matching and extending the 09-08 note's verdict now that the variance question has real
data behind it:

1. **Primary specification: associational/correlational**, explicitly framed as such in the
   manuscript (per `threats_to_validity.md` reviewer-criticism #5, already pre-authorized). Use
   total gambling-revenue dependence (not sports-betting-only) as the continuous predictor, with
   state and year fixed effects, standard political/fiscal controls (budget-shortfall history,
   party control, existing casino/tribal-gaming presence as a pre-treatment covariate), and
   report it as a policy-regime correlation, not a causal claim.
2. **Robustness check, not headline result: build the shift-share instrument** (pre-existing
   gambling-market structure × national sports-betting revenue growth) as a secondary/IV
   specification. Since no precedent exists for this exact application, the manuscript should
   justify the exclusion restriction explicitly from first principles (a state's *pre-existing*
   lottery/casino market structure, fixed years before sports-betting legalization, plausibly
   affects its post-legalization *revenue level* without directly determining its post-legalization
   *consumer-protection policy choices* — arguable, not airtight; say so).
3. **Rhode Island and West Virginia become natural qualitative/case-study anchors** regardless of
   which quantitative specification is used — as the two clearest high-dependence cases, their
   actual consumer-protection policy stringency (once `policy/state_policy_variables.md` is built
   out) is worth checking by hand as a face-validity test of the whole mechanism, independent of
   the panel regression.

## The one real judgment call left for Britton (not resolved here)

Broadening the dependence measure to total gambling revenue is what makes the design workable,
but it shifts the paper's identity from "a sports-betting paper" to "a gambling-revenue-dependence
paper that treats sports betting as its motivating/newest case." Both framings are defensible and
this doesn't have to be resolved before more building happens — but it changes the literature
review's center of gravity (broader gambling-policy political economy vs. sports-betting-specific
literature) and should be a conscious choice, not a drift. Flagging it here rather than deciding
it silently.
