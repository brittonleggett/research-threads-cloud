# 2026-08-12 — Orientation: Data Center Backlash Paper

Exploratory. Nothing below is locked — this is the same stage the Tariff
Paper was at before its 2026-08-04 design-lock conversation. Purpose here is
to lay out the real-world grounding and candidate theory options so Britton
can make the same kind of design call he made for Tariff Study 2.

## The real-world hook (why this is timely and topic-fit, not a stretch)

**Three Louisiana data center stories, all live in 2026:**

1. **Meta "Hyperion"** (Richland Parish) — Manhattan-sized hyperscale facility.
   Needs **10 new natural gas power plants** (7,500 MW) to run. Registered
   water use of **23 million gallons/day** — would nearly double the entire
   parish's water withdrawals. Meta projected to receive up to **$3.6 billion**
   in sales tax exemptions over the first decade; Entergy separately seeking
   to avoid $237M in local property taxes over 10 years via PILOT deals.
   ([DeSmog](https://www.desmog.com/2026/05/08/in-louisiana-data-center-hype-faces-ai-regulation-and-community-resistance/))
2. **Amazon** (Caddo Parish) — similar PILOT-deal structure, less public detail
   surfaced so far.
3. **MS Solar Grid Data** (New Orleans East, near I-10/Read Blvd) — smaller
   proposed facility, now dead after community pushback. Notable: proposed for
   a residential neighborhood with deep roots in the city's **African American
   and Vietnamese American communities** — advocates explicitly framed this as
   an **environmental-justice** issue, arguing the neighborhood has "long
   shouldered a disproportionate share of industrial and environmental burden."
   Triggered a **New Orleans City Council 6-0 vote for a one-year moratorium**
   on new data center development (Jan 2026), with Council President JP
   Morrell noting the city doesn't even have data centers defined in its
   zoning ordinance yet.
   ([Verite News via search summary](https://veritenews.org/2026/01/28/data-centers-ban-new-orleans-council/);
   [WWNO](https://www.wwno.org/economy/2026-01-29/new-orleans-city-council-bans-data-center-development-for-a-year-heres-why))

**Broader pattern, not just Louisiana:** at least 11 states have passed data
center moratoriums; nationwide polling shows skepticism about data
centers/AI development "across party lines and age brackets"
([technical.ly](https://technical.ly/civics/data-center-world-opposition-concerns/)).
Louisiana legislature has 24+ AI-related bills filed this session. A common
thread across all three LA projects: **secrecy** — NDAs kept residents and
some officials unaware of the Meta deal until an October 2024 Entergy filing
became public.

## Candidate theoretical frames (pick one primary chain, not all of these)

The recurring shape in Britton's other work is antecedent → psychological
mediator → downstream outcome, with a moderator that reshapes the relationship
(see `user_research_corpus.md`). Several candidates fit that same shape here:

- **Environmental justice / distributive justice** — is the burden (water,
  energy, land, noise, health risk) falling disproportionately on communities
  that already carry other industrial burdens? Directly evidenced in the New
  Orleans East case, not a theoretical reach.
- **Procedural justice** — were residents informed and consulted before the
  deal was finalized, or presented with a fait accompli under NDA? The
  secrecy angle is the strongest, most concrete manipulable variable across
  all three LA cases.
- **Psychological reactance (Brehm, 1966)** — same construct already in the
  Tariff Paper's frame; applies naturally to an outside corporation imposing
  a resource-intensive facility without community consent.
- **Risk perception / psychometric paradigm (Slovic)** — "dread risk" (health,
  environmental harm) and "unknown risk" (opaque AI/data-center technology)
  both plausible drivers of opposition independent of actual harm.
  distinguishes emotional/dread-based opposition from analytic/cost-based
  opposition — could be a useful mediator split.
- **Resource scarcity / commons dilemma** — water and grid capacity framed as
  shared, finite local resources being appropriated by an outside firm.
- **Place attachment / solastalgia** — disruption to community identity and
  sense of place, especially relevant to the New Orleans East case's framing
  of "deep roots" in the neighborhood.

**Strongest candidate primary model** (mirrors the Tariff Paper's structure
closely enough to reuse a lot of the same instrument-development playbook):

Framing of the announcement (transparent/community-consulted vs.
secretive/imposed) **→** perceived procedural injustice / distributive
unfairness **→** trust in company and/or local government **→** opposition
intention (support for moratorium, protest/activism intention, political
voting intention), **moderated by** community environmental-justice history
(prior industrial burden) or by perceived necessity (AI/tech is seen as
inevitable vs. optional).

This is a proposal, not a lock — flagging it because it would let Study 2
reuse much of the Tariff Paper's measurement/analysis approach (fairness →
trust → downstream intention chain, PLS-SEM), which is presumably part of why
"milking all three threads similarly" appeals.

## Candidate Study 1 designs (this is the actual open decision)

Two different corpus types would produce two different kinds of Study 1,
matching the Tariff-vs-CCS split already established in
`AI_Assisted_TA_Shared_Method.md`:

**Option A — corporate/official messaging analysis (Tariff-paper-style).**
Corpus: company and government announcements, press statements, PILOT-deal
filings. Method label: AI-assisted thematic/content analysis of corporate
messaging. Builds a typology of *how firms frame* these projects (economic
development, job creation, "clean" energy claims, etc.) — parallels Tariff's
Theme 2 (causation attribution) almost exactly, just for benefit-framing
instead of cost-attribution.

**Option B — public/resident discourse analysis (CCS-paper-style,
netnography).** Corpus: public comment testimony, news-quoted resident
statements, advocacy group communications (Alliance for Affordable Energy,
Union of Concerned Scientists), social media discourse. Method label:
AI-assisted netnography (Kozinets & Seraj-Aksit 2024 precedent, already in
the shared-method doc). Builds a typology of *objection frames* people
actually use — this is the more direct read of "people seem to dislike them"
and would surface real language for Study 2 vignette/survey items the same
way Nike/Mattel's actual quotes grounded Tariff's vignettes.

**Option C — both, paired** (mirrors dual entitlement's inherent two-sided
structure: what companies claim they're entitled to do vs. what the public
judges as fair) — heavier lift, but the most theoretically complete, and
would let Study 1 itself report a framing-mismatch finding (e.g., companies
emphasize jobs/investment; residents emphasize water/secrecy/justice) that's
publishable groundwork on its own before Study 2 even runs.

## What's needed to move this forward

1. Britton picks a Study 1 corpus option (A/B/C above) — same kind of call he
   made 2026-08-04 for Tariff's Study 2 design.
2. Confirm which theory frame(s) to lead with — environmental justice and
   procedural justice/secrecy are the two best-evidenced by the real cases
   found so far; reactance and risk-perception are more speculative until a
   corpus is actually coded.
3. Once a direction is picked, this follows the same six-phase protocol as
   Tariff/CCS — see `Study1_AI_Thematic_Analysis_Publishable_Protocol.md`.
4. Target venue not yet considered — worth a look at JCM (same special issue
   the Tariff Paper targets explicitly names "consumer responses to global
   disruptions," and AI/data-center backlash arguably fits), or a
   sustainability/CSR-adjacent outlet given the environmental-justice angle.
