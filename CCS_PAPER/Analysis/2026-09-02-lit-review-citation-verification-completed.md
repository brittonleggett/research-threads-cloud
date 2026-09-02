# Lit-review citation verification — remaining pool cleared

2026-09-02. Third and final verification pass on `CCS_Lit_Review_Foundation.docx`'s reference list,
following the 08-31 (12 checked) and 09-01 (21 checked) sessions.

## Method

Extracted the docx via `python-docx` (391 non-empty paragraphs; reference list runs B1–B58). All 25
DOIs for the target B-numbers were queried directly against the Crossref REST API
(`api.crossref.org/works/{doi}`), checking full author roster (given + family names, in order),
title, journal/container-title, volume, issue, page range or article number, and year against what
the docx states — same method as the two prior passes.

## Result: all 25 remaining citations verified, zero discrepancies

The candidate pool handed off from 09-01's note (B5, B6, B7, B11, B14, B15, B16, B17, B18, B21, B22,
B23, B24, B25, B32, B34, B35, B37, B48, B50, B51, B52, B53, B54, B56) is **25 distinct B-numbers**, not
18 — see the count discrepancy below. All 25 checked:

| B# | Citation (short) | Result |
|---|---|---|
| B5 | Hansson, Anshelm, Fridahl & Haikola (2022), ERSS 90, 102606 | Exact match |
| B6 | Thomas, Pidgeon & Roberts (2018), ERSS 46, 1–9 | Exact match |
| B7 | Atkinson, Dankel & Romanak (2024), Frontiers in Marine Science 10, 1154543 | Exact match |
| B11 | Mabon, Kita & Xue (2017), Marine Policy 83, 243–251 | Exact match |
| B14 | Devine-Wright (2009), J. Community & Applied Social Psychology 19(6), 426–441 | Exact match |
| B15 | Devine-Wright & Batel (2017), Global Environmental Change 47, 110–120 | Exact match |
| B16 | Batel (2018), J. Environmental Policy & Planning 20(3), 356–369 | Exact match |
| B17 | Bergquist, Ansolabehere, Carley & Konisky (2020), ERSS 63, 101396 | Exact match |
| B18 | Cha (2020), ERSS 69, 101657 | Exact match |
| B21 | Sovacool & Dworkin (2015), Applied Energy 142, 435–444 | Exact match |
| B22 | Sovacool, Heffron, McCauley & Goldthau (2016), Nature Energy 1(5), 16024 | Exact match |
| B23 | Jenkins, Sovacool & McCauley (2018), Energy Policy 117, 66–74 | Exact match |
| B24 | McCauley, Ramasar, Heffron, Sovacool, Mebratu & Mundaca (2019), Applied Energy 233–234, 916–921 | Exact match |
| B25 | Walker & Day (2012), Energy Policy 49, 69–75 | Exact match |
| B32 | Hall, Lacey, Carr-Cornish & Dowd (2015), J. Cleaner Production 86, 301–310 | Exact match |
| B34 | Horowitz, Keeling, Lévesque, Rodon, Schott & Thériault (2018), Extractive Industries & Society 5(3), 404–414 | Exact match |
| B35 | Boutilier (2021), Extractive Industries & Society 8(2), 100743 | Exact match |
| B37 | Ó Maonaigh, Fitzgerald & Reilly (2025), ERSS 126, 104139 | Exact match |
| B48 | Whitmarsh, Xenias & Jones (2019), Palgrave Communications 5(1), 17 | Exact match |
| B50 | Pianta, Rinscheid & Weber (2021), Energy Policy 151, 112149 | Exact match |
| B51 | Demski, Butler, Parkhill, Spence & Pidgeon (2015), Global Environmental Change 34, 59–69 | Exact match |
| B52 | Liebe, Bartczak & Meyerhoff (2017), Energy Policy 107, 300–308 | Exact match |
| B53 | Liebe & Dobers (2020), Sustainability 12(19), 8084 | Exact match |
| B54 | Walker, Wiersma & Bailey (2014), ERSS 3, 46–54 | Exact match |
| B56 | Chewinski, Anders & Parkins (2023), Environmental Sociology 9(4), 477–489 | Exact match |

Every checked field — full author roster in exact order (including tricky repeat-surname cases like
the three McCauley/Sovacool-coauthored papers B22/B23/B24, and diacritics like Ó Maonaigh, Lévesque,
Thériault), title wording, journal name, volume/issue, page range or article number, and year —
matched Crossref's canonical metadata exactly. No paraphrasing, no wrong numbers, no non-existent
records. **Zero fabrications, zero numeric errors found in this batch.**

## Running total across all three sessions

- **58 of 58** distinct reference-list entries now checked (33 across 08-31/09-01, plus 25 tonight).
- Only exception: **B19**, which the docx itself already flags as "DOI uncertain" (no Crossref DOI
  registered) — not independently re-verified by DOI lookup in any session, though it wasn't flagged
  as fabricated either, just unconfirmable by this method.
- **Zero fabricated citations found across the entire reference list.**
- One real, correctable numbers error found in a prior session (McCauley et al. 2013 — volume "3"
  should be "32"; still needs Britton's fix in the docx, unchanged status).
- Three references carry the online-first-vs-print-year dating ambiguity (Cox et al., Bergquist,
  Awāsis) — still not errors, still needs Britton's house-style pick before manuscript-final.

## New finding: the docx's own "51 unique" summary line doesn't reconcile

The reference list runs **B1 through B58** (58 numbered entries, all distinct DOIs — confirmed no
repeated DOI anywhere in B1–B58). But the docx's own summary line states: "Total verified sources in
core set: 51 (B1–B58 excluding duplicates of Moffat & Zhang and Gough et al. across streams)."

This doesn't reconcile with the actual list. Moffat & Zhang and Gough et al. each appear as **exactly
one** numbered reference-list entry (B31 and B4 respectively) — they're simply cited multiple times
in-text across different sections of the paper, which is normal reuse, not a duplicated reference-list
entry. Excluding two citations from 58 would give 56, not 51, and no second B-number exists for either
source. As extracted, the reference list itself contains 58 unique, distinct entries, not 51.

**This does not appear to reflect any fabricated or duplicated source** — it looks like a bookkeeping/
arithmetic inconsistency in the docx's own front-matter summary line, not a citation-integrity problem.
Flagging for Britton to reconcile the summary line with the actual list (58, or figure out what the
intended exclusion actually was) rather than silently editing it.

## For Britton

1. **Lit-review citation verification is now complete**: all 58 reference-list entries checked across
   three sessions (08-31, 09-01, 09-02), zero fabrications found anywhere. B19 remains unconfirmable
   by DOI lookup (no registered DOI) but was never flagged as suspicious either — same status as
   before, just explicitly noted as the one item this method can't close.
2. **New, easy fix needed:** the docx's "Total verified sources in core set: 51" summary line doesn't
   match its own 58-entry list — reconcile the count (recommend just correcting it to 58, unless there
   was a real intended exclusion I'm not seeing).
3. Unchanged, still yours: the McCauley et al. (2013) volume/page fix, the three-instance date-
   convention pick, and Track A/B/C.
4. Routine checks (legis.la.gov codification lag, new HB79/Act 614/HB804 legal challenges) were not
   re-run tonight since this session focused on closing out the citation pool — worth a re-check next
   time this project comes up in rotation if it's been a while.
