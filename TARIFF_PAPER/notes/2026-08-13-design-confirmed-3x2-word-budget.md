# 2026-08-13 — 3×2 design reconfirmed after JCM word-budget check

## Decision
Britton reconfirmed the existing locked design (`2026-08-04-design-locked-jcm-fit.md`):
**Attribution Frame (3: tariff-explicit / general-cost-explicit / silent) × Cost-Response
(2: full pass-through / shared-burden absorption), 6 cells.** Considered and rejected both
alternatives raised this session:
- **Collapsing to 2×2** (dropping the general-cost-explicit middle level) — would have freed
  up word-count margin but was not the direction Britton wanted.
- **Expanding to a true 3×3** (adding a third Cost-Response level, 9 cells) — checked the
  word math first; this would land right at the 8,000-word ceiling with no slack. Not pursued.

## Word-budget check (why 3×2 is fine, shown the arithmetic before confirming)
Confirmed via web search that Emerald/JCM's word count is the strict version: **includes all
text — references, tables, figures, abstract/keywords — not just running prose**, and each
table/figure counts as a flat 280 words against the limit regardless of actual size. (Emerald
standard boilerplate across their marketing titles; worth Britton double-checking the exact
line on ScholarOne when he's in there, but treat as reliable for planning purposes.)

Section-by-section estimate for the 3×2, two-study paper (Study 1 qual + Study 2 experiment),
built off actual word counts from the drafted Intro/Theory section (813w) and Study 1 Method
draft (~900w real prose):

| Section | Est. words |
|---|---|
| Abstract/keywords | 200 |
| Introduction | 400 |
| Theory/Hypotheses | 850 |
| Study 1 Method (tightened) | 650 |
| Study 1 Results (themes — not yet drafted) | 600 |
| Study 2 Method | 800 |
| Study 2 Results (2 main effects w/ 3-level pairwise contrasts + interaction) | 800 |
| Discussion/Implications | 1150 |
| Limitations/Conclusion | 580 |
| References (~40-60 cites) | 700 |
| Figures/tables (1 model diagram, 280w flat) | 280 |
| **Total** | **~7010** |

**~990-word buffer under the 8,000 cap** — workable, but thin enough that it should absorb
a first-round reviewer's likely ask (extra robustness check, extra citation, longer lit
grounding) without much room to spare. Worth keeping an eye on total length as sections get
drafted for real rather than assuming the buffer holds.

## New decision this session: bank additional scales for a future companion paper
Britton wants to add measured (not manipulated, not hypothesized in *this* paper) constructs
to the Study 2 and/or Study 3 instrument now, while Prolific respondents are already being
paid for and recruited, so a second paper can be built off the same data collection without
touching the current 3×2 design or bloating the JCM word count (unreported measured
constructs don't count against the manuscript's word limit — only what's written up does).

**Candidate direction, not yet decided — see next note / ask Britton directly:** the "full"
ChatGPT model diagram (superseded by the leaner primary model on 2026-08-04) already dropped
three constructs that are natural, zero-new-literature-search candidates to revive as banked
measures: **Perceived Transparency, Inferred Firm Motive, Brand Attitude**. Also floated but
not yet vetted: elevating the single-item political ideology demographic question to a full
validated scale (tariffs are politically polarized; a "does ideology moderate the fairness
penalty for silence" companion paper is plausible), or a consumer-ethnocentrism/animosity
angle (CETSCALE, Shimp & Sharma 1987) — flagged as the more novel but higher-lift option,
since animosity models typically want a named country-of-origin cue the current vignettes
don't have, so it might require more than "just add a scale."

## Still needed before this is IRB-ready
1. Britton's actual pick on which banked scale(s) to add (see above).
2. Once picked: source validated items, add to Study 2/3 instrument flow, update time
   estimate and compensation figures in `2026-08-04-IRB-draft-content.md` and
   `build_irb_docx.py` accordingly (extra scales = a few more minutes of survey time).
3. Everything else already flagged in `2026-08-04-IRB-draft-content.md`'s "still needed"
   list (CITI number, exact scale wording, full instrument assembly, debriefing text,
   realistic dates) is unaffected by this decision and still outstanding.
