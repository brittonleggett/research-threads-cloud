# PLS-SEM reporting standards & moderated-mediation workflow (2026-08-11)

Britton is already an expert in PLS-SEM (see [[user_research_corpus]] — it's his
default empirical method across all 5 of his read papers, and his native model
shape is a mediated chain plus a context moderator). This doc isn't a tutorial
for him — it's a **standards checklist I can check his tables/output against**
so I can actually flag problems instead of just nodding along.

Sources (real transcripts pulled via yt-dlp):
- "How to use smartPLS: Tutorial, Reporting Standards and Guidelines" — webinar
  by Dr. Faizan Ali (USF, M3 research center), citing Hair/Ringle/Sarstedt and
  Henseler & Sarstedt's current PLS-SEM literature (youtube.com/watch?v=RcN3dSTanjA)
- "Moderated Mediation in SmartPLS" — worked SmartPLS demo
  (youtube.com/watch?v=aPMR9A_1Ecw)

## The 4-stage process (Hair et al. framing)

1. **Determine the research goal** — PLS-SEM is built for exploratory/prediction-
   oriented theory-building, not strict confirmatory testing. If the goal is
   truly confirmatory (testing an established theory in normally-distributed
   data with a large sample), CB-SEM is the better tool — or PLSc (PLS-consistent),
   which bridges the two. Worth naming explicitly in a paper's method
   justification, since reviewers ask "why PLS" constantly.
2. **Structural model specification** — define direct paths, indirect/mediation
   paths, and moderation (interaction) paths as explicit hypotheses before
   touching the software.
3. **Measurement model specification** — decide reflective vs. formative per
   construct, single- vs. multi-item, and whether any construct is a
   higher-order (hierarchical component) model.
4. **Model estimation and results evaluation** — the checklist below.

## Reflective construct assessment (Stage 1 / outer model)

| Criterion | Threshold | Notes |
|---|---|---|
| Indicator (item) loadings | > 0.708 | Don't reflexively delete an item below this — if AVE is still ≥0.5 with it in, it can often stay; only drop when deletion clearly improves AVE/reliability. |
| Cronbach's alpha | 0.7–0.95 | Below 0.7 = unreliable; **above 0.95 is also a flag** (item redundancy/near-duplicate wording), not a win. |
| Composite reliability (CR) | 0.7–0.95 | Same upper-bound caveat as alpha. |
| rho_A | > 0.7 | Newer measure, sits between alpha (conservative) and CR (liberal) — worth reporting alongside both. |
| AVE (convergent validity) | > 0.5 | Construct's items explain at least half its variance. |
| Discriminant validity — HTMT | < 0.85 (current) | Older standard was <0.90 — cite whichever your target journal's recent papers use, but 0.85 is the safer/current bar. Fornell-Larcker is the older method; if HTMT fails, Fornell-Larcker usually does too — **don't cherry-pick whichever one passes**, go find the actual data problem (usually two constructs that are conceptually too close). |

## Formative construct assessment (different logic — do NOT apply reflective rules)

- No loadings/reliability/AVE — instead check: convergent validity, collinearity, and indicator significance/relevance.
- **VIF < 3.3** (current standard; older/looser thresholds said <5 or <10 — 3.3 is the defensible one now).
- Get indicator significance via bootstrap (t-value/p-value) on the **outer weights**, not loadings.
- **Retain/drop decision rule (formative only):**
  - weight significant → keep, full stop.
  - weight not significant but loading > 0.5 → still keep (item has value even if not a top driver).
  - weight not significant AND loading < 0.5 → only then is dropping defensible.
  - Rationale: deleting a formative indicator changes the construct's definition (unlike reflective, where items are interchangeable proxies for the same thing) — this is the opposite instinct from reflective cleanup and worth double-checking he's not applying reflective logic to a formative construct by habit.

## Structural model assessment (Stage 2 / inner model)

- Report path coefficients (β), t-statistics/p-values, **and bootstrapped
  confidence intervals** (bias-corrected, from bootstrap resampling) — a
  relationship is non-significant if its CI straddles zero, regardless of the
  point estimate's sign.
- **Bootstrap subsamples: 5,000–10,000**, not the software default of 500/1000 —
  worth checking any of his output before it goes to a reviewer.
- R² bands are field-relative — no universal good/bad cutoff, calibrate to what's
  typical in marketing/consumer behavior venues rather than a generic rule of thumb.
- **Model fit (SRMR, NFI, dULS/dG, RMStheta) is still contested in PLS-SEM** —
  useful mainly for *comparing alternative models* in an exploratory design,
  not as an absolute goodness-of-fit claim the way CB-SEM reviewers might expect.
  SRMR < 0.08 and NFI > 0.90 are the usual bars if reported at all; RMStheta was
  flagged as still under active development — avoid leaning on it.

## Common method bias

Not PLS-specific — it's a data-collection design issue, not a statistical one.
Design-stage remedies (temporal separation of IV/DV measurement, psychological
separation via different question sections/instructions, methodological
separation via different scale formats) are the credible fix. Post-hoc
statistical tests (Harman's single factor, marker-variable technique) are
weaker evidence reviewers are increasingly skeptical of — worth knowing which
kind of defense a manuscript is leaning on.

## Moderated-mediation testing procedure (matches his recurring chain+moderator shape)

Straight from the SmartPLS demo, and directly useful given [[user_research_corpus]]'s
note that his native structure is "antecedent → mediator → outcome, reshaped by
a context moderator" (Twitter followers in the MLB paper, sales subculture in
the gritty-salespersons paper, hybrid/office in [[project_remote_work_study]]):

1. **Test the plain mediation model first** — path analysis + bootstrap on the
   indirect effect, before adding any moderator. Establish full vs. partial
   mediation as the baseline.
2. **Add one candidate moderator at a time**, on one specific path (a, b, or c) —
   draw the moderator's path onto that link, let the software generate the
   interaction/product term, then bootstrap again.
3. **Check the interaction term's significance.** If it's non-significant, that
   variable doesn't moderate that path — remove it and either try a different
   path or a different candidate moderator, rather than forcing the story.
4. Only report a moderated mediation finding once the interaction term itself
   clears significance in the bootstrap — the demo's worked example rejected
   one candidate moderator (trust) before finding a second one (earning) that
   actually worked, which is the normal/expected pattern, not a failure.

## Staying current

Both sources point to `smartpls.com/documentation` (specifically the
"Recommended Readings" / "Literature" pages) as an actively maintained tracker
of new PLS-SEM methods papers — worth a periodic check since thresholds
(HTMT, VIF) have moved multiple times in the last decade and will likely move
again.
