# State Consumer-Protection Policy Variables — First Pass (2026-09-09, extended same day)

**Status: partial, not exhaustive, but the blocking gap is closed.** Now covers 17 of the ~37-40
states with legal sports betting, coded directly from two primary sources: the AGA's per-state
"Gaming Regulatory Fact Sheet" series and, more importantly, the AGA's full **"Responsible Gaming
Regulations and Statutes Guide" (2025 edition)** — a ~450-page document that quotes actual statute
and administrative-code text state by state (`americangaming.org/resources/responsible-gaming-regulations-and-statutes-guide/`,
PDF: `americangaming.org/wp-content/uploads/2025/07/AGA-2025-Responsible-Gaming-Regulations-and-Guidelines.pdf`).
Pulled via direct PDF download + `pdftotext` — WebFetch's own PDF handling failed on these files
(returns "binary data, no readable text"), consistent with this project's earlier Coombs/Madonia/
Nencka/Smith PDF-extraction failure; local `pdftotext` worked cleanly both times. **Rhode Island
and West Virginia — the two named high-dependence cases the whole design depends on — are now
scored**, cross-checked against two independent AGA documents each. Louisiana is also now scored
(was previously flagged unscored). Do not treat a state's absence from this file as "no policy" —
it means "not yet coded."

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
| Massachusetts | Strong — bans "free" labeling when user risks own money, bars targeting minors/self-excluded individuals, mandatory helpline messaging | Not identified as capped this pass | Mandated data/algorithmic triggers for problem-gambling intervention | 4-5 (most stringent identified this pass) |
| Ohio | Banned "risk-free"/"free bet" language Jan. 2023 (OCCC rule); active enforcement — three operators fined $150K-$350K for violations | Doubled tax rate July 2023, explicitly citing high promotional-spending volume as the rationale (a de facto promotional disincentive via the tax code rather than a direct deduction cap) | Not separately identified this pass | 4 |
| Colorado | Not separately identified this pass beyond general audience-targeting rules | Free-bet promotional deduction phased out on a schedule, fully eliminated July 1, 2026 | Algorithmic/data-driven RG intervention rules identified (grouped with MA/NJ/NC in this pass's search) | 3-4 |
| Maine | Bars advertising promotional bonus offers in public forums (2023 rule) | Not identified this pass | Not separately identified this pass | 3 |
| New Jersey | Audience-targeting rules since 2022; pending 2025 bill (A4003) would bar extending promotions to users of RG tools | Not identified as capped this pass | Algorithmic/data-driven RG intervention rules identified | 3-4 |
| New York | Audience-targeting rules since 2022 | Not identified as capped this pass; notably NY's headline policy lever is its very high tax rate (~51%) rather than promo-deduction treatment specifically — worth treating tax rate as a related but distinct policy variable, not folded into this scale | Not separately identified this pass | 3 (on these three dimensions specifically; NY's overall regulatory posture is stricter than this narrow scale captures) |
| North Carolina | Audience-targeting rules since 2022 | Not identified this pass | Algorithmic/data-driven RG intervention rules identified | 3 |
| Illinois | Audience-targeting rules since 2022 | Not identified this pass | Not separately identified this pass | 2-3 |
| Virginia | Not separately identified this pass | **Corrected 2026-09-09**: the "removed effective mid-2025" framing was imprecise. The actual mechanism, verified against the live statute text (Va. Code §58.1-4030, `law.lis.virginia.gov/vacode/58.1-4030/` — bonuses/promotions remain deductible from adjusted gross revenue in the statute itself, no sunset date in that section) plus corroborating reporting (sportshandle.com, EGR, vixio.com): a **separate budget-language provision caps the promo deduction to each operator's first 12 months of Virginia operation**, not a single mid-2025 statewide policy change. Since VA's major operators (BetMGM, Caesars, DraftKings, FanDuel) all launched Jan. 2021, their 12-month windows expired years ago — so by 2025 the *practical* effect is $0 promotional deductions for all major operators (confirmed in Virginia Lottery's own 2025 monthly sports-betting reports), but the mechanism is a standing per-operator sunset, not a mid-2025 policy shift. Net effect on the stringency score is the same; the causal story about *when* and *why* is not. | Not separately identified this pass | 4 (corrected — full practical loss of promo deduction, via an older per-operator sunset mechanism, not a 2025 reform) |
| Louisiana | **New 2026-09-09, AGA Responsible Gaming Guide, La. Admin. Code tit. 42 §VI-517**: real, specific audience-targeting ban — licensees may not advertise/market to self-excluded, barred, or under-21 persons by phone/email/individually-targeted material; ads/marketing may not depict minors; no promotional activity at [primary/secondary schools, cut off in this pass's excerpt]. | Not separately identified this pass — the promo-deduction cap referenced in `PROJECT_STATUS.md`'s prior scoping note is still not independently re-verified | Comprehensive statutory self-exclusion regime (LA Rev. Stat. §27:27.1, LAC 42:III.304) plus a mandated employee-training requirement specifically on recognizing/assisting problem gamblers — broader than most states coded so far | 3-4 (strong on advertising/self-exclusion; promo-deduction still an open gap) |
| Rhode Island | **Scored 2026-09-09, cross-checked against 2 AGA primary sources (per-state fact sheet + national Responsible Gaming Guide)**: no audience-targeting, "risk-free"/"free bet" language ban, or misleading-ad rule found in either source. Only requirement identified: problem-gambling helpline number displayed in advertisements and on-premises. **This is the weakest advertising regime of any state coded in this file.** | **No cap identified in either source — explicit full exemption.** The AGA fact sheet states directly: "Tax on Promotional Credits: No. Online sports wagering revenue does not include free play... subsequently 'won back'... for which the [operator] can demonstrate it has not been reimbursed in cash." Promotional credits are structurally excluded from the tax base with no phase-out. | Statutory funding requirement ($200,000/year aggregate from the two casinos) for RG programs; mandated self-exclusion program (casino + iGaming + sports-wagering platforms all required to surface problem-gambling info); no algorithmic/data-driven intervention mandate found in either source. Single-operator market structure (Bally's/IGT exclusive) confirmed via SB 948 (2023). | **2 — lowest scored so far.** Face-validity match: RI is both the most fiscally gambling-dependent state examined and has the weakest advertising regime and a full promotional-tax subsidy of any state coded. |
| West Virginia | **Scored 2026-09-09, cross-checked against 2 AGA primary sources**: genuinely mixed/nuanced, not simply "none." The per-state fact sheet says "Advertising Restriction: No" (no content-based rule — no audience-targeting or misleading-claim ban found). But the national Responsible Gaming Guide's more detailed statutory citations show **all advertising requires prior written approval from the Lottery Director** before publication (W. Va. Code §29-22A-9(a)(12); WV CSR §179-9-2, §179-10-22) — a real, if procedural rather than content-based, restriction. Both findings are accurate; they describe different things, not a contradiction. | **Sports betting specifically disallows the deduction** — the fact sheet states plainly: "Tax on Promotional Credits: Yes [i.e., promo credits ARE taxed/not deductible]. Operators are only permitted to deduct winnings paid to wagerers from taxable revenue." This is the opposite tax treatment from Rhode Island. | Compulsive Gambling Treatment Fund (W. Va. Code §29-22A-19, $150,000-$500,000/year, DHHR-administered); statutory self-exclusion list (director-controlled, since 2008); WV also has the highest age gate found in this pass — 21+ to gamble or be on the gaming floor, vs. 18 in most other coded states. No algorithmic-intervention mandate found. | **3 — mixed profile.** Weak content-based advertising rules (like RI) but paired with a real promo-deduction tax disincentive and a stricter age gate that RI lacks. Both RI and WV — the two highest-dependence states — score low-to-moderate and share the "no content-based ad restriction" trait; they diverge specifically on the tax treatment of promotional credits, which is itself a useful empirical nuance for the paper (dependence doesn't predict a uniformly lax policy bundle — it predicts weak advertising rules specifically, with the tax dimension varying). |
| Arizona | **New 2026-09-09, Ariz. Admin. Code §19-4-110, §19-4-111, §5-1320**: one of the most comprehensive regimes found in this pass. Statutory ban on advertising that targets/appeals to under-21s, contains false/misleading information, promotes irresponsible/excessive play, or implies guaranteed social/financial/personal success; helpline number required on all ad formats (TV, radio, internet, print, billboards). RG: written internal-control-system + RG-training-program requirement for every operator; weekly self-exclusion list distribution to operators; 24-hour violation reporting; cross-agency debt-offset against winnings (child support, SNAP overpayments, court debt) for self-excluded persons who evade the ban. | Not separately identified this pass. | See advertising column — RG plan and self-exclusion enforcement are unusually detailed and codified. | 4-5 |
| Michigan | **New 2026-09-09, MCL 432.225(9), MCL 432.209c(2), Mich. Admin. Code R 432.674/R 432.774**: narrower than Arizona/Louisiana — the advertising ban is scoped to disassociated/self-excluded persons specifically (no direct-mail, marketing, or solicitation to listed individuals; casinos may still advertise non-gaming amenities like hotels/restaurants to anyone), not a general audience-targeting rule. Helpline number required on all printed ads/promotional materials. Third-party vendors that receive the self-exclusion list may only use it to suppress targeted marketing, not for other purposes (violation = discipline/civil fine). | Not separately identified this pass. | Self-exclusion-list enforcement is the dominant RG mechanism identified (extends to third-party marketing vendors specifically) — no algorithmic-intervention or deposit-limit mandate found in the excerpt pulled this pass. | 3 |
| Pennsylvania | **New 2026-09-09, 58 Pa. Code §501a.7, §813a.2, §1409a.1, §812a.9, 4 Pa. Const. Stat. §13B02**: ads may not contain false/misleading information or obscure conditions/limits via font/color/placement tricks; state gaming office (OCPG) can order an ad discontinued if it "could adversely impact the public or the integrity of gaming" — a real content-based enforcement lever, though not a specific audience-targeting rule like AZ/LA. Applies uniformly across retail, interactive, and sports-betting licensees. | Not separately identified this pass. | One of the more detailed self-limitation mandates found: players must have a clear mechanism to set deposit/wager/loss/session-duration limits, with an asymmetric-friction design written directly into regulation — a *decrease* to a self-limit takes effect at next login, but an *increase* only takes effect after the prior limit's time period has fully expired and the player reaffirms it. | 4 |
| Tennessee | **New 2026-09-09, Tenn. Code Ann. §4-51-318, Rule 1350-01-.07**: statutory ban on directly advertising/promoting to minors; unusually procedural oversight layer — licensees must submit electronic copies of all advertising/marketing/promotional material to the state Sports Wagering Council within 5 business days of publication. All ads must carry a Council-approved helpline (the "Tennessee REDLINE") with detailed vetting criteria (hours of operation, text-capability, whether it collects usage data for RG research) if a licensee wants to use an alternate hotline. | Not separately identified this pass. | Helpline/messaging requirements above are the RG mechanism found this pass; no separate deposit-limit or algorithmic-intervention rule identified in the excerpt pulled. | 4 |

## Reading this table honestly

- "Not identified this pass" is still a search-coverage gap, not a finding of "no policy in that
  state" — 7 states (AZ, MI, PA, TN newly added, plus MA/OH/CO/ME/NJ/NC/IL from the first pass)
  still have no promo-deduction column populated; that dimension needs its own targeted pass
  through each state's tax code specifically, since the AGA Responsible Gaming Guide is
  RG/advertising-focused and doesn't consistently cover tax treatment.
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

## Next steps (not done this pass)

1. **Promo-deduction coverage is now the thinnest dimension** — AZ, MI, PA, TN (this pass's new
   states) and most of the original 10 still need direct tax-code verification; the AGA guide
   used this pass is not reliably comprehensive on this dimension specifically. A different
   primary source (each state's actual sports-wagering tax statute, or the Tax Foundation's
   sin-tax-rate comparisons for corroboration only) is the right next tool.
2. Expand beyond the current 17 states toward fuller ~37-40-state coverage — the AGA Responsible
   Gaming Guide covers most/all legal states, so remaining coverage is a matter of more passes
   through the same document, not a new-source problem.
3. Decide whether tax rate belongs in the stringency construct or as a separate variable (see
   New York and RI/WV notes above) — this is now better-evidenced as a real measurement-design
   choice, not a data-gathering gap. Recommend Britton weigh in once the panel is closer to full.
4. Virginia's correction above should be reflected in `DECISION_LOG.md` and in any manuscript
   text that cites the earlier "mid-2025 removal" framing if that language was used anywhere else.
