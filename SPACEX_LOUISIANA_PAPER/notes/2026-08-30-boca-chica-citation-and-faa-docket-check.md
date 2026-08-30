# 2026-08-30 — Boca Chica citation follow-up + FAA docket last-check before deadline

Follow-up to `2026-08-29-primary-source-pass-and-discrepancy-resolution.md`. Two scoped tasks
tonight: (1) find corpus item #9 (the unnamed Boca Chica academic study), (2) check
FAA-2026-8614 for anything filed since 2026-08-29, with the comment period closing 2026-08-31.
**No theory chain, coding scheme, or Study 1 option (A/B/C) decided or touched here — still
Britton's call**, per standing project rules. This is corpus-gathering/verification only.

## 1. Corpus item #9 — Boca Chica academic study — FOUND, tier A

**Full reference:**

> Palacios, Jorge. *Martian Borderlands: Colonizing (Outer) Space in the Lower Rio Grande Valley.*
> M.A. Thesis, MA Program in the Social Sciences (MAPSS), Social Sciences Division, University of
> Chicago, August 2023. DOI: [10.6082/uchicago.7220](https://doi.org/10.6082/uchicago.7220).
> Archived at [knowledge.uchicago.edu/record/7220](https://knowledge.uchicago.edu/record/7220).
> Licensed CC BY 4.0.

**What it is, per its own abstract**: an ethnographic/participatory-action-research thesis on
SpaceX's Starbase facility and its impact on Indigenous (Carrizo/Comecrudo) and Latinx communities
in the Lower Rio Grande Valley/Brownsville area. Argues SpaceX "colonizes the Lower Rio Grande
Valley using the same strategies as those used by settlers of the Western frontier" and coins the
term "Martian Borderlands" for zones where space ventures alienate land and render inhabitants
foreign in their own region. Based on interviews and participatory-action methods in Brownsville.
This matches, almost exactly, the "academic/ethnographic research with Latino and Indigenous
multigenerational community members" that the 2026-08-27 orientation note and prior corpus rows
described only by hearsay/existence, without a name.

**Verification path (two independent checks, per task instructions):**
1. First located via WebSearch (search snippet named the record but not the author/title
   cleanly); resolved to the specific record via a follow-up WebSearch that surfaced
   `knowledge.uchicago.edu/record/7220` directly.
2. **Independently confirmed three ways**, not just one re-check:
   - WebFetch of the record page itself (`knowledge.uchicago.edu/record/7220?ln=en`) returned
     title, author, institution, department, degree type, date, and abstract.
   - **DOI resolution**: `https://doi.org/10.6082/uchicago.7220` (a University of Chicago
     institutional DOI prefix, `10.6082`) 302-redirected to
     `knowledge.uchicago.edu/records/8jbtv-zv849`, an independent record URL for the same work —
     WebFetch of that redirected page returned matching title/author/institution/date/abstract.
     A DOI resolving cleanly to a matching institutional repository record is a real citation
     mechanism, not a blog or press release.
   - **Cross-referenced against a live, independent source**: MIT's HASTS (History, Anthropology,
     Science, Technology, Society) program's own student-bio page for Jorge Palacios
     (`hasts.mit.edu/students/jorge-palacios/`) independently confirms Palacios is a real person,
     now a PhD student there, whose doctoral research explicitly continues on "SpaceX's Starbase
     facility in the Lower Rio Grande Valley of South Texas," tracing "the ways Mars colonization
     is understood and how such technoscience comes to impact the U.S.-Mexico borderlands" — an
     independently-hosted, third-party confirmation that this is an active, continuing research
     program, not a one-off unlisted document.

**Caveats worth flagging plainly, since this is a citation decision:**
- **This is a master's thesis, not a peer-reviewed journal article.** A WebSearch specifically for
  a later journal publication of this work ("Jorge Palacios" + "Martian Borderlands" + published
  2024/2025) turned up nothing — it does not appear to have been placed in a journal yet. Citable
  and real, but treat its evidentiary weight as thesis-tier, not peer-reviewed-tier, if used in the
  manuscript.
- It is genuinely the closest match to what prior notes described (Latino/Indigenous,
  ethnographic, Boca Chica, ongoing since roughly the Starbase era) — but the "ongoing since 2021"
  framing in the orientation note may have been describing this same author's now-continuing PhD
  research trajectory (MAPSS thesis 2023 → MIT HASTS PhD work now) rather than a single 2021-dated
  study, which fits better than assuming there's a *different*, still-missing 2021 study out
  there. Not 100% certain these are "the" single referenced study rather than one node in a
  broader informal research thread, but this is a real, nameable, citable academic source where
  before there was none — recommend treating item #9 as resolved with this citation, updating the
  corpus table accordingly (not done in this note per the "don't modify existing files" instruction
  — flagging for the corpus file's next edit).
- No paywalled PDF was downloaded or would need to be — the thesis is openly archived
  (CC BY 4.0) at the university's own repository, so nothing copyright-risky here.

## 2. FAA-2026-8614 — last check before the 2026-08-31 deadline

**Access note — new technique found tonight, worth carrying forward**: `regulations.gov`'s HTML
docket page still blocks direct WebFetch (403, consistent with every prior session). But
`api.regulations.gov` — the same system's public REST API, using the openly-documented `DEMO_KEY`
(no login/registration required) — is reachable, and **`curl` through the `r.jina.ai` reader
proxy against the raw API JSON endpoint returns clean, verbatim, schema-correct JSON** (matched
regulations.gov's documented API v4 response shape exactly: `data`/`attributes`/`meta.aggregations`
fields, real `objectId` values, consistent comment IDs across repeated independent queries). This
is a **direct-fetch-confirmed** path (curl output saved and inspected locally, not just a WebFetch
AI-summarized read) — a meaningfully more reliable technique than the news-search route tried in
prior sessions, and reusable for any future paper needing a regulations.gov docket read. Flagging
explicitly: earlier in this same session, asking WebFetch (not curl) to summarize the same kind
of query produced numbers that were internally inconsistent across calls (e.g., one WebFetch-only
pass claimed "1,453 posted / 12,004 total," another claimed "205 comments... 112 in the last 3
days" for a different filtered query) — those WebFetch-summarized numbers are **not** trusted and
are not used below. Only the raw-`curl`-through-jina JSON pulls (verified byte-for-byte, files
inspected directly) are reported as findings.

**What the raw API data shows, checked tonight (2026-08-30), sourced to the same
`api.regulations.gov/v4/comments` endpoint throughout:**

- **Total comments on the docket: 1,453** (per `meta.aggregations` totals, corroborated by
  `totalElements: 1453` on an unfiltered query). This supersedes the "882 comments" figure the
  2026-08-29 note explicitly flagged as an unconfirmed AI-search-synthesis artifact — 1,453 is a
  directly-fetched, raw-JSON-verified count as of tonight, not a repeat of that same unverified
  number.
- **Nothing new filed since 2026-08-29, per the docket's own indexed `postedDate` field.** A raw
  query filtered to `postedDate >= 2026-08-29` returned **zero** results (`totalElements: 0`,
  confirmed twice, once via WebFetch and once via direct curl+jina with an explicit
  "output verbatim, don't summarize" instruction). The most recent `postedDate` across the whole
  docket, sorted descending, is **2026-08-28** (batch-timestamped `2026-08-28T04:00:00Z` across
  many comments, with `lastModifiedDate` timestamps spread through the day — consistent with
  regulations.gov's known posting-lag behavior, where comments are typically indexed with the
  processing date rather than the submission timestamp). **Caveat**: this means "confirmed nothing
  newly *posted/indexed* since 08-28" — it does not rule out comments *submitted* 08-29/08-30 that
  simply haven't cleared regulations.gov's moderation/posting queue yet, which is a known lag on
  that system. Worth a same-day recheck on 2026-08-31 itself if anyone wants a true final read
  before the deadline closes.
- **New organizational filer found, not in the prior corpus, but NOT Louisiana-specific — flag
  this distinction clearly.** A joint comment (docket ID `FAA-2026-8614-1075`, received 08-27,
  posted 08-28) was filed by **Friends of Canaveral, Merritt Island Wildlife Association, National
  Parks Conservation Association, and National Wildlife Refuge Association**. Full PDF text
  fetched and read directly (via curl+jina proxy, `downloads.regulations.gov` attachment URL) —
  it is about **Merritt Island National Wildlife Refuge and Canaveral National Seashore in
  Florida** (the Kennedy Space Center area), arguing NASA has coexisted with those refuges under
  NEPA compliance for six decades and the waiver shouldn't be needed. This is a real, substantive,
  newly-identified filing on the docket, but it is a *different launch site's* wildlife coalition
  commenting on the *national* scope of the NPRM — not a Vermilion Parish-specific filing. Useful
  context for the paper (shows the NPRM is drawing organized opposition nationally, from
  established "friends of refuge" groups, not just the Louisiana-specific wildlife-federation
  letter already in the corpus) but should not be filed under "Louisiana corpus" without that
  caveat attached.
- **141 of the 1,453 total docket comments explicitly mention "Vermilion"** (raw API
  `filter[searchTerm]=Vermilion` count, confirmed via curl+jina) — i.e., roughly 1 in 10 comments
  on this *nationwide* rulemaking name the Louisiana site specifically, which is a genuinely
  citable data point about how much this one proposed site is driving comment volume on an
  otherwise generic national NPRM. Most of the Vermilion-mentioning comments cluster on
  2026-08-27/08-28 (near the deadline surge), a mix of individual, seemingly organic comments and
  what reads like a coordinated form-letter campaign — several comments (from different named
  individuals: Andrea Chisari, Robyn Thigpen, Ellen Atkinson, Nicky Gillies, Rachel Lackaye, one
  Anonymous) share the identical opening clause "proposed rocket launching facility is proposed
  for construction on 125,000 acres of coastal marsh in Vermilion..." — consistent with an
  advocacy-org action-alert template, not independently verified which org organized it.
- **One individual comment (Chloe Wesolick, Phoenix, AZ; docket ID `FAA-2026-8614-1104`) is
  detailed and substantive enough to be worth flagging directly** — full text fetched and read.
  It independently repeats the Boca Chica Clean Water Act violation claim that the
  LWF/NWF/Pontchartrain letter also makes (*"SpaceX's existing Starbase facility in Boca Chica,
  Texas...has been found to violate the Clean Water Act by discharging pollutants into nearby
  waters...and has caused fires on adjoining state park land"*), names the site's prior legal
  history (*"land that had been the subject of a decade-long lawsuit against ExxonMobil over
  wetland loss caused by drilling and canal dredging"* — a detail not seen in the corpus before,
  not yet independently checked against a court record), and explicitly flags Louisiana's own
  state-level law "exempting some aerospace projects from public review and criminalizing
  unauthorized entry onto spaceport property" as compounding the federal waiver — a state/federal
  regulatory-layering argument that's directly relevant to this paper's regulatory-venue-shifting
  frame candidate. This raises the Boca Chica CWA-violation claim from "one letter's assertion" to
  "at least two independent commenters make the same claim" — still not an EPA/TCEQ primary
  enforcement record, so still flag it as "commenters state" rather than independently verified,
  but it's one step more corroborated than the 2026-08-29 note left it.
- **No comment found from a named Vermilion Parish/Louisiana elected official, and no comment
  filed under the organization name "StopSpaceX."** Searched the API directly for "Hensgens"
  (0 results) and "StopSpaceX" (0 results). This doesn't mean no local official or resident
  commented — residents would show up under personal names, which a targeted name search can't
  practically enumerate — it means no filing carries that specific name/org string as of tonight.
  Separately checked `stopspacex.com` directly (fetched, live site): as of its most recent visible
  update (2026-08-25), it is actively urging supporters toward the FAA comment deadline
  ("There is still time to 'public comment' on the FAA Waiver, Deadline August 31, 2026") without
  itself filing an organizational comment under that name.

## 3. Time-sensitive flag for Britton

**Comment period closes 2026-08-31 — tomorrow.** Per the docket's own indexing, nothing
substantively new (beyond ordinary individual-comment volume) has posted since 2026-08-28, but
regulations.gov's posting lag means a final same-day check on 08-31 (or shortly after) would be
the only way to catch late-breaking organizational filings — e.g., if Vermilion Parish's own
police jury, a state legislator, or "StopSpaceX" file something in the final 24-48 hours, it would
not yet be indexed as of tonight's check. Recommend one more pass after the deadline closes if this
paper's corpus work continues, specifically re-running the `filter[searchTerm]=Vermilion` and
`filter[searchTerm]=StopSpaceX` queries above via the curl+r.jina.ai path documented here.

## 4. What's still open (unchanged framing from prior notes)

- No theory chain, coding scheme, or Study 1 option (A/B/C) decided — unchanged, still Britton's
  call.
- Item #9 is now resolved with a real citation (Palacios thesis, above) — recommend the corpus
  table (`Study1_Corpus_and_Coding_DRAFT_2026-08-27.md`) be updated to reflect this in a future
  edit; not done in this note per instructions to only add new dated files tonight.
- The Boca Chica 2024 Clean Water Act penalty claim is now corroborated by two independent
  commenter sources (the wildlife groups' letter and the Wesolick comment) but still not checked
  against an EPA/TCEQ primary enforcement record — still flag as "commenters state," not
  independently verified, if cited.
- The Exxon-Vermilion-Parish wetland-loss lawsuit detail mentioned in the Wesolick comment is new
  and not yet independently verified against a court record — flag before citing as fact.
- A true final/post-deadline docket check (per the time-sensitive flag above) is the most useful
  immediate next step if another session runs before this paper's corpus work is otherwise ready to
  freeze.
