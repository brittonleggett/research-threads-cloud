# Standalone paper outline — SP500 tariff-disclosure corpus
_Drafted 2026-08-04. This turns the existing corpus (README.md, same folder) from a
"companion" artifact into its own submission, per the AI-augmented-researcher positioning
decision — this is proof-point #1._

## Working titles (pick one, or riff)
1. "Same Shock, Different Story: Audience-Tailored Disclosure of Tariff Costs in Corporate
   Communications"
2. "Speaking to Regulators vs. Speaking to Customers: Asymmetric Tariff-Cost Disclosure in
   S&P 500 Filings"
3. "Hidden in Plain Sight: How Firms Selectively Foreground Tariff Costs Across Stakeholder
   Audiences"

## The actual contribution (this is the part that makes it a paper, not just a corpus)
The corpus alone is a methods artifact. The paper needs a **finding**, and there already is
one, sitting half-stated in the existing README: within the 80 SEC filings that verifiably
disclose a *realized* (not hypothetical/risk-factor) tariff cost, only **18.75% explicitly
name tariffs as the cause** — the other 81.25% either bury it in a longer factor list
(77.5%) or stay silent/unclear (3.75%). That's a striking contrast with Study 1's
consumer/press-facing corpus (the Tariff Paper's own Study 1, now 15 candidate artifacts),
where explicit tariff-naming is the norm — Nike, Mattel, Williams-Sonoma, Lennox, IKEA, and
others all name tariffs directly to consumers and the press.

**The puzzle this sets up:** dual entitlement theory (Kahneman, Knetsch & Thaler, 1986)
predicts firms *should* want to name tariffs explicitly — an external, uncontrollable cause
legitimizes a price increase to consumers. Study 1's corpus shows firms doing exactly that.
So why do the same firms, facing the same cost shock, go quiet or vague about it when talking
to investors and regulators in SEC filings? That asymmetry — not just "here's a big corpus"
— is the actual research question.

## Research question
Do firms disclose tariff-driven cost pressures differently depending on audience (regulators/
investors via SEC filings vs. consumers/press via public-facing communications), and what
explains the asymmetry?

## Theoretical framing
- **Disclosure/obfuscation literature (accounting)** — Li (2008), "Annual Report Readability,
  Current Earnings, and Earnings Persistence," *Journal of Accounting and Economics* — firms
  with less favorable news write less readable disclosures. Bloomfield (2002), "The
  'Incomplete Revelation Hypothesis' and Financial Reporting," *Accounting Horizons* — costly
  processing means firms can bury unfavorable information in complexity without technically
  omitting it. This is the literature that explains *why* SEC-filing language would be vaguer
  even when the underlying fact (tariffs raised costs) is the same.
- **Dual entitlement theory** (Kahneman, Knetsch & Thaler, 1986) — already the tariff paper's
  anchor theory, reused here as the reason the asymmetry is *surprising*, not merely
  descriptive.
- **Stakeholder/audience-tailored communication theory** (Freeman's stakeholder theory
  lineage) — different disclosure obligations, risk profiles (litigation, political
  sensitivity, competitive intelligence), and audiences plausibly justify different framing
  strategies, which is the paper's proposed *explanation* for the asymmetry, worth testing
  against alternatives (e.g., simple SEC boilerplate convention) rather than asserting.

## Method (mostly already built — recap from README.md in this folder)
- Corpus: 1,890 S&P 500 filings (10-K/10-Q/8-K) mentioning "tariff," 2025-01-01 to
  2026-07-24, via SEC EDGAR full-text search API. Multi-pass trade-vs-utility disambiguation
  (validated 35/35 on an independent sample). Realized-vs-hypothetical split (80 verified
  realized, full manual read not sampling). Causation-attribution coding within the realized
  bucket (explicit/vague/silent).
- **New for this paper:** formal head-to-head comparison against Study 1's consumer/press
  corpus (currently 15 candidates, growing), using the *same* causation-attribution coding
  scheme across both, then a statistical test of the distributional difference (chi-square or
  Fisher's exact, given the SEC bucket's small explicit-attribution cell (n=15) — Fisher's is
  the safer choice).
- **Second coder + Cohen's Kappa** — not yet done. This is the single biggest gap before the
  causation-attribution numbers are citable as more than a hypothesis (already flagged in the
  README's own journal-readiness section).

## Target venue
**Primary: Industrial Marketing Management.** Direct methodological precedent already
identified: Cooper et al. (2022), "Text-mining 10-K (annual) reports: A guide for B2B
marketing research," *Industrial Marketing Management*, 106 — same data source, same general
method family, established B2B/marketing-strategy venue. This is a much better fit than JCM
(too heavy a methods lift for that venue's typical papers) or a top-tier stretch (JM/Marketing
Science/JMR) unless the audience-asymmetry finding turns out to be stronger than expected
once formally tested.
**Backup: Journal of Business Research.**

## What's needed before this is a real draft, not just an outline
1. **Second, independent coder** on the causation-attribution scheme (both the SEC bucket and
   Study 1's corpus, for consistency), report Cohen's Kappa. This is the load-bearing
   methodological gap.
2. **Formal statistical comparison** between the two corpora's causation-attribution
   distributions — not yet run.
3. **Full lit review section** — theory citations above are a starting scaffold, not a
   written review.
4. **Decide the comparison group's final N** — Study 1's corpus is still at 15 candidates
   pending your Phase 3 review (per tonight's tariff-paper corpus-expansion note); this paper
   needs that count settled before the comparison table is final.
5. **Re-verify the realized-bucket window-selection caveat** already flagged in the README if
   the SEC corpus is extended past its current 2026-07-24 cutoff before this goes to
   submission.

## Why this is worth doing now, not later
Per the career-positioning conversation: this paper is close to submission-ready on the
methods side (unusual for a paper this early — most of the hard data-collection and
first-pass classification work is done), and it's the single strongest existing proof-point
for the "disclosed, validated, rigorous AI-augmented research" brand — the corpus README's
own error-correction trail (the realized-bucket precision bug, the 3 utility-sense
mis-classifications caught and fixed) is itself evidence of the rigor this positioning is
built on, not something to clean up or hide before showing anyone.
