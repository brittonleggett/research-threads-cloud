# 2026-08-14 — SCOTUS/IEEPA legal sequence: confirmed and dated (follow-up to 2026-08-13 flag)

Follow-up to `2026-08-13-IMPORTANT-scotus-ieepa-flag-RECOVERED.md`, which flagged that the legal
authority behind "the tariffs" shifted mid-project and asked for the sequence to be pinned down
precisely. Same tooling caveat as the pass-3 note above: `WebFetch` is blocked network-wide this
session, so what follows is `WebSearch`-summarized, not directly fetched from the primary law-firm
alerts/court documents. Still a real upgrade over yesterday's "leads, not confirmed" state — the
search tool's own summaries pull specific dates/numbers, cross-corroborated across multiple
independent outlets (Wharton Budget Model, Holland & Knight, WilmerHale, Skadden, PwC, Deloitte,
Z2Data, IndustrialSage, Statt, jtradehelp, GingerControl, TariffsTool), so confidence is decent —
just not "read the primary document myself" confidence.

## The confirmed sequence

1. **Feb 20, 2026** — Supreme Court ruled **6-3** that IEEPA does not grant the President
   authority to impose tariffs of indefinite scope. Roberts wrote/led; Gorsuch and Barrett joined
   the majority along with Sotomayor, Kagan, Jackson (per Penn Wharton Budget Model's summary).
2. **12:00am ET, Feb 24, 2026** — all IEEPA-based tariffs terminated. Same day, the administration
   issued an executive order formally ending them and simultaneously imposed a new **10% tariff
   on imports from all countries**, this time under **Section 122 of the Trade Act of 1974**
   (a statute with a built-in 150-day clock, unlike IEEPA).
3. **May 7, 2026** — Court of International Trade ruled the Section 122 tariffs themselves
   exceeded presidential authority (per jtradehelp/other trade-compliance summaries) — a second
   legal challenge, distinct from the SCOTUS/IEEPA ruling, though search didn't surface enough
   detail on this ruling's practical effect before the statutory clock ran out anyway.
4. **12:01am EDT, July 24, 2026** — Section 122's 150-day clock expired; Congress didn't act to
   extend it. In the same minute, a **Section 301-based replacement** took effect: two-tier duties
   of **10%/12.5%** on roughly 60 economies (~99.4% of U.S. imports), tied to findings on
   forced-labor supply-chain practices — the lower rate for countries with at least partial
   forced-labor import protections, 12.5% for the rest. Unlike Section 122, this Section 301 layer
   has **no statutory expiration** — only litigation or negotiation removes it.
5. **Net effective-rate context:** search estimates put the average effective U.S. tariff rate
   falling from roughly 13% to roughly 7% with the Section 122 → Section 301 transition — a
   real magnitude, not a cosmetic legal swap.

So: IEEPA (struck down Feb 20/terminated Feb 24) → Section 122 (10% flat, expired by its own
150-day clock July 24) → Section 301 (10-12.5% tiered by country, open-ended). Three distinct
legal bases within the likely span of TARIFF_PAPER's Study 1 corpus and any Study 2 data
collection window.

## Why this matters for the paper — still Britton's call, not a rewrite

The Introduction/Theory draft and Study 1 corpus currently treat "the tariffs" as one stable
policy backdrop. They don't currently distinguish which legal authority was in force when a
given corpus artifact (a company statement, a news article) was published — which matters
because:
- **Insteel Industries** (see pass-3 note above) explicitly ties its causation story to
  **Section 232** steel tariffs specifically, a fourth, separate statutory basis not part of the
  IEEPA→122→301 sequence above (Section 232 tariffs on steel/aluminum predate and run alongside
  this timeline rather than being replaced by it).
- Corpus artifacts published between Feb 24 and July 24, 2026 were responding to a flat 10%
  Section 122 tariff; artifacts after July 24 are responding to the tiered, open-ended Section 301
  regime; artifacts before Feb 24 were under IEEPA. If Study 1's corpus spans this window (several
  entries — Walmart's Q1 FY26 transcript, for instance — predate the Feb 24 IEEPA termination),
  the "cause" respondents/companies were naming wasn't a constant across the corpus.
- This is a **framing/timeline/discussion-section decision**, not something to silently patch
  into existing drafts. Flagging it plainly again, one level more specific than yesterday's
  version, per the standing rule that Phase 3-adjacent judgment calls are Britton's.

## Confidence and next step

This resolves yesterday's "confirm the sequence precisely" ask at WebSearch-summary confidence.
Recommend one direct-fetch pass (once WebFetch/browsing access is restored) against the actual
Supreme Court opinion, the Federal Register notices for the Section 122 and Section 301 actions,
and the CIT's May 7 ruling, before this sequence is cited with page/paragraph precision in a
manuscript. The dates and structure above are consistent enough across many independent
secondary sources that they're very likely correct, but "very likely correct via search" and
"verified against the primary text" are different standards, and this paper's stated
citation-rigor bar (see `Overnight_Citation_Verification_2026-07-08.md`) is the latter.
