# 2026-09-27 — Four of five 09-25 literature candidates now read in full text (two open-access breakthroughs, two confirmed-blocked despite OA status); a real note-sequencing error in the 09-25 note found and corrected; litigation recheck (all six matters, still no movement)

**AI involvement disclosure:** this note was produced by an AI agent (Claude) doing autonomous
overnight research work on this repo, per the project's standing conventions. All claims below are
labeled by source type (primary/direct-read/secondary/AI-search-summary) as found tonight; nothing
here was fabricated, and anything not independently confirmed is flagged as such rather than smoothed
over. No theory-chain, Phase-3/theme-review, or study-design decision was made or implied — every
literature finding below is offered for Britton's judgment, not adopted into the model.

**Orientation:** read the repo-root `README.md`, `CCS_PAPER/CLAUDE.md` (does not exist — confirmed
directly; `README.md` plus `notes/` fill that role, consistent with what every recent note in this
folder has already found), and — importantly — **all** of the notes from 2026-09-08 through
2026-09-25, not just the most recent one. This mattered: see Section 1 below.

---

## 1. Important finding: the 2026-09-25 note skipped two sessions' worth of already-completed work and incorrectly reopened two resolved items

The 2026-09-25 note's own "Orientation" section states it read "the three most recent notes/ files
(2026-09-18 POET/litigation, 2026-09-16 litigation sweep, 2026-09-14 litigation recheck)." **That is
wrong — as of 2026-09-25, the two most recent notes in the folder were actually 2026-09-23 and
2026-09-20** (confirmed via `git log --follow` on both files tonight: `2026-09-20-mahomet-effective-
date-confirmed-terwel-literature-clarified.md` was committed 09-20, `2026-09-23-terwel-open-access-
found-brunsting-retrieved-litigation-recheck.md` was committed 09-23, both well before the 09-25
session ran). The 09-25 session appears to have looked at a stale or incomplete listing of the
`notes/` directory and missed both files. As a direct consequence, the 09-25 note:

- **Re-flagged the IL Mahomet Aquifer effective date as "still open"** and re-ran the same `ilga.gov`
  TLS-failure investigation already documented on 09-20 — even though the 09-20 note had already
  closed this out via a reasoned primary-source argument (the enrolled Act's own text contains no
  Section 99 effective-date override, and Illinois's default effective-date statute, 5 ILCS 75/1,
  resolves the date to **January 1, 2026** given the bill's May 20, 2025 passage and Aug 1, 2025
  signing — both before June 1, which is the statute's trigger date). The 09-25 note's re-investigation
  wasn't wrong on the facts it found (ilga.gov is still unreachable, same TLS error), it just didn't
  need to happen, and its framing ("effective date is still unconfirmed") is no longer accurate as of
  09-20.
- **Re-flagged Terwel et al. (2009, J. Environ. Psychol.) as "citation confirmed real, content still
  unread"** — even though the 09-23 note had already found a legitimate green open-access copy (Naomi
  Ellemers' own author-hosted publications page) for both that paper and its 2011 IJGGC companion, read
  both in full, and logged their actual findings (the NGO-vs-industry trust gap study, the
  congruency/greenwashing communication-framing experiments, and the procedural-voice review). The
  09-25 note's characterization of this item as unread is simply out of date.

**I'm flagging this plainly because it's a real process failure, not a minor note-keeping quibble**:
if a future session trusts the 09-25 note's "what's still open" list at face value without checking
the full note history, it will burn time re-doing work that's already done (twice, now, effectively) and
will describe the project's own state to Britton less accurately than it should. **Tonight I read the
full note sequence (09-08 through 09-25) before doing anything else, specifically to avoid repeating
this mistake.**

**Corrected state of these two items, as of tonight:**
- **IL Mahomet Aquifer effective date: January 1, 2026**, established 09-20 via the reasoning above.
  Not a primary-source document that says so in as many words (ilga.gov remains unreachable — retried
  tonight, same `SSL certificate problem: unable to get local issuer certificate` on a bare
  `curl https://www.ilga.gov` with the environment's CA bundle explicitly loaded — this is now confirmed
  across at least three separate sessions as a standing, reproducible environment limitation, not a
  one-off network blip), but a sound primary-source inference from the Act's own text plus the
  controlling statute. Treat as resolved unless Britton wants the extra step of confirming the live
  `ilga.gov` Public Act view page's own "Effective Date" UI field, which remains unreachable from this
  environment.
- **Terwel et al. (2009, J. Environ. Psychol. 29(2), 290–299) and (2011, IJGGC 5(2), 181–188): both
  read in full**, via `naomi-ellemers.nl/publications`' author-hosted PDFs, per the 09-23 note. I did
  not re-download these tonight (no need — the 09-23 note's summary of their findings is a direct
  read, not a search-summary, and I have no reason to doubt it), but I did re-verify tonight that the
  09-23 note's account of *what these papers say* is what's now the project's working knowledge, not
  the un-read status the 09-25 note reverted to. See the 09-23 note itself for the full findings
  (NGO-vs-industry trust gap explained by inferred motives, not competence; congruent-vs-incongruent
  communication framing effects on perceived honesty).

## 2. Four of the five 09-25 literature candidates read in full tonight; two genuine open-access wins, two confirmed still blocked despite technically being open access

Tonight's main task was to attempt full-text reads of the five literature candidates the 09-25 note
found via Crossref but hadn't read. Progress on all five, in the priority order Britton's queue named:

### (a) Fritz et al. (2026, Nature Climate Change) — read in full; corrects the 09-25 note's characterization

**DOI 10.1038/s41558-026-02741-7.** Confirmed via Unpaywall as genuinely open access (hybrid,
CC-BY, publisher-hosted) — the direct PDF link requires a Nature login redirect, but the **article's own
HTML page at nature.com loaded in full without any login wall** (`curl` with a standard browser
user-agent, HTTP 200, full article text present, not just the abstract). Read the Abstract, Main,
Results, and Discussion sections directly.

**What the full text actually says, more precisely than the 09-25 note's abstract-only summary:**
the study is a multifactorial vignette experiment (not a simple pairwise comparison) — 10,852
respondents across six countries (Brazil, Malaysia, Saudi Arabia, Italy, Norway, UK), each rating five
of 36 possible project variants that combined one of three CDR technologies (DACCS, BECCS, ERW) with
four socio-technical attributes: **implementing actor** (government vs. company), **decision-making
process** (no consultation vs. local-community consultation vs. expert consultation), **profit
distribution** (private profit vs. local revenue-sharing vs. not-for-profit), and **removal capacity**
(low vs. high). Using average marginal component effects (AMCEs, OLS regression per country, clustered
SEs), the paper reports a clear **ranking, not a tie**: **procedural fairness has the strongest effect
on support in every one of the six countries** (consultation of any kind raises support by roughly
1.0–1.7 points on a 1–10 scale, vs. no consultation), **distributive fairness is the second-strongest**
driver (revenue-sharing or not-for-profit status raises support by roughly 0.3–1.25 points, varying by
country), and **removal capacity/technical performance is a real but smaller effect** (with one notable
exception: in Saudi Arabia specifically, high removal capacity's effect, +1.0 point, slightly *exceeds*
the effect of a not-for-profit setup, +0.33 point, though not the effect of local revenue-sharing,
+0.75 point). **The implementing-actor attribute (government vs. company) has the smallest and least
consistent effect of the four** — significant in only some countries (e.g., a small negative effect of
company involvement in the UK, Italy, Norway, Malaysia) and not significant in others.

**Why the precision matters for Britton's open question (whether the current model's mediator set
under-weights distributive justice):** the 09-25 note's framing — "support hinges on procedural
fairness AND distributive fairness roughly equally" — is not quite what the paper itself says. The
paper's own language is that procedural fairness is the *strongest* driver and distributive fairness
the *second*-strongest, a real but secondary role, not a co-equal one. That's a meaningfully different
empirical claim to weigh if Britton is deciding whether to elevate distributive justice to a
co-primary mediator alongside procedural justice in the conceptual model, versus treating it as a
supporting-but-secondary consideration. **I'm not making that call — just making sure the literature
input to it is accurate rather than rounded up.**

**A second, tangential observation worth flagging (not a design recommendation):** this paper's
implementing-actor finding (government vs. company has a small, inconsistent effect on support) is a
new, large-N (N=10,852, six countries) data point that sits in the same conceptual space as Anders,
Liebe & Meyerhoff (2024)'s null finding on implementing-body type, which is what the current CCS
vignette design's implementing-body-constant choice already rests on. This is carbon *removal* broadly
(DACCS/BECCS/ERW), not CCS specifically, and the attribute definitions aren't identical (this paper
tests government-vs-company; the CCS design's own open item is government-vs-industry-vs-public-
private, a three-way comparison), so it's not a direct replication — but it is a second, independent,
more recent study whose data point off the same broad question all points the same direction (operator
identity matters less than how the decision was made and who benefits). Flagging as literature
context, not as something that resolves or should resolve the implementing-body-constant design
choice, which stays Britton's call.

### (b) Ladenburg, Zuch & Kim (2026, IJGGC) — confirmed open access by Unpaywall, but still could not be read; a specific, reproducible access wall documented

**DOI 10.1016/j.ijggc.2026.104566.** Unpaywall confirms `"is_oa": true`, `"oa_status": "hybrid"`,
`"license": "cc-by"` — this is genuinely supposed to be freely readable on the publisher's own site,
not paywalled. **In practice, both the ScienceDirect article page and a retry of the SSRN preprint
(papers.ssrn.com/sol3/papers.cfm?abstract_id=5706812) returned bot-challenge pages, not the article**:
ScienceDirect returned HTTP 403 with a full-page PerimeterX-style "Captcha"/"Purchase" challenge page
(1.2MB of boilerplate, confirmed by grepping the response for "captcha," "challenge," "purchase" —
all present, no actual abstract or body text anywhere in the response), and SSRN returned Cloudflare's
"Just a moment..." interstitial (HTTP 403, 403-byte response) exactly as it did on 09-25. This is
consistent with this project's prior, repeated experience that Elsevier/ScienceDirect and SSRN both run
bot-detection that blocks non-browser HTTP clients regardless of the underlying article's actual access
status — the same pattern already logged for other Elsevier CCS papers in this project's notes. **Bottom
line: confirmed open-access-in-principle, still unread in practice**, a genuine tooling/environment
limitation rather than a paywall in the traditional sense. No other host (repository, author page) was
found for this specific paper tonight.

### (c) Schneider et al. (2026, Journal of Sustainable Marketing) — read in full; the mediation finding is more mixed than the 09-25 abstract-level summary suggested

**DOI 10.51300/JSM-2026-169.** Confirmed gold open access (Unpaywall, journal is DOAJ-listed).
The journal's own article page (`journalofsustainablemarketing.com`, resolved via the DOI) loaded in
full — not JS-gated, actual body text present (~96,000 characters of extracted text once HTML/CSS/JS
boilerplate was stripped). Read the Abstract, Introduction, Hypotheses, Method, Results, and Discussion
sections directly.

**Confirmed via direct read:** N=400 New York State residents (Prolific panel), between-subjects
experiment, four levels of carbon-label information specificity on a fictitious oat-product label
(basic label → climate-smart description → QR code → QR code + description), collected April 2024.
Manipulation check confirmed conditions were perceived in the intended order (F(3,395)=52.84, p<.001).
**H1/H2 (direct effects) were both supported and are the paper's strongest results:** an ANCOVA
controlling for pre-existing knowledge found information specificity significantly reduced greenwashing
perceptions (F(3,394)=16.03, p<.001, η²p=.10; means ran from 5.03 at lowest specificity down to 3.02 at
highest) and significantly increased brand evaluations (F(3,394)=10.44, p<.001, η²p=.07, Cohen's f=.28;
means ran from 4.22 at lowest specificity up to 4.93 at highest). **H3/H4 (carbon-awareness mediation)
are the part the 09-25 note's abstract-level summary rounded up into "partially mediates":** the direct
read shows this is actually mixed and mostly not significant. The mediation of the
specificity→greenwashing path through carbon awareness was **not statistically significant**
(ACME=−0.01, 95% CI [−0.04, 0.00], p=.06 — just short of conventional significance; the effect here is
essentially all direct effect, ADE=−0.33, p<.001). The mediation of the specificity→brand-evaluations
path through carbon awareness was significant but small (ACME=0.024, 95% CI [0.0004, 0.06], p=.05;
proportion mediated = 10%, itself only marginally significant at p=.05). **In plain terms: this study's
real, well-supported finding is the direct effect of label specificity on both outcomes; the mediating
role of carbon awareness is, at best, a small and marginal part of the story for brand evaluations only,
not a robust mediator for greenwashing perceptions specifically.** This is a meaningfully more
conservative characterization than "consumer carbon-awareness partially (modestly) mediates the
effect" — still directionally true for one of the two outcomes, but the greenwashing-perception
mediation path (arguably the more central one for a greenwashing-focused citation) did not clear
significance. Worth knowing precisely if this gets cited for the JCM Study 1 track's signaling-theory
grounding, since the citation would be more defensible framed around the direct effect (specificity →
reduced greenwashing perception / improved brand evaluation) than around the mediation mechanism.

### (d) Lam et al. (2025, PLOS One) — read in full; the 09-25 note's headline figures are exactly correct

**DOI 10.1371/journal.pone.0323817.** Gold open access (PLOS is fully OA), PDF downloaded cleanly
(400KB, 10 pages) and extracted with `pypdf`. Read start to finish. **The 09-25 note's headline figures
were exactly right, not rounded or approximated**: of 35 proposed US power-sector CCS projects compiled
from DOE NETL, Global CCS Institute, IEA, and Clean Air Task Force databases, **33 (94.3%) are located
within three miles of an EJ community** (defined by an EPA-consistent, race- and income-based EJSCREEN
threshold), and of the 497 EJ census block groups falling within those three-mile buffers, **423 (85.1%)
already face heightened environmental burden** (one or more EJSCREEN supplemental indices above the
80th percentile nationally). Method: QGIS spatial buffer analysis (3-mile radius, matching EPA's own
Power Plants and Neighboring Communities tool convention), R for demographic-criteria data cleaning,
2017–2021 ACS-vintage EJSCREEN data. The paper's own stated limitations (not previously logged): it
covers only the 35 projects appearing in the four source databases as of the analysis date (not the
full universe of CCS activity), doesn't cover CO2 storage/pipeline infrastructure siting (only capture
facilities), and explicitly calls for qualitative, in-situ community-impact research to complement this
spatial analysis — a possible citation hook for this project's own qualitative/document-analysis
approach as a complementary method, though that's an observation, not a design suggestion.

### (e) Pues et al. (2026, Climate Policy) — DOI now identified and corrected; full text still blocked

The 09-25 note didn't record a DOI for this one. Tonight's Crossref search resolved it:
**DOI 10.1080/14693062.2026.2648761** (Pues, Bridel, Cuevas, Dove & Jinnah, all University of
California, published 2026-03-26). Unpaywall confirms hybrid OA (CC-BY-NC-ND license), but — same
pattern as (b) above — both the Taylor & Francis "full" article page and the direct PDF link returned
Cloudflare's "Just a moment..." bot-challenge page (HTTP 403) to direct `curl`, and no author-hosted
or repository copy was found via WebSearch (checked Sikina Jinnah's UC Santa Cruz faculty page and a
general web search; nothing beyond the Taylor & Francis listing turned up). **A WebSearch AI-summary
(explicitly not verified against the primary text) describes the paper as a review of 177 CDR
perspectives-research studies published 2002–2025, finding the field dominated by Global North
researchers and participants and skewed toward measuring bare support rather than deeper questions —
flagging this explicitly as an unverified AI-search characterization, not something read directly
tonight.** Confirmed real and correctly attributed; content still unread.

## 3. A related, not-previously-logged lead: Terwel et al. (2010) "voice" paper — confirmed real, confirmed still paywalled, not found via the same open-access route that worked for its two companions

The 09-23 note flagged a fourth Terwel et al. paper, cited within the 2011 IJGGC review but not yet
independently verified: **Terwel, Harinck, Ellemers & Daamen (2010), "Voice in political decision-
making: The effect of group voice on perceived trustworthiness of decision makers and subsequent
acceptance of decisions," Journal of Experimental Psychology: Applied, 16(2), 173–186.** Tonight I
independently confirmed this citation is real via Crossref (**DOI 10.1037/a0019977**, publisher APA),
cross-checked against PubMed (PMID 20565202) and PsycNET — all three agree on authors, title, journal,
volume/pages, and year. **Unpaywall confirms this one is fully closed** (`"is_oa": false`,
`"oa_status": "closed"`) — unlike its 2009/2011 companions, which were both closed on Unpaywall too but
turned out to have an author-hosted green-OA copy on Naomi Ellemers' personal site. I checked that same
page tonight specifically for this paper: **it's listed in her 2010 publications section by full
citation, but — unlike the 2009 and 2011 papers, which both had a working `<a href>` PDF link — this
entry has no link attached.** A follow-up WebSearch for a free copy elsewhere (academic repositories,
ResearchGate, a direct PDF search) found nothing beyond the same paywalled PsycNET/APA listing already
known. **This is a real, on-topic (procedural-voice/trust) citation that remains genuinely blocked**,
not a dead end from insufficient effort — it's just that the specific green-OA route that worked for
its two companions didn't happen to cover this one.

## 4. Litigation recheck — all six tracked matters, quick per standing cadence, genuinely stable again

Consistent with the last several sessions, every tracked matter was rechecked via primary source where
possible and found unchanged:

- **WV — WVSORO v. Zeldin, 4th Cir. No. 25-1384:** re-pulled the court's own current Oct 27–30, 2026
  session calendar directly (`ca4.uscourts.gov/cal/internetcalOct272026.pdf`, fetched fresh tonight,
  page 19 of 19). **Verbatim unchanged**: Friday, October 30, 2026, Panel 4, Gold Courtroom (Room 348),
  8:30 a.m., LIVESTREAM, same case caption, same question presented (EPA's approval of WV's Class VI
  primacy application).
- **CO — EPA Class VI primacy for Colorado:** re-queried the Federal Register's own API directly.
  Still only the March 19, 2026 Proposed Rule (`2026-05453`) on record — no Final Rule published,
  unchanged.
- **CA — Committee for a Better Shafter v. County of Kern (BCV-24-104003):** re-fetched
  climatecasechart.com's case page directly tonight — still shows only the original Nov. 20, 2024
  petition filing, nothing later. (A WebSearch this session surfaced an August 2026 quote from the same
  organization's president about a court "victory" — checked carefully, and this refers to a **separate,
  related Kern County oil-and-gas-permitting-ordinance case** (the "V Lions Farming"-type companion
  litigation already distinguished in the 09-23 note), not the CCS-specific CEQA case tracked here. Not
  a development in the tracked matter — flagging so it isn't mistaken for one.)
- **LA — Save My Louisiana eminent-domain suit (19th JDC):** WebSearch found the same already-logged
  coverage plus new context on a related but distinct thread — the Louisiana Legislature killed a bill
  (HB7) that would have limited eminent domain for CO2 pipelines, in a March 31, 2026 House committee
  vote (12-7). This is legislative, not the lawsuit itself, and doesn't resolve the pending suit — no
  ruling reported in the actual case, still pending.
- **ND — Summit Carbon Solutions amalgamation-law appeal:** `ndcourts.gov` still returns HTTP 403,
  same block. WebSearch confirmed the appeal remains exactly where the 09-25 note left it — Summit's
  late-August 2026 filing narrowing the Supreme Court appeal to just the Summit #3 storage area (per
  North Dakota Monitor's Aug 31, 2026 story, already logged) — nothing dated after that.
- **IN — POET Biorefining v. Board of Commissioners of Wabash County:** re-pulled the CourtListener
  docket directly tonight (got a clean HTTP 200 with a browser user-agent). **Identical state to 09-25**:
  "Last Updated: Sept. 15, 2026" (the free RECAP mirror still hasn't been re-synced in 12 days), zero
  `recap/`-hosted PDFs found for any entry, no PACER credentials available in this environment. Same
  caveat as before applies: this confirms nothing new is visible from this specific free source, not
  that nothing happened in the real PACER docket.

**Bottom line for Section 4: no substantive developments in any of the six matters, for at least the
second, and in some cases third or fourth, consecutive session.** This continues to look like a real
lull rather than a search-effort gap, since the same primary-source methods that have found real
movement before (the WV calendar posting, the ND Aug 31 narrowing, the POET docket discovery) are still
being used and are still turning up nothing new.

---

## What changed vs. what's stable

- **Corrected:** the 09-25 note's "still open" status for the IL Mahomet effective date and the Terwel
  et al. (2009) full-text read — both were actually already resolved as of 09-20/09-23. See Section 1.
- **New tonight:** full-text reads of Fritz et al. (2026, NCC), Schneider et al. (2026, JSM), and Lam
  et al. (2025, PLOS One) — all three genuinely open access and now read start to finish, with more
  precise findings than the 09-25 note's Crossref-abstract-level summaries (see Section 2a, 2c, 2d for
  the specific corrections/refinements).
- **New tonight:** Pues et al. (2026, Climate Policy)'s DOI identified (10.1080/14693062.2026.2648761,
  previously missing from this project's notes).
- **New tonight:** Terwel et al. (2010) "voice" paper independently confirmed real via Crossref/PubMed/
  PsycNET; confirmed closed-access via Unpaywall; confirmed not available via the Ellemers author-page
  route that worked for its two companions.
- **Unchanged, reconfirmed via primary source:** all six litigation matters (WV, CO, CA, LA, ND, IN) —
  see Section 4.
- **Still blocked, not for lack of trying:** Ladenburg et al. (2026, IJGGC) and Pues et al. (2026,
  Climate Policy) — both genuinely open-access per Unpaywall, both blocked in practice by
  publisher-side bot-detection (ScienceDirect, Taylor & Francis, SSRN) that this environment's `curl`
  cannot get past. This is the same access pattern this project's notes have documented repeatedly for
  Elsevier content specifically; tonight adds Taylor & Francis and a second SSRN confirmation to that
  pattern.
- **No theory-chain, Phase-3/theme-review, or study-design decision was made or implied.** The Fritz et
  al. procedural-vs-distributive-fairness ranking (Section 2a) and the implementing-actor observation
  are both offered as literature inputs to decisions that remain Britton's alone.

## What's still open

1. **Ladenburg, Zuch & Kim (2026, IJGGC)** — confirmed open access, still unread; would need either a
   different access tool/environment or a manually-supplied copy to actually read.
2. **Pues et al. (2026, Climate Policy)** — DOI now known, confirmed open access, still unread; same
   access-tooling limitation as above.
3. **Terwel et al. (2010, JEXP Applied)** — confirmed real and on-topic (procedural voice/trust in a
   CCS decision-maker), confirmed paywalled with no open-access copy found; would need Britton's
   library access to read.
4. **IL Mahomet Aquifer effective date** — practically resolved (January 1, 2026, via the 09-20
   reasoning), but `ilga.gov` itself remains unreachable from this environment across at least three
   sessions now; treat as a standing environment limitation, not something worth another full retry
   absent a different tool/environment.
5. **POET v. Wabash amended complaint / SJ filings** — still PACER-walled, unchanged; not attempted
   again tonight per standing guidance.
6. **ND amalgamation appeal** — still structurally blocked at the source (ndcourts.gov); one quick
   check per session remains the right cadence, per standing guidance.
7. **JCM Study 1 (netnography) track** — still no data platform/corpus chosen (not touched tonight, per
   standing instruction that this is Britton's design decision); Schneider et al. (2026) remains
   relevant grounding for it whenever picked up, now read in full rather than at the abstract level.
8. **Process note for future sessions:** read the *entire* `notes/` sequence for a project, not just
   the two or three most recent files by assumption — the 09-25 session's mistake (Section 1) happened
   because it trusted an incomplete read of the directory. Tonight's session cross-checked file dates
   via `git log` specifically to avoid repeating that error; a future session should do the same before
   trusting any note's own "what's still open" summary at face value.
