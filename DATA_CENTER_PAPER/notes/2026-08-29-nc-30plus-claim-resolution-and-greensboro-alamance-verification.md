# 2026-08-29 — NC "30+ jurisdictions" claim run down; Greensboro/Alamance primary-verified; Durham date resolved

Follow-up to `2026-08-27-naacp-hearing-update-nc-ky-moratorium-wave.md` and
`2026-08-28-nc-ky-direct-fetch-verification.md`. Continues the verification pass on the NC/KY
moratorium wave. Corpus restructuring/sizing and Phase 3 remain untouched, per standing rule —
this is a verification pass only, nothing added to the working corpus table. All candidate row
numbers/dates below are proposed corrections to the existing draft table in the 08-27 note, not
edits to that file and not insertions into the locked corpus.

## WebFetch status — working tonight
Tested against `en.wikipedia.org/wiki/Data_center` (standing control): succeeded, correct
one-sentence summary returned. Used WebFetch as primary tool throughout this session — most
findings below are direct-fetch verified, not WebSearch-summary-only. Where a URL still failed
(403/404/paywall redirect), that's noted explicitly and the finding is flagged as WebSearch-level
confidence instead.

---

## 1. The "30+ NC jurisdictions" claim — traced to its origin, and it does NOT hold up as a precise number

### What I did
Directly fetched all six sources the 08-27 note cited as its "collective read" for this claim:
WUNC, WRAL, WFAE (homepage — the actual dated article wasn't linked from there, found and fetched
separately below), WHQR (homepage, same issue), indyweek (homepage, same issue), and GovTech (already
ruled out on 08-28). Then used WebSearch to find the actual originating source, and direct-fetched it.

### Result: none of the six originally-cited outlets state a statewide count when read directly
- **WUNC** (direct fetch, Durham County article): no statewide count. Confirms only the Triangle
  regional breakdown ("Status of data center moratoriums in the Triangle").
- **WRAL** (direct fetch, Durham County article): no statewide count.
- **WFAE**: the homepage doesn't surface the relevant article by default; found the actual dated
  article via WebSearch (`wfae.org/2026-08-26/durham-county-data-center-moratorium`) and direct-
  fetched it — **no statewide count**, only the Triangle-region list.
- **WHQR**: homepage direct-fetch found no relevant article at all (the WHQR version of the same
  WFAE-network story exists at a dated URL not linked from the homepage; given the WFAE original
  already ruled out a statewide count, didn't chase the WHQR mirror further — low value).
- **indyweek**: homepage direct-fetch found no relevant article; the specific indyweek piece found
  via search (`Durham County Moves Toward Data Center Moratorium`) is about Durham only, not a
  statewide tracker.
- **GovTech**: already ruled out 08-28 (Durham/City of Durham coverage only, no statewide number).

**So the specific six-source trail the 08-27 note cited does not, and never did, support the "30+"
number when any individual source is read directly — confirmed again tonight with the two sources
not yet checked (WFAE's actual article, indyweek/WHQR).**

### Where "30+" actually comes from
WebSearch for the number itself surfaced it being independently repeated by multiple outlets, so I
traced it further:

- **thecooldown.com** (direct fetch, pub. Aug 4, 2026, byline James Nanzo): "more than 30 county and
  city governments in the state have put temporary holds on new data center proposals since
  February" — and explicitly attributes it: *"As Carolina Journal reported..."* This is a
  re-publication, not an original count.
- **Carolina Journal** (direct fetch, pub. **July 31, 2026**, byline **Andrew Pomeranz**) — the
  apparent origin point: *"More than 30 North Carolina local governments have temporarily halted new
  data center development since February."* **The article cites no tracker, no law firm database, no
  advocacy-group list, no state agency, and no methodology for this count** — it presents the number
  as the outlet's own reporting, uncited. Worth flagging for source-quality purposes: Carolina Journal
  is published by the John Locke Foundation, a conservative-leaning NC think tank — that doesn't make
  the number wrong, but it means "30+" traces to a single outlet's undocumented tally, not to a
  neutral tracker or public database.
- **ncnewsline.com** (attempted direct fetch): 403 Forbidden, could not verify whether it has an
  independent count or is also repeating Carolina Journal's.
- **North State Journal** (`nsjonline.com`, attempted direct fetch): 403 Forbidden. A WebSearch
  AI-summary attributes to it the figure "at least 11 counties and 17 towns" (= 28) sourced to
  "public records, resolutions and official meetings" — this is a *more specific and more
  methodologically-described* number than Carolina Journal's, and closer to what I could
  independently reconstruct below, but **I could not read the original article myself**, so this
  stays at WebSearch-summary confidence only, not primary-verified.
- **datacenterbans.com**: direct-fetched — repeats "over 30 North Carolina jurisdictions" but the
  page's own content is explicitly labeled *"AI Overview... Generated 13 minutes ago by Claude"* and
  cites no sources for the NC-specific claims. This is a live demonstration of how the unsourced
  number is propagating through AI-generated aggregator pages, not independent corroboration.

### Independent trackers give smaller, non-matching counts
- **SAVRN Infrastructure Platform** (direct fetch, per-entry sourced, explicitly dated "as of
  August 2026 update"): lists **14** NC jurisdictions by name (7 counties: Alamance, Chatham,
  Cumberland, Davie, Orange, Surry, Watauga; 7 cities/towns: Charlotte, City of Durham, City of
  Wilson, Greensboro, Boone, Hillsborough, Waxhaw) — notably **missing** Durham County itself (only
  lists the city), Mount Airy, Yadkin, Gates, Brevard, Canton, Clay, Madison, Swain, Clyde, Apex,
  Wendell, Rowan, Kings Mountain — i.e., missing most of what WFAE's own reporting names. Clearly a
  partial/stale list, not a comprehensive one.
- **GPU Lease Index** (direct fetch, cites "county board minutes & NC news coverage" generically, no
  per-entry links): 15 confirmed active + several "pending/considering" = "20+ jurisdictions total,"
  dated April 2026 in its own header — i.e., stale by four-plus months relative to tonight, predating
  the entire Durham/Greensboro/Alamance/Mount Airy/Surry/Yadkin wave from June–August.

### My own reconstructed count from everything read tonight
Combining every distinctly-named NC jurisdiction that appeared in at least one directly-fetched
source or a WFAE-article WebSearch summary tonight (not all individually primary-verified — see
caveats below):

Gates County, Brevard, Clay County, Canton, Watauga County, Madison County, Boone, Swain County,
Clyde, Chatham County, Orange County, Apex, Wendell, Rowan County, Kings Mountain, Surry County,
Yadkin County, Durham County, City of Durham, Mount Airy, Greensboro, Alamance County, Charlotte,
Cumberland County, Davie County, City of Wilson, Town of Hillsborough, Town of Waxhaw — **28 named
jurisdictions**, in the right ballpark of "30+" but not identical to it, and most of these 28 are
NOT individually primary-source verified (they come from aggregator trackers or a WebSearch AI-
summary of WFAE's own article, not each a direct-fetched local news story).

### Bottom line for Britton
**The wave itself is real** — multiple independent, credible outlets (WFAE across many separate
dated articles, WRAL, WUNC, Carolina Public Press, NC Newsline) all independently describe a large,
ongoing, multi-region NC moratorium wave since roughly Gates County's December 2025 first-mover
action. That is not in question. **What does not hold up is "more than 30" as a precise, sourced
statewide count.** It traces to one outlet's (Carolina Journal, July 31, 2026) uncited tally, has
since propagated through re-publication and at least one AI-generated aggregator page that just
repeats it without independent verification, and none of the six sources originally cited for it
actually state the number when read directly. My own reconstruction from everything checked tonight
lands at **28 named jurisdictions**, which is close to "30+" in magnitude but built from a mix of
primary and aggregator sources, not a clean count.

**Recommendation:** if this figure is used in the manuscript, either (a) drop the precise "30+" and
describe the wave qualitatively with the individually-verified anchor examples (Durham, Greensboro,
Alamance, Louisville as the KY comparator), or (b) cite it explicitly as *"more than 30 per Carolina
Journal (July 31, 2026); methodology not disclosed by that outlet"* rather than presenting it as an
independently-confirmed fact. Do not cite "30+" as if it came from the WUNC/WRAL/WFAE/GovTech
reporting — those outlets don't say it.

---

## 2. Greensboro — now primary-source verified (previously WebSearch-only)

Prior attempts (08-28) hit 403/404 on myfox8 and greensboro-nc.gov; **retried the same URLs tonight
and got the same 403s** — this is a real, persistent bot-block on those specific hosts, not an
environment fluke (WebFetch worked fine on many other sites in the same session). Found and
direct-fetched an alternate source instead:

**greensborothread.com** (direct fetch): confirms **8-0 vote**, **180-day moratorium**, applies to
new data centers with electrical demand exceeding **10 megawatts**, Mayor Pro Tem **Denise Roth
recused** (her stated reason: her role on the Gateway Research Park board, where the "Dream Center"
data center project is planned — she says her "prior understanding was that the data center
ordinance and related moratorium would not have implications for the Dream Center"). Expanded from
an initially-proposed 120 days to 180 days after public input; residents had pushed for a much
longer window (one figure cited: 32 months) and felt 180 days was still insufficient.

**Date discrepancy found and resolved:** greensborothread.com states **"Tuesday, August 19, 2026."**
Checking the calendar: **August 19, 2026 is a Wednesday, not a Tuesday** — internally inconsistent.
August 18, 2026, by contrast, **is** a Tuesday, and matches the date given consistently elsewhere
(WFAE-network reporting, thecooldown.com's "Greensboro adopted a 180-day pause 8-0 on August 18").
**Conclusion: the actual vote date is almost certainly Tuesday, August 18, 2026** — greensborothread
appears to have a one-day date slip while keeping the correct weekday label wrong for its own stated
date. Flag this precisely if the row gets drafted: cite August 18, not August 19.

**Bonus finding — the "Council Reverses Course" thread from 08-27's note is now resolved.** Direct-
fetched **Rhino Times** (pub. Aug 6, 2026): on **July 21, 2026** the council voted **5-4 against**
pursuing a moratorium at all; on **August 3, 2026** it reversed and voted **9-0** to begin the formal
legal process (direct staff to draft an ordinance, schedule a public hearing for Aug. 17) — this
August 3 vote did not itself impose a moratorium, just started the process. The August 17 public
hearing then led to the final **8-0** vote (one fewer than the Aug. 3 procedural vote, accounting for
Roth's recusal) enacting the actual 180-day moratorium on **August 18**. This is a coherent,
well-sourced three-step narrative (reject → reverse/start process → enact), not a contradiction —
worth including if the paper wants a "contested process" angle for Greensboro specifically, since
most other NC jurisdictions in this wave appear to have gone straight to approval.

## 3. Alamance County — now primary-source verified (previously WebSearch-only)

Prior attempts (08-28) failed on the FOX8 URL; **retried tonight, same 403.** Found and direct-
fetched an alternate: **Yahoo News** (syndicated wire copy, direct fetch succeeded): *"Alamance
County commissioners voted **5-0** Monday night to approve a one-year moratorium on data center
[consideration/discussion]"* — pauses any consideration of data center proposals in the county for a
year. This **refines** the 08-27 note's "unanimous" framing with the exact tally: Alamance's board
has 5 seats, so 5-0 is unanimous, consistent with the original characterization, just now with the
precise vote count. No statewide NC count appeared in this article either (checked specifically) —
it named only neighboring-county context (Davie County's earlier one-year moratorium, Stokes
County's rejection of a six-month moratorium, Forsyth County's rejection of an AI data center
rezoning), reinforcing point 1 above.

**Date check:** the public hearing was August 17, 2026, and the vote is described as "Monday night."
August 17, 2026 **is** a Monday (verified against the calendar) — no discrepancy here, unlike
Durham and Greensboro.

## 4. Durham County vote date — resolved via the county's own government page

Found (via WebSearch, then direct-fetched) Durham County's **own official government site**:
`dconc.gov/DurhamCo-News/BOCC-Regular-Session-on-August-24-2026.htm` — an agenda announcement titled
*"BOCC Regular Session on August 24, 2026,"* confirming the meeting date as **Monday, August 24,
2026**, and listing the data center moratorium public hearing as agenda item **26-0437**: *"A Public
Hearing will be held to Consider the Adoption of a Proposed Moratorium on the Acceptance and
Processing of Applications for New or Expanded Data Centers with some exceptions with Durham
County."* This page doesn't itself state the vote tally, but it is the **primary, official source
for the meeting date**, and it resolves the WUNC (Aug 26) vs. WRAL (Aug 25) discrepancy flagged
08-28: **neither news outlet had the correct date** — the actual meeting was Monday, **August 24**,
which is genuinely a Monday (verified by calendar), unlike either Aug 25 (a Tuesday) or Aug 26 (a
Wednesday). WUNC was off by two days, WRAL by one, both while correctly saying "Monday night." The
4-1 vote tally and Commissioner Nida Allam's dissent (from WUNC/WRAL/GovTech, all consistent) are
unaffected by this — only the calendar date needed correcting.

**Recommended citation for any future corpus row: Durham County vote/hearing date = August 24, 2026**
(primary-sourced via dconc.gov), not Aug 25 or Aug 26.

## 5. NAACP v. SpaceXAI — null result confirmed, no change since 08-27
Re-checked via WebSearch: the Aug. 24, 2026 preliminary-injunction hearing (N.D. Miss., Clean Air
Act claims re: the ~69 unpermitted turbines) was postponed per an Aug. 21 court notice; **no new
hearing date has surfaced** in tonight's search either. Same "stalled, not resolved" state as every
check since 08-25. DOJ's motion to intervene/dismiss: still no ruling found.

## 6. Sabey / Decatur Township — null result confirmed, no change since 08-21
Re-checked via WebSearch: most recent confirmable events remain the June 15 motion to dismiss and
June 29 status conference. No ruling, no outcome coverage found for either, same as every check
since 08-21. Genuinely still pending.

---

## Revised candidate-row detail table (PROPOSED corrections only — not inserted into corpus, Britton's call per standing rule)

This supersedes only the **date fields** for rows #35 and #36 from the 08-27 note's draft table, and
adds the primary-source citations found tonight. Row numbering/inclusion is still entirely up to
Britton; nothing below is added to the working corpus.

| # | Site/Project | State | Date (corrected) | Vote | Key primary source found tonight |
|---|---|---|---|---|---|
| 34 | Durham County 9-month moratorium | NC (Durham Co.) | **2026-08-24** (was cited as 08-25/08-26; resolved via county's own agenda page) | 4-1, dissent Cmr. Nida Allam | [dconc.gov agenda](https://dconc.gov/DurhamCo-News/BOCC-Regular-Session-on-August-24-2026.htm) (official, date only), WUNC/WRAL (vote detail) |
| 35 | Greensboro 180-day moratorium | NC (Greensboro) | **2026-08-18** (greensborothread.com's "Aug 19" is a probable date slip — Aug 19, 2026 is a Wednesday, not the Tuesday the source itself claims) | 8-0, 1 recusal (Mayor Pro Tem Denise Roth) | [greensborothread.com](https://greensborothread.com/news/politics/greensboro-nc-data-center-moratorium-denise-roth/) (direct fetch), [Rhino Times](https://www.rhinotimes.com/news/council-reverses-course-on-data-center-moratorium/) (direct fetch, backstory: 5-4 rejection Jul 21 → 9-0 process-start Aug 3 → 8-0 enactment Aug 18) |
| 36 | Alamance County 1-year moratorium | NC (Alamance Co.) | 2026-08-17 (confirmed, no discrepancy — verified as an actual Monday) | **5-0** (refines "unanimous") | [Yahoo News syndication](https://www.yahoo.com/news/us/articles/alamance-county-commissioners-unanimously-approve-022232895.html) (direct fetch) |

**On the "30+ NC jurisdictions" state-level framing:** do not add a row or claim asserting a precise
statewide count. If a state-level summary row is ever drafted, the defensible framing is qualitative
("a large, ongoing, multi-region moratorium wave, first jurisdiction Gates County Dec. 2025, at
least ~28 named jurisdictions identifiable across trackers and news coverage as of Aug. 2026, precise
statewide total not independently verifiable from any single sourced tracker") rather than a bare
"30+" figure attributed to news coverage in general.

---

## What's still open
- **North State Journal's "11 counties and 17 towns" figure**: more specific and better-described
  than Carolina Journal's, but I could not read the source article (403'd) — worth a retry with a
  different fetch approach (archive.org, a different user-agent path if available) in a future
  session, since it's the most promising lead toward an actual defensible statewide number.
- **WHQR's own dated article** and **indyweek's own dated article** on the Durham story specifically
  (not just their homepages) weren't individually fetched tonight after the WFAE original already
  ruled out a statewide count — low expected value, but not technically checked.
- Candidate rows #33 (Austin Co. TX) and #37 (Louisville) — untouched tonight, no new information
  beyond what 08-27/08-28 already have.
- Corpus-restructuring, corpus-size, and Phase 3 theme review: untouched, per standing rule — all
  still Britton's call. The now-clearer picture (NC wave is real and large but not a clean "30+,"
  with 3 jurisdictions now individually primary-verified) should make that conversation easier
  whenever Britton wants to have it, not more complicated.
