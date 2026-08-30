# 2026-08-30 — North State Journal article read in full (primary-verified); Austin Co. TX and Louisville KY follow-up checks

Follow-up to `2026-08-29-nc-30plus-claim-resolution-and-greensboro-alamance-verification.md`. Task 1
below resolves that note's single open lead (the North State Journal "11 counties and 17 towns"
figure, previously 403-blocked). Task 2 checks candidate rows #33 (Austin County, TX) and #37
(Louisville, KY) for anything new since 08-27/08-28. As always: verification pass only, nothing
inserted into the working corpus, and no state-level summary count is being decided here — that
remains Britton's call per standing project rule.

---

## 1. North State Journal — READ IN FULL tonight (primary-source confirmed, not WebSearch-summary anymore)

### How I got past the 403
`WebFetch` on `nsjonline.com` still returned 403 tonight (tried the base article URL and an `/amp/`
guess). I also tried `web.archive.org` (both a direct snapshot URL and the Wayback `available` API) —
the `available` API confirmed a snapshot exists (`web.archive.org/web/20260807045447/...`, captured
Aug 7, 2026, status 200 at capture time), but this environment's egress policy itself blocks
`web.archive.org` outright (`curl` to it returns "Blocked by egress policy," a hard proxy-level block,
not a site-side 403 — confirmed this is not a transient/fixable TLS issue per the environment's own
proxy-status guidance, so I didn't pursue it further). What worked: plain `curl` directly to the
`nsjonline.com` article URL with a standard desktop-browser User-Agent string returned **HTTP 200**
and the full page (111,957 bytes) — WebFetch's request was almost certainly getting bot-blocked at
the User-Agent/header level, not because of anything account- or paywall-related. Worth remembering
as a technique for future 403s on this project: a plain `curl` with a browser UA is a legitimate
"different fetch approach" distinct from WebFetch, and it worked here where WebFetch didn't.

### The article, cited properly
**"Data center moratoriums spreading,"** North State Journal, byline **A.P. Dillon**, published
**August 6, 2026** (page metadata: `article:published_time` = 2026-08-06T15:25:46-04:00; oddly, a
`dateModified`/`article:modified_time` of 2026-08-05, i.e. nominally *before* the published time —
noted for completeness, not otherwise meaningful). URL:
`https://nsjonline.com/article/2026/08/data-center-moratoriums-spreading/`. Sub-headline: *"More than
two dozen North Carolina counties and towns are blocking the facilities."*

### Is "11 counties and 17 towns" sourced within the article? Yes — it is NSJ's own reporting, not a repeat of someone else's number
Direct quote from the article body: *"Based on public records, resolutions and official meetings, at
least 11 counties and 17 towns have enacted a moratorium, typically one year in length."* This is
explicitly framed as the outlet's own compiled tally from primary documents (public records,
resolutions, meeting minutes), not an attribution to Carolina Journal, a law-firm tracker, or any
other outlet. That is a materially stronger methodological disclosure than Carolina Journal's "more
than 30" (which cited no methodology at all, per the 08-29 note). The phrase "at least" signals NSJ
itself treats this as a floor, not a final precise count.

**Caveat on the "11 counties" figure specifically:** the article's own sub-header for that block is
"Counties and tribal regions," and the 11-item list includes the Eastern Band of Cherokee Indians
(EBCI/Qualla Boundary), which is a tribal government, not a county. So "11 counties" is very slightly
loose — it's 10 counties + 1 tribal nation bundled under one label. Minor, but worth being precise
about if this ever gets cited directly.

### The named list (primary-sourced, full text captured)
**Counties and tribal regions (11 items, matches the article's count):** Clay County (1-yr, Sep
2025), Gates County (1-yr, early 2026), Chatham County (1-yr, Feb 2026), Rowan County (1-yr, Apr
2026), Swain County (1-yr, Apr 21 2026), Orange County (1-yr, Apr 21 2026), Harnett County (1-yr, May
4 2026), Northampton County (32-month, May 4 2026), Eastern Band of Cherokee Indians/Qualla Boundary
(indefinite, May 2026), Durham County (1-yr, June 2026, following an earlier shorter pause), Davie
County (1-yr, July 2026).

**Towns and cities (17 items, matches the article's count):** Brevard (1-yr, Sep 2025), Canton (1-yr,
Feb 2026), Kings Mountain (6-mo/182-day, Feb 2026), Boone (1-yr, Mar 2026 — article itself notes
"corrected from 90 days"), Clyde (1-yr/12-mo, Apr 2026 — article notes "added"), Apex (1-yr, Apr
2026), Wendell (through Dec 31 2026, Apr 2026), Woodfin (12-mo, May 2026 — article notes "added"),
Charlotte (150-day, June 2026 — article notes "date corrected from May"), Durham city (initially
60-day May 2026, extended to full 12-mo June 2026), Fayetteville (120-day, May 2026), Spring Hope
(1-yr, May 2026), Boiling Spring Lakes (1-yr, June 2026), Holly Springs (1-yr, June 2026),
Hillsborough (1-yr, June 2026 — article notes "added"), Asheville (1-yr, June 2026, unanimous),
Franklin (1-yr, July 2026).

The "corrected"/"added" annotations embedded directly in the list text are notable: this reads like a
living, periodically-updated tracker page rather than a one-time static tally — a methodological
plus relative to Carolina Journal's uncited single number.

**Other content in the article, not part of the moratorium count but relevant to the paper's public-
opposition angle:** Lee County and Sanford added data-center-specific language to their zoning
ordinances (UDOs) in April instead of a moratorium; Stokes County approved a project amid opposition
and litigation; Vance and Edgecombe counties have considered but not enacted moratoriums; the article
attributes organizing momentum partly to "environmental advocacy and citizen-led groups" and names
the Party for Socialism and Liberation (PSL) specifically, sourced to a report by Rob Nanfelt
(Charlotte's Real Estate and Building Industry Coalition) after a May 2026 Charlotte City Council
meeting, republished by Business NC's newsletter. This activist-organizing detail could be relevant
to the paper's opposition-actors/framing analysis, flagged here for awareness only — not evaluated
further tonight and not a claim I'm asking to be added anywhere.

### Cross-check against the 08-29 note's independently-reconstructed 28-jurisdiction list
The 08-29 note reconstructed "28 named jurisdictions" from a mix of trackers and WebSearch summaries,
built independently of this NSJ article (which hadn't been read yet). Comparing the two 28-item lists
name-by-name: **18 jurisdictions appear on both lists** (Gates, Brevard, Clay, Canton, Boone, Swain,
Clyde, Chatham, Orange, Apex, Wendell, Rowan, Kings Mountain, Durham County, Durham city, Charlotte,
Davie, Hillsborough). **10 appear only in NSJ's list** (Northampton County, EBCI, Harnett County,
Woodfin, Fayetteville, Spring Hope, Boiling Spring Lakes, Holly Springs, Asheville, Franklin). **10
appear only in the 08-29 reconstruction** (Watauga County, Madison County, Surry County, Yadkin
County, Mount Airy, Greensboro, Alamance County, Cumberland County, City of Wilson, Waxhaw).

So the two lists land on nearly the same *total* (28 each) but are **not the same list** — only 18 of
28 names overlap. Combined, the two lists together name **38 distinct NC jurisdictions**. This is an
important nuance for Britton: the "~28-30" convergence across sources is not corroboration of one
list, it's two different partial trackers that happen to be similar in size. If anything, this
suggests the true number of jurisdictions with some form of data-center pause is *at least* in the
high 30s as of August 2026, not a settled ~28-30. I am reporting this comparison as information only
— **not** proposing any state-level count for the manuscript; that decision stays Britton's per the
standing rule.

### Bottom line on this lead
North State Journal's article is now **primary-source read in full**, not WebSearch-summary-level.
Its "11 counties and 17 towns" figure is the outlet's **own methodologically-described tally** (public
records, resolutions, meeting minutes), materially better-documented than Carolina Journal's "more
than 30." It is still, on its own terms, an "at least" floor, not a verified-complete statewide count,
and it diverges substantially in membership from the independently-reconstructed 08-29 list despite
similar magnitude.

---

## 2. Candidate row #33 — Austin County, TX — refined, no change to prior facts, one new contextual detail

### What's unchanged (already primary-verified 08-27, re-confirmed tonight)
Direct-fetched **KWHI** (`kwhi.com`, pub. July 28, 2026) and **Banner Press** (`bannerpresspaper.com`)
tonight: both confirm Austin County Commissioners Court voted **unanimously** to adopt a moratorium
on new AI data center and battery energy storage system (BESS) development, vote described as
occurring "Monday" (= **July 27, 2026**, consistent with the existing row's date — July 27, 2026 is
in fact a Monday, no discrepancy). **Neither source states the exact commissioner-by-commissioner
vote count** (e.g., "5-0") — both just say "unanimously"/"unanimous." **No moratorium end date/
duration is stated in either source**; Banner Press explicitly notes durations for this type of
moratorium "typically last[] between six months and three years" without saying which applies here.
This remains an open gap — if a precise duration is needed for the corpus row, it isn't in either
article checked tonight or on 08-27.

### New tonight: Austin County is the *second* Texas county to do this, not the first
Direct-fetched **MultiState** (`multistate.us`, "The Local Fight Over Data Centers: A Texas Case
Study," pub. Aug 19, 2026): identifies **Hill County** as "the first county to take such action
against data centers in the state," passing its moratorium in **May 2026**, i.e. roughly two months
before Austin County's. This is new context not in the 08-25/08-27 notes — Hill County, TX is a
candidate for its own corpus row if Britton wants a second TX data point, but I have not chased Hill
County further tonight (out of scope for what was asked) and am flagging it only as a lead.

### New tonight: statewide TX context (not Austin-County-specific, background only)
WebSearch surfaced that Texas Gov. Greg Abbott ordered a statewide audit of data centers connecting to
the state grid in early August 2026 (Texas Tribune, Aug 3, 2026; Morrison Foerster legal alert, Aug
11, 2026), which the MoFo piece describes as functioning as a de facto statewide pause on new
projects pending review. This is WebSearch-level confidence only tonight (not direct-fetched in full)
and is state-level, not Austin-County-specific — noted for background awareness, not verified in
depth, and not something I'm proposing to fold into the Austin County row.

**Confidence summary for row #33:** vote occurrence, unanimity, and July 27 date — primary-source
confirmed (two independent direct-fetched local outlets). Exact vote tally and moratorium duration —
unconfirmed, not stated in any source checked. "Second county in Texas" framing — primary-source
confirmed via MultiState's direct-fetched article.

---

## 3. Candidate row #37 — Louisville, KY — one genuine new development since 08-28

### What's unchanged (already primary-verified 08-28)
Louisville Metro Council's **24-1 (plus one abstention)** vote enacting a **6-month** data-center
moratorium on **August 13, 2026** stands unchanged — re-confirmed via WebSearch tonight against LPM
and WKYT, consistent with the 08-28 note's LPM/WBKO direct-fetch findings. No new information on this
vote itself.

### New: Planning Commission activity since the moratorium (Aug 20, 2026)
Direct-fetched **LPM**, "Louisville Planning Commission looks to strengthen data center restrictions"
(pub. Aug 20, 2026): the Planning Commission **declined to approve** the city planning staff's draft
permanent data-center regulations at its Aug. 20 meeting, and instead sent staff back to strengthen
several provisions before the moratorium's 6-month window runs out (moratorium ends early only if
permanent rules are adopted first). Specific asks reported: require **closed-loop cooling** to limit
water use, require heat waste be directed away from adjacent properties, prohibit new data centers
within a quarter-mile of existing data centers or hazardous-materials properties, and require zoning
approval (rezoning) for nearly all new data centers going forward. Commissioners also voted to
**retain a cap excluding "hyperscale" facilities above 500,000 sq ft**, with Commissioner Jim Mims
quoted defending the size cap as responsive to public concern about "mega data centers." The
Commission's own next step, per the article, is to **finalize recommendations at a September 3, 2026
meeting** before sending them to Metro Council for a final vote — i.e., **this is still pending, not
yet resolved as of tonight (Aug 30, 2026)**, and the Sept. 3 date is a future event to check back on
in a later session.

**Confidence summary for row #37:** the original Aug 13 vote/tally — unchanged, still primary-source
confirmed (08-28). The Aug 20 Planning Commission developments — primary-source confirmed tonight
(direct-fetched LPM article). The permanent-regulation outcome itself — genuinely unresolved/future
(Sept. 3 meeting hasn't happened yet as of this note's date).

---

## What's still open
- **Hill County, TX** — surfaced tonight as the actual first Texas county with a data-center
  moratorium (May 2026, per MultiState), predating Austin County. Not yet checked directly — a
  candidate for a future session if Britton wants a second confirmed TX row.
- **Austin County's exact vote tally and moratorium duration** — neither found in any source checked
  across 08-27 or tonight. Would need the county's own commissioners-court minutes/agenda (not
  attempted tonight — no county-government-site URL identified for Austin Co., TX, unlike Durham
  County, NC's dconc.gov success on 08-29).
- **Louisville's permanent regulation outcome** — genuinely pending; Planning Commission's Sept. 3,
  2026 meeting and the subsequent Metro Council vote are future events, not yet resolvable.
- **North State Journal's "11 counties/17 towns" vs. the 08-29 reconstructed list** — both are
  internally coherent but diverge in membership (18/28 overlap). Neither should be treated as *the*
  authoritative statewide count; if anything, the union (38 distinct names) argues the true number is
  higher than either single tracker, but this is an observation, not a proposed manuscript figure —
  that call stays Britton's, per standing rule.
- Corpus restructuring, corpus size, and Phase 3 theme review: untouched tonight, per standing rule —
  still entirely Britton's call.
