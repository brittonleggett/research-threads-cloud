# Study 1 — Concept and Corpus Plan (Section 10)

Status: planning/scoping draft, 2026-09-03. Corpus inclusion criteria must be
finalized and reviewed before any mass coding begins (per project research
standards). This is NOT a locked design — it proposes a feasible approach for
Britton to approve, adjust, or reject.

## Candidate research question
How do supply-chain actors (processors, USDA/agencies, producer associations,
retailers) attribute responsibility for meat-price changes and justify
outcomes for producers vs. consumers in public discourse?

This mirrors the TARIFF_PAPER Study 1 purpose (build an inductive typology of
corporate messaging strategies) more than the CCS_PAPER Study 1 purpose
(characterize *consumer* discourse) — the corpus here is actor-generated
(corporate, agency, trade-association) communication, not netnography of
ordinary consumers. Method label should therefore be **AI-assisted
thematic/content analysis of institutional discourse**, not netnography — see
the divergence table in
`Claude_Knowledge/Thematic Analysis/AI_Assisted_TA_Shared_Method.md`.

## Method (adopt the shared six-phase engine as-is)
Same engine used across TARIFF_PAPER and CCS_PAPER — see
`Claude_Knowledge/Thematic Analysis/AI_Assisted_TA_Shared_Method.md` for the
full phase-by-phase protocol (Phase 0 optional quant triage → 0.5 brief the
LLM → 1 coding → 2 theme generation → 3 human-only theme review → 4 defining/
naming → 5 write-up), the validation plan (manual+LLM pilot subsample,
agreement statistic — Cohen's Kappa or Gwet's AC1, report honestly whichever
fits), and the netnography/data-ethics checklist (mostly N/A here since this
is institutional/corporate speech, not consumer-generated content, but the
AI-bias-check-against-manual-subsample item still applies).

**Branding decision:** use small-q/coding-reliability TA, explicitly branded
as such (or "systematic thematic analysis" per Naeem et al. 2025) — not
reflexive/Big-Q TA — consistent with the shared-method doc's warning that
mislabeling is the most common reviewer-bait mistake in this literature, and
consistent with both sister papers' choice.

Opening/framing citations for the methods section, per the shared-method doc:
Epp & Humphreys (2025, *JCR*) first (qualitative/thematic-analysis framing),
Berger et al. (2020, *JM*) second (automated-text-methods-in-marketing
legitimacy claim).

## Candidate corpus actors
- Processors: Tyson Foods, JBS USA (and JBS S.A. parent where relevant),
  Cargill (Cargill Protein), National Beef, Smithfield Foods (WH
  Group-owned), and major poultry processors (e.g., Pilgrim's Pride,
  Perdue, Sanderson Farms/Wayne-Sanderson) — confirm current corporate
  structure/ownership before finalizing this list; ownership has changed
  historically (e.g., Smithfield/WH Group) and needs a current-as-of-2026
  check.
- Government/regulatory: USDA (Secretary statements, ERS/AMS releases),
  USDA press office, FSIS.
- Producer/trade associations: National Cattlemen's Beef Association
  (NCBA), R-CALF USA (notably more adversarial toward packers/imports than
  NCBA — useful for capturing genuine intra-producer-side disagreement,
  not just a single "farmer voice"), National Pork Producers Council,
  National Chicken Council, United Egg Producers (if poultry scope extends
  to eggs — likely out of scope; poultry here means meat, confirm).
- Retailers: only if a specific retailer statement is directly on-topic
  (e.g., testimony or a price-related public statement) — the brief's own
  guidance is not to over-include retailers/politicians unless directly
  relevant to *policy discourse* about pricing.
- Politicians/government officials: only when directly tied to policy
  discourse (e.g., a Secretary of Agriculture press conference on beef
  prices, a DOJ/FTC statement on a packer investigation) — not general
  campaign rhetoric.

## Candidate artifact types
Earnings calls/transcripts, SEC filings (10-K risk-factor and MD&A
language on input costs/margins is often more candid and useful than press
releases), press releases, corporate investor-relations webpages,
Congressional testimony (House/Senate Agriculture Committee hearings are the
most likely venue), USDA statements/press releases, producer-association
statements and testimony, public comments on relevant rulemakings (e.g., the
COOL-related dockets — see `NOTES/COOL_Regulatory_Timeline.md` once drafted),
trade-group position documents.

## Candidate inductive/deductive coding starting concepts (NOT to be imposed
— themes must emerge from the actual corpus; this list is only a sensitizing
starting point per Phase 0.5 briefing)
Input-cost attribution, labor-cost attribution, inflation attribution,
supply-shortage attribution, foreign-import attribution, regulatory
attribution, retailer attribution, farmer attribution, processor attribution,
consumer-demand attribution, margin justification, shared burden, producer
protection, consumer protection, national food security, fairness,
transparency, domestic sourcing, foreign sourcing, efficiency, competition,
market-power accusations.

## Time window and event anchors (to be finalized with Britton)
Candidate anchor period: 2020–2026, to capture COVID-era supply-chain
disruption, 2021–2023 high food inflation, any DOJ/FTC packer-concentration
investigations or COOL-rule changes in that window, and current (2026)
discourse. Exact start date should be set once
`NOTES/COOL_Regulatory_Timeline.md` and `LITERATURE/Market_Concentration_
Evidence.md` identify the most theoretically relevant anchor events (e.g., a
DOJ investigation announcement, a specific price spike) rather than an
arbitrary calendar cutoff.

## Open scoping questions for Britton (do not resolve unilaterally)
1. Beef-only Study 1, or beef+pork+poultry in one corpus with commodity as a
   coded/moderating attribute? The commodity-structure differences documented
   in `NOTES/Commodity_Structure_Comparison.md` may argue for beef as the
   anchor case (richest public discourse, clearest producer/consumer price
   narrative) with pork/poultry as a smaller comparison slice — mirroring how
   DATA_CENTER_PAPER kept Louisiana as the anchor case in a multi-state
   design rather than treating all states identically.
2. Include R-CALF USA (adversarial, pro-tariff/anti-concentration producer
   group) alongside NCBA (more industry-establishment-aligned) to capture
   genuine intra-producer disagreement, or is that scope creep?
3. How far to lean into SEC-filing language (10-K/10-Q, earnings-call
   transcripts) vs. public-facing press releases — filings are more candid
   about margin drivers but are also more legally hedged/boilerplate; may
   need both, coded separately.
4. IRB status: this is public corporate/government/trade-association
   documents, not human-subjects data — should qualify for exempt status
   analogous to TARIFF_PAPER's Study 1 (45 CFR 46.102(e)), but confirm before
   assuming.

## Explicit instruction followed
Corpus inclusion criteria (actor list, artifact types, time window, inclusion/
exclusion rules) must be documented and reviewed with Britton before mass
coding begins. This document is that inclusion-criteria draft, not a
green light to start coding.
