# 2026-08-20 — Face-validity review of adapted scale items

Closes out open item #3 from `2026-08-19-instrument-adaptation-and-manipulation-checks.md`
("face-validity piloting for the items flagged above... normal instrument-development next
step, not a literature gap"). Proceeds under the same standing one-time Phase 3/instrument-build
exception as 08-16/08-19 (`2026-08-16-phase3-theme-review-and-theory-lock.md`) — this is
face-validity/wording review of already-verified, already-sourced item sets, not a new design
decision. Does **not** touch either Britton-gated item: archival distributive-surveillance-
exposure moderator feasibility, and single-manipulation-vs-factorial / PLS-SEM-vs-PROCESS. Both
untouched.

Method: re-read each adapted item side-by-side against the exact source wording transcribed in
`2026-08-16-scale-sourcing.md` (which was pulled directly from the Reisig et al. 2007, Miethe et
al. 2025, and van Zomeren et al. 2004 source PDFs via Ole Miss library access — real, verified
text, not reconstructed from memory). Flagging anywhere the adapted wording drifts from what the
source item is actually measuring, not just anywhere the phrasing sounds awkward.

---

## 1. Trust item 4 — construct contamination, not just "distance from source"

08-19's note flagged this one as "the furthest adaptation from the original" but described the
problem as wording distance. Looking at it again against the source text specifically, the
problem is more precise than distance — it's **construct contamination with Mediator 1**.

- Source (Reisig et al. 2007, Trust in Police subscale, item 4): *"Most police officers in your
  community do their job well."* — a general-competence item. No process/fairness content.
- Current adapted version: *"The police department does a good job managing the camera network
  responsibly."*

"Responsibly" imports a normative/procedural-fairness judgment that isn't in the source item at
all — the source is asking about competence ("do their job well"), not about whether the job is
done *fairly* or *properly*. That's a problem specifically because Mediator 1 (procedural
injustice, Quality of Decision Making) already measures exactly that — "handle the tradeoffs
fairly," "based upon the facts." If Trust item 4 reads as another fairness-process item, it risks
cross-loading with Mediator 1 rather than cleanly measuring the distinct "general institutional
confidence" construct Mediator 2 is supposed to capture — a real discriminant-validity risk in a
serial-mediation PLS-SEM model where M1 and M2 sit right next to each other in the chain.

**Revised wording:** *"The police department does a good job running the camera network."*

Keeps the general-competence framing of the source item (swap "do their job well" →parallel
"does a good job running," same register), drops "managing... responsibly," and removes the
fairness-adjacent language entirely. This is the item to prioritize piloting if only one gets
piloted, since it's the one most likely to affect the model's discriminant validity, not just its
face validity.

## 2. Trust item 2 — a second, previously-unflagged drift (agent → policy shift)

Not flagged in the 08-19 note, but the same side-by-side comparison surfaces it:

- Source (item 2): *"People's basic rights are well protected by the police."* — the police are
  the acting/protecting agent.
- Current adapted version: *"People's basic rights are well protected under the camera network's
  current policies."*

The adaptation quietly swapped the acting agent (the police, doing the protecting) for an
evaluation of a policy artifact ("under... current policies"). That's a construct shift, not just
a wording tweak — it turns an item about *trusting the institution* into an item about
*evaluating a policy document*, which again edges toward what Mediator 1's items already measure
(the decision/policy itself). It also breaks internal consistency with Trust items 1 and 3, both
of which correctly keep "the police" as the acting agent ("police... have too much power over how
camera data is used"; "the police can be trusted to make the right decisions about camera data").

**Revised wording:** *"People's basic rights are well protected by the police department's
handling of camera data."*

Restores the police as the protecting agent (matching items 1 and 3's structure), while keeping
the domain-specific anchor ("camera data") that makes it relevant to this study rather than a
generic policing item.

## 3. Procedural injustice item 3 — double-barreled, redundant with item 5

Also not previously flagged. Comparing against source:

- Source (Quality of Decision Making, item 3): *"Make decisions based on their own personal
  opinions"* [reverse-scored] — a single claim, the mirror image of item 1's "based upon the
  facts."
- Current adapted version: *"The [police department / city] made its camera data-sharing
  decision based on its own opinions, not what residents wanted."*

The added clause — "not what residents wanted" — isn't in the source item and turns a single-
construct item into two: (a) was the decision based on the department's/city's own opinions, and
(b) did it ignore what residents wanted. A respondent who believes staff used their own
professional judgment *and* that judgment happened to match what residents wanted has no clean
way to answer. It also duplicates item 5's actual job ("didn't listen to residents before
deciding") — item 5 is already the voice/listening item; item 3 is supposed to be the
facts-vs-opinions item (the reverse mirror of item 1), not a second voice item.

**Revised wording:** *"The [city] made its camera data-sharing decision based on its own opinions,
not the facts."*

Restores the single-construct facts-vs-opinions contrast that mirrors item 1, and removes the
overlap with item 5.

## 4. "The city" vs. "the police department" — resolving the open bracket, with the tension named honestly

08-19 left this as "recommend 'the city'... pilot both if there's any doubt." That's a real,
substantive framing choice, not just a wording question, so it's worth resolving with a stated
rationale rather than leaving the bracket open across the whole instrument.

**The tension, stated plainly:** Reisig et al.'s Quality of Decision Making subscale is
constructed as a *police* process-based-policing measure — the source items are literally about
police decision-making, sitting inside the Tyler procedural-justice-in-policing tradition this
paper's whole theory chain leans on. Using "the city" for that subscale, as 08-19 proposed, is
itself a real adaptation away from the construct's original referent, not a neutral wording
choice — worth stating that openly in the eventual Methods section rather than treating it as a
cosmetic substitution.

**Recommendation, held to given the vignette structure:** this study's actual manipulation is a
*city's* disclosure decision at the point of adoption (per the design memo: "a vignette
describing a city adopting an ALPR camera network..."), not an in-the-field police decision — so
construct-match to *what's manipulated* argues for "the city" specifically for the Quality of
Decision Making items (Mediator 1), even though that's a disclosed departure from Reisig et al.'s
original police-specific referent. Use "the city" consistently across all 5 Quality of Decision
Making items (not mixed per-item) — the two edited above should read "The city made its decision
about camera data-sharing based upon the facts," "The city explained its camera data-sharing
decision to the people it affects," etc.

For Mediator 2 (Trust in Police), keep "the police department" consistently across all 4 items —
that subscale is explicitly the source's "Trust in Police" construct, and this paper's downstream
trust mechanism is specifically about confidence in the operating law-enforcement agency (matches
the real corpus pattern too: in Bend, it's the police department, via Capt. Beekman, whose
trustworthiness comes under public scrutiny after the secrecy revelation, not the city council in
the abstract).

If the secondary Quality of Treatment items (6-10) are used, they're about ongoing interpersonal
conduct toward residents raising concerns — more naturally attributed to the police department as
the agency residents would actually interact with day to day, not the city as an abstract
governing body. Recommend "the police department" for those, if included.

**Net effect:** one consistent, theoretically-stated rule (M1 = "the city," M2 [and Quality of
Treatment, if used] = "the police department") instead of an open per-item bracket. Piloting
whether respondents track this distinction correctly is still a live open item (see below) — this
resolves *which* wording to pilot, not whether piloting is still needed.

## Items checked and left as-is

Compared against source text and found to be clean, non-double-barreled, single-construct
substitutions with no drift worth flagging: Quality of Decision Making items 1, 2, 4, 5;
Quality of Treatment items 6-10 (all direct domain substitutions); Trust items 1 and 3; both
Moderator 2 items (Miethe et al.); all 4 Opposition Intention items (van Zomeren et al.) — the
"this proposal"/"fellow students" → "the camera network's continued operation"/"fellow residents"
substitution is applied consistently across all four and doesn't alter what's being measured;
manipulation-check and confound-check items (study-specific, no source-fidelity question
applies).

---

## Updated item sets (supersedes the flagged items in 2026-08-19's note; that note is left
unedited as the dated record of what was drafted that day)

**Mediator 1 — Procedural injustice, Quality of Decision Making (primary, all referent "the
city"):**
1. The city made its decision about camera data-sharing based upon the facts.
2. The city explained its camera data-sharing decision to the people it affects.
3. The city made its camera data-sharing decision based on its own opinions, not the facts.
   *(reverse-scored)*
4. The city made its camera data-sharing decision to handle the tradeoffs fairly.
5. The city didn't listen to residents before deciding how camera data would be shared.
   *(reverse-scored)*

**Mediator 2 — Institutional trust, Trust in Police (all referent "the police department"):**
1. The police department has too much power over how camera data is used. *(reverse-scored;
   minor grammatical tightening from "the police in your community" for subject-verb consistency
   with the other three items, no construct change)*
2. People's basic rights are well protected by the police department's handling of camera data.
3. The police department can be trusted to make the right decisions about camera data in your
   community.
4. The police department does a good job running the camera network.

All other item sets (Quality of Treatment secondary items, Moderator 2, DV, manipulation/confound
checks) unchanged from 2026-08-19.

---

## What's still open (unchanged in substance, restated for clarity)

1. Archival distributive-surveillance-exposure moderator — still needs Britton's feasibility
   sign-off. Not touched.
2. Single-manipulation vs. factorial design, and PLS-SEM vs. Hayes-PROCESS — both still his
   calls. Not touched.
3. Actual face-validity **piloting** (as opposed to this desk review) is still a real next step —
   this pass resolves what to pilot and fixes the issues a pilot would likely have caught anyway,
   it doesn't substitute for one. Trust item 4's revised wording is the single highest-priority
   item to check in piloting, given the discriminant-validity stakes.
4. No IRB draft yet — unchanged from 08-19.
