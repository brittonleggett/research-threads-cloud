# 2026-09-11 — Primary-source corrections pass (3 diagnosed items checked)

Scope: bounded fact-checking only, no Phase-3/theme/hypothesis-direction work touched.

## 1. Home Depot McPhail→Bastek attribution — already fixed, confirmed correct, no action needed

Checked `Study1_Corpus_and_Coding_DRAFT_2026-08-21.md`: the correction was actually applied on
2026-08-29 (changelog note at top of file, artifact 15 text, corpus table row 89) after being
re-confirmed four separate times without landing. Also checked
`Study1_Validation_Pilot_BLIND_CODING_WORKSHEET_2026-08-27_FULL_CORPUS.md` (the file flagged as
still having the error as of 2026-08-29) — a correction note dated 2026-09-01 is already present
there too (lines ~265-268), including the "Wall Street Journal" misattribution fix. **Both
documents are current and correct. No changes made.**

## 2. Insteel "freight" vs. "profit" — resolved

Read Motley Fool's transcript page (`fool.com/earnings/call-transcripts/2026/07/23/insteel...`)
directly via raw HTML fetch (curl + text search), deliberately bypassing any AI-mediated
summarization step, to settle what the page itself actually says rather than trusting another
AI's paraphrase of it. Result: the word is **"profit"** — appears twice independently on the
page (once in Motley Fool's own AI-generated "Takeaways" bullet, once in the actual
dialogue-transcript body: "...But when a profit cost $1.5 thousand to send to a destination now
$3 thousand somebody's gotta pay the bill.") Cross-checked GuruFocus's coverage of the same call
— it doesn't include this specific Q&A exchange, so no independent second source exists to
triangulate against.

**Important finding: the "freight" version was never actually source-verified either.** Traced
it back to `notes/2026-08-14-primary-source-verification-pass3-websearch-only.md`'s own
reasoning ("freight is almost certainly correct; profit doesn't make grammatical sense there")
— an AI inference, not a source read. Later notes (2026-08-18, 2026-08-28, 2026-08-29) kept
citing this as the presumptive correct answer without anyone re-deriving it, which is why it
read as more settled than it actually was.

**Verdict:** "profit" is what Motley Fool's page verbatim says, but it is almost certainly a
transcription artifact (the sentence isn't grammatical with "profit" as the subject of "cost...
to send to a destination"). Cannot be corrected to the true original wording without the actual
call audio, which isn't available to this project. **Recommendation, applied to the corpus
file:** don't quote this verbatim in the manuscript either way — paraphrase the substance (a
shipping-type cost roughly doubled, $1,500→$3,000, per CEO Woltz) and treat the exact word as
unverifiable rather than picking a side.

**Files changed:**
- `Study1_Corpus_and_Coding_DRAFT_2026-08-21.md` — artifact 14 entry (line ~164) and footnote ³
  (near line 94) updated with the resolution and recommendation; new changelog note added at top
  of file (line ~19).

## 3. SCOTUS/IEEPA legal-sequence primary-source verification — already done, confirmed correct

`notes/2026-08-14-scotus-ieepa-legal-sequence-confirmed.md` was flagged as secondary-source-only
(law firm summaries, Wharton Budget Model). Checked `notes/2026-08-29-mcphail-bastek-fix-and-new-developments-check.md`
§3: the actual slip opinion was already read directly and in full that night — the WebFetch
binary was saved locally and read via the Read tool (same PDF-workaround used for the Home Depot
transcript). Confirmed there: case name/docket (*Learning Resources, Inc. v. Trump*, No.
24-1287, consolidated with *Trump v. V.O.S. Selections, Inc.*, No. 25-250), decided Feb 20,
2026, holding that IEEPA does not authorize the tariffs, full disposition and vote breakdown, and
the Roberts quote — all independently confirmed against the primary opinion text, not just
secondary sources. **This matches what the 08-14 note describes; no discrepancy found. No
changes made.**

**Still genuinely open (not this pass's task, noted for completeness):** the *post-ruling
aftermath* — refunds process, CIT follow-on litigation, de minimis exemption status — remains
WebSearch-only per the 08-29 note, since the CRS Legal Sidebar PDF fetch was garbled and not
re-attempted via the save-then-Read workaround that worked for the opinion itself. Did not
attempt this tonight (out of this pass's specific scope, and it's a secondary/contextual point,
not load-bearing for the corpus itself) — worth a future session's five minutes given the
workaround is already proven to work twice on this exact project.

## Summary

- **Corrected:** Insteel quote wording flag (item 2) — resolved with an honest "unverifiable,
  recommend paraphrase" outcome rather than forcing a pick.
- **Confirmed already correct, no action needed:** Home Depot attribution (item 1, both files),
  SCOTUS legal sequence (item 3).
- **No new integrity issues found** beyond the pre-existing "freight was never actually verified"
  observation above, which is now documented so it doesn't get treated as settled again.
