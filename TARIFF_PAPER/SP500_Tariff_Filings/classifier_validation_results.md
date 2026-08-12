# Classifier Validation — Fresh Sample, Post-Resolution

## Methodology

A fresh random sample (seed 777, non-overlapping with the 25 filings read in
`validation_sample.md`) was pulled from the final corpora after the 227 ambiguous filings were
manually resolved (see `ambiguous_resolved.csv`): **20 filings from the `trade` bucket** and
**15 from the `utility_only` (excluded) bucket**. Each filing's matched snippet (~400 chars
around the "tariff" occurrence) was read independently and judged against its assigned label,
without looking at how the automated classifier or the ambiguous-resolution pass had reasoned
about it.

## Results

**Trade bucket: 20/20 agree (100% precision on this sample).** Every sampled filing was
genuine trade-tariff discussion — tariff cost impacts, IEEPA/Section-232 references, "trade
and tariff policy" risk-factor language, supply-chain/sourcing tariff exposure, etc. Two
filings are worth flagging specifically because they show the classifier correctly
disambiguating *within* companies that also have utility-sense tariff mentions elsewhere in
the corpus: PSE&G (T12, "tariffs, curtailments by suppliers" — a fuel-supply-chain trade-tariff
risk, correctly separated from PSE&G's *other* filings about "commodity supply tariffs," which
are utility-rate-sense and correctly excluded — see U3/U11 below) and Exelon (T16, "significant
increases in relevant tariffs" on supply chain/materials — correctly separated from Exelon's
earlier utility "recovered under separate tariffs" mention). This is a meaningful sanity check:
the classifier isn't just excluding by sector, it's distinguishing by sense within the same
filer.

**Utility_only bucket: 15/15 agree (100% precision on this sample).** Every sampled filing was
a genuine non-trade "tariff" sense — FERC market-based rate tariffs (NRG, Constellation Energy,
Xcel Energy), state PUC/PSC rate filings and rate schedules (American Water Works, PPL,
Alliant Energy generic legal boilerplate, Dominion Energy), and utility rate/tariff programs
(DTE's green tariff program, PSE&G's commodity supply tariffs).

**Combined: 35/35 agreement on this fresh sample.**

## Honest caveats

- n=35 is a sanity-check sample, not a full audit. It supports the classifier as a defensible
  first-pass filter; it does not prove zero errors exist across the full 1,891-filing trade
  corpus or 118-filing excluded set.
- All judgments here (and in the ambiguous-resolution pass) were made by the same
  process (careful reading by the AI assistant), not by an independent second human coder.
  For actual journal submission, standard practice is a second, independent human coder on a
  subsample with a reported inter-rater statistic (Cohen's Kappa or % agreement) — this
  validation sample is evidence of internal consistency, not inter-rater reliability in the
  formal sense the shared AI-assisted TA method's validation-plan section calls for.
- The 100% agreement rate is higher than typical validation numbers reported in the AI-assisted
  coding literature (e.g. GAATA's Kappa of 0.94, not 1.0) — plausible here because this is a
  comparatively easy *binary sense-disambiguation* task (trade vs. utility meaning of one word)
  rather than *latent thematic coding*, which is a fundamentally harder judgment call. Don't
  extrapolate this precision rate to any later thematic/framing coding done on this corpus.

## Recommended next step before citing this number in a methods section

Have a second independent reader (Britton, a coauthor, or a second AI pass with no visibility
into the first pass's reasoning) code a fresh sample and report agreement formally with Cohen's
Kappa, per the validation-plan convention in
`Claude Knowledge\Thematic Analysis\AI_Assisted_TA_Shared_Method.md`.
