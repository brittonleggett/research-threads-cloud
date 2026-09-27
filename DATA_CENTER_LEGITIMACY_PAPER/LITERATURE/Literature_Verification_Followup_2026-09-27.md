# Literature Verification Follow-Up — "The Cloud Has a Zip Code"

**Date:** 2026-09-27
**AI involvement disclosure:** This document was produced by an AI agent (Claude) working the six
open items carried forward from `Literature_Verification_Followup_2026-09-24.md`: (1) Kollar (2026,
JAPA) full-text retry via an alternate route, (2) Taufiq et al. (2026, Energy Policy) full-text via
the SSRN preprint route, (3) independent Crossref/OpenAlex verification of the Journal of Energy &
Natural Resources Law nuclear-consenting article, (4) a targeted full-text attempt on Ancona et al.
(2026, Nature Cities), (5) a full read of the Ngata et al. (2025) arXiv HTML version, and (6) one
more attempt on Cartwright (2026, Climate and Energy). No new theory, dimension, moderator name, or
proposition wording was decided — this is literature input only. Method: WebSearch, direct WebFetch,
Crossref API (`api.crossref.org`), OpenAlex API (`api.openalex.org`), Unpaywall API
(`api.unpaywall.org`), Semantic Scholar API, and direct `curl` (with a standard browser user-agent,
to rule out a WebFetch-specific block) against the Taylor & Francis PDF endpoint. No paywalled PDFs,
Sci-Hub, DeepDyve, or any pirated-content route was used. Where a full PDF was read (Taufiq et al.),
it came from a legitimate DOE-funded public repository (Tethys, run by Pacific Northwest National
Laboratory), not from bypassing a publisher paywall, and it was not downloaded into this repo — only
its content was extracted for this note, consistent with the "no paywalled PDFs committed" rule.

**Source-tier key (unchanged from prior passes):** **Crossref/OpenAlex-verified** = confirmed against
that service's authoritative bibliographic/abstract metadata for the specific DOI. **Full-text-read**
= the actual article/preprint text was fetched and read directly (not a summary of a summary).
**Search-summarized-only** = corroborated only by WebSearch result snippets, not a primary source.
**General-web (non-academic)** = a press release, blog, or trade piece — flagged explicitly.

---

## 1. Kollar (2026), JAPA — still blocked, one more documented attempt

**Result: unchanged. Full text still not accessible.** Tried three new routes this session:
(a) a Google-indexed search for a preprint/repository copy on `dusp.mit.edu`, `ssrn.com`, or a PDF —
none found; (b) Kollar's own MIT DUSP faculty page (`dusp.mit.edu/people/justin-kollar`) — read
directly; it does not list this paper or link any preprint/PDF at all (it lists only 2016–2022 edited
volumes); (c) a direct `curl` against the Taylor & Francis PDF endpoint
(`tandfonline.com/doi/pdf/10.1080/01944363.2026.2618221`) using a standard desktop-browser user agent,
to rule out a WebFetch-tool-specific block. This returned an HTTP 403 with response headers showing
`cf-mitigated: challenge` — i.e., Cloudflare's bot-challenge page, not a simple referer/UA check. This
confirms the blocking is a JS/browser challenge that no non-browser tool can pass, not a fixable
request-header issue. Unpaywall was also checked directly: it lists the article as `oa_status: hybrid`
with a CC-BY license, but its "best OA location" is the same paywalled-behind-challenge T&F URL, and
`has_repository_copy: false` — so there is no independent green-OA copy anywhere Unpaywall indexes.
**Bibliographic verification is unchanged and solid** (Crossref + OpenAlex + Unpaywall all agree:
Justin Kollar, MIT Department of Urban Studies and Planning, published online 2026-02-18, CC-BY 4.0).
**Recommendation: stop attempting via automated tools — this needs a human with institutional access
or a real browser session to clear the Cloudflare challenge, not another scripted fetch.**

## 2. Taufiq et al. (2026), *Energy Policy* — full text obtained (this session's biggest find)

**Result: full text read directly, via a legitimate open repository, not the SSRN preprint.** The
`doi.org/10.2139/ssrn.6018835` redirect landed on `ssrn.com/abstract=6018835`, which returned HTTP 403
to WebFetch (SSRN's abstract pages are themselves bot-gated). However, a WebSearch for the paper
surfaced a listing on **Tethys** (`tethys.pnnl.gov`), the U.S. Department of Energy/Pacific Northwest
National Laboratory's public knowledge base for wind and marine renewable-energy environmental
research. That listing hosts a full PDF (`tethys.pnnl.gov/sites/default/files/publications/
Taufiq-et-al-2026.pdf`, deposited by PNNL as public research infrastructure, not a paywall-bypass
route). The PDF was fetched and its text extracted directly (via `pypdf`, not just a summarizer), and
the footer confirms it is paginated exactly as the published version: **"H.A. Taufiq et al., Energy
Policy 215 (2026) 115275."** This is the actual published article text, not a preprint draft.

**Confirmed details, read directly from the paper:**
- Full author list and affiliations: **Hossain Ahmed Taufiq** (Oregon State University School of
  Public Policy; also Thunderbird School of Global Management, Arizona State University), **Gregory
  Joseph Stelmach** (OSU), **Umama Rahman** (OSU), **Muhammad Usman Amin Siddiqi** (Dept. of
  Psychology, University of Bath, UK), **Hilary Boudet** (OSU).
- Method: choice-based conjoint survey experiment, **n = 2,999** West Coast (CA/OR/WA) respondents,
  three CBA (Community Benefit Agreement) attributes tested — benefit size, primary recipient, and
  fund manager — analyzed via average marginal component effects (AMCE) and marginal means (MM).
- Key results with actual effect sizes (not just direction): larger benefits generally preferred, but
  younger, lower-income, and conservative respondents often prioritized specific recipient sectors
  (especially housing) over sheer benefit size; nonprofits (established or newly created) preferred
  over local government for fund management; conservatives significantly less favorable toward
  environmental-restoration use of funds (AMCE = −0.118, p < .001) than moderates/liberals; housing
  most strongly favored by lower-income respondents; geographic differences by state (CA/OR strongest
  housing preference) and coastal-vs-non-coastal residence (coastal respondents preferred larger
  benefit packages).
- The paper explicitly frames itself around **distributive and procedural fairness/justice** in CBA
  design and cites social-license-to-operate literature (Prno & Slocombe 2012; Boutilier 2017) when
  discussing why nonprofit intermediaries are trusted over local government.
- Discussion/policy recommendations call for a national CBA framework (e.g., via the Bureau of Ocean
  Energy Management) and note CBA preferences are highly heterogeneous by demographic/ideological/
  geographic group — i.e., a one-size-fits-all "benefit localization" approach would misfire.

**Bearing on the model:** this is now a fully-verified, full-text-read, large-n, quantitative empirical
study directly on point for P5 (benefit localization moderates BBA → distributive justice). It is
about offshore wind, not data centers, but operationalizes exactly the "how are benefits targeted/
localized, and to whom" question P5 raises, with real coefficients rather than just topical relevance.
Recommended as the strongest fully-verified P5 candidate in the reading list to date.

## 3. Journal of Energy & Natural Resources Law nuclear-consenting article — now independently verified

**Result: fully verified via both Crossref and OpenAlex — this is a real article, and its actual
title/author differ from what the 09-24 note's search-summary implied.** Direct Crossref API lookup
on the DOI (`10.1080/02646811.2026.2635979`) and a separate OpenAlex lookup both return matching
records:

> **Title:** "The energy justice implications of reduced consent in planning reforms: assessing UK
> nuclear planning reforms for small modular reactors"
> **Author:** Darren McCauley (single author), Newcastle Law School, Newcastle University, UK (ORCID
> confirmed: 0000-0002-3951-1129)
> **Published:** 2026-03-11, pp. 1–22, *Journal of Energy & Natural Resources Law*, CC-BY 4.0 licensed,
> funded in part by the NWO Dutch Funding Council. OpenAlex lists it in the top 3% by citation impact
> for its cohort (`fwci: 18.217`) despite being only months old — flagging that as a metric worth
> knowing, not a claim about content quality.

**Correction to the 09-24 note:** the prior pass's search-summary described this as being about
"nuclear siting/consenting reform" generally with an author "affiliated with Newcastle Law School" —
that affiliation detail is now confirmed exactly right, but the actual scope is narrower and more
specific than the summary suggested: it is specifically about **UK small modular reactor (SMR)
planning reforms**, not nuclear consenting in general or any US context. Full text was attempted via
the Taylor & Francis PDF endpoint and returned the same Cloudflare bot-challenge 403 as Kollar (2026)
— consistent pattern, same publisher family. Unpaywall confirms `oa_status: hybrid`, CC-BY, but no
independent repository copy (`has_repository_copy: false`).

**Bearing on the model:** now a legitimately citable source, but narrower than the 09-24 flag implied —
it is single-country (UK), single-technology (SMR nuclear) energy-justice legal/policy analysis, not a
general treatment. Topically adjacent to P1/P2 (procedural-fairness reductions and distributive-burden
concerns under expedited/reduced-consent planning regimes) in the same way Kollar (2026) is, but
should be cited with the corrected, narrower scope description if used.

## 4. Ancona et al. (2026), *Nature Cities* — full text still paywalled, but much richer detail obtained via press materials

**Result: the Nature.com article page itself redirected to an authentication wall (`idp.nature.com`)
— still not directly readable, and Unpaywall confirms `oa_status: closed`, no OA location anywhere.**
However, this session located and read two institutional press releases that go well beyond the
abstract-level detail catalogued on 09-24: NYU Tandon School of Engineering's own news page
(`engineering.nyu.edu/news/inside-urban-machine-where-americas-data-centers-actually-live`) and the
EurekAlert! syndication of the same release. These are the researchers' home institution's own
official press communications (not third-party trade press), so this is a step up in reliability from
generic WebSearch summaries, though still not the peer-reviewed text itself — cite as press material
if used, not as if it were the paper.

**New detail confirmed across both press sources (consistent with each other):**
- Dataset: 4,283 commercial data centers, contiguous U.S., 2025 snapshot from the Data Center Map
  commercial database (operational + planned + under-construction + land-banked).
- 97.5% sited inside metropolitan/micropolitan statistical areas; the remaining 2.5% averaged only 8.5
  miles from the nearest urban edge — i.e., even the "rural" ones are barely rural.
- Five metro areas (Washington-Arlington-Alexandria, Chicago, Dallas-Fort Worth, New York-Newark-
  Jersey City, Phoenix) hold nearly a third of all U.S. facilities; Washington-Arlington-Alexandria
  alone hosts 610 facilities (14.2% of the national total).
- Data centers under development are roughly twice as likely to be sited in federally-designated
  "Energy Community" areas (i.e., places with legacy fossil-fuel infrastructure/employment) versus
  non-designated areas — this is the specific "burdens land where prior industrial burdens already
  were" mechanism flagged as strong objective-BBA support on 09-24, now with an actual likelihood
  comparison rather than just "coal-plant-legacy" description.
- Carbon-footprint variance is stark by region: Montana/North Dakota facilities emit 350,000+ tons
  CO2/year versus under 3,000 tons/year for Vermont/New Hampshire/Arkansas facilities — a striking
  illustration of geographic dispersion/scale-mismatch in practice, tied to each state's electricity
  generation mix.
- Direct author quotes: Maurizio Porfiri (lead) — "There is a prevailing narrative of these data
  centers being somewhere in the middle of nowhere" (challenging the rural-siting myth); Anton
  Rozhkov — "Where the infrastructure already exists, the data centers follow"; Ofek Lauber Bonomo —
  on the difficulty of the topic given "limited publicly available data on its footprint."

**Bearing on the model:** this substantially strengthens Ancona et al. as an objective-BBA / geographic-
dispersion citation — the Energy-Community-siting finding in particular is a quantified, on-point
illustration of burdens concentrating where prior industrial burdens already existed, which is more
specific and more usable than the 09-24 note's general "coal-plant-legacy" framing. Still recommend
flagging in the manuscript that the specific figures above are sourced to the authors' own institutional
press release, not a full read of the peer-reviewed text itself, since that full text remains
inaccessible.

## 5. Ngata et al. (2025), arXiv/ACM COMPASS — full text read directly, all figures verified against raw source

**Result: the full arXiv HTML paper (`arxiv.org/html/2506.03367v1`) was fetched and read directly, and
every specific figure was independently checked against the raw page text (not just a summarizer's
output) using a script that searched the extracted plain text for each claimed statistic.** This is a
step up in rigor from the 09-24 pass, which only read the abstract page. All of the following were
confirmed to actually appear in the paper's own text (not fabricated by any summarization step):

- **Title:** "The Cloud Next Door: Investigating the Environmental and Socioeconomic Strain of
  Datacenters on Local Communities." License: CC BY-NC-SA 4.0. arXiv:2506.03367v1 [cs.DC], submitted
  3 June 2025. Confirmed as an ACM COMPASS 2025 Late Breaking Work (not a full paper) — this "Late
  Breaking Work" status is itself worth noting if cited, since it signals early-stage/preliminary
  research rather than a complete study.
- **Full author list (six):** Wacuka Ngata, Noman Bashir, Michelle Westerlaken, Laurent Liote (all
  MIT), Yasra Chandio (University of Massachusetts Amherst), Elsa Olivetti (MIT).
- **Methodology:** IRB-exempt (MIT Protocol Exempt ID E-6721); mixed methods combining semi-structured
  interviews, document analysis (local newsletters, public reports), community-event participation,
  and social-media engagement with stakeholders, alongside quantitative field measurements (noise via
  NIOSH Sound Level Meter app, power-quality/harmonic-distortion data, utility outage data from PJM
  Interconnection Data Miner and NOVEC, and EPA Air Quality System pollutant data). Explicitly framed
  as early-stage/ongoing research with plans to expand.
- **Specific findings, confirmed verbatim in context:** datacenters account for less than 0.5% of the
  Northern Virginia workforce (cited to U.S. Census Bureau/BLS 2024); in Loudoun County, VA, more than
  6.8% of homes recorded at least one monthly reading exceeding an 8% total-harmonic-distortion (THD)
  threshold that can damage appliances, and in Prince William County over two dozen of 1,100 deployed
  sensors recorded up to 13% THD (both cited to a Bloomberg/Nicoletti et al. 2024 dataset analysis);
  noise measured at 22.3 dB at 2 miles from a datacenter site versus 28.0 dB at 200 feet; projected
  $37/month increase in residential electricity bills in Northern Virginia by 2040, cited to JLARC
  (Virginia's Joint Legislative Audit and Review Commission), 2024; three "dominant attitudes toward
  datacenters" identified across ten stakeholder types — **concerned, incentivized, and indifferent**
  (exact wording); residents describing "a sense of hopelessness in their efforts to retain the quality
  of life they sought when moving into the area."

**Correction confirmed from 09-24 stands:** the paper's own term is "Data Center Valley," not "Data
Center Alley" — reconfirmed again this session directly against the full paper text, not just the
abstract page.

**Bearing on the model:** this is now the most thoroughly-verified single citation in the whole
project's literature file — full text read, every quoted statistic checked against source text
directly rather than trusted from a summary. It remains what it was on 09-24: strong, real, on-point
empirical grounding for visibility asymmetry, temporal mismatch (the 2040 electricity-cost projection),
and P2/P6 (the "who benefits and who bears the costs" power-dynamics framing), from a CS-conference
Late Breaking Work rather than a management/social-science journal — cite accordingly.

## 6. Cartwright (2026), *Climate and Energy* — one more attempt, unchanged result, but exact title now confirmed

**Result: still closed-access, no new full text — as expected, and per instructions, not over-invested
in further.** OpenAlex confirms `oa_status: closed`, no repository copy. One new detail this session:
the article's **exact title** is now confirmed as **"The Environmental Justice and Community Impacts of
Data Centers"** (OpenAlex bibliographic record, single author Echo D. Cartwright, no institutional
affiliation listed in the record) — the 09-24 note described this only by its abstract content, not by
title. A WebSearch also surfaced that the piece is listed on DeepDyve (a pay-per-article rental
service); this was **not used** to obtain the text, consistent with the no-paywall-bypass rule — noting
its existence only so it isn't mistaken later for a legitimate open-access route. No change to the
09-24 conclusion: this is a short, real, DOI-bearing commentary/briefing piece (Wiley, vol. 42, pp.
15–17), not an empirical study, and does not narrow the "no dedicated peer-reviewed empirical
data-center-EJ study" gap.

---

## Summary table — this session

| Item | Result | Confidence tier |
|---|---|---|
| Kollar (2026), JAPA | Unchanged — confirmed the block is a Cloudflare bot-challenge (via direct curl with browser UA), not a fixable header issue; no repository/preprint copy found anywhere (MIT DUSP page, SSRN, Unpaywall all checked) | Bibliographic: OpenAlex/Crossref/Unpaywall-verified. Full text: still inaccessible |
| Taufiq et al. (2026), *Energy Policy* | **Full text read directly** via a legitimate DOE/PNNL public repository (Tethys), confirmed as the actual published version (page-numbered to match the journal record); full author list, methodology, and effect-size-level results extracted | Full-text-read |
| J. Energy & Nat. Resources Law article | **Now independently verified** via Crossref + OpenAlex: real title is "The energy justice implications of reduced consent in planning reforms: assessing UK nuclear planning reforms for small modular reactors," Darren McCauley, Newcastle Law School — narrower in scope (UK SMR-specific) than the 09-24 summary implied | Crossref/OpenAlex-verified (bibliographic); full text still blocked (same Cloudflare pattern as Kollar) |
| Ancona et al. (2026), *Nature Cities* | Full peer-reviewed text still inaccessible (closed access confirmed via Unpaywall), but substantially richer detail obtained from the authors' own institutional press release (NYU Tandon) and its EurekAlert syndication — exact figures and direct author quotes now in hand | Press-release-verified (institutional, not third-party); peer-reviewed text itself still unread |
| Ngata et al. (2025), arXiv/ACM COMPASS | **Full text read and every cited statistic independently checked against the raw source text** — all confirmed accurate, nothing fabricated by prior summarization steps | Full-text-read, statistic-by-statistic verified |
| Cartwright (2026), *Climate and Energy* | Unchanged — still closed access; exact article title now confirmed ("The Environmental Justice and Community Impacts of Data Centers"); not pursued further per standing guidance | Crossref/OpenAlex-verified (bibliographic only) |

---

## What remains open / not attempted this pass

- **Kollar (2026) and the McCauley (2026) J. Energy & Nat. Resources Law full texts** — both are
  blocked by the identical Taylor & Francis Cloudflare bot-challenge, confirmed this session to be a
  JS challenge rather than a scriptable header problem. **This needs a human with either institutional
  access or a real browser session** (or Britton's own library proxy) — further automated attempts are
  unlikely to succeed and are not recommended as a next-pass priority.
- **Ancona et al. (2026) full peer-reviewed text** — still not obtained; the Nature.com authentication
  wall was not bypassed. The press-release-level detail obtained this session is a reasonable
  substitute for citing the paper's headline findings, but anyone wanting exact statistical
  methodology (e.g., regression specification, confidence intervals) will still need the actual paper.
- **Cartwright (2026)** — per standing instruction, not pursued beyond this one attempt; treat as a
  closed, low-priority item unless Britton has personal Wiley access.
- As in every prior pass: nothing in this document should be read as settling any modeling,
  construct-naming, dimension-count, or proposition-wording question — those stay Britton's call. The
  Taufiq et al. (2026) full-text confirmation in particular is reported as a strengthened citation
  candidate for P5, not a decision about how P5 should be worded.
- **Nothing new turned up this session on the BBA novelty-defense question** — that scan was not
  re-run this pass (09-24's fresh-angle scan is the most recent one and its "no scoop found" conclusion
  was not re-tested here; a repeat scan wasn't part of this pass's assigned priority list).
- **A useful next-pass focus**, if Britton wants one: since four of the six open items from 09-24 are
  now either fully resolved (Ngata, J. Energy & Nat. Resources Law verification) or as resolved as
  automated tools can make them (Kollar, Cartwright — both need human/browser access to go further),
  the highest-value remaining literature-grounding work is probably either (a) a fresh currency sweep
  for new 2026 data-center-siting or CBA/benefit-sharing empirical work, since Taufiq et al. and Ancona
  et al. both turned out to be stronger than expected once actually read, or (b) revisiting the BBA
  novelty-defense scan with a new round of search angles, since it has now gone three sessions without
  a fresh attempt producing anything new to check against.
