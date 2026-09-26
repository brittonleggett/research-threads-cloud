# 2026-09-26 — No ruling yet on DOJ's stay motion (deadline is Sept 28, still 2 days out); PI evidentiary hearing confirmed never held; Fifth Circuit docket still not found; Caddo's Epperson resolution mystery resolved via primary-source minutes (it wasn't voted down — it appears to have fallen through committee); Loudoun's final vote now dated to Oct 20

## What this is

Direct follow-up to the five open items flagged in `2026-09-24-naacp-xai-stay-motion-caddo-moratorium-vote-loudoun-pause-adopted.md`, plus a general Tier 2 litigation/regulatory recheck (GA/UT/VA/AZ/Clinton County IN) and a brief literature-gap scan. No design/theme/Phase-3 decisions touched. Two corpus edits made (both to
`Study1_Corpus_and_Coding_DRAFT_2026-08-17_national-restructure.md`, rows 16b and 23) — see below.

**AI involvement disclosure:** this note, the docket/document reads, and the corpus edits were produced by an AI agent (Claude) doing autonomous overnight research; all litigation and regulatory claims below are sourced to primary documents (court dockets, filed PDFs, official parish minutes) or named news outlets, direct-fetched or WebFetched tonight, with URLs given so Britton can re-verify independently.

## 1. NAACP v. X.AI Corp. (3:26-cv-00074, N.D. Miss.) — no ruling yet on the stay motion; docket still tops out at entry 127

**Method:** direct-fetched the CourtListener docket with `curl` (browser User-Agent) at both
`?page=1` and `?page=2` (this docket is long enough to paginate at 92 entries/page — worth noting for
future rechecks, since a single-page fetch will silently miss entries beyond 92). Response headers
confirmed a live, uncached fetch (`x-cache: Miss from cloudfront`, `date: Sat, 26 Sep 2026 05:14:37 GMT`).
Parsed every `id="entry-N"` anchor across both pages: entries run 1 through **127 with no gaps and no
entry 128** — i.e., **no new docket activity since the 09-24 note's own read of entry 127** (the "Last
Updated" metadata ticked forward from Sept 23 1:42pm to **Sept 25, 2:08pm**, but that field can update
from a bare PACER re-scrape with no new filing text, and today's fetch confirms there is, in fact, no new
entry — the page-2 "next" pagination control is disabled, confirming 127 is genuinely the last entry).

**Direct answer to the flagged question: the United States asked for a ruling on its Motion to Stay
(entry 124, filed Sept 21) by September 28, 2026. As of this fetch (2026-09-26, docket current through
entry 127), no ruling has been entered.** This is a genuine "not yet" — today is Sept 26, two days before
the requested deadline, so absence of a ruling is not itself notable yet. Whoever checks next should
specifically look for entry 128 (or later) being an order on the stay motion, expected on or shortly after
Sept 28.

**Docket:** [courtlistener.com/docket/73188848](https://www.courtlistener.com/docket/73188848/national-association-for-the-advancement-of-colored-people-v-xai-corp/)

## 2. PI evidentiary hearing (docket #51) — confirmed via the docket's own text: it was continued indefinitely and never rescheduled

This resolves the open item from 09-24 (which had inferred, but not confirmed, that the hearing hadn't
happened). Tracing the docket entries directly:

- **Entry 42** (May 26, 2026): notice of an evidentiary hearing on the **original** PI motion (#20), set for
  Aug. 24, 2026, 9:30 AM.
- **Entry 50** (June 12, 2026): the original PI motion (#20) is **denied without prejudice**, with leave to
  amend; entry 51 (same day) is the renewed/amended PI motion that all recent notes have been tracking.
- **Entry 112** (Aug. 21, 2026) — three days before the scheduled date — explicit docket text: *"NOTICE
  Continuing EVIDENTIARY Hearing re 42 Notice of Hearing on Motion. Evidentiary Motion Hearing set
  for 8/24/2026 continued until further notice."* This is the Aug. 24 hearing being formally postponed
  sine die, tied back to entry 42's own notice.
- **Entry 114** (Aug. 24, 2026) is a separate "Telephonic Status Conference," not an evidentiary hearing —
  confirmed distinct from the continued hearing by the docket text itself, not just by inference.
- Searching every entry's text for "evidentiary" or "hearing" across the full 127-entry docket turns up
  **no subsequent notice of a new evidentiary-hearing date** for the renewed PI motion (#51) anywhere
  through entry 127 (Sept 22, 2026) — consistent with DOJ's Sept 21 stay motion (entry 124) calling it
  "the upcoming preliminary injunction hearing," present tense, not yet held.

**Conclusion, stated plainly: the PI evidentiary hearing has not happened.** It was continued from its
original Aug. 24 date and no new date has been docketed as of Sept. 26, 2026.

## 3. Fifth Circuit docket number — still not found tonight, tried four independent methods

- CourtListener's search UI, scoped `court=ca5`, tried five query variants (`"National Association for the
  Advancement of Colored People" X.AI`, `"X.AI Corp"`, `"3:26-cv-00074"`, `xAI MZX`, `"United States of
  America" X.AI`) — the two exact-phrase/docket-number queries returned **0 results**; the two
  broader-term queries returned results, but every one inspected was an unrelated case (a different,
  older "NAACP v. ..." matter from 2021, an SEC case, a Chamber of Commerce/FCC petition, unrelated
  criminal appeals) — no false-positive treated as a match.
- CourtListener's REST API without authentication returned `401` (not the `429` rate-limit hit on 09-24 —
  a different, harder blocker: this session has no API credentials, so the quota resetting doesn't help).
- Justia's docket page for the district case 403'd on direct `curl`.
- WebSearch (two queries) surfaced Bloomberg Law, Mealey's, and a Steve Vladeck newsletter post all
  discussing the Sept. 18 Notice of Appeal — **none give a Fifth Circuit case number**; Vladeck's post is
  dated June 22, 2026 (pre-appeal) and is about the underlying intervention dispute generally, not this
  specific appeal.

**Still an open item, genuinely unresolved** — likely because the Fifth Circuit docket hasn't yet been
scraped into RECAP (which requires someone to pull it via PACER first), not because it doesn't exist.

## 4. LPSC Docket U-37882 — September 16 minutes still not posted (10 days out); October 22 agenda not posted; no red flag

- Corrected the base URL this time (`http://www.lpsc.louisiana.gov/...` 307-redirects; the live site is
  `https://lpsc.louisiana.gov/...`, no `www`) — retested `September_16_2026_Minutes.pdf` and
  `Sept_16_2026_Minutes.pdf` directly under `/docs/minutes/`: both **404**. As a sanity check, the known-
  good `August_12_2026_Minutes.pdf` at the same path returned **200** — confirms the fetch method
  works and August 12 genuinely is still the most recent posted minutes file.
- WebFetched the Commission's own `/Agenda` page directly: confirms **September 16, 2026** had a
  posted (revised) agenda back on 9/8/2026, and confirms an **October 22, 2026** meeting is scheduled
  (location: Louisiana Supreme Court building, New Orleans) — but no agenda link posted for it yet, and
  no mention of docket U-37882 on that page. Consistent with prior nights: **no change**, still within the
  documented 3-5 week posting lag.

## 5. Caddo Parish's Epperson resolution — resolved via the parish's own official minutes (primary source), not inferred

This was the corpus-ambiguity item flagged 09-24. Went past secondary news coverage entirely this time
and pulled the Caddo Parish Commission Clerk's own minutes archive directly:

**Method:** `caddo.gov/commission-clerks-office/minutes/` renders its minutes tables via an AJAX call
(WordPress Ninja Tables plugin) that isn't in the static HTML — found the underlying endpoint
(`caddo.gov/wp-admin/admin-ajax.php?action=wp_ajax_ninja_tables_public_action&table_id=...`) and
queried all three of the site's minutes tables (Work Session: `table_id=7055`; Regular/Special Session:
`6340`; Committee: `7056`) directly for JSON data. This surfaced a direct link to the **official PDF minutes
of the Aug. 31, 2026 Work Session** (`caddo.gov/wp-content/uploads/2026/09/2026-8-31-Work-Session-
Minutes.pdf`), which I downloaded and read in full.

**What the minutes actually say (this is the primary source — supersedes all secondary-news framing
used in the 09-24 note):**

- **Commissioner Ken Epperson was marked ABSENT from the entire Aug. 31 meeting**, along with
  Commissioner Gage-Watts (10 of 12 commissioners present).
- The New Business section that day took up exactly three items: Ordinance No. 6641 (a street
  abandonment, unrelated), **"Resolution No. 52 of 2026"** — which, as read into the record that day, is
  **a resolution to approve the assignment/conveyance of unrelated State Agency Leases (Nos. 20126,
  20381, 22023)** — and **Resolution No. 53 of 2026** (Commissioner J. Young's data-center-moratorium
  request to Planning & Zoning), which failed on a roll-call vote: **AYES: Burrell, Cothran, Kracman, J.
  Young (4); NAYS: Atkins, Blake, Jones, Lazarus, Thomas, G. Young (6); ABSENT: Epperson, Gage-Watts
  (2)** — matching KSLA's reported 6-4/2-absent tally exactly.
- **The resolution numbers were reassigned/reused between mid-August and Aug. 31.** Epperson's
  environmental-impact-study resolution had been introduced under the number "Resolution 52" at the
  Aug. 17 work session (confirmed via the parish's own Aug. 17 agenda) and sent, along with Young's
  measure, to the **Special Projects Committee on Aug. 19** (an 11-0 referral vote, after an 8-3 vote
  against sending both straight to a floor vote — confirmed via a Center Square/Brushwood Media
  Network article, byline Misty Castile, pub. Aug. 19, quoting Parish Attorney Donna Frazier's warning
  that a moratorium "cannot be enacted via resolution"). By Aug. 31, the parish's own numbering had
  moved on to an unrelated item also called "Resolution 52" — ordinary sequential renumbering, not a
  cover-up, but exactly the kind of numbering coincidence that produced the ambiguity in the first place.
- **Checked the parish's own Committee-minutes table for any Special Projects Committee meeting
  between Aug. 19 and Sept. 26 that might have taken up Epperson's item: none is listed** (the most
  recent Special Projects Committee minutes on file are from July 9, 2026, before the Aug. 19 referral).
  Also checked the one committee meeting that did occur in this window (Aug. 20 Joint Appropriations
  & Economic Development Committee) directly — it covered an unrelated NGO-funding matter
  (BirthWell Shreveport) with no data-center content at all.

**Best-supported conclusion: Epperson's environmental-impact-study resolution was not voted down
alongside Young's on Aug. 31 — it appears to still be sitting in (or having fallen through) the Special
Projects Committee, unaddressed, with its sponsor not even present that day.** This is a materially
different fact pattern from "both resolutions failed together," and the corpus row has been corrected
accordingly (see below). I could not find any primary source (parish minutes or otherwise) showing this
resolution being formally taken up, voted, or withdrawn at any point after Aug. 19 — if Britton wants this
tracked further, the next check should be the Special Projects Committee's minutes table for any
meeting posted after tonight.

**Corpus edit:** row 16b in `Study1_Corpus_and_Coding_DRAFT_2026-08-17_national-restructure.md`
rewritten in place with the above, keeping all original citations and adding the primary-source PDF link
and the Aug. 19 committee-referral source. Flagging for Phase 3: this "resolution never resolved, just
stalled procedurally" pattern may be worth its own note alongside the existing `venue-adaptation-after-
defeat` candidate code — it's a different mechanism (institutional inertia/non-action, not a floor defeat).

## 6. Tier 2 general recheck — Georgia, Utah, Virginia, Arizona, Clinton County (IN)

- **Georgia (Bockrath v. Coweta County):** fresh WebSearch, no September ruling found — case appears
  to still be pending at the Coweta County Superior Court level (filed May 2026). **No change** from
  09-24's "still pending" read; did not find a hearing date.
- **Utah (Bar H Ranch / Stratos):** fresh WebSearch, no refiling of the withdrawn water-rights
  applications found. **No change.**
- **Virginia (Loudoun County) — new, precise detail added.** The Sept. 16 vote was 7-1-1 to *advance* a
  12-month-pause proposal (direct staff to draft the resolution), not a final adoption — this matches the
  09-24 note's framing, but tonight found via WTOP that the **final vote is specifically scheduled for the
  Board's October 20, 2026 business meeting** (previously logged only as "October 2026"). Corpus row
  23 updated with this date and the WTOP source.
- **Arizona:** fresh WebSearch for anything past Sept 9 (Gov. Hobbs declining AG Mayes' statewide-
  moratorium call) — nothing dated later found. **No change**, consistent with 09-22/09-24.
- **Clinton County, IN:** fresh WebSearch — all results trace back to the original January 2026
  rezoning-denial (already fully logged in this project's notes). **No change.**

## 7. Light literature-gap scan

One new, verifiable, directly relevant lead: **"The AI Factory: Data Centers, Power, and Resistance in
Late Industrial Pennsylvania"** — a 78-page report from the nonprofit research institute **Data & Society**,
released **Sept. 21, 2026**, based on 18 months of ethnographic fieldwork (Nov. 2024-Apr. 2026) and
interviews with 44 Pennsylvanians across seven participant categories (experts, activists/organizers,
labor, policymakers, institutional leaders, archivists, residents). Covered by TechCrunch, Spotlight PA,
and Bucks County Beacon (all pub. Sept. 2026). Direct link, confirmed live via `curl` (HTTP 200) tonight:
[datasociety.net/research-library/the-ai-factory-...](https://datasociety.net/research-library/the-ai-factory-data-centers-power-and-resistance-in-late-industrial-pennsylvania/).

**This is a nonprofit research-institute report, not a peer-reviewed journal article — it has no DOI, so it
is not Crossref-verifiable in the usual sense; its "verification" here is the direct, live URL plus three
independent news outlets' coverage of the same release date.** Its key finding — that opposition is
"post-partisan" and driven partly by "industrial trauma" from PA's coal/oil/steel/fracking history plus
distrust of secretive industry tactics (NDAs with local officials) — is thematically close to this paper's
own framing and may be worth a citation/discussion-section mention, but that's Britton's call, not
something I added to the corpus or theme material. Not added anywhere except this note.

Did not have time for a deeper systematic lit search beyond this one lead — the litigation recheck (items
1-6) took priority per tonight's task framing.

## For Britton — plain summary

- **No ruling yet on DOJ's motion to stay the entire NAACP v. X.AI case.** DOJ asked for one by Sept 28;
  today is Sept 26, so this is genuinely just "not yet," confirmed by direct-fetching the live docket (127
  entries, no new activity since 09-24, page-2 pagination checked so nothing was missed). Worth a
  same-week recheck around the 28th-29th.
- **The preliminary-injunction evidentiary hearing has not happened**, and this is now confirmed by the
  docket's own text rather than inferred: it was formally continued "until further notice" three days before
  its scheduled Aug. 24 date and no new date has been set since.
- **Fifth Circuit appeal docket number: still not found**, after four different lookup methods tonight (up
  from two on 09-24). Most likely explanation is that it simply isn't in CourtListener's RECAP archive yet,
  not that it doesn't exist.
- **LPSC's Sept 16 minutes: still not posted** (10 days out), no October 22 agenda either — both
  unremarkable given the Commission's documented lag.
- **The Caddo Parish ambiguity is resolved, and it changes the story a bit:** pulling the parish's actual
  meeting minutes (not just news coverage) shows Commissioner Epperson's environmental-impact-study
  resolution was never voted down alongside Commissioner Young's moratorium-request resolution — its
  sponsor wasn't even at the Aug. 31 meeting, and the resolution appears to have simply stalled in
  committee rather than being defeated. Corrected the corpus row to reflect this rather than the vaguer
  "one loose end" framing from 09-24.
- **Loudoun County's final vote on its 12-month pause is now specifically dated to Oct. 20, 2026** —
  added to the corpus.
- **Georgia, Utah, Arizona, Clinton County (IN): no material change** since 09-24.
- **One literature lead worth your attention:** a new Data & Society report on PA data-center opposition
  (ethnographic, 44 interviewees, released Sept. 21) that argues opposition is bipartisan/post-partisan and
  driven partly by regional "industrial trauma" — thematically close to this project's framing. Flagged, not
  added to any corpus or theme material — your call whether it's worth citing.
- **Corpus changed tonight:** rows 16b and 23 both edited in place in
  `Study1_Corpus_and_Coding_DRAFT_2026-08-17_national-restructure.md` — no new rows added, no
  rows removed, all original sources kept alongside the new primary-source material.
- No design/theme/Phase-3 decisions were made or attempted tonight.
