# 2026-08-14 — Primary-source verification, pass 3 of 8 (La-Z-Boy, Birkenstock, Insteel, Home Depot)

**Tooling caveat — read before using anything below:** `WebFetch` was blocked for every domain
tried this session (`EGRESS_BLOCKED` on whitecase.com, hklaw.com, z2data.com, industrialsage.com,
tariffstool.com, budgetmodel.wharton.upenn.edu, and even en.wikipedia.org — a network-wide
egress-proxy block, not a per-site issue). This is the same failure mode the 2026-08-13 afternoon
run hit and self-flagged as "DEGRADED." So unlike pass 1 and pass 2 (which fetched and quoted
primary source pages directly — Ingka/WSJ statement, Walmart's own IR-hosted transcript PDFs),
**this pass is `WebSearch`-only**: the quotes below come from Claude's web-search result
summaries, not from a fetched, directly-read source document. Treat this as upgraded-secondary,
not primary — one more verification step (a direct fetch once WebFetch is working again) is
still warranted before anything here goes in a manuscript.

## #9 La-Z-Boy — status changes materially: **the story is more complicated than the corpus entry assumed**

Original draft entry: "Price increases following the 25% furniture tariff... `causation-explicit`,
`industry-norm-appeal`."

What search turned up complicates that: La-Z-Boy's 2025 price increases were real (single-digit
%, described by its own executives as "the very low end of what we're hearing is out in the
market" — via IndexBox/Supply Chain Dive coverage), but the company **also said it did not
expect to raise prices again** if the planned Jan 1, 2026 furniture-tariff increase (25% → 30%)
went through, citing that it manufactures nearly all its products domestically. Then that Jan 1
increase itself was delayed a year by the White House (furniture/cabinets/vanities tariff hike
postponed, current 25% held in place), per Supply Chain Dive's "White House delays furniture
tariff increases for a year" piece.
- Sources (search-summarized, not fetched): [Supply Chain Dive — La-Z-Boy volumes steady](https://www.supplychaindive.com/news/la-z-boy-volumes-remain-steady-tariff-driven-price-hike/806496/), [Supply Chain Dive — furniture tariff delay](https://www.supplychaindive.com/news/trump-furniture-cabinets-tariffs-delay/808681/), [IndexBox](https://www.indexbox.io/blog/la-z-boy-maintains-steady-volume-following-2025-tariff-price-hikes/)
- **Revised coding suggestion:** `causation-explicit` still holds for the 2025 increases, but
  `industry-norm-appeal` from the original draft doesn't clearly hold up — what search surfaced
  reads more like a domestic-manufacturing-insulation narrative than an industry-norm framing.
  Add `no-further-increase-anticipated` as a candidate code, and flag for Phase 3 whether this
  is really a clean "tariff pass-through" exemplar at all, given the domestic-sourcing angle —
  this may fit better as a counter-example (limited tariff exposure) than as another
  pass-through case.

## #12 Birkenstock — upgraded, corpus entry's framing holds up and gets sharper

Original draft entry: "Mixed/nuanced... `causation-vague`, `mitigation-narrative`,
`selective/style-by-style framing`."

Search corroborates and sharpens this with a named executive and real numbers. CFO **Ivica
Krolo**, on FY2026 guidance: expects ~100bp decline in both gross margin and EBITDA from
incremental tariffs; the company reviews and adjusts prices **style by style each season**
rather than uniformly. Quote (via WWD/Supply Chain Dive coverage): "the price increase would
have to be 2.5x the tariffs" to fully protect margin, which "is not something we would do to
our customers, being a democratic brand." Illustrative math given: a $10 tariff on a $100 shoe
would need a ~$25 price increase to hold the existing 60% gross margin; taking less than that
lets margin slip toward 54.5%.
- Sources (search-summarized, not fetched): [Supply Chain Dive](https://www.supplychaindive.com/news/birkenstock-2026-margin-hit-tariffs-bite/809309/), [WWD — Krolo interview](https://wwd.com/footwear-news/shoe-industry-news/birkenstock-ivica-krolo-tariffs-prices-second-quarter-1237724929/), [Business of Fashion](https://www.businessoffashion.com/news/retail/birkenstock-price-increase-tariff/)
- **Revised coding:** keep `causation-explicit` (Krolo is explicit about tariffs driving the
  margin math), `mitigation-narrative`, `selective/style-by-style framing`. Add
  `partial-absorption-quantified` as a candidate code — the "2.5x" and "$25 vs $10" framing is
  a genuinely quantified partial-absorption argument, in the CEO/CFO's own numbers, which is
  richer than the original draft entry captured.

## #14 Insteel Industries — confirms the original quote, low-effort as pass 2's note predicted

Original draft entry already had the core quote from the initial expansion pass. Search
reconfirms via multiple transcript-aggregator sources (Motley Fool, Globe and Mail, Benzinga,
GuruFocus): CEO **Woltz**, Q3 2026 earnings call — "when a [freight] cost $1,500 to send to a
destination now $3,000 somebody's gotta pay the bill." Additional context found beyond the
original entry: management ties this specifically to **Section 232 steel tariffs** (not just
generic "tariffs") keeping domestic steel prices above world-market levels, and announced a
price increase effective **July 13, 2026** to recover the inflationary cost.
- Sources (search-summarized, not fetched): [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/07/23/insteel-industries-iiin-q3-2026-earnings-call-transcript/), [GuruFocus](https://www.gurufocus.com/news/8963423/insteel-industries-inc-iiin-q3-2026-earnings-call-highlights-navigating-challenges-with-strategic-pricing-and-financial-flexibility)
- **Revised coding:** keep `causation-explicit`, `vivid-quotable-framing`. Add
  `section-232-specific` as a metadata tag — worth noting in the write-up that Insteel's
  causation story is about a *specific named statute* (Section 232 steel tariffs), which is
  more legally precise than most of the corpus's generic "tariffs" framing, and ties directly
  into the SCOTUS/IEEPA legal-sequence note (below) about which tariff authority is actually
  in play for a given artifact.

## #15 Home Depot — the "reverse the drop-Home-Depot call" finding from 2026-08-13 is confirmed, with a fuller and more useful story than the one-liner that survived the lost container

Original draft entry called this the weakest lead, placeholder only. 2026-08-13's recovered
summary said the run found "solid corroboration of a real within-wave reversal" but the quotes
were lost. Search reconstructs a **three-beat sequence**, not just a single reversal:
1. **May 2025 (spring):** Home Depot said it would *not* raise prices due to tariffs — "we don't
   see broad-based price increases for our customers at all going forward" — citing that >50% of
   purchases are U.S.-sourced and no single non-U.S. country would exceed 10% of purchases within
   a year.
2. **August 2025:** CFO **Richard McPhail**, to the Wall Street Journal — reversal — customers
   would see "some modest price movement for some categories," though "not on a broad scale,"
   because tariffs on some goods were higher by August than they'd been in May.
3. **May 2026:** a further update — CFO cites additional cost pressure from fuel/commodity
   inputs plus new tariffs, framing it as "the environment is changing almost every day."
- Sources (search-summarized, not fetched): [The Hill/Nexstar](https://thehill.com/homenews/nexstar_media_wire/5459448-some-prices-to-rise-at-home-depot-despite-earlier-stance-cfo-says/), [Yahoo Finance](https://finance.yahoo.com/news/home-depot-said-wouldnt-raise-021516060.html), [CFO Dive](https://www.cfodive.com/news/home-depot-warns-tariff-impact-modest-price-hikes/758202/), [Digital Commerce 360 — May 2026](https://www.digitalcommerce360.com/2026/05/19/home-depot-cost-changes-tariffs-oil-prices/)
- **Revised coding suggestion:** this is no longer the weakest lead in the batch — it's arguably
  the richest *narrative-arc* artifact in the whole expansion set (explicit denial →
  explicit reversal → ongoing volatility framing, all with named-executive quotes across three
  dated moments). Candidate codes: `causation-explicit` (from August on), `reversal-narrative`
  (new code — track record of a stated position changing under continued cost pressure),
  `hedged-commitment` ("environment changing almost every day"). Recommend **against** dropping
  this one; recommend promoting it given the strength of the reversal arc.

## Status after pass 3: 7 of 8 done (Chipotle, Lovesac, IKEA, Walmart, La-Z-Boy, Birkenstock, Insteel, Home Depot — wait, that's actually all 8)

Correction while writing this up: the original 8-candidate list (`2026-08-04-study1-corpus-
expansion.md`) was IKEA, La-Z-Boy, Lovesac, Chipotle, Birkenstock, Walmart, Insteel, Home Depot —
exactly 8. Passes 1+2 covered Chipotle, Lovesac, IKEA, Walmart (4). This pass covers the
remaining 4 (La-Z-Boy, Birkenstock, Insteel, Home Depot). **That's all 8 candidates now with at
least a verification pass done** — pass 1/2 at primary-source-fetched confidence, this pass at
WebSearch-summarized confidence pending a re-fetch.

## What's still yours to do (same standing rule)
1. Once `WebFetch` (or direct browsing) is working again, re-verify this pass's four entries
   against the actual source pages/transcripts, matching pass 1/2's standard — search-result
   summaries are a real upgrade over the original one-line draft entries, but shouldn't be the
   final citation basis.
2. La-Z-Boy in particular needs a design call: does it belong in the corpus as a pass-through
   example, given the "won't raise prices again" / delayed-tariff complication found here?
3. Home Depot's promotion (from weakest-lead to richest-narrative-arc) is a recommendation, not
   a decision — Phase 3 is still yours.
4. Two new candidate codes proposed across this pass (`no-further-increase-anticipated`,
   `partial-absorption-quantified`, `reversal-narrative`) — same rule as the original expansion
   pass's `full-absorption-promise`: flag for Phase 3, don't treat as locked.
