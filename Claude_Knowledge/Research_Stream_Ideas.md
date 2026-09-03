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

## 2026-08-21 — nightly scouting run (WebSearch this session; WebFetch confirmed `EGRESS_BLOCKED`
again tonight — 10th straight session with this failure mode. Below is entirely WebSearch-
summarized, leads not primary-verified.)

### 7. Tariff-surcharge non-reversal after the Supreme Court's IEEPA ruling — perceived corporate
opportunism as a trust-erosion mechanism (new, well-evidenced, distinct from both TARIFF_PAPER's
Study 1 and idea 2a)
- **Gap/question:** the Supreme Court struck down Trump's IEEPA-based tariffs 6-3 on Feb 20 2026
  (Roberts writing, Gorsuch/Barrett joining in full, Sotomayor/Kagan/Jackson in part; Thomas/
  Kavanaugh/Alito dissenting); all IEEPA tariffs terminated Feb 24 2026, and the Court of
  International Trade ordered CBP on Mar 4 2026 to liquidate/re-liquidate entries without the now-
  illegal duties, opening ~$166B in refund claims from 330,000+ companies. That created a clean,
  real natural experiment TARIFF_PAPER's existing design doesn't use: companies had spent a year-plus
  telling consumers tariffs were *why* prices rose (the causal-attribution framing TARIFF_PAPER's
  Study 1 already codes); now the stated cause is legally gone, and reporting through mid-2026 (a
  Modern Retail piece specifically headlined "online merchants aren't lowering prices despite Supreme
  Court ruling," a Forbes/Danziger piece titled "Consumers Won't See Tariff Refunds") confirms most
  retailers simply didn't roll prices back. That's a distinct question from both existing entries:
  not "how do companies frame the cause of a price increase" (TARIFF_PAPER Study 1) and not "does
  tariff-attributed framing accelerate switching" (idea 2a) — this is "what happens to trust/loyalty
  when the stated justification is publicly invalidated and the price doesn't move," a broken-promise/
  attribution-of-blame dynamic with its own literature hook (asymmetric "rockets and feathers"
  pricing — well-established in economics, prices rise fast and fall slow — but with no marketing-
  journal PLS-SEM treatment found tying it to this specific 2026 event).
- **Why tractable soon:** the natural experiment has fixed, verifiable dates (Feb 20/24, Mar 4 2026)
  and is still live as of this search — meaning a survey or vignette fielded now captures salient,
  current behavior rather than recalled or hypothetical scenarios. Industry commentary is already
  using almost exactly the attribution-theory framing a mediator model would need: one piece states
  plainly that "without transparency, consumers will interpret price increases as retailer
  opportunism," and that consumers "may assume companies kept the benefit if they believe tariffs
  fell and prices did not" — that's the perceived-opportunism mediator, industry-observed but not yet
  academically modeled. Separately, a Statista-sourced 2026 stat (60% of US consumers say they'd stop
  buying a favorite brand over tariff-driven price hikes, 53% would switch to generic) and a
  RetailWire piece (85% of consumers believe brands use inflation as a "scapegoat" for price hikes)
  give a lit-review base to build from immediately. A WebSearch check for an existing PLS-SEM or
  academic marketing study on tariff-surcharge non-reversal / post-ruling price stickiness came back
  empty — only consultancy pulse reports (Simon-Kucher, PIIE) and news coverage, no peer-reviewed
  treatment, which given how recent the ruling is (six months old) reads as genuinely open rather than
  a search-quality artifact.
- **Rough method sketch:** fits Britton's antecedent→mediator→outcome template directly. Antecedent:
  price non-reversal / awareness that the stated tariff justification was legally invalidated
  (measured as an individual-difference variable in a survey design, or manipulated as
  rolled-back-vs-not in a vignette experiment). Mediator: perceived corporate opportunism/attribution
  of blame (adaptable from attribution-theory scales already likely reviewed for TARIFF_PAPER).
  Outcome: trust erosion, boycott intention, negative WOM. Plausible moderator: price transparency
  (whether the retailer itemized a "tariff surcharge" line vs. folded it into list price — Amazon-
  seller and DTC-brand behavior reportedly varies here) or political attentiveness/awareness of the
  ruling itself. Survey-based PLS-SEM is the more natural fit than a full experiment given the need to
  measure real awareness of a real event rather than induce it artificially.
- **Target venue:** Journal of Consumer Marketing — same target as TARIFF_PAPER's main paper, and this
  reads as a natural companion/follow-on piece rather than a competing use of the same corpus (different
  DV, post-ruling timeframe, trust/attribution focus vs. TA-based messaging-framing focus). Journal of
  Public Policy & Marketing is a plausible alternate given the live price-gouging political salience
  (Warren/DeLauro FTC letters already treat this as a policy question, not just a marketing one).
- Leads (unverified, WebSearch only): [WilmerHale — Supreme Court strikes down IEEPA tariffs](https://www.wilmerhale.com/en/insights/client-alerts/20260220-supreme-court-strikes-down-ieepa-tariffs-what-now), [Modern Retail — online merchants aren't lowering prices despite ruling](https://www.modernretail.co/operations/marketplace-briefing-online-merchants-arent-lowering-prices-despite-supreme-court-ruling/), [Forbes/Danziger — consumers won't see tariff refunds](https://www.forbes.com/sites/pamdanziger/2026/04/29/consumers-wont-see-tariff-refunds-smart-retailers-will-turn-them-into-price-cuts/), [NPR — companies line up for refunds](https://www.npr.org/2026/02/21/g-s1-110987/supreme-court-tariffs-refunds), [RetailWire — 85% believe brands use inflation as scapegoat](https://retailwire.com/discussion/consumers-brands-inflation-scapegoat/), [Statista — brand-purchase change due to tariffs](https://www.statista.com/statistics/1560133/brand-purchase-change-due-to-tariffs-price-hike-us/), [Warren/DeLauro FTC price-gouging letter](https://www.warren.senate.gov/imo/media/doc/trump-tariff-price-gouging-letter.pdf)

### 8. AI-generated misinformation as a driver of rural Louisiana solar-farm siting opposition
(moderate confidence — genuine gap exists but narrower than idea 7; adjacent academic literature
already exists)
- **Gap/question:** Louisiana has several live 2026 parish-level solar-siting fights (Entergy's
  Cypress Harvest Solar in Iberville Parish; a ~4,700-acre project near Moss Bluff in Calcasieu
  Parish drawing opposition from a state representative; Iberia Parish's solar moratorium/setback
  ordinance) and a new statewide law (HB 459, mandating 300-ft residential setbacks for solar
  projects ≥75 acres, with room for parishes to go further). Reporting from this week specifically
  (Daily Yonder/WXPR, Aug 13 2026; Planetizen, Aug 2026; The Lens, Jun 2026) frames a chunk of the
  opposition as fueled by AI-generated "slop" — fabricated graphics and claims (cancer risk, soil
  poisoning, property-value collapse, even "homegrown tornadoes") circulating on social media, not
  organic grassroots concern alone. That's a genuinely different antecedent than the rest of Britton's
  siting-opposition line (Data Center, LNG, nuclear are all about corporate/government actors and
  procedural/distributive justice) — here the opposition-generating mechanism is a content-generation
  technology itself, which also ties to Britton's AI-methods interest, though as a stimulus/subject
  rather than as his usual research tool.
- **Saturation check (real, not hand-waved):** a WebSearch specifically for prior academic work on
  AI-generated misinformation and renewable-energy opposition found this is *not* a blank slate — a
  2026 Scientific Reports/PMC study already examines whether GenAI dialogue can dispel wind-farm
  misinformation, and a ScienceDirect longitudinal study already covers conspiracy belief and wind-
  farm opposition. Both are wind-specific (not solar) and frame GenAI as a countermeasure/dialogue
  partner rather than as the misinformation source itself, and neither is marketing-journal-framed
  with a PLS-SEM design, nor Louisiana-specific — so there's a real opening (solar, AI-as-source not
  AI-as-cure, marketing/PLS-SEM framing, Louisiana's live multi-parish fights and new state law) but
  it's a narrower, more contested opening than idea 7, not a clean unclaimed space.
- **Rough method sketch:** Study 1 (AI-assisted content analysis, if a corpus of the actual circulating
  graphics/claims and parish-meeting testimony can be assembled) to build a claim-type typology across
  the Iberville/Calcasieu/Iberia fights; Study 2 (experimental vignette) manipulating attributed source
  of an anti-solar claim (AI-generated vs. traditional/human-authored, holding claim content constant),
  measuring perceived source credibility and risk perception as mediators, opposition intention as the
  outcome, rural/agricultural identity or trust-in-local-vs-outside-information as a moderator.
- **Target venue:** Energy Research & Social Science reads as the best fit given the misinformation-
  plus-energy-siting specificity and that outlet's precedent for exactly this kind of study; Journal of
  Public Policy & Marketing is a plausible alternate if pitched as a policy-communication problem, but
  this is civic/political opposition rather than purchase behavior, so a pure consumer-marketing
  journal (JCM) is a weaker fit than for the other entries in this file.
- Leads (unverified, WebSearch only): [Daily Yonder/WXPR — fears amplified by "AI slop" hamper solar boom](https://dailyyonder.com/in-rural-communities-fears-amplified-by-ai-slop-and-social-media-hamper-solar-boom/2026/08/07/), [Planetizen — misinformation and "AI slop" hamstringing rural solar](https://www.planetizen.com/news/2026/08/138179-misinformation-and-ai-slop-are-hamstringing-rural-solar-development), [The Lens — unfounded fears hamper Louisiana's solar boom](https://thelensnola.org/2026/06/30/unfounded-fears-hamper-louisianas-solar-boom/), [WAFB — Iberville Parish residents oppose Entergy solar farm](https://www.wafb.com/2026/07/28/iberville-parish-residents-oppose-entergy-solar-farm-plan-along-hwy-75/), [KPLC — Moss Bluff 4,700-acre solar farm draws opposition](https://www.kplctv.com/2026/08/20/proposed-4700-acre-solar-farm-draws-opposition-state-rep-moss-bluff-residents/), [ScienceDirect — conspiracy belief and wind-farm opposition, longitudinal](https://www.sciencedirect.com/science/article/pii/S0272494425001033), [Nature Scientific Reports — GenAI's potential to dispel wind-farm misinformation](https://www.nature.com/articles/s41598-026-42790-8)

Both proposals only, per standing rule — nothing built, nothing committed to. Idea 7 is the stronger
of the two (clean natural experiment, live fixed dates, no academic treatment found); idea 8 is
genuine but flagged moderate-confidence given real adjacent literature already exists on the
wind-farm side — Britton should weigh whether the solar/Louisiana/marketing-framing gap is enough
distance from that existing work before greenlighting.

## 2026-08-22 — nightly scouting run (WebSearch only this session; did not test WebFetch/egress
tonight, so no fresh confirmation either way on the network issue logged every prior session —
treat sourcing below as WebSearch-summarized leads, not primary-source-verified, consistent with
every prior entry in this file)

### 9. Louisiana shrimp-tariff natural experiment — domestic/provenance branding and consumer
willingness-to-pay (high confidence — sharp Louisiana+tariff crossover, dated real-world hooks,
genuine gap versus older COOL literature)
- **Gap/question:** 2026 brought a concrete, dated tariff shock to Louisiana's shrimp industry —
  the U.S. International Trade Commission's five-year sunset review kept antidumping duties on
  frozen warmwater shrimp from China/India/Thailand/Vietnam in place, new ITC tariffs were placed
  on shrimp from India, Ecuador, Indonesia and Vietnam, and Sens. Cassidy (R-LA) and Hyde-Smith
  (R-MS) reintroduced the India Shrimp Tariff Act in 2026 (a stepped 10%→20%→40% duty on Indian
  shrimp 2026-2028, plus a flat per-kilogram tax on all imported shrimp), with Louisiana lawmakers
  separately petitioning the ITC directly and domestic shrimpers reportedly being paid as little as
  25 cents/lb against cheap imports. The state already has a ready-made branding mechanism to study
  this against — the Louisiana Department of Wildlife and Fisheries' "Certified Louisiana Seafood" /
  Wild Louisiana Seafood Certification Program, an official provenance label consumers can be shown
  directly. The open question: does *this* tariff-and-price-shock episode, layered onto an existing
  domestic-provenance certification consumers can recognize, shift willingness-to-pay and purchase
  intention for certified-local shrimp in a way prior country-of-origin-labeling (COOL) research
  didn't find — older USDA-ERS work on the 2005 seafood COOL mandate found consumers largely
  *indifferent* to origin labels absent a live economic/trade narrative attached to them. This is a
  live economic-distress-plus-tariff narrative COOL's original rollout didn't have, and it crosses
  two of Britton's four adjacent buckets at once (tariffs + Louisiana) rather than just one.
- **Why tractable soon:** the tariff/legislative timeline is dated and current (ITC sunset-review
  ruling and new country-specific tariffs this year, Cassidy/Hyde-Smith bill reintroduced in 2026
  with duties scheduled to step up starting January 2026), giving a live before/after economic
  reference point rather than a hypothetical scenario, and industry advocacy coverage (SeafoodSource,
  Southern Shrimp Alliance, WAFB) describes Q2 2026 as "one of the most active advocacy periods in
  recent memory" for the industry — meaning the framing is actively circulating in Louisiana media
  right now, not something that needs manufacturing. A WebSearch check for existing PLS-SEM or
  marketing-journal treatment of this specific angle (shrimp COOL + tariff-driven WTP) came back
  empty — the closest prior work (a Journal of Agricultural and Applied Economics WTP study on
  "Homegrown by Heroes"/local/BAP shrimp attributes, a China-beef-market COOL/ethnocentrism study,
  the older USDA-ERS indifference finding) uses discrete-choice or hedonic-price methods, not PLS-SEM,
  and none are tied to this year's specific tariff episode — a genuine, not just assumed, gap.
- **Rough method sketch:** fits Britton's antecedent→mediator→outcome template well. Antecedent:
  awareness/salience of the shrimp-tariff narrative (economic-distress-of-domestic-shrimpers framing)
  paired with exposure to the Certified Louisiana Seafood label (could be manipulated in a vignette —
  labeled vs. unlabeled, tariff-narrative-present vs. absent — or measured as awareness in a survey).
  Mediator candidates: consumer ethnocentrism / "support local" sentiment, or perceived authenticity
  of the domestic product. Outcome: willingness-to-pay premium, purchase intention for certified-local
  vs. imported shrimp. Plausible moderator: Louisiana/regional identity strength, or price sensitivity/
  income. Study 1 (AI-assisted thematic analysis) could code Louisiana news/advocacy-group discourse
  (Southern Shrimp Alliance statements, legislator press releases, WAFB/SeafoodSource coverage) for
  how the tariff-and-distress narrative is being framed, before Study 2 (PLS-SEM survey) tests the
  WTP/purchase-intention model — same two-study shape as the other active papers.
- **Target venue:** Journal of Consumer Marketing (companion angle to TARIFF_PAPER, but a distinct
  regional-industry/provenance-branding study rather than the corporate-messaging-attribution focus
  TARIFF_PAPER already has) or Journal of Food Products Marketing / British Food Journal given the
  food-provenance-labeling literature base it would sit alongside; a Louisiana-specific
  economic-development angle could also make Journal of Public Policy & Marketing plausible if
  framed around the certification program itself as policy.
- Leads (unverified, WebSearch only): [The Advocate — Louisiana's shrimping industry faces threats from imports](https://www.theadvocate.com/acadiana/news/business/louisianas-shrimping-industry-still-fighting-to-survive/article_675e6022-2936-4365-bb3d-226253944542.html), [SeafoodSource — LA lawmakers ask ITC to extend antidumping duties](https://www.seafoodsource.com/news/supply-trade/louisiana-lawmakers-ask-international-trade-commission-to-extend-antidumping-duties-on-shrimp-imports), [Southern Shrimp Alliance — India Shrimp Tariff Act](https://shrimpalliance.com/general-tariffs-can-change-india-shrimp-tariff-act-offers-long-term-solution/), [WAFB — Louisiana, Southern shrimpers praise bill targeting hazardous imports](https://www.wafb.com/2026/07/25/louisiana-southern-shrimpers-praise-bill-targeting-hazardous-imports/), [Louisiana Dept. of Wildlife & Fisheries — Wild Seafood Certification Program](https://lwscpadmin.wlf.louisiana.gov/LWSCP/), [The Fish Site — consumers appear indifferent to COOL for shrimp (USDA-ERS)](https://thefishsite.com/articles/consumers-appear-indifferent-to-countryoforigin-labeling-for-shrimp), [Journal of Agricultural and Applied Economics — WTP for shrimp with local/Homegrown-by-Heroes attributes](https://www.cambridge.org/core/journals/journal-of-agricultural-and-applied-economics/article/willingness-to-pay-for-shrimp-with-homegrown-by-heroes-communitysupported-fishery-best-aquaculture-practices-or-local-attributes/9393EE1CE8A05033230323D07A41CF0D)

### 10. AI-answer brand exclusion ("zero-click"/GEO visibility gap) as a consumer-marketing
mechanism (moderate confidence — real, distinct mechanism, but weaker dated hook and a crowded
adjacent literature on general AI-trust-and-purchase-intention)
- **Gap/question:** as AI search answers (Google AI Overviews, ChatGPT, Perplexity) replace
  traditional link-clicking for product research, brands not cited in an AI's answer appear to
  functionally disappear from the consumer's consideration set rather than just ranking lower — one
  2026 audit of 33 brands found 52% invisible or barely visible in AI answers, and more pointedly,
  audited brands were named in *zero* of 34 purchase-intent-stage prompts even when visible earlier
  in the funnel, while cited brands saw meaningfully higher click-through than non-cited competitors
  on the same queries. That's a distinct mechanism from generic "does AI recommendation build trust"
  research (which a saturation check tonight confirmed is already a fairly active PLS-SEM literature
  — AI-generated review transparency, AI-personalization, AI-agent trust studies all already exist):
  this is specifically about *exclusion/invisibility* at the consideration-set-formation stage, not
  about trusting an AI recommendation once one is given. It's also a different consumer-journey stage
  than idea 6 (already logged 2026-08-20, "Agentic AI commerce delegation"), which is about handing
  off the purchase/execution decision to an agent — this is about upstream discovery/consideration,
  before a purchase decision is even being delegated.
- **Why tractable soon, honest caveats:** the trend data is very current (68% of Google searches
  ended without a click in early 2026, up from 60% in 2024; AI Overviews cut non-cited-brand organic
  CTR by 61% in one cross-organization analysis) and there's live regulatory/legal salience attached
  (EU Commission opened a formal antitrust probe into Google's AI Overviews in Dec 2025; Penske Media's
  Feb 2026 court filing alleges AI Overviews cut publisher clicks by 58%; Senate Democrats have pushed
  FTC/DOJ to investigate) — but that legal fight is about publishers vs. Google, not directly about
  consumers, so it's a weaker "dated hook" than idea 9's or idea 7's fixed legislative/court dates; the
  underlying trend itself is closer to the "vague evergreen topic" this file's own standing instructions
  warn against than a single fixed event. Treat this as real but slower-moving than the other entries.
- **Rough method sketch:** fits the antecedent→mediator→outcome template if narrowly scoped. Antecedent:
  brand citation/omission in an AI answer to a category query (manipulable in a vignette — show
  participants an AI answer that does or doesn't name a target brand for a purchase-intent query).
  Mediator: perceived brand relevance/credibility, or awareness itself (does omission read as "doesn't
  exist" vs. "wasn't chosen"). Outcome: consideration-set inclusion, purchase intention. Plausible
  moderator: category familiarity or prior brand loyalty (a familiar brand may survive omission better
  than an unfamiliar one). Could also run as Study 1 (AI-assisted content analysis of actual AI-answer
  outputs across a category, building a citation-inclusion typology) → Study 2 (PLS-SEM/experimental
  survey) if Britton wants the two-study shape, though this leans more experimental than the TA-heavy
  papers.
- **Target venue:** Journal of Interactive Marketing or Journal of Retailing and Consumer Services fit
  the digital-consumer-behavior framing best; Journal of Consumer Marketing is a plausible alternate but
  would need to be pitched clearly distinct from idea 6 to avoid reviewer overlap concerns given both
  are AI-and-purchase-journey papers from the same research line.
- Leads (unverified, WebSearch only): [Digital Elevator — 33 AI-search audits reveal brand visibility gap](https://thedigitalelevator.com/blog/ai-search-visibility-gap-study/), [Search Engine Land — Google zero-click searches reach 68% in early 2026](https://searchengineland.com/google-zero-click-searches-2026-study-479717), [Similarweb — Zero-Click Marketing: what the 2026 data means](https://www.similarweb.com/blog/marketing/geo/zero-click-marketing/), [ALM Corp — Google AI Overviews and publisher traffic, antitrust filing analysis](https://almcorp.com/blog/google-ai-overviews-publisher-traffic-decline-antitrust-lawsuit-analysis/), [Yahoo/AFP — EU Commission probes Google's AI search mode](https://www.yahoo.com/news/articles/eu-commission-probes-googles-ai-092631086.html)

Both proposals only, per standing rule — nothing built, nothing committed to. Idea 9 is the
stronger of the two tonight (sharp dated tariff/legislative hooks, crosses two of Britton's four
adjacent buckets at once, clean gap versus older non-PLS-SEM COOL literature); idea 10 is a real,
distinct mechanism but flagged moderate-confidence given the weaker single-event hook and the
adjacent "AI trust and purchase intention" literature already being fairly active — Britton should
weigh whether the exclusion/invisibility framing is different enough from that existing work, and
whether it's differentiated enough from idea 6 in the same file, before greenlighting. Also checked
tonight and set aside as not-a-new-idea: Flock/ALPR state legislation restricting ICE data-sharing
(Washington's Driver Privacy Act, Illinois camera-access reporting, more contract terminations) and
further Louisiana CCS opposition news (Air Products blue-hydrogen plant abandoned in June, Exxon's
CO2-pipeline antitrust dispute) — both are live and real, but read as corpus-extension material for
the already-active FLOCK_CAMERAS_PAPER and CCS_PAPER respectively, not distinct new paper ideas, so
neither got a standalone write-up here (same call as the RTCC note on 2026-08-20).

## 2026-08-24 — nightly scouting run (WebSearch only this session; did not test WebFetch/egress
tonight, so no fresh confirmation either way on the network issue logged every prior session —
treat sourcing below as WebSearch-summarized leads, not primary-source-verified, consistent with
every prior entry in this file)

### 11. Surveillance/algorithmic pricing disclosure-mandate wave — perceived fairness and trust
under a live 2026 state-law rollout (moderate confidence — strong, unusually close dated hook;
honest caveat that the underlying fairness-perception construct is an already-active literature)
- **Gap/question:** 2026 has produced a fast state-legislative wave against "surveillance
  pricing" (setting different prices for the same good based on a consumer's personal data via
  AI/algorithmic tools) — more than 40 bills introduced across at least 24 states this year alone,
  already outpacing all of 2025. Maryland's Protection From Predatory Pricing Act (food retailers/
  delivery apps) and Connecticut's surveillance-pricing ban both take effect **October 1, 2026** —
  about five weeks from tonight — and Connecticut's law specifically mandates a consumer-facing
  *disclosure label* at the point of sale, not just a ban. New York's One Fair Price Act passed the
  legislature June 4, 2026, and California's AG opened a retail/grocery/hotel investigative sweep in
  January 2026. The open question this wave creates that existing personalized-pricing-fairness
  literature doesn't yet answer: does a *mandated, standardized disclosure label* — the actual
  regulatory instrument now going live, not just abstract awareness that pricing might be
  personalized — change perceived fairness, trust, and purchase/switching intention differently than
  generic disclosure does, and does support for these bans track a distributive-justice or a
  procedural-justice (autonomy/consent) logic more strongly.
- **Why tractable soon, honest caveat included:** the Oct 1, 2026 effective dates give an unusually
  precise, near-term before/after natural-experiment window — a survey or vignette fielded around
  that date captures a real regulatory change landing in real time, not a hypothetical. But a
  WebSearch saturation check tonight found this is *not* a blank slate: perceived price fairness
  under personalized/algorithmic pricing is an established stream (Journal of Revenue and Pricing
  Management has run studies on this since at least 2019, with more in 2024; a 2024 CHI paper
  specifically compares algorithmic vs. human price discrimination and price-fairness perceptions).
  What that existing work doesn't cover is the *specific 2026 disclosure-label mandate as the
  stimulus* — most existing studies manipulate awareness/suspicion of personalized pricing in the
  abstract, not a real, dated, government-mandated label format. That's a narrower, real gap, not a
  wide-open one — Britton should weigh whether the disclosure-mandate framing is different enough
  from the existing fairness-perception literature to clear review, not assume it automatically is.
  Louisiana's own version of this bill (HB 471, SB 362) was checked tonight and is weak as a
  Louisiana-specific hook — SB 362 is dead, HB 471 stalled in committee as of March 2026 — so this
  reads as a genuinely *national* consumer-marketing paper adjacent to Britton's tariff/consumer-
  behavior line, not a Louisiana-specific one, similar in scope to the national framing already used
  for ideas 2a/6/7/10.
- **Rough method sketch:** fits the antecedent→mediator→outcome template. Antecedent: exposure to a
  disclosure label mirroring the actual Connecticut-mandated format (vs. no label / vs. a generic AI-
  pricing disclosure) in a vignette purchase scenario, or awareness of the state-law change measured
  in a survey fielded post-Oct-1. Mediators: perceived price fairness (distributive) and perceived
  autonomy/control (procedural) as parallel or competing mediators — literature above supports both
  as live constructs. Outcome: trust in retailer, purchase intention, switching/boycott intention,
  support for further regulation. Plausible moderator: prior awareness of surveillance pricing as a
  practice, or general privacy concern. PLS-SEM survey design is the more natural fit than a TA-based
  Study 1, given there's no discourse corpus equivalent to the infrastructure-opposition papers here.
- **Target venue:** Journal of Consumer Marketing or Journal of Public Policy & Marketing (the
  policy-disclosure-mandate framing fits JPP&M's usual lane well, and is a plausible companion piece
  to Britton's existing JPP&M-track work without competing with it on design or corpus).
- Leads (unverified, WebSearch only): [Bloomberg Law — states are cracking down on algorithmic pricing](https://news.bloomberglaw.com/legal-exchange-insights-and-commentary/states-are-cracking-down-on-algorithmic-pricing-are-you-ready), [Skadden — Maryland becomes first state to restrict surveillance pricing in food industry](https://www.skadden.com/insights/publications/2026/05/maryland-becomes-the-first-state-to-restrict-surveillance-pricing), [Loeb & Loeb — New York's One Fair Price Act](https://www.loeb.com/en/insights/passle/2026/06/one-fair-price-act-new-yorks-developing-approach-to-surveillance-pricing), [Holland & Knight — surveillance pricing and dynamic pricing, Aug 2026](https://www.hklaw.com/en/insights/publications/2026/08/surveillance-pricing-and-dynamic-pricing-what-general-counsels), [ailawsbystate.com — 24-state tracker](https://www.ailawsbystate.com/tools/surveillance-pricing-tracker), [MyRepTracker — Louisiana HB 471](https://www.myreptracker.com/louisiana/bills/la-2026-regular-session-hb-471), [Springer/JRPM — antecedents and outcomes of consumer fairness perceptions in personalized pricing](https://link.springer.com/article/10.1057/s41272-024-00509-2), [CHI 2026 proceedings — algorithmic vs. human price discrimination and fairness](https://dl.acm.org/doi/10.1145/3613904.3642280)

### 12. St. James Parish "Cancer Alley" racial-zoning ruling — a legally distinct environmental-
justice hook, adjacent to but not a restatement of DATA_CENTER_PAPER/CCS_PAPER (moderate confidence
— strong, sharply dated legal hook; honest caveat that it's structurally similar in shape to several
already-logged infrastructure-opposition ideas)
- **Gap/question:** on February 9, 2026, a federal district court ruled that Inclusive Louisiana,
  Mt. Triumph Baptist Church, and RISE St. James can proceed on *all* claims in their suit against
  St. James Parish — including that the parish's decades-long practice of zoning heavy petrochemical
  industry into its majority-Black 4th and 5th Districts violates the Thirteenth Amendment (as a
  "vestige of slavery") and the Fourteenth Amendment's Equal Protection Clause. That's a materially
  different legal theory and opposition object than any of Britton's three infrastructure papers or
  the ideas already logged in this file (data centers, LNG, nuclear, solar): those are about siting a
  *new* facility and contesting its arrival; this is about a *historical land-use pattern itself*
  being challenged as racially discriminatory under constitutional (not just environmental-
  regulatory) doctrine — a procedural-justice claim about the zoning process and its history, not
  about a single facility's environmental review. The open marketing/public-policy question: how do
  residents, advocacy groups, and industry frame this land-use/zoning-discrimination claim rhetorically
  compared to the facility-specific opposition frames already coded or being coded in DATA_CENTER_PAPER
  and CCS_PAPER, and does explicit constitutional/civil-rights framing (vs. environmental-harm framing)
  produce a distinct persuasion or legitimacy-perception pattern.
- **Why tractable soon, honest caveat included:** the Feb 9, 2026 ruling is a fixed, dated, and
  unusually significant procedural win (surviving a motion to dismiss on every count, including the
  13th Amendment claim, which is a rare and notable legal theory to survive this stage) — meaning
  there will be continued docket activity and press coverage to build a corpus from as the case
  proceeds. The honest caveat: this is the *fourth* Louisiana industrial-siting/environmental-justice
  angle surfaced across this file's scouting sessions (after LNG at #3/3a, nuclear at #5, and
  solar-misinformation at #8), all sharing the same broad procedural/distributive-justice theoretical
  vocabulary and the same likely venue (JPP&M) — Britton should weigh whether this is genuinely
  differentiated by its distinct legal theory (racial zoning/13th Amendment vs. facility-specific
  environmental review) or whether the well is being drawn from too many times in one thread. A
  WebSearch check tonight for existing marketing/PLS-SEM treatment of this specific case came back
  empty — coverage is legal/journalistic (Earthjustice, Capital B News, Center for Constitutional
  Rights, e&e News), not academic-marketing, so the immediate gap is real even if the broader
  infrastructure-opposition vein is getting crowded.
- **Rough method sketch:** same Study 1 (AI-assisted discourse analysis of case coverage, advocacy-
  group statements, parish council/zoning records where public) → Study 2 (PLS-SEM) template as the
  other three papers. Candidate chain: perceived procedural injustice (historical zoning pattern) as
  antecedent, legitimacy of the land-use/regulatory process as mediator, support for a facility
  moratorium or distrust of parish government as outcome — civil-rights framing as a plausible
  moderator on the antecedent-mediator link.
- **Target venue:** Journal of Public Policy & Marketing (same lane as DATA_CENTER_PAPER/CCS_PAPER)
  or Journal of Business Ethics/Business & Society given the explicit civil-rights/constitutional
  framing, which is a slightly different fit than the consumer-facing JPP&M angle.
- **Recommendation, not a decision:** given how close this sits to the already-logged infrastructure-
  opposition ideas and to DATA_CENTER_PAPER/CCS_PAPER's own template, Britton may prefer this as a
  candidate *fourth case* folded into DATA_CENTER_PAPER's now-national comparative design (procedural-
  justice framing across facility types/regions) rather than a fully separate fifth paper — flagging
  the choice rather than assuming either answer, same as idea 3a's LNG entry did.
- Leads (unverified, WebSearch only): [Capital B News — Black residents win key ruling in Cancer Alley environmental racism case](https://capitalbnews.org/cancer-alley-residents-pollution-lawsuit/), [Center for Constitutional Rights — court rules lawsuit can proceed on all counts](https://ccrjustice.org/home/press-center/press-releases/victory-black-residents-cancer-alley-court-rules-landmark-lawsuit), [Earthjustice — a deserved reprieve for St. John residents](https://earthjustice.org/experts/deena-tumeh/in-louisianas-cancer-alley-a-deserved-reprieve-for-st-john-residents-after-years-of-environmental-injustice), [E&E News — court stymies EPA enforcement push at Cancer Alley plant](https://www.eenews.net/articles/court-stymies-epa-enforcement-push-at-cancer-alley-plant/)

Both proposals only, per standing rule — nothing built, nothing committed to. Idea 11 has the
sharper near-term dated hook (Oct 1, 2026 disclosure-mandate effective dates, five weeks out) but
sits in a literature that's already moderately active, so it's a narrower gap than it first looks;
idea 12 has an even sharper dated legal hook (a fixed Feb 9, 2026 ruling date) and a genuinely novel
legal theory, but is the fourth entry in this file's Louisiana-infrastructure-opposition vein and
reads structurally close enough to DATA_CENTER_PAPER's own scope that Britton may want it folded in
rather than spun out standalone. Also checked tonight and set aside as not-a-new-idea or too weak a
hook: a Louisiana bill (SB246, health-insurance AI-claims-denial human-review mandate) that stalled
at "subject to call" in the Senate in April 2026 with no confirmed final passage found as of tonight
— too uncertain a legislative hook to anchor a study on, and the general AI-disclosure-and-trust
construct is already a fairly active literature (an American Impact Review systematic lit review on
exactly this published March 2026); a Louisiana crawfish-tariff angle (ITC renewed antidumping duties
on Chinese crawfish tail meat, June 2026; Cassidy's Home Market Restoration Act) that reads as too
close a mechanical repeat of idea 9's shrimp-tariff/provenance-branding design to be a distinct paper
rather than a corpus variant of the same idea; and shrinkflation/FTC scrutiny, which remains the same
generically-true, no-fixed-recent-date topic it would have been in any prior year, not a fresh 2026
hook.

## 2026-08-25 — nightly scouting run (WebSearch only this session; did not test WebFetch/egress
tonight — treat sourcing below as WebSearch-summarized leads, not primary-source-verified, consistent
with every prior entry in this file)

### 13. Louisiana's App Store Accountability Act (HB 570/Act 481) — a state-mandated age-verification/
parental-consent gate on app marketing to minors, with a fixed 2027 effective date (moderate-high
confidence — genuinely fresh Louisiana-specific dated law, no marketing/PLS-SEM treatment found; honest
caveat that the adjacent parental-mediation/advertising-to-children literature is old and well-
established, so the novelty is in the specific stimulus, not the general topic)
- **Gap/question:** Louisiana's App Store Accountability Act (HB 570 by Rep. Kim Carver, signed by Gov.
  Landry June 30, 2025, Act No. 481 of the 2025 Regular Session) requires app stores (Apple, Google) to
  verify a user's age category and obtain verifiable parental consent before a minor can download an app
  or make in-app purchases — and, notably, Louisiana's version explicitly rejects the "safe harbor" Texas
  and Utah's versions give developers for relying on the app store's age signal, so app-level marketers
  and developers carry independent compliance exposure here in a way they don't in the other two states.
  A delay bill (HB 977, signed May 15, 2026) pushed the effective date to **July 1, 2027**. The open
  question: does inserting a mandatory, friction-adding age-verification/parental-consent step change
  how minors and parents perceive an app's trustworthiness and privacy-protectiveness, and does it
  actually change download/in-app-purchase behavior — or does it mostly shift friction onto parents
  without changing minors' underlying exposure to marketing, the way COPPA-era consent walls have been
  argued to do. This sits squarely in Britton's surveillance/privacy-in-marketing bucket and is
  Louisiana-specific like the energy/infrastructure line, but is a genuinely different mechanism from
  anything else logged in this file — not facility-siting opposition, not pricing, marketing-to-minors
  friction at the point of app acquisition.
- **Why tractable soon, honest caveat included:** July 1, 2027 is a fixed, dated, already-once-delayed
  effective date roughly eleven months out — close enough to plan a survey or vignette study around a
  real, imminent regulatory change (pre-implementation attitudes now, a natural post-implementation
  follow-up next summer), similar in shape to how idea 11 used the Oct 1, 2026 surveillance-pricing
  disclosure dates. NetChoice has already testified against the law and it is publicly expected to face
  the same First Amendment/compelled-speech legal challenges Texas's and Utah's versions have drawn
  (both already litigated), so there is a real chance the effective date slips again or the law is
  enjoined — that uncertainty is worth flagging plainly, not smoothing over. A WebSearch check tonight
  for existing academic marketing/PLS-SEM treatment of app-store-level age-verification/parental-consent
  mandates came back empty — coverage found was entirely legal/compliance-firm and advocacy material
  (Alston & Bird, Wiley, McDermott, Digital Childhood Alliance, NetChoice), not academic-marketing. The
  honest caveat: parental-mediation theory and advertising-to-children research are long-established
  literatures (decades old), so this isn't a brand-new construct space — the gap is specifically in
  testing this new device-level, store-wide consent-gate mechanism (as opposed to a single app's or
  platform's own age gate) as the stimulus, which no one has been able to study yet because it hasn't
  taken effect anywhere.
- **Rough method sketch:** fits the antecedent→mediator→outcome template. Antecedent: exposure to (or
  awareness of) the mandatory age-verification/parental-consent flow, manipulable in a vignette (a
  mocked-up consent-gate screen vs. a normal frictionless download) or measured as awareness in a survey
  fielded on parents of Louisiana minors. Mediator candidates: perceived privacy protection/trust in the
  app, or perceived parental control/reduced anxiety. Outcome: intended app engagement, willingness to
  allow in-app purchases, attitude toward the app/developer brand. Plausible moderator: parent vs. minor
  respondent (this is one of the few designs in this file where surveying minors as well as parents would
  strengthen it, which raises the standing human-subjects/IRB flag this repo can't resolve on its own —
  flagging clearly, not proceeding). A Study 1 (AI-assisted content analysis of the legislative record,
  NetChoice/industry opposition testimony, and Louisiana Family Forum/advocacy framing) could map the
  competing "child safety" vs. "compelled speech/privacy overreach" argument structures before any Study
  2 survey work, same two-study shape as the other active papers.
- **Target venue:** Journal of Public Policy & Marketing (policy-mandate framing, consistent with
  Britton's other JPP&M-track work) or Journal of Consumer Affairs given the consumer-protection/
  parental-consent angle; Journal of Interactive Marketing is a plausible alternate given the
  app-marketing specificity.
- **Human-subjects flag:** any design that actually surveys parents or minors (rather than just coding
  public legislative/advocacy discourse) requires primary data collection and, for minors specifically,
  extra IRB sensitivity — flagging per standing repo rule, not proceeding past the idea stage.
- Leads (unverified, WebSearch only): [Alston & Bird — Louisiana delays App Store Accountability effective date to July 2027](https://www.alstonprivacy.com/louisiana-delays-app-store-accountability-effective-date-to-july-2027/), [Digital Childhood Alliance — Louisiana becomes third state to sign App Store Accountability legislation](https://www.digitalchildhoodalliance.org/louisiana-becomes-third-state-to-sign-app-store-accountability-legislation-into-law/), [Route Fifty — Louisiana becomes third state to pass app store accountability law](https://www.route-fifty.com/customer-experience/2025/07/louisiana-becomes-third-state-pass-app-store-accountability-law/406661/), [NetChoice testimony in opposition to Louisiana's app store age-verification bill](https://netchoice.org/netchoice-testimony-in-opposition-to-louisianas-app-store-age-verification-bill/), [Louisiana Legislature — enrolled Act No. 481, 2025 Regular Session, House Bill 570](https://www.legis.la.gov/legis/ViewDocument.aspx?d=1427667), [Wiley — State App Store Accountability Acts introduce new obligations](https://www.wiley.law/alert-State-App-Store-Accountability-Acts-Introduce-New-Obligations-for-App-Developers)

### 14. Empirically testing the "AI Booing / AI Washing" mistrust cycle against a real recurring
corporate case (Coca-Cola's AI holiday ads) (moderate confidence — the theoretical model already exists
as a 2025 conceptual paper; the opportunity is an empirical/PLS-SEM test of it, not a from-scratch gap,
and that distinction should be weighed honestly before greenlighting)
- **Gap/question:** Ozturkcan & Bozdağ (2025, International Journal of Market Research) recently
  published a conceptual framework — "AI Washing" (firms exaggerating/over-messaging AI use for
  marketing advantage) triggering "AI Booing" (public backlash over unmet expectations and authenticity
  concerns), which in turn pushes firms toward more symbolic AI-transparency gestures that restart the
  cycle. That paper is conceptual, not an empirical/SEM test. Coca-Cola has now run AI-generated holiday
  ad campaigns two years running (2024's "Holidays Are Coming" remake, 2025's "Refresh Your Holidays"
  with Silverside/Secret Level) and drawn documented, escalating social-media backlash both years without
  discontinuing the practice — a real, dated, repeating corporate case that maps onto the washing/booing
  cycle almost exactly as the theory describes it, but the theory itself hasn't been tested against
  consumer-level survey data. The open question: does *repeated* corporate use of AI-generated creative
  content despite public backlash (a defiance/doubling-down pattern, distinct from a single-exposure
  AI-disclosure event) produce cumulative trust erosion or, alternatively, backlash fatigue/habituation —
  and which of perceived authenticity-violation vs. perceived corporate insincerity better mediates that
  effect. This is a different question from the already-crowded single-exposure AI-ad-disclosure
  literature (see caveat below) because it's about repetition and defiance, not first exposure.
- **Why tractable soon, honest caveat included:** a WebSearch saturation check tonight found the
  single-exposure AI-ad-disclosure-and-trust space is already fairly active — a Manchester paper, a
  Tandfonline "Disclaimer! This Content Is AI-Generated" study, a ScienceDirect generative-AI-service-ads
  paper, and an American Impact Review systematic lit review (already flagged in this file's 2026-08-24
  entry) all exist, several using PLS-SEM already. What's *not* yet done, as far as tonight's search
  found, is an empirical test of the specific washing/booing *cycle* framework, or any study using a
  real multi-year repeating corporate campaign (rather than a single manipulated stimulus) as the
  measurement anchor. Industry-side survey data already shows the trend moving fast and being tracked
  longitudinally — a 2026 Fractl tracking study found consumers saying heavy AI use would decrease trust
  in a favorite brand roughly doubled year-over-year (20% in 2025 to 40% in 2026), which is exactly the
  kind of erosion-over-repetition data point the cycle theory needs and that a fielded study could extend
  with primary data. The near-term hook is real but not fully confirmed: Coca-Cola has not yet announced
  a 2026 (third) holiday AI campaign as of tonight — the pattern of two consecutive years makes a
  third plausible around November 2026, but that is this scout's inference, not a confirmed fact, and
  should be treated as such. If Coca-Cola does not repeat the campaign this year, the "repetition despite
  backlash" natural-experiment framing weakens considerably and the paper would need a different anchor
  case.
- **Rough method sketch:** fits the antecedent→mediator→outcome template. Antecedent: awareness of a
  brand's repeated (vs. single, vs. no) use of AI-generated advertising despite documented public
  backlash — measurable as a real-world awareness variable in a survey fielded around this year's holiday
  season, or manipulated as a repetition count in a vignette. Mediators: perceived authenticity violation
  and perceived corporate insincerity/hypocrisy as parallel or competing mediators (both are explicit
  constructs in the Ozturkcan & Bozdağ conceptual model, giving a ready-made theoretical basis to operationalize
  rather than build from nothing). Outcome: brand trust, purchase intention, willingness to
  publicly criticize/boycott. Plausible moderator: prior general AI attitude or Gen Z/generational cohort
  (industry data already shows a sharp generational split — Gen Z roughly twice as likely as Boomers to
  lose trust over heavy AI-ad use). Survey-based PLS-SEM around the 2026 holiday season is the natural
  fit; Study 1 (AI-assisted content analysis of the actual social-media backlash text across 2024 and
  2025, and 2026 if it recurs) could build the theme typology feeding Study 2's measures.
- **Target venue:** Journal of Consumer Marketing or International Journal of Market Research itself
  (the venue that published the conceptual model — a natural home for the first empirical test of it,
  though also the highest-scrutiny venue for exactly that reason); Journal of Advertising is a plausible
  alternate given the ad-specific framing.
- Leads (unverified, WebSearch only): [SAGE/IJMR — Ozturkcan & Bozdağ, "Responsible AI in Marketing: AI Booing and AI Washing Cycle of AI Mistrust" (2025)](https://journals.sagepub.com/doi/10.1177/14707853251379285), [Marketing Dive — Coca-Cola doubles down on AI in new holiday campaign](https://www.marketingdive.com/news/coca-cola-doubles-down-ai-new-holiday-campaign/804303/), [Campaign US — Coca-Cola reignites AI ad debate with new holiday campaign](https://www.campaignlive.com/article/coca-cola-reignites-ai-ad-debate-new-holiday-campaign/1938664), [Forbes — Coca-Cola sparks backlash with AI-generated Christmas ad, again](https://www.forbes.com/sites/danidiplacido/2025/11/04/coca-cola-sparks-backlash-with-ai-generated-christmas-ad-again/), [Tandfonline — "Disclaimer! This Content Is AI-Generated": how AI-disclosures influence trust](https://www.tandfonline.com/doi/full/10.1080/15252019.2025.2554149)

Both proposals only, per standing rule — nothing built, nothing committed to. Idea 13 has the cleaner,
more novel gap (a Louisiana-specific law with no academic-marketing treatment found yet, though it
carries a real human-subjects/IRB flag if it ever moves past discourse analysis into surveying parents
or minors); idea 14 is honestly the weaker of the two — it extends rather than fills a gap, since the
underlying conceptual framework already exists and the single-exposure AI-ad-disclosure literature
around it is already fairly active, and its near-term hook (a plausible third Coca-Cola holiday AI
campaign) is inferred, not confirmed, as of tonight. Also checked tonight and set aside as not a
distinct new idea: Super Bowl LXI (confirmed hosted in Los Angeles/SoFi Stadium in 2027, not New
Orleans — ruled out as a Louisiana hook entirely); Louisiana coffee-roaster tariff pass-through
(Community Coffee, French Truck Coffee) — real and current, but mechanically too close to ideas 2a, 7,
and 9 (tariff-attribution framing, surcharge-line-item transparency, and Louisiana-provenance branding
are all already logged) to be a distinct paper; Louisiana's coastal-erosion litigation against oil
majors (Chevron's $744.6M verdict remanded to federal court after an 8-0 April 2026 SCOTUS ruling;
Exxon separately reached a settlement with the state in May 2026) — a real and Louisiana-specific
corporate-reputation story, but no confirmed near-term trial date was found (Exxon settled, Chevron's
case has no scheduled retrial date yet), and the adjacent greenwashing/corporate-environmental-boycott
PLS-SEM literature is already fairly active, making this a weaker hook than ideas 13/14 tonight; and the
FTC's "click-to-cancel" subscription rule and California's Delete Act data-broker deadline, both
real 2026 privacy/consumer-protection stories but weak hooks right now — click-to-cancel is still stuck
at the ANPRM stage with no confirmed new effective date after last year's Eighth Circuit vacatur, and the
Delete Act's DROP deadline (August 1, 2026) has already passed as of tonight rather than sitting ahead of
it.

## 2026-08-27 — nightly scouting run (WebSearch only this session; did not test WebFetch/egress
tonight — treat sourcing below as WebSearch-summarized leads, not primary-source-verified, consistent
with every prior entry in this file)

### 15. Sports prediction markets (Kalshi/Polymarket) advertised as a regulatory-category loophole
around responsible-gambling disclosure rules, tested against Louisiana's active enforcement fight
(moderate-high confidence — genuinely new mechanism not yet touched in this file, no academic-marketing
treatment found; honest caveat that the single sharpest federal date, the CFTC comment deadline, has
already passed and the resulting rule's finalization timeline isn't confirmed)
- **Gap/question:** CFTC-regulated "event contract" platforms (Kalshi, Polymarket, and similar) now let
  users wager on game outcomes, point differentials, and win/loss results in a form functionally close to
  sports betting, but because they're classified as derivatives exchanges rather than state-licensed
  sportsbooks, their advertising isn't subject to the responsible-gaming disclosure rules (self-exclusion
  notices, help-line messaging, age-gating enforcement) that apply to licensed operators like DraftKings or
  FanDuel. Louisiana is one of the states most actively contesting this: the Louisiana Gaming Control Board
  sent an advisory (reported Dec 10, 2025) declaring sports event contracts fall within the state's legal
  definition of sports betting, and Attorney General Liz Murrill has publicly criticized the platforms
  ("They literally will let people bet on anything you can think of") — while Kalshi is simultaneously
  reported as now the most visible sports-betting-adjacent brand by digital ad impressions nationally, and
  an American Gaming Association analysis found roughly 43% of digital sports-betting-category ads in early
  2026 didn't need to comply with state responsible-gaming messaging requirements at all, precisely because
  of this classification gap. The open marketing question: does presenting a functionally identical wager
  as a regulated "financial/event contract" rather than as "sports betting" — the actual ad-copy and
  framing choice these platforms are making — lower consumers' perceived risk and perceived need for
  self-regulation, and does the resulting absence of responsible-gaming messaging measurably change
  betting/trading intention compared to an ad for the identical wager framed and disclosed as gambling.
  That's a distinct question from the general problem-gambling-and-advertising literature (already
  large and not something this file needed to re-log) because the mechanism here is specifically a
  regulatory-classification framing choice, not exposure to gambling advertising generally.
- **Why tractable soon, honest caveat included:** this is a live, moving, multi-front fight, not a
  retrospective one — beyond Louisiana's advisory and AG statements, Kalshi alone is reportedly party to
  19 federal lawsuits, other states (New York's AG Letitia James, Kentucky's AG, and others per a 2026
  lawsuit tracker) have sued or issued cease-and-desist orders, and the CFTC itself has been actively
  rulemaking: it issued a Notice of Proposed Rulemaking on June 10, 2026 that would specifically govern
  which sports-related event contracts are permitted, with a public-comment deadline of July 27, 2026 —
  meaning the comment period has already closed as of tonight and a final rule could land at any point
  from here, an honest limit on how precisely "near-term" this is compared to entries with a still-future
  fixed date. What keeps it tractable regardless: DraftKings, Fanatics, and FanDuel — the licensed
  incumbents who bear the disclosure costs these platforms currently avoid — were reported (Covers.com,
  Aug 24, 2026) to be actively lobbying for prediction-market consumer protections just this week, and the
  National Council on Problem Gambling has published specific policy asks (age verification, self-exclusion
  parity, help-line access) aimed squarely at this gap, giving a live advocacy record to build a Study 1
  corpus from immediately. A WebSearch saturation check tonight for existing academic marketing treatment
  of prediction-market/event-contract advertising came back empty — what exists is computational/finance
  literature on arbitrage pricing (arXiv) and legal/policy analysis (CRS, Congress.gov, law-firm client
  alerts), not a marketing or PLS-SEM treatment of the advertising-framing/disclosure-gap question. Given
  how new sports event contracts are (mainstream since roughly 2025), this reads as a genuinely open, not
  merely under-searched, gap.
- **Rough method sketch:** fits the antecedent→mediator→outcome template, with a moderator available from
  the regulatory record itself. Antecedent: ad framing of a wager as a "financial/event contract" vs. as
  regulated "sports betting" for an otherwise identical outcome (manipulable directly in a vignette — two
  mocked-up ads differing only in classification language and the presence/absence of a responsible-gaming
  disclosure line, closely modeled on real Kalshi/DraftKings ad copy). Mediator candidates: perceived risk
  of the wager, or perceived legitimacy/regulatory endorsement (does "CFTC-regulated" read to consumers as
  safer than "state-licensed," reversing the actual protection level). Outcome: betting/trading intention,
  amount willing to wager. Plausible moderator: prior sports-betting experience, or exposure to problem-
  gambling-helpline messaging specifically (does its mere presence in the comparison ad measurably reduce
  intention, testing whether the disclosure requirement these platforms are avoiding actually does anything
  behaviorally). A Study 1 (AI-assisted content analysis of actual prediction-market vs. sportsbook ad
  creative, the LGCB advisory, Murrill's public statements, and the CFTC docket's public comments) could
  build the classification-framing typology before any Study 2 vignette-survey work.
- **Human-subjects flag:** Study 1 as scoped (advertising creative, regulatory filings, public statements)
  is public-record content analysis, no IRB concern. Any Study 2 that shows ad vignettes to real
  respondents and measures betting intention is primary human-subjects survey data and would need IRB
  approval before proceeding — flagging per standing repo rule, not building toward it.
- **Target venue:** Journal of Public Policy & Marketing (regulatory-gap/advertising-self-regulation
  framing fits its lane directly, consistent with several of Britton's other JPP&M-track ideas in this
  file) or Journal of Consumer Affairs given the consumer-protection-disclosure angle; Journal of
  Advertising is a plausible alternate given the ad-copy-manipulation design.
- Leads (unverified, WebSearch only): [iGamingBusiness — Louisiana warns sports prediction markets are illegal sports betting](https://igamingbusiness.com/sports-betting/louisiana-prediction-markets-sports-betting-letter/), [The Advocate — the prediction market boom Louisiana can't tax](https://www.theadvocate.com/baton_rouge/news/prediction-markets-illegal-louisiana-loophole-kalshi-polymarket/article_b032de66-0745-4502-b195-d41e01703e41.html), [Stateline — Kalshi and Polymarket are skirting laws on sports betting, states say](https://stateline.org/2026/03/06/kalshi-and-polymarket-are-skirting-laws-on-sports-betting-states-say/), [American Gaming Association — Prediction Market Advertising Trends](https://www.americangaming.org/resources/prediction-market-advertising-trends/), [National Council on Problem Gambling — Consumer Protections for Prediction Market Event Contracts](https://www.ncpgambling.org/advocacy/consumer-protection-prediction-markets/), [Covers.com — DraftKings, Fanatics, FanDuel seek PM consumer protections](https://www.covers.com/industry/draftkings-fanatics-fanduel-seek-consumer-safeguards-for-prediction-markets-august-24-2026), [CFTC — Notice of Proposed Rulemaking, event contracts (Jun 10, 2026)](https://www.cftc.gov/PressRoom/PressReleases/9249-26), [Federal Register — Prediction Markets NPRM](https://www.federalregister.gov/documents/2026/03/16/2026-05105/prediction-markets), [NOTUS — Letitia James takes aim at prediction market Kalshi](https://www.notus.org/courts/letitia-james-new-york-prediction-market-kalshi-lawsuit-polymarket)

Proposal only, per standing rule — nothing built, nothing committed to. Also checked tonight and set
aside as weaker hooks or corpus-extension material rather than distinct new paper ideas: Louisiana's
food-additive/dye disclosure law (SB 14, amended by SB 57 on June 1, 2026) — genuinely Louisiana-specific
and marketing-adjacent (QR-code-linked "NOTICE" disclaimers on packaging), but SB 57 pushed the effective
date out to December 31, 2028, more than two years off, and an academic study was already found tonight
(Illinois Experts — "The MAHA movement: Early evidence of consumer perceptions of ingredient warning
labels," a 1,020-respondent survey), closing the "no prior treatment" gap this file otherwise looks for;
Louisiana's 2026 carbon-capture legislative session (the Landowners Protection Act/HB 7 rejected in
committee, the new Louisiana Energy Protection Act shielding industry from climate-change lawsuits) — real
and current, but reads as corpus-extension material for the already-active CCS_PAPER rather than a
standalone idea, same call this file has made for CCS/Flock news in prior sessions; continued Flock/ALPR
contract cancellations (Santa Barbara ended Aug 23, 2026; Tempe and other Phoenix suburbs; Sheboygan) —
same call, corpus material for FLOCK_CAMERAS_PAPER; Louisiana's property-insurance reform push (a possible
2027-session cap on general damages) — real but no fixed near-term date, reforms described in coverage as
"remain untested," too vague a hook right now; and two national (not Louisiana-specific) consumer-marketing
stories — GLP-1 telehealth direct-to-consumer marketing enforcement (FDA warning letters, Mar 2026) and
buy-now-pay-later disclosure regulation (CFPB retreating federally, states like New York stepping in) —
both real and current but already heavily trodden by decades-deep DTC-pharma-advertising and fast-moving
fintech-disclosure literatures respectively, with no sharp Louisiana angle to differentiate either from
existing coverage.

## 2026-08-27 — added mid-session at Britton's request (WebSearch only; not a nightly-routine entry)

### 16. SpaceX's $100B Vermilion Parish spaceport — economic-benefit and environmental-commitment
framing vs. the FAA regulatory-waiver fight and the Boca Chica, TX precedent (high confidence — breaking
this week, directly extends machinery already built for DATA_CENTER_PAPER, no marketing-specific academic
treatment of the parallel Texas case found despite 4+ years of coverage there)
- **What happened:** SpaceX announced (Aug 25, 2026) a second Starship spaceport on ~130,000 acres of
  former Exxon property in coastal Vermilion Parish, Louisiana — a $100B investment, first launch targeted
  2029. Musk's own announcement video framed it as "probably 10,000 really exciting jobs"; Louisiana
  Economic Development's official estimate is more conservative and specific — 3,000+ direct jobs
  (avg. $92,600/yr) plus ~8,100 indirect. Fiscal terms: SpaceX pays local taxing authorities a flat
  $25M/year in lieu of property tax, a $20M upfront payment, and $100M toward the state's coastal master
  plan. Simultaneously, the Louisiana Wildlife Federation, National Wildlife Federation, and Pontchartrain
  Conservancy have filed comments opposing an FAA regulatory change that would waive environmental-review
  requirements for the site, citing endangered/threatened species that depend on the wetlands (whooping
  crane, piping plover, Kemp's ridley sea turtle) — while SpaceX has separately stated it will keep large
  portions of the 130,000 acres undeveloped and is coordinating with Louisiana's CPRA on habitat/hydrology
  work.
- **Gap/question:** two framing gaps stacked in the same story, both squarely in Britton's existing
  theoretical toolkit. (1) **Magnitude/specificity framing**: Musk's round, large, informal jobs number
  ("10,000 exciting jobs") vs. LED's precise, lower, sourced figure (3,000 direct + 8,100 indirect) — an
  attribution-specificity gap structurally identical to the explicit/vague/silent causation-attribution
  theme already coded in TARIFF_PAPER's Study 1, just applied to economic-benefit claims instead of
  cost-attribution claims. (2) **Environmental-commitment framing**: SpaceX's own voluntary-restraint
  language ("keeping large portions... untouched") and philanthropic-sounding fiscal commitments
  ($100M coastal master plan) running in parallel with an active push to *remove* the regulatory review
  that would otherwise verify those claims — a real, live instance of the CSR/greenwashing framing problem
  (saying environmental care publicly while lobbying to weaken the mechanism that would check it), and a
  direct match for DATA_CENTER_PAPER's already-built `regulatory-venue-shifting` code (there it was
  utilities moving fights to friendlier venues; here it's the same mechanism at the federal/FAA level).
- **Why tractable and why now:** unlike most scouted ideas in this file, there is a ready-made comparison
  case with four-plus years of outcome data already public: SpaceX's Starbase, Boca Chica, TX (operating
  since 2021). Academic/investigative work already exists there (Cameron County's own $800M economic-impact
  claim; ethnographic/environmental-justice research on Latino and Indigenous community members' experience
  of road closures, beach-access loss, and sonic-boom disruption; reporting that local politicians'
  personal real-estate/campaign gains outpaced broader community economic gains) — but that existing work
  reads as sociology/environmental-justice/investigative-journalism, not a marketing or PLS-SEM treatment of
  the framing-claim-vs-outcome gap specifically. That's the open lane: Louisiana's announcement is young
  enough to capture the *framing* in real time (something Boca Chica's retrospective coverage can't offer
  now), while Boca Chica supplies real, checkable longitudinal outcome data to frame Louisiana's promises
  against — a comparative design with one prospective and one retrospective case a single-site study
  couldn't offer.
- **Rough method sketch:** two options, not mutually exclusive with existing work. (a) Standalone Study
  1 (AI-assisted thematic/content analysis) coding a corpus of SpaceX/Musk statements, LED and Gov. Landry
  official materials, FAA docket comments, wildlife-group filings, and local Louisiana news, cross-coded
  against an equivalent archival Boca Chica corpus (2021 announcement through present) for the same
  magnitude-specificity and environmental-commitment-vs-verification codes — a same-company, same-playbook,
  two-site comparison. A Study 2 vignette-survey could manipulate benefit-claim specificity (precise/sourced
  vs. large/round) × environmental-commitment verifiability (backed by a named regulatory review vs. a
  voluntary/unverified pledge) and measure public support, trust, and perceived greenwashing, with prior
  awareness of the Boca Chica outcome as a plausible moderator (does knowing how the Texas promises played
  out change how Louisiana's version of the same claims lands).
- **Decided 2026-08-27 (same day):** Britton's call is standalone paper, not folded into
  DATA_CENTER_PAPER — "while there is overlap, I think it's distinct" (different industry/regulator: FAA
  vs. state utility commissions/PSCs). **Promoted from scouted idea to active project the same day** —
  see `SPACEX_LOUISIANA_PAPER/CLAUDE.md` and `SPACEX_LOUISIANA_PAPER/notes/2026-08-27-orientation.md` for
  the full project brief; this entry stays here as the scouting-log record of how the idea originated.
- **Human-subjects flag:** Study 1 as scoped (corporate statements, FAA docket comments, wildlife-group
  filings, news coverage) is public-record content analysis, no IRB concern. Any Study 2 vignette-survey
  work would need IRB approval before proceeding.
- **Target venue:** Journal of Public Policy & Marketing (same lane as DATA_CENTER_PAPER, and the
  regulatory-waiver/greenwashing angle fits directly) as lead candidate; Journal of Consumer Affairs or
  Journal of Marketing Management (CSR/greenwashing framing) as alternates.
- Leads (unverified, WebSearch only): [TechCrunch — SpaceX will build a second, $100B 'Starbase' spaceport in Louisiana](https://techcrunch.com/2026/08/25/spacex-will-build-a-second-100b-starbase-spaceport-in-louisiana/), [CNBC — SpaceX plans to build a $100 billion spaceport in Louisiana](https://www.cnbc.com/2026/08/25/spacex-louisiana-spaceport.html), [CNN — SpaceX plans to build the 'biggest launch site on Earth' for $100 billion in Louisiana](https://www.cnn.com/2026/08/25/science/spacex-launch-site-louisiana), [Louisiana Illuminator — Musk plans $100 billion SpaceX launch site in coastal Louisiana](https://lailluminator.com/2026/08/25/spacex-louisiana-2/), [Louisiana Illuminator — Wildlife groups warn not to waive protections to accommodate Louisiana SpaceX site](https://lailluminator.com/2026/08/25/wildlife-spacex/), [Louisiana Radio Network — Questions raised concerning effects of announced Vermilion Parish SpaceX facility on area wildlife](https://louisianaradionetwork.com/2026/08/27/47951/), [Gizmodo — SpaceX's Plan to Build the World's Biggest Spaceport Could Be an Environmental Disaster](https://gizmodo.com/spacexs-plan-to-build-the-worlds-biggest-spaceport-could-be-an-environmental-disaster-2000803286), [Fortune — SpaceX says it's building its largest spaceport yet, committing $100 billion for a Louisiana site](https://fortune.com/2026/08/27/spacex-largest-spaceport-100-billion-louisiana-expansion/), [Washington Times — 5 questions about SpaceX's new Louisiana spaceport](https://www.washingtontimes.com/news/2026/aug/26/5-questions-spacexs-new-louisiana-spaceport/), [Opportunity Louisiana (LED) — SpaceX in Vermilion Parish](https://www.opportunitylouisiana.gov/spacex), [The Conversation — The Starbase rocket testing facility is permanently changing the landscape of southern Texas](https://theconversation.com/the-starbase-rocket-testing-facility-is-permanently-changing-the-landscape-of-southern-texas-242450)

Proposal only, per standing rule — nothing built, nothing committed to.

## 2026-08-29 — nightly scouting run (WebSearch this session; WebFetch tested and, unlike every prior
session logged in this file, was NOT network-wide blocked tonight — `lailluminator.com` returned a plain
HTTP 403 (that site's own bot-protection, not the `EGRESS_BLOCKED` proxy failure logged repeatedly before),
while `legis.la.gov` fetched successfully and returned a real PDF's raw bytes/metadata [Producer: Corel PDF
Engine, created Aug 25, 2026, 7 pages] confirming the document exists and is current — but this session had
no PDF-to-text tool available to read its content, so the bill text below is still drawn from secondary
legal-summary coverage, not directly read from the primary document. Worth flagging for whoever runs this
next: egress may no longer be the blocker it was in every session from 2026-08-13 through at least 2026-08-27.)

### 17. Louisiana's own Click-to-Cancel Act (HB750/Act No. 830) filling the vacuum left by the stalled
federal FTC rule — subscription-cancellation friction as a trust/loyalty mechanism (high confidence — sharp,
newly-signed Louisiana-specific law with a fixed near-term compliance date; genuine gap versus adjacent
dark-pattern/UX literature, which doesn't test a legal mandate as the stimulus in a marketing-trust frame)
- **Gap/question:** the FTC's own federal "click-to-cancel" Negative Option Rule was vacated by the Eighth
  Circuit and remains stalled (already checked and flagged as too weak a hook in this file's 2026-08-24
  entry) — but states are stepping into that vacuum on their own, and Louisiana is one of them: Gov. Landry
  signed HB750, the Click-to-Cancel Act (Act No. 830 of the 2026 Regular Session), June 9, 2026. It requires
  any business operating in Louisiana that offers an auto-renewing subscription/purchase agreement to provide
  a cancellation mechanism that is "cost-effective, timely, and easy-to-use" and not "unreasonably burdensome
  or designed to deter cancellation," plus pre-renewal notice (at least 3 days ahead) for annual-or-longer
  terms, material changes, or trial-to-paid conversions — enforced by the Louisiana AG with civil penalties up
  to $500/violation. Compliance is required by January 1, 2027. The open question: when a company visibly
  complies with (vs. still resists/works around) a newly mandated easy-cancellation requirement, does that
  change perceived autonomy/trust and brand loyalty specifically — as opposed to just usability or re-
  engagement, which is what the existing adjacent literature measures (see saturation check below). This is a
  different mechanism from every AI/pricing-disclosure idea already logged in this file (11, 13) — it's about
  *exit* friction from an existing relationship, not entry-point disclosure or consent.
- **Why tractable soon:** the Jan 1, 2027 compliance date is about four months out from tonight — close
  enough to field a survey or vignette study capturing pre-implementation attitudes now, with a natural
  post-implementation follow-up available next year, the same shape idea 11 used for its Oct 1, 2026
  disclosure-mandate dates. This is also a live multi-state wave, not a Louisiana-only curiosity — California,
  Colorado, New York and others have their own versions — so the design and framing could be pitched either as
  Louisiana-specific (using the AG-enforcement/$500-penalty mechanism as the concrete stimulus) or as a
  national trend-piece, matching the flexibility this file's ideas 2a/6/7/10/11 already used. A saturation
  check tonight found real adjacent work — a 2026 ACM ECCE conference paper builds a 44-pattern dark-pattern
  taxonomy and measures usability (System Usability Scale) and a Human-Computer Trust Scale after a vignette
  cancellation experience — but that is HCI/UX-framed (usability, willingness to re-engage with *an*
  interface), not a marketing-journal PLS-SEM treatment of a *specific state law mandate* as the antecedent
  and brand trust/loyalty/WOM as the outcome. A follow-up search specifically for a PLS-SEM or marketing-
  journal study of a state click-to-cancel law's effect on consumer trust/switching came back empty — closest
  hits were compliance-law-firm coverage and a UX-compliance vendor's own material, not peer-reviewed
  marketing research.
- **Rough method sketch:** fits the antecedent→mediator→outcome template directly. Antecedent: experienced (or
  vignette-manipulated) ease/difficulty of cancelling a subscription — compliant one-click cancellation vs. a
  friction-laden process (calls-only, retention-offer gauntlets, etc.), which could also be framed as
  awareness of the new legal requirement itself. Mediator candidates: perceived autonomy/control over the
  relationship, or perceived corporate goodwill/trustworthiness (does an easy exit read as the company
  respecting the customer, distinct from the dark-pattern literature's usability framing). Outcome: brand
  trust, willingness to resubscribe/repurchase, positive WOM — testing whether easy exit *increases* loyalty
  (the "confident commitment" hypothesis some retention-marketing practitioners already argue informally) or
  simply accelerates churn, which is a genuinely open empirical question. Plausible moderator: subscription
  category (utility/streaming vs. something higher-stakes like gym memberships, which have their own older,
  separate cancellation-friction reputation) or prior negative-cancellation-experience history. Study 1 (AI-
  assisted content analysis of the bill's legislative record, consumer complaints to the LA AG's office if
  public, and national press coverage of the broader state-law wave) could map the "why this law now" framing
  before a Study 2 vignette-survey tests the trust/loyalty model — same two-study shape as the other active
  papers.
- **Human-subjects flag:** Study 1 as scoped (legislative record, public AG complaint data if available, news
  coverage) is public-record content analysis, no IRB concern. Any Study 2 vignette-survey work measuring real
  respondents' trust/loyalty judgments is primary human-subjects data collection and would need IRB approval
  before proceeding — flagging per standing repo rule, not building toward it.
- **Target venue:** Journal of Consumer Marketing or Journal of Consumer Affairs (consumer-protection-mandate
  framing fits both); Journal of Public Policy & Marketing is a plausible alternate given the state-AG-
  enforcement angle, consistent with several of Britton's other JPP&M-track ideas in this file.
- Leads (mostly WebSearch-summarized secondary coverage; the enrolled Act itself was confirmed to exist and be
  current via a direct WebFetch — see session note above — but its text wasn't machine-readable this session):
  [Regulatory Oversight/Foley — Companies Doing Business in Louisiana Must Prepare for New 'Click-to-Cancel
  Act'](https://www.regulatoryoversight.com/2026/06/companies-doing-business-in-louisiana-must-prepare-for-new-click-to-cancel-act/),
  [Lexology — same summary, syndicated](https://www.lexology.com/library/detail.aspx?g=412a83c6-2a56-4919-a85b-f48aa4cc3b9f),
  [Louisiana Legislature — HB750 enrolled Act No. 830, 2026 Regular Session (PDF, confirmed live via WebFetch,
  not text-extracted)](https://www.legis.la.gov/Legis/ViewDocument.aspx?d=1481459),
  [LegiScan — Louisiana HB750 (2026) bill history/status](https://legiscan.com/LA/bill/HB750/2026),
  [Arnall Golden Gregory — State Wave of Click-to-Cancel Rules](https://www.agg.com/news-insights/publications/state-wave-of-click-to-cancel-rules/),
  [Kronenberger Rosenfeld — Court Blocks Click-to-Cancel, federal rule vacatur](https://kr.law/news/article-detail/court-blocks-click-to-cancel-halting-federal-consumer-protection-against-unfair-subscription-practices),
  [ACM ECCE 2026 — "Dark patterns in subscription service cancellation processes"](https://dl.acm.org/doi/10.1145/3746175.3746211)

Proposal only, per standing rule — nothing built, nothing committed to. Also checked tonight and set aside,
each for a specific reason rather than by default:
- **Data-center water usage/aquifer opposition** (Meta's Richland Parish "Hyperion" expansion drawing on the
  Mississippi River Alluvial Aquifer, no state body monitoring usage over time) — real and current, but this
  is the same actor, same site, and same opposition dynamic DATA_CENTER_PAPER's corpus already covers; it
  reads as another antecedent/theme within that paper's existing national-opposition design (like the RTCC and
  CCS-legislative-session items set aside in prior sessions), not a structurally distinct new paper the way 1a
  (ratepayer cost-shifting, a different actor/question/outcome) was. Flagging as corpus material for whoever
  next works DATA_CENTER_PAPER, not writing it up standalone.
- **AI companion-chatbot regulation and parasocial trust/dependency** — genuinely fresh regulatory wave (12
  states with companion-chatbot laws by mid-2026, Oregon's private right of action), and this file's own
  Louisiana-relevance standard means checking Louisiana's own "AI Bill of Rights" (HB734), which would have
  covered companion chatbots specifically. Checked and it does NOT hold up as a Louisiana hook — HB734 was
  withdrawn March 30, 2026 and never became law. Separately, a saturation check found the disclosure-and-trust
  mechanism itself is already a more active experimental literature than expected — multiple field experiments
  already show chatbot-identity disclosure lowering trust/purchase behavior (one cited a 79.7% purchase-rate
  drop), on top of the AI-ad-disclosure literature already flagged in this file's idea 14. Set aside on both
  counts, not just one.
- **Retail facial recognition (Kroger, Walgreens, Walmart BIPA suits; Kroger's abandoned "targeted coupon"
  facial-recognition plan)** — a real, live consumer-backlash story with Congressional attention (Warren/Casey/
  Tlaib), but a saturation check found a fairly active existing marketing-academic literature already
  (facial-recognition-payment adoption studies in Information Systems Research and Humanities & Social Sciences
  Communications, a 2026 systematic literature review on facial recognition + neuromarketing specifically), and
  the dynamic-pricing angle of it overlaps substantially with idea 11 (surveillance pricing) already logged
  2026-08-24. Not distinct enough from existing coverage, both academic and within this file.
- **Louisiana's 2024 gubernatorial veto of a political-deepfake bill** — turned up in an early search and
  looked promising, but checking the date showed it's June 2024 news, not a 2026 hook; ruled out as stale.
- **Stablecoin/crypto-debit-card marketing framed to dodge disclosure rules** — the classification-loophole
  mechanism that made idea 15 (prediction markets) work doesn't hold here: 2026 coverage shows stablecoin
  regulation (the GENIUS Act framework) converging toward *more* disclosure and licensing, not a gap
  advertisers are exploiting. Mechanism doesn't match the story; ruled out.

## 2026-08-30 — nightly scouting run (WebSearch this session; WebFetch attempted twice against
`journals.uchicago.edu` JACR forthcoming-issue pages and blocked both times with a plain HTTP 403 — that
site's own bot-protection, the same shape of block `lailluminator.com` gave in the 2026-08-29 session, not
the network-wide `EGRESS_BLOCKED` proxy failure from earlier sessions. So the special-issue details below
are WebSearch-summarized secondary/indexed text, cross-checked across three independent queries that all
returned matching specifics, not a direct read of the primary CFP page.)

### 18. A methods/protocol paper on Britton's own six-phase AI-assisted thematic analysis workflow, targeted
at JACR's "AI in the Consumer Marketplace" special issue (moderate confidence — a real, dated, well-matched
venue opportunity that needs essentially no new primary data collection, but a genuine and growing adjacent
literature on LLM-assisted thematic analysis already exists, so this is a narrower, more defensible gap than
a first-mover claim)
- **Gap/question:** the *Journal of the Association for Consumer Research* has an open special issue, "AI in
  the Consumer Marketplace" (Vol. 13, Issue 3; editors Bernd Schmitt, Ana Valenzuela, Reto Hofstetter, and
  Luca Cian), that explicitly names "what standards ensure transparency and reproducibility in AI-assisted
  research (prompt reporting, model documentation, validation practices)" as a topic of interest, alongside
  "how can GenAI tools be used for theory abstraction, stimuli creation, or qualitative coding." Britton's
  team already has exactly this in hand and already tested across five live projects: the six-phase
  AI-assisted thematic analysis workflow in `Claude_Knowledge/Thematic Analysis/AI_Assisted_TA_Shared_
  Method.md` and `Study1_AI_Thematic_Analysis_Publishable_Protocol.md`, including the explicit human-only
  Phase 3 safeguard (and the one documented, reasoned exception for `FLOCK_CAMERAS_PAPER`) that is itself a
  concrete, defensible answer to the CFP's transparency/reproducibility question. A saturation check tonight
  found this is **not an empty lane**: there is a real and growing published literature on LLM-assisted
  thematic analysis specifically — De Paoli 2024 (Sage, *Field Methods* per the DOI path, on the limits of
  using an LLM for inductive TA of interview transcripts), a 2026 Springer Nature *Discover AI* piece asking
  whether LLMs can code text for TA, several PMC/arXiv papers comparing LLM-vs-human coding agreement
  (kappa/Spearman figures reported), and — closest of all — a 2026 *Humanities and Social Sciences
  Communications* (Nature) paper describing "GATOS" (Generative AI-enabled Theme Organization and
  Structuring), an open-source-ML thematic-analysis workflow demonstrated across three case studies. None of
  what turned up tonight is a marketing/consumer-research-journal treatment applying a disclosed, multi-phase,
  human-AI-divided-labor protocol specifically to *public corporate/marketing-controversy content* (corporate
  statements, regulatory filings, public comments) simultaneously across several live real-world case
  studies — the closest hits are healthcare/HCI transcript-coding studies or a single open-source-tool
  demonstration paper, not a consumer-marketing methods contribution built on a track record across five
  concurrent corporate-controversy corpora. That's a real but narrower gap than "nobody has tried this," and
  should be presented to Britton with that hedge rather than as an unclaimed lane.
- **Why tractable soon:** the submission portal for this special issue opens February 1, 2027 and the first
  deadline is April 1, 2027 — about seven months from tonight, and unlike most ideas in this file, this one
  requires no new corpus, no new fieldwork, and no IRB exposure at all, because the paper's subject *is* the
  already-built and already-applied methodology, not a new empirical study. The manuscript would essentially
  be a write-up-and-generalize job over material Britton's team has already produced (the shared method docs,
  the five projects' worth of applied experience, the one documented Phase-3-exception decision as a case
  study in itself of how the team handles an edge case) rather than a from-scratch research undertaking,
  which is unusual tractability for this file.
- **Rough method sketch:** this doesn't fit Britton's usual mediated-antecedent → psychological-mediator →
  outcome / PLS-SEM template — it's a methods/protocol contribution, not an empirical consumer-behavior study,
  which is a deliberate fit to what the task brief asked to scout (AI-augmented qualitative methods) rather
  than a mismatch. A plausible shape: (1) present the six-phase workflow itself as the contribution, with the
  human-only Phase 3 rule framed explicitly as a reproducibility/validity safeguard; (2) illustrate it across
  two or three of the five live projects (e.g., Tariff, Data Center, Flock Cameras) as parallel demonstration
  cases, echoing GATOS's multi-case-demonstration structure but on marketing-controversy content instead of
  general qualitative data; (3) if reviewers would expect a quantified reliability claim, a modest inter-rater
  check (a second human coder independently reviewing a subsample of AI-proposed themes against the already-
  locked Phase 3 human calls, reporting agreement) would strengthen the transparency claim without requiring
  new primary data collection.
- **Human-subjects flag:** as scoped, this is a methods paper about an internal research workflow applied to
  already-public-record corpora — no participant data involved. If a reliability check adds a second human
  coder, that's ordinary co-author/research-team methodology practice, not human-subjects data collection in
  the regulatory sense, though this is a plain-language read, not a legal one — worth Britton (or the IRB
  office, if he wants to be certain) confirming before treating it as settled.
- **Target venue:** *Journal of the Association for Consumer Research*, "AI in the Consumer Marketplace"
  special issue (Vol. 13, Iss. 3), portal opens Feb 1, 2027, deadline Apr 1, 2027, decisions expected ~Mar
  2028, publication ~Jul 2028 — a long final timeline typical of a journal special issue, but the near-term
  action (drafting toward an April 2027 deadline) is what makes this worth flagging now rather than later.
- Leads (WebSearch-summarized secondary/indexed text only, primary CFP page blocked by 403 both times
  tonight — see session note above): [Journal of the Association for Consumer Research — Call for
  papers](https://www.journals.uchicago.edu/journals/jacr/forthcoming-13.3), [Association for Consumer
  Research — JACR](https://acrwebsite.org/jacr/), [De Paoli 2024, SAGE — Performing an Inductive Thematic
  Analysis of Semi-Structured Interviews With a Large Language Model](https://journals.sagepub.com/doi/10.1177/08944393231220483),
  [Springer Nature, Discover AI 2025/2026 — Can large language models be used to code text for thematic
  analysis?](https://link.springer.com/article/10.1007/s44163-025-00441-3), [Nature, Humanities and Social
  Sciences Communications 2026 — Thematic analysis with open-source generative AI and machine learning
  (GATOS)](https://www.nature.com/articles/s41599-026-06508-5), [arXiv — Human-AI Collaboration in Thematic
  Analysis using ChatGPT](https://arxiv.org/pdf/2311.03999)

Proposal only, per standing rule — nothing built, nothing committed to. Also checked tonight and set aside,
each for a specific reason rather than by default:
- **Louisiana Data Privacy Act (SB386, signed May 29, 2026, effective Jan 1, 2027, the state's 22nd
  comprehensive privacy law)** — real, current, and has a concrete near-term compliance date structurally
  identical to idea 17's, but a saturation check found the specific consumer-facing mechanism (an opt-out
  right for targeted advertising) sits on top of an already-substantial existing research base built around
  CCPA/CPRA since 2018–2023 (opt-out-effectiveness studies, Global Privacy Control research, survey data on
  consumer opt-out preferences). Louisiana being the 22nd state to pass a near-identical law, rather than the
  first or most distinctive, makes it hard to argue a fresh mechanism rather than one more entrant in an
  already-well-studied wave; set aside rather than force a differentiator that wasn't found tonight.
- **Louisiana's two 2026 grocery/surveillance-pricing bills, HB800 ("Make Affordable Groceries Again Act")
  and HB471 (surveillance-based price discrimination)** — both genuinely on-point (grocery pricing ties
  directly to Britton's tariff/affordability interest, and surveillance-pricing is squarely idea 11's
  mechanism), but both stalled in House committee as of their last recorded action (Feb/Mar 2026) with no
  further movement found and no effective date to anchor a before/after design — and even if either had
  passed, it would read as the same mechanism idea 11 already logged 2026-08-24, not a distinct new idea.
  Set aside on both the stalled-status and the duplication grounds.
- **Louisiana Act No. 182 (60-day advance-notice requirement before insurers cancel/non-renew property or
  auto policies, effective July 1, 2026)** — real and Louisiana-specific, but the compliance date is already
  nearly two months in the past as of tonight, losing the clean prospective before/after window this file
  otherwise looks for, and insurer-cancellation trust/switching behavior is a long-established research area
  in insurance/marketing journals; no distinct new mechanism found to justify treating it as a fresh gap.
- **The Louisiana PSC's Aug 12, 2026 ruling blocking a subpoena that would have forced Meta to disclose data
  center economic-impact and power-demand documentation, and the related ratepayer-cost-exposure coverage
  (Entergy's pending application for 7 more gas plants, PSC decision expected Dec 16, 2026)** — real, current,
  and even has a concrete near-term decision date, but this is the same actor, same site, and same regulatory
  fight DATA_CENTER_PAPER's corpus already covers (Britton's own Meta/Richland-Parish anchor case); reads as
  corpus/update material for that already-active project, not a structurally distinct new paper, same call
  made for the water-usage/aquifer item set aside in the 2026-08-29 entry. Flagging for whoever next works
  DATA_CENTER_PAPER, not writing it up standalone.
- **Louisiana's 2026 PBM (pharmacy benefit manager) reforms (reimbursement-formula floor by Mar 1, 2026, the
  $45M CVS Caremark settlement, HB1236's cost-share protections)** — real and current, but the affected
  relationship (PBM-to-pharmacy reimbursement formulas, PBM-to-insurer contracting) is a B2B/regulatory-
  compliance dynamic, not a consumer-facing marketing-communication or trust mechanism a patient/consumer
  directly experiences and evaluates; doesn't fit Britton's consumer-behavior lane without a stretch not
  attempted tonight.
- **LNG export-terminal opposition in southwest Louisiana (Venture Global's Calcasieu Pass 2 expansion,
  Commonwealth LNG's contested permit, both drawing active Cameron Parish resident opposition over safety,
  wastewater discharge, and infrastructure strain)** — real, current, and would fit Britton's industrial-
  siting-opposition interest structurally, but Britton already has three active projects in almost exactly
  this genre (data center, CCS, and SpaceX siting opposition) plus idea 5 (nuclear) already logged in this
  file; no distinct new mechanism (versus regulatory-venue-shifting, magnitude-framing, or the other codes
  already built) turned up tonight to justify a fourth or fifth entry in the same bucket rather than reading
  as more corpus material for an existing line. Worth another look only if a sharper, different mechanism
  surfaces later.
- **The August 2026 Walmart boycott (a viral creator ban) and the ongoing Target DEI-rollback boycott/"Shop
  Smart, Not Target" campaign** — real, current, and squarely about consumer trust and brand behavior, but a
  saturation check found boycott-intention and political-consumerism is already an active, recent academic
  literature (a 2026 *International Journal of Advertising* piece specifically on political identity,
  corporate response, and boycott intention turned up directly in the search), and neither story has a
  distinct Louisiana angle to differentiate it from that existing coverage.
- **Louisiana SB254 (bans retail surcharges specifically on debit-card payment, with a private right of
  action)** — real and current, but sits on top of a decades-deep existing marketing literature on
  partitioned/drip pricing and surcharge fairness perception; no fresh mechanism found tonight to distinguish
  it from that established base.

## 2026-08-31 — nightly scouting run (WebSearch this session; WebFetch tried once against `marketplace.org`
and got a plain HTTP 403 — that site's own bot-protection, same shape of block `lailluminator.com`/
`journals.uchicago.edu` gave in the two prior sessions, not the network-wide `EGRESS_BLOCKED` proxy failure
from earlier in the file. Below is WebSearch-summarized, leads not primary-source-verified.)

### 19. De minimis tariff-exemption elimination and the collapse of Temu/Shein/AliExpress's "too-cheap-to-
question" value proposition — perceived pricing-legitimacy and platform trust as a tariff-shock mechanism
distinct from ideas 2a/7/9 (high confidence — sharp, multiply-dated legal timeline, real measured behavioral
shift already in industry data, no academic-marketing treatment found)
- **Gap/question:** the U.S. eliminated the "de minimis" duty-free import exemption (previously $800/
  shipment) in stages — China/Hong Kong lost it May 2, 2025, all other countries lost it August 29, 2025 — and
  that suspension has since been repeatedly re-upheld on its own legal footing, separate from the broader
  IEEPA tariff program already covered in this file's idea 7: the U.S. Court of International Trade
  specifically declined to overturn the suspension on August 13, 2026 (ruling it rests on CBP's Section
  321/Trade Facilitation and Trade Enforcement Act discretion, not the IEEPA authority the Supreme Court
  struck down in February), and the "One Big Beautiful Bill Act" separately repeals the statutory exemption
  outright, permanently, effective July 1, 2027. The result: platforms whose entire consumer proposition was
  "impossibly cheap, delivered duty-free" (Temu, Shein, AliExpress) saw 20-40% price increases and products
  disappearing from U.S. catalogs, and audience data shows it actually changed behavior, not just prices —
  Temu's U.S. audience fell as much as 62% and Shein's 47% from pre-suspension levels, both still running
  roughly 30% below baseline as of April 2026, with Target/Walmart/Amazon absorbing the displaced shoppers.
  One tracking piece (Measure Protocol) frames the remaining core as having shifted "from deal-hunting to
  trust-checking" — i.e., the shock didn't just raise prices, it appears to have changed how the *surviving*
  low-price claims from these platforms are evaluated. That's a distinct mechanism from every other tariff
  entry already logged here: not corporate causal-attribution framing at an established retailer (2a), not
  post-ruling price non-reversal on goods already in the market (7), and not a domestic-provenance/COOL
  branding question (9) — this is about an entire platform category's core value proposition (near-zero
  markup, enabled by a now-closed regulatory loophole) being revealed as artificially cheap, and whether
  that revelation itself (not just the resulting price increase) erodes trust in the platform's future price
  claims.
- **Why tractable soon, honest caveat included:** three separate fixed dates give this real temporal
  structure rather than a single vague trend: the original suspension dates (May/Aug 2025) are now over a
  year in the rearview, meaning any survey fielded now captures lived, not hypothetical, experience; the Aug
  13, 2026 CIT ruling (18 days before tonight) re-confirmed the suspension is durable, not a fluke pending
  further litigation; and the July 1, 2027 permanent statutory repeal (about ten months out) gives a genuine
  future before/after point distinct from the already-lived initial shock, useful for a longitudinal framing.
  A WebSearch saturation check tonight for prior academic or PLS-SEM treatment of de minimis elimination and
  consumer trust/switching came back empty — what exists is trade-press/logistics-industry coverage
  (SupplyChainBrain, CNBC, Newsweek, WWD, Measure Protocol's own audience-tracking data) and legal/customs-
  compliance analysis (RVIA, KPMG, Alvarez & Marsal on the CIT ruling), not a marketing-journal treatment of
  the consumer-trust mechanism. Given how new and still-unfolding the legal timeline is (the CIT ruling is
  barely three weeks old, the permanent repeal hasn't happened yet), this reads as a genuinely open gap, not
  an under-searched one. Honest caveat: the *general* tariff-driven-brand-switching consumer-survey base (the
  60%-would-switch-brands, Circana private-label-stickiness data already cited under idea 2a) is the same
  industry evidence base this idea would also draw on, so the lit review overlaps with 2a even though the
  stimulus/mechanism is different — Britton should weigh that shared evidence base explicitly if he greenlights
  both, to avoid the two papers reading as thin variations of each other in a lit review.
- **Rough method sketch:** fits the antecedent→mediator→outcome template. Antecedent: awareness/experience of
  a previously-trusted low-cost platform's price jump and product disappearance following the loophole's
  closure — measurable as an individual-difference/awareness variable in a survey of past Temu/Shein/
  AliExpress shoppers, or manipulated in a vignette (a mock product listing shown at the old vs. new price,
  framed as "duty-free" vs. "duty added"). Mediator candidates: perceived pricing legitimacy/authenticity (was
  the original low price ever a real, sustainable offer, or an artifact of a loophole), or perceived platform
  trustworthiness going forward. Outcome: platform loyalty/switching intention (to Amazon/Walmart/Target, per
  the audience data above), willingness to pay a premium at the same platform post-price-increase, or general
  skepticism toward other "too good to be true" pricing claims (a spillover-trust outcome worth testing).
  Plausible moderator: prior awareness that the low price depended on a tariff loophole (does knowing *why*
  the price rose change the trust effect, similar to 2a's/7's causal-attribution logic) or platform loyalty/
  purchase frequency pre-suspension. Survey-based PLS-SEM fits better than a TA-based Study 1 here, given
  there's no discourse corpus equivalent to the infrastructure-opposition papers — though a light Study 1
  (AI-assisted content analysis of platform reviews/social commentary on the price changes, which is
  extensive and public) could still map the trust-erosion language before a Study 2 survey.
- **Target venue:** Journal of Consumer Marketing or Journal of Retailing — a genuine companion to
  TARIFF_PAPER and idea 2a (same broad tariff-and-consumer-behavior line) but a structurally distinct
  paper (platform-level value-proposition collapse, not corporate messaging framing or COOL/provenance
  branding), not a competing use of the same design.
- Leads (unverified, WebSearch only): [SupplyChainBrain — EU to end de minimis with new customs fee in 2026](https://www.supplychainbrain.com/articles/43004-eu-to-end-de-minimis-with-new-customs-fee-in-2026), [Marketplace.org — yep, the de minimis tariff exemption is still suspended](https://www.marketplace.org/story/2026/03/03/supreme-court-tariffs-de-minimis-exemption-cheap-imports) (WebFetch blocked 403 tonight, title/date from search index only), [CNBC — Shein and Temu see U.S. demand plunge on 'de minimis' trade loophole closure](https://www.cnbc.com/2025/06/05/shein-temu-see-us-demand-plunge-on-de-minimis-trade-loophole-closure.html), [Measure Protocol — Shein & Temu After Tariffs: Where Shoppers Went](https://www.measureprotocol.com/insights/shein-temu-shoppers-after-us-tariffs), [Newsweek — 'De minimis exception': how Trump's China tariffs will hurt Temu and Shein](https://www.newsweek.com/de-minimis-exception-trump-tariff-shein-temu-2025483), [RVIA — United States Court of International Trade (CIT) upholds suspension of de minimis](https://www.rvia.org/news-insights/united-states-court-international-trade-cit-upholds-suspension-de-minimis), [KPMG — US Trade Court: IEEPA authorizes presidential rescission of de minimis exemption](https://kpmg.com/us/en/taxnewsflash/news/2026/08/us-trade-court-ieepa-de-minimis-treatment.html), [Alvarez & Marsal — USCIT upholds IEEPA suspension of de minimis treatment in Axle of Dearborn](https://www.alvarezandmarsal.com/thought-leadership/uscit-upholds-ieepa-suspension-of-de-minimis-treatment-in-axle-of-dearborn)
- **Update, 2026-09-01 (checked, no change):** rechecked for anything new since the entry above.
  Nothing has moved — the Aug 13, 2026 CIT ruling (*Axle of Dearborn v. Dep't of Commerce*) upholding
  the suspension stands, a WebSearch tonight found no Federal Circuit appeal filed against it, and the
  audience-decline figures (Temu, Shein) are still the same pre-April-2026 data points cited above, not
  fresher numbers. No update needed to the gap/method sketch; logged here rather than as a new idea.

Proposal only, per standing rule — nothing built, nothing committed to. Also checked tonight and set aside,
each for a specific reason rather than by default:
- **New York's Tariff Transparency Act (A8241/S3567), which would require a "tariff cost estimate" on new
  cars' federal Monroney window-sticker label** — a genuinely on-point mechanism (a mandated tariff-specific
  disclosure label, structurally similar to idea 11's surveillance-pricing disclosure-label logic but for
  tariffs specifically) and a real gap versus the general tariff-attribution literature, but a direct check of
  the bill's status tonight (via WebFetch on the NY Senate's own bill tracker) found it's stalled — introduced
  May 5, 2025, re-referred to the Assembly Transportation Committee January 7, 2026, no further movement since
  — too uncertain a legislative hook to anchor a study on right now, same standard this file has applied to
  other stalled bills (HB800/HB471 set aside 2026-08-30, SB246 set aside 2026-08-24). Worth rechecking if it
  moves.
- **LLM/"silicon sample" synthetic survey respondents as a methods-paper angle** (an alternative AI-augmented-
  methods idea to sit alongside idea 18's AI-assisted-TA/JACR pitch) — real and directly relevant to Britton's
  own PLS-SEM toolkit (synthetic respondents replacing or augmenting a fielded survey sample), but a saturation
  check tonight found this is thoroughly claimed already: Sarstedt et al. 2024 in *Psychology & Marketing* — a
  paper by one of PLS-SEM's own leading methodologists — is specifically titled "Using large language models to
  generate silicon samples in consumer and marketing research: Challenges, opportunities, and guidelines," and
  a wave of 2026 psychometric-audit and cross-domain-benchmark papers (several on arXiv, one explicitly finding
  LLM survey samples fabricate indirect/mediation effects on placebo paths) has followed it. Not a gap; set
  aside outright rather than logged as a candidate.
- **Hyundai's $5.8B Donaldsonville/Ascension Parish steel mill** — a real, live, well-documented Louisiana
  siting fight (air-permit fast-tracking concerns, a coalition of United Steelworkers District 13, NAACP
  Louisiana, Sierra Club Delta Chapter, and Rural Roots Louisiana demanding a longer public-comment period,
  reporting through Aug 28, 2026) that pattern-matches the same economic-benefit-claim-vs-environmental/
  procedural-justice-opposition template already active in DATA_CENTER_PAPER, CCS_PAPER, and
  SPACEX_LOUISIANA_PAPER, plus already-logged ideas 3a (LNG), 5 (nuclear), 8 (solar), and 12 (Cancer Alley
  zoning) — the same reasoning this file already applied to set aside further LNG-terminal opposition
  2026-08-30 ("Britton already has three active projects in almost exactly this genre... no distinct new
  mechanism... to justify a fourth or fifth entry"). No sharper or different mechanism than what's already
  coded turned up tonight; flagging as corpus-extension material for whoever next works DATA_CENTER_PAPER or
  CCS_PAPER (it sits closest to CCS_PAPER's industrial-permitting angle) rather than a standalone idea.
- **Orion Renewable Energy Group's 1 GW "Persimmon Energy Center" solar/storage project, North Calcasieu
  Parish** — same underlying story as the ~4,700-acre Moss Bluff solar opposition already covered under idea 8
  (2026-08-24 entry); this is a name/detail update on the same project, not a new one. No standalone write-up.
- **Meta's $17.1B multistate settlement over Instagram/Facebook's addictive design and harm to minors**
  (announced Aug 26, 2026, largest state consumer-protection settlement outside Big Tobacco, mandates
  algorithmic-feed opt-outs and overnight/school-hours notification limits for minors) — real, current, and
  squarely in the marketing-to-minors space, but it's a national story with no distinct Louisiana angle, its
  core mechanism (algorithmic-feed opt-outs/parental-consent-style protections for minors) overlaps
  substantially with idea 13's App Store Accountability Act framing already logged 2026-08-25, and a "does a
  post-scandal settlement change trust in a platform's safety claims" framing would sit on top of a very large
  existing crisis-communication/corporate-trust-repair literature this file didn't find time to fully
  saturation-check tonight — flagging as worth a closer look later rather than either logging or fully ruling
  out.

## 2026-09-01 — nightly scouting run (WebSearch only this session; did not test WebFetch/egress
tonight)

**Numbering/continuity note:** tonight's task briefing referenced "idea 19" (the de minimis/
Temu-Shein-AliExpress entry above) and a 2026-08-31 Meta-settlement flag as already logged. This
session's git worktree had branched from an older point in this file's history (before those
entries existed) and didn't have them yet when it ran, so it re-researched the de minimis question
independently — that check found no new developments since 2026-08-31 and has been folded into a
short dated update on idea 19 above, rather than duplicated as a separate entry. The two genuinely
new items below continue the real numbering (20, 21) rather than restarting from a stale 16.

### 20. Meta's $17.1B multistate minors-safety settlement — saturation check completed tonight as
requested: real, narrow gap, distinct from idea 13 (high confidence on the gap being real and
unduplicated; the caveat is that the settlement itself is six days old as of tonight, so this is
necessarily speculative about what the post-implementation literature will look like)
- **What happened, confirmed tonight:** Meta agreed Aug 26, 2026 to pay up to $17.1B to 48 states, DC,
  Puerto Rico, and other territories, settling claims it knowingly designed Instagram/Facebook to be
  addictive to minors, misled the public about the harm, and improperly collected data from
  under-13 users. Terms include a default 2-hour/day cumulative time limit for under-18 users
  (parent-overridable only), hidden like-counts on minors' posts by default, a ban on "extreme"
  beauty filters for minors, and a contractual bar on Meta making "false, misleading, or deceptive"
  statements about platform safety going forward. Meta owes the full amount unless TikTok and YouTube
  also settle and adopt comparable defaults, in which case Meta's share drops to 70%.
  Reporting since (TechCrunch, France24, Al Jazeera, Aug 26-28) converges on one specific practical
  problem: the settlement's core mechanism — determining which accounts belong to under-18 users —
  depends on age-verification technology that, per multiple outlets, "doesn't work well," with no
  reliable industry-standard method existing yet; child-safety advocates (e.g., Jean Twenge, quoted
  in coverage) flag this as the linchpin the whole settlement rests on.
- **Saturation check (the specific ask tonight):** searched directly for existing marketing/
  consumer-behavior academic literature on post-settlement platform-trust-repair in a minors-safety
  context. Found none — unsurprising given the settlement is six days old. What *does* already exist,
  and matters for scoping this honestly: (1) a well-established general corporate-trust-repair/image-
  repair literature (warmth-and-competence apology models, SEM studies showing apologies restore trust
  via perceived warmth/competence as mediators); (2) a specific, directly-relevant precedent case
  already studied — Facebook's 2018 post-Cambridge-Analytica apology-and-marketing-campaign response,
  which the general trust-repair literature already treats as a case example. So the *general
  mechanism* (corporate apology → perceived sincerity → trust restoration) is not a gap; a straight
  replication of that design on this settlement would be a weak contribution.
  **Where the real, undercovered gap sits:** the existing literature is almost entirely about
  *voluntary* corporate apologies/CSR gestures following a scandal. This case is different in a way
  that looks testable — the corrective action here is *court-mandated* (a legal settlement with
  contractual behavior requirements and a bar on future deceptive safety claims), not a chosen
  gesture, and its flagship mechanism (age verification) is *publicly and simultaneously reported as
  unreliable* even as it rolls out — meaning the "corrective action" itself may not be perceived as
  credible independent of Meta's sincerity. That's a mandated-vs.-voluntary compliance-credibility
  distinction the existing apology/image-repair literature doesn't test, and a live, dated natural
  experiment now exists to test it against (rollout is required within one year per settlement terms,
  so implementation, not just announcement, will be observable within this file's usual planning
  horizon).
- **Distinct from idea 13, confirmed:** idea 13 (App Store Accountability Act) is about a *state-law-
  mandated* age-verification/parental-consent gate applied at the *app-store* level, before download —
  a friction-at-acquisition mechanism, with the open question being whether that friction changes
  perceived trustworthiness and download/purchase behavior. This Meta entry is about a *company's own*
  account-level enforcement following a *litigation settlement* (not a legislature), applied to
  *existing* users post-signup, with the open question being whether mandated (vs. voluntary) corrective
  action under public skepticism about its own technical credibility produces trust repair or backlash.
  Different regulatory instrument (litigation settlement vs. statute), different point in the user
  lifecycle (existing account vs. pre-download), different literature gap (mandated-compliance
  credibility vs. store-level friction). Not a duplicate — a real, separate gap.
- **Rough method sketch:** fits the antecedent→mediator→outcome template. Antecedent: exposure to/
  awareness of the settlement's mandated changes, framed as either court-imposed (mandated) or
  reframed as a voluntary safety initiative (manipulable in a vignette holding the actual changes
  constant and varying only the mandated-vs.-voluntary framing — a clean 2-cell or 2x2 design).
  Mediator candidates: perceived sincerity/corporate insincerity (from the existing apology
  literature) and, as the novel addition, perceived implementation credibility (does the parent/user
  believe the age-verification mechanism will actually work, given it's being reported as unreliable
  in the same news cycle). Outcome: trust in the platform, continued-use intention for parents of
  minors specifically, support for the settlement/regulatory approach generally. Plausible moderator:
  parent vs. non-parent respondent, or prior awareness of the age-verification-technology-doesn't-work
  reporting. Given the settlement rolls out over the coming year, a Study 1 (AI-assisted content
  analysis of coverage/advocacy reaction as it accumulates) tracking how the "mandated but maybe
  unworkable" frame develops in public discourse, feeding a Study 2 (PLS-SEM survey) once rollout is
  underway, would let this follow the same two-study shape as the other active papers rather than
  requiring everything fielded at once.
- **Human-subjects flag:** Study 1 as scoped (settlement documents, news coverage, advocacy statements)
  is public-record content analysis, no IRB concern. Any Study 2 survey of parents (or, worse, minors)
  is primary human-subjects data and would need IRB approval before proceeding — flagging per standing
  repo rule, not proceeding past the idea stage.
- **Target venue:** Journal of Public Policy & Marketing (regulatory/settlement-compliance framing) or
  Journal of Consumer Affairs (consumer-protection angle); Journal of Advertising or Journal of Business
  Ethics are plausible alternates given the "false/misleading safety claims" contractual language, which
  edges toward corporate-communication-ethics territory.
- Leads (unverified, WebSearch only): [NPR — Meta, states agree to $17 billion settlement in child safety trial](https://www.npr.org/2026/08/26/nx-s1-5944781/meta-settlement-child-safety-lawsuit), [Axios — Meta agrees to $17 billion settlement in states' Facebook, Instagram lawsuit](https://www.axios.com/2026/08/26/meta-lawsuit-settlement-states-facebook), [CNBC — Meta $17 billion settlement mandates new safeguards for minors](https://www.cnbc.com/2026/08/28/new-meta-safeguards-teens.html), [TechCrunch — Meta's $18B child-safety deal hinges on age-verification tech that doesn't work well](https://techcrunch.com/2026/08/26/metas-18b-child-safety-deal-hinges-on-age-verification-tech-that-doesnt-work-well/), [France24 — Meta's teen safety deal runs into an unsolved problem: proving age](https://www.france24.com/en/live-news/20260828-meta-s-teen-safety-deal-runs-into-an-unsolved-problem-proving-age), [Al Jazeera — Meta's $18bn settlement: how social platforms will change for child users](https://www.aljazeera.com/features/2026/8/27/metas-18bn-settlement-how-social-platforms-will-change-for-child-users), [The Conversation — changes to Facebook and Instagram are key part of Meta's $17B settlement](https://theconversation.com/changes-to-facebook-and-instagram-are-key-part-of-metas-17b-settlement-with-the-states-over-harm-to-teens-290582)

### 21. "Made in USA" claim proliferation under tariff pressure, against a *declining* baseline of
consumer persuadability and a live 2026 FTC truthful-advertising crackdown (moderate confidence —
genuine gap versus PLS-SEM literature on origin labels specifically, but sits inside a very old
country-of-origin research tradition, and the sharpest baseline data point is now a year old, not
fresh)
- **Gap/question:** two 2026 trends are pulling in opposite directions on the same claim. On one side,
  tariffs are pushing more brands to advertise domestic origin than ever (retailers and manufacturers
  citing tariff exposure as a reason to lean into "Made in USA" positioning, echoed by a March 2026
  White House executive order, "Ensuring Truthful Advertising of Products Claiming to Be Made in
  America," directing the FTC to prioritize enforcement, followed by an actual FTC enforcement sweep in
  April 2026 — three settlements and two closing letters over U.S.-origin claims). On the other side, The
  Conference Board's own survey work (n=3,000 US adults) found the persuasive power of "Made in USA" on
  purchase intention fell 18% since 2022 — consumers are, if anything, growing more skeptical of the
  claim at the exact moment more companies are making it under enforcement scrutiny. The open question:
  does *awareness that "Made in USA" claims are being actively investigated/found false* (enforcement
  salience) function like a spillover-skepticism effect — making consumers discount even accurate,
  verifiable claims more heavily — and does claim *specificity* (a vague blanket "Made in USA" vs. a
  specific, checkable claim like "assembled in Ohio from US-sourced steel") moderate that discounting,
  the same vague/specific distinction TARIFF_PAPER's Study 1 already codes for price-increase-cause
  attribution, just applied to origin claims instead.
- **Why tractable soon, honest caveat included:** the regulatory hook (EO March 2026, FTC sweep April
  2026) is a live, ongoing enforcement priority, not a one-off event, so awareness of "Made in USA"
  claims being scrutinized is plausibly current and rising, not a settled backdrop. The honest caveat:
  the sharpest quantitative data point (the 18%-decline figure) comes from an August 2025 Conference
  Board report, over a year old as of tonight, not a fresh 2026 data point — this reads more as an
  already-existing baseline condition that the 2026 enforcement wave is landing on top of, rather than
  a single fresh event the way idea 7's Supreme Court ruling or idea 19's de minimis closure are. A
  WebSearch saturation check tonight for a PLS-SEM or academic-marketing treatment of this specific
  claim-specificity/enforcement-salience-skepticism mechanism came back empty — what exists is general
  country-of-origin/ethnocentrism research (a decades-old, heavily-studied tradition, unlike the newer
  gaps elsewhere in this file) and general AI-content-label/authenticity-trust studies, neither of
  which tests this specific "enforcement-salience discounts even true claims" mechanism.
- **Rough method sketch:** experimental (vignette) design fits well. Manipulate (1) claim specificity
  (blanket "Made in USA" vs. specific/verifiable sourcing detail) and (2) enforcement-salience priming
  (a news snippet about the FTC's Made-in-USA crackdown present vs. absent) in a 2x2, measuring
  perceived claim credibility as the mediator and purchase intention/willingness-to-pay premium as the
  outcome. Plausible moderator: general skepticism toward advertising, or tariff-policy awareness.
- **Target venue:** Journal of Consumer Marketing or Journal of Advertising — a country-of-origin-
  labeling study with a live regulatory-enforcement twist, distinct from TARIFF_PAPER's messaging-
  attribution focus and from idea 9's shrimp/provenance-certification design (that one is about a
  positive, official state-certification label; this one is about a legally-regulated but
  self-declared, non-certified origin claim under active-fraud-enforcement conditions — a different
  credibility mechanism).
- Leads (unverified, WebSearch only): [The Conference Board — US consumers less swayed by "Made in USA"](https://www.conference-board.org/press/consumers-less-swayed-by-made-in-america), [Fibre2Fashion — 18% decline in Made in USA influence since 2022](https://www.fibre2fashion.com/news/association-news/conference-board/18-decline-in-made-in-usa-influence-since-2022-tcb-survey-304582-newsdetails.htm), [Axios — why the "buy American" movement is fading for US consumers](https://www.axios.com/2025/08/11/buy-american-products-study), [White House — Ensuring Truthful Advertising of Products Claiming to Be Made in America](https://www.whitehouse.gov/presidential-actions/2026/03/ensuring-truthful-advertising-of-products-claiming-to-be-made-in-america/), [Global Policy Watch — FTC sweep on "Made in the USA" claims](https://www.globalpolicywatch.com/2026/04/ftc-sweep-on-made-in-the-usa-claims/), [Arnold & Porter — FTC launches Made in the USA enforcement sweep following Trump executive order](https://www.arnoldporter.com/en/perspectives/blogs/consumer-products-and-retail-navigator/2026/04/ftc-launches-made-in-the-usa-enforcement-sweep)

Both proposals only, per standing rule — nothing built, nothing committed to. Of the two, idea 20
(Meta settlement saturation check) is the one tonight's brief specifically asked for and is the
stronger: a real, confirmed-undupicated gap with a clean distinction from idea 13. Idea 21
(Made-in-USA) is real and undupicated at the specific mechanism level, but sits inside a much
older, heavily-trodden general literature (country-of-origin labeling), so Britton should weigh
novelty carefully before greenlighting. Also checked tonight and set aside: a Louisiana
coffee-roaster tariff-relief non-pass-through angle (coffee/cocoa tariff-exempted Nov 2025, but
retail prices still up 17-23% YoY as of tonight's search) — this is close enough to both idea 7's
price-stickiness mechanism and the coffee-roaster angle already explicitly rejected in this file's
2026-08-27 entry to not be a distinct new idea; and an AI-companion-chatbot/minors-safety angle
(FTC inquiry into Character.AI, OpenAI, Meta, Snap, Alphabet, xAI chatbots, open since Sept 2025;
California's SB 243 effective Jan 1, 2026) — real and adjacent to idea 20's Meta settlement, but
the FTC inquiry and state law are both about a year old already and the space is already crowded
with wrongful-death litigation and press coverage, reading as a weaker, less fresh hook than idea
20 tonight rather than a distinct addition.

## 2026-09-02

### 22. Tariff-refund windfall retention — corporate distribution decisions on IEEPA refunds as a live distributive-fairness test (moderate-high confidence — real and undupicated, but close enough to the existing tariff-messaging line to need explicit differentiation from idea 21)

- **Gap/question:** following the Supreme Court's February 2026 IEEPA ruling, the government has
  refunded roughly $100–168B in tariffs directly to importers (Walmart $2.9B, Target $994M, Apple
  ~$2.2B, Ford $1.3B, Home Depot $730M, Nike $684M, Amazon $640M). Sen. Warren sent public letters
  (mid-to-late August 2026) pressing seven companies to pass those refunds on to the consumers who
  actually paid the tariff-inflated prices. Corporate responses are now on the record and split:
  UPS/FedEx/DHL committed to rolling consumer refunds with dedicated portals; Amazon said refunds only
  in "limited circumstances" it can trace to specific customers; Walmart's CFO said refunds would go to
  earnings, not customers. This is a clean, currently-forming corpus of contrastive corporate
  statements on a live fairness question — distinct mechanism from idea 21 (which is about claims-
  credibility on "Made in USA" labeling, not about who keeps a refund).
- **Why tractable soon:** the refund wave and the Warren letters are both within the last few weeks;
  CFO statements are already quoted verbatim in press coverage and earnings-call transcripts, so a
  contrastive-statement corpus can be assembled now without waiting on more events to happen.
- **Rough method sketch:** antecedent = corporate refund-distribution decision/framing (full pass-
  through vs. partial/traceable-only vs. retain-as-earnings) → mediator = perceived distributive/
  procedural fairness (windfall-retention framing) → outcome = brand trust, repurchase intention, or
  willingness to boycott; candidate moderator = perceived corporate market power, or political
  ideology (flagged as a real confound risk, since tariff politics are partisan — worth Britton's
  attention if this moves forward). Data: Warren's letters and company replies, earnings-call
  transcripts, news coverage (NPR, CNN, Fortune, Newsweek).
- **Target venue:** *Journal of Consumer Affairs* (official journal of ACCI) — strong, specific fit
  for consumer-policy/distributive-fairness work; *Journal of Public Policy & Marketing* as the
  alternative for a more marketing-strategy framing.
- **Honest differentiation note (from the scouting session that found this):** this sits close enough
  to both the existing TARIFF_PAPER line and to idea 21 that it risks reading as a variation rather
  than a new idea — worth pitching to Britton explicitly as "windfall-retention fairness" (who keeps a
  refund) vs. idea 21's "claims-credibility" (is a labeling claim true) framing, so he can judge
  whether it's differentiated enough to run alongside idea 21 rather than instead of it.

### Refresh, not a new idea: idea 1/1a's ratepayer cost-shifting angle has new, sharper material

Idea 1a (Louisiana data-center ratepayer cost-shifting, first logged 2026-08-13/14, referenced several
times since) now has substantially fresher and more specific evidence than what's in the file already:
the Louisiana PSC fast-tracked Entergy Louisiana's application to triple gas plants (10 total, ~7.5 GW
— over 6x New Orleans peak demand) to power Meta's Hyperion data center in Richland Parish; regulators
recently **killed a subpoena** that would have forced Meta to disclose more about its plans/costs;
Union of Concerned Scientists and the Alliance for Affordable Energy now estimate ratepayers could see
**$8–13/month** increases, with hundreds of millions to billions in costs shifted onto non-beneficiary
customers; and the PSC's **final vote is set for December 16, 2026** — giving this a concrete,
near-term endpoint and a growing comment/advocacy corpus through fall 2026. This sharpens 1a's
transparency-withholding/distributive-injustice mechanism (the killed subpoena is a strong antecedent
candidate: perceived transparency-withholding by the utility/company → perceived distributive
injustice or regulatory capture → political trust erosion / support for rate-case intervention) with a
real news hook, rather than being a new numbered idea. Not logged as its own number — flagging so
whoever next picks up 1a doesn't have to re-search for what's changed since 08-14.

### Noted, not logged as a new idea: SpaceX Starbase Louisiana has substantial new corpus material

This session's SPACEX_LOUISIANA_PAPER note
(`SPACEX_LOUISIANA_PAPER/notes/2026-09-02-faa-docket-post-close-comment-batch-analysis.md`) and the
scouting pass both independently surfaced a lot of new material for the *existing* SpaceX line (idea
16, already logged 2026-08-25) rather than a new stream: the FAA's proposal to waive 13 environmental
laws for commercial launch licensing, a "Stop SpaceX" resident coalition, and — new since the FAA
docket closed — formal opposition filings from national environmental NGOs, SpaceX's own launch
competitors (Blue Origin, Rocket Lab, etc.), and a California state-agency coalition. Not logged as a
new numbered idea, since it's squarely corpus material for the already-existing, already-in-rotation
SPACEX_LOUISIANA_PAPER project, not a new research stream.

Idea 22 is a proposal only, per standing rule — nothing built, nothing committed to. Idea 20 (Meta
settlement) and idea 21 (Made-in-USA) remain from 09-01, still awaiting a greenlight call.

## 2026-09-03

### 23. Amazon's "secret ad-auction surcharge" FTC lawsuit — B2B deception exposure as a trust-spillover shock to consumer belief in "Sponsored" labels (high confidence — brand-new, three days old at time of scouting, no academic treatment exists yet)

- **Gap/question:** on August 31, 2026, the FTC and 22 state AGs sued Amazon, alleging that for 7+
  years Amazon told advertisers it ran a "second-price" Sponsored Products/Brands/Display auction
  (winner pays "one cent more than the next highest bidder") while in practice charging advertisers
  close to their own winning bid ~80% of the time — effectively a covert first-price auction,
  extracting what the complaint frames as tens of billions in extra ad spend from 1M+ brands/sellers.
  This is a B2B deception story on its face, but it opens an untested B2C question: when a platform is
  publicly revealed to have lied to *advertisers* about how its "Sponsored" listings are priced, does
  that spill over into *consumers'* trust that the "Sponsored" vs. organic distinction on the same
  search results page means anything — i.e., does institutional deception exposed at one level
  (advertiser-facing auction mechanics) erode belief in a disclosure label the same platform shows
  consumers? A saturation check found adjacent literature (influencer sponsorship-disclosure/trust; an
  arXiv paper on AI shopping agents discounting "Sponsored" labels) is about human endorsers or
  algorithmic agents, not a platform's own documented, litigated auction-deception as a spillover-
  distrust cue for ordinary consumers evaluating search results generally.
- **Why tractable soon:** the lawsuit is dated (Aug 31, 2026); the complaint quotes internal Amazon
  documents admitting disclosure would cause "irrevocable damage to advertiser trust"; Amazon's public
  rebuttal is already on record — a contrastive-statement corpus (FTC complaint language vs. Amazon's
  defense) exists today. Litigation will generate ongoing docket/press material as it proceeds.
- **Rough method sketch:** antecedent = awareness of the FTC's auction-deception allegations
  (news-vignette manipulable) → mediator = perceived platform integrity/institutional trust (distinct
  from ad-specific trust) → outcome = trust in "Sponsored"-labeled results specifically, general
  platform trust, purchase intention on Amazon vs. switching to Walmart. Candidate moderator: prior
  Amazon loyalty/Prime tenure. Study 1 (AI-assisted content analysis of complaint text, Amazon's
  response, social/press reaction) → Study 2 (PLS-SEM or vignette survey) — the usual two-study shape.
- **Target venue:** *Journal of Consumer Marketing* or *Journal of Retailing and Consumer Services*
  (retail-platform trust framing); *Journal of Public Policy & Marketing* as an alternate given the
  live FTC-enforcement angle.
- **Sources:** [FTC press release, Aug 31, 2026](https://www.ftc.gov/news-events/news/press-releases/2026/08/ftc-states-sue-amazon-over-secret-ad-surcharge-scheme), [TechCrunch](https://techcrunch.com/2026/08/31/ftc-accuses-amazon-of-running-a-secret-ad-surcharge-scheme-in-new-lawsuit/), [CNBC](https://www.cnbc.com/2026/08/31/amazon-ftc-lawsuit-advertisers.html), [Amazon's response](https://www.aboutamazon.com/company-news/amazon-ftc-sponsored-ads-lawsuit-response), [Marketing Dive](https://www.marketingdive.com/news/amazon-hid-surcharges-on-ad-auctions-alleges-ftc-complaint/829274/), [NPR](https://www.npr.org/2026/08/31/nx-s1-5950482/ftc-amazon-advertising-lawsuit)
- **Note:** a related, narrower angle (semiconductor Section 232 tariffs and silent price pass-through
  in electronics) was checked and explicitly ruled out as its own idea — same mechanism TARIFF_PAPER's
  Study 1 already codes for, just a new product category. Flagging only as a possible future
  corpus-extension for TARIFF_PAPER, not logged separately.

### 24. Louisiana's insurer premium-transparency mandates (HB148 "previous premium" disclosure, live now; Act 428's full rate-transparency report, effective Jan 1 2027) — a Louisiana-specific price-disclosure shock inside an active insurance-crisis narrative (high confidence — Louisiana-specific, dated, no PLS-SEM treatment found)

- **Gap/question:** Louisiana's property/auto insurance market has been in a well-documented
  affordability crisis (nonrenewals, insurer exits, coastal unavailability). Two new disclosure
  mandates are now live or imminent: HB148 already requires insurers, on 2026 renewals, to show the
  customer's *previous premium side-by-side with the new one* — a first-time forced comparison point;
  Act No. 428 (2025 Regular Session) goes further, requiring insurers to file an annual rate-
  transparency report breaking a premium down into loss/expense/profit shares, effective **January 1,
  2027**, with Commissioner Temple's implementing Bulletin 2026-05 already issued (March 2026). Open
  question: does forced premium-comparison and cost-component disclosure — landing inside an active
  "why is Louisiana insurance so broken" media narrative — increase perceived fairness/trust and
  shopping/switching intention, or backfire by making already-salient price increases feel more like
  betrayal (a distributive-fairness mechanism, in an untouched product category: annual-cycle,
  high-stakes, low-frequency insurance rather than retail/subscription/algorithmic pricing). A
  saturation check found the closest prior work is the UK FCA's 2016-era field trials on showing "last
  year's premium next to this year's" (UK-specific, pre-dates the Louisiana crisis narrative entirely)
  — no PLS-SEM or U.S./Louisiana marketing-journal treatment of this mechanism was found.
- **Why tractable soon:** HB148's comparison-disclosure is already appearing on real renewal notices
  this year (immediate corpus/survey-timing opportunity); Act 428's fuller mandate has a fixed Jan 1,
  2027 date (~4 months out), giving a genuine before/after window. Commissioner Temple, Triple-I, and
  the Louisiana Dept. of Insurance are all actively producing public commentary right now.
- **Rough method sketch:** antecedent = exposure to the previous-vs-new-premium disclosure (and/or the
  fuller cost-breakdown report), manipulable in a vignette or measured as real awareness in a survey of
  Louisiana homeowners. Mediators: perceived distributive fairness and perceived insurer transparency/
  trustworthiness as parallel candidates. Outcome: shopping/switching intention, trust in insurer,
  support for further LDI regulation. Moderator: prior nonrenewal experience or coastal-parish
  residence. PLS-SEM survey fits better than a TA-heavy Study 1, though a light Study 1 coding LDI
  bulletins, Triple-I/insurer statements, and news coverage could map the "crisis narrative vs.
  reform-is-working" framing split evident in coverage itself.
- **Target venue:** *Journal of Public Policy & Marketing* (regulatory-disclosure-mandate framing,
  consistent with several of Britton's other JPP&M-track ideas) or *Journal of Consumer Affairs* given
  the consumer-protection angle.
- **Sources:** [Insurance Journal — Louisiana insurers must disclose prior policy premiums under controversial new law](https://www.insurancejournal.com/news/southcentral/2025/07/15/831755.htm), [Insurance Journal — New law orders Louisiana insurers to show prior policy premiums](https://www.insurancejournal.com/magazines/mag-features/2025/08/04/834138.htm), [Live Insurance News](https://www.liveinsurancenews.com/louisiana-renewal-notices-higher/8572159/), [Insurance Business — Louisiana urges annual insurance market data in new rate transparency push](https://www.insurancebusinessmag.com/us/news/risk-compliance-legal/louisiana-urges-annual-insurance-market-data-in-new-rate-transparency-push-577417.aspx), [LDI Bulletin 2026-05 PDF](https://ldi.la.gov/docs/default-source/documents/legaldocs/bulletins/bul2026-05-cur-ratetransparencyrep.pdf), [Fox 8 — Louisiana homeowners still trapped in insurance crisis](https://www.fox8live.com/2026/06/02/louisiana-homeowners-still-trapped-insurance-crisis-hurricane-season-begins/), [Yahoo/Triple-I — reforms begin to deliver rate relief but challenges remain](https://finance.yahoo.com/healthcare/articles/triple-louisiana-insurance-reforms-begin-152700682.html)

### 25. NY's AI Transparency in Advertising Act (synthetic-performer disclosure mandate, effective June 9, 2026) as a specific stimulus for an AI-ad-trust study (moderate confidence — real, dated, state-mandated hook, but sits in the file's most crowded adjacent literature; logging with an explicit weakness flag rather than pushing it)

- **Gap/question:** NY's law (signed Dec 11, 2025, effective June 9, 2026) is the first state statute
  specifically requiring "conspicuous disclosure" when an ad features a synthetic/AI-generated
  performer — distinct from the FTC's general endorsement-rule enforcement (Operation AI Comply, 12+
  actions in 2026, treating undisclosed virtual-influencer endorsement as deceptive because "the
  audience is being asked to trust a relationship that does not exist"). The narrow open question: does
  a *mandated, standardized* synthetic-performer disclosure label (vs. a voluntary or ad-hoc AI-content
  notice) change perceived source credibility and purchase intention differently than the existing
  AI-disclosure literature has tested — echoing the "real mandate as stimulus" logic already used for
  ideas 11, 13, and 17.
- **Honest caveat (why this is the weakest of tonight's three):** the AI-ad-disclosure-and-trust space
  is, per this file's own repeated saturation checks (ideas 14, and 20's adjacent notes), already
  fairly active — a Tandfonline "Disclaimer! This Content Is AI-Generated" study, a ScienceDirect
  generative-AI-service-ads paper, an American Impact Review systematic lit review — and overlaps with
  idea 14's Coca-Cola AI-washing/booing entry. The differentiator (a state-mandated label for synthetic
  *performers* specifically, not general AI-generated content) is real but narrow, similar in shape to
  how idea 11 was flagged as "a narrower gap than it first looks."
- **Target venue:** *Journal of Advertising* or *Journal of Consumer Marketing*.
- **Sources:** [Dynamis LLP — AI Disclosure Rules 2026](https://www.dynamisllp.com/knowledge/ai-disclosure-in-2026-recent-developments-and-practical-steps-for-brands-and-influencers), [Duke Undergraduate Law Review — synthetic performers in digital advertising](https://www.dukeundergraduatelawreview.com/online-journal/4zpxec24o44zuz07rpgbexesztttyi), [Hollywood Branded — FTC AI influencer compliance](https://blog.hollywoodbranded.com/what-the-ftc-taught-hollywood-branded-about-ai-influencer-compliance), [thestacc.com — FTC AI Disclosure Rules 2026](https://thestacc.com/blog/ftc-ai-disclosure-rules-2026/)

Ideas 23-25 are proposals only, per standing rule — nothing built, nothing committed to. Also checked
tonight and explicitly not written up: multimodal AI thematic analysis (video/image coding) as an
idea-4/18 extension — real 2026 commercial momentum (ATLAS.ti multimodal support, Conveo AI-moderated
video interviews) but reads as a crowded, vendor-driven capability space without a sharp enough
academic-gap differentiator. No material found tonight that sharpens or refreshes any pre-existing
entry (unlike 09-02's 1a/SpaceX refreshes) — 23-25 are genuinely new mechanisms/objects. Ideas 20, 21,
22 remain from prior nights, still awaiting a greenlight call.
