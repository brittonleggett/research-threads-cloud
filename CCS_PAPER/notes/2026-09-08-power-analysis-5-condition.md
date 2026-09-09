# 2026-09-08 — Power analysis for the redesigned 5-condition consultation-extent design

Same Monte Carlo method used for Flock earlier today (`FLOCK_CAMERAS_PAPER/notes/
flock_power_analysis_2026-09-08.py`), rerun for CCS's 5-condition design (down from the original
6-level governance-frame idea, per `Conceptual_Model_and_Theory_v2_DRAFT_2026-09-08.md` Section 3).

## Results

**Omnibus 5-group main effect on a mediator** (any condition differs): well-powered at modest N.
Medium effect (Cohen's f=.25): 99.8% power at n=100/cell (500 total). Small-medium effect (f=.15):
92.5% power at n=150/cell (750 total).

**Extreme-condition contrast (no-consultation vs. Tribal-consultation), full mediation chain**:
literature-informed effect sizes (a=.30, b=.40, c'=.10, drawing on Anders et al. 2024's
consultation-effect robustness) reach 75% power at n=150/cell (300 in that pairwise contrast),
87% at n=200/cell. Conservative assumptions (a=.20, b=.30) need n=250-300/cell for comparable
power.

**Adjacent-step contrasts (e.g., affected-community vs. broader-regional consultation) — real
caution here.** A smaller expected step-effect (a=.15) stays underpowered even at large N: only
56% power at n=400/cell. **Practical implication: the design can confidently detect whether
consultation matters at all (the omnibus test) and whether the extremes differ (no-consultation
vs. Tribal), but testing every adjacent pairwise step along the gradient is not realistically
powered at any feasible sample size.** Recommend treating the omnibus effect and the extreme
contrast as the primary confirmatory tests, with adjacent-step comparisons reported as
exploratory/descriptive rather than confirmatory hypothesis tests.

## Suggested target N

Given the above, n=150/cell (750 total) is a reasonable target: well-powered for the omnibus test,
adequately powered (75%) for the primary extreme-contrast test, and consistent with the budget
logic already established for Flock's 4-arm design earlier today. n=200/cell (1,000 total) would
be safer (87% on the extreme contrast) if budget allows.

## Still open

Not yet reconciled with the Louisiana-only vs. Gulf Coast panel-availability question — if
Louisiana-only proves too thin a pool to reach 750-1,000 respondents in reasonable time/cost, the
Gulf Coast regional expansion (Section 6 of the conceptual model doc) becomes the more likely path
independent of this power analysis.
