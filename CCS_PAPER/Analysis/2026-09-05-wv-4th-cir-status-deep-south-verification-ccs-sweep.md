# 2026-09-05 — WV 4th Cir. docket status re-check, Deep South Center opinion verification, national CCS/Class VI litigation sweep

## What this is

Follow-up on the 09-04 note's two flagged items (WV oral-argument date; Deep South Center precedent) plus a
general litigation/regulatory sweep for developments since 09-04. Method: CourtListener's public search API
(the docket detail/docket-entries JSON endpoints require an auth token and returned 401 in this environment —
noted below as a real access limitation, not a finding), a fresh primary-source pull and independent text
extraction of the actual Fifth Circuit opinion, and WebSearch/WebFetch corroboration from law-firm client
alerts and the Sabin Center's monthly climate litigation roundups. Everything below is sourced; primary vs.
secondary is marked explicitly.

---

## 1. WV 4th Circuit (No. 25-1384) — status re-check

**Reconfirms the 09-04 note's finding: no oral argument date is set, and "late October 2026" still does not
check out against anything found.** One correction to the 09-04 note itself, detailed below: the May 20, 2026
reply brief it flagged as unconfirmed is real.

### Primary-source docket pull (partial — access-limited)

CourtListener's RECAP docket detail and docket-entries JSON endpoints (`/api/rest/v4/dockets/{id}/` and
`/api/rest/v4/docket-entries/`) both returned **HTTP 401 Unauthorized** in this environment — those need an
API token I don't have. The public search endpoint (`/?q=...&type=r&court=ca4`) worked intermittently (some
requests succeeded, most returned 403 — looks like bot-rate-limiting on CourtListener's end, not a real
gate) and returned genuine docket data when it did work:

- **Docket ID 69917497**, filed April 11, 2025, status "Active (no termination date)."
- Docket entries actually surfaced: Entry 16 (May 9, 2025) — order granting WV/WVDEP's motion to intervene
  (matches the 09-04 note). Entry 33 (Dec 19, 2025) — an attorney (Zoe Brahamsha Palenik) terminated from the
  case on an order granting withdrawal — minor personnel matter. **Entry 50 (April 10, 2026)** — "Docket
  correction requested from American Petroleum Institute. Motion due: 04/13/2026" — i.e., API is active in
  the case, consistent with the "amicus briefs...by industry groups" the 09-04 note flagged as unverified
  beyond a summary; this is closer to independent confirmation that at least one industry amicus (API) has
  filed something, though I did not see the amicus brief itself. Total document count as of that pull: 61.
- I could not get a fresh pull of the docket's *current* (Sept 5, 2026) state — later identical/near-identical
  queries to the same CourtListener search URL returned 403. So the newest primary-source-confirmed docket
  entry I have is **April 10, 2026**; anything between then and now, I'm relying on secondary sources for.

### Secondary-source corroboration (post-April 2026)

- **InsideEPA.com, "EJ Groups Renew Standing Claims Over West Virginia Class VI Primacy Rule"** (published
  May 22, 2026, subscription-gated — I only have the search-indexed summary, not the full paywalled text):
  confirms petitioners filed a **reply brief on May 20, 2026**, and states plainly that "\[t\]heir May 20
  reply brief is the last substantive filing before the U.S. Court of Appeals for the 4th Circuit schedules
  oral arguments in the case" — i.e., **as of that article, oral argument had explicitly not yet been
  scheduled.** This *is* the InsideEPA source the 09-03 note was apparently drawing on — the 09-04 note
  couldn't confirm it existed; it does exist, dated correctly (May 20, 2026), just not accessible full-text
  behind the paywall. **Correction to the 09-04 note:** don't continue flagging the May 20, 2026 reply brief
  as unconfirmed — it's real, per this independent re-find. Only the *"late October 2026" oral-argument date*
  remains unconfirmed/unsupported by anything found in either pass.
- **Arnold & Porter, "CCUS State Update 2026"** (dated May 2026, already cited in the 09-04 note): briefing
  concluded in April 2026, oral argument not yet scheduled — consistent with the above.
- **Sabin Center for Climate Change Law, monthly "Climate Litigation Updates"** — I checked every issue from
  Jan 30, 2026 through the most recent one published, **Aug 31, 2026** (Jan 30, Mar 23, May 29, Jun 30,
  Jul 30, Aug 31). Only the Jan 30, 2026 issue mentions this case at all (summarizing the opening brief,
  no new information beyond the brief itself). **None of the March, May, June, July, or August 2026 issues
  mention WVSORO v. Zeldin, an oral argument date, or a decision.** The Sabin Center roundup is not
  exhaustive of every circuit-court filing, so silence isn't proof nothing happened, but it's a real negative
  data point: no oral-argument-scheduling news significant enough to make a widely-read climate-litigation
  tracker between February and September 2026.

**Bottom line for Britton:** as of the most recent evidence I could find (an April 10, 2026 primary docket
entry, a May 20/22, 2026 secondary report that argument was not yet scheduled, and no news of scheduling
through the Aug 31, 2026 Sabin Center roundup), **no oral argument date has been confirmed for No. 25-1384.**
Treat "late October 2026" as still unconfirmed and don't put it in the manuscript. If Britton has PACER
access, a direct docket pull there would be the fastest way to get today's actual status — I could not do
that from here (no PACER credentials in this environment).

---

## 2. Deep South Center for Environmental Justice v. EPA, 138 F.4th 310 (5th Cir. 2025) — independent verification

**I re-pulled the actual opinion PDF directly from the Fifth Circuit's own site
(https://www.ca5.uscourts.gov/opinions/pub/24/24-60084-CV0.pdf) and extracted it myself with `pdftotext`
(poppler-utils was available in this environment tonight, unlike the pdfminer workaround the 09-04 note
needed). This is a fresh, independent primary-source pull — not a re-read of the 09-04 note's extraction —
and it confirms every substantive detail the 09-04 note recorded. No errors found.**

Specifically verified against the extracted opinion text:

- **Caption/docket:** No. 24-60084, filed May 21, 2025, Fifth Circuit. Petitioners: Deep South Center for
  Environmental Justice, Healthy Gulf, Alliance for Affordable Energy. Respondents: EPA; Lee Zeldin,
  Administrator. Matches the note exactly.
- **Panel:** "Before Graves, Engelhardt, and Oldham, Circuit Judges." Opinion by "Andrew S. Oldham, Circuit
  Judge." Matches.
- **Opening lines**, quoted exactly from the extracted text: *"In 2024, the Environmental Protection Agency
  granted the State of Louisiana primary enforcement authority over a class of underground carbon
  sequestration wells. Three environmental organizations petitioned for review of the final rule granting
  that authorization. All three lack standing. We therefore dismiss the petition."* Matches the note's
  quote verbatim.
- **Disposition**, quoted exactly: *"Because all three petitioners fail to demonstrate Article III standing,
  the petitions for review are DISMISSED."* Matches.
- **Deep South's "abstract social interests" holding**, quoted exactly: *"Deep South's opposition to EPA's
  action, no matter how intense, amounts to 'a setback to \[its\] abstract social interests,' which has
  never sufficed to confer standing."* — immediately followed by the "850 hours" detail: *"Even though
  Deep South's staff has 'dedicated approximately 850 hours to education and advocacy,' \[Wright Decl. ¶ 16\]
  that claimed injury embodies the exact 'expansive theory of standing' that \[FDA v.\] Alliance \[for
  Hippocratic Medicine\] rejected."* Both match the note (note paraphrased "~850 hours" slightly but
  accurately).
- **Healthy Gulf/Alliance for Affordable Energy's injury theories** — confirmed as resting on
  speculation/attenuation/traceability grounds throughout the opinion (the words "speculat-," "attenuat-,"
  and "traceab-" recur dozens of times in the relevant sections), consistent with the note's "too
  speculative/attenuated on both injury-in-fact and traceability grounds" characterization. I did not
  re-quote every passage but the framing holds up.
- **The stringency footnote** — quoted exactly (footnote 10): *"If anything, EPA's decision to grant Class VI
  primacy to the State makes the standards stricter and hence makes the wells safer. That is because
  Louisiana's standards generally mirror the federal regulations but are more stringent in some ways. See
  Intervenor's Br. at 38–40 (collecting state standards that exceed federal ones)."* Matches the note's
  quote and its attribution to the state intervenor's brief. The sentence immediately following the footnote
  in the main text confirms petitioners' actual dispute was about *administration/enforcement* quality, not
  the stringency comparison itself — so "uncontested by petitioners on this point," as the note characterized
  it, holds up on a direct read.
- **Judge Graves's concurrence** — confirmed: "James E. Graves, Jr., Circuit Judge, concurring in the
  judgment only," and his own text uses the word **"overstated"** to describe the majority opinion
  (*"I concur in the judgment only, however, because in my view the majority's opinion is overstated."*),
  matching the note's characterization exactly.

**One thing I could not independently verify:** the specific reporter citation "138 F.4th 310." The slip
opinion PDF itself (as filed by the court) doesn't carry a permanent reporter citation — that's assigned by
West/Thomson Reuters after the fact — and my searches for that exact citation string didn't surface a
citator confirmation (just unrelated search noise). This is a minor, mechanical citation-format detail, not
a substantive-holding concern — everything about the case's identity, date, court, docket number, holding,
and reasoning is now independently confirmed twice (09-04's pdfminer extraction and tonight's pdftotext
extraction agree). Recommend a quick citation-format check (Westlaw/Lexis, if Britton has access) before
final manuscript submission, same as any other citation.

**Conclusion: the 09-04 note's account of Deep South Center is accurate and can be relied on as written.**

---

## 3. National CCS/Class VI litigation and regulatory sweep (since 09-04, with some useful older context)

### State primacy status as of tonight (for the record — not new litigation, but useful context)

Per multiple concurring secondary sources (Baker Botts Dec. 2025 client alert; Hunton "Nickel Report"; EPA
press releases; National Law Review): six states now hold final Class VI primacy, in order granted —
**North Dakota (2018), Wyoming (2020), Louisiana (Jan. 2024), West Virginia (Feb. 2025), Arizona (final Sept.
10, 2025, effective Oct. 15, 2025), Texas (final Nov. 12, 2025, effective Dec. 15, 2025).** **Colorado is the
seventh state in the pipeline** — EPA's proposed rule was signed March 16, 2026, published in the Federal
Register March 19, 2026, comment period closed May 4, 2026, virtual hearing held April 23, 2026 — **not yet
finalized** as of the most recent secondary source checked (a frESH Law Blog post dated Aug. 6, 2026, on the
Colorado–Wyoming cross-border MOU, discussed below). None of this is new tonight, but it wasn't in the
project's prior notes as a consolidated state-by-state list, so flagging it as useful background for any
"national landscape" framing in the paper.

### New/notable items found tonight

- **Colorado–Wyoming Class VI cross-border coordination MOU**, executed **May 4, 2026** (same day EPA's
  Colorado comment period closed) — governs Class VI projects within 1 mile of, or crossing, the CO/WY state
  line: permitting state must notify the other within 30 days of receiving an application, the other agency
  acknowledges within 14 days, and either state can raise legal/regulatory/environmental concerns within 60
  days and request a consultation meeting. Source: frESH Law Blog, Aug. 6, 2026
  (https://www.freshlawblog.com/2026/08/06/colorados-class-vi-primacy-and-the-colorado-wyoming-mou-...).
  Secondary source, not independently verified against the MOU text itself (I didn't find a publicly hosted
  copy of the MOU). This is the first *interstate coordination* mechanism found in this research line — worth
  a mention if the paper discusses the multi-state regulatory landscape, since it's structurally different
  from anything WV/LA-specific.
- **Louisiana — new 2026 legislative development, not previously in project notes:** **House Bill 7 (2026
  session), the "Louisiana Landowners Protection Act,"** sponsored by Rep. Mike Johnson, would have
  eliminated CCS eminent-domain authority entirely. **Rejected 12–7 by the House Committee on Natural
  Resources** after extensive testimony (per Rapides Parish Journal, April 8, 2026 — secondary source,
  local news, not independently cross-checked against the legislature's own bill-tracking site tonight).
  This is a distinct bill from HB5/HB79/HB804/Act 614, which the project's existing notes already track from
  the 2025 session — HB7 is 2026-session and appears not yet logged anywhere in `CCS_PAPER/notes/` or
  `Analysis/`. Worth a follow-up primary-source check (legis.la.gov) if Britton wants this in the legislative
  history.
- **Indiana — genuinely new geography, first CCS legal dispute found outside LA/WV/TX in this research
  line:** **POET Biorefining – North Manchester LLC v. Wabash County Board of Commissioners**, U.S. District
  Court, N.D. Indiana, Case No. 3:26-cv-00291-SJF, filed **March 5, 2026**. Challenges Wabash County Ordinance
  2025-85-07 (passed June 2025), which indefinitely bans local improvement-location permits for any
  carbon-sequestration-related structure. Theories: state preemption (Indiana law declares CCS a public
  interest), Fifth/Fourteenth Amendment takings/due-process claims (property-value destruction), and a state
  Home Rule Act violation (county allegedly lacked authority to regulate CCS at all). Seeks an injunction and
  damages. Status not reported beyond the filing. Source: The Indiana Lawyer
  (https://www.theindianalawyer.com/articles/bioprocessing-company-sues-wabash-county-board-of-commissioners-over-carbon-sequestration-ordinance),
  secondary, not independently pulled from PACER. **This is the inverse fact pattern from WV/LA** — here a
  CCS developer is suing a *local government* for restricting CCS, not community/EJ groups suing to block
  CCS. If the paper's comparative-litigation framing wants a "who sues whom" dimension, this is a genuinely
  different axis worth at least a footnote.
- **California — older but not previously in project notes, useful comparison case:** *Committee for a
  Better Shafter v. Kern County* (Kern County Superior Court, filed ~Nov. 2024), a CEQA challenge to Kern
  County's approval of **Carbon TerraVault 1** (California Resources Corp., ~1M metric tons CO2/year,
  46M-ton total capacity, near Bakersfield). Challenges the adequacy of the project's environmental impact
  report. Source: E&E News/POLITICO (https://www.eenews.net/articles/lawsuit-challenges-californias-first-carbon-capture-project/),
  secondary. **Flagging the date clearly: this is a Nov. 2024 filing, well before the 09-04/09-05 window** —
  it surfaced in tonight's general sweep, not because it's new, but because it wasn't in the project's notes
  before and is a useful fourth state/fourth legal-theory (CEQA/environmental-review-adequacy, distinct from
  standing, eminent domain, and home-rule preemption) comparison point if Britton wants a broader
  multi-theory table.
- **Confirmed still-live and unchanged:** the Save My Louisiana eminent-domain suit (19th JDC, filed Nov.
  2025) remains active; no ruling found. The Rapides Parish Journal piece frames the core unresolved legal
  question well and is worth a direct read if Britton wants a plain-English secondary summary of the
  eminent-domain-vs.-Act-851 tension, but it's local news, not a primary filing.
- **No developments found** for Arizona or Texas primacy specifically being challenged in court — several
  law-firm client alerts describe litigation risk against Texas as *anticipated* but none report an actual
  filed challenge to Texas's or Arizona's primacy grants as of tonight's search.

---

## What's still open / worth Britton's attention

- **WV oral argument date: still unconfirmed.** Best-available status: briefing closed April 2026, reply
  brief filed May 20, 2026 (now confirmed real, correcting the 09-04 note's uncertainty on that point), no
  argument scheduled as of the newest source found (Aug. 31, 2026 Sabin Center roundup, which doesn't
  mention the case at all — a negative but not conclusive signal). "Late October 2026" remains unsupported
  by anything found across two research passes — don't use it. If Britton has PACER, a live docket pull
  there would resolve this definitively; I don't have that access from this environment.
- **Deep South Center v. EPA, 138 F.4th 310 — now independently double-verified**, primary source both
  times, no discrepancies. Safe to cite as recorded in the 09-04 note. Only the bare reporter-citation
  string wasn't re-confirmed against a citator (minor, mechanical).
- **New candidates for the paper's national/comparative framing**, none yet vetted for fit or added to any
  corpus: Colorado–Wyoming interstate MOU (regulatory-coordination angle); LA HB7 2026 rejection
  (legislative-history gap); Indiana POET v. Wabash County (developer-sues-government axis, new state); CA
  Committee for a Better Shafter v. Kern County (CEQA angle, new state, older filing date — flagged clearly
  above). All are secondary-sourced tonight; none independently pulled from a court's own site the way the
  WV brief and Deep South opinion were. Treat as leads, not verified-and-ready citations.
- **CourtListener API access limitation, for whoever runs the next pass:** the docket-detail and
  docket-entries JSON endpoints need an auth token (401 without one); only the public search endpoint works,
  and it's inconsistently rate-limited (succeeded twice, 403'd on ~5 other identical/near-identical requests
  tonight). A next pass hoping for a definitive live docket read should expect the same friction, or use
  PACER directly if Britton has credentials.
- **Unchanged, explicitly not touched tonight per instructions:** McCauley volume-number issue, docx
  "51 vs. 58" reconciliation, Track A/B/C, the date-convention pick, and any theme/Phase-3/design-lock
  decisions all remain Britton's, untouched.
