# Submission Tracker — Tariff Messaging & Consumer Behavior (JCM Special Issue)

**⚠ Reconciliation note (2026-09-09, early morning): this file was
overwritten back to a stale (~2026-09-04/09-03) state on disk overnight**
— almost certainly the nightly research pipeline pulling down the GitHub
mirror copy, which had never received the 2026-09-08 evening session's
edits (they were made locally and not yet pushed/synced). That pipeline
run also did real, valuable new work of its own (the CITI policy-page
finding below, dated 2026-09-09) — kept and integrated, not discarded.
Everything else in this note restores what the stale overwrite erased,
confirmed directly by Britton in the 2026-09-08 evening session, not
re-derived or guessed:
- **IRB was submitted to McNeese HSIRB on 2026-09-08.** Submitted
  intentionally covering all three studies (Study 1/2/3), even though
  Study 3 has since been cut from the paper's actual scope — Britton's
  explicit call, in case the cut gets reversed later. No amendment needed.
- **Study 3 is cut from this paper's scope** (cost/word-budget reasons) —
  Study 1 + Study 2 only going forward. Sequencing simplifies to IRB
  approval → Pretest → Study 2.
- **Validation-pilot coders are Holden (grad assistant) + Jason (another
  professor)**, not Britton doing his own coding pass. As of 2026-09-08:
  Holden is done, waiting on Jason. Co-authorship for Jason is still an
  open, undecided question.
- **CITI — see the flagged conflict below, not yet resolved.** Britton
  said tonight "I got the basic and I think that's all we need," but the
  nightly pipeline independently found McNeese's own published policy
  page requiring the Comprehensive module. This is a live discrepancy,
  not settled either way — see Open Question 1.

**Last updated: 2026-09-04** (writing-prep pass ahead of Britton's weekend session — see
note at bottom of Status table and the new consolidated Methods file). This is the
living, single-source-of-truth
status doc for getting this paper submitted. Everything else in this
project (38+ dated files in `notes/`) is the detailed record of *how* each
piece got built; this file is *where things stand* and *what's left*. Update
it whenever real status changes — don't let it go stale the way the
scattered notes did.

## Deadline

- **Hard deadline: October 15, 2026 — full-manuscript deadline for the AMS
  conference track** (locked venue: JCM special issue *"Crafting Shape in a
  Fluid World,"* AMS 2026, per `notes/2026-08-04-design-locked-jcm-fit.md`).
  Full paper only, no abstract-only option.
- **Britton's self-imposed target (as of 2026-08-04): submit by late
  September.** That date is effectively already gone or nearly gone as of
  today — treat Oct 15 as the real constraint from here on, but recognize
  the schedule has already slipped past the original plan once.
- **Today is 2026-09-03. That leaves 42 days (6 weeks) to the hard
  deadline.**
- **Britton's stated target (2026-09-03): IRB package completed and
  submitted this weekend (~2026-09-05/06)** — he's got other work in
  between now and then, so no further action needed on this thread until
  then unless something changes.
- ~~Flagged 2026-09-09: weekend target passed with nothing indicating
  submission~~ — **resolved: Britton confirmed directly, IRB was submitted
  2026-09-08.** The nightly pipeline's flag was accurate as of the stale
  mirror it read from, just superseded by real-time information the
  pipeline had no visibility into.
- **2026-09-10: the "Section 301 government response is overdue" litigation
  thread (unrelated to IRB, background docket-tracking only) is resolved —
  it was filed on time (Sep 4); CourtListener's own docket mirror just hadn't
  synced it in until after Sep 8, which is why five straight nightly checks
  missed it. See `notes/2026-09-10-litigation-recheck-section301-government-
  response-was-filed-on-time-not-actually-overdue.md`. No action needed.
- **2026-09-10: CITI Comprehensive-vs-Basic finding independently
  re-confirmed** (second direct fetch of McNeese's HSIRB policy page, same
  exact text as 09-09), and one more attempt made to find a stated HSIRB
  turnaround time / submission portal — still not publicly findable, this
  genuinely needs a direct ask to the IRB office. Clean 5-minute summary of
  everything currently blocking this project:
  `notes/2026-09-10-blocker-briefing-for-britton.md`.
- **Working backward-planned schedule, unchanged otherwise (pending
  confirmation of actual HSIRB turnaround — see open question #2):** IRB
  submitted this weekend → if approved in ~1-2 weeks, data collection
  (Pretest → Study 2, Study 3 in parallel) complete by ~2026-09-27 →
  analysis + write-up ~2026-09-28 to 2026-10-08 → final polish + submission
  by 2026-10-15. This schedule has almost no slack — see
  `notes/2026-08-04-IRB-draft-content.md` Questions 3-4 for the full
  reasoning, including the Pretest→Study 2 sequencing dependency.
- A separate JCM ScholarOne direct-submission window (June 15–Aug 15, 2026)
  already closed before this project's design was even locked — the AMS
  conference-track route is the only path left for this special issue.

## ⚠ Urgent discrepancy found 2026-09-03 — read before touching the scales

Britton's memory system (`project_tariff_paper_pipeline.md`) states that
**all 5 Study 2/3 scales were already verified on 2026-08-13**, via his Ole
Miss library access through the claude-in-chrome extension — and with
**better answers than anything found via Consensus.app today**:
- Campbell (1999) and Maxham & Netemeyer (2002): "verified with real item
  wording, both corrected earlier wrong reconstructions" (real library
  PDFs, not AI-synthesized secondary corroboration like today's Consensus
  pass).
- Xia, Monroe & Cox (2004): confirmed no scale of its own (matches today's
  independent Consensus finding — good convergent validation on that
  specific point) — but memory says it was **replaced with Homburg, Hoyer
  & Koschate (2005)'s verified 3-item Perceived Motive Fairness scale**,
  which Britton signed off on same-day. Today's Consensus pass never found
  this paper at all.
- Dodds, Monroe & Grewal (1991): memory says verified via JSTOR as a
  **5-item "Willingness to Buy Indicators" scale**, not the 3-item guess
  this project had been carrying, and not the 4-item Fennell et al. (2025)
  proxy Consensus found today either.

**Checked just now (2026-09-03): none of this is actually in the repo.**
`grep` for "Homburg" and "Willingness to Buy Indicators" across the entire
`TARIFF_PAPER` folder returns nothing. `notes/2026-08-04-full-instrument-
assembly.md` and `notes/2026-08-04-scale-items-verification-status.md`
still show `[UNVERIFIED]` tags throughout — `git log` confirms neither file
has been touched since the initial repo mirror. **The 2026-08-13 verification
session's real findings appear to have been done in an interactive session
and never committed anywhere** — the same failure pattern already
documented once in this project's memory for the Home Depot McPhail→Bastek
citation fix (found and "fixed" four separate times before it actually
landed in a file).

**Searched claude.ai's history 2026-09-03 — the session was not found.**
Checked both the regular chat history and the "Claude Code" cloud sessions
list (`claude.ai/code`). The only cloud session from ~mid-August is titled
"APA citation style skill" and is about building an APA-citation-checking
skill, tested against `Introduction_and_Theory_DRAFT_2026-08-12.md` — not
the scale-verification work. Notably, **that session's own citation review
still flags Campbell (1999) as "not checked in this project's prior
citation-verification pass"** — a real data point suggesting the Ole Miss
scale-verification work may not have been fully completed/saved even in a
session that did happen, not just lost afterward. The three regular-chat
entries from Aug 13 (Chrome extension troubleshooting, two GitHub-access
threads) are unrelated tooling fixes. **Most likely explanation: that
verification ran in a local terminal Claude Code session on Britton's own
machine, which doesn't sync to claude.ai's cloud session list.** Britton:
worth a quick check locally if you remember running it that way, but this
is not blocking further work.

**Decision: proceeded on Consensus.app answers, and got a strong result.**
A fifth targeted query found Campbell (1999)'s actual Perceived Fairness
scale with quoted item text and a reported reliability statistic (2-item,
r=.84) — not an inference, a direct quote-level match. **Fairness and
Opportunism — the two theoretically load-bearing mediators H1a/H1b/H2a/H2b
depend on — are now both resolved with real, correctly-attributed item
wording**, folded directly into `notes/2026-08-04-full-instrument-
assembly.md` (items 6-7). Only Purchase Intention and Word-of-Mouth
(secondary/downstream DVs, not mediators) remain genuinely open — see
`notes/2026-09-03-consensus-dodds-maxham-scales-partial.md`. If the lost
2026-08-13 local session surfaces later, reconciling it is a fast
follow-up, not a blocker — the instrument no longer needs it to move
forward.

## The one thing that matters most

**Updated 2026-09-09: IRB is submitted (2026-09-08). Study 2 (and Study 3,
though Study 3 is now cut from scope) still have zero data collected**, and
no evidence exists that Prolific recruitment or Qualtrics fielding has
started. Everything else — Introduction, Theory/Hypotheses, Study 1 corpus,
Study 1 coding, vignette stimuli, instrument content, model diagrams — is
drafted or far along. The empirical work that actually produces a Results
section has not begun. **The bottleneck now is HSIRB's decision turnaround
(out of anyone's control) plus building the actual Qualtrics instrument**,
which can and should happen now in parallel with waiting.

## Status by component

| Component | Status | Blocking? |
|---|---|---|
| Venue/design lock (3×2 factorial, JCM fit) | **Done** (2026-08-04, reconfirmed 2026-08-13) | No |
| Introduction & Theory/Hypotheses draft | **Strong first draft done** (2026-08-12) — needs Britton's read-through, H3 confirmation, and the scale-citation fixes below reflected in-text | No — but should get a final pass once scales lock |
| Study 1 corpus (real corporate tariff-messaging artifacts) | **Actively maintained, high confidence** — near-daily verification/correction passes through 2026-09-03 | No |
| Study 1 coding/themes (6 themes final) | **Phase 3 done 2026-09-04, by Britton.** Reviewed Claude's proposed 7-theme resolution and overrode one item — Home Depot's `reversal-narrative` kept as a deviant case, not elevated to a 7th theme (single artifact, more conservative call) — see `Study1_Phase3_Quick_Decisions_2026-09-04.md` | No |
| Study 1 Methods section draft | **Drafted, fully consolidated**, updated same day once Phase 3 closed (`Study1_Methods_Section_DRAFT_2026-09-04_CONSOLIDATED.md`) | No |
| Study 1 Results write-up (themes → manuscript prose) | **Done 2026-09-04** (~600w), in `Tariff_Manuscript_Working_Draft_2026-09-04.md`, reflecting the final six-theme structure | No |
| Study 1 validation pilot (blind coding vs. sealed AI codes) | Coders are **Holden (grad assistant) + Jason (another professor)**, not Britton. As of 2026-09-08: **Holden is done, waiting on Jason.** Co-authorship for Jason still undecided. No Gwet's AC1 computed yet — needs Jason's pass first | **Yes — external dependency on Jason's time, not Britton's** |
| **Pretest** (vignette validation, N=150-180, Prolific) | Design specified (`notes/2026-08-04-pretest-design.md`) — **not yet run.** Must complete and be analyzed BEFORE Study 2 can launch (may trigger vignette revisions) — this is a real sequencing dependency, not something that can run in parallel with Study 2 | **Yes — gates Study 2 specifically; only Study 3 can run in parallel with Pretest+Study 2** |
| Study 2 vignette stimuli (6 cells) | **Drafted v1** (2026-08-04) | No |
| Study 2/3 instrument content & flow | **Fully specified with recommended defaults for every remaining decision** (2026-08-04, updated 2026-09-03) — not yet built in Qualtrics | No longer blocking on content — just needs Britton's confirm/override pass and the actual Qualtrics build |
| Study 2/3 scales (5 total) | **4 of 5 fully resolved with quote-level/verbatim wording** (Trust, Fairness, Opportunism, WOM — WOM resolved 2026-09-04, Maxham & Netemeyer 2002's verbatim 3-item Favorable WOM scale, fetched directly from the paper's own Appendix A). Purchase Intention is substantially improved: the real 1991 Dodds, Monroe & Grewal appendix is still paywalled, but Grewal et al. (1998, *Journal of Retailing*, co-authored by one of the original scale's own authors) reproduces the 3 items verbatim in its own Table 1 — item 3 matches the project's existing draft, items 1-2 don't and have been swapped for the Grewal et al.-sourced wording as the new recommended default in `notes/2026-08-04-full-instrument-assembly.md` item 9 (2026-09-04). | **Down to one confirm-or-override** — WOM is done; Purchase Intention has a strong default in place, just needs Britton's sign-off (or a 1991-appendix pull if library access is handy this weekend) |
| IRB application package | **Draft content complete.** Britton completed a CITI refresher 2026-09-03 (new Record ID 79382211, McNeese-affiliated, expires 2029-09-03) — this resolved 2 of 3 flagged concerns (institution affiliation, expiration). **One item still open: it's still "Stage 1 - Basic Course," not the "Comprehensive" module McNeese's policy text names.** | **Down to one specific confirm-with-IRB-office question** — everything else in the package is ready |
| **IRB submission to McNeese HSIRB** | **Submitted 2026-09-08.** Awaiting HSIRB decision — turnaround unknown | **Waiting on HSIRB — nothing more to do here until they respond** |
| Study 2 data collection (Prolific, N target 360–600) | **Not started** | Depends on IRB |
| Study 3 data collection (Prolific, N target 300–400) | **Cut from paper scope (2026-09-08)** — IRB still covers it in case the cut reverses | N/A — not being run |
| Study 2 analysis (MANOVA/mediation) | Not started (no data) | Depends on data collection |
| Study 3 analysis (PLS-SEM) | Not started (no data) | Depends on data collection |
| Results sections (Study 1, 2, 3) | Not started — correctly, per project rule against writing results before real data exists | Depends on above |
| Discussion/Implications, Limitations/Conclusion | Not drafted | Depends on Results |
| Word-budget (8,000-word Emerald/JCM hard cap incl. refs/tables/figures) | Planning estimate ~7,010w with ~990w buffer (2026-08-13) — **built on placeholder estimates for unwritten sections; re-check once Results/Discussion are real** | No, but watch it |
| Citation-accuracy pass | One full pass done 2026-07-08 (caught a real author-list error); today's Consensus pass caught a second real error (Xia/Monroe/Cox misattribution) | No, but do one more full pass before submission |
| Model diagrams | **Done** (ChatGPT_model.png, leaner version, Tariff_Model_Lean) | No |

## Critical path to submission (do these roughly in this order)

1. **This week:** Get your CITI certificate number/expiration (only you can
   pull this — already done, see item 1 below) and confirm-or-override which
   Purchase Intention items to use — **RESOLVED 2026-09-07: real Dodds,
   Monroe & Grewal (1991) appendix pulled via your library access
   (`Literature/Dodds_Monroe_Grewal_1991_JMR_EffectsPriceBrandStore.pdf`),
   verbatim 5-item "Willingness to Buy" scale now in hand — no more wording
   uncertainty, see `notes/2026-09-07-purchase-intention-1991-original-
   resolved-library-pull.md`.** Only remaining choice: all 5 items, or a
   3-item subset (items 1/4/5 are the safest generic fallback; items 2-3
   reference "the price shown," which fits this study's price-manipulation
   vignettes well). Fairness, Opportunism, Trust, and WOM are all done — no
   action needed on any of those four.
2. **This week/early next:** Finalize IRB application package (fold in CITI
   number, finalized scale wording, realistic dates) and **submit to
   McNeese HSIRB**. This is the single highest-leverage action available
   right now — every downstream step depends on it, and its turnaround time
   is the one project timeline element Claude Code has no visibility into.
   **Britton: what's McNeese HSIRB's typical turnaround for a minimal-risk,
   Prolific-based survey/experiment? That number should drive everything
   else on this list.**
3. **In parallel with IRB review:** Build the actual Qualtrics instruments
   for Study 2 and Study 3 (content is already fully specified in
   `notes/2026-08-04-full-instrument-assembly.md` — this is implementation,
   not design work). Confirm blind-coding validation-pilot agreement
   analysis is actually complete (see flag above).
4. **Once IRB approved:** Launch the **Pretest** (N=150-180) and **Study 3**
   (N=300-400) in parallel — Study 3 doesn't depend on vignette stimuli, so
   it can start immediately. **Study 2 (N=360-600) cannot launch until the
   Pretest is complete AND analyzed**, since it may trigger vignette
   revisions. Typical Prolific turnaround for these sample sizes is usually
   days, not weeks, once live — the Pretest→Study 2 sequencing, not
   Prolific speed, is the real time cost here.
5. **Once data in:** Run analyses (MANOVA/mediation for Study 2, PLS-SEM
   for Study 3), draft Results sections for Study 1/2/3, draft
   Discussion/Implications/Limitations/Conclusion.
6. **Final week(s):** Full citation-accuracy pass (same rigor as the
   2026-07-08 pass), word-budget check against the real (not estimated)
   final draft, full read-through, submit via the AMS conference track.

## Open questions only Britton can answer

0. **(Resolved 2026-09-03 — no longer blocking)** Searched claude.ai's
   history for the 2026-08-13 session; not found in the cloud session list
   (see the ⚠ section above for detail). If you happen to have it in a
   local terminal session's history, worth a quick check and reconciliation
   — but the project is moving forward on today's Consensus.app-sourced
   scale answers in the meantime.
1. **CITI: down to one specific question — strong evidence found 2026-09-09.**
   Britton refreshed his training 2026-09-03 under McNeese's own CITI
   affiliation (Record ID 79382211, score 93/100, expires 2029-09-03) —
   resolved the institution-affiliation and expiration concerns. **Still
   Stage 1 - Basic Course, not the "Comprehensive" module.** Fetched
   McNeese's own published HSIRB policy page directly 2026-09-09
   (`mcneese.edu/policy/human-subjects-institutional-review-board-hsirb-policy/`)
   — its exact text: *"All researchers involved in research with human
   subjects must complete a CITI Program training module about human
   subjects protection, either 'Biomedical Comprehensive' or
   'Social/Behavior/Educational Comprehensive'"* — no mention of Basic
   Course/Refresher anywhere. Strong evidence the Basic Course won't
   satisfy this, not a confirmed final answer (policy pages can lag
   practice) — see `notes/2026-09-09-docket-recheck-partial-waf-block-and-
   citi-comprehensive-finding.md`. **Recommend just completing the
   Social/Behavior/Educational Comprehensive CITI module now** (same-day,
   self-paced) rather than waiting on an IRB-office confirmation, given the
   Oct 15 deadline.

   **⚠ Live, unresolved conflict (2026-09-09) — flagging, not resolving:**
   Britton stated directly in the 2026-09-08 evening session "I got the
   basic and I think that's all we need," treating this as already closed.
   That's the opposite conclusion from what McNeese's own policy page says
   above. Since the IRB package has already been submitted with Basic
   Course on file, this isn't hypothetical — worth Britton either (a)
   confirming directly with the IRB office that Basic Course was accepted
   in practice, or (b) completing the Comprehensive module proactively as a
   precaution. Not assuming either answer here — this is a compliance
   question, not a judgment call for an AI session to settle.
2. McNeese HSIRB's realistic turnaround time — this determines whether the
   Oct 15 deadline is actually reachable and, if not, whether to (a) push
   IRB submission literally today, (b) request expedited review if the
   design qualifies (minimal risk, no vulnerable populations, no
   deception beyond standard hypothesis-non-disclosure), or (c) start
   thinking now about whether Oct 15 is realistic at all.
3. ~~Fairness scale~~ — **resolved 2026-09-03**, Campbell (1999) Study 2
   two-item scale (r=.84), see `notes/2026-08-04-full-instrument-
   assembly.md` item 6.
4. ~~Purchase Intention~~ — **resolved 2026-09-07**, real Dodds, Monroe &
   Grewal (1991) appendix pulled via library access, verbatim 5-item
   "Willingness to Buy" scale (not the Grewal et al. 1998 proxy), see
   `notes/2026-09-07-purchase-intention-1991-original-resolved-library-
   pull.md`. Only remaining choice is 5 items vs. a 3-item subset — a quick
   yes/no, not a blind pick.
5. **Has the grad assistant completed the blind-coding worksheet yet?**
   Confirmed this pass: as of 2026-08-27 it was still an unfilled
   instruction sheet, not a completed comparison — no Gwet's AC1 computed.
   This is an external dependency (someone else's time, not just yours) and
   the Study 1 Method section's validation-plan claim needs this closed —
   worth checking on today, in parallel with everything else, since it's
   not on your own critical path to unblock.
6. H3 (the interaction hypothesis) — **still open**, separately from the Phase 3 items
   above, which Britton has now finalized. Claude's recommendation (2026-09-04) is to
   keep it as originally drafted (amplified-under-absorption /
   attenuated-under-pass-through direction) — see chat for reasoning — but this one
   hasn't been through Britton's own review yet. Confirm your own predicted direction
   against `Introduction_and_Theory_DRAFT_2026-08-12.md`'s open
   item #2.
7. Which banked/measured-but-unreported scales (if any) to add to the
   instrument for a future companion paper, per
   `notes/2026-08-13-design-confirmed-3x2-word-budget.md` — resolve before
   instrument build so it isn't a late change.

## Research tooling note
Britton has a paid Consensus.app subscription (see memory:
`reference_consensus_app.md`) — used today for the scale-verification pass
above. Good next use: verifying Campbell (1999)'s actual fairness-item
wording directly, and any citation-accuracy spot-checks during the final
pass in step 6 above.
