# 2026-08-16 — Study 2 design memo (AI-drafted, autonomous per Britton's explicit exception)

Proposes how to operationalize the locked theory chain
(`notes/2026-08-16-phase3-theme-review-and-theory-lock.md`) as a fieldable experiment. This is
a design proposal, not a finished, piloted instrument — real scale item text is still pending
(`notes/2026-08-16-scale-sourcing.md`).

## Manipulation: disclosure condition (between-subjects, 2 levels)

Grounded directly in real corpus language rather than a researcher-invented scenario, matching
Tariff Paper's own practice of building vignettes from real messaging:

- **Transparent/local-only condition:** a vignette describing a city adopting an ALPR camera
  network with an explicitly disclosed, publicly posted data-sharing policy limiting access to
  the local police department for local crime-solving purposes only.
- **Secret/broad-access condition:** a vignette describing the same adoption, but where — as in
  Bend's real "National Lookup" episode — a technical default the city did not know about and
  was not told about at adoption time allows federal and out-of-state agencies to query the same
  data. Recommend echoing Capt. Beekman's real language ("we didn't know [X] was a reciprocal
  sharing feature") structurally, without directly quoting a real named official in a fictional
  vignette — paraphrase the mechanism, not the specific case, to avoid conflating the stimulus
  with a real, identifiable news event respondents might recognize and react to as news rather
  than as the intended manipulation.

Single factor, not the 3×2/factorial structure Tariff Paper used — this design has one primary
manipulated antecedent with two theorized moderators (see below), not two crossed manipulated
factors. Flag for Britton: if he wants a second manipulated factor (e.g., crossing disclosure
with an explicit "here's why we need this" necessity-framing manipulation, rather than measuring
perceived necessity as an individual-difference moderator), that would more closely mirror
Tariff's factorial structure and is a legitimate alternative design — his call.

## Moderators

- **Distributive-surveillance-exposure (first-stage, Moderator 1):** proposed as an *archival*
  variable tied to each respondent's actual community (see scale-sourcing note #5), not a
  manipulated or self-report factor. This makes Study 2 a moderated-mediation design with one
  experimentally manipulated antecedent, one archival/measured moderator, and one
  survey-measured moderator — not a fully factorial experiment. Practically, this requires
  either (a) recruiting respondents by geography and linking each to real local camera-density/
  demographic data, or (b) a simpler fallback: a self-report proxy ("to your knowledge, are ALPR
  cameras in your area concentrated in some neighborhoods more than others?") if the archival
  linkage proves infeasible — flagged as a fallback, not the recommended primary approach, since
  self-report awareness and actual disparity are conceptually different things.
- **Perceived crime-solving necessity/efficacy (last-stage, Moderator 2):** measured, not
  manipulated — a survey scale (source: Miethe et al. 2025 construct, see scale-sourcing note).

## Analysis approach

**Recommend PLS-SEM**, matching the established approach across Tariff, Data Center, and CCS
papers — this design's moderated serial-mediation structure (manipulated IV → Mediator 1 →
Mediator 2 → DV, with first-stage and last-stage moderation) is directly analyzable in PLS-SEM
via interaction terms and indirect-effect bootstrapping, consistent with Britton's established
toolkit (see `user_research_corpus.md` re: his PLS-SEM familiarity). Flag one alternative worth
naming: because the manipulation is a true experimental factor (not just measured constructs),
a Hayes PROCESS-style moderated-mediation regression model (Model 15-type: first-stage and
last-stage moderation around a serial mediator chain) is a legitimate and arguably more
standard-in-policy-journals alternative to PLS-SEM for this specific structure — worth
Britton's call given the public-policy venue target (PAR/GIQ-type journals may find
PROCESS/regression-based mediation more familiar to their reviewer base than PLS-SEM, which is
more a marketing/IS convention). Recommend deciding this based on venue commitment, not
defaulting to PLS-SEM purely for cross-paper consistency.

## Sample considerations

- **General population sample is fine for the main effects and serial mediation (H1-H4)**, but
  the first-stage moderator (H5, distributive-surveillance-exposure) needs real variance on that
  moderator to detect an interaction — a sample drawn only from low-disparity-exposure
  communities would have no power to detect it. Recommend either (a) deliberately oversampling
  respondents from documented high-disparity-exposure communities (the corpus itself names real
  candidates: Hampton Roads/Norfolk VA, any other city with a documented CNU-style disparity
  study or DeFlock-trackable deployment pattern), or (b) a large enough general national sample
  that natural variance in local deployment patterns provides sufficient power — (a) is more
  reliable and directly traceable to real corpus evidence, recommend it as primary.
- No IRB concerns beyond what Study 2 experiments normally require (human-subjects survey
  research) — flag for the same IRB-aware treatment as Tariff/Data Center's eventual Study 2s,
  not yet drafted.

## What Britton needs to decide

1. Single-manipulation moderated-mediation design (as proposed) vs. a factorial design crossing
   disclosure with an explicit necessity-framing manipulation.
2. PLS-SEM vs. a Hayes-PROCESS-style regression approach, informed by final venue choice.
3. Archival vs. self-report operationalization of the distributive-surveillance-exposure
   moderator, and whether the data-access work that requires is feasible.
4. Whether to oversample high-disparity-exposure communities and how (this needs real
   geographic/demographic sampling frame work, not a simple panel-vendor quota).
