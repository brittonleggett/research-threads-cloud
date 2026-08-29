# 2026-08-29 — WebFetch retry, direct-fetch literature upgrades, vignette mechanical fixes,
# readability check, Study 2 Methods draft

## What this is

Continues the autonomous build-out under the project's standing 2026-08-16 Phase 3/instrument-build
exception (`notes/2026-08-16-phase3-theme-review-and-theory-lock.md`). No locked theme, hypothesis,
or design element was touched tonight. No decision was made on any of the three items still
explicitly reserved for Britton (archival-moderator feasibility, single-manipulation vs. factorial,
PLS-SEM vs. Hayes-PROCESS). The Nhan & Helfers researcher-independence question was **not**
re-attempted, per the 08-27 note's own recommendation to stop automated retries on that specific
question — see that note and the 08-27 follow-up for why (five sessions, ~25 queries, one direct
fetch confirming a publisher-side HTTP 403 bot-block, all null).

Five things happened, in priority order: (1) tested and confirmed WebFetch is working tonight,
unlike most of the last several weeks of sessions; (2) used it to upgrade two literature claims from
WebSearch-triangulated to direct-fetch-verified confidence; (3) ran one fresh literature-gap sweep
to check for new competing studies since the 08-24 deep scan; (4) applied the two purely mechanical
vignette fixes flagged as in-scope from the 08-27 face-validity review, plus a real Flesch-Kincaid
readability calculation; (5) drafted the project's first Study 2 Methods section, synthesizing
scattered design notes into one manuscript-shaped document.

## 1. WebFetch status: working tonight

Tested against `en.wikipedia.org/wiki/Automatic_number-plate_recognition` (control) — loaded
cleanly, full content returned. This is a real change from the `EGRESS_BLOCKED` failures logged in
every session from roughly 2026-08-13 through 2026-08-25, consistent with the environment-level fix
referenced in the 2026-08-27 second-pass note (diagnosed and fixed that day, first nightly run to
actually exercise it). Several publisher/database sites still returned clean HTTP 403 or 451
responses tonight (`ij.org`, `cnn.com`, `sciencedirect.com`) — these are **not** egress failures,
they're those sites' own bot-defense or region-blocking, the same distinct failure mode the 08-27
note first identified with SAGE. Worth stating plainly: egress being fixed does not mean every
source becomes fetchable — paywalled/bot-defended publisher pages remain a real, separate barrier
that only library/manual access solves, same conclusion as 08-27's Nhan & Helfers finding.

## 2. Two literature claims upgraded to direct-fetch confidence

### Mountain View state/federal access paragraph

Directly fetched `https://abc7news.com/post/city-mountain-view-alleges-federal-state-agencies-accessed-flock-safety-camera-data-consent/18518963/`
— the exact ABC7 piece the 08-24 note flagged as "recommended before this goes into a submitted
manuscript." Every specific detail in the existing draft paragraph (`Introduction_and_Theory_DRAFT_2026-08-16.md`,
contextual-integrity section) matches the article precisely: the federal agencies involved (ATF
Kentucky/Tennessee offices, Langley Air Force Base, U.S. GSA Office of Inspector General, Lake Mead
National Recreation Area, an Ohio Air Force Base), the "29 of 30 cameras" state-level access figure,
and the internal-audit discovery mechanism. **No wording changed in the draft paragraph itself** —
it was already accurate — only the confidence-tier annotation in the "what's still needed" section
was updated to reflect direct-fetch verification. This closes the specific follow-up item the 08-24
note left open.

### Institute for Justice "21 similar cases" function-creep figure

The draft previously flagged this figure as "cited but not yet independently verified... attributed
by search results to the Institute for Justice." Tonight: IJ's own database page
(`ij.org/the-ij-database-of-alpr-abuse/`) returned a clean HTTP 403 on direct fetch — bot-blocked,
same pattern as SAGE, not an egress failure. But two independent secondary outlets that themselves
directly quote the IJ analysis were successfully direct-fetched:

- Fox 13 Tampa Bay / Fox 35 Orlando (shared syndicated piece,
  `fox13news.com/news/flock-adds-new-guardrails-police-misuse-license-plate-readers-draws-scrutiny`):
  cites IJ's "dozens of cases" language and a separate, broader figure of "more than 50 law
  enforcement officers... accused of or charged with misusing Flock cameras."
- Malwarebytes security-news desk
  (`malwarebytes.com/blog/news/2026/07/the-backlash-against-flock-cameras-is-spreading`): quotes
  directly, "An Institute for Justice analysis identified **at least 22 cases** nationwide in which
  officers allegedly [misused ALPR to monitor romantic interests]... the bulk of those incidents
  happening since 2024" — also notes IJ's own caveat that the count "is likely an undercount because
  misconduct may never be discovered or publicly reported."

**Updated the draft's figure from "at least 21" to "at least 22"** and added a direct-fetch
confidence annotation (`Introduction_and_Theory_DRAFT_2026-08-16.md`). The 21→22 shift across
sessions is treated as IJ's tracker being actively updated as new cases surface, not a discrepancy
to investigate further — both figures come from the same evolving IJ database, just pulled at
different points in time by different search passes.

## 3. Literature-gap sweep: no new competing study found

Three targeted WebSearch queries tonight, checking for anything published or surfaced since the
2026-08-24 deep scan:
1. General sweep for new Flock-specific academic scholarship, August 2026.
2. ALPR + disclosure/transparency + survey experiment + procedural justice + institutional trust,
   combined (the paper's exact causal-chain vocabulary, same query family as 08-24's #6).
3. ALPR/license-plate-reader + vignette experiment + public opinion + procedural justice +
   institutional trust + journal.

**No study was found that experimentally manipulates ALPR/Flock disclosure or tests this paper's
specific serial-mediation chain** — the novelty claim continues to hold. Two new adjacent works
surfaced that weren't in any prior session's notes, neither added to the draft (judgment call, not
a verification failure — both are real but tangential):

- Shjarback (2024), "Examining Police Officers' Perceptions of Automated License Plate Readers
  Before Technology Expansion," *Policing: An International Journal* — surveys **police officers'**
  perceptions of ALPR, not public/citizen opinion. Different population than this paper's design;
  not a competitor, not obviously a citation this paper needs either (its theoretical territory —
  officer attitudes toward new technology — doesn't overlap with the disclosure→injustice→trust
  chain here). Noting for completeness, not adding.
- An untitled-in-search-results 2025 *Taylor & Francis* piece, "An Evaluation of a Major Expansion
  in Automated License Plate Reader (ALPR) Technology" — appears to be an outcome evaluation (crime
  reduction) based on one ALPR vendor's installation records across 216 agencies, not a public-
  opinion or trust study. Also not added — flagged as a possible candidate if Britton wants
  real-world efficacy evidence for the Moderator 2 (crime-solving necessity) discussion, but this
  wasn't independently confirmed via direct fetch (ScienceDirect/Taylor & Francis pages weren't
  pulled tonight) and shouldn't be cited without that.

Also attempted a direct-fetch spot-check of the Przeszlowski & Guerette (2025) *Journal of Criminal
Justice* citation (flagged in the 08-25 note as needing one before submission) —
`sciencedirect.com/science/article/abs/pii/S0047235224001855` returned HTTP 403, same bot-block
pattern as everywhere else on ScienceDirect tonight. **Still not direct-fetch-verified** — the
08-25 WebSearch-triangulated confidence (RePEc bibliographic listing + independent co-authorship
corroboration) is unchanged, not upgraded tonight. This spot-check remains a genuine open item.

## 4. Two mechanical vignette fixes applied (`Study2_Instrument_DRAFT_2026-08-27.md`, Section 4)

Per the task brief's explicit scope: fixed the two purely mechanical issues the 2026-08-27
face-validity review flagged, and left the two substantive/design-adjacent flags (the government-
incompetence confound in Condition B's framing; the general reading-level gap) untouched or only
partially addressed where a mechanical fix alone could help.

**(a) "Three sentences" factual error corrected.** The document's delivery notes claimed both
conditions had "three sentences of condition-specific content"; both were actually two. Corrected
inline, with the real sentence/word counts stated explicitly (see instrument doc for full detail).

**(b) Condition B's first sentence split for complexity.** The original 46-word sentence containing
two embedded em-dash parenthetical clauses ("— one the city council was not told about when it
approved the contract —") was split into two sentences (33 and 15 words) that preserve every fact
and framing element unchanged — nothing was added, removed, or reworded, only the sentence
boundary moved. This is a punctuation/structure change, not a content change, consistent with the
task brief's instruction not to touch manipulation content/framing without flagging it.

**Deliberately NOT fixed:** the government-incompetence confound flagged in the 08-27 review
(finding 2d) — Condition B's "discovered via news investigation, officials didn't know" framing may
still test something beyond disclosure/secrecy. That's a content/framing question, explicitly
outside this session's scope per the task brief, and remains flagged for Britton or a pilot.

## 5. Readability check: Flesch-Kincaid Grade Level, computed via `textstat`

No readability-formula tool had been run in any prior session (the 08-27 review explicitly flagged
this as unavailable that night). Installed the `textstat` Python library tonight (its accompanying
`cmudict` syllable-dictionary download required a one-time NLTK proxy-egress opt-in,
`NLTK_ALLOW_PROXIED_URLOPEN=1`, since it fetches from a GitHub-hosted index — flagging this in case
a future session hits the same block) and ran Flesch-Kincaid Grade Level and Flesch Reading Ease
on the consent risk-language sentence and both full vignette conditions (shared opening +
condition-specific text), before and after the Condition B split above. Full script:
`/tmp/claude-0/-home-user-research-threads-cloud/677cb59c-da05-5b7d-9983-a20ddc4ce492/scratchpad/readability_check.py`
(scratchpad only, not part of the repo).

| Text | Words | Sentences | FK Grade | Flesch Ease |
|---|---|---|---|---|
| Consent risk-language sentence | 34 | 2 | 11.2 | 45.3 |
| Full Condition A (shared opening + condition text) | 121 | 5 | 14.9 | 31.3 |
| Full Condition B, ORIGINAL | 119 | 5 | 15.2 | 28.4 |
| Full Condition B, REVISED (after split) | 121 | 6 | 13.7 | 32.5 |

**Confirms the 08-27 review's finding (2c) with real numbers**: both vignette conditions sit far
above the instrument's own stated ~8th-grade target — roughly a 15th-grade (senior-undergraduate/
early-graduate) reading level, not 8th. The consent sentence, while not part of the vignette,
independently also exceeds 8th grade (11th-grade level) — noted here since it uses the same stated
target, though the task brief scoped tonight's edits to the vignette only, so this wasn't changed.

**The Condition B split reduced but did not close the gap** — FK grade dropped from 15.2 to 13.7,
a real improvement and now closer to Condition A's 14.9, but still roughly seven grade levels above
the stated target. Closing that fully would require shortening sentences further and/or simplifying
vocabulary (e.g., "automated license-plate-reader (ALPR)," "law-enforcement databases," passive
constructions like "would be accessible," "were not told") — changes that begin to touch the actual
wording and content of the stimulus, not just its punctuation. Per the task brief's boundary, this
was flagged rather than done unilaterally; see the instrument doc's updated "what's still needed"
section.

## 6. New: `Study2_Methods_Section_DRAFT_2026-08-29.md`

The project had a full Study 1 Method section
(`Study1_Methods_Section_DRAFT_2026-08-16.md`) and a full Study 2 instrument
(`Study2_Instrument_DRAFT_2026-08-27.md`), but no prose Study 2 Method section synthesizing design,
participants, procedure, measures, and analysis plan into one manuscript-shaped document — that
material lived only across five separate dated notes files. Wrote that section tonight, pulling
from the design memo, both instrument-adaptation notes, and the IRB draft rather than deciding
anything new. Written to remain accurate under either branch of all three reserved design calls
(explicitly states each open call inline rather than picking a default). Includes an honest
Limitations subsection (single-item Moderator 2 with no internal-consistency statistic; unsettled
Moderator 1 operationalization; no pilot yet run; single-manipulation vs. factorial scope).

## What this pass did NOT do

- Did not touch the locked thematic map, hypotheses, or any design element.
- Did not decide any of the three items reserved for Britton (archival-moderator feasibility,
  single-manipulation vs. factorial, PLS-SEM vs. PROCESS).
- Did not re-attempt the Nhan & Helfers independence question — per the 08-27 note's own
  recommendation, treating that as closed to further automated attempts.
- Did not fix the vignette's government-incompetence confound (08-27 finding 2d) or fully close the
  reading-level gap — both are content/framing questions, outside tonight's mechanical-fix scope.
- Did not run an actual human pilot — the readability check and mechanical fixes supplement, but do
  not replace, the pilot every prior session has correctly flagged as still needed.
- Did not add the two newly-found adjacent works (Shjarback 2024; the 2025 ALPR-expansion
  evaluation) to the draft — flagged as candidates, not verified enough or clearly on-topic enough
  to add without Britton's or a future session's closer look.

## Open items for Britton

1. Everything already open in prior notes remains open (archival-moderator feasibility,
   single-manipulation vs. factorial, PLS-SEM vs. PROCESS, CITI certificate number, power analysis,
   Theme 3 promotion gut-check, the consent risk-language sentence, Condition B's
   government-incompetence framing question).
2. New: even after tonight's mechanical split, both vignette conditions remain well above the
   instrument's stated ~8th-grade reading-level target (FK grade ~14-15) — closing that gap further
   would require simplifying wording/vocabulary, which edges toward a content decision worth his
   input before a session does it unilaterally.
3. New: the Institute for Justice figure is now "at least 22" (was "21"), direct-fetch confirmed via
   two independent outlets quoting IJ, though IJ's own page remains bot-blocked to direct fetch.
4. New: two adjacent-but-not-added literature finds (Shjarback 2024 on officer perceptions; a 2025
   ALPR-expansion outcome evaluation) — neither added to the draft, flagged for his judgment if
   either seems worth folding in later.
5. New: `Study2_Methods_Section_DRAFT_2026-08-29.md` is a first draft, unreviewed, written to stay
   accurate regardless of how the three reserved design calls resolve.
6. WebFetch is working again as of tonight, but several individual publisher/database sites
   (ij.org, cnn.com, sciencedirect.com, journals.sagepub.com) remain independently bot-blocked
   (HTTP 403/451) regardless of egress status — that's a separate, likely permanent barrier for
   those specific sources, not something expected to resolve with further retries.
