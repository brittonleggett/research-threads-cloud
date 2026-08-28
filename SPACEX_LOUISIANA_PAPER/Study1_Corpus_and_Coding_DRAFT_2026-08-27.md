# SpaceX Vermilion Parish Spaceport — Study 1 Corpus (DRAFT, corpus-building only)

**No theory chain, coding scheme, or Study 1 option (A/B/C, see `notes/2026-08-27-orientation.md`)
is decided here — this file only inventories candidate artifacts with sources, so a corpus
exists to code once Britton picks a direction.** Confidence tiers follow the same convention as
TARIFF_PAPER/DATA_CENTER_PAPER: A = primary-fetched, B = search-summarized pending re-fetch,
C = existence-confirmed but content not yet extracted.

## Louisiana side (corporate/official messaging — candidate Option A material)

| # | Source | Type | Date | Tier | Link |
|---|--------|------|------|------|------|
| 1 | Louisiana Economic Development | Official program page (investment/jobs/fiscal terms) | current as of 2026-08-27 | A | [opportunitylouisiana.gov/spacex](https://www.opportunitylouisiana.gov/spacex) |
| 2 | Gov. Jeff Landry | Public quote, via LED page | 2026-08-25 announcement | A | (same LED page above) |
| 3 | Elon Musk | Public quote/video, via LED page + news coverage | 2026-08-25 | A (quote) / B (video itself not directly fetched) | (same LED page above); [TechCrunch](https://techcrunch.com/2026/08/25/spacex-will-build-a-second-100b-starbase-spaceport-in-louisiana/) |

## Louisiana side (opposition/regulatory — candidate Option B material)

| # | Source | Type | Date | Tier | Link |
|---|--------|------|------|------|------|
| 4 | Louisiana Wildlife Federation, National Wildlife Federation, Pontchartrain Conservancy | Joint FAA comment letter (PDF, directly hosted) | 2026-08-24 | C — confirmed real/hosted, text not yet extracted (WebFetch pulled raw bytes; local PDF-render tooling unavailable this session) | [lawildlifefed.org PDF](https://lawildlifefed.org/wp-content/uploads/FAA-Comment-Letter-8-24-2026-LWF_NWF_PC.pdf) |
| 5 | FAA | Proposed rule docket (waives NEPA/Endangered Species Act/Clean Water Act/Clean Air Act/National Historic Preservation Act reviews for commercial launch sites) | comment period through ~2026-08-31 | B — docket number FAA-2026-8614 identified via WebSearch only, not confirmed on a directly-loaded regulations.gov page (regulations.gov 403'd WebFetch) | not yet a confirmed direct link — needs a browser session, not WebFetch, to load regulations.gov |
| 6 | Louisiana Illuminator | News coverage of the wildlife-groups' opposition | 2026-08-25 | A (news article itself fetched/read) | [lailluminator.com](https://lailluminator.com/2026/08/25/wildlife-spacex/) |

## Boca Chica, TX comparison corpus (candidate Option C material — the paper's built-in
comparison case)

| # | Source | Type | Date | Tier | Link |
|---|--------|------|------|------|------|
| 7 | Cameron County, TX | Self-released Starbase economic-impact stats (~$800M claim) | released 2024, covering prior period | B — WebSearch-summarized only; both outlets covering the release (myrgv.com, valleycentral.com) 403'd direct WebFetch tonight | [MyRGV](https://myrgv.com/publications/the-monitor/2024/06/21/spacex-claims-it-has-800m-impact-in-cameron-county/), [ValleyCentral](https://www.valleycentral.com/spacex/cameron-county-releases-starbase-local-impact-economic-stats/) |
| 8 | The Conversation | Academic-adjacent commentary on Starbase's landscape/community impact | 2026 | A (article itself fetched earlier tonight, see orientation note) | [theconversation.com](https://theconversation.com/the-starbase-rocket-testing-facility-is-permanently-changing-the-landscape-of-southern-texas-242450) |
| 9 | Unidentified academic/ethnographic research program | Ongoing community-impact research with Latino/Indigenous Boca Chica residents, referenced since 2021 | ongoing | C — existence referenced by search summaries, the specific researcher(s)/institution/publication not yet identified | not yet found — needs a follow-up pass specifically searching for the named study, not just news mentions of "academic research has been conducted" |

## What's still needed before this is a workable Study 1 corpus

1. **Extract the FAA comment-letter PDF's actual text** (#4) — the file is confirmed real and
   saved locally; a session with working PDF-to-text tooling (or Britton opening it directly)
   should pull the specific species/habitat arguments rather than relying on news paraphrase.
2. **Confirm the FAA-2026-8614 docket number directly** (#5) — regulations.gov blocks WebFetch;
   this needs a browser-driven check (claude-in-chrome) rather than another WebFetch attempt.
3. **Identify the actual Boca Chica community-impact study** (#9) by name/author, not just its
   existence — several notes have referenced "academic research since 2021" without naming it.
4. Once Britton picks a Study 1 option (A/B/C from the orientation note), this table's scope
   narrows accordingly — right now it's deliberately broad across both corporate and opposition
   material.
