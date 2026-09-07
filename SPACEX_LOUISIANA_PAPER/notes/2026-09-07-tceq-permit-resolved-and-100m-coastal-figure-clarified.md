# 2026-09-07 — TCEQ Docket 2024-1821-IWD resolved (permit issued, parallel federal suit dropped),
# Travis County suit still a genuine access gap, FAA docket flat for a fifth reading, Boca Chica
# BCO addenda chain confirmed steady, and the "$100M coastal master plan" figure substantially
# clarified as likely conflated with SpaceX's $100M land-purchase price

Follow-up to `2026-09-05-faa-quiet-nda-document-and-osprey-loi-found.md`. Read-only research pass
(background agent). **No theory chain, coding scheme, or Study 1 option (A/B/C) decided or touched
here — still Britton's call**, per standing project rules. Tooling: `poppler-utils` reinstalled
again this session (not persisted between sessions); PDFs fetched with `curl` + read with
`pdftotext -layout` where noted as primary; several sources required the `r.jina.ai` proxy (noted
inline) after direct `curl`/WebFetch hit Cloudflare 403s — those are flagged as proxy-fetched news
reads, not synthesized search summaries, per this project's tiering convention, except where
explicitly marked as a WebSearch-summary only.

## 1. TCEQ Docket 2024-1821-IWD — resolved since 09-05's note, not previously confirmed here

The 09-05 note left this open: "SpaceX's position and the ED's recommendation are primary-confirmed;
the Commission's final ruling is not." Tonight, three independent findings close this out:

**a) TCEQ's own commissioners' agenda for Feb 13, 2025** — fetched directly
(https://www.tceq.texas.gov/downloads/agency/decisions/agendas/2025/250213.pdf, HTTP 200, direct
`curl`, `pdftotext -layout`): confirms Item 1 on that agenda was exactly Docket 2024-1821-IWD,
"Consideration of the application by Space Exploration Technologies Corp.... The Commission will
also consider requests for hearing or reconsideration... and the Executive Director's response to
comments." This is the scheduling document, not the outcome, but it primary-confirms the hearing
actually happened on the date already known.

**b) The Executive Director's Response to Hearing Requests, fetched directly**
(https://www.tceq.texas.gov/downloads/agency/decisions/agendas/backup/2024/2024-1821-iwd-edr.pdf,
HTTP 200, direct `curl`, `pdftotext -layout`, 1172 lines): confirms, in the ED's own words, Section
VII (Conclusion): "The Executive Director recommends the following actions by the Commission: 1.
The Executive Director recommends that the Commission deny all hearing requests... 2. The Executive
Director recommends that the Commission deny all requests for reconsideration." This is consistent
with, and now directly sourced alongside, SpaceX's own filing making the same standing argument
(already primary-confirmed 09-05).

**c) The outcome itself — via a primary federal court docket, not a news summary.** Searching for
what happened to the related coalition penalty-objection thread surfaced a **fourth**, previously
untracked Boca Chica legal action: **Save RGV v. Space Exploration Technologies Corporation**,
1:24-cv-00148, U.S. District Court for the Southern District of Texas, filed Oct. 9, 2024 — Save RGV
suing **SpaceX directly** (not TCEQ), separate from all three coalition actions already in the
corpus. Fetched the docket directly via CourtListener (via `r.jina.ai` proxy after a direct 403):
https://www.courtlistener.com/docket/69241580/save-rgv-v-space-exploration-technologies-corporation/
**Confirmed directly from the docket**: Save RGV filed a "NOTICE of Dismissal as to All Parties" on
**February 18, 2025**, and Judge Rolando Olvera entered an "ORDER OF DISMISSAL" the same day (Docket
Entry #37). Cross-referencing WebSearch results pointing to MyRGV's own headline — "Save RGV drops
SpaceX lawsuit; cites approval of water discharge permit" (published 2025-02-18) — ties the
voluntary dismissal directly to the TCEQ permit approval. **The MyRGV article itself could not be
directly fetched tonight** (site 403s WebFetch and direct `curl`; the Wayback Machine snapshot found
via the archive.org availability API also 403'd through this session's proxy) — so the *headline
and framing* rests on WebSearch-summarized secondary sourcing, but the **dismissal date and fact
of dismissal are primary-court-record-confirmed** via CourtListener.

**Net finding, stated plainly**: TCEQ's TPDES Permit No. WQ0005462000 for the deluge/washdown/
stormwater discharge was approved following the Feb. 13, 2025 commission meeting (ED recommended
denying all hearing requests; multiple independent WebSearch summaries converge on "issued Feb. 18,
2025"), and the coalition's related direct suit against SpaceX was dropped the same day. **What
remains not independently verified**: the actual signed Commission order/vote record itself — TCEQ's
site did not surface a distinct "final order" PDF the way it did for the 09-04 note's $3,750 agreed
order, and TCEQ's permit-search database (`apps.tceq.texas.gov`, `search.tceq.texas.gov`) could not
be reached this session (`CONNECT tunnel failed, response 502` — a proxy-level access limitation,
not a negative finding). Recommend closing this thread as resolved-with-secondary-corroboration
rather than fully primary-document-closed.

## 2. Travis County suit (SOTXEJN/Carrizo-Comecrudo v. TCEQ) — case number found, status still a
## genuine gap, now with a documented access constraint

Case number located via WebSearch and cross-checked twice: **D-1-GN-24-010020**, Travis County
District Court, filed Dec. 16, 2024 (matches the SOTXEJN press release already primary-confirmed
09-05). Attempted to reach Travis County's own case-search portals directly:
`judicial-search.traviscountytx.gov` (CONNECT tunnel failed, 502) and the district clerk's general
site (`traviscountytx.gov/district-clerk`, HTTP 200 but no case-search function on that landing
page). No dedicated public docket-lookup tool for this case was reachable through this session's
proxy. Ran two additional targeted WebSearches for any 2025/2026 ruling, dismissal, or hearing on
this specific suit — both returned only the original Dec. 2024 filing coverage and unrelated cases
(the beach-closure TX Supreme Court matter, already resolved and primary-verified 09-04, kept
surfacing as a false-positive on shared party names — confirmed it is NOT the same case: different
court, different defendants, different legal theory). **This is now a genuinely well-tested gap,
with a documented access barrier** (the court's own search portal unreachable), not an
under-searched one. If Britton wants this resolved, a direct Travis County District Clerk request
(by phone/portal, outside this session's tooling) is probably the only path — recommend not
re-running the same WebSearch pattern nightly.

## 3. FAA docket (FAA-2026-8614) — raw re-check tonight, still flat, fifth consecutive identical
## reading

Given two nights since the last raw fetch (09-04 was the last raw check; 09-05 was news-only per
that night's own recommendation), did a raw re-fetch tonight rather than another news-only pass, to
avoid the gap between "genuinely stable" and "just not re-checked" growing too long. Fetched via
`r.jina.ai` proxy (direct still 403s, unchanged across every session of this project):
- Status: **"Closed for Comments"**
- **Posted: 3,201** — identical to every reading since 09-02
- **Received: 14,670** — identical to every reading since 09-02

Also ran a fresh news search (`"FAA-2026-8614" OR "Vermilion Parish" spaceport environmental review
waiver news`) — surfaced only background material already in the corpus (the NPRM itself, the LWF/
NWF/Pontchartrain Conservancy comment letter, general project coverage). One clarification worth
logging: a search for "FAA-2026-8614" specifically also surfaced a **different, unrelated FAA
docket — FAA-2026-9736**, a Request for Information on spaceport siting/launch corridors nationally
(published Aug. 25, 2026, the same day as the Vermilion Parish announcement). **Do not conflate
these two dockets** — 9736 is a separate, national RFI process, not the Vermilion-Parish-specific
environmental-waiver NPRM this project has been tracking as 8614.

**Recommendation, now stronger than 09-04/09-05's**: this docket has shown the exact same two
numbers across five separate nightly sessions (09-02 through tonight, with one intentional skip).
Recommend fully deprioritizing to news-only, or dropping to a weekly cadence, unless a news search
specifically surfaces movement.

## 4. Boca Chica — FWS Biological and Conference Opinion addenda chain confirmed via FAA's own EA

The 09-05 note flagged a 2023 addendum and 2025 "Amended BCO Addendum #2" as an unpursued lead:
"did later addenda relax or tighten the 'not likely to jeopardize' finding as SpaceX scaled up?"
Tonight, fetched FAA's own **Final Tiered Environmental Assessment for SpaceX Starship/Super Heavy
Vehicle Increased Cadence at the Boca Chica Launch Site** directly (https://www.faa.gov/media/94346,
HTTP 200, 1.9MB, direct `curl`, `pdftotext -layout`, 4,396 lines) plus its Executive Summary
(https://www.faa.gov/media/94341, HTTP 200, direct `curl`).

**Confirmed directly from the document text**:
- **USFWS 2022** — Final Biological and Conference Opinion (already in corpus, 09-05).
- **USFWS 2023** — "Addendum to the 2022 Biological and Conference Opinion."
- **USFWS 2025 (April)** — "Final Amended Biological and Conference Opinion Addendum #2 of the
  SpaceX Starship/Super Heavy Launch Vehicle Program at the Boca Chica Launch Site in Cameron
  County Texas." Dated **April 2025** in the EA's own reference list.
- Quoted directly, verbatim, appearing twice in the document (Section 1.6 and again in the
  cumulative-impacts discussion): **"The 2022 USFWS Biological Conference Opinion (BCO), 2023
  Addendum to the BCO, and the 2025 Addendum to the BCO issued by USFWS, concluded the Proposed
  Action is not likely to jeopardize the continued existence of any federally listed species or
  adversely modify designated critical habitat."**

**This answers the 09-05 lead directly, with an important caveat on whose voice it is in**: per
FAA's own characterization of USFWS's conclusions, the "not likely to jeopardize" finding **did
not erode** across three iterations spanning 2022–2025, even as launch cadence increased (this EA
is specifically titled "...Increased Cadence"). The caveat: this is FAA's summary of USFWS's
findings inside an FAA document whose whole purpose is to support approving increased cadence — it
is a primary regulatory document, but not an independent third-party read of whether the science
actually held up; a genuinely independent assessment would need to read the 2025 Addendum #2 itself
rather than FAA's characterization of it. **The Addendum #2 document itself was not located/fetched
tonight** (only cited, dated, and titled inside the EA) — flagging as a further lead if Britton
wants the underlying USFWS document rather than FAA's summary of it.

**One additional nuance found, worth keeping distinct**: the same EA also cites a **separate** 2023
document — "USFWS. 2023. Addendum to the October 2021 Biological Assessment for the SpaceX
Starship-Super Heavy Launch Vehicle Program... Addressing Operation of a Deluge System." This is an
addendum to the *Biological Assessment* (the applicant/FAA-side document that triggers consultation)
specifically about the deluge system, not the *Biological and Conference Opinion* addendum chain
above (USFWS's own determination). Two different "2023 addendum" documents exist in this record;
don't conflate them if citing either.

Also noted in passing, useful scale context for comparing to the Vermilion Parish FAA docket: this
EA's own public comment history — Draft EA (30 days, Jul–Aug 2024): 112 comments; Revised Draft EA
(45 days, Nov 2024–Jan 2025): **12,303 comments**. The Boca Chica increased-cadence EA process alone
drew a comparable order of magnitude to the Vermilion Parish waiver docket's ~14,670 received — a
useful data point if the paper ends up characterizing "public engagement volume" as a variable
across the two sites/processes.

## 5. The "$100M coastal master plan" vs. "$25M charitable donation" discrepancy — substantially
## clarified, likely resolved as a conflation, not two competing figures for the same commitment

This was flagged unresolved 08-29 and again 09-05. Tonight's biggest find. A Verite News
investigation, republished by both Louisiana Illuminator (2026-09-05, 10:00 AM CT,
https://lailluminator.com/2026/09/05/spacex-coastal-restoration/) and The Current LA
(2026-09-04, https://thecurrentla.com/2026/will-spacex-save-louisianas-coast/) — fetched both via
`r.jina.ai` proxy after direct WebFetch 403'd on both — directly quotes **CPRA Executive Director
Michael Hare**:

> "SpaceX has not committed a predetermined amount of money to CPRA or agreed to restore a specific
> number of acres."

The article explains coastal funding "could come through several avenues as the project develops,
including required mitigation for wetlands damaged by construction, voluntary restoration and
shoreline protection, and **proceeds from SpaceX's $100 million purchase of the state-owned
property**" [emphasis added].

**Reading this plainly**: the "$100 million coastal master plan" figure that circulated in
announcement-day coverage and that this project has been treating as a distinct pledge does not
correspond to any written, contractual, or even verbally-quantified CPRA commitment — the agency's
own director says so on the record. The $100M figure appears to trace to (or be conflated with) a
**different transaction entirely**: SpaceX's **$100 million purchase price for the state-owned land
itself**, which is a land sale, not a restoration fund. Whether *proceeds* from that land sale might
eventually flow to coastal restoration is speculative per Hare's own quote ("could come through"),
not a commitment. This is consistent with, and now better-explained than, the 09-05 finding that
LED's own written "Letter of Intent for Project Osprey" contains **no line item at all** for a
"$100M coastal master plan" — because, per this finding, there may never have been one as a fixed
dollar commitment. The **$25M charitable donation to the Community Foundation of Acadiana**, by
contrast, remains the one figure on this side of the deal that is directly, contractually documented
in LED's own LOI (09-05 finding) — i.e., the $25M is the real, written commitment; the $100M
"coastal" figure looks like public-facing framing around a land-sale price, not a comparable
written pledge.

**New grounding on where the land itself came from**, also found tonight: per Gov. Landry's own
June 2026 announcement (covered independently by WBRZ, 2026-08-19, and The Advocate/Fox8, both
found via WebSearch and cross-checked — not yet independently WebFetched tonight, flagged as
WebSearch-summary tier), the ~130,000 acres were conveyed to the State of Louisiana via a **"final
settlement"** resolving a decade-plus-old wave (2013–2016) of parish-led coastal-erosion litigation
against ExxonMobil — not a direct Exxon-to-SpaceX transfer as the project's own `CLAUDE.md`
currently frames it ("former Exxon property"). **The settlement's own terms are reported as sealed
by court order** (per WebSearch summary of The Advocate's coverage — not independently confirmed,
since a sealed settlement has no public document to fetch by definition), so the state's actual
consideration to Exxon can't be verified either way. The chain, as best supported tonight: Exxon
coastal-litigation settlement (June 2026, sealed) → land conveyed to the State of Louisiana → State
sells ~130,000 acres to SpaceX for ~$100M → Landry publicly frames a "$100M coastal master plan"
commitment that CPRA's own director says has no fixed dollar or acreage figure attached to it. **One
inconsistency flagged, not resolved**: an earlier WBRZ piece (Aug. 19, 2026, pre-announcement)
describes SpaceX simply "acquiring the use of" Exxon-owned acreage directly, without the state as an
intermediary — this may just be less-precise pre-announcement reporting superseded by the fuller
September coverage, but flagging the discrepancy rather than silently picking the later version as
correct.

**Recommend treating this discrepancy as substantially resolved** (the answer being "it looks like
a conflation between a land-sale price and a restoration pledge that was never actually quantified,
per the agency's own director," not "two real figures that need reconciling") — a good, clean,
primary-quote-backed finding for whichever economic-benefit-claim-specificity framing Britton
eventually locks in, without this note picking that framing.

## 6. NDA scope — a firmer number than "dozens"

While chasing the coastal-figure story, a joint **Gulf States Newsroom / Type Investigations**
probe (covered by KPEL/96.5 KVKI, byline Joe Cunningham, published 2026-08-21 — WebFetch-summarized,
not independently primary-fetched tonight) puts a harder number on the NDA practice already flagged
09-05: **54 elected Louisiana officials** have signed NDAs tied to major industrial developments
(SpaceX, Meta/Richland Parish, Amazon, Applied Digital) since Gov. Landry took office — described as
**77% of the state Senate and 13% of the House**, including leadership of both chambers. This is
more precise than the "dozens of local and state officials" figure already in the corpus from the
WWNO/Gulf States Newsroom piece (09-05), and appears to be the same underlying investigation, just
reported with the specific count in this syndicated version. **Not independently verified against
the original Gulf States Newsroom/Type Investigations piece directly** — attempted to locate and
fetch it directly tonight, unsuccessful (WebSearch kept surfacing syndicated versions on WWNO/WRKF/
KRVS rather than a distinct Type Investigations byline page); flagging this as WebFetch-summary tier
until a direct fetch of the original happens. The **Jacob Landry NDA document itself remains
blocked** — retried the DocumentCloud path tonight via direct API/JSON endpoints
(`documentcloud.org`, `api.www.documentcloud.org`) rather than the HTML page; both returned the same
Cloudflare "Attention Required" challenge page as 09-05's attempt. Recommend not re-attempting via
DocumentCloud specifically; a different host or a direct records request would be needed.

## 7. What's still open

- Travis County suit (D-1-GN-24-010020) status — genuine gap, court search portal unreachable this
  session (502 CONNECT failures); needs either a different access path or a direct county records
  request, not more WebSearching.
- TCEQ Docket 2024-1821-IWD's actual signed Commission order — resolved via secondary corroboration
  (news-search convergence + the related federal suit's primary-confirmed dismissal) but the final
  order document itself not located; TCEQ's permit-search database unreachable this session.
- USFWS's actual 2025 "Amended Biological and Conference Opinion Addendum #2" document — cited,
  dated (April 2025), and titled via FAA's EA, but not itself located/fetched; would give an
  independent (non-FAA-summarized) read of whether the science genuinely held steady.
- The Exxon-to-state settlement (June 2026) — reportedly sealed; the WBRZ/Advocate/Fox8 coverage of
  it not yet independently WebFetched (WebSearch-summary tier only tonight); the pre-announcement
  WBRZ framing (direct Exxon-to-SpaceX) vs. later framing (Exxon-to-state-to-SpaceX) discrepancy
  not resolved.
- The original Gulf States Newsroom/Type Investigations "54 officials" piece — not directly fetched,
  only a syndicated version (KPEL/96.5 KVKI).
- Jacob Landry NDA document — still blocked at DocumentCloud via every path tried across two
  sessions now (HTML, JSON, API).
- Unchanged from prior nights: broader "Stop SpaceX" coalition-wide leadership/scale (treated as a
  closed gap per 09-05); FWS's 2023 Biological Assessment addendum (deluge-system-specific, distinct
  from the BCO addendum chain) not fetched; Act 343/HB 1250 enrolled text not independently fetched;
  "Golden Eagles' Conservation Society" filer name still unverified.
- No theory chain, coding scheme, or Study 1 option (A/B/C) decided — unchanged, still Britton's
  call.

## Summary: what's new vs. stable since 09-05

| Item | Status |
|---|---|
| TCEQ Docket 2024-1821-IWD | **Resolved** — ED recommended denying all hearing requests (primary); permit approved and a related federal suit against SpaceX (1:24-cv-00148, newly found) dismissed Feb 18, 2025 (primary court record); final signed Commission order itself not located |
| Travis County suit (D-1-GN-24-010020) | Case number found; status remains a genuine, access-blocked gap |
| FAA docket | Raw re-checked — flat at 3,201/14,670, fifth consecutive identical reading; recommend deprioritizing further |
| Boca Chica FWS BCO addenda (2023, April 2025 #2) | Chain confirmed via FAA's own EA — "not likely to jeopardize" held steady across all three; the 2025 document itself not yet independently fetched |
| "$100M coastal master plan" vs. "$25M donation" | **Substantially clarified** — CPRA's own director says no dollar/acreage commitment exists; $100M figure likely conflated with SpaceX's $100M land-purchase price, a separate transaction; $25M remains the one real written commitment |
| Land provenance (Exxon → ?) | New: state-settlement intermediary framing found (June 2026, sealed), revising the "former Exxon property" shorthand already in CLAUDE.md — not fully reconciled with one earlier, differently-framed report |
| NDA signatory count | Firmer figure found — 54 officials (77% of Senate, 13% of House), vs. "dozens" previously; not yet primary-fetched from the original investigation |
| Jacob Landry NDA document | Still blocked, all paths tried |

All claims above are labeled by tier inline: primary document directly fetched and text-extracted
(TCEQ 250213 agenda, TCEQ ED response, FAA Final Tiered EA + Executive Summary) vs. primary court
docket directly read (CourtListener, via proxy) vs. news article fetched via proxy, not
AI-search-synthesized (Illuminator/Verite coastal-restoration piece, The Current LA) vs.
WebSearch-summary only, not independently fetched (MyRGV dismissal story, WBRZ/Advocate Exxon
settlement coverage, the 54-officials KPEL/KVKI piece) — nothing load-bearing above relies on a bare
WebSearch snippet without saying so.
