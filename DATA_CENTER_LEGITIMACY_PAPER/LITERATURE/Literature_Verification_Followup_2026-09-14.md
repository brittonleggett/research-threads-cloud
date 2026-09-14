# Literature Verification Follow-Up — "The Cloud Has a Zip Code"

**Date:** 2026-09-14
**AI involvement disclosure:** This document was produced by an AI agent (Claude) doing a
targeted citation-verification pass on the open items flagged in
`Literature_Audit_2026-09-10.md` (Sections 3, 8, 10). No new theory, dimension, moderator
name, or proposition wording was decided — verification only, per instructions. Method:
Crossref API (`api.crossref.org`) for authoritative bibliographic metadata, WebSearch for
abstracts/leads, and direct WebFetch attempts at publisher pages. Wiley (onlinelibrary.wiley.com)
blocked all direct WebFetch attempts with HTTP 403, same as the 2026-09-10 pass — Crossref
metadata and independently-corroborated abstract snippets were used as the fallback
verification path where publisher pages were unreachable. No paywalled PDFs or long paywalled
excerpts were fetched or saved.

---

## 1. The distributive/procedural-justice correlation meta-analysis (Section 3/8 priority item) — FOUND

**Confirmed citation:**
Hauenstein, N.M.A., McGonigle, T., & Flinder, S.W. (2001). "A Meta-Analysis of the Relationship
Between Procedural Justice and Distributive Justice: Implications for Justice Research."
*Employee Responsibilities and Rights Journal*, 13(1), 39–56. DOI: 10.1023/A:1014482124497.
Verified via Crossref (authoritative record: title, all three authors, journal, volume/issue/pages
all match) and corroborated independently by a Springer abstract page and a Hauenstein CV/citation
listing found via WebSearch (full text itself is paywalled — not fetched or saved).

**Reported finding (from the abstract, not full text):** A meta-analysis estimating the
bivariate relationship between procedural and distributive justice found the relationship
**strong (ρ = .64) across all studies**, though **moderated by research context**, with
"substantial evidence of variability" even within context. The paper's stated purpose was
specifically to correct for the field's tendency to treat PJ and DJ as independent while
ignoring their bivariate relationship — i.e., this paper's entire reason for existing is the
exact question the audit flagged for P2.

**Bearing on the open P2 question (reporting only, not deciding):** This is a real, moderate-to-strong
positive correlation from a dedicated meta-analysis on exactly this pair of constructs — in the
same range as the organizational-justice literature the audit already cited (Colquitt et al. 2001,
also re-verified below, ρ commonly reported ~.6 in that tradition). It does not by itself say DJ/PJ
*must* be modeled as correlated co-outcomes rather than independent mediators — that is a modeling
decision, not a literature fact, and stays Britton's call — but it means the "DJ and PJ move together"
claim in the audit is not speculative: it has a specific, real, moderate-strength (not near-1.0)
meta-analytic number behind it now, plus an explicit "moderated by context" caveat that could matter
argumentatively either way.

**Recommendation:** Cite Hauenstein, McGonigle & Flinder (2001) by name alongside Colquitt et al.
(2001) wherever the manuscript engages the DJ/PJ correlation question — upgrade from "lead found,
author unconfirmed" to a real, citable reference.

---

## 2. Three CSREM articles — direct-fetch verification attempts

All three: WebFetch to the Wiley `onlinelibrary.wiley.com` page returned **HTTP 403** (same
publisher-blocking behavior noted in the 2026-09-10 audit). Fell back to Crossref (authoritative
metadata, not just a search snippet) plus WebSearch-surfaced abstract content.

**Cai (2024)** — DOI 10.1002/csr.2609 — **UPGRADED to VERIFIED**
Crossref confirms: Shaohan Cai, Zhining Wang, Zhilin Yang, "Does community attitude matter? The
effects of local community environmental orientation on firms' environmental practices,"
*Corporate Social Responsibility and Environmental Management*, 31(2), 929–947 (2024). WebSearch
surfaced actual abstract content (not just the title): institutional-theory framing, survey of 372
Chinese firms, community environmental orientation → local legislation + community stakeholder
pressure (as two institutional forces) → firm environmental actions (green investment, environmental
operations) → firm reputation; explicitly notes community orientation does *not* directly affect firm
action (institutional forces mediate). This substantively matches the audit's description and is
detailed enough to be a real content check, not just a title match — though the underlying Wiley PDF
itself was not read. Recommend treating as usable for the manuscript's benefit-localization/BBA→PJ
section per the audit's original placement note.

**Oliveira (2026)** — DOI 10.1002/csr.70399 — **remains LIKELY-REAL, upgraded confidence but not full VERIFIED**
Crossref confirms the record exists and is indexed (as of 2026-09-05): Felipe Moura Oliveira & Elaine
Aparecida da Silva, "Corporate Social Responsibility (CSR) in Mining: An Integrated Institutional and
Agency Theory Perspective," *CSREM*, 33(4), 4591–4606 (2026), open access (CC-BY license per Crossref
metadata). This confirms the article is real, has the stated authors/title/journal, and — notably —
is CC-BY open access, meaning a legitimate full-text copy should be fetchable without paywall issues
once the Wiley 403 is worked around (e.g., via library proxy or a direct CC-BY mirror), unlike the
other two. WebSearch also surfaced a plausible plot summary (institutional + agency theory account of
CSR as a legitimation mechanism in mining) consistent with the audit's description, but this was not
confirmed against the actual open-access full text this session — full abstract-level content was not
independently corroborated the way Cai's was. Recommend a follow-up pass specifically targeting the
CC-BY full text.

**Castilho Rossoni (2026)** — DOI 10.1002/csr.70341 — **UPGRADED to VERIFIED**
Crossref confirms: Renata Luiza de Castilho Rossoni & Manolita Correia Lima, "Critical Discourse
Analysis in Corporate Reports: Legitimation Strategies in the Context of Environmental
Controversies," *CSREM*, 33(3), 3563–3581 (2026). WebSearch (ResearchGate/Semantic Scholar listings)
corroborates the substantive claim: critical discourse analysis of environmental disclosure as a
legitimacy-crisis management tool in a mining company, examining how corporate narratives can
minimize responsibility while presenting a favorable image. This matches the audit's description
closely enough to confirm fit for the Discussion/corporate-response placement the audit proposed.

---

## 3. Two "verify exact title/volume" items

**Been (1994) — CORRECTION NEEDED, not just verification.**
The audit's citation (`Been, J.L. (1994), "What's Fairness Got to Do With It? Environmental
Justice and the Siting of Locally Undesirable Land Uses," Cornell Law Review 78(6)`) has **two
errors**, confirmed via direct WebFetch of the Cornell Law School scholarship repository page
plus corroborating WebSearch results:
- **Author is Vicki Been, not "J.L. Been."** No source found uses "J.L." as an initial for this
  author; every citation (Cornell's own repository, Google Scholar-indexed listings, SSRN
  cross-references) gives the author as Vicki Been.
- **Year is 1993, not 1994.** The Cornell Law Review repository page lists the piece as Volume 78,
  Issue 6 (1993).
- Volume/issue (78(6)) and the title itself are correct.
- Page range: the Cornell repository citation format gives a starting page of 1001; one
  WebSearch snippet reported the closing page as 1085, this session's direct WebFetch of the
  Cornell page reported 1048 (inferring from formatting rather than an explicit end-page field).
  **The exact end page could not be pinned down with full confidence this session — flag 1001 as
  the confirmed start page and treat the end page as still needing a direct check (e.g., a
  library database or the PDF's own footer) before it goes into a reference list.**

**Recommendation:** Correct the in-project citation to **Been, V. (1993), "What's Fairness Got to
Do With It? Environmental Justice and the Siting of Locally Undesirable Land Uses," Cornell Law
Review, 78(6), 1001–[end page tbd]** wherever it currently appears (Section 3/P1, Section 7,
Section 10/#29 of the audit). This is exactly the kind of small-but-real error the README's
citation-verification convention asks to be caught and reported plainly, not smoothed over.

**Esteves & Vanclay (2009) — CONFIRMED, no correction needed.**
Verified via Crossref: Ana Maria Esteves & Frank Vanclay, "Social Development Needs Analysis as a
tool for SIA to guide corporate-community investment: Applications in the minerals industry,"
*Environmental Impact Assessment Review*, 29(2), 137–145 (2009). DOI: 10.1016/j.eiar.2008.08.004.
The audit's title, volume/issue/pages, and year were already exactly correct — **upgrade from
LIKELY-REAL to VERIFIED**, no change needed to the citation text itself.

---

## 4. Additional Tier-1/Tier-2 verification pass (time-permitting item)

All six named items checked via Crossref (journal articles) or multi-source book/publisher
confirmation (monographs, which don't carry DOIs):

| Citation | Result | Detail |
|---|---|---|
| Wilson, J.Q. (1980), *The Politics of Regulation*, Basic Books | **UPGRADED to VERIFIED** | Confirmed via Cambridge/APSR book review, AbeBooks, Open Library, HathiTrust, Google Books — consistently New York: Basic Books, 1980, 468 pp., ISBN 0465059678. Note: several sources describe this as an *edited volume* (Wilson as editor of a multi-author collection) rather than a single-authored monograph — worth a quick check against however the manuscript currently cites it (single-author vs. edited-volume citation format differ). |
| Moffat, K., & Zhang, A. (2014), *Resources Policy* 39:61–70 | **UPGRADED to VERIFIED** | Confirmed via Crossref exactly: "The paths to social licence to operate: An integrative model explaining community acceptance of mining," DOI 10.1016/j.resourpol.2013.11.003. Title, volume, pages all match the audit exactly. |
| Walker, G., & Devine-Wright, P. (2008), *Energy Policy* 36(2):497–500 | **UPGRADED to VERIFIED** | Confirmed via Crossref exactly: "Community renewable energy: What should it mean?" DOI 10.1016/j.enpol.2007.10.019. Exact match. |
| Tyler, T.R. (1990/2006), *Why People Obey the Law*, Princeton University Press | **UPGRADED to VERIFIED** | Confirmed via Princeton University Press's own catalog page and multiple retailer/library listings: 2006 paperback edition (with new afterword) ISBN 9780691126739; original 1990 edition also confirmed extant (Yale UP originally, per some listings — the 2006 Princeton reissue is the one most citation lists use). Cite as Tyler (2006) if citing the Princeton edition specifically, or note both years if citing the theory's original statement. |
| Oates, W.E. (1972), *Fiscal Federalism*, Harcourt Brace Jovanovich | **UPGRADED to VERIFIED** | Confirmed via Cambridge/APSR book review, RePEc, Internet Archive, Amazon: New York: Harcourt, Brace, Jovanovich, 1972, 256 pp. Exact match. |
| Gehman, J., Lefsrud, L.M., & Fast, S. (2017), *Canadian Public Administration* 60(2):293–317 | **UPGRADED to VERIFIED** | Confirmed via Crossref exactly: "Social license to operate: Legitimacy by another name?" DOI 10.1111/capa.12218. Exact match. |

Also opportunistically re-verified while checking the P2 item, since it came up directly:

- **Colquitt, Conlon, Wesson, Porter & Ng (2001)**, *Journal of Applied Psychology* 86(3):425–445,
  "Justice at the millennium: A meta-analytic review of 25 years of organizational justice
  research." **Confirmed via Crossref, DOI 10.1037/0021-9010.86.3.425** — exact match to the
  audit's citation. Was already flagged LIKELY-REAL/canonical; now VERIFIED.

---

## 5. Summary table — status changes

| Citation | Audit status (09-10) | Status now (09-14) |
|---|---|---|
| Hauenstein, McGonigle & Flinder (2001) — DJ/PJ correlation meta-analysis | Lead found, author unconfirmed | **Found and verified** — ρ = .64, moderated by context |
| Cai (2024), CSREM 31(2):929-947 | UNVERIFIED beyond title/abstract | **VERIFIED** (Crossref + corroborated abstract detail) |
| Oliveira (2026), CSREM 33(4):4591-4606 | LIKELY-REAL | Still LIKELY-REAL — Crossref confirms it's real and CC-BY (fetchable in principle), but abstract-level content not independently corroborated this session |
| Castilho Rossoni (2026), CSREM 33(3):3563-3581 | LIKELY-REAL | **VERIFIED** (Crossref + corroborated substantive summary) |
| Been (1993, not 1994) — Cornell Law Review 78(6) | LIKELY-REAL, "verify exact title/volume" | **Verified but citation needs correcting** — wrong year (1994→1993) and wrong author initials ("J.L."→Vicki); end page still unconfirmed |
| Esteves & Vanclay (2009), EIAR 29(2):137-145 | LIKELY-REAL, "verify exact title/year" | **VERIFIED**, no changes needed |
| Wilson (1980) | LIKELY-REAL | **VERIFIED** (note possible single-author vs. edited-volume citation-format issue) |
| Moffat & Zhang (2014) | LIKELY-REAL | **VERIFIED** |
| Walker & Devine-Wright (2008) | LIKELY-REAL | **VERIFIED** |
| Tyler (1990/2006) | LIKELY-REAL | **VERIFIED** |
| Oates (1972) | LIKELY-REAL | **VERIFIED** |
| Gehman, Lefsrud & Fast (2017) | LIKELY-REAL | **VERIFIED** |
| Colquitt et al. (2001) | LIKELY-REAL, canonical | **VERIFIED** |

## What remains open / not attempted this pass

- Oliveira (2026) full-text still not directly read — recommend a follow-up specifically
  fetching the CC-BY version (it should not require a paywall workaround given the license).
- The Been (1994→1993) end-page number is still ambiguous (1048 vs. 1085 from two sources) —
  needs a direct library/database check before finalizing a reference-list entry.
- Not re-attempted this pass (out of scope for tonight, no negative finding to report): McCauley
  et al. (2013), Jenkins et al. (2016), Sovacool & Dworkin (2015), Soja (2010), Star (1999, already
  VERIFIED in the original audit), Acevedo/Fischhoff/Patrício (2026), Gross (2007), Cash et al./
  Cumming et al. (2006, already VERIFIED). None of these were flagged as suspect — just not
  re-checked given the time budget, prioritizing the task-brief's explicit list.
- No citation checked this session turned out to be fabricated or non-existent. The one real
  problem found is the Been citation's incorrect year and author name — a correction, not a
  removal.
- The DJ/PJ correlation finding (ρ = .64) is reported here as literature-verification input only;
  whether to soften P2 or model DJ/PJ as correlated co-outcomes remains explicitly Britton's
  decision, per the open question noted from 2026-09-12 in other projects' summaries.
