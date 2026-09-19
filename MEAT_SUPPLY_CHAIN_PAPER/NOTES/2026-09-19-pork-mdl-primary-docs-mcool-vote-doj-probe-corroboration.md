# 2026-09-19 — Pork MDL primary-document pull, MCOOL vote-count check, DOJ retailer-probe corroboration

Ninth research session. Scope tonight, chosen from `PROJECT_STATUS.md`'s own flagged open items rather
than re-doing closed threads: the Schaefer/poultry-concentration discrepancy (Open Decision #6) and the
core facts of scouting-log idea 28 are both already resolved as of 2026-09-08/09-15 — reconfirmed that by
reading the current `PROJECT_STATUS.md` and `NOTES/Claim_Fact_Check.md` before starting, and did not
re-run that work. Instead, three genuinely open loose ends were picked up: (1) the $117.065M pork
price-fixing settlement flagged 2026-09-17 as "not yet independently read against a primary document";
(2) the 17-6 vs. 16-7 Senate Ag Committee MCOOL vote-count discrepancy flagged 2026-09-17 as
"unresolved"; (3) a secondary-sourced detail from the DOJ retailer-probe thread (idea 28) flagged
2026-09-08 as "NOT independently confirmed" — the July 14, 2026 letter date. Method: direct `curl`
fetches of government-hosted PDFs (govinfo.gov) and CourtListener-adjacent sources, `pdftotext` for
extraction (installed `poppler-utils`/`tesseract-ocr` again — confirms this container doesn't persist
packages across sessions, consistent with prior nights' notes), `WebSearch`/`WebFetch` for corroboration.
No design decisions touched, no external contact made, nothing submitted anywhere.

## 1. Pork antitrust MDL ($117.065M settlement) — primary court documents read directly; one real correction to the project's existing note

Found the actual docket via a `govinfo.gov` URL pattern that turned up in search results
(`USCOURTS-mnd-0_18-cv-01776`) and pulled several adjacent document numbers directly. This is
**In re Pork Antitrust Litigation, Civil No. 18-1776 (JRT/JFD), D. Minn., Judge John R. Tunheim** — the
same court and same judge as the beef MDL (22-3031) and the Agri Stats DOJ case, a different docket
number. Two documents read in full:

**Doc. 3436 (filed 7/31/26) — "Order Granting Approval of Consumer Indirect Purchaser Plaintiffs' Motion
for Approval of Direct Notice, Plan of Notice, and Plan of Allocation."** This is the actual court
order behind the date this project's 2026-09-17 note recorded as "preliminarily approved July 31, 2026."
**Reading it directly shows that characterization needs a correction**: July 31, 2026 is not when the
settlements were preliminarily approved — it's when the Court approved the *notice plan* for a group of
settlements that had already been preliminarily approved on five separate, earlier, staggered dates,
listed explicitly in the order's own text:
- Hormel: preliminary approval July 9, 2024 (Docket No. 2414)
- Seaboard: preliminary approval Aug. 6, 2024 (Docket No. 2453)
- Clemens: preliminary approval June 13, 2025 (Docket No. 3073)
- Tyson: preliminary approval Nov. 7, 2025 (Docket No. 3193)
- Triumph and Agri Stats (bundled together): preliminary approval May 5, 2026 (Mem. Op. and Order,
  Docket No. 3389)

So "$117.065M preliminarily approved July 31, 2026" (as recorded 2026-09-17, sourced only to
claims-administrator/trade coverage) should be corrected to: **the five processor settlements
(Tyson $85M, Clemens $13.5M, Seaboard $10M, Hormel $4.465M, Triumph $4.1M = $117.065M combined) were
preliminarily approved individually between July 2024 and May 2026; July 31, 2026 is when the Court
approved sending class notice and set the claims/objection schedule** — a real, material precision
correction, not a contradiction of the dollar figures themselves (which the primary order's exhibits
reference consistently and which multiple independent claims-administrator sites already had right).
The order also gives the actual class definition and confirms the correct official name for this
plaintiff group is **"Consumer Indirect Purchaser Plaintiffs,"** not "End-User Consumer" (the label this
project has been using, carried over from the broiler-chicken MDL's own terminology, which does use
"End-User Consumer" as its actual class name — the two MDLs use different official class names for what
is functionally the same type of class, a real cross-case terminology trap worth flagging). Per the
order's own schedule table: notice begins Order+30 days, exclusion/objection/claims deadline is
Order+90 days (≈ Oct. 29, 2026 — consistent with the Oct. 29 claims deadline independently reported by
several claims-administrator sites, a good cross-check), and the Final Approval Hearing is set for
"40 days from the last day to request exclusion" (≈ early-to-mid December 2026 — consistent with, though
not identical in wording to, secondary reporting of a Dec. 11, 2026 fairness hearing; the exact date
was not stated as a fixed calendar date in this order, so treat "~Dec. 11, 2026" as secondary-sourced,
plausible, and not contradicted, not primary-confirmed to the day).

**New finding, not previously tracked by this project at all: Doc. 3472 (filed 9/10/26) — "Order
Granting Motion for Final Approval of the Class Action Settlement Between Direct Purchaser Plaintiffs
and Agri Stats, Inc."** This is a *separate* pork-specific Agri Stats settlement track — the **Direct
Purchaser Plaintiffs' (DPP)** settlement with Agri Stats in this same pork MDL, distinct from the
Consumer Indirect Purchaser Plaintiffs' pork-Agri-Stats settlement referenced in Doc. 3436's recitation
above (preliminarily approved as part of the Triumph/Agri Stats bundle, May 5, 2026). The DPP-Agri
Stats pork settlement reached **final approval on September 10, 2026** — the identical date DOJ's own
civil Agri Stats case (broiler/turkey) reached Final Judgment, and nine days after the private
End-User Consumer broiler settlement's own Sept. 1, 2026 final approval. This order dismisses all DPP
claims against Agri Stats "on the merits and with prejudice" but, like the broiler-side Agri Stats
settlements already documented in this project, **does not state a dollar figure in its own text** —
consistent with, but not proof of, the "behavioral-only, no cash" pattern already established for
Agri Stats elsewhere; this specific order doesn't independently confirm that pattern for the pork-DPP
track since it simply incorporates-by-reference a Settlement Agreement (Docket No. 3381) whose terms
weren't separately pulled tonight. **Net effect: Agri Stats now has confirmed settlement resolutions
across four separate litigation tracks in this project's timeline (DOJ civil case, broiler End-User
Consumer, pork Consumer IPP, pork DPP) — all landing within about six weeks of each other
(May–September 2026), all sharing the same defendant, and all following the same broad pattern
(behavioral/data-practice remedies, no admission of wrongdoing) as far as has been directly read.**
This strengthens, with one more directly-read data point, the existing Claim #15 observation that
Agri Stats' conduct (data-pooling/information-sharing) is being treated categorically differently by
courts than the processors' own price-fixing conduct.

Also incidentally found and skimmed three related dismissal orders in the same docket family (Docs.
3434, 3435, 3439 — Domino's Pizza v. Triumph, Golden Corral v. Triumph, Winn-Dixie v. Agri Stats, all
filed 7/31/26–8/4/26): these are individual **Direct Action Plaintiffs** (companies that opted out of
the class to sue on their own) settling and dismissing their own separate suits against individual
defendants. Not independently significant for this project's claims, but useful confirmation that the
pork MDL, like the beef and broiler MDLs already documented, has a large family of parallel
class-action and opt-out tracks that should not be conflated with each other — same lesson this
project has already learned twice (broiler DOJ-vs-private, and beef $87.5M-vs-$82.5M).

## 2. MCOOL committee vote count: 17-6 vs. 16-7 — not primary-resolved, but now substantially clarified

The official Senate Agriculture Committee record itself remains inaccessible (agriculture.senate.gov's
newsroom page 404'd; congress.gov's committee-meeting page 403'd to both `curl` and `WebFetch` — same
wall as 2026-09-17). However, direct reads of the actual underlying articles (not just search
snippets) sharpen the picture considerably:

- **Capital Press** (Aug. 7, 2026) and **DTN/Progressive Farmer's own original Aug. 6, 2026 article**
  ("Bipartisan Senate Vote Advances Beef MCOOL...") both independently give a **17-6** count, and DTN's
  own August piece names individual senators: 6 Republicans voting yes (Thune, Fischer, Hoeven,
  Hyde-Smith, Grassley, Ernst) plus "all Senate Democrats," against 6 Republicans voting no (McConnell,
  Marshall, Tuberville, Justice, Moran, and Committee Chairman Boozman). If the committee has 11
  Democrats (matching "all Democrats" support) and 12 Republicans (6 yes + 6 no), that's a 23-member
  committee splitting 17-6 — internally consistent arithmetic.
- **Capital Press**, read directly, separately states the raw numbers slightly differently in its own
  prose — "Six Republicans and 11 Democrats supported" the amendment (=17) against "six Republicans...
  voted against" (=6) — the same 17-6 total, corroborating DTN's breakdown independently.
- The **lone 16-7 figure** traces to a single DTN/Progressive Farmer *Washington Insider* piece dated
  2026-09-17 (fetched directly tonight, quote: "passed by a 16-7 vote in August, in favor of MCOOL") —
  a different DTN article than the one with the detailed 17-6 breakdown, published six weeks later,
  with no senator-level detail given.

**Assessment**: two independently-authored, contemporaneous (Aug. 6-7, 2026) articles with a named,
internally-consistent vote breakdown say 17-6; one later (Sept. 17) DTN piece with no supporting detail
says 16-7. This doesn't rise to a primary-source resolution (that would require the committee's own
roll-call record, still blocked), but it meaningfully shifts the balance of evidence toward **17-6 as
the more likely correct figure, with 16-7 plausibly a transcription/reporting error in the later DTN
piece** (rather than, say, a senator flipping their recorded vote after the fact, for which no evidence
exists). Recommend the project state "17-6 per the most detailed contemporaneous reporting, though one
later source gives 16-7" rather than treating this as a coin-flip — a modest but real sharpening from
"genuinely unresolved" to "leans clearly toward one figure."

## 3. DOJ retailer-probe July 14, 2026 letter date: upgraded from unconfirmed to corroborated (still not DOJ's own document)

The 2026-09-08 note flagged one specific secondary-sourced detail — that DOJ's information-request
letters to the eight retailers were dated July 14, 2026, weeks before the public Sept. 1-2 announcement
— as "NOT independently confirmed this pass and should not be used without further verification."
Tonight: **Transport Topics** (a legitimate trade-press outlet, syndicating Bloomberg wire content) was
fetched directly and quotes: *"Woodward, in letters dated July 14, asked the grocers to supply
investigators with details about their beef purchasing and strategy."* Bloomberg's own article
(bloomberg.com/news/articles/2026-09-02/amazon-walmart-face-data-requests-in-doj-beef-antitrust-probe)
could not be fetched directly (403, paywall-adjacent), but the Transport Topics republish independently
carries the same July 14 date and the same Woodward attribution already confirmed via DOJ's own social
post. **This is still not a DOJ-authored document** (the letters themselves haven't been located/read),
but it is now corroborated by a named, dated, reputable wire-service report rather than resting on
unattributed aggregator summaries — a real, if modest, evidentiary upgrade. Recommend continuing to
flag it as "reported by Bloomberg/wire services, not independently confirmed against the letters
themselves" rather than treating it as fully primary-verified.

## What did NOT change tonight

- Tyson $82.5M DPP settlement (MDL 22-3031): searched again; found nothing that changes the
  2026-09-15/17 finding (Final Approval Hearing Nov. 12, 2026, objection deadline Oct. 23, 2026, not yet
  decided). The settlement-administrator site (beefdirectpurchasersettlement.com) is JavaScript-rendered
  and returned no usable text via either `curl` or `WebFetch` tonight — not a contradiction, just an
  unhelpful source, consistent with this being a non-issue rather than a new blocker.
- Idea 28 (DOJ beef price-fixing probe): no indictments, no material developments beyond the July 14
  letter-date corroboration above. Still open, as before.
- Schaefer/poultry-concentration (Open Decision #6) and the core Claim_Fact_Check verdicts: reconfirmed
  already resolved/current by reading `PROJECT_STATUS.md` before starting — not re-touched tonight, per
  this project's "don't redo already-verified work" instruction.
- Literature-gap scouting was not repeated tonight (two dedicated passes, 09-15 and 09-17, already ran
  targeted searches with different angles and both came up empty on the project's specific gap) —
  judged lower-value than closing the three items above given a finite session; flagging this choice
  explicitly rather than silently skipping it.

## Genuinely still open / hard walls, stated plainly

- **The Senate Agriculture Committee's own official roll-call record for the Aug. 6, 2026 MCOOL vote is
  a genuine hard wall**: agriculture.senate.gov (404 on the newsroom path tried) and congress.gov
  (403 to both `curl` and `WebFetch`) have now been tried on two separate nights (2026-09-17, 2026-09-19)
  with no success. Recommend not spending further automated-retry time on this specific record — if the
  exact 17-6/16-7 figure ever needs to be pinned down with certainty, that likely requires either a
  non-automated browser session or Britton's own access, not this environment's tooling.
- **The pork MDL's Doc. 3381 (the actual Settlement Agreement exhibit) was not pulled tonight** — it
  would state the Agri Stats pork-DPP settlement's actual terms (cash or no cash) directly rather than
  by inference from the pattern established elsewhere. A reasonable next-session target if this thread
  gets picked up again, though it is not currently blocking any claim in `Claim_Fact_Check.md`.
- **The exact December 2026 Final Approval Hearing date for the $117.065M pork settlement** was not
  pinned to a specific calendar date from the primary order itself (it's expressed as "40 days from
  the exclusion deadline," which computes to early-to-mid December but wasn't stated as a fixed date in
  the document read) — secondary sources say Dec. 11, 2026; treat that as plausible, not primary-verified
  to the day.

## For Britton

Three small-to-medium corrections/upgrades tonight, none changing any headline verdict in
`Claim_Fact_Check.md`, all worth knowing before the $117M pork settlement or the MCOOL vote count get
cited in any manuscript draft:

1. The $117.065M pork settlement's "preliminarily approved July 31, 2026" framing (recorded 09-17) was
   imprecise — read directly, that date is when the Court approved sending class notice, not when the
   five settlements were preliminarily approved (they were, individually, between July 2024 and May
   2026). The $117.065M total and per-company breakdown are unaffected and remain correct.
2. A previously-untracked fourth Agri Stats settlement track surfaced: a pork-specific Direct Purchaser
   Plaintiff settlement reached final approval Sept. 10, 2026 — the same day as DOJ's own civil case
   against Agri Stats. Agri Stats has now resolved four separate litigation tracks (DOJ, broiler
   End-User Consumer, pork Consumer Indirect Purchaser, pork Direct Purchaser) within about six weeks
   of each other, all on broadly similar behavioral/no-admission terms as far as directly confirmed.
3. On the 17-6 vs. 16-7 MCOOL vote-count question: the evidence now leans clearly toward 17-6 (two
   independent, detailed, contemporaneous reports with named senators) over 16-7 (one later report, no
   detail) — not certain without the committee's own record, but no longer a genuine coin-flip.

No design decisions were made or needed. No money spent. No one contacted. Nothing submitted anywhere.
