# 2026-09-08 — Four-arm Study 2 vignette draft (design conversation with Britton)

## What changed and why

Britton reviewed the 9 new papers dropped into `Literature/` this session (see
`notes/` for the extraction) plus a follow-up snowball/search pass, then decided to expand Study 2
from the original 2-condition disclosure manipulation
(`notes/2026-08-16-study2-design-memo.md`, `Study2_Instrument_DRAFT_2026-08-27.md` — that draft
currently only lives in `research-threads-cloud/FLOCK_CAMERAS_PAPER/`, not this local folder; needs
a dual-save sync) into a 4-arm single-factor between-subjects design that mirrors the paper's own
Study 1 candidate themes directly:

1. **Neutral/baseline** — routine deployment, no elaboration.
2. **Safety-benefit** — camera network helps solve a specific crime (ambivalent safety-benefit
   theme; Flock's own public crime-solving claims).
3. **Broad-network-access** — camera data searchable by many outside agencies (institutional
   secrecy/function-creep theme; replaces an earlier ICE-specific draft, see below).
4. **Disparate-impact** — cameras concentrated in minority/lower-income neighborhoods
   (distributive-injustice theme; now the most independently-replicated theme in the corpus per
   the 2026-09-08 literature pass — Monahan 2026, Keener/Finn/Baird 2026, Sapp et al. 2021, CNU
   Hampton Roads study already in the corpus).

Design decisions made this session (all Britton's calls, not defaulted):
- **4 arms, not 5** — dropped a wrongful-stop/accuracy-harm arm to control CloudResearch cost.
- **Between-subjects** (not within) — Britton's explicit call for publishability in policy/PA
  journals.
- **CloudResearch for main fielding, student/convenience sample for pilot** — cost management;
  pilot still needs IRB coverage even as a convenience sample, not exempt just because informal.
- Baseline trust in police added as a moderator (not in the original design memo) — direct
  response to Merola, Lum & Murphy (2018)'s own stated future-research call that their unusually
  high-trust Fairfax County sample likely produced a conservative trust-erosion estimate.

## Vignette text (first full draft, not yet piloted)

**Shared opening (all 4 conditions):**

> The city of Meridian Falls recently installed automated license-plate-reader cameras at
> intersections around the city. The cameras photograph the license plates of passing vehicles and
> check them against law-enforcement databases. City officials said the cameras are meant to help
> local police solve crimes such as car theft.

**Condition 1 — Neutral/baseline (39 words, 2 sentences):**

> The cameras began operating within a few weeks of installation, and the city posted basic
> information about the new system on its public works website. Local news covered the change as
> part of a routine story about city infrastructure.

**Condition 2 — Safety-benefit (37 words, 2 sentences):**

> Two months after the cameras went live, they helped police identify a car connected to a string
> of home burglaries in the area. Police said the arrest would not have happened as quickly without
> the camera network.

**Condition 3 — Broad-network-access (32 words, 2 sentences):**

> The camera network is connected to a national database that many other police departments use.
> Departments in other cities and states can search this database for camera information collected
> in Meridian Falls.

**Condition 4 — Disparate-impact (36 words, 2 sentences):**

> An independent analysis of camera locations found that minority and lower-income neighborhoods
> had far more cameras installed than other parts of the city. Some neighborhoods had several
> cameras within a few blocks, while others had none.

All four are matched on sentence count (2) and stay in a 32-39 word band, active voice throughout,
no embedded parentheticals — designed to avoid the two problems the 08-27 face-validity review
found in the original 2-condition draft (a syntactic-complexity mismatch, and a
readability level of FK 13.7-14.9 against an 8th-grade target). **Not yet run through an actual
Flesch-Kincaid calculation** (the 08-29 note used the `textstat` Python library for the old draft —
same check needed here before piloting) and **not yet human-piloted** — this is a first-pass draft
for Britton's review, same standing caveat as every prior draft in this project.

## Two design calls Britton made explicitly this session

**1. Dropped ICE-specific wording.** An earlier pass in this same conversation drafted Condition 3
around "federal immigration agents, including U.S. Immigration and Customs Enforcement (ICE)" —
Britton flagged ICE as too hot-button a name, risking the manipulation testing partisan reaction to
ICE specifically rather than the intended institutional-secrecy/broken-promise mechanism. Replaced
with generic "many other police departments" / "departments in other cities and states" language,
which is arguably *more* theoretically faithful anyway — the real underlying mechanism per the
Monahan (2026) FOIA data and Flock's actual "National Lookup" network feature is breadth of access
beyond the local department, not immigration enforcement specifically. If a future draft wants to
restore some federal-reach flavor without naming ICE, "federal law enforcement agencies"
(unspecified) is a middle option — not adopted here, flagging in case Britton wants to reconsider.

**2. Race/class wording: "minority and lower-income neighborhoods," not "Black neighborhoods" or
"economically disadvantaged" alone.** Britton was clear he didn't want to explicitly name Black
neighborhoods. He also raised a real, testable concern about "economically disadvantaged" alone:
would respondents actually infer race from purely economic language, or would that manipulation
end up testing a different construct (class-based disparate impact) than the one the literature
actually documents (race + poverty together — Keener, Finn & Baird 2026's own title is "Race,
Poverty, and the Geography of ALPR Deployment"; Sapp et al. 2021's "social justice" construct was
about fair treatment of women/minorities generally, not race alone). Landed on "minority and
lower-income neighborhoods" combined as the closest match to how the strongest supporting papers
actually operationalize this theme, without naming a specific racial group.

**Recommended pilot addition, not yet built into the instrument:** an exploratory (non-scored)
item after the Condition 4 vignette asking respondents to estimate the racial composition of the
described neighborhoods — turns Britton's "I don't know if we could infer race" concern into a
measured pilot finding rather than a design assumption. Worth deciding whether to also run this
same exploratory item under a "lower-income" (no "minority") wording variant in the pilot, to
directly test whether the word "minority" is doing real work or whether "lower-income" alone would
have sufficed — a cheap thing to check with the free/cheap convenience-sample pilot before
committing the CloudResearch budget to one fixed wording.

## Manipulation check — redesigned as one shared item across all 4 arms

Replaces the old per-condition forced-choice recall items with a single item that also functions as
a cross-contamination check (an incorrect answer reveals whether a respondent confused their actual
condition with another arm's content):

> "According to the description, which of the following is true about the camera network in
> Meridian Falls?"
> (a) It helped identify a car connected to a string of burglaries. [correct — Safety]
> (b) Many other police departments can search the camera data. [correct — Broad-network-access]
> (c) An independent analysis found cameras concentrated in some neighborhoods more than others.
>     [correct — Disparate-impact]
> (d) None of the above were mentioned. [correct — Neutral]

Continuous clarity item (generic wording works across all 4 arms, carried over from the original
design): "How clearly did the description explain what happened with this camera network?" (1-7).

Confound-check items unchanged from the original instrument (should show no significant difference
across arms): ease-of-understanding, source-credibility (Hovland & Weiss 1951, reused from Tariff
Paper's battery), realism ("This reads like something that could really happen...").

## Everything else carried over unchanged from `Study2_Instrument_DRAFT_2026-08-27.md`

Mediator 1 (procedural injustice, Reisig/Bratton/Gertz items), Mediator 2 (institutional trust,
same source), Moderator 2 (crime-solving necessity, Miethe et al. 2025), DV (opposition intention,
van Zomeren et al. 2004) all carry over as-is — only the manipulation (Section 4) and manipulation
checks (Section 5) change. Randomization moves from 2-condition to 4-condition equal-probability
assignment.

## New moderator added this session, not in the original 08-16 design memo

**Baseline trust in police**, measured *before* vignette exposure (so it isn't contaminated by the
manipulation) — direct response to Merola, Lum & Murphy (2018)'s own future-research call: their
Fairfax County sample's unusually high baseline trust (80.79%) likely produced a conservative
estimate of the awareness-to-trust-erosion effect, and they explicitly suggested testing this across
communities with varying baseline trust. Britton's national (vs. single-metro) sampling frame is
well-suited to this. Direction of the moderation is deliberately treated as an open empirical
question (could go either way — a floor effect vs. a confirmation effect) rather than assumed.

## Power analysis (run 2026-09-08, Monte Carlo simulation via numpy/scipy — see
`flock_power_analysis.py` in that session's scratchpad, not yet copied into this project folder)

Three separate tests matter here, with very different power profiles:

1. **Omnibus 4-group main effect on the mediator** (any condition differs): well-powered even at
   modest per-cell N. A medium effect (Cohen's f = .25) hits ~99% power at n=100/cell (400 total);
   even a small effect (f = .15) hits 88% power at n=150/cell (600 total).
2. **Planned contrast, neutral vs. disparate-impact, full mediation chain (H1+H2)**: needs more.
   Using Merola, Lum & Murphy (2018)'s own observed trust-erosion effect (d=.33) as the a-path and
   a moderate mediator-to-DV link (b=.40), n=150/cell (300 in that pairwise contrast) gives ~75%
   power; n=200/cell gets to ~87%. A more conservative effect-size assumption (a=.20, b=.30) needs
   n=300/cell for comparable power — a real range depending on how much the literature-informed
   effect size is trusted.
3. **Moderated first-stage interaction (H3, baseline trust × condition), the hardest to power.**
   Realistic interaction effect sizes in field research are small (β≈.10-.20, per McClelland &
   Judd 1993's general point that interactions are almost always smaller than main effects) — at
   those sizes, even n=300-400/cell only reaches 50-70% power under a plain random sample. This is
   the reason for the oversampling design below.

**Design decision from this session's discussion with Britton: oversample on baseline trust in
police, not political ideology.** Ideology was considered as a cheaper proxy (pre-existing,
filterable panel attribute) but rejected — no literature found validating ideology-as-proxy for a
different construct's power, and it's cleaner to just measure the actual construct directly via a
short custom screener if the panel supports one.

**Method, refined after checking the actual literature (not the naive "screen, keep only the
extremes" version):** Preacher, Rucker, MacCallum & Nicewander (2005, *Psychological Methods*) —
the standard critique of the pure "extreme groups approach" (EGA) — themselves point to
McClelland & Judd (1993, *Psychological Bulletin*) and Pitts (1993) as establishing a better,
related technique specifically for interaction/moderation power: **oversampling** the tails while
still retaining a reasonable share of midrange respondents, then analyzing the moderator as
continuous (not dichotomized into low/high groups) — McClelland & Judd's own finding was that
removing the middle entirely is "unwise" and adding it back "can only increase power." This is
the version to build, not full extreme-groups exclusion.

- **Mechanics:** run a short screener (a brief trust-in-police scale, a few minutes, low cost) to
  a broad initial pool; collect each respondent's platform participant ID via a URL parameter;
  build a follow-up invite list weighted toward low- and high-trust scorers but not excluding the
  middle entirely; invite that list to the full paid Study 2 instrument. Confirmed as a real,
  documented workflow on Prolific specifically (a "custom allowlist" screener keyed to
  participant IDs collected from a prior study) — not yet confirmed whether CloudResearch supports
  an equivalent mechanic; check once the account exists.
- **Reporting caveat for the eventual Results/Methods section:** oversampling inflates R² and
  standardized effect sizes for the moderator test, but does not bias unstandardized regression
  coefficients (assuming linearity) — report the interaction in raw coefficient terms, not just a
  standardized effect size, and disclose the oversampling design explicitly to reviewers.
- **Real risk to manage, not just disclose:** regression to the mean — someone extreme on trust at
  screening may not still be as extreme by the time they take the main study. Run the two waves
  close together in time to limit this, don't let weeks elapse between screener and main field.

## Still open / not decided this session

1. Exact final wording pass + real Flesch-Kincaid check on all 4 conditions before piloting.
2. Whether to test a "lower-income only" (no "minority") wording variant alongside the combined
   version in the pilot, per the recommendation above.
3. CloudResearch vs. Prolific turnaround-time comparison — checked 2026-09-08; no rigorous
   head-to-head found. Cost is roughly at parity per a peer-reviewed comparison (Prolific
   $1.90/high-quality respondent vs. CloudResearch $2.00 — see Peer et al., PMC10013894),
   correcting an earlier, wrong assumption in this conversation that CloudResearch was
   meaningfully cheaper. Turnaround itself remains unverified head-to-head; treat the first actual
   CloudResearch field as the real answer.
4. IRB submission covering the student/convenience-sample pilot and the CloudResearch main
   study — explicitly not started yet; Britton's call to defer (2026-09-08), wants to flesh out
   the CCS Paper next instead.
5. CloudResearch's equivalent (if any) to Prolific's custom-allowlist follow-up-invite mechanic —
   needs checking once Britton has the account.
6. Sync this file and the underlying instrument draft to `research-threads-cloud/` and
   `G:\My Drive\Claude Folder\` per standing dual-save practice — not yet done for this file's
   latest edits (only the pre-power-analysis version was mirrored).
