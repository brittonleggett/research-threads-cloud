# Literature Verification Follow-Up — "The Cloud Has a Zip Code"

**Date:** 2026-09-16
**AI involvement disclosure:** This document was produced by an AI agent (Claude) doing a
targeted, priority-ordered citation-verification pass on the three open items flagged in
`Literature_Verification_Followup_2026-09-14.md`'s "What remains open" section. No new theory,
dimension, moderator name, or proposition wording was decided — verification only, per
instructions. Method: Crossref API (`api.crossref.org`), Semantic Scholar API, Unpaywall/OpenAlex
lookups, direct WebFetch/curl attempts at publisher and repository pages, and WebSearch for
abstracts and institutional-repository corroboration. Wiley (`onlinelibrary.wiley.com`) blocked
every direct fetch attempt tonight — WebFetch tool, and a direct `curl` with a browser user-agent
— with the same behavior seen in the 09-10 and 09-14 passes (see Section 1 for the specific
diagnostic). No paywalled PDFs or long paywalled excerpts were fetched or saved; the Cornell Law
Review PDF checked in Section 2 is a law school's own open institutional repository, not a
paywalled source, and was not saved to this repo (page-range check only, from search-tool
summaries of the page, not a saved file).

**Source-tier key used throughout:** **Crossref-verified** = confirmed against Crossref's
authoritative bibliographic (and, where present, abstract) metadata for that DOI.
**Institutional-repository-corroborated** = no Crossref DOI record found, but the citation is
independently corroborated by multiple authors'-own-institution repository pages (a strong but
not database-authoritative tier). **Search-summarized-only** = corroborated only by WebSearch
result snippets/summaries, not a primary metadata record.

---

## 1. Oliveira (2026), CSREM 33(4):4591-4606, DOI 10.1002/csr.70399 — priority item 1

**Goal:** fetch the CC-BY full text (confirmed genuinely open-access in the 09-14 pass) and
confirm/correct the audit's description of the article's content.

**What was tried, in order:**
1. WebFetch tool on `onlinelibrary.wiley.com/doi/full/10.1002/csr.70399` → **HTTP 403**.
2. WebFetch tool on the direct PDF link `onlinelibrary.wiley.com/doi/pdf/10.1002/csr.70399` →
   **HTTP 403**.
3. Direct `curl` (bypassing the WebFetch tool entirely) with a standard browser user-agent on
   `onlinelibrary.wiley.com/doi/pdfdirect/10.1002/csr.70399` → **HTTP 403**, and critically the
   response body was not a paywall notice but a **Cloudflare "Just a moment…" bot-challenge page**
   (confirmed by inspecting the raw response: `<title>Just a moment...</title>`, Cloudflare
   challenge script). This is a meaningful diagnostic upgrade over the earlier passes' plain "403"
   notes: **the block is anti-bot/anti-scraper protection, not a paywall or license gate** — a
   human clicking the link in an ordinary browser would very likely get through, since the license
   genuinely permits it. No automated fetch tool available in this session can pass a Cloudflare
   interactive challenge.
4. DOI resolver (`doi.org/10.1002/csr.70399`) → redirects to the same Wiley URL → same 403.
5. Unpaywall API — rejected the request (422, "please use your own email address"); not pursued
   further since it would only have pointed back to the same blocked Wiley URL anyway (confirmed
   via Semantic Scholar, next).
6. **Semantic Scholar API** (`api.semanticscholar.org`) — returned a full record confirming
   **`openAccessPdf.status: "HYBRID"`, `license: "CCBY"`**, independently corroborating the 09-14
   pass's Crossref-based CC-BY finding from a second database. Its PDF link also points to the
   same Wiley URL — no independent full-text mirror exists yet on Semantic Scholar, ResearchGate
   (checked via WebSearch — no ResearchGate full-text mirror found for this specific DOI), OpenAlex
   (queried directly, record not yet indexed — likely too new, published online 2026-01-08), or
   CORE.

**What was obtained instead — a genuine content upgrade:** The **Crossref API record itself now
returns the full published abstract** for this DOI (it did not on the 09-14 pass, or was not
checked at that field level). This is **Crossref-verified**, a stronger tier than the 09-14 pass's
"plausible plot summary" from WebSearch. Full abstract, reproduced for the record:

> "Mining is one of the foundations of economic development but has historically been associated
> with severe socioenvironmental impacts, such as ecosystem degradation, displacement of
> traditional communities, and large-scale disasters. In this context, corporate social
> responsibility (CSR) plays a central role as a mechanism for legitimizing mining companies,
> configured not merely as a voluntary strategy but as an ethical, social, and institutional
> requirement. This study aims to propose a theoretical model that integrates Institutional Theory
> and Agency Theory, elucidating the mechanisms that lead mining companies to adopt CSR practices
> as a strategic response to the demands of the external environment and the internal dynamics of
> governance. The research is based on a systematic literature review (SLR), following the PRISMA
> protocol, and included articles indexed in SciELO, Scopus, and Web of Science. Bibliometric and
> qualitative analyses were applied, supported by software such as VOSviewer, to map keyword
> co-occurrence and organize thematic clusters. The results revealed that while coercive,
> normative, and mimetic pressures induce greater socioenvironmental commitment, agency conflicts
> often limit the effectiveness of CSR, favoring symbolic practices or greenwashing. By integrating
> both theoretical approaches, the study concludes that the effectiveness of CSR in mining depends
> not only on responsiveness to external pressures but also on the integrity of internal
> governance."

**Bearing on the audit's description (fit-check, not a modeling decision):** The audit described
Oliveira as an "institutional + agency-theory account of CSR in an extractive, host-community-facing
industry," recommended for Theoretical Foundations as the closest in-journal industry analog
("large-footprint, locally concentrated burden, diffuse benefit"). The confirmed abstract supports
the institutional+agency-theory framing exactly. One nuance worth flagging for whoever drafts that
section: **the article itself is a systematic-literature-review/PRISMA bibliometric study
(VOSviewer-based), not a primary empirical or host-community study** — it proposes a theoretical
model about *why* mining firms adopt CSR (institutional pressure vs. internal agency conflicts →
greenwashing), and does not itself discuss benefit-burden distribution, host communities, or siting
directly. It is a strong theoretical-scaffolding citation for the institutional-legitimacy argument,
but the "locally concentrated burden, diffuse benefit" framing is the audit's own extrapolation to
the mining industry generally, not something this specific article states. Worth a precise
in-text framing (cite it for the institutional/agency mechanism, not for a burden-distribution
finding it doesn't contain).

**Status: full body text still not obtained (Cloudflare-blocked across every method tried this
session); abstract-level content is now Crossref-verified (upgraded from search-summarized-only).
Recommend Britton or a person with normal browser access simply open the link directly — the
license genuinely permits it and the block appears to be bot-detection, not access control.**

---

## 2. Been (1993), Cornell Law Review 78(6) — end page — priority item 2

**Goal:** resolve the ambiguous end page (1048 vs. 1085 per the 09-14 pass) with a direct check.

**What was tried:** Direct WebFetch/curl of the Cornell Law School repository's own PDF for the
Been article itself → **HTTP 403 / Cloudflare challenge**, same pattern as Section 1 (this
repository is evidently also behind Cloudflare now; it was reachable via WebFetch in the 09-14
pass, so this may be an intermittent protection change on Cornell's side rather than a persistent
block). Falling back to an indirect but reliable method:

**Method:** Law reviews paginate continuously within a bound volume — the article immediately
following Been's in the same issue necessarily starts on the page right after Been's ends. The
09-14 pass had already confirmed (via direct WebFetch of the issue's own scholarship-repository
page) that Been's article is **Article 1** of *Cornell Law Review* Vol. 78, Issue 6 (September
1993), starting at page 1001. This session identified the next piece in that issue — **Barbara
Holden-Smith, "Lords of Lash, Loom, and Law: Justice Story, Slavery, and Prigg v. Pennsylvania,"**
Article 2 of the same issue — and checked its own starting page directly.

**Result:** Both (a) a WebSearch summary and (b) a **direct WebFetch of the Cornell scholarship
repository's own citation page for the Holden-Smith article**
(`scholarship.law.cornell.edu/clr/vol78/iss6/2/`) independently returned the identical recommended
citation: **"Barbara Holden-Smith, *Lords of Lash Loom and Law: Justice Story Slavery and Prigg v.
Pennsylvania*, 78 Cornell L. Rev. 1086 (1993)."** Two independent retrieval paths, same institution's
own primary metadata, same number.

**Conclusion:** Since Holden-Smith's article starts at page **1086**, and Cornell Law Review pages
are numbered continuously within an issue with no gap pages between articles (confirmed pattern
across the other issue-6 citation pages checked), **Been's article ends at page 1085** — resolving
the 09-14 pass's ambiguity in favor of **1085, not 1048**. This is inferential (next-article-start
minus one) rather than a direct read of the last page of Been's own PDF, since that PDF was
Cloudflare-blocked again tonight, but it rests on two independently-retrieved, institution-authored
primary citation records, which is about as solid as a check can get without opening the PDF
itself.

**One additional finding, not requested but relevant:** WebSearch surfaced a **separate, related
Vicki Been article from 1994** — "Locally Undesirable Land Uses in Minority Neighborhoods:
Disproportionate Siting or Market Dynamics?" (*Yale Law Journal*, 1994) — a companion piece with a
very similar title and topic. This is almost certainly the source of the original audit's "1994"
year error: the two Been pieces (Cornell L. Rev. 1993 and Yale L.J. 1994) are easy to conflate by
year and topic. Worth noting in case the manuscript ever wants to cite the Yale piece too — it is a
real, distinct article, not a duplicate or an error to remove.

**Recommendation:** Finalize the citation as **Been, V. (1993), "What's Fairness Got to Do With
It? Environmental Justice and the Siting of Locally Undesirable Land Uses," Cornell Law Review,
78(6), 1001–1085.** No further check needed unless the manuscript wants a direct PDF-footer
confirmation, which remains blocked by Cloudflare protection on both Wiley and (tonight) Cornell's
repository.

---

## 3. Energy-justice "triumvirate" citations — priority item 3 (3 of the 6 listed items checked)

Picked the three most load-bearing and thematically linked items from the 09-14 pass's deferred
list — McCauley et al. (2013), Jenkins et al. (2016), and Sovacool & Dworkin (2015) — since the
audit cites all three together as "the full energy-justice tripartite framework" (Section 8) and
they anchor P1/P2's distributive/procedural-justice logic directly. Soja (2010), Acevedo/Fischhoff/
Patrício (2026), and Gross (2007) were not reached this session (see "What remains open").

### Jenkins, K., McCauley, D., Heffron, R., Stephan, H., & Rehner, R. (2016) — VERIFIED
**Crossref-verified**: "Energy justice: A conceptual review," *Energy Research & Social Science*,
11, 174–182 (published 2016-01). DOI: `10.1016/j.erss.2015.10.004`. Title, all five authors,
journal, volume, and pages match the audit's citation (#9) exactly.
**Abstract-level content** (search-summarized-only, corroborated identically across three
independent listings — Stirling, St Andrews, and an ADS abstract-service record): the paper gives
an account of energy justice's three core tenets — **distributional, recognition, and
procedural** — and promotes applying this three-pronged framework across the energy system. This
directly substantiates the audit's "full energy-justice tripartite framework" characterization and
is a strong, exact-fit citation for the P1/P2 distributive/procedural framing.
**Status change: LIKELY-REAL → VERIFIED.**

### Sovacool, B.K., & Dworkin, M.H. (2015) — VERIFIED
**Crossref-verified**: "Energy justice: Conceptual insights and practical applications," *Applied
Energy*, 142, 435–444 (2015-03). DOI: `10.1016/j.apenergy.2015.01.002`. Title, both authors,
journal, volume, and pages match the audit's citation (#10) exactly.
**Abstract-level content** (search-summarized-only, corroborated via SSRN, RePEc/EconPapers, and a
ScienceDirect abstract listing): the paper frames energy justice as an analytical tool that
**integrates distributive and procedural justice concerns** that are usually treated as distinct,
combining Kantian, libertarian, pluralist, recognition-justice, and utilitarian elements into a
decision-making framework. This is directly on-point for the manuscript's P1/P2 distinction and
its DJ/PJ-correlation question flagged in the 09-14 pass (Section 1) — worth citing alongside
Hauenstein, McGonigle & Flinder (2001) and Colquitt et al. (2001) wherever that correlation is
discussed.
**Status change: LIKELY-REAL → VERIFIED.**

### McCauley, D., Heffron, R., Stephan, H., & Jenkins, K. (2013) — VERIFIED (institutional-repository tier)
**No Crossref DOI record found** for this specific article — a Crossref title/bibliographic search
returned only later, related papers (e.g., Heffron's 2024 "Energy justice – the triumvirate of
tenets revisited and revised," *Journal of Energy & Natural Resources Law*, 42(2):227–233, DOI
`10.1080/02646811.2023.2256593` — a 2024 follow-up piece explicitly revisiting this same 2013
paper, which is itself indirect corroboration that the original exists). *International Energy Law
Review* does not appear to register DOIs with Crossref for articles of this era/type (a practice-
note-style current-awareness journal, not an academic journal with a full Crossref deposit — this
is a plausible, non-suspicious explanation, not a red flag).
**Institutional-repository-corroborated** instead, via a direct WebFetch of the University of
Stirling's own research-output repository page (one of the authors' home institution) plus
independently-matching listings from the University of Brighton, University of St Andrews, and
Erasmus University Rotterdam repositories, ResearchGate, Semantic Scholar, and PhilPapers — all
giving the identical citation: **McCauley, D.A., Heffron, R.J., Stephan, H., & Jenkins, K. (2013),
"Advancing Energy Justice: The Triumvirate of Tenets," *International Energy Law Review*, 32(3),
107–110.** This resolves the audit's citation, which had the volume/issue (32(3)) but no page
numbers.
**Abstract-level content** (search-summarized-only): the article analyzes energy justice's
distributional, procedural, and recognition aspects with reference to UK energy-policy examples —
consistent with, and evidently the founding piece behind, the same tripartite framework Jenkins et
al. (2016) elaborates.
**Status change: LIKELY-REAL → VERIFIED** (institutional-repository tier, not Crossref — flagging
this distinction explicitly per the source-tier convention, since it is a one-notch-lower
confidence tier than a DOI-backed Crossref match, even though five independent repositories agree).

---

## 4. Summary table — status changes (this session)

| Citation | Status before (09-14) | Status now (09-16) | Tier |
|---|---|---|---|
| Oliveira (2026), CSREM 33(4):4591-4606 | LIKELY-REAL, abstract-level content not independently corroborated | **Abstract now Crossref-verified** (full abstract text confirmed); full body text still unobtained — Wiley/Cloudflare blocks every fetch method tried | Crossref-verified (abstract only) |
| Been (1993), Cornell L. Rev. 78(6) | Verified but end page ambiguous (1048 vs. 1085) | **End page resolved: 1001–1085** (1048 rejected) | Institutional-repository-corroborated (two independent retrievals) |
| Jenkins, McCauley, Heffron, Stephan & Rehner (2016) | LIKELY-REAL, not re-checked | **VERIFIED** | Crossref-verified |
| Sovacool & Dworkin (2015) | LIKELY-REAL, not re-checked | **VERIFIED** | Crossref-verified |
| McCauley, Heffron, Stephan & Jenkins (2013) | LIKELY-REAL, not re-checked, no page numbers | **VERIFIED**, pages now known (107-110) | Institutional-repository-corroborated |

---

## What remains open / not attempted this pass

- **Oliveira (2026) full body text** — still not obtained. The block is specifically a Cloudflare
  bot-challenge (confirmed by inspecting the raw HTTP response tonight), not a plain paywall
  refusal — a human with an ordinary browser should be able to open
  `https://onlinelibrary.wiley.com/doi/full/10.1002/csr.70399` directly and read the CC-BY text
  with no institutional access needed. Recommend Britton try that link directly next time he's at
  a keyboard, rather than another automated attempt — the tooling available to this session cannot
  pass an interactive bot challenge.
- **Been (1993) end page (1085)** — resolved with high confidence via two independent
  cross-institution citation records for the following article, but not from a direct read of the
  last page of Been's own PDF (Cornell's repository was also Cloudflare-blocked tonight, unlike the
  09-14 pass). If a fully primary confirmation is ever wanted, a law-library database (HeinOnline,
  Westlaw) or a person opening the Cornell PDF directly in a browser would close the last gap.
- **Soja (2010), Acevedo/Fischhoff/Patrício (2026), Gross (2007)** — not reached this session
  (time budget went to the three energy-justice items above, which are more directly load-bearing
  for P1/P2). None flagged as suspect — simply not checked yet. Recommend these three for the next
  pass, in that order (Soja is a monograph and will need the same multi-source approach as Wilson
  1980 and Tyler 1990/2006 did on 09-14; Acevedo et al. and Gross both look like journal articles
  that should be checkable via Crossref the same way tonight's three were).
- No citation checked this session turned out to be fabricated, non-existent, or wrong on any
  point other than the Been end-page ambiguity already flagged (which is now resolved, not a new
  error).
- As in prior passes: none of tonight's abstract-level content findings should be read as settling
  any modeling, construct-naming, or proposition-wording question — those stay Britton's call. The
  Sovacool & Dworkin (2015) finding in particular bears on the same DJ/PJ-correlation question
  flagged in the 09-14 pass's Section 1 and is reported here as literature input only.
