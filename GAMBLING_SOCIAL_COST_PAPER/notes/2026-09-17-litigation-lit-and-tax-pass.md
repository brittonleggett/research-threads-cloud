# 2026-09-17 — Kalshi/prediction-market litigation wave, Category F re-check, 4-state tax-treatment expansion

This project's last dedicated pass was 09-15. This session worked the four assigned items in order:
(1) open_questions.md/claims_to_verify.md triage, (2) another Category F search specifically for a
JPP&M/JCR/Journal of Advertising/Journal of Retailing US sportsbook-advertising study, (3)
promo-deduction tax-treatment coding for a next batch of states beyond the current 17, (4) new
litigation/regulatory movement since 09-15. Item 4 turned up the most substantively new material
this pass.

## 1. open_questions.md / claims_to_verify.md triage

Nothing new to resolve without Britton's judgment call. All five items in `open_questions.md`
(folder structure, literature-investment level, the GO/MODIFY/STOP design pivot, priority
sequencing against the other 6 threads, venue confirmation) are explicitly his calls per the
standing instruction — not touched, not contradicted. In `claims_to_verify.md`, items 1-6 are
already fully or partially resolved from prior passes; items 7-10 (the Tucker Carlson podcast
figures: "$500B wagered since 2018," "$166B in 2025," "$1 bet = $2 less savings," "25-30% increase,"
DeWine's Ohio remark) were not re-attempted this pass — they weren't part of tonight's assigned
scope and each needs either an AGA handle-total lookup or a clean read of Baker et al.'s full text,
which is better done as its own dedicated pass rather than squeezed in here. Flagging so the next
pass doesn't assume they were checked.

## 2. Category F — still no marketing-journal-specific US sportsbook-advertising study found

Ran fresh, dedicated searches this pass targeting "Journal of Public Policy & Marketing,"
"Journal of Advertising," "Journal of Consumer Research," and (new this pass) "Journal of
Retailing," each combined with sportsbook/sports-betting-advertising terms. Result: **the gap is
still real.** Nothing new turned up in that specific venue set. The same evidence base already in
`literature/literature_map.md` Category F kept resurfacing (Han & Saunak 2025 in *Journal of
Gambling Studies*, the McGrane et al. and Obiol-Anaya et al. systematic reviews, the Di Censo et
al. UK/Australia study, etc.) — nothing changed there. Two new, minor items worth a one-line flag,
not entries: a preprint ("The Business of Sports Betting: How U.S. Sportsbooks Profit and the Costs
They Create," Research Archive of Rising Scholars) that has not been read or verified this pass —
existence only, not content — and a *Washington Post* AI-assisted content analysis of gambling-ad
frequency on sports broadcasts (May 2026), which is journalism, not a peer-reviewed study, but could
be a useful motivating citation for ad-volume claims if Britton wants a current media citation
alongside Meiselbach et al.'s podcast-spend numbers.

**State plainly, as instructed**: after three dedicated passes now (09-04, 09-15, 09-17) using
general web search, no peer-reviewed article in JPP&M, JCR, JCP, Journal of Advertising, Journal of
Macromarketing, Journal of Consumer Affairs, or Journal of Retailing studying US sportsbook
advertising directly has been found. This is "not found by general web search," not "confirmed not
to exist" — the standing recommendation from 09-15 stands: a real answer needs a licensed
database search of those journals' back issues (or Consensus.app run against those venues
specifically), which is beyond what this session's tools can do. Recommend not running a fourth
identical general-web-search pass on this specific question without a different tool/access method;
diminishing returns are evident.

## 3. Promo-deduction tax-treatment coding — 4 new states added (Indiana, Iowa, Kansas, Connecticut)

Full detail and quoted/summarized statutory language is in each state's row in
`policy/state_policy_variables.md` (updated this pass) — this section is the short version.

Scope was deliberately narrow: **tax-treatment only**, not the advertising/RG columns (those still
need the AGA Responsible Gaming Guide pass this project uses for the other 17 states) — this matches
the 09-15 pass's own recommendation to keep using statute-level sourcing for tax treatment on any
newly added state rather than reverting to the AGA guide.

- **Indiana** — ✅ statute-confirmed. IC 4-38-2-2's sports-wagering-specific "adjusted gross
  receipts" definition has no promotional/free-play deduction language at all — same "no deduction
  identified" category as Massachusetts/Maine/Illinois. Worth flagging as a real gotcha this pass
  ran into and resolved: an initial general search surfaced a $3M-$5M/year promotional-deduction cap
  for Indiana, which turned out to belong to a *different* statute — IC 4-33-13-7, governing
  traditional riverboat/casino gambling, not sports wagering (IC 4-38) at all. Confirming against
  the actual sports-wagering definitions section (not the riverboat article) caught this before it
  became a wrong entry in the map. A useful general reminder for future state passes: Indiana-style
  states with both an old casino-gambling code and a newer sports-wagering code are a real
  conflation risk.
- **Iowa** — ✅ statute-confirmed, with one honestly-flagged loose end. Iowa Code §99F.1 defines
  "sports wagering net receipts" as gross receipts minus winnings minus promotional play receipts
  — an explicit, apparently uncapped deduction. But the same section separately suspended the
  *general* "adjusted gross receipts" (gambling-games/casino) promotional deduction for exactly
  July 1, 2021-June 30, 2026 — a window that, as of today (2026-09-17), just expired. Whether that
  suspension clause ever applied to sports wagering specifically (as opposed to only casino table
  games/slots under the same chapter) could not be fully confirmed this session — the tax-rate
  section (99F.11) that would settle it returned corrupted/unparseable text on every extraction
  attempt, the same PDF-extraction failure pattern this project has hit before (Coombs/
  Madonia/Nencka/Smith, Michigan's legislature site in the 09-15 pass). Read as "sports wagering
  deduction is uncapped and was likely never part of the suspension," not certain.
- **Kansas** — ✅ statute-confirmed, cleanest of the four. K.S.A. 74-8702 was read directly on
  **ksrevisor.gov**, the Kansas Office of Revisor of Statutes' own official site (a true primary
  source, not a mirror) — "sports wagering revenues" excludes "free plays or other promotional
  credits" from the tax base with no cap language found. Apparently uncapped deduction.
- **Connecticut** — 🔶 partially sourced, flagged honestly as the weakest of the four. The
  sports-wagering tax rate (13.75% of "gross gaming revenue," Conn. Gen. Stat. §12-867) is
  confirmed via a direct Justia search-result citation, but the actual definitions section
  (§12-850, which should define "gross gaming revenue" and any promotional-coupon carve-out for
  sports wagering specifically) could not be read directly this session — Justia 403'd on every
  repeated direct fetch of that section, and cga.ct.gov's own chapter page 503'd. The 25%/20%/15%
  phased promotional-deduction cap that shows up in secondary coverage (public-gaming.com, an
  investigative piece, aggregated Public Act 21-23 text) is confirmed for **online casino gaming**,
  not confirmed this session as the same rule for **sports wagering** specifically — do not copy
  that figure into a sports-wagering stringency score without reading the actual statute text
  (Britton's own Westlaw/Lexis access, if he has it, would resolve this in one query). This is the
  first state in this project where the underlying statute genuinely couldn't be read directly
  this session, as opposed to needing a mirror site — worth knowing it's a real access gap, not a
  research shortcut.

**Running total**: 21 states now have a promo-deduction tax-treatment entry (17 with full
advertising/RG coding too, 4 new ones tax-only). ~16-19 states with legal sports betting still have
no entry at all in this file. Mechanical to keep extending at roughly the pace demonstrated here
(1-3 targeted searches per state, more if a state has split/legacy statutes like Indiana's or a
hard-to-reach state site like Connecticut's).

## 4. New litigation/regulatory movement since 09-15 — the Kalshi/prediction-market lawsuit wave

This is the most substantively new finding this pass, and it's a genuinely different angle than
anything previously in this project's design: **a fast-moving, multi-state legal fight over whether
"prediction market" platforms (Kalshi, and by extension Polymarket) offering sports-outcome
contracts are unlicensed sports betting in disguise.** Verified directly against primary sources
(state AG press releases), not secondary summaries, for the core facts below:

- **Washington** — AG Nick Brown sued Kalshi March 27, 2026, alleging violations of the Washington
  State Gambling Act and Consumer Protection Act. The complaint itself cites Kalshi's own
  advertising as evidence: an ad in which someone says they "found a way to bet on the NFL even
  though we live in Washington," which the AG frames as Kalshi acknowledging it's circumventing
  state law. The complaint also alleges Kalshi marketed to college students aged 18-21 and
  attempted to recruit a 15-year-old influencer. (Source: atg.wa.gov press release, read directly.)
- **Massachusetts** — sued Kalshi in September 2025 (before this project's window, but the
  necessary predicate for the item below) over unlicensed sports betting; the AG's complaint notes
  roughly 90% of Kalshi's ~$1B/month in user activity is sports-outcome-focused. Kalshi's defense:
  its contracts are federally regulated "swaps," not state-regulable gambling.
  (Source: ag.ny.gov press release describing the MA case, read directly.)
- **Connecticut** — sued Kalshi August 26, 2026 (following a December 2025 state cease-and-desist
  order), alleging the same "event contracts are gambling in disguise" theory. The CT AG's release
  specifically frames prediction-market advertising as "a coordinated campaign to convince people
  they are offering investments that are somehow safe" and alleges targeting of minors and
  self-excluded individuals. (Source: portal.ct.gov/ag press release, read directly.)
- **A 38-state-plus-DC amicus coalition** (New York AG Letitia James's office named as a
  representative signer) filed an amicus brief April 24, 2026 in the Massachusetts Supreme Judicial
  Court supporting the state's case against Kalshi — a genuinely broad bipartisan alignment across
  Louisiana, most other states already in this project's design, and dozens more. (Source:
  ag.ny.gov press release, read directly, which lists the full coalition.)
- **Arizona** also sued Kalshi (AG Kristin Mayes) per secondary reporting — not independently
  confirmed against a primary AZ AG source this session; flag as 🔶 pending direct verification.
- **Congressional pressure on the FTC**: Reps. Kevin Mullin and Gabe Vasquez led an 9-member House
  Democrat letter to FTC Chairman Andrew Ferguson (sent early June 2026, response requested by
  June 29) asking whether the FTC will investigate prediction-market platforms for allegedly
  presenting themselves to consumers as sports-gambling apps while presenting themselves to
  regulators as financial instruments. The letter itself could not be read directly this session —
  its PDF returned unparseable/corrupted text on extraction, the same recurring PDF-extraction
  failure pattern noted above — so this item rests on secondary reporting (Congressman Mullin's own
  site plus several trade-press outlets, which agree on signers, date, and substance) rather than
  the primary letter text itself. Flag as 🔶, not ✅.

**Why this matters for the paper's actual mechanism, not just as color**: the whole design premise
here is fiscal dependence on sportsbook tax revenue predicting weak consumer-protection regulation.
Prediction markets operating as unlicensed, untaxed sports-betting-adjacent products are a direct
threat to that same tax base — if they succeed in carving out a federally-regulated lane, it could
either (a) accelerate states' fiscal dependence on their remaining licensed sportsbooks (intensifying
the mechanism this project studies), or (b) genuinely erode state gambling-tax revenue over time
(complicating any panel that treats state tax revenue as a stable, only-increasing series post-
legalization). This is squarely a "flag for whoever builds the analysis panel" item, parallel to how
North Carolina's SB 595 was flagged in the 09-15 pass — not something to resolve now, but something
that could matter for panel construction and definitely worth a paragraph in any related-work/
motivation section about the current regulatory landscape being less settled than a simple post-2018
legalization story implies.

## 5. NCAA-related development — college prop-bet bans, a live and growing state-by-state trend

Smaller finding, but real and dated: the NCAA (per its own site, ncaa.org, read via search-result
content) has continued actively lobbying state gaming commissions to eliminate individual
college-athlete prop bets, citing both integrity risk (NCAA enforcement staff has ~40 open
investigations into potential game manipulation by student-athletes across 20 schools, largely
prop-bet and first-half-under-spread related) and athlete-harassment concerns. **Louisiana —
already a named state in this project's design — is one of four states (with Maryland, Ohio, and
Vermont) that have banned individual college-athlete prop bets since 2024**, and two more state
legislatures were considering codifying bans as of this pass. This is a separate stringency
dimension from the advertising/RG/tax-treatment columns already coded for Louisiana in
`policy/state_policy_variables.md` — not added to that file this pass (would need its own coding
pass across all 17+ coded states, not just LA, to be usable comparatively), but worth flagging as a
concrete, likely-tractable next stringency dimension to add given several coded states already have
public, dated policy actions on it.

## For Britton

Three things worth your attention, in order of how much this pass thinks they matter:

1. **The Kalshi/prediction-market litigation wave (Section 4) is genuinely new context for the
   paper's core mechanism**, not busywork — it's a live, multi-state fight over whether a whole
   category of unlicensed, untaxed products competing with licensed sportsbooks should exist at
   all, and it directly touches the state-tax-revenue-dependence variable this project's whole
   design is built around. Worth a paragraph in whatever section discusses the current regulatory
   landscape, and worth knowing about before this project's identification strategy is finalized,
   since it could affect how "stable" a state's post-legalization tax revenue series should be
   assumed to be going forward.
2. **The Category F literature gap is now checked three separate times (09-04, 09-15, 09-17) via
   general web search and hasn't moved** — I'd treat this as a real, stable finding rather than
   something one more general-search pass will fix. If closing it matters for the manuscript,
   it needs your Consensus.app subscription run against those specific journals, or actual
   database/library access — not more of the same search method.
3. **The tax-treatment coding for the 4 new states (Section 3) is solid for 3 of them** (Indiana,
   Iowa, Kansas) and genuinely weaker for the 4th (Connecticut) — Connecticut is the first state in
   this project where the statute itself, not just an easier mirror, was unreachable this session.
   If you have Westlaw/Lexis/a CT-specific subscription, a two-minute check of Conn. Gen. Stat.
   §12-850 would resolve whether the 25/20/15% online-casino promotional-deduction cap also governs
   sports wagering specifically, which this pass could not confirm either way.
