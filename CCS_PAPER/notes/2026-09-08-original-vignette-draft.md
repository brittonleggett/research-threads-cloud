# 2026-09-08 — Original CCS Study 2 vignette draft (consultation-extent design)

**Provenance statement, for the eventual Methods section (paste-able):** "The multifactorial
vignette design follows the general approach of Anders, Liebe & Meyerhoff (2024, *Nature Climate
Change*), who varied CCS implementation attributes including consultation extent across a
fractional-factorial vignette set. All vignette text below is original, written for this study's
Louisiana context; no wording is reproduced from Anders et al. (2024) or any other source." Every
sentence below was written fresh for this project — none of it is copied or closely paraphrased
from Anders et al. (2024)'s own (unseen, since the Supplementary Information wasn't pulled)
vignette text, or from any other source. Per Britton's explicit standing priority
([[feedback_academic_integrity_top_priority]]), reuse here is limited to the *structural design
choice* (a consultation-extent gradient as the primary manipulated attribute) — a methodological
approach, not protected text — with full original wording and explicit citation.

## Why this design, not the lit review's original 6-level frame

Per `2026-09-08-anders-et-al-full-read.md`: Anders et al. (2024) found implementing-body type
(industry vs. public-private vs. government) did NOT significantly affect acceptance across five
countries, while consultation extent robustly did. That's a real reason to lead with the
consultation-extent gradient as the primary manipulated factor, rather than treating all six of
the lit review's original governance-frame levels (which included two "who approved it"
implementing-body-style frames) as equally load-bearing. Implementing body is held constant across
all conditions below (always the real Louisiana permitting body) rather than manipulated — this
can be revisited if Britton wants to test it as a secondary factor.

## Shared opening (all conditions) — 45 words, 2 sentences

> The Louisiana Department of Energy and Natural Resources is reviewing a permit application for
> a new well that would inject and store carbon dioxide deep underground in a rural parish. The
> well would operate under the state's federal-approved permitting program, with the EPA's Region
> 6 office providing oversight, and the company says the project will reduce emissions from
> nearby industrial facilities.

(Grounded in the lit review's own Part H recommendation to reference a plausible, real permitting
structure — Louisiana's actual Class VI primacy program and EPA Region 6 oversight — rather than
an implausible hypothetical.)

## Five conditions along the consultation-extent gradient

**Condition 1 — No consultation (36 words, 2 sentences):**

> State regulators reviewed the company's application and technical data on their own, following
> the same internal review process used for similar well permits. No public meetings or comment
> periods were held before the permit was approved.

**Condition 2 — Notice-only / tokenistic (36 words, 2 sentences):**

> State regulators posted a public notice about the application on their website for two weeks
> before approving the permit. No public meetings were held, and none of the comments submitted
> during that time changed the final decision.

**Condition 3 — Affected-community consultation (39 words, 2 sentences):**

> Before deciding, state regulators held a public meeting in the parish where the well would be
> located and accepted written comments from residents. Several changes were made to the
> monitoring plan based on concerns raised at the meeting.

**Condition 4 — Broader regional consultation (31 words, 2 sentences):**

> Before deciding, state regulators held public meetings in several parishes across the region and
> collected input from residents statewide. The permit conditions were revised based on that input
> before final approval.

**Condition 5 — Tribal consultation (35 words, 2 sentences):**

> Before deciding, state regulators formally consulted with the federally recognized tribal
> government whose historic lands include the project area, as required under tribal consultation
> procedures. The tribal government's input was incorporated into the final permit conditions.

All five: 31-39 words, 2 sentences, active voice, no embedded clauses — same length/structure
discipline established for Flock's vignettes today. Not yet checked with an actual
Flesch-Kincaid calculation or piloted.

## Condition 5 — mandatory ethics handling, per the lit review's own Part H

This condition tests **general-public perception of the idea that tribal consultation occurred**
— it does not measure, represent, or imply anything about actual Tribal nations' views, consent,
or satisfaction with the process. The vignette text above is written to state only that
consultation happened procedurally (parallel in structure to Conditions 3-4), without describing
tribal reaction, opinion, or endorsement — deliberately avoiding any implication that the vignette
speaks for a tribal government's actual position. Per Part H's recommendations (already logged in
`2026-09-08-lit-review-foundation-digest.md`): the Methods section needs its own "Scope and
limitations regarding Indigenous research" subsection, and reaching out to Louisiana's
federally-recognized tribal liaison offices is worth doing as a courtesy if this condition survives
piloting — not resolved by this draft, still Britton's call.

## Manipulation check (one shared item across all 5 conditions, parallel to Flock's design)

> "According to the description, which of the following best describes what state regulators did
> before approving the permit?"
> (a) Reviewed the application on their own, no public input sought. [Condition 1]
> (b) Posted a public notice but held no meetings. [Condition 2]
> (c) Held a public meeting in the affected parish and took resident comments. [Condition 3]
> (d) Held public meetings across the region and took statewide input. [Condition 4]
> (e) Formally consulted with the tribal government whose lands include the project area.
>     [Condition 5]

## Readability — actually measured, not just asserted (2026-09-09)

Installed `textstat` and ran real Flesch-Kincaid checks on the draft above. **Results were worse
than expected — worse than even Flock's original flagged-as-too-complex 2-condition draft**: FK
grade 15.2-17.8 across the five conditions (Tribal-consultation the worst at 17.8, Flesch Reading
Ease 10.4 — "very difficult"). The 8th-grade target requires real revision, not just the
matched-length/active-voice/no-embedded-clauses discipline already applied — the driver here is
vocabulary complexity (bureaucratic/regulatory terms: "regulators," "consultation," "permitting,"
"federally recognized," "jurisdiction"-adjacent language), not sentence length alone.

**Revised (v2) text, re-tested, real improvement:**

Shared opening: "The Louisiana Department of Energy and Natural Resources is reviewing a request
for a new well in a rural parish. The well would pump carbon dioxide gas deep underground for
storage. The EPA's Region 6 office would also oversee the well. The company says the project will
help cut pollution from nearby factories."

- No consultation: "State regulators looked at the company's request and technical data on their
  own. They followed the same process used for similar well permits. No public meetings were held
  before they approved it." — **FK 8.4**
- Notice-only: "State regulators posted a notice about the request on their website for two weeks.
  They did not hold any public meetings. None of the comments people sent in changed the final
  decision." — **FK 8.2**
- Affected-community: "Before deciding, state regulators held a public meeting in the parish. They
  also accepted written comments from residents. They changed the monitoring plan based on
  concerns raised at the meeting." — **FK 8.9**
- Broader-regional: "Before deciding, state regulators held public meetings in several parishes.
  They also collected input from residents across the state. They changed the permit conditions
  based on that input." — **FK 9.2**
- Tribal-consultation: "Before deciding, state regulators consulted with the federally recognized
  tribal government whose historic lands include the project area. State rules require this
  consultation. The tribal government's input was included in the final permit conditions." —
  **FK 11.0** (still elevated — "federally recognized" and "consultation" are hard to simplify
  further without losing the precision Part H's ethics guardrails require; recommend keeping this
  wording despite the readability cost rather than sacrificing accuracy on this specific condition)

Four of five conditions now land at or near the 8th-grade target (8.2-9.2); Tribal-consultation
stays elevated for a defensible, flagged reason. Real formula-based result, not an assertion —
computed via `textstat` (`flesch_kincaid_grade`), script saved at
`notes/readability_check_2026-09-09.py`. Still not a substitute for an actual human pilot.
**Recommend adopting this v2 wording as the actual draft going forward**, superseding the v1 text
above.

## What's still open

1. **Not yet crossed with a "frame strength" (token vs. substantive) second factor** — the lit
   review's original 2×3 idea (leveraging Walker et al. 2014's boomerang finding) is still
   available if Britton wants a richer design; this draft keeps it single-factor, 5 levels, for
   simplicity and to control cost, consistent with the same budget concern that shaped Flock's
   4-arm (not 5-arm) design.
2. **Implementing-body type held constant, not manipulated** — worth Britton's explicit
   confirmation this is the right call given Anders et al.'s null finding, rather than a silent
   default.
3. Real Flesch-Kincaid check and human pilot both still needed, same standing caveat as every
   other vignette draft in this project.
4. Mediators/moderators/DV from the lit review's Part F (procedural + recognition justice, trust,
   legitimacy, support; landowner status, rural identity, political ideology, etc.) carry over
   unchanged — only the manipulation itself is new here.
