# 2026-09-08 — Digest of CCS_Lit_Review_Foundation.docx (Britton's own, dated 2026-05-22)

Converted from the binary .docx (Read tool can't handle .docx directly — extracted via zipfile/
XML parsing of word/document.xml). Full extracted text at
`AppData\Local\Temp\claude\...\scratchpad\ccs_lit_review_extracted.txt` this session, not yet
copied into the project — worth saving a clean .md version here since the original will need
re-extraction if referenced again. This predates the whole Claude-assisted CCS thread (started
2026-07-23) by two months and was never referenced during Track C's build-out.

## What it is

A commissioned literature-review foundation for a paper titled **"Beyond Public Acceptance:
Procedural Justice, Indigenous Rights, and the Social License for Carbon Capture Deployment,"**
target journal **Energy Research & Social Science (ERSS)**. 51 peer-reviewed core sources
(numbered B1-B58, some consolidated), every DOI verified against the Crossref API at compile
time. Organized in 8 parts (A: outline, B: annotated sources, C: thematic tagging, D: six
theoretical anchors ranked primary/supporting, E: methodological precedents, F: a full defensible
conceptual model with hypotheses, G: gap statement + draft contribution paragraph, H: methodological/
ethical cautions specific to Indigenous-rights research).

## The conceptual model (Part F) — already fully worked out

**Causal chain:** Governance frame (manipulated) → procedural justice perception + recognition
justice perception → institutional trust (competence-based and integrity-based, Terwel et al.
2009) → perceived legitimacy → support for CCS infrastructure.

**Proposed manipulation:** governance frame as a 6-level factor — (a) state regulator approval,
(b) industry technical expertise, (c) local referendum/voting, (d) property-rights protection,
(e) affected-community consultation, (f) Tribal/Indigenous consultation — plus a control/no-frame
condition. Optionally crossed 2×3 with frame strength (token vs. substantive), leveraging Walker
et al. (2014)'s "boomerang effect" finding (late-stage compensation framed as a "bribe" backfires).

**Mediators:** Tyler's (2003) four-item procedural justice battery (voice, neutrality,
trustworthiness, dignitary treatment); recognition justice perception; institutional trust
(competence/integrity split); perceived legitimacy (Gehman, Lefsrud & Fast 2017 cues + Tyler
legitimacy items).

**Moderators/controls specified with sources for each:** landowner status (Chewinski et al.
2023), rural identity (Bergquist et al. 2020; Cha 2020), political ideology (Pianta et al. 2021),
proximity to existing CCS/oil-and-gas infrastructure (Krause et al. 2014; Cox et al. 2021), prior
oil/gas household employment (Cha 2020), climate concern (Devine-Wright & Batel 2017), perceived
economic/environmental benefits (Walker et al. 2014; Thomas et al. 2018), safety risk perception
(Krause et al. 2014; Terwel et al. 2009), pre-treatment trust in scientists/government/industry
(Terwel et al. 2009), CCS familiarity (L'Orange Seigo et al. 2014). Indigenous/Tribal
identification explicitly flagged as **sub-sample-only, not a general moderator** — see ethics
section below.

**Six hypotheses (H1-H6)** already drafted, roughly: consultation-type frames > industry/regulator
frames on procedural justice; procedural + recognition justice → trust; trust → legitimacy;
legitimacy → support; the whole chain is a mediation; frame effects moderated by landowner
status/rural identity/ideology/proximity.

## Real, specific US Gulf Coast + CCS-specific anchor already found

**Atkinson, Dankel & Romanak (2024, Frontiers in Marine Science)** — factorial survey across
Texas, Louisiana, and Florida on CCS monitoring-message acceptance; community-member endorsements
performed on par with or better than scientist endorsements for some publics. The lit review
flags this as the principal existing empirical anchor for Gulf Coast CCS acceptance and recommends
following its sampling approach, "but explicitly oversample in proximity to active Louisiana Class
VI permitted sites if feasible."

**Alexander & Stanley (2022, Environment and Planning E)** — "the single most directly relevant
peer-reviewed article": theorizes CCS in Alberta's tar sands as a "colonial flanking mechanism"
legitimizing extraction on Indigenous lands. The only peer-reviewed paper applying a
settler-colonial analytic to CCS specifically — flagged as a primary theoretical interlocutor, not
background.

## Part H — ethics/methods guardrails on the Indigenous-rights angle (read this before touching
that angle at all)

Explicit, detailed, and worth following closely if this direction is pursued:
- The manuscript can measure **general/regional public** reactions to a Tribal-consultation
  governance *frame* — that is a study of settler/general-public attitudes toward an
  institutional frame, not a study of Indigenous attitudes, and the two must never be conflated.
- Cannot claim to speak to Indigenous nations' substantive views on CCS/FPIC/consent without
  actual Tribal-government engagement and Indigenous research methodology — that requires
  Tribal-government partnership, not survey-panel self-identification.
- Do NOT sub-analyze "Indigenous respondents" incidentally captured in a general-population
  panel — report numbers transparently if they appear, draw no community-level inferences from
  them.
- Recommends an explicit "Scope and limitations regarding Indigenous research" Methods subsection,
  a positionality note (non-Indigenous marketing scholar), and reaching out to Louisiana's
  federally-recognized Tribal nations' formal liaison offices (**Coushatta Tribe of Louisiana,
  Chitimacha Tribe of Louisiana, Tunica-Biloxi Tribe of Louisiana, Jena Band of Choctaw**) plus the
  state-recognized **United Houma Nation** — even a courtesy notice — if the manuscript will claim
  any implications for Indigenous communities.
- Recommends pre-registering the experimental design on OSF before data collection.
- Explicitly flags the SLO-research-reproduces-developer-framing risk (Owen & Kemp 2013; Batel
  2018; Boutilier 2021) — position the paper as testing *whether* SLO can be redefined through
  procedural/recognition justice, not as measuring how much social license CCS firms currently
  enjoy.

## The real tension with today's (2026-09-08) Track C differentiation test — flagged for Britton,
not resolved here

This lit review's model and today's Track C reframed lead theory
(`2026-09-08-theoretical-differentiation-test.md`: technology-legibility/EOR-confusion +
institutional-legitimacy-manipulation/astroturfing) are **not the same paper**. They share almost
no theoretical vocabulary — this lit review never mentions astroturfing, push-polling, or the
CO2-storage-vs-EOR confusion angle; Track C's corpus never surfaced governance-frame variation,
recognition justice, or Indigenous/Tribal consultation (the CCS project memory already flagged
that "the Coushatta/Tribal-consultation story from the 07-23 lit scan never surfaced on Reddit at
all" — this lit review explains *why that gap matters theoretically*, not just that it's a data
gap). The lit review is also far more rigorous: 51 sources verified via Crossref DOI lookup
(most reachable, several full-text-confirmed like Rodriguez 2023 was for Track C's Theme 3),
versus today's astroturfing-pillar pass, which only reached search-snippet-level verification on
its best citations.

**This is a real fork for Britton to choose, not something to quietly merge:**
- **Path 1 — stay with Track C** (astroturfing/EOR-confusion, Reddit-corpus-grounded, GO-decided
  today). Thinner literature currently, but already has a real Study 1 corpus built and coded.
- **Path 2 — pivot to this lit review's governance-frame/energy-justice/SLO design.** Far more
  rigorously grounded, has a complete Study 2 design and even a drafted contribution paragraph
  already, targets a specific real journal (ERSS) with a stated gap-in-the-literature argument —
  but would need a different Study 1 approach (or possibly no netnography-style Study 1 at all;
  the lit review's own draft doesn't assume one) since Reddit discourse doesn't capture
  governance-frame variation or Tribal-consultation framing.
- **Path 3 — some hybrid**, e.g., keep Track C's corpus as motivating/illustrative material in the
  Introduction while running Study 2 on this lit review's governance-frame design instead of an
  astroturfing-derived manipulation — plausible but not yet worked out, and it's not obvious the
  two theories combine cleanly rather than reading as two different papers stapled together.

**Not decided here.** This is exactly the kind of design-lock decision that's been Britton's call
on every paper in this pipeline — flagging clearly rather than picking one and building it out.

## Practical next step suggested by the lit review itself, if Path 2 or 3 is chosen

"Suggested next steps" (Part G/end of document) says to pull full texts of six most-contemporary
anchors first: Alexander & Stanley (2022), Stephanides et al. (2025), Anders et al. (2024), San
Román-Niaves et al. (2026), Minadakis & Vega-Araújo (2024), Ó Maonaigh et al. (2025) — via Ole
Miss library/Consensus.app, not yet done.
