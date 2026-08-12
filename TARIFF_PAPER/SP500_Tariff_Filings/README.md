# S&P 500 Tariff-Mention SEC Filings — Corpus & Methodology

Built 2026-07-24. Reframed (per Britton's decision) as a **separate large-N text-mining
companion contribution**, not part of Study 1's small typology-building thematic analysis —
see the marketing text-mining precedent lineage (Tirunillai & Tellis; Netzer et al.; Berger et
al. 2020 "Uniting the Tribes") in `Claude Knowledge\Thematic Analysis\AI_Assisted_TA_Shared_Method.md`.

## What this is

Every 10-K, 10-Q, and 8-K filed by an S&P 500 constituent between 2025-01-01 and 2026-07-24
that contains the word "tariff," pulled via SEC EDGAR's free full-text search API, then
automatically classified to separate genuine trade-tariff discussion from a false-positive
sense of the word (utility/regulatory rate "tariffs" — FERC filings, electricity rate
schedules — which is a completely different meaning that a naive keyword search can't tell
apart from trade tariffs).

## Method

**1. S&P 500 constituent list** (`sp500_constituents.csv`) — pulled from the
`datasets/s-and-p-500-companies` GitHub CSV, snapshot 2026-07-24. Membership drifts over time;
this is a point-in-time list, not necessarily identical to the index at any other date.

**2. CIK mapping** — joined against SEC's free `company_tickers.json` (ticker → CIK). 503 of
503 constituents matched.

**3. Full-text search** — SEC EDGAR full-text search API (`efts.sec.gov/LATEST/search-index`),
query `"tariff"` (quoted phrase match), `forms=10-K,10-Q,8-K`, date range 2025-01-01 to
2026-07-24, filtered per-company via the `ciks` parameter. Every request sent a descriptive
`User-Agent` header per SEC's fair-access policy, paced at ~6-7 req/sec (under SEC's 10/sec
guidance). Script: `fetch_tariff_filings.py` (has resume support — safe to re-run, skips
already-fetched companies).

Raw pull: 2,018 filings across 336 of 503 companies (66.8%) had ≥1 raw "tariff" hit.

**4. Validation spot-check** (`validation_sample.md`) — before trusting the raw pull, pulled
actual document text for a random 25-filing sample and read the context around each "tariff"
match by hand. Found real contamination: several hits were utility/regulatory rate tariffs
(Constellation Energy citing FERC tariff filings, CMS Energy's "large load tariff," Public
Service Enterprise Group's commodity-supply tariffs), not trade tariffs — concentrated in the
Utilities sector, as expected (same ambiguity flagged earlier in the academic-literature radar
scan for this project). This is the reason step 5 exists — a raw "tariff" keyword count is
**not** publication-safe on its own.

**5. Trade vs. utility-rate disambiguation** (`classify_trade_vs_utility.py`) — for every one of
the 2,018 filings, fetched the actual document, located every "tariff" occurrence, and checked
a ±200-character window around each for co-occurring signal terms:
- **Trade signal words:** trade policy/war/agreement/action/tension/barrier/restriction,
  import, export, duty/duties, customs, China, IEEPA, Section 301/232/122, retaliatory,
  trading partner, supply chain, countervailing, antidumping, sourcing, reciprocal tariff,
  geopolitical, cost of goods, manufacturing, gross margin, price increase.
- **Utility signal words:** FERC, PUC, public utility commission, rate case, commodity supply,
  feed-in, distribution/transmission/electric/gas/retail/delivery tariff, ISO-NE/PJM/MISO/NYISO,
  large load tariff, rate schedule, tariff filing/sheet, capacity market, utility commission.

A filing is classified **trade** if any occurrence has a trade signal nearby (even if it also
discusses utility tariffs elsewhere — mixed filings do exist), **utility_only** if every
occurrence only shows utility signals, **ambiguous** if neither signal set fires clearly, and
**no_match**/**fetch_failed** for retrieval issues (all fetch failures were retried and
resolved on a second pass).

**This is a keyword-co-occurrence heuristic, not a semantic classifier** — it's a defensible,
transparent, reproducible first-pass filter, not a substitute for human/AI-assisted review of
the ambiguous bucket before final analysis. Be honest about this in any methods section.

**6. Ambiguous-bucket resolution** (`resolve_ambiguous.py`, `ambiguous_resolved.csv`) — the 227
filings where step 5's keyword heuristic found neither signal set were read individually
(snippet was sufficient in all 227 cases; no full-document fetches were needed) and classified
by judgment rather than more keyword rules. 186 resolved to `trade`, 41 to `utility_only`
(including two word senses the original signal lists didn't anticipate: railroad "public
tariff" as a common-carrier freight rate schedule — Norfolk Southern — and FERC-regulated
pipeline "tariff-based customers" — Oneok, Williams Companies; both are the same non-trade
regulatory-rate sense as electric/gas utility tariffs, just outside the Utilities GICS sector).
Zero filings were genuinely unresolvable. Both buckets were merged into the final corpora below.

**7. Classifier validation** (`classifier_validation_results.md`) — a fresh, non-overlapping
random sample (20 `trade`-labeled, 15 `utility_only`-labeled) was independently read and judged
against its label: **35/35 agreement**. Two of the trade-labeled sample filings (PSE&G, Exelon)
are useful sanity checks — both companies also have utility-sense tariff mentions elsewhere in
the corpus, and the classifier correctly separated the two senses *within the same filer*
rather than just excluding by sector. See that file for the full caveats — this is a strong
internal-consistency check, not a formal inter-rater-reliability statistic with a second
independent human coder, which is what a methods section should ultimately cite.

**8. Realized vs. hypothetical/risk-factor split, and causation-attribution coding**
(`analyze_realized_vs_riskfactor.py`, output merged into
`sp500_tariff_TRADE_corpus_analyzed.csv`) — most SEC "tariff" mentions are forward-looking
risk-factor boilerplate ("could result in...", generic risk laundry lists), not disclosure of
an actually-*realized* price/cost action. Study 1's messaging typology (Nike, Mattel, BMW, etc.)
was built specifically from realized price-increase artifacts, so only this corpus's realized
subset is directly comparable to it. Every filing was fetched and scanned for tight,
co-located cost/action signal language (e.g. `"tariff-related costs of $"`,
`"increased prices... due to tariffs"`, `"mitigated the impact of tariffs"`) within the same
~250-char window as a "tariff" mention — **a first version of this classifier over-fired
(precision bug: a dollar figure anywhere in a document could trigger "realized" even when
unrelated to tariffs — caught by manually spot-checking its output, e.g. Marvell/Duke
Energy/PG&E generic risk-factor lists were wrongly tagged "realized"), so it was rebuilt to
require the signal and dollar figure to co-occur in the same tight window, then rerun from
scratch.** All 80 filings the rebuilt classifier labeled "realized" were then read in full by
hand (not sampled) — this caught a further residual issue: a few filings (AES, Duke Energy,
Exelon) are genuinely in the trade corpus for legitimate reasons elsewhere in the same
document, but the specific window that triggered "realized" was actually a utility-sense tariff
mention (Argentina generation-dispatch tariff, a legal tax-definition clause, a data-center
utility tariff) — corrected to `hypothetical_risk_factor` for those 3. One filing (Atmos Energy
10-Q) turned out to have been included in the trade corpus purely on the strength of an XBRL
inline-tag name (`ato:securitizedutilitytariffbondsmember`) rather than real prose — removed
from the corpus entirely. See `realized_full_dump.txt` for the full manual-review record.

Within the 80 verified "realized" filings, causation-attribution was coded (Study 1's Theme 2 —
the strongest candidate for the Study 2 vignette manipulation axis): **explicit** (tariffs
named as the direct cause, e.g. "tariff-related costs of $100 was primarily attributable to
tariffs") vs. **vague/listed** (tariff cost mentioned but embedded in a longer comma-separated
list of factors) vs. **silent/unclear**.

## Final numbers

| Bucket | Filings | Unique companies |
|---|---|---|
| **`sp500_tariff_TRADE_corpus.csv`** — primary corpus | **1,890** | **334 / 503 (66.4%)** |
| `sp500_tariff_EXCLUDED_utility.csv` — false positives, excluded | 119 | — |
| `sp500_tariff_NO_MATCH_or_failed.csv` | 9 | — |

(227 originally-ambiguous filings are folded into the two buckets above — see step 6. One
XBRL-artifact row was removed from the trade corpus during step 8's manual review — see above.)

Trade corpus by form: 8-K 682, 10-Q 808, 10-K 397, 10-Q/A 2, 8-K/A 1.
By year: 2025 → 1,147 filings; 2026 (through July 24) → 743 filings.
By GICS sector (filings / companies): Industrials 369/61, Financials 243/40, Health Care 243/45,
Consumer Discretionary 209/29, Information Technology 223/47, Consumer Staples 206/27,
Utilities 164/30 (post-filter — down from 266/31 raw, confirming the sector-specific
contamination the validation sample predicted), Materials 113/23, Energy 59/15, Real Estate
41/13, Communication Services 20/4.

**Realized vs. hypothetical split** (n=1,890): 80 filings (4.2%, 45 unique companies) are
verified realized tariff-cost/price disclosures; 1,538 (81.4%) are hypothetical/risk-factor
boilerplate; 262 (13.9%) unclear; 10 fetch failures. **Within the 80 realized filings:** 15
(18.75%) explicitly name tariffs as the cause, 62 (77.5%) mention tariff cost but bury it in a
longer factor list, 3 (3.75%) silent/unclear. **Headline pattern**: even when firms *do*
disclose a real, quantified tariff cost to investors, the large majority still frame it as one
item in a list rather than foregrounding tariffs as the cause — a notably more hedged posture
than Study 1's hand-picked consumer/press-facing artifacts (Nike, Mattel, Williams-Sonoma all
named tariffs explicitly), consistent with a real difference between what firms tell
regulators/investors vs. what they tell consumers/press. Worth treating as a hypothesis to
report carefully, not an established finding — see limitations below.

Full stats: `final_summary_stats.json`. Every row carries a `matched_snippet` and/or
`analysis_window` column (~400-700 chars of actual filing text around the match) so you can
eyeball classification decisions without re-fetching anything.

## Journal-readiness status

**Corpus construction is now defensible for a methods section**: reproducible free-data
pipeline, a documented multi-pass disambiguation (automated keyword filter → full manual
resolution of everything the filter couldn't resolve → a rebuilt-after-precision-bug
realized/hypothetical classifier → full manual read of every "realized"-labeled filing, not a
sample), and validated samples at two different layers (35/35 agreement on trade/utility;
100% manual coverage, not sampling, on the realized/causation layer). The audit trail — including
the mistakes found and fixed along the way — is intentionally left in this README rather than
cleaned up, because showing the error-correction process is itself evidence of rigor. Four
things still worth doing before submission, in order of importance:

1. **Get a second, independent coder** on a validation subsample and report Cohen's Kappa —
   everything so far (spot-checks, ambiguous resolution, classifier validation, realized-bucket
   review) was done by the same process (Claude, one continuous session). A formal inter-rater
   number with a second human coder is what reviewers will expect, per the shared TA method's
   validation-plan convention.
2. **There is now a finding, not just a corpus** — the realized-vs-hypothetical split and the
   causation-attribution pattern within it (see above) — but it rests on a heuristic classifier
   that needed two rounds of correction to get this far. Treat the 83.6%→77.5% vague-framing
   number as a hypothesis pending independent replication, not a citable statistic yet.
3. **The realized-bucket window-selection bug is a general lesson, not just a one-off fix**: the
   classifier picks the *first* matching window per document, which can be the wrong one in
   multi-topic filings (a utility company discussing both real trade tariffs and unrelated
   utility-rate tariffs in the same 10-Q). The 3 corrected rows were caught by manually reading
   all 80 — if the realized bucket grows substantially in a re-run (e.g. a later cutoff date),
   repeat that full manual read rather than assuming the classifier generalizes safely.
4. **Reproducibility note:** date range, search term, and form types are hardcoded in
   `fetch_tariff_filings.py` / `classify_trade_vs_utility.py` / `resolve_ambiguous.py` /
   `analyze_realized_vs_riskfactor.py` — keep them consistent if this needs to be re-run or
   extended (e.g., a later cutoff date as more 2026 filings come in).

## Target venue note

Britton's target is *Journal of Consumer Marketing* (JCM) for the tariff-messaging Study
1/2/3 program this corpus grew out of, but **this companion large-N analysis reads better in a
different tier of outlet than JCM.** JCM (Emerald) wants marketing-practice framing at
moderate methodological depth — a 1,890-filing SEC full-text corpus with a custom
disambiguation pipeline is a heavier methods lift than that venue typically carries. The
closer fit is the top-tier computational-text-as-data lineage already cited in
`Claude Knowledge\Thematic Analysis\AI_Assisted_TA_Shared_Method.md` (Berger et al. 2020 *JM*;
Tirunillai & Tellis *Marketing Science*/*JMR*; Netzer et al. *Marketing Science*) — i.e.
*Journal of Marketing*, *Marketing Science*, *Journal of Marketing Research*, or (methods-first,
slightly lower tier but still ABDC A) *International Journal of Research in Marketing*. A more
directly on-point precedent: **Cooper et al. (2022), "Text-mining 10-K (annual) reports: A
guide for B2B marketing research," *Industrial Marketing Management*, 106** — an actual methods
paper on mining 10-Ks for marketing research, in a solid ABDC-A B2B/marketing-strategy venue.
Since this corpus is corporate-disclosure/firm-behavior data rather than a consumer-behavior
study, Industrial Marketing Management (or Journal of Business Research) is likely the more
realistic primary target than either JCM or the A* stretch tier — cite Cooper et al. as the
methodological anchor if that's the direction taken. Once
there's an actual analysis/finding on top of this corpus, the finding itself should drive final
venue choice — a strong descriptive pattern (e.g., how messaging strategy varies by sector,
timing relative to Section 122's expiration, or firm size) could justify the top tier; a purely
descriptive corpus paper without a novel theoretical contribution is a harder sell above
IJRM-tier outlets regardless of data-collection effort. This is a call to make once Study 1 and
this companion analysis both have findings, not now.
