# 2026-08-27 — $1M fallback provision resolved (present-law, non-contradictory this time), HB804/Act 614 still quiet, WebFetch still blocked, small literature-scan addition

Follow-up to `2026-08-25-HB804-quiet-again-1M-fallback-partially-corroborated-webfetch-still-blocked.md`,
working the items it left open. **No Option A/B call made, no corpus file touched, no theme/design
decision touched** — those stay Britton's, per every prior note and the README. Phase 3 stays
human-only for this paper (no exception here — that's Flock Cameras only).

## 1. WebFetch — still blocked, confirmed on two more domains, one brief retest as instructed

Per the task's "one brief confirmation is enough" guidance, tried the actual highest-value target
first rather than a Wikipedia control (already confirmed dead many times over):

```
WebFetch https://legis.la.gov/Legis/BillInfo.aspx?i=249698   -> EGRESS_BLOCKED (domain: legis.la.gov)
WebFetch https://law.justia.com/codes/louisiana/revised-statutes/title-30/rs-30-1109/ -> EGRESS_BLOCKED (domain: law.justia.com)
```

`law.justia.com` is a new domain/domain-type for this thread's block log (a legal-code aggregator,
distinct from legis.la.gov, legiscan.com, a news outlet, and Wikipedia already confirmed on prior
nights). Still the same failure signature (`EGRESS_BLOCKED`, proxy-level). This is now roughly the
17th consecutive session with WebFetch fully dead, across five different site categories. Not
retesting further tonight — repeating the standing recommendation from 08-24/08-25 that this needs
someone to look at the proxy/egress configuration directly, not another nightly confirmation.

## 2. HB804/Act 614 legal status — still quiet, no new lawsuit or challenge

Fresh WebSearch pass tonight ("HB804 Louisiana Energy Protection Act lawsuit constitutional
challenge August 2026") returned the same April–June 2026 legislative-process coverage already
documented across the 08-20 through 08-25 notes, plus reconfirmation of facts already on record
(signed by Gov. Landry June 11 2026; Rep. Brett Geymann R-Lake Charles sponsor; the Senate
grandfathering amendment protecting 40+ existing coastal-erosion suits — all already in the 08-20
and 08-21 notes, not new tonight). **No lawsuit, constitutional challenge, or enforcement action
against HB804 or HB79/Act 614 found as of tonight (08-27).** Extending the negative result. Also
did not find a specific Act number for HB804 itself in tonight's searches (only HB79's Act 614 has
been established in prior notes) — flagging as a minor, low-priority open item, not urgent.

## 3. The $1M noneconomic-damages fallback — now resolved with good multi-source convergence, no internal contradiction this time

This has been the thread's most persistently confusing item (08-24: "likely misattributed to
HB169"; 08-25: "plausible but unconfirmed," with the same three searches disagreeing on which law
the $250K/$500K caps belong to). Tonight, three differently-phrased WebSearch passes converged on
one consistent, internally-coherent account — **no discrepancy between passes this time**:

1. A search for the HB79 bill digest itself surfaced what reads as the actual Present
   Law/Proposed Law digest language directly:
   > **Present Law:** ...civil liability actions against owners and operators of carbon dioxide
   > storage facilities and carbon dioxide transmission pipelines and generators of the carbon
   > dioxide being transported or stored... general limit on compensatory damages for noneconomic
   > losses at $250,000 per person and the limit for exceptional cases at $500,000 per person.
   > Present law also provides the maximum amount recoverable for noneconomic losses at $1 million
   > when the law is found to be unconstitutional or invalid (the fallback provision).
   > **Proposed Law:** The bill removes these damage caps entirely, allowing for unlimited
   > recovery of noneconomic damages...
   (Search-engine-assembled summary, not an independently fetched primary document — WebFetch is
   still blocked — but this is a direct quote-style rendering of a bill digest, a more specific
   artifact than the general-summary answers prior nights got.)
2. A second, independently-phrased search for the R.S. 30:1109 statute text itself returned a
   quoted statutory fragment consistent with the above: "if [the cap is] finally determined by a
   court of law to be unconstitutional or otherwise invalid, the maximum amount recoverable as
   damages for noneconomic loss shall thereafter not exceed one million dollars per person."
3. A third search, targeting HB169 (2024 session — the bill 08-24 worried this was being
   cross-attributed from) specifically, clarified rather than contradicted: **HB169 (2024) is the
   bill that changed R.S. 30:1109's $250,000/$500,000 caps from a "per occurrence" basis to a
   "per person" basis** — i.e., HB169 amended the caps' *unit*, not the $1M fallback figure itself,
   and predates HB79 by one session. This becomes "present law" HB79 then acts on in 2026.

**Net picture, all three passes agreeing:** R.S. 30:1109 (before HB79) capped noneconomic damages
at $250,000/person (general) and $500,000/person (wrongful death/permanent-disfigurement
exceptions), with a $1,000,000/person fallback that would apply only if a court struck the caps
down as unconstitutional — all of this is **present/prior law**, not something HB79 introduces.
HB79's own operative change (**"Proposed Law"**) is to repeal all three figures and allow
unlimited noneconomic-damages recovery. This also matches 08-21's independent, non-WebSearch
finding from directly extracting the *introduced* bill's PDF text (`HB_79_Damages_Threshold.pdf`,
`HLS 26RS-572 ORIGINAL`): "the as-introduced text (Section 2) fully repeals the damages-cap
subsection (G) and rewrites (B)-(F) to strike the $250K/$500K/$1M caps entirely."

**Confidence level:** Upgraded from 08-25's "plausible but unconfirmed" to **high-confidence,
multi-source-convergent** — three independently-phrased WebSearch passes tonight agree with each
other and with 08-21's direct PDF extraction of the introduced bill, with no internal
contradiction this time (unlike 08-24 and 08-25, which each caught a discrepancy). **Still not
primary-source-confirmed** in the strict sense used throughout this thread (no direct WebFetch/
legis.la.gov read of the enrolled Act 614 text) — that distinction matters and I'm not collapsing
it — but this is materially stronger evidence than any prior night reached, and it would take an
actual contradicting primary-source read to overturn it at this point, not just another search
pass. **Safe to describe in a manuscript-adjacent note as "present law provided a $250K/$500K
per-person cap with a $1M per-person unconstitutionality fallback; HB79/Act 614 (2026) repealed
all of it"** — with the standard caveat that a primary-text read is still the right final step
before this goes into an actual manuscript citation.

## 4. Small literature-scan addition (legal-status checks were not fully empty, but added a modest amount of grounding time per the task's step 3)

Two searches for CCS-discourse/public-opposition and CCS-liability/greenwashing literature
published since the 08-16 grounding note surfaced one genuinely new, WebSearch-confidence-only
candidate worth flagging for Track C's novelty argument (not independently fetched/verified —
flagging exactly at that confidence level, consistent with 08-16's own tiering):

- **Xiao, T., Middleton, E., Bakelli, O., Cheng, S., Zhu, D., Xu, L., & McPherson, B.
  "Public Perceptions and Engagement for Carbon Capture, Utilization, and Storage: Literature
  Review With a Case Study of Utah, USA." *Greenhouse Gases: Science and Technology*, Wiley
  Online Library, DOI 10.1002/ghg.2381.** Two search passes tonight disagreed on the publication
  year (one said 2026, one said 2025) — flagging that discrepancy explicitly rather than picking
  one, same search-hygiene practice this thread already applies to other conflicting details;
  verify the year from the DOI page directly before citing. Substantively: a recent (2025 or 2026)
  literature review + Utah newspaper-article case study (195 articles, Salt Lake Tribune/Deseret
  News) that explicitly did **not** analyze CCUS discourse on social media, citing
  sample-collection difficulty as the reason. This is useful, current corroboration for the 08-16
  novelty-check conclusion (Track C's AI-assisted netnography of public/Reddit CCS discourse is
  still a real gap) — a 2025/2026-dated review paper naming social-media CCUS discourse as an
  unaddressed methodological gap is stronger support for "this gap is current, not stale" than
  the single 2018 Keane precedent alone. Not added to any manuscript file; flagged only.
- A second, related 2026 ScienceDirect systematic review ("Drivers and barriers to social
  acceptance of carbon capture, utilisation and storage: a systematic literature review of
  survey-based studies") surfaced but wasn't examined in enough depth to summarize responsibly
  tonight — survey-based, not discourse-based, per its own title; worth a closer look in a future
  session if literature-grounding time is prioritized again, not claiming more than the title
  states here.
- No new hit on CCS-specific greenwashing/liability-shield academic literature (the second search
  mostly returned general corporate-greenwashing-liability material, e.g. carbon-credit/Apple
  litigation commentary, not CCS-specific) — a genuine dead end for that angle, not pursued further.

This is a light addition, not a full grounding pass — the 08-16 note remains the authoritative
literature-grounding document for this paper; tonight only adds one dated, WebSearch-confidence
candidate on top of it.

## Bottom line / what's still open for Britton

1. **HB804/Act 614: still no new legal or legislative development.** Genuinely quiet through
   08-27, extending the negative result documented since 08-22.
2. **WebFetch: still fully blocked**, now confirmed on a fifth site category (law.justia.com)
   across roughly 17 consecutive sessions. Recommend, again, that this stop being retested
   nightly and instead get a direct look at the proxy/egress configuration.
3. **The $1M fallback question is now resolved with high confidence** (three convergent
   WebSearch passes tonight, agreeing with each other and with 08-21's direct PDF extraction, no
   internal contradiction this time): the $250K/$500K/$1M figures are all present/prior law
   (R.S. 30:1109, with HB169-2024 having set the caps to a per-person basis); HB79/Act 614 (2026)
   repeals all of them, allowing unlimited noneconomic-damages recovery. Still short of a strict
   primary-source (WebFetch) confirmation, but safe to describe at this confidence level with the
   caveat noted above — this is the strongest this finding has looked across four nights of
   rechecking it.
4. **One new literature candidate flagged** (Xiao et al., Utah CCUS-perceptions review,
   *Greenhouse Gases: Science and Technology*, year unconfirmed 2025 vs. 2026 — verify before
   citing) — supports Track C's existing novelty argument, not independently fetched.
5. **Option A/B choice: unchanged, still Britton's call.** Nothing tonight bears on it either way.
6. **Phase 3 / theme review: untouched, stays human-only for this paper** — no exception here.
