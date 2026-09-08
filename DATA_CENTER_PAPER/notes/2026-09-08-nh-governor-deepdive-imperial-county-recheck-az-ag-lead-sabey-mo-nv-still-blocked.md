# 2026-09-08 — NH governor-level lead deepened, Imperial County CA rechecked (still tentative, county committed to redraft), a new AZ AG statewide-pause lead, Sabey/Decatur still unresolved (4th night), MO/NV re-attempted with a new access route and still blocked

## What this is
Direct continuation of 09-07's open items, per tonight's assignment: (1) another push
on Sabey/Decatur's Aug 20 hearing outcome and MO/NV court access from new angles,
(2) a deeper follow-up on the New Hampshire governor-level moratorium lead, (3) a
recheck of the two pending Imperial County, CA rulings, (4) a fresh national sweep
if time allowed. All AI-conducted research (WebSearch + WebFetch + direct `curl`),
disclosed per repo convention. No fabricated citations — every claim below is
sourced to a specific fetch, and per the README's standing warning about
WebSearch-fabricated case/docket numbers (caught twice already, 09-05 and 09-07),
**no case number below was accepted from a search-tool synthesis without being
independently confirmed by reading an actual primary document; where I could not
get a primary document to confirm one, I say so and don't supply a substitute
number.** Nothing added to the actual corpus files or Study1 design docs — this is
a verification/gathering pass only, per this project's standing rule that
corpus/design restructuring (the region-as-moderator pivot) stays Britton's call,
untouched tonight. Read-only otherwise; no git commands run.

---

## 1. Sabey/Decatur (Indianapolis) — Aug 20 hearing outcome: still genuinely unresolved, now four consecutive nights (09-04, 09-05, 09-07, tonight)

Tried several angles not used in the last two passes:
- Fresh phrasing sweeps ("status update," "summary judgment," "briefing schedule,"
  "trial date," "construction begins/groundbreaking") — nothing dated after Aug 20
  turned up anywhere.
- Direct-fetched Mirror Indy's original judicial-review article, its rolling
  `mirrorindy.org/data-centers/` tracker page, and the Sabey-branded project site
  (`sabeydecaturdatacenter.com`) — none mention the Aug 20 hearing, its outcome, or
  any litigation status at all; the project's own site has no news/updates section,
  just static regulatory-filing dates through March 2026.
- Tried UniCourt and a general "case number" search for **Cause No.
  49D05-2604-PL-021609** (the real, primary-source-confirmed number from 09-05) —
  no docket entries surfaced on UniCourt or anywhere else searchable.
- Re-tested `mycase.in.gov`/`public.courts.in.gov/mycase` — confirmed again it's a
  session-based JavaScript case-search application, same conclusion as 09-05: not
  GET-addressable, would need an interactive browser session a human has and this
  environment doesn't.
- Checked IBJ's own "Lawsuits" topic page and a general IndyStar search — nothing
  Sabey-specific past the June 15 motion-to-dismiss/June 29 status-conference
  facts already in the 08-21 note.

**One real (if modest) new data point, not a hearing outcome:** Sabey's own August
27, 2026 press release ("Sabey Data Centers Outlines Community Commitments,"
direct-fetched from GlobeNewswire) states construction is now expected to **begin
Q2 2027**, with phased occupancy Q4 2029 through 2035 — a materially later start
than the "site prep/groundbreaking in 2026" language circulating in some outlet
summaries earlier this year. The press release does not mention the lawsuit at
all, so this can't be read as a signal about how the case is going (a normal
company might push a construction timeline for many non-litigation reasons) — just
flagging the discrepancy with earlier "groundbreaking 2026" claims in case it
matters for the write-up's timeline.

**Bottom line: treat this as a standing, real information gap, not a search
failure** — the same conclusion three prior nights reached, now with a fourth
confirmation. Recommend not re-trying the same web-search angles again without a
new access method (e.g., Britton pulling the docket himself via a normal browser
at `mycase.in.gov`, case number 49D05-2604-PL-021609, Marion Superior Court 5).

---

## 2. Missouri / Nevada court access — still blocked; found and confirmed the *specific* mechanism blocking Nevada's own court portal (not just DocumentCloud)

### Missouri
Re-tested `courts.mo.gov/casenet/base/welcome.do` and `courts.mo.gov/cnet/index.do`
directly via `curl` with a spoofed desktop User-Agent: both still return **HTTP
403**. No change from 09-05's WAF-block conclusion. Did not burn further time
re-trying the same route, per the standing "known ceiling" conclusion — spent the
saved time on Nevada instead, below.

### Nevada — new finding: found the Washoe County court's *own* case-search portal (not just the DocumentCloud-hosted complaint), and confirmed exactly why it can't be scripted
Previous nights' MO/NV checks focused on `courts.mo.gov` and the DocumentCloud-
hosted NV Energy v. Tract complaint (both WAF-blocked). Tonight, starting from
`washoecourts.com` (the Second Judicial District Court's own site, which *does*
load, HTTP 200), found its real case-lookup tool at
`caseinfo.washoecourts.com` — a Drupal-based "eCourt Public Portal" with a proper
**"Case Search"** page (`/node/393`). This is a genuinely different, more official
access route than anything tried in 09-05.

However: inspecting the search form's actual HTML shows required fields named
`captcha_response`, `captcha_sid`, and `captcha_token` alongside the search
criteria fields. **This confirms the specific blocking mechanism is a CAPTCHA on
the court's own portal**, not (only) a Cloudflare WAF challenge on a third-party
document host. This is a more precise diagnosis than 09-05 had (which attributed
the NV block to DocumentCloud's Cloudflare WAF and a proxy-IP reputation issue
with `r.jina.ai`) — the court's *own* system is separately, deliberately
CAPTCHA-gated for public case search, which is a different and harder kind of
block than a WAF: it requires solving a visual challenge, not just presenting as a
normal browser. No case/docket number obtained for NV Energy v. Tract.

**Bottom line, both states: still genuinely blocked, now for two distinct and
independently confirmed reasons (MO: network-level WAF/bot-detection; NV: an
explicit CAPTCHA on the case-search form itself).** Recommend continuing to treat
this as a structural ceiling for autonomous runs, not a nightly retry target,
unless Britton wants to pull either record himself via a normal browser session
(for NV: `caseinfo.washoecourts.com`, "Case Search," party name "Tract" or "NV
Energy"; for MO: `courts.mo.gov` Case.net, party names Daniel Pate/Kerry McCullen
or "City of St. Louis Board of Adjustment").

---

## 3. New Hampshire — Gov. Ayotte's anti-data-center stance: substantially more detail than 09-07 had; a real multi-official, cross-party moment

09-07 had this as a single-source (NHPR), single-quote lead. Tonight, direct-
fetched NHPR again plus indepthnh.org's dedicated roundup piece and the Union
Leader — considerably more texture:

- **The trigger, more precisely:** the site under discussion is the **former
  Merrimack Station coal plant in Bow, NH** (345 acres), owned by **Granite Shore
  Power, LLC**. **Eversource Energy** conducted an interconnection feasibility
  study at FERC's request for a **350 MW** data center project on the site. **State
  Consumer Advocate Donald Kreis** is the one who discovered and publicized these
  FERC filings (via social media), which is what set off the current round of
  political reaction. **Discrepancy flagged, not resolved:** indepthnh.org/NHPR
  describe the coal plant as having "closed since September 2025"; the Union
  Leader describes it as "closing 2028." Both are direct-fetched, professionally
  reported sources describing the same plant — didn't find a way to adjudicate
  which is correct tonight (possibly a partial-closure/full-closure distinction
  not spelled out in either piece). Flag for whoever writes this up to re-check
  before citing a specific closure date.
- **Gov. Kelly Ayotte (R)** — confirmed via direct quote (NHPR): "I want to reduce
  energy prices and the amount of energy a data center takes will raise energy
  costs in the state of New Hampshire, and I can't support that." She consulted
  ISO-New England executives before finalizing her position. Her moratorium would
  go in the **budget trailer bill** (the policy-changes vehicle attached to the
  two-year state budget), effective **no earlier than July 2027**, though she
  could act sooner via **executive order**. Per the Union Leader (direct-fetched):
  her plan is explicitly framed as something she'll pursue **"if reelected"** —
  worth knowing that 2026 is a New Hampshire gubernatorial election year and this
  is at least partly a campaign-season position, not only a policy one.
- **This is a genuinely cross-party moment**, not just a Democratic-vs-Republican
  story: a **Republican governor** and multiple **Democratic** officials are
  independently converging on "pause new data centers," for at least partly
  different reasons (Ayotte: consumer energy costs; Democrats below: community
  protections, disclosure, host-community compensation).
- **Cinde Warmington** (Democratic gubernatorial candidate, i.e. Ayotte's
  opponent) — pledged a **day-one executive order** for a temporary moratorium,
  and criticized Ayotte for having signed pro-development legislation in 2025 and
  letting protective bills die in committee; proposed a "Community Bill of Rights"
  framework as an alternative approach.
- **Karen Liot Hill** (D-Lebanon, Executive Councilor) — wants action sooner than
  Ayotte's July 2027 timeline: "Waiting for a moratorium until the next state
  budget takes effect in July 2027 is too late."
- **Rep. Eleana Colby** (D-Bow) — is demanding disclosure of the project's
  location, resource demands, and cost allocation from the developer/town.
- **House Democrats / Rep. Tom Cormen (D-Lebanon)** — filed two Legislative
  Service Requests for the **2027 session**: **LSR 2027-0002 and LSR 2027-0048**,
  which would establish a **24-month moratorium** and a **30-megawatt
  cost-responsibility threshold**. Cormen, direct-quoted: "New Hampshire should
  not hand massive corporations a blank check and leave Granite Staters to deal
  with the consequences." Attempted to pull the actual LSR text directly from
  `gc.nh.gov`'s LSR search tool — the specific URL surfaced by search
  (`gc.nh.gov/lsr_search/billText.aspx?id=1435&type=3`) returned only an
  application error ("Index 0 is either negative or above rows count"), not the
  bill text — **so the LSR numbers above are WebSearch/news-sourced, not yet
  independently confirmed against the primary legislative record.** Worth a
  follow-up once the LSR search tool is navigated properly (it's likely an
  ID-lookup form, not a direct-URL system) or once these get formal bill numbers
  in the 2027 session.
- **Stefany Shaheen** (Democratic candidate, NH's 1st Congressional District) —
  called for *federal* legislation requiring data center developers to compensate
  host communities — a federal-policy angle distinct from all the state-level
  moratorium talk elsewhere in this corpus.

**Read for the paper:** this is a stronger comparative data point than 09-07
realized — not just "a new governor opposes data centers" but a live, multi-actor,
cross-party, election-year fight with at least four distinct concrete proposals in
play (Ayotte's budget-trailer-bill moratorium, Warmington's day-one EO pledge, the
House Dem 24-month/30MW bill, and Shaheen's federal compensation-mandate idea) —
useful if the national design ends up wanting a "top-down political mobilization"
category distinct from the resident-litigation cases that dominate the corpus so
far. Still genuinely un-integrated into the corpus/design, per the standing rule
that's Britton's call.

---

## 4. Imperial County, CA — both tentative rulings rechecked: neither has become final; new primary-source detail on what the county is doing about it

Direct-fetched **Imperial County's own government press releases** (not just news
coverage) tonight — a first for this thread:

- **`imperialcounty.org/2026/08/icdcmoratorium2026/`** (Aug 28, 2026, county's own
  site): confirms Judge Jones's tentative ruling that the county's moratorium
  findings didn't meet the "current and immediate threat" legal standard, and
  that the county's response is to (1) review the ruling, (2) **prepare a new,
  legally-compliant moratorium for Board of Supervisors consideration**, and (3)
  keep the Data Center Advisory Committee process running. Confirms the
  moratorium's own history directly: the original 45-day moratorium (June 2026)
  was extended by **10 months and 15 days** in July 2026, before Jones's ruling.
- **`imperialcounty.org/2026/08/moratorium08312026/`** (Aug 31, 2026, county's own
  site, three days later): county staff are "actively developing a proposed
  moratorium that takes into account the issues identified by the Superior Court"
  — but **no board meeting date has been set yet** ("additional information...
  will be provided once available"). This is a real, if incremental, update since
  09-07 — confirms via primary source that the county isn't abandoning the
  moratorium approach, just redrafting to fix the specific legal defect Jones
  identified, with no date yet for when that comes back to the Board.
- **Judge Anderholt's separate CEQA ruling** (the opposition-favoring one):
  re-checked via `ivpressonline.com`'s original July 30 article and fresh search
  tonight — **still tentative**. Confirmed again: 20 days after "notice of entry"
  to meet-and-confer on a proposed writ/judgment, and nothing dated after the
  already-known Sept 1 KPBS coverage (09-07's source) turned up tonight
  suggesting finalization. No writ or final judgment found as entered.

**Bottom line: functionally unchanged from 09-07 in outcome** (both rulings still
tentative, neither final) **but meaningfully better-sourced** — this is now
confirmed from the county's own government communications, not just news
paraphrase, and there's a real new fact (the county has publicly committed, in its
own words, to bringing a *revised* moratorium back to the Board, just with no date
yet). Recommend a future-night check once the county sets that board-meeting date.

---

## 5. Coweta County, GA — Project Oak: the "no stated reasoning" gap from 08-31 is now filled

The 08-31 note flagged that commissioners voted unanimously to deny Project Oak's
rezoning without discussing it on the record, so no reasoning was available.
Direct-fetched a Sept 1, 2026 follow-up from The Citizen (thecitizen.com):
**Commissioner Jeff Fisher** has since explained his vote. Key points, worth
noting because they complicate a simple "opposition wins" reading: Fisher
explicitly **distinguished Project Oak from two other Coweta data-center
proposals he supports** (Project Peach and Project Sail — "every project has to
stand on its own"), and grounded his no-vote in a **specific zoning-conditions**
argument (the property's 2024 zoning conditions capped it at office/warehouse use
up to 2.1M sq ft; he "wasn't convinced that we should change the zoning
conditions already in place for this particular project") rather than a
categorical anti-data-center stance. He also said he weighed both the developer's
presentation and nearby residents' concerns. **Read for the paper:** this is a
useful nuance against treating every commissioner "no" vote in the corpus as
straightforward resident-opposition-wins-the-day — at least one of them is
better described as a procedural/zoning-consistency vote by a commissioner who is
otherwise pro-data-center on adjacent projects in the same county.

---

## 6. DeKalb County, GA — filled in the moratorium's own status (it was about to lapse, then didn't); adds context to the developer-suit thread already in the corpus

Not part of tonight's assigned five leads, but surfaced while national-sweeping
and directly relevant to the DeKalb thread the corpus already has (Shadowbox
Studios v. DeKalb County, per 09-07's note). Direct-fetched decaturish.com (twice)
and Capital B News (Atlanta):

- **June 23, 2026:** DeKalb's Board of Commissioners **unanimously rejected** its
  own proposed permanent data-center land-use ordinance (would have capped
  campuses at 1M sq ft, required 750-ft residential buffers, restricted to
  industrial zones) — not because commissioners wanted *less* regulation, but
  because a resident coalition (quoted: activist Gina Mangham) argued it "did not
  give us adequate protection," i.e. was too permissive as written.
  **Commissioner Ted Terry** warned this left the county's existing moratorium
  legally vulnerable to a developer challenge, since DeKalb has no statutory
  definition of "data center" to justify extending a pause.
- **July 7, 2026:** the Board voted to **extend the moratorium to March 30,
  2027** (i.e., it was on track to lapse Sept 30, 2026 — a near-term cliff — but
  that's now resolved for several more months). **Ted Terry cast the lone
  dissenting vote** — not because he opposed extending the pause, but because he
  objected to the mechanism (having the county CEO's own departments study
  impacts internally rather than commissioning independent outside research) —
  worth noting as a genuine nuance, not "the pro-regulation commissioner voted
  against the moratorium."

**Bottom line:** the moratorium is stable through March 2027, the near-term
"replace-it-or-lose-it" pressure the June articles implied has passed for now,
and there's now a clearer account of *why* the county's own permanent-regulation
effort stalled (resident coalition said it was too weak, not local pushback for
being too strong) — useful texture for the existing DeKalb corpus material.

---

## 7. New lead — Arizona Attorney General calls for a statewide pause; a second state-level official-track voice for the corpus, confirmed via her own office's press release

Found via general national sweep, confirmed via a direct-fetch of the **Arizona
Attorney General's own press release** (`azag.gov`, published **Monday, August
31, 2026**) — a genuine government-primary source, not news paraphrase:

- **Attorney General Kris Mayes** is calling on the Legislature and **Gov. Katie
  Hobbs** to pass legislation **pausing new data center approvals** statewide,
  pending an industry management plan. Direct quote: "The only sane thing to do
  is to pause the approval of new data centers."
- Cited rationale: rising energy bills, a **~30% Colorado River water-supply
  cut**, a projected **450%+ surge** in data-center water demand for greater
  Phoenix, and that air-cooled facilities can raise nearby ambient temperatures
  up to 4°F.
- Ties directly to a specific project: **Menlo Digital's** planned hyperscale
  data center in **Ahwatukee** (a Phoenix neighborhood) — the AG's office
  announced a **town hall Oct. 14** in Ahwatukee to gather community input on that
  project specifically.
- No enforcement mechanism or legal authority is claimed in the release itself —
  this is Mayes using her office's public voice to call for legislative action,
  not (yet) litigation or a formal regulatory action.
- Context already in the corpus (08-16 scan) that this connects to: Arizona's
  Legislature already passed a **3-year pause on the state's data-center tax
  incentives** in its FY2026 budget (Gov. Hobbs + GOP legislative leaders) — the
  AG's ask is a *further*, broader step (pausing approvals themselves, not just
  tax breaks).

**Read for the paper:** this is a second state-level-official lead (alongside NH's
governor) surfacing in less than a week — worth watching as a possible pattern
(state AGs/governors, not just county commissioners and city councils, entering
the fight) if the national design ends up wanting that as its own category.
**Oct. 14 Ahwatukee town hall is a concrete future date** worth a follow-up
check.

---

## For Britton — plain summary of what moved and what didn't

- **Sabey/Decatur:** still no outcome for the Aug. 20 hearing, now four
  consecutive nightly checks across every reasonable search angle and several new
  ones (UniCourt, the project's own site, IBJ's lawsuit archive). Treat this as a
  standing information gap. One incidental find: Sabey's own Aug. 27 press
  release now says construction starts Q2 2027, later than earlier "2026
  groundbreaking" language — not a litigation signal, just a timeline note.
- **MO/NV court access:** still blocked, but I found *why* more precisely for
  Nevada tonight — the Washoe County court's own case-search portal
  (`caseinfo.washoecourts.com`) exists and is reachable, but its search form is
  explicitly CAPTCHA-gated, a different and harder block than the Cloudflare/WAF
  issue on DocumentCloud that 09-05 documented. Missouri's `courts.mo.gov` is
  still a flat 403. Both need your own browser session to move further.
- **New Hampshire:** much richer than 09-07 knew — this is now a real,
  multi-official, cross-party (Republican governor + several Democrats),
  election-year fight, not just one quote from the governor. Four distinct
  concrete proposals are in play. One factual discrepancy flagged, not resolved:
  sources disagree on whether the Merrimack Station coal plant closed in Sept.
  2025 or is closing in 2028 — worth checking before citing a specific date.
- **Imperial County, CA:** no resolution yet on either tentative ruling — but now
  confirmed directly from the county's own press releases (not just news) that
  they're actively redrafting a legally-compliant moratorium, just with no board
  date set yet.
- **Two general-sweep finds worth your attention:** (1) Coweta County GA's
  Project Oak denial now has an on-record commissioner rationale (zoning
  consistency, not blanket anti-data-center) — nuances the "opposition win"
  framing a bit. (2) DeKalb County GA's moratorium, which the corpus's existing
  developer-suit material doesn't fully explain, is now clearly stable through
  March 2027 (not an imminent cliff), and the story behind its stalled permanent
  ordinance is that residents said it was too weak, not that it faced pushback
  for being too strong.
- **New lead: Arizona's Attorney General** (Kris Mayes) publicly called for a
  statewide pause on data center approvals Aug. 31, tied to a specific Ahwatukee
  project (Menlo Digital) and an Oct. 14 town hall — a second state-official-level
  voice for the corpus alongside New Hampshire's governor, confirmed via her own
  office's press release.
- **Nothing here touches the national-scope corpus/design restructuring
  question** (region-as-moderator) — still your call, per the README, untouched
  tonight.
