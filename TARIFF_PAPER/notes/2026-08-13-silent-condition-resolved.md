# 2026-08-13 — Silent-condition design tension, resolved

## The problem
Flagged since 2026-08-04 (`2026-08-04-vignette-drafts-v1.md`, "One design tension worth your
explicit sign-off"): the Silent condition (Cells 5-6) couldn't be truly silent, because
Cost-Response (full pass-through vs. shared-burden absorption) needs *something* to
manipulate, and the only available hook was "what it now costs us." That phrase gave the
Silent cells a de facto cost-based rationale even though no sentence explicitly said "because
of X" — leaving them reading uncomfortably close to the General-cost-explicit condition
(Cells 3-4), which explicitly says "due to rising costs... because of these higher costs."
Two conditions in a 3-level factor that participants can't cleanly tell apart is a real
manipulation-check risk, not just an aesthetic one.

## Why it was fixable without breaking the factorial
The two prior options on the table (2026-08-04 note) were "keep as drafted" or "drop
Cost-Response from Silent entirely and break the clean 3×2 into an irregular 2×2+2." Neither
was necessary. The actual fix: **decouple the noun the Cost-Response sentence refers to from
"cost."** Cost-Response only needs *some* referent to describe absorbing vs. passing along —
it doesn't have to be "cost" specifically. Every vignette already states "prices... will be
increasing" before the Cost-Response sentence, which supplies a clean alternative referent:
*"this price increase."* Rewriting Cells 5-6 to describe the company's behavior toward "this
price increase" rather than toward "what it now costs us" keeps Cost-Response fully legible
(full pass-through: "passing along the full amount of this price increase"; shared-burden:
"absorbing a significant portion... and passing along only part of it") while removing the
word "cost" and every causal connective ("because of," "due to") from the Silent cells
entirely.

## What changed
`2026-08-04-vignette-drafts-v1.md` Cells 5-6, and the mirrored Section 6 vignette text in
`build_irb_docx.py` / `IRB-Application-Package-Tariff-Messaging-v2-DRAFT.docx`, both updated
to the new wording:

> **Cell 5 (Silent × Full pass-through):** "We want to keep you informed about some upcoming
> changes here at Meridian Home. Starting next month, prices on select items across our
> stores will be increasing. We are passing along the full amount of this price increase to
> our customers. We appreciate your continued business and look forward to serving you as
> always." (54 words)

> **Cell 6 (Silent × Shared-burden):** "We want to keep you informed about some upcoming
> changes here at Meridian Home. Starting next month, prices on select items across our
> stores will be increasing. We are absorbing a significant portion of this price increase
> ourselves, and passing along only part of it to our customers. We appreciate your continued
> business and look forward to serving you as always." (61 words)

Both stay within the ~55-65 word range established for the other four cells (avoids the
length confound the pretest is designed to check for). Neither contains "cost" or a causal
connective — confirmed by direct search, not eyeballed.

## Why this should hold up at the manipulation-check stage
- **Attribution Frame recall** ("what did the company say was the reason for the price
  increase — tariffs / general rising costs / no reason given / don't recall"): Cells 5-6 now
  have zero causal language for a respondent to (mis)code as "general rising costs." Cells 1-2
  keep "tariffs." Cells 3-4 keep "due to rising costs... because of these higher costs." The
  three levels no longer share ambiguous territory.
- **Cost-Response recall** ("is the company absorbing part of the cost, or passing it fully to
  customers?"): still directly answerable from "passing along the full amount of this price
  increase" vs. "absorbing a significant portion... and passing along only part of it" — the
  construct doesn't require the literal word "cost" to be legible, only a stated fraction of
  the increase being passed through or absorbed.
- No change to Cells 1-4 — the fix is fully localized to the two cells with the actual
  problem.

## Still needed
1. **Britton's face-validity read** — this is a rewrite, not yet reviewed by him. Flag
   anything that doesn't sound like a real corporate email, or any residual "give-away" of
   causation.
2. Pretest (N=150-180) is the real test — manipulation-check ANOVAs should now show a clean
   3-way split on the attribution item with no cross-contamination between Cells 3-4 and 5-6.
   If Silent still reads as "vaguely cost-related" to real respondents despite the wording fix,
   that's empirical grounds to revisit (Option 2 from the original note remains available as a
   fallback, just no longer the only fix on the table).
3. IRB package (`IRB-Application-Package-Tariff-Messaging-v2-DRAFT.docx`) already regenerated
   with the new Cell 5-6 text as of this note — no separate action needed there.
