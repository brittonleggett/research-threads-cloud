# 2026-09-22 — Litigation recheck (real movement on Section 301 and Section 122, non-substantive) + a literature-currency sweep surfaces a 2025 JCR paper by the same Campbell whose scales this project already uses

## What this is (disclosure)

AI-assisted (Claude Code) autonomous overnight session. Two parts: (1) the
standing four-docket litigation recheck; (2) since the Campbell (1999)
opportunism-scale lead is genuinely closed per the 09-21 note (not
reopened here), this session's second half was a literature-currency
sweep for new 2025-2026 tariff-messaging/consumer-behavior work relevant
to this project's theory, plus a public-information check on
`SUBMISSION_TRACKER.md`'s standing open items (CITI module, HSIRB
turnaround).

## 1. Litigation recheck — real docket movement tonight, but nothing that changes either pending deadline

Same four CourtListener docket URLs as every prior night, fetched via
plain `curl` with a browser User-Agent:

1. Section 301 forced-labor master docket — `https://www.courtlistener.com/docket/74219533/in-re-section-301-forced-labor-cases/`
2. Section 122 appeal, *State of Oregon v. Trump* (CAFC 26-1804/-1805) — `https://www.courtlistener.com/docket/73318531/state-of-oregon-v-trump/`
3. V.O.S. Selections (CAFC 26-1895) — `https://www.courtlistener.com/docket/73433096/vos-selections-inc-v-trump/`
4. Axle of Dearborn (CIT 1:25-cv-00091) — `https://www.courtlistener.com/docket/70287201/axle-of-dearborn-inc-v-department-of-commerce/`

All four returned HTTP 200 with `x-cache: Miss from cloudfront` and
`date:` headers of `Tue, 22 Sep 2026 05:08:0[2-5] GMT` — matching
tonight's actual fetch time within 3 seconds across all four, confirming
fresh (not cached) responses.

| Docket | Entries 09-21 | Entries tonight | Change |
|---|---|---|---|
| Section 301 | 52 | **53** | +1 (new) |
| Section 122 | 104 | **106** | +2 (both backfilled, see below) |
| V.O.S. Selections | 26 | 26 | None |
| Axle of Dearborn | 79 | 79 | None |

**Section 301 — one genuinely new entry.** Entry #53, filed and entered
09/21/2026: a **Joint Appendix** (5 volumes, Tabs 1-89) filed by Pratik A.
Shah (Akin Gump) on behalf of All Plaintiffs — the standard record
compilation that follows briefing (entry #52 was the plaintiffs' Sep 18
reply). This is normal case progression, not a ruling or a new deadline;
no plaintiff/government deadline is created or changed by a Joint
Appendix filing itself.

**Section 122 — two entries, but both are backfill of already-known
Sep 18 activity, not new events.** Entries #105-106: #105 is a
"CORRECTED AMICUS CURIAE BRIEF" by Cato Institute/Ilya Somin (marked
"PENDING COMPLIANCE REVIEW"), #106 is a same-day "Notice of Correction"
to #105 — both dated/entered 09/18/2026, i.e. the same day as the
Economists' corrected amicus brief (entry #104, already known from
09-19/09-21) but not yet reflected in CourtListener's docket mirror as of
last night's fetch. Same sync-lag pattern documented repeatedly in this
project's litigation-recheck history (Section 301's Sep 4 filing not
mirrored until Sep 10; V.O.S. Selections' Sep 15 order not mirrored until
09-17). **The government's own brief deadline is unaffected and confirmed
still 11/12/2026** — checked directly in the docket text (`"...to file
brief...11/12/2026...By: Per Curiam...[Entered: 09/14/2026 04:45 PM]"`),
not just inferred from the absence of a new order.

**V.O.S. Selections and Axle of Dearborn — fully unchanged.** Reread
entries #25-26 (V.O.S.) and #78-79 (Axle) directly; text matches the
09-21 account verbatim in every case. V.O.S. Selections' response brief
remains due 10/05/2026 (now under two weeks out).

Checked all four dockets for a "Date Terminated" field or any
termination-related case-status text (searched case-insensitively across
each full page) — none found on any; all four remain open/active.

**Bottom line: nothing that changes the messaging-framing basis this
project relies on.** The Section 301 Joint Appendix and the Section 122
backfilled amicus-correction entries are routine procedural filings, not
rulings. The two dates worth actually watching are unchanged: **V.O.S.
Selections' 10/05/2026 response brief (now ~2 weeks out)** and
**Section 122's 11/12/2026 government brief (still ~7 weeks out)**.

## 2. Literature-currency sweep — one notable find

Searched for 2025-2026 tariff-messaging/consumer-behavior and
price-fairness/attribution work relevant to this project's H1a/H1b/H2a/H2b
theory chain (fairness and opportunism/inferred-motive as mediators).

**Campbell, Pomerance, & Percival Carter (2025), "Painful Prices: The
Moral Harm Model of Price Fairness,"** *Journal of Consumer Research*,
53(3), 444-466, DOI `10.1093/jcr/ucaf045` (published online July 9, 2025).
Confirmed directly via the journal's own abstract page
(academic.oup.com/jcr) — real citation, not inferred. First author is
**the same Margaret C. Campbell** already cited in this project's
instrument for the Fairness scale (Campbell 1999) and, per the ongoing
opportunism-scale lead, connected to the 2007 follow-up too. This 2025
paper proposes a general conceptual model of perceived price fairness as
a *moral judgment* arising from consumers' inferred potential harm from a
price — with **inferred firm self-defense motive as an explicit
moderator**, and political orientation as another. Per the abstract: "The
authors develop a conceptual model of PPF as moral judgments and propose
that these moral PPF arise from consumer inferences of potential harm
from a price," tested across eight studies. Abstract quoted directly, not
paraphrased into a stronger claim than it makes; full text not fetched
(paywalled at Oxford Academic, per this repo's no-paywalled-full-text
rule).

**Why this matters for this project:** it's a live, 2025 theoretical
update from the *same author* whose 1999 instrument is already load-
bearing here (Fairness scale, H1a/H1b), and it deals with exactly this
project's mechanism — inferred motive as a driver/moderator of price-
fairness judgments in a context (tariffs) that plausibly maps onto her
"potential harm" and "self-defense motive" framing. This is a **citation
opportunity for the Introduction/Theory section**, not a scale-sourcing
fix — it doesn't resolve the still-open Campbell 1999 vs. 2007
opportunism-item question from prior nights (not reopened here, per
task scope), but it is new, directly on-topic theory Britton likely wants
to at least be aware of and consider citing, especially since it comes
from the same scholar. **Recommend Britton skim the abstract/intro (or
pull it via library access) before the final Introduction/Theory pass.**

One adjacent, unconfirmed lead, flagged but not verified: a Columbia
Business School "faculty awards" page describes an active project titled
**"How Tariff Price Presentation Affects Consumer Responses, Fairness
Perceptions, and Attitudes toward Firms and Government"** — directly
on-topic (tariff price presentation, fairness perceptions, firm/
government blame attribution) but the page (business.columbia.edu) gave
an HTTP 403 on direct fetch and a follow-up search did not surface
author names, a journal, or a paper/working-paper link — only the
project-description text from Google's indexed snippet. **Not confirmed
as a citable paper, just a project description; flagging as an adjacent
research thread to watch, not something to cite.** No further attempt
made to access it past the 403.

A broader search for a "novelty defense" framing specifically (as named
in tonight's task) surfaced attribution-theory literature on price-
increase fairness generally (dual entitlement, locus-of-causality,
novelty-of-pricing-method effects on attribution) but nothing that uses
that specific term or maps cleanly onto it — no claim made that a
"novelty defense" literature exists under that name; this remains an
open framing question for Britton's own theory-building, not something
this search resolved.

## 3. SUBMISSION_TRACKER.md open items — public-information check

Checked the two items most likely to have new *public* information
(CITI module requirement, HSIRB turnaround) without touching Britton's
private accounts, per tonight's scope.

**CITI Comprehensive-vs-Basic conflict: re-confirmed unchanged, third
direct fetch of the same policy page.** Fetched
`https://www.mcneese.edu/policy/human-subjects-institutional-review-board-hsirb-policy/`
directly tonight. Exact text, unchanged from the 09-09/09-10 fetches:
*"All researchers involved in research with human subjects must complete
a CITI Program training module about human subjects protection, either
'Biomedical Comprehensive' or 'Social/Behavior/Educational
Comprehensive'... certificate of completion to submit with an HSIRB
application."* One new data point: the page's own revision history now
reads **"Enacted February 28, 2023; Revised July 28, 2025; February 19,
2026"** — meaning it was revised as recently as this past February,
several months *after* it started requiring the Comprehensive module
language quoted in this tracker's earlier notes — i.e., this isn't
stale/outdated policy language accidentally left over from an old
version; it's been through a revision cycle since and still says
Comprehensive. That's a small additional point in favor of taking the
policy text at face value rather than assuming it's lagging practice.
Still not a substitute for Britton confirming directly with the IRB
office what was actually accepted for the already-submitted application.

**HSIRB turnaround time: still not publicly findable, confirmed again.**
The policy page states the detailed review process lives in a
"procedural manual" hosted on the **Graduate School SharePoint** — i.e.,
an internal, non-public document, not something a web fetch can reach.
`mcneese.edu/hsirb/irb_application_guidelines/` (referenced in a search
result) returned HTTP 404 on direct fetch; `mcneese.edu/hsirb/` also
404s. No public source states a typical turnaround time. This confirms,
rather than newly discovers, what 09-09/09-10 already concluded: **this
genuinely requires a direct ask to the IRB office**, not something
further searching will resolve.

The other standing open items (Jason's blind-coding worksheet, Purchase
Intention item count, banked scales, the two Qualtrics-build decisions)
depend on Britton's own decisions or other people's private status, not
public information — not touched tonight, consistent with task scope.

## Project-file drift check

`git log` for `TARIFF_PAPER/` still shows the 09-21 note as the last
commit; nothing else in the project changed outside tonight's work. No
files touched other than this note — `SUBMISSION_TRACKER.md` was not
modified, since nothing here rises to a tracked status change (the
Section 301/122 docket entries are routine procedural filings, not
rulings that change a deadline or outcome the tracker records; the CITI
and HSIRB-turnaround findings are re-confirmations, not new information).

## For Britton

- **Litigation: some new docket activity tonight, but nothing that
  changes the two dates that actually matter.** Section 301 picked up a
  Joint Appendix filing (routine post-briefing record compilation, not a
  ruling); Section 122 picked up two entries that were really just a
  delayed docket-mirror sync of Sep 18 activity already known. V.O.S.
  Selections' response brief (10/05/2026) is now under two weeks out;
  Section 122's government brief (11/12/2026) is still about seven weeks
  out. All four dockets remain open, no terminations.
- **New literature worth a look: Campbell, Pomerance, & Percival Carter
  (2025), "Painful Prices: The Moral Harm Model of Price Fairness,"**
  *JCR* 53(3), 444-466. Same Margaret Campbell already cited for this
  project's Fairness scale — a 2025 conceptual update on inferred-motive/
  moral-harm price fairness judgments, directly relevant to this
  project's H1a/H1b/H2a/H2b framing. Worth a skim (or a library pull)
  before the final Introduction/Theory pass; this doesn't resolve the
  still-open Campbell 1999-vs-2007 opportunism-item sourcing question,
  it's a separate, newer paper.
- One unconfirmed, adjacent lead: a Columbia Business School project
  description (title only, no accessible authors/venue found) on tariff
  price-presentation and fairness/blame-attribution — directly on-topic
  as a research area to watch, but not verified enough to cite.
- **CITI and HSIRB-turnaround questions: both re-confirmed unchanged**,
  no new public information found beyond one detail — McNeese's HSIRB
  policy page has been revised as recently as Feb 2026 and still
  requires the Comprehensive module, so it's not stale language. HSIRB's
  actual turnaround time is genuinely not published anywhere public (it
  lives in an internal SharePoint manual) — still needs a direct ask to
  the IRB office, same conclusion as every prior check.
- Everything else (Jason's blind-coding worksheet, Purchase Intention
  item count, banked scales, the two Qualtrics-build decisions) is
  unchanged — not touched tonight, no new public information on any of
  them (these depend on private/personal status, not public sources).
