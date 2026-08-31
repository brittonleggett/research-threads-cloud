# 2026-08-31 — Developer-litigation-against-moratoriums pattern (TX + KY), Coweta GA update, open-lead rechecks

Follow-up to `2026-08-30-nc-moratorium-followup.md`. Chased the "new unchased lead" flagged there
(Hill County, TX) and it opened into a much bigger, well-sourced finding: developers suing local
governments to kill moratoriums is a real, recurring, cross-state pattern (Texas and Kentucky both),
not a one-off. Also checked the other three open items from 08-30/08-16 notes (Louisville Sept 3,
NAACP v. xAI, Sabey). As always: verification/scouting pass only, nothing inserted into the working
corpus or codebook, no design-lock or restructuring decisions made — those stay Britton's.

WebFetch worked fine on most targets tonight (direct fetches succeeded on Texas Tribune, KWTX,
MultiState, KERA, LPM, Times-Herald, bgdailynews, kentuckylantern-adjacent sources); a handful of
403s (louisvilleky.gov, courtlistener.com, one kentuckylantern URL) — flagged individually below,
worked around with WebSearch or an alternate outlet where possible, same convention as prior notes.

---

## 1. Hill County, TX — the "first Texas county" framing from 08-30 needs a major update: the moratorium didn't survive three weeks

### What 08-30's note had (correct as far as it went, but incomplete)
08-30 flagged Hill County (May 2026) as "the first Texas county" to pass a data-center moratorium,
predating Austin County (July 2026), based on a MultiState article — and explicitly hadn't chased it
further. Chasing it tonight found the rest of the story.

### Direct-fetched primary sources tonight: Hill County rescinded its moratorium under lawsuit pressure
- **Adoption:** Hill County Commissioners Court voted **3-2** on **May 12, 2026** to adopt a
  moratorium (up to one year) on new data center, battery-energy-storage, and power-generation
  projects in unincorporated parts of the county — confirmed via direct fetch of
  [Texas Tribune](https://www.texastribune.org/2026/06/05/texas-hill-county-moratorium-rescinded-data-centers/)
  and [KWTX](https://www.kwtx.com/2026/06/04/hill-county-commissioners-court-rescinds-moratorium-data-center-wake-lawsuit/).
  (Note: KWTX's own headline says the rescission meeting was "Thursday," and both the Texas Tribune
  and KWTX bodies independently give **June 4, 2026** as that Thursday — Route Fifty/other secondary
  coverage says June 5; June 4, 2026 is in fact a Thursday per the calendar, June 5 is a Friday, so
  June 4 is the better-supported date. Flagging this exactly like the recurring weekday-mismatch
  pattern in the NC notes.)
- **Lawsuit:** **RCM Hill, LLC** — developer behind a 1,235-megawatt data center project ("Project
  Aquila") near Hillsboro, TX, with ~16 months and ~$1M already invested per its own complaint — filed
  suit in **federal court** (Waco division, Western District of Texas) on **May 27, 2026**, seeking
  **over $100 million** in damages and arguing the county's moratorium was **"ultra vires"** — beyond
  a Texas county's lawful authority. Texas is a **Dillon's Rule state**: counties, unlike home-rule
  cities, only have the regulatory powers the legislature has expressly granted them, and land-use
  authority in unincorporated areas is especially limited. County Attorney David Holmes had warned
  commissioners of exactly this exposure at the May meeting, per Texas Tribune.
- **Rescission:** Commissioners voted **unanimously** on June 4 to rescind the moratorium — roughly
  three weeks after adopting it — and replaced it with a **developer checklist/review requirement**
  instead (no formal legal force comparable to a moratorium; County Judge Shane Brassell described its
  authority as derived from "various state statutes," not a zoning ordinance). One commissioner's
  on-record reaction: **"Unfortunately, we tried."** Precinct 3 Commissioner Scotty Hawkins — who had
  voted *against* the original moratorium — **resigned** at the same meeting (reason not stated in
  either source fetched tonight).
- **Judge Brassell's stated read of the outcome:** the brief moratorium still "accomplished its goal"
  in his view because "some projects that were less desirable...they left the county" during the
  three-week window, and it bought time to develop the checklist.

### New, corroborating: ripple/deterrent and legal-context findings via MultiState (direct-fetched)
[MultiState, "The Local Fight Over Data Centers: A Texas Case Study" (Aug 19, 2026)](https://www.multistate.us/insider/2026/8/19/the-local-fight-over-data-centers-a-texas-case-study),
direct-fetched in full tonight:
- **Tom Green County, TX dropped its own planned moratorium** after watching Hill County's lawsuit
  exposure play out — a direct, named deterrence effect, not a hypothetical one.
- Names **HB 2127** (Texas's so-called "Death Star" bill, a real, commonly-used nickname per this and
  the KERA piece below — not editorializing on my part) as a further legal threat: it broadly preempts
  local regulations that conflict with certain state law, adding to counties' Dillon's-Rule exposure.
- Confirms **Austin County's** July 2026 moratorium is a different posture (framed by the county as a
  temporary evaluation pause) and that, as of this Aug 19 article, **no lawsuit against Austin County
  had been filed** — consistent with 08-30's finding that no vote-tally/duration detail exists yet,
  and now also confirming no legal challenge yet exists as an separate open question.

### New: statewide political context (KERA/KUT, Aug 19, 2026, direct-fetched)
[KERA, "Austin-area residents are pushing for data center bans. State leaders are divided..."](https://www.keranews.org/texas-news/2026-08-19/austin-tx-texas-data-centers-regulations-greg-abbott):
Gov. Abbott's own position has moved — from calling Texas the "epicenter of AI development" in
November 2025 to saying in June 2026 he was "pushing back against these AI data centers," issuing two
directives on ratepayer cost, water conservation, and neighborhood-impact minimization. He has **not**
called a special legislative session to put any of this into statute, and per Texas Politics Project
director Jim Henson, legislators are "look[ing] to the governor to lead the way" rather than acting
themselves — KUT reports state lawmakers contacted for comment on this "all declined to comment."
Abbott's August 2026 order for a statewide grid-connection audit (already noted 08-30 as
background/WebSearch-level) functions, per both MultiState and KERA, as a **de facto statewide
pause superseding the fragmented county-level moratorium approach** — this reframes that audit from
"background context" (08-30's framing) to a more central fact: the state executive branch stepping in
specifically *because* county moratoria are legally fragile, not incidentally alongside them.

**Bottom line for row #33/Austin County and the TX thread generally:** Austin County's moratorium
itself is unchanged from 08-30 (still standing, no lawsuit found as of Aug 19). What's new is the
*context* around it — it is not a stable, "first-of-many" instance the way 08-30 might have implied;
it exists in a legal environment where the only prior TX county to try this was sued into rescinding
within three weeks, and where the state's own governor and a "Death Star" preemption law are actively
crowding out the county-moratorium mechanism.

---

## 2. New: the same developer-litigation pattern is happening independently in Kentucky — genuinely new material, well-sourced

Found while checking on Louisville/KY context (Gov. Beshear's Aug 6, 2026 executive order, see #4
below, mentioned this in passing) — chased it and it's substantial enough to warrant its own writeup.

### Simpson County (Franklin, KY) — TenKey LandCo v. Simpson County Fiscal Court
- **Ordinance:** Simpson County Fiscal Court, under Judge-Executive Mason Barnes, passed an ordinance
  in **December 2025** requiring any new data-center project (and related "integrated energy system"
  infrastructure, e.g. on-site gas turbines) to be sited on heavy-industrial-zoned land **and** obtain
  a **conditional use permit** — giving the county leverage to impose mitigation conditions.
- **The project:** TenKey LandCo I LLC is developing a **~$1.6 billion** data center off I-65 near
  Franklin, KY, for an undisclosed "one of the largest tech companies in the world" end user. The
  Franklin Planning and Zoning Commission (a *city* body) had already approved a preliminary
  development plan in March 2026.
- **The lawsuit:** TenKey filed in **Simpson Circuit Court on January 20, 2026** [(direct-fetched via
  LPM)](https://www.lpm.org/news/2026-01-28/data-center-developer-sues-simpson-county-government-over-land-use-ordinance),
  arguing the *county* ordinance cannot reach a project sited inside *city* limits because Franklin's
  own independent planning/zoning commission has exclusive jurisdiction there — a legal theory (city
  authority displacing county authority) structurally different from Hill County's ultra-vires theory,
  interesting as a second, distinct legal path developers are using nationally.
- **County's counter-argument** (per [bgdailynews, Aug 9, 2026, direct-fetched](https://bgdailynews.com/2026/08/09/court-hears-arguments-from-county-developer-over-simpson-data-center-ordinance/)):
  a different state statute requires county ordinances to apply countywide, including inside cities,
  unless the city's own rule is stricter — "the city of Franklin is not in a bubble, it's part of the
  county," per county attorney Aaron Smith.
- **Status:** Oral arguments held Aug 9, 2026; **Judge Mark Thurmond took the matter under advisement**
  and set a **status conference for October 14, 2026**, by which he indicated he hoped to have a
  decision — i.e., genuinely pending, with a concrete future date worth a re-check in Britton's next
  data-center session after mid-October.
- **A second, related suit:** a citizens' group, **Franklin Citizens for Responsible Development**,
  separately sued the Franklin Planning Commission and TenKey in April 2026 over the *city's* approval
  process — oral arguments on motions to dismiss that suit were heard in July 2026, also still pending
  per the same search pass. Two-track litigation (developer-vs-county AND citizens-vs-city/developer)
  around the same project is itself a notable structural feature.
- **Contagion effect, directly analogous to Tom Green County, TX:** neighboring **Allen County, KY**
  passed its own 24-month data-center moratorium after watching the "headaches" Simpson County leaders
  faced over this dispute (per Kentucky Lantern, WebSearch-summary level, not yet direct-fetched).

### Cave City, KY — Kentucky Industrial Alliance v. Cave City
- **Moratorium:** Cave City Council passed a **12-month** moratorium on data-center projects in
  **May 2026** (public records give May 20, 2026 for the specific ordinance date, per one WebSearch
  result — worth confirming with a direct fetch in a future session if this becomes a corpus row).
- **The project/developer:** **Kentucky Industrial Alliance**, proposing a **$4.8 billion** hyperscale
  data center on 600+ acres near **Mammoth Cave National Park** — a National Park Service proximity
  angle that's a genuinely distinct grievance/stakes profile from every other row in this project's
  corpus so far.
- **Two lawsuits, now consolidated:** Kentucky Industrial Alliance filed suit challenging the
  moratorium itself (arguing its development plan predates the moratorium and should be reviewed under
  the zoning rules in place when filed — direct-fetched via
  [Spectrum News 1](https://spectrumnews1.com/ky/louisville/news/2026/06/10/lawsuit-filed-over-data-center-),
  filed ~June 9-10, 2026), **and** a second suit seeking to reverse the property's 2024 annexation into
  Cave City limits (so the property would fall outside the moratorium's jurisdiction entirely). Per
  WCLU Radio (WebSearch-summary level, not direct-fetched), the two suits were **consolidated before
  Judge John T. Alexander in Barren District Court on August 24, 2026** — very recent, and still
  procedurally pending, no ruling.
- **Council member on record:** Leticia Cline (the moratorium's sponsor) expressed confidence "the
  court will uphold the council's decision," calling the process correct due process.

### Why this matters for the paper, flagged for Britton's eye (not deciding anything)
This is a **second independent state** (after TX) showing the identical mechanism: local government
passes a data-center moratorium/ordinance in response to public opposition → developer sues, on one of
several available legal theories (ultra vires/Dillon's Rule in TX; city-vs-county jurisdiction in KY;
pre-existing-application/vested-rights and annexation-reversal in Cave City) → outcome is either an
early rescission under pressure (Hill County, 3 weeks) or a slow-moving, still-pending court fight
(Simpson County, Cave City — both many months in, no ruling). This looks like a genuinely new,
citable, cross-state mechanism worth naming alongside the existing `regulatory-venue-shifting` code
from the 08-16 national-scan note — related but distinct: venue-shifting is the *developer* switching
which government body it works with; this is the developer switching to the *courts* entirely,
specifically targeting the legal authority of the body that passed the restriction. A candidate label
would be something like `developer-litigation-countermobilization`, but that's a codebook/theme call
that stays Britton's, same as `regulatory-venue-shifting` did in 08-16 — flagging the pattern and its
evidence base here, not proposing to add it myself.

---

## 3. Kentucky's own "30+" statewide moratorium figure — flag the same caution as NC's, unverified tonight

[LPM, "Kentucky Gov. Beshear to require data centers prove no impact on ratepayers" (Aug 6, 2026,
direct-fetched)](https://www.lpm.org/news/2026-08-06/kentucky-gov-beshear-to-require-data-centers-prove-no-impact-on-ratepayers)
states **"more than 30 Kentucky counties and localities have passed moratoriums"** in the course of
covering Simpson County and Cave City as its two named examples of developer lawsuits. I did **not**
run this number down the way the 08-29 note ran down NC's "30+" — no time budget left tonight to trace
its source/methodology. Given the NC experience (an uncited "30+" from one outlet turned out to be a
single undocumented tally), **this KY figure should be treated as unverified, not repeated as fact,
until someone runs the same kind of source-tracing pass on it** that 08-29 did for NC. Flagging this
explicitly rather than letting a second "30+" figure quietly acquire credibility by association with
the now-better-understood NC one.

Also from the same article, for completeness (not independently verified beyond this one direct-fetch
tonight): Beshear's Aug 6 executive order requires data-center developers to (1) submit energy plans
to the Energy and Environment Cabinet and not pass project costs to ratepayers, with permits to be
denied over air/water/natural-resource harm; (2) pay local and school taxes rather than use existing
exemptions to avoid them; (3) hold public discussions with local community leaders/members. The
article itself flags the order's own enforcement gap: "It is unclear from the order what penalties
developers will face if they fail to agree to some of the required commitments."

---

## 4. Louisville, KY — Sept 3, 2026 Planning Commission meeting: still a future event, nothing new to report

Checked directly. The Aug 20 Planning Commission developments already fully covered in 08-30's note
are the most recent facts available — confirmed via a fresh WebSearch pass tonight (LPM's own article
index, WDRB) that no article postdating Aug 20 exists yet. `louisvilleky.gov`'s own data-centers page
403'd on direct WebFetch tonight (same bot-block pattern seen on several `.gov`/city sites in prior
notes, e.g. myfox8/greensboro-nc.gov on 08-28/08-29) — did not find or need a workaround since
WebSearch confirms no newer coverage exists regardless. Today is Aug 31, 2026; the Sept 3 meeting is
three days out. **Genuinely nothing new here** — re-check after Sept 3 in a future session.

## 5. NAACP v. xAI (N.D. Miss.) — still postponed, no new hearing date found, unchanged since 08-29

Re-confirmed: the Aug. 24, 2026 preliminary-injunction hearing was postponed per an **Aug. 21, 2026
court notice** (direct-fetched via AOL/syndicated coverage tonight, same fact the 08-29 note already
had at WebSearch-summary level — now direct-fetch confirmed). **No new hearing date has been
published** in any source found tonight. `courtlistener.com`'s docket page 403'd on direct WebFetch
(couldn't check raw docket entries directly) — tried, didn't work around it, flagging as a genuine gap
rather than a resolved negative. DOJ's motion to intervene/dismiss: still no ruling found. This is the
same "stalled, not resolved" status reported in every note since 08-25 — reporting the null result
plainly rather than implying progress that didn't happen.

## 6. Sabey / Decatur Township (Indianapolis) — still pending, no ruling found, unchanged since 08-22

Re-checked via WebSearch: the June 15 motion-to-dismiss and June 29 status conference remain the most
recent dated events found; no coverage of a ruling on either the motion to dismiss or the separate
citizens'-petition judicial-review case turned up tonight. Same null result as every check since
08-21/08-22 — genuinely still pending, not a search-technique gap.

---

## 7. Coweta County, GA — Project Sail litigation still pending; but a *second* Coweta project (Project Oak) was formally denied — a new "opposition wins" data point

### Project Sail — no change
Direct-fetched [Times-Herald, "Where Coweta's five proposed data centers stand" (June 2, 2026)](https://www.times-herald.com/data_center/where-cowetas-five-proposed-data-centers-stand/article_55ee204a-0e00-43e4-9ad1-78c92b679d06.html)
and ran a fresh WebSearch tonight: the May 5, 2026 residents' suit in Coweta County Superior Court
(seeking to void the April 2026 3-2 rezoning) has **no ruling reported** as of tonight — same "pending"
status the 08-22 note already had, now re-confirmed rather than newly resolved.

### New: Project Oak (a different, separate Coweta County data-center proposal) — rezoning unanimously DENIED, Aug 2026
Direct-fetched [Times-Herald, "Project Oak data center denied by commissioners" (pub. Aug 25, 2026)](https://www.times-herald.com/news/project-oak-data-center-denied-by-commissioners/article_76db6b0a-615b-48e6-aacd-5042bdd0f401.html):
- Project Oak — a proposed 255-acre data-center campus near Walt Sanders Road in Coweta County,
  reported water use ~28,000 gallons/day — is **a separate project from Project Sail**, not a renaming
  or the same site (confirmed via the June 2 "five proposed data centers" roundup, which lists Sail,
  Oak, Pegasus, Bridgeport, and Peach as five *distinct* filings).
- Coweta County Board of Commissioners **unanimously denied** the rezoning request, after receiving
  **121 letters of opposition from 112 individuals and zero letters in support** — the article notes
  commissioners did not discuss the petition on the record before voting, so no stated reasoning is
  available beyond the vote itself.
- Developers ("Project Oak's developers," specific company not named in the article) argued the site
  was already industrial-zoned and the request didn't require variances — an ambivalent-economic vs.
  community-opposition contrast worth noting, similar in shape to Clinton County, IN's 3-0 denial
  (08-16 note) as one of the relatively few outright opposition *wins* nationally, and now a second GA
  data point alongside (not replacing) Coweta's own separate, still-pending Project Sail litigation.
  A "Stop Project Oak" resident group and a Change.org petition ("Students Against Project Oak and
  Sail") existed prior to the vote — WebSearch-level confidence on the petition/group details, not
  independently direct-fetched tonight, vote outcome itself is primary-source confirmed via Times-Herald.

---

## What's still open
- **Simpson County, KY (TenKey v. Simpson Fiscal Court):** under advisement; Judge Thurmond's status
  conference is **October 14, 2026** — a concrete future date worth a targeted re-check in whichever
  session falls after it.
- **Cave City, KY (Kentucky Industrial Alliance v. Cave City):** two suits consolidated Aug 24, 2026
  before Judge John T. Alexander (Barren District Court); no ruling yet.
- **Kentucky's "more than 30 counties/localities" moratorium figure:** unverified tonight — needs the
  same source-tracing treatment the 08-29 note gave NC's "30+" before it's treated as reliable.
- **Allen County, KY's** 24-month moratorium (cited as a contagion effect from Simpson County's
  dispute): WebSearch-level only, not yet direct-fetched.
- **Cave City's exact moratorium ordinance date** (May 20 vs. general "May 2026"): not resolved with a
  direct fetch tonight.
- **NAACP v. xAI:** still postponed with no new hearing date; `courtlistener.com` 403'd on direct
  fetch, so the raw docket couldn't be checked directly tonight — try again or find an alternate docket
  mirror in a future session.
- **Sabey/Decatur Township:** still pending, no ruling; same as every check since 08-21/08-22.
- **Louisville's Sept 3, 2026 Planning Commission recommendations and the subsequent Metro Council
  vote:** genuinely still in the future — re-check after Sept 3.
- **Project Sail (Coweta) litigation outcome:** still pending, unchanged since 08-22.
- **New candidate mechanism-level pattern — developer litigation against local moratoria/ordinances
  (TX: Hill County/RCM Hill, Tom Green County's deterred moratorium; KY: Simpson County/TenKey, Cave
  City/Kentucky Industrial Alliance):** flagged here as a well-sourced, cross-state pattern worth
  Britton's attention for the codebook/theme discussion — not added to any codebook or corpus row
  myself, per standing rule that Phase 3/design decisions stay his.
- Corpus restructuring, corpus size, and the two-list NC jurisdiction-count discrepancy from 08-30:
  untouched tonight, still entirely Britton's call, as always.
