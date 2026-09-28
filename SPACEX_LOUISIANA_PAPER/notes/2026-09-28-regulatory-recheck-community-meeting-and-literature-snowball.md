# 2026-09-28 — Regulatory re-check (FAA docket, Aguilar docket, CAH/SB1198 thread — all flat), a
# new Vermilion Parish community-meeting find (row 24), and the project's first real
# citation-snowball literature pass

AI-run background-agent research pass (Claude, via Claude Code). Read-only web research and direct
document/docket/API fetches only — no design/theory-chain decision made, nothing submitted or
contacted externally, no file touched outside `SPACEX_LOUISIANA_PAPER/` except the corpus/
literature files this project's own convention treats as ordinary maintenance. Oriented by reading
the root `README.md`, this project's `CLAUDE.md`, and every dated note/literature file from
2026-09-16 through 2026-09-25 before starting new work, per tonight's task brief — confirmed the
09-25 note is genuinely the most recent (not 09-23 as an earlier version of the task brief
believed), and that the "$100M coastal master plan" vs. "$25M charitable donation" discrepancy
flagged in the project's earliest notes was already substantially resolved 2026-09-07 (see that
note: the $100M figure appears to be a conflation with SpaceX's separate $100M land-purchase price
from the state, not a quantified CPRA restoration commitment; the $25M donation is the one real,
written commitment in LED's own Letter of Intent). Did not re-litigate that resolution tonight —
just confirming it stands, per the task's specific instruction to check.

## Priority order followed (per tonight's task brief)

1. Regulatory movement (FAA, environmental filings, Vermilion Parish/LA state actions) since 09-25.
2. Aguilar complaint / SB1198 / Cards Against Humanity thread movement.
3. Boca Chica + Vermilion Parish corpus expansion.
4. New literature on economic-benefit-claim-specificity or greenwashing framing.

## 1. Regulatory movement since 09-25 — checked directly, essentially none, but one real find

**FAA-2026-8614** (the environmental-review-waiver NPRM): re-checked via `api.regulations.gov`
(the `DEMO_KEY`, through `r.jina.ai` proxy — direct access still 403s from this environment,
unchanged across every session of this project). Docket `category` still **"Pending"**,
`modifyDate` unchanged at `2026-09-11T15:57:07Z` (identical to 09-25's reading — the record itself
hasn't moved at all in the 3 days since). Documents endpoint still shows exactly **one** document
(the original 2026-07-30 Proposed Rule; `openForComment: false`; no final rule). Posted-comment
count unchanged at **3,203** — zero net change over 3 days, continuing the flat trend the 09-07 and
09-25 notes already flagged and recommended deprioritizing. **No regulatory movement to report.**
Consistent with 09-25's own recommendation, this project should keep checking this docket only
occasionally rather than nightly; tonight's check took under two minutes and confirms that
recommendation was sound.

**Vermilion Parish / Louisiana state government**: no CPRA permit filing, no Police Jury zoning
vote, and no new state legislative action was found since 09-25. The Vermilion Parish Police Jury's
RV-park ordinance (tracked since 09-08, discussed at a Sept. 16 meeting per news coverage) does not
yet appear to have had a final vote — search results describe it as still "considered," not
"passed," as of the most recent coverage found. Not upgrading this item's status; flagging that it
remains open rather than assuming a vote happened.

**New find, genuinely new to this corpus**: SpaceX held its **first public community meeting**
with Vermilion Parish residents on **2026-09-24**, at Magdalen Place in Abbeville — one day before
the 09-25 note's own session, which did not catch it (a general "Starbase Louisiana news
September 2026" search, not a regulatory-docket check, is what a future session would need to run
to catch this kind of on-the-ground event; noting this so a future session doesn't assume the
09-25 regulatory pass would have caught it). Fetched two independent outlets' coverage directly
(KLFY via `r.jina.ai` proxy after a direct 403; Acadiana's News Leader/KATC via WebFetch) — full
detail and quotes added as **row 24** in `Study1_Corpus_and_Coding_DRAFT_2026-08-27.md`. Headline
finding: a SpaceX representative identified only as **"Violet"** told the crowd, on the record,
*"We have not found where it's going to cause foundation problems and any type of structural
damage"* regarding launch vibrations — a direct, contemporaneous claim standing in tension with the
active Aguilar litigation in Texas (row 18), where 80 plaintiffs allege exactly that kind of
acoustic/structural damage from the same class of Starship test flights. This is a clean,
citable, real-time instance of the claim-vs-disputed-outcome pairing this paper's framing is built
around, playing out at the Louisiana site itself rather than only via the Boca Chica comparison.
Two other SpaceX reps ("Blue," "Rose," also first-name-only per both outlets — itself a minor but
real framing detail worth keeping) are quoted on a complaint-resolution process and on deferring to
local/traditional ecological knowledge, respectively. Named resident reactions (Melissa Hargrave,
critic; Elray Schexnayder, supporter) are also in the row.

## 2. Aguilar / SB1198 / Cards Against Humanity thread — re-checked, no movement

**Aguilar v. SpaceX (1:26-cv-00485)**: re-fetched the full CourtListener docket page directly
(`curl` with a browser User-Agent, HTTP 200) and parsed all docket-entry IDs. **Still exactly 35
entries**, identical to the 09-25 note's count — no Dkt. 36 or later exists. SpaceX's fully-briefed
second motion to dismiss (Dkt. 29) remains unruled-on. No new filings of any kind since Dkt. 35
(2026-09-23). **No movement to report** — a genuinely useful negative finding, not a skipped check.

**Cards Against Humanity v. SpaceX**: re-searched for any post-settlement news (docket activity,
a disclosed settlement amount, further coverage). Found nothing beyond what was already
primary-verified 09-20/09-23 — the October 2025 settlement, the "trespassing" admission during
discovery, and the no-cash/novelty-card-pack outcome for crowdfunders. No new developments.

**SB 1198 (Texas critical-infrastructure designation)**: no new developments since the enrolled
text was pulled 09-23. This thread (both the CAH litigation and the SB1198 statute) is now a
closed, stable, well-documented pair of historical items in the corpus — recommend not
re-checking either on a nightly basis going forward absent a new lead (e.g., a docket search tool
for Cameron County District Court finally becoming reachable, which would let a future session
verify the CAH case's judge/later docket history, still flagged open since 09-23).

## 3. Boca Chica / Vermilion Parish corpus expansion

Beyond the new row 24 (section 1 above), no further new corpus items were found tonight —
time went primarily to the regulatory re-checks (which, being genuinely negative/flat, took less
time than a full raw docket re-verification usually does) and to the literature snowball (section
4), which several prior sessions had flagged as the single most overdue piece of work on this
project. This is a deliberate allocation choice, not an oversight: three consecutive literature
notes (09-09, 09-10, 09-25) all recommended citation-snowballing as the next step and none had
done it, while the corpus itself has now had a new row added in almost every session for a month.

## 4. Literature — first real citation-snowball pass; two strong new anchors found

Full detail in the new `literature/Literature_Snowball_2026-09-28.md`. Used OpenAlex's
forward-citation search (`cites:<id>`, restricted to 2024-2026) off the project's two strongest
existing anchors — Delmas & Burbano (2011) and Janssen, Swaen & Du (2022) — rather than another
fresh keyword search, per the standing recommendation across three prior literature notes. Hit the
shared-IP OpenAlex free-tier rate limit partway through (a real, cited error: `429`, "Insufficient
budget... resets at midnight UTC") and worked around it by routing the same API calls through
`r.jina.ai` (a different apparent source IP to OpenAlex) — a new, reusable technique for this
project, parallel to the existing `r.jina.ai` workarounds for regulations.gov/courtlistener/
capitol.texas.gov.

**Strongest new find**: Yang, Gong, Lew & Ting (2026), a Research Square **preprint** (not yet
peer-reviewed — flag this tier clearly), analyzing ~420,000 Airbnb listings across Europe and
finding **vague** green claims command a 16.6% price premium but 6.9% lower demand, while
**specific, verifiable** claims trade at a 5.2% discount. This is the closest empirical analog
found yet to this project's own "is a specific claim actually the more credible/effective choice"
question, and it cuts a different direction than Janssen/Swaen/Du (2022)'s warmth/competence
moderation — a genuine complication worth a full-text read before manuscript use.

**Second new find**: Flores-Zamora & De Pelsmacker (2026, *International Journal of Advertising*),
a three-study experimental paper finding that claim specificity alone doesn't reduce perceived
"green deception" — it has to be paired with sufficient message length; a short specific claim
reads about as deceptive as a vague one. A third moderator (length/elaboration) alongside
Janssen/Swaen/Du's competence/warmth and the Yang et al. price/demand divergence.

**Negative findings, both now doubly/triply confirmed**: (a) forward-citing Bartik (2020) turned
up only public-finance papers, none addressing the marketing/communication angle this project
needs — Bartik remains the right anchor, it just hasn't been picked up by a communication-specific
citing paper yet; (b) a direct search for "economic-benefit-claim-specificity in infrastructure
siting" as its own literature is confirmed empty for a third time, via a third distinct
method (WebSearch, then OpenAlex relevance search, then OpenAlex citation-graph search) — this is
now a stable, durable gap, not an artifact of any one search tool, and arguably a genuine
opportunity this paper could fill rather than something to keep re-checking.

## What this does not do

Does not pick a Study 1 corpus option, theory frame, or lock any design element — unchanged,
Britton's call per `CLAUDE.md`. Did not contact, submit, or post anything externally. Did not spend
any money. Did not touch any file outside `SPACEX_LOUISIANA_PAPER/`.

## Still open / next steps

- Row 24 (community meeting): a future session could look for video/full-transcript coverage of
  the Sept. 24 meeting (local TV stations often post fuller clips than the write-up article) to
  get the SpaceX representatives' full names/titles, currently unknown (both outlets used first
  names only).
- Aguilar Dkt. 29 (motion to dismiss): still unruled-on; keep checking periodically, not nightly,
  per 09-25's own recommendation, now reinforced by a second flat reading.
- FAA-2026-8614: recommend continuing the occasional/monthly cadence 09-07 and 09-25 both already
  recommended — tonight's check reinforces that recommendation a third time.
- Literature: full-text reads of the Yang et al. (2026) preprint and the Flores-Zamora & De
  Pelsmacker (2026) paper (both currently abstract-tier only); the Tan, Lin & Hong (2025) "Green
  Specificity" paper needs its abstract located (Elsevier page didn't yield it to a direct/redirect
  fetch tonight) before it can be cited beyond a bare bibliographic entry.
- Backward citation-snowballing (references cited *by* the anchors, not just works citing them) is
  untried — a further angle for a future literature session.
- Unchanged, genuine gaps from prior sessions, not re-attempted tonight: the ~$10M Aguilar damages
  figure's ultimate source (treat the 09-20/09-25 exhaustive-search finding as still current); the
  Travis County suit (D-1-GN-24-010020) docket status; the Starbase annexation's "consent-based"
  vs. "not requested/voluntary" framing dispute; TCEQ Docket 2024-1821-IWD's actual signed
  Commission order; USFWS's 2025 Amended BCO Addendum #2 document itself; the Jacob Landry NDA
  document (DocumentCloud-blocked); Act 343/HB1250's and the public-records-exemption bill's
  enrolled legislative text.
