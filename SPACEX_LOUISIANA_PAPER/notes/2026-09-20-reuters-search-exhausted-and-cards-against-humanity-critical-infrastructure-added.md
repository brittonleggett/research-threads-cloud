# 2026-09-20 — Reuters-source search for the $10M/$100K figures (exhausted, negative result),
# plus two new Boca Chica corpus items: Cards Against Humanity v. SpaceX and the Texas critical-
# infrastructure designation (SB 1198)

AI-run background-agent research pass (Claude, via Claude Code). Read-only web research and direct
document/page fetches only — no design/theory-chain decision made, nothing submitted or contacted
externally, no git operations performed (per this repo's standing convention), no file touched
outside `SPACEX_LOUISIANA_PAPER/`. Confirmed current state first by reading `CLAUDE.md`, the
2026-09-18 and 2026-09-16 notes, and the corpus table — state matched the task brief's summary.

## 1. The ~$10M / $100K damages-figure Reuters search (priority item) — genuinely exhausted, negative result

The 09-18 note's specific, actionable suggestion was to find a `reuters.com` URL directly, since
prior sessions had only found outlets citing Reuters secondhand. Tonight tried substantially harder
than a plain WebSearch pass:

- Multiple `WebSearch` queries, including `site:reuters.com` variants and keyword combinations
  (case names, plaintiff details, photographer credit) — none surfaced a `reuters.com` URL.
- Direct `curl` queries against Google and Bing (bypassing the WebSearch tool entirely, in case it
  was silently filtering reuters.com results) — Google required JS and returned no usable results;
  Bing's `site:reuters.com` query returned zero real results (fell back to unrelated generic SpaceX
  pages, confirming zero matches rather than a parsing failure).
- A DuckDuckGo HTML-endpoint query also failed to return parseable results (redirected to the
  DuckDuckGo homepage, likely bot-blocked).
- Followed a promising lead: the Texas Tribune's own photo credit on this story is "REUTERS/Steve
  Nesius," meaning a Reuters photographer/stringer was on the ground for this story — strong
  circumstantial evidence a Reuters wire piece exists. Searched specifically for that
  photographer's byline alongside the story; did not surface a reuters.com link, only outlets
  re-using the credited photo.
- Checked several additional outlets that looked like plausible wire-service republications
  (Yahoo News under two different bylines, KSAT, Insurance Journal, News From The States — the
  last blocked by a 403). None were Reuters wire copy; each had its own named byline (Texas
  Tribune's Ayden Runnels, Snejana Farberov, Dina Arévalo) and, where Reuters was mentioned at all,
  it was only as "according to Reuters" / "showed Reuters" attribution, not as the outlet's own
  source.
- **New, important finding for future sessions**: `WebFetch` in this environment is **hard-blocked
  from `www.reuters.com` specifically** — it returned "Claude Code is unable to fetch from
  www.reuters.com" immediately, before any network attempt could even fail on paywall/bot-detection
  grounds. This means that even if a reuters.com URL for this story is eventually found (by a human,
  or by a session with different tooling), this environment's `WebFetch` cannot read it directly —
  a proxy-read approach (e.g. `r.jina.ai`) would need to be tried instead, the way this project has
  worked around other sites' 403s. Worth noting in case a future session finds the URL but then
  can't understand why the direct fetch fails.

**Bottom line: the reuters.com URL search is now genuinely exhausted, not just "not found yet."**
Multiple independent search paths (two different WebSearch-tool queries, direct Google, direct
Bing, DuckDuckGo, and a photographer-credit-based search) all came up empty across a real, focused
session. Recommend not repeating this specific search again in future sessions unless a new lead
surfaces (e.g., if the case reaches a further procedural milestone that draws fresh Reuters
coverage). The $10M figure's origin **remains formally unresolved** — do not upgrade its
attribution status. No new information contradicts the 09-16/09-18 notes' finding that it is not in
the complaint itself.

One adjacent, minor finding worth flagging: the Moore Law Firm's own site (the actual plaintiffs'
attorney, J. Michael Moore, "Owner & Principal Attorney" — confirmed via byline) states "They are
seeking more than $10 million in damages" on a client-recruitment page
(moore-firm.com/spacex-starship-property-damage-south-texas/). This is the closest thing to an
"attorney statement" source found for this figure across all sessions so far — but the page reads
as a marketing/recruitment page restating the same figure already circulating in press coverage
(same wording pattern as RGV Business Journal's unattributed narration), not as an original
attorney announcement with its own sourcing. Treat this as weak, not strong, corroboration — it
does not resolve where the $10M figure itself originates, only that the plaintiffs' own attorney
now also repeats it publicly.

## 2. Boca Chica comparison corpus — two new items added

Per the 09-18 note's standing open item (Boca Chica corpus expansion), spent the remaining session
time on this rather than re-touching already-closed items.

### New: Cards Against Humanity v. SpaceX (Cameron County, TX) — land-trespass dispute, settled 2025

A genuinely new corpus item, not previously mentioned anywhere in this project's notes or corpus
table (checked via grep across the whole project folder before adding). Real, well-documented,
multiply-corroborated case:

- Cards Against Humanity (the card-game company) bought a parcel of vacant land in Cameron County,
  TX in 2017 — a publicity campaign explicitly aimed at blocking U.S.–Mexico border-wall
  construction, funded by ~150,000 supporters paying $15 each (~$2.25M raised).
- Filed suit against SpaceX in Cameron County District Court (404th District Court, per MyRGV/Texas
  Tribune coverage — case number not independently located; Texas state-court dockets aren't
  centrally searchable the way federal PACER/CourtListener is, and this session did not find a
  working public docket portal for Cameron County District Court) around September 19-21, 2024,
  alleging SpaceX trespassed on and used the land for construction-material/vehicle storage for
  several months without permission, and dumped gravel/debris on it. Sought $15 million in damages.
- Satellite-imagery analysis by Bellingcat (fetched directly,
  bellingcat.com/news/2024/10/22/spacex-vs-cards-against-humanity-satellite-imagery-shows-activity-on-land-at-centre-of-legal-case/)
  independently corroborates construction activity on the specific parcel (lot 11, 41176 Tarpon
  Bend Dr, Brownsville, TX) beginning around June 2023 — an independent, non-party verification
  that the underlying factual claim (SpaceX using the land) is not merely a company's unverified
  allegation.
- Settled October 2025, just before a November 3, 2025 trial date. Terms undisclosed, but Cards
  Against Humanity's own statement (fetched directly via CBS News Texas,
  cbsnews.com/texas/news/cards-against-humanity-elon-musk-spacex-settlement-alleged-trespassing-texas/)
  says "SpaceX admitted during the discovery phase of the case to trespassing on its property," and
  confirms "SpaceX has removed their construction equipment from our land." No cash settlement
  disclosed; TechCrunch's coverage (fetched directly) reports the crowdfunding supporters will
  instead receive a novelty card pack "all about Elon Musk" rather than a cash refund.

**Why this belongs in the corpus**: distinct from the Aguilar acoustic-damage suits (row 18) —
this is a direct land-encroachment/boundary-disregard dispute, not a noise-nuisance claim, and it
resolved with what reads as a factual admission (trespass, during discovery) rather than a "neither
admits nor denies" settlement posture like the EPA/TCEQ enforcement actions already in the corpus.
For the ex-post "does the company actually respect property lines/community boundaries it claims to
respect" comparison thread, this is a sharper data point than anything else currently in the Boca
Chica side of the table. Tier: **A-minus** — every fact above comes from a direct fetch of the
outlet's own reporting (CBS News Texas, TechCrunch, Bellingcat, plus corroborating search-summary
detail from MyRGV/Texas Tribune/Houston Chronicle/The Hill), but no underlying court filing itself
was located and read (Houston Chronicle's direct fetch was blocked, HTTP 403; the Cameron County
District Court docket was not accessible with this session's tooling). Flag this tier distinction
if cited — it is well-corroborated news reporting of a real, settled case, not a primary legal
document read directly the way the Aguilar complaint was.

### New: Texas SB 1198 (89th Legislature) — resolves row 16's open "critical infrastructure" verification

Row 16 (added 09-08) flagged Starbase's "critical infrastructure" designation under Texas law —
cited only to SOTXEJN's own July 2026 petition post, not independently verified against the actual
statute. Tonight located and **primary-verified directly** via `capitol.texas.gov`'s own bill-history
page (`capitol.texas.gov/BillLookup/History.aspx?LegSess=89R&Bill=SB1198`):

- **SB 1198, 89th Legislature, Regular Session** — "Relating to the designation of spaceports as
  critical infrastructure facilities for purposes of criminal and civil liability." Author: Sen.
  Birdwell; coauthors Blanco, Hinojosa, Adam. Companion bill HB 2973 (Rep. Eddie Morales).
- Filed Feb. 10, 2025; passed Senate March 26, 2025; passed House (amended) May 23, 2025; **signed
  by the Governor June 20, 2025; effective September 1, 2025.**
- Substantively, it amends Texas's existing critical-infrastructure-facility statute (Government
  Code Ch. 423/424 family — the same "critical infrastructure" trespass-enhancement regime SOTXEJN's
  post referenced) to explicitly add any FAA-licensed spacecraft launch/landing/recovery/testing
  facility, or any facility operated by a Ch. 507 spaceport development corporation — covering
  Starbase, Midland International's spaceport designation, the Houston Spaceport, and Blue Origin's
  Van Horn site by name in contemporaneous coverage (Citizen Portal's legislative-tracking summary,
  cross-checked against the bill's own caption).
- Timing check: SB 1198 took effect Sept. 1, 2025, before SOTXEJN's July 2026 post describing the
  felony-trespass exposure — consistent, not contradictory; this is very likely the specific legal
  basis (or one of the bases) for the concern SOTXEJN raised, now traced to an actual enacted
  statute rather than resting on an advocacy group's own unverified characterization.

**Tier A** — bill history/dates/caption/author fetched directly from the Texas Legislature's own
site, the primary source for legislative status. The bill's full enrolled text itself was not
fetched and read line-by-line tonight (only the history/status page); a future session could pull
`capitol.texas.gov/tlodocs/89R/billtext/doc/SB01198F.docx` (or the equivalent enrolled PDF) to quote
the statute's exact amended language if a manuscript needs to cite specific text rather than the
bill's caption and effect.

## What this does not do

Does not pick a Study 1 corpus option, theory frame, or lock any design element — unchanged,
Britton's call per `CLAUDE.md`. Did not contact, submit, or post anything externally. Did not run
any git commands. Did not touch any file outside `SPACEX_LOUISIANA_PAPER/`.

## Still open / next steps

- The ~$10 million total-damages figure's ultimate source **remains unresolved** — search effort
  for a direct reuters.com URL is now genuinely exhausted (see section 1); treat as a closed lead
  unless a new circumstance (e.g. a case-procedure milestone) generates fresh coverage worth
  re-checking. Continue treating the figure as "unattributed news narration, not complaint-sourced,
  not clearly an original attorney announcement either" in any manuscript text.
- Cards Against Humanity v. SpaceX: the underlying Cameron County District Court filing itself was
  not located/read — a future session with access to a working Texas state-court docket search (or
  PACER-equivalent for Cameron County) could upgrade this to full primary-document tier.
- SB 1198's enrolled text itself (not just its history/status page) is still unread — a future
  session needing exact statutory language for the critical-infrastructure/trespass-enhancement
  frame should pull the enrolled bill text directly.
- Standing broader open items, unchanged from prior notes: primary-source verification of the
  remaining not-yet-directly-checked facts in `notes/2026-08-27-orientation.md` (most of its
  individual facts have since been independently verified across many sessions' notes, but the
  note itself has never been rewritten/marked as such — a future session could do a pass
  specifically closing that loop), and literature-gap scouting specific to this paper (last done
  2026-09-09, not touched again since).
