# Research Stream Ideas — Scouting Log

Running file, append-only, dated entries. Per the nightly-rotation convention in the root
`README.md`: this is scouting, not commitment. Nothing here should turn into a built corpus or
locked design without Britton greenlighting it first.

**Recovery note (2026-08-13):** the two nightly-routine runs that generated these ideas both
lost their full write-ups when their containers couldn't push (see `OVERNIGHT_SUMMARY_2026-08-13.md`
for the full story). These are one-line recreations of the ideas themselves, not the original
fuller reasoning/sourcing behind each — treat as titles to revisit, not fleshed-out proposals.

## 2026-08-13 — from the 1:07am run

1. **Ratepayer cost-shifting fairness** — Louisiana's data-center power buildout, looked at
   through who bears the cost (ratepayers vs. data-center operators), distinct from
   DATA_CENTER_PAPER's existing backlash/opposition angle.
2. **Tariff-driven brand/private-label switching** — a consumer-response angle adjacent to but
   distinct from the existing Tariff Paper studies.

## 2026-08-13 — from the afternoon test run

3. **LNG-terminal community opposition (Cameron Parish, LA)** — same real-world-grounded logic
   as the Data Center paper, different infrastructure type.
4. **AI-assisted research workflows as a methods paper in its own right** — a possible
   standalone contribution documenting the AI-assisted thematic-analysis method itself, rather
   than just using it as a tool within the substantive papers.

## 2026-08-14 — fleshing out two of the above with real evidence (WebSearch this session; WebFetch
was network-blocked all session, so nothing below is a directly-fetched primary source — treat
sourcing as leads to verify, same caveat as the TARIFF_PAPER notes from tonight)

### 1a. Ratepayer cost-shifting fairness (Louisiana data centers) — now has real, current material
- **Gap/question:** who bears the cost of data-center-driven grid buildout — ratepayers vs.
  operators — and how do Louisianans perceive the fairness of that allocation, distinct from
  DATA_CENTER_PAPER's opposition/backlash framing (which is about resistance to the facilities
  existing at all, not about who pays for the grid).
- **Why tractable soon:** this is an *active, unresolved* policy fight, not a retrospective one —
  a Union of Concerned Scientists report (April 2026) projects data centers could add up to $26B
  in wholesale electricity costs and $90B in health/climate damages over 15 years; Gov. Landry
  signed an executive order in June 2026 explicitly aimed at protecting ratepayers from
  data-center costs, but UCS's follow-up coverage argues Louisiana's actual PSC policy still
  allows more cost pass-through, not less. There's a concrete example to anchor coding: Meta's
  Richland Parish deal has Meta paying for turbines but Entergy customers absorbing $550M in
  transmission-line costs. This is a live fairness controversy with a policy body (LPSC) actively
  deciding, which is a strong hook for a marketing/public-policy framing right now.
- **Rough method sketch:** likely the same Study1 (AI-assisted thematic analysis of public
  discourse/comment) → Study2 (PLS-SEM survey, perceived fairness/distributive justice as
  mediator) template already used across the three existing papers. Corpus candidates: LPSC
  docket comments, news coverage (nola.com, Louisiana Illuminator, The Lens, AAE Alliance for
  Affordable Energy), the UCS report itself as a framing/statistics source (not corpus).
- **Target venue:** Journal of Public Policy & Marketing (same as DATA_CENTER_PAPER's current
  leading candidate) — could be a companion piece or, if Britton wants separation, Journal of
  Consumer Affairs given the ratepayer/consumer-protection angle.
- Leads (unverified, WebSearch only): [UCS report coverage, The Lens](https://thelensnola.org/2026/04/21/louisiana-data-centers-energy-costs-ai-electricity-bills/), [Louisiana Illuminator — Landry order](https://lailluminator.com/2026/06/26/landry-order-data-power/), [nola.com — Entergy $30B grid expansion](https://www.nola.com/news/entergy-growth-ratepayer-cost-data-center/article_1c99dffb-a2b1-4230-a467-e9c6c2fc70d6.amp.html), [UCS blog — LPSC policy critique](https://blog.ucs.org/paul-arbaje/louisianas-new-policy-allows-even-more-data-center-costs-to-be-passed-to-ratepayers/)

### 2a. Tariff-driven brand/private-label switching — now has survey-level evidence to point to
- **Gap/question:** does tariff-attributed (vs. generic inflation-attributed) price framing
  specifically accelerate private-label switching, and does that effect persist after tariffs
  ease — i.e., is tariff messaging creating a *sticky* behavioral shift rather than a temporary
  one? This sits naturally alongside TARIFF_PAPER's existing causation-attribution focus (how
  companies frame *why* prices rose) but asks the consumer-response question TARIFF_PAPER's
  current design doesn't: does the causation frame change switching behavior, not just attitudes.
- **Why tractable soon:** search surfaced a 2026 survey finding 60% of U.S. consumers say
  they'd stop buying a favorite brand over tariff-driven price increases, and 48% would consider
  switching to private label — plus industry reporting (Circana, Simon-Kucher) describing this
  private-label shift as "sticking" rather than reverting, which is exactly the kind of
  persistence claim that's testable and citable. eMarketer's framing ("tariffs will shape
  consumer behavior long after policy shifts fade") is a good literature-anchor phrase to check
  against primary eMarketer content once fetching works again.
- **Rough method sketch:** experimental (vignette) design fits better than TA here — manipulate
  cause-attribution framing (tariff-specific vs. generic "rising costs") in a mock price-increase
  scenario, measure brand-switching intention/private-label consideration, test a
  perceived-fairness or perceived-permanence mediator. Could reuse TARIFF_PAPER's Study 2
  instrument-design infrastructure (see `notes/2026-08-04-full-instrument-assembly.md`) as a
  starting point rather than building from scratch.
- **Target venue:** Journal of Consumer Marketing or Journal of Retailing — a genuinely distinct
  paper from TARIFF_PAPER's current JCM submission (different DV, experimental not TA-based), not
  a competing use of the same design.
- Leads (unverified, WebSearch only): [Statista — brand-purchase change due to tariffs](https://www.statista.com/statistics/1560133/brand-purchase-change-due-to-tariffs-price-hike-us/), [Circana — private label trends](https://www.circana.com/post/4-consumer-trends-shaping-the-future-of-private-label), [eMarketer — tariffs and long-term consumer behavior](https://www.emarketer.com/content/tariffs-will-shape-consumer-behavior-long-after-policy-shifts-fade), [Orchard Insights](https://hello.orchard-insights.com/blog/how-inflation-and-tariffs-are-reshaping-consumer-choices)

Both of these are still proposals, not commitments — flagging for Britton to greenlight, per
standing rule. Neither has a corpus, survey, or design built yet.

## 2026-08-15 — fleshing out idea #3 (LNG-terminal opposition, Cameron Parish) with real
evidence (WebSearch this session; WebFetch was `EGRESS_BLOCKED` again tonight — third
consecutive session, see this date's TARIFF/DATA_CENTER notes and the summary for the
same caveat — treat sourcing as leads to verify, not primary-source-confirmed)

### 3a. LNG-terminal community opposition (Cameron Parish, LA) — now has real, current material
- **Gap/question:** how do Cameron Parish residents and advocacy groups frame opposition to
  the parish's LNG export buildout (six projects proposed/approved/operating), and does that
  framing pattern-match the same justice/procedural-exclusion/infrastructure-strain themes
  already emerging in DATA_CENTER_PAPER's corpus, or produce a distinct typology specific to
  heavy industrial/energy-export infrastructure vs. data centers.
- **Why tractable soon:** this is live, not retrospective — a Delfin LNG pipeline rupture
  released 56 million cubic feet of gas (ignited, ejected pipe fragments) this year; Venture
  Global is seeking a permit to discharge Calcasieu Pass 2 wastewater into the Calcasieu Ship
  Channel over resident objection; Venture Global separately sought a two-year closure of a
  local road for construction, drawing opposition over traffic/emergency-response strain on a
  two-lane highway; a judge ruled a Commonwealth LNG permit ignored potential climate impacts;
  Commonwealth LNG's contested permit is now in a public-comment period despite ongoing legal
  challenges. Existing long-form journalism already exists to mine (Louisiana Illuminator's
  "What Happened When an LNG Giant Came to Town," also republished at Inside Climate News;
  The Lens's "Cameron Parish is a constant warning, not an exception") — meaning a corpus for
  this could be built relatively fast if greenlit, since the deep-dive sourcing legwork is
  partly already done by others.
- **Rough method sketch:** same Study 1 (AI-assisted netnography/discourse analysis) → Study 2
  (PLS-SEM) template as the other three papers. Corpus candidates: the Illuminator/Inside
  Climate News/The Lens long-form pieces, Commonwealth LNG public-comment docket entries once
  that period is public, wastewater-discharge-permit comment record. Natural theory overlap
  with DATA_CENTER_PAPER's candidate frames (procedural justice, distributive/environmental
  justice, infrastructure strain) — worth explicitly deciding whether this is a fourth
  standalone paper or a comparative extension within DATA_CENTER_PAPER (energy-export
  infrastructure vs. AI infrastructure, same opposition grammar or not) rather than building
  it as a fully separate thread by default.
- **Target venue:** same candidates as DATA_CENTER_PAPER (Journal of Public Policy &
  Marketing) given the shared infrastructure-controversy angle, or an energy-policy-adjacent
  outlet if Britton wants it kept separate from the data-center thread specifically.
- Leads (unverified, WebSearch only): [Louisiana Illuminator — "What Happened When an LNG Giant Came to Town"](https://lailluminator.com/2026/07/05/venture-global-3/), [Inside Climate News — same piece, syndicated](https://insideclimatenews.org/news/28062026/venture-global-lng-terminals-in-cameron-louisiana/), [The Lens — Cameron Parish as warning](https://thelensnola.org/2026/02/26/dying-tired-communities-cameron-parish-is-a-constant-warning-not-an-exception-to-the-dangers-of-lng/), [Louisiana Illuminator — wastewater discharge fight](https://lailluminator.com/2026/06/03/lng-wastewater/), [Louisiana Illuminator — Commonwealth LNG reapproval](https://lailluminator.com/2025/12/04/commonwealth-lng/), [American Press — Commonwealth LNG public comment](https://americanpress.com/2026/07/08/public-comment-begins-for-contested-commonwealth-lng-permit/)

Still a proposal only, per standing rule — nothing built, nothing committed to. Idea #4
(AI-assisted-research-workflows methods paper) remains an unfleshed one-line title from
2026-08-13 — not reached tonight, next in the scouting queue.
