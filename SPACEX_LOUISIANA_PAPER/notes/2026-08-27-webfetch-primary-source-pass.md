# 2026-08-27 (evening) — First WebFetch primary-source pass

Follow-up to the same-day orientation note, which was WebSearch-sourced only. This session's
WebFetch works (unlike the cloud routine's, which was EGRESS_BLOCKED for 17+ nights until fixed
tonight) — used it to upgrade several facts to primary-source confidence.

## Upgraded to primary-verified

**Louisiana Economic Development's own page** (opportunitylouisiana.gov/spacex) fetched directly.
Confirms and refines the WebSearch-sourced figures from the orientation note, with some real
differences worth flagging rather than silently merging:
- $100 billion investment — confirmed.
- Jobs: 3,000 direct over 10 years, ~8,100 indirect, $92,600 average annual salary — confirmed
  exactly as previously reported.
- **Fiscal terms are more specific than previously recorded**: $20 million upfront PILOT payment;
  a **minimum $25 million annually for 25 years (totaling $825+ million)** — the orientation
  note's "$25M/year flat" was right on the annual figure but didn't have the 25-year/$825M+ total
  framing. **New/different figure**: LED's own page names a **$25 million charitable donation to
  the Community Foundation of Acadiana** — this does not match the earlier-reported "$100M to the
  state's coastal master plan" figure from news coverage. Both may be real (a charitable donation
  and a separate coastal-master-plan commitment aren't necessarily the same line item), but this
  needs reconciling before either figure is treated as settled — flagging the discrepancy plainly
  rather than picking one.
- Infrastructure: five launch complexes with two launch pads each at full buildout, plus
  propellant farms, a production facility, and employee housing — new detail not in the
  orientation note.
- Timeline: construction beginning by end of 2027 (orientation note said "starting 2027," now
  more precisely "by end of 2027"); first launch targeted 2029 — confirmed.
- Quotes confirmed on LED's own page: Gov. Landry — "We have the people, the ingenuity and the
  work ethic to build things the rest of the world once thought impossible." Musk — "Starbase,
  Louisiana will unlock that future" (re: routine space access).

**Found the actual FAA docket comment letter — a real primary source, not yet readable this
session.** The Louisiana Wildlife Federation / National Wildlife Federation / Pontchartrain
Conservancy joint comment letter is a real, directly-hosted PDF:
`https://lawildlifefed.org/wp-content/uploads/FAA-Comment-Letter-8-24-2026-LWF_NWF_PC.pdf`
(dated 2026-08-24, submitted electronically via regulations.gov, per its own title). WebFetch
pulled the raw file (433KB, saved locally) but could not extract readable text from it — the
tool reported binary/compressed PDF content it couldn't parse, and this environment's `Read`
tool couldn't render it either (`pdftoppm`/poppler-utils not installed). **This is a real,
confirmed-to-exist, directly-hosted PDF that just needs a working PDF text-extraction path** —
worth a retry in a session with better PDF tooling, or a direct download for Britton to open
locally, before assuming the content itself needs re-chasing. Do not re-search for this letter;
its existence and URL are confirmed.

**FAA docket identified via WebSearch, not yet directly confirmed on a docket page**: search
results point to docket **FAA-2026-8614** as the relevant proposed-rule docket (would waive 13
laws governing commercial launch/reentry licenses — NEPA, Endangered Species Act, Clean Water
Act, Clean Air Act, National Historic Preservation Act — with a public-comment window that
appears to run through 2026-08-31). This docket number came from a WebSearch summary, not a
directly fetched regulations.gov page (regulations.gov itself returned 403 to a direct WebFetch,
likely bot-blocking) — treat the docket number as WebSearch-confidence only until someone can
load regulations.gov directly (browser session, not WebFetch) and confirm FAA-2026-8614 is real
and pulls up the actual docket.

## Still blocked / not found

- **Cameron County's own Starbase economic-impact materials**: both `myrgv.com` and
  `valleycentral.com` (the two outlets covering Cameron County's release of its own stats)
  returned 403 to direct WebFetch. The $800M figure and the underlying academic/ethnographic
  community-impact research mentioned in the orientation note remain WebSearch-summarized only —
  not upgraded tonight.
- **SpaceX's own site** (spacex.com/updates): JS-rendered, WebFetch got no usable content. No
  official SpaceX statement pulled directly; LED's page is the only primary source obtained
  tonight, not a SpaceX-authored one.

## What this doesn't do

No theory-chain, corpus-option (A/B/C), or Study 1 design decision made or implied — that's
still open per the orientation note, still Britton's call. This is fact-verification only.
