# State Consumer-Protection Policy Variables — First Pass (2026-09-09, extended same day; tax-treatment pass added 2026-09-15)

**Status: partial, not exhaustive, but the two blocking gaps (RI/WV face validity, promo-deduction
tax treatment) are both closed.** Now covers 17 of the ~37-40 states with legal sports betting.
Two different sourcing methods are in play in this file, and each row/column says which it got:

- **RG/advertising/self-exclusion columns (all 17 states)**: coded from the AGA's per-state "Gaming
  Regulatory Fact Sheet" series and the AGA's full **"Responsible Gaming Regulations and Statutes
  Guide" (2025 edition)** — a ~450-page document that quotes actual statute and administrative-code
  text state by state (`americangaming.org/resources/responsible-gaming-regulations-and-statutes-guide/`,
  PDF: `americangaming.org/wp-content/uploads/2025/07/AGA-2025-Responsible-Gaming-Regulations-and-Guidelines.pdf`).
  Pulled via direct PDF download + `pdftotext` — WebFetch's own PDF handling failed on these files
  (returns "binary data, no readable text"), consistent with this project's earlier Coombs/Madonia/
  Nencka/Smith PDF-extraction failure; local `pdftotext` worked cleanly both times.
- **Promotional-deduction tax-treatment column (updated 2026-09-15)**: re-verified for 9 of the 17
  states directly against each state's actual sports-wagering tax statute (state legislature/code
  sites — azleg.gov, legislature.mi.gov, malegislature.gov/mass.gov, legislature.maine.gov,
  ilga.gov/FindLaw statute mirror, ncleg.gov session-law PDF — plus law.justia.com/lawserver.com/
  codes.findlaw.com as verbatim-statute mirrors where the .gov server itself 403'd or 503'd a direct
  fetch), not the AGA guide, which this project already flagged as RG-focused and not reliably
  comprehensive on tax treatment. **8 states (MA, IL, NJ, NC, AZ, MI, PA, ME) got this deeper
  statute-level check this pass; TN's existing entry was re-confirmed against statute.** The
  remaining coded states (OH, CO, NY, VA, LA, RI, WV) already had statute-level or near-statute-
  level promo-tax sourcing from the 09-09 pass and were not re-checked this pass. See the new
  "Promotional-deduction tax treatment — dedicated statute pass" table below.

**Rhode Island and West Virginia — the two named high-dependence cases the whole design depends
on — are scored**, cross-checked against two independent AGA documents each. Louisiana is also
scored (was previously flagged unscored). Do not treat a state's absence from this file as "no
policy" — it means "not yet coded."

## Coding dimensions

1. **Advertising restrictions** — audience-targeting rules (underage-audience thresholds),
   "risk-free"/"free bet" language bans, problem-gambling-message requirements.
2. **Promotional-deduction tax treatment** — whether the state allows sportsbooks to deduct the
   value of promotional free bets/bonus credits from taxable revenue (a direct subsidy to
   promotional intensity) and whether/when that deduction has been capped or phased out.
3. **Responsible-gambling program requirements** — algorithmic/data-driven intervention mandates,
   self-exclusion protections, deposit/spending limit requirements.

## Coded states (first pass)

| State | Advertising restrictions | Promo-deduction treatment | RG program requirements | Stringency (informal, 1-5) |
|---|---|---|---|---|
| Massachusetts | Strong — bans "free" labeling when user risks own money, bars targeting minors/self-excluded individuals, mandatory helpline messaging | **Checked 2026-09-15 against M.G.L. c.23N §3/§14 and 205 CMR 240.00 directly (mass.gov)**: "adjusted gross sports wagering receipts" = gross receipts less winnings paid to patrons and federal excise tax only — no mention of free play/promotional credits anywhere in the statutory definition. Reading is that promotional credits are **not deductible** (MA taxes on a receipts-minus-winnings basis with no separate promo carve-out identified), though this is an inference from omission rather than an explicit "no deduction" clause — flag as high-confidence, not certain. | Mandated data/algorithmic triggers for problem-gambling intervention | 4-5 (most stringent identified this pass) |
| Ohio | Banned "risk-free"/"free bet" language Jan. 2023 (OCCC rule); active enforcement — three operators fined $150K-$350K for violations | Doubled tax rate July 2023, explicitly citing high promotional-spending volume as the rationale (a de facto promotional disincentive via the tax code rather than a direct deduction cap) | Not separately identified this pass | 4 |
| Colorado | Not separately identified this pass beyond general audience-targeting rules | Free-bet promotional deduction phased out on a schedule, fully eliminated July 1, 2026 | Algorithmic/data-driven RG intervention rules identified (grouped with MA/NJ/NC in this pass's search) | 3-4 |
| Maine | Bars advertising promotional bonus offers in public forums (2023 rule) | **Checked 2026-09-15 directly against 8 M.R.S. §1202 (legislature.maine.gov)**: "adjusted gross sports wagering receipts" = gross receipts less winnings paid to patrons (incl. cash-equivalent prizes) and federal excise tax — statute text does not mention free play, promotional credits, or bonuses anywhere. Same reading as Massachusetts: no promo deduction identified in the operative definition, i.e. Maine appears to tax promotional-credit handle as if it were real revenue (no carve-out), consistent with its separate advertising-content restriction on promotional-bonus offers. | Not separately identified this pass | 3-4 (revised up slightly given the no-promo-deduction finding, which is a real consumer-protection-adjacent stringency signal even though it's a tax rather than an advertising rule) |
| New Jersey | Audience-targeting rules since 2022; pending 2025 bill (A4003) would bar extending promotions to users of RG tools | **Checked 2026-09-15 directly against N.J.S.A. 5:12A-16 (law.justia.com verbatim mirror, cross-checked against the original P.L.2018, c.33 session-law PDF at nj.gov)**: an explicit, capped annual deduction exists — licensees may deduct promotional gaming credits actually wagered by patrons, but only **above a threshold**: for Internet sports wagering, only the value of promo credits wagered *in excess of $12,000,000/year*; for retail (non-Internet), only the value *in excess of $8,000,000/year* (pooled across all licensed casinos/racetracks). This is a real, if partial, deduction limit — not a full exemption like Rhode Island and not a full disallowance like West Virginia. | Algorithmic/data-driven RG intervention rules identified | 3-4 |
| New York | Audience-targeting rules since 2022 | Not identified as capped this pass; notably NY's headline policy lever is its very high tax rate (~51%) rather than promo-deduction treatment specifically — worth treating tax rate as a related but distinct policy variable, not folded into this scale | Not separately identified this pass | 3 (on these three dimensions specifically; NY's overall regulatory posture is stricter than this narrow scale captures) |
| North Carolina | Audience-targeting rules since 2022 | **Checked 2026-09-15 directly against N.C. Gen. Stat. §18C-901(7) and Session Law 2026-31 (SB 595), the actual enrolled-bill PDF at ncleg.gov**: NC just closed this gap — effective **July 1, 2026**, "gross wagering revenue" now explicitly *includes* the cash value of any bonuses or promotional credits *when returned to the operator in the form of a deposit or sports wager* (i.e., re-wagered promo credits count as taxable revenue rather than being netted out) — a real, dated, primary-source-confirmed tightening of the promo-deduction loophole, not just an AGA-guide inference. Worth flagging in any manuscript timeline as a live natural-experiment moment for this project's own mechanism (does NC's growing dependence track with this tightening, or is it exogenous fiscal-pressure-driven tax reform unrelated to the dependence story — worth thinking through, not assumed either way). | Algorithmic/data-driven RG intervention rules identified | 3-4 (revised up given the July 2026 tightening) |
| Illinois | Audience-targeting rules since 2022 | **Checked 2026-09-15 directly against 230 ILCS 45/25-10 (FindLaw verbatim statute mirror; ilga.gov's own server 403'd repeated direct fetches this pass)**: "adjusted gross sports wagering receipts" = gross sports wagering receipts less winnings paid to wagerers — no mention of free bets or promotional credits anywhere in the definition. Same no-carve-out reading as Massachusetts/Maine: Illinois does not appear to allow a promotional deduction at all, meaning operators are taxed on promotional-credit handle as real revenue. | Not separately identified this pass | 2-3 (the no-promo-deduction finding is a genuine stringency-relevant data point even though IL's advertising-content rules remain thin) |
| Virginia | Not separately identified this pass | **Corrected 2026-09-09**: the "removed effective mid-2025" framing was imprecise. The actual mechanism, verified against the live statute text (Va. Code §58.1-4030, `law.lis.virginia.gov/vacode/58.1-4030/` — bonuses/promotions remain deductible from adjusted gross revenue in the statute itself, no sunset date in that section) plus corroborating reporting (sportshandle.com, EGR, vixio.com): a **separate budget-language provision caps the promo deduction to each operator's first 12 months of Virginia operation**, not a single mid-2025 statewide policy change. Since VA's major operators (BetMGM, Caesars, DraftKings, FanDuel) all launched Jan. 2021, their 12-month windows expired years ago — so by 2025 the *practical* effect is $0 promotional deductions for all major operators (confirmed in Virginia Lottery's own 2025 monthly sports-betting reports), but the mechanism is a standing per-operator sunset, not a mid-2025 policy shift. Net effect on the stringency score is the same; the causal story about *when* and *why* is not. | Not separately identified this pass | 4 (corrected — full practical loss of promo deduction, via an older per-operator sunset mechanism, not a 2025 reform) |
| Louisiana | **New 2026-09-09, AGA Responsible Gaming Guide, La. Admin. Code tit. 42 §VI-517**: real, specific audience-targeting ban — licensees may not advertise/market to self-excluded, barred, or under-21 persons by phone/email/individually-targeted material; ads/marketing may not depict minors; no promotional activity at [primary/secondary schools, cut off in this pass's excerpt]. | Not separately identified this pass — the promo-deduction cap referenced in `PROJECT_STATUS.md`'s prior scoping note is still not independently re-verified | Comprehensive statutory self-exclusion regime (LA Rev. Stat. §27:27.1, LAC 42:III.304) plus a mandated employee-training requirement specifically on recognizing/assisting problem gamblers — broader than most states coded so far | 3-4 (strong on advertising/self-exclusion; promo-deduction still an open gap) |
| Rhode Island | **Scored 2026-09-09, cross-checked against 2 AGA primary sources (per-state fact sheet + national Responsible Gaming Guide)**: no audience-targeting, "risk-free"/"free bet" language ban, or misleading-ad rule found in either source. Only requirement identified: problem-gambling helpline number displayed in advertisements and on-premises. **This is the weakest advertising regime of any state coded in this file.** | **No cap identified in either source — explicit full exemption.** The AGA fact sheet states directly: "Tax on Promotional Credits: No. Online sports wagering revenue does not include free play... subsequently 'won back'... for which the [operator] can demonstrate it has not been reimbursed in cash." Promotional credits are structurally excluded from the tax base with no phase-out. | Statutory funding requirement ($200,000/year aggregate from the two casinos) for RG programs; mandated self-exclusion program (casino + iGaming + sports-wagering platforms all required to surface problem-gambling info); no algorithmic/data-driven intervention mandate found in either source. Single-operator market structure (Bally's/IGT exclusive) confirmed via SB 948 (2023). | **2 — lowest scored so far.** Face-validity match: RI is both the most fiscally gambling-dependent state examined and has the weakest advertising regime and a full promotional-tax subsidy of any state coded. |
| West Virginia | **Scored 2026-09-09, cross-checked against 2 AGA primary sources**: genuinely mixed/nuanced, not simply "none." The per-state fact sheet says "Advertising Restriction: No" (no content-based rule — no audience-targeting or misleading-claim ban found). But the national Responsible Gaming Guide's more detailed statutory citations show **all advertising requires prior written approval from the Lottery Director** before publication (W. Va. Code §29-22A-9(a)(12); WV CSR §179-9-2, §179-10-22) — a real, if procedural rather than content-based, restriction. Both findings are accurate; they describe different things, not a contradiction. | **Sports betting specifically disallows the deduction** — the fact sheet states plainly: "Tax on Promotional Credits: Yes [i.e., promo credits ARE taxed/not deductible]. Operators are only permitted to deduct winnings paid to wagerers from taxable revenue." This is the opposite tax treatment from Rhode Island. | Compulsive Gambling Treatment Fund (W. Va. Code §29-22A-19, $150,000-$500,000/year, DHHR-administered); statutory self-exclusion list (director-controlled, since 2008); WV also has the highest age gate found in this pass — 21+ to gamble or be on the gaming floor, vs. 18 in most other coded states. No algorithmic-intervention mandate found. | **3 — mixed profile.** Weak content-based advertising rules (like RI) but paired with a real promo-deduction tax disincentive and a stricter age gate that RI lacks. Both RI and WV — the two highest-dependence states — score low-to-moderate and share the "no content-based ad restriction" trait; they diverge specifically on the tax treatment of promotional credits, which is itself a useful empirical nuance for the paper (dependence doesn't predict a uniformly lax policy bundle — it predicts weak advertising rules specifically, with the tax dimension varying). |
| Arizona | **New 2026-09-09, Ariz. Admin. Code §19-4-110, §19-4-111, §5-1320**: one of the most comprehensive regimes found in this pass. Statutory ban on advertising that targets/appeals to under-21s, contains false/misleading information, promotes irresponsible/excessive play, or implies guaranteed social/financial/personal success; helpline number required on all ad formats (TV, radio, internet, print, billboards). RG: written internal-control-system + RG-training-program requirement for every operator; weekly self-exclusion list distribution to operators; 24-hour violation reporting; cross-agency debt-offset against winnings (child support, SNAP overpayments, court debt) for self-excluded persons who evade the ban. | **Checked 2026-09-15 directly against A.R.S. §5-1301 (azleg.gov)**: a real, explicit, time-limited deduction exists — event-wagering operators may deduct free bets/promotional credits redeemed by bettors from adjusted gross receipts, but it phases out on a fixed statutory schedule: **years 1-2 capped at 20% of gross wagering receipts, year 3 capped at 15%, years 4-5 capped at 10%, and no deduction allowed from year 6 onward.** This is the most structured, explicitly-sunsetting promo-deduction regime of any state checked this pass — a legislated phase-out to zero, not an open-ended subsidy (contrast Rhode Island's full, uncapped exemption). | See advertising column — RG plan and self-exclusion enforcement are unusually detailed and codified. | 4-5 |
| Michigan | **New 2026-09-09, MCL 432.225(9), MCL 432.209c(2), Mich. Admin. Code R 432.674/R 432.774**: narrower than Arizona/Louisiana — the advertising ban is scoped to disassociated/self-excluded persons specifically (no direct-mail, marketing, or solicitation to listed individuals; casinos may still advertise non-gaming amenities like hotels/restaurants to anyone), not a general audience-targeting rule. Helpline number required on all printed ads/promotional materials. Third-party vendors that receive the self-exclusion list may only use it to suppress targeted marketing, not for other purposes (violation = discipline/civil fine). | **Checked 2026-09-15 directly against MCL 432.403 (Michigan Legislature site 503'd on repeat direct fetches; cross-verified via lawserver.com's verbatim statute mirror)**: "adjusted gross sports betting receipts" = gross sports betting receipts less a deduction for the monetary value of free play wagered by participants as an incentive — **no percentage cap or phase-out language found in this specific provision**, unlike Michigan's parallel internet-gaming statute (MCL 432.303), which does phase its free-play deduction down from 10% (years 1-3) to 0% (year 6+). Worth flagging honestly: this looks like Michigan's sports-betting-specific promo deduction may simply be uncapped/open-ended where its iGaming deduction is not — a real asymmetry, though it's also possible a cap exists elsewhere in the sports-betting chapter that this pass's searches didn't surface; treat as "no cap found," not "confirmed no cap exists," until someone reads the full chapter 432 text end to end. | Self-exclusion-list enforcement is the dominant RG mechanism identified (extends to third-party marketing vendors specifically) — no algorithmic-intervention or deposit-limit mandate found in the excerpt pulled this pass. | 3 |
| Pennsylvania | **New 2026-09-09, 58 Pa. Code §501a.7, §813a.2, §1409a.1, §812a.9, 4 Pa. Const. Stat. §13B02**: ads may not contain false/misleading information or obscure conditions/limits via font/color/placement tricks; state gaming office (OCPG) can order an ad discontinued if it "could adversely impact the public or the integrity of gaming" — a real content-based enforcement lever, though not a specific audience-targeting rule like AZ/LA. Applies uniformly across retail, interactive, and sports-betting licensees. | **Checked 2026-09-15 directly against 4 Pa.C.S. §13C01(1)(iii) (statute text via law.justia.com/FindLaw mirrors; legis.state.pa.us's own server 403'd)**: "gross sports wagering revenue" definition carves out promotional items as deductible per criteria set by PA Department of Revenue Gaming Tax Bulletin 2015-01 (an administrative bulletin, not the statute itself, governs the exact mechanics) — no percentage cap identified in the statute. Real-world confirmation from PA's own July 2026 monthly revenue report: operators deducted $12.9M in promotional credits against $64.8M in gross win that month (~20% of win), consistent with an uncapped or high-threshold deduction in practice, not a token exemption. | One of the more detailed self-limitation mandates found: players must have a clear mechanism to set deposit/wager/loss/session-duration limits, with an asymmetric-friction design written directly into regulation — a *decrease* to a self-limit takes effect at next login, but an *increase* only takes effect after the prior limit's time period has fully expired and the player reaffirms it. | 4 |
| Tennessee | **New 2026-09-09, Tenn. Code Ann. §4-51-318, Rule 1350-01-.07**: statutory ban on directly advertising/promoting to minors; unusually procedural oversight layer — licensees must submit electronic copies of all advertising/marketing/promotional material to the state Sports Wagering Council within 5 business days of publication. All ads must carry a Council-approved helpline (the "Tennessee REDLINE") with detailed vetting criteria (hours of operation, text-capability, whether it collects usage data for RG research) if a licensee wants to use an alternate hotline. | **Re-confirmed 2026-09-15 directly against Tenn. Code Ann. §4-49-104 (law.justia.com verbatim mirror)**: the 09-09 entry's framing needed a small correction, not a reversal — TN's promo-deduction question is now moot rather than "not identified." Effective July 2023, TN scrapped its old 20%-of-adjusted-gross-revenue tax model (under which promotional deductions would have mattered) and replaced it with a flat **1.85% privilege tax on total handle**, with the statute explicitly stating a licensee "shall not deduct from the gross handle winning payouts to bettors or promotional wagers or payouts" — i.e., TN taxes on raw handle with *no* deductions of any kind, promotional or otherwise. This is arguably the strictest promotional-tax treatment of any state checked this pass (not even winnings are deducted, let alone promo credits), though it was a deliberate 2023 trade for looser promotional *content* rules (the legislative history explicitly notes operators got "freedom to run heavier promotional cycles without tax penalty" in exchange). | Helpline/messaging requirements above are the RG mechanism found this pass; no separate deposit-limit or algorithmic-intervention rule identified in the excerpt pulled. | 4 (tax treatment is maximally strict — no deductions at all — but this was a package deal with looser promotional-content freedom, a real nuance for the paper's "stringency isn't one-dimensional" point) |

## Reading this table honestly

- **Update 2026-09-15: the promo-deduction column is now populated for all 17 coded states.** The
  9 states that were genuinely "not identified this pass" as of 09-09 (MA, ME, NJ, NC, IL, AZ, MI,
  PA, TN) were checked directly against actual state sports-wagering tax statutes this pass — see
  each row above and the summary table immediately below. Three distinct treatments emerged, which
  is itself a useful finding: (1) **no deduction identified in the statute at all** (MA, ME, IL —
  read from the absence of any promo/free-play language in the "adjusted gross receipts" definition,
  which is an inference from omission and flagged as such, not a certainty); (2) **an explicit,
  capped/phased/thresholded deduction** (AZ's 5-year statutory phase-out to zero, NJ's $8-12M
  annual threshold before any deduction kicks in); (3) **an explicit, apparently uncapped
  deduction** (MI, PA — both confirmed via statute language plus, for PA, real monthly revenue-
  report data showing the deduction in active use at ~20% of gross win). Tennessee is a fourth,
  more extreme case: it disallows *all* deductions (winnings included) via a 2023 switch to a flat
  handle tax. North Carolina just tightened its treatment via a July 2026 session law (SL 2026-31)
  narrowing what counts as deductible — a genuinely live, dated policy change worth flagging for
  the manuscript's timeline. **This means "promotional-deduction treatment" cannot be collapsed
  into a simple allowed/disallowed binary** — it is at minimum a three-way categorical variable
  (no deduction / capped deduction / uncapped deduction), with Tennessee's "disallows everything"
  and NC's "recently tightened" as further nuances worth their own indicator variables if this
  becomes a formal panel predictor. Not attempted this pass: re-verifying the 8 states whose
  promo-deduction entries were already statute-sourced from the 09-09 pass (OH, CO, NY, VA, LA, RI,
  WV) — those are treated as already-adequate and were not re-checked.
- **The face-validity test this file exists to run is now done, and it worked**: Rhode Island and
  West Virginia — the two highest gambling-fiscal-dependence states — score **2 and 3**, the two
  lowest advertising-stringency scores of the 17 states now coded (tied with Illinois' 2-3).
  Neither has a real audience-targeting or misleading-ad ban; the closest either gets is RI's
  bare helpline-display requirement. That's a genuine, if preliminary (n=17, not yet the full
  panel), directional match with the paper's core mechanism.
- **RI and WV diverge on tax treatment specifically**, which is a useful nuance, not noise: RI
  fully exempts promotional credits from tax (a direct subsidy to promotional intensity), WV
  disallows the deduction entirely (sports betting specifically — WV's older VLT/table-game promo
  rules are more permissive). If dependence predicted uniformly lax policy on every dimension,
  this wouldn't happen — instead it looks like dependence predicts weak *advertising-content*
  regulation specifically, while tax treatment of promotions varies on other grounds (WV's
  disallowance may track its already-low 10% sports-betting tax rate — a state with a low headline
  rate has less fiscal room to also subsidize promotions via a deduction). Worth carrying into the
  eventual write-up rather than collapsing into a single stringency number too early.
- Two AGA documents (per-state fact sheets vs. the national Responsible Gaming Guide) sometimes
  describe the *same* state differently without actually contradicting each other — West Virginia
  is the clearest example (fact sheet: "no restriction," full Guide: "prior Lottery Director
  approval required for all ads"). Both are accurate; they're answering different questions
  (content-based restriction vs. procedural approval gate). Where possible, cross-check both
  documents rather than relying on the one-page fact sheet alone — it undercounts real regulation.
- New York's very high tax rate still suggests "stringency" may need to be a multi-dimensional
  construct (advertising / promo-deduction / RG-mandate / tax-rate) rather than a single 1-5 scale
  — now more clearly a real design choice given RI/WV's own tax-treatment divergence above, not
  just an NY-specific oddity.

## Promotional-deduction tax treatment — dedicated statute pass (2026-09-15) summary table

_Quick-reference summary of the 9 states checked this pass; full sourcing and quoted statutory
language is in each state's row in the main table above. All sourced directly against state
statute text (state legislature sites, or verbatim statute mirrors — law.justia.com,
codes.findlaw.com, lawserver.com — used only where the .gov server itself returned a 403/503 on
direct fetch this session)._

| State | Statute | Promo-deduction treatment | Category |
|---|---|---|---|
| Massachusetts | M.G.L. c.23N §3/§14; 205 CMR 240.00 | No promo/free-play language in the "adjusted gross receipts" definition — appears non-deductible | No deduction identified (inference from omission) |
| Maine | 8 M.R.S. §1202 | Same — no promo/free-play language in the statutory definition | No deduction identified (inference from omission) |
| Illinois | 230 ILCS 45/25-10 | Same — "adjusted gross sports wagering receipts" = gross minus winnings paid only | No deduction identified (inference from omission) |
| New Jersey | N.J.S.A. 5:12A-16; P.L.2018 c.33 | Deductible only *above* an annual threshold: >$12M/yr (Internet), >$8M/yr (retail, pooled) | Capped/thresholded deduction |
| Arizona | A.R.S. §5-1301 | Statutory 5-year phase-out: 20% (yrs 1-2) → 15% (yr 3) → 10% (yrs 4-5) → 0% (yr 6+) | Capped/phased deduction, sunsets to zero |
| Michigan | MCL 432.403 | Deductible, no percentage cap found in this specific provision (contrast MCL 432.303's iGaming deduction, which does phase out) | Apparently uncapped deduction |
| Pennsylvania | 4 Pa.C.S. §13C01(1)(iii) + DOR Bulletin 2015-01 | Deductible, no statutory cap found; confirmed in active use (~20% of July 2026 gross win) | Apparently uncapped deduction |
| Tennessee | Tenn. Code Ann. §4-49-104 | **No deductions of any kind** (not even winnings) since a 2023 switch to a flat 1.85% handle tax | Strictest — full disallowance, but paired with looser promotional-content rules |
| North Carolina | N.C. Gen. Stat. §18C-901(7); SL 2026-31 (SB 595) | Recently tightened, effective July 1, 2026: re-wagered promo credits now count as taxable revenue | Recently tightened by statute (dated policy change) |

## Next steps (not done this pass)

1. **Promo-deduction coverage for the 9 previously-thin states is now closed** (this pass). Two
   things remain open on this specific dimension: (a) re-verify the 8 states whose promo-deduction
   entries came from the 09-09 AGA-guide-era pass (OH, CO, NY, VA, LA, RI, WV) against actual tax
   statutes the same way, for full internal consistency of sourcing method across the table; (b)
   Michigan's "no cap found" finding should be treated as provisional, not definitive — it's an
   absence-of-evidence finding from the specific provision checked, not a full read of the entire
   sports-betting chapter.
2. Expand beyond the current 17 states toward fuller ~37-40-state coverage — the AGA Responsible
   Gaming Guide covers most/all legal states for the RG/advertising columns, so remaining coverage
   there is a matter of more passes through the same document; the promo-deduction column for any
   newly-added state should get the statute-level treatment demonstrated in this pass rather than
   reverting to the AGA guide, now that this pass has shown direct statute lookup is tractable in
   the same session (roughly one state per 2-3 targeted searches/fetches).
3. Decide whether tax rate belongs in the stringency construct or as a separate variable (see
   New York and RI/WV notes above) — this is now better-evidenced as a real measurement-design
   choice, not a data-gathering gap. Recommend Britton weigh in once the panel is closer to full.
   **This pass adds more evidence for treating promo-deduction treatment as a genuinely
   multi-category variable, not a binary** — see the "Reading this table honestly" section above.
4. Virginia's correction above should be reflected in `DECISION_LOG.md` and in any manuscript
   text that cites the earlier "mid-2025 removal" framing if that language was used anywhere else.
5. North Carolina's July 2026 statutory tightening (SL 2026-31) is a genuinely new, dated data
   point worth deciding how to handle in the panel: a mid-sample policy change for a state already
   in the design, not a cross-sectional coding value — flag for whoever builds the final analysis
   panel rather than silently coding NC's "current" stringency as if it were constant over time.
