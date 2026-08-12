# 2026-08-04 — Study 1 corpus expansion (7 → 15 candidate artifacts)

Overnight pass to address the explicitly flagged gap: Study 1's corpus was 7 artifacts,
short of a standard TA sample (15-20). Found 8 new candidates, all secondary-sourced (news
coverage), same caveat as the original 7: **pull primary sources (8-Ks, IR pages, official
statements) before these go in the paper.** Light preliminary codes applied, consistent with
the existing style — **this is draft Phase 1 coding, not Phase 3 theme review, which stays
yours per the established rule** (Xu 2026 precedent, already followed for the original 7).

Good news on diversity: several of these are more consumer-facing retail than the original
7 (which skewed B2B/industrial — Lennox, Dormakaba, GMS) — useful given the JCM special
issue's stated preference for retail as focal context. One of these (Chipotle) also fills a
real gap: the original 7 had no clean "full absorption, explicitly will not raise prices"
case.

---

## 8. IKEA — Furniture/home goods retail
Explicit tariff attribution, quantified: sofas +~$50, bedroom sets +~$100. Consumer-facing
retail, strong parallel to Williams-Sonoma (#7 in original corpus).
Source: [AOL/multiple outlets](https://www.aol.com/articles/ikea-home-depot-more-retailers-140000050.html)
→ Codes: `causation-explicit`, `numeric-transparency`

## 9. La-Z-Boy — Furniture retail
Price increases following the 25% furniture tariff. Consumer-facing.
→ Codes: `causation-explicit`, `industry-norm-appeal` (part of a furniture-sector-wide wave)

## 10. Lovesac — Furniture retail
"Tariff mitigation plan" explicitly combining price increases + sourcing diversification +
supplier concessions — richest mitigation-narrative language found in this expansion pass,
strong match to Theme 3.
→ Codes: `causation-explicit`, `mitigation-narrative`, `restraint-language`

## 11. Chipotle — Food service/restaurant
CEO explicitly stated intent to **absorb** tariff costs rather than pass to consumers
("It is our intent as we sit here today to absorb those costs"), while flagging this could
change later. **Fills a real gap** — the original 7 corpus had no clean full-absorption/
no-pass-through case; GMS's surcharge reduction is the closest but is about lowering an
existing surcharge, not a forward-looking absorption promise.
→ Codes: `causation-explicit`, `full-absorption-promise` (new code, not in original 5 themes
— flag for Phase 3 review as a possible Theme 6 candidate), `restraint-language`,
`hedged-commitment` (the CEO's "as we sit here today" qualifier)

## 12. Birkenstock — Footwear retail
Mixed/nuanced: absorbing tariffs "across a variety of channels" but making style-by-style
price decisions. A genuine middle case between full pass-through and full absorption —
useful if Theme 2/Cost-Response ends up needing a 3rd granularity level in future work,
though the current locked design treats Cost-Response as binary.
→ Codes: `causation-vague` (channel-level, not itemized), `mitigation-narrative`,
`selective/style-by-style framing` (new code)

## 13. Walmart — General merchandise retail
Executives publicly acknowledged tariff-driven inflation across general merchandise
(electronics, appliances) — large-format, mass-market retail, different scale/positioning
than anything in the original 7.
→ Codes: `causation-explicit`, `category-broad` (not itemized to specific products)

## 14. Insteel Industries — Steel/industrial (B2B)
CEO Woltz: vivid, quotable causation-explicit language on shipping-cost tariff pass-through
("$1,500 to $3,000... somebody's gotta pay the bill"). More B2B-skewed like Lennox/Dormakaba/
GMS, but strong quote quality for illustrating Theme 2 in the paper's write-up.
Source: [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/07/23/insteel-industries-iiin-q3-2026-earnings-call-transcript/)
→ Codes: `causation-explicit`, `vivid-quotable-framing`

## 15. Home Depot — Home improvement retail
Flagged in the same retailer round-up as IKEA for tariff-driven price increases across
categories. Needs its own primary-source pull to confirm specific language before coding in
detail — included here as a placeholder candidate, weakest-sourced of the 8.

---

## Corpus status after this pass
**7 original + 8 new candidates = 15**, hitting the low end of the standard TA sample size.
Recommend pulling primary sources and doing real Phase 1 coding on 12-13 of these 15
(Home Depot is the weakest lead and could be dropped or replaced), which lands the corpus
in the 15-20 range the shared method calls for.

## What's still yours to do (same rule as the original 7)
1. Decide which of these 8 are worth pulling primary sources for.
2. Full Phase 1 coding once primary sources are in hand (draft codes above are illustrative,
   not final).
3. Phase 3 theme review — human-only, including whether Chipotle's `full-absorption-promise`
   deserves to be a genuine 6th theme or folds into an existing one.
4. Decide whether Birkenstock's style-by-style granularity is worth revisiting the
   Cost-Response factor's binary structure — flagging this as a possible design question, not
   deciding it.
