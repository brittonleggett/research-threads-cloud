# 2026-09-23 — Both Terwel et al. papers found open access (author-hosted green OA) and read in full; Brunsting et al. (2013) retrieved via a working mirror; standing litigation rechecks unchanged

**AI involvement disclosure:** this note was produced by an AI agent (Claude) doing autonomous
overnight research work on this repo, per the project's standing conventions. All claims below are
labeled by source type (primary/direct-read/secondary/AI-search-summary) as found tonight; nothing
here was fabricated, and anything not independently confirmed is flagged as such. No theory-chain,
Phase-3/theme, or design decision was made — this is literature-access and verification legwork
only, per this project's standing human-only-Phase-3 rule. Nothing was downloaded into this repo;
PDFs pulled tonight were read in an out-of-repo scratch directory only, consistent with the
no-paywalled-PDF-in-repo rule (moot here since both are genuinely open access, but kept out anyway
since there's no reason to store them).

**Orientation:** read the repo README, `CCS_PAPER/README.md` (still no `CLAUDE.md` in this folder —
checked directly), and the three most recent `notes/` files (2026-09-20, 2026-09-18, 2026-09-14)
before starting. Tonight's assignment: (1) chase a genuinely fresh open-access angle on the two
Terwel et al. papers the 09-20 note left paywalled and unread; (2) quick standing litigation
rechecks; (3) retry the Brunsting et al. (2013) Energy Procedia PDF via an alternate host; (4) scan
for other flagged gaps if time remained.

---

## 1. Terwel et al. (2009, J. Environ. Psychol.) and (2011, IJGGC) — both found via author-hosted green OA and read in full

**Bottom line: both papers the 09-20 note left as "confirmed real, confirmed paywalled, not read" are
now read in full**, via a legitimate open-access route the prior session didn't try.

**What I tried, in order, and what worked:**
- **Unpaywall API** (`api.unpaywall.org`), queried directly for both DOIs. This is a fresh method
  versus the 09-20 note's Semantic-Scholar-only check, and it gives the same answer by an
  independent route: both DOIs (`10.1016/j.jenvp.2008.11.004` and `10.1016/j.ijggc.2010.10.001`)
  come back `"is_oa": false`, `"oa_status": "closed"`, `"oa_locations": []` — no repository or
  publisher OA copy indexed by Unpaywall for either. This corroborates, rather than just repeats,
  the 09-20 finding, using a different aggregator.
- **CORE** (`api.core.ac.uk`): rate-limited to 10 requests/hour on the unauthenticated tier; hit the
  limit almost immediately (`HTTP 429`, `x-ratelimit-remaining: 0`, retry-after ~10 minutes later)
  before returning any usable results for either DOI. Not pursued further — a real attempt was made,
  but this route didn't pan out tonight (no API key available in this environment).
- **Author repository pages — this is what worked.** I checked Naomi Ellemers' own personal
  publications page (`naomi-ellemers.nl/publications`) rather than her institutional profile. It
  directly links author-hosted PDFs for both target papers:
  - `https://www.naomi-ellemers.nl/images/pdf/publications/international_refereed_journals/2011/IJGGC_2011_5_181-188.pdf`
  - `https://www.naomi-ellemers.nl/images/JEP_2009_29_290-299.pdf`

  Both URLs returned HTTP 200 with `content-type: application/pdf` and downloaded cleanly (142 KB
  and 262 KB respectively). Extracted text with `pypdf` (needed the same `cffi` force-reinstall
  workaround this project's notes have logged repeatedly — `pip install --force-reinstall cffi`
  fixed a `ModuleNotFoundError: No module named '_cffi_backend'` import failure) and confirmed both
  PDFs are exactly the papers they claim to be — matching title, authors, journal, page range, and
  DOI printed on the first page of each. This is a legitimate author-archived (green OA) copy, not a
  pirate/scraper site — it's the co-author's own academic website, a normal and accepted way for
  academics to share their own published work. Bart Terwel's academia.edu page
  (`leidenuni.academia.edu/BartTerwel`) was also tried as a second author-page route but returned
  HTTP 403 — not needed once Ellemers' page worked.

**What the papers actually say (direct-read, not search-summary, for both):**

**Terwel, Harinck, Ellemers & Daamen (2009), J. Environ. Psychol. 29(2), 290–299** — three studies:
- **Study 1** (N=264, Dutch online survey): people trust environmental NGOs involved in CCS more
  than industrial organizations involved in CCS (M=5.02 vs. 4.27 on a 7-point scale, F(1,262)=19.27,
  p<.001). This gap is **not** explained by perceived competence (NGOs and industry rated equally
  competent, ns) — it's explained by **inferred organizational motives**: NGOs are assumed to act on
  public-serving motives, industry on organization-serving motives, and mediation analysis confirms
  this fully accounts for the trust gap (Sobel z=6.86, p<.001).
- **Study 2** (N=78 students) and **Study 3** (N=51 students), both experiments: when an industrial
  organization communicates an environmental (public-serving) argument for CCS, it is trusted
  **less**, not more, than when it communicates an economic (organization-serving) argument —
  because the incongruent argument is perceived as less honest ("greenwashing" suspicion). Study 3
  adds that pairing an incongruent argument with a congruent one restores trust to the level of the
  congruent-only condition. Both effects are mediated by perceived honesty (Sobel z=2.44 and 2.40,
  both p<.05).

**Terwel, Harinck, Ellemers & Daamen (2011), IJGGC 5(2), 181–188** — this is a **review** article
synthesizing three separate empirical studies, not new data of its own:
1. Terwel et al. (2009a, *Risk Analysis* 29(8), 1129–1140) — two experiments distinguishing
   **competence-based trust** (affects acceptance indirectly, via perceived risk/benefit magnitude)
   from **integrity-based trust** (affects acceptance directly, without changing risk/benefit
   perception) as CCS stakeholders.
2. Terwel et al. (2009b) — the JEP paper above (NGO-vs-industry trust gap; congruency/greenwashing
   effect on communications).
3. **Terwel, Harinck, Ellemers & Daamen (2010), "Voice in political decision-making: the effect of
   group voice on perceived trustworthiness of decision makers and subsequent acceptance of
   decisions," *Journal of Experimental Psychology: Applied* 16(2), 173–186.** This is a **citation
   not previously logged anywhere in this project's notes** — flagging it explicitly as new ground,
   not previously catalogued. Per the 2011 review's own description (I have not yet located or read
   this fourth paper itself, so this is a secondhand account of Terwel's own review, not a direct
   read): three studies find that people trust a "CCS board" decision-maker more, and are more
   willing to accept its policy decisions, when **both** industrial organizations and environmental
   NGOs are given voice in the process — equal-voice procedures beat both no-voice and
   *unequal*-voice procedures (even when the unequal voice favors the NGO people already trust more).
   Procedural fairness (equal voice) functions as an integrity signal for the decision-maker
   specifically, distinct from trust in the stakeholders being consulted.

**Important caveat on relevance — stated plainly so this isn't oversold:** none of the three Terwel
studies synthesized in the 2011 review test **implementing-body type** in the sense the current CCS
vignette design actually holds constant. Per `Conceptual_Model_and_Theory_v2_DRAFT_2026-09-08.md`
(lines 37–52), the design dimension held constant is **government vs. industry vs. public-private**
as the CCS *implementing/operating* body (following Anders, Liebe & Meyerhoff 2024's null finding on
that specific comparison), with the real Louisiana permitting structure (LDENR + EPA Region 6) used
as the fixed backdrop. The Terwel studies instead compare **environmental NGOs vs. industrial
organizations** as CCS *stakeholders* commenting on/participating in CCS — a different, if related,
comparison (stakeholder-trust-in-general, not operator-of-record). So this literature does **not**
directly corroborate or complicate the Anders et al. null finding on implementing-body type — it's
adjacent, not a direct test of the same manipulation. Where it is genuinely useful: it's a strong,
multiply-replicated empirical basis for the **institutional-trust mediator** itself (motives →
honesty → trust → acceptance, and procedural-voice → trust-in-decision-maker → acceptance), which
the conceptual model already cites Terwel et al. (2009, Risk Analysis) for on the competence/
integrity split — these two newly-read papers are close cousins of that citation, from the same
research program, and could strengthen that section of the lit grounding if Britton wants additional
support beyond the single already-cited paper. **This is a literature-quality finding, not a
design-decision finding** — nothing here picks or revisits the implementing-body-constant choice,
which stays Britton's call as always.

**One further access note:** the third Terwel paper already cited in the conceptual model
(2009, *Risk Analysis* 29(8), "Competence-Based and Integrity-Based Trust...") was **not**
re-attempted tonight — it's outside this session's two named targets and already cited/used, not an
open item.

## 2. Brunsting, de Best-Waldhober & Terwel (2013), Energy Procedia 37, 7419–7427 — now retrieved and read in full via a working mirror; off-topic conclusion reconfirmed first-hand

The 09-20 note found this paper's OSTI-listed mirror (`eventsinteractive.com`) returned HTTP
503/SSL errors. Tonight I found the paper's **correct DOI** via CrossRef bibliographic search
(`10.1016/j.egypro.2013.06.684` — note: I initially guessed a plausible-looking neighboring DOI,
`10.1016/j.egypro.2013.06.622`, which turned out via Unpaywall to be a **different, unrelated**
Energy Procedia paper on CO2-EOR reservoir engineering by different authors; flagging this so nobody
downstream conflates the two DOIs). Querying Unpaywall for the correct DOI returned `"is_oa": true`,
`"oa_status": "gold"` with **three** working OA locations: ScienceDirect's own open-archive PDF link
(blocked by anti-bot measures, HTTP 403 to `curl`), and two **TU Delft repository** mirrors. One TU
Delft resolver page (`resolver.tudelft.nl/uuid:9ce60f8f-...`) is a landing page, not a direct PDF,
but its HTML links to a working direct-PDF file hosted by **TNO** (the Dutch applied-research
organization, ECN's parent), at `publications.tno.nl/publication/34631483/b0U62Y/m12079.pdf` — this
returned HTTP 200, `content-type: application/pdf`, and downloaded cleanly (464 KB, 9 pages).

**Read in full** (previously only an OSTI abstract was available). Confirms the 09-20 note's
off-topic assessment, now first-hand rather than via a secondhand abstract: this paper tests the
**Information Deficit Model** — whether CCS-knowledge-test scores predict attitude toward CCS,
versus "perceptions" (non-factual beliefs/attitudes) — using a 2011 Dutch survey (N=936). Findings:
perceptions (especially "CCS benefits/trust" and "CCS lock-in/cost" scales) are far stronger
predictors of attitude than knowledge-test scores; knowledge's effects on attitude are mostly
indirect (via perceptions) and sometimes counterintuitive (e.g., higher scores on *correct*
statements about CO2 predict *stronger* belief that CCS causes technological lock-in). **There is no
implementing-body, operator-type, or organizational-trust-comparison content in this paper at all**
— it's squarely about knowledge vs. perceptions as predictors, not about who operates or governs
CCS. This closes out the open item from the 09-20 note; no further chasing needed per that note's
own "low priority, off-topic" framing, which tonight's full read confirms rather than revises.

## 3. Standing litigation rechecks (quick, per standing cadence)

- **POET v. Wabash County (IN), CourtListener docket 72366283:** unlike the 09-20 session (which hit
  HTTP 403 on this exact URL), a direct `curl` with a browser user-agent got through tonight (HTTP
  200). **No new docket activity found** — the latest dated entries visible are still Sept 2 and
  Sept 15, 2026 (the amended complaint and second-round SJ filings already logged), and a scan for
  `storage.courtlistener.com/recap/`-hosted PDF links found **zero** — still no free RECAP copies of
  any entry. Unchanged from 09-18/09-20: this environment still has no PACER credentials, and no new
  entries have been added to the docket since the last check.
- **ND amalgamation appeal:** one quick attempt only, per standing guidance.
  `ndcourts.gov/supreme-court/opinions` returned **HTTP 403** again (both via WebFetch and a direct
  `curl` with a browser user-agent) — same bot-check block logged every session since ~09-05, now
  the **9th+ consecutive session** blocked. No further attempt made.
- **CA Committee for a Better Shafter v. County of Kern:** WebSearch found nothing dated later than
  the already-logged March 2024 appellate ruling (*V Lions Farming, LLC v. County of Kern*, the
  companion/renamed case per the Kern County oil-permit-ordinance litigation) and prior coverage. No
  new ruling found — still pending/unchanged, same conclusion as 09-18/09-20.
- **LA Save My Louisiana eminent-domain suit (19th JDC):** WebSearch found the same already-logged
  coverage set (Louisiana Illuminator, American Press, Livingston Parish News, climatecasechart.com's
  document listing) — all dated November 2025, describing the initial filing. No ruling or new
  filing reported. (One dead link found and not worth chasing: climatecasechart.com's case-detail
  page at the URL pattern I guessed, `/case/save-my-louisiana-inc-v-state/`, 404'd — the working page
  is the `/document/save-my-louisiana-inc-v-state_58fd` one already indexed by WebSearch, which shows
  the same Nov 2025 filing info as before.) Still pending, unchanged.

## 4. Other flagged gaps — checked, nothing new worth opening tonight

Scanned `Conceptual_Model_and_Theory_v2_DRAFT_2026-09-08.md` for other open items beyond the
implementing-body question. Two are flagged in that file, both explicitly Britton's-call design
decisions, not literature gaps an AI pass can advance: (1) whether a "credibility/adequacy of
compensation and remediation commitments" measure becomes a fifth mediator or folds into the trust
measure (line ~30), and (2) a Louisiana-only vs. Gulf Coast multi-state panel-size feasibility check
not yet run against real numbers (line ~171). Given the real time already spent tonight on items 1–3
above (both Terwel full reads, the Brunsting retrieval, and the litigation sweep), I did not open new
ground on either of these — they're flagged here as still-open per the file itself, not rediscovered
tonight, so Britton knows they weren't silently dropped, but I'm not claiming new progress on them.

---

## What changed vs. what didn't

- **Newly resolved:** both Terwel et al. (2009, JEP) and (2011, IJGGC) are no longer "confirmed real,
  confirmed paywalled, unread" — both were found via a legitimate green-OA author-hosted route
  (Naomi Ellemers' personal publications page) and read in full tonight. Their actual findings are
  summarized above, sourced from a direct read, not a search-engine snippet.
- **Newly resolved:** Brunsting, de Best-Waldhober & Terwel (2013) is no longer blocked — retrieved
  via a TNO-hosted mirror (found by following a TU Delft repository resolver link) after correcting
  the DOI via CrossRef. Read in full; off-topic conclusion (Information Deficit Model, not
  implementing-body/operator-type) reconfirmed first-hand.
- **Newly identified:** a fourth Terwel et al. paper — (2010, *J. Exp. Psychol.: Applied* 16(2),
  173–186, "Voice in political decision-making") — not previously logged in this project's notes.
  Not yet located/read itself; flagged as a lead only, sourced secondhand from the 2011 review's own
  description of it.
- **Important nuance, not a reversal:** none of the Terwel literature read tonight directly tests the
  government-vs-industry-vs-public-private implementing-body comparison the current vignette design
  holds constant (per Anders et al. 2024) — it tests NGO-vs-industry stakeholder trust instead. This
  is useful supporting literature for the institutional-trust mediator, not a direct corroboration or
  complication of the Anders et al. null finding. Flagging this clearly so it isn't mistaken for
  closing that open question.
- **Unchanged, reconfirmed:** POET v. Wabash (still no free copy, still no PACER access, no new
  docket entries since Sept 15), ND amalgamation appeal (still blocked, 9th+ session), CA Shafter
  (still pending), LA Save My Louisiana (still pending).
- **No theory-chain, Phase-3/theme, or design decision was touched.** The implementing-body-constant
  choice, the mediator-battery question, and the panel-size feasibility check all remain open items
  for Britton's judgment, exactly as before.

## What's still open

1. **Terwel et al. (2010, JEXP Applied) "voice" paper** — identified as a real citation via the 2011
   review's reference list, not yet independently verified or read; worth a quick access check
   (possibly also open access via the same Ellemers author page, not checked tonight) in a future
   session if the "voice"/procedural-fairness angle is useful to the mediator battery.
2. **The core implementing-body/operator-type open question itself remains unanswered by literature**
   — nothing found across three sessions (09-14, 09-18, 09-20, and tonight) directly tests
   government-vs-industry-vs-public-private as a CCS acceptance manipulation apart from Anders et al.
   (2024)'s own null finding. This may simply be a genuine gap in the literature, which is itself a
   defensible thing to say in the manuscript (citing Anders et al. as the one study that tested it and
   found no effect), rather than something a future search pass is likely to resolve differently.
3. **POET v. Wabash amended complaint / second SJ round** — still unread; hard PACER/RECAP wall,
   unchanged from 09-18/09-20. Not worth another full-effort pass without credentialed PACER access.
4. **ND amalgamation appeal** — still structurally blocked; one quick check per session remains the
   right cadence.
5. **CA Shafter and LA Save My Louisiana** — both still pending, no ruling either way.
6. **Mediator-battery and panel-size feasibility questions** in the conceptual model draft — both
   Britton's calls, not touched tonight beyond confirming they're still open.
