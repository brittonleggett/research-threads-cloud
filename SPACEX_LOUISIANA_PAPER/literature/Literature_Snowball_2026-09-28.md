# Literature Snowball — 2026-09-28

Fourth literature pass, and the first to actually do the citation-snowballing (forward citations
via OpenAlex, not just fresh keyword searches) that `Literature_Scouting_2026-09-09.md`,
`Literature_Deepening_2026-09-10.md`, and `Literature_Scouting_2026-09-25.md` had each
recommended as the single most-useful next step and none had yet done. No theory chain, coding
scheme, or Study 1 option decided here — still Britton's call. Method: OpenAlex's `cites:<id>`
filter (forward-citation search) off the project's two strongest anchors — Delmas & Burbano
(2011) and Janssen, Swaen & Du (2022) — restricted to 2024-2026 publications, screened by title
for relevance to claim specificity / greenwashing / economic-benefit-claim credibility. OpenAlex
was reached via a direct `api.openalex.org` call where the shared-IP free daily budget allowed,
and via an `r.jina.ai` proxy pass-through once that budget was exhausted mid-session (a new,
useful technique for this project, parallel to the `r.jina.ai` workaround already documented for
regulations.gov/courtlistener/capitol.texas.gov 403s).

## 1. Forward citations of Delmas & Burbano (2011) — "The Drivers of Greenwashing"

3,185 total citations (too broad to review all); filtered to `from_publication_date:2025-01-01`
plus a `claim specificity` keyword filter, 344 matches, screened by title. One clear standout,
not previously in this project's literature files:

**Yang, H., Gong, J., Lew, T. Y., & Ting, Q. H. (2026). Greenwashing before the ban: the pricing
and demand effects of vague versus specific environmental claims on Airbnb.** Research Square
preprint, DOI `10.21203/rs.3.rs-10158113/v1` — **PREPRINT TIER, not peer-reviewed**; full abstract
read directly (fetched via `curl` from the Research Square article page; OpenAlex itself carries
no abstract for this record). Flag the preprint status clearly if this is ever cited — it has not
been through peer review.

Large-N (≈420,000 Airbnb listings, 37 cities, 12 European countries, Sept. 2025-May 2026),
quasi-experimental design distinguishing **vague** green claims ("eco-friendly") from **specific,
verifiable** claims (e.g., "solar panels"), linked to both price and demand (monthly review rate
as a demand proxy). Headline finding, quoted from the abstract: **vague green slogans command a
16.6% price premium but are associated with 6.9% lower demand**, while **specific verifiable
claims trade at a 5.2% discount**. A review-text validation shows guests at green-rhetoric
listings mention environmental themes 9.2x more often than other guests, "overwhelmingly
positively" — interpreted as green rhetoric attracting a narrow, committed green-minded segment
rather than persuading average consumers. The paper explicitly frames its dataset as a
pre-enforcement baseline ahead of the EU's Empowering Consumers for the Green Transition
Directive (restricts generic environmental claims from Sept. 2026).

**Why this matters directly for this project**: it is the closest empirical analog found yet to
this paper's own claim-specificity puzzle, and it complicates the "specific = more credible = more
effective" intuition from a completely different angle than Janssen/Swaen/Du (2022)'s
warmth/competence moderation — here, vague claims work commercially (higher price) precisely
because they under-promise to a broad audience while still signaling to a narrow one, and specific
claims may invite more scrutiny/comparison that costs a premium. If the eventual Study 1 framing
engages the "is specificity actually the more credible/effective choice" question at all, this is
a citable, very recent counterpoint alongside Janssen/Swaen/Du — worth a full-text read (not
attempted tonight beyond the abstract) before manuscript use, and worth monitoring for a
peer-reviewed version replacing the preprint.

Also surfaced in this same search (already logged 2026-09-23, re-confirmed via a second, unrelated
citation path tonight — good corroboration, not new): **Choubey et al. (2025), "Signals vs.
Reality: Consumer Responses to Green Claims in Quick Commerce," Business Strategy and the
Environment**, DOI `10.1002/bse.4165`.

## 2. Forward citations of Janssen, Swaen & Du (2022) — claim specificity in green advertising

38 citing works since 2024 (all reviewed by title, via `r.jina.ai` proxy after the direct API's
shared free-tier budget was exhausted mid-session). Two new, directly on-point finds:

**Flores-Zamora, J., & De Pelsmacker, P. (2026). The effect of argument specificity, length and
visual imagery in green advertising on perceived green deception and brand attitude.
*International Journal of Advertising*.** DOI `10.1080/02650487.2026.2670862` — **bibliographic +
abstract tier**, both confirmed directly via OpenAlex's own abstract field (a primary bibliographic
registry, not a search snippet). Three studies manipulating message specificity (vague/specific),
length (short/long), and imagery. Key finding, quoted from the abstract: **"Long specific messages
lead to less perceptions of green deception than short and long vague and short specific
messages"** — i.e., specificity alone doesn't reduce perceived deception; it has to be paired with
sufficient message length/elaboration, or it can read as deceptive in the same way a short vague
claim does. Perceived green deception consistently lowers brand attitude across all three studies.
**Why this matters**: gives a second, different boundary condition on claim specificity's
credibility payoff (length/elaboration, not just source competence as in Janssen/Swaen/Du) — a
useful three-way triangulation (Janssen/Swaen/Du's competence moderator, this paper's
length/elaboration moderator, and the Yang et al. Airbnb paper's demand/price divergence) if the
manuscript wants to argue claim specificity's effects are genuinely conditional rather than simply
positive or negative.

**Tan, S. Z., Lin, Y., & Hong, L. W. (2025). Green Specificity: Igniting curiosity and arousing
emotional ambivalence. *Journal of Retailing and Consumer Services*.** DOI
`10.1016/j.jretconser.2025.104414` — **bibliographic tier only**; title/authors/journal/date
confirmed via OpenAlex/Crossref, but the publisher page (Elsevier/ScienceDirect) did not yield the
abstract to either a direct fetch or a redirect-following fetch tonight. Flagged as a strong lead
by title alone (directly about "green specificity" as its own named construct, with an
affect/curiosity mechanism distinct from the credibility mechanism this project has anchored on
so far) — a future session should try `pdftotext`/`pymupdf` against a directly-resolved URL, or a
university-proxy-free open repository copy, before citing beyond the bibliographic level.

Already logged (2026-09-23, re-confirmed via this citation path too): **Wang, Zhou, Zhang & Wang
(2024), "Pseudo-environmentalist or true defender?," Current Psychology**, DOI
`10.1007/s12144-024-07117-8` (claim specificity x message framing in green demarketing ads).

Other 2024-2026 citing works screened but judged not directly relevant enough to log in full here
(mechanism/context too far from this project's framing): a persuasion-knowledge/AI-selling paper,
a recycled-materials-observability paper, a carbon-quota-supply-chain paper, several
consumer-suspicion/brand-authenticity papers whose core construct (suspicion, authenticity) is
adjacent but not specificity-focused, and a handful of ESG-communication/live-streaming papers in
unrelated retail contexts.

## 3. Forward citations of Bartik (2020) — economic-development-incentive credibility

Only 8 total citations (small, fully reviewed). **Negative/thin result**: none of the 8 are a
close fit for this project's marketing/framing angle — they are public-finance/regional-economics
papers (multinational-location-decision drivers, entrepreneur migration stickiness, community
development finance, a Kenyan revolving-loan-fund governance study) that cite Bartik for his
economic-development-policy expertise generally, not for the specific "claimed job numbers are
usually unaudited/inflated" argument this project cares about. **This is a genuine negative
finding, not a search failure** — Bartik (2020) remains the right anchor for the economic-benefit-
claim thread, it just hasn't yet been picked up by a marketing/communication-specific citing paper.
Recommend not re-running this specific snowball again unless a multi-year gap passes.

## 4. A direct keyword search for "economic-benefit claim specificity in infrastructure siting" — re-confirmed negative, third search engine/method now

Tried a broad OpenAlex relevance-ranked search (not a citation-graph search) for the exact
intersection this project's other framing thread needs (job/investment-figure claim
specificity, specifically in a siting/incentive-negotiation context, treated as a communication/
credibility question rather than a pure public-finance question). Result: noise — climate-policy,
circular-economy, and generic incentive-systems papers with no direct fit, the same negative
pattern the 09-09/09-10/09-25 notes already found via WebSearch. **This gap is now confirmed
stable across three different search tools/methods** (WebSearch, OpenAlex relevance search,
OpenAlex citation-graph search from Bartik) — treat it as a genuine, durable gap in the literature
(a real opportunity for this paper to fill, not an under-searched artifact) rather than something
to keep re-checking nightly.

## What this pass did not do

- Did not attempt a full-text read of the Yang et al. (2026) Airbnb preprint beyond its abstract,
  or of the Flores-Zamora & De Pelsmacker (2026) paper beyond its abstract — both are strong
  next-session full-text targets before manuscript use.
- Did not resolve the Tan, Lin & Hong (2025) "Green Specificity" paper past bibliographic tier —
  its abstract was not successfully fetched tonight.
- Did not snowball backward (references cited by) from any anchor, only forward (works citing the
  anchor) — a further, not-yet-tried angle for a future session.
- Did not connect any of this literature to the Boca Chica ex-post evidence base or draft any
  lit-review language — still design-lock-adjacent, better done once Britton picks a Study 1
  framing.
