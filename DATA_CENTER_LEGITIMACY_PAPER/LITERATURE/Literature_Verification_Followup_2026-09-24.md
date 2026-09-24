# Literature Verification Follow-Up — "The Cloud Has a Zip Code"

**Date:** 2026-09-24
**AI involvement disclosure:** This document was produced by an AI agent (Claude) doing a
priority-ordered pass working the `Literature_Verification_Followup_2026-09-21.md` "next-pass
focus" list: (1) full-text/abstract-level verification of the three new 2025–2026 empirical items
flagged but not verified on 09-21 (Cartwright 2026, Ancona et al. 2026, Ngata et al. 2025), (2)
locating and reading the primary YPCCC source for the Yale data-center-opinion figure, (3) a fresh
novelty-defense scan for "benefit–burden asymmetry" (BBA) using new search angles, and (4) a
general 2025–2026 literature-currency sweep with emphasis on anything bearing on P1–P6 or the
"institutional distance from burden" construct-label question. No new theory, dimension, moderator
name, or proposition wording was decided — this is literature input only, per instructions.
Method: WebSearch, direct WebFetch of publisher/press pages, Crossref API (`api.crossref.org`),
OpenAlex API (`api.openalex.org`). ScienceDirect, Wiley Online Library, and (newly this session)
Taylor & Francis Online (`tandfonline.com`) all returned HTTP 403 to direct WebFetch, consistent
with every prior pass — Crossref/OpenAlex abstract-level metadata was used as the fallback
verification path in each case. No paywalled PDFs, Sci-Hub, or any pirated-content route was used,
and no full paywalled text was fetched or saved. Oliveira (2026) full text and the Been (1993)
footer-page question were **not** re-attempted, per standing instruction (both already resolved or
flagged as human-only next steps in prior passes).

**Source-tier key (unchanged from prior passes):** **Crossref/OpenAlex-verified** = confirmed
against that service's authoritative bibliographic/abstract metadata for the specific DOI.
**Search-summarized-only** = corroborated only by WebSearch result snippets/summaries, not a
primary metadata record. **General-web (non-academic)** = a blog, trade-press piece, law-review
blog post, or press page — not peer-reviewed or database-indexed — flagged explicitly whenever
cited below so it is never mistaken for a scholarly source.

---

## 1. Full-text/abstract-level follow-through on the three 09-21 items

### 1a. Cartwright, E.D. (2026), *Climate and Energy*, 42, 15–17, DOI `10.1002/gas.70012`

**Result: Crossref-verified abstract obtained. Confirms the 09-21 suspicion — this is a short
commentary/briefing piece, not an empirical study.** Crossref's own abstract field (present for
this DOI, unlike most Wiley records this project has checked) reads: *"From small towns facing
rising utility costs to global concerns about carbon emissions, the impact of the digital
revolution extends well beyond server rooms. As worries and pressures grow over the rapid
development of massive data centers, an issue rarely discussed is the impact on communities,
particularly from an environmental justice perspective. To date, the focus has primarily been on
the energy-intensive nature of these centers, whether the electric grid can accommodate the
increased demand..., and on the water usage..."* This is journalistic/trade-briefing framing
("worries and pressures grow," "an issue rarely discussed") over a 3-page article (pp. 15–17),
single-authored, in a Wiley trade-format title, not a methods-and-data empirical article.
**Recommendation carried forward from 09-21, now confirmed rather than suspected: do not treat
this as narrowing the "no dedicated peer-reviewed empirical data-center-EJ study" gap.** It is a
real, citable, DOI-bearing commentary that the phenomenon is being discussed in a Wiley venue — useful
as one more sign of topical relevance to CSREM's publisher family — but not a source that fills the
empirical gap.

### 1b. Ancona, Lauber Bonomo, Rozhkov & Porfiri (2026), *Nature Cities*, DOI `10.1038/s44284-026-00487-z`

**Result: Crossref-verified. This is a substantial, real, peer-reviewed empirical article** — *Nat
Cities* vol. 3, issue 8, pp. 756–767, published online 2026-07-31, 92 references, four named
authors (Camilla Ancona, Ofek Lauber Bonomo, Anton Rozhkov, Maurizio Porfiri; NYU/NYU Abu Dhabi).
WebSearch-summarized key findings (not yet read at full-text level, publisher page required
authentication): data centers are "an overwhelmingly urban phenomenon," with **97.5% of facilities
in metropolitan/micropolitan statistical areas** (directly contradicting a "rural cloud expansion"
narrative); siting is driven primarily by proximity to existing power-plant nameplate capacity, and
secondarily by broadband quality, retired coal-plant sites, IT employment, and natural-hazard
exposure. **Bearing on the model:** this is strong, quantitative, large-sample (4,283+ sites)
objective-BBA / geographic-dispersion support — siting tracks pre-existing energy infrastructure
rather than being randomly distributed, and the coal-plant-legacy finding specifically supports a
"burdens land where prior industrial burdens already were" framing. Still abstract/press-summary
level, not full-text; recommend as a strong citation candidate once full text is read.

### 1c. Ngata, Bashir, Westerlaken, Liote, Chandio & Olivetti (2025), ACM COMPASS '25, DOI `10.1145/3715335.3736324`

**Result: Full abstract obtained directly from the arXiv preprint (`arxiv.org/abs/2506.03367`),
which is open access — a step beyond the 09-21 pass's abstract-summary-only tier.** Full abstract:
*"Datacenters have become the backbone of modern digital infrastructure... this expansion has
brought growing tensions in the local communities where datacenters are already situated or being
proposed... the local socio-environmental consequences — such as health impacts, water usage,
noise pollution, infrastructural strain, and economic burden — remain largely underexplored...
Focusing on Northern Virginia's 'Data Center Valley,' we highlight how datacenter growth reshapes
local environments and everyday life, and examine the power dynamics that determine **who benefits
and who bears the costs**. Our goal is to bring visibility to these impacts and prompt more
equitable and informed decisions..."* (emphasis added). Six named authors confirmed (MIT-affiliated
based on Bashir/Olivetti).

**Correction to the 09-21 note:** the 09-21 followup called this region **"Data Center Alley"**
(the common trade-press term for Northern Virginia's data-center cluster). **The paper's own
abstract uses "Data Center Valley," not "Alley."** This session verified the exact wording directly
against the arXiv page rather than a search-engine summary (three independent occurrences of
"Data Center Valley," zero of "Alley," on the abstract page). This is a small but real factual
correction worth flagging exactly per the audit's own standards — if this citation is ever used in
the manuscript, use "Data Center Valley" as the paper's own term (optionally noting that
"Data Center Alley" is the more common informal/trade-press name for the same region, if useful
context).

**Bearing on the model:** the phrase "who benefits and who bears the costs" is about as close as
this session found to BBA's core intuition appearing in someone else's abstract this cycle — but it
is descriptive framing in a CS-conference (ACM SIGCAS/SIGCHI) mixed-methods paper, not a named,
operationalized, multidimensional construct competing with BBA. Positioning caveat from 09-21
stands: useful, on-point empirical grounding for visibility asymmetry and P2/P6, but not a
management/social-science-journal peer, so cite with care about venue type.

---

## 2. Yale/YPCCC data-center-opinion figure — primary source located (09-21's top open item, now resolved)

**Result: Primary source found and read directly.** The relevant YPCCC page is
`climatecommunication.yale.edu/publications/six-americas-and-data-centers/` ("What do Global
Warming's Six Americas think about data centers?"), distinct from the event-announcement page the
09-21 pass could only reach. This page was fetched directly and gives:

> "**73%** 'strongly' or 'somewhat' support a proposal requiring new data centers to offset their
> electricity use by installing rooftop solar on, and/or helping to weatherize and insulate nearby
> homes."

**Survey details, confirmed on the page:** Spring 2026 *Climate Change in the American Mind*
survey, **n = 1,060**, nationally representative U.S. adults, fielded April 17–26, 2026, jointly by
Yale Program on Climate Change Communication and the George Mason University Center for Climate
Change Communication. Support crosses party lines (liberal Democrats 88%, moderate/conservative
Democrats 77%, liberal/moderate Republicans 71%, conservative Republicans 63%, per the page). The
page also separately reports that 58% of registered voters oppose data centers being built in their
area, and 60% believe a nearby data center would raise their own electricity bills — additional
figures not previously catalogued, both useful motivating-color statistics for an Introduction.

**Important correction:** the widely-syndicated NPR-affiliate coverage (KJZZ/KNPR/KUNC/etc., and
this session's own re-check via UPR's Mountain West News Bureau article) reports **74%**, not the
primary source's **73%**. This session fetched the UPR article directly and confirmed it says
"74% of survey respondents said they would be more supportive of data centers if developers
somehow helped offset their home electricity costs" and separately quotes Kristin Eberhard
(identified in the article as an analyst, not a YPCCC researcher) characterizing opposition as
resistance to *"a bad bargain, where communities are asked to absorb the costs while somebody else
gets the benefit."* **This means the "bad bargain" framing is a quoted commentator's language from
the secondary press coverage, not YPCCC's own report language**, and the 73%/74% discrepancy
between the primary source and secondary press coverage should be resolved in favor of the primary
source (73%) if this figure is cited in the manuscript. **Status change from 09-21: this figure is
now citable** — cite the YPCCC page directly (73%, n=1,060, Spring 2026 CCAM survey) rather than the
secondary radio-coverage figure or its "bad bargain" quote, which are corroborating color at most.

---

## 3. Novelty-defense scan for BBA — continued, fresh search angles

**Result: unchanged — no scoop found.** This session ran additional exact-phrase and adjacent-
framing searches beyond the 09-21 pass's list: `"benefit-burden asymmetry" OR "benefit burden
asymmetry" construct 2026`, `"diffuse benefits" "concentrated costs" data center OR "AI
infrastructure" legitimacy construct 2026`, `"decision-maker proximity" justice construct
governance 2026`, `"spatial mismatch" OR "benefit dispersion" "burden concentration" infrastructure
justice construct 2026`, `"scale mismatch" OR "magnitude mismatch" benefit burden data center
construct 2026`, and `"AI infrastructure legitimacy" OR "infrastructure legitimacy" construct
academic 2026 management journal`. None returned a named, multidimensional academic construct that
collides with BBA. The bare phrase "benefit-burden asymmetry" still turns up only unrelated
domains (a Japanese child-support-levy policy piece, a nutrient-targeting agronomy term, general
prosocial-behavior/LLM-agent papers using "burden asymmetry" as a plain-English description, not a
named theory).

**What these searches did surface — real-world/trade-press color, not competing theory, but worth
recording because the language keeps converging on BBA's intuition independently:**
- A Data Center Knowledge trade article (Shane Snider, published 2026-06-15,
  `datacenterknowledge.com/build-design/ai-infrastructure-s-new-constraint-public-trust`) quotes
  Subodha Kumar (Temple University Fox School of Business) saying *"Communities frequently perceive
  an imbalance between local costs and local benefits,"* and quotes industry consultant Ihab Osman
  framing the core question host communities ask as *"What does this place get, and what does this
  place risk?"* and stating AI infrastructure has *"crossed from a real estate and power procurement
  problem into a public legitimacy problem."* General-web, non-academic, no named construct — but a
  third independent instance (after the WEF/Utility Dive/Teneo material already catalogued 09-21,
  and the Yale/YPCCC "bad bargain" quote above) of a subject-matter expert describing BBA's exact
  intuition in plain language without naming it as theory. This strengthens rather than weakens the
  novelty case: the phenomenon is clearly salient and being talked about by name-brand experts, and
  still nobody has formalized it as a construct.
- A Harvard Law Review Blog essay (Aug. 5, 2026), "Building at the Speed of AI: Data Centers,
  Expedited Permitting, and Who Bears the Burden" — general-web (law-review blog, not a
  peer-reviewed journal article), confirmed via direct WebFetch. It states plainly: *"The benefits
  of speed are framed in national terms... The burdens, by contrast, are often experienced
  locally,"* and names a **"governance gap"** — *"a mismatch between the national push to build AI
  infrastructure quickly and the weakening of the procedures through which affected communities can
  identify, contest, and mitigate its local burdens."* This is legal commentary drawing on existing
  NEPA/environmental-law doctrine, explicitly **not** proposing a named theoretical construct (this
  was checked directly, not inferred). "Governance gap" here is informal essay language, not an
  operationalized academic construct, so it is not a naming collision — but it is close enough in
  spirit to P2/P6 that it is worth knowing about as framing/motivating material, and its use of
  "governance gap" specifically should be kept distinct from BBA's own "institutional distance from
  burden"/candidate "decision-maker proximity" label so the manuscript doesn't accidentally start
  using two different terms for adjacent ideas.

**Bottom line for Britton: the novelty case is unchanged and still holds.** Three additional
sessions' worth of searching (09-18, 09-21, and now 09-24) have converged on the same result: no
academic paper anywhere has named a multidimensional benefit/burden diagnostic construct under this
or a close variant name, while practitioner and legal-commentary language keeps independently
gesturing at the same underlying intuition without formalizing it. That combination — a live,
widely-felt, frequently-described-in-passing phenomenon with no existing academic name — is
actually a fairly clean novelty argument to make explicitly in the manuscript's contribution
section, if Britton wants a line for it.

---

## 4. New literature relevant to specific propositions (P1–P6) and the institutional-distance/
   decision-maker-proximity question

### 4a. Kollar, J. (2026), "Planning Under Preemption: State Power and Local Authority in the AI
Data Center Era," *Journal of the American Planning Association*, DOI `10.1080/01944363.2026.2618221`
— **strong new candidate citation for P2/P6**

**Result: Crossref-verified bibliographic record; full abstract obtained via OpenAlex (the
publisher's own CC-BY-licensed indexed abstract, not a third-party summary).** Single-authored by
Justin Kollar, MIT Department of Urban Studies and Planning. Published online 2026-02-18, print
issue 2026-04-03 (vol./issue as indexed; JAPA issue 2), 32 references, CC-BY 4.0 licensed (though
direct WebFetch of the T&F-hosted full text still returned HTTP 403 this session, consistent with
this project's recurring publisher-blocking experience — the CC-BY license did not help against the
bot-challenge). OpenAlex abstract, in full:

> "A new wave of state legislation is fundamentally reshaping American planning by reducing local
> authority over land use, zoning, and environmental review, particularly for artificial
> intelligence (AI)–related energy and data center infrastructure. Drawing on recent cases across
> multiple states, I examine how planning power is being rescaled through statutory overrides,
> utility governance, fiscal incentives, and procedural constraints. These mechanisms shift
> decision-making authority upward to state agencies, utilities, and corporate actors, transforming
> planning from deliberative practice into administrative coordination. This reconfiguration raises
> critical questions about democratic participation, environmental protection, and planning's role
> within accelerated infrastructural capitalism."

**Why this matters for the model:** this is a real, current (Feb 2026), peer-reviewed, single-topic
academic treatment of exactly the phenomenon the "institutional distance from burden"/candidate
"decision-maker proximity" moderator (P6) is meant to capture — decision-making authority over
AI/data-center siting being moved away from the people who bear the local burden (local planning
boards) and toward more distant actors (state agencies, utilities, corporate actors), specifically
because of AI data center infrastructure. It is not a psychological/justice-perception study (it's a
planning-law/governance analysis), so it does not directly supply an empirical effect size for P6 —
but it is strong, timely, directly-on-topic ancestor/motivating literature for the moderator's
real-world referent, and a much closer topical match than the subsidiarity/fiscal-federalism/
Kostova literature the 09-10 audit already catalogued as the moderator's theoretical home. **This
should be added to the reading list for the P6/institutional-distance section regardless of which
label Britton ultimately picks** — it grounds the phenomenon in a live, data-center-specific,
2026 example rather than only general governance theory.

### 4b. Taufiq, Stelmach, Rahman, Siddiqi & Boudet (2026), "Community benefit agreement preferences
for energy development offshore California, Oregon, and Washington: Insights from a choice-based
conjoint experiment," *Energy Policy*, 215, 115275, DOI `10.1016/j.enpol.2026.115275` (SSRN preprint
also available: DOI `10.2139/ssrn.6018835`) — **candidate citation for P5 (benefit localization)**

**Result: Crossref-verified (both the journal-of-record DOI and an SSRN preprint DOI confirmed).**
Large-sample (n = 2,999) choice-based conjoint survey experiment across CA/OR/WA testing preferences
for community benefit agreement design (benefit size, who receives the benefit, who manages the
fund) tied to offshore-wind energy development. WebSearch-summarized findings: larger benefits,
nonprofit fund oversight, and housing/services-directed funds were preferred; preferences varied by
demographic and ideological subgroup. Not data-center-specific (offshore wind), and not yet read at
full-text level, but this is a genuinely on-point, large-n, 2026, quantitative empirical study of
exactly the mechanism P5 (benefit localization moderates the BBA→distributive-justice relationship)
proposes — it operationalizes "how benefits are localized/targeted" and measures preference effects
directly. An open-access SSRN version exists, which should make full-text verification easier than
the Wiley/Elsevier/T&F paywalled sources this project keeps running into — recommended as a
next-pass full-text priority specifically because of that accessibility.

### 4c. Journal of Energy & Natural Resources Law, DOI `10.1080/02646811.2026.2635979` (nuclear
siting/consenting reform, energy-justice framework) — **flagged, not yet a clean citation candidate**

WebSearch-summarized only (title/full author list not independently confirmed this session; one
author appears affiliated with Newcastle Law School per search-summarized text, published online
2026-03-11). Reported to apply an energy-justice framework to ask whether reduced/accelerated
nuclear-consenting reforms compromise procedural fairness and equitable distribution of benefits
and burdens. Topically adjacent to P1/P2 (procedural fairness reductions and their relationship to
distributive-burden concerns) but about nuclear consenting, not data centers, and this session could
not independently verify the title/full author list against Crossref/OpenAlex (searches returned
only the DOI and a general topic summary, not a clean bibliographic record) — **do not treat as
verified; needs a dedicated Crossref/OpenAlex lookup next pass before use.**

### 4d. Spatial distributive justice framework (2024) — noted but explicitly not a new finding

A ScienceDirect *Energy Research & Social Science* article, "Spatial distributive justice has many
faces: The case of siting renewable energy infrastructures" (`sciencedirect.com/science/article/
pii/S2214629624003608`), surfaced repeatedly across this session's P1/P5 searches. It predates the
audit window (published September 2024, so technically pre-existing rather than new 2025–2026
literature) and was not in the 09-10 audit's catalogued reading list. It offers a formal three-part
specification for distributive-justice claims (who are the recipients; which benefits/burdens; which
distributive principle) applied to renewable-siting Gini coefficients — a possible P1 supporting
citation for how to formally specify "distributive justice" in the model, though it is about
renewable energy siting generally, not data centers, and full text was not read this session.
Flagging its existence rather than recommending immediate use — Britton may already know this one.

---

## 5. Summary table — this session

| Item | Result | Confidence tier |
|---|---|---|
| Cartwright (2026), *Climate and Energy* | Crossref abstract obtained — confirms short commentary/briefing format, not empirical study; does not narrow the "no dedicated empirical data-center-EJ study" gap | Crossref-verified (abstract) |
| Ancona et al. (2026), *Nature Cities* | Crossref-verified as substantial peer-reviewed article (12 pp., 92 refs); strong siting-pattern support for geographic dispersion | Crossref-verified (bibliographic); findings still search-summarized only |
| Ngata et al. (2025), ACM COMPASS | Full abstract read directly from arXiv; **correction**: paper says "Data Center Valley," not "Data Center Alley" as the 09-21 note stated; abstract language ("who benefits and who bears the costs") closely echoes BBA's intuition but is not a named construct | Primary source (arXiv abstract page) read directly |
| Yale/YPCCC data-center-opinion figure | **Resolved.** Primary source found and read: 73% (not 74%) support offset requirement, n=1,060, Spring 2026 CCAM survey; "bad bargain" framing is a quoted commentator's language in secondary press coverage, not YPCCC's own | Primary source (YPCCC page) read directly |
| BBA novelty-defense scan (fresh angles) | No scoop found; novelty case unchanged and still holds; practitioner language keeps converging on BBA's intuition independently without naming a construct | WebSearch across 6 new query angles + 2 direct WebFetch verifications |
| Kollar (2026), JAPA | New, strong, directly-on-topic citation candidate for P2/P6 (state preemption shifts data-center siting authority away from local government) | OpenAlex-verified abstract (CC-BY, publisher-indexed) |
| Taufiq et al. (2026), *Energy Policy* | New, large-n (2,999) conjoint-experiment candidate citation for P5 (benefit localization); open-access SSRN version exists | Crossref-verified (bibliographic); findings search-summarized only |
| J. Energy & Nat. Resources Law nuclear-consenting article | Topically adjacent to P1/P2 but **not independently bibliographically verified this session** — needs a dedicated lookup | Search-summarized only — unverified |
| "Spatial distributive justice has many faces" (2024) | Pre-2025, not new, but not previously catalogued; possible P1 supporting citation for formal distributive-justice specification | Search-summarized only |

---

## What remains open / not attempted this pass

- **Full text of Kollar (2026) JAPA** — abstract-level only; T&F blocked WebFetch with HTTP 403
  despite the CC-BY license. If this becomes a load-bearing citation for P6, a human-fetched PDF
  is the likely next step (same publisher-blocking pattern as Wiley/ScienceDirect throughout this
  project).
- **Full text of Taufiq et al. (2026)** — the SSRN preprint (`doi.org/10.2139/ssrn.6018835`) should
  be tried first for full-text access, since it may not carry the same bot-blocking as the Elsevier
  journal-of-record page; not attempted this session (found late in the pass).
- **Journal of Energy & Natural Resources Law nuclear-consenting article** — title, full author
  list, and content need independent Crossref/OpenAlex verification before this is treated as a
  real, citable source; only a WebSearch topic summary was obtained this session.
- **Ancona et al. (2026) full text** — still abstract/press-summary level only; the Nature.com page
  required an authentication redirect this session that was not completed. Recommend a targeted
  fetch next pass, since this is a strong objective-BBA citation candidate.
- **Cartwright (2026) and Ngata et al. (2025) full text** — still not obtained (Wiley 403 for
  Cartwright; the arXiv HTML full paper was not read beyond the abstract page for Ngata et al.,
  though the arXiv version is fully open and should be easy to read completely next pass).
- **Oliveira (2026) full text** and **Been (1993) exact page number** — not re-attempted, per
  standing instruction from prior passes (both already resolved with high confidence or flagged as
  human-only next steps).
- As in every prior pass: nothing in this document should be read as settling any modeling,
  construct-naming, dimension-count, or proposition-wording question — those stay Britton's call.
  The Kollar (2026) and Taufiq et al. (2026) citations in particular are reported as strong
  candidates worth adding to the reading list, not as a decision about how P5/P6 should be worded
  or labeled.
- **A useful next-pass focus**, if Britton wants one: (1) full-text read of Kollar (2026) and the
  Taufiq et al. (2026) SSRN preprint, since both are new, on-topic, and currently only
  abstract-verified; (2) independent bibliographic verification of the Journal of Energy & Natural
  Resources Law nuclear-consenting piece; (3) a full read of the Ngata et al. (2025) arXiv HTML
  version, which is fully open-access and has not yet been read beyond its abstract across any
  session.
