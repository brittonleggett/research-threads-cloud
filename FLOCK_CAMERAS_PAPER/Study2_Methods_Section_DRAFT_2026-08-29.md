# Study 2: Method — Draft (2026-08-29)

**Status note (delete before submission):** AI-drafted, under Britton's standing one-time exception
for this paper (`notes/2026-08-16-phase3-theme-review-and-theory-lock.md`). This is the first prose
Method-section draft for Study 2 — until now, the design lived only in scattered notes (the
2026-08-16 design memo, the 2026-08-19/08-20 instrument-adaptation notes, the 2026-08-21 IRB draft,
and the 2026-08-27 instrument-assembly document). This section synthesizes those into a single
manuscript-shaped draft, written to stay accurate under **either** branch of the two design calls
still explicitly reserved for Britton (archival vs. self-report Moderator 1; single-manipulation vs.
factorial; PLS-SEM vs. Hayes-PROCESS) — nothing below decides any of the three. Study 2 has not been
fielded. There is no Results section and there will not be one until it runs. Nothing here has been
reviewed by Britton.

**2026-09-20 sync note (AI-run, under the standing 2026-08-16 Phase 3 exception):** this draft still
described the original 2-condition disclosure manipulation and an unresolved single-manipulation-
vs.-factorial call. Britton actually decided this on 2026-09-08
(`notes/2026-09-08-four-arm-vignette-draft.md`): a **4-arm single-factor between-subjects design**
(neutral / safety-benefit / broad-network-access / disparate-impact), plus a new pre-exposure
**baseline trust in police** moderator and a real Monte Carlo power analysis. This resolves the
single-manipulation-vs.-factorial call (the actual answer was neither original option) but leaves
the archival-vs.-self-report and PLS-SEM-vs.-Hayes-PROCESS calls open, unchanged. Sections below are
updated to match; `Study2_Instrument_DRAFT_2026-08-27.md` was synced the same session.

**2026-09-23 addition (AI-drafted, under the standing exception):** the baseline-trust-in-police
screener item wording (Measures below), previously flagged "not yet drafted," is now drafted — see
`notes/2026-09-23-baseline-trust-screener-pitts-citation-and-municipal-wave-verification.md`.

---

## Study 2: Method

### Design Overview

**Revised 2026-09-20 — see sync note above.** Study 2 tests the theory chain locked in Study 1
(`Introduction_and_Theory_DRAFT_2026-08-16.md`; `notes/2026-08-16-phase3-theme-review-and-theory-
lock.md`) via a **single-factor, 4-level (4-arm), between-subjects experimental vignette design**
with moderated serial mediation. The manipulated factor is condition content — neutral/baseline,
safety-benefit, broad-network-access, or disparate-impact (`notes/2026-09-08-four-arm-vignette-
draft.md`; supersedes the original 2-condition transparent-vs.-secret disclosure manipulation) —
mirroring Study 1's own candidate themes directly rather than a single disclosure/non-disclosure
contrast. The design retains the paper's locked mediation structure: the manipulated condition
predicts perceived procedural injustice (Mediator 1), which predicts institutional trust
(Mediator 2), which predicts opposition intention (DV) — moderated at the first stage by prior
distributive-surveillance-exposure (H5) and at the last stage by perceived crime-solving
necessity/efficacy (H6) (`Introduction_and_Theory_DRAFT_2026-08-16.md`). A **baseline trust in
police** measure, collected before vignette exposure, was added 2026-09-08 as an additional
first-stage moderator/covariate not part of the original locked H1-H6 chain — see Measures below.

**Design calls now resolved (2026-09-08, Britton):**
- **4 arms, not the originally-considered 5** — a wrongful-stop/accuracy-harm arm was dropped to
  control CloudResearch fielding cost.
- **Between-subjects, not within-subjects** — Britton's explicit call for publishability in
  policy/public-administration journals.
- **Single-factor 4-level, not a 2×2 factorial** crossing disclosure with a necessity-framing
  manipulation — this closes the design-call question the 2026-08-29 draft of this section left
  open; the actual answer was neither of the two originally-considered options.

**Still open, unchanged:** archival vs. self-report operationalization of Moderator 1 (Section 8 of
the instrument document), and PLS-SEM vs. Hayes-PROCESS analysis approach.

### Participants

**Revised 2026-09-20.** Per Britton's 2026-09-08 decision, the main study will be fielded on
**CloudResearch**, with a **student/convenience sample used for the pilot** (cost management;
`notes/2026-09-08-four-arm-vignette-draft.md`) — a change from the earlier plan to use Prolific
throughout, matching Tariff Paper's Study 2 platform (`notes/2026-08-21-irb-application-draft.md`'s
Recruitment Procedure section). CloudResearch vs. Prolific cost is roughly at parity per a
peer-reviewed comparison checked 2026-09-08 (Peer et al., PMC10013894: Prolific ≈$1.90/high-quality
respondent vs. CloudResearch ≈$2.00), correcting an earlier assumption in project notes that
CloudResearch was meaningfully cheaper; head-to-head turnaround time remains unverified and will be
treated as an open question until the first actual CloudResearch field. Sample restricted to U.S.
adult residents (18+, screened at entry — see Procedure). Standard attention-check and
English-fluency screening items are embedded in the survey flow
(`Study2_Instrument_DRAFT_2026-08-27.md`, Section 2). The pilot sample requires its own IRB coverage
even though it is a convenience sample, not exempt simply because it is informal
(`notes/2026-09-08-four-arm-vignette-draft.md`) — IRB submission for both the pilot and the main
study has not yet been started (Britton's 2026-09-08 call to defer this and prioritize CCS Paper
work first).

**Sample size and power analysis — run 2026-09-08** (Monte Carlo simulation via numpy/scipy;
script not yet copied from that session's scratchpad into this project folder, per
`notes/2026-09-08-four-arm-vignette-draft.md`), **replacing the earlier N=500-800 placeholder**.
Power differs sharply by which test is asked of the data:

1. **Omnibus 4-group main effect on the mediator** (any condition differs): well-powered even at
   modest per-cell N — a medium effect (Cohen's f = .25) reaches ~99% power at n=100/cell (400
   total); even a small effect (f = .15) reaches 88% power at n=150/cell (600 total).
2. **Planned contrast, neutral vs. disparate-impact, full mediation chain (H4-style serial
   mediation through both mediators)**: needs more. Using Merola, Lum & Murphy (2018)'s own
   observed trust-erosion effect (d = .33, **citation verified 2026-09-20** via Crossref, DOI
   10.1007/s11292-018-9332-8, *Journal of Experimental Criminology*, 15(1), 55-66) as the a-path
   and a moderate mediator-to-DV link (b = .40), n=150/cell (300 in the pairwise contrast) gives
   ~75% power; n=200/cell reaches ~87%. A more conservative assumption (a = .20, b = .30) needs
   n=300/cell for comparable power — the real target depends on how much this literature-informed
   effect-size assumption is trusted.
3. **Moderated first-stage interaction (baseline-trust-in-police × condition), the hardest to
   power.** Realistic field-research interaction effect sizes are small (β ≈ .10-.20, per
   McClelland & Judd 1993's general point that interactions are almost always smaller than main
   effects — **citation verified 2026-09-20** via Crossref, DOI 10.1037/0033-2909.114.2.376,
   *Psychological Bulletin*, 114(2), 376-390). At those sizes, even n=300-400/cell reaches only
   50-70% power under a plain random sample, motivating the oversampling design below.

**Oversampling design for the moderated interaction test.** Rather than a naive "screen and keep
only the extremes" approach, this design follows the technique Preacher, Rucker, MacCallum, &
Nicewander (2005, *Psychological Methods*, 10(2), 178-192, DOI 10.1037/1082-989x.10.2.178 —
**citation verified 2026-09-20** via Crossref) identify, via McClelland & Judd (1993) and Pitts
(1993), as the better alternative to the pure extreme-groups approach (EGA) for interaction/
moderation power specifically: **oversample the tails of baseline trust in police while retaining a
reasonable share of midrange respondents**, then analyze the moderator continuously rather than
dichotomizing it — McClelland & Judd's own finding is that removing the middle entirely is "unwise"
and that adding it back "can only increase power." **Pitts (1993) citation now verified 2026-09-23**
by reading Preacher et al. (2005)'s own reference list directly (open-access author PDF,
quantpsy.org, text-extracted and checked): **Pitts, S. C. (1993). The utility of extreme groups
analysis to detect interactions among correlated predictor variables. Unpublished master's thesis,
Arizona State University, Tempe.** Confirms this session's standing inference that it was an
unpublished, secondhand-cited source (a master's thesis, specifically, not a dissertation as
previously guessed) — this is exactly why no Crossref/OpenAlex/Semantic Scholar record exists; it
was never published. Correctly cited here as a secondary citation (Pitts, 1993, as cited in
Preacher, Rucker, MacCallum, & Nicewander, 2005), which is standard practice for an unpublished,
unobtainable primary source.

- **Mechanics:** field a short baseline-trust-in-police screener to a broad initial pool, collect
  each respondent's platform participant ID via a URL parameter, then build a follow-up invite list
  weighted toward low- and high-trust scorers (not excluding the middle) and invite that list to
  the full paid Study 2 instrument. Confirmed as a real, documented workflow on Prolific (a "custom
  allowlist" screener keyed to prior-study participant IDs); not yet confirmed whether CloudResearch
  supports an equivalent mechanic — check once the account exists.
- **Reporting caveat for the eventual Results section:** oversampling inflates R² and standardized
  effect sizes for the moderator test but does not bias unstandardized regression coefficients
  (assuming linearity) — report the interaction in raw coefficient terms, not only standardized
  effect size, and disclose the oversampling design explicitly to reviewers.
- **Regression-to-the-mean risk:** someone extreme on trust at screening may not remain as extreme
  by the time they take the main study — run the two waves close together in time to limit this.

**Sampling consideration for H5** (prior distributive-surveillance-exposure, the paper's original
locked first-stage moderator, distinct from the new baseline-trust-in-police moderator above):
detecting this effect also requires real variance on that moderator. The design memo's
recommendation to deliberately oversample respondents from communities with documented disparity
patterns (e.g., Hampton Roads/Norfolk VA, or other DeFlock-trackable high-disparity deployment
areas identified in the Study 1 corpus) remains unaddressed by the 2026-09-08 session's oversampling
design above, which targets the baseline-trust moderator specifically — real geographic-sampling-
frame work for H5 is still not done, and remains an open operational item.

### Procedure

**Revised 2026-09-20.** After electronic informed consent and screening
(`Study2_Instrument_DRAFT_2026-08-27.md`, Sections 1-2), participants complete the **baseline
trust in police** measure (Section 2b) before any exposure to the manipulation. Participants are
then randomly assigned with equal probability to one of **four** vignette conditions (Section 3)
describing a fictitious city ("Meridian Falls") adopting an ALPR camera network: neutral/baseline,
safety-benefit, broad-network-access, or disparate-impact (Section 4) — replacing the original
2-condition transparent-vs.-secret disclosure manipulation. A brief forced minimum-time-on-page
delay discourages skimming, matching Tariff Paper's own instrument convention. Participants then
complete the shared manipulation-check item and confound-check items (Sections 5-6), the Mediator 1
(procedural injustice), Moderator 1 (if the self-report branch is used), Mediator 2 (institutional
trust), and Moderator 2 (crime-solving necessity) measures, the DV (opposition intention), and a
demographics battery, before receiving a full debriefing (Sections 7-13). Estimated completion time
is 10-12 minutes, compensated at the panel's academic rate (target ~$12.00/hour, matching Tariff
Paper's own rate — `notes/2026-08-21-irb-application-draft.md`, Compensation section); exact rate
on CloudResearch not yet separately confirmed.

### Measures

Full item wording, response formats, and source citations for every construct are in
`Study2_Instrument_DRAFT_2026-08-27.md`; this subsection summarizes sourcing and verification
status for the Method write-up.

- **Manipulation check and confound checks** are study-specific, with no literature source needed
  (standard practice for experimental-vignette manipulation checks; modeled structurally on Tariff
  Paper's own manipulation/confound battery, including reuse of the Hovland & Weiss 1951 Source
  Credibility Model items for the credibility confound check).
- **Mediator 1 (perceived procedural injustice)** and **Mediator 2 (institutional trust)** are
  adapted from the Quality of Decision Making and Trust in Police subscales, respectively, of
  Reisig, Bratton, & Gertz (2007, *Criminal Justice and Behavior*, 34(8), 1005-1028). Item wording
  was pulled directly from the source article's Table 2 via full-text access (Ole Miss/SAGE
  Journals), then adapted to the camera-network context and given a face-validity desk review that
  revised three items for construct-contamination and double-barreling risk against the verified
  source wording (`notes/2026-08-16-scale-sourcing.md`; `notes/2026-08-20-face-validity-review-scale-items.md`).
  Both subscales use the source's original 4-point response format (1 = *strongly disagree* to
  4 = *strongly agree*).
- **Moderator 2 (perceived crime-solving necessity/efficacy)** is adapted from Miethe, Dudinskaya,
  Forepaugh, & Sousa (2025, *Crime & Delinquency*, 71(4), 1025-1051), a two-item paired
  agree/disagree measure with no internal-consistency statistic available in the source (noted here
  as a real limitation, not smoothed over — see Limitations below).
- **DV (opposition intention)** is adapted from van Zomeren, Spears, Fischer, & Leach (2004, *Journal
  of Personality and Social Psychology*, 87(5), 649-664), Study 2's 4-item collective-action-
  tendency scale (α = .84 in the source), 7-point Likert (1 = *not at all* to 7 = *very much*).
- **Moderator 1 (prior distributive-surveillance-exposure)** has no validated published scale
  (`notes/2026-08-16-scale-sourcing.md`, construct #5) and instead branches on an open design call:
  an **archival** measure (per-respondent camera-density/demographic-disparity score, computed by
  linking ZIP/tract data to Flock deployment or DeFlock-tracker data cross-referenced with Census
  tract data) or, as a fallback, a **single self-report item**
  (`Study2_Instrument_DRAFT_2026-08-27.md`, Section 8). Which branch is used is Britton's decision,
  not resolved by this draft.
- **Baseline trust in police** (new pre-exposure moderator/covariate, added 2026-09-08, not part of
  the original locked H1-H6 chain). **Item wording drafted 2026-09-23**: rather than a new,
  unvalidated custom screener, this reuses the same validated 4-item Trust in Police subscale already
  sourced for Mediator 2 — Reisig, Bratton, & Gertz (2007, *Criminal Justice and Behavior*, 34(8),
  1005-1028; DOI `10.1177/0093854807301275`, re-confirmed via Crossref 2026-09-23) — administered
  pre-exposure with the source's original general-community referent ("police in your community"),
  not the camera-network-specific referent used post-exposure in Mediator 2, both to fit the
  pre-exposure flow (participants haven't yet been told about Meridian Falls or its camera network)
  and to avoid a repeated-item demand effect. Full item text and scoring in
  `Study2_Instrument_DRAFT_2026-08-27.md`, Section 2b. A targeted search this session for a
  purpose-built short-form trust-in-police screener (distinct from the full scales already in this
  project) did not surface one; reusing an already-verified field-tested subscale was judged more
  defensible than constructing new items. Motivated by Merola, Lum, & Murphy (2018)'s own
  future-research call regarding their high-trust Fairfax County sample (**citation verified
  2026-09-20**, DOI 10.1007/s11292-018-9332-8).

**Verification status, stated plainly:** all four literature-sourced constructs above (Mediators 1
and 2, Moderator 2, the DV) have been checked at the item-wording level against directly-pulled
source text, not reconstructed from memory or WebSearch summaries alone — the fullest verification
tier this project's own standing practice defines. No Study 2 measure remains at a lower
verification tier as of this draft.

### Manipulation and Confound Checks

**Revised 2026-09-20:** the manipulation check is now a single shared 4-option item across all four
conditions, which doubles as a cross-contamination check (`Study2_Instrument_DRAFT_2026-08-27.md`,
Section 5; redesigned 2026-09-08, superseding the original per-condition forced-choice recall
item). Pass-fail criteria were set before piloting, not post hoc: a strong main effect of condition
on the continuous clarity item, ≥80% correct on the shared forced-choice item per condition, and no
significant between-condition difference on any confound-check item
(`notes/2026-08-19-instrument-adaptation-and-manipulation-checks.md`). Both checks are retained in
the main study instrument for data-quality screening, not run only as a separate pretest — matching
Tariff Paper's own practice.

### Planned Analysis

**Not yet decided (Britton's call, per `notes/2026-08-16-study2-design-memo.md`):** whether the
moderated serial-mediation model is estimated via PLS-SEM (matching the established approach across
Tariff, Data Center, and CCS papers) or a Hayes PROCESS-style moderated-mediation regression model
(a legitimate, arguably more reviewer-familiar alternative given this paper's public-policy/public-
administration venue target, where PLS-SEM is less conventional than in marketing/IS journals). Both
approaches are analytically compatible with the design as instrumented; the choice affects the
eventual Results section's statistical presentation, not anything in this Method section or the
instrument itself. If PLS-SEM is used, reliability/validity reporting will follow the thresholds in
`Claude_Knowledge/AI Research Workflows/PLS-SEM Standards Checklist.md`.

### Pilot Testing

**Not yet run.** The instrument document's scale items received a literature-grounded face-validity
desk review (`notes/2026-08-20-face-validity-review-scale-items.md`). The *original 2-condition*
vignette text received a face-validity desk review on 2026-08-27 that surfaced four concerns (a
factual documentation error, a sentence-complexity mismatch between conditions, both conditions
likely exceeding the instrument's stated ~8th-grade reading-level target, and a possible confound
between Condition B's framing and perceived government incompetence —
`notes/2026-08-27-webfetch-retry-and-study2-vignette-face-validity-review.md`); two of these were
mechanically fixed 2026-08-29. That design has since been **superseded by the 4-arm design**
(2026-09-08), whose v2 wording was directly built with the reading-level lesson applied and
measured via real Flesch-Kincaid checks (FK 7.6-9.7 across the four conditions, 2026-09-09 —
`notes/readability_check_2026-09-09.py`), rather than inheriting the original design's unresolved
13.7-14.9 gap. **None of this substitutes for an actual human pilot with real respondents**, which
remains the single highest-priority step before fielding anything — no condition in either design
has been pilot-tested with real respondents.

### Limitations (to carry into the eventual manuscript)

- Moderator 2 (crime-solving necessity) is measured with two single items with no internal-
  consistency statistic available, inherited from the source study's own reporting practice, not a
  design choice made for convenience.
- Moderator 1's operationalization is not yet settled (archival vs. self-report), and the archival
  branch's feasibility (real data access to Flock deployment records or the DeFlock tracker at
  ZIP/tract granularity) has not been confirmed.
- The new baseline-trust-in-police moderator now reuses a validated published scale (Reisig,
  Bratton & Gertz 2007's Trust in Police subscale) rather than an invented custom screener
  (drafted 2026-09-23); still not piloted with real respondents.
- No validation pilot has been run on any measure with actual respondents; all face-validity work
  to date is desk review against source text, real Flesch-Kincaid calculations, and general
  vignette-methodology principles, not empirical piloting.
- The 4-arm single-factor design (revised 2026-09-20) tests condition content as the sole
  experimental factor; a wrongful-stop/accuracy-harm fifth arm was considered and dropped for cost
  reasons, and it does not test an explicit necessity-framing manipulation crossed with condition,
  which a factorial extension could address if Britton reconsiders that design instead.
- Oversampling on baseline trust in police (for the moderated-interaction test) inflates R² and
  standardized effect sizes for that test; unstandardized coefficients remain unbiased under
  linearity, but this must be disclosed explicitly to reviewers.

---

## What still needs to happen before this section is submission-ready

**Updated 2026-09-20 — see sync note at the top of this file.**

1. Britton's resolution of the two remaining reserved design calls (archival-moderator feasibility,
   PLS-SEM vs. Hayes-PROCESS) — this draft is written to remain accurate either way, but the final
   manuscript needs one committed answer per call. The single-manipulation-vs.-factorial call is
   now resolved (4-arm single-factor, 2026-09-08).
2. Final target N — the Monte Carlo power analysis (2026-09-08) replaced the N=500-800 placeholder
   with test-specific figures (see Sample size and power analysis above), but still depends on the
   PLS-SEM-vs-PROCESS decision and which effect-size assumption is trusted.
3. An actual human face-validity pilot of the 4-arm vignette and scale items — still not run.
4. Baseline-trust-in-police screener item wording — **drafted 2026-09-23** (reused Reisig, Bratton
   & Gertz 2007 subscale, general referent). Still not piloted.
5. IRB submission and approval, covering both the pilot and CloudResearch main study (draft
   application exists — `notes/2026-08-21-irb-application-draft.md` — not yet formally submitted;
   Britton's 2026-09-08 call to defer this).
6. Resolution of the geographic-oversampling operational question for H5 (how to identify and
   recruit from documented high-disparity-exposure communities through a panel platform) if
   Moderator 1's archival branch is adopted — distinct from, and still unaddressed by, the
   2026-09-08 baseline-trust oversampling design.
7. Confirmation of whether CloudResearch supports a Prolific-style custom-allowlist follow-up-invite
   mechanic, needed for the baseline-trust oversampling design.
