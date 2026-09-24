# 2026-09-24 — Litigation recheck, USITC import-price-effect primary source (Claim #7 advanced), Schaefer thread reviewed, brief literature scouting

Eleventh research session. Orientation: read `CLAUDE.md`, `PROJECT_STATUS.md` (open decisions + all
dated passes through 2026-09-22), the 2026-09-22 note, and `SOURCE_VERIFICATION/Evidence_Table*.md`
before starting. Scope tonight, per the brief: (1) litigation recheck on the four tracked threads, (2)
push the Schaefer/poultry-concentration thread forward if possible, (3) real primary-source verification
work on 1-2 open claims from `NOTES/Claim_Fact_Check.md`, (4) light literature-gap scouting. Method:
`WebSearch` + `WebFetch` for most of tonight; `curl` + locally-reinstalled `poppler-utils`
(`apt-get install -y poppler-utils` — the package was missing again this session's container, same as
earlier sessions; installing it took two tries because the first `apt-get install` hit a stale
`security.ubuntu.com` 404 until `apt-get update` was run first) for one primary PDF that WebFetch
couldn't reach. No design decisions made. No external contact, no money spent, nothing submitted
anywhere.

**Mid-session note on process**: partway through this pass, edits already made to `Claim_Fact_Check.md`
and `Evidence_Table_Imports.md` (and this note file itself, on a first write attempt) were found reverted
to their pre-session state — `git reflog` showed another concurrent session had run a `merge
origin/main: Fast-forward` on this shared repo checkout in between my edits, which reset the working
tree. All three edits were redone afterward and verified present; `PROJECT_STATUS.md`'s edit (made after
the reset) survived untouched. Flagging this for whoever compiles the repo-wide summary: parallel
overnight sessions sharing one working tree can silently clobber each other's uncommitted edits — worth
knowing if anything looks missing.

## 1. Litigation recheck

**Tyson $82.5M DPP settlement**: reconfirmed unchanged. Fairness Hearing remains scheduled for
**November 12, 2026, Courtroom 15, District of Minnesota**; claims deadline Nov. 30, 2026. New detail
not previously in this project's notes: Plaintiffs and Co-Lead Counsel will file their motion(s) for
attorneys' fees, litigation costs, and class-representative service awards **by October 1, 2026** — a
concrete date worth knowing but not a settlement-outcome change. (Feedstuffs.)

**Pork DPP Agri Stats settlement**: no new developments found; remains as confirmed 2026-09-22 (final
approval granted at the Sept. 8, 2026 hearing, written order entered Sept. 10, 2026, no cash/conduct
reforms only). Not re-worked in depth tonight — already closed out.

**Agri Stats DOJ case / broiler and pork tracks generally**: a fresh search surfaced no appeal, no new
filing, and no contradiction of the "four settlement tracks resolved within ~6 weeks of each other,
behavioral/injunctive only" picture already established. Nothing new to report.

**DOJ's eight-retailer beef-price probe**: re-searched fresh; no indictments, no new DOJ.gov document,
no change from the 2026-09-19/09-22 status (idea 28 remains open/ongoing). The underlying Bloomberg
article (bloomberg.com/news/articles/2026-09-02/...) was visible in search-result titles tonight but
still could not be fetched directly (blocked), so the July 14, 2026 letter date remains at
"corroborated via Transport Topics," not upgraded to primary.

**Senate farm-bill / MCOOL-restoration effort — real update to the timeline framing, a genuine
correction worth flagging to Britton:**

- The project's existing framing ("floor vote expected after the November 2026 midterms," first
  recorded 2026-09-17) is **more settled than the actual evidence supports**. Tonight's fresh reporting
  shows active, unresolved disagreement about timing: Sen. Grassley is publicly and explicitly pushing
  Majority Leader Thune for a **pre-midterm** floor vote — "Thune is going to have to force the issue
  on the United States Senate floor" (Brownfield Ag News, Sept. 17, 2026, quoting Grassley directly) —
  while Sen. Klobuchar's own stated goal is only "to get this farm bill done... by the end of the year"
  (DTN, Sept. 17, 2026), and Sen. Hyde-Smith says "the legislative calendar shrinks with every passing
  day, which will make it difficult, but not impossible, to get a new farm bill enacted this year" (same
  DTN article). Independent reporting (Brownfield) states plainly: **"The Senate is scheduled to remain
  in session through early October"** before turning to midterm campaigning — i.e., there is a real,
  narrow pre-midterm floor-vote window that some senators are actively pushing to use, not a settled
  "after midterms" plan. Recommend updating Claim #11 / Open Decision #11's framing from "floor vote
  expected after the November 2026 midterms" to "floor-vote timing genuinely contested — a narrow
  pre-midterm window exists and Republicans are pushing to use it; Democrats are not committing to a
  timeline; no vote has been scheduled as of this check."
- **A methodological catch worth logging on its own**: `WebSearch`'s own synthesized answer for one
  query tonight asserted that a specific DTN article (Jennifer Carrico, Sept. 18, 2026) "states" the
  MCOOL markup vote was 17-6. A direct `WebFetch` of that exact article found **no vote count anywhere
  in its text** — the search tool's summarization had blended content from other results into an
  attribution to the wrong specific article. This project's MCOOL 17-6 assessment is unaffected (it
  already rests on four *directly-read* sources, not this one), but it's a concrete, dated example of
  why this project's standing practice — fetching and reading the specific article, not trusting a
  search engine's synthesized summary — continues to matter. No further automated-retry time spent on
  the vote count itself tonight, per the 2026-09-22 note's recommendation.
- **Separately confirmed, not previously in this project's notes**: the Aug. 3, 2026 bipartisan
  Senate funding deal (Collins/Murray) extended *general government funding* through **December 11,
  2026** — but this is a **different, unrelated deadline** from the farm bill's own Sept. 30, 2026
  extension. Confirmed directly via NBC News' own article (fetched and read): "The article does not
  mention the farm bill, agriculture funding, or any farm bill extension." The two deadlines should not
  be conflated — the farm bill's Sept. 30 cliff is real and separate, and (per CRS/multiple ag-press
  sources) a lapse mainly threatens program-authorization continuity and the eventual "dairy cliff"
  (permanent 1930s-era law reverting Jan. 1, 2027 for dairy, then wheat/corn later), not an immediate
  government shutdown.
- No change to whether MCOOL has been enacted — it has not. Claim #11's core verdict (Unsupported, as
  commonly believed — mandatory COOL for beef was repealed 2015, no bill enacted yet) is unchanged.

## 2. Schaefer/poultry-concentration thread (Open Decision #6) — reviewed, no further automated progress possible

Read `NOTES/2026-09-07-schaefer-pozo-idea28-followup.md`, `NOTES/2026-09-08-schaefer-2024-broiler-cr4-pull-attempt.md`,
and `NOTES/2026-09-08-schaefer-2024-direct-read-resolves-poultry-discrepancy.md` in full per the brief's
instruction. Assessment: **this thread is already substantively resolved and there is nothing left for
automated tooling to do.** Recap of where it actually stands, stated plainly since the open-decision
text in `PROJECT_STATUS.md` is long and split across several dated updates:

- Britton directly read the actually-cited paper (Saitone, Schaefer, Scheitrum, Arita, Breneman, Nemec
  Boehm & Maples, 2024, *Review of Industrial Organization* 64, 35-56) via his own institutional access,
  2026-09-08. Its own broiler CR4 for FY2021 is **52%**, not 78%; its own broiler CR10 for FY2021 is
  **77%**, and the paper's own historical trajectory (32% in 1980 → 51% in 2010 → 52% in 2021) "leaves
  no room for a 78% figure at any point in this series" (2026-09-08 note's own words, still accurate on
  a fresh re-read tonight).
- The "78%" figure was independently confirmed real, verbatim, in a *different*, NETS-based 2025
  companion paper by five of the same authors — so it's not a fabrication, just very likely a
  mis-citation from one paper in this author team's body of work to another.
- The PDF itself is not present in this repo (per its own `.gitignore`, correctly kept out of git
  history as a copyrighted PDF) and is not re-accessible to this environment's tooling — Unpaywall's own
  index reported `is_oa: false` for the DOI as of 2026-09-08, meaning no open-access copy exists
  anywhere for automated tooling to find, not just that this environment couldn't reach one.
- **No further access attempt was made tonight.** Retrying the same blocked channels (Springer, the
  USDA mirror, RePEc, Unpaywall, Semantic Scholar) a third time, after two prior sessions (09-07, 09-08)
  already exhausted them with a documented `is_oa: false` verdict, would not be a good use of tonight's
  time — this matches the 2026-09-08 note's own recommendation ("recommend no further automated-retry
  time on this specific paper"). **Recommendation for Britton, restated plainly: this thread needs no
  further action from either Britton or an automated pass.** The working citation-mix-up hypothesis
  (78% belongs to the 2025 NETS paper, not the actually-cited 2024 FSIS paper) is about as strongly
  supported as it can be without Britton independently re-checking the 2024 paper's own reference list
  or footnotes for whether it cites its own 2019 broiler CR4 anywhere — a two-minute check for Britton if
  he still has the PDF, not something worth further automated search time.
- The poultry regional-monopsony finding flagged 2026-09-08 (Table 2, Eastern Mountain region
  cattle-plant "neighbor" competition falling from 59.9 to 18.2 competing plants within 150 miles,
  1991→2021) has not yet been pulled into `LITERATURE/Market_Concentration_Evidence.md` — checked
  tonight, still not done. Low-priority housekeeping item, noted but not actioned tonight given time
  spent on the litigation recheck and Claim #7 work below.

## 3. Claim #7 primary-source verification — real advance, not just re-description

Per the brief's instruction to do real primary-source verification on 1-2 open claims. Picked Claim #7
("Do imports materially suppress domestic cattle prices?" — genuinely Unresolved, "no verified
econometric estimate of the size of any import effect" per the 2026-09-05 update) because it's one of
only two remaining genuinely-Unresolved claims (with #5) and because it's central to this paper's actual
motivating question.

**Search chain**: WebSearch for "econometric estimate effect beef imports U.S. cattle prices elasticity"
surfaced a specific, on-point working paper — Brester, G.W. & Marsh, J.M. (1999), "U.S. Beef and Cattle
Imports and Exports: Data Issues and Impacts on Cattle Prices," *Policy Issues Papers* 2, Montana State
University Trade Research Center. A `curl` fetch of the actual PDF (ageconsearch.umn.edu) returned
**HTTP 202 with an empty body**, consistently, on two attempts with different user agents — a genuinely
unusual response (not a straightforward block/403), not resolved tonight. `WebFetch` of the same URL
403'd. The paper's own bibliographic record on **ideas.repec.org** (RePEc, a legitimate academic
bibliographic archive, not an AI-search synthesis) was fetched directly and gives the paper's full
abstract in its own words, including a specific numeric finding: **of an $8/cwt decline in U.S. slaughter
cattle prices during the 1990s, ~$0.35/cwt (≈4.4%, ≈$4.20/head for a 1,200-lb fed steer) is attributable
to increased Canadian imports.** This is secondary-sourced (RePEc's restatement of the paper, not the
primary PDF itself) — flagged as such in the Evidence Table, not treated as a direct primary read.

**Better outcome: a related USITC investigation report, found via the same search, WAS obtained and read
in full as a genuine primary source.** USITC Publication 3048, "Cattle and Beef: Impact of the NAFTA and
Uruguay Round Agreements on U.S. Trade" (Investigation No. 332-371, July 1997) — `curl` succeeded (HTTP
200, 9.4MB) where `WebFetch` 403'd; `poppler-utils` (missing from this session's container, reinstalled
via `apt-get`) extracted 10,761 lines of readable text via `pdftotext -layout`. Direct quotes and figures
read from the report itself:

- **"Marsh and Greer (1994) analyzed the U.S. price effects from exports of Canadian live cattle and
  beef. They estimated that during 1993 and 1994, exports of LCFS and meat from Canada led to a decline
  in U.S. steer prices by about $2 per hundred weight (less than .3 percent). In a similar study, Marsh
  and Peck (1996) looked at the effects of U.S. beef and live cattle trade on the prices of U.S. feeder
  cattle. In both studies, the relatively minor impact Canadian exports were found to have on U.S. fed
  and feeder cattle prices reflects the small share of total U.S. beef supplies these exports represent
  (3 percent)."** (p. K-3)
- The report's own econometric model of Mexican beef import demand (OLS, monthly data Jan. 1991-Dec.
  1996, Adj. R²=0.85): **"for every 1-percent increase in the price of imported beef, import demand falls
  about 1.1 percent"** (p. I-6) — an import-demand elasticity, not a domestic-price-suppression estimate;
  kept conceptually distinct in the Evidence Table entry.
- The report's own synthesis of multiple contemporary CGE/partial-equilibrium studies: **"The URA will
  result in small increases in U.S. beef prices, in the range of 4 to 6 percent"** (p. C-10) — i.e., the
  Uruguay Round's *net* projected effect on U.S. beef prices was positive (via expanded export access),
  the opposite mechanism from "imports suppress prices," a useful complicating data point.
- The report's own overall conclusion on NAFTA specifically: **"The analysis indicates the NAFTA has not
  had any major impact on the trade in LCFS. This can be explained by the fact that the ad valorem
  equivalent of the rate of duty for LCFS was less than 2 percent before January 1994 when the NAFTA was
  signed"** (p. K-11) — directly undercuts a simple "NAFTA caused the import surge" narrative for live
  cattle.
- Also noted in passing (not this session's focus but worth flagging): the report's own 1994 steer/heifer
  slaughter CR4 figure is **81%** ("the four largest firms accounted for 81 percent of steer and heifer
  slaughter in 1994," p. xiii) — close to, and a useful additional corroboration of, AER-785's
  independently-documented 80% by 1997 and PSD's 85% (2019)/81% (2020-21) figures already anchoring
  Claim #3. Not added as a new Evidence Table row tonight (out of scope), but worth knowing this report
  is a second largely-independent primary source for that period's concentration level.

**Net effect on Claim #7**: upgraded from "Unresolved, no verified econometric estimate exists" to a
split verdict — real, mutually-corroborating quantitative estimates now exist for the **historical,
Canada-specific, NAFTA-era (1990s) case** (three independent studies from the same Montana State
research group, all converging on a small-magnitude effect, well under 5% of observed price movements),
while the **current (2020s) import environment** — dominated by Australia and Brazil, not Canada, against
a record-low domestic cattle herd — has no comparable estimate and remains genuinely unresolved. This is
a real, structurally important distinction: these 1990s Canada-specific findings should not be
extrapolated to characterize today's import effect, and the manuscript should say so explicitly if it
cites these figures at all. Full detail and all four new rows: `SOURCE_VERIFICATION/Evidence_Table_Imports.md`
(Beef section); verdict rewritten in `NOTES/Claim_Fact_Check.md` (Claim #7 row and the cross-cutting
notes section).

## 4. Brief literature-gap scouting

One additional relevant-but-adjacent paper found and independently checked via `WebFetch` (not just a
search snippet): **Sun, K.-A. & Moon, J. (2025), "Exploring the Antecedents and Consequences of Perceived
Fairness in Beef Pricing: The Moderating Role of Freshness Under Conditions of Information Overload,"
*Foods* 14(11), 1844.** U.S. beef consumers (n=415), Hayes Process Macro moderation analysis: organic
perception positively affects both price fairness and revisit intention, but freshness information
*moderates this downward* — pairing organic claims with freshness cues made consumers perceive prices as
*less* fair (information-overload effect). Confirmed via direct read of the article's own content, not
just a title match: this study does **not** address country-of-origin labeling, corporate
price-increase-explanation types, or value-distribution transparency (farmer vs. processor vs. retailer
share) — it's a food-science-journal (not marketing-journal) behavioral study of organic/freshness
cue-stacking. Same conclusion as the 2026-09-22 pass's finding on Holdershaw & Konopka (2023): adjacent,
not occupying, this project's specific price-fairness × corporate-explanation-type × COO-disclosure gap.
That gap still reads as open after a third scouting pass with a different search angle.

## What did NOT change tonight

- No design decisions made or needed.
- Claim_Fact_Check.md: only Claim #7's row and the cross-cutting-notes paragraph were edited; all other
  verdicts unchanged.
- Open Decision #6 (Schaefer): no verdict change, just confirmed as already-closed with nothing further
  for automated tooling to do.

## Genuinely still open, stated plainly

- Claim #5 (asymmetric price transmission) remains fully Unresolved — not worked tonight, given time
  spent on Claim #7 and the litigation recheck.
- Claim #7's *current-era* (2020s, Australia/Brazil-dominated) import-price-effect magnitude remains
  unresolved — only the 1990s Canada-specific case now has real numbers behind it.
- Brester & Marsh (1999)'s own PDF remains unobtained (ageconsearch.umn.edu returns HTTP 202/empty to
  both `curl` and WebFetch) — the figure is currently sourced to RePEc's bibliographic restatement, one
  notch below this project's usual primary-document standard. Worth one more attempt in a future session
  with a different access method (e.g., Google Scholar cache, a different mirror) if the exact figure
  ever needs to go in the manuscript with a primary citation.
- Farm-bill floor-vote timing is now correctly flagged as contested/unsettled rather than a single
  "after midterms" data point — no actual date exists yet either way.
- MCOOL committee roll-call record: still a hard wall (agriculture.senate.gov now loads without a 404 but
  has no vote-tally content on its farm-bill summary page; congress.gov not re-attempted tonight,
  consistent with the 2026-09-22 recommendation to stop spending automated-retry time on it).

## For Britton

Three things worth knowing: (1) the farm bill's "floor vote expected after the midterms" framing in this
project's notes is more settled-sounding than reality — there's live, unresolved political pressure for a
pre-midterm vote in a narrow window (Senate in session through early October), and nobody has actually
committed to a date either way; (2) Claim #7 (does the literature actually quantify an import
price-suppression effect on cattle prices?) now has a real answer for the historical NAFTA-era Canadian
case — small (under ~5%), from a coherent multi-study Montana State research program — but nothing
comparable exists yet for the current Australia/Brazil-dominated import environment this paper is
actually about, which is worth being explicit about in any manuscript language; (3) the Schaefer
poultry-CR4 thread needs no further action from anyone — it's as resolved as it's going to get without a
two-minute check of the paper's own footnotes, which only Britton can do if he still has the PDF.

No money spent. No one contacted. Nothing submitted anywhere.
