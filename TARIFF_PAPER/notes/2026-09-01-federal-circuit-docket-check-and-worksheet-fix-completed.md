# 2026-09-01 — Federal Circuit docket re-check (no new activity found); McPhail→Bastek fix
actually completed this time (was only half-applied on 2026-08-29)

Two pieces of work tonight: (1) the requested follow-up check on the consolidated Federal
Circuit appeal (Nos. 26-1895/-1897/-1899) for docket activity since the opening brief (filed
2026-08-10, per the 2026-08-31 note); (2) a discovered, unfinished fix from a prior night that
I completed. Did not touch the refund-wave corpus-scope call or the Insteel quote — both remain
Britton's, untouched tonight, per standing instruction.

---

## 1. Federal Circuit docket check — negative result, tools worked, nothing new found

**Method:** Reused the 2026-08-31 note's CourtListener REST search API technique
(`courtlistener.com/api/rest/v4/search/?q=...&type=r&court=cafc`, plain unauthenticated curl).
Confirmed again tonight: docket detail and docket-entries endpoints both return 401
("Authentication credentials were not provided") without a login; the *search* endpoint works
fine unauthenticated and returns a `recap_documents` array (RECAP-archived filings only, capped
at ~3 highest-relevance hits per query — not a full docket listing).

Ran the V.O.S. Selections case (docket_id 73433096, PACER case ID 24456) through eight different
search-term variants (plain case name, "opening brief," "response brief," "extension of time,"
"corrected brief," "amicus," "oral argument," "principal brief," "notice of appearance") to
surface as much of the RECAP-held document list as this technique allows. **Highest document
number found across every query: #19, the opening brief filed 2026-08-10** — the same document
the 2026-08-31 note already had. No RECAP-archived filing postdating it turned up. Also
recovered docket entries #12/13/17/18 (consolidation order, motion-to-dismiss/deconsolidation of
26-1898, and the order setting the Aug 10 opening-brief deadline) — all already dated before or
on 08-10, nothing new.

**Cross-checked against the Federal Circuit's own public oral-argument calendars** (direct curl
worked cleanly against `cafc.uscourts.gov` — no WAF block on this .gov site, unlike
`cit.uscourts.gov`): downloaded and read in full the September 2026 calendar (revised 8/19/2026)
and the October 2026 calendar (Chicago sitting, revised 8/27/2026; DC sitting, revised 8/21/2026).
**Neither lists 26-1895, -1897, or -1899, or any party name from that case, on any panel.** No
oral argument has been scheduled for this consolidated appeal as of either revision date.

**WebSearch corroboration (secondary, not primary-confirmed):** several law-firm trackers
(Jackson Walker among them) describe the importers'/appellees' response brief as due sometime in
September 2026, consistent with typical Federal Circuit briefing timelines after an August 10
opening brief — but I could not find a primary document (order or docket entry) stating the exact
due date, and RECAP has no document for it yet. Treating this as B-tier only.

**Also checked: has Axle of Dearborn (the CIT's Aug 13, 2026 de minimis ruling, per the 08-30
note) been appealed to the Federal Circuit?** WebSearch found no reporting of an appeal filed as
of tonight (only ~2.5 weeks post-ruling; the standard 60-day window for the government to appeal
a CIT judgment hasn't run yet). Genuinely open/unresolved, not yet actionable either way.

**Bottom line: stable negative result.** No new appellate docket activity in the consolidated
V.O.S. Selections/AGS/Grant & Bowman appeal since the opening brief. Nothing in the manuscript's
framing needs updating on this point tonight. Worth another pass once late September/October
news of a response brief surfaces, or once RECAP picks up a new filing.

## 2. Refund-processing status (context only, not corpus-scope call, not inserted anywhere)

WebSearch surfaced CBP's own refund-processing dashboard figures as of ~Aug 25, 2026: ~$132.5B
of the refund pool has entered CAPE for processing, ~$106.6B certified/sent to Treasury (~64% of
the pool disbursed), and CBP announced a delay to "Phase 3" (finally-liquidated entries, >80 days
post-liquidation) to build additional validations. These are WebSearch-sourced only tonight, not
independently primary-verified, and — per standing instruction — **not added to any corpus or
manuscript file**, since the refund-wave corpus-scope question is explicitly Britton's call, not
mine. Flagging only as current-state context in case it's useful when he makes that call.

## 3. Home Depot McPhail→Bastek fix — found to be only half-applied on 2026-08-29, now actually completed

While re-reading the consolidated corpus draft to orient for tonight's work, I found that the
2026-08-29 note's claim to have "actually applied" this fix (after four prior nights of
re-confirming it without editing) was **itself only partially true**. On inspection tonight,
`Study1_Corpus_and_Coding_DRAFT_2026-08-21.md` was internally inconsistent: the corpus table row
(line 62/68) and its footnote correctly said "Bastek, not McPhail," but the "Known drift" note
still read "**Not fixed in this file yet**" and the actual Phase-1 write-up for artifact 15 (item
15 in the numbered code list) still said "CFO Richard McPhail reversed" with the old paraphrased
quote. So the table got fixed, the narrative text didn't — the exact kind of partial-fix drift
the project has been chasing since 08-18.

**Fixed properly tonight, in the same file:**
- The "Known drift" note now says the fix is complete (2026-09-01), cites the verbatim primary
  quote from Home Depot's own IR transcript (already read in full on 2026-08-29, per that note),
  and is explicit that the 08-29 note's claim was only partly right.
- Item 15's write-up now names Billy Bastek (EVP Merchandising) and uses the verbatim quote
  ("there'll be some modest price movement in some categories, but it won't be broad based")
  instead of the paraphrase.

**Also fixed tonight, in `Study1_Validation_Pilot_BLIND_CODING_WORKSHEET_2026-08-27_FULL_CORPUS.md`**
(artifact 15 entry): this file — the one meant for the grad assistant's blind second-coding pass
— still had both the McPhail misattribution *and* an unsupported "to the Wall Street Journal"
sourcing claim that no source in this project's corpus actually supports (flagged as
likely-fabricated by the 2026-08-29 note, left unfixed at the time out of caution about the
"don't casually overwrite" convention). Corrected the speaker, added the verbatim quote, removed
the WSJ claim, and added an inline dated correction note so the grad assistant sees exactly what
changed and why, with a note that the correction doesn't change what's being coded (same event,
same company) in case they'd already started before this fix landed. This document had *not* yet
been fixed as of tonight — no note between 08-29 and today mentions touching it, and the file
itself still had the error at the start of tonight's session.

I did not touch `Study1_Validation_Pilot_AI_CODES_SEALED_2026-08-27_FULL_CORPUS.md` (the sealed
answer key) — checked it and it never had the McPhail/WSJ error in the first place, so nothing
needed fixing there.

## Untouched per standing instructions

Refund-wave corpus-scope call and the Insteel Industries "freight"/"profit" quote — both
Britton's, not approached tonight.

---

## For Britton

1. **No new Federal Circuit activity** in the consolidated V.O.S. Selections/AGS/Grant & Bowman
   appeal (26-1895/-1897/-1899) since the Aug 10 opening brief — checked via CourtListener's
   RECAP search and the Federal Circuit's own September/October 2026 oral-argument calendars,
   both read directly. No oral argument scheduled yet on either calendar as of their most recent
   revisions (8/19, 8/21, 8/27). A response brief is reportedly due sometime in September per
   secondary sources, but I couldn't pin down an exact date from a primary document.
2. **The McPhail→Bastek fix is now actually, fully applied** in both
   `Study1_Corpus_and_Coding_DRAFT_2026-08-21.md` and the grad-assistant-facing
   `Study1_Validation_Pilot_BLIND_CODING_WORKSHEET_2026-08-27_FULL_CORPUS.md` — the latter also
   had an apparently-fabricated "Wall Street Journal" sourcing detail removed. If the grad
   assistant hasn't started coding yet, this closes the loose end from the reminder scheduled for
   2026-08-31. If they *have* already started under the old (wrong) text, worth a quick check with
   them — the correction shouldn't change the substance of the coding, but flagging in case it
   matters to them.
3. Worth noting as a process point, not a content one: this is the second time a note in this
   project claimed a fix was "actually applied" when it was only partially applied (table/footnote
   fixed, body text missed). Future passes touching this artifact might want to grep for both
   "McPhail" and "Bastek" across the whole file before declaring it done, rather than checking only
   the section that was the original target.

## Reconciliation note (added during overnight merge, 2026-09-01)

This session ran in a git worktree that, due to a tooling issue, was branched from an older
point in history (2026-08-27) rather than the actual current `main` — so it never saw the real
2026-08-29 commit that fixed `Study1_Corpus_and_Coding_DRAFT_2026-08-21.md`. On reconciling
against the true current file at merge time, item 15's write-up **was already fully corrected**
to Billy Bastek with the verbatim quote — the "half-applied fix" described in section 3 above was
real relative to this session's own (stale) starting point, but not an accurate description of
the file Britton has actually had all along. No changes from this session were applied to that
file during the merge; it was left as-is. The one genuinely new, still-needed fix from tonight —
correcting `Study1_Validation_Pilot_BLIND_CODING_WORKSHEET_2026-08-27_FULL_CORPUS.md` (same
McPhail→Bastek error, plus removing the unsupported "Wall Street Journal" sourcing claim) — was
real and has been kept; that file had not been touched by any prior session.
