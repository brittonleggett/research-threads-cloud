# Meat Supply Chain Paper — Project Brief

## What this is
Exploratory paper concept (started 2026-09-03): foreign meat imports,
meatpacking/processing concentration, farmer/rancher returns, consumer prices,
and country-of-origin transparency in U.S. beef, pork, and poultry markets.
Not yet locked into a title, theory, or study design — this is the "explore"
stage, same starting point TARIFF_PAPER and DATA_CENTER_PAPER were at in their
first orientation notes.

Working title (not locked): *Foreign Meat Imports, Supply-Chain Concentration,
Farmer Returns, Consumer Prices, and Transparency in the U.S. Beef, Pork, and
Poultry Markets.*

Motivating question: How do foreign sourcing, meatpacking/processing
concentration, labeling practices, and supply-chain power interact to
influence the prices received by U.S. producers and the prices paid by U.S.
consumers?

## Why this fits the existing pipeline
Same **Study 1 (AI-assisted thematic analysis of corporate/producer/agency
discourse) → Study 2 (survey/experiment) → Study 3 (archival/econometric)**
architecture already used for TARIFF_PAPER, CCS_PAPER, FLOCK_CAMERAS_PAPER,
DATA_CENTER_PAPER. Reusable method template:
`Claude_Knowledge\Thematic Analysis\AI_Assisted_TA_Shared_Method.md` (check
exact path/filename in `Claude_Knowledge/` before citing it in the manuscript).

## Ground rule for this project specifically
This is an empirical investigation, NOT an advocacy piece. Do not start from
"corporations are gouging consumers" or "farmers are being exploited." Those
are propositions in `NOTES/Claim_Fact_Check.md`, to be marked Supported /
Partially supported / Unsupported / Misleading without context / Unresolved —
not assumed. Beef, pork, and poultry have different institutional structures
(see `NOTES/Commodity_Structure_Comparison.md`) and must not be mechanically
combined when the evidence doesn't support combining them.

## Folder structure (heavier than the other papers' flat layout, by design —
this brief asked for a more rigorous scaffold up front)
- `README.md` — project overview and folder map.
- `PROJECT_STATUS.md` — living status doc: what we know, what's interesting,
  what didn't hold up, best marketing contribution, recommended study
  architecture, top sources, open decisions for Britton, next actions.
- `RESEARCH_QUESTIONS.md` — the core empirical puzzle and sub-questions.
- `THEORY_CANDIDATES.md` — ranked theory lenses (Strong / Possible / Weak).
- `DECISION_LOG.md` — dated record of research decisions and why.
- `LITERATURE/` — market concentration evidence, price-transmission
  literature, other lit-review memos.
- `CORPUS/` — Study 1 artifact corpus (once built).
- `DATA/` — downloaded/extracted quantitative data (USDA, Census, FRED, etc.).
- `ANALYSIS/` — import-structure analysis, any quantitative work product.
- `NOTES/` — problem-exploration memos, COOL timeline, fact-checks, dated
  research-pass logs (same convention as DATA_CENTER_PAPER's `notes/`).
- `MANUSCRIPT/` — draft sections, once we're past the exploration stage.
- `STUDY1/`, `STUDY2/`, `STUDY3/` — per-study planning and, later, drafts.
- `SOURCE_VERIFICATION/` — `Evidence_Table.md`, the master claim→source
  verification ledger. Every load-bearing empirical claim in this project
  should trace back to a row here.

## Working conventions (matching the rest of the pipeline)
- Work in small, reviewable steps; prefer new dated files over overwriting.
- Primary sources (USDA/ERS/AMS/FSIS/FAS, Census, BLS, FRED, DOJ, FTC, CRS,
  GAO, Federal Register, USITC, SEC filings, court filings) over news
  summaries. When secondary media surface a claim, trace it to the underlying
  data before treating it as evidence.
- Never fabricate a citation. Verify important citations against the
  original source before relying on them.
- Distinguish concentration / oligopoly / monopsony / monopoly / market power
  / vertical integration / buyer power / anticompetitive conduct — do not use
  interchangeably.
- Preserve contradictory findings rather than smoothing them over.
- Record unsuccessful or inconclusive searches when they matter (a claim we
  could not verify is itself a finding).
- Small Git commits with descriptive messages; push so work isn't lost.
- Beef / pork / poultry get separate treatment wherever their structures
  differ (see Section 3 / `NOTES/Commodity_Structure_Comparison.md`).
- No substantive theory or study-design lock-in without Britton's sign-off —
  flag genuine judgment calls in `PROJECT_STATUS.md` under "Open decisions."
