# 2026-08-30 — Verifying the two 2026-08-29 literature leads: Shjarback (2024) and the 2025 ALPR-expansion evaluation

## What this is

The 2026-08-29 note (`notes/2026-08-29-vignette-mechanical-fixes-and-buildout.md`) found two
adjacent literature leads during its gap-sweep but flagged both as "not verified or added" —
"Shjarback 2024" (on officer perceptions) and "an untitled-in-search-results 2025 *Taylor &
Francis* piece... an outcome evaluation." This session tracks down full citations for both, using
WebSearch plus WebFetch (WebFetch has been intermittently working since 2026-08-27; tested again
tonight and reached SAGE Journals cleanly, though Taylor & Francis and CrimRxiv both returned HTTP
403 bot-blocks, consistent with the pattern already documented for ScienceDirect/IJ/SAGE in prior
sessions), and assesses topical fit against this paper's actual theory chain.

Per the task brief: this is literature-grounding work under the project's standing 2026-08-16
Phase 3/autonomous-buildout exception (`notes/2026-08-16-phase3-theme-review-and-theory-lock.md`),
not a design decision. None of the three items reserved for Britton (archival-moderator
feasibility, single-manipulation vs. factorial, PLS-SEM vs. Hayes-PROCESS) were touched. The
Condition B government-incompetence confound and the vignette reading-level gap were also not
touched — both remain exactly as the 08-29 note left them.

---

## 1. Shjarback (2024) — CONFIRMED REAL, but topical fit fails

### Full citation (direct-fetch verified)

**Shjarback, J. A. (2024).** "Examining Police Officers' Perceptions of Automated License Plate
Readers Before Technology Expansion." *Criminal Justice Policy Review*, 35(1), 3–21.
Published online 2023-12-29. DOI: [10.1177/08874034231220627](https://doi.org/10.1177/08874034231220627).
Sole author.

**Correction to the 08-29 note:** that note attributed this article to *Policing: An
International Journal*. The actual venue is *Criminal Justice Policy Review*. This was caught by
directly fetching the SAGE Journals page for the DOI
(`journals.sagepub.com/doi/10.1177/08874034231220627`), which returned cleanly tonight (no
bot-block on this particular SAGE title, unlike the Nhan & Helfers SAGE page, which has been
403'd every time it's been retried since 08-27) — full title, author, journal, volume/issue,
pages, and abstract all confirmed directly from the publisher, not just WebSearch summaries.

### Abstract (direct-fetch, verbatim from SAGE)

> "Automated license plate readers (ALPRs) are one of the most recent technological advancements
> that have rapidly diffused across U.S. law enforcement. A majority of the large police agencies
> utilize ALPRs, yet little empirical and evaluative research has been conducted on this
> technology. This study seeks to (a) synthesize what is known about ALPRs and (b) examine police
> officers' perceptions of ALPRs before a major expansion of the technology in a single agency in
> the Mid-Atlantic region of the United States. Using an officer survey of 110 respondents,
> results found that those with prior experience using the technology, younger and more
> inexperienced officers, and those with stronger guardian orientations possessed more positive
> perceptions of the ALPR expansion."

### Topical-fit assessment: does NOT clearly fit — not added

The task brief names three candidate fit categories for this literature: ALPR opposition,
officer perceptions of surveillance tech, or outcome evaluations of camera-network expansion.
Shjarback (2024) literally is a study of "officer perceptions of surveillance tech" by title, so
it is not off-topic in the loosest sense — but the paper's actual theory chain is specifically
about **citizens'/the public's** response to ALPR (disclosure → perceived procedural
injustice/contextual-integrity violation → institutional trust → opposition intention, moderated
by prior distributive-surveillance exposure and perceived crime-solving necessity). Shjarback
(2024) surveys **police officers**, not citizens, on **different predictor constructs** (prior
hands-on experience with the technology, age/tenure, "guardian orientation" — a policing-identity
construct with no analog in this paper's model) predicting officers' own receptivity to a coming
technology rollout. It does not measure or discuss disclosure, procedural justice, contextual
integrity, institutional trust, or public opposition in any form.

This matches the 08-29 note's own tentative read ("not obviously a citation this paper needs...
its theoretical territory — officer attitudes toward new technology — doesn't overlap with the
disclosure→injustice→trust chain here"), and a full read of the abstract (not just a search
snippet) confirms rather than complicates that read. **Not added to the draft.** The only
plausible use I can see — citing it briefly as evidence that "existing ALPR perception research
has focused on officers, not the public" to motivate the paper's own citizen-facing contribution
— would be a legitimate literature-review move in the abstract, but is a wording/framing choice
about how the Introduction characterizes the literature gap, not a pure add-a-verified-fact
action, so it's left for Britton or a future explicitly-scoped session rather than done here.

---

## 2. Shjarback & Sarkos (2025) — CONFIRMED REAL, topical fit holds (for a specific, narrow use) — ADDED

### Full citation

**Shjarback, J. A., & Sarkos, J. A. (2025).** "An Evaluation of a Major Expansion in Automated
License Plate Reader (ALPR) Technology." *Justice Evaluation Journal*, 8(2), 225–242 (Smart
Policing special issue). Published online 2025-03-06 (received 2025-01-18, accepted 2025-02-23).
DOI: [10.1080/24751979.2025.2473363](https://doi.org/10.1080/24751979.2025.2473363). Open access.
Co-authors: John A. Shjarback (Rowan University) and James A. Sarkos (Atlantic City Police
Department).

This is the piece the 08-29 note found under the working title "An Evaluation of a Major
Expansion in Automated License Plate Reader (ALPR) Technology" without author names — same lead
author, John Shjarback, as item 1 above (a coincidence worth flagging: he has now published two
distinct ALPR studies, one on officer perceptions in 2024, one on outcome evaluation in 2025;
these are two different papers, not the same study double-counted).

### Verification method and confidence

The Taylor & Francis publisher page itself (`tandfonline.com/doi/full/10.1080/24751979.2025.2473363`
and the `/abs/` version) returned a clean HTTP 403 on direct fetch tonight — the same bot-block
pattern documented for ScienceDirect/IJ/SAGE-Nhan&Helfers in prior sessions, not an egress
failure. A CrimRxiv preprint mirror (`crimrxiv.com/pub/gbu63hj3/release/1`) was also 403-blocked.
**However**, the full author names, journal, volume/issue, and page numbers were independently
corroborated by fetching **John Shjarback's own Rowan University faculty research-profile page**
(`researchwithrowan.com/en/persons/john-shjarback`), which lists this exact work — "Shjarback,
J. A. & Sarkos, J. A., *Justice Evaluation Journal*, 8(2), 225–242 (18 pages), 2025, Open
Access, 3 Scopus citations" — matching the publisher-page bibliographic details found via
WebSearch across three independent listings (Taylor & Francis abstract page, CrimRxiv, and the
faculty profile). This is a step above pure WebSearch-summary confidence (an institutional
author-affiliated source independently lists the identical citation) but short of a direct
publisher full-text pull, since the publisher page itself is bot-blocked — flagging this
distinction per the project's own confidence-tiering convention.

### What the study found (from WebSearch summaries of the abstract/full text, not independently
### fetched full-text — flagged per the project's standard)

A process-and-impact evaluation of a Smart Policing Initiative (SPI) federal grant-funded
expansion of fixed/stationary ALPR cameras at every vehicle entrance/exit to Atlantic City, NJ (a
barrier-island jurisdiction, which limits ingress/egress points and makes a comprehensive
fixed-camera perimeter unusually feasible). Using descriptive statistics, bivariate associations,
and interrupted time-series analysis: ALPR use turned out to be more siloed within specific
investigative units than deployed broadly for patrol functions; the technology expansion was
**not** associated with a reduction in violent crime, but **was** associated with reductions in
shootings, motor vehicle thefts, and property crime.

### Topical-fit assessment: fits the "outcome evaluations of camera-network expansion" category — added, narrowly scoped

This is a genuine, peer-reviewed, real-world outcome evaluation of an ALPR network expansion —
squarely the third category named in the task brief. It does **not** bear on the paper's primary
disclosure→injustice→trust→opposition chain (it measures crime statistics, not public opinion,
disclosure, procedural justice, or institutional trust), so it is not a citation for H1–H5 or the
core mediation model. But it does bear directly on **Moderator 2 (perceived crime-solving
necessity/efficacy, H6)** — that section of the Introduction draws entirely on adjacent
facial-recognition survey literature (Miethe et al. 2025; Bradford et al. 2020) for how *perceived*
efficacy moderates trust-opposition links, without any real-world efficacy evidence about ALPR
itself grounding why that perception might be reasonable or contested. Shjarback & Sarkos (2025)
supplies exactly that: real, mixed, on-topic outcome evidence (works for some crime types, not
others) that materially strengthens — without altering — the moderator's existing framing that
ALPR's public-safety value is "neither straightforwardly proven nor straightforwardly absent."

**Added** to `Introduction_and_Theory_DRAFT_2026-08-16.md`'s Moderator 2 section, as a new
sentence following the existing Michigan/Oakland anecdotal-efficacy examples, plus a
corresponding dated entry (#10) in that draft's "What's still needed" tracking section. No
hypothesis wording, theme, or locked design element was changed — this is an additional citation
supporting existing text, not a rewrite of H6 or the moderator's theoretical logic.

---

## What this session did not do

- Did not touch any of the three reserved design calls (archival-moderator feasibility,
  single-manipulation vs. factorial, PLS-SEM vs. Hayes-PROCESS).
- Did not touch the Condition B government-incompetence confound or the vignette reading-level
  gap (both still open per the 08-27/08-29 notes).
- Did not independently pull the Shjarback & Sarkos (2025) full text — the publisher page and its
  CrimRxiv mirror both remain bot-blocked (HTTP 403). The institutional-profile corroboration
  above is a genuine independent check, but a full-text read (library access, or a future working
  route around the Taylor & Francis block) would still be worth doing before this citation's
  specific quantitative findings (which crime types dropped, by how much) are stated as fact
  rather than "found by" summary in a submitted manuscript.
- Did not add or reword anything characterizing "existing ALPR research focuses on officers, not
  the public" using Shjarback (2024) — flagged above as a plausible framing move, left for
  Britton/a future explicitly-scoped session rather than decided here.
- Did not re-attempt the Nhan & Helfers independence question or the Przeszlowski & Guerette
  ScienceDirect spot-check — both remain exactly as the 08-29 note left them, out of scope for
  tonight's specific task.

## Open items for Britton

1. Everything already open in prior notes remains open (see the 08-29 note's own list).
2. New: Shjarback (2024) is confirmed real but was judged off-topic for this paper's citizen-facing
   theory chain and was not added — flag if a different framing use (motivating the paper's own
   contribution by noting officer-vs-public gap) is wanted instead.
3. New: Shjarback & Sarkos (2025) was added to the Moderator 2 discussion as real-world outcome
   evidence — a narrow, discussion-grounding use, not a core-chain citation. Worth a full-text
   library pull before submission since the publisher page itself couldn't be direct-fetched.
4. New, minor: the 08-29 note misattributed Shjarback (2024) to the wrong journal (*Policing: An
   International Journal* instead of *Criminal Justice Policy Review*) — corrected in this note
   and in the draft's tracking section; worth noting as a reminder that even "found via search"
   leads should get a direct-fetch or independent-source check before a journal name is repeated
   as fact, which is exactly what this session did.
