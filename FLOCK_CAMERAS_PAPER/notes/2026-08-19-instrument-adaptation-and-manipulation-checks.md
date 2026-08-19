# 2026-08-19 — Adapt verified scale wording to the ALPR context + draft manipulation-check items

Closes out items #3 and #4 from `2026-08-16-scale-sourcing.md`'s "what Britton needs to do"
list — both explicitly flagged there as not needing his input first (#3 has no literature
dependency, #4 is mechanical adaptation of already-verified wording). Both proceed under his
standing one-time exception for this paper only (Phase 3/instrument-build autonomy) — nothing
here touches the two items that *do* need him (#2 archival-moderator feasibility sign-off, the
factorial-vs-single-manipulation and PLS-SEM-vs-PROCESS design calls from the study2 memo).

**Framing anchor used throughout:** per the study2 design memo, the manipulation is disclosure
condition (secret/broad-access default vs. transparent/local-only), and Mediator 1 (procedural
injustice) is specifically about *the process by which the camera network's data-sharing policy
was set and disclosed* — not general policing quality. That distinction drove which of Reisig
et al.'s two subscales to lead with below.

---

## Mediator 1 — Perceived procedural injustice (adapted from Reisig, Bratton, & Gertz 2007)

Original source has two 5-item subscales (Quality of Treatment, Quality of Decision Making).
**Recommend leading with Quality of Decision Making** — it's the subscale that's actually about
*how the data-sharing decision was made and explained*, which is what this study's manipulation
varies; Quality of Treatment is about general interpersonal conduct, not decision process, and
is a weaker match to what's being manipulated.

**Quality of Decision Making (primary, adapt all 5):**
1. The [police department / city] made its decision about camera data-sharing based upon the
   facts.
2. The [police department / city] explained its camera data-sharing decision to the people it
   affects.
3. The [police department / city] made its camera data-sharing decision based on its own
   opinions, not what residents wanted. *(reverse-scored)*
4. The [police department / city] made its camera data-sharing decision to handle the tradeoffs
   fairly.
5. The [police department / city] didn't listen to residents before deciding how camera data
   would be shared. *(reverse-scored)*

**Quality of Treatment (secondary/supplementary — include if instrument length allows, cut
first if trimming):**
6. The [police department / city] treats residents with respect regarding the camera network.
7. The [police department / city] takes time to listen to residents' concerns about the camera
   network.
8. The [police department / city] treats residents fairly regarding the camera network.
9. The [police department / city] respects residents' rights regarding the camera network.
10. The [police department / city] is courteous to residents who raise concerns about the
    camera network.

4-point scale, matching the source (1 = strongly disagree, 4 = strongly agree), per
scale-sourcing note's own recommendation to keep response scales as the source studies used
them. Bracketed [police department / city] — pick one consistently based on which entity the
vignette frames as the decision-maker (the study2 memo's vignette centers a *city* adopting the
network, with the *police department* as the operating agency — recommend "the city" for items
about the disclosure/adoption decision specifically, since that's the manipulated actor, and
pilot both if there's any doubt residents distinguish the two).

## Mediator 2 — Institutional trust (adapted from Reisig et al. 2007, Trust in Police subscale)

Scale-sourcing note already recommended this 4-item subscale over the fuller 8-item legitimacy
index, for good reason (avoids conflating trust with the obligation-to-obey construct this
paper's chain doesn't need):

1. The police in your community have too much power over how camera data is used. *(reverse-
   scored)*
2. People's basic rights are well protected under the camera network's current policies.
3. The police can be trusted to make the right decisions about camera data in your community.
4. The police department does a good job managing the camera network responsibly.

4-point scale, same as source. Item 4 is the furthest adaptation from the original ("do their
job well" → "manages the camera network responsibly") since the source item is a general
police-competence item with no direct data-management analog — flagging this one specifically
for face-validity piloting, the other three track the source wording closely.

## Moderator 2 — Perceived crime-solving necessity (adapted from Miethe, Dudinskaya, Forepaugh, & Sousa 2025)

Both items from the source's paired-item approach, directly parallel (same technology-adjacent
construct — facial recognition → ALPR, both policing surveillance tech):

1. ALPR (license-plate-reader) cameras increase public safety.
2. The privacy costs of ALPR cameras outweigh their public safety benefits. *(reverse-scored
   if summed with item 1 into a single index; can also be analyzed as two separate single-item
   measures, matching how Miethe et al. themselves report them)*

Agree/disagree format, matching source. Single-item-per-construct means this moderator has no
internal-consistency check available — worth noting as a real limitation in the methods
section (same honest-limitations standard as everything else in this project), not a reason to
invent additional items with no source.

## DV — Opposition intention (adapted from van Zomeren, Spears, Fischer, & Leach 2004, Study 2 4-item version)

Recommend the 4-item Study 2 version per the scale-sourcing note (α = .84, more complete than
the 3-item Study 1 version):

1. I would participate in a demonstration against the camera network's continued operation.
2. I would participate in raising our collective voice to stop the camera network's continued
   operation.
3. I would do something together with fellow residents to stop the camera network's continued
   operation.
4. I would participate in some form of collective action to stop the camera network's continued
   operation.

7-point Likert (1 = not at all, 7 = very much), matching source exactly.

---

## Manipulation-check items (construct #1 — no literature dependency, study-specific)

Modeled directly on Tariff Paper's own manipulation/confound-check structure
(`TARIFF_PAPER/notes/2026-08-04-pretest-design.md`) — same logic, adapted construct.

**Manipulation check (should differ sharply by condition):**
- Continuous item: "How clearly did the description explain who can access the camera
  network's data?" (1 = not at all clearly, 7 = very clearly)
- Forced-choice recall: "According to the description, who can access the camera network's
  data?" — *local police department only* / *local police plus federal and out-of-state
  agencies* / *not specified* / *don't recall*. (Correct answer differs by condition — this is
  the primary manipulation-check item, matching Tariff's forced-choice-recall pattern exactly.)

**Confound checks (should show NO significant difference between the two conditions —
same logic as Tariff's confound battery):**
- Perceived message length/complexity ("this description was easy to understand").
- Perceived city/police-department credibility or likability — adaptable from the Source
  Credibility Model (Hovland & Weiss 1951), same source Tariff Paper already uses for its own
  confound check, reasonable to reuse here for consistency across the four papers' instruments.
- Perceived realism ("this reads like something that could really happen in a city adopting
  this kind of camera network").

**Pass-fail criteria, set before piloting (same standard as Tariff's pretest design):** expect
a strong main effect of disclosure condition on the manipulation-check items, no significant
difference on the confound items, and a concrete forced-choice-recall threshold (e.g., ≥80%
correct per condition) before treating the manipulation as validated.

---

## What's still open (unchanged from 2026-08-16, not touched by this pass)

1. Archival distributive-surveillance-exposure moderator — needs Britton's feasibility
   sign-off (Flock deployment data / DeFlock tracker + Census access), still unaddressed.
2. Single-manipulation vs. factorial design, and PLS-SEM vs. Hayes-PROCESS — both still his
   calls per the study2 memo.
3. **New from this pass:** face-validity piloting for the items flagged above (Trust item 4's
   wording distance from source; whether "the city" vs. "the police department" reads correctly
   to pilot respondents) — normal instrument-development next step, not a literature gap.
4. No IRB draft exists yet for this project (unlike Tariff Paper, which has one in progress) —
   worth flagging as a real gap once Study 2 moves toward actual fielding, same human-subjects
   care standard as the other three papers.
