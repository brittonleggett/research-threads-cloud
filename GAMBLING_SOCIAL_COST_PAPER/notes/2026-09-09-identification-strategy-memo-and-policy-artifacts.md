# 2026-09-09 — Identification strategy memo formalized, first policy artifacts built

Executed `PROJECT_STATUS.md`'s next-deliverables #1-3 under the standing autonomy mandate. No
design lock made — the causal-identification and dependence-measure-scope questions are flagged
for Britton in `research_design/identification_strategy.md`'s closing section.

## What was done

1. **`research_design/identification_strategy.md`** — formalizes and extends the 09-08 feasibility
   note. Verified directly (Rockefeller Institute, Mass Budget and Policy Center, Tax Foundation-
   style sin-tax ranking) that broadening the dependence measure from sports-betting-only to total
   gambling tax revenue produces real, multi-source-confirmed cross-state variance (national
   average ~2.23% of state revenue; Rhode Island and West Virginia both meaningfully above that,
   roughly 3-4%+ depending on source/year) — the sports-betting-only measure genuinely lacks this
   variance (confirmed again, no change from 09-08). Searched for a shift-share/Bartik-instrument
   precedent in gambling-dependence political economy specifically — **found none**; the technique
   exists in adjacent state-fiscal literature but would be this project's own contribution to build,
   not a borrowed design. Recommendation: associational primary specification (already
   pre-authorized in `threats_to_validity.md`), shift-share IV as a robustness check only, Rhode
   Island/West Virginia as case-study anchors. **Flagged, not decided:** broadening to total
   gambling revenue shifts the paper's framing from "a sports-betting paper" to "a gambling-
   dependence paper using sports betting as its motivating case" — a real choice, not a data
   technicality.
2. **`policy/state_legalization_timeline.csv`** — real state-by-state retail/mobile legalization
   and launch dates, sourced from a live fetch of sportsbettingdime.com's tracker (~37 states + DC),
   cross-checked against separate web-search results for the two newest entries (Missouri launched
   Dec. 1, 2025; Wisconsin authorized online betting April 9, 2026 but **not yet launched** as of
   this pass — coded explicitly as not-yet-launched, not as a 2026 treatment date, since treating it
   as launched would be a fabrication). Flagged several states needing hand-verification before use
   in analysis (Illinois's phased mobile-registration rollout, Florida's online-before-retail
   sequencing, Arkansas's exact mobile date) rather than presenting a single clean date where the
   real history is messier.
3. **`policy/state_policy_variables.md`** — first-pass coding of advertising restrictions,
   promotional-deduction tax treatment, and responsible-gambling program mandates for ~10 states
   with the best-documented policy actions (Massachusetts, Ohio, Colorado, Maine, New Jersey, New
   York, North Carolina, Illinois, Virginia, Louisiana) plus Rhode Island and West Virginia
   (explicitly left **unscored** — searches this pass did not surface their specific policy details,
   and fabricating a stringency score for the two states the whole design most depends on would be
   exactly the wrong place to guess). **This is the single highest-priority gap left open**: RI/WV
   coding is the closest thing this project has to a direct face-validity check on the core
   mechanism, and it's currently the least-covered part of the table.

## Not done, and why

- Full 38-40-state policy coding — would require a direct read of AGA's Responsible Gaming
  Regulations and Statutes Guide state-by-state, not a handful of web searches; scoped as the
  explicit next step rather than rushed to fake completeness.
- The Britton-only manual task (`peternencka.com/assets/gambling.pdf`, automated extraction failed
  twice previously) — not retried; still needs him to open it directly.

## Fork in the road for Britton (not decided here)

Two related open choices, both flagged in `identification_strategy.md`:
1. Does the paper's dependence measure broaden to total gambling revenue (recommended, since
   sports-betting-only lacks real variance), reframing the paper's identity in the process?
2. Is the associational-primary / shift-share-robustness framing acceptable, or does Britton want
   to push harder for a fully causal headline design before more building continues?

Everything else in this note (data-gathering, sourcing, first-pass coding) was executed directly
per the standing mandate, not proposed and parked.
