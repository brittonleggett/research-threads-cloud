# State Consumer-Protection Policy Variables — First Pass (2026-09-09)

**Status: partial, not exhaustive.** This is a first pass covering the states with the best
documented, most-searched policy actions (advertising restrictions, promotional-deduction tax
treatment, and responsible-gambling program requirements) — roughly 10 of the ~37-40 states with
legal sports betting. Coding the remaining states requires going state-by-state through each
gaming commission's actual regulations (the AGA's "Responsible Gaming Regulations and Statutes
Guide," `americangaming.org/resources/responsible-gaming-regulations-and-statutes-guide/`, is the
right primary source for the full sweep — flagged as the next concrete step, not done this pass).
Do not treat a state's absence from this file as "no policy" — it means "not yet coded," which is
a different thing. This distinction matters for the two named high-dependence cases (Rhode Island,
West Virginia) especially, since their coding is the closest thing this project has to a direct
face-validity test of the whole mechanism — both are included below.

## Coding dimensions

1. **Advertising restrictions** — audience-targeting rules (underage-audience thresholds),
   "risk-free"/"free bet" language bans, problem-gambling-message requirements.
2. **Promotional-deduction tax treatment** — whether the state allows sportsbooks to deduct the
   value of promotional free bets/bonus credits from taxable revenue (a direct subsidy to
   promotional intensity) and whether/when that deduction has been capped or phased out.
3. **Responsible-gambling program requirements** — algorithmic/data-driven intervention mandates,
   self-exclusion protections, deposit/spending limit requirements.

## Coded states (first pass)

| State | Advertising restrictions | Promo-deduction treatment | RG program requirements | Stringency (informal, 1-5) |
|---|---|---|---|---|
| Massachusetts | Strong — bans "free" labeling when user risks own money, bars targeting minors/self-excluded individuals, mandatory helpline messaging | Not identified as capped this pass | Mandated data/algorithmic triggers for problem-gambling intervention | 4-5 (most stringent identified this pass) |
| Ohio | Banned "risk-free"/"free bet" language Jan. 2023 (OCCC rule); active enforcement — three operators fined $150K-$350K for violations | Doubled tax rate July 2023, explicitly citing high promotional-spending volume as the rationale (a de facto promotional disincentive via the tax code rather than a direct deduction cap) | Not separately identified this pass | 4 |
| Colorado | Not separately identified this pass beyond general audience-targeting rules | Free-bet promotional deduction phased out on a schedule, fully eliminated July 1, 2026 | Algorithmic/data-driven RG intervention rules identified (grouped with MA/NJ/NC in this pass's search) | 3-4 |
| Maine | Bars advertising promotional bonus offers in public forums (2023 rule) | Not identified this pass | Not separately identified this pass | 3 |
| New Jersey | Audience-targeting rules since 2022; pending 2025 bill (A4003) would bar extending promotions to users of RG tools | Not identified as capped this pass | Algorithmic/data-driven RG intervention rules identified | 3-4 |
| New York | Audience-targeting rules since 2022 | Not identified as capped this pass; notably NY's headline policy lever is its very high tax rate (~51%) rather than promo-deduction treatment specifically — worth treating tax rate as a related but distinct policy variable, not folded into this scale | Not separately identified this pass | 3 (on these three dimensions specifically; NY's overall regulatory posture is stricter than this narrow scale captures) |
| North Carolina | Audience-targeting rules since 2022 | Not identified this pass | Algorithmic/data-driven RG intervention rules identified | 3 |
| Illinois | Audience-targeting rules since 2022 | Not identified this pass | Not separately identified this pass | 2-3 |
| Virginia | Not separately identified this pass | Promotional-deduction tax credit removed effective mid-2025 per state budget action (exact date needs verification against the actual budget bill text before use) | Not separately identified this pass | 3 (pending date verification) |
| Louisiana | Not separately identified this pass | Promotional-deduction cap referenced in `PROJECT_STATUS.md`'s prior scoping note but not independently re-verified this pass | Not separately identified this pass | Unscored — needs direct verification |
| Rhode Island | Not identified this pass — needs direct check, high priority given its role as a named high-dependence case | Not identified this pass | Not identified this pass | **Unscored — priority gap.** Single-operator (IGT/Bally's) market structure may itself be a relevant policy-proxy worth checking |
| West Virginia | Not identified this pass — needs direct check, high priority given its role as a named high-dependence case | Not identified this pass | Not identified this pass | **Unscored — priority gap.** |

## Reading this table honestly

- "Not identified this pass" is a search-coverage gap, not a finding of "no policy in that state."
  Several states almost certainly have real advertising or RG rules that a broader search (or a
  direct read of each state gaming commission's regulations) would surface.
- **The two states this project most needs coded — Rhode Island and West Virginia, the named
  high-dependence cases in `research_design/identification_strategy.md` — are currently the two
  least-covered in this table.** That's the single highest-priority gap to close before this file
  can support any real analysis, not a peripheral state.
- New York's very high tax rate suggests "stringency" may need to be a multi-dimensional
  construct (advertising / promo-deduction / RG-mandate / tax-rate) rather than a single 1-5 scale
  collapsing all of them — worth deciding once more states are coded and the construct's structure
  becomes clearer empirically, not before.

## Next steps (not done this pass)

1. Direct read of AGA's Responsible Gaming Regulations and Statutes Guide for full-coverage
   coding across all ~37-40 states, prioritizing Rhode Island and West Virginia first.
2. Verify Virginia's promotional-deduction-removal date against the actual 2025 budget bill text
   (currently sourced only from secondary reporting).
3. Decide whether tax rate belongs in the stringency construct or as a separate variable (see
   New York note above) — this is a measurement-design choice, not a data-gathering one.
