# FAA docket FAA-2026-8614 — post-close comment batch analysis

2026-09-02. Follow-up to 2026-09-01's close-of-comment-period check (docket closed
2026-09-01T03:59:59Z; 2,785 posted / 14,669 received at that time).

## Posted count moved up

Confirmed directly via the regulations.gov public API (`api.regulations.gov/v4/comments`,
`filter[docketId]=FAA-2026-8614`):

- **Posted comments: 2,785 → 3,200** (+415).
- All 415 new comments carry `postedDate: 2026-09-01T04:00:00Z` (a placeholder), but real
  `lastModifiedDate` values cluster in a **~2.5-minute window, 2026-09-01T17:15:33Z–17:17:55Z**
  (~12:15–12:18pm CDT) — a single automated moderation-queue release, not organic trickle.
- **Zero comments posted with `postedDate ≥ 2026-09-02`** — confirmed directly. The posted count has
  been flat at 3,200 since Sept 1 afternoon; nothing new as of today's check.
- **"Vermilion"-mentioning posted comments: 345 → 406** (+61, ~15% of the new batch).

**"Total received" (14,669 baseline) could NOT be re-verified or updated.** That figure isn't exposed
by the public regulations.gov v4 API (only posted-comment totals are). The docket's public page is a
client-side app backed by internal endpoints that returned 403/empty-shell to automated access. Report
this as **unverified**, not as unchanged — the posted-vs-received gap may have narrowed, held, or grown
and we don't currently know which.

## New batch composition — a distinct institutional layer, not just individuals

Pulled all 415 titles/submitters (321 unique names) and read 9 full comment texts as a sample.

- **86 "Anonymous" submissions** (~21% of the batch).
- **~309 apparent individual named submitters**, surnames skewing heavily Acadiana/south Louisiana
  (Broussard, Theriot, Hebert, Vidrine, Guidry, etc.) — consistent with local/regional grassroots
  participation. All 9 full texts sampled were distinctly worded, personal letters, not shared
  boilerplate (e.g., Caleb Theriot: "lifelong resident of Acadiana... I strongly oppose Docket
  FAA-2026-8614"; Rosalind Hinton citing "debris and destruction these space launches have brought to
  Texas"; Virginia Walcott on Pecan Island bird migration; Dandy Weeden on wetlands harm; Susan Cooper
  invoking decades of oil-industry impact on the state; Todd Mouton on NEPA/Clean Water Act). Caveat:
  9 of 415 read, not a full-batch similarity audit — a templated sub-cluster among the rest can't be
  ruled out from this sample alone.
- **At least 26 organizational/institutional filings — new and corpus-relevant:**
  - **Commercial space industry, including competitors and SpaceX itself:** Space Exploration
    Technologies Corp. (SpaceX's own legal name), Blue Origin LLC, Rocket Lab USA Inc., Stoke Space
    Technologies Inc., Relativity Space, Alaska Aerospace Corporation, Commercial Space Federation
    (industry trade group), an entry titled "US Space Industry."
  - **National/regional environmental & wildlife groups (several not previously reported by name):**
    National Audubon Society, Orange Audubon Society, Surfrider Foundation (3 entries), Defenders of
    Wildlife (4 entries), Save the Manatee Club, NRDC, Southern Environmental Law Center, Healthy Gulf,
    Louisiana Environmental Action Network (2 entries), Friends of San Pablo Bay National Wildlife
    Refuge, Baton Rouge Group of the Sierra Club. ("Golden Eagles' Conservation Society" also appears —
    name unfamiliar, worth independent verification before citing.)
  - **Government bodies:** a joint filing from CA Attorney General/CalEPA/CA Natural Resources
    Agency/CA Coastal Commission/CDFW; California Air Resources Board; Santa Barbara County Air
    Pollution Control District; "Agencia de Transformación Digital y Telecomunicaciones (ATDT)"
    (appears to be a Puerto Rico digital/telecom agency — relevance unclear, flag for review).
  - **Academic:** Tulane Institute on Water Resources Law & Policy.
  - **Aviation-noise advocacy groups unrelated to Vermilion specifically:** "ATL Neighbors Needing
    Quiet Skies (ANNQS)," "Trenton Threatened Skies" — these appear to be commenting on the national
    NEPA-waiver precedent generally, which helps explain why only ~15% of the new batch names
    "Vermilion" by name.
  - **Local Louisiana business/civic:** LifeCity, Natural Resource Professionals LLC.

**Overall read:** the new batch looks like two things released together at moderation-queue close —
a wave of last-minute institutional/legal filings (aerospace competitors, national environmental
NGOs, out-of-state government agencies commenting on the national precedent) plus continuing organic
individual, Louisiana-flavored personal comments. It does not look like a single organized form-letter
campaign based on the sample read.

## No news coverage found characterizing the surge

Multiple targeted searches (surge figures, "Stop SpaceX," named orgs, post-9/1 coverage) found no
article published on/after 2026-09-01 characterizing the surge's volume or composition, or referencing
the specific figures (2,785, 1,453, 14,669, 3,200). One relevant lead: a profile piece ("'Louisiana Is
Not a Launchpad': Inside the Revolt Against Elon Musk's $100B Starbase," trendingtopics.eu) describes a
"Stop SpaceX" coalition (residents, hunters, conservation groups, scientists, outdoor-economy
businesses, some elected officials) that was "directing its supporters" to submit FAA comments during
the open window — circumstantial support for an organized-but-organic push, not form-letter-vendor
astroturfing, but the article gives no comment counts and doesn't name the docket. This remains an
evidence gap: nothing quantifies who organized the surge or at what scale.

## For Britton

- Posted comments now 3,200 (from 2,785), all released in one batch Sept 1 afternoon; nothing new
  since. Total-received figure (14,669) is currently unverifiable via the public API — a real gap, not
  a stable figure to keep citing without a caveat.
- The institutional-filer list (SpaceX itself, Blue Origin/Rocket Lab/other launch competitors,
  national environmental NGOs, a California state-agency coalition) is new corpus material worth
  deciding whether/how to fold into the design — these are qualitatively different commenters than the
  individual-resident-heavy "Vermilion surge" characterized 09-01, and could matter for a
  stakeholder-diversity or coalition-breadth framing.
- Comment-composition/organizer identity remains an open evidence gap — no news source has
  characterized it, and the "Stop SpaceX" coalition lead carries no quantitative backing yet.
- No theory chain assigned to any of tonight's findings — still your call, same as every prior night.
