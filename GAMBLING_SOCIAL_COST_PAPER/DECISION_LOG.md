# Decision Log

## 2026-09-24 — Connecticut promo-deduction fully resolved via direct primary-statute read; Arizona/Kalshi docket corrected (see `notes/2026-09-24-arizona-docket-connecticut-primary-source-scouting.md` for full detail)
Two items closed this pass, full sourcing/detail in the dated note, not repeated here: (1) Connecticut's
promotional-deduction tax treatment (13.75% GGR rate; 25%/20%/15% Year 1/2/3 promo-coupon cap) is now
confirmed directly against Sec. 18 of the enrolled Public Act 21-23 text itself (cga.ct.gov, previously
503'd three passes running, returned cleanly this pass) — upgraded from two-secondary-source to
primary-text confirmation, matching what both secondary sources already said. (2) The Arizona/Kalshi
docket (*KalshiEX LLC v. Johnson*, CV-26-1715-PHX-MTL, D. Ariz.) was read directly via CourtListener —
the May 5, 2026 order was a **preliminary** injunction won by the **CFTC's** motion, not a permanent
injunction won by Kalshi (whose own TRO/PI motions were actually denied in April); the case has been
stayed since May 18, 2026 pending Ninth Circuit mandates and shows no docket activity reacting to the
Ninth Circuit's Aug 28 Assad ruling. See `policy/state_policy_variables.md` Connecticut row and the
2026-09-24 note for full sourcing, quotes, and docket-entry citations.


## 2026-09-15 — Promo-deduction tax-treatment gap closed via direct statute pass; found a real 4-category structure, not a binary
Per the 09-09 next-step flag, checked all 9 previously-unpopulated states (MA, ME, NJ, NC, IL, AZ,
MI, PA, TN) directly against their actual sports-wagering tax statutes (state legislature/code
sites, with verbatim-statute mirrors used only where a .gov server itself 403'd/503'd a direct
fetch this session) rather than the AGA Responsible Gaming Guide, which this project had already
correctly flagged as not reliably comprehensive on tax treatment. **Finding: promotional-deduction
treatment is not a binary allowed/disallowed variable — it's at least four distinct categories**:
no deduction identified in the statutory definition (MA, ME, IL — inferred from the absence of any
promo/free-play language in the "adjusted gross receipts" definition, flagged as an omission-based
inference, not a certainty), an explicit capped/thresholded deduction (NJ's $8-12M/year threshold,
AZ's legislated 5-year phase-out to zero), an explicit apparently-uncapped deduction (MI, PA — PA
confirmed in active use at ~20% of gross win via a real monthly revenue report), and full
disallowance of everything including winnings (TN, since a 2023 switch to a flat handle tax).
**Judgment call: did not re-verify the 8 states whose promo-deduction entries already had
statute-level or near-statute-level sourcing from the 09-09 pass** (OH, CO, NY, VA, LA, RI, WV) —
time-boxed to closing the genuine gap rather than re-doing already-adequate work. Full detail:
`policy/state_policy_variables.md`.

## 2026-09-15 — North Carolina's July 2026 promo-tax tightening (SL 2026-31) is a real, dated mid-sample policy change
While checking NC's promo-deduction statute directly, found Session Law 2026-31 (SB 595), signed
by Gov. Stein, **effective July 1, 2026**, which narrows what counts as taxable sports-wagering
revenue by including re-wagered promotional credits that had previously been excluded. This is a
genuine, primary-source-confirmed (enrolled-bill PDF at ncleg.gov) policy change during the
project's own study period, not a coding artifact — flagging here so whoever eventually builds the
analysis panel treats NC's stringency as time-varying around this date rather than constant.
Confirmed via the actual session-law PDF, not a secondary summary.

## 2026-09-15 — McCarthy/Taylor working paper's third co-author confirmed via direct SSRN search: Kenneth C. Wilbur (UCSD Rady)
Per `notes/claims_to_verify.md` item 6, which specifically asked for a direct SSRN search (not
just Consensus.app) before citing the full author list. Confirmed: **Kenneth C. Wilbur, UC San
Diego Rady School of Management** — cross-checked across the SSRN abstract listing, SMU Scholar's
institutional repository, the Marketing Science Institute's own working-paper page, and a UC San
Diego news release, all agreeing. Safe to cite the three-author list (McCarthy, Taylor, Wilbur)
going forward. One wrinkle worth carrying forward, not a fabrication risk: the paper has apparently
been retitled across revisions/venues (at least three different titles found for the same SSRN
abstract ID, 4856684) — check SSRN directly for whichever title is current at citation time rather
than assuming the title recorded in this project's 09-04 literature-map entry is still accurate.

## 2026-09-15 — Category F literature expansion: 3 new entries, 1 existing entry corrected (Di Censo sample is UK/Australia, not US)
Added Han & Saunak (2025, JGS — a real US-based experimental study on sportsbook-ad celebrity
endorsers, the closest thing found yet to the marketing-journal-specific treatment this project has
been looking for, albeit published in JGS not a marketing journal), Meiselbach et al. (2026, Health
Affairs Scholar — current podcast-ad-spend data), and Holbert & Holbert (2025, Communication &
Sport — national US Pew survey data on media exposure and gambling attitudes/behavior). Also
corrected an existing entry: Di Censo, Delfabbro & King (2024, JGS) previously had its venue
unconfirmed; now fully verified via direct PMC full-text read, which also surfaced that **its
sample is UK and Australia (88.4% UK-born), not US** — the prior map entry didn't specify this and
it matters given the project's US focus. **Judgment call, stated plainly rather than spun**: the
core gap (a peer-reviewed, marketing-specific-journal treatment of US sportsbook advertising) is
still not found, despite venue-targeted searches this pass (JPP&M, JCR, Journal of Advertising,
Journal of Macromarketing, Journal of Consumer Affairs). Both this pass and the 09-04 pass used
general web search / Consensus.app rather than a systematic database search of those journals'
actual back issues — flagging that "not found by these methods" is a different, weaker claim than
"confirmed not to exist," and a real database search remains the right next step if Britton wants
to close this gap definitively.

## 2026-09-15 — Real published precedent found for the associational-only identification strategy: Jayawardhana et al. (2014, PLoS ONE) on tobacco MSA dependence
A dedicated search for analogous "vice/settlement-revenue dependence → regulatory stringency"
designs (severance-tax/resource-curse and tobacco-settlement literatures checked) found
Jayawardhana, Bradford, Jones, Nietert & Silvestri (2014, PLoS ONE): 50-state panel data showing a
state's per-capita tobacco Master Settlement Agreement disbursement is negatively associated with
its Strength of Tobacco Control Index — the same directional mechanism this project hypothesizes
for gambling, in a structurally analogous setting. Method: plain fixed-effects panel regression, no
instrumental variable, with the authors explicitly naming (and not resolving) the same kind of
endogeneity concern this project faces. **No shift-share or other IV precedent was found for this
class of question either** — the 09-09 finding stands that this project's own shift-share
robustness check, if built, would be original work, not borrowed. **Judgment call: this precedent
is being treated as meaningfully de-risking the associational-primary-specification recommendation
already on record (09-09), not as resolving the identification-strategy choice itself** — that
choice remains Britton's. Added to `research_design/identification_strategy.md`, cross-referenced
from `research_design/threats_to_validity.md` reviewer-criticism #5.


## 2026-09-04 — Folder structure chosen from kickoff brief, not TARIFF_PAPER precedent
The brief's Section 15 specifies a nested folder structure (literature/, research_design/, data/, policy/, analysis/, notes/, archive/). Britton's other paper threads (e.g. TARIFF_PAPER) use a flatter, less-nested structure. Since this is a brand-new project with no existing files to preserve, and the brief is explicit and detailed about its preferred structure, the brief's structure was used as-is rather than matching sibling-folder convention. **Ambiguous call — flagging for Britton to confirm or override** if he'd prefer this restructured to match his other papers' flatter layout.

## 2026-09-04 — Literature map capped at ~20 entries instead of the brief's 30-50 target
The brief asks for 30-50 high-relevance papers. This pass produced ~20 well-documented entries plus explicit gap notes in the two categories (health/behavioral, marketing/consumer research) that most needed volume. Padding to 30-50 would have required including weaker or less-verified papers just to hit a count, which conflicts with the brief's own "quality over quantity" instruction and no-fabrication rule. **Judgment call: prioritized verification quality over target count.** Flagging as an open item — Britton or a future session should decide whether to invest more search time to reach the target count, particularly in the marketing/consumer-research category.

## 2026-09-04 — GO/MODIFY/STOP called as MODIFY, not GO or STOP
See `PROJECT_STATUS.md` for full reasoning. Briefly: STOP was rejected because the specific recommended pivot (fiscal-dependence → policy-laxity mechanism) is genuinely untested; GO (as originally scoped) was rejected because the literal net-monetization framing is both partially occupied by an existing working paper and not currently executable with defensible data. **This is the single highest-stakes judgment call in this audit — Britton's confirmation or override is the primary next action.**

## 2026-09-04 — Several health-outcome claims (suicide/hotline findings) included despite being UNVERIFIED
Per the brief's own instruction to "note null findings and papers that contradict the proposed narrative," two conflicting suicide-related claims were kept in the literature map even though neither could be traced to a primary source this session (secondary press aggregation only). **Judgment call: included with explicit UNVERIFIED flags rather than omitted**, on the reasoning that flagging an uncertain-but-potentially-important finding is more useful to Britton than silently dropping it. Do not let these propagate into a manuscript without verification.

## 2026-09-04 — Consensus.app pass resolved most open literature items without needing Britton's library
A background Consensus.app session resolved 4 of 5 blocked items in `notes/claims_to_verify.md` using Consensus's own licensed full-text access — no institutional library login was needed for any of them. Notably: the two conflicting UNVERIFIED suicide claims turned into a real, better contradiction (Ozer/Greenwood/Gopal, *Information Systems Research* 2026, peer-reviewed, finds a real suicide/helpline effect vs. Kavanagh et al., a medRxiv preprint with 4.6M+ respondents finding no discernible suicide effect) — the old "age 15-34 up/35-54 down" claim was never real and is dropped. Category F (marketing/consumer research, previously the thinnest) gained 5 real citations (McGrane 2025 *Addiction* systematic review, Browne 2019 *Journal of Behavioral Addictions*, Hing's inducement-taxonomy work, Ceallaigh's experimental decision-error study, Di Censo's marketing-exposure work) — conclusion revised to: substantial adjacent addiction/behavioral literature exists, but a marketing-journal-specific US treatment remains the real gap. **The one item that does need Britton directly is not a library-access issue**: the Coombs/Madonia/Nencka/Smith working paper PDF is freely hosted at peternencka.com/assets/gambling.pdf but failed automated text extraction twice — he just needs to open and skim it himself. Full detail in updated `literature/literature_map.md` and `notes/claims_to_verify.md`.

## 2026-09-04 — Manuscript ground rule: never cite or mention the Tucker Carlson podcast origin anywhere in the paper
Britton: "we don't need to mention anywhere in the paper where my ideas come from, certainly don't mention Tucker because a lot of the liberal high ed reviewers probably despise him." **Hard rule for every future draft, section, or figure of this paper: no reference to Tucker Carlson, Saagar Enjeti, the podcast episode, or the phrase "origin" tying the idea to it.** `notes/2026-09-03-tucker-carlson-podcast-origin.md` stays as internal project documentation only (useful for cross-checking which claims are real vs. media distortion) — it is a working note, not manuscript material, and must never be cited, footnoted, or paraphrased in any manuscript-facing text (intro motivation, acknowledgments, etc.). Manuscript framing should motivate the research question purely from the academic/policy literature and public facts (PASPA repeal, state revenue figures, existing scholarship) — never from where Britton personally got the idea.

## 2026-09-04 — Data sweep confirms Design C (not D) carries Study 1; D folded in as exploratory only
Britton wanted both C and D but asked for a quick public-data feasibility sweep to see which should anchor Study 1, per his standard pattern (Study 1 = secondary/free data, informs Study 2's primary-data model). Result: Census QTAX/State Tax Collections breaks out sports-betting tax revenue separately by state-quarter since Q3 2021, giving a real free fiscal-dependence measure; consumer-protection policy-laxity variables are hand-codeable from AGA's Responsible Gaming Regulations Guide + Legal Sports Report's state tracker (~38-40 states, 5-8 dimensions, days not months). Design D's core predictor — state-level sportsbook promotional/advertising intensity — has **no free public data source at all**, only unusable national aggregates; its outcome side (BRFSS gambling module) is real but inconsistently adopted state-to-state. **Decision: Study 1 = full Design C panel (fiscal dependence → policy laxity, 2021-present), with Design D folded in only as exploratory subgroup outcomes (BRFSS gambling-module states) rather than a standalone causal claim.** This also resolves what Study 2 (primary data) needs to capture: since promotional/ad exposure can't be measured secondarily, the Study 2 survey instrument should ask bettors directly about perceived promotional/ad exposure, with Study 1's hand-coded state policy-stringency scores used as a moderator on those individual-level outcomes. Full detail: `research_design/study1_data_feasibility_sweep.md`.

## 2026-09-09 (evening) — RI/WV policy-coding gap closed; genuine face-validity match found
Per Britton's instruction to "get it going" ahead of a coauthor conversation, closed the top blocking
gap flagged in `PROJECT_STATUS.md` and `policy/state_policy_variables.md`: Rhode Island and West
Virginia are now scored, using two independent AGA primary sources each (per-state fact sheets +
the full ~450-page "Responsible Gaming Regulations and Statutes Guide," pulled via direct PDF
download since WebFetch's own PDF text extraction failed on both — `pdftotext` worked cleanly,
same workaround the project used previously for the Coombs/Madonia/Nencka/Smith paper). **Result:
RI and WV score 2 and 3 — the two lowest advertising-stringency scores of the 17 states now coded**
(tied with Illinois). This is a real, if preliminary, face-validity match for the paper's core
mechanism, not a guaranteed one — worth being honest that n=17 states and no formal regression has
run yet; this is a directional pattern check, not a finding. Also found a genuine nuance worth
carrying forward: RI and WV diverge sharply on promotional-credit tax treatment (RI fully exempts,
WV disallows the deduction) even though both are weak on advertising content rules — suggesting
dependence may predict weak advertising regulation specifically rather than uniform laxity across
every policy dimension. Full detail and sourcing: `policy/state_policy_variables.md`.

## 2026-09-09 (evening) — Virginia's promo-deduction "mid-2025 removal" note was imprecise, corrected
The existing table described VA's promotional-deduction removal as a single mid-2025 budget action.
Checked directly against the live statute (Va. Code §58.1-4030) and multiple secondary sources
(sportshandle.com, EGR, vixio.com): the actual mechanism is a **12-months-post-launch sunset per
operator**, an older provision, not a 2025 policy change — VA's major operators all launched
January 2021, so their windows expired years before 2025. The *practical* effect by 2025 (near-$0
deductions, confirmed in VA Lottery's own monthly reports) matches what the old note implied, but
the timing/mechanism was wrong. Corrected in `policy/state_policy_variables.md`; flagging here since
this is exactly the kind of precise-claim-from-search error this pipeline has been catching in
other projects (case numbers, dates) — caught before it could propagate into a manuscript.

## 2026-09-09 (evening) — Expanded policy coding to 17 states without a full AGA-guide sweep of all ~38-40
Time-boxed this pass to Rhode Island, West Virginia (priority), Virginia (correction), Louisiana
(previously flagged unscored), plus four more well-documented states (Arizona, Michigan,
Pennsylvania, Tennessee) pulled from the same national AGA Responsible Gaming Guide already in
hand. **Judgment call: stopped at 17 rather than continuing to all ~38-40** — the highest-value,
face-validity-critical states (RI/WV) are done, and going further has declining marginal value
until the promotional-deduction dimension (now the thinnest column across nearly every state) gets
its own dedicated pass through actual tax statutes rather than the RG-focused AGA guide used this
session. Flagged as the clear next step in `policy/state_policy_variables.md`, not done here.

## 2026-09-09 (evening) — One new literature entry added and independently verified; one flagged but not verified
Added Obiol-Anaya et al. 2026 (*Frontiers in Sports and Active Living*, DOI confirmed via direct PMC
fetch) to Category F — a 29-study systematic review of sponsorship/advertising bans that
corroborates this project's own novelty claim (no US state-level policy comparison exists in that
literature either) and gives international causal evidence that comprehensive/mandatory ad
restrictions work while voluntary/partial ones don't, useful for framing RI/WV's weak regimes.
A second candidate (*Journal of Gambling Studies* 2026, "Sports Betting Ads are Everywhere") could
not be read past a Springer login wall — logged as an existence-only flag, not cited with any
claimed finding, matching this project's no-fabrication rule. Literature map now at ~29 verified
entries (was ~28 as of the 2026-09-04 Consensus.app pass), still short of the 30-50 target —
did not chase further this pass given the time-boxing above; Category F specifically would
benefit from a dedicated JPP&M/JCR/Journal of Macromarketing back-issue search as the next step.

## 2026-09-04 — Britton confirmed the MODIFY pivot: Design C (fiscal dependence → policy laxity) as Study 1
Britton reviewed the GO/MODIFY/STOP call and candidate designs and confirmed: "I like that pivot to looking at state's dependence on gambling funds and their modification of laws as the study 1 here." This locks in **Design C** (state revenue dependence → consumer-protection policy laxity) as the lead empirical study, framed as "Study 1" of the paper — consistent with how Britton structures his other multi-study threads (Tariff, Data Center). He named the core mechanism (dependence → law modification) specifically, not the paired Design D vulnerable-consumer-outcome layer — treat D as a candidate Study 2 / extension rather than assuming it's bundled into Study 1 unless he says otherwise. **Open item:** the identification strategy for "dependence causes weaker protection" (vs. mere correlation) is still unresolved — see `research_design/candidate_designs.md` Design C causal-credibility note (scored 3/5, flagged as needing a revenue-shock instrument or fiscal-threshold-crossing design). This is now the top blocking task before any data collection starts.
