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

---

## Study 2: Method

### Design Overview

Study 2 tests the theory chain locked in Study 1 (`Introduction_and_Theory_DRAFT_2026-08-16.md`;
`notes/2026-08-16-phase3-theme-review-and-theory-lock.md`) via a single-factor, two-condition,
between-subjects experimental vignette design with moderated serial mediation: a manipulated
disclosure condition (transparent/local-only vs. secret/broad-access-default data-sharing policy)
predicts perceived procedural injustice (Mediator 1), which predicts institutional trust
(Mediator 2), which predicts opposition intention (DV) — moderated at the first stage by prior
distributive-surveillance-exposure and at the last stage by perceived crime-solving
necessity/efficacy (H1-H6, `Introduction_and_Theory_DRAFT_2026-08-16.md`).

**Open design call, not resolved here:** whether this remains a single-manipulation design (as
described above) or is expanded to a 2×2 factorial crossing disclosure with an explicit
necessity-framing manipulation is Britton's call (`notes/2026-08-16-study2-design-memo.md`). This
section describes the single-manipulation version as the base case; a factorial extension would
add a second manipulated factor and corresponding hypotheses without changing the measures,
procedure, or recruitment approach described below.

### Participants

Participants will be recruited through an online research panel (Prolific, matching the recruitment
platform used in Tariff Paper's own Study 2 — `notes/2026-08-21-irb-application-draft.md`'s
Recruitment Procedure section), restricted to U.S. adult residents (18+, screened at entry — see
Procedure). Standard attention-check and English-fluency screening items are embedded in the
survey flow (`Study2_Instrument_DRAFT_2026-08-27.md`, Section 2).

**Sample size:** target N = 500-800, currently a placeholder pending a formal a priori power
analysis (flagged as outstanding in both the IRB draft and the design memo — not run as of this
draft, since it depends on the PLS-SEM-vs-PROCESS analytic decision below). This range reflects the
IRB draft's own reasoning that a moderated serial-mediation design with two moderators needs a
larger sample than a simple two-group mean comparison, not a calculated target.

**Sampling consideration specific to this design:** detecting the first-stage moderation effect
(H5, prior distributive-surveillance-exposure) requires real variance on that moderator. A sample
drawn only from communities with little documented camera-placement disparity would have low power
to detect this interaction regardless of overall N. The design memo recommends deliberately
oversampling respondents from communities with documented disparity patterns (e.g., Hampton
Roads/Norfolk VA, or other DeFlock-trackable high-disparity deployment areas identified in the
Study 1 corpus) rather than relying on natural variance in a general national sample — this requires
real geographic-sampling-frame work not yet done, and is noted as an open operational item, not a
theoretical one.

### Procedure

After electronic informed consent and screening (`Study2_Instrument_DRAFT_2026-08-27.md`, Sections
1-2), participants are randomly assigned with equal probability to one of the two vignette
conditions (Section 3) describing a fictitious city ("Meridian Falls") adopting an ALPR camera
network, differing only in whether the network's data-sharing policy was disclosed and limited to
local law enforcement (transparent condition) or included an undisclosed default allowing broader
federal/out-of-state access (secret condition) (Section 4). A brief forced minimum-time-on-page
delay discourages skimming, matching Tariff Paper's own instrument convention. Participants then
complete manipulation-check and confound-check items (Sections 5-6), the Mediator 1 (procedural
injustice), Moderator 1 (if the self-report branch is used), Mediator 2 (institutional trust), and
Moderator 2 (crime-solving necessity) measures, the DV (opposition intention), and a demographics
battery, before receiving a full debriefing (Sections 7-13). Estimated completion time is
10-12 minutes, compensated at the panel's academic rate (target ~$12.00/hour, matching Tariff
Paper's own rate — `notes/2026-08-21-irb-application-draft.md`, Compensation section).

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

**Verification status, stated plainly:** all four literature-sourced constructs above (Mediators 1
and 2, Moderator 2, the DV) have been checked at the item-wording level against directly-pulled
source text, not reconstructed from memory or WebSearch summaries alone — the fullest verification
tier this project's own standing practice defines. No Study 2 measure remains at a lower
verification tier as of this draft.

### Manipulation and Confound Checks

Pass-fail criteria were set before piloting, not post hoc: a strong main effect of disclosure
condition on both manipulation-check items, ≥80% correct recall per condition on the forced-choice
item, and no significant between-condition difference on any confound-check item
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
desk review (`notes/2026-08-20-face-validity-review-scale-items.md`); the vignette text received a
separate face-validity desk review on 2026-08-27 that surfaced four concerns (a factual
documentation error, a sentence-complexity mismatch between conditions, both conditions likely
exceeding the instrument's stated ~8th-grade reading-level target, and a possible confound between
Condition B's framing and perceived government incompetence — `notes/2026-08-27-webfetch-retry-and-study2-vignette-face-validity-review.md`).
Two of these were mechanically fixed 2026-08-29 (see `notes/2026-08-29-vignette-mechanical-fixes-and-buildout.md`
and `Study2_Instrument_DRAFT_2026-08-27.md` Section 4); the reading-level gap was reduced but not
closed, and the government-incompetence confound question was deliberately left for Britton's
judgment rather than resolved unilaterally. **None of this substitutes for an actual human pilot
with real respondents**, which remains the single highest-priority step before fielding anything.

### Limitations (to carry into the eventual manuscript)

- Moderator 2 (crime-solving necessity) is measured with two single items with no internal-
  consistency statistic available, inherited from the source study's own reporting practice, not a
  design choice made for convenience.
- Moderator 1's operationalization is not yet settled (archival vs. self-report), and the archival
  branch's feasibility (real data access to Flock deployment records or the DeFlock tracker at
  ZIP/tract granularity) has not been confirmed.
- No validation pilot has been run on any measure with actual respondents; all face-validity work
  to date is desk review against source text and general vignette-methodology principles, not
  empirical piloting.
- Single-manipulation design (as described above) tests disclosure as the sole experimental factor;
  it does not test whether an explicit necessity-framing manipulation would interact with
  disclosure, a question a factorial extension could address if Britton chooses that design instead.

---

## What still needs to happen before this section is submission-ready

1. Britton's resolution of the three reserved design calls (archival-moderator feasibility,
   single-manipulation vs. factorial, PLS-SEM vs. Hayes-PROCESS) — this draft is written to remain
   accurate either way, but the final manuscript needs one committed answer per call.
2. A real a priori power analysis to replace the N=500-800 placeholder, which depends on the
   PLS-SEM-vs-PROCESS decision above.
3. An actual human face-validity pilot of the vignette and scale items — still not run.
4. IRB submission and approval (draft application exists — `notes/2026-08-21-irb-application-draft.md`
   — not yet formally submitted).
5. Resolution of the geographic-oversampling operational question (how to identify and recruit from
   documented high-disparity-exposure communities through a panel platform) if Moderator 1's
   archival branch is adopted.
