# 2026-08-15 — Corpus expansion pass 1 (WebSearch-only confidence)

**Tooling note (same as the last two nights):** `WebFetch` returned `EGRESS_BLOCKED` for
every domain tried tonight (tested against wwno.org). `WebSearch` worked fine. Everything
below is WebSearch-summarized, not directly fetched and read — one step short of this
project's primary-source standard. Flag for a follow-up direct-fetch verification pass once
WebFetch (or direct browsing) is working again, same caveat as the last two TARIFF_PAPER
notes and the 2026-08-14 summary.

**What this is:** the corpus in `Study1_Corpus_and_Coding_DRAFT_2026-08-12.md` sat at 11
artifacts and hadn't been touched since 2026-08-12 — three nights of the rotation queue.
Per that draft's own "what's needed to move forward" item 4 (expand toward the 15-20
standard TA sample size), this is a corpus-expansion pass, not a Phase 3 theme-review pass —
no themes are finalized or re-locked here, that stays Britton's call per the standing rule.
The pass also directly answers a gap the original `CLAUDE.md` flagged explicitly: Amazon's
Caddo Parish project had "less public detail surfaced so far" than Meta's. That's no longer
true — Amazon/Caddo turns out to have its own real opposition story, on par with Meta's.

---

## New candidate artifacts (6, bringing the corpus from 11 to 17)

### 12. Meta wins secrecy fight before Louisiana PSC (Aug 12-13, 2026)
Louisiana Public Service Commission voted **3-1 along party lines** (Republicans Coussan,
Francis, Skrmetta vs. Democrat Lewis) to let Meta keep Richland Parish data center details
confidential — reversing Chief Administrative Law Judge Melanie Verzwyvelt's order that Meta
produce documents substantiating its investment, job-creation, and power-consumption
projections. The subpoena originated with the Alliance for Affordable Energy and Union of
Concerned Scientists, challenging Entergy's request to expand the power system (the same
$13B power-plant buildout referenced in the original corpus). This is a **direct escalation**
of the original secrecy/NDA episode (#8 in the existing corpus, Oct 2024 filing) — now it's
not just corporate secrecy, it's a state regulatory body actively voting to uphold it against
a judge's own order, on a party-line vote. Strongest single new artifact for Theme 2
(procedural exclusion) — arguably stronger than anything currently in the corpus, since it
shows the exclusion being actively re-affirmed by an elected public body, not just alleged.
Multiple outlets covered it near-identically: [Louisiana Illuminator](https://lailluminator.com/2026/08/13/meta-data-center-private/),
[Fox8](https://www.fox8live.com/2026/08/13/louisiana-psc-allows-meta-keep-richland-parish-data-center-details-confidential/?outputType=amp),
[KTBS](https://www.ktbs.com/news/louisiana/meta-wins-secrecy-fight-before-louisiana-utility-regulators/article_991d105a-327a-54ea-925c-6e20979a36f4.html),
[American Press](https://americanpress.com/2026/08/13/meta-wins-secrecy-fight-before-louisiana-utility-regulators/).
→ Codes: `institutional-secrecy-endorsement`, `party-line-regulatory-capture-framing`,
`procedural-exclusion-secrecy` (extends existing code), `advocacy-org-standing`

### 13. New Orleans City Planning Commission proposes post-moratorium zoning rules (2026, date TBC — surfaced via nola.com, exact publish date needs verification on next fetch pass)
Follow-up to the corpus's existing #9-11 (Jan 2026 moratorium, Jul 2026 "hits pause"
extension): city planners have now proposed allowing *smaller* data centers under specific
conditions — under 100,000 sq ft, ≥500 ft from residential property, ≤20 MW power draw;
sub-20,000-sq-ft facilities allowed in commercial zones, larger ones industrial-only. This is
the resolution arc the existing corpus entries were left hanging on — worth adding as the
"what actually got decided" endpoint of the New Orleans thread. [nola.com](https://www.nola.com/news/new-orleans-planners-call-for-ban-on-large-data-centers-allowing-smaller-ones/article_52a05391-99a3-45f4-ad19-0891aec9612c.html)
→ Codes: `regulatory-resolution-graduated-restriction`, `size-based-compromise-framing`

### 14. Amazon $12B Caddo/Bossier Parish announcement (Feb 23-24, 2026)
Gov. Landry announced Amazon's $12B data center campuses spanning Caddo and Bossier
parishes — Amazon's first north-Louisiana / first data center. ~540 direct jobs (at/above
150% of statewide average wage), ~1,700 more supported in the community. Third site at
Resilient Tech Park (west Shreveport, off Greenwood Road) confirmed separately, not part of
the $12B figure. Establishes the economic-opportunity framing baseline for the Amazon case,
parallel to the Fox8/NOLA.com "boomtown" framing already coded for Meta (existing codes
`rapid-transformation-narrative`, `economic-opportunity-framing` apply directly).
[KSLA](https://www.ksla.com/2026/02/24/campuses-newly-announced-amazon-data-center-spanning-bossier-caddo-parishes-confirmed/),
[nola.com](https://www.nola.com/news/business/amazon-ai-data-centers-louisiana/article_ddb965ff-ed4d-40a8-9a70-6369f99a3298.html)

### 15. Sierra Club-backed litigation/appeal against Resilient Tech Park (Amazon, west Shreveport) (Apr-Jun 2026)
Caddo Parish Judge Ramon Lafitte dismissed (Apr 20, 2026) a challenge — brought by three
plaintiffs plus Sierra Club Delta Chapter — to the city council's approval of a special-use
permit, after the city planning commission had *initially blocked* the project. Plaintiffs
appealed to the Second Circuit Court of Appeal (deadline June 26, appeal proceeding).
Grounds cited: notice, environmental impact, infrastructure strain — directly parallel to
the existing corpus's `infrastructure-strain` code (#2-3, KNOE) and a new,
more institutionalized/legal form of the `collective-political-mobilization` code (#9-11,
currently only coded for New Orleans). This is the single most important find for filling
the "Amazon has less material" gap: it shows organized, formal legal opposition to Amazon
specifically, not just softer "residents want more information" sentiment.
[KTBS](https://www.ktbs.com/news/louisiana/sierra-club-backs-appeal-against-west-shreveport-data-center-development/article_02fbcd31-883a-59a4-b561-e03d01df0f48.html),
[Center Square](https://www.thecentersquare.com/louisiana/article_8aa1b34d-b246-4dac-ad81-c500ab1541f1.html)
→ Codes: `formal-legal-opposition`, `planning-commission-council-override` (city council
approved after planning commission had blocked it — a procedural-override pattern worth
comparing against New Orleans, where planning commission and council moved the same
direction), `infrastructure-strain` (extends existing code)

### 16. Caddo Parish commissioners push (and fail to pass) transparency/environmental-study measures for Blanchard site (Jun-Aug 2026)
Commissioner Ken Epperson proposed a resolution requiring an environmental study
(flooding risk to an adjacent neighborhood that "already struggles with flooding," and tree
removal near Greenwood Road) and an ordinance regulating temporary workforce-housing sites
for construction crews. **Neither measure passed the commission.** Commissioner Chris
Kracman, on record: "I've been begging for transparency left and right and have gotten very
little." This is a distinct flavor of procedural exclusion from Meta's PSC case — here the
elected local body itself tried and failed to get more transparency, rather than being the
body actively withholding it. Useful contrast for Phase 3 to consider: secrecy imposed
top-down by a state regulator (Meta/PSC) vs. secrecy a *local* elected body couldn't
overcome (Amazon/Caddo Commission) — same outcome, different institutional mechanism.
[KSLA](https://www.ksla.com/2026/06/02/caddo-parish-commissioners-seek-environmental-studies-data-center-projects/),
[Shreveport-Bossier Advocate](https://www.shreveportbossieradvocate.com/business/staack-and-aws-to-host-first-data-center-meeting-for-caddo-parish/article_7824f681-e203-475e-ab4b-71ab2835a5ad.html)
→ Codes: `local-transparency-request-failure`, `flooding-infrastructure-concern`,
`workforce-housing-concern` (new, not previously coded in this corpus)

### 17. Caddo Parish considers freezing tax breaks for data centers (Aug 2026)
Caddo Parish is weighing a temporary freeze on tax incentives for data centers — surfaced
same week as the Meta PSC secrecy vote, suggesting Aug 2026 is a genuine inflection point
across multiple LA jurisdictions simultaneously (worth noting for the paper's framing: this
isn't one isolated controversy, momentum is building on several fronts at once as of this
writing). [Center Square](https://www.thecentersquare.com/louisiana/article_6dfb8e12-29d7-4c97-b4da-53ddf9b35f97.html?a=)
→ Codes: `extractive-tax-framing` (extends existing code, now evidenced at Caddo too, not
just the Meta/Richland PILOT deals), `policy-momentum-clustering`

---

## What this changes about the draft thematic map (observations for Phase 3, not decisions)

- **The rural/urban split (Richland Parish vs. New Orleans East) that the original draft
  flagged as "itself analytically useful" is now better described as a three-way split**:
  Richland Parish (rural, Meta), New Orleans East (urban, Amazon-adjacent... no, correction —
  New Orleans East was the MS Solar Grid Data proposal, unrelated to Amazon) stays as-is, and
  now Caddo/Bossier (suburban/small-city, Amazon) adds a third site type with its own
  distinct opposition mechanism (formal litigation + failed local-government transparency
  push, rather than either New Orleans's successful moratorium or Richland's
  church-community-split framing). Whether to keep this three-way comparative structure or
  pool the corpus is exactly the kind of call the existing draft already flagged as Phase-3,
  Britton's-call — not resolved here, just noting the new material makes the three-way
  version more viable than it was with only 11 artifacts.
- **Theme 2 (procedural exclusion) is now the best-evidenced theme in the corpus by a wide
  margin**, not just tied with Theme 1 (distributive/environmental injustice) — artifacts
  #12, #15, and #16 all land there, from three different institutional levels (state
  regulator, judiciary, parish commission). Still Britton's call whether that makes it the
  Study 2 manipulation axis, but the evidentiary case for it strengthened materially tonight.
- **New code family worth flagging for Phase 3:** `formal-legal-opposition` and
  `local-transparency-request-failure` (both from tonight) don't fit cleanly under any of
  the six existing candidate themes — they're about the *mechanism* of opposition (courts,
  commission votes) rather than its *content* (justice, distrust, displacement). Might argue
  for a distinct theme about opposition escalating from discourse to formal institutional
  channels, which would also make Theme 6 ("collective political mobilization," currently
  flagged as maybe-a-DV-not-a-theme) more clearly a DV — litigation and failed commission
  votes are concrete, measurable "how far did opposition escalate" outcomes.

## Corpus is now at 17, within the 15-20 target range

No further expansion needed to hit the numeric target from `Study1_Corpus_and_Coding_DRAFT`'s
"what's needed to move forward" item 4. Still outstanding from that same item: pulling
primary sources (council/commission meeting minutes or video, the actual PSC order text,
court filings) for direct quotation — none of tonight's 6 additions are primary-sourced,
same caveat as the rest of the corpus. Recommend that as the next WebFetch-dependent pass.

## Not touched tonight
Phase 3 theme review itself, the Study 1 corpus-option decision (A/B/C), and the Study 2
design — all remain open, Britton's-call items per the existing orientation note. This pass
only adds material for him to review against, doesn't make any of those calls.
