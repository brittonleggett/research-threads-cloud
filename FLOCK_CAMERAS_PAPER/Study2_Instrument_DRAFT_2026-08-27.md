# Study 2 — Full Instrument Assembly (DRAFT)

**Status note (delete before submission):** AI-drafted, 2026-08-27, under Britton's standing
one-time exception for this paper (`notes/2026-08-16-phase3-theme-review-and-theory-lock.md`).
Closes item #5 from `notes/2026-08-21-irb-application-draft.md`'s "still needed" list — "full
survey instrument assembly... combining consent, screener, vignette, manipulation checks, scales,
demographics, and debriefing into an actual platform-ready survey flow document. Not started."
This is that document: a single, in-order draft of the whole Study 2 flow, pulling together
already-locked/verified pieces from prior notes rather than deciding anything new. **Nothing here
has been piloted or reviewed by Britton.** The vignette text (Section 4) is newly drafted for this
pass — everything else is a direct assembly of previously drafted/revised content, cited to its
source note inline.

**What this pass did NOT decide** (both remain explicitly Britton's call, flagged inline at the
relevant section below, same as every prior note):
1. Archival (Path A) vs. self-report (Path B) operationalization of Moderator 1 — Section 8 below
   is written to cover both, not to pick one.
2. Single-manipulation design (as built here) vs. a factorial design crossing disclosure with an
   explicit necessity-framing manipulation.
3. PLS-SEM vs. Hayes-PROCESS analysis approach — doesn't affect instrument content, only the
   eventual analysis plan, not addressed here.

**2026-09-20 sync note (AI-run, under the standing 2026-08-16 Phase 3 exception):** this document
still described the *original 2-condition* disclosure manipulation as of this revision, even though
Britton decided on 2026-09-08 (`notes/2026-09-08-four-arm-vignette-draft.md`) to expand Study 2 into
a **4-arm single-factor between-subjects design** (neutral / safety-benefit / broad-network-access /
disparate-impact), added a **baseline trust in police** pre-exposure moderator, and ran a Monte Carlo
power analysis — none of which had been folded into this instrument document yet (flagged explicitly
as an open sync gap, item 6 of that note's "still open" list, and again in `Study2_Methods_Section_
DRAFT_2026-08-29.md`'s own still-2-condition text). Sections 3-5 below are now updated to match.
**This also resolves open design call #2 above**: Britton's actual choice was neither the original
single-2-condition-manipulation design nor a 2×2 factorial crossing disclosure with a necessity-
framing manipulation, but a single-factor 4-level (4-arm) manipulation directly mirroring Study 1's
candidate themes. Calls #1 (archival vs. self-report Moderator 1) and #3 (PLS-SEM vs. Hayes-PROCESS)
remain open, unchanged.

---

## 1. Consent

Electronic informed consent, ~8th-grade reading level, per
`notes/2026-08-21-irb-application-draft.md`'s Voluntary Participation section. Study purpose
stated at a general level ("public perceptions of surveillance camera policy," not the specific
disclosure/trust hypotheses). Estimated time: ~10-12 minutes (per IRB draft's Compensation
section). Radio buttons: "I agree to participate" / "I do not agree to participate." Non-consenting
respondents redirected out immediately, no penalty.

**Risk language note (per IRB draft's Risk/Benefit section):** because this topic (police,
surveillance, federal immigration data-sharing) is more likely than a neutral consumer topic to
touch personally salient material for some respondents, consent language should name this plainly
rather than defaulting to generic "mild, transient annoyance" boilerplate — draft sentence for
Britton's review: *"This study asks about your opinions on a public policy topic (surveillance
cameras and law enforcement). Some people may find this topic personally relevant or sensitive;
you are free to stop at any time."*

## 2. Screener

- Age (open text or range select) — terminate if <18.
- "Do you currently reside in the United States?" — terminate if No.
- Attention/English-fluency filter item embedded naturally in the screener (matching Tariff
  Paper's own screener convention, `TARIFF_PAPER/notes/2026-08-04-full-instrument-assembly.md`).
- **[Path A only, if adopted — see Section 8]** ZIP code or city/state of residence, collected
  here so it can be de-linked from response data immediately per the IRB draft's Confidentiality
  section. Not collected at all under Path B.

## 2b. Pre-exposure moderator: Baseline trust in police (added 2026-09-20, per 2026-09-08 design session)

**Measured before random assignment / vignette exposure**, immediately after the screener and
before Section 3, so it cannot be contaminated by the manipulation. Added per
`notes/2026-09-08-four-arm-vignette-draft.md` as a direct response to Merola, Lum, & Murphy
(2018)'s own stated future-research call — **citation now verified via Crossref** (2026-09-20,
this session; DOI `10.1007/s11292-018-9332-8`): "The impact of license plate recognition
technology (LPR) on trust in law enforcement: a survey-experiment," *Journal of Experimental
Criminology*, 15(1), 55–66 (published online 2018-06-02; print issue March 2019 — the draft's
"(2018)" citation follows the online-first year, matching this project's established convention
for online-first-vs-print-issue citation years, e.g. Schiff et al. 2025). Their Fairfax County,
VA sample's unusually high baseline trust (80.79%, per the 09-08 note; not independently
re-verified against the article's full text tonight — SAGE/Springer full-text access was not
attempted this session, so treat the specific 80.79% figure as carried over from the 09-08 note
rather than freshly confirmed) likely produced a conservative estimate of their observed
awareness-to-trust-erosion effect; they explicitly suggested testing this across communities with
varying baseline trust, which this design's national CloudResearch sampling frame is suited to.

No validated multi-item published scale for this specific construct was located; per the 09-08
note, a short trust-in-police screener item set (not yet drafted in this document) will double as
(a) the baseline-trust covariate/moderator measure and (b) the oversampling screener described in
`Study2_Methods_Section_DRAFT_2026-08-29.md`'s Sampling section. **Not yet drafted as specific
item wording** — flagged here as the concrete next step for this construct, rather than inventing
item wording without a source.

Direction of this moderation is treated as an open empirical question (could attenuate via a floor
effect, or amplify via a confirmation-bias-style effect), not assumed in either direction.

## 3. Random assignment

**Revised 2026-09-20** (was: single factor, two conditions). Per Britton's 2026-09-08 design
decision (`notes/2026-09-08-four-arm-vignette-draft.md`), this is now a **single-factor, 4-level,
equal-probability between-subjects randomization** (not the original 2-condition disclosure
manipulation, and not a 2×2 factorial — see the 2026-09-20 sync note above). Participant sees
exactly one of the four vignette conditions below.

## 4. Vignette exposure (revised 2026-09-20 — supersedes the original 2-condition text)

**This section replaces the original Condition A/B disclosure-manipulation text below with the
4-arm design from `notes/2026-09-08-four-arm-vignette-draft.md`, using its recommended v2 wording
(the version with real, measured Flesch-Kincaid scores, not the unscored v1 draft).** All four
conditions describe the same fictitious city ("Meridian Falls") adopting an ALPR camera network,
matching this project's established fictitious-but-realistic stimulus convention, and are matched
on sentence count (2 each) and word-count band (32-39 words for the condition-specific text).

**Shared opening (all 4 conditions):**

> The city of Meridian Falls set up license-plate cameras at intersections around the city. The
> cameras take photos of car plates and check them against police lists. City officials said the
> cameras will help police solve crimes such as car theft.

**Condition 1 — Neutral/baseline:**

> The cameras started working a few weeks after they went up. The city posted basic facts about
> the new cameras on its website. Local news covered the story as routine city news.

**Condition 2 — Safety-benefit** (Flock's own public crime-solving claims; ambivalent
safety-benefit theme):

> Two months after the cameras went live, they helped police find a car linked to a string of home
> burglaries. Police said the arrest would not have happened as fast without the cameras.

**Condition 3 — Broad-network-access** (institutional secrecy/function-creep theme; replaces an
earlier ICE-specific draft — see decision note below):

> The camera network links to a national database that many other police departments use.
> Departments in other cities and states can search this database for camera data from Meridian
> Falls.

**Condition 4 — Disparate-impact** (distributive-injustice theme; the most independently
replicated theme in the corpus per the 2026-09-08 literature pass — Monahan 2026, Keener/Finn/
Baird 2026, Sapp et al. 2021, and the CNU Hampton Roads study):

> A new study of camera locations found that minority and lower-income neighborhoods had far more
> cameras than other parts of the city. Some neighborhoods had several cameras nearby, while others
> had none.

**Readability (measured 2026-09-09 via `textstat`/Flesch-Kincaid, script at
`notes/readability_check_2026-09-09.py`):** Neutral FK 7.6, Safety-benefit FK 7.7,
Broad-network-access FK 9.7, Disparate-impact FK 9.7 — three of four at or near the instrument's
own ~8th-grade target; the two conditions naming multi-syllable technical nouns ("database,"
"neighborhoods") stay slightly elevated for reasons tied to real content, not avoidable wordiness.
This is a real, measured improvement over the original 2-condition draft's FK 13.7-14.9 (see the
retained text at the bottom of this section for comparison). **Still not a substitute for an
actual human pilot** — no condition in this design has been piloted with real respondents.

**Two design calls Britton made explicitly on 2026-09-08, carried over here:**
1. **Dropped ICE-specific wording** from Condition 3 (an earlier draft named "U.S. Immigration and
   Customs Enforcement (ICE)" explicitly) — Britton flagged ICE as too hot-button, risking testing
   partisan reaction to ICE specifically rather than the intended institutional-secrecy/broken-
   promise mechanism. Current generic "many other police departments" wording is arguably more
   theoretically faithful to the real underlying mechanism (breadth of access beyond the local
   department, per Monahan 2026's FOIA data and Flock's actual "National Lookup" feature) than
   naming one federal agency. Not adopted, but flagged as a middle option if reconsidered: "federal
   law enforcement agencies" (unspecified).
2. **Race/class wording is "minority and lower-income neighborhoods,"** not "Black neighborhoods"
   (Britton was clear he didn't want to name a specific racial group) or "economically
   disadvantaged" alone (a real, testable concern that pure economic language might not actually
   cue race for respondents, which would test a different construct — class-based disparate impact
   — than the literature's actual race+poverty operationalization; Keener, Finn & Baird 2026's own
   title is "Race, Poverty, and the Geography of ALPR Deployment").

**Recommended pilot addition, not yet built into this instrument:** an exploratory (non-scored)
item after the Condition 4 vignette asking respondents to estimate the racial composition of the
described neighborhoods, to turn "does 'minority and lower-income' actually cue race" into a
measured pilot finding rather than an assumption — possibly run alongside a "lower-income only"
(no "minority") wording variant in the pilot to test whether the word "minority" is doing real
work. Neither has been built or piloted.

---

**Original 2-condition text (2026-08-27/08-29), retained below for reference only — superseded by
the 4-arm design above, not currently part of the instrument flow:**

Both versions describe a fictitious city ("Meridian Falls") adopting an ALPR camera network —
matching Tariff Paper's own convention of a fictitious-but-realistic stimulus name rather than a
real, identifiable city (`2026-08-16-study2-design-memo.md` explicitly recommends paraphrasing the
mechanism, not directly quoting or naming a real case, "to avoid conflating the stimulus with a
real, identifiable news event respondents might recognize and react to as news rather than as the
intended manipulation"). The disclosure mechanism in both versions is grounded in the corpus's real
recurring pattern (Bend's "National Lookup" default; Mountain View's undisclosed federal/state
query access) but written as a generic, unnamed policy mechanism, not a quotation or a
recognizable real-world detail.

**Shared opening (both conditions):**

> The city of Meridian Falls recently approved a contract with a private company to install
> automated license-plate-reader (ALPR) cameras at intersections throughout the city. The cameras
> photograph license plates of passing vehicles and check them against law-enforcement databases.
> City officials said the goal is to help local police solve property crimes like car theft.

**Condition A — Transparent/local-only (disclosed):**

> As part of the contract, the city published a public data-sharing policy stating that camera
> data would be accessible only to the Meridian Falls Police Department, for local investigations,
> and would not be shared with any outside agency without a warrant. The policy was presented to
> the city council in a public meeting before the contract was approved, and residents were able to
> review it in advance.

**Condition B — Secret/broad-access default (undisclosed):**

> After the cameras were installed, a local news investigation found that the camera system had a
> default setting that automatically allowed federal agencies and out-of-state police departments
> to search the city's camera data. The city council had not been told about this setting when it
> approved the contract. City officials said they had not known the setting existed until the news
> investigation brought it to their attention.

FK 14.9 (Condition A) / 15.2 (Condition B) originally, improved to 13.7 for Condition B after a
2026-08-29 sentence split — both still well above the 8th-grade target, which is the main reason
the 4-arm v2 wording above (FK 7.6-9.7) is the recommended design going forward. Full history of
this original design's mechanical fixes remains in
`notes/2026-08-29-vignette-mechanical-fixes-and-buildout.md` and
`notes/2026-08-27-webfetch-retry-and-study2-vignette-face-validity-review.md` for reference.

## 5. Manipulation checks (revised 2026-09-20 for the 4-arm design)

**Redesigned 2026-09-08** as one shared item across all 4 arms, which also functions as a
cross-contamination check (an incorrect answer reveals whether a respondent confused their actual
condition with another arm's content) — replaces the original per-condition forced-choice recall
item below, which was written for the 2-condition disclosure design and no longer fits the 4-arm
content.

> "According to the description, which of the following is true about the camera network in
> Meridian Falls?"
> (a) It helped identify a car connected to a string of burglaries. [correct — Safety-benefit]
> (b) Many other police departments can search the camera data. [correct — Broad-network-access]
> (c) An independent analysis found cameras concentrated in some neighborhoods more than others.
>     [correct — Disparate-impact]
> (d) None of the above were mentioned. [correct — Neutral]

Continuous clarity item (generic wording, works across all 4 arms, carried over unchanged from the
original design): "How clearly did the description explain what happened with this camera
network?" (1 = not at all clearly, 7 = very clearly).

**Pass-fail criteria (set before piloting, per the 08-19 note, still applicable):** expect a strong
main effect of condition on the continuous item, and ≥80% correct on the shared forced-choice item
per condition before treating the manipulation as validated. Not yet piloted, so not yet tested.

**Original 2-condition-design item, retained for reference only, no longer part of the flow:**
Forced-choice recall — "According to the description, who can access the camera network's data?"
— *local police department only* / *local police plus federal and out-of-state agencies* / *not
specified* / *don't recall*. (Per `notes/2026-08-19-instrument-adaptation-and-manipulation-checks.md`.)

## 6. Confound checks

Per the same note — should show **no** significant difference between conditions:

- "This description was easy to understand." (perceived complexity/length)
- Source-credibility items (Hovland & Weiss 1951, reused from Tariff Paper's own confound battery
  for cross-project consistency — perceived city/police-department credibility or likability).
- "This reads like something that could really happen in a city adopting this kind of camera
  network." (perceived realism)

## 7. Mediator 1 — Perceived procedural injustice (Quality of Decision Making)

Final wording per `notes/2026-08-20-face-validity-review-scale-items.md` (supersedes 08-19's
first-draft wording — items 3 revised there for double-barreling, referent standardized to "the
city"). Source: Reisig, Bratton, & Gertz (2007). 4-point scale (1 = strongly disagree, 4 = strongly
agree).

1. The city made its decision about camera data-sharing based upon the facts.
2. The city explained its camera data-sharing decision to the people it affects.
3. The city made its camera data-sharing decision based on its own opinions, not the facts.
   *(reverse-scored)*
4. The city made its camera data-sharing decision to handle the tradeoffs fairly.
5. The city didn't listen to residents before deciding how camera data would be shared.
   *(reverse-scored)*

**Supplementary/cut-first-if-trimming (Quality of Treatment, referent "the police department"
per the 08-20 note):**

6. The police department treats residents with respect regarding the camera network.
7. The police department takes time to listen to residents' concerns about the camera network.
8. The police department treats residents fairly regarding the camera network.
9. The police department respects residents' rights regarding the camera network.
10. The police department is courteous to residents who raise concerns about the camera network.

## 8. Moderator 1 — Prior distributive-surveillance-exposure (first-stage moderator)

**Britton's open design call — instrument branches here, per `notes/2026-08-16-study2-design-memo.md`
and `notes/2026-08-21-irb-application-draft.md`. Not resolved by this pass.**

- **Path A (archival, recommended in the design memo):** no survey item here — the moderator is
  computed after the fact by linking the ZIP/tract collected in Section 2 to a camera-density/
  demographic disparity score (Flock deployment data or the DeFlock tracker, cross-referenced with
  Census tract data). Requires the geographic-linkage data-engineering work flagged as unresolved
  in the design memo and IRB draft.
- **Path B (self-report fallback):** single survey item — "To your knowledge, are ALPR cameras in
  your area concentrated in some neighborhoods more than others?" (Yes, in certain neighborhoods
  more than others / No, spread evenly / Don't know / Not sure my area has ALPR cameras at all).

**If Path A is adopted, omit this section from the participant-facing instrument entirely** (the
ZIP collection already happened in the screener) — it is included here only to show where in the
flow Path B's item would sit if that path is chosen instead.

## 9. Mediator 2 — Institutional trust (Trust in Police)

Final wording per `notes/2026-08-20-face-validity-review-scale-items.md` (items 2 and 4 revised
there — see that note for the construct-contamination rationale). Source: Reisig, Bratton, & Gertz
(2007), Trust in Police subscale. 4-point scale, referent "the police department" throughout.

1. The police department has too much power over how camera data is used. *(reverse-scored)*
2. People's basic rights are well protected by the police department's handling of camera data.
3. The police department can be trusted to make the right decisions about camera data in your
   community.
4. The police department does a good job running the camera network.

## 10. Moderator 2 — Perceived crime-solving necessity (last-stage moderator)

Per `notes/2026-08-19-instrument-adaptation-and-manipulation-checks.md`. Source: Miethe,
Dudinskaya, Forepaugh, & Sousa (2025). Agree/disagree format, matching source. Analyzed as two
single-item measures (per source's own reporting practice) — no internal-consistency check
available for this construct, a real limitation to note in the eventual Methods section.

1. ALPR (license-plate-reader) cameras increase public safety.
2. The privacy costs of ALPR cameras outweigh their public safety benefits. *(reverse-scored if
   summed into an index)*

## 11. DV — Opposition intention

Per `notes/2026-08-19-instrument-adaptation-and-manipulation-checks.md`. Source: van Zomeren,
Spears, Fischer, & Leach (2004), Study 2 4-item version (α = .84 in source). 7-point Likert (1 =
not at all, 7 = very much).

1. I would participate in a demonstration against the camera network's continued operation.
2. I would participate in raising our collective voice to stop the camera network's continued
   operation.
3. I would do something together with fellow residents to stop the camera network's continued
   operation.
4. I would participate in some form of collective action to stop the camera network's continued
   operation.

## 12. Demographics

Matching Tariff Paper's own demographic battery for cross-project consistency where the constructs
overlap (`TARIFF_PAPER/notes/2026-08-04-full-instrument-assembly.md`), plus one study-specific
item:

- Age, gender, household income bracket, education.
- Political ideology (single 7-point liberal–conservative item) — relevant here for the same
  reason Tariff Paper includes it (a live polarization dimension), and directly relevant to this
  paper's own topic given policing/surveillance attitudes are well-documented to correlate with
  political ideology; worth testing as a supplementary covariate/robustness check, not part of the
  hypothesized model.
- Prior direct contact with law enforcement in a stop or investigation (Yes/No/Prefer not to say)
  — study-specific; flagged as sensitive per the IRB draft's Risk/Benefit note about this topic
  touching personally salient material for some respondents. Optional item, "prefer not to say"
  always available.

## 13. Debriefing

Full statement already drafted in `notes/2026-08-21-irb-application-draft.md` ("Debriefing
statement (Study 2 and Pretest) — first draft") — not reproduced here to avoid two divergent
copies; that file is the single source for debriefing text. Includes researcher and IRB contact
information (real, not placeholder, per that note — confirm current before use).

---

## What's still needed before this is fieldable

**Updated 2026-09-20 for the 4-arm design — see the sync note at the top of this file.**

1. **Britton's read-through** — nothing here has been reviewed, same standing caveat as every
   other draft in this project, including this session's 4-arm sync itself.
2. **Remaining open design calls:** Section 8's Path A/B branch (archival vs. self-report
   Moderator 1), and PLS-SEM vs. Hayes-PROCESS analysis. The single-manipulation-vs.-factorial call
   is now resolved (4-arm single-factor design, per the sync note).
3. **Actual piloting** — the 4-arm vignette text (Section 4) has a real, measured Flesch-Kincaid
   check (FK 7.6-9.7, near the 8th-grade target) but **no human pilot yet**, same standing gap as
   the original design. This remains the single highest-priority item before fielding anything.
4. **Baseline-trust-in-police item wording** (Section 2b) — not yet drafted; needed both as the
   pre-exposure moderator measure and as the oversampling screener.
5. **Exploratory race-composition item and "lower-income only" wording variant** (flagged in
   Section 4) — recommended for the pilot, neither built yet.
6. **Platform build** — this is a content-order document, not a configured Qualtrics/panel-vendor
   flow. No branching logic, 4-arm randomization weights, or attention-check placement have been
   implemented anywhere.
7. **CloudResearch account and its equivalent (if any) to Prolific's custom-allowlist follow-up-
   invite mechanic** for the oversampling design (`notes/2026-09-08-four-arm-vignette-draft.md`) —
   needs checking once Britton has the account.
8. **IRB submission** covering both the student/convenience-sample pilot and the CloudResearch main
   study — explicitly not started (Britton's 2026-09-08 call to defer this).
9. A priori power analysis — **done 2026-09-08** via Monte Carlo simulation (see
   `notes/2026-09-08-four-arm-vignette-draft.md`'s Power Analysis section and
   `Study2_Methods_Section_DRAFT_2026-08-29.md`'s updated Sample Size subsection); still pending
   final target N, which depends on the PLS-SEM-vs-PROCESS decision and how much the
   literature-informed effect-size assumptions (Merola, Lum & Murphy 2018's d=.33) are trusted.
