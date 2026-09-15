# 2026-09-15 — Tax-statute pass, SSRN co-author verification, Category F expansion, identification-strategy precedent

This project hadn't had a dedicated pass since ~09-08/09-09 and was flagged overdue. This session
worked the priority queue from that flag: (1) the promo-deduction tax-treatment gap in
`policy/state_policy_variables.md`, (2) the still-open McCarthy/Taylor third-co-author
verification, (3) Category F literature expansion, (4) identification-strategy literature
precedent search. All four were worked; nothing was skipped.

## 1. Promotional-deduction tax-treatment statute pass (`policy/state_policy_variables.md`)

The 09-09 entry flagged the promo-deduction column as the thinnest dimension across nearly every
coded state, because the AGA Responsible Gaming Guide used for the RG/advertising columns isn't
reliably comprehensive on tax treatment. This pass went directly to primary sources — each state's
actual sports-wagering tax statute (state legislature/code sites, with law.justia.com/
codes.findlaw.com/lawserver.com used as verbatim-statute mirrors only where a .gov server itself
403'd or 503'd a direct fetch) — for the 9 states that had genuinely no promo-deduction entry:
Massachusetts, Maine, New Jersey, North Carolina, Illinois, Arizona, Michigan, Pennsylvania, and
Tennessee. All 9 are now filled in with statute-level detail, not AGA-guide inference. Full detail,
including quoted statutory language and citations, is in each state's row in the policy file and
in a new summary table there.

**What the statute pass found, in brief**: promotional-deduction treatment is not a binary — it's
at least a four-way categorical variable across the states checked: (a) **no deduction identified
in the statutory definition at all** (Massachusetts, Maine, Illinois — the "adjusted gross
receipts" definitions in these states simply don't mention free play/promotional credits, so the
reading is that promotional handle gets taxed as real revenue; flagged as an inference from
omission, not a certainty, since a separate provision could exist that these searches didn't
surface); (b) **an explicit, capped/thresholded deduction** (New Jersey's $8-12M/year threshold
before any deduction kicks in; Arizona's legislated 5-year phase-out from 20% down to 0%); (c) **an
explicit, apparently uncapped deduction** (Michigan, Pennsylvania — both confirmed via statute
text, and for Pennsylvania also confirmed in active use via a real July 2026 monthly revenue report
showing ~20% of gross win deducted as promotional credits); (d) **full disallowance of everything**
(Tennessee, which scrapped its old adjusted-gross-revenue tax entirely in 2023 for a flat 1.85%
handle tax that deducts nothing — not even winnings — as a deliberate trade for looser promotional
*content* rules). North Carolina turned up a genuinely new, dated finding: **Session Law 2026-31
(SB 595), effective July 1, 2026**, just tightened NC's definition of taxable revenue to include
re-wagered promotional credits — a live, primary-source-confirmed mid-sample policy change for a
state already in this project's design, worth flagging for whoever eventually builds the analysis
panel so it isn't coded as a constant.

This confirms and sharpens the RI/WV divergence the 09-09 pass already flagged (RI fully exempts
promo credits from tax, WV disallows the deduction entirely) — it's not an RI/WV-specific oddity,
it's a real, multi-category dimension across the whole panel that the eventual stringency construct
needs to represent honestly rather than collapsing into a single number too early.

**Not done this pass**: re-verifying the promo-deduction entries for the 8 states that already had
statute-level or near-statute-level sourcing from the 09-09 pass (OH, CO, NY, VA, LA, RI, WV) — those
were treated as already adequate. Expanding beyond the current 17 states toward full ~37-40-state
coverage is still open (mechanical from here using the same two-track method demonstrated this
pass).

## 2. McCarthy/Taylor third co-author — resolved via direct SSRN search

`notes/claims_to_verify.md` item 6 asked for a direct SSRN search (not just Consensus.app) before
ever citing the working paper's full author list. Done: the third co-author is **Kenneth C. Wilbur,
UC San Diego Rady School of Management** — confirmed independently across the SSRN abstract listing
itself plus three further mirrors (SMU Scholar institutional repository, the Marketing Science
Institute's own working-paper page, and a UC San Diego news release), all agreeing on the same
three-author list (McCarthy, Taylor, Wilbur). One genuine wrinkle, not a fabrication risk: the paper
appears to have been retitled across revisions/venues — at least three different titles turned up
for what looks like the same underlying SSRN abstract (ID 4856684) — so don't lock in one title as
definitive without checking SSRN directly at citation time (its own page 403'd on direct fetch this
session; the abstract_id itself is stable and is the thing to check against). Full detail in
`notes/claims_to_verify.md` item 6 and the corresponding `literature/literature_map.md` row, both
updated with the confirmed author list and the title-versioning caveat.

## 3. Category F (marketing/consumer research) literature expansion

Three new, fully-verified entries added to `literature/literature_map.md`, plus one existing entry
(Di Censo et al.) upgraded from "venue not captured" to fully sourced with exact regression
coefficients:

- **Han & Saunak (2025), *Journal of Gambling Studies*** — a genuine experimental (not just
  correlational) study of celebrity-endorser effects in sportsbook advertising, 383 US sports
  bettors, finding endorser image-congruence increases both betting intentions and responsible-
  gambling-message awareness, with a race-contingent effect depending on local social acceptance of
  sports betting. This is the closest thing found in this or the prior session's searches to a real
  US-specific, persuasion/consumer-psychology-framed empirical treatment of sportsbook advertising
  tactics.
- **Meiselbach, Clarkwest, Westermeyer & Eisenberg (2026), *Health Affairs Scholar*** — current
  (2024-2025) podcast-advertising spend data: sportsbooks spent $63.4M on podcast ads in 2025, 2.9x
  alcohol-industry spend, DraftKings alone outspending all alcohol advertisers combined. Not a
  marketing/consumer-psychology paper, but a real, current, rigorously sourced number for the
  manuscript's motivation section on the scale/sophistication of sportsbook ad spend.
- **Holbert & Holbert (2025), *Communication & Sport*** — secondary analysis of 2022 Pew American
  Trends Panel data (N=3,900, nationally representative US sample): social-media news
  exposure/satisfaction predicts belief that sports betting is good for society and predicts actual
  gambling behavior, though not baseline awareness of legalization. Corroborated via multiple
  independent secondary listings since SAGE's own page 403'd on direct fetch — flagged 🔶 rather than
  ✅ per this project's existing verification-tier convention.
- **Di Censo, Delfabbro & King (2024), *Journal of Gambling Studies*** — venue, sample, and exact
  coefficients now confirmed via direct PMC full-text read (was previously "exact venues not
  captured"). Important correction to how this should be cited going forward: **the sample is UK
  and Australia (88.4% UK-born), not the US** — the existing map entry didn't specify this, and it
  matters given this project's US focus. Perceived susceptibility to inducements is the strongest
  marketing predictor of problem-gambling severity found in this category (β=.41, p<.001).

**The core gap is still real and is stated plainly, not spun**: no peer-reviewed article in a
marketing-specific journal (JPP&M, JCR, JCP, Journal of Advertising, Journal of Macromarketing,
Journal of Consumer Affairs) studying US sportsbook advertising directly was found in this pass
either, despite dedicated searches targeting those venues by name. The honest caveat: this and the
09-04 pass have both used general web search / Consensus.app, not a systematic database search of
those journals' actual back issues — it's possible such a paper exists and doesn't surface well in
general search. Literature map is now at roughly 32 substantively documented entries (up from ~29),
still short of the 30-50 target but closer, and Category F specifically has gone from genuinely thin
to a real, if not marketing-journal-specific, evidence base.

## 4. Identification-strategy literature precedent (threats_to_validity.md reviewer-criticism #5)

A dedicated search for analogous "vice/settlement-revenue dependence → regulatory stringency"
designs (checked: severance-tax/resource-curse literature, tobacco-settlement literature, general
sin-tax political economy) found one genuinely close, directly usable, verified precedent:
**Jayawardhana, Bradford, Jones, Nietert & Silvestri (2014), *PLoS ONE*** — using 50-state panel
data, they find a state's per-capita Master Settlement Agreement (tobacco settlement) disbursement
is *negatively* associated with the Strength of Tobacco Control Index (i.e., more settlement-revenue
dependence predicts weaker tobacco-control regulation) — the same directional mechanism this
project hypothesizes for gambling, in a structurally analogous setting (an ongoing state revenue
stream tied to a regulated vice industry, predicting regulatory laxity). Method: plain fixed-effects
panel regression, no instrumental variable, with an explicitly acknowledged and *unresolved*
endogeneity caveat (their outcome could itself affect their predictor). No shift-share or other IV
application was found for this class of question either, so the 09-09 finding stands that no ready-
made instrument exists to borrow — this project's own shift-share robustness check, if built, would
still be original. But this precedent meaningfully de-risks Britton's currently-recommended
associational-primary-specification choice: it's not a compromise invented to paper over a missing
instrument, it's how a structurally similar question has actually been published before. Added to
`research_design/identification_strategy.md` and cross-referenced from
`research_design/threats_to_validity.md`'s reviewer-criticism #5.

## For Britton

Two concrete wins to know about: the promo-deduction tax-treatment gap you flagged as the next
step on 09-09 is closed for all 9 states that were missing it, sourced directly against actual
state statutes rather than the AGA guide — and it turned up a real, dated policy change (North
Carolina tightened its promotional-credit tax treatment effective July 1, 2026) that's worth
keeping in mind once someone builds the actual analysis panel, since it's a mid-sample change for
a state already in the design. The McCarthy/Taylor/Wilbur working paper's author list is now fully
confirmed directly from SSRN and three independent mirrors — safe to cite the full three-author
list going forward, just double-check which title is current on SSRN itself at the time you cite
it, since it's been retitled at least twice across revisions.

On literature: Category F picked up three solid new papers this pass, including a real US-based
experimental study on celebrity endorsers in sportsbook ads (Han & Saunak 2025) that's about as
close as anything found so far to the marketing-journal treatment this project has been looking
for — it's just published in Journal of Gambling Studies rather than a marketing journal. The
actual gap — a JPP&M/JCR/Journal of Advertising-specific US sportsbook-advertising paper — still
wasn't found, and I want to be straightforward that this project's searches (both this pass and
09-04) have been general web search, not a real database search of those journals' back issues, so
"not found" here means "not found by these methods," not "confirmed not to exist."

On the identification-strategy question (still the single most serious open design issue): I found
a real precedent — a published paper studying tobacco-settlement-revenue dependence and finding it
predicts weaker tobacco-control regulation, using the same kind of associational panel design your
Study 1 would use, with the same kind of endogeneity caveat named openly rather than solved. This
doesn't make the identification-strategy choice for you, but it's good evidence that reviewers at a
real journal have accepted this exact class of design for a structurally similar question before.
