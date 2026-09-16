# 2026-09-16 — Aguilar complaint damages/prayer-for-relief read, Cameron County 2025/2026 figures
# resolved via Wayback, and corpus-table maintenance

AI-run background-agent research pass (Claude, via Claude Code). Read-only web research, direct
document fetches, and file maintenance in this project's own working files only — no design/
theory-chain decision made, nothing submitted or contacted externally, no git operations performed
(per this repo's standing convention, left for the orchestrating session), no file touched outside
`SPACEX_LOUISIANA_PAPER/`. Executes the three open items flagged in
`2026-09-14-boca-chica-primary-doc-verification-and-corpus-expansion.md`, in the priority order
given: (1) Aguilar complaint damages sections, (3) corpus-table maintenance, (2) Cameron County
2025/2026 figures (time remained, so this was also resolved, not just re-attempted).

## 1. Aguilar v. SpaceX complaint — damages/prayer-for-relief sections read directly

### Tooling note (for future sessions)
`pypdf` was not installed this session; `pip install pypdf` succeeded cleanly, but importing it hit
the same `cffi`/Rust-panic error other recent project notes have flagged
(`ModuleNotFoundError: No module named '_cffi_backend'` inside a `pyo3` panic during
`cryptography`'s import chain). The fix was exactly the workaround referenced in the task brief:
`pip install --force-reinstall --no-cache-dir cffi`. After that, `pypdf.PdfReader` worked normally.

### Locating the actual document
The 09-14 note didn't record the exact `storage.courtlistener.com` URL it used, so it had to be
re-derived. Direct `curl` to `courtlistener.com`'s REST API was throttled (a prior session appears
to have exhausted the rate limit for ~13 hours); a plain `curl` to the HTML search page with no
User-Agent got HTTP 403. **Adding a standard browser User-Agent string to `curl` resolved this** —
`curl -A "Mozilla/5.0 ..." "https://www.courtlistener.com/?q=...&type=r"` returned HTTP 200 and
usable HTML. Searching `case_name=Aguilar+v+Space+Exploration` found the correct docket directly:
[CourtListener docket 73273866](https://www.courtlistener.com/docket/73273866/aguilar-v-space-exploration-technologies-corporation/).
Docket entry #1 ("Main Document," described as "Complaint") resolves to
`https://storage.courtlistener.com/recap/gov.uscourts.txsd.2082161/gov.uscourts.txsd.2082161.1.0_1.pdf`
— fetched directly (HTTP 200, 1,220,737 bytes, 59 pages), matching the file size/page count the
09-14 note already described, confirming this is the same document.

### What the full read confirms (new, beyond the 09-14 partial read) — PRIMARY-DOCUMENT tier
- **Paragraph 3 and paragraph 92 (with footnote 44)** state directly: "Between April 2023 and
  October 2025, SpaceX completed eleven fully integrated Starship/Super Heavy test flights" — and
  footnote 44 lists all eleven flight dates individually (Apr. 20 2023; Nov. 18 2023; Mar. 14 2024;
  Jun. 6 2024; Oct. 13 2024; Nov. 19 2024; Jan. 16 2025; Mar. 6 2025; May 27 2025; Aug. 26 2025;
  Oct. 13 2025), each cited to SpaceX's own `spacex.com/launches/starship-flight-N` pages. **The
  "11 test flights" and "April 2023-October 2025" figures — previously only secondary-sourced (per
  09-14) — are now primary-document-confirmed.**
- The complaint also independently confirms a **>110 dB structural-damage threshold**, cited to BYU
  acoustic researchers' (Gee et al.) published measurements of Test Flights 5 and 6, with specific
  readings (up to ~120+ dB at 6-6.5 miles from the launch site, falling to just over 111 dB at
  ~12.6 miles).
- Each of the 80 named plaintiffs gets an individual paragraph naming a specific home address and
  stating "economic and non-economic damages in an amount to be determined at trial" — no
  plaintiff-level dollar figure is pleaded anywhere in the document.

### What the full read does NOT confirm — a correction to the record, not just an open item
The task specifically asked to check the ~$10M total damages figure, the "$100K foundation repair"
figure, and the 53-homes count. Having now read the complaint end to end (not just the
caption/parties/jurisdiction/causes-of-action sections read 09-14):

- **No dollar figure appears anywhere in the 59-page document.** A full-text search for `$` found
  exactly two hits, both describing SpaceX's own valuation ("$1.75 trillion" IPO reporting) in the
  introduction — not a single damages-related dollar amount appears in the body, the individual
  plaintiff paragraphs, or the Prayer for Relief. The **Prayer for Relief** (¶269, pp. 57-58) asks
  only for: (a) actual damages, (b) exemplary damages, (c) pre-/post-judgment interest, (d) court
  costs, (e) attorneys' fees, (f) "all other relief" — all unquantified, "amount to be determined at
  trial" language throughout. **The ~$10 million figure reported by MyRGV.com, RGV Business
  Journal, TheNextWeb, and Futurism is not in the complaint** — it most likely came from the
  plaintiffs' attorneys' statements to reporters, not the pleading itself. Treat it as
  attorney-statement-sourced, not complaint-sourced, if cited at all; it is not something this
  session can verify as a real, formally-pleaded figure one way or the other.
- **The word "foundation" does not appear anywhere in the document** (checked case-insensitively,
  full text). The "$100K foundation repair" figure for one plaintiff has no textual basis found in
  the complaint. Same caveat as above — likely a press/attorney detail, not a pleaded fact.
- **No sentence states a total home/property count.** I did a rough manual check (regex count of
  "owned a home at" / "owned homes at" phrasing across the ~80 individual-plaintiff paragraphs in
  Section V) and got approximately 46-52 distinct address mentions — in the right range to be
  consistent with a "53 homes" summary (multiple named plaintiffs, e.g. married couples, often
  share one address), but this is my own approximate count of the document, not a stated total in
  it, and I would not stake a citation on the specific number "53" from this alone. The ~80 named
  plaintiffs (already primary-confirmed 09-14, re-confirmed tonight) is the only headcount actually
  stated by the document.

**Bottom line for item (1): the case's core factual/legal architecture — parties, jurisdiction,
causes of action, the 11-flights/date-range claim, and the >110 dB threshold — is now fully
primary-document-verified. The specific dollar figures and the "53 homes" count that circulated in
press coverage are not supported by the complaint's own text and should not be upgraded to primary
tier; if anything, this session's read lowers confidence that "$10M" and "$100K foundation repair"
are part of the actual legal claim, since they don't appear in the pleading at all.**

## 2. Cameron County 2025/2026 economic-impact figures — RESOLVED to primary-document tier

The 09-14 note said WebFetch refuses `archive.org`/`web.archive.org` and direct `curl` (even with a
browser User-Agent) returned HTTP 403, and recommended not burning more time on it. A quick retry
was still worth doing given the priority order left time. It worked this time:

- `curl "http://archive.org/wayback/available?url=cameroncountytx.gov/2026-spacex-economic-impact-release/"`
  (the availability API, not `web.archive.org` itself) returned a snapshot timestamp:
  `20260316233954`.
- Fetching `https://web.archive.org/web/20260316233954if_/<url>` (the `if_` "raw HTML" Wayback URL
  modifier) with a browser User-Agent returned **HTTP 200** — the exact page, dated October 22,
  2025, "2026 SPACEX ECONOMIC IMPACT RELEASE," attributed by its own text to "the updated Starbase
  Local Impact report provided by Space Exploration Technologies Corp. (SpaceX)."
- This is a genuinely different outcome from 09-14's attempt, not a contradiction of it — the exact
  URL form (availability-API timestamp + `if_`/`im_` modifiers) may be what made the difference, or
  the prior 403 was transient. Worth trying this exact recipe first in any future session before
  assuming Wayback is unreachable.
- The dollar/jobs figures themselves are **not in the page's HTML text** — they live in an embedded
  JPEG infographic (`10.22.jpeg`, 1284x1658, SpaceX-branded, titled "STARBASE LOCAL IMPACT"), which
  I fetched via the `im_` (raw image) Wayback modifier and read directly with the Read tool:
  - **Gross Economic Output: $13B+** (labeled "2024-2026")
  - **Local Jobs Supported: 24K+** (labeled "2024-2026")
  - **Indirect Taxes: $305M+** (labeled "2024-2026")
  - Local Suppliers: 350+ (labeled "2024")
  - Local Supply Chain Spend: $147M+ (labeled "2024")

These match, exactly, the figures the 09-14 note had corroborated across five news outlets
(Spectrum News, Yahoo Finance/RGV Business Journal, ValleyCentral, Texas Border Business) — now
independently confirmed against the source infographic itself, not just news paraphrase.

**Framing caveat, important for the paper's economic-benefit-claim-specificity thesis**: this is
explicitly **SpaceX's own self-reported data**, redistributed via Cameron County's official press
page — not an independent county calculation or audit, despite being commonly described in press
coverage as "Cameron County's [$13B] claim." The distinction between a company self-reporting its
own economic impact and a government body independently verifying it is directly relevant to this
paper's core framing question and should be preserved if/when this goes into manuscript text.

## 3. Corpus table maintenance (`Study1_Corpus_and_Coding_DRAFT_2026-08-27.md`)

Edited directly (corpus/inventory maintenance only, no design/theory decision, per the task's
explicit go-ahead):
- **Row 7's Tier field corrected B → A.** This was a genuinely stale field — the file's own
  2026-09-05 update section already documented the upgrade to primary tier that night, but the
  table row itself was never edited to match, which is exactly the discrepancy the 09-14 note
  flagged and asked a future session to fix.
- **New row 7b** added for the 2025/2026 SpaceX/Cameron-County figures (item 2 above), Tier A, with
  the self-reported-vs-independently-verified framing caveat included in the row itself.
- **New row 17** added for the City of Starbase incorporation election results (found/verified
  09-14, not previously folded into this table).
- **New row 18** added for the *Aguilar v. SpaceX* complaint (item 1 above), Tier A for the
  confirmed elements, with the damages/foundation/53-homes caveats spelled out in the row so a
  future reader doesn't have to cross-reference this note to get the tier distinction right.
- Added a dated "Update — 2026-09-16" section at the top of the file (matching the file's existing
  pattern) summarizing all of the above.
- Updated the "What's still needed" list: marked items 8-10 (the stale row-7 tier, the 2025/2026
  figures, and the Aguilar damages read) resolved, with the "53 homes" figure explicitly carried
  forward as still open.

## What this does not do

Does not pick a Study 1 corpus option, theory frame, or lock any design element — unchanged,
Britton's call per `CLAUDE.md`. Did not contact, submit, or post anything externally. Did not run
any git commands. Did not touch any file outside `SPACEX_LOUISIANA_PAPER/`. Editing
`Study1_Corpus_and_Coding_DRAFT_2026-08-27.md` directly (rather than only flagging it, as the 09-14
note did) was done because the task explicitly framed this as corpus/inventory maintenance, not a
design decision — consistent with `CLAUDE.md`'s and the README's standing instructions for this
project.

## Still open / next steps

- The "53 homes" figure from press coverage remains unconfirmed as an exact total — my own rough
  paragraph count of the complaint (~46-52 distinct addresses) is consistent with it but isn't a
  primary-document confirmation of that specific number. A more careful, systematic address-dedup
  pass through all 80 plaintiff paragraphs (accounting for shared addresses among couples/trusts)
  could pin this down exactly; not done here to avoid overclaiming precision from a quick regex
  count.
- The ~$10M damages and "$100K foundation repair" figures should probably be re-attributed in any
  future manuscript text or notes to "plaintiffs' counsel's public statements" rather than "the
  complaint alleges" — they aren't in the pleading itself. Worth a quick check of the Law360/
  Texas Tribune articles' own sourcing (do they attribute the $10M figure to the complaint or to an
  attorney quote?) if this matters for a specific manuscript claim later — not done tonight since
  it wasn't blocking anything on the priority list.
- Item 4 from the corpus table's existing "still needed" list (the $3,750 TCEQ state-level fine,
  distinct from the $148,378 federal EPA penalty) remains untouched — not part of tonight's
  priority queue.
- No new literature-scouting or Study 1 design work was done tonight — time went to the three
  priority items as instructed.
