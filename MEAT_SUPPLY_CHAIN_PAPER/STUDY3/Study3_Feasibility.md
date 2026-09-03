# Study 3 — Feasibility Assessment (Section 12)

Status: feasibility memo, 2026-09-03. Not a design lock. Purpose: assess
whether a third study should be archival/econometric, an event study, or a
consumer survey/SEM — and recommend which, without forcing SEM into the
paper if archival data tell a stronger story (per explicit brief
instruction).

## Option 1 — Time-series / archival (price-spread and concentration data)
**What it would use:** USDA ERS meat price-spread series (farm/wholesale/
retail, by commodity), BLS CPI components, USDA AMS boxed-beef/wholesale
data, concentration measures over time, import volumes (FAS/Census) — most
of which `LITERATURE/Price_Transmission_Literature.md`,
`LITERATURE/Market_Concentration_Evidence.md`, and
`ANALYSIS/Import_Structure_Beef_Pork_Poultry.md` are independently building
right now as part of the evidence base.
**Feasibility:** High — these are public, well-documented, regularly updated
government data series; no new data collection needed, just extraction and
modeling (e.g., correlation/regression of producer-retail spread on import
volume and concentration proxies over time).
**Contribution risk:** This is squarely agricultural-economics/IO territory.
Ag-econ journals have already published extensively on price transmission
and marketing margins (see `LITERATURE/Price_Transmission_Literature.md` once
drafted) — for a *marketing*-journal contribution, this study would need to
be framed as evidence/motivation feeding the marketing-theory story (Study
1/2), not as the paper's central contribution. Best used as a supporting/
robustness study, not the lead study.

## Option 2 — Difference-in-differences / event study
**Candidate events:** 2015 COOL repeal for beef/pork, a 2024+ USDA voluntary
"Product of USA" labeling rule change (pending `NOTES/COOL_Regulatory_
Timeline.md` confirming exact effective date), major packing-plant closures
(e.g., COVID-era plant shutdowns), a DOJ/FTC antitrust action or settlement
against a major processor, COVID-19 disruption itself as a shock.
**Feasibility:** Medium. Needs a clean, dateable policy/event shock and
sufficiently granular price/quantity data around it (weekly or monthly
series ideally). The COOL repeal (2015) is the cleanest natural experiment
candidate — well-documented effective date, directly testable effect on
either price behavior or, more promisingly for a marketing angle, on
consumer perception/survey data collected before/after if any exists in
secondary sources (unlikely to have panel data spanning that exact event,
so this is more useful as a *qualitative* before/after regulatory-context
device for Study 1's discourse corpus than as its own quantitative event
study, unless a specific pre/post price series is unusually clean).
**Contribution risk:** Similar to Option 1 — an event study on prices alone
is an ag-econ contribution. A marketing contribution would need to pair the
event with some measure of *consumer* response (e.g., search-trend data,
sentiment/discourse shift in Study 1's corpus timed around the event) rather
than price data alone.

## Option 3 — Consumer survey / SEM
**Candidate model:** foreign-sourcing/transparency perceptions →
perceived opportunism/fairness/trust → purchase or policy-support outcomes.
**Feasibility:** High in principle (Britton's established PLS-SEM toolkit
and prior chain+moderator theory pattern — see
`Claude_Knowledge/` — transfers directly), but only *after* Study 1 and
`THEORY_CANDIDATES.md` establish which constructs actually belong in the
chain; premature to specify the model now.
**Contribution risk:** Lowest risk of the three for a marketing-journal fit
— this is the most native format for the target journals. But it risks
duplicating Study 2 if Study 2 already does a survey-embedded experiment;
Study 3 as SEM only earns its place as a *separate* study if it captures
something Study 2's manipulated-vignette design can't (e.g., real-world
individual-difference moderators like consumer ethnocentrism or general
institutional trust, measured rather than manipulated, across a broader
population).

## Recommendation (tentative)
Do not lock Study 3 yet — genuinely depends on (a) what Study 1's corpus
actually contains and (b) which theory lens(es) survive
`THEORY_CANDIDATES.md`. Current lean: **Option 1 (archival price/
concentration data) as a supporting/motivating study feeding the paper's
opening empirical-puzzle section**, not a standalone Study 3, combined with
**Option 3 (SEM) as the actual Study 3** once Study 1/2 constructs are
locked — this matches the brief's own caution not to force SEM in if
archival data are stronger, while still giving the paper a native-format
marketing study rather than ending on an ag-econ event study. Option 2
(event study) is the weakest standalone candidate here; its best use is as
contextual grounding for Study 1's corpus time-window decision (see
`STUDY1/Study1_Concept_and_Corpus_Plan.md`), not as its own study.

## Explicit non-decision
This is a lean, not a lock. Britton should decide once Study 1 corpus
findings and `THEORY_CANDIDATES.md` rankings are in hand.
