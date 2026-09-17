# 2026-09-17 — Agri Stats broiler (End-User Consumer) final-approval confirmed, MCOOL farm-bill development, literature scouting

Eighth research session. Scope tonight, per the task brief: (1) recheck `PROJECT_STATUS.md`'s Open
Decisions and litigation-tracking items — specifically the Sept. 1, 2026 Agri Stats broiler
final-approval hearing (that date has now passed as of today, 2026-09-17), the Tyson $82.5M DPP
settlement, and the (separate) End-User Consumer class's own Agri Stats settlement; (2) advance
`NOTES/Claim_Fact_Check.md` where possible; (3) a literature-gap scouting pass; (4) write up findings
and update `PROJECT_STATUS.md`. Method: `WebSearch`/`WebFetch` for everything, plus direct `curl`
(browser User-Agent) for a settlement-administrator document site and CourtListener's HTML search/
docket pages. Installed `poppler-utils` and `tesseract-ocr` locally again (this container evidently
doesn't persist packages installed in a prior session's container) to extract text from downloaded
court PDFs. No design decisions touched, no external contact made.

## 1. Agri Stats End-User Consumer broiler settlement — Sept. 1, 2026 final-approval hearing: CONFIRMED HELD, settlement APPROVED

This was the specific, dated, previously-unconfirmed item the task brief asked about, and tonight
resolves it — with one honest caveat about verification depth (see below).

**Finding: final approval was granted at the September 1, 2026 hearing.** Best source: MLex (a
paid specialist antitrust-law newswire; the same source type this project has cited before for the
DOJ Agri Stats case), article "US judge approves Agri Stats settlement, finds value in behavioral
changes." I checked its own byline directly rather than trusting a WebSearch paraphrase: **"By
Clayton Vickers (September 1, 2026, 19:40 GMT | Insight)"** — i.e., published same-day. Its own
first sentence, quoted directly: *"A no-cash settlement reached between Agri Stats and end-user
consumer plaintiffs to resolve their broiler chicken price-fixing claims is still valuable due to
behavioral changes the company agreed to, a US judge said Tuesday before granting the settlement
final approval."* (September 1, 2026 was indeed a Tuesday.) This is the **private End-User Consumer
class's own Agri Stats settlement** — the one `SOURCE_VERIFICATION/Evidence_Table.md` has flagged
since 2026-09-07 as "not independently re-verified against the docket" — genuinely distinct from
DOJ's civil case against Agri Stats (Final Judgment Sept. 10, 2026, already resolved in this
project's 2026-09-13 pass). I independently confirmed the DOJ case really is a separate MLex
article (a different story ID, dated Sept. 11 discussing "DOJ, states," no mention of the private
plaintiffs) — the two tracks are not being conflated here.

**Terms**: no cash from Agri Stats specifically (distinct from the $203.35M End-User Consumer fund,
which comes from the poultry-processor defendants, already known to this project) — purely
injunctive/behavioral: Agri Stats will stop listing subscriber names on report covers, stop
including competitor-/plant-level price and production data, and is barred from helping
de-anonymize subscriber data, plus compliance-program commitments. This closely parallels the DOJ
settlement's own terms (also injunctive-only) — a real substantive pattern worth noting: **two
independent tracks against the same defendant (DOJ civil suit, private class action) landed on
essentially the same remedy type (data-sharing-practice reform, no money from Agri Stats itself)
within ten days of each other**, which is itself a piece of evidence about what kind of "wrongdoing"
regulators/courts saw here (information-sharing conduct, not price-fixing Agri Stats itself directly
profited from).

**What I could NOT do, stated plainly**: I could not pull the actual signed court order's text
directly, despite trying multiple channels. I found the correct CourtListener docket for the master
case (*In re Broiler Chicken Antitrust Litigation*, No. 1:16-cv-08637, N.D. Ill., Judge Thomas M.
Durkin — courtlistener.com/docket/4508538/) via a working search-page fetch, but the docket's main
page didn't expose entries beyond a first RECAP-cached page without a PACER-backed fetch, and the
official settlement-administrator site I also found and pulled PDFs from
(broilerchickenantitrustlitigation.com) turned out — after actually checking each document's own
"Filed:" date — to hold only the 2024-vintage **Direct Purchaser Plaintiffs'** own, earlier and
already-closed Agri Stats settlement (Document #7423, filed 10/24/24), not the 2026 End-User
Consumer settlement. **I'm flagging this explicitly rather than silently citing the wrong document**:
initially I nearly treated that site's PDFs as confirmation before checking their filed-dates, which
would have been exactly the kind of source-conflation error this project's process exists to catch.
So tonight's confirmation rests on a same-day, named-byline, specialist-newswire report (MLex) rather
than a directly-read court order — a step below this project's usual "primary court-record read"
standard for litigation items, but a real step up from "unconfirmed," which is where this sat as of
2026-09-15. Recommend a future pass try to pull the actual order (likely filed under the End-User
Consumer sub-docket of the same 1:16-cv-08637 case) if RECAP/PACER access becomes available.

**Bottom line for Britton**: the private End-User Consumer track's Agri Stats settlement is now
final (Sept. 1, 2026), same outcome type (behavioral-only, no incremental cash) as DOJ's own
settlement nine days later. The $203.35M consumer cash fund itself (from the poultry processors,
not Agri Stats) is unrelated to this and — per the last data point found — still had no distribution
date as of early August 2026; not rechecked further tonight, out of scope for what was asked.

## 2. Tyson $82.5M DPP settlement — no change since 2026-09-15

Searched for anything new. Found nothing that changes the 2026-09-15 finding: Final Approval
Hearing remains scheduled for **November 12, 2026** (objection/opt-out deadline October 23, 2026),
not yet decided. One clarifying non-development: search results this week are dominated by news
about the **different, already-resolved $87.5M** indirect-purchaser beef settlement's claims-filing
deadline (June 30, 2026) and pending distribution — the same conflation risk flagged in the
2026-09-09 note. Keeping the two settlements ($82.5M direct-purchaser vs. $87.5M end-user/indirect)
distinct, as before. **No update needed to `PROJECT_STATUS.md` item 9 beyond noting tonight's
recheck found nothing new.**

## 3. New, not previously tracked: a $117.065M pork price-fixing consumer settlement, and confirmation of an Agri Stats pork track

Not something tonight's brief asked about specifically, but surfaced while checking litigation
generally and worth recording since it bears on Claim #15 (price-fixing spans all three
commodities). A separate End-User Consumer pork antitrust MDL (D. Minn., same court family as the
beef DPP case) has a **combined $117.065M settlement with five pork processors — Tyson ($85M),
Clemens ($13.5M), Seaboard ($10M), Hormel ($4.465M), Triumph ($4.1M)** — preliminarily approved
July 31, 2026, per multiple claims-administrator/trade outlets (topclassactions.com,
openclassactions.com, Daily Hodl, several local-news claims-syndication sites — all describing the
same figures consistently, a good sign, but none of these are primary court documents and none were
independently read in full tonight). The same coverage states **JBS and Smithfield's portions of
this same pork MDL already separately settled and closed to new claims** (consistent with this
project's existing ~$200M Smithfield / $20M JBS pork figures already in Claim #15 — this doesn't
contradict those, it's a different, later wave of defendants in the same litigation family) — **and
that Agri Stats also has a pork-antitrust settlement, behavioral-only like its chicken/turkey
settlements, no cash**. This confirms Agri Stats' settlement pattern (data-sharing reform, no
money) now spans all three poultry/pork-adjacent tracks this project has been following (DOJ,
chicken End-User Consumer, and now pork). **Not yet folded into `Claim_Fact_Check.md` or the
Evidence Table with full citations — flagging as a real, found item for a future pass to verify
against a primary settlement-administrator or docket document before manuscript use**, not doing
that verification tonight since it's outside what was specifically asked.

## 4. Genuinely significant, not previously tracked: live Senate action to restore mandatory COOL for beef — as recent as yesterday (Sept. 16, 2026)

This is the most consequential new finding of the night, and it bears directly on this project's
core factual claim (Claim #11: mandatory COOL for beef/pork was repealed Dec. 2015 and nothing has
replaced it). **That underlying fact remains true as of today — no bill has been enacted** — but
there is now a real, bipartisan, actively-moving legislative effort that a manuscript relying on
"consumers cannot verify origin" as a stable structural fact should be aware could change before
publication. Found via general web search while checking for COO/price-fairness literature, then
verified across several independent trade-press and one official Senate source (methodology below);
**no primary court/legislative-text document was independently read tonight** (congress.gov,
govtrack.us, and the official Senate Agriculture Committee site's specific press materials all
403'd to both `WebFetch` and direct `curl` with a browser UA) — this section is secondary-sourced,
corroborated across multiple independent outlets, not primary-verified, and should be read with that
caveat.

Timeline, as reported:
- **February 5, 2025**: Sens. Cory Booker (D-NJ) and John Thune (R-SD) reintroduced the "American
  Beef Labeling Act" (S.421, 119th Congress) — mandatory COOL for beef.
- **October 24, 2025**: Reps. Harriet Hageman (R-WY) and Ro Khanna (D-CA) reintroduced a House
  companion, the "Country of Origin Labeling Enforcement Act of 2025" (H.R. 5818).
- **August 6, 2026**: During a Senate Agriculture, Nutrition & Forestry Committee farm-bill markup,
  Thune's beef-MCOOL amendment (based on S.421) was adopted — reported as a **17-6** bipartisan vote
  by several outlets (TSLN, two Ag Bull Trading pieces) but as **16-7** by a DTN/Progressive Farmer
  Washington Insider piece published 2026-09-17 — **a real discrepancy between sources, not
  resolved tonight**, flagging it rather than picking one number. All sources agree the amendment
  passed with bipartisan support (all Democrats plus several Republicans from cattle states) over
  opposition from Republicans from packing/feedlot/export-heavy states, including the committee
  chairman. The full farm bill itself did **not** advance that day — markup stalled separately over
  a SNAP dispute.
- **September 4, 2026**: Per a TSLN article quoting R-CALF USA, President Trump directed USDA to
  review pathways (regulatory or legislative) for implementing MCOOL — **this specific claim was
  not independently verified against a White House or USDA primary document tonight**, treat as
  reported-only.
- **September 16, 2026 (yesterday)**: The full Senate Agriculture Committee reported the "Agricultural
  Act of 2026" (the Senate's 2026 farm bill) out of committee on a **12-11 party-line vote**
  (Democrats unanimously opposed, on unrelated SNAP grounds per reporting, not on MCOOL), aided by
  Sen. Mitch McConnell's return to the committee — **retaining the MCOOL beef-labeling provision**
  adopted in the August markup. Sources: TSLN, DTN/Progressive Farmer (two separate pieces, one
  published today), AGDAILY, a National Association of Counties summary, and Sen. Thune's own
  official press release (which independently confirms Republicans "successfully voted to advance
  the Senate farm bill out of the Agriculture Committee," though it doesn't itself give the vote
  count). **Next step, per this reporting**: a full Senate floor vote, expected after the November
  2026 midterm elections, then likely a conference negotiation with the House's own farm bill
  version if it passes — not close to enactment yet.
- Separately and previously unnoticed by this project: USDA's own October 2025 "Beef Industry Plan"
  white paper (announced by Secretary Rollins) names **"consumer transparency"** as one of its three
  explicit policy pillars, tied concretely to FSIS enforcement of the "Product of USA" labeling rule
  — i.e., USDA's own current framing already uses transparency language adjacent to this project's
  own. **I could not fetch the white paper's own PDF directly tonight** (usda.gov 403'd both
  `WebFetch` and direct `curl`) — this is reported via secondary ag-trade coverage only (Ohio Ag
  Net, Southeast AgNet, Iowa Capital Dispatch, NACo — consistent across outlets on the three-pillar
  structure, but none independently read as primary text tonight).

**Why this matters for the project, stated plainly and not as a design recommendation**: this
project's Claim #11 and its "consumers cannot verify origin from a standard label" framing are
still factually correct *today*, but they describe a legal status that a live, bipartisan Senate
effort is actively trying to change, with real (if early-stage) momentum. This doesn't change any
verdict in `Claim_Fact_Check.md` — nothing has passed — but it is a genuinely new, dated,
well-corroborated development Britton should know about before finalizing any manuscript language
that treats COOL's absence as a settled, unchanging backdrop, and it is itself excellent potential
Study 1 discourse material (NCBA vs. R-CALF positions on MCOOL, a live legislative fight, are exactly
the kind of institutional-attribution discourse the project's Study 1 concept already targets) —
flagging that as an observation, not a scope recommendation; Study 1 commodity/source-scope stays
Britton's call per Open Decision #1/#2.

## 5. Literature-gap scouting

One additional real marketing-journal source found, adjacent but not gap-closing: **Holdershaw, J.,
& Konopka, R. (2023). "The effect of visibility of country of origin labelling on consumers' fresh
meat preferences." *Asia Pacific Journal of Marketing and Logistics*, 35(9), 2266–2281.** Method:
Best-Worst Scaling across two countries, varying COOL font size and package placement. Finding:
consumers prefer domestic over imported meat and larger label fonts; label *placement* matters less
than font size. This is a real marketing-journal (not food-science) COO-labeling study in a meat
context — closer to this project's angle than anything found 2026-09-15 — but it studies label
*design/visibility* mechanics, not price-fairness, corporate explanation type, or value-distribution
transparency, so it doesn't occupy this project's specific gap. Worth citing as adjacent COO-in-meat
marketing literature, not as a competing paper. No new source was found this pass on the project's
specific combination (COO disclosure × corporate price-explanation type → price-fairness attribution
→ trust/purchase intention, in a meat context, in a marketing journal) — **the gap identified
2026-09-15 still reads as open**, now checked twice with different search angles.

## For Britton

Two genuinely new, dated developments tonight, in order of how much they should matter to you:

1. **A live, bipartisan Senate effort to restore mandatory country-of-origin labeling for beef is
   materially advancing right now** — a farm-bill provision (Thune's American Beef Labeling Act)
   passed committee markup Aug. 6, 2026 (17-6 per most outlets, 16-7 per one — genuine discrepancy,
   not resolved), and the full Senate farm bill containing it was reported out of committee
   yesterday, Sept. 16, 2026, on a 12-11 party-line vote. Next stop is a full Senate floor vote,
   expected after the November midterms — this is still early, not close to becoming law, but it's
   real and moving, and it's the closest Congress has come to acting on beef MCOOL since its 2015
   repeal. This doesn't change any current fact in the paper, but it's worth knowing the "consumers
   can't verify origin" backdrop could shift during your writing/review timeline, and the political
   discourse around it (who's for/against, and why) looks like strong Study 1 material. I could not
   independently read the actual bill text or committee vote record tonight (congress.gov and the
   Senate committee's own site both blocked automated fetches) — this rests on consistent trade-press
   reporting plus one official Senate press release, not a primary document I read myself.
2. **The Sept. 1, 2026 Agri Stats broiler final-approval hearing you flagged did happen, and the
   settlement was approved** — this is the *private* End-User Consumer class's own Agri Stats
   settlement (behavioral-only, no cash from Agri Stats), distinct from DOJ's own Agri Stats case
   (already resolved Sept. 10). Confirmed via a same-day, named-byline specialist antitrust
   newswire (MLex) — solid, but a notch below this project's usual "read the actual order" standard,
   since I could not locate/pull that specific order's text tonight (tried CourtListener and a
   settlement-administrator site; the latter turned out to hold a different, older 2024 Agri Stats
   settlement for a different plaintiff group — caught before it got miscited, not after).

Also found, lower priority: a new $117M pork price-fixing consumer settlement (Tyson, Clemens,
Seaboard, Hormel, Triumph — preliminarily approved July 31, 2026) not yet folded into the Evidence
Table; and one more real marketing-journal COO/meat-labeling study (Holdershaw & Konopka 2023,
*APJML*) that's adjacent to but doesn't occupy this project's specific gap. The Tyson $82.5M DPP
settlement needed no update (Nov. 12, 2026 hearing still pending, nothing new found).

No design decisions were made or needed. No money spent. No one contacted.
