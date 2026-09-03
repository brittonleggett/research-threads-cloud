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

**6. Perceived Price Fairness** [BEST AVAILABLE — quote-level, r=.84] — Campbell (1999),
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

**9. Purchase Intention** [PROVISIONAL — genuine gap, decide before locking] — cite Dodds,
Monroe & Grewal (1991), but the exact 1991 item wording is not recoverable via search tools
(no appendix/measure table accessible). Two candidate wordings, NOT reconciled:
  (a) this project's original 3-item draft: "The likelihood of purchasing this product is
      high" / "If I were going to buy a product like this, I would consider buying this one"
      / "The probability that I would consider buying this product is high."
  (b) Fennell, Niedrich & Rice (2025)'s 4-item scale, explicitly stated as adapted from Dodds
      et al. (1991): "The likelihood that I would purchase the [product] from [retailer] is..."
      / "The probability that I would purchase the [product] from [retailer] is..." / "My
      willingness to buy the [product] from [retailer] is..." / "I would definitely try the
      [product] at [retailer]'s current price."
  **Britton's call which to use**, or pull the actual 1991 JMR appendix if there's time. See
  `notes/2026-09-03-consensus-dodds-maxham-scales-partial.md`.

**10. Word-of-Mouth Intention** [PROVISIONAL — genuine gap] — Maxham & Netemeyer (2002), 3
items, exact wording NOT recoverable via search tools; format confirmed (3-item, 7-pt Likert)
via a related 2003 paper in the same research stream, but not the item text. This project's
original 3-item draft ("I would say positive things about [Company]..." / "I would recommend
[Company]..." / "I would encourage friends and relatives...") remains the best available
placeholder — genuinely unverified, needs library access or direct acceptance as-is for now.
See `notes/2026-09-03-consensus-dodds-maxham-scales-partial.md`.

**11. Demographics** — age, gender, household income bracket, education, how often they
shop at retailers like the one described, political ideology (single 7-pt liberal–
conservative item — worth including given the CFP's own framing around "social and political
polarization" as a live theme for this special issue; also lets you check whether Attribution
Frame or Cost-Response effects vary by respondent ideology as a supplementary analysis).

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
1. **Fairness and Opportunism are now resolved** (2026-09-03, quote-level, see items 6-7
   above) — no longer blocking. **Purchase Intention (item 9) needs Britton's pick between
   two candidate wordings, or a fresh library pull. WOM (item 10) needs a library pull or
   acceptance of the unverified placeholder as-is** — these two are the only remaining
   blockers, and neither is as theoretically load-bearing as Fairness/Opportunism were.
2. Decide on exact demographic response options/brackets.
3. Decide whether to counterbalance scale order (fairness/opportunism before or after trust)
   or keep the theoretical order shown above — theoretical order is simpler to justify and is
   what I'd default to unless you have a specific concern about ordering effects.
4. Build actual Qualtrics logic (randomization, branching, skip logic) — this note specifies
   content and order, not the Qualtrics-file mechanics themselves.
