# 2026-09-18 — POET v. Wabash County: attempted document pull hits a real PACER-login wall (not retrieved); litigation recheck otherwise unchanged; one unverified lit lead on implementing-body/operator-type

**AI involvement disclosure:** this note was produced by an AI agent (Claude) doing autonomous
overnight verification work on this repo, per the project's standing conventions. All claims below
are labeled by source type (primary/secondary/unverified) as found tonight; nothing here was
fabricated, and anything not independently confirmed is flagged as such rather than smoothed over.

**Orientation:** read `CCS_PAPER/README.md` and the three most recent `notes/` files (2026-09-16
litigation sweep, 2026-09-14 litigation recheck, 2026-09-14 implementing-body-constant literature
check) before starting. Confirmed against the actual files — the summary this session's task was
handed matches what's actually in the notes: POET v. Wabash County's Sept 2 amended complaint and
Sept 15 second-round summary-judgment filings were logged as docket *metadata* only (entry labels
and dates), with the underlying document text explicitly flagged as not yet pulled/read, and the
09-16 note speculated retrieval "appears to be free/cheap via PACER per the '0' cost shown for
entries checked."

---

## 1. IN POET v. Wabash County (3:26-cv-00291-SJF, N.D. Ind.) — document text NOT retrieved; this is a genuine access limitation, and one prior note's cost read needs correcting

**Bottom line up front: I could not retrieve or read the actual text of the September 2, 2026
amended complaint or the September 15, 2026 summary-judgment filings tonight.** This is a real
environment limitation, not a search-effort gap — documented below so a future pass doesn't waste
time re-trying the same blocked paths.

**Correction to the 09-16 note's PACER-cost reading:** the "0 🙏" badge next to each docket entry on
CourtListener is **RECAP's "prayer" counter** (a crowdfunding-style feature where users request that
someone else buy a document from PACER and upload it to the free RECAP archive; the number is how
many people have "prayed" for it, currently zero for every entry in this docket) — **it is not a
PACER dollar-cost indicator.** I checked the "Buy on PACER" modal's actual content and it contains
no fee information at all, just a generic pitch to install the RECAP browser extension. So the
09-16 note's inference that retrieval "appears to be free/cheap" was a misreading of the UI, not a
confirmed fact. Standard PACER pricing is $0.10/page (capped at $3.00 for most documents, waived
under $30/quarter in total usage) — plausible these documents would in fact be cheap in PACER's own
terms, but I have no source confirming that, and it's moot regardless because of the next point.

**Why I couldn't pull them:** CourtListener's docket page (`courtlistener.com/docket/72366283/...`)
confirms entries 46 (Amended Complaint, Sep 2, 2026), 47 (Motion for Summary Judgment, Sep 15), 48
(Statement, Sep 15), 49 (Memorandum in Support, Sep 15), and 50 (Notice, Sep 15) exist, but **none
of the ~50 docket entries in this case have been purchased/uploaded into RECAP's free archive** — I
confirmed this by scanning the full page for any `storage.courtlistener.com/recap/...`-hosted PDF
link (found zero) versus "Buy on PACER" links (found ~98, i.e., roughly two per entry). Every "Buy
on PACER" link resolves to `ecf.innd.uscourts.gov`, the real federal court's CM/ECF system, which
immediately redirects to `pacer.login.uscourts.gov` requiring an authenticated PACER account. I
confirmed this by direct `curl` fetch of the entry-46 link — the response is CM/ECF's own login
redirect page, not a document. CourtListener's REST API (`/api/rest/v4/dockets/...` and
`/api/rest/v4/docket-entries/...`) also requires authentication (HTTP 401) even for read-only
metadata access beyond what the public HTML page shows. I also tried Justia's docket mirror
(`dockets.justia.com/docket/indiana/inndce/3:2026cv00291/126575`) via both direct `curl` and
WebFetch — both returned HTTP 403. **This environment has no PACER account credentials** (checked
`env` for any PACER-related variables — none), so there is no path available tonight to actually
read these two filings' substance. This is worth flagging to Britton directly: getting the real text
requires someone with an actual PACER login (or a RECAP "prayer" fulfilled by another PACER user) to
buy and upload these five entries — an environment/access problem, not something a future AI pass
can solve differently by trying harder.

**What I did retrieve, for context (this is NOT the amended complaint — flagging clearly so it isn't
conflated):** the original March 5, 2026 complaint is hosted directly as a public PDF by a local news
outlet (`wane.com/wp-content/uploads/sites/21/2026/03/POET-complaint.pdf`, not behind PACER), so I
pulled and read it in full (24 pages, via `curl` + `pypdf`) to establish the underlying claims the
amended complaint most likely builds on. The original complaint pleads three counts against Wabash
County's June 2, 2025 moratorium ordinance banning local improvement-location permits for "any
structure related to any carbon sequestration project":

- **Count I — Unconstitutional Taking** (5th/14th Amendment, via 42 U.S.C. § 1983, citing *Knick v.
  Township of Scott*, 588 U.S. 180 (2019)): argues the ordinance takes POET's property interest in
  pore space (the subsurface rock cavities used for CO2 storage) without just compensation, rendering
  that pore space economically worthless with no other viable use.
- **Count II — Violation of Indiana's Home Rule Act** (Ind. Code § 36-1-3-8(a)(7), § 36-1-3-5(a)):
  argues the County lacks authority to regulate conduct the state has assigned to a state agency
  (Indiana DNR, per Ind. Code § 14-39-1 et seq. and 312 IAC 30).
- **Count III — State-law preemption**: argues the ordinance directly conflicts with and is
  preempted by Indiana's 2019/2022 CCS-authorizing statutes (Ind. Code §§ 14-39-2-5 to -7), which
  expressly permit CCS projects and vest permitting authority in IDNR.

Relief sought: declaratory judgment that the ordinance is unconstitutional/void, injunctive relief,
just compensation, and attorneys' fees under 42 U.S.C. § 1988. Given (per the 09-16 note's docket
read) that Wabash County's motion to dismiss (Apr 27, 2026) doesn't show a visible resolution in the
entry labels, and POET filed its *first* summary-judgment motion May 27 before amending its complaint
Sept 2 and filing a *second* summary-judgment motion Sept 15 — the amended complaint likely either
adds/refines claims or responds to something raised during the first SJ round (a new fact, a standing
argument, narrowed relief, etc.), but **this is inference, not confirmed** — I want to be explicit
that I do not know why POET amended, and the docket's terse category labels alone can't answer that.
This is exactly the kind of detail only the actual amended-complaint text would resolve, which is
what's still blocked.

## 2. Other tracked litigation — quick recheck, all "nothing moved" confirmed since 09-16

- **North Dakota amalgamation appeal:** one quick re-attempt only, per standing instruction not to
  keep hammering this. `ndcourts.gov/supreme-court/opinions` still returns HTTP 403 (bot-check
  interstitial); `ndcourts.gov/dockets` still HTTP 404. Same structural block as every session since
  ~09-05, now a seventh-plus consecutive session. No further attempt made tonight. WebSearch also
  turned up nothing newer than the Aug 31, 2026 KFYR-TV coverage already logged (Summit forfeited two
  of its three ND storage permits, continuing the fight only over the Summit #3 area; both the
  voided-permit ruling and the underlying-law ruling remain on appeal to the ND Supreme Court with no
  docket number/schedule reachable from this environment).
- **Colorado Class VI primacy:** re-queried the Federal Register's own public API directly
  (`federalregister.gov/api/v1/documents.json`, sorted newest-first). Still only the March 19, 2026
  Proposed Rule (`2026-05453`) on record — no Final Rule published. Primary-source-confirmed, no
  movement since the 09-16 check.
- **CA Committee for a Better Shafter v. County of Kern:** WebSearch found nothing dated later than
  the case's already-logged 2024 CEQA ruling and 2026 Inside Climate News coverage. No movement
  found.
- **LA Save My Louisiana eminent-domain suit (19th JDC, filed Nov. 20, 2025):** WebSearch found the
  same already-logged coverage set (Louisiana Illuminator, Business Report, Rapides Parish Journal).
  No ruling reported — still pending, unchanged.
- **WV WVSORO v. Zeldin:** not touched tonight, per the 09-14 note's guidance that it's already
  primary-confirmed (Oct 30, 2026 oral argument) and not due for recheck yet.

## 3. Literature-check follow-up on the implementing-body-constant open item — inconclusive, one unverified lead only

The 09-14 note's still-open item was whether any *other* CCS/pipeline acceptance study tests
operator/implementing-body type as a factor (to corroborate or complicate the Anders, Liebe &
Meyerhoff 2024 null finding the design currently relies on). I WebSearched for the three
not-yet-full-text sources named in `Conceptual_Model_and_Theory_v2_DRAFT_2026-09-08.md` Section 8,
item 6:

- **Sovacool, Baum & Fritz (2024)** and its companion **World Development (2024)** piece on
  minority/Indigenous perceptions of climate interventions — based on search-result summaries only
  (I did not pull full text tonight), these appear to be about geoengineering/CDR technologies
  broadly and Indigenous/minority-group attitudes, not an implementing-body/operator-type
  manipulation.
- **Chailleux, Arnauld de Sartre & Briday (2023)** — appears (per search-result title/abstract) to be
  a French CCUS ecological-modernization framing-coalition study (qualitative, industry/policy
  framing), not an operator-type experiment.
- **Lefstad, Allesson, Busch & Carton (2024)** — appears to be "Burying problems? Imaginaries of
  carbon capture and storage in Scandinavia" (ERSS 113), a qualitative-imaginaries study, not an
  operator-type experiment either.

None of these three look, from search summaries alone, like they test implementing-body/operator
type as a factor — so this pass does not close the open item, but also doesn't find anything in them
worth pulling full-text for on this specific question. **One unverified lead surfaced instead:** a
broader search turned up an older Terwel/de Best-Waldhober-line paper on how "organizational motives
and communications affect public trust" in CCS, comparing government/industry/NGO actors and finding
Dutch respondents trust NGOs more than industry — potentially a more directly relevant counter-source
to the implementing-body-constant design choice than any of the three papers above. **I have not read
this paper and I'm not citing it as confirmed** — WebSearch's own synthesis of snippets asserted
"operator type significantly influences acceptance through trust mechanisms," but that's an AI
search-summary claim I have not independently verified against the actual paper, so it should be
treated as an unverified lead only, flagged for a future full-text pull if Britton wants to keep
pursuing this question, not as new grounding.

---

## What changed vs. what didn't

- **Not resolved (real limitation, not a gap in effort):** POET v. Wabash County's Sept 2 amended
  complaint and Sept 15 SJ filings remain unread — this environment lacks PACER credentials and
  RECAP has no free-archive copies of these documents yet. Multiple independent retrieval paths were
  tried and all dead-ended at a login wall (CourtListener HTML/API, direct PACER ECF, Justia via curl
  and WebFetch).
- **Corrected:** the 09-16 note's inference that these documents are "free/cheap via PACER" was based
  on misreading RECAP's "prayer" counter as a cost figure — it isn't; no fee information was found at
  all tonight.
- **New context (not a substitute for the amended complaint):** original March 5, 2026 complaint's
  three counts (unconstitutional taking, Home Rule Act violation, state preemption) read in full from
  a public PDF, for background only.
- **Unchanged, reconfirmed:** ND amalgamation appeal (still blocked, 7th+ session), Colorado Class VI
  primacy (still proposed-rule-only, Federal Register API-confirmed), CA Shafter (still pending), LA
  Save My Louisiana (still pending).
- **No theory-chain, Phase-3/theme, or design decision was touched** — this project's Phase 3 stays
  human-only, and nothing here makes or implies a design call; the literature lead in Section 3 above
  is flagged for Britton's judgment, not treated as resolved.

## What's still open

1. **POET v. Wabash amended complaint / second SJ round — still unread.** The only way forward is a
   real PACER account (someone logs in and buys the ~5 documents, likely a few dollars total under
   standard $0.10/page pricing) or waiting for another RECAP user to fulfill the "prayer" — this
   environment cannot do either. Worth telling Britton directly this is a hard access wall, not
   something worth another AI pass without a credentialed PACER path.
2. **Why POET amended its complaint on Sept 2** (after its first SJ motion, before its second) is
   unknown — inference only in Section 1 above, not confirmed.
3. **ND amalgamation appeal:** still structurally blocked; per standing guidance, one quick check per
   session is enough, don't over-invest.
4. **IL Mahomet Aquifer effective-date confirmation:** still open from the 09-08 `Analysis/` note, not
   attempted tonight — lower priority, unchanged status.
5. **Implementing-body/operator-type literature lead** (Terwel/de Best-Waldhober organizational-trust
   paper) is unverified — flagged for a future full-text pull, not yet grounding for anything.
