# Overnight Summary — 2026-09-19

## What tonight did

Ran five research passes in parallel (each confined to its own directory; each commit landed
and pushed as soon as that pass's completion report arrived, same process as 09-17/09-18).
Rotated toward TARIFF_PAPER (always top priority, plus the specific same-day-or-next-morning
Section 301 recheck flagged by last night's note) and the three projects not touched since
09-17 — DATA_CENTER_PAPER, GAMBLING_SOCIAL_COST_PAPER, MEAT_SUPPLY_CHAIN_PAPER — plus scouting.
CCS_PAPER, FLOCK_CAMERAS_PAPER, and SPACEX_LOUISIANA_PAPER weren't touched tonight (all three
got full passes 09-18).

**TARIFF_PAPER** — closed out the standing Section 301 deadline question from last night. The
government reply due 09-18 was in fact filed on time (docket entry #52, confirmed via a fresh
direct fetch dated 2026-09-19). **One correction to the last four nights' notes and tracker**:
that entry is a *plaintiffs'* reply (filed by Pratik A. Shah/Akin Gump on behalf of All
Plaintiffs), not the government's — standard motion practice means the movant replies to the
government's response, and this got mislabeled starting 09-15. The deadline-met outcome is
unaffected; only the party label was wrong, and it's now corrected in both the note and
`SUBMISSION_TRACKER.md` without altering historical bullets. Section 122 picked up two new,
non-substantive entries (102→104, an already-known amicus "file out of time" motion resolved);
V.O.S. Selections and Axle of Dearborn unchanged. Detail:
`TARIFF_PAPER/notes/2026-09-19-litigation-recheck.md`.

**DATA_CENTER_PAPER** — NAACP v. X.AI Corp. still shows no ruling as of a Sept 18 RECAP refresh
(the freshest "no ruling yet" reading this project has recorded on this case). LPSC Docket
U-37882's Sept 16 session agenda (read directly, PDF-extracted) confirms the "not ripe" item
flagged 09-17 was a separate Attorneys'-Eyes-Only confidentiality settlement among Entergy,
Alliance for Affordable Energy, and Union of Concerned Scientists — not a reopening of the
already-decided Meta subpoena fight. The actual Sept 16 vote outcome isn't posted yet (minutes/
transcript pending) — flagged for a later pass. New lead surfaced and cross-confirmed across
three outlets: Meta's $27B financing deal with Blue Owl Capital (Meta keeping only a 20%/4-year
exit stake against 30-year gas-plant commitments) and the LPSC's Feb 25, 2026 refusal to
investigate the ratepayer risk — a clean fit for the paper's regulatory-capture theme, not yet
folded into the Tier 1 coding scheme (Britton's call). Georgia and Utah Tier 2 cases rechecked,
no change. Also flagged: LPSC's docket-document API, working as of 09-17, now 500-errors on
every parameter tried — a tooling regression, not a content finding. Detail:
`DATA_CENTER_PAPER/notes/2026-09-19-xai-docket-recheck-lpsc-september-session-agenda-and-blue-owl-financing-lead.md`.

**GAMBLING_SOCIAL_COST_PAPER** — the most substantive find of the night. Downloaded and read
the actual Baker et al. "Gambling Away Stability" working paper directly (WebFetch extraction
failed, `pdftotext` worked — a now-recurring pattern for this project). The paper's own 2SLS
estimate is **$0.99 of reduced net investment per $1 bet** for the average household and
**$3.07** for savings-constrained households — matching neither the podcast's "$1→$2" claim nor
the "~20% cut, heavy bettors >50%" figures already sitting in the literature map (those came
from BYU/EurekAlert press coverage, not the primary text). Traced "$1→$2" to Northwestern's own
Kellogg Insight article covering its faculty member's paper — a real, faithfully-repeated quote,
just one that doesn't match the underlying paper's own numbers. Literature map corrected to the
primary-text figures; the press paraphrases flagged as unreliable rather than deleted. Also:
Arizona's Kalshi action confirmed via azag.gov as 20 **criminal** charges (not the civil suit
"sued" implied), plus a new Ninth Circuit ruling (KalshiEX v. Assad, Aug 28) affirming state
authority over sports event contracts; Connecticut's promo-deduction cap confirmed via a
previously-untried findlaw mirror to apply directly to sports wagering, not just casino gaming.
One process note: this pass hit a mid-session scare where its own edits appeared to revert —
root-caused (see below) to the orchestrator's concurrent git staging, not data loss; it
re-verified everything landed correctly. Detail:
`GAMBLING_SOCIAL_COST_PAPER/notes/2026-09-19-podcast-claims-litigation-tax-followups.md`.

**MEAT_SUPPLY_CHAIN_PAPER** — first direct read of the pork antitrust MDL's own court orders
(*In re Pork Antitrust Litigation*, No. 18-1776, D. Minn., via govinfo.gov). **Correction**: the
$117.065M pork settlement's "preliminarily approved July 31, 2026" framing (recorded 09-17) was
imprecise — that date is when the Court approved the class-notice plan; the five underlying
settlements (Tyson $85M, Clemens $13.5M, Seaboard $10M, Hormel $4.465M, Triumph $4.1M) were each
preliminarily approved individually between July 2024 and May 2026. Dollar figures unaffected.
**New finding**: a previously-untracked fourth Agri Stats settlement track — a pork-specific
Direct Purchaser Plaintiff settlement reached final approval Sept 10, 2026, the same day as
DOJ's own civil Agri Stats judgment — giving Agri Stats four settlement tracks resolved within
about six weeks of each other, all on similar behavioral/no-admission terms. The MCOOL 17-6 vs.
16-7 vote-count discrepancy is sharpened, not resolved: two independent, contemporaneous,
named-vote-breakdown sources (Capital Press, DTN's original Aug 6 article) both give 17-6; the
lone 16-7 figure traces to one later, undetailed DTN piece. The DOJ retailer-probe's July 14
letter date is now corroborated via a named wire-service report (Transport Topics/Bloomberg),
still short of the letters themselves. Schaefer/poultry-concentration and idea-28 threads
reconfirmed already resolved, not re-worked. Detail:
`MEAT_SUPPLY_CHAIN_PAPER/NOTES/2026-09-19-pork-mdl-primary-docs-mcool-vote-doj-probe-corroboration.md`.

**Scouting** — logged **one new idea** (42) and one refresh. Idea 42: OpenAI's in-answer
ChatGPT sponsored messages as a "conversational native advertising" disclosure test, anchored to
Sept 16 coverage and a Zappi trust survey showing a live gap (82% call AI-assistant ads at least
as trustworthy as Google ads, but 33%/28%/27% worry about bias/confusability/commercial
influence) — flagged honestly as the fifth AI-disclosure entry in the file (after 10, 25, 31,
38), differentiated but crowded. Refresh: LPSC's expedited "Lightning Initiative" approval
pathway (no public-comment period; Cleco became the first case to skip ALJ review, Sept 17) —
logged as a second, distinct antecedent for idea 1a's regulatory-capture chain. Also
investigated idea 40's open corpus-integrity question for CCS_PAPER/DATA_CENTER_PAPER: found no
evidence of astroturfing exposure, but only because neither project has built a bulk
public-comment corpus yet — not a clean bill of health, worth rechecking once one does.
`Claude_Knowledge/Research_Stream_Ideas.md`.

## Fabrication/correction watch

No fabricated citations, docket entries, dates, or figures introduced tonight. Real corrections
caught and fixed: TARIFF_PAPER's four-night-running mislabeling of the Section 301 reply as the
government's (it was the plaintiffs'); GAMBLING_SOCIAL_COST_PAPER's literature-map figures for
Baker et al., corrected from secondary press coverage to the primary paper's own reported
coefficients; MEAT_SUPPLY_CHAIN_PAPER's imprecise framing of the pork settlement's "preliminary
approval" date (was actually the notice-plan order) and its borrowed class-name label ("End-User
Consumer" instead of "Consumer Indirect Purchaser Plaintiffs"). All are precision corrections
against primary documents, not previously-undetected fabrications.

## Process note — a git-coordination near-miss, fixed, worth reading

Departing from 09-17/09-18's cleaner cadence: this orchestrating session tried to `git stash`
in-progress files out of the way mid-run (twice) so it could push earlier passes' commits while
the GAMBLING and MEAT passes were still actively editing their own project files. This caused a
brief but real risk: a `git stash pop` conflict on `MEAT_SUPPLY_CHAIN_PAPER/PROJECT_STATUS.md`
partially reverted that file to an older state for a few minutes (both the GAMBLING agent and
the MEAT agent independently noticed and flagged what looked like their own edits vanishing).
Caught before any commit landed: diffed the stashed content against the live file for every
affected file, confirmed the GAMBLING agent's own re-verification pass had already made its
files whole, and manually merged the two non-overlapping edits that had landed on
`PROJECT_STATUS.md` (a header/section update and a separate numbered-list item) so nothing was
lost. Nothing was actually lost in the final commits — `aa01ecb`'s `PROJECT_STATUS.md` contains
both edits — but the near-miss means: **don't stash files that a still-running background pass
might be actively writing to.** Next run should let each pass fully finish (and its files go
quiet) before touching git in that pass's directory at all, rather than trying to interleave a
push while other passes are still live.

## What's still open / blocked on you

- **TARIFF_PAPER**: litigation thread's active watch item (Section 301 deadline) is now closed
  out — nothing time-sensitive remains there. Standing items unchanged: CITI Comprehensive-vs-
  Basic module conflict, McNeese HSIRB turnaround (still needs a direct ask to the IRB office),
  Jason's blind-coding worksheet, Purchase Intention item count, banked scales, two small
  Qualtrics-build decisions (Opportunism item 2 anchor direction; attention-check flag-only vs.
  hard-terminate).
- **DATA_CENTER_PAPER**: confirm the Sept 16 LPSC vote outcome once minutes/transcript post;
  decide whether/how the Blue Owl financing lead gets folded into the Tier 1 coding scheme (a
  corpus call, yours to make, not urgent tonight).
- **GAMBLING_SOCIAL_COST_PAPER**: if you want full certainty on the Connecticut statute reading,
  a one-query Westlaw/Lexis check on §12-850/867 would close the last gap; otherwise the
  findlaw-mirror confirmation stands. Standing open_questions.md items untouched, as before.
- **MEAT_SUPPLY_CHAIN_PAPER**: the Senate Ag Committee's own MCOOL roll-call record and
  congress.gov are both blocked to this environment's tooling on two separate nights now — a
  genuine hard wall; closing the 17-6/16-7 question with certainty likely needs non-automated
  access. The pork MDL's actual Settlement Agreement exhibit (Doc. 3381) wasn't pulled — would
  give the newly-found DPP-Agri Stats settlement's cash/no-cash terms directly.
- **Scouting**: idea 42 needs your read on venue/framing, same as ideas 37-41 carried forward
  from prior nights. Idea 40's corpus-integrity question stays open for CCS_PAPER/
  DATA_CENTER_PAPER — worth a real check once either project builds a bulk public-comment
  corpus.
- **CCS_PAPER / FLOCK_CAMERAS_PAPER / SPACEX_LOUISIANA_PAPER**: not touched tonight (all three
  got full passes 09-18) — nothing new to report, no new blockers.
