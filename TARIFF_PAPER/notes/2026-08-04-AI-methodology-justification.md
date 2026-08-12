# 2026-08-04 — Literature justification: AI-assisted data collection + thematic analysis

Pulled from the existing shared method file (`Claude Knowledge\Thematic Analysis\
AI_Assisted_TA_Shared_Method.md`, built jointly for the CCS and Tariff papers, 17 citations
Crossref-verified 2026-07-08) — not re-researched, adapted specifically for Study 1's actual
context here: AI-assisted collection and thematic coding of corporate tariff-messaging
artifacts (not a Reddit/netnography corpus like CCS).

## 1. Justification for AI-assisted data collection ("scraping"/gathering the corpus)

Two distinct precedent tracks, both worth citing — a qualitative-methods track and a much
more prestigious top-marketing-journal track. Lead with the second for a JCM reviewer.

**Opening/framing citation, use first:**
Berger, J., Humphreys, A., Ludwig, S., Moe, W. W., Netzer, O., & Schweidel, D. A. (2020).
"Uniting the Tribes: Using Text for Marketing Insight." *Journal of Marketing*, 84(1), 1-25.
The field's own integrative, legitimizing statement for computational/AI-assisted text
methods in marketing, published in the flagship journal.

**Establishes this is a mature tradition, not a fad:**
- Tirunillai, S., & Tellis, G. J. (2012). "Does Chatter Really Matter? Dynamics of
  User-Generated Content and Stock Performance." *Marketing Science*, 31(2), 198-215.
- Tirunillai, S., & Tellis, G. J. (2014). "Mining Marketing Meaning from Online Chatter."
  *Journal of Marketing Research*, 51(4), 463-479.
- Netzer, O., Feldman, R., Goldenberg, J., & Fresko, M. (2012). "Mine Your Own Business:
  Market-Structure Surveillance Through Text Mining." *Marketing Science*, 31(3), 521-543.

**LLM-specific legitimacy (most directly relevant to justifying Claude's role here):**
- Arora, N., Chakraborty, I., & Nishimura, Y. (2025). "AI-Human Hybrids for Marketing
  Research: Leveraging LLMs as Collaborators." *Journal of Marketing Research*.
- Wang, M., Zhang, D. J., & Zhang, H. (2025/26). "Large Language Models for Market Research:
  A Data-Augmentation Approach." *Marketing Science*.
- Sarstedt, M., Adler, S. J., Rau, L., & Schmitt, B. (2024). "Using LLMs to Generate Silicon
  Samples in Consumer and Marketing Research." *Psychology & Marketing*, 41(6), 1254-1270.

**One honest gap to carry into the write-up, not smooth over:** no paper in this top-journal
set was confirmed to use Anthropic's Claude specifically — the published record uses
GPT-family models or traditional ML (LDA, CNN, BERT-family). Cite the *method tradition*
(LLM-assisted text analysis in marketing research generally), not a Claude-specific
precedent, if a reviewer asks why this tool specifically.

## 2. Justification for (AI-assisted) thematic analysis as Study 1's method

**Foundational TA citations (already in the lit review):** Braun & Clarke (2006, 2019).

**Critical branding decision — get this right or it's reviewer bait:** Braun & Clarke's TA
splits into "Big Q" reflexive TA (interpretive, explicitly *rejects* reliability statistics)
vs. "small q" / coding-reliability TA (codebooks, multiple coders, agreement statistics).
Since Study 1 feeds into a confirmatory quantitative program (vignette stimuli → PLS-SEM),
**this should be branded small-q / coding-reliability thematic analysis, not "reflexive TA."**
Reporting a Kappa/agreement statistic while calling it reflexive TA is, per the shared
method's own note, "the single most common reviewer-bait mistake in this literature."

**AI-assisted-TA precedent cluster:**
- Xu, W. (2026). "Doing Thematic Analysis in the Age of Generative AI: Practices, Ethics and
  Reflexivity." *International Journal of Qualitative Methods*, 25, 1-14. (Source of the
  "keep theme-review human-only" rule already built into Study 1's Phase 3.)
- Naeem, M., Smith, T., & Thomas, L. (2025). "Thematic Analysis and Artificial Intelligence: A
  Step-by-Step Process for Using ChatGPT in Thematic Analysis." *IJQM*, 24, 1-18.
- Jayawardene, D., & Ewing, M. (2026). "Generative AI-Augmented Thematic Analysis (GAATA)."
  *International Journal of Market Research*, 68(2), 162-193. (Reports Cohen's Kappa = 0.94
  on consumer app reviews — closest precedent in corpus type/semantic-heaviness to Study 1's
  corporate-messaging artifacts.)
- Misra, R., et al. (2026). "Large Language Models in Qualitative Analysis: Comparing
  Traditional and Researcher-Interpreted Approaches." *IJQM*.
- Goyanes, M., Lopezosa, C., & Jordá, B. (2025). "Thematic analysis of interview data with
  ChatGPT: designing and testing a reliable research protocol." *Quality & Quantity*, 59,
  5493-[pages].
- Turobov, A., Coyle, D., & Harding, V. (2024). "Using ChatGPT for Thematic Analysis."
  arXiv:2405.08828.

## 3. What Study 1 still needs to do to actually earn these citations

Citing the methodology literature justifies the *approach*; it doesn't substitute for
following it. Per the shared method file, still outstanding for Study 1:
1. **Validation pilot** — code a subsample manually and with the LLM, compute and report
   agreement (Kappa or % agreement). Not yet done for the tariff corpus. GAATA's 0.94 Kappa
   (semantic-heavy, similar corpus type) is the closest reference point for what to expect,
   not a number to borrow directly.
2. **Explicit AI-use disclosure** in the methods section and acknowledgements — expected
   practice in this literature now, not optional.
3. **Phase 3 (theme review) stays human-only** — already the plan per
   `Study1_Corpus_and_Coding_DRAFT_2026-07-24.md`, consistent with Xu (2026)'s precedent.
4. **Expand the corpus** before this goes in the paper — currently 7 artifacts, a standard TA
   sample would be closer to 15-20 (already flagged in the Study 1 draft as a to-do), and pull
   primary sources (8-Ks, IR pages) rather than secondary news coverage where possible.

## Bottom line for the methods section

Two clean sentences to anchor the paragraph: "Following an established and growing tradition
of AI-assisted text analysis in top marketing journals (Berger et al. 2020; Tirunillai &
Tellis 2012, 2014; Netzer et al. 2012) and dedicated methodological guidance for AI-assisted
thematic analysis (Braun & Clarke 2006, 2019; Xu 2026; Naeem et al. 2025), Study 1 employed a
small-q, coding-reliability thematic analysis of publicly available corporate tariff-
messaging artifacts, with AI assistance in coding (Phases 1-2) and theme naming (Phase 4)
but human-only theme review (Phase 3), consistent with Xu (2026)'s precedent for that step."
