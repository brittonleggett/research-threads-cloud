# AI-Assisted Thematic/Content Analysis — Shared Method (CCS paper + Tariff paper)

Synthesized from: Jayawardene & Ewing (2026, GAATA, *IJMR*); Turobov, Coyle & Harding (2024,
arXiv:2405.08828); Xu (2026, *IJQM*); Naeem, Smith & Thomas (2025, *IJQM*); Cheah (2025,
*IJQM*); Kozinets & Seraj-Aksit (2024, *JMM*); Misra et al. (2026, *IJQM*); Goyanes, Lopezosa
& Jordá (2025, *Quality & Quantity*). Full citation list at the bottom.

## The branding decision (read this before doing anything else)

Braun & Clarke's TA splits into two incompatible camps:

- **"Big Q" reflexive TA** — interpretive, quality = researcher reflexivity, explicitly
  *rejects* reliability statistics (Cohen's Kappa etc.) as a quality marker.
- **"Small q" / coding-reliability TA** — codebooks, multiple coders, agreement statistics.

Both papers end in confirmatory quant work (CCS → PLS-SEM; tariff Study 1 feeds vignette
stimuli for a PLS-SEM/PROCESS experiment). **Use small-q / coding-reliability TA for both
Study 1s, branded honestly as that** (or cite Naeem et al.'s "systematic thematic analysis"
framing) — not "Braun & Clarke reflexive TA." Reporting a Kappa while calling it reflexive TA
is the single most common reviewer-bait mistake in this literature.

**How bad the mistake can get, confirmed 2026-08-13:** Karhu, Smolander & Kasurinen (2026,
arXiv:2605.00922, "To Vibe Research or Not to Vibe Research?") report that 419 qualitative
researchers — including Braun and Clarke themselves, thematic analysis's own creators —
signed a statement rejecting generative AI for reflexive/Big-Q qualitative research (citing
Jowsey, Braun, Clarke, Lupton & Fine, 2025, "We Reject the Use of Generative Artificial
Intelligence for Reflexive Qualitative Research," *Qualitative Inquiry* — this citation is
reported secondhand via Karhu et al., not independently verified against the original). Karhu
et al. name using inter-rater reliability (a small-q concept) to validate AI performance inside
a Big-Q/reflexive framework as "a clear example of methodological incongruence" — precisely the
mistake this doc has been warning against. That makes the branding decision above not a stylistic
nicety but the difference between a citable design and one the method's own founders have
publicly disowned. See the Publishable Protocol doc's new "know the opposition" section for
more detail on their specific objections.

## The shared workflow (six phases, both papers use the identical engine)

**Phase 0 — Optional quantitative triage (JMP Text Explorer, Topic Analysis).**
Run rotated-SVD topic analysis across the full raw corpus before touching the LLM. This is
statistical term-co-occurrence clustering, not semantic understanding — use it to see what
large-scale clusters exist and to sanity-check/seed the coding frame, not as thematic
findings in their own right. Report it as a triangulating quantitative pass, never as "the
thematic analysis."

**Phase 0.5 — Brief the LLM.** Give it: research question, data type/source, theoretical
frame (CCS: signaling theory + greenwashing/skepticism; tariff: dual entitlement + prospect
theory + psychological reactance), and which TA variant is in use. Have it summarize back;
correct until accurate before coding starts.

**Phase 1 — Coding.**
- Deductive prompt pattern: *"This is my [data]. Code it deductively using [framework] to
  answer [RQ]."*
- Inductive prompt pattern: *"This is my [data]. Code it inductively to capture [aspect] and
  answer [RQ]."*
- Optional keyword-triage pass first on large volumes (Naeem et al.'s "6 Rs": realness,
  richness, repetition, rationale, repartee, regal) before full coding.
- **Known failure mode:** LLMs stay semantic/surface and miss latent meaning (sarcasm,
  in-group slang, context) unless you feed that context explicitly. Expect to manually
  recover latent/interpretive codes yourself, especially for CCS's Reddit-style discourse.

**Phase 2 — Theme generation.** *"These are [inductive/deductive] codes and data extracts.
Cluster them, explore meaning patterns, and develop candidate themes."* Ask for a thematic
map. Naeem et al.'s "4 Rs of theming" (reciprocal, recognizable, responsive, resourceful) is
a usable rubric for judging candidates.

**Phase 3 — Reviewing themes: human-only, no AI.** Xu (2026) deliberately dropped the LLM at
this phase — it lacks the recursive, contextual judgment reviewing requires. This is the
non-negotiable step every paper in this literature keeps human.

**Phase 4 — Defining and naming.** *"This is one of my themes [X]; write a brief definition
explaining its key takeaway."* Then: *"Given this definition, suggest a few [concise] names."*
Genuinely useful for generating options; final choice is the researcher's.

**Phase 5 — Write-up.** AI for proofreading/language only, not analytic content. Disclose AI
use explicitly in methods + acknowledgements — expected practice now, not optional.

## Validation plan (do this before the real run, for both papers)

Pick a pilot subsample, code it manually AND with the LLM, compute agreement, and report it.
Don't borrow someone else's number — it varies hugely by model and by semantic-vs-latent
themes:

| Study | Agreement measure | Result |
|---|---|---|
| GAATA (GPT-class, consumer app reviews, semantic-heavy) | Cohen's Kappa | 0.94 |
| Misra et al. (open-source Gemma2/Llama3.1, health interviews) | % "meaningful context" | ~45%, 22–39% duplicative |
| JMIR (GPT-4, clinical interviews) | % agreement (Kappa not applicable to their design) | >80% descriptive/semantic, ~30% latent |
| Qian, Gong & Xu 2026 (*JRCS*; OpenAI o4-mini classifying BERTopic clusters into framing categories, YouTube/Instagram comments) | LLM consensus rate (10 repeated runs) / frame-consistency rate (LLM vs. human) | 0.94 consensus / 0.98 consistency at the *generic-frame* level — issue-specific frames needed manual review |

Expect — and plan the write-up to say so — lower agreement on latent/interpretive codes than
semantic ones. Qian et al.'s pattern fits the same shape one level up: coarse (generic-frame)
classification agrees almost perfectly across repeated runs and against humans; finer-grained
(issue-specific) classification did not, and required a human merge/review pass before the
authors trusted it — consistent with AlGhamdi's code-vs-theme-level finding above.

## Netnography / data-collection ethics checklist

(From Cheah 2025 + Kozinets & Seraj-Aksit's actual Reddit practice — applies most directly to
CCS's consumer-discourse scrape; tariff's Study 1 is corporate documents, not human subjects,
so most of this is CCS-specific, but the AI-bias-check item applies to both.)

1. Public data, no direct interaction with posters → informed consent generally not required
   (confirm current platform ToS before scraping)
2. Pseudonymize usernames
3. Lightly edit quoted text to blunt reverse-searchability
4. Data minimization — collect only what the RQ needs, not full user histories
5. Document every AI prompt used — audit trail, disclosed in methods
6. Bias-check the AI's coding specifically (not just your own) against a manual subsample —
   this is where sarcasm, in-group slang, and non-mainstream framing get missed
7. Keep a reflexive/audit journal regardless of TA branding

## Where the two papers diverge (and should)

| | CCS Study 1 | Tariff Study 1 |
|---|---|---|
| Data source | Consumer-generated social media discourse (Reddit, likely) | Corporate-generated communications (press releases, earnings calls, corporate social posts) |
| Method label | AI-assisted netnography (Kozinets & Seraj-Aksit precedent) | AI-assisted thematic/content analysis of corporate messaging (not netnography — no community being observed) |
| Purpose | Characterize public discourse/skepticism to motivate and inform Study 2 constructs | Build an inductive typology of messaging strategies to ground realistic Study 2 vignette stimuli |
| IRB | Exempt — public data, no human-subjects contact | Exempt — 45 CFR 46.102(e), public documents, no human-subjects contact |
| Theory frame | Signaling theory, greenwashing/green skepticism | Dual entitlement theory, prospect theory, psychological reactance |

Same engine (phases 0–5, validation plan, disclosure practice), different corpus, different
purpose, different — and correctly so — method label.

## A second precedent track: quantitative text-mining lineage in top marketing journals

The AI-assisted-TA cluster above (Xu, Naeem, Cheah, GAATA, etc.) mostly lives in qualitative-
methods journals (IJQM), not marketing's own top-ranked outlets. Separately, there's a much
older and more prestigious tradition of computational text-as-data work published directly in
ABDC A*/A marketing journals — a stronger legitimacy anchor for framing Study 1 as "text
mining, scraping, coding" to a marketing audience/reviewer. All 17 citations below were
Crossref-verified 2026-07-08 — clean, no errors, safe to cite directly.

**Opening/framing citation decision (revisited 2026-08-13):** Epp & Humphreys (2025, *JCR*) now
opens ahead of Berger et al. (2020, *JM*) whenever the paper is specifically doing AI-assisted
*qualitative/thematic* analysis (i.e., every Study 1 built from this protocol). Read in full —
see below — it's not just a good anchor, it's the closer match: it's published in the field's
own home journal for qualitative/consumer-culture work, it's built from interviews with
researchers actually doing GenAI-assisted qualitative analysis (not automated text-mining
generally), and it hands you a ready-made four-principle reporting checklist (transparency,
provenance, privacy, verisimilitude) that a methods section can lean on directly. Berger et al.
is the better citation for the broader "automated text methods belong in marketing" claim
(topic models, dictionaries, embeddings, classification) — keep it as the second citation, and
lead with it instead when Study 2 is the quantitative-text-mining kind of paper rather than a
qualitative-coding one. For thematic analysis specifically: Epp & Humphreys first, Berger et al.
second.

Epp, A. M., & Humphreys, A. (2025). Collaborating with Generative AI in Consumer Culture
Research. *Journal of Consumer Research*, 52(1), 32–48. DOI: 10.1093/jcr/ucaf014. Interview
study (participant researchers who use GenAI on qualitative/textual consumer data) proposing
four tradeoffs (theoretical, embodied, empirical, historical) and four reporting principles
(transparency, provenance, privacy, verisimilitude). Explicitly recommends documenting example
prompts/outputs in a web appendix and reporting quote-level evidence alongside AI-generated
summaries — both directly actionable for a Study 1 methods section. Already being cited and
followed by other applied papers (Pueschel, Hao & Schmitt 2026, *JBR*, explicitly says they
"follow" its guidelines).

**Opening/framing citation for the automated-text-methods claim generally:**
Berger, J., Humphreys, A., Ludwig, S., Moe, W. W., Netzer, O., & Schweidel, D. A. (2020).
Uniting the Tribes: Using Text for Marketing Insight. *Journal of Marketing*, 84(1), 1–25.
DOI: 10.1177/0022242919873106. Integrative review of automated text methods for marketing
(topic models, dictionaries, embeddings, classification) — the field's own legitimizing
statement for this category of work, published in the flagship marketing journal.

Herhausen, D., Ludwig, S., Abedin, E., Ul Haque, N., & de Jong, D. (2025). From Words to
Insights: Text Analysis in Business Research. *Journal of Business Research*, 198, 115491.
DOI: 10.1016/j.jbusres.2025.115491. JBR framework paper comparing topic models, dictionaries,
supervised ML, and LLMs, with a message-design-logic conceptual lens and an explicit
author/reviewer checklist (their Table 4) for judging construct definition, method choice,
and transparency. Cite this for the "why an LLM is a legitimate, reviewer-recognized method
choice in business research generally" claim — not thematic-analysis-specific, but a strong
general-purpose companion to Epp & Humphreys.

**Foundational UGC/text-mining-at-scale precedents (establishes this isn't a fad):**
- Tirunillai, S., & Tellis, G. J. (2012). Does Chatter Really Matter? Dynamics of
  User-Generated Content and Stock Performance. *Marketing Science*, 31(2), 198–215.
  DOI: 10.1287/mksc.1110.0682
- Tirunillai, S., & Tellis, G. J. (2014). Mining Marketing Meaning from Online Chatter:
  Strategic Brand Analysis of Big Data Using LDA. *Journal of Marketing Research*, 51(4),
  463–479. DOI: 10.1509/jmr.12.0106
- Netzer, O., Feldman, R., Goldenberg, J., & Fresko, M. (2012). Mine Your Own Business:
  Market-Structure Surveillance Through Text Mining. *Marketing Science*, 31(3), 521–543.
  DOI: 10.1287/mksc.1120.0713

**Sentiment-method benchmarking (relevant given VADER underperformed on the CCS government
corpus — worth revisiting sentiment tooling with this citation if that work continues):**
Hartmann, J., Heitmann, M., Siebert, C., & Schamp, C. (2023). More than a Feeling: Accuracy
and Application of Sentiment Analysis. *International Journal of Research in Marketing*,
40(1), 75–87. DOI: 10.1016/j.ijresmar.2022.05.005. Meta-analysis of 272 datasets/~12M
labeled documents; releases the SiEBERT transformer-based sentiment model as a
better-performing alternative to lexicon tools like VADER.

**LLM-as-synthetic-data precedent (different use case — generating data, not coding existing
text — but useful for the broader "LLMs are legitimate in marketing research" argument):**
- Li, P., Castelo, N., Katona, Z., & Sarvary, M. (2024). Frontiers: Determining the Validity
  of Large Language Models for Automated Perceptual Analysis. *Marketing Science*, 43(2),
  254–266. DOI: 10.1287/mksc.2023.0454
- Sarstedt, M., Adler, S. J., Rau, L., & Schmitt, B. (2024). Using LLMs to Generate Silicon
  Samples in Consumer and Marketing Research. *Psychology & Marketing*, 41(6), 1254–1270.
  DOI: 10.1002/mar.21982

**Gap resolved 2026-08-11, deepened 2026-08-13:** two papers now directly validate Claude
specifically. Hill et al. (2026, *PLOS Digital Health*) ran a blinded comparison of Claude 4
Sonnet, ChatGPT-5, and QualiGPT against human analysts on deductive coding of a focus-group
transcript — Claude 4 Sonnet reached 93.5% mean agreement / Gwet's AC1 = 0.93 vs. humans' 92.7%
/ AC1 = 0.92 (non-inferior, arguably superior). AlGhamdi (2026, *IJQM*) goes further and
validates **Claude Code specifically** (not just chat-based Claude) against a human/NVivo
baseline from a published PhD dataset — see full writeup and citations in the companion doc,
`Study1_AI_Thematic_Analysis_Publishable_Protocol.md`, in this same folder. As of 2026-08-13
the paper's abstract (not the full text — Sage returned a 403 on direct fetch) confirms the
existing summary: the human baseline is a 2012 doctoral e-commerce dataset originally coded in
NVivo; AlGhamdi ran four independent Claude Code sessions against it, testing general prompts
vs. structured multi-phase prompts; alignment measured via F1 at both code and theme level,
consistency via bidirectional mapping across session pairs. Full per-statistic numbers (the
actual F1 values) are still not confirmed — flag that specifically if a reviewer wants the
number, don't invent one. This top-journal set still doesn't use Claude, but the
qualitative-methods-journal cluster now does, and directly. No more need to hedge on tool choice
when asked "why Claude Code."

Full source list: `Desktop\Downloads\marketing_textmining_papers.md` (17 rows, all
Crossref-verified 2026-07-08, ABDC A*/A ranked journals only).

## Full citation list

- Jayawardene, D., & Ewing, M. (2026). Generative AI-Augmented Thematic Analysis (GAATA).
  *International Journal of Market Research*, 68(2), 162–193. DOI: 10.1177/14707853251405043
- Turobov, A., Coyle, D., & Harding, V. (2024). Using ChatGPT for Thematic Analysis.
  arXiv:2405.08828
- Xu, W. (2026). Doing Thematic Analysis in the Age of Generative AI: Practices, Ethics and
  Reflexivity. *International Journal of Qualitative Methods*, 25, 1–14.
  DOI: 10.1177/16094069261425173
- Naeem, M., Smith, T., & Thomas, L. (2025). Thematic Analysis and Artificial Intelligence: A
  Step-by-Step Process for Using ChatGPT in Thematic Analysis. *IJQM*, 24, 1–18.
  DOI: 10.1177/16094069251333886
- Cheah, C. W. (2025). AI-Augmented Netnography: Ethical and Methodological Frameworks for
  Responsible Digital Research. *IJQM*, 24, 1–11. DOI: 10.1177/16094069251338910
- Kozinets, R. V., & Seraj-Aksit, M. (2024). Everyday activism: an AI-assisted netnography of
  a digital consumer movement. *Journal of Marketing Management*, 40(3–4), 347–370.
  DOI: 10.1080/0267257X.2024.2307387
- Misra, R., et al. (2026). Large Language Models in Qualitative Analysis: Comparing
  Traditional and Researcher-Interpreted Approaches. *IJQM*. DOI: 10.1177/16094069261426100
- Nguyen-Trung, K. (2025). ChatGPT in thematic analysis: Can AI become a research assistant in
  qualitative research? *Quality & Quantity*, 59(6), 4945–4978.
  DOI: 10.1007/s11135-025-02165-z
- Goyanes, M., Lopezosa, C., & Jordá, B. (2025). Thematic analysis of interview data with
  ChatGPT: designing and testing a reliable research protocol. *Quality & Quantity*, 59,
  5493–[pages]. DOI: 10.1007/s11135-025-02199-3
- JMIR AI (2025). Evaluating ChatGPT in Qualitative Thematic Analysis With Human Researchers
  in the Japanese Clinical Context. *JMIR AI*, e71521
- Arora, N., Chakraborty, I., & Nishimura, Y. (2025). AI–Human Hybrids for Marketing Research:
  Leveraging LLMs as Collaborators. *Journal of Marketing Research*.
  DOI: 10.1177/00222429241276529 (background/legitimacy citation)
- Wang, M., Zhang, D. J., & Zhang, H. (2025/26). Large Language Models for Market Research: A
  Data-Augmentation Approach. *Marketing Science*. DOI: 10.1287/mksc.2025.0009 (background)
- Sarstedt, M., et al. (2024). Using Large Language Models to Generate Silicon Samples in
  Consumer and Marketing Research. *Psychology & Marketing* (background)

**Added 2026-08-13 (read/verified in full unless noted otherwise):**
- Epp, A. M., & Humphreys, A. (2025). Collaborating with Generative AI in Consumer Culture
  Research. *Journal of Consumer Research*, 52(1), 32–48. DOI: 10.1093/jcr/ucaf014
- Herhausen, D., Ludwig, S., Abedin, E., Ul Haque, N., & de Jong, D. (2025). From Words to
  Insights: Text Analysis in Business Research. *Journal of Business Research*, 198, 115491.
  DOI: 10.1016/j.jbusres.2025.115491
- Qian, T. Y., Gong, H., & Xu, C. (2026). Sports, Politics, and Social Media: A Human-AI
  Collaborative Analysis of Consumer Reactions to Trump's Break 50 Appearance. *Journal of
  Retailing and Consumer Services*, 88, 104520. DOI: 10.1016/j.jretconser.2025.104520
- Pueschel, J., Hao, S., & Schmitt, B. (2026). Understanding Luxury Shaming: A Multi-Study
  Exploration Using Qualitative Inquiry and Generative AI. *Journal of Business Research*, 206,
  115996. DOI: 10.1016/j.jbusres.2026.115996
- Paulus, T., Lester, J. N., & Davis, C. (2026). The Construction of the Role of AI in
  Qualitative Data Analysis in the Social Sciences. *AI & Society*, 41, 1737–1748.
  DOI: 10.1007/s00146-025-02488-3
- AlGhamdi, R. (2026). From Code Variability to Theme Convergence: AI–Human Alignment in
  Thematic Analysis With Claude Code. *International Journal of Qualitative Methods*.
  DOI: 10.1177/16094069261462093 (abstract-level detail confirmed via search; full text
  paywalled/403 on direct fetch — see companion protocol doc)
- Lazarus, M. D., Zhao, L., Gibson, A., Martinez-Maldonado, R., & Stephens, G. C. (2026). Risky
  or Rigorous? Developing Trustworthiness Criteria for AI-Supported Qualitative Data Analysis.
  *Anatomical Sciences Education*, 19, 330–337. DOI: 10.1002/ase.70125 (abstract/summary-level
  detail confirmed via search; full text paywalled/402 on direct fetch — see companion protocol
  doc for what could and couldn't be recovered)
- Nyaaba, M., SungEun, M., Apam, M. A., Acheampong, K. O., Dwamena, E., & Zhai, X. (under
  review, *Journal of Digital Educational Measurement*). Human–AI Collaborative Inductive
  Thematic Analysis: How AI Guides Analysis and Researchers Reclaim Interpretive Authority.
  arXiv:2601.11850. Note: under-review preprint, not yet peer-reviewed/published; the reading
  list's placeholder title/authors are superseded by this — see companion protocol doc.
- Karhu, K., Smolander, K., & Kasurinen, J. (2026). To Vibe Research or Not to Vibe Research?
  Generative AI in Qualitative Research. arXiv:2605.00922
- Jowsey, T., Braun, V., Clarke, V., Lupton, D., & Fine, M. (2025). We Reject the Use of
  Generative Artificial Intelligence for Reflexive Qualitative Research. *Qualitative Inquiry*.
  (Cited secondhand via Karhu et al. above — not independently fetched/verified; treat as
  reported, not confirmed, until read directly.)
