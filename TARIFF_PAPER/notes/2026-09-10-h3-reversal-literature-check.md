# 2026-09-10 — H3 reversed per Britton's instruction, literature check before finalizing

## What happened

Britton reviewed the theory draft's open item #2 (H3, the interaction hypothesis,
unresolved since 2026-09-04) and gave a specific, detailed reversal instruction: keep
the interaction, but flip its predicted direction, reframing it as a compensatory/
cue-substitution interaction (partial absorption already supplies behavioral evidence
of fair intent, so verbal attribution matters *less* under absorption and *more* under
full pass-through, where it's the only cue available) rather than the original
"two good things amplify each other" framing. He supplied a provisional hypothesis and
asked for literature verification before finalizing — this note is that verification.

**Direction change:**
- **Old (2026-08-04 draft):** attribution's fairness benefit is *amplified* under
  shared-burden absorption, *attenuated* under full pass-through.
- **New (Britton's instruction, 2026-09-10):** attribution's fairness benefit is
  *stronger* under full pass-through, *weaker* under shared-burden absorption.

## What was checked, and what it found

**Kelley (1972), discounting principle / compensatory causal schema — directly
supports Britton's mechanism, high confidence.** Verified via multiple independent
WebSearch results (not a single source) describing the actual content of Kelley's
1972 chapter "Causal schemata and the attribution process," in Jones, Kanouse, Kelley,
Nisbett, Valins, & Weiner (Eds.), *Attribution: Perceiving the Causes of Behavior*
(General Learning Press). The discounting principle: the causal role of a given cause
is discounted to the degree other plausible causes for the same effect are present.
Kelley specifically names a **compensatory causal schema** for cases where causes are
"perceived as continuous and inversely related to each other" — this is close to an
exact match for the mechanism Britton described (cost absorption and verbal
attribution as substitutable, not additive, routes to the same fair-intent inference).
This is the strongest, most directly on-point finding of the check. The original 1972
book chapter's full text was not pulled (it predates open digital archives); the
principle's content is corroborated across several independent secondary/summary
sources rather than a single one, which is the standard used elsewhere in this
project for citations that can't be full-text verified.

**Kirmani & Rao (2000) and Connelly et al. (2011), signaling theory — supports the
costly-vs-cheap-signal framing used to justify *why* cost absorption counts as strong
evidence.** Both citations verified (journal, volume, issue, pages) via WebSearch
against publisher/database records. Core mechanism confirmed from abstracts/
secondary descriptions: signal power scales with cost, because costly signals are
harder for a low-quality/opportunistic actor to fake. A direct PDF pull of Kirmani &
Rao (2000) was attempted (found a public PDF via Carlson School of Management) but
failed — this environment's PDF text-extraction tooling is currently broken (same
poppler-utils/pypdf gap already flagged in `notes/2026-09-10-litigation-recheck-
section301-...md` for the Tariff docket PDF). The general mechanism is solid; the
exact terminology Kirmani & Rao use for their signal typology was not independently
confirmed word-for-word, and the write-up avoids quoting specific typology labels for
that reason.

**Campbell (1999), price-fairness/inferred-motive literature — no direct evidence
either way.** Re-confirmed the citation itself (Journal of Marketing Research, 36(2),
187–199) but found nothing in the available search results specifically testing
whether verbal justification's impact changes depending on whether accompanying
behavioral/costly evidence is present. This is consistent with treating the specific
interaction as this paper's extension, not a replication of an existing price-fairness
finding — which is exactly how the rewritten section frames it.

**Follow-up check, same day: Xia, Monroe & Cox (2004) and Bolton, Warlop & Alba
(2003) — gap now closed, no contrary evidence.** Got full text of Xia, Monroe & Cox
(2004) directly (a real PDF, not a search summary — `storage` at seekscholar.com,
read in full via this session's PDF tool). It is the standard price-fairness
literature *review* — a conceptual/propositional paper (nine propositions, P1–P9),
not an experiment — and it does not test, hypothesize, or discuss an attribution ×
cost-response interaction of any kind, substitution or additive. Its closest relevant
passage: "buyers may accept a firm's goodwill motive even when the higher price is
not due to cost-related factors and is controlled by the company (Campbell 1999)" —
broadly consistent with a substitution logic (a goodwill/motive signal can stand in
for a cost-based cause) but stated about motive-inference generally, not the specific
cost-absorption/verbal-attribution redundancy this paper proposes. Nothing in the
paper's discussion of attribution, controllability, or its own citation of Bolton,
Warlop & Alba (2003) — "consumers respond more unfavorably if a perceived price
inequality is due to a firm's volitional intentions or actions (internal locus of
causality and controllability) (Bolton, Warlop, and Alba 2003; Vaidyanathan and
Aggarwal 2003)"; "making the seller's costs salient reduces people's estimate of a
firm's profit margin... not all costs are equally legitimate (Bolton, Warlop, and
Alba 2003)" — addresses whether justification and behavioral cost evidence combine
additively or substitutably. Bolton, Warlop & Alba (2003)'s own full text was not
independently pulled (JSTOR/Oxford Academic paywalled, ResearchGate and SciSpace both
returned empty/blocked pages to this session's fetch tools) — this check relies on
Xia et al.'s own extensive, multi-point citation of it (in the Appendix's results
summary and four further in-text citations) as the secondary-source substitute,
consistent with this project's standing convention for sources that can't be
full-text verified directly. **Conclusion: the "no prior price-fairness study tests
this specific interaction" claim in the manuscript holds up under a full-text check
of the field's own standard review, not just an abstract-level one.** This gap is now
closed.

## Bottom line for Britton

**No contrary evidence found.** The compensatory/discounting mechanism you described
maps cleanly onto Kelley's (1972) own compensatory causal schema — this isn't just
compatible with your logic, it's close to the canonical example of it, which makes H3
more defensible than the original amplifying version, not less. Your provisional
hypothesis wording was already clean and was kept close to verbatim (see the rewritten
"The Interaction" section in `Introduction_and_Theory_DRAFT_2026-08-12.md` and the
mirrored section in `Tariff_Manuscript_Working_Draft_2026-09-04.md`). The follow-up
check of Xia/Monroe/Cox (2004) and Bolton/Warlop/Alba (2003) (above) closes the one
gap flagged earlier the same day — full text of the field's own standard review
confirms it doesn't test this interaction either, so the "genuine extension, not a
replication" framing in the manuscript is on solid ground. Bolton/Warlop/Alba (2003)'s
own full text is still paywalled everywhere this session could reach — worth a direct
pull via your library access if a reviewer specifically challenges this point, but not
blocking.

## Files changed
- `TARIFF_PAPER/Introduction_and_Theory_DRAFT_2026-08-12.md` — rewrote the H2 bridge
  sentence, the full "Interaction" section, H3 itself, and the checklist item.
- `TARIFF_PAPER/Tariff_Manuscript_Working_Draft_2026-09-04.md` — mirrored the same
  changes (it duplicates this section) and added Kelley (1972), Kirmani & Rao (2000),
  and Connelly et al. (2011) to its reference list, each with a verification-status
  note matching this file's existing convention.
