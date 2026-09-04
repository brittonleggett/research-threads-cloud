# 2026-08-04 — Full Qualtrics instrument assembly (Study 2 and Study 3)

Combines everything drafted so far into actual survey flow order.

**Updated 2026-09-03:** Scale wording below now reflects the best available
answers from a Consensus.app Deep Research verification pass (see
`notes/2026-09-03-consensus-campbell-1999-opportunism-scale.md`,
`notes/2026-09-03-consensus-xia-monroe-cox-2004-citation-risk.md`,
`notes/2026-09-03-consensus-dodds-maxham-scales-partial.md`). Status tags
now use **[VERIFIED]** (Trust only), **[BEST AVAILABLE]** (Opportunism,
sourced from Campbell's own 2007 follow-up — reasonably confident) and
**[PROVISIONAL]** (Fairness, Purchase Intention, WOM — genuine gaps remain,
see each item's note; a possibly-superior 2026-08-13 verification pass may
exist in a local Claude Code session not yet recovered, see
`SUBMISSION_TRACKER.md`'s discrepancy flag). **Do not treat [PROVISIONAL]
items as final without one more check if time allows before fielding** —
but per Britton's 2026-09-03 call, proceeding toward IRB submission on this
basis rather than blocking further.

**Further updated 2026-09-04** (see `notes/2026-09-04-purchase-intention-wom-scales-
resolved.md`): WOM (item 10) is now **[VERIFIED]** — a direct fetch of the actual cited
paper's own Appendix A gave verbatim item wording. Fairness (item 6) should also read
**[VERIFIED]**, not [PROVISIONAL] — the 2026-09-03 note above already found Campbell
(1999)'s actual quote-level wording (r=.84); the status tag here was never updated to
match. Purchase Intention (item 9) moves from "genuinely unverified, pick blind between
2 candidates" to **[BEST AVAILABLE — quote-level, one step short of the 1991 original]**:
a co-author of the 1991 scale reproduced it verbatim in his own later paper. Full item
text for both below.

---

## STUDY 2 — Vignette experiment (3×2, N target 360-600)

**1. Consent** — per `Informed_Consent_Tariffs.docx`, time estimate updated to ~12 minutes.
Radio buttons: "I agree to participate" / "I do not agree to participate."

**2. Screener** (redundant check on top of Prolific's own pre-screen)
- Age (open text or range select) — terminate if <18.
- "Do you currently reside in the United States?" — terminate if No.
- Attention/English-fluency filter item embedded naturally in the screener.

**3. Random assignment** — Qualtrics randomizer, equal probability across the 6 cells
(`2026-08-04-vignette-drafts-v1.md`).

**4. Vignette exposure** — participant sees exactly one of the 6 "Meridian Home" emails, per
their assigned cell. Include a brief forced pause or minimum-time-on-page setting (e.g., 10
seconds) to discourage skimming.

**5. Manipulation checks** (per `2026-08-04-pretest-design.md`, retained in the main study for
data-quality screening, not just the pretest)
- "According to the message, what did the company say was the reason for the price
  increase?" — tariffs / general rising costs / no reason given / don't recall.
- Continuous item: "How clearly did the message explain the reason for the price increase?"
  (1 = not at all clearly, 7 = very clearly)
- "According to the message, is the company passing along the full cost increase, or
  absorbing part of it?" — full amount / partial, company absorbing some / unclear.

**6. Perceived Price Fairness** [VERIFIED — quote-level, r=.84] — Campbell (1999),
Study 2, two items, averaged: (1) bipolar 7-pt item, 1="very fair" to 7="very unfair"; (2)
"This price is not fair," 1="strongly agree" to 7="strongly disagree", **reverse-scored**
before averaging with item 1. Reliability reported in the original: r=.84, p<.0001. Cite
Campbell (1999), NOT Xia, Monroe & Cox (2004) — the latter is a conceptual/theoretical paper
with no scale of its own; correctly used elsewhere in this project for the *theoretical*
framing (dual entitlement/equity/procedural justice) but was mistakenly the attributed scale
source before 2026-09-03. See `notes/2026-09-03-consensus-campbell-1999-fairness-scale-
resolved.md`.

**7. Perceived Opportunism** [BEST AVAILABLE — quote-level] — Campbell (2007), building
directly on the 1999 inferred-motive construct: (1) motive rating, 7-pt, 1="bad" to 7="good";
(2) "The intent in this situation was to take advantage of you (the customer)," 1="agree" to
7="disagree" — **note the reverse coding** relative to most other items in this instrument;
either flip anchors for consistency or reverse-score explicitly in analysis. See
`notes/2026-09-03-consensus-campbell-1999-opportunism-scale.md`.

**8. Trust in the Company** [VERIFIED] — Chaudhuri & Holbrook (2001): I trust this company /
I rely on this company / this is an honest company / this company is safe. 7-pt Likert.

**9. Purchase Intention** [BEST AVAILABLE — quote-level, 2026-09-04] — cite Dodds, Monroe &
Grewal (1991) for the construct/attribution; exact item wording via Grewal, Krishnan, Baker &
Borin (1998, *Journal of Retailing*, 74(3), 331–352) — Dhruv Grewal, a co-author of the 1991
original, reproduces the 3-item scale verbatim in that paper's own Table 1, explicitly
attributed to "Dodds, Monroe, and Grewal (1991)." Bracketed product name genericizes to this
study's stimuli:
  1. "I would purchase this [product]." (item reliability .92)
  2. "I would consider buying at this price." (item reliability .90)
  3. "The probability that I would consider buying [this product] is [high]." (item
     reliability .94)
  Composite reliability = .92; variance extracted = .92. Item 3 matches this project's prior
  3-item draft almost exactly (independently corroborated again by Dodds's 2002 solo paper's
  single-item measure); items 1-2 of the prior draft do NOT match this source and should be
  replaced with the wording above. **This is a strong secondary source (a co-author's own
  verbatim reproduction) but still one step short of the 1991 JMR appendix itself** — if
  Britton has library/JSTOR access and 5 minutes this weekend, pulling the original appendix
  is the one remaining upgrade; otherwise this wording is defensible to use directly, citing
  both the 1991 original (construct) and the 1998 paper (item source). See
  `notes/2026-09-04-purchase-intention-wom-scales-resolved.md`.

**10. Word-of-Mouth Intention** [VERIFIED — verbatim, 2026-09-04] — Maxham & Netemeyer (2002,
*Journal of Marketing*, 66(4), 57-71), Appendix A "Measurement Scales," Favorable WOM, 3 items,
7-point (all "strongly disagree" to "strongly agree" except item 1, a likelihood item),
genericized from "banking services"/"firm name" to this study's product/company framing:
  1. "How likely are you to spread positive word-of-mouth about [company]?"
  2. "I would recommend [company]'s [products/services] to my friends."
  3. "If my friends were looking for [a product/service like this], I would tell them to try
     [company]."
  Reliability: coefficient alpha .83-.97 across all measures/time periods in the original
  (not broken out per-construct). This replaces the project's prior unverified 3-item draft
  — the wording above is a direct, correctly-cited quote from the actual paper's own appendix,
  not a reconstruction. See `notes/2026-09-04-purchase-intention-wom-scales-resolved.md`.

**11. Demographics** — age, gender, household income bracket, education, how often they
shop at retailers like the one described, political ideology (single 7-pt liberal–
conservative item — worth including given the CFP's own framing around "social and political
polarization" as a live theme for this special issue; also lets you check whether Attribution
Frame or Cost-Response effects vary by respondent ideology as a supplementary analysis).

**Proposed response options (2026-09-03), standard survey-methodology defaults — override
freely, these are low-stakes choices:**
- Age: open numeric entry (more precise than brackets for a Prolific sample; screener already
  terminates <18).
- Gender: Male / Female / Non-binary / Prefer to self-describe / Prefer not to say.
- Household income: <$25k / $25k-49,999 / $50k-74,999 / $75k-99,999 / $100k-149,999 /
  $150k+ / Prefer not to say (standard Census-adjacent brackets, works for MANOVA covariate
  use without too many sparse cells).
- Education: Less than high school / High school or GED / Some college, no degree /
  Associate's / Bachelor's / Graduate or professional degree.
- Shopping frequency at retailers like the one described: Never / Rarely (a few times a
  year) / Occasionally (monthly) / Regularly (a few times a month) / Frequently (weekly or
  more).
- Political ideology: single 7-pt item, 1="Very liberal" to 7="Very conservative."

**Scale-order decision, formalized (2026-09-03):** using the theoretical order shown in this
document (manipulation checks → Fairness → Opportunism → Trust → Purchase Intention → WOM →
demographics) rather than counterbalancing — this was already the note's own default
recommendation ("simpler to justify... what I'd default to unless you have a specific
concern"); treating as decided unless Britton flags an ordering-effects concern.

**12. Debriefing** — `2026-08-04-debriefing-statement.md`.

---

## STUDY 3 — SEM validation survey (correlational, no manipulation, N target 300-400)

No vignette. Participants report on a real recent experience instead, to preserve natural
variance in the constructs for model validation (rather than re-testing the same manipulated
scenario).

**1. Consent** — same template, time estimate ~15 minutes.

**2. Screener** — same as Study 2.

**3. Recall prompt** — "Think of a time in the last 12 months when a retailer you shop with
raised prices on something you buy. Please briefly describe what happened." (open text,
also usable as a lightweight secondary qualitative check). Branch/skip logic: if a
participant cannot recall any such instance, redirect to a brief generic-attitude version of
the items instead of forcing a fabricated memory.

**4-8. Same five scales as Study 2** (Fairness, Opportunism, Trust, Purchase Intention, WOM
Intention), reworded to reference "the retailer" / "this experience" instead of "Meridian
Home" / "the message."

**9. Demographics** — same battery as Study 2, plus a covariate on the recency/category of
the recalled price increase (useful for ruling out category-specific confounds in PLS-SEM
robustness checks).

**10. Debriefing** — lighter version; no incomplete-disclosure element since there's no
manipulation to explain, just a shorter thank-you + purpose statement.

---

## Open items before either survey can actually be built in Qualtrics
**Status as of 2026-09-04: content is now fully specified, and 4 of 5 scales (Trust,
Fairness, Opportunism, WOM) have real quote-level or verbatim wording — no more blind
guessing on any of them.** Remaining items need only Britton's confirm-or-override:
1. Fairness, Opportunism, Trust, WOM — **all resolved**, quote-level or verbatim (items
   6-8, 10).
2. Purchase Intention (item 9) — **strong quote-level default now available** (Grewal et
   al. 1998's verbatim reproduction of the Dodds, Monroe & Grewal 1991 scale); confirm
   or pull the actual 1991 appendix this weekend if library access + 5 minutes allow.
3. Demographic response options — **proposed defaults given** above; confirm or override.
4. Scale order — **formalized as theoretical order** (the note's own prior default); confirm
   or flag an ordering-effects concern.
5. Build actual Qualtrics logic (randomization, branching, skip logic) — this note specifies
   content and order, not the Qualtrics-file mechanics themselves; needs Britton's Qualtrics
   account access to actually build.
