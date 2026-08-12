# 2026-08-04 — Vignette pretest design

Validates the 6 cells in `2026-08-04-vignette-drafts-v1.md` before they're used in Study 2.

## Structure
Between-subjects, single-vignette exposure per participant (mirrors main-study exposure so
respondents can't compare cells against each other and infer the manipulation).

## Sample size
**N=150-180** (~25-30 per cell). Correction from an earlier looser "50-100" estimate given
in conversation — that number, split six ways, is too thin for reliable manipulation-check
ANOVAs. 25-30/cell is the standard convention for a manipulation-check pretest (distinct
from the larger N needed for the hypothesis-testing main study).

## Measures
**Manipulation checks (should differ sharply by condition):**
- Attribution Frame: continuous item ("how clearly did the message attribute the increase to
  tariffs?") + forced-choice recall (tariffs / general rising costs / no reason given / don't
  recall).
- Cost-Response: continuous item on perceived absorption ("is the company absorbing part of
  the cost, or passing it fully to customers?").

**Confound checks (should show NO significant difference across the 6 cells):**
- Perceived message length/complexity.
- Perceived company likability/credibility — candidate items adaptable from the Source
  Credibility Model (Hovland & Weiss 1951), which is already Britton's own toolkit from his
  dissertation (see `user_research_corpus.md` in the memory system).
- Perceived realism ("this reads like something a real company would say").

## Analysis / pass-fail criteria (set before looking at data)
- ANOVA on each manipulation-check item: expect a strong main effect of Attribution Frame on
  the attribution item, strong main effect of Cost-Response on the absorption item, and no
  cross-contamination (Attribution Frame shouldn't move the Cost-Response check, and vice
  versa).
- ANOVA on confound items: expect no significant differences across the 6 cells.
- Concrete threshold, e.g., ≥80% correct recall per condition on the forced-choice items.

## Cost estimate
N=150-180, ~6-7 min survey (vignette + both manipulation-check sets + confound items) on
Prolific at the academic rate (~$12/hr recommended pay + 33.3% platform fee): roughly
**$260-$340** total. (Revises an earlier, less carefully-reasoned $65-$200 estimate given
before the measures/N were actually specified.)

## IRB implication
This pretest is itself Prolific data collection on human subjects — it needs to be built
into the IRB application as an explicit Phase 1, not treated as a separate exempt afterthought.
Sequence is: IRB approval → Pretest → (possible vignette revision) → Study 2 → Study 3.
Real bottleneck for the late-September target is McNeese HSIRB's turnaround time, which is
still unconfirmed — worth asking Britton directly.

## Status
Design finalized. Depends on the vignette drafts (`2026-08-04-vignette-drafts-v1.md`) being
reviewed/finalized first.
