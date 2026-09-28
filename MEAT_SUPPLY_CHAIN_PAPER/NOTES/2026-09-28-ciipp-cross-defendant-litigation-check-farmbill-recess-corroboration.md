# 2026-09-28 — Cross-defendant CIIPP litigation check (the 09-26 follow-up), farm-bill recess corroboration, DOJ/Schaefer/literature rechecks

Thirteenth research session. Orientation: read root `README.md`, `MEAT_SUPPLY_CHAIN_PAPER/CLAUDE.md`,
`PROJECT_STATUS.md` in full (through the 2026-09-26 pass), `RESEARCH_QUESTIONS.md`, `THEORY_CANDIDATES.md`,
`SOURCE_VERIFICATION/Evidence_Table*.md`, and `NOTES/Claim_Fact_Check.md` before starting. Today is
2026-09-28 — the farm bill's Sept. 30 extension deadline is 2 days away. No design decisions made. No
external contact, no money spent, nothing submitted anywhere. Method: `WebSearch` + `WebFetch`; `curl` with
a browser User-Agent for a court PDF WebFetch couldn't parse cleanly; `pdftotext -layout` (via
`poppler-utils`, missing again from this session's fresh container — reinstalled, same recurring gap noted
in several prior sessions) for that PDF.

## 1. Cross-defendant CIIPP settlement check (the 2026-09-26 note's own recommended follow-up)

The 2026-09-26 pass found that Tyson's own SEC 10-Q revealed two previously-untracked Commercial and
Institutional Indirect Purchaser Plaintiff (CIIPP) settlement classes (beef $47M, pork $48M) and recommended
"a future session check whether other defendants (JBS, Cargill, National Beef, Smithfield) have parallel
untracked CIIPP-class settlements, using the same read-the-primary-filing method." That is tonight's main
piece of work.

**Beef CIIPP/Consumer-IPP landscape — real findings, one genuine primary-source read, one real ambiguity
flagged rather than resolved by guessing:**

- **JBS's own 2023 beef CIIPP settlement, already known to exist but not previously dollar-verified in this
  project, is $25 million** (JBS S.A. and three U.S. subsidiaries, per the settlement-administrator notice
  and corroborating trade coverage) — a settlement track separate from and earlier than Tyson's 2025-2026
  CIIPP settlement, not a duplicate.
- **Tyson's $47M beef CIIPP settlement (already tracked from its own 10-Q, 2026-09-26) is confirmed, via the
  actual PR Newswire class-notice text (a court-ordered settlement notice, read directly), to name Tyson
  alone** — "Tyson Foods, Inc., Tyson Fresh Meats, Inc., and related/affiliated entities" — with the notice
  itself stating "a separate JBS settlement was previously reached and noticed in 2023" (the $25M settlement
  above). **This matters because two independent WebSearch syntheses tonight both initially conflated this
  $47M CIIPP figure with Cargill, describing it as "Cargill and Tyson['s] combined $47 million CIIPP
  settlement."** Reading the actual settlement notice directly shows that framing is wrong: $47M is Tyson's
  alone. Do not use a Cargill-specific CIIPP dollar figure in this project until a primary source actually
  states one.
- **Cargill's $32.5 million share of the beef Consumer Indirect Purchaser Plaintiff (Consumer IPP) class
  settlement is a genuinely new, useful granular fact** — the project previously only had the $87.5M
  aggregate (Cargill + Tyson) for this class. Two independent sources (a law-firm client-alert site and an
  independent WebSearch synthesis of settlement-administrator/press coverage) both give the same split:
  Cargill $32.5M + Tyson $55M = $87.5M, consistent with the already-tracked May 27, 2026 final-approval
  date and case citation (*In re Cattle and Beef Antitrust Litigation*, No. 0:22-MD-3031-JRT-JFD, D. Minn.).
  Not independently read from a primary court order tonight, but internally consistent arithmetic across
  two independent secondary sources is a reasonable (not primary-grade) basis for using this split.
- **Cargill's own CIIPP-class status remains genuinely unconfirmed** — no source found tonight states
  Cargill separately settled CIIPP (business/institutional-purchaser) claims at all, distinct from its
  Consumer IPP settlement. Flag as open, not "presumably similar to Tyson."
- **National Beef and JBS's own beef Direct Purchaser Plaintiff claims remain unsettled** — multiple
  sources confirm the $87.5M Consumer IPP settlement "resolves claims against Cargill and Tyson only," with
  JBS and National Beef named as continuing, non-settling defendants in the underlying MDL (*In re Cattle
  and Beef Antitrust Litigation*, 22-md-3031). No settlement found for either on any class tonight.

**Pork CIIPP landscape — a genuine, primary-source-confirmed correction to a real cross-source conflation:**

Two independent WebSearch syntheses tonight gave two different, mutually inconsistent sets of pork CIIPP
settlement figures for the same five non-Tyson defendants:
- Set A: Hormel $2.4M, Seaboard $9.75M, JBS $24.5M, Smithfield $83M, Triumph $700K
- Set B: Hormel $2.429M, Seaboard $4.96M, JBS $12.75M, Smithfield $42M, Clemens $7.75M, Triumph $700K

These disagree materially on JBS (by roughly 2x), Seaboard (by roughly 2x), and Smithfield (by roughly 2x)
— exactly the kind of AI-search-synthesis unreliability this project's standing practice (read the primary
document, don't trust a search engine's summary) exists to catch. Rather than pick one set, tonight tracked
down and read the actual primary court filing for the one figure that could be checked directly:

- **JBS's pork CIIPP settlement is $12,750,000.00 ($12.75 million) — confirmed by direct primary-source
  read of the actual court filing**: *In re Pork Antitrust Litigation*, D. Minn., "Motion for Preliminary
  Approval of Settlement Between CIIPP and JBS" (filed 4/15/21), fetched directly via `curl` and read in
  full via `pdftotext` after installing `poppler-utils` (missing again from this fresh session container).
  The document states in its own text: "JBS will pay $12,750,000.00 (twelve million seven hundred and
  fifty thousand dollars)... Settlement Amount." **This resolves the JBS figure in favor of Set B's $12.75M,
  not Set A's $24.5M** — Set A's figure should not be used.
- **Smithfield's pork CIIPP settlement is very likely the $42 million figure** already independently visible
  in this project's own prior work: Smithfield's own SEC disclosure (found this session, not previously read
  in this project) states it "made payments of $75 million, $42 million and $77 million in fiscal years
  2023, 2022 and 2021" to settle pork antitrust class claims, breaking out "a $42 million settlement with
  restaurants and caterers" (i.e., commercial/institutional purchasers — the CIIPP class) separately from "a
  $75 million settlement with a class of consumers" (i.e., the Consumer IPP class). This favors Set B's $42M
  over Set A's $83M (which is likely a conflation with a different fiscal-year total or class). **Not
  independently read from the primary 10-Q footnote text tonight** (only a WebSearch synthesis of it) — a
  direct pull of that footnote would fully close this out.
- **Hormel, Seaboard, Clemens, and Triumph's pork CIIPP figures remain genuinely unconfirmed.** Both figure
  sets agree closely on Hormel (~$2.4M) and Triumph ($700K), giving those two some cross-source
  corroboration, but Seaboard's figure is contested ($9.75M vs. $4.96M) and Clemens appears in only one set
  ($7.75M) with no corroboration at all. **Do not adopt any of these four figures in the manuscript or
  Evidence Table without a direct primary-source read** (the settlement-administrator site,
  porkcommercialcase.com, 403-blocked both `curl` and WebFetch tonight; a targeted pull of Hormel's,
  Seaboard's, or Clemens's own SEC filings, or the actual court settlement/preliminary-approval order for
  each, would resolve this — recommended for a future session).

**Net effect**: the 2026-09-26 recommendation to cross-check other defendants' own filings was real,
productive work — it surfaced one already-known-but-undollar-verified JBS beef settlement, one genuinely new
useful fact (Cargill's specific $32.5M Consumer IPP share), one important correction-by-primary-source (JBS
pork CIIPP = $12.75M, not the higher $24.5M a search synthesis offered), and one real, stated-plainly
unresolved discrepancy (Smithfield/Seaboard/Clemens/Hormel pork CIIPP figures) rather than a false sense that
this thread is now fully closed out. Claim #15 in `NOTES/Claim_Fact_Check.md` updated accordingly.

## 2. Farm-bill floor-vote timing and the Senate recess discrepancy — corroborated, not resolved

The 2026-09-26 note left a specific, named discrepancy open: whether the Senate's pre-midterm recess begins
before or after the Sept. 30, 2026 farm-bill extension deadline, with one low-credibility source
(`themoneyoverview.com`, citing an unverifiable "AgWeb Senate aide" quote) claiming recess begins *before*
Sept. 30, against other reporting suggesting the Senate remains in session "through October 2."

Tonight's fresh search materially firms up (without fully primary-confirming) the "through early October"
side: **three independent secondary sources — Bloomberg Government (news.bgov.com), Roll Call, and The Well
News — all independently describe the Senate's 2026 pre-midterm recess as covering full weeks beginning
Oct. 4, 11, 18, 25, and Nov. 1**, i.e., a recess that starts the week after Sept. 30, not before it. This is
inconsistent with the "recess begins before Sept. 30" framing and consistent with the "in session through
early October" framing already favored (cautiously) in the 2026-09-26 note. **Still not primary-confirmed**
— the Senate's own calendar page (`dailypress.senate.gov`) only exposes a calendar-navigation interface, not
the actual schedule text, to automated fetching, and no attempt tonight reached the Senate's own printed
2026 calendar PDF directly. Recommend treating "the Senate remains in session into early October, with the
pre-midterm recess beginning the week of Oct. 4" as the better-supported framing going forward, while still
flagging it as secondary-sourced, three-way-corroborated rather than primary-confirmed.

**No Senate floor vote on the farm bill has been scheduled as of Sept. 27, 2026** (the most recent dated
coverage found tonight) — consistent with, not a change from, the 2026-09-26 finding. One outlet (High
Plains Journal, syndicating AgWeb) states plainly that a floor vote "could happen within a few weeks... or as
late as November or December — the timeline is not clear," which is consistent with this project's existing
"genuinely contested, no date set" framing and does not warrant a verdict change to Claim #11. Also
newly reconfirmed (not previously stated this explicitly in this project's notes): mandatory country-of-
origin labeling for beef is explicitly named as one of the bill's "key farm priorities" alongside year-round
E15 and the Fertilizer Transparency Act in multiple Sept. 16-18 committee-passage summaries — useful,
consistent framing for Study 1 material, not a new fact about legislative status.

## 3. DOJ beef-pricing probe / idea 28 — rechecked, no material change

Fresh search confirms: no indictments, no new DOJ.gov document. The "reviewed more than 3 million documents"
figure (Acting AG Todd Blanche) and the eight named retailers (Kroger, Walmart, Publix, Albertsons, Aldi,
Ahold Delhaize USA, Costco, Amazon) are both reconfirmed via multiple consistent outlets (Yahoo Finance,
Fortune, Fox Business, Forbes, farmpolicynews.illinois.edu), consistent with — not beyond — what the
2026-09-08/09-26 passes already established. Ground-beef retail price cited at $6.89/lb (July 2026, +10%
YoY) reconfirmed, consistent with the AFBF 41-store tracking data already in Claim #7. Nothing new to report.

## 4. Schaefer/poultry-concentration thread — reviewed, no further action needed

Consistent with the 2026-09-24/09-26 passes' own conclusion, no new automated-access channel was found or
attempted tonight (Unpaywall's own index already showed `is_oa: false` for this DOI as of 2026-09-08/09-24;
nothing in tonight's unrelated searches surfaced a new channel). Genuinely nothing further for automated
tooling to do here without Britton's own institutional access, as already recorded.

## 5. Literature-gap scouting — one candidate checked directly, confirmed already-tracked, not new

A search for recent country-of-origin/price-fairness/meat-marketing literature surfaced "Exploring the
Antecedents and Consequences of Perceived Fairness in Beef Pricing: The Moderating Role of Freshness Under
Conditions of Information Overload" (PMC) as a promising-looking hit. **Checked directly (not just a search
snippet): this is Sun & Moon (2025, *Foods*), the same paper already identified and characterized in this
project's 2026-09-15 literature scan** (organic-perception/freshness/price-fairness, no COO or
corporate-price-explanation dimension) — not a new source. Also surfaced but not the project's specific
gap: Berikou et al. (2026, *PLOS One*, Purdue), on sustainability-label price premiums across beef/pork/
chicken via web-scraped retail data — adjacent (labeling → price) but about sustainability certification,
not COO disclosure or corporate price-explanation framing. **This project's specific COO-disclosure ×
corporate-explanation-type × price-fairness gap in a meat context, in a marketing journal, still reads as
open after a fourth scouting pass with different search terms.**

## What did NOT change tonight

- No Study 1/2/3 design decisions made or needed.
- Claim #7, #11 verdicts unchanged (Claim #7's split-verdict structure and Claim #11's "Unsupported as
  commonly believed, nothing enacted" both stand).
- Open Decision #6 (Schaefer): unchanged.
- The overall litigation-settlement landscape's size keeps growing as more primary filings get read
  directly (this session added real detail, per Section 1) — a reminder that "the litigation section is
  fully inventoried" should not be assumed even now.

## Genuinely still open, stated plainly

- Cargill's own CIIPP-class settlement status (beef) — unconfirmed either way.
- Hormel's, Seaboard's, and Clemens's exact pork CIIPP settlement dollar figures — two conflicting
  search-synthesized figure sets exist; neither is primary-confirmed. Smithfield's $42M figure is
  reasonably well-supported (Smithfield's own SEC disclosure language) but not read from the primary
  footnote text directly.
- The Senate's exact pre-midterm recess start date is better-supported (three sources now favor "recess
  begins the week of Oct. 4") but still not confirmed against the Senate's own primary calendar text.
- Farm-bill floor-vote timing: still no date set, 2 days before the Sept. 30 deadline itself lapses.

## For Britton

Three things worth knowing: (1) tonight's cross-defendant litigation check (following up on the 09-26
note's own recommendation) both added real detail (Cargill's specific $32.5M Consumer IPP share) and caught
a real error before it could enter the manuscript — a search-engine synthesis had JBS's pork CIIPP
settlement at $24.5M, but the actual court filing, read directly, says $12.75M; (2) the same check found a
second, not-yet-resolved figure conflict (Hormel/Seaboard/Clemens's exact CIIPP figures) that would need a
future session's primary-document time to close out properly, not a guess between two search-engine outputs;
(3) the farm bill's Sept. 30 deadline lapses in 2 days with no floor vote scheduled — a further extension
remains the likely near-term outcome, consistent with everything tracked since 2026-09-24, and nothing about
this changes any of this project's Claim #11 framing.

No money spent. No one contacted. Nothing submitted anywhere.
