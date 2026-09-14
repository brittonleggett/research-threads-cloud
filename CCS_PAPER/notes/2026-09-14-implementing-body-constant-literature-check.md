# 2026-09-14 — Literature-grounding check on the "implementing-body-constant" design choice (informational only — not a decision, Britton's call stays Britton's)

**AI involvement disclosure:** produced by an AI agent (Claude) doing autonomous overnight
literature-grounding work on this repo. This note does not decide anything — it's legwork meant to
help Britton evaluate the open item, flagged as such per tonight's task instructions.

**What this is:** `Conceptual_Model_and_Theory_v2_DRAFT_2026-09-08.md` Section 3 holds "implementing
body" (LDENR with EPA Region 6 oversight) constant across all five vignette conditions rather than
manipulating it, on the strength of one citation — Anders, Liebe & Meyerhoff (2024, Nature Climate
Change) — which the draft says found implementing-body type did *not* significantly affect CCS
acceptance, while consultation-extent did. Section 8's open-items list flags "implementing-body-
constant confirmation" as still open. Tonight I went back to that paper directly (via an open
preprint, not the paywalled published version — see sourcing note below) to check whether the
draft's characterization of it is accurate, rather than taking the earlier session's summary of it
on faith.

## What the source actually says

Found and read the open-access preprint (Research Square, `rs-3405741/v1`,
"Cross-border CO2 Transport Decreases Public Support for Carbon Capture and Storage" — same
authors/study as the published Anders, Liebe & Meyerhoff 2024 *Nature Climate Change* 14, 692–695,
DOI 10.1038/s41558-024-02023-0; title differs slightly between preprint and final publication, as is
normal). This is a legitimate open preprint, not a paywalled full-text pull, so it's fine to quote
directly per this repo's copyright rule.

The study is a multifactorial vignette (discrete-choice-style) experiment across five countries
(Canada, Germany, Netherlands, Norway, UK; 988–1,021 respondents per country), varying **seven
attributes**: implementation body, proximity to respondent's residence, CO2 mitigative capacity,
geographical origin of CO2 emissions, extent of public consultation in CCS approval, extent of
information on seismicity risk, and compensation to affected communities.

Direct quote of the relevant finding:

> "attributes deemed to increase public involvement positively affect evaluations of CCS for
> fairness... and acceptance... Our results clearly show that consulting the public during the CCS
> approval process, providing transparency through information sharing on the seismic and CO2
> leakage risks of CCS matter irrespective of the country studied... **Interestingly, neither the
> potential mitigative contribution of CCS to CO2 removal nor the type of implementing body, and
> thus possible differences in public trust between CCS stakeholder groups, appear to matter to
> views on CCS on either side of the Atlantic.**"

**This confirms the draft's characterization is accurate**, not a loose paraphrase: the paper does
directly report (a) consultation extent and risk-information transparency as attributes that
significantly moved both fairness and acceptance ratings across all five countries, and (b)
implementing-body type as an attribute that did not appear to matter, in the same breath as CO2
mitigative capacity. So the CCS_PAPER design's choice to hold implementing body constant while
manipulating consultation extent has direct empirical support from exactly the source cited for it —
this isn't a citation being stretched further than it holds.

## Caveats worth Britton's attention before treating this as settled support

1. **Geography and CCS-maturity mismatch.** All five countries in the source study (Canada, Germany,
   Netherlands, Norway, UK) have far more mature, higher-salience public CCS discourse than Louisiana
   currently does. A null finding on "implementing body doesn't matter" in publics already fairly
   CCS-aware may not transfer cleanly to a US Gulf Coast sample where CCS is newer and where
   distrust of specific institutional actors (state regulator LDENR specifically, versus industry)
   could plausibly be a live, salient axis in a way it wasn't in the source study's populations. The
   source paper doesn't claim to test a US or Gulf Coast sample at all.
2. **"Implementing body" as operationalized there may not map exactly onto LDENR/EPA Region 6.** I
   could not find the specific level-set used for the implementing-body attribute (e.g., "government
   agency" vs. "industry operator" vs. "public-private partnership") in the portion of the preprint I
   could access without the supplementary tables (Table S2/S3, referenced but not reproduced in the
   main text I read) — those tables would show the exact wording/levels tested. Worth pulling the
   supplementary material (openly available alongside the preprint/published article, not paywalled)
   before treating the null finding as squarely on-point for a "state regulator vs. industry vs.
   federal" framing specifically, if that's closer to what the original May 2026 6-condition design
   had in mind.
3. **One study, one null result.** This is the paper's own novel finding, not (as far as this pass
   found) something independently replicated elsewhere in the CCS-acceptance literature yet. I did
   not find, in tonight's limited search, another PLS-SEM or discrete-choice CCS/pipeline study that
   separately tests and confirms (or contradicts) a null implementing-body effect — this pass wasn't
   long enough for a full second-citation search, and I don't want to claim corroboration I didn't
   actually find. If Britton wants this locked down further, a next step would be a dedicated search
   for other CCS/pipeline acceptance studies (e.g., the Sovacool, Baum & Fritz 2024 and Lefstad et
   al. items already flagged as not-yet-full-text-pulled in the conceptual model doc's Section 8 item
   6) specifically for whether any of them test operator/implementing-body type as a factor.

## Bottom line (informational, not decisional)

The literature does say what the draft says it says — this specific concern about the citation being
over-read is not supported; the quote is squarely on point. What's still open, if Britton wants more
before locking the constant-implementing-body choice: (a) pull the supplementary tables to confirm
the exact implementing-body levels tested lines up with LDENR/EPA Region 6 framing, and (b) decide
how much weight a five-country European/Canadian null result should carry for a Louisiana-specific
design, given CCS-discourse-maturity differences the source study doesn't address. Neither of those
is resolved here — flagging for Britton's judgment, not deciding either way.
