# Submission Tracker — Tariff Messaging & Consumer Behavior (JCM Special Issue)

**Last updated: 2026-09-03.** This is the living, single-source-of-truth
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

**Action needed from Britton, higher priority than anything else on this
list:** do you remember pulling Campbell (1999), Maxham & Netemeyer (2002),
Homburg, Hoyer & Koschate (2005), and Dodds, Monroe & Grewal (1991) via your
Ole Miss library access around 2026-08-13? If that chat session is still
in your claude.ai history, the verified item wording is sitting there and
just needs to be copied into the project files — that would be faster and
higher-confidence than anything else on this list, including today's
Consensus-sourced partial answers. If that history is gone, today's
Consensus.app findings (`notes/2026-09-03-consensus-*.md`, 3 files) are the
fallback, but they are lower-confidence than what you apparently already
had once. **Do not build the Qualtrics instrument on either today's
Consensus answers or the original placeholder guesses until this is
resolved one way or the other.**

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
| Study 1 coding/themes (3 themes: restraint signaling, causation attribution, mitigation-effort) | **Done**, stable since design-lock | No |
| Study 1 Methods section draft | **Drafted** (2026-08-11, consolidated 2026-08-21) | No |
| Study 1 Results write-up (themes → manuscript prose) | **Not started** (~600w budgeted) | No — but needs doing |
| Study 1 validation pilot (blind coding vs. sealed AI codes) | Worksheet is prepared **for a grad assistant to complete as second coder** (2026-08-27, full 15-artifact corpus) — worksheet text confirms it's an *instruction sheet awaiting completion*, not a finished comparison; no Gwet's AC1 or agreement stats computed yet as of this pass | **Yes — external dependency on the grad assistant, not just Britton's own time; check on this immediately given the timeline** |
| Study 2 vignette stimuli (6 cells) | **Drafted v1** (2026-08-04) | No |
| Study 2/3 instrument content & flow | **Fully specified on paper** (2026-08-04) — not yet built in Qualtrics | Yes, once scales lock |
| Study 2/3 scales (5 total) | **See the ⚠ discrepancy flag at the top of this file first** — memory claims all 5 were verified 2026-08-13 via Ole Miss library access but that work isn't in the repo; today's Consensus.app pass is a lower-confidence fallback, not confirmed as the final answer | **Yes — sits directly upstream of instrument build and IRB submission** |
| IRB application package | **Draft content exists** (2026-08-04) but explicitly incomplete: missing CITI number, needs final scale wording reflected, needs realistic dates (placeholder Aug25–Sep15 window has already passed) | **Yes — hard blocker on all data collection** |
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
   pull this) and confirm/reconcile the two still-shaky scales (Fairness —
   likely re-sourced to Campbell 1999 itself; Purchase Intention — decide
   whether to use the existing 3-item draft or Fennell et al.'s 4-item
   proxy, or pull the real Dodds et al. 1991 appendix). WOM can proceed on
   its current best-guess wording if needed — flag it as such in the IRB
   package rather than blocking submission on it.
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
4. **Once IRB approved:** Launch Study 2 and Study 3 on Prolific
   (can likely run in parallel). Typical Prolific turnaround for these
   sample sizes is usually days, not weeks, once live.
5. **Once data in:** Run analyses (MANOVA/mediation for Study 2, PLS-SEM
   for Study 3), draft Results sections for Study 1/2/3, draft
   Discussion/Implications/Limitations/Conclusion.
6. **Final week(s):** Full citation-accuracy pass (same rigor as the
   2026-07-08 pass), word-budget check against the real (not estimated)
   final draft, full read-through, submit via the AMS conference track.

## Open questions only Britton can answer

0. **(Highest priority — see ⚠ flag above)** Do you have the 2026-08-13
   session's chat history where you pulled Campbell, Maxham & Netemeyer,
   Homburg et al., and Dodds/Monroe/Grewal via your Ole Miss library
   access? If yes, that content needs to be copied into
   `notes/2026-08-04-full-instrument-assembly.md` and
   `notes/2026-08-04-scale-items-verification-status.md` for real this
   time, verified against a fresh `git log`/`grep` check before moving on.
1. CITI certificate number/expiration.
2. McNeese HSIRB's realistic turnaround time — this determines whether the
   Oct 15 deadline is actually reachable and, if not, whether to (a) push
   IRB submission literally today, (b) request expedited review if the
   design qualifies (minimal risk, no vulnerable populations, no
   deception beyond standard hypothesis-non-disclosure), or (c) start
   thinking now about whether Oct 15 is realistic at all.
3. Fairness scale: confirm using Campbell (1999)'s own fairness items (once
   sourced) rather than the incorrectly-attributed Xia/Monroe/Cox wording.
4. Purchase Intention: which version — existing 3-item draft, Fennell et
   al.'s 4-item proxy, or wait for a direct pull of Dodds et al. (1991)?
5. **Has the grad assistant completed the blind-coding worksheet yet?**
   Confirmed this pass: as of 2026-08-27 it was still an unfilled
   instruction sheet, not a completed comparison — no Gwet's AC1 computed.
   This is an external dependency (someone else's time, not just yours) and
   the Study 1 Method section's validation-plan claim needs this closed —
   worth checking on today, in parallel with everything else, since it's
   not on your own critical path to unblock.
6. H3 (the interaction hypothesis) — confirm the predicted direction, per
   `Introduction_and_Theory_DRAFT_2026-08-12.md`'s open item #2.
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
