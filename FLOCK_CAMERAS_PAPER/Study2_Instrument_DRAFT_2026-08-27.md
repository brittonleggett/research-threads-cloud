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

## 3. Random assignment

Single factor, two conditions, equal-probability randomization (per
`notes/2026-08-16-study2-design-memo.md` — one manipulated antecedent, not the 3×2 factorial
Tariff Paper used). Participant sees exactly one of the two vignettes below.

## 4. Vignette exposure (newly drafted this pass)

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
> default setting — one the city council was not told about when it approved the contract — that
> automatically allowed federal agencies and out-of-state police departments to search the city's
> camera data. City officials said they had not known this setting existed until the news
> investigation brought it to their attention.

**Delivery notes:**
- Include a brief forced pause / minimum-time-on-page setting (e.g., 10 seconds), matching
  Tariff Paper's instrument convention, to discourage skimming.
- Both versions are matched for length and structure (three sentences of shared setup + three
  sentences of condition-specific content) to avoid a length/complexity confound — verify this
  once actual final wording is set; see confound-check items below, which test exactly this.

## 5. Manipulation checks

Per `notes/2026-08-19-instrument-adaptation-and-manipulation-checks.md`, retained in the main
study (not just a separate pretest) for data-quality screening, matching Tariff Paper's own
practice:

- Continuous item: "How clearly did the description explain who can access the camera network's
  data?" (1 = not at all clearly, 7 = very clearly)
- Forced-choice recall: "According to the description, who can access the camera network's data?"
  — *local police department only* / *local police plus federal and out-of-state agencies* / *not
  specified* / *don't recall*.

**Pass-fail criteria (set before piloting, per the 08-19 note):** expect a strong main effect of
condition on both items, and ≥80% correct on the forced-choice item per condition before treating
the manipulation as validated.

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

1. **Britton's read-through** — nothing here has been reviewed, same standing caveat as every
   other draft in this project.
2. **The two open design calls** (Section 8's Path A/B branch; single-manipulation vs. factorial)
   — this document is written to be usable either way for Path A/B, but factorial vs.
   single-manipulation would require a second manipulated vignette dimension not drafted here.
3. **Actual piloting** — the vignette text in Section 4 is newly drafted and has had no
   face-validity review of any kind (unlike the scale items, which went through the 08-20 desk
   review). This is the single highest-priority item to pilot before fielding anything, higher
   priority than the already-reviewed scale items.
4. **Platform build** — this is a content-order document, not a configured Qualtrics/panel-vendor
   flow. No branching logic, randomization weights, or attention-check placement have been
   implemented anywhere.
5. **Length/complexity confound check on the vignette pair (Section 4)** — flagged inline above;
   worth an actual word-count/readability check once the wording is finalized, not just the
   "matched sentence count" design intent stated here.
6. A priori power analysis and finalized target N — still pending the PLS-SEM-vs-PROCESS decision,
   per the IRB draft.
