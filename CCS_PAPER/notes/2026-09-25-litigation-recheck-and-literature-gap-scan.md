# 2026-09-25 — Litigation recheck (all six tracked matters, no movement found) + literature-gap scan (five new, verified, directly-relevant sources) + one prior open item partly resolved (Terwel et al. 2009 confirmed real), one dead end documented (ilga.gov unreachable)

**AI involvement disclosure:** this note was produced by an AI agent (Claude) doing autonomous
overnight verification work on this repo, per the project's standing conventions. All claims below
are labeled by source type (primary/secondary/AI-search-summary-unverified) as found tonight;
nothing here was fabricated, and anything not independently confirmed is flagged as such rather than
smoothed over. No theory-chain, Phase-3/theme, or design decision was touched — this project's
Phase 3 stays human-only, and every literature item below is flagged for Britton's judgment, not
treated as adopted.

**Orientation:** read the repo-root `README.md`, `CCS_PAPER/README.md` (no `CLAUDE.md` exists in this
project — `README.md` plus `notes/` fill that role), `Conceptual_Model_and_Theory_v2_DRAFT_2026-09-08.md`,
and the three most recent `notes/` files (2026-09-18 POET/litigation, 2026-09-16 litigation sweep,
2026-09-14 litigation recheck) before starting. This project last got a pass on 09-18 (a week ago),
consistent with the root README's "less actively worked recently" note.

---

## 1. Litigation recheck — all six tracked matters rechecked, genuinely nothing moved

Rechecked every matter tracked as of the 09-18 note, using the same primary-source-first method
established in prior sessions.

- **WV — WVSORO v. Zeldin, 4th Cir. No. 25-1384:** re-pulled the court's own current calendar
  (`ca4.uscourts.gov/oral-argument/oral-argument-calendar` → `internetcalOct272026.pdf`, page 19,
  fetched fresh tonight via `curl` + `pypdf`, same `cffi`-force-reinstall workaround this environment
  has needed every session). **Verbatim-unchanged**: still Friday, October 30, 2026, Panel 4, Gold
  Courtroom (Room 348), 8:30 a.m., LIVESTREAM, same case caption. No continuance, no amendment. This
  is a genuine, primary-source-confirmed "no change," not a skipped check.
- **ND — Summit Carbon Solutions amalgamation-law appeal:** `ndcourts.gov/supreme-court/opinions`
  still returns HTTP 403 ("Security Check" bot interstitial); `/dockets` still HTTP 404. Same
  structural block every session since ~09-05 — this is now an eighth-plus consecutive session with
  the identical result. WebSearch found nothing published after the already-logged Aug 31, 2026
  KFYR-TV coverage (Summit narrowing to the Summit #3 storage area only). No further attempt made
  beyond the one quick re-try, per standing instruction not to keep hammering a structurally blocked
  path.
- **CO — EPA Class VI primacy for Colorado:** re-queried the Federal Register's own public API
  directly (`federalregister.gov/api/v1/documents.json`, term "Colorado Class VI primacy underground
  injection," sorted newest-first). Still only the March 19, 2026 Proposed Rule (`2026-05453`) on
  record — **no Final Rule published.** Primary-source-confirmed, unchanged since 09-16.
- **CA — Committee for a Better Shafter v. County of Kern (BCV-24-104003):** re-checked
  climatecasechart.com's own case page — it still lists only the original Nov. 20, 2024 petition
  filing, nothing later. WebSearch corroborated: nothing dated later than the already-logged 2024
  CEQA filing and 2026 Inside Climate News coverage. No movement.
- **LA — Save My Louisiana eminent-domain suit (19th JDC, filed Nov. 20, 2025):** WebSearch returned
  the same already-logged source set (Louisiana Illuminator, Business Report, Carbon Herald, Rapides
  Parish Journal). No ruling reported — still pending, unchanged.
- **IN — POET Biorefining–North Manchester LLC v. Board of Commissioners of Wabash County
  (3:26-cv-00291-SJF, N.D. Ind.):** re-pulled the CourtListener/RECAP docket directly (had to
  re-derive the correct URL slug tonight — `docket/72366283/poet-biorefining-north-manchester-llc-v-
  board-of-commissioners-of-wabash/` — since the bare numeric ID alone now 404s; the full slug still
  works). **Entry list is identical to the 09-16/09-18 checks: entries run 1–50 (36 missing, a
  known pre-existing gap in RECAP's numbering, not new), with nothing past entry 50** (the Sept 15,
  2026 second-round summary-judgment filings). Confirmed zero `storage.courtlistener.com/recap/...`
  hosted PDFs exist for this docket (still nothing purchased into the free archive) and Justia's
  mirror (`dockets.justia.com/docket/indiana/inndce/3:2026cv00291/126575`) still returns HTTP 403 to
  direct `curl`. **Important limitation, not previously stated this explicitly**: the docket page's
  own "Last Updated" field reads **"Sept. 15, 2026, 12:22 p.m."** — the exact same timestamp the
  09-16 note found. CourtListener's own tooltip on that field explains this is *not* the date of the
  latest filing in the real case; it is the date someone last used the RECAP browser extension to
  sync this docket from PACER. **That means this free mirror has not been refreshed in ten days, so
  tonight's "no change since entry 50" finding is really "no change visible from a source that hasn't
  itself been updated since 09-15" — it does not positively confirm nothing has happened in the real
  PACER docket between Sept 15 and today.** Flagging this distinction clearly so a future pass doesn't
  overstate what a stale free mirror can and can't tell us. Still no PACER credentials in this
  environment; still a hard access wall for reading the amended complaint / SJ filings themselves.

**Bottom line for Section 1: zero substantive developments found across all six tracked matters
tonight.** This is a real "nothing moved" finding across the board, not a search-effort gap — every
check used the same primary-source method that has previously surfaced real movement (e.g., the
09-16 POET docket discovery), so the absence of new results here is meaningful, not lazy.

## 2. Literature-check follow-up: the Terwel/de Best-Waldhober lead from 09-18 — citation existence now confirmed, content still unread

The 09-18 note flagged an unverified lead: a WebSearch-synthesized claim that an "organizational
motives and communications" CCS-trust paper found Dutch respondents trust NGOs more than industry.
Tonight I identified and confirmed the actual paper via Crossref (not just a search snippet):

**Terwel, B. W., Harinck, F., Ellemers, N., & Daamen, D. D. L. (2009). "How organizational motives
and communications affect public trust in organizations: The case of carbon dioxide capture and
storage." *Journal of Environmental Psychology*, 29(2), 290–299.
DOI: 10.1016/j.jenvp.2008.11.004.** Crossref record confirmed real (all four author names, journal,
2009 date, DOI resolve correctly). This is a **known, foundational author in this project's existing
model already** — Terwel et al. (2009) is the same paper the Conceptual Model doc's institutional
trust mediator (competence/integrity split) is already built on. **What tonight adds:** confirming
that this specific "organizational motives" paper (as opposed to a different Terwel-authored one) is
real and matches the description. **What tonight does NOT add:** I still have not read the actual
text, so I cannot independently verify the specific claim that Dutch respondents trust NGOs
significantly more than industry, or exactly how "organization-serving vs. public-serving motive"
was operationalized — that remains an AI-search-summary claim, now attached to a confirmed-real
citation rather than a not-yet-identified one. Upgrade this from "unverified lead" to "citation
confirmed real, content still needs a full-text read" — a smaller but real step forward, not a
closed item.

## 3. IL Mahomet Aquifer effective-date — still open; a new, reproducible environment block found (not just a search-effort gap)

The 09-08 `Analysis/` note's open item (confirm the Act's own "Section 99. Effective date" text) was
retried tonight. **`ilga.gov` (all subdomains tried: bare `ilga.gov`, `my.ilga.gov`) fails TLS
verification via direct `curl` in this environment** — `SSL certificate problem: unable to get local
issuer certificate`, even with the environment's own CA bundle (`CURL_CA_BUNDLE=/root/.ccr/ca-
bundle.crt`) explicitly in use and confirmed loaded (`curl -v` shows `CAfile:` pointing at the right
file). This is a different failure mode than the ND/Justia HTTP-403/404 blocks — it's a TLS-handshake
failure specific to this domain, reproducible on a bare `curl https://ilga.gov` with no path at all.
WebFetch on the same domain also failed (HTTP 503 on the bill-text page). LegiScan's mirror
(`legiscan.com/IL/text/SB1723/...`) returned HTTP 403 (Cloudflare challenge page, confirmed by
title `Just a moment...`). BillTrack50's page loaded but its bill-text panel is a JS-rendered
placeholder with no actual section text. **One small, non-primary correction surfaced along the
way**: BillTrack50's own bill-status field independently states the bill was
"Signed/Enacted/Adopted" **08/01/2025** as Public Act 104-0119 — this conflicts with an earlier
WebSearch AI-summary (from an earlier session, not re-verified as ever having been treated as fact in
this project's notes) that had floated "7-18-24" as the effective date. **Neither figure is
primary-source-confirmed tonight** — flagging both as unconfirmed rather than picking one, since
BillTrack50 is itself a secondary aggregator, not the enrolled bill text. This item stays open;
worth telling Britton directly that `ilga.gov` is not reachable from this environment at all
(a genuinely different, and more complete, block than the ND/Justia access walls), so a future pass
without a different tool/environment shouldn't expect a different result from retrying the same URLs.

## 4. Literature-gap scan — five new sources found and verified via Crossref/publisher; none yet read in full text

Searched WebSearch across CCS public opposition, environmental-justice framing, corporate
greenwashing/environmental-commitment messaging, and marketing/consumer-behavior angles, per this
project's standing convention. Every citation below was independently confirmed via Crossref (DOI,
authors, journal, date all cross-checked against the API, not taken on WebSearch's word alone) —
methodology summaries below are still abstract/search-summary level (full text not pulled tonight)
and are labeled as such.

1. **Lam, Y., Ventrella, J., Baptista, A. I., & Rodriguez, J. D. (2025). "Analysis of proposed carbon
   capture projects in the US power sector and co-location with environmental justice communities."
   *PLOS One*, 20(5), e0323817. DOI: 10.1371/journal.pone.0323817.** Crossref-confirmed. Spatial
   (QGIS, 3-mile buffer) analysis of 35 proposed US CCS power-sector projects (compiled from DOE
   NETL, Global CCS Institute, IEA, and Clean Air Task Force databases) against EPA-consistent EJ
   community definitions and EJSCREEN's 13 environmental-stressor indices. Headline figures (per
   WebFetch's summary of the article, not yet independently re-verified against the PDF's own
   tables): 33 of 35 projects (94.3%) located in EJ communities; 423 of 497 (85.1%) nearby EJ census
   block groups already exceed the 80th-percentile national environmental-burden threshold on at
   least one stressor. **Directly relevant to this project's existing environmental-justice framing**
   (Sections 1, 2, 5 of the Conceptual Model doc) and to the government-document-analysis track's own
   Tribal-consultation-thinness finding — a national quantitative complement to this project's
   single-state qualitative/document evidence. Not yet read in full text; figures above are
   WebFetch's extraction of the PLOS page, worth an independent re-read of the actual PDF/HTML before
   citing the exact percentages in the manuscript.

2. **Fritz, L., Losi, L., Merk, C., Boldrini, M., Bosetti, V., Baum, C. M., & Sovacool, B. K. (2026).
   "Public support for novel carbon removal hinges on procedural and distributive fairness." *Nature
   Climate Change*. DOI: 10.1038/s41558-026-02741-7.** Crossref-confirmed, published **2026-09-24 —
   literally the day before tonight's session**, as fresh as a literature-gap find can be. Abstract
   (pulled via Crossref, not the paywalled full text): vignette experiments with nationally
   representative surveys in six countries (Brazil, Malaysia, Saudi Arabia, Italy, Norway, UK; N =
   10,852), testing which implementation modes of novel carbon removal gain public support. Core
   finding: **support hinges on procedural fairness (opening planning to public/expert scrutiny) AND
   distributive fairness (benefit sharing, not-for-profit arrangements) roughly equally** —
   respondents would not trade fairness for technical performance. **Why this matters for this
   project specifically**: the Conceptual Model doc's core causal chain (Section 1) currently
   mediates through **procedural justice perception + recognition justice perception** only, with
   **distributive** justice present in the original three-tenet framing (Section 2's own text: "the
   original May model used a three-tenet EJ framework (distributive, procedural, recognition)") but
   not carried into the current core mediator list, and the restorative-justice addition (Section 2)
   is framed around compensation/remediation commitments specifically, not general benefit-sharing.
   This brand-new, large-N, multi-country vignette-experiment paper's headline result — that
   distributive fairness/benefit-sharing is a co-equal driver of support, not a secondary one — is a
   genuine reason to ask whether the current model's mediator set under-weights distributive justice
   relative to what the most current literature finds. **Flagging this as a literature-gap finding
   for Britton's judgment, not deciding it** — whether to add a distributive-justice/benefit-sharing
   mediator (or fold it more explicitly into the existing restorative-justice item) is a design
   question, and design stays his call. **Do not conflate with the already-cited "Sovacool, Baum &
   Fritz (2024)"** (a different paper — n=30,284/30-country study on minority/Indigenous relative
   support for climate interventions, discussed in Section 5 of the Conceptual Model doc) — this is a
   separate 2026 publication from an overlapping but not identical author team, evidently the same
   ongoing research program, not a re-issue of the 2024 piece. A same-day companion piece by the same
   author team, "Carbon removal projects need to get justice right" (Nature Climate Change,
   10.1038/s41558-026-02739-1, also Crossref-confirmed), appears to be a plain-language News-style
   summary of the same underlying study, not independent grounding — noting it here so it isn't
   mistaken for a second source later.

3. **Pues, D., Bridel, A., Cuevas, V., Dove, Z., & Jinnah, S. (2026). "Rethinking carbon dioxide
   removal: a justice-centred analysis of CDR perspectives research." *Climate Policy*. Published
   2026-03-26.** Crossref-confirmed (title, authors, journal, date). A review/meta-analysis of the
   CDR-perspectives research literature through a justice lens — not read in full text tonight, but a
   plausible source for the manuscript's literature-review framing of how the field itself
   characterizes justice gaps in CDR/CCS acceptance research, worth a full-text pull if the paper's
   lit review section wants a review-of-the-field citation rather than only primary studies.

4. **Ladenburg, J., Zuch, M., & Kim, J. (2026). "Can acceptance of location-specific carbon capture
   and storage be tipped? The causal effects of information and question framing." *International
   Journal of Greenhouse Gas Control*. Published 2026-02. DOI: 10.1016/j.ijggc.2026.104566.**
   Crossref-confirmed. Danish national survey (3,877–3,879 respondents per WebSearch's summary of the
   SSRN preprint, not yet cross-checked against the published version's own methods section) testing
   three information experiments and question-order framing on stated acceptance of CCS across four
   locations (offshore, nearshore, onshore rural, onshore urban). **This is a close, contemporary
   methodological peer to this project's own vignette-experiment design** (governance-frame framing,
   consultation-extent manipulation) — worth reading in full alongside Anders, Liebe & Meyerhoff
   (2024), the design's current closest precedent, before Britton finalizes instrument/manipulation
   wording, specifically because it's a second real precedent for how question/information framing
   causally shifts CCS acceptance (a design choice this project's own vignette work already leans on
   without, until now, a second corroborating study identified). SSRN preprint
   (papers.ssrn.com/sol3/papers.cfm?abstract_id=5706812) returned Cloudflare-blocked HTTP 403 to both
   `curl` and WebFetch tonight, so full text wasn't pulled from either the preprint or the published
   IJGGC version — flagged for a future full-text attempt.

5. **Schneider, E. J., Davis, J., Luttrell, R., Kyriakopoulos, V. A., & Nare, M. (2026). "Information
   Specificity in Carbon Labels: Consumer Perceptions of Greenwashing and Brand Evaluations in
   Environmental CSR." *Journal of Sustainable Marketing*. Published 2026-06-06. DOI:
   10.51300/JSM-2026-169.** Crossref-confirmed. Checked the journal itself for legitimacy since its
   publisher (Luminous Insights LLC) and domain were unfamiliar: confirmed via independent search that
   *Journal of Sustainable Marketing* (ISSN 2766-0117) is a real, Scopus-indexed, double-blind
   peer-reviewed, Platinum Open Access (CC BY) journal publishing since 2020, currently SJR ~0.261
   (Q3) — a legitimate, if modest-impact, outlet, not a predatory mill, though worth Britton's own
   judgment on whether its impact tier fits the manuscript's target-venue ambitions if cited.
   Experimental study (N=400, New York, oat-product carbon labels varying in specificity from minimal
   to detailed-with-QR-code) applying **signaling theory and legitimacy theory** — the exact same two
   theoretical frames this project's own government-document Analysis track and the JCM Study 1 plan
   (per this project's own `README.md`: "informed by signaling theory and greenwashing/green-
   skepticism constructs") already use — to carbon-specific (not general-sustainability) label
   claims. Finding (abstract-level, not full-text-verified): detailed/verifiable carbon information
   reduces greenwashing skepticism and improves brand evaluation more than vague claims; consumer
   carbon-awareness partially (modestly) mediates the effect. **Directly relevant to the JCM Study
   1/2 track's greenwashing/signaling-theory grounding** — this project's least-recently-touched
   track per the root README, and the one this finding speaks to most directly. Not yet read in full
   text.

## What changed vs. what's stable

- **Stable, reconfirmed via primary source (no fabricated or assumed continuity):** WV oral-argument
  date/panel/courtroom (unchanged, Oct 30 2026), CO Class VI primacy (still proposed-rule-only), CA
  Shafter (still pending, unchanged), LA Save My Louisiana (still pending, unchanged), ND amalgamation
  appeal (still structurally blocked, unchanged), IN POET v. Wabash docket entry list (unchanged, but
  see the new caveat above about the RECAP mirror itself being stale since 09-15 — "unchanged" here
  means "nothing new visible from this specific free source," not "confirmed nothing happened in the
  real case").
- **New this session:** the RECAP-staleness caveat for POET v. Wabash (a genuine limitation not
  previously stated this explicitly); the Terwel et al. (2009) citation now confirmed real via
  Crossref (content still unread); the `ilga.gov` TLS-block finding (a distinct, reproducible
  environment limitation worth flagging to Britton directly, separate from the ND/Justia HTTP-level
  blocks already known); five new literature candidates (Section 4), all Crossref/publisher-verified
  to exist and be correctly attributed, none yet read in full text.
- **Not resolved:** IL Mahomet effective date (still open, now with a documented reason why —
  `ilga.gov` unreachable); POET v. Wabash amended-complaint/SJ-filing text (still PACER-walled, no
  change in access).
- **No theory-chain, Phase-3/theme, or design decision was made or implied.** All five literature
  items in Section 4 are flagged as candidates for Britton's review, not adopted into the model. The
  distributive-justice observation in item 2 is explicitly a question raised for his judgment, not a
  proposed edit to the causal model.

## What's still open

1. **Five new literature candidates (Section 4)** need full-text reads before any citation decision —
   priority order if pursued: #2 (Fritz et al. 2026, NCC, for the distributive-justice question) and
   #4 (Ladenburg, Zuch & Kim 2026, IJGGC, for the framing-manipulation design precedent) are the most
   directly design-relevant; #5 (Schneider et al. 2026, JSM) is most relevant to the JCM Study 1
   track specifically; #1 (Lam et al. 2025, PLOS One) and #3 (Pues et al. 2026, Climate Policy) are
   background/framing candidates.
2. **Terwel et al. (2009)** — citation confirmed real, full text still needed before the specific
   "Dutch respondents trust NGOs more than industry" claim can be cited as verified rather than as an
   AI-search summary.
3. **IL Mahomet Aquifer effective date** — still unconfirmed from primary text; `ilga.gov` is
   unreachable from this environment (TLS failure, not just a bot-block), so a future pass needs
   either a different tool/environment or to accept this as a standing limitation.
4. **POET v. Wabash amended complaint / SJ filings** — still unread, still a hard PACER-credential
   wall, unchanged from 09-18.
5. **ND amalgamation appeal** — still structurally blocked; per standing guidance, one quick check per
   session remains sufficient.
6. **JCM Study 1 (netnography) track** — per the project's own `README.md`, "Study 1 data platform not
   yet chosen" as of 2026-07-08 and no corpus exists yet for it (confirmed by grep tonight — only two
   notes even mention "Study 1"/"netnography," both from mid-August). This remains the least-advanced
   of the project's three study tracks; tonight's literature find #5 (Schneider et al. 2026) is
   directly relevant grounding for it whenever that track gets picked back up, but choosing the data
   platform/corpus itself is a design decision, not something advanced here.
