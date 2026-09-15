# 2026-09-15 — Litigation recheck: real movement on two of three pending motions; tracker synced, no other drift found

## What this is

Re-ran the same four-docket litigation check per the 09-13 note
(`2026-09-13-litigation-recheck.md`), using the same four CourtListener docket URLs
that note and its predecessors used. All four fetched directly via `curl` with a
browser User-Agent (HTTP 200, real docket HTML, `x-cache: Miss from cloudfront` and a
`date:` header matching tonight's actual fetch time on every response — confirmed
fresh, not a cached/stale copy, not a WebSearch/AI-summary substitution). Parsed each
docket's raw HTML with BeautifulSoup, reading entry-by-entry by `id="entry-N"` and
diffing the full text of every new entry against the 09-13 note's account.

**Headline: this was not a quiet night. Two of the three pending motions the tracker
has been following got ruled on — both granted.**

## 1. Section 301 forced-labor master docket — 45 → 51 entries, the amicus wave was resolved

`https://www.courtlistener.com/docket/74219533/in-re-section-301-forced-labor-cases/`

Six new entries (#46-51) since 09-13. The important one is **entry #48, an order
entered 9/14/2026**: it **grants all 11 pending motions for leave to file as amicus
curiae** — Cato Institute/McConnell/Somin, Burlap and Barrel/Collective Horology, a
20-plus-state coalition led by Oregon, an economists' group (Unikowsky et al.), the
Former U.S. Trade Officials, Barry Appleton, Goldwater Institute, Ed Gresser/PPI,
Timothy Meyer/Gregory Shaffer, and Consumer Watchdog — and deems each of their briefs
filed. This resolves the entire amicus-motion backlog the 09-04 through 09-13 notes
had been tracking as pending. Entries #49-51 (Sep 14) are routine notice-of-appearance
and corporate-disclosure filings from the Economists group's counsel following the
grant, not substantive.

**Entry #22 (the government's Sep 4 response) reread directly and unchanged**: still
"Replies due by 9/18/2026." **That deadline is now 3 days out from today (2026-09-15)**,
exactly as the task brief expected, and nothing on the docket suggests it will move.

## 2. Section 122 appeal (State of Oregon v. Trump, CAFC 26-1804/-1805) — 96 → 99 entries, the extension motion was granted

`https://www.courtlistener.com/docket/73318531/state-of-oregon-v-trump/`

Three new entries since 09-13. **Entry #99, an order entered 9/14/2026, grants the
government's motion (entry #96) to extend its brief deadline to 11/12/2026** — this
is the exact motion the task brief flagged as pending. It's now resolved: the
government has until 11/12/2026 to file its response/reply brief.

Entries #97 and #98 (both Sep 14) are Notices of Non-Compliance from the clerk against
two of the amicus briefs already on file (Cato Institute/Somin, and an economists'
group led by Stan Veuger) — formatting/filing-rule defects, not substantive rulings;
compliant versions are due 9/21/2026. Worth knowing about but not affecting the
paper's tracked deadlines.

## 3. V.O.S. Selections (CAFC 26-1895) — unchanged, still 25 entries

`https://www.courtlistener.com/docket/73433096/vos-selections-inc-v-trump/`

Reread entries #20-25 directly — text matches the 09-13 account exactly. **Appellee
V.O.S. Selections' motion to extend its brief deadline to 10/05/2026 (entry #25) has
still not been ruled on.** This is now the only one of the three originally-pending
motions still open.

## 4. Axle of Dearborn (CIT 1:25-cv-00091) — unchanged, still 79 entries

`https://www.courtlistener.com/docket/70287201/axle-of-dearborn-inc-v-department-of-commerce/`

Reread entries #74-79 directly — text matches the 09-13 (and 09-12, 09-10) account
exactly: Cape Phase 3 motion, the Aug 13 Slip Op. 26-94 ruling and partial judgment,
the Aug 17 reassignment, and the Aug 25 stay/reliquidation order pair. No new activity.

Checked all four dockets for a "Date Terminated" field (would indicate a closed case)
— none found on any of the four. All four remain open/active.

## Tracker updated

Added a dated entry to `SUBMISSION_TRACKER.md`'s Deadline section recording both
rulings and the still-open V.O.S. Selections motion, plus the Sep 18 reply deadline
now being 3 days out. This is reporting rulings that happened, not a design/judgment
call.

## Tracker staleness check (task priority 2) — no drift found tonight

Compared `SUBMISSION_TRACKER.md` against the actual project file listing. Every file
in `TARIFF_PAPER/` (root level and `notes/`) carries the same 2026-09-13 mirror
timestamp except the docket files just fetched and this note — meaning **nothing new
was built or decided in this project between the 09-13 note and tonight**, so there
was no fresh drift for the tracker to have fallen behind on. The two items the 09-13
note caught and fixed (H3 status, Qualtrics build status) are still correctly
reflected. No further tracker corrections were needed tonight beyond the litigation
update above.

## Other open items (priority 3) — status check only, no re-search performed

Per the task brief's own guidance not to re-run searches without a real reason to
think something changed, and because nothing in the project changed since 09-13
(see above), these were not re-searched tonight. Current status, unchanged from the
09-13 note:

- **CITI Comprehensive-vs-Basic module conflict** — still open. Britton's "I got the
  basic and I think that's all we need" (2026-09-08) vs. McNeese's own HSIRB policy
  page naming the Comprehensive module (confirmed twice, 09-09 and 09-10). Needs
  Britton to confirm with the IRB office or complete the Comprehensive module as a
  precaution.
- **McNeese HSIRB turnaround time** — still not publicly findable (confirmed dead-end
  three prior nights running). Needs a direct ask to the IRB office.
- **Jason's blind-coding worksheet** — still no file in the repo, no Gwet's AC1
  computed. External dependency on Jason's time.
- **Purchase Intention item count (5 vs. 3-item subset)** — Britton's confirm/override
  call, untouched.
- **Banked scales for a future companion paper** — Britton's call, untouched.
- **Open Question #8 (Opportunism item-2 anchor direction; attention-check
  hard-terminate vs. flag-only)** — both quick yes/no Qualtrics-build decisions,
  don't block importing the survey, untouched.

## Literature-gap / critical-path work (priority 4)

Checked the tracker's critical path for anything actionable that isn't already
blocked on Britton or an external party (IRB office, Jason, Qualtrics import).
Everything currently open on the critical path — Purchase Intention item count,
IRB/HSIRB turnaround, Jason's coding pass, the Qualtrics live import itself — needs
either Britton's decision or someone else's action, not more AI-side research. No
new literature-gap work was identified tonight that would genuinely advance the paper
without duplicating already-completed verification passes; didn't force any.

## Tooling note

Same approach as 09-12/09-13: plain `curl` with a browser User-Agent, confirmed fresh
via `x-cache: Miss from cloudfront` and matching `date:` headers, parsed with
`beautifulsoup4` (had to `pip install` it fresh this session — not preinstalled in
this container). No WAF block, no 403/401 on any of the four URLs tonight.

## For Britton

- **Litigation dockets: real movement tonight, both favorable in the sense of just
  being resolved rather than dragging.** Section 301's entire amicus-brief backlog
  (11 motions, including the Cato Institute, a 20-plus-state coalition, and an
  economists' group) was granted in one order on Sep 14 — all those briefs are now
  officially part of the record. Section 122's government extension motion was also
  granted the same day — their brief is now due 11/12/2026 instead of whatever the
  original date was. The government's Section 301 reply is still due **9/18/2026,
  three days from today**. The one loose end left is V.O.S. Selections' own motion to
  extend its brief deadline to 10/05/2026 — still sitting unruled.
- Two new, minor items on the Section 122 docket: the clerk flagged two amicus briefs
  (Cato/Somin and an economists' group) as not compliant with court formatting rules;
  corrected versions are due 9/21/2026. Not something that affects this paper or needs
  your attention — just docket noise, noted for completeness.
- Nothing else changed in the project since the 09-13 session — no new files, so no
  new tracker drift to fix. Everything else (CITI Comprehensive question, HSIRB
  turnaround, Jason's coding worksheet, Purchase Intention item count, banked scales,
  the two small Qualtrics decisions) is exactly where it was Saturday — still waiting
  on you or on Jason, not on anything this session could resolve.
