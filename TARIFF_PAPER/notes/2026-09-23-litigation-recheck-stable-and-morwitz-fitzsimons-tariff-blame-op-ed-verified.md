# 2026-09-23 — Litigation recheck (all four dockets fully unchanged since 09-22) + a verified new lead on the Columbia tariff-blame-attribution research thread flagged 09-22

## What this is (disclosure)

AI-assisted (Claude Code) autonomous overnight session. Three parts, same
scope as recent nights: (1) the standing four-docket litigation recheck;
(2) a literature-currency sweep for new 2025-2026 tariff-messaging/
consumer price-fairness/attribution-theory work, picking up specifically
on the unconfirmed Columbia Business School lead flagged in the 09-22
note; (3) a quick public-information recheck on the two SUBMISSION_TRACKER.md
items (CITI module, HSIRB turnaround) per tonight's task scope.

## 1. Litigation recheck — all four dockets fully unchanged since 09-22

Same four CourtListener docket URLs as every prior night, fetched via
plain `curl` with a browser User-Agent, parsed with `beautifulsoup4`
(installed fresh this session, as usual for this container):

1. Section 301 forced-labor master docket — `https://www.courtlistener.com/docket/74219533/in-re-section-301-forced-labor-cases/`
2. Section 122 appeal, *State of Oregon v. Trump* (CAFC 26-1804/-1805) — `https://www.courtlistener.com/docket/73318531/state-of-oregon-v-trump/`
3. V.O.S. Selections (CAFC 26-1895) — `https://www.courtlistener.com/docket/73433096/vos-selections-inc-v-trump/`
4. Axle of Dearborn (CIT 1:25-cv-00091) — `https://www.courtlistener.com/docket/70287201/axle-of-dearborn-inc-v-department-of-commerce/`

All four returned HTTP 200 with `x-cache: Miss from cloudfront` and
`date:` headers of `Wed, 23 Sep 2026 05:15:2[2-5] GMT` — matching
tonight's actual fetch time within 3 seconds across all four, confirming
fresh (not cached) responses.

| Docket | Entries 09-22 | Entries tonight | Change |
|---|---|---|---|
| Section 301 | 53 | 53 | None |
| Section 122 | 106 | 106 | None |
| V.O.S. Selections | 26 | 26 | None |
| Axle of Dearborn | 79 | 79 | None |

Extracted every entry ID present in each page (`id="entry-N"`) and
compared the max ID to last night's count — identical on all four.
Reread the last 1-2 entries on each docket directly (not just the
count) — text matches the 09-22 account verbatim:

- **Section 301**: entry #52 (Sep 18 plaintiffs' reply) and #53 (Sep 21
  Joint Appendix, 5 volumes) — unchanged.
- **Section 122**: entries #105-106 (Sep 18 corrected Cato/Somin amicus
  brief and same-day notice of correction) — unchanged. Government's own
  brief deadline still 11/12/2026 (not re-verified in the docket text
  tonight since nothing changed since it was directly confirmed 09-22;
  no order affecting it has posted).
- **V.O.S. Selections**: entry #25 (Sep 11 extension motion) and #26 (Sep
  15 text-only order granting it, response due 10/05/2026) — unchanged.
  **This deadline is now 12 days out** — checked specifically for any new
  activity given the "under two weeks out" flag from 09-22 and last
  night's note; still only 26 entries, nothing filed since the Sep 15
  order.
- **Axle of Dearborn**: entries #78-79 (Aug 25 stay/reliquidation order
  pair) — unchanged.

Checked all four dockets case-insensitively for "Date Terminated" or any
termination-status text — none found on any; all four remain open/active.

**Nothing new to report on litigation tonight.** The two dates worth
watching are unchanged from 09-22: **V.O.S. Selections' 10/05/2026
response brief (12 days out)** and **Section 122's 11/12/2026 government
brief (~7 weeks out)**.

## 2. Literature-currency sweep — a verified new lead on the Columbia tariff-blame-attribution thread

The 09-22 note flagged an *unconfirmed* lead: a Columbia Business School
"faculty awards" page describing a project titled "How Tariff Price
Presentation Affects Consumer Responses, Fairness Perceptions, and
Attitudes toward Firms and Government" — page gave HTTP 403 on direct
fetch, no author names found. Tonight, WebSearch surfaced a second,
related Columbia Business School page: **"Opinion: Rising prices upset
shoppers. Do retailers dare tell the truth about who's to blame?"** —
also 403'd on direct fetch (confirmed again tonight: both Columbia URLs
return an HTTP 403 with a Cloudflare bot-challenge response, `cf-mitigated:
challenge` — this is a real anti-bot block on Columbia's own site, not a
tooling failure on this end).

**Verified via a primary source instead: Vicki Morwitz's own official
Columbia Business School CV** (fetched directly,
`business.columbia.edu/sites/default/files-efs/person/cv/Morwitz_Vicki_CV_2025.pdf`,
"Revised December 2025," read via this session's PDF tool). Under
"Editorials and Op-Eds," verbatim:

> Morwitz, Vicki and Gavan Fitzsimons, "Rising Prices Upset Shoppers. Do
> Retailers Dare Tell the Truth about Who's to Blame?" *Market Watch*,
> September 3, 2025.

This confirms as **real and verified, directly from the author's own CV
(not inferred from a search snippet):**
- **Vicki G. Morwitz** — Bruce Greenwald Professor of Business, Columbia
  Business School (Columbia since 2019, previously NYU Stern; PhD
  Wharton 1991) — a senior, highly-credentialed consumer-pricing-
  psychology scholar (former JCR co-editor 2014-2017, former JACR
  editor-in-chief 2021-2024), with a decades-long research line
  specifically on partitioned pricing, drip pricing, and surcharges —
  i.e., exactly the "who's responsible for this added cost" attribution
  question this project's theory chain also turns on.
- **Gavan Fitzsimons** (Duke Fuqua, Edward S. & Rose K. Donnell
  Professor of Marketing and Psychology) as co-author — confirmed as a
  real, established consumer-psychology scholar via Duke's own faculty
  page (fuqua.duke.edu/faculty/gavan-fitzsimons); a Fuqua-affiliated
  LinkedIn post referencing this same op-ed's title was also found,
  independently corroborating it circulated as real, promoted research
  commentary.
- **Real venue and date**: MarketWatch, September 3, 2025.

**Important verification caveat — what is NOT independently confirmed:**
the actual op-ed text was not obtained. The original Columbia mirror
(403, bot-blocked) and a syndicated newswire copy that turned up in
search results (`allpennystocks.com`) both failed to load (the newswire
copy 404'd on direct fetch tonight — likely expired/removed). The
specific findings attributed to this piece in WebSearch's synthesized
summaries — a study of "over 1,500 U.S. adults," itemized tariff
disclosure shifting blame toward government while reducing perceived
fairness and purchase intent, and a partisan (Trump-supporter) difference
in blame attribution — come only from Google-indexed snippets/search-
engine synthesis, not from a direct read of the source. Per tonight's
task instructions, that's not suffient to cite as verified content; only
the **existence, authorship, venue, and date of the op-ed itself** are
confirmed, via the CV primary source. Also checked: neither Morwitz's own
"Working Papers" nor "Research in Progress" list (both current as of the
Dec 2025 CV revision) contains a title matching the tariff-price-
presentation project or this op-ed's underlying study — so there is not
yet an identifiable, citable peer-reviewed or working-paper version of
whatever study underlies the op-ed. A parallel search for a matching
Fitzsimons working paper at Duke (Scholars@Duke, Fuqua faculty page, SSRN)
found nothing by that title either.

**Bottom line for this find:** stronger than 09-22's flag (real,
named, credentialed authors now confirmed via primary source, not just
a page description), but still **not a citable academic source** — it's
a real op-ed by real, on-point scholars, describing an apparently real
but not-yet-independently-verified study, with no accessible full text
and no located peer-reviewed/working-paper version yet. Recommend
Britton treat this as: (a) a signal that Morwitz and Fitzsimons are
actively working this exact space (blame attribution for tariff-driven
price increases, itemized disclosure, partisan moderation) and a paper
may surface from them within the submission window, worth a periodic
check; (b) NOT something to cite in the manuscript yet, since neither
the op-ed's actual text nor an underlying paper has been directly
verified.

**Broader sweep, nothing else new found.** Re-ran several angles (price-
fairness attribution mediators 2025-2026, tariff pass-through/disclosure/
brand-trust literature) beyond the Campbell (2025) JCR paper already
logged 09-22 (not re-summarized here, see that note) and did not surface
any other clearly on-point, verifiable 2025-2026 academic paper. One
tangential item noted but not pursued further given time budget and its
distance from tariffs specifically: Ohlwein & Bruno (2025), "Algorithms
of (un)fairness – Is personalized pricing fair game or foul play?"
(SAGE, DOI visible in search result:
`journals.sagepub.com/doi/10.1177/14707853251338579`) — about
personalized/algorithmic pricing fairness with suspicion/moral-emotion
mediators, a structurally similar mechanism but a different pricing
context (algorithmic personalization, not tariffs); not verified via
Crossref tonight, flagging only as a possible future lead, not treating
it as confirmed.

## 3. SUBMISSION_TRACKER.md open items — quick public-information recheck

Per tonight's task scope ("only if a new angle occurs to you; don't force
it"), did one direct refetch of McNeese's HSIRB policy page
(`mcneese.edu/policy/human-subjects-institutional-review-board-hsirb-policy/`)
rather than a new search angle, since nothing new occurred to try.
**Fully unchanged from 09-22**: same "Enacted February 28, 2023; Revised
July 28, 2025; February 19, 2026" revision history, same exact
Comprehensive-module requirement text, no stated turnaround time
anywhere on the page. No new angle found tonight on either the CITI
conflict or the HSIRB turnaround question — both remain genuinely
blocked on a direct ask to the IRB office, same conclusion as every
prior check back to 09-09.

## Project-file drift check

`git log` for `TARIFF_PAPER/` still shows the 09-22 note as the last
commit; nothing else in the project changed outside tonight's work. No
files touched other than this note — `SUBMISSION_TRACKER.md` was not
modified, since nothing tonight rises to a tracked status change
(litigation fully unchanged; the Morwitz/Fitzsimons find is a literature
lead, not a resolved citation or a project-status fact; CITI/HSIRB
re-confirmed, not newly resolved).

## For Britton

- **Litigation: nothing changed, all four dockets identical to 09-22.**
  V.O.S. Selections' 10/05/2026 response brief is now 12 days out with
  no new activity; Section 122's 11/12/2026 government brief is still
  about seven weeks out. All four dockets remain open, no terminations.
- **New literature-thread lead, verified but not yet citable:** Vicki
  Morwitz (Columbia, the same fairness/pricing-psychology tradition your
  Fairness scale sits in — though not the same Campbell whose 1999/2025
  papers your instrument uses) and Gavan Fitzsimons (Duke) co-wrote a
  real MarketWatch op-ed (Sept 3, 2025) on exactly this project's
  question — does making tariffs visible on a bill shift consumer blame
  from retailer to government, and at what fairness/purchase-intent
  cost. Confirmed real via Morwitz's own CV. Could not get the actual
  op-ed text or find an underlying academic paper — worth you doing a
  quick author-name search yourself periodically (or a library-access
  pull of the MarketWatch piece) since a formal paper from this pair
  would be a strong, closely-on-point citation if/when it surfaces.
- **CITI and HSIRB-turnaround: unchanged, no new angle found tonight** —
  same conclusion as every check since 09-09, still needs a direct ask
  to the IRB office.
- Everything else (Jason's blind-coding worksheet, Purchase Intention
  item count, banked scales, the two Qualtrics-build decisions, the
  still-open Campbell 1999-vs-2007 opportunism-item sourcing question)
  is unchanged — not touched tonight, consistent with task scope.
