# 2026-09-21 — Litigation recheck (all four dockets unchanged since 09-20) + a second, different-angle attempt on the Campbell (1999) opportunism-scale question (still blocked, now more definitively)

## What this is (disclosure)

AI-assisted (Claude Code) autonomous overnight session. Two parts, same
scope as every recent night: (1) the standing four-docket litigation
recheck; (2) since litigation had nothing new, one more focused attempt on
the Campbell (1999)/(2007) opportunism-scale citation-consolidation
question flagged in `notes/2026-09-20-litigation-recheck-and-campbell-
1999-source-check.md`, this time via API-based routes rather than
retrying the same paywalled pages.

## 1. Litigation recheck — all four dockets fully unchanged since 09-20

Same four CourtListener docket URLs as every prior night, fetched via
plain `curl` with a browser User-Agent:

1. Section 301 forced-labor master docket — `https://www.courtlistener.com/docket/74219533/in-re-section-301-forced-labor-cases/`
2. Section 122 appeal, *State of Oregon v. Trump* (CAFC 26-1804/-1805) — `https://www.courtlistener.com/docket/73318531/state-of-oregon-v-trump/`
3. V.O.S. Selections (CAFC 26-1895) — `https://www.courtlistener.com/docket/73433096/vos-selections-inc-v-trump/`
4. Axle of Dearborn (CIT 1:25-cv-00091) — `https://www.courtlistener.com/docket/70287201/axle-of-dearborn-inc-v-department-of-commerce/`

All four returned HTTP 200 with `x-cache: Miss from cloudfront` and `date:`
headers of `Mon, 21 Sep 2026 05:09:06-14 GMT` — matching tonight's actual
fetch time within 8 seconds across all four, confirming fresh (not
cached) responses. Parsed with `beautifulsoup4` (installed fresh this
session, as usual for this container).

**Result: nothing changed on any of the four dockets since the 09-20
note.**

| Docket | Entries 09-20 | Entries tonight | Change |
|---|---|---|---|
| Section 301 | 52 | 52 | None |
| Section 122 | 104 | 104 | None |
| V.O.S. Selections | 26 | 26 | None |
| Axle of Dearborn | 79 | 79 | None |

Reread the last 1-2 entries on each docket directly (not just the count) —
text matches the 09-19/09-20 account verbatim in every case: Section
301's #51 (Economists' corporate disclosure statement, Sep 14) and #52
(plaintiffs' Sep 18 reply, filed by Pratik Shah/Akin Gump); Section 122's
#103-104 (Sep 18 order granting the Economists' out-of-time motion, then
the corrected amicus brief); V.O.S. Selections' #25-26 (the extension
motion and the Sep 15 order granting it, response due 10/05/2026); Axle
of Dearborn's #78-79 (the Aug 25 stay/reliquidation order pair). Checked
all four for a "Date Terminated" field — none found on any; all four
remain open/active.

**Nothing new to report on litigation for a second consecutive night.**
The two pending dates worth watching remain Section 122's 11/12/2026
government brief deadline and V.O.S. Selections' 10/05/2026 response
brief deadline — both still weeks out, nothing to check yet.

## 2. Non-litigation work: a second, different-angle attempt at the Campbell (1999) opportunism-scale question

Per the 09-20 note, the open lead is whether Campbell (1999, *JMR*,
"Perceptions of Price Unfairness: Antecedents and Consequences," DOI
`10.1177/002224379903600204`) — already cited for the 2-item Fairness
scale — also contains the inferred-motive/opportunism items this project
currently sources from Campbell's 2007 follow-up instead. The 09-20
session tried SAGE, ResearchGate, ProQuest, and SciSpace and got blocked
by all four. Per tonight's task scope, tried a genuinely different route
this time — structured metadata APIs rather than retrying publisher/
aggregator pages — capped at one focused attempt as instructed.

**Semantic Scholar API** (`api.semanticscholar.org/graph/v1/paper/DOI:...`):
confirmed the paper record (title, 1999, sole author Margaret C. Campbell)
but the `abstract` field came back `null`, with an explicit publisher
notice: *"The following paper fields have been elided by the publisher:
{'abstract'}... subject to the license by the author or copyright owner."*
No full text available through this route, by design (Semantic Scholar
doesn't host publisher-restricted content).

**Unpaywall API** (`api.unpaywall.org/v2/10.1177/002224379903600204`) —
this is a more authoritative negative check than a search engine miss,
since Unpaywall's whole purpose is indexing legitimate open-access copies
across repositories: `"is_oa": false`, `"oa_status": "closed"`,
`"oa_locations": []`, `"best_oa_location": null`. There is no legitimate
open-access copy of this article anywhere Unpaywall indexes — not a
green-OA repository copy, not an author's institutional page, nothing.
This is a stronger, more direct confirmation than the four individual
403s/paywalls hit on 09-20: it's not that four specific sites blocked
access, it's that no open copy exists at all.

**WebSearch (Google-indexed snippets), two more targeted queries:**
searched for citing/secondary sources that might reproduce Study 2's
inferred-motive item wording verbatim (the same move that resolved
Purchase Intention via Grewal et al. 1998's Table 1 reproducing Dodds,
Monroe & Grewal 1991's items). Found nothing beyond what 09-20 already
had: SAGE's own abstract page, ResearchGate/ScienceDirect-style summaries
describing Study 1 (inferred motive/relative profit → unfairness) and
Study 2 (firm reputation → inferred motive), and the same Campbell (1999,
*JPBM*) "Why Did You Do That?" companion paper already flagged 09-20. No
citing paper surfaced that quotes Study 2's actual item wording in a
table the way Grewal et al. (1998) did for Dodds, Monroe & Grewal.

**Conclusion: still not resolved, and now more definitively closed off as
a route that doesn't work without direct library/database access.** Per
this repo's no-paywalled-full-text rule, no attempt was made to obtain or
retain a copy even where a route might exist behind a login. This
matches the 09-20 assessment exactly — nothing changed the substance of
the open question, only the confidence that it can't be resolved by
free/public means. Not spending further session time on this per
tonight's one-attempt cap; it remains a low-stakes, non-blocking
citation-hygiene lead, not a new problem, since the current
Campbell-(2007)-sourced "BEST AVAILABLE" opportunism items already stand
on their own regardless of the outcome.

## Project-file drift check

`git log` for `TARIFF_PAPER/` still shows the last commit as the 09-20
note; nothing else in the project changed outside tonight's work. No
files touched other than this note — `SUBMISSION_TRACKER.md` was not
modified, since nothing material resolved tonight (litigation
unchanged, citation question still open).

## For Britton

- **Litigation: nothing new, second night running.** All four dockets
  unchanged since 09-20. Next dates that could actually move something:
  Section 122's government brief (11/12/2026) and V.O.S. Selections'
  response brief (10/05/2026) — both still weeks out.
- **Campbell (1999) opportunism-scale lead: still open, but now
  confirmed via Unpaywall's OA index that there is no free/legitimate
  open copy anywhere** — this genuinely needs your library access (Ole
  Miss/McNeese, same as resolved the Purchase Intention scale via the
  1991 Dodds, Monroe & Grewal appendix) if you want to check Study 2's
  methods section for the inferred-motive items. Not urgent — the
  existing Campbell (2007)-sourced opportunism items are already usable
  as-is; this would only potentially let the instrument cite one paper
  instead of two.
- Everything else (CITI Comprehensive-vs-Basic conflict, HSIRB turnaround,
  Jason's blind-coding worksheet, Purchase Intention item count, banked
  scales, the two Qualtrics-build decisions) is unchanged — not touched
  tonight, no new public information on any of them.
