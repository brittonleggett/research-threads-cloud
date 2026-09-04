# Submission Tracker — Tariff Messaging & Consumer Behavior (JCM Special Issue)

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

**Study 2 and Study 3 have zero data collected, the IRB application has not
been submitted to McNeese HSIRB, and no evidence exists in this project's
files that Prolific recruitment or Qualtrics fielding has started.**
Everything else — Introduction, Theory/Hypotheses, Study 1 corpus, Study 1
coding, vignette stimuli, instrument content, model diagrams — is drafted
or far along. The empirical work that actually produces a Results section
has not begun. With 42 days left, **IRB submission is the critical-path
bottleneck and should happen this week**, not after every scale is
perfectly verified.

## Status by component

| Component | Status | Blocking? |
|---|---|---|
| Venue/design lock (3×2 factorial, JCM fit) | **Done** (2026-08-04, reconfirmed 2026-08-13) | No |
| Introduction & Theory/Hypotheses draft | **Strong first draft done** (2026-08-12) — needs Britton's read-through, H3 confirmation, and the scale-citation fixes below reflected in-text | No — but should get a final pass once scales lock |
| Study 1 corpus (real corporate tariff-messaging artifacts) | **Actively maintained, high confidence** — near-daily verification/correction passes through 2026-09-03 | No |
| Study 1 coding/themes (7 themes final, up from the original 3-5) | **Phase 3 done 2026-09-04** — see `Study1_Phase3_Quick_Decisions_2026-09-04.md`. Used a recommend-and-confirm protocol (Claude proposed each resolution with reasoning, Britton confirmed adopting) rather than researcher-only review — the Methods draft's AI-Use Disclosure was updated to describe this accurately rather than left stating "no AI involvement" | No |
| Study 1 Methods section draft | **Drafted, fully consolidated**, updated same day once Phase 3 closed (`Study1_Methods_Section_DRAFT_2026-09-04_CONSOLIDATED.md`) | No |
| Study 1 Results write-up (themes → manuscript prose) | **Done 2026-09-04** (~600w), in `Tariff_Manuscript_Working_Draft_2026-09-04.md` | No |
| Study 1 validation pilot (blind coding vs. sealed AI codes) | Worksheet is prepared **for a grad assistant to complete as second coder** (2026-08-27, full 15-artifact corpus) — worksheet text confirms it's an *instruction sheet awaiting completion*, not a finished comparison; no Gwet's AC1 or agreement stats computed yet as of this pass | **Yes — external dependency on the grad assistant, not just Britton's own time; check on this immediately given the timeline** |
| **Pretest** (vignette validation, N=150-180, Prolific) | Design specified (`notes/2026-08-04-pretest-design.md`) — **not yet run.** Must complete and be analyzed BEFORE Study 2 can launch (may trigger vignette revisions) — this is a real sequencing dependency, not something that can run in parallel with Study 2 | **Yes — gates Study 2 specifically; only Study 3 can run in parallel with Pretest+Study 2** |
| Study 2 vignette stimuli (6 cells) | **Drafted v1** (2026-08-04) | No |
| Study 2/3 instrument content & flow | **Fully specified with recommended defaults for every remaining decision** (2026-08-04, updated 2026-09-03) — not yet built in Qualtrics | No longer blocking on content — just needs Britton's confirm/override pass and the actual Qualtrics build |
| Study 2/3 scales (5 total) | **4 of 5 fully resolved with quote-level/verbatim wording** (Trust, Fairness, Opportunism, WOM — WOM resolved 2026-09-04, Maxham & Netemeyer 2002's verbatim 3-item Favorable WOM scale, fetched directly from the paper's own Appendix A). Purchase Intention is substantially improved: the real 1991 Dodds, Monroe & Grewal appendix is still paywalled, but Grewal et al. (1998, *Journal of Retailing*, co-authored by one of the original scale's own authors) reproduces the 3 items verbatim in its own Table 1 — item 3 matches the project's existing draft, items 1-2 don't and have been swapped for the Grewal et al.-sourced wording as the new recommended default in `notes/2026-08-04-full-instrument-assembly.md` item 9 (2026-09-04). | **Down to one confirm-or-override** — WOM is done; Purchase Intention has a strong default in place, just needs Britton's sign-off (or a 1991-appendix pull if library access is handy this weekend) |
| IRB application package | **Draft content complete.** Britton completed a CITI refresher 2026-09-03 (new Record ID 79382211, McNeese-affiliated, expires 2029-09-03) — this resolved 2 of 3 flagged concerns (institution affiliation, expiration). **One item still open: it's still "Stage 1 - Basic Course," not the "Comprehensive" module McNeese's policy text names.** | **Down to one specific confirm-with-IRB-office question** — everything else in the package is ready |
| **IRB submission to McNeese HSIRB** | **No evidence of actual submission as of 2026-09-03** | **Yes — the critical-path item** |
| Study 2 data collection (Prolific, N target 360–600) | **Not started** | Depends on IRB |
| Study 3 data collection (Prolific, N target 300–400) | **Not started** | Depends on IRB |
| Study 2 analysis (MANOVA/mediation) | Not started (no data) | Depends on data collection |
| Study 3 analysis (PLS-SEM) | Not started (no data) | Depends on data collection |
| Results sections (Study 1, 2, 3) | Not started — correctly, per project rule against writing results before real data exists | Depends on above |
| Discussion/Implications, Limitations/Conclusion | Not drafted | Depends on Results |
| Word-budget (8,000-word Emerald/JCM hard cap incl. refs/tables/figures) | Planning estimate ~7,010w with ~990w buffer (2026-08-13) — **built on placeholder estimates for unwritten sections; re-check once Results/Discussion are real** | No, but watch it |
| Citation-accuracy pass | One full pass done 2026-07-08 (caught a real author-list error); today's Consensus pass caught a second real error (Xia/Monroe/Cox misattribution) | No, but do one more full pass before submission |
| Model diagrams | **Done** (ChatGPT_model.png, leaner version, Tariff_Model_Lean) | No |

## Critical path to submission (do these roughly in this order)

1. **This week:** Get your CITI certificate number/expiration (only you can
   pull this — already done, see item 1 below) and confirm-or-override
   Purchase Intention's new recommended default (Grewal et al. 1998-sourced
   wording — see `notes/2026-08-04-full-instrument-assembly.md` item 9) or
   pull the real Dodds et al. (1991) appendix if there's time. Fairness,
   Opportunism, Trust, and WOM are all done — no action needed on any of
   those four.
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
1. **CITI: down to one specific question.** Britton refreshed his training
   2026-09-03 under McNeese's own CITI affiliation (Record ID 79382211,
   score 93/100, expires 2029-09-03) — resolved the institution-affiliation
   and expiration concerns. **Still Stage 1 - Basic Course, not the
   "Comprehensive" module McNeese's policy text names.** Ask the IRB office
   directly whether Basic Course/Refresher satisfies the requirement in
   practice, or whether a separate Comprehensive module is needed — don't
   guess either way.
2. McNeese HSIRB's realistic turnaround time — this determines whether the
   Oct 15 deadline is actually reachable and, if not, whether to (a) push
   IRB submission literally today, (b) request expedited review if the
   design qualifies (minimal risk, no vulnerable populations, no
   deception beyond standard hypothesis-non-disclosure), or (c) start
   thinking now about whether Oct 15 is realistic at all.
3. ~~Fairness scale~~ — **resolved 2026-09-03**, Campbell (1999) Study 2
   two-item scale (r=.84), see `notes/2026-08-04-full-instrument-
   assembly.md` item 6.
4. Purchase Intention: the Grewal et al. (1998)-sourced wording is now the
   recommended default in `notes/2026-08-04-full-instrument-assembly.md`
   item 9 (item 3 already matched the prior draft; items 1-2 replaced) —
   just needs your confirm-or-override, or a direct pull of Dodds et al.
   (1991)'s own 1991 appendix if you get library access this weekend. Last
   real scale decision, and it's now a quick yes/no, not a blind pick.
5. **Has the grad assistant completed the blind-coding worksheet yet?**
   Confirmed this pass: as of 2026-08-27 it was still an unfilled
   instruction sheet, not a completed comparison — no Gwet's AC1 computed.
   This is an external dependency (someone else's time, not just yours) and
   the Study 1 Method section's validation-plan claim needs this closed —
   worth checking on today, in parallel with everything else, since it's
   not on your own critical path to unblock.
6. ~~H3 (the interaction hypothesis)~~ — **resolved 2026-09-04**, kept as originally
   drafted (amplified-under-absorption / attenuated-under-pass-through direction),
   per Britton's confirm-Claude's-judgment call. Still worth a final gut-check on your
   own read-through, but no longer an open design question.
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
