# Candidate Research Designs

_Compiled 2026-09-04. Scored 1-5 (5 = best/strongest) per the brief's Section 12 criteria. See `literature/literature_map.md` and `data/DATA_SOURCES.md` for the evidence behind each score._

## Design A — Net State Welfare/Fiscal Study (the brief's original core concept)
Compare gambling revenue with causally estimated, monetized external costs; compute a Net Public Benefit or Social Cost Ratio.

| Criterion | Score | Why |
|---|---|---|
| Novelty | 2 | McCarthy, Taylor et al. (working paper, UMD Smith/SMU/UCSD) are already juxtaposing state revenue against a harm metric using superior proprietary transaction data. They stop short of full monetization, which leaves a narrow gap, not an open one. |
| Theoretical contribution | 3 | Would be strong *if* the monetization were defensible — but `social_cost_theory.md` shows the field itself hasn't solved this problem, and neither would we with public data alone. |
| Data availability | 2 | The individual-transaction-level data the strongest published papers use is restricted-access; public aggregates are a weaker substitute (see DATA_SOURCES.md). |
| Causal credibility | 3 | Staggered DiD on public state panels is doable, just not at the resolution of the anchor papers. |
| Execution difficulty | 2 (harder = lower score) | Monetizing even 2-3 cost categories defensibly, per the 6-part test in `social_cost_theory.md`, is a multi-month undertaking on its own. |
| Publication potential | 3 | Reviewers in economics/finance will directly compare this to Hollenbeck et al. and Baker et al. and ask "what's different" — a hard bar. |
| Marketing relevance | 2 | This version reads as economics/public finance, not marketing — weak fit for JPP&M unless reframed. |
| Likely reviewer objections | High risk | "Why should we believe your monetized cost figures over the many competing methodologies?" is a near-certain first-round objection. |

**Verdict: Not recommended as scoped.** The theoretically most ambitious design is also the most crowded and the hardest to execute credibly with available data.

---

## Design B — Financial Well-Being Study (narrower, state-aggregate version)
Focus tightly on consumer financial distress following mobile legalization, using public state-aggregate data (bankruptcy filings, NY Fed regional credit reports) rather than proprietary transaction data.

| Criterion | Score | Why |
|---|---|---|
| Novelty | 2 | Directly overlaps Hollenbeck et al. and Baker et al., just with coarser data and likely less statistical power — a replication-with-worse-data problem unless a genuinely new angle (state policy heterogeneity, a specific under-studied outcome) is added. |
| Theoretical contribution | 2 | Limited beyond what's already published, unless narrowed to something specific the anchor papers didn't cover (e.g., a specific state cluster, an under-studied outcome like SNAP/TANF). |
| Data availability | 4 | Fully public-data feasible (US Courts bankruptcy data, NY Fed public regional reports). |
| Causal credibility | 3 | Standard staggered-DiD threats apply; public data limits the granularity of controls compared to household-transaction panels. |
| Execution difficulty | 4 (easier) | Straightforward panel construction, well-precedented methods. |
| Publication potential | 2 | Would need a clear differentiator from already-published work to avoid a "so what, this is already known" desk reject. |
| Marketing relevance | 2 | Still reads as finance/economics unless reframed around consumer financial well-being as a marketing/consumer-welfare construct (Journal of Consumer Affairs is a plausible fit if reframed this way). |

**Verdict: Weak as a standalone design** — too close to already-published, well-resourced work. Could work as a secondary/robustness component of Design C or D rather than the lead design.

---

## Design C — State Revenue Dependence / Consumer Protection Tradeoff
Examine whether states that become more fiscally dependent on gambling revenue adopt weaker consumer-protection rules (advertising limits, promotional-deduction caps, responsible-gambling funding) or permit more aggressive marketing.

| Criterion | Score | Why |
|---|---|---|
| Novelty | 4 | No study located this session directly tests this political-economy / regulatory-capture-adjacent mechanism for sports betting specifically. The closest adjacent finding (Section B of the literature map) is only anecdotal — "reliance creates political inertia against rate reductions" — not a tested empirical claim. |
| Theoretical contribution | 4 | Squarely a public-policy-and-marketing contribution: government-as-stakeholder incentives shaping consumer-protection policy is a genuinely distinct frame from the finance papers. |
| Data availability | 3 | Requires hand-coding state policy variables (advertising rules, promotional-deduction caps, responsible-gambling funding levels) across ~35+ states — labor-intensive but entirely public-record (state statutes, gaming commission rules). |
| Causal credibility | 3 | This is more a policy-heterogeneity / correlational design than a clean natural experiment — reviewers will want a clear identification strategy for "dependence causes weaker protection" rather than just correlation (e.g., using a revenue-shock instrument, or timing of when a state crosses a fiscal-dependence threshold). |
| Execution difficulty | 3 | The policy-coding effort is real but bounded and matches skills already used in the Data Center and Flock Cameras paper threads (coding state-level regulatory text). |
| Publication potential | 4 | Directly fits JPP&M's actual subject matter (public policy design, consumer protection, government-industry tension) — a much better editorial fit than Design A/B. |
| Marketing relevance | 5 | This is the design most clearly "marketing and public policy," not applied economics. |

**Verdict: Strongest design identified this session**, contingent on finding (or building) a credible identification strategy for the dependence→policy-laxity link rather than settling for description.

---

## Design D — Marketing Access and Vulnerable Consumers
Study whether mobile access and promotional/advertising intensity disproportionately affect vulnerable populations (young men, low-income, financially constrained).

| Criterion | Score | Why |
|---|---|---|
| Novelty | 4 | The literature map's Category F finding is that peer-reviewed marketing scholarship on sportsbook advertising/promotional design is thin — journalistic and legal coverage exists, but a causal marketing-journal treatment is largely missing. |
| Theoretical contribution | 3-4 | Strong if grounded in consumer-vulnerability/marketplace-access theory already established in JPP&M/Journal of Consumer Affairs; the heterogeneous-effects finding already in the finance literature (young men, low-income, less-educated households bear disproportionate harm across nearly every paper in Category A/C) gives this design a strong empirical anchor to build on rather than starting from zero. |
| Data availability | 3 | State advertising-restriction rules are hand-codable (public record); a true promotional-*intensity* measure (ad spend, bonus-offer frequency) is harder to obtain publicly — may need to proxy via a state's regulatory permissiveness rather than actual ad-spend data. |
| Causal credibility | 3 | Same staggered-adoption toolkit as other designs; heterogeneity-by-subgroup analysis is well precedented in the literature already reviewed. |
| Execution difficulty | 3 | Moderate — main risk is the promotional-intensity data gap noted above. |
| Publication potential | 4 | Strong JPP&M/Journal of Consumer Affairs fit; would need to clear the marketing-literature-review bar the current session couldn't fully populate (Category F gap). |
| Marketing relevance | 5 | Directly on-topic for the target venue. |

**Verdict: Second-strongest design** — pairs well with Design C (both could be combined: does fiscal dependence on gambling revenue predict *both* weaker consumer-protection rules *and* worse outcomes for vulnerable populations, i.e., Design C as the policy mechanism and Design D as the consumer-welfare outcome it produces).

---

## Design E — Policy-Regime Heterogeneity
Compare states with different tax/advertising/promotional/operator/responsible-gambling regimes to determine which structures reduce harm while preserving revenue.

| Criterion | Score | Why |
|---|---|---|
| Novelty | 3 | Adjacent to Design C but outcome-focused (harm reduction) rather than mechanism-focused (why policy diverges); some existing work (Tax Foundation, AGA) already documents tax-rate variation and its revenue effects, but not paired against harm outcomes systematically. |
| Theoretical contribution | 3 | Useful policy-relevant contribution, less theoretically novel than C or D. |
| Data availability | 3 | Same state-policy hand-coding burden as Design C. |
| Causal credibility | 2 | Cross-state policy-regime comparison is closer to correlational than a clean natural experiment — states self-select into their regulatory regimes for reasons likely correlated with unobserved harm-relevant factors. |
| Execution difficulty | 3 | Similar to C. |
| Publication potential | 3 | Useful as a policy brief or a secondary analysis; less likely to clear a top marketing journal's theoretical-contribution bar on its own. |
| Marketing relevance | 3 | Policy-relevant but less theoretically grounded in a marketing construct than C/D. |

**Verdict: Viable as a secondary/exploratory analysis, not a strong standalone lead design.**

---

## Recommendation

**Lead with a combined Design C + D**: state fiscal dependence on sports-betting revenue as the driver of both (1) consumer-protection policy laxity and (2) differential harm to financially vulnerable populations — framed through a consumer-vulnerability / marketplace-access lens rather than a pure economics cost-benefit lens. This is the version of the project that is simultaneously most novel (per the literature audit), most defensible given real data constraints (avoids the monetization trap in Design A), and the best editorial fit for the stated target venue (JPP&M).

This does **not** fully answer the brief's original central question (Section 2's monetized net-benefit framing) — it answers an adjacent, more tractable question the literature audit suggests is actually open. That tradeoff is exactly what the brief's Section 19 GO/MODIFY/STOP framework anticipates; see `PROJECT_STATUS.md` for the formal recommendation.
