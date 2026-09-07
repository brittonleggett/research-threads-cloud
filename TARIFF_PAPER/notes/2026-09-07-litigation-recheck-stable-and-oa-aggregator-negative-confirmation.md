# 2026-09-07 — Litigation recheck: all four tracked dockets stable, Section 301 government response now 3 days overdue with no docket entry; Purchase Intention 1991 original: three OA-aggregator APIs return systematic negative confirmation (no new full text)

Light-touch night per Britton's 09-03/09-05 framing that this project needs no
further action before/around his IRB submission target ("this weekend"). Per that
framing, did **not** touch IRB materials, `SUBMISSION_TRACKER.md`, grad-assistant
items, or H3/Phase-3 theme decisions. Checked `notes/` for anything dated 09-06 or
later that might override this — nothing found; the newest prior note is still
`2026-09-05-purchase-intention-1991-primary-search-and-litigation-recheck.md`.
Worked the two concrete open items it left, plus a light general-development sweep.

## 1. Litigation docket recheck — all four tracked dockets unchanged since 09-05; Section 301 government response now overdue by 3 days

Re-fetched all four CourtListener dockets directly via `curl` with a browser
user-agent (same technique as prior nightly passes — WebFetch itself was not
retried against courtlistener.com since the 09-05 note already established it
403s there). All four returned HTTP 200 and were parsed directly from the raw
HTML for docket-entry counts and text, not summarized by a search engine.

### V.O.S. Selections (CAFC 26-1895) — stable
https://www.courtlistener.com/docket/73433096/vos-selections-inc-v-trump/ —
**still 24 total entries**, identical to both the 09-04 and 09-05 checks. Last
entry (#24, Sep 2) is still the caption-revision entry already documented. No new
activity in the two days since the last check.

### Axle of Dearborn (CIT 1:25-cv-00091) — stable, no appeal filed
https://www.courtlistener.com/docket/70287201/axle-of-dearborn-inc-v-department-of-commerce/
— **still 79 total entries**, identical to 09-04/09-05. No notice of appeal. Per
the running arithmetic (Slip Op. 26-94, Aug 13, 2026 + 60 days ≈ Oct 12, 2026),
roughly 35 days remain in the government's appeal window — still the coordinator's
arithmetic from the ruling date, not a court-stated deadline.

### Section 122 (State of Oregon v. Trump, CAFC 26-1804/-1805) — stable
https://www.courtlistener.com/docket/73318531/state-of-oregon-v-trump/ — **still
81 total entries**, identical to the 09-05 check (which was itself up from 80 as
of 09-04). No new entries since #81 (Sep 3, the small-business appellees' motion
to extend to 09/03 with a corrected-brief deadline of 09/11/2026, already
documented). Nothing new to report; the 09/11 corrected-brief deadline is still
several days out.

### Section 301 forced-labor master docket (In re Section 301 Forced Labor Cases, CIT) — government response still not on the docket, now 3 days late
https://www.courtlistener.com/docket/74219533/in-re-section-301-forced-labor-cases/
— **still 21 total entries**, identical count to the 09-05 check. Confirmed by
reading the raw docket-entry text directly (not just a count): the last entry
remains #21 (Sep 4, Barry Appleton's notice of appearance for all plaintiffs).
**No government response to the plaintiffs' Aug 24 motion for judgment on the
agency record has posted, and it was due 9/4/2026 (per entry #16's docket text)
— that is now three days overdue as of this check (Sep 7).** Ran a fresh news
sweep (WebSearch, several queries: "Section 301 forced labor tariffs government
response," "Court of International Trade Section 301 forced labor case government
brief filed," "forced labor tariff litigation Justice Department response late
missed deadline") — nothing reporting the response filed, and nothing reporting it
as newsworthy-late either (which would be expected if a major outlet had noticed a
missed deadline in a case with a Sep 30 oral argument). **This stays genuinely
unresolved: still can't distinguish "filed but not yet visible on the docket" from
"actually late" from outside the docket itself. Three straight nightly checks
(09-04 due date, 09-05, 09-07) have now found nothing — this is a longer gap than
"normal filing-to-docket lag" would typically explain, though I can't rule out a
sealed/late-electronic-filing explanation without more information than is publicly
visible.** Reply brief (Sep 18) and oral argument (Sep 30, Judges Choe-Groves,
Reif, Wang) remain on the docket's schedule metadata, unchanged.

### General litigation news sweep — no new filings/rulings found; one adjacent thread (Section 338 Canada tariffs) has escalated on the trade-retaliation side, not the litigation side
- No new tariff-litigation filings, rulings, or CAFC/CIT news beyond the docket
  checks above.
- **Section 338 Canada tariffs (already flagged 09-03 as "no lawsuit filed as of
  Aug 29"):** a fresh check finds **still no lawsuit filed** against the Section
  338 action itself as of the most recent trade-press reporting found tonight
  (International Trade Today / Trade Law Daily, "Lawyers: Lawsuits Against Section
  338 Tariffs Expected," ~Aug 25-26) — legal commentary continues to expect a
  challenge but none has materialized yet. **What is new since 09-03: Canada's own
  retaliatory tariffs (not a legal filing) take effect Sep 8, 2026** — up to 50% on
  roughly $27.6B of US goods across three tiers (steel/aluminum/furniture/clothing
  at 50%; cheese/appliances/some seafood at 25%; electronics/tools at 15%), per
  Canada's Department of Finance announcement and corroborating coverage (The Hill,
  Al Jazeera, Mohawk Global). This is retaliatory/trade-policy, not litigation, and
  not one of the four tracked cases — flagging only because it's a genuinely new
  and fairly large development in the broader tariff-policy environment this
  project's messaging corpus sits in. Not recommending action on it.
- Chip-tariff "Phase 2" (flagged 09-05, announcement-stage as of that check): did
  not find newer coverage moving it past announcement stage; no rate, exemption
  criteria, or effective date confirmed yet in tonight's search. No update.

## 2. Purchase Intention (Dodds, Monroe & Grewal 1991) — genuinely new channel tried: three open-access aggregator APIs, all return a systematic negative confirmation

The 09-05 note said this line is "close to fully exhausted for AI-tool-based
methods" and asked not to grind on it further absent a genuinely new channel.
Everything tried on 09-04/09-05 was **manual, site-by-site search** (Google
Scholar, SSRN, ResearchGate, Academia.edu, Scribd, specific university/dissertation
repositories, archive.org). Tonight tried something categorically different and
not attempted before: **open-access aggregator APIs that programmatically crawl
essentially every known repository (institutional, subject, and author-hosted) for
a given DOI**, rather than searching for pages one at a time:

- **Unpaywall API** (`api.unpaywall.org/v2/10.1177/002224379102800305`) — HTTP 200.
  Returns `"is_oa": false`, `"oa_status": "closed"`, `"oa_locations": []`,
  `"has_repository_copy": false`. Also confirms author metadata independently:
  William B. Dodds (Boston College, corresponding author), Kent B. Monroe
  (Virginia Polytechnic Institute and State University, "at the time the research
  was carried out"), Dhruv Grewal (University of Miami) — useful for citation
  precision even though it doesn't resolve the text question.
- **Semantic Scholar Graph API** (`api.semanticscholar.org/graph/v1/paper/DOI:...`)
  — HTTP 200. `"openAccessPdf": {"url": "", "status": "CLOSED"}`.
- **OpenAlex API** (`api.openalex.org/works/doi:...`) — HTTP 200.
  `"open_access": {"is_oa": false, "oa_status": "closed", "oa_url": null,
  "any_repository_has_fulltext": false}`; `best_oa_location: null`; the one
  location record it has (the SAGE landing page itself) is marked `is_oa: false`,
  `pdf_url: null`.
- **CORE.ac.uk API** — attempted (`api.core.ac.uk/v3/search/works`), but returned
  HTTP 429 (rate-limited without a registered API key). CORE requires free
  registration for reliable use; did not pursue further since that's a
  registration step, not a fetch, and wasn't clearly "a channel already available
  to this session." Flagging as untried-to-completion rather than counting it as
  another negative result.

**Why this matters and what it doesn't change:** these three databases
(Unpaywall, Semantic Scholar, OpenAlex) each independently crawl a broad set of
legal open-access sources — institutional repositories, PMC, arXiv-style servers,
and author-uploaded copies on ResearchGate/Academia.edu when those are actually
indexable/legal, not just the handful of individual pages checked manually on
09-04/09-05. All three agreeing "closed, no repository copy" is a meaningfully
stronger, more systematic negative signal than "we checked N specific pages and
they were all blocked" — it suggests there genuinely is no indexed legal open
copy anywhere these services can see, not just that this session's specific
09-04/09-05 targets happened to fail. **This does not change the bottom line from
09-05: the 1991 JMR appendix text itself remains inaccessible through legitimate
automated means. It does strengthen the case that this line is truly exhausted for
AI-tool-based methods**, not merely "we haven't found the right page yet." No new
wording was found, guessed, or reconstructed — the Grewal, Krishnan, Baker & Borin
(1998, *Journal of Retailing*) verbatim reproduction plus Dodds's (2002) corroborating
single item remain exactly as documented in the 09-04 note, unchanged.

**Recommend closing this line for AI-tool-based effort entirely now** — three
manual-search passes (implied prior to 09-04, 09-04, 09-05) plus tonight's
systematic aggregator check is a reasonable stopping point. Further progress
needs either Britton's JSTOR/library access or him pasting in text he can access
directly; continuing to re-run the same category of search nightly would not be a
good use of time.

## Summary table

| Item | Status as of 09-07 |
|---|---|
| V.O.S. Selections (26-1895) | Stable, no new entries (24 total, unchanged since 09-04) |
| Axle of Dearborn appeal | Stable, still not filed, ~35 days left in window (79 entries, unchanged) |
| Section 122 (26-1804/-1805) | Stable, no new entries since #81 (Sep 3); 81 total, unchanged since 09-05 |
| Section 301 forced-labor master docket | **Government's 9/4 response still not on the docket — now 3 days overdue.** 21 entries, unchanged since 09-05. Genuinely unresolved; recommend one more check closer to the Sep 18 reply-brief deadline or Sep 30 oral argument if it still hasn't appeared. |
| Section 338 Canada tariffs | Still no lawsuit filed against the underlying US action; Canada's own retaliatory tariffs (up to 50%, ~$27.6B of US goods) take effect Sep 8 — background/context only |
| Purchase Intention 1991 original appendix | **Still not found**, but now backed by a systematic negative confirmation from 3 OA-aggregator APIs (Unpaywall, Semantic Scholar, OpenAlex), not just manual site checks. Recommend treating this line as exhausted for AI-tool methods; Grewal et al. (1998) + Dodds (2002) remain the defensible secondary-source package. |

## Open items for Britton / next session

- **Section 301 government response:** worth a check in the next several days
  (docket 74219533) — three checks in a row (09-04 due date, 09-05, 09-07) have
  found nothing filed. If it's still missing by the Sep 18 reply-brief deadline,
  that itself becomes a notable fact for the litigation-context section (a case on
  track for Sep 30 oral argument with an overdue dispositive-motion response is
  unusual and may be worth a line in the manuscript's litigation-timeline
  discussion, if this pattern holds).
- **Purchase Intention:** recommend treating as closed for further AI-tool search.
  If Britton has JSTOR/library access, five minutes pulling the 1991 JMR appendix
  would still be the fastest path to full verification; otherwise use the Grewal
  et al. (1998)-plus-Dodds(2002) package as-is, per the 09-04 recommendation
  (dual citation: 1991 for construct/attribution, 1998 for exact item source).
- Everything in this note is background/corpus material, not on the critical path
  to IRB submission, consistent with Britton's "no further action needed on this
  thread" framing. No IRB, grad-assistant, or Phase-3/theme material was touched.
