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

Three separate kinds of precedent, worth citing together because they answer
three different reviewer objections:

1. **"AI in marketing research at all is legitimate."** Berger, Humphreys,
   Ludwig, Moe, Netzer & Schweidel (2020), *Journal of Marketing*, "Uniting
   the Tribes: Using Text for Marketing Insight" — the field's own flagship-
   journal legitimizing statement for automated text methods. Open with this
   citation in any methods section defending the general approach.
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
   published PhD dataset. Key finding, and genuinely useful for how we should
   run this: **code-level agreement is noisier than theme-level agreement**
   (hierarchical convergence) — individual codes vary session to session, but
   the higher-order themes those codes cluster into are stable. Structured
   multi-phase prompting outperformed generic one-shot prompting. Alignment
   measured via F1 score; consistency via bidirectional mapping across
   repeated sessions.

Practical implication of #3: **don't panic if two coding passes don't produce
identical codes.** That's expected and reported in the validating literature.
What has to converge is the theme layer, not the code layer — measure and
report agreement at both levels separately, and expect the theme-level number
to look better.

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
| AlGhamdi 2026 (Claude Code, e-commerce interviews) | F1 (code-level vs. theme-level) | code-level noisier, theme-level stable |
| Misra et al. 2026 (open-source Gemma2/Llama3.1, health interviews) | % "meaningful context" | ~45%, 22–39% duplicative |
| JMIR 2025 (GPT-4, clinical interviews) | % agreement | >80% descriptive/semantic, ~30% latent |

Expected pattern to plan the write-up around: **higher agreement on
descriptive/semantic/deductive coding, lower on latent/interpretive coding,
and theme-level agreement more stable than code-level agreement.** State this
plainly rather than being surprised by it mid-analysis.

**Also report, per Hill et al.'s explicit recommendation:** quote
verification (spot-check that quoted supporting text actually says what the
code claims) and error rates, not just an aggregate agreement number.

## Trustworthiness framing for the rigor paragraph

Lazarus et al. (2026, *Anatomical Sciences Education*) adapt the standard
qualitative trustworthiness criteria — credibility, dependability,
confirmability, transferability — specifically for AI-supported analysis.
(Paywalled — haven't pulled full operational detail per criterion yet; worth
a closer read before drafting the actual rigor paragraph, but the framework
itself is citable now as the structure to organize that paragraph around.)

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

- **General legitimacy of AI/text methods in marketing:** Berger et al. 2020 (JM); Arora, Chakraborty & Nishimura 2025 (JMR).
- **Reliability of LLM-coded TA specifically:** Hill et al. 2026 (PLOS Digital Health, Claude 4 Sonnet); AlGhamdi 2026 (IJQM, Claude Code).
- **Step-by-step method/protocol to cite as "following the protocol of":** Naeem, Smith & Thomas 2025; Goyanes, Lopezosa & Jordá 2025.
- **Trustworthiness/rigor framework:** Lazarus et al. 2026.
- **Reflexivity/ethics of AI in qualitative work:** Xu 2026; Cheah 2025 (if netnography).
- **Precedent in marketing's own top journals for text-as-data generally:** Tirunillai & Tellis 2012, 2014; Netzer et al. 2012.
- **Know the opposition, preempt in methods:** Nguyen-Trung 2025 (Big-Q/reflexivity objection — address head-on, don't get blindsided).

Full bibliographic details for all of the above are already compiled in
`AI_Assisted_TA_Shared_Method.md` and `AI_Thematic_Analysis_Reading_List.csv`
in this same folder — this doc adds the two new tool-specific validation
papers (Hill et al., AlGhamdi) and generalizes the workflow/reporting
standard so it's not locked to the two papers currently in flight.
