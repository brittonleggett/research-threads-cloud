# Tariff Paper — Study 1: Corporate Tariff-Messaging Corpus & Coding (DRAFT)

**Status: Phases 0.5–2 complete (AI-assisted). Phase 3 (theme review) is yours to do — not run by AI, per the shared method's non-negotiable rule.**

Method: AI-assisted thematic/content analysis of corporate messaging (small-q, coding-reliability
TA — not netnography, not reflexive TA), per
`Claude Knowledge\Thematic Analysis\AI_Assisted_TA_Shared_Method.md`. IRB-exempt (45 CFR
46.102(e) — public corporate documents, no human-subjects contact), so this can proceed
independent of the Study 2/3 IRB filing decision.

---

## Phase 0.5 — Brief

- **RQ:** How do firms discursively frame tariff-driven price increases to consumers/investors,
  and what typology of messaging strategies emerges that could ground realistic Study 2 vignette
  stimuli?
- **Theory frame:** dual entitlement theory (Kahneman, Knetsch & Thaler, 1986 — firms are seen as
  "entitled" to pass through cost increases, but not to raise prices opportunistically for profit),
  prospect theory (loss framing / reference-dependence), psychological reactance (Brehm, 1966 —
  resistance to perceived-forced, non-consensual price changes).
- **Data type:** public corporate communications — earnings-call transcripts, press coverage of
  official statements, price bulletins. Not survey/interview data, not human subjects.

---

## Corpus (7 artifacts, sourced 2026-07-24)

| # | Firm | Industry | Artifact type | Date | Source |
|---|------|----------|---------------|------|--------|
| 1 | Nike | Apparel/footwear | Earnings call (CFO Matthew Friend) | Q4 FY2026 (~June 2026) | [CNBC](https://www.cnbc.com/2026/06/30/nike-nke-q4-2026-earnings.html), [Supply Chain Dive](https://www.supplychaindive.com/news/nike-1b-tariff-sourcing-price-hikes/752159/) |
| 2 | Mattel | Toys | Earnings call (CFO Anthony DiSilvestro) + CEO public statement | 2026 | [Seeking Alpha](https://seekingalpha.com/news/4441242-mattel-says-higher-prices-in-the-us-will-be-a-part-of-its-tariff-mitigation-strategy), [ABC7](https://abc7ny.com/post/mattel-ceo-confirms-plans-raise-prices-he-calls-zero-tariffs-toys/16338243/) |
| 3 | BMW | Automotive | Dealer price bulletin | Effective 2026-01-01 | [Carscoops](https://www.carscoops.com/2025/12/bmw-increasing-prices-by-up-to-1500-in-2026/) |
| 4 | Lennox Int'l | HVAC | Earnings call (CFO Michael Quenzer) | Q4 2025 (Jan 2026 call) | [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/01/28/lennox-lii-q4-2025-earnings-call-transcript/) |
| 5 | Dormakaba | Building hardware | Price list update + press statement | Effective 2026-03-02 | [Business Reporter](https://www.business-reporter.co.uk/news/dormakaba-to-pass-on-tariff-costs-to-customers-as-it-targets-north-american-growth-13354) |
| 6 | GMS | Building materials distribution | Surcharge adjustment notice | Effective 2026-02-01 | [Banner Solutions](https://www.bannersolutions.com/news/2026-manufacturer-price-changes) |
| 7 | Williams-Sonoma | Home goods retail | Earnings call (Q1 2026) | 2026-05-21 | [Motley Fool transcript](https://www.fool.com/earnings/call-transcripts/2026/05/21/williams-sonoma-wsm-q1-2026-earnings-transcript/) |

**Corpus notes:** All secondary-sourced (news coverage / transcript aggregators of primary
earnings calls and bulletins), not scraped directly from SEC filings — good enough for an initial
inductive pass, but before this goes in the paper, pull primary-source transcripts (8-K exhibits,
investor-relations pages) for direct quotation and page/paragraph citation. BMW's artifact is a
*dealer* bulletin, not a consumer-facing statement — flag this as a possible data-type outlier
when you review.

---

## Phase 1 — Inductive codes

**1. Nike** — Names tariffs explicitly as cost driver (~$1B). Uses "surgical price increase"
language — precision/restraint framing, implies limited scope. Pairs the price increase with a
visible mitigation narrative (sourcing shift out of China, supplier/retailer negotiation) — firm
is *seen to be absorbing* what it can before passing through the rest.
→ Codes: `causation-explicit`, `restraint-language`, `mitigation-narrative`, `phased-rollout`

**2. Mattel** — CFO quantifies exact cost ($270M) — numeric transparency as legitimation. CEO
publicly calls for "zero tariffs on toys" — externalizes blame to policy, distances firm from
causation ("we didn't choose this"). "Where necessary" — conditional/selective language, echoes
Nike's restraint framing. Price actions explicitly done "in collaboration with retail partners" —
diffuses unilateral responsibility. Supply-chain diversification (exit China) — long-horizon
mitigation signal.
→ Codes: `causation-explicit`, `blame-externalization`, `restraint-language`, `numeric-transparency`, `shared-responsibility-framing`, `mitigation-narrative`

**3. BMW** — Official bulletin **avoids tariff language entirely**; frames increase as routine
("in line with past pricing communications"). No cost quantification, no mitigation narrative.
→ Codes: `causation-silent`, `normalization-as-routine`, `non-disclosure`

**4. Lennox** — Leads with cost-mitigation effort (material cost reduction, productivity programs)
rather than the price increase itself; tariff impact ($125M) stated matter-of-factly, blended into
a broader cost-management story rather than foregrounded as the reason for a price increase.
→ Codes: `causation-explicit-but-backgrounded`, `mitigation-narrative`, `cost-diffusion` (price is one lever among several, not the headline)

**5. Dormakaba** — Relabels an existing temporary "surcharge" as a permanent "list price
increase" — linguistic shift from exceptional/temporary framing to normalized/permanent framing.
Explicitly invokes "in line with industry practices" — social-proof/legitimation appeal.
→ Codes: `reframing-temporary-to-permanent`, `industry-norm-appeal`, `normalization-as-routine`

**6. GMS** — Tariff *surcharge* (explicitly tariff-labeled when imposed) is *reduced*, but the
reduction is attributed to generic "market conditions" rather than credited to tariff relief —
asymmetric transparency: specific/tariff-blamed language going up, vague language coming down.
→ Codes: `causation-explicit` (increase) / `causation-vague` (decrease), `asymmetric-disclosure`

**7. Williams-Sonoma** — Most transparent artifact in the corpus: names specific tariff sections
(232, 301, 122), explicitly says "impossible to say" where tariffs will land, walks through
uncertainty and timing (H1 2026 peak impact) rather than asserting confidence.
→ Codes: `causation-explicit`, `high-technical-transparency`, `uncertainty-acknowledgment`

---

## Phase 2 — Candidate themes (draft thematic map — needs your Phase 3 review)

**Theme 1: Restraint signaling** (Nike, Mattel) — "surgical," "where necessary" — language that
frames the firm as taking the *minimum* action required, directly mapping onto dual entitlement's
fairness logic (pass-through of unavoidable cost = acceptable; opportunistic increase = not).

**Theme 2: Causation attribution — explicit vs. silent vs. vague** (spans all 7) — firms vary from
naming tariffs specifically and often (Williams-Sonoma, Mattel, Nike) to omitting cause entirely
(BMW) to using vague substitute language especially when the news is favorable (GMS's price
*decrease*). **This may be the strongest candidate for the Study 2 vignette manipulation axis** —
it's the dimension with the clearest theoretical mapping (prospect-theory framing + reactance:
unexplained/forced-seeming price changes should trigger more reactance than clearly-justified
ones) and the most corpus variation.

**Theme 3: Mitigation-effort narrative** (Nike, Mattel, Lennox) — pairing the price increase with
visible internal effort (sourcing shifts, cost programs) — a legitimation strategy distinct from
just naming the cause; firm shows it isn't *only* passing costs through passively.

**Theme 4: Normalization through relabeling** (Dormakaba, and arguably BMW's "in line with past
pricing communications") — reduces the salience of the increase as an exceptional, tariff-caused
event by presenting it as routine business-as-usual. Theoretically interesting tension: this may
*reduce* reactance (doesn't feel like an imposition) while *weakening* the dual-entitlement
justification (doesn't clearly earn "fair pass-through" status either) — worth flagging as a
possible design trade-off in Study 2.

**Theme 5 (tentative, single-case — flag for more corpus support before treating as a theme):**
Asymmetric disclosure — specific/blame-attributing language on price increases, vaguer language on
decreases (GMS). Only one artifact currently supports this; worth deliberately sourcing 1-2 more
"price decrease / surcharge rollback" artifacts before deciding if this is a real pattern or noise.

---

## What's yours to do next (Phase 3, by design — not run by AI)

1. Review these 5 candidate themes against the actual corpus artifacts (links above) — does the
   clustering hold up, would you split/merge any, is anything mislabeled.
2. Decide whether Theme 2 (causation attribution: explicit/silent/vague) is in fact your Study 2
   manipulation axis, or whether Theme 1 (restraint) or Theme 4 (normalization) is a better fit —
   this is a design call, not something to defer to AI.
3. Once themes are settled: Phase 4 (naming/definitions) — I can generate name options once you
   give me a settled theme to work from, per the method.
4. Before this goes in the paper: expand the corpus (aim for a more standard TA sample size —
   maybe 15-20 artifacts) and pull primary sources (8-Ks, IR pages) rather than secondary news
   coverage, then run the validation step (manual-vs-AI pilot subsample agreement) the method
   calls for.

**Disclosure note for methods section:** This coding pass (Phases 0.5-2) was AI-assisted (Claude,
Anthropic) per the documented 6-phase workflow; theme review (Phase 3) was researcher-only, no AI
involvement, consistent with Xu (2026)'s precedent for that phase.
