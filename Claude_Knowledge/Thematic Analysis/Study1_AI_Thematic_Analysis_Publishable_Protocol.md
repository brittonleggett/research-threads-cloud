# Study 1: AI-Assisted Thematic Analysis — a reusable, publishable protocol

Britton's ask (2026-08-11): figure out how to actually do an AI thematic
analysis and how to report it so it gets published, so it can become a
**standing Study 1 template** — qualitative/thematic mechanism-identification,
followed by Study 2 (survey or experiment) — for future papers generally, not
just the two currently in flight (CCS, Tariff — see
`AI_Assisted_TA_Shared_Method.md`, which this doc generalizes from and adds to).

This is the reusable version. When starting a new paper with this design,
copy this doc's structure, fill in the paper-specific columns (data source,
theory frame, RQ), and go.

## Why this is publishable now (the legitimacy stack)

Four separate kinds of precedent, worth citing together because they answer
four different reviewer objections. **Read the opening-citation call below
before drafting a methods section** — it changed as of 2026-08-13.

0. **"Is it legitimate to use GenAI to help analyze *qualitative* data in
   consumer/marketing research, specifically?"** Epp & Humphreys (2025,
   *Journal of Consumer Research*), "Collaborating with Generative AI in
   Consumer Culture Research" — **this is now the opening citation, ahead of
   Berger et al. below, for any Study 1 that is a thematic/qualitative
   analysis** (as opposed to a quantitative text-mining exercise). Reasoning:
   JCR is the field's own home journal for qualitative/consumer-culture work;
   the paper is built from interviews with researchers actually doing
   GenAI-assisted qualitative analysis (not automated text-mining generally);
   and it hands you a ready-made reporting checklist — four principles
   (transparency, provenance, privacy, verisimilitude) with a worked example
   of documenting prompts and outputs in a web appendix. It's already being
   cited and explicitly followed by other applied papers (Pueschel, Hao &
   Schmitt 2026, *JBR*, say outright they "follow" its guidelines). Berger et
   al. is the better opener when Study 1 is quantitative text-mining rather
   than qualitative coding — keep both citations, just in the order that
   matches what Study 1 actually is.
1. **"AI in marketing research at all is legitimate."** Berger, Humphreys,
   Ludwig, Moe, Netzer & Schweidel (2020), *Journal of Marketing*, "Uniting
   the Tribes: Using Text for Marketing Insight" — the field's own flagship-
   journal legitimizing statement for automated text methods generally (topic
   models, dictionaries, embeddings, classification). Second citation for a
   thematic-analysis methods section; first citation for a text-mining one.
   Herhausen et al. (2025, *JBR*), "From Words to Insights" is a useful
   companion here too — a JBR framework paper comparing topic
   models/dictionaries/supervised ML/LLMs with an explicit author/reviewer
   checklist (their Table 4) for method-choice justification.
2. **"LLM-coded qualitative analysis specifically is reliable enough to
   trust."** Hill et al. (2026, *PLOS Digital Health*) — blinded comparison,
   Claude 4 Sonnet reached 93.5% agreement / Gwet's AC1 = 0.93 against human
   analysts (humans: 92.7% / AC1 = 0.92) on deductive coding — non-inferior,
   arguably superior. This is the number to cite when a reviewer asks "how do
   we know the AI coded this correctly."
3. **"Claude Code specifically, not just chat-based LLMs, is validated."**
   AlGhamdi (2026, *IJQM*), "From Code Variability to Theme Convergence:
   AI–Human Alignment in Thematic Analysis With Claude Code" — compared 4
   independent Claude Code sessions against a human/NVivo baseline from a
   published PhD dataset (a 2012 doctoral study on e-commerce). Two prompting
   strategies were tested — general prompts vs. structured multi-phase
   prompts. Key finding, and genuinely useful for how we should run this:
   **code-level agreement is noisier than theme-level agreement**
   (hierarchical convergence) — individual codes vary session to session, but
   the higher-order themes those codes cluster into are stable. Structured
   multi-phase prompting outperformed generic one-shot prompting. Alignment
   measured via F1 score; consistency via bidirectional mapping across
   repeated session pairs. **Access note (2026-08-13):** the full text is
   paywalled — Sage returned a 403 on direct fetch. Everything in this
   paragraph is confirmed at the abstract level via search, which matches and
   confirms what this doc already said; the specific F1 numbers themselves
   are not confirmed and shouldn't be quoted as if they were.

Practical implication of #3: **don't panic if two coding passes don't produce
identical codes.** That's expected and reported in the validating literature.
What has to converge is the theme layer, not the code layer — measure and
report agreement at both levels separately, and expect the theme-level number
to look better. A second, independent paper backs this same pattern up one
level removed: Nyaaba et al. (under review, arXiv:2601.11850 — see "Related
finding" below) found that verbatim/in-vivo codes needed far less human
correction than higher-order gerund/categorical codes, which is the same
"trust the raw layer more, expect to rework the abstracted layer" shape.

## The branding decision (make this call explicit, every time, before coding starts)

Braun & Clarke's thematic analysis splits into two incompatible camps:

- **"Big Q" reflexive TA** — interpretive, quality = researcher reflexivity,
  explicitly *rejects* reliability statistics (Cohen's Kappa, etc.) as a
  quality marker.
- **"Small q" / coding-reliability TA** — codebooks, multiple coders,
  agreement statistics.

**Default to small-q / coding-reliability TA whenever the design reports a
reliability statistic** (which it should, per Hill et al./AlGhamdi above) —
or cite Naeem et al.'s "systematic thematic analysis" framing as a middle
ground. Reporting a Kappa/AC1/F1 while calling the method "reflexive TA" is
the single most common reviewer-bait mistake in this literature — a reviewer
trained in reflexive TA (Nguyen-Trung 2025's GAITA paper voices exactly this
objection) will catch the inconsistency immediately. Decide the label first,
then make sure everything downstream is consistent with it.

**How high the stakes on this are, confirmed 2026-08-13:** Karhu, Smolander &
Kasurinen (2026, arXiv:2605.00922) report that 419 qualitative researchers —
including Braun and Clarke themselves — signed a statement rejecting
generative AI for reflexive/Big-Q qualitative research (citing Jowsey, Braun,
Clarke, Lupton & Fine 2025, "We Reject the Use of Generative Artificial
Intelligence for Reflexive Qualitative Research," *Qualitative Inquiry* —
reported secondhand via Karhu et al., not independently fetched). Karhu et
al. name using inter-rater reliability, a small-q concept, to validate AI
output inside a Big-Q/reflexive framework as textbook "methodological
incongruence." That is exactly the mistake flagged above — it isn't a
stylistic quibble, it's the difference between a design the field's own
method-founders would recognize as legitimate and one they've publicly
disowned. See "Know the opposition" further down for their full argument.

## The six-phase engine (generalizable — fill in brackets per project)

**Phase 0 — Optional quantitative triage.** Run a term-co-occurrence/topic
pass (e.g. JMP Text Explorer) across the raw corpus before touching the LLM,
purely to sanity-check/seed the coding frame. Report as a triangulating
quantitative pass, never as "the thematic analysis" itself.

**Phase 0.5 — Brief the model.** Give it the research question, data
type/source, and theoretical frame. Have it summarize the brief back; correct
until accurate before coding starts. This is also where you declare the TA
variant (small-q vs. Naeem's systematic framing) so the model's outputs match
the label you'll report.

**Phase 1 — Coding.**
- Deductive: *"This is my [data]. Code it deductively using [framework] to
  answer [RQ]."*
- Inductive: *"This is my [data]. Code it inductively to capture [aspect] and
  answer [RQ]."*
- **Use structured multi-phase prompting, not a single generic prompt** —
  AlGhamdi's finding was that this materially improves alignment.
- Optional keyword-triage first pass on large volumes: Naeem et al.'s "6 Rs"
  (realness, richness, repetition, rationale, repartee, regal).
- **Known failure mode:** the model stays semantic/surface and misses latent
  meaning (sarcasm, in-group slang, unstated context) unless that context is
  fed explicitly. Plan to manually recover latent/interpretive codes — expect
  and report lower agreement here specifically (see validation table below).

**Phase 2 — Theme generation.** *"These are [inductive/deductive] codes and
data extracts. Cluster them, explore meaning patterns, and develop candidate
themes."* Ask for a thematic map. Naeem et al.'s "4 Rs of theming"
(reciprocal, recognizable, responsive, resourceful) is a usable rubric.

**Phase 3 — Reviewing themes: human-only, no AI.** Every validating paper in
this literature drops the model at this step — it lacks the recursive,
contextual judgment reviewing requires. Non-negotiable.

**Phase 4 — Defining and naming.** *"This is one of my themes [X]; write a
brief definition explaining its key takeaway."* Then: *"Given this
definition, suggest a few concise names."* Useful for generating options;
final choice is the researcher's, always.

**Phase 5 — Write-up.** AI for proofreading/language only, never analytic
content at this stage. **Disclose AI use explicitly in methods +
acknowledgements** — expected practice now, not optional, and increasingly
what reviewers screen for regardless of whether the results hold up.

## Validation plan (run before the real coding pass, every time)

Pick a pilot subsample, code it manually AND with the model, compute
agreement **at both the code level and the theme level separately**, and
report both — don't borrow someone else's published number, it varies by
model and by how semantic vs. latent the themes are:

| Study | Agreement measure | Result |
|---|---|---|
| Hill et al. 2026 (Claude 4 Sonnet, healthcare focus group, deductive) | Gwet's AC1 | 0.93 (vs. human 0.92) |
| AlGhamdi 2026 (Claude Code, e-commerce interviews, 2012 PhD dataset vs. NVivo) | F1 (code-level vs. theme-level) | code-level noisier, theme-level stable (exact F1 not confirmed — paywalled) |
| Misra et al. 2026 (open-source Gemma2/Llama3.1, health interviews) | % "meaningful context" | ~45%, 22–39% duplicative |
| JMIR 2025 (GPT-4, clinical interviews) | % agreement | >80% descriptive/semantic, ~30% latent |
| Qian, Gong & Xu 2026 (*JRCS*; OpenAI o4-mini classifying BERTopic clusters into generic frames, 47K YouTube/Instagram comments) | LLM consensus rate (10 repeated runs) / frame-consistency rate (LLM vs. human) | 0.94 consensus / 0.98 consistency at the coarse (generic-frame) level; finer issue-specific frames needed manual merge/review |

Expected pattern to plan the write-up around: **higher agreement on
descriptive/semantic/deductive coding, lower on latent/interpretive coding,
and theme-level (or coarse-category) agreement more stable than code-level
(or fine-category) agreement.** Qian et al. reproduce this same shape one
level removed from thematic analysis proper — worth citing as a second,
methodologically different confirmation of the general pattern, not just
AlGhamdi's. State this plainly rather than being surprised by it mid-analysis.

**Also report, per Hill et al.'s explicit recommendation:** quote
verification (spot-check that quoted supporting text actually says what the
code claims) and error rates, not just an aggregate agreement number.

## Trustworthiness framing for the rigor paragraph

Lazarus, Zhao, Gibson, Martinez-Maldonado & Stephens (2026, *Anatomical
Sciences Education*, 19, 330–337) adapt the standard qualitative
trustworthiness criteria — credibility, dependability, confirmability,
transferability — specifically for AI-supported analysis. **Still paywalled
as of 2026-08-13** (Wiley returned 402 Payment Required on direct fetch; a
ResearchGate mirror and a QUT ePrints listing exist but both also blocked the
fetch) — the per-criterion operational detail Britton would need for an
actual rigor paragraph is *not* independently confirmed here. What the
search-level abstract/summary genuinely supports, and is safe to cite at this
level of specificity:

- **Core argument:** AI vendors market "efficiency" and "bias-free" analysis
  as though these were self-evidently good for qualitative rigor; Lazarus et
  al. argue this framing risks violating core tenets of qualitative rigor
  *unless* trustworthiness is deliberately built back in — i.e., don't let a
  tool's marketing copy substitute for a rigor argument.
- **The four criteria, generic definitions (not yet AI-specific
  operationalization):** credibility maps to internal validity, established
  through triangulation, multiple perspectives, or participant/member
  validation; dependability is established through rigorous, documented data
  collection and analysis procedures. (Confirmability and transferability
  appear in the same four-part frame but no further operational detail
  surfaced in what's accessible.)
- **Framing stance:** they position AI-supported analysis as needing to be a
  *collaborative* effort that combines AI's strengths with human judgment —
  consistent with this doc's overall approach, not in tension with it.

**Bottom line: the framework (the four named criteria) is citable now as the
structure to organize the rigor paragraph around, but don't attribute
specific per-criterion AI operationalizations to Lazarus et al. that weren't
actually confirmed here.** If Britton needs the real per-criterion detail
before drafting that paragraph, the next step is an institutional-access
pull of the actual PDF (library proxy, interlibrary loan, or emailing the
corresponding author), not another web-search pass — search snippets appear
to have already been exhausted for this one.

## Which rhetorical stance to write into (Paulus, Lester & Davis 2026)

Paulus, Lester & Davis (2026, *AI & Society*, 41, 1737–1748), "The
Construction of the Role of AI in Qualitative Data Analysis in the Social
Sciences" — read in full 2026-08-13, this is genuinely worth its own section
rather than a citation-stack line, because it answers a question this
protocol has been answering by instinct rather than by naming explicitly:
*which way of talking about AI's role in a methods section is safest?*

The authors ran a discourse analysis on 29 peer-reviewed papers that use or
propose GenAI for QDA, coding how each one frames the human/AI relationship.
They found five recurring stances:

1. **"QDA is inherently problematic"** — papers frame qualitative work itself
   (slow, subjective, labor-intensive) as the problem AI solves, quietly
   recasting qualitative research's actual epistemological strengths as
   defects. **Avoid this framing** — it's the stance most likely to read as
   naive or hostile to a qualitative-methods-literate reviewer, and it's not
   even accurate to how this protocol treats human interpretive work.
2. **"QDA is easily, and will inevitably be, automated"** — treats coding and
   theming as basically solved by AI, with an undertone of inevitability
   ("the revolution is here"). **Avoid this framing too** — it overclaims,
   and it's the stance that provoked the Jowsey et al. 419-researcher
   rejection statement (see "Know the opposition" below).
3. **"AI will disrupt methods without (immediately) replacing humans"** — AI
   is powerful and destabilizing, but humans remain the last check. Better
   than 1–2, but still centers AI as the primary actor with humans as a
   backstop/QA function rather than as the analyst.
4. **"AI-human hybrid methods are the future"** — AI and humans are
   co-analysts in a structured, mutually-checked workflow; human judgment is
   foregrounded as constitutive, not corrective. **This is the stance this
   protocol's six-phase engine already matches, and the one to write
   explicitly into the methods section.** It's also the stance the strongest
   validating literature actually uses: AlGhamdi's framing of AI sessions as
   "an independent analytical perspective... points of methodological
   triangulation," and the empirical precedent below (Nyaaba et al.) both
   describe hybrid workflows, not automation.
5. **"De-centering ethical concerns and model limitations"** — ethics
   (hallucination, bias, environmental/labor cost, data privacy) get
   mentioned but pushed to the end of the paper and treated as minor,
   temporary caveats rather than live constraints on the design. **Avoid
   this pattern specifically** — don't let the ethics paragraph become an
   afterthought; the "netnography / data-collection ethics checklist" below
   and the disclosure requirements in Phase 5 exist precisely so this
   doesn't happen by default.

**The call:** this protocol's existing framing (six-phase human-AI engine,
Phase 3 always human-only, structured multi-phase prompting, explicit
disclosure) already lines up with stance 4 — it just wasn't named that way
before. Write the methods section explicitly into stance-4 language: AI as
co-analyst inside a structured, human-supervised, auditable workflow, not as
an automation layer that "solves" qualitative research's inherent
slowness (stance 1) or as an inevitability humans must simply adapt to
(stance 2).

**Empirical precedent for what stance 4 looks like in practice:** Nyaaba,
SungEun, Apam, Acheampong, Dwamena & Zhai (under review, arXiv:2601.11850),
"Human–AI Collaborative Inductive Thematic Analysis" — read in full
2026-08-13 (freely available, full text obtained). Three qualitative
researchers each used a purpose-built GPT-4-based inductive-TA tool on
Ghanaian teacher-education interview transcripts, with every AI output kept
as provisional and auditable. Findings, useful beyond the stance point:

- Researchers exercised epistemic authority through five recurring actions —
  **modification, deletion, rejection, insertion, commenting** — a usable
  vocabulary for documenting exactly *how* human oversight happened, not just
  asserting that it did.
- **Verbatim/in-vivo codes were consistently the most trusted layer**;
  gerund-based and categorical (higher-abstraction) codes needed the most
  human correction — the same "raw layer more reliable, abstracted layer
  needs rework" pattern AlGhamdi found at the code-vs-theme level.
- They quantified this: across three coders, total substantive human
  interventions per transcript were 15, 15, and 8 — a citable example of
  what "human-in-the-loop" looks like as an actual count, not just a claim.
- Caveat: this is a preprint **under review, not yet peer-reviewed** (listed
  in the reading list as arXiv 2601.11850 with a placeholder title/author —
  the real title is "Human–AI Collaborative Inductive Thematic Analysis: How
  AI Guides Analysis and Researchers Reclaim Interpretive Authority," authors
  as above, target outlet abbreviated "JDEM" in the manuscript). Cite as a
  preprint, not as settled peer-reviewed literature.

## Know the opposition (strengthened 2026-08-13)

The existing "opposition" citation was Nguyen-Trung (2025) — useful, but not
the strongest version of the objection. Two sources read in full this pass
sharpen it considerably:

**Karhu, Smolander & Kasurinen (2026), arXiv:2605.00922, "To Vibe Research or
Not to Vibe Research? Generative AI in Qualitative Research"** — read in full
(freely available). Their core framework is the same small-q/Big-Q split
this protocol already uses, which is itself a useful confirmation that the
branding decision above is the right axis to be arguing on. Their specific
objections, in order of how likely a reviewer is to raise them:

1. **Methodological incongruence** — using inter-rater reliability (a
   small-q metric) to validate AI output inside a Big-Q/reflexive framework
   is internally inconsistent. This protocol is immune to this specific
   objection *only if* the small-q/coding-reliability branding decision is
   made explicitly and consistently, which is exactly why that decision gets
   flagged first in this doc, every time.
2. **AI cannot be reflexive** — generative AI produces statistically likely
   text, not reflexive meaning-making; it cannot occupy the researcher's
   subjective, positioned stance that Big-Q/reflexive TA requires as a
   feature, not a bug.
3. **Ethical cost of the AI supply chain** — environmental cost and labor
   exploitation (citing Miceli et al. 2025 on data-worker conditions) are
   treated by Karhu et al. as a *first-order* objection, not an afterthought
   — directly the opposite of the Paulus et al. "de-centering ethics" stance
   flagged above as something to avoid replicating.
4. **The 419-researcher rejection statement** (Jowsey, Braun, Clarke, Lupton
   & Fine 2025, *Qualitative Inquiry* — cited secondhand via Karhu et al.,
   not independently fetched) is their sharpest citation: the creators of
   thematic analysis itself, plus 417 others, formally rejecting GenAI for
   reflexive/Big-Q qualitative research. This is the single most credible
   version of the opposition case available and should be named directly in
   any methods section's positioning paragraph, not danced around.

Karhu et al.'s own bottom line is close to this protocol's: generative AI is
plausible for small-q, coding-reliability qualitative research (their words:
"hallucinations can be managed... using quantitative metrics, such as
intercoder reliability") but they remain skeptical of AI for Big-Q research
specifically. That is not a rejection of this protocol's approach — it's a
confirmation of the branding decision's stakes, from the strongest possible
version of the opposing camp.

## Ethics / data-collection checklist (when Study 1's corpus involves human-generated text)

1. Public data, no direct interaction with posters → informed consent
   generally not required (confirm current platform ToS before scraping).
2. Pseudonymize usernames.
3. Lightly edit quoted text to blunt reverse-searchability.
4. Data minimization — collect only what the RQ needs.
5. Document every AI prompt used — audit trail, disclosed in methods.
6. Bias-check the AI's coding specifically against a manual subsample — this
   is where sarcasm, in-group slang, and non-mainstream framing get missed.
7. Keep a reflexive/audit journal regardless of TA branding.

(Not all of this applies when Study 1's corpus is corporate documents rather
than human subjects' text — see the CCS-vs-Tariff divergence table in
`AI_Assisted_TA_Shared_Method.md` for how that call gets made.)

## The Study 1 → Study 2 handoff (the part that makes this a repeatable design, not a one-off)

The pattern Britton wants standardized: Study 1 (this protocol) identifies or
validates a **mechanism, typology, or messaging dimension** inductively/
deductively from real-world text; Study 2 is a confirmatory survey or
experiment (his native PLS-SEM chain+moderator shape — see
[[user_research_corpus]]) that tests it causally/quantitatively. Concretely:

- Study 1's output should be a **small number of named, defined themes** —
  these become either (a) constructs to measure in a survey, or (b) levels/
  conditions to manipulate in an experimental vignette.
- Write Study 1's themes with Study 2 already in mind: a theme that can't be
  turned into a scale item or a manipulable vignette condition isn't doing
  its job in a two-study paper, even if it's analytically interesting.
- The methods section should say explicitly that Study 1 grounds Study 2 —
  reviewers reward showing the qualitative work did real theoretical labor,
  not just decorative color before "the real (quantitative) study."

## Citation stack, organized by the objection each one answers

- **"Is doing AI-assisted qualitative/thematic analysis legitimate at all, in
  a marketing/consumer-research context specifically?"** Epp & Humphreys 2025
  (JCR) — open with this one; see legitimacy-stack item 0 above for why.
- **General legitimacy of AI/text methods in marketing/business research
  more broadly:** Berger et al. 2020 (JM); Herhausen et al. 2025 (JBR, with
  author/reviewer checklist); Arora, Chakraborty & Nishimura 2025 (JMR).
- **Reliability of LLM-coded TA specifically:** Hill et al. 2026 (PLOS
  Digital Health, Claude 4 Sonnet); AlGhamdi 2026 (IJQM, Claude Code —
  abstract-confirmed, full text still paywalled); Qian, Gong & Xu 2026 (JRCS,
  0.94 consensus / 0.98 consistency at coarse-category level, adjacent ML
  pipeline not thematic analysis proper, still a useful second data point).
- **Applied precedent — a marketing/consumer-behavior journal actually
  publishing a hybrid human-GenAI qualitative design:** Pueschel, Hao &
  Schmitt 2026 (JBR — closest methodological cousin to this protocol: manual
  NVivo thematic analysis run in parallel with NotebookLM/ChatGPT, explicitly
  following Epp & Humphreys' guidelines); Qian, Gong & Xu 2026 (JRCS).
- **Step-by-step method/protocol to cite as "following the protocol of":**
  Naeem, Smith & Thomas 2025; Goyanes, Lopezosa & Jordá 2025.
- **Trustworthiness/rigor framework:** Lazarus et al. 2026 (framework citable
  now; per-criterion AI-specific operationalization still not confirmed —
  see "Trustworthiness framing" section above).
- **Which rhetorical stance to write the methods section into:** Paulus,
  Lester & Davis 2026 (AI & Society) — write into their stance 4 ("AI-human
  hybrid methods are the future"), not stances 1, 2, or 5.
- **Reflexivity/ethics of AI in qualitative work:** Xu 2026; Cheah 2025 (if
  netnography).
- **Empirical precedent for what human epistemic authority looks like in
  practice (five analytic actions, quantified):** Nyaaba et al. (under
  review, arXiv:2601.11850) — cite as a preprint, not settled literature.
- **Precedent in marketing's own top journals for text-as-data generally:**
  Tirunillai & Tellis 2012, 2014; Netzer et al. 2012.
- **Know the opposition, preempt in methods:** Nguyen-Trung 2025 (Big-Q/
  reflexivity objection); Karhu, Smolander & Kasurinen 2026 (arXiv:2605.00922
  — sharper version: methodological-incongruence argument, AI-can't-be-
  reflexive argument, AI-supply-chain-ethics argument, and the Jowsey et al.
  2025 419-researcher rejection statement — cite that last one as reported
  via Karhu et al., not independently verified).

Full bibliographic details for all of the above are already compiled in
`AI_Assisted_TA_Shared_Method.md` and `AI_Thematic_Analysis_Reading_List.csv`
in this same folder — this doc adds the two original tool-specific validation
papers (Hill et al., AlGhamdi) plus, as of 2026-08-13, Epp & Humphreys,
Herhausen et al., Pueschel/Hao/Schmitt, Qian/Gong/Xu, Paulus/Lester/Davis,
Nyaaba et al., and Karhu/Smolander/Kasurinen, and generalizes the
workflow/reporting standard so it's not locked to the two papers currently
in flight.
