# 2026-08-04 — Full Qualtrics instrument assembly (Study 2 and Study 3)

Combines everything drafted so far into actual survey flow order. **Items marked
[UNVERIFIED] use the reconstructed wording from `2026-08-04-scale-items-verification-status.md`
— do not field this until those are checked against the original articles.**

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

**6. Perceived Price Fairness** [UNVERIFIED] — Xia, Monroe & Cox (2004), 7-pt semantic
differential: unfair–fair / unacceptable–acceptable / unreasonable–reasonable.

**7. Perceived Opportunism** [UNVERIFIED — lowest confidence, verify first] — Campbell
(1999), items on inferred exploitative vs. legitimate motive.

**8. Trust in the Company** [VERIFIED] — Chaudhuri & Holbrook (2001): I trust this company /
I rely on this company / this is an honest company / this company is safe. 7-pt Likert.

**9. Purchase Intention** [UNVERIFIED, moderate-high confidence] — Dodds, Monroe & Grewal
(1991), 3 items on likelihood/consideration/probability of purchase.

**10. Word-of-Mouth Intention** [UNVERIFIED, moderate confidence] — Maxham & Netemeyer
(2002), 3 items on saying positive things / recommending / encouraging others.

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
1. Verify the four [UNVERIFIED] scales against original articles (blocking item).
2. Decide on exact demographic response options/brackets.
3. Decide whether to counterbalance scale order (fairness/opportunism before or after trust)
   or keep the theoretical order shown above — theoretical order is simpler to justify and is
   what I'd default to unless you have a specific concern about ordering effects.
4. Build actual Qualtrics logic (randomization, branching, skip logic) — this note specifies
   content and order, not the Qualtrics-file mechanics themselves.
