# 2026-08-16 — Primary-source verification pass 1 (artifacts #12-17)

Follows up on `2026-08-15-corpus-expansion-pass1-websearch-only.md`, which added artifacts
#12-17 (bringing the corpus to 17) but flagged all six as WebSearch-summarized only, not
directly fetched — one step short of this project's primary-source standard. That pass ran
inside the cloud routine, which was hitting a WebFetch `EGRESS_BLOCKED` failure; this pass ran
in an interactive session where WebFetch worked fine (confirming the block is
routine-environment-specific, not a general tool failure). Direct-fetched primary sources
below for all six; two sub-items (NOLA CPC's exact MW threshold, one workforce-housing detail)
remain WebSearch-only where direct fetch was blocked (nola.com blocks WebFetch entirely —
403 on every URL tried; two other outlets hit 429/402).

---

### 12. Meta wins secrecy fight before Louisiana PSC — VERIFIED, corrected
Fetched directly: Fox8, American Press.
- **Vote:** 3-1, Wednesday **August 12, 2026** (not the 13th — that's when it was reported).
  Confirmed voting to allow confidentiality: **Jean-Paul Coussan** (R, District 2). Dissenting:
  **Davante Lewis** (D). The other two majority votes weren't named in either source fetched.
- **Administrative Law Judge: Melanie Verzwyvelt** (confirmed, American Press) — her original
  subpoena covered job-creation, investment, and power-consumption data; Meta declined citing
  trade secrets; PSC quashed the subpoena on the 3-1 vote.
- **No docket/case number found** in either source — still open if needed for the paper.
- **Real quotes, direct:**
  - Coussan: "What you're looking for is more granular data, and that's fine, I just don't
    think it's necessarily appropriate relative to our role right here."
  - Lewis: "So when the Governor and the president and Meta and Entergy says they're paying
    their fair share for their contract, but their contract is not the lifespan of the
    infrastructure that we're building."
  - Lindsay Garcia (Democratic congressional candidate, public comment, American Press):
    on NDAs — "Trust us, we're bringing jobs" amounts to "demanding it from us" rather than
    requesting trust. Strong line for the procedural-exclusion/trust theme.
- **Correction to original note:** did not find Alliance for Affordable Energy or Union of
  Concerned Scientists quotes in either article — the original note's framing of them as the
  subpoena's originators wasn't contradicted, just not independently re-confirmed here.

### 13. New Orleans CPC zoning proposal — VERIFIED, one real correction
Direct fetch of nola.com blocked (403, both the original URL and the Gambit version — appears
to be a site-wide WebFetch block, not a dead link). Filled in via thecooldown.com (direct
fetch) and WebSearch triangulation across nola.com/Gambit, WGNO, veritenews headlines.
- **Exact date: August 6, 2026** (original note flagged this as TBC).
- **Size threshold confirmed: under 100,000 sq ft** citywide.
- **Correction — distance requirement was wrong in the original note.** Original said "≥500 ft
  from residential property." Actual (per WebSearch of the nola.com/Gambit piece): data centers
  in industrial districts must be **three blocks from all residentially zoned properties**, and
  **500 feet from one another** (i.e., 500 ft is a facility-to-facility spacing rule, not a
  facility-to-residence one). Worth fixing in the corpus coding.
- **MW power-draw threshold (≤20 MW) from the original note: not confirmed by any source
  checked this pass** — flag as unverified, don't cite without a source. May have been a
  WebSearch-summary error on 8/15, or a real detail in a source not yet found.
- **New quote, strong for the paper:** JP Morrell (City Council President), on the legal
  ambiguity itself: "We want to make it clear to all parties that until we figure out what the
  hell a data center is in the law... we are clearly stating that... under whatever definition
  you put out there, data centers are not permitted." Good primary material for a
  regulatory-ambiguity/institutional-improvisation angle, distinct from the secrecy theme.
- Context confirmed: proposal is explicitly framed as smaller than Meta's 4-million-sq-ft
  Richland Parish facility; the Jan 2026 moratorium has to be formally lifted before any new
  rule takes effect.

### 14. Amazon $12B Caddo/Bossier announcement — VERIFIED
Direct fetch of KSLA succeeded cleanly.
- **Feb 23, 2026**, $12B, 540 direct jobs (≥150% statewide average wage), 1,700 more
  community-supported jobs, ~1,500 construction jobs.
- **New detail not in the original note:** **$400M water infrastructure investment**, and
  **SWEPCO will fully fund new energy infrastructure at no cost to Louisiana ratepayers** —
  directly relevant to Theme 3 (institutional distrust of utility cost promises); this is the
  actual promise the paper's later artifacts (e.g. #12's Lewis quote about contract lifespan)
  can be read as pushing back against.
- Quotes confirmed: Gov. Landry, Amazon's David Zapolsky, and Justyn Dixon (NLEP) on
  transmission-line redundancy.

### 15. Sierra Club-backed appeal, Resilient Tech Park — VERIFIED, corrected
Direct fetch of Shreveport-Bossier Advocate succeeded; WebSearch filled in the rest.
- **Plaintiffs named (original note had them anonymous): Tyler Gordon (Mooringsport Mayor),
  Mary Blakemore, Michael Craft**; attorney **Jack Bailey**.
- **Ruling date correction: April 21, 2026** (original note said April 20).
- **Sequence correction — this matters for accuracy:** at the time of the ruling, the appeal
  had **not yet been filed**; Bailey said only that they were "considering" it, with 30-60 days
  to decide, and cautioned "it is not 100% guaranteed that the appellate court is going to take
  it up." The Sierra Club Delta Chapter's formal backing (chair **Angelle Bradford Rosenberg**),
  the June 26 appeal deadline, and the $20K spent / $10K more anticipated funding detail all
  come from a *later* article (dated ~May 22 per its SettleTalk republish date) — i.e., the
  original note's framing (Sierra Club backing an already-proceeding appeal) is accurate as of
  its own writing, just compressing a real ~1-month gap between the dismissal and Sierra Club's
  formal involvement. Worth keeping that sequence straight if the paper narrates this case.
- **New project specifics:** $6B cost, 1.3 million sq ft, 150-170 permanent jobs, 2-3 year
  construction — Amazon Web Services is the named tenant.

### 16. Caddo commissioners' transparency push — VERIFIED, mechanism clarified
Direct fetch of KSLA succeeded; WebSearch (KTBS headline) confirms the outcome.
- **Real mechanics, more specific than the original note:** Epperson's resolution (examine
  construction impact on flooding/traffic) advanced at a **Monday work session**; **Kracman
  amended it** to also cover the Stateline Data Center campus in rural Caddo Parish (amendment
  granted). Separately, **Commissioner John Paul Young** proposed developers implement
  rainwater-collection systems.
- **Outcome confirmed via KTBS headline: "Caddo Parish Commission rejects new data
  center-related resolutions"** — matches the original note's "neither measure passed."
- Kracman's "I've been begging for transparency left and right and have gotten very little"
  quote — **confirmed real**, direct from KSLA.
- Epperson quote, new: "My concern is, once you remove all the shrubs and streams upstream
  from that data center, is that going to exacerbate the drainage situation here?"
- Workforce-housing ordinance detail from the original note not independently re-confirmed by
  direct fetch this pass (KSLA's own article focus was the environmental-study resolution) —
  plausible, not contradicted, just not re-verified word-for-word.

### 17. Caddo Parish tax-break freeze — VERIFIED, meaningfully more specific than original note
Direct fetch blocked (402/429 on two outlets); resolved via WebSearch across thehayride.com,
Center Square, BIZ Magazine, and 1012industryreport.com.
- **Correction — this is not what the original note described.** It's not a freeze on existing
  incentives; it's a proposed **two-year moratorium on *future* tax-incentive agreements**
  (PILOTs and other abatements) for data centers, sponsored by **Commissioner John-Paul Young**
  (same commissioner as #16's rainwater-collection proposal). The resolution would also convene
  a study committee to report back on local risks/concerns within **18 months**, with **60
  more days** for the commission to vote on the findings — i.e., if adopted, this delays any
  *new* deal by up to ~20 months, not an immediate freeze.
- Young quote: "We entered into this tax agreement offer with very little information" —
  referring to the Dec 2025 vote that helped land the AWS campus; cites environmental impact,
  water use, heat, and utility-cost concerns.
- **Timeline is live, not historical: work session Aug 17, regular meeting Aug 20, 2026** —
  i.e., this could resolve in the next few days from today (2026-08-16). Worth checking back
  after 8/20 for the actual vote outcome before finalizing this artifact's coding, and worth
  flagging to Britton directly since it's imminent, not settled history like the rest of the
  corpus.

---

## Net effect on the corpus
All 6 of the 8/15 additions are now primary-source-verified (2 with minor sub-details still
open — NOLA's MW threshold, #16's workforce-housing ordinance wording). Three real corrections
worth fixing in `Study1_Corpus_and_Coding_DRAFT_2026-08-12.md`'s coding when it's next touched:
NOLA's distance rule (three blocks from residential + 500 ft between facilities, not "500 ft
from residential"), the Sierra Club appeal's sequence (dismissal → considering appeal →
Sierra Club backing ~1 month later, not simultaneous), and #17's actual mechanism (2-year
moratorium on *new* agreements + study committee, not a blanket freeze). None of these
corrections change which themes the artifacts support — if anything #12's Garcia quote, #14's
SWEPCO/ratepayer detail, #13's Morrell quote, and #17's Young quote are all strong *additional*
citable material for Themes 2 and 3 that wasn't captured in the 8/15 pass.

**Not done this pass:** folding these corrections into the actual coding table in
`Study1_Corpus_and_Coding_DRAFT_2026-08-12.md`, or Phase 3 theme review — still Britton's call
per the standing rule, this pass only verifies and adds primary-source detail to review against.
