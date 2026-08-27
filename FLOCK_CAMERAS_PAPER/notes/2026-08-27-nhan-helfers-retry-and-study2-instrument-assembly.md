# 2026-08-27 — Nhan & Helfers retry (fresh angles), full Study 2 instrument assembly

## What this is

Continues the autonomous build-out under the project's standing 2026-08-16 Phase 3 exception. Two
things happened tonight: (1) another attempt at the still-unresolved Nhan & Helfers researcher-
independence claim, using search angles not tried in the 08-21/08-22/08-24 passes, and (2) —
the higher-value item, since the independence question is now a genuinely primary-source-gated
dead end for search alone — assembling the first full, platform-ready Study 2 instrument document,
closing an explicit gap flagged in the 08-21 IRB draft ("full survey instrument assembly...
combining consent, screener, vignette, manipulation checks, scales, demographics, and debriefing
into an actual platform-ready survey flow document. Not started.").

No locked theme, hypothesis, or design element was touched. No new design decision was made on
either item still explicitly reserved for Britton (archival-moderator feasibility, single-
manipulation vs. factorial, PLS-SEM vs. Hayes-PROCESS) — the instrument document is written to
stay usable regardless of how those resolve.

## WebFetch status: still blocked (17th+ consecutive session)

Tested against two targets tonight: `en.wikipedia.org` (control) and `journals.sagepub.com` (the
Nhan & Helfers article's own publisher page, direct target). Both failed `EGRESS_BLOCKED`,
identical to every prior session. Also tried a new target not attempted in prior Flock sessions —
`sage.cnpereading.com`, a SAGE-affiliated reading-platform mirror that WebSearch surfaced tonight
as hosting the same article — also `EGRESS_BLOCKED`. This is consistent with the repo-wide
15th-17th-session assessment already recorded in `OVERNIGHT_SUMMARY_2026-08-25.md`: an
environment-level proxy/egress issue, not anything domain- or paper-specific. No further value in
retesting this nightly without a platform-side change; noting it briefly per the task brief rather
than re-litigating the diagnosis.

## Nhan & Helfers independence claim: fresh angles tried, still unresolved

Five new WebSearch queries tonight, deliberately different from the eight run 08-22 and the two
run 08-24 (institutional grant-announcement angle, explicit conflict-of-interest phrasing, a
stopflocksafety.org-targeted funding query, a direct quote-hunt for reported "brought in late"
language):

1. University-press-release angle: "Helfers Nhan Flock Safety grant [University of Louisville /
   Wichita State] research agreement 2025" — no results tying either author's home institution to
   a Flock grant announcement.
2. Direct conflict-of-interest phrasing: "Police Journal Nhan Helfers Flock Safety 2026 declare
   conflict of interest funding" — **found the article's actual title and DOI for the first time**
   (see below), but no disclosure-statement text.
3. SAGE-mirror WebFetch attempt (`sage.cnpereading.com`) — blocked, see above.
4. Quote-hunt: "'brought in' OR 'brought into' study late Flock quote" — one search-result summary
   mentioned Nhan discussing being "brought into a study late in the process" and future work with
   Flock, but the underlying source for that specific claim did not surface in the result list
   itself; not verifiable enough to cite, and it's about the researchers' relationship generally,
   not the disclosure statement specifically. Flagging as an unconfirmed lead, not a finding.
5. stopflocksafety.org-targeted funding query and an "authors declare" / "no potential conflict"
   phrase-hunt — both null, consistent with every prior pass.

**Genuine new find: the article's title and DOI.** Prior notes cited this only as "Nhan and
Helfers's (2026) study" with no title. Tonight's searches converged on: **"Cops and hotlists:
Balancing security and privacy with ALPR technology," Johnny Nhan & Richard C. Helfers,
*The Police Journal*, DOI 10.1177/0032258X251349633.** Confirmed via three independent listings
(the SAGE DOI-resolving page itself, the SAGE-affiliated mirror, and a stopflocksafety.org summary
page — all describing the same interview-based study with law-enforcement users, policymakers, and
Flock Safety representatives, matching every prior session's description of the study's substance).
This is WebSearch-triangulated, not direct-fetch-verified, same caveat as everything else tonight —
but it's a real citation-precision improvement (title + DOI, not just author/year), and low-risk to
add since it doesn't touch the unresolved independence question at all. **Added to
`Introduction_and_Theory_DRAFT_2026-08-16.md`.**

**Bottom line on independence, unchanged:** no funding/disclosure statement, contract term, or
secondary source quoting one was found tonight, same as every prior pass (08-21, 08-22, 08-24).
This is now four independent sessions and roughly 25 combined search queries across several
distinct angles (grant records, disclosure phrasing, activist-site coverage, journalist reporting,
CV/institutional pages, and tonight's press-release and direct-quote angles) with a consistent null
result. Continuing to treat this as **genuinely primary-source-gated** rather than something a
fifth search session is likely to crack — the honest recommendation is the same as 08-22's: a
direct read of the article (library access or working WebFetch) is the only real path to resolving
it, not more search. Did not touch the already-softened language in the draft (from 08-22/08-24) —
it remains accurate to what's actually known.

## Study 2 full instrument assembly (new file: `Study2_Instrument_DRAFT_2026-08-27.md`)

Assembled the complete Study 2 participant-facing flow, in order, pulling from prior notes rather
than deciding anything new:

1. **Consent** — per the IRB draft's Voluntary Participation section, plus a drafted risk-language
   sentence naming the topic's sensitivity plainly (per the IRB draft's own recommendation that
   this go further than generic "mild, transient annoyance" boilerplate) — a draft sentence for
   Britton's review, not asserted as final.
2. **Screener** — age/residence/attention-check, plus a conditional ZIP-collection step if Path A
   (archival moderator) is adopted.
3. **Vignette (newly drafted this pass)** — a fictitious city ("Meridian Falls," matching Tariff
   Paper's own fictitious-stimulus-name convention) with two matched-length conditions: transparent/
   disclosed-local-only vs. secret/undisclosed-broad-access-default. Grounded in the corpus's real
   recurring mechanism (Bend's "National Lookup" default; Mountain View's undisclosed federal/state
   query access) but deliberately paraphrased into a generic, unnamed mechanism rather than
   quoting or naming any real case — matching the design memo's explicit instruction to avoid
   respondents reacting to the stimulus as recognizable news. **This vignette text has had no
   face-validity review of any kind** — flagged as the single highest-priority thing to pilot,
   higher priority than the scale items (which already went through the 08-20 desk review).
4. **Manipulation checks and confound checks** — assembled verbatim from the 08-19 note.
5. **Mediator 1 (procedural injustice)** — final wording from the 08-20 face-validity review
   (supersedes 08-19's first draft).
6. **Moderator 1 branch point** — both Path A (archival, no visible item) and Path B (self-report
   item) shown, with the document explicit that only one applies depending on Britton's still-open
   call.
7. **Mediator 2 (institutional trust)**, **Moderator 2 (crime-solving necessity)**, **DV (opposition
   intention)** — all final wording from prior notes, assembled in flow order.
8. **Demographics** — matched to Tariff Paper's own battery where constructs overlap, plus one
   study-specific optional item (prior direct contact with law enforcement), flagged as sensitive
   per the IRB draft's own risk note, with "prefer not to say" always available.
9. **Debriefing** — pointed at the IRB draft's existing debriefing text rather than duplicating it,
   to avoid two divergent copies drifting apart over time.

This is a content-order assembly, not a configured survey platform — no Qualtrics branching logic,
randomization weights, or attention-check placement implemented. It's the single document Britton
(or a future session) would need to actually build the survey from, which didn't exist before
tonight.

## What this pass did NOT do

- Did not touch the locked thematic map, hypotheses, or any design element.
- Did not decide either item still reserved for Britton (Moderator 1 Path A/B; single-manipulation
  vs. factorial; PLS-SEM vs. PROCESS) — the instrument document is written to remain usable under
  either branch of the first two.
- Did not pilot or face-validity-review the newly drafted vignette text — flagged plainly as not
  done, not silently assumed fine.
- Did not resolve the Nhan & Helfers independence claim — still genuinely unresolved.
- Did not attempt direct-fetch verification of the new title/DOI finding — WebFetch still blocked.

## Open items for Britton

1. Everything already open in prior notes remains open (archival-moderator feasibility,
   single-manipulation vs. factorial, PLS-SEM vs. PROCESS, CITI certificate number, power analysis,
   Theme 3 promotion gut-check).
2. New: the Study 2 instrument document's vignette text (Section 4) needs an actual face-validity
   pilot before fielding — it's new text with no review yet, unlike the already-reviewed scale
   items.
3. New: the consent-language risk sentence drafted in the instrument document is a proposal, not
   settled — his call on final wording.
4. Nhan & Helfers independence claim: now four sessions and ~25 queries deep with a consistent null
   result. Recommend treating this as resolved-as-unresolvable-by-search and not re-running it
   nightly going forward unless a new lead surfaces — a direct read of the article (library access
   or working WebFetch) is the only realistic path to closing it.
5. WebFetch: 17th+ consecutive session blocked, same environment-level diagnosis as the rest of the
   repo. No new information tonight beyond confirming it again.
