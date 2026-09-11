# Study 2 Qualtrics Instrument — Build-Ready Spec (2026-09-09)

Assembled from `notes/2026-08-04-full-instrument-assembly.md` (all content decisions
now resolved/confirmed as of 2026-09-07) into exact Qualtrics block/flow order.
This is a formatting/assembly pass only — no content or design decisions made here.
Everything below is either [VERIFIED] quote-level wording or an already-confirmed
default per that note. Estimated length: ~12 minutes, N target 360–600 (3×2 design,
6 cells).

---

## Survey Flow (top to bottom, matches Qualtrics "Survey Flow" panel)

1. **Block: Consent**
2. **Block: Screener** (embedded terminate logic)
3. **Randomizer** → routes to 1 of 6 **Vignette Exposure** sub-blocks (equal
   probability, "Evenly Present Elements")
4. **Block: Manipulation Checks**
5. **Block: Fairness**
6. **Block: Opportunism**
7. **Block: Trust**
8. **Block: Purchase Intention**
9. **Block: Word-of-Mouth**
10. **Block: Demographics**
11. **Block: Debriefing**

Scale order is fixed (theoretical order), **not counterbalanced** — confirmed
2026-09-03 default, treat as locked unless Britton flags an ordering concern.

---

## Block 1 — Consent
- Source: `Informed_Consent_Tariffs.docx` (paste full text into a Text/Graphic
  question).
- Time estimate in the consent text: **~12 minutes**.
- Question type: Multiple Choice, single answer.
  - "I agree to participate"
  - "I do not agree to participate"
- **Skip logic:** if "I do not agree," End of Survey (with a brief thank-you/
  ineligible message) — set via Qualtrics Survey Flow "Branch If."

## Block 2 — Screener
1. Age — Text Entry, numeric validation. **Skip logic: if <18, terminate**
   (Branch If age < 18 → End of Survey).
2. "Do you currently reside in the United States?" — Yes/No. **Skip logic: if
   No, terminate.**
3. Attention/English-fluency check — embed naturally in this block (e.g., an
   instructional-manipulation-check item: "To show you're reading carefully,
   please select 'Somewhat agree' for this item" on a filler Likert scale).
   **Skip logic: fail → flag for exclusion at analysis (don't hard-terminate
   unless Britton wants to), or terminate per his preference — not yet
   specified, default to flag-not-terminate since Prolific's own pre-screen
   already filters most bad actors.**

## Block 3 — Randomizer + Vignette Exposure
- Qualtrics **Randomizer** element in Survey Flow, "Evenly Present Elements,"
  6 sub-blocks, 1 element per subject.
- Each sub-block = one of the six "Meridian Home" vignette emails per
  `2026-08-04-vignette-drafts-v1.md` (Attribution Frame: explicit/vague/silent
  × Cost-Response: absorption/pass-through — 3×2).
- **Timing:** add a Timing question (JavaScript minimum-time or Qualtrics'
  native "Force Response after N seconds") set to **10 seconds minimum
  on-page** before the Next button becomes clickable, to discourage skimming.
- Embed a **piped-text embedded data field** (e.g., `AttributionFrame`,
  `CostResponse`) set within each sub-block so condition assignment is
  logged automatically in the data export — don't rely on reconstructing
  condition from block order later.

## Block 4 — Manipulation Checks
1. "According to the message, what did the company say was the reason for
   the price increase?" — Multiple Choice, single answer:
   - Tariffs
   - General rising costs
   - No reason given
   - Don't recall
2. "How clearly did the message explain the reason for the price increase?"
   — Slider or 7-pt Likert, 1 = "Not at all clearly" to 7 = "Very clearly."
3. "According to the message, is the company passing along the full cost
   increase, or absorbing part of it?" — Multiple Choice, single answer:
   - Full amount
   - Partial, company absorbing some
   - Unclear

## Block 5 — Perceived Price Fairness [VERIFIED, Campbell 1999 Study 2, r=.84]
Both items 7-pt, average after reverse-scoring item 2:
1. Bipolar item: 1 = "Very fair" to 7 = "Very unfair."
2. "This price is not fair." 1 = "Strongly agree" to 7 = "Strongly disagree"
   — **reverse-score before averaging with item 1.**

## Block 6 — Perceived Opportunism [BEST AVAILABLE, Campbell 2007]
1. Motive rating, 7-pt: 1 = "Bad" to 7 = "Good."
2. "The intent in this situation was to take advantage of you (the
   customer)." 1 = "Agree" to 7 = "Disagree."
   - **Note the reverse polarity relative to the rest of the instrument** —
     either flip this item's displayed anchors to match everything else
     (Disagree→Agree, 1→7) for respondent-facing consistency, or leave as-is
     and reverse-score in analysis. **Not yet decided which — flag for
     Britton**, since it's the one item in the whole instrument running
     backward from the rest; recommend flipping the anchors so respondents
     never encounter an inconsistent scale direction mid-survey.

## Block 7 — Trust in the Company [VERIFIED, Chaudhuri & Holbrook 2001]
All 7-pt Likert, strongly disagree–strongly agree:
1. "I trust this company."
2. "I rely on this company."
3. "This is an honest company."
4. "This company is safe."

## Block 8 — Purchase Intention [VERIFIED, Dodds/Monroe/Grewal 1991, all 5 items]
Britton's 2026-09-07 call: use all 5 original items (not the trimmed 3-item
subset). Flag in Method section as deliberate; run discriminant-validity
check against Fairness (item overlap on "at the price shown" wording) once
data is in.
1. "The likelihood of purchasing this product is:" — 7-pt, "Very high" to
   "Very low."
2. "If I were going to buy this product, I would consider buying this
   product at the price shown." — Strongly agree to strongly disagree.
3. "At the price shown, I would consider buying the product." — Strongly
   agree to strongly disagree.
4. "The probability that I would consider buying the product is:" — 7-pt,
   "Very high" to "Very low."
5. "My willingness to buy the product is:" — 7-pt, "Very high" to "Very low."

## Block 9 — Word-of-Mouth Intention [VERIFIED, Maxham & Netemeyer 2002]
1. "How likely are you to spread positive word-of-mouth about [company]?" —
   7-pt likelihood scale.
2. "I would recommend [company]'s products to my friends." — Strongly
   disagree to strongly agree.
3. "If my friends were looking for a product like this, I would tell them
   to try [company]." — Strongly disagree to strongly agree.
- Piped text: `[company]` = "Meridian Home" throughout, matching the
  vignette.

## Block 10 — Demographics
1. Age — Text Entry, numeric (screener already excludes <18).
2. Gender — Multiple Choice: Male / Female / Non-binary / Prefer to
   self-describe (with open text) / Prefer not to say.
3. Household income — Multiple Choice: <$25k / $25k–49,999 / $50k–74,999 /
   $75k–99,999 / $100k–149,999 / $150k+ / Prefer not to say.
4. Education — Multiple Choice: Less than high school / High school or GED /
   Some college, no degree / Associate's / Bachelor's / Graduate or
   professional degree.
5. Shopping frequency at retailers like the one described — Multiple
   Choice: Never / Rarely (a few times a year) / Occasionally (monthly) /
   Regularly (a few times a month) / Frequently (weekly or more).
6. Political ideology — single 7-pt item, 1 = "Very liberal" to 7 = "Very
   conservative." (Enables an H3/ideology supplementary analysis per the
   CFP special-issue's polarization framing.)

## Block 11 — Debriefing
- Source: `notes/2026-08-04-debriefing-statement.md`.
- Full incomplete-disclosure debrief (the vignette used a fictional company
  and manipulated framing) — display as a final Text/Graphic block, no
  further questions after.

---

## Embedded Data / Export Fields to Set Up Before Fielding
- `AttributionFrame` (explicit / vague / silent)
- `CostResponse` (absorption / pass-through)
- `AttentionCheckPass` (1/0)
- `ManipCheck1Correct` (1/0, auto-scored against the "tariffs" response)
- Qualtrics `ResponseID`, `Progress`, `Duration (in seconds)` — default fields,
  just confirm they're included in the export.

## Items Still Needing Britton's Confirm-or-Override (not decided by this pass)
1. **Opportunism item 2's reverse polarity** — flip anchors vs. reverse-score
   in analysis (see Block 6 above). Recommend flipping anchors; not decided.
2. **Attention-check failure handling** — flag-only vs. hard-terminate (see
   Block 2). Recommend flag-only; not decided.
3. Everything else in the original assembly note (scale order, demographic
   brackets, Purchase Intention item count) is already confirmed/locked —
   listed here only for completeness, not open questions.

## What This Document Is NOT
This is a complete, unambiguous content/logic spec — someone with Qualtrics
access can build the live survey from this document mechanically in well
under an hour. It is not a live Qualtrics survey; no browser automation was
attempted this pass (fragile multi-step Qualtrics UI builds are higher-risk
to attempt unsupervised than producing this spec). Building the actual
survey still requires Britton's (or an assistant's) Qualtrics account access.
