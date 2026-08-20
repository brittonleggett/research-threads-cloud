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

## 2026-08-16 — fleshing out idea #4 (AI-assisted research workflows methods paper) (WebSearch
this session; WebFetch tested against `www.dce.louisiana.gov` and returned `EGRESS_BLOCKED`
again — fifth consecutive session across the repo's notes counting tonight's CCS_PAPER check;
a direct Bash `curl` fallback also failed with a proxy 403, so this is session-wide network
egress, not a WebFetch-specific limit. Below is WebSearch-summarized, leads not primary-verified.)

### 4a. Not "does AI help thematic analysis" (saturated) — "autonomous scheduled agents as
qualitative-research infrastructure, with human-gated interpretive authority" (open)
- **Gap/question:** the existing AI-assisted-TA literature (see
  `Claude_Knowledge/AI_Thematic_Analysis_Reading_List.csv` — GAATA/Jayawardene & Ewing 2026,
  Epp & Humphreys 2025, Lazarus et al. 2026, a dozen others) is uniformly about a researcher
  sitting down with an LLM chat interface for a bounded coding session. None of it documents
  what this repo's own nightly-rotation setup actually is: a *scheduled, autonomous* agent that
  runs unattended overnight across *multiple concurrent research projects*, with no per-run
  human prompting, whose outputs are version-controlled (git commits as a literal, timestamped
  audit trail of every AI-authored change) and whose interpretive authority is explicitly and
  structurally bounded (Phase 3 theme-finalization is coded as off-limits in this repo's own
  README, not just a norm the researcher tries to remember). That's a different object than
  "I used ChatGPT to help code my interviews" — it's an operations/infrastructure question:
  what does it take to run AI-assisted qualitative research *as an unattended pipeline* across
  a real, live multi-study program, and what governance does that require that a single-session
  tool doesn't?
- **Why tractable soon, and genuinely self-evidenced:** this project has real data most authors
  attempting this paper would have to construct artificially. As of tonight there are 4 nightly
  `OVERNIGHT_SUMMARY_*.md` files, per-project dated `notes/` directories, and a git history
  spanning multiple weeks across three simultaneous qualitative-coding projects (TARIFF, DATA
  CENTER, CCS) — a naturally-occurring case study, not a designed experiment, which is honest
  framing for a methods/reflexivity piece rather than a validation study. Concrete material
  already sitting in this repo's own history that a paper could analyze directly: (1) a documented
  failure-recovery incident (`c5ab89b "Manually recover stranded 2026-08-13 nightly-run work"`)
  showing what breaks when unattended runs fail partway and how provenance let it be reconstructed;
  (2) a documented tooling-outage pattern (WebFetch egress-blocked five sessions running, each one
  logged with its exact failure mode rather than silently worked around) — a real example of a
  system transparently reporting its own degraded-confidence state instead of masking it;
  (3) the rotation logic itself (priority-queue-across-projects, "recheck actual state rather than
  mechanical order") as a designed policy for resource allocation across a multi-study program,
  something individual-session AI-TA papers don't need to solve at all.
  A quick check tonight (WebSearch) confirms this angle isn't already claimed: the closest existing
  work is either single-session AI-assisted-TA validation (the whole Tier 1-5 reading list) or
  autonomous-agent-for-research papers in *quantitative*/computational science (e.g., an ML-research
  agent pipeline documenting failure modes, a physics corpus-to-manuscript pipeline) — none framed
  around *interpretivist, human-gatekept* qualitative social-science work specifically. That's the
  open seam.
- **Rough method sketch:** likely an autoethnographic/reflexive methods paper (the researcher
  studying his own AI-research infrastructure), not a between-subjects validation study — closer
  in genre to Paulus, Lester & Davis 2026's discourse-analysis-of-the-field piece (already in the
  reading list) than to GAATA's accuracy-benchmarking design. Candidate structure: (1) describe the
  pipeline and its governance rules as a case; (2) systematically code the repo's own git history
  and nightly summaries as data — what kinds of errors occurred, what the human-gate (Phase 3,
  judgment-call flagging) actually caught vs. missed, how tooling failures were surfaced vs.
  silently absorbed; (3) discuss implications for qualitative-research trustworthiness criteria
  (dependability, confirmability — same five criteria from Lazarus et al. 2026) when the "who did
  this coding pass" question includes an unattended, scheduled process rather than only a present
  researcher.
- **Target venue:** *International Journal of Qualitative Methods* (where much of the existing
  reading list already sits — Lazarus, Xu, Misra et al., Cheah, Naeem et al.) is the natural fit
  given the field's own venue; *Organizational Research Methods* or *AI & Society* (companion to
  Paulus, Lester & Davis 2026) are plausible alternates if the framing leans more toward
  research-operations/governance than qualitative-methods-specifically.
- **Honest caveat, not a decision:** this paper is *about* Britton's own workflow and this repo's
  own history — meaning it would require him to decide how much of the actual pipeline/process
  (not the underlying substantive research, which stays untouched) he's comfortable describing in
  a public methods paper, and there's a bootstrapping question (is 2-3 weeks of one researcher's
  pipeline history enough of a "case" to publish, or does it need more runtime first). Flagging
  both for Britton rather than assuming either answer. Proposal only, nothing built.
- Leads (unverified, WebSearch only): [Jayawardene & Ewing 2026, GAATA](https://journals.sagepub.com/doi/10.1177/14707853251405043), [autonomous ML-research-agent failure modes survey](https://arxiv.org/pdf/2607.02329) (computational-science analog, not qualitative), [PaperClaw — agentic research with human-in-the-loop refinement](https://arxiv.org/pdf/2606.22610) (same computational-science-not-qualitative caveat)

## 2026-08-20 — nightly scouting run (WebSearch this session; WebFetch tested against
`lailluminator.com` and returned `EGRESS_BLOCKED` again — same network-wide egress-proxy failure
mode logged every session since 08-13. Below is WebSearch-summarized, leads not primary-verified.)

### 5. Louisiana's nuclear fuel-cycle buildout — a new, distinct energy-siting-opposition object
(not a data-center restatement)
- **Gap/question:** in July 2026 the U.S. Department of Energy shortlisted Louisiana (one of five
  states) for a federal "Nuclear Lifecycle Innovation Campus," and the state's own pitch proposes
  three geographically distinct hubs: Baton Rouge (uranium enrichment, leveraging existing
  petrochemical/LSU infrastructure), Northwest Louisiana (SMR/microreactor deployment, explicitly
  to power data centers), and Port Fourchon (a research station exploring offshore salt-dome
  storage of high-level nuclear waste under the Gulf of Mexico). This is a materially different
  opposition object from DATA_CENTER_PAPER's facility-siting fights or CCS_PAPER's underground-
  injection framing: it bundles three infrastructure types with three different risk-perception
  logics (industrial enrichment, reactor siting, waste storage) under one federal selection, and
  the waste-storage piece specifically revives a *dormant, previously-settled* controversy — Bayou
  Corne's 2012 salt-dome sinkhole disaster — that Louisiana law (RS 30:2117) currently addresses by
  banning radioactive waste in *state-territory* salt domes, with the federal-waters siting at Port
  Fourchon read by advocates as an explicit loophole around that state law. That "state law says no,
  offshore siting routes around it" framing is a sharper procedural-legitimacy hook than most of
  the existing corpus has.
- **Why tractable soon:** live and moving fast, not retrospective — federal MOU announced Jul 29
  2026; the Louisiana Public Service Commission is separately voting Sept 16 2026 on a "nuclear
  tariff" (a 20-cent/month fee on Entergy Louisiana/Cleco/SWEPCO bills to fund SMR feasibility
  studies), which Commissioner Davante Lewis has already publicly objected to on cost-shifting
  grounds ("utility companies should pay for their own research") — a live vote with a fixed date
  gives this a natural before/after data point. Jackson Voss of the Alliance for Affordable Energy
  (the same advocacy group already sourced in this file's 1a entry) is on record specifically
  invoking Bayou Corne on the waste-storage piece, meaning the opposition-actor network is already
  partly the same one Britton's Data Center/ratepayer work tracks — a low-cost extension, not a
  cold start. Note the tariff-funding mechanism overlaps with 1a's ratepayer-fairness framing, but
  the siting/waste-storage risk-perception piece is genuinely new territory 1a doesn't cover.
- **Rough method sketch:** Study 1 (AI-assisted thematic analysis) of LPSC docket comments on the
  nuclear tariff proceeding, Bayou Corne-referencing public comment/news discourse, and DOE
  campus-selection coverage; Study 2 (PLS-SEM) candidate chain: risk-perception/trust-in-regulator
  as mediator between siting-transparency (procedural justice) and opposition intention, with
  prior-disaster salience (Bayou Corne recall) as a plausible moderator — fits Britton's standard
  mediated-antecedent → psychological-mediator → outcome template directly.
- **Target venue:** Journal of Public Policy & Marketing (same candidate as Data Center/CCS) given
  the shared regulatory-body-as-central-actor framing, or Energy Research & Social Science if
  Britton wants it positioned as energy-policy rather than marketing-adjacent.
- Leads (unverified, WebSearch only): [Louisiana Illuminator — feds pick Louisiana for nuclear campus](https://lailluminator.com/2026/07/29/louisiana-nuclear-campus/), [KPLC — state responds to nuclear waste disposal concerns](https://www.kplctv.com/2026/07/30/state-responds-concerns-over-nuclear-waste-disposal-plan/), [Louisiana Illuminator — "nuclear tariff" on power bills](https://lailluminator.com/2026/08/13/nuclear-tariff/), [Yahoo News — Louisiana wants to store nuclear waste under Gulf of Mexico](https://www.yahoo.com/news/politics/articles/louisiana-wants-store-nuclear-waste-003044072.html), [RS 30:2117 — LA law banning radioactive waste in salt domes](https://law.justia.com/codes/louisiana/revised-statutes/title-30/rs-30-2117/)

### 6. Agentic AI commerce delegation — a new consumer-marketing-behavior chain, not a restatement
of the tariff/private-label idea (2a)
- **Gap/question:** as AI shopping agents move from product-research assistants to agents capable
  of executing purchases, 2026 industry surveys show a sharp split between *researching* and
  *delegating*: consumers report surprisingly high trust in AI agents generally (Accenture's 2026
  Consumer Pulse, n=25,590 across 16 countries, found 74% would trust a personal AI agent more than
  their best friend to make a purchase for them) but sharply constrain what they'll actually hand
  over — only 32% would let an agent choose within a set budget/brand, just 9% are open to fully
  autonomous purchasing including payment. Accenture frames this as a "delegation dial" that varies
  by product category and stakes, not a single trust construct. That gap between stated general
  trust and category-specific delegation willingness is exactly the kind of construct a mediation
  model is built for, and it's currently unclaimed academically: a search for PLS-SEM or other
  academic treatments of AI-agent purchase delegation turned up only industry/consultancy reports
  (Accenture, McKinsey, Checkout.com, Alchemer) — no peer-reviewed marketing paper yet modeling
  delegation willingness as an outcome with trust/perceived-risk as mediators.
- **Why tractable soon:** the surveys are recent (Accenture's report published Jun 2026, an
  Alchemer 2026 retail report separately found "AI adoption outpaces consumer trust," and 86% of
  U.S. online shoppers who used AI for product research say they still verify the AI's
  recommendation elsewhere before buying) — meaning there's already a public evidence base to build
  a lit review and hypotheses from even before Britton runs his own instrument, and the topic is
  moving fast enough that a paper submitted in the next few months would be genuinely current rather
  than late to the conversation.
- **Rough method sketch:** experimental/survey design closer to 2a's sketch than to the TA-based
  papers — manipulate agent type (fully autonomous vs. confirm-before-purchase vs. research-only)
  and/or product category (low-stakes/routine vs. high-stakes/considered purchase) in a vignette,
  measure delegation willingness as the outcome, with perceived trust and perceived risk/loss-of-
  control as competing or serial mediators, transparency/override-ability as a plausible moderator
  (Accenture's own data flags override options and permission granularity as trust conditions).
  PLS-SEM fits directly if run as a survey-based model instead of a vignette experiment.
- **Target venue:** Journal of Consumer Marketing or Journal of Retailing and Consumer Services —
  genuinely distinct from both TARIFF_PAPER and 2a (different antecedent entirely: agent-type/
  category, not tariff-attribution framing), so not a competing use of the same design.
- Leads (unverified, WebSearch only): [Accenture — consumers show growing trust in AI shopping agents](https://www.artificialintelligence-news.com/news/ai-shopping-agents-consumer-trust-accenture-report/), [Checkout.com — consumer demand for AI shopping vs. trust catching up](https://www.checkout.com/newsroom/consumer-demand-for-ai-shopping-is-forming-fast-but-trust-for-agentic-commerce-is-still-catching-up), [Alchemer — 2026 Retail Report: AI adoption outpaces consumer trust](https://www.alchemer.com/resources/benchmark-report/2026-retail-report-ai/), [Chain Store Age — Accenture: customers trust AI agents to perform these tasks](https://chainstoreage.com/accenture-customers-trust-ai-agents-perform-these-tasks-them)

Both proposals only, per standing rule — nothing built, nothing committed to. Note: real-time
crime center (RTCC) expansion was also searched tonight as a candidate new Louisiana-surveillance
angle (Ouachita Parish, Lafayette Parish, Baton Rouge, New Orleans all now running RTCCs bundling
ALPR with broader camera networks), but this reads as corpus-extension material for the already-
active FLOCK_CAMERAS_PAPER rather than a distinct new paper idea, so it wasn't written up as a
standalone entry here — flagging for whoever next works FLOCK_CAMERAS_PAPER instead.
