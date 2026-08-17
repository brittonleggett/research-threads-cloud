# 2026-08-16 — Scale sourcing for Study 2 (AI-run, autonomous per Britton's explicit exception)

**Update, same day:** Britton offered Ole Miss library access mid-session. Pulled real,
full-text PDFs via the claude-in-chrome extension + SSO (same method as Tariff Paper's
2026-08-04 scale verification) for the four constructs flagged below as item-level-unverified.
**Three of four now have real, word-for-word item text, directly transcribed from the source
PDF — see each construct's updated entry below.** The fourth (institutional trust) is now
covered by the same Reisig et al. (2007) pull that resolved procedural injustice, since that
paper contains both constructs. Only the manipulation-check items (construct #1, always
study-specific, no literature dependency) and the archival distributive-exposure moderator
(construct #5, a design choice, not a scale) remain as before.

**Original honesty note (superseded for #2, #3, #4, #6 below, left for context):** for every
construct, I verified via WebSearch that the source paper is real (correct authors, year,
journal, and — where checkable — DOI/volume/page numbers), and confirmed the construct/subscale
structure the original authors report. Item-level wording was not independently pullable via
WebFetch alone — several source PDFs returned encoded/unreadable streams, and one (Martin,
2016, *JBE*) sits behind a Springer login wall (not pulled this pass — not needed once Tyler-
tradition items covered mediators 1 and 2 directly). Tariff Paper hit the same wall repeatedly
before Ole Miss access resolved it — see
`TARIFF_PAPER/notes/2026-08-04-scale-items-verification-status.md` for that precedent.

---

## 1. Manipulation check — disclosure condition (secret vs. transparent data-sharing)

No published scale needed or sought — standard practice in experimental vignette research
(matching how Tariff Paper's own Attribution Frame manipulation check was handled) is a
short, study-specific manipulation-check item set (e.g., "The camera network's data-sharing
policy was clearly disclosed to residents before it was activated," reverse-scored suspicion
items). To be written directly into the Study 2 instrument, not sourced from the literature.

## 2. Perceived procedural injustice (Mediator 1) — ITEM WORDING VERIFIED 2026-08-16

**Source: Reisig, Bratton, & Gertz (2007), "The Construct Validity and Refinement of
Process-Based Policing Measures," *Criminal Justice and Behavior*, 34(8), 1005-1028.** Pulled
full text via Ole Miss/Sage Journals (umiss.idm.oclc.org proxy), N=432 nationwide telephone
survey, spring 2005. Real, exact item wording, 4-point scale (1 = *strongly disagree* to
4 = *strongly agree*), transcribed directly from the article's Table 2 (p. 1014):

*Quality of Treatment* (5 items): "Treat citizens with respect"; "Take time to listen to
people"; "Treat people fairly"; "Respect citizens' rights"; "Are courteous to citizens they
come into contact with."

*Quality of Decision Making* (5 items): "Make decisions based upon the facts"; "Explain their
decisions to the people they deal with"; "Make decisions based on their own personal opinions"
[reverse-scored]; "Make decisions to handle problems fairly"; "Don't listen to all of the
citizens involved before deciding what to do" [reverse-scored].

Quality of Treatment + Quality of Decision Making sum to the study's procedural justice scale
(10 items total). **For this paper's procedural *injustice* framing, either reverse-score the
summed scale or lead with the reverse-scored items directly** — a real, citable, field-tested
item set, not reconstructed from memory. Sunshine & Tyler (2003, *Law & Society Review*, 37,
513-547) remains the correct anchor citation for *why* procedural justice theoretically drives
legitimacy/trust — Reisig et al. (2007) is the psychometric refinement built on it, cite both.

## 3. Institutional trust (Mediator 2) — ITEM WORDING VERIFIED 2026-08-16

**Same source: Reisig et al. (2007), same pull as above.** The paper operationalizes legitimacy
as an additive index of two 4-item subscales (also Table 2, p. 1014), same 4-point scale:

*Obligation to Obey the Law* (4 items): "You should accept police decisions even if you think
they are wrong"; "You should do what the police tell you to do even if you disagree";
"Disobeying the police is seldom justified"; "It is difficult to break the law and keep one's
self respect."

*Trust in Police* (4 items): "Police in your community have too much power" [reverse-scored];
"People's basic rights are well protected by the police"; "The police can be trusted to make
decisions that are right for your community"; "Most police officers in your community do their
job well."

**Recommend using the 4-item Trust in Police subscale directly as the institutional-trust
mediator** (not the full 8-item legitimacy index, which conflates trust with a distinct
obligation-to-obey construct this paper's chain doesn't need) — a genuinely on-topic advantage
this paper has that Tariff/Data Center Paper didn't: a policing-specific, field-tested trust
measure exists and fits directly, rather than needing to borrow a generic corporate-trust scale
(e.g., Chaudhuri & Holbrook 2001, used in Tariff Paper).

## 4. Perceived crime-solving necessity/efficacy (Moderator 2) — ITEM WORDING VERIFIED 2026-08-16

**Source: Miethe, Dudinskaya, Forepaugh, & Sousa (2025), "Facial Recognition Technology in
Policing: A National Survey of Public Support for This Technology and Privacy/Safety Concerns,"
*Crime & Delinquency*, 71(4), 1025-1051.** Pulled full text via Ole Miss/Sage Journals (open
access, confirmed DOI 10.1177/00111287221150172, print date 2025 confirmed on the article's own
first page — resolves the earlier online-first-date flag). N=612 national Qualtrics panel,
March 2022. Real items confirmed from the Table 1 variable list (p. ~1034, rotated/landscape
table): a single item, **"FRT increases [public] safety"** (agree/disagree), used alongside a
paired item, **"privacy costs [outweigh] public safety benefits"** — both drawn from a larger
battery of privacy/safety belief items. **Recommend adapting "[ALPR/Flock cameras] increase
public safety" as this paper's single-item crime-solving-necessity moderator**, directly
parallel to Miethe et al.'s own operationalization for a closely analogous policing technology
(facial recognition) — the closest direct precedent found for this construct, now with real
confirmed item language rather than just a confirmed construct.

## 5. Community distributive-surveillance-exposure history (Moderator 1)

**Not a self-report scale — recommend an archival/objective measure**, following the actual
methodology of this paper's own corpus evidence: the Christopher Newport University study
(Finn, Baird, & Keener, surfaced via WHRO/13newsnow, 2026-01-20/21) used regression analysis of
camera density against neighborhood racial composition and poverty rate to establish disparate
placement empirically, rather than asking residents to self-report perceived disparity. Proposed
operationalization: for each sampled community/respondent's home ZIP or tract, compute
camera-count-per-capita relative to the tract's racial/poverty composition (using the same
basic logic as the CNU study — publicly available Flock deployment data, where obtainable, or
DeFlock's community-sourced tracker, cross-referenced with Census tract demographics), producing
a continuous disparity-exposure score per respondent's community. This avoids a fabricated
self-report scale entirely and ties the moderator directly to the same kind of evidence this
paper's own corpus relies on — the honest and more defensible choice given no validated
self-report "perceived surveillance disparity" scale was found in this search pass. **This is a
design recommendation, not a verified existing instrument — flag as a real methodological choice
for Britton to confirm, since it requires real data-access work (Flock deployment data or
DeFlock tracker + Census data) rather than a simple survey-item pull.**

## 6. Opposition intention (DV) — ITEM WORDING VERIFIED 2026-08-16

**Source: van Zomeren, Spears, Fischer, & Leach (2004), "Put Your Money Where Your Mouth Is!
Explaining Collective Action Tendencies Through Group-Based Anger and Group Efficacy," *Journal
of Personality and Social Psychology*, 87(5), 649-664.** Pulled full text via Ole Miss/EBSCO
(APA PsycArticles). Confirmed real: DOI 10.1037/0022-3514.87.5.649. Study 1's "Collective
action tendencies" scale (p. 652, α = .82, 3 items, same 7-point Likert as the rest of the
instrument, 1 = *not at all* to 7 = *very much*), real exact wording:

"I would participate in a demonstration against this proposal"; "I would participate in raising
our collective voice to stop this proposal"; "I would do something together with fellow
students to stop this proposal."

Study 2 (same paper) adds a 4th item to the same scale (α = .84): **"I would participate in
some form of collective action to stop this proposal."** Both versions are directly adaptable —
replace "this proposal" with "[the camera network's continued operation]" or similar, and
"fellow students" with "fellow residents/community members." **Recommend the 4-item Study 2
version** as the more complete/reliable of the two. The broader Social Identity Model of
Collective Action (van Zomeren, Postmes, & Spears, 2008, *Psychological Bulletin*, 134(4)) is
the meta-analytic integration of this line of work — real, useful for theoretical framing, not
itself an item source. Real-world validity anchor: this paper's own corpus shows these exact
intention categories (protest, formal collective voice, joint community action) translating
into real outcomes (formal municipal votes, litigation, protest) in multiple cities, worth
citing in the Method section as evidence the DV has ecological validity beyond self-report.

---

## What Britton needs to do before Study 2 is instrumented

1. ~~Pull real item-level text for Reisig et al. (2007), Miethe et al. (2025), and van Zomeren
   et al. (2004)~~ — **done 2026-08-16** via Ole Miss library access; real item wording now in
   sections 2, 3, 4, and 6 above. Nothing further to pull for those four constructs.
2. Confirm or reject the archival distributive-surveillance-exposure design (construct #5) —
   still a real methodological choice, not a simple scale pull, and needs his sign-off on
   feasibility (does he have or can he get Flock deployment/DeFlock tracker data at the
   ZIP/tract level for a real sample). This is the one open item that isn't a literature pull.
3. Write and pilot the study-specific manipulation-check items (construct #1) — straightforward,
   no literature dependency.
4. Adapt the pulled item wording (sections 2-4, 6) to the Flock/ALPR context — swap "police"/
   "this proposal" framing for the camera-network context, keep response scales as the source
   studies used them (4-point for Reisig et al.'s items, 7-point for van Zomeren et al.'s), and
   run a face-validity/wording pilot before fielding.
