# 2026-09-27 — Still no ruling on DOJ's stay motion (deadline is tomorrow, Sept 28); Fifth Circuit docket still not found (one more attempt, still nothing); Caddo committee silence reconfirmed with one minor correction; Tier 2 states unchanged; Loudoun unchanged

## What this is

Direct follow-up to `2026-09-26-litigation-recheck.md`, re-verifying the same open items
one night later per tonight's task framing. No design/theme/Phase-3 decisions touched.
No corpus edits were needed tonight — every item checked came back "no change" from
09-26, with one small factual correction noted below (item 4) that does not affect any
corpus row's actual claims.

**AI involvement disclosure:** this note and all findings below were produced by an AI
agent (Claude) doing autonomous overnight research. All litigation/regulatory claims are
sourced to primary documents (the live CourtListener docket, an LPSC page fetch, Caddo
Parish's own committee-minutes data endpoint) or named news outlets, fetched tonight,
with URLs/methods given so Britton can re-verify independently. WebSearch summaries were
not treated as fact for any ruling/date claim without a primary-source check.

## 1. NAACP v. X.AI Corp. (3:26-cv-00074, N.D. Miss., CourtListener docket 73188848) — still no ruling; docket unchanged at 127 entries

**Method:** direct `curl` fetch (browser User-Agent) of both docket pages (`?page=1` and
`?page=2`), same method as 09-26. Response headers confirm a live, uncached fetch
(`x-cache: Miss from cloudfront`, `date: Sun, 27 Sep 2026 05:15:43 GMT`). Parsed every
`id="entry-N"` anchor across both pages programmatically: entries run **1 through 127,
no gaps, no entry 128** — confirmed by checking every integer 1-127 is present and
nothing higher exists. Page 2's pagination control shows only a "prev" link back to page
1, no "next" — confirming page 2 is genuinely the last page (nothing beyond it was
missed).

**The "Last Updated" metadata field still reads "Sept. 25, 2026, 2:08 p.m."** — identical
to what 09-26's note reported, even though today's fetch is from Sept 27. This is a
useful cross-check: it means CourtListener's own re-scrape of this docket hasn't found
anything new to update since the 25th either, consistent with (not just equal to) the
direct entry-count check.

**Direct answer: as of this fetch, no ruling has been entered on the United States'
Motion to Stay (entry 124, filed Sept 21), which asked for a ruling by September 28,
2026.** Today is Sept 27 — the deadline is tomorrow. This is still a legitimate "not
yet," not a missed deadline. Read entries 124-127 directly (the stay motion, its
supporting memorandum, X.AI/MZX's response, and their supporting memorandum) to confirm
none of them is itself the order — they are not; the most recent entry (127, Sept 22) is
X.AI/MZX's memorandum in support of their response to the stay motion. **Whoever checks
next should watch specifically for entry 128 or later being the actual order, expected
on or shortly after Sept 28.**

**Docket:** [courtlistener.com/docket/73188848](https://www.courtlistener.com/docket/73188848/national-association-for-the-advancement-of-colored-people-v-xai-corp/)

## 2. Fifth Circuit appeal docket number — one more attempt made tonight, still not found

Per tonight's task framing ("one more attempt is fine, don't burn excessive time"), tried
one additional method beyond the four already exhausted on 09-26: a CourtListener search
scoped `court=ca5` with a `q=` query for `"NAACP" "X.AI"` — returned **0 Results** twice
over (the search page renders two separate "0 Results" result panels). Also re-checked
whether the *district* docket's own page mentions a Fifth Circuit case/appeal number
anywhere in its text (sometimes a district docket cross-references its own appeal) — a
case-insensitive search of both fetched docket pages for "fifth circuit," "USCA," "court
of appeals," or "appeal no" turned up **nothing**.

**Stopping here per the task's own guidance** — this is a fifth failed method
(WebSearch also independently returned no Fifth Circuit case number tonight, consistent
with 09-26). Still most likely a RECAP scraping lag (the Fifth Circuit docket needs
someone to pull it via PACER before it shows up on CourtListener) rather than the appeal
not existing — the district docket's own Notice of Appeal entry (from prior nights'
notes) is not in question, just its resulting appellate docket number. Not spending
further time on this specific dead end tonight.

## 3. LPSC Docket U-37882 — September 16 minutes still not posted; October 22 agenda still not posted — no change

- Re-tested both `September_16_2026_Minutes.pdf` and `Sept_16_2026_Minutes.pdf` under
  `https://lpsc.louisiana.gov/docs/minutes/`: both **404** tonight. Sanity check against
  the known-good `August_12_2026_Minutes.pdf` at the same path: **200** — confirms the
  fetch method still works and August 12 is still the most recent posted minutes file.
  It has now been 11 days since the Sept. 16 meeting with no minutes posted, still within
  the documented 3-5 week posting lag.
- WebFetched the Commission's own `/Agenda` page directly tonight: confirms September 16,
  2026 shows "Agenda posted (revised 9/8/2026)" and October 22, 2026 (New Orleans) is
  listed as a scheduled date with **no agenda link posted yet**. No mention of docket
  U-37882 anywhere on the page. **No change** from 09-26.

## 4. Caddo Parish's Epperson resolution — reconfirmed no committee action since the Aug. 19 referral, with one small correction to 09-26's account

Re-queried the parish's Ninja Tables AJAX data endpoint directly
(`caddo.gov/wp-admin/admin-ajax.php`, `table_id=7056` for the Committee-minutes table) —
this returns the full underlying JSON dataset rather than the rendered page, so it's not
subject to pagination/rendering gaps. Pulled and inspected all 245 rows.

**Correction to 09-26's note:** that note stated "the most recent Special Projects
Committee minutes on file are from July 9, 2026, before the Aug. 19 referral." This
undercounted by one meeting — the full dataset actually shows an **August 3, 2026
Special Projects Committee meeting** (with posted agenda, minutes PDF, and video link:
`caddo.gov/wp-content/uploads/2026/08/8.3.2026-Special-Projects-Committee-Minutes.pdf`)
between the July 9 and Aug 19 dates. **This does not change any substantive conclusion**
— August 3 still predates the Aug. 19 committee referral of Epperson's resolution, so it
could not have addressed an item that hadn't been referred yet. Did not download/read
this Aug. 3 minutes PDF (not relevant to Epperson's item), just confirming its existence
for the record and to correct the prior night's slightly imprecise framing.

**The substantive finding is unchanged and now double-confirmed by two different fetch
methods across two nights:** filtering the full 245-row dataset for every 2026 committee
meeting of any kind shows **nothing dated after August 20, 2026** (the Joint
Appropriations & Economic Development Committee meeting already checked and ruled
irrelevant on 09-26) — no September or October 2026 entries anywhere in the table, for
any committee. **Epperson's environmental-impact-study resolution has still not received
any committee hearing** as of tonight; it remains, as of the parish's own posted minutes
data, sitting unaddressed since the Aug. 19 Special Projects Committee referral.

## 5. Tier 2 general recheck — Georgia, Utah, Virginia (Loudoun), Arizona, Clinton County (IN)

All five checked via fresh WebSearch tonight (WebSearch summaries only, not treated as
fact where any ruling/date claim was at stake — none of tonight's searches surfaced a
new ruling or vote to verify against a primary source in the first place):

- **Georgia (Bockrath v. Coweta County):** no ruling or hearing date found past the
  May 2026 filing; case appears to remain pending at Coweta County Superior Court.
  **No change** from 09-24/09-26.
- **Utah (Bar H Ranch / Stratos):** no refiling of the withdrawn water-rights
  applications found; coverage found tonight (CSMonitor Sept 1 piece) is consistent
  with, not newer than, what was already logged. **No change.**
- **Virginia (Loudoun County):** confirmed via fresh search (WTOP among sources) that
  the Sept. 16 vote (7-1-1, advancing a resolution) and the Oct. 20, 2026 final-vote date
  are exactly as logged in the corpus already — no new information. Per the task's own
  framing this is low priority until closer to Oct. 20. **No change.**
- **Arizona:** no dated-later-than-Sept-9 development found on the Hobbs/Mayes
  moratorium dispute. **No change.**
- **Clinton County, IN:** all results still trace to the original January 20, 2026
  rezoning denial already fully logged. **No change.**

## 6. Grey-literature lead (Data & Society PA report) — not independently re-verified tonight, no new information

The Sept. 21, 2026 Data & Society ethnographic report on Pennsylvania data-center
opposition ("The AI Factory...") flagged in the 09-26 note was not re-checked tonight
beyond confirming it's still the same, already-verified lead — no new reading or
re-verification work was done on it, since tonight's task priority was the litigation
recheck. It remains flagged for Britton's citation call, not added to any corpus or
theme material. If useful for the Tier 2 transferability discussion, a proper read
(not just the abstract-level confirmation from 09-26) is still an open task for a future
night, time permitting.

## Corpus/tracker files — no edits made tonight

`Study1_Corpus_and_Coding_DRAFT_2026-08-17_national-restructure.md` was read and checked
against tonight's findings; every relevant row (16b, 21-27) already reflects the current,
verified state as of 09-26 and needed no update tonight. No new rows added, none removed.

## For Britton — plain summary

- **Still no ruling on DOJ's motion to stay the entire NAACP v. X.AI case.** Deadline
  DOJ asked for is tomorrow, Sept 28. Confirmed via a fresh, live docket fetch tonight
  (127 entries, unchanged from yesterday, both pages checked so nothing was missed).
  Worth checking again in the next day or two — this is the single most likely thing to
  move soon.
- **Fifth Circuit appeal docket number: still not found**, after a fifth lookup method
  tonight. Per the task framing, not spending more time on this specific dead end unless
  you want it pursued differently (e.g., a PACER account, which this session doesn't
  have).
- **LPSC's Sept 16 minutes and Oct 22 agenda: still not posted** — both unremarkable
  given the Commission's documented lag.
- **Caddo's Epperson resolution: still sitting unaddressed in committee**, now confirmed
  via a second, independent pull of the parish's full committee-minutes dataset (245
  rows, no committee meeting of any kind after Aug 20, 2026). One small correction to
  09-26's note: there was actually an Aug 3 Special Projects Committee meeting (missed
  in that note's phrasing), but it predates the Aug 19 referral, so it doesn't change
  anything about whether the resolution's been heard.
- **Loudoun, Georgia, Utah, Arizona, Clinton County (IN): no material change** since
  09-24/09-26.
- **Data & Society PA report:** still just flagged, not re-verified further tonight —
  a full read is still open if you want it for the Tier 2 discussion.
- **No corpus edits were needed tonight** — everything checked came back confirming the
  existing corpus text rather than requiring a change.
- No design/theme/Phase-3 decisions were made or attempted tonight.
