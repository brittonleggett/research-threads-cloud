# 2026-08-30 — Act 614 enrolled text verified against ORIGINAL: $250K/$500K/$1M repeal language is identical, no floor amendments changed it

## 0. Housekeeping: WebFetch/egress appears unblocked tonight

Control test against `en.wikipedia.org` succeeded (full normal page summary returned), and direct
`curl` downloads of PDFs from `legis.la.gov` also succeeded without proxy errors. This is the
first working WebFetch/direct-fetch session since the block that started 2026-08-13 (last
confirmed-blocked check was 08-20). Not the main finding of the night, but worth flagging since
it's what made tonight's verification possible at all — if this holds up in future sessions, a
lot of the "WebSearch-confidence, not primary-source" caveats scattered through July/August notes
could be upgraded.

## 1. Found all four legislative-history versions of HB79/Act 614 via BillInfo

`https://www.legis.la.gov/legis/BillInfo.aspx?i=249698` lists every document version for the
bill. Direct-fetched all four as PDFs via `curl` (bypassing WebFetch's own PDF handling, which
flattens struck-through/underlined redline formatting into indistinguishable plain text — see
§3):

| Version | URL | HTTP | Size |
|---|---|---|---|
| Original (HLS 26RS-572) | `ViewDocument.aspx?d=1436661` | 200 | 44,135 B |
| Engrossed (HLS 26RS-572 ENGROSSED) | `ViewDocument.aspx?d=1466012` | 200 | 41,075 B |
| Enrolled | `ViewDocument.aspx?d=1478869` | 200 | 44,441 B |
| Act No. 614 | `ViewDocument.aspx?d=1480515` | 200 | 47,843 B |

All four confirmed via their own header stamps (ORIGINAL / ENGROSSED / ENROLLED / ACT No. 614)
and all four carry the identical "AN ACT / To amend and reenact R.S. 30:1109(B) through (F) and
to repeal R.S. 30:1109(G)..." title.

**Act 614 confirmed at primary-source confidence** (upgrading 08-20's WebSearch/LegiScan-only
citation): House Bill 79, 2026 Regular Session, became **Act No. 614**, effective **August 1,
2026**. Sponsors at enrollment: Reps. Robby Carter, Mike Johnson, McCormick, and Owen (Original
was Carter alone — McCormick/Johnson/Owen were added as co-authors by engrossment, consistent
with normal House practice, not a substantive change).

## 2. Byte-level diff of the operative text (Original vs. Engrossed vs. Enrolled vs. Act 614)

Extracted text from all four PDFs (`pdfplumber`) and diffed them page-content-normalized (header
stamps and page-break line numbers vary; substance doesn't). Result: **Section 1's full
amend-and-reenact text and Section 2's repeal of R.S. 30:1109(G) are byte-identical across all
four versions.** The only differences anywhere in the four documents are: (a) the header stamp
(ORIGINAL/ENGROSSED/ENROLLED/ACT No. 614), (b) the sponsor byline (Carter alone → four
co-authors), (c) pagination artifacts from re-typesetting, and (d) the Original/Engrossed
versions carry the House Legislative Services digest on their final page, which the
Enrolled/Act versions replace with the Speaker/President/Governor signature block. **No
substantive text differs anywhere.**

## 3. Visual redline confirmation: the full $250K/$500K/$1M repeal is intact, unchanged, in Act 614

This is the part that needed real care. Plain-text extraction (and WebFetch's own PDF
summarization) **cannot distinguish struck-through (deleted) from underlined (added) text** —
both render as flat, undecorated text, so a naive read of the extracted text makes reenacted
language that repeals a paragraph look identical to language that merely retypes it unchanged.
An initial pass tonight using PDF glyph-position/curve heuristics to infer strikethrough
placement produced a wrong answer (it suggested the dollar figures might be unmarked/retained) —
flagging this here as a dead-end method, not a finding, since it was corrected by the next step
before anything wrong got written down.

**Resolved by rendering both PDFs to page images (`pdftoppm`) and reading the actual redline
visually**, which Louisiana bills mark unambiguously per their own coding key ("Words in struck
through type are deletions from existing law; words underscored are additions"):

- **Original bill, page 1–2:** The entirety of R.S. 30:1109(B)(1) and (B)(2) — the full civil-
  liability-cap paragraph, including all three dollar figures ("two hundred fifty thousand
  dollars per person," "five hundred thousand dollars per person," "one million dollars per
  person") and the wrongful-death/permanent-injury carve-out list — is struck through, start to
  finish, with **no replacement text inserted**. Confirms the 08-28 note's finding exactly.
- **Enrolled/Act 614, same pages:** **Pixel-for-pixel identical strikethrough pattern.** Same
  paragraph, same start point, same end point, same three dollar figures struck, same absence of
  any replacement language. Compared side-by-side (rendered images of both), the redline
  markup is indistinguishable between the two versions.
- Subsections (C) through (G) also show identical, matching redline in both versions: a minor
  wording fix in (C) ("shall establish or create" → "establishes or creates" — a tense/clarity
  edit, not substantive), and a one-letter-per-subsection shift ((C)→(B)'s new content, (D)→(C),
  (E)→(D), (F)→(E), (G)→(F)) that fills the slot vacated by (B)'s emptied cap language, with
  Section 2 formally repealing the now-unused terminal letter (G). This shift is mechanical
  housekeeping consistent with a clean full repeal, not a hidden substantive change — and it,
  too, is identical between Original and Enrolled/Act 614.

**Conclusion: no floor amendment changed, narrowed, restored, or added back any part of the
damages-cap repeal between introduction and final enactment.** The full repeal of the
$250,000/$500,000/$1,000,000 per-person caps that the 08-28 note found in the ORIGINAL bill is
**confirmed identically present in the enrolled Act 614 text actually signed into law**. This
closes the open item flagged at the end of the 08-28 note and in the 08-20 note.

**Sources (primary, directly fetched and rendered):**
- [HB79 Original, legis.la.gov](https://www.legis.la.gov/legis/ViewDocument.aspx?d=1436661)
- [HB79 Engrossed, legis.la.gov](https://www.legis.la.gov/legis/ViewDocument.aspx?d=1466012)
- [HB79 Enrolled, legis.la.gov](https://www.legis.la.gov/legis/ViewDocument.aspx?d=1478869)
- [Act No. 614, legis.la.gov](https://www.legis.la.gov/legis/ViewDocument.aspx?d=1480515)
- [HB79 BillInfo page, legis.la.gov](https://www.legis.la.gov/legis/BillInfo.aspx?i=249698)

## 4. One loose end, not a concern for the manuscript but worth flagging for whoever touches this next

Legis.la.gov's own **codified "current law" page** for R.S. 30:1109
(`https://legis.la.gov/Legis/Law.aspx?d=670795`) still shows the **pre-Act-614 text** as of
tonight (Aug 30, 2026) — full $250K/$500K/$1M caps still listed, subsection (G) still present,
amendment history line stops at "Acts 2025, No. 458" with no mention of Act 614. This is almost
certainly just the state's routine codification lag (Act 614 took effect less than a month ago,
Aug 1, 2026) rather than any indication Act 614 didn't take effect — the enrolled/Act document
itself is unambiguous and is the controlling primary source. But **anyone citing "current R.S.
30:1109" by fetching that Law.aspx page today would get stale text** — cite the Act 614 document
above instead, or re-check that Law.aspx page later in the fall once the state's codification
catches up.

## What's still open / blocked on Britton

- Track A/B/C reframing choice untouched, per standing instruction — not addressed here.
- Phase 3 theme review remains human-only for this paper.
- The manuscript can now cite HB79/Act 614's repeal of the $250K/$500K/$1M noneconomic-damages
  caps at full manuscript-final precision — this was the last outstanding verification step from
  08-28, and it's now closed.
