# Study 1: Method — Manuscript-Ready Draft (2026-08-11)

**Status note (delete before submission):** This is a draft methods section written
in submission-ready academic prose, current as of 2026-08-11. It incorporates two
newly available validation citations (Hill et al. 2026; AlGhamdi 2026) that close the
"no paper validates Claude specifically" gap flagged in the 2026-08-04 justification
note. It does **not** mark Phase 3 (theme review) or the reliability validation pilot
as complete — those remain outstanding per this project's own established rule that
theme review is researcher-only, never AI-run (see `AI_Assisted_TA_Shared_Method.md`).
Sections marked **[PENDING]** need Britton's input or further work before this is
truly submission-ready. Everything else is written as it would read in the manuscript.

---

## Study 1: Method

### Purpose and Theoretical Framing

Study 1 addressed an inductive research question — how do firms discursively frame
tariff-driven price increases to consumers and investors, and what typology of
messaging strategies emerges from actual market practice — with the explicit goal of
grounding the experimental stimuli for Study 2 in real-world messaging patterns rather
than researcher-generated hypotheticals. The analysis was informed by three
theoretical lenses: dual entitlement theory (Kahneman, Knetsch, & Thaler, 1986), which
holds that firms are perceived as entitled to pass through unavoidable cost increases
but not to raise prices opportunistically; prospect theory's framing effects
(Kahneman & Tversky, 1979; Tversky & Kahneman, 1981); and psychological reactance
theory (Brehm, 1966), which predicts resistance to price changes perceived as
unexplained or non-consensual.

### Data

The corpus consisted of publicly available corporate communications — earnings-call
transcripts, official press statements, and price bulletins — addressing tariff-driven
pricing decisions, drawn from **15** firms spanning apparel, toys, automotive, HVAC,
building materials, home goods, furniture, and food service **[PENDING: finalize at
15–20 per standard thematic-analysis sampling conventions; 7 artifacts are coded from
primary or high-quality secondary transcripts, 8 remain draft-coded from secondary
news coverage pending primary-source (8-K exhibit, investor-relations page)
verification before final analysis]**. Because the corpus consists exclusively of
publicly available corporate disclosures with no interaction with or data collection
from human subjects, Study 1 was determined exempt from IRB review under 45 CFR
46.102(e).

### Analytic Approach

Consistent with a growing body of methodological guidance on AI-assisted qualitative
analysis (Braun & Clarke, 2006, 2019; Xu, 2026; Naeem, Smith, & Thomas, 2025), Study 1
employed a **small-q, coding-reliability thematic analysis** — distinct from Braun and
Clarke's "Big Q" reflexive tradition, which treats researcher subjectivity as the
locus of quality and explicitly rejects reliability statistics as a validity marker.
Because Study 1's themes were intended to ground a confirmatory quantitative program
(Study 2's experimental manipulation, Study 3's structural model), a coding-reliability
framing — in which agreement between coders is reported as evidence of trustworthiness
— was the methodologically consistent choice.

Coding was conducted through a human–AI collaborative workflow using Claude (Anthropic),
following an established six-phase procedure adapted from Naeem et al. (2025) and
consistent with the practice documented in Xu (2026) and Goyanes, Lopezosa, and Jordá
(2025): (0) optional quantitative triage of the corpus, (0.5) briefing the model on the
research question, data source, and theoretical frame, (1) deductive and inductive
coding of individual artifacts, (2) clustering of codes into candidate themes, (3)
review and refinement of candidate themes, (4) definition and naming of finalized
themes, and (5) write-up. Consistent with the precedent established in Xu (2026),
**Phase 3 (theme review) was conducted by the researcher alone, without AI
involvement** — a deliberate methodological choice reflecting the judgment that
recursive, contextual theme refinement is not a task current models perform reliably
without a human interpretive check.

### Reliability and Validity

The growing empirical literature on LLM-assisted thematic and qualitative coding
provides a basis for confidence in this approach while also indicating its limits.
In a blinded comparison against human analysts, Hill et al. (2026) found Claude 4
Sonnet achieved deductive-coding agreement (93.5%; Gwet's AC1 = .93) statistically
indistinguishable from, and numerically exceeding, trained human coders (92.7%;
AC1 = .92) on a comparable corpus. AlGhamdi (2026), evaluating Claude Code
specifically against a human/NVivo baseline, reported a pattern of **hierarchical
convergence**: agreement at the level of individual codes was more variable than
agreement at the level of higher-order themes, and structured, multi-phase prompting
produced more stable alignment than single-shot prompting — the prompting approach
adopted here. Both studies, along with Misra et al. (2026) and prior work in this
literature, converge on a consistent pattern: agreement is highest for
descriptive/semantic coding and lower for latent, interpretive coding, a pattern this
study's own validation is expected to replicate and is reported against rather than
treated as a surprise if it emerges.

**[PENDING — required before submission]** A validation pilot has not yet been
conducted for this corpus. Per standard practice in this literature, a subsample of
the corpus should be independently coded by a second human coder and compared against
both (a) the AI-assisted coding and (b) the primary researcher's own coding, with
agreement reported at both the code level and the theme level using an appropriate
statistic (Gwet's AC1 or Cohen's Kappa). Quote verification — confirming that
AI-selected supporting quotations in fact substantiate their assigned code — and
reporting of any error rate should accompany this pilot, per Hill et al.'s (2026)
explicit recommendation.

### Coding Procedure and Preliminary Themes

**[PENDING — provisional, awaiting final Phase 3 sign-off]** Inductive coding of the
corpus to date has surfaced five candidate themes, subject to the researcher's
ongoing review: (1) *restraint signaling*, in which firms frame price actions as the
minimum necessary response; (2) *causation attribution*, ranging from explicit
naming of tariffs as cause to vague or silent framing, present in some form across
the full corpus and the strongest candidate for a theoretically motivated
experimental manipulation; (3) *mitigation-effort narrative*, in which price increases
are paired with visible internal cost-reduction or sourcing efforts; (4)
*normalization through relabeling*, in which price increases are framed as routine
rather than exceptional; and a fifth, single-case-supported candidate,
(5) *asymmetric disclosure* between price increases and decreases, which requires
additional corpus support before being treated as a stable theme. A sixth candidate —
*full-absorption promise*, surfaced in the corpus-expansion pass and not present in
the original seven artifacts — remains an open Phase 3 decision as to whether it
constitutes a distinct theme or a variant of restraint signaling.

### AI-Use Disclosure

Consistent with emerging disclosure norms in this literature (Xu, 2026; Naeem et al.,
2025), the authors disclose that AI assistance (Claude, Anthropic) was used in corpus
coding (Phases 1–2) and theme-naming support (Phase 4). Theme review (Phase 3) and all
substantive interpretive judgments were conducted by the authors without AI
involvement. [Full disclosure statement to be finalized in acknowledgements per
journal requirements.]

---

## What still needs to happen before this section is submission-ready

1. Decide which of the 8 corpus-expansion artifacts get primary-source verification
   (8-K exhibits, investor-relations pages) vs. get dropped — target 15–20 finalized.
2. Complete Phase 1 coding on any retained expansion artifacts using primary sources.
3. Conduct Phase 3 theme review (researcher-only) on the full finalized corpus,
   including the "full-absorption promise" Theme 6 decision.
4. Run the validation pilot: second human coder on a subsample, code-level and
   theme-level agreement statistics, quote verification, documented error rate.
5. Finalize the N and update this draft's placeholder language accordingly.
