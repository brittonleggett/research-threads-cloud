# 2026-09-24 — DOJ moves to stay NAACP v. X.AI pending appeal (docket now at 127, reveals a live PI motion), Caddo Parish rejected its own moratorium resolution Aug 31, Loudoun County actually adopted its pause Sept 16

## What this is

Nightly follow-up to `2026-09-22-xai-doj-notice-of-appeal-lpsc-sept16-no-minutes-tier2-recheck.md`.
Rechecked the xAI/NAACP docket directly (moved again — four new entries since 09-22, the most
significant since the Notice of Appeal itself), rechecked LPSC for September 16 minutes/October
agenda (still nothing), did a full Louisiana Tier 1 sweep (Hyperion expansion news, Caddo Parish),
and a fresh Tier 2 pass on GA/UT/VA/AZ/Clinton County IN. Two corpus edits made tonight (both to
`Study1_Corpus_and_Coding_DRAFT_2026-08-17_national-restructure.md` — confirmed this is the live
corpus file: its header says it supersedes the 08-12 draft, and it already carries dated addenda
from 2026-09-10; the 08-12 file explicitly says "Superseded 2026-08-17" at its own top). No design/
theme/Phase-3 decisions were touched.

**Note on this file itself:** an earlier attempt tonight to write this note and make the corpus
edits appears to have been silently reverted mid-session (the corpus file briefly showed my edits,
then a re-check found it back at its original 201 lines with no trace of them, and this note file
had vanished entirely) — likely a concurrent git operation elsewhere in this multi-project repo
touching uncommitted working-tree state, not anything I did deliberately. Redid both the corpus
edits and this note a second time and verified with `grep`/`wc -l` immediately after, so what's on
disk now should be correct — but flagging this so whoever compiles the repo-wide summary/commits
tonight's work double-checks that this file and the two corpus edits below are actually present
before assuming they are.

## 1. NAACP v. X.AI Corp. (3:26-cv-00074, N.D. Miss.) — docket moved from 123 to 127; DOJ now wants the whole case frozen pending its Fifth Circuit appeal, and this surfaced a live Preliminary Injunction motion prior notes hadn't foregrounded

**Method:** re-fetched the docket directly with `curl` (browser User-Agent, docket ID 73188848 —
double-checked against the citation field per 09-22's own caution about a wrong-ID mixup). Response
headers: `x-cache: Miss from cloudfront`, `date: Thu, 24 Sep 2026 05:15:46 GMT` — live, not cached.
Parsed the saved HTML directly for every `id="entry-N"` anchor from 1 through 127 — **no gaps**,
confirming 127 is genuinely the current highest entry, not a partial render. **RECAP "Last Updated":
Sept. 23, 2026, 1:42 p.m.** — one day fresher than 09-22's reading.

**Four new entries since 09-22 (123 was the last one that note found):**

- **Entry 124 (Sept 21, 2026)** — the United States' **Motion to Stay All Proceedings Pending
  Appeal**. Downloaded and read the actual filed PDF directly (not a docket-text summary;
  `storage.courtlistener.com/recap/gov.uscourts.msnd.52261/gov.uscourts.msnd.52261.124.0_1.pdf`,
  confirmed a real 2-page PDF). Signed by **Stanley E. Woodward, Jr., Associate Attorney General**
  — a more senior DOJ signatory than Andrew Darlington, who signed the Notice of Appeal and every
  prior DOJ filing this project has logged. Quoted directly: *"The United States moves to stay all
  proceedings in this case while the Fifth Circuit addresses the critical issue of the United
  States' involvement in this case... Staying the case will avoid irreparable harm to national
  security and infringement of the United States' exclusive authority to enforce federal law...
  Given the upcoming preliminary injunction hearing and all additional reasons and arguments
  contained in the separately filed memorandum in support of this motion, the United States moves
  to stay all proceedings pending appeal and requests entry of a written order by September 28.
  Plaintiffs oppose this motion. Defendants consent to this motion."*
- **Entry 125 (Sept 21, 2026)** — a 16-page Memorandum in Support (downloaded, read directly;
  table of contents confirms it argues (I) inherent discretion to stay, (II) the four-factor stay-
  pending-appeal standard — likelihood of success, irreparable harm, balance of harms/public
  interest).
- **Entry 126 (Sept 22, 2026)** — Defendants' (X.AI Corp. and MZX Tech LLC) **Response in Support**
  of DOJ's stay motion — they agree with the government and ask the court to grant the stay,
  "in particular... refrain from scheduling a preliminary injunction hearing, pending the United
  States' appeal."
- **Entry 127 (Sept 22, 2026)** — Defendants' 9-page memorandum supporting that response, arguing
  the stay avoids wasted effort if the Fifth Circuit later says DOJ should have been allowed to
  intervene, and reiterating the national-security framing.

**Why this matters beyond "more filings": it surfaces a live, fully-briefed Preliminary Injunction
motion (docket #51, filed 2026-06-12) that none of this project's prior notes had put front and
center.** Tracing the docket's own PI-motion thread (entries 20, 51, and the briefing around them):
NAACP/Mississippi NAACP filed an original PI motion (#20, May 6, 2026), which the court denied
without prejudice June 12 while granting leave to amend; a renewed PI motion (#51) followed the same
day and was fully briefed by mid-July 2026 (opposition and reply memoranda, entries 60-96). An
evidentiary hearing on it was originally noticed for **August 24, 2026, 9:30 AM** — the same date
and courtroom as the "Telephonic Status Conference" (entry 114) that prior notes have treated as
just the DOJ-intervention ruling. **The docket does not show a separate "evidentiary hearing held"
entry**, so it's unclear from the docket text alone whether that Aug 24 conference resolved,
absorbed, or simply didn't reach the PI evidentiary hearing — DOJ's Sept 21 motion calling it "the
upcoming preliminary injunction hearing" strongly implies it has **not** yet happened and no new
date is visible anywhere in entries 113-127. **Flagging this precisely as an open item, not
resolving it by inference:** whoever next checks this docket should specifically look for (a) a
ruling on the stay motion (DOJ asked for one by Sept 28 — four days out) and (b) any new PI-hearing
notice.

**Procedural alignment worth noting for the manuscript's federal-preemption theme:** plaintiffs
(NAACP) **oppose** the stay — they want the case, including the PI motion, to keep moving.
Defendants (xAI/MZX) **consent** to it, aligning procedurally with DOJ even though DOJ is not
(yet) a party — reinforcing the existing corpus note that this case pits the civil-rights
plaintiffs against an unusual federal-government/corporate-defendant alignment.

**Fifth Circuit docket number: not found tonight.** Tried a WebSearch and a direct
`courtlistener.com` search-by-court query; the search endpoint returned `403`, and the REST API
returned `401`/`429` (daily rate limit already exhausted — "125/day" cap hit, likely shared across
sessions using this project's tooling). Bloomberg Law (news, paywalled beyond the lede, fetched
2026-09-21 dateline) independently corroborates the Sept 18 Notice of Appeal but doesn't give a
Fifth Circuit case number either. **Open item for a future pass** once the API quota resets.

## 2. LPSC Docket U-37882 — still no September 16 minutes/transcript, still no October 22 agenda

Re-tested the same filename patterns as 09-22 (`Sept_16_2026_Minutes.pdf`,
`Sept_16_2026_Minutes_revised.pdf`, `Sept_16_2026_Transcript.pdf`, `September_16_2026_Minutes.pdf`
in `/docs/minutes/` and `/docs/transcripts/`) — **all 404, eight days out now.** Also re-tested two
October-agenda filename guesses (`Oct_22_2026_Agenda.pdf`, `October_22_2026_Agenda.pdf`) —
**both 404.** No change from 09-22; still within the Commission's documented 3-5 week posting lag,
not a red flag. A WebSearch specifically for September 16 LPSC minutes surfaced nothing past what
09-19/09-22 already found (only February and April 2026 minutes indexed).

## 3. Tier 1 (Louisiana) deep-dive

**a) Caddo Parish Commission rejected a data-center pause resolution 6-4 on August 31, 2026 —
genuinely new, added to the corpus.** This directly continues the storyline the 2026-08-15 note's
artifact #16 opened ("Caddo Parish commissioners push (and fail to pass) transparency/
environmental-study measures for Blanchard site, Jun-Aug 2026") — tonight found the actual outcome
and a follow-up.

- **The vote:** direct-fetched KSLA (published Sept. 14, 2026, 10:17 PM CDT, covering an Aug. 31
  event — an unusual ~2-week reporting lag for local TV, but internally consistent with a second,
  independent source below). Quoting the article's own transcription of the meeting audio: *"That
  motion does not advance, 4 in support and 6 in opposition and 2 absent."* The resolution "sought
  to ask the Planning and Zoning Commission to consider pausing data center construction" — i.e.,
  procedurally one step short of an actual moratorium (a request that P&Z study one), consistent
  with Caddo's unincorporated areas having no zoning at all (confirmed independently by an earlier
  WebSearch summary of the parish attorney's public comments: a real moratorium would need a master
  plan, not a resolution).
- **The sponsor:** direct-fetched a second, independent article — Shreveport-Bossier Advocate
  (published Sept. 8, 2026, about parish Planning & Zoning Chairman Jake Brown's Sept. 8 proposal
  for alternative tools) — which identifies the sponsor in passing: *"Commissioner John-Paul Young
  previously proposed a moratorium plan on August 31, which fellow commissioners rejected."*
  Cross-referenced against a WebSearch summary of a separate ktalnews.com piece describing "District
  4 Commissioner John-Paul Young has a resolution to declare a two-year moratorium on new data
  center development in unincorporated parts of Caddo Parish" — consistent naming and district,
  though that ktalnews article itself could not be direct-fetched tonight (403 Forbidden). **One
  live ambiguity, flagged rather than resolved:** the same ktalnews summary also names Commissioner
  Ken Epperson's separate resolution (requiring environmental-impact studies from developers); the
  Aug. 31 vote tally (6-4) is confirmed to be on "a resolution" tied to pausing construction, which
  reads as Young's, but I could not directly confirm from a fetched primary source whether Epperson's
  resolution was voted on the same day, separately, or is still pending. Do not assume both failed
  together without further sourcing.
- **The follow-up (Sept 8, 2026):** the same Shreveport-Bossier Advocate piece (direct-fetched)
  quotes Planning & Zoning Chairman Jake Brown pivoting to Caddo's **police power** (ordinances)
  rather than comprehensive zoning, since the failed resolution route is closed off for now: expand
  nuisance ordinances to cover "excessive heat, noise and the emissions data centers can create,"
  halt tax-incentive packages for data centers, and have an environmental committee run footprint/
  noise studies to slow development. Direct quote: *"Y'all have got tools that you can use to try
  to combat this."* Brown separately described data centers as "colossal concrete monoliths that
  permanently erase wildlife habitat and completely alter the local microclimate."
- **Added to the corpus** as Tier 1 row `16b` in `Study1_Corpus_and_Coding_DRAFT_2026-08-17_
  national-restructure.md` (see that file for the exact row and provisional codes: `regulatory-void`
  extension, a second `formal-opposition-institutional-loss` instance, and a new candidate code
  `venue-adaptation-after-defeat` for Phase 3 to weigh in on). **Not Phase-1 coded line-by-line** —
  flagged the same as the rest of Tier 1 for a real coding pass.

**b) Meta's Hyperion expansion to 5 GW / $50B+ — found, not added to the corpus, flagged as
context.** WebFetched Yahoo Finance directly (article published **2026-07-27**, not previously
logged in this project's `notes/` per a `grep -rli "5 gigawatt\|5GW"` check — zero hits before
tonight): Meta's Hyperion campus is expanding to **5 gigawatts of IT capacity at a cost exceeding
$50 billion**, more than double the original $27B/2GW plan; "on track to hit 2 gigawatts by 2030,"
no date given for full 5GW. The article's own framing is celebratory, not opposition-coded: $1.6B+
in local contracts, $5M in community-college scholarships, teacher bonuses up to $50,000, a
governor's press event. **This is two months old and purely a self-reported/economic-benefit
story, not an opposition artifact** — it fits Theme 5 (ambivalent economic-opportunity framing,
the corpus's existing counter-current) if anything, not a new opposition theme. Not added as a
corpus row tonight; flagging it here as a lead for whoever next touches Theme 5, per the same
practice prior notes used for the Blue Owl financing lead.

## 4. Tier 2 recheck — Georgia, Utah, Virginia, Arizona, Clinton County (IN)

- **Georgia (Bockrath v. Coweta County, "Project Sail"):** fresh WebSearch for a September 2026
  ruling — nothing found; case still appears pending. **One correction worth logging:** a search
  hit for a "Coweta data center hearing to resume Sept. 11 at fairgrounds" article looked, out of
  context, like new September 2026 activity. Direct-fetched it and checked its actual byline date
  and content against a second search — **it is from August 2025**, part of the county's general
  data-center-ordinance drafting process (which concluded with a Dec. 2025, 4-1 commission vote
  passing the ordinance) and is unrelated to the Bockrath lawsuit against the already-approved
  Project Sail rezoning (approved 3-2 in April 2026, sued over in May 2026). **No change from
  09-19/09-22's "still pending, no ruling" framing** — this is a corrected non-finding, not new
  information.
- **Utah (Bar H Ranch / Stratos):** fresh WebSearch for a refiling of the withdrawn water-rights
  applications (withdrawn May 5-7 and May 27, 2026). No refiling found tonight. **No change.**
- **Virginia — genuinely new, added to the corpus.** Loudoun County's Board of Supervisors, which
  the existing corpus row #23 had only as "considering" a pause (per a July 24, 2026 article), **
  actually voted 7-1-1 on September 16, 2026 to adopt a 12-month pause on new data center
  applications** (not existing/pending ones). Direct-fetched WJLA: Chair Phyllis Randall and 6
  others voted yes; Supervisor Kristen Umstattd (Leesburg) voted no; Supervisor Caleb Kershner
  (Catoctin) abstained. County attorney reportedly advised that an indefinite moratorium would
  invite legal challenge but a temporary 12-month pause would be defensible. A final resolution
  vote is expected in October 2026 — **not yet a permanent policy**, worth being precise about that
  in any citation. Independently corroborated by a Bloomberg headline ("Virginia's Data Center
  Alley Moves to Pause New Applications," Sept. 16, 2026) surfaced in the same search, though
  Bloomberg's own article body wasn't fetched (paywall). **Updated corpus row #23** with the vote
  detail and both new sources.
- **Arizona:** fresh WebSearch for anything past Sept 9 (Gov. Hobbs rejecting AG Mayes' moratorium
  call, already logged). Nothing dated after Sept 9 found. **No change**, consistent with 09-22.
- **Clinton County, IN:** fresh WebSearch. One result (KNS Radio, "Clinton County To Weigh Data
  Center Rezoning At September 2 Meeting") looked like it could be new September activity — checked
  against the 09-17 note, which already traced this exact article to the **2025** Area Plan
  Commission hearing (part of the pre-2026 "Data One" backstory, not a new 2026 filing). **No
  change** — re-confirming the 09-17 note's resolution rather than re-discovering it as new.

## For Britton — plain summary

- **The xAI/NAACP case had its most consequential week yet.** After the DOJ's Sept 18 Notice of
  Appeal (found 09-22), it followed up Sept 21 with a motion — signed by a more senior DOJ official
  than before — asking the district court to freeze the *entire* case, including a fully-briefed
  Preliminary Injunction motion that turns out to have been sitting live and largely un-highlighted
  in this project's prior notes, while the Fifth Circuit sorts out whether DOJ can intervene. xAI
  and its co-defendant MZX Tech back the stay; NAACP opposes it. DOJ asked for a ruling by
  September 28 — worth checking back on specifically. No Fifth Circuit docket number found yet
  (that court's own docket wasn't searchable tonight — CourtListener's API hit a daily rate limit).
- **LPSC's September 16 minutes are still not posted** (8 days out) and **no October 22 agenda
  either** — both expected given this Commission's documented lag, not a red flag.
- **Real, verified new Louisiana material for the corpus:** Caddo Parish's commission voted 6-4 on
  Aug. 31 to reject a resolution (sponsored by Commissioner John-Paul Young) that would have asked
  Planning & Zoning to consider pausing data center construction — and by Sept. 8, the parish's
  zoning chairman was already pivoting to ordinance-based tools (nuisance rules, pulling tax
  incentives, environmental studies) since Caddo has no zoning in its unincorporated areas at all.
  Added to the corpus as a continuation of the existing Caddo storyline. One loose end: couldn't
  fully confirm whether a second Caddo resolution (Commissioner Epperson's, on environmental-impact
  studies) failed the same day or is still separately pending.
- **Virginia's Loudoun County actually adopted its data-center pause** (7-1-1, Sept. 16) rather
  than just considering it, as the existing corpus row said — updated that row. It's a 12-month
  pause on *new* applications only, not yet final (October vote still to come).
- **Georgia, Utah, Arizona, Clinton County (IN): no real change**, though I corrected one Georgia
  search result that looked like September 2026 news but was actually from August 2025.
- **Meta's Hyperion expansion to 5GW/$50B+** (July 2026, not previously logged here) is a real,
  well-sourced economic-benefit counter-narrative worth knowing about for the Theme 5 discussion,
  but it's not an opposition artifact, so I didn't add it as a corpus row — flagging it here instead.
- **Corpus changed tonight:** one new Tier 1 row (`16b`, Caddo Parish) added; one existing Tier 2
  row (`23`, Loudoun County) updated in place — both in
  `Study1_Corpus_and_Coding_DRAFT_2026-08-17_national-restructure.md`. Net row-count change: +1
  (28 → 29 numbered Tier 1 + Tier 2 entries, though Tier 1's own count was already scattered across
  two documents before tonight — not something I tried to consolidate).
- No design/theme/Phase-3 decisions were made or attempted tonight — this is verification and
  primary-source work only, consistent with the locked multi-state design.
- Per this task's instructions, no git commit/push was made — the orchestrating session handles
  that.
