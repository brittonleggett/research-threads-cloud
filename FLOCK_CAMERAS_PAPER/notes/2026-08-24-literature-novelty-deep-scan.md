# 2026-08-24 — Deeper literature-novelty scan

## What this is

`CLAUDE.md` flags that the 2026-08-16 orientation pass's novelty check was "a quick first pass,
not the deep multi-agent scan Data Center Paper got" and explicitly says "don't treat 'looks
novel' as confirmed until a proper scan is run." This is that scan — not a multi-agent process
(no sub-agent tooling was used), but a substantially deeper single-session pass: roughly a dozen
targeted WebSearch queries across several angles (ALPR-specific experiments, Flock-specific
academic literature, adjacent police-technology survey experiments, adjacent theoretical
combinations), rather than the 1-2 queries the orientation pass ran. WebFetch remains fully
blocked (see `2026-08-24-corpus-verification-and-draft-merge.md`), so everything below is
WebSearch-summary confidence, not full-text-verified — flagged per the project's standard.

## Bottom line

**The novelty claim in the Introduction draft holds up after a real search.** No study was found
that experimentally manipulates disclosure of an ALPR/license-plate-reader network's data-sharing
practice, tests the specific serial-mediation chain (disclosure → perceived procedural injustice
→ institutional trust → opposition intention), or combines procedural-justice and
contextual-integrity theory as this paper's joint theoretical frame. This is a genuine,
searched-for-and-not-found result, not an assumption carried over from the shallow first pass.

That said, the literature is not as empty as the 2026-08-16 orientation pass's single query
suggested — several adjacent works exist that a knowledgeable reviewer would expect this paper to
engage with. Two have been folded into the draft tonight; one more is flagged but not yet added
(citation incomplete).

## What was searched

1. ALPR + procedural justice + contextual integrity + trust, combined
2. "Flock Safety" + survey experiment + public opinion
3. License plate reader + disclosure/secrecy + public trust + experiment/vignette
4. ALPR/license plate reader + "contextual integrity" + Nissenbaum specifically
5. Flock Safety + academic journal + 2026 (general sweep for any new Flock-specific scholarship)
6. Surveillance technology + disclosure + procedural justice + institutional trust + opposition
   intention + mediation/experiment (the paper's exact causal-chain vocabulary)
7. Follow-up deep dives on the two most promising hits from #6 (the RTCC vignette experiment and
   the Miethe/Lieberman video-surveillance dataset)
8. Follow-up deep dive on the Schiff et al. PAR paper surfaced in #5/#6
9. Follow-up deep dives on the two Monahan 2026 papers surfaced in #5
10. ALPR + disclosure/transparency + experiment + public support/opposition, 2025-2026 specifically

## Closest things found, and why none of them anticipates this paper's design

### 1. Nhan & Helfers (2026), *The Police Journal* — already known and cited (nothing new here;
confirms it's still the closest single prior work). Interview-based, not experimental.

### 2. Monahan (2026a), "Grounding the Flock: Confronting Police Surveillance of Mobilities,"
*Mobile Media & Communication* — **new find tonight, not in any prior session's notes.** Published
online May 2026, open access. Critical-surveillance-studies analysis of Flock's network
architecture as a "communicative network" that exposes people to discriminatory,
cross-jurisdictional policing, extending to reproductive-healthcare and immigration surveillance.
Qualitative/theoretical, not an experiment, no trust or procedural-justice constructs measured.
**Added to the Introduction draft's literature paragraph tonight** (full citation verified via
publisher/SAGE Journals listing, DOI 10.1177/20501579261453519).

### 3. Monahan (2026b), "Flock on campus: university police as appendages of a national policing
apparatus," *Policing and Society* — **new find tonight, not in any prior session's notes.**
Published online July 20, 2026. Document analysis built on open-records requests to public
universities/colleges using Flock, arguing campus police become nodes in a national policing
network. Qualitative/document-analytic, not an experiment. **Added to the Introduction draft's
literature paragraph tonight** (full citation verified via Taylor & Francis listing, DOI
10.1080/10439463.2026.2702635).

Both Monahan pieces are recent enough (May/July 2026) that they plausibly postdate, or were
simply missed by, the 2026-08-16 orientation pass's single-query novelty check — this is a real
example of why a deeper pass was worth running, not just a formality.

### 4. Schiff, Schiff, Adams, McCrain, & Mourtgos (2025), "Institutional factors driving citizen
perceptions of AI in government: Evidence from a survey experiment on policing," *Public
Administration Review*, 85(2), 451-467 — **new find tonight.** Pre-registered survey experiment,
*n* = 4,200, manipulating bureaucratic proximity (local sheriff vs. national FBI), algorithmic
target (predictive policing vs. misconduct review), and agency capacity, in the context of AI use
in policing generally (not ALPR/Flock specifically). Found citizens respond most strongly to the
local-vs-national institutional distinction; limited/politicized response to algorithmic target;
no response to agency capacity. **Does not test a disclosure manipulation, does not measure
procedural injustice or institutional trust as mediators, does not test an opposition-intention
DV** — it's a genuine methodological cousin (survey experiment on public perception of a policing
technology, published in a leading candidate venue for this paper) but not a competitor. **Added
to the draft's theory section tonight**, both as a citable precedent for the general method and
because its local-vs-national manipulation structurally echoes this paper's own
local-police-vs-federal-agency distinction running through the corpus. Full citation confirmed
across multiple listings (Wiley Online Library, CrimRxiv preprint, OSF preregistration, a co-author's
own faculty publication page) — high confidence this citation is accurate.

### 5. Unnamed authors, "Public perceptions on police use of information technologies: Findings
from a randomized vignette experiment," *Journal of Criminal Justice*, Vol. 96 (2024/2025), Article
102332 — **new find tonight, flagged but NOT added to the draft.** Randomized vignette experiment,
*n* = 345, on public perceptions of police technologies housed in Real-Time Crime Centers (RTCCs),
manipulating "informational stimuli" (framed as transparency/legitimacy/effectiveness dimensions)
and finding transparent, neutral messaging increases public approval. This is, structurally, the
single closest prior work found in this entire scan — a vignette experiment manipulating
transparency-adjacent framing of a police technology and measuring approval — but (a) it studies
RTCCs, not ALPR/Flock specifically, (b) based on available search summaries it does not appear to
model procedural injustice and institutional trust as a serial-mediation chain the way this paper
does, and (c) **the full author list could not be confirmed via WebSearch** — result summaries
consistently omit it, and the ScienceDirect page itself is behind the same WebFetch block as
everything else tonight. **Do not cite this by title/journal/volume alone without the author
names** — that's an incomplete citation, not a verified one. Recommend a library-access or
working-WebFetch pull of `sciencedirect.com/science/article/abs/pii/S0047235224001855` as a
concrete, well-defined next step; if the design turns out to be as close as it looks, this paper
should engage with it directly (as a "closest prior work, and here's how this paper's chain still
differs" paragraph), not just add it to a reference list.

### 6. Miethe & Lieberman (PIs), "Perceptions of Trust and Procedural Justice as Sources of
Receptivity and Resistance to Video Surveillance," ICPSR dataset (study 37341), fielded 2017-2018
— national U.S. survey (n = 3,000+) plus a Las Vegas-metro survey (n = 2,000+) on public
support/opposition to video-surveillance technologies (drones, body-worn cameras — not ALPR),
using trust and procedural justice as predictors. **Correlational survey, not an experiment.**
Notable because Terance Miethe is already a cited author in this draft (Miethe, Dudinskaya,
Forepaugh, & Sousa, 2025, the crime-solving-necessity scale source) — this is earlier work from
the same research program, on a related but distinct set of technologies, using a
non-experimental design. Judged not worth adding as a separate citation tonight: the newer,
already-cited Miethe et al. (2025) study is the more specific and more recent precedent from the
same lab, and this dataset doesn't add a claim the draft needs that Miethe et al. (2025) doesn't
already support. Noted here for completeness, not added to the manuscript.

### 7. Industry/polling sources (not academic, checked for completeness) — a Hanwha Vision America
consumer survey (April 2026, *n* = 1,000) found ~74% of Americans want public quarterly reporting
on ALPR use, and a YouGov daily-question poll tracks general support/oppose sentiment on ALPR.
Both are real, findable, descriptive polling, not peer-reviewed academic work and not experiments
— useful as color for a "the public wants transparency" framing claim if Britton wants it, but not
literature-review material and not added to the draft.

## What this scan did not do

- Did not attempt a systematic database search (Web of Science, Scopus, PsycINFO) — WebSearch via
  a general search engine only, same limitation as every prior literature pass in this project.
- Did not use multiple parallel sub-agents the way Data Center Paper's original deep scan did —
  this was one session running sequential targeted queries, a real improvement over the 2026-08-16
  single-query pass but not identical in method to that scan.
- Did not verify any of these new citations via direct fetch — all WebSearch-summary confidence,
  same caveat as everything else in this project's literature-verification notes.

## Recommendation

Treat tonight's result as good evidence, not final proof, that the paper's core empirical
contribution is novel. The two Monahan citations and the Schiff et al. citation are safe,
verified, non-design-altering additions and are already merged into the draft. The
*Journal of Criminal Justice* RTCC vignette experiment is the one loose end worth a deliberate
follow-up — it's the closest analog found in two literature passes now, and citing it properly
(with real author names) would meaningfully strengthen the "here's exactly how this paper differs
from the closest prior work" framing a reviewer will look for.
