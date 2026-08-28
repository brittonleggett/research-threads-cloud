# 2026-08-13 — Banked scales for a future companion paper

## Decision
Britton confirmed (2026-08-13, following the 3×2 word-budget check —
`2026-08-13-design-confirmed-3x2-word-budget.md`): revive the three constructs dropped from
the "full" ChatGPT model diagram when the primary model was leaned down on 2026-08-04 —
**Perceived Transparency, Inferred Firm Motive, Brand Attitude**. These get **measured but
not hypothesized** in Study 2 (and, where they fit the recall-based format, Study 3): folded
into the same Prolific data collection, not written up or tested in the JCM manuscript, so
they cost nothing against the 8,000-word budget. They're banked for a second paper — most
naturally, publishing the *fuller* model (dual entitlement/reactance manipulations → all five
mediating perceptions → Trust → PI/WOM) via PLS-SEM, which fits Britton's own established
toolkit (see `user_research_corpus.md`) and could target a different, more theory-dense
outlet than JCM once the lean paper is out.

Same rigor standard as the primary five scales in `2026-08-04-scale-sourcing.md`: real,
identifiable, widely-cited scales, but **exact item wording not yet verified against the
original articles** — pull verbatim text from the McNeese library before finalizing the
Qualtrics instrument. Confidence levels flagged per item, same convention as the existing
sourcing note and the IRB draft's [VERIFIED]/[UNVERIFIED] tags.

## Perceived Transparency
**Kang, J., & Hustvedt, G. (2014), "Building Trust Between Consumers and Corporations: The
Role of Consumer Perceptions of Transparency and Social Responsibility," *Journal of Business
Ethics*, 125(2), 253–265.** — Moderate-high confidence. Measures consumer-perceived corporate
transparency directly (disclosure, honesty, openness about practices) in a B2C context, closer
fit than the more commonly-cited Eggert & Helm (2003) transparency scale, which is B2B-relationship-specific. Worth comparing both before locking item wording.

## Inferred Firm Motive
**Ellen, P. S., Webb, D. J., & Mohr, L. A. (2006), "Building Corporate Associations: Consumer
Attributions for Corporate Socially Responsible Programs," *Journal of the Academy of
Marketing Science*, 34(2), 147–157.** — High confidence. The standard marketing citation for
consumer attribution of firm motive along a values-driven/other-serving vs. profit-driven/
self-serving dimension — a more precise fit for "inferred motive" specifically than Campbell
(1999), which is already doing double duty as the Perceived Opportunism outcome measure in
the primary model. Using Ellen et al. here keeps the two constructs conceptually distinct
(motive attribution as antecedent vs. opportunism as the fairness-adjacent judgment) rather
than measuring the same thing twice under two names.

## Brand Attitude
**Spears, N., & Singh, S. N. (2004), "Measuring Attitude Toward the Brand and Purchase
Intentions," *Journal of Current Issues & Research in Advertising*, 26(2), 53–66.** — High
confidence. Field-standard semantic-differential brand-attitude battery (e.g.,
good–bad, favorable–unfavorable, like–dislike), widely used and easy to defend to a reviewer.

## Practical implications (needs folding into the IRB instrument + package)
- Adds an estimated **2-3 minutes** to Study 2 (and Study 3, if included there) — bump the
  time estimate and Prolific compensation figures in `2026-08-04-IRB-draft-content.md` and
  `build_irb_docx.py` accordingly.
- These items still fall under the same 45 CFR 46.104(d)(3) benign-behavioral-intervention
  exemption — nothing about adding standard consumer-perception Likert items changes the
  risk profile. Should still be disclosed in the instrument-flow section of the IRB package
  even though they won't appear in the JCM manuscript, since IRB disclosure covers what's
  actually collected from subjects, not just what's ultimately published.
- Sample size (N=360-600 for Study 2) doesn't need to change — same respondents, more items
  per respondent, not more respondents.

## Still needed
1. Verify all three items' exact wording against the original articles (same task as the
   primary five scales — see `2026-08-04-scale-items-verification-status.md`, should be
   expanded to cover these three too).
2. Decide whether these are collected in Study 3 as well as Study 2, or Study 2 only (Study 3
   is a correlational field survey without the vignette manipulation, so Transparency/Motive/
   Brand Attitude would need to be asked about the recalled real retailer rather than
   "Meridian Home" — same adaptation already planned for the primary five scales there).
