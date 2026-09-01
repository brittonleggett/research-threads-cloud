# 2026-09-01 — Literature citation verification pass (AI-run, under the standing 2026-08-16 Phase 3 exception)

## First: a discrepancy in this session's own briefing, stated plainly

This session's task briefing referred to two notes that do not exist anywhere in this repository:
a `2026-08-30` literature-verification note said to cover "Shjarback and ALPR-evaluation
citations," and a `2026-08-31-vignette-wording-options-readability-and-confound.md` note said to
contain scored wording alternatives for the readability gap and Condition B confound the
2026-08-27 face-validity review flagged. I checked this worktree's `notes/` folder, every other
worktree branch attached to this repo (`main`, and four sibling `worktree-agent-*` branches), and
one additional sibling worktree checkout on disk not yet on any branch I could enumerate — none of
them contain a file dated after `2026-08-27`. The real, actual newest files as of this session are
the two dated `2026-08-27`: `notes/2026-08-27-nhan-helfers-retry-and-study2-instrument-assembly.md`
and `notes/2026-08-27-webfetch-retry-and-study2-vignette-face-validity-review.md`. I am not
fabricating the content of the 08-30/08-31 files described in the briefing, and I did not attempt
to reconstruct or "helpfully" guess what they might have said — I'm flagging this mismatch so
Britton and the next session know the described state doesn't match the repo's actual git history,
rather than silently treating a hallucinated status update as ground truth. Everything below builds
on the actual `2026-08-27` state.

One consequence: the second `2026-08-27` note (webfetch-retry-and-study2-vignette-face-validity-
review.md) already raised the Flesch-Kincaid readability gap and the Condition B secrecy/
government-incompetence confound as open findings for Britton — this is very likely what the
briefing's phantom "08-31" note was referring to, just under the wrong date and wrong framing
("scored wording alternatives," which was never actually drafted; the real note only raises the
concerns and recommends fixes, it doesn't score options). Per the task's own instruction, I did not
touch vignette wording, did not score alternatives, and did not decide anything about it — that
review's status is unchanged: still open, still Britton's call.

## What this pass did

WebFetch and outbound network access were confirmed working tonight (a real change from the 17+
consecutive `EGRESS_BLOCKED` sessions recorded through 2026-08-27) — tested against a Wikipedia
control page first, which returned real content cleanly. Given a fully verified but growing
literature stack behind this paper's theory chain, and several items explicitly flagged across
prior sessions as "WebSearch-triangulated, not direct-fetch-verified, spot-check before
submission," this pass's chosen next step was to actually spot-check them now that fetching works,
rather than repeat the vignette review or touch any design call.

**Method:** rather than fighting SAGE's and ScienceDirect's own bot-blocking (both returned clean
HTTP 403s tonight, confirming the 2026-08-27 diagnosis that this is publisher-side bot detection,
not a network-egress problem — the network path itself worked fine, e.g. the Nhan & Helfers DOI
resolved and redirected cleanly before SAGE's own page rejected the request), I used open
bibliographic-metadata APIs instead: the Crossref REST API (`api.crossref.org`), Semantic Scholar's
API, and OpenAlex, fetched both via the WebFetch tool and, for the highest-stakes finding, via a
direct `curl` pull of the raw, un-summarized JSON (to eliminate any risk of the WebFetch tool's
internal summarization model inventing a field that wasn't really there). This is legitimate,
citable publisher-registered metadata, not paywalled full text — no copyright concern, nothing
that needs to stay out of this public repo.

## Findings, citation by citation

**1. Nhan & Helfers (2026) — the researcher-independence question, genuinely resolved (partially),
after five prior sessions found nothing.** Crossref's own funder metadata for DOI
10.1177/0032258X251349633 lists **"Flock Safety" as a funder, with award number 23854** — real,
publisher-submitted metadata (the funder field is what SAGE itself registers with Crossref at DOI
creation), confirmed twice independently: once via WebFetch with an explicit instruction not to
guess if the field was absent, and once via a raw `curl` JSON pull with no LLM summarization in the
loop at all, specifically to guard against the possibility that the first result was a WebFetch
hallucination. Both agree. Cross-checked against OpenAlex's raw JSON for the same DOI, which has no
`grants` field for this record at all — a data-coverage gap on OpenAlex's side (confirmed by
checking OpenAlex's raw JSON directly, not an artifact of asking two different questions), not a
contradiction of the Crossref record. **What this does and doesn't establish:** it is real,
structured evidence that Flock Safety funded this research (a specific award number, not just "some
relationship") — a stronger and more precise finding than any prior session reached. It is *not*
the article's own printed disclosure-statement wording, which remains unread (SAGE's page itself
is bot-blocked to automated fetch, confirmed again tonight). I updated the funding/independence
paragraph in `Introduction_and_Theory_DRAFT_2026-08-16.md` to state this plainly, with the same
"partially verified, not fully" framing here. Full bibliographic precision also added: *The Police
Journal: Theory, Practice and Principles*, 99(1), 160–179; published online 2025-06-04, print issue
2026-03 (confirms the draft's "(2026)" citation year matches the print issue).

**2. Przeszlowski & Guerette (2025) — real title and DOI now confirmed**, resolving the explicit
"spot-check before submission" flag from the 2026-08-24/08-25 sessions. Actual title: "Public
Perceptions on Police Use of Information Technologies: Findings from a Randomized Vignette
Experiment," *Journal of Criminal Justice*, 96, article 102336, DOI
10.1016/j.jcrimjus.2024.102336 (Crossref). The prior WebSearch-triangulated attribution (author
names, journal, sample size, RTCC-focus) all check out against the real record — no correction
needed there, just an upgrade from triangulated to metadata-confirmed confidence, and the actual
DOI/article number the draft was missing.

**3. Li (2024)** — real title confirmed: "Institutional Trustworthiness on Public Attitudes toward
Facial Recognition Technology: Evidence from U.S. Policing," *Government Information Quarterly*,
41(3), 101941, DOI 10.1016/j.giq.2024.101941. The draft previously cited this by author/year only
with no title or DOI at all; added.

**4. Bradford, Yesberg, Jackson, & Dawson (2020)** — real title confirmed: "Live Facial
Recognition: Trust and Legitimacy as Predictors of Public Support for Police Use of New
Technology," *The British Journal of Criminology*, DOI 10.1093/bjc/azaa032. Same gap as Li — the
draft previously named authors/year and method only, no journal name or DOI; added.

**5 & 6. Both Monahan (2026) papers** — real titles/DOIs confirmed via a single Crossref query that
returned both: "Grounding the Flock: Confronting Police Surveillance of Mobilities" (*Mobile Media
& Communication*, DOI 10.1177/20501579261453519) and "Flock on Campus: University Police as
Appendages of a National Policing Apparatus" (*Policing and Society*, 34, 1–23, DOI
10.1080/10439463.2026.2702635). The draft's existing description of which paper covers which theme
(communicative-network/discriminatory-policing vs. campus-police/national-apparatus) matches the
real titles correctly — no swap, just added precision.

**7. Schiff, Schiff, Adams, McCrain, & Mourtgos (2025)** — confirmed real title, volume/issue/pages
(*Public Administration Review*, 85(2), 451–467), and DOI 10.1111/puar.13754. Notable: Crossref
shows this article published online 2023-10-26 but in the March 2025 print issue — the draft's
"(2025)" citation year is the correct one (matches print-issue convention), not an error, but worth
knowing the online-first date exists in case a reviewer checks it.

**8. Reisig & Lloyd (2009) and Sunshine & Tyler (2003)** — both confirmed real via Crossref, exact
volume/page match what the 2026-08-16 scale-sourcing note already had (Sunshine & Tyler: *Law &
Society Review*, 37(3), 513–547, DOI 10.1111/1540-5893.3703002 — DOI newly added). One factual note
on Reisig & Lloyd (2009), *Police Quarterly*, 12(1), 42–62, DOI 10.1177/1098611108327311: the
sample is **Jamaican high school students** (n=289), not a U.S. general-population sample — this
doesn't make the citation wrong (procedural-justice/legitimacy theory is explicitly cross-national
in scope, and the paper is cited correctly for the theoretical point it supports), but it's worth
Britton knowing precisely what population this specific supporting citation draws on, in case he'd
rather anchor that particular sentence on a U.S.-sample study instead.

**9. Nissenbaum (2010), Tyler (1990), Tyler & Huo (2002)** — all three confirmed as real published
books via Crossref (Nissenbaum's *Privacy in Context* has its own DOI, 10.1515/9780804772891,
Stanford University Press, monograph type; Tyler 1990 and Tyler & Huo 2002 confirmed via
book-review records citing exact publisher/page-count details matching the draft's own citations).
No further action needed on these — they were never actually in doubt, just formally unconfirmed.

## What remains unverified or open (stated plainly)

- **Nhan & Helfers's exact disclosure-statement wording** is still unread. The funder-metadata
  finding above is real and citable, but it is not a substitute for the article's own printed
  paragraph. SAGE's page is bot-blocked to every automated method tried across six sessions now
  (WebFetch, direct curl-equivalent fetch via WebFetch, a SAGE-affiliated mirror). Recommend closing
  this to further automated attempts, same as 2026-08-27's own recommendation — only a library pull
  or manual read closes the remaining gap.
- **The IJ ALPR-misuse-count figure (now 24, was "at least 21")** is sourced via a secondary
  article's direct quote of the Institute for Justice's tally, not IJ's own page (also bot-blocked,
  403). It's explicitly a running tally, so treat any number cited here as dated (mid-July 2026),
  not fixed — worth a fresh check closer to submission.
- **The vignette-wording readability gap and Condition B confound** flagged 2026-08-27 remain
  completely untouched by this session, as instructed. No scoring, no rewrite, no recommendation
  beyond what 2026-08-27 already said. Still open, still Britton's.
- **The three standing design calls** (archival-moderator feasibility, single-manipulation vs.
  factorial, PLS-SEM vs. Hayes-PROCESS) are unchanged — not addressed tonight, per the task's
  explicit instruction.
- **Shjarback and any other "ALPR-evaluation" citations** the briefing mentioned as covered
  2026-08-30 were not found or verified tonight, because — per the discrepancy noted at the top —
  no such prior pass exists in this repo to build on. If Britton knows of a real Shjarback ALPR
  citation he wants checked, that's a concrete, easy next step for a future session; I did not
  invent one to fill the gap.
- No locked theme, hypothesis, moderator, or the primary theory chain itself was touched tonight —
  everything above is citation-precision and one funding-relationship fact, not a design change.

## Files touched

- `Introduction_and_Theory_DRAFT_2026-08-16.md` — nine citation-precision edits (see above) plus
  one new dated log entry (item 9) at the bottom, following this file's own established convention
  of a running per-session update log.
- This note (new).

## Sources used (all open, non-paywalled metadata — nothing paywalled was pulled or stored)

Crossref REST API (`api.crossref.org`), Semantic Scholar API (`api.semanticscholar.org`), OpenAlex
API (`api.openalex.org`), plus a small number of WebSearch queries and one direct fetch of a news
aggregator article (theautowire.com) quoting the Institute for Justice's tally directly.
