# 2026-08-31 — Concrete wording options for the two open vignette issues (readability gap,
# Condition B incompetence confound) — options only, neither decided

## What this is

Continues the autonomous build-out under the project's standing 2026-08-16 Phase 3/instrument-build
exception (`notes/2026-08-16-phase3-theme-review-and-theory-lock.md`). No locked theme, hypothesis,
or design element was changed tonight. This session does **not** decide either of the two vignette
issues below — both are explicitly flagged in every recent note (08-27, 08-29) as content/framing
questions reserved for Britton or a pilot, not mechanical fixes. What follows is concrete, scored
wording alternatives so that whichever way he wants to go, there's real drafted material and real
numbers to start from rather than an abstract flag. Nothing here has been substituted into
`Study2_Instrument_DRAFT_2026-08-27.md` — that file is unchanged.

None of the three items reserved for Britton (archival-moderator feasibility, single-manipulation
vs. factorial, PLS-SEM vs. Hayes-PROCESS) were touched.

Tooling note: `textstat` was not installed in this session's environment (prior sessions' installs
don't persist across sessions); reinstalled via `pip install textstat`, and the same
`NLTK_ALLOW_PROXIED_URLOPEN=1` opt-in the 08-29 note flagged was needed again to download the
`cmudict` syllable corpus. Re-ran the existing vignette (shared opening + both conditions, as
currently drafted) first, as a sanity check — got FK grade 14.9 (Condition A) / 13.7 (Condition B),
matching the 08-29 note's own numbers exactly, confirming the calculation method is being applied
consistently across sessions. Script: `readability_options.py` in this session's scratchpad
(not part of the repo, per convention — not committed).

---

## 1. Reading-level gap — two concrete simplified alternatives, scored

### The problem, restated with the numbers

Current draft (`Study2_Instrument_DRAFT_2026-08-27.md`, Section 4), full vignette (shared opening +
condition text):

| | Words | Sentences | FK Grade | Flesch Ease |
|---|---|---|---|---|
| Condition A (current) | 121 | 5 | 14.9 | 31.3 |
| Condition B (current, post-08-29 split) | 121 | 6 | 13.7 | 32.5 |

Stated instrument target (per `notes/2026-08-21-irb-application-draft.md`'s consent-language
convention, applied by extension to the vignette in the 08-27 review): ~8th grade. Current gap:
roughly six grade levels.

### Option "Moderate" — shorter sentences, plain-language substitutions, technical terms kept but introduced

Rewrites every sentence to one clause where possible, replaces "intersections throughout the city"
→ "streets around the city," "photograph license plates of passing vehicles and check them against
law-enforcement databases" → "take pictures of license plates on passing cars. They check the
plates against police databases," and drops the appositive ALPR definition into its own short
sentence rather than a parenthetical. No fact, number, or causal claim changed from the current
draft — same actors, same sequence of events, same specific details (warrant requirement, "city
council was not told," "officials said they did not know").

**Shared opening (moderate):**

> The city of Meridian Falls recently signed a contract with a private company. The company will
> install license-plate-reader cameras on streets around the city. These are called ALPR cameras
> for short. The cameras take pictures of license plates on passing cars. They check the plates
> against police databases. City officials said the goal is to help local police solve property
> crimes, like car theft.

**Condition A (moderate):**

> As part of the contract, the city published a public policy about camera data. The policy says
> camera data can only be used by the Meridian Falls Police Department. It can only be used for
> local investigations. It cannot be shared with any outside agency unless a judge approves a
> warrant. The city council reviewed this policy at a public meeting before approving the contract.
> Residents could read the policy before the meeting, too.

**Condition B (moderate):**

> After the cameras were installed, a local news investigation found a problem. The camera system
> had a default setting that let federal agencies and police departments from other states search
> the city's camera data. This happened automatically, without the city choosing it. The city
> council was not told about this setting when it approved the contract. City officials said they
> did not know the setting existed until the news investigation found it.

| | Words | Sentences | FK Grade | Flesch Ease |
|---|---|---|---|---|
| Shared opening | 64 | 6 | 7.7 | 58.5 |
| Condition A full | 138 | 12 | **8.6** | 53.5 |
| Condition B full | 136 | 11 | **9.0** | 52.5 |

This lands within roughly one grade level of the stated 8th-grade target on both conditions — a
real, substantial improvement over the current 13.7-14.9 — while every sentence is still a complete,
naturally-phrased sentence (not clipped fragments) and the wording stays close enough to the current
draft that face validity likely transfers without a fresh review. Condition-specific word count:
A = 74, B = 72 (close to matched, within 2 words — comparable to the current draft's 67/67 match).

### Option "Aggressive" — shortest possible sentences, plainest possible words

Pushes further: nearly all sentences under 10 words, "a default setting that let federal agencies
and police departments from other states search the city's camera data" split across three
sentences, "No one turned this setting on by hand. It was on by default." as an explicit plain-
language gloss on "default setting."

**Shared opening (aggressive):**

> Meridian Falls is a city. The city signed a contract with a private company. The company will put
> cameras on city streets. The cameras read license plates on cars. This is called ALPR technology.
> The cameras check plates against police records. City officials say the cameras will help stop
> car theft.

**Condition A (aggressive):**

> The city wrote a public policy about the camera data. Only the Meridian Falls Police Department
> can use the data. Police can only use it for local cases. Police cannot share the data with
> outside agencies. An outside agency needs a warrant from a judge first. The city council saw this
> policy at a public meeting. This happened before the council approved the contract. Residents
> could also read the policy before that meeting.

**Condition B (aggressive):**

> After the cameras were installed, local news found a problem. The camera system had a hidden
> setting. The setting let federal agencies search the city's camera data. It also let police from
> other states search the data. No one turned this setting on by hand. It was on by default. The
> city council did not know about the setting. The council did not know when it approved the
> contract. City officials say they also did not know. They learned about it from the news
> investigation.

| | Words | Sentences | FK Grade | Flesch Ease |
|---|---|---|---|---|
| Shared opening | 51 | 7 | 6.2 | 63.4 |
| Condition A full | 124 | 15 | **7.0** | 59.9 |
| Condition B full | 136 | 17 | **5.7** | 68.7 |

This clears the 8th-grade target with room to spare (in fact undershoots it — 5.7-7.0), but at a
real cost: (a) word-count symmetry across conditions gets *worse*, not better — condition-specific
text is 73 words (A) vs. 85 words (B), a 12-word gap, versus the current draft's near-exact 67/67
match and the Moderate option's 74/72; (b) the choppy, declarative-sentence style ("It was on by
default." "The council did not know when it approved the contract.") reads noticeably less like
natural news-style prose and more like a controlled-reading-level exercise, which plausibly risks
tripping the instrument's own existing realism confound check (Section 6: "This reads like something
that could really happen in a city adopting this kind of camera network") — a real trade-off between
solving one confound risk (reading level) and creating exposure to another (perceived
artificiality/unrealism) that a genuinely 8th-grade target does not automatically avoid.

### Recommendation framing (not a decision)

Moderate gets close to the target (8.6/9.0 vs. an 8th-grade goal) with lower realism risk and
better-preserved word-count symmetry than Aggressive, which overshoots the target and reintroduces a
symmetry gap while risking the realism confound. If Britton wants to close the reading-level gap
before piloting, Moderate looks like the better starting draft of the two — but this is a
face-validity read, not a test; either option (or something between them) needs the same human
pilot every prior note has flagged as the real gate, and any adopted wording should get its own
face-validity pass before fielding, same as the current draft got on 08-27. Both options are left
here as drafted alternatives; neither has been substituted into the instrument document.

---

## 2. Condition B's incompetence-confound framing — three concrete alternatives, scored

### The problem, restated

`notes/2026-08-27-webfetch-retry-and-study2-vignette-face-validity-review.md` (finding 2d) flagged
that Condition B's "discovered via news investigation, officials didn't know" framing may confound
the intended manipulation (disclosed vs. secret default data-sharing) with a *different* signal:
perceived government incompetence (officials who "didn't know" what their own contract did read as
inattentive/negligent, not just secretive). The 08-29 note applied a mechanical sentence-split fix
but explicitly left this substantive question untouched. It remains open.

A relevant framing for why this matters theoretically, not just as a wording nitpick: Mayer, Davis,
& Schoorman's (1995) ability/benevolence/integrity model of organizational trust — *"An Integrative
Model of Organizational Trust," Academy of Management Review, 20(3), 709-734* (bibliographic
details corroborated tonight via WebSearch against a JSTOR listing and an independent academic
citation-index page; not independently full-text fetched this session, so treat this as the same
WebSearch-triangulated confidence tier used elsewhere in this project's notes, not a direct-fetch
verification) — distinguishes trust erosion driven by perceived *ability* (competence) from trust
erosion driven by perceived *integrity* (honesty/good faith). "Officials didn't know" is squarely an
ability-type signal (they should have known, they were careless); this paper's actual theoretical
target — institutional secrecy — is more naturally an integrity-type signal (information was
deliberately withheld). If the current wording pulls respondents toward an ability/competence
judgment instead of (or alongside) the intended integrity/secrecy judgment, Mediator 2 (institutional
trust, Reisig/Bratton/Gertz 2007) could be responding to a mixed signal rather than a clean test of
the secrecy manipulation — this is not just a face-validity concern, it bears directly on construct
validity for the paper's own locked theory chain. This is offered as theoretical grounding for why
the confound is worth resolving, not as a citation added to the manuscript draft itself.

### Option 1 — Baseline (current draft): "officials didn't know" (negligence/incompetence framing)

> After the cameras were installed, a local news investigation found that the camera system had a
> default setting that automatically allowed federal agencies and out-of-state police departments to
> search the city's camera data. The city council had not been told about this setting when it
> approved the contract. City officials said they had not known the setting existed until the news
> investigation brought it to their attention.

FK grade (full vignette): 13.7. Words (condition text): 67. This is the version flagged as
potentially confounded.

### Option 2 — "Concealment" framing: officials knew, chose not to disclose

> After the cameras were installed, a local news investigation found that the camera system had a
> default setting that automatically allowed federal agencies and out-of-state police departments to
> search the city's camera data. City records later showed that officials were aware of this setting
> before the contract was approved, but did not share this information with the city council or the
> public.

FK grade (full vignette): 15.0. Words (condition text): 62.

This directly removes the incompetence signal and replaces it with a cleaner integrity/secrecy
signal (officials knew and withheld it) — arguably the wording most directly aligned with the
paper's own theoretical construct name ("institutional secrecy"). But it is not a free substitution:
it changes the moral character of Condition B from an oversight/failure story to a deliberate-
deception story, which is a stronger, more adversarial claim about the fictitious city government
than the current draft makes. Two things worth flagging for whoever decides this: (a) it may
*increase* effect sizes on the mediators relative to the current draft, which is not obviously wrong
(a cleaner manipulation of the intended construct) but is a real shift in what "Condition B" means
substantively, not just stylistically; (b) it introduces a new specific claim — "city records later
showed officials were aware" — that itself would need to survive scrutiny as a plausible vignette
detail (how would a fictitious city's internal awareness become public record before the meeting the
respondent is being asked to evaluate?), a minor internal-plausibility question the current draft's
"officials said they hadn't known... until the investigation" framing avoids by keeping the discovery
mechanism the same for the vignette and for the reader.

### Option 3 — "Neutral" framing: state the fact of non-disclosure, omit officials' state of knowledge entirely

> After the cameras were installed, a local news investigation found that the camera system had a
> default setting that automatically allowed federal agencies and out-of-state police departments to
> search the city's camera data. This setting had not been disclosed to the city council or the
> public before the contract was approved.

FK grade (full vignette): 14.3. Words (condition text): 51.

This drops the "officials said they didn't know" sentence entirely rather than replacing it with a
different claim about officials' knowledge. It states only what actually differs from Condition A
(disclosed vs. not disclosed) without taking a position on why it wasn't disclosed — negligence,
deliberate concealment, or something else are all left to the respondent's own inference rather than
supplied by the stimulus. A concrete reason this is a plausible strong candidate, not just a
compromise: **neither of the instrument's two manipulation-check items (Section 5) tests officials'
state of knowledge at all** — both ask what the respondent recalls about *who can access the data*,
not whether officials knew about the setting. The "officials didn't know" sentence is doing zero
manipulation-check-relevant work in the current draft; it exists only for narrative plausibility
(explaining how the secret setting became public), which Option 3's shorter phrasing ("had not been
disclosed... before the contract was approved") still accomplishes without asserting anything about
officials' awareness. This option is also the shortest of the three (51 words vs. 67/62), which
independently helps the readability gap in Section 1 above.

The trade-off: Option 3 is less narratively vivid/concrete than either alternative (no "who found
out and how" story beat), and by leaving the reason for non-disclosure ambiguous, it may increase
between-respondent variance in what respondents infer (some will assume incompetence, some
concealment, some something else) rather than controlling for it — which could either be a feature
(the vignette manipulates only the theoretically-intended variable, disclosure status, and lets
naturally-occurring attribution variance become a measurable individual-difference moderator instead
of an uncontrolled confound baked into the stimulus) or a bug (more measurement noise on the
mediators), depending on how it's used analytically. That is itself a design judgment, not a
wording one.

### Summary table

| Option | FK grade (full) | Condition-text words | Confound direction | Narrative concreteness |
|---|---|---|---|---|
| 1. Baseline (current) | 13.7 | 67 | Ability/incompetence-leaning | High |
| 2. Concealment | 15.0 | 62 | Integrity/deception-leaning (arguably closer to construct) | High, but stronger claim |
| 3. Neutral | 14.3 | 51 | Attribution left to respondent; no manipulation-check item touches it either way | Lower |

None of these is adopted. All three remain compatible with the locked primary theory chain
(disclosed vs. secret default data-sharing) — the difference is only in how Condition B explains
*why* the secret setting existed and was found, not in the disclosure/non-disclosure fact itself,
which is unchanged across all three and remains the actual manipulated variable per the
manipulation-check items.

---

## What this session did not do

- Did not substitute either the readability options or the confound-framing options into
  `Study2_Instrument_DRAFT_2026-08-27.md`. That document is unchanged.
- Did not decide the reading-level gap or the Condition B framing question — both remain Britton's
  or a pilot's call, per every prior note's explicit boundary on this point.
- Did not touch the three reserved design calls (archival-moderator feasibility, single-manipulation
  vs. factorial, PLS-SEM vs. Hayes-PROCESS).
- Did not run a new literature-gap sweep or add any new citation to the Introduction/Theory draft —
  this session's time went entirely into the two wording-option analyses above. The Przeszlowski &
  Guerette (2025) ScienceDirect direct-fetch spot-check flagged as still open in the 08-29 note
  remains open and was not re-attempted tonight.
- Did not independently fetch the Mayer, Davis, & Schoorman (1995) full text — cited above at
  WebSearch-triangulated confidence (title/journal/volume/pages corroborated via JSTOR + an academic
  citation-index page), used only as theoretical framing for why the confound matters, not added as
  a source in any manuscript draft.

## Open items for Britton

1. Everything already open in prior notes remains open (archival-moderator feasibility,
   single-manipulation vs. factorial, PLS-SEM vs. PROCESS, CITI certificate number, power analysis,
   Theme 3 promotion gut-check, the consent risk-language sentence's own reading level, the
   Przeszlowski & Guerette direct-fetch spot-check, the two adjacent Shjarback literature items from
   08-29/08-30).
2. New: two scored, drafted alternative vignette texts (Moderate, Aggressive) for closing the
   reading-level gap — Moderate gets within about one grade level of the stated 8th-grade target
   (FK 8.6-9.0) without the word-count-symmetry loss or realism-confound risk that Aggressive
   (FK 5.7-7.0) introduces. Neither has been substituted into the instrument or pilot-tested.
3. New: three scored, drafted alternative Condition B framings for the incompetence-confound
   question (baseline/current, concealment, neutral) — Option 3 (neutral) is flagged as a candidate
   worth serious consideration because the manipulation-check items don't test officials' knowledge
   state at all, meaning that sentence's content is currently doing no measured work and could be
   shortened to just the disclosure fact without weakening the actual manipulation. Option 2
   (concealment) is flagged as the closest wording to the paper's own "institutional secrecy"
   construct language, grounded in the ability/benevolence/integrity trust framework (Mayer, Davis &
   Schoorman 1995), but changes Condition B from a negligence story to a deliberate-deception story,
   a substantive shift worth his eyes before adopting. None of the three is recommended over the
   others outright — this is presented as an options table, not a pick.
4. If Britton picks a direction on either issue, the natural next autonomous step is substituting
   the chosen wording into `Study2_Instrument_DRAFT_2026-08-27.md` Section 4, re-running the
   confound-check/manipulation-check logic against the new text, and flagging it for a fresh
   face-validity pass (matching the 08-27 review's own process) before any pilot.
