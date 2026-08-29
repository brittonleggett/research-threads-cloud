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
| 4 | Louisiana Wildlife Federation, National Wildlife Federation, Pontchartrain Conservancy | Joint FAA comment letter (PDF, directly hosted) | 2026-08-24 | **A — UPGRADED 2026-08-29**: full text extracted directly (`curl` + `pdftotext`, poppler-utils installed this session) and cross-checked against an independent extraction path (r.jina.ai reader proxy on the same URL); both agree. See notes/2026-08-29 for full extracted text and summary. | [lawildlifefed.org PDF](https://lawildlifefed.org/wp-content/uploads/FAA-Comment-Letter-8-24-2026-LWF_NWF_PC.pdf) |
| 5 | FAA | NPRM "Waiver of Specified Statutory Requirements for Commercial Space Launch and Reentry Actions," Docket No. FAA-2026-8614, Notice No. 26-11, RIN 2120-AM51 (waives NEPA/ESA/CWA/CAA/NHPA/MMPA + 7 more statutes for commercial launch/reentry licensing) | Federal Register notice 2026-07-30; comments due on or before **2026-08-31** | **A — UPGRADED 2026-08-29**: docket number, notice number, RIN, and comment deadline all confirmed directly from the Federal Register's own PDF (govinfo.gov mirror, fetched via `curl`+`pdftotext` after federalregister.gov and regulations.gov both continued to block WebFetch/bot access). Independently corroborated by the docket number cited in the wildlife groups' own comment letter (#4). | [Federal Register PDF via govinfo.gov](https://www.govinfo.gov/content/pkg/FR-2026-07-30/pdf/2026-15415.pdf) (regulations.gov docket page itself still not directly loadable: [regulations.gov/docket/FAA-2026-8614](https://www.regulations.gov/docket/FAA-2026-8614)) |
| 6 | Louisiana Illuminator | News coverage of the wildlife-groups' opposition | 2026-08-25 | A (news article itself fetched/read) | [lailluminator.com](https://lailluminator.com/2026/08/25/wildlife-spacex/) |
| 6b | Louisiana Illuminator | "Pecan Island residents fight to be heard on SpaceX" — reports LED required elected officials to sign NDAs (State Rep. Jacob Landry signed one in Feb. 2026; State Sen. Bob Hensgens signed then rescinded), residents first noticed survey crews ~Aug. 10, formed "StopSpaceX" group | 2026-08-19 | A — fetched via reader-proxy after direct site 403 (see notes/2026-08-29); content plausible/internally consistent, treat as A-minus pending a second independent confirmation of the NDA detail specifically | [lailluminator.com/2026/08/19/pecan-island-spacex](https://lailluminator.com/2026/08/19/pecan-island-spacex/) |
| 6c | KPLC (Lake Charles CBS affiliate) | "'Landry really stabbed us in the back' — Pecan Island residents still concerned after SpaceX announcement" — direct resident quotes on lack of warning, eminent-domain fear, noise/Boca-Chica comparison, crabbing-business livelihood concern | 2026-08-26 | A (fetched directly) | [kplctv.com](https://www.kplctv.com/2026/08/26/landry-really-stabbed-us-back-pecan-island-residents-still-concerned-after-spacex-announcement/) |
| 6d | Fox 8 Live (WVUE New Orleans) | "Some Pecan Island residents complain they were left in the dark about SpaceX project" — resident Crystal Mhire quote on outreach failure | 2026-08-26 | A (fetched directly) | [fox8live.com](https://www.fox8live.com/2026/08/26/some-pecan-island-residents-complain-they-were-left-dark-about-spacex-project/) |
| 6e | Louisiana Economic Development | Official press release (distinct URL from the /spacex program page, #1 above) — confirms $25M Community Foundation of Acadiana donation, PILOT terms, no coastal-master-plan dollar figure | 2026-08-25 | A (fetched directly) | [opportunitylouisiana.gov/news/...](https://www.opportunitylouisiana.gov/news/spacex-launches-new-era-of-commercial-spaceflight-with-100-billion-louisiana-campus) |
| 6f | The Current (Lafayette) | Live-blog of the Aug. 25 press conference in Abbeville — contemporaneous, timestamped reporting; the only source located that attributes a specific "$100 million coastal master plan" figure to a direct Landry statement to press (see notes/2026-08-29 for the $25M/$100M reconciliation) | 2026-08-25 | A — fetched via reader-proxy after direct site 403 (flagging the proxy-mediated path per repo verification norms) | [thecurrentla.com/2026/live-is-spacex-coming-to-pecan-island](https://thecurrentla.com/2026/live-is-spacex-coming-to-pecan-island/) |

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

## Update — 2026-08-29 primary-source pass

See `notes/2026-08-29-primary-source-pass-and-discrepancy-resolution.md` for full detail. Summary
of what changed in this table:
- **#4 (FAA comment letter) and #5 (FAA docket) both upgraded C/B → A.** Working PDF text
  extraction (poppler-utils `pdftotext`) was available this session; both documents were pulled
  and read in full, not paraphrased from search snippets.
- **New rows 6b-6f added**: local-resident opposition/transparency material (NDAs signed by
  elected officials, "StopSpaceX" group, direct resident quotes) that the earlier corpus pass
  didn't have — this is genuinely new Option-B-relevant material, distinct from the wildlife-group
  filing angle already in the table.
- **The $25M vs. $100M discrepancy flagged on 2026-08-27 is now resolved** (moderate-high
  confidence): both figures are real and distinct. See the dedicated notes file for sourcing and
  reasoning — not restating the full analysis here to avoid the table drifting out of sync with
  the notes file.
- No theory chain, coding scheme, or Study 1 option decided — same standing rule as before.
