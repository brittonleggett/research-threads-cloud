# Overnight Summary — 2026-08-13 (recovered manually, see note below)

**How this file came to exist:** The nightly routine ran twice on 2026-08-13 (once on
schedule at 1:07am Central, once as a manual test later that afternoon) and did real work
both times, but a GitHub App permission problem meant neither run could push its commits.
Both ephemeral containers are gone now. This file was reconstructed by Britton's interactive
Claude Code session from the run logs (`get_run_log` on both sessions) — full detail below on
what's a faithful recovery vs. what's lost and needs to be redone.

## What's fully recovered (high confidence, exact numbers/facts)

**SEC filings vs. Study 1 consumer corpus — first-pass statistical comparison** (exploratory,
not yet citable): ran on data/codes already in the repo, no new coding.
- Firms name tariffs explicitly in **18.8%** of realized-impact SEC filings (n=80).
- Firms name tariffs explicitly in **75.0%** of Study 1's consumer/press corpus.
- 2×2 Fisher's exact test (explicit vs. not-explicit): table `[[15,65],[9,3]]`, odds ratio =
  0.077, **p = 0.000193**.
- 2×3 chi-square (descriptive only, some expected counts <5): χ² = 18.711, df=2, p = 8.6e-05.
- **Status:** preliminary first pass only. Needs a second independent coder on the
  causation-attribution scheme before this is citable, and it's Britton's Phase 3 call whether
  it goes in the paper at all.

**Real-world legal-context flag for the Tariff paper — worth Britton's attention:**
The Supreme Court struck down the administration's IEEPA tariff authority in February 2026.
Tariffs have since been reimposed under different legal bases — a Section 122 tariff (which
itself expired July 24, 2026) and, per later search results, a Section 301-based layer. The
TARIFF_PAPER Study 1 corpus and Introduction/Theory draft were written without addressing this
legal back-and-forth. **This needs Britton's read, not an AI rewrite** — it may or may not
change the paper's framing, that's his call. Real sources surfaced during the search (not yet
individually verified/quoted, just found and worth Britton or a future run checking directly):
White & Case client alert ("United States terminates IEEPA-based tariffs following supreme
court decision"), Tax Foundation analysis of the ruling, Z2Data's writeup of the Section 122
expiration. No exact quotes from these are reproduced here — that verification step didn't
happen before the container was lost.

## What's NOT recovered — needs to be redone, not guessed at

The 1:07am run completed primary-source verification passes for all 8 of the Tariff Paper's
corpus-expansion candidates (previously 4/8 were done). The last 4 — **La-Z-Boy, Birkenstock,
Insteel Industries, Home Depot** — were written up in that run's session but the detailed notes
(specific quotes, source links, exact wording) only exist in the lost container. The one
concrete headline fact that carried through clearly: **the earlier "drop Home Depot" call
should be reversed** — the run found solid corroboration of a real within-wave reversal in
Home Depot's public tariff-pricing stance, making it a usable data point rather than a weak
lead. But the underlying quotes/citations were not recovered and need a fresh verification pass
before anything from that pass 3 goes in a draft.

A second, later attempt at Insteel/Birkenstock/La-Z-Boy (afternoon run) was explicitly labeled
"DEGRADED" by the routine itself, because its `WebFetch` tool was blocked all session (an
unrelated Anthropic-side infrastructure issue, confirmed across many unrelated domains) — so
even if that note had been pushed, it was self-flagged as lower-confidence and worth a redo
anyway.

## Two new research-stream ideas were logged (titles only recovered, not full write-ups)

1. **Ratepayer cost-shifting fairness** — Louisiana data-center power buildout, adjacent to
   but distinct from DATA_CENTER_PAPER's existing angle (backlash/opposition framing vs. this
   angle's cost-distribution framing).
2. **Tariff-driven brand/private-label switching** — consumer response angle adjacent to but
   distinct from the existing Tariff Paper studies.
3. From the afternoon run: an LNG-terminal opposition angle (Cameron Parish, LA) and a
   possible methods-paper angle on AI-assisted research workflows themselves.

These are proposals only, per the project's standing rule — nothing here is a commitment or a
locked design.

## Bottom line for Britton

Two nights of real research output, but the actual value recovered here is: (1) a genuinely
new and important legal-context flag on the Tariff paper (SCOTUS/IEEPA), (2) a real
preliminary stats result worth knowing about, (3) confirmation the "drop Home Depot" call
should reverse (headline only, not backing quotes), and (4) four new candidate research-stream
ideas as one-liners. The detailed primary-source verification writing itself (the actual
value-add of that 8-source pass) needs to be redone once the GitHub App / Routines access issue
is actually fixed — that's a support ticket in progress, not an AI task.
