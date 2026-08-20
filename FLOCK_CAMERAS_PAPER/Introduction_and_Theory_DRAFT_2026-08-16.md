# ALPR Camera Networks and Public Trust — Introduction & Theoretical Development (DRAFT)

**Status note (delete before submission):** AI-drafted, 2026-08-16, under Britton's explicit
one-time exception letting AI complete Phase 3 (theme review) and draft through Theory —
see `notes/2026-08-16-phase3-theme-review-and-theory-lock.md` for the disclosure and reasoning
behind every judgment call made without his prior sign-off. This is real academic prose
grounded in the verified 22-artifact corpus and real, checked literature citations (see
citation-verification notes inline and in `notes/2026-08-16-scale-sourcing.md`), but it is
**pending Britton's read-through** — nothing here should be treated as final until he's seen
it. No Results section — Study 2 has not run.

---

## Introduction

In May 2026, Menominee, Michigan's city council learned that Flock Safety automated
license-plate-reader (ALPR) cameras had already been activated in their community — before the
council had voted to approve them. The council's response was unanimous and unambiguous: an
8-0 vote against adoption, and the contract was canceled. Menominee is not an outlier. In Bend,
Oregon, police discovered only after the fact that "National Lookup," a setting enabled by
default on Flock's platform, was a reciprocal data-sharing feature that let federal immigration
and customs agencies query the department's plate-read data — Captain Beekman's own words to
the city council were blunt: "What we didn't know is that National Lookup is a reciprocal
sharing feature." In Illinois, a state audit found that even Flock's own leadership was unaware
its Customs and Border Protection pilot program was running in a local department at all. Across
at least fourteen states in 2026 alone, city councils, courts, and state regulators have
confronted a common pattern: a surveillance technology adopted for one stated purpose — solving
property crime — whose actual data-sharing architecture was not disclosed to, or understood by,
the communities and even the police departments deploying it.

This is not a story about whether ALPR technology works. Flock itself credits its camera
network with contributing to 800,000 to 1 million solved crimes per year, including a rapid
response to a campus shooting at Brown University and the recovery of more than 2,000 missing
persons — claims that mainstream press coverage treats as credible alongside the privacy
critique, not as one-sided industry spin (PBS NewsHour, 2026). Nor is it only a story about
disparate impact, though that pattern is real and well-documented: a Christopher Newport
University analysis of Hampton Roads, Virginia found Black neighborhoods surveilled at
approximately four times the rate of white ones, and a federal lawsuit brought by the Institute
for Justice centers on the discovery that Norfolk State University — the only historically
Black college or university in the region — is ringed by seventeen ALPR cameras, compared to
roughly five near Old Dominion University and two near Christopher Newport. It is, at its core,
a story about **disclosure**: whether the public and the institutions that serve them know, at
the point of adoption, what a surveillance system will actually do with their data — and what
happens to public trust and political opposition when they find out they did not.

This paper addresses that question empirically in two studies. Study 1 inductively derives a
typology of real ALPR controversies from a 22-artifact corpus spanning fourteen states and one
national-level pattern, identifying institutional secrecy around default data-sharing practices
— not corporate non-disclosure agreements, but a *technical* default nobody flagged at the
point of adoption — as the mechanism with the broadest evidentiary support and the clearest
manipulable structure for experimental study. Study 2 experimentally manipulates disclosure of
a camera network's data-sharing practice (transparent, local-only vs. secret, broad-access) and
traces its downstream consequences through perceived procedural injustice and institutional
trust to opposition intention, testing two theoretically motivated moderators: a community's
prior exposure to disparate surveillance placement, and the public's perceived necessity of the
technology for public safety.

The contribution is threefold. First, we extend procedural justice and police legitimacy theory
(Tyler, 1990; Sunshine & Tyler, 2003) — developed principally to explain compliance and
cooperation in direct police-citizen encounters — to a domain that theory has not yet been
tested against: ambient, largely invisible surveillance infrastructure, where the "encounter"
citizens are judging is not a traffic stop but a disclosure about how their movements are being
recorded and shared. Second, we integrate this policing-legitimacy tradition with Nissenbaum's
(2010) theory of privacy as contextual integrity, treating the ALPR secrecy pattern not as a
generic privacy violation but as a specific violation of the informational norms under which
data was originally volunteered — plate data given to solve local property crime, flowing
instead to federal immigration enforcement or other out-of-jurisdiction agencies without the
public's knowledge. Third, this paper is, to our knowledge, the first study to move beyond
qualitative and interview-based treatments of ALPR controversy — most directly, Nhan and
Helfers's (2026) interview study with Flock Safety representatives, law-enforcement users, and
policymakers — to a design that inductively derives its theoretical mechanism from a large,
geographically diverse corpus of real public controversies and then tests that mechanism's
causal structure experimentally. Where Nhan and Helfers document practitioner and vendor
perspectives on the security-privacy tradeoff, this paper centers the public's own reaction and
tests whether disclosure, not just accuracy or capability, is what determines whether that
tradeoff is judged legitimate. It is also worth noting plainly, in the interest of an even-handed
comparison, that Nhan and Helfers's study was conducted under a research grant from Flock Safety
itself (with contractually stipulated researcher independence on topic, methodology, and
findings) and relied on Flock as a gatekeeper for agency access; the present study uses no
vendor funding or vendor-facilitated access, drawing instead on public news coverage, court
filings, and government records.

## Theoretical Background and Hypothesis Development

### Procedural Justice, Contextual Integrity, and the Secrecy Mechanism

Procedural justice theory in policing holds that public evaluations of police and policing
institutions are shaped less by outcomes than by the perceived fairness of the process —
whether citizens are treated with respect, given voice, and dealt with in a neutral, transparent
manner (Tyler, 1990; Sunshine & Tyler, 2003). A large empirical literature has since shown that
procedural justice judgments are a stronger predictor of institutional trust and legitimacy than
either police effectiveness or the citizen's own self-interest (Tyler & Huo, 2002; Reisig,
Bratton, & Gertz, 2007). That literature has been built almost entirely around direct,
person-to-person encounters — traffic stops, arrests, service calls. ALPR surveillance
represents a structurally different kind of encounter: ambient, continuous, and — per this
paper's corpus — frequently undisclosed even to the local officials nominally overseeing it.

Nissenbaum's (2010) theory of contextual integrity supplies the missing piece: privacy is not
violated by data collection per se, but by data flows that breach the norms of the context in
which the data was originally shared. A community that accepts ALPR cameras to solve local
property crime has, in effect, consented to a specific informational norm — plate data flows to
local police, for local crime-solving purposes. When that same data instead flows to federal
immigration enforcement (Evanston, Bend, Syracuse), or is queried hundreds of thousands of times
by outside agencies without a warrant (San Jose: 261,711 warrantless searches by the city's own
police department alone, per the ACLU/EFF lawsuit filed on behalf of SIREN and CAIR-CA), the
violation is not merely that data was collected — it is that data moved outside the context the
public understood it to be confined to. We treat undisclosed default data-sharing as a
contextual-integrity violation that should be perceived as a specific, procedural form of
injustice, distinct from a generic privacy-concern measure.

This paper's proposed institutional-trust mechanism (H2 below) is not a theoretical reach into
an unstudied domain. Li (2024), drawing on a 2021 nationally representative U.S. survey
(*n* = 4,679), found that institutional trustworthiness — specifically the integrity dimension —
was the strongest and most consistent predictor of public acceptability of a closely analogous
policing technology (facial recognition), with the effect largest in the highest-privacy-concern
scenario tested (public protests). That study, notably, was published in *Government Information
Quarterly* — this paper's own leading target venue — which is both a direct empirical precedent
for the trust-mediated structure proposed here and a signal that this journal's editorial
community already treats institutional-trustworthiness-in-policing-technology as squarely
in-scope. Bradford, Yesberg, Jackson, and Dawson (2020) reach a structurally identical
conclusion via a different method (a UK live-facial-recognition field survey), finding trust and
legitimacy — not perceived effectiveness — predicted public support. Both studies measure
trustworthiness/legitimacy as an antecedent to acceptance broadly rather than testing an
experimentally manipulated disclosure condition specifically, which is this paper's point of
departure from both:

> **H1.** A camera network operating under a secret, undisclosed default data-sharing practice
> will produce higher perceived procedural injustice than one operating under an explicitly
> disclosed, local-only policy.

### From Procedural Injustice to Institutional Trust

Consistent with the process-based model of policing (Tyler & Huo, 2002; Reisig et al., 2007;
Reisig & Lloyd, 2009), we predict that perceived procedural injustice translates into reduced
trust in the institutions responsible for the technology — the local police department and, by
extension, local government. This paper's corpus offers a direct illustration: Illinois
Secretary of State Alexi Giannoulias's own audit finding that Flock had shared data with Customs
and Border Protection in violation of state law prompted Flock to pause its CBP pilot program
nationwide — an institutional response that itself signals the reputational stakes of a
disclosed procedural failure.

> **H2.** Perceived procedural injustice will be negatively associated with institutional trust
> (in local police and local government).

### From Institutional Trust to Opposition Intention

Reduced institutional trust is expected, in turn, to predict opposition intention — a
composite of support for camera removal, willingness to contact officials or attend a public
meeting, and broader protest/political-engagement intention (see Study 2 design memo for
operationalization, grounded in the collective-action literature: van Zomeren, Spears, Fischer,
& Leach, 2004). The corpus's own municipal-rejection wave — Ord, Nebraska's unanimous 5-0
removal vote; Denver's unanimous non-renewal and physical removal of 110 cameras; Menominee's
8-0 rejection — is real-world validity evidence that opposition intention, once mobilized,
frequently translates into formal institutional outcomes at the local level, distinct from this
paper's data center-controversy sibling study, where formal opposition more often failed against
state-level utility regulators. This asymmetry — local, directly accountable bodies proving more
responsive than state-level or vendor-controlled ones — is not tested directly in Study 2, but
motivates treating opposition intention as ecologically meaningful rather than a purely
attitudinal outcome.

> **H3.** Institutional trust will be negatively associated with opposition intention.
> **H4 (serial mediation).** The effect of data-sharing disclosure condition on opposition
> intention will be serially mediated by perceived procedural injustice and institutional trust.

### Moderator 1: Prior Distributive-Surveillance Exposure (First-Stage Moderation)

Not every community encounters a secrecy revelation from the same starting point. The corpus's
Norfolk State University case is theoretically instructive precisely because it combines two of
this paper's themes in a single artifact: a documented disparity in camera placement (17 cameras
around the region's only HBCU, versus roughly 5 near Old Dominion and 2 near Christopher
Newport) *and* a federal lawsuit centered on undisclosed surveillance practice. We propose that
a community's prior exposure to disparate, unequal surveillance placement sensitizes its
interpretation of a new disclosure failure — the same secrecy revelation should land as a more
severe injustice in a community that already suspects, or has evidence, that it is
disproportionately watched. This is modeled as a **first-stage moderator**, operating on the
disclosure-condition → procedural-injustice path, because the theoretical mechanism is
interpretive: prior exposure changes how the same objective information (a secret data-sharing
default) is *appraised*, not how injustice subsequently affects trust or opposition.

> **H5.** Community distributive-surveillance-exposure history (operationalized archivally, see
> Study 2 design memo) will moderate the effect of disclosure condition on perceived procedural
> injustice, such that the effect is stronger in communities with higher pre-existing camera-
> placement disparity.

### Moderator 2: Perceived Crime-Solving Necessity (Last-Stage Moderation)

The corpus also contains a genuine, mainstream-covered counter-current: real, named police
officials crediting Flock cameras with solving specific violent crimes (a murder and a
double-murder in Ferndale and Hazel Park, Michigan; a carjacking response in Oakland County),
and Flock's own aggregate claims running alongside the privacy critique in the same PBS
NewsHour segment rather than being presented as a rebutted talking point. This mirrors a
documented pattern in the adjacent facial-recognition-in-policing literature: perceived
public-safety effectiveness and privacy concern are both independent, simultaneous predictors
of technology support, and their relative weight shifts by context (Miethe, Dudinskaya,
Forepaugh, & Sousa, 2025). Bradford, Yesberg, Jackson, and Dawson (2020), studying public
reaction to live facial recognition deployment in the UK, found a structurally identical
pattern directly relevant to this moderator: trust and, especially, perceived police
legitimacy *alleviated* respondents' privacy concerns about the technology — legitimacy did
not just coexist alongside privacy concern but actively softened it. That finding is close to
a direct precedent for H6 below, not merely an adjacent one. We treat perceived crime-solving necessity as a value-tradeoff
variable that should buffer, not eliminate, the consequences of low institutional trust — even
a resident who distrusts the department's handling of camera data may not translate that
distrust into active opposition if they believe the technology is genuinely necessary for
public safety. This is modeled as a **last-stage moderator**, operating on the
trust → opposition-intention path, because the mechanism is a value tradeoff made at the point
of behavioral intention, not an interpretive filter on the injustice appraisal itself.

> **H6.** Perceived crime-solving necessity/efficacy will moderate the relationship between
> institutional trust and opposition intention, such that the negative effect of low trust on
> opposition intention is attenuated among respondents who perceive high crime-solving
> necessity.

### A Note on Themes Not Built Into the Primary Model

Study 1's corpus surfaced two further real, well-evidenced patterns not incorporated into the
hypotheses above, reported here for completeness rather than omitted silently. First, a
function-creep pattern — the network sold as a stolen-vehicle tool but used for
reproductive-healthcare surveillance or personal stalking — is real but rests on only two,
thinly sourced corpus artifacts (see `Study1_Corpus_and_Coding_DRAFT_2026-08-16.md`, #5 and
#19) and is treated as a discussion-section direction for future work rather than a hypothesis
in this design. Second, algorithmic accuracy and wrongful-stop harms (a Toledo, Ohio K9 mauling
following a single-digit plate misread; a Los Angeles Police Department audit finding a 32.3%
false-positive rate on stolen-vehicle flags) constitute a distinct causal story — dread risk
(Slovic) operating largely independent of the disclosure/trust chain modeled here — and are
flagged as a strong candidate for a follow-up study or robustness check rather than force-fit
into the present design.

---

## What's still needed before this is submission-ready

1. Britton's read-through — every theoretical and hypothesis-wording choice here was made
   without his prior input, per his explicit 2026-08-16 instruction; flag anything that doesn't
   match his own read of the corpus or theory.
2. ~~Scale item-level wording is not yet verified against original sources~~ — **resolved
   2026-08-16 through 2026-08-20.** Item-level wording for all four literature-sourced
   constructs (procedural injustice and institutional trust, Reisig, Bratton, & Gertz 2007;
   crime-solving necessity, Miethe, Dudinskaya, Forepaugh, & Sousa 2025; opposition intention,
   van Zomeren, Spears, Fischer, & Leach 2004) was pulled directly from source PDFs via Ole Miss
   library access (`notes/2026-08-16-scale-sourcing.md`), adapted to the ALPR/camera-network
   context (`notes/2026-08-19-instrument-adaptation-and-manipulation-checks.md`), and given a
   face-validity desk review that revised three items for construct-contamination and
   double-barreling risk (`notes/2026-08-20-face-validity-review-scale-items.md`). Still
   outstanding: an actual pilot test with respondents (not yet run — desk review isn't a
   substitute), and the archival distributive-surveillance-exposure moderator (Britton's
   feasibility call, unresolved).
3. No Results section exists and shouldn't until Study 2 actually runs.
4. The two "not built into the primary model" themes (function creep, algorithmic accuracy) are
   real findings worth Britton's own read — he may want either promoted into the design rather
   than held for a discussion section or follow-up study.
