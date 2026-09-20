# 2026-09-20 — Litigation recheck (all four dockets unchanged) + a substantive lead on the Campbell (1999)/(2007) opportunism-scale citation gap

## What this is (disclosure)

AI-assisted (Claude Code) autonomous overnight session. Two parts: (1) the
standing four-docket litigation recheck, same method as every prior night
in this thread; (2) since litigation had nothing new to report, spent the
rest of the session on the one open, non-blocked research thread flagged
in `notes/2026-09-10-citation-accuracy-pass.md` — Campbell (2007)'s exact
opportunism scale-item wording, which that pass left as "still open."

## 1. Litigation recheck — all four dockets fully unchanged since 09-19

Same four CourtListener docket URLs as every prior night, fetched via plain
`curl` with a browser User-Agent:

1. Section 301 forced-labor master docket — `https://www.courtlistener.com/docket/74219533/in-re-section-301-forced-labor-cases/`
2. Section 122 appeal, *State of Oregon v. Trump* (CAFC 26-1804/-1805) — `https://www.courtlistener.com/docket/73318531/state-of-oregon-v-trump/`
3. V.O.S. Selections (CAFC 26-1895) — `https://www.courtlistener.com/docket/73433096/vos-selections-inc-v-trump/`
4. Axle of Dearborn (CIT 1:25-cv-00091) — `https://www.courtlistener.com/docket/70287201/axle-of-dearborn-inc-v-department-of-commerce/`

All four returned HTTP 200, `x-cache: Miss from cloudfront`, and `date:`
headers of `Sun, 20 Sep 2026 05:07:39-42 GMT` — matching tonight's actual
fetch time within 3 seconds across all four, confirming fresh (not cached)
responses. Parsed with `beautifulsoup4` (installed fresh this session, as
usual for this container — still not preinstalled).

**Result: nothing changed on any of the four dockets since the 09-19 note.**

| Docket | Entries 09-19 | Entries tonight | Change |
|---|---|---|---|
| Section 301 | 52 | 52 | None |
| Section 122 | 104 | 104 | None |
| V.O.S. Selections | 26 | 26 | None |
| Axle of Dearborn | 79 | 79 | None |

Reread the last 1-2 entries on each docket directly (not just the count) —
text matches the 09-19 account verbatim in every case: Section 301's #51
(Economists' corporate disclosure statement) and #52 (plaintiffs' Sep 18
reply); Section 122's #103-104 (order granting the Economists' out-of-time
motion, then the corrected amicus brief); V.O.S. Selections' #25-26 (the
extension motion and the order granting it, due 10/05/2026); Axle of
Dearborn's #78-79 (the Aug 25 stay/reliquidation order pair). Checked all
four for a "Date Terminated" field — none found, same as every prior
night; all four remain open/active.

This is a genuinely uneventful check, which is an expected, fine outcome —
the 09-19 note already closed out the one live deadline this thread was
watching (Section 301's Sep 18 reply), and nothing has moved since. No
further nightly recheck is producing new information at the moment; worth
continuing on the existing cadence in case any of the pending items
(Section 122's 11/12/2026 government brief, V.O.S. Selections' 10/05/2026
response brief) develop, but there's nothing to report until one of those
dates approaches.

## 2. Non-litigation work: chased the Campbell (2007) opportunism-scale citation gap flagged 2026-09-10

Per `SUBMISSION_TRACKER.md` and `CLAUDE.md`, the standing blockers (CITI
Comprehensive-vs-Basic conflict, HSIRB turnaround, Jason's blind-coding
worksheet, Purchase Intention item count, banked scales, the two
Qualtrics-build decisions on Opportunism item 2 anchor direction and
attention-check flag-vs-terminate) are all still open and all still
external-dependency/Britton's-call items — not re-researched tonight, no
new public information on any of them. **One item was genuinely
actionable and non-blocked: `notes/2026-09-10-citation-accuracy-pass.md`
flagged Campbell (2007)'s exact opportunism scale-item wording as "the one
real remaining gap" from that pass, not yet pulled from the primary
source.** This is real literature verification, not a design/theory-chain
decision, so spent the rest of tonight's session on it.

### What was checked

Confirmed via WebSearch that the manuscript's current citation is real and
correctly formatted: **Campbell, M.C. (1999), "Perceptions of Price
Unfairness: Antecedents and Consequences," *Journal of Marketing
Research*, 36(2), 187–199** — DOI `10.1177/002224379903600204`, hosted at
`journals.sagepub.com` (the AMA/JMR's actual publisher). This is the
citation already used for the 2-item Perceived Price Fairness scale
(r=.84) in `Tariff_Manuscript_Working_Draft_2026-09-04.md` and
`notes/2026-08-04-full-instrument-assembly.md` item 6.

**Substantive finding, not yet a resolution — flagging for Britton, not
deciding:** multiple independent search summaries of this same 1999 JMR
paper (SAGE's own abstract page, a ScienceDirect-style aggregator, and
several citing-paper summaries) consistently describe **both of its two
studies as being about inferred motive** — Study 1 shows inferred motive
(and inferred relative profit) causally drives perceived price unfairness;
Study 2 shows firm reputation shapes that same inferred-motive judgment.
That is exactly the "opportunism/inferred motive" construct this project
has been sourcing from **Campbell's 2007 follow-up paper** instead
(`notes/2026-09-03-consensus-campbell-1999-opportunism-scale.md`), because
a 2026-09-03 Consensus.app pass reported it "could not find the exact item
wording" in the 1999 paper itself. **It's now plausible — not
confirmed — that the opportunism/inferred-motive items are actually in the
same 1999 JMR paper already cited for fairness (most likely in Study 2,
which is explicitly about firm-reputation → inferred-motive), which would
mean the whole 2-construct instrument could cite one paper instead of two,
and the "BEST AVAILABLE" 2007-sourced opportunism items could potentially
be upgraded to a same-paper verification.**

**This is not resolved.** Tried to reach the actual article text to check:
`journals.sagepub.com` (403, paywalled), the ResearchGate copy (403,
requires login), ProQuest's openview link (preview only — title/author/
citation, no body text), and SciSpace (returned no extractable content).
No copy of the full text was accessible without a paywall, consistent with
every prior session's experience with this paper. Per this repo's
no-paywalled-full-text rule, did not attempt to obtain or store the PDF
even if a route had been found — the goal here was reading to verify, not
retaining a copy.

**Incidental finding, unrelated to the current instrument but worth
flagging for future reference:** there is a *third*, separate Campbell
paper from the same year with an even more literally on-point title —
Campbell, M.C. (1999), "Why Did You Do That? The Important Role of
Inferred Motive in Perceptions of Price Fairness," *Journal of Product &
Brand Management*, 8(2), 145–152 (Emerald; received a "Highly Commended"
award per Emerald's own listing). This project does not currently cite
this paper anywhere, and I'm not recommending it be substituted in — just
flagging that there are now three distinct, real Campbell papers in play
(JMR 1999, JPBM 1999, JMR 2007) and any future scale-sourcing pass should
be careful not to conflate them by author+year alone.

### Recommendation (not a decision — Britton's call)

If library access is available before submission (the same McNeese/Ole
Miss access mentioned throughout this project's notes), pulling the actual
Campbell (1999) JMR article and checking Study 2's methods section for an
inferred-motive item would either (a) confirm the opportunism items are
in fact drawn from the same 1999 paper, letting the instrument cite one
source instead of two, or (b) confirm they're genuinely absent from 1999,
in which case the existing Campbell (2007)-sourced "BEST AVAILABLE" items
stand as they are. Either way this is a low-stakes, non-blocking
citation-hygiene question, not a new problem — the current instrument
already has usable item wording either way; this would only firm up the
attribution.

## Project-file drift check

`git log` for `TARIFF_PAPER/` still shows the last commit as the 09-19
litigation note (`88ac61c`); no non-litigation commits since the 09-11
Qualtrics-import addition. Nothing else in the project changed outside
tonight's work.

## For Britton

- **Litigation: nothing new.** All four dockets unchanged since 09-19 —
  Section 301's watched deadline stayed closed out, no other movement.
- **New, non-blocking lead on the opportunism scale:** the Campbell (1999)
  JMR paper already cited for the Fairness scale may itself contain the
  inferred-motive/opportunism items currently sourced from the 2007
  follow-up instead — not confirmed (paywalled), just flagged as worth a
  quick library check if you have a spare few minutes, not urgent.
- Everything else (CITI Comprehensive question, HSIRB turnaround, Jason's
  coding worksheet, Purchase Intention item count, banked scales, the two
  Qualtrics decisions) is unchanged and still waiting on you or Jason —
  not touched tonight, no new public information surfaced on any of them.
