# 2026-09-13 — Litigation recheck: all four dockets stable overnight, no rulings yet on any pending motion; caught two stale items in SUBMISSION_TRACKER.md and synced them

## What this is

Re-ran the same four-docket litigation check per the 09-12 note
(`2026-09-12-litigation-recheck.md`), using the same four CourtListener docket URLs
that note and its predecessors used. All four fetched directly via `curl` with a
browser User-Agent (HTTP 200, real docket HTML, `x-cache: Miss from cloudfront` and a
`date:` header matching tonight's actual fetch time on every response — confirmed
fresh, not a cached/stale copy). Parsed each docket's raw HTML with BeautifulSoup
(same approach as 09-12), reading entry-by-entry by `id="entry-N"` rather than
inferring from an entry-count delta, and diffed the full text of every entry near the
prior max against what the 09-12 note already recorded.

**Headline: nothing changed on any of the four dockets since the 09-12 check.** No
new entries, no rulings on any of the three motions left pending as of last night.

## 1. Section 301 forced-labor master docket — unchanged, still 45 entries

`https://www.courtlistener.com/docket/74219533/in-re-section-301-forced-labor-cases/`

**Still 45 entries** (same max as 09-12; no entry 46 exists). Reread entries #40-45
(the tail of the 7-filer amicus wave) directly — text matches the 09-12 account
exactly, including the Cato Institute and Burlap and Barrel/Collective Horology
filings. None of the amicus motions for leave have been ruled on. Reread entry #22
(the government's Sep 4 response) directly: still reads "Modified on 9/8/2026,"
"Entered: 09/04/2026," **Replies due by 9/18/2026** — unchanged, that deadline still
stands and is now 5 days out.

## 2. Section 122 appeal (State of Oregon v. Trump, CAFC 26-1804/-1805) — unchanged, still 96 entries

`https://www.courtlistener.com/docket/73318531/state-of-oregon-v-trump/`

**Still 96 entries.** Reread entries #91-96 directly — text matches the 09-12 account
exactly. **The government's motion to extend its brief deadline to 11/12/2026
(entries #93/#96, filed then re-filed after a correction) has not been ruled on** —
no grant or denial order appears after entry #96. Still just a pending motion, not an
order.

## 3. V.O.S. Selections (CAFC 26-1895) — unchanged, still 25 entries

`https://www.courtlistener.com/docket/73433096/vos-selections-inc-v-trump/`

**Still 25 entries.** Reread entries #20-25 directly — text matches the 09-12 account
exactly. **Appellee V.O.S. Selections' motion to extend its brief deadline to
10/05/2026 (entry #25) has not been ruled on.**

## 4. Axle of Dearborn (CIT 1:25-cv-00091) — unchanged, still 79 entries

`https://www.courtlistener.com/docket/70287201/axle-of-dearborn-inc-v-department-of-commerce/`

**Still 79 entries.** Reread entries #74-79 directly — text matches the 09-12 (and
09-10) account exactly: Cape Phase 3 motion, the Aug 13 Slip Op. 26-94 ruling and
partial judgment, the Aug 17 reassignment, and the Aug 25 stay/reliquidation order
pair. No notice of appeal, no new activity.

Also checked all four dockets' full page text for a "Date Terminated" field (would
indicate a case closed) — none found on any of the four. All four remain open/active.

## Tooling note

No WAF block, no 403/401, no WebSearch-summary substitution needed tonight — plain
`curl` with a browser User-Agent got clean HTTP 200 responses with fresh (not cached)
`Miss from cloudfront` headers on the first try for all four URLs. Same
`beautifulsoup4` parsing approach as 09-12.

## Other open items checked tonight (verification/sync only, no design-lock calls made)

Per the standing rule that Phase 3 (thematic-analysis theme review) and any
scale/design/hypothesis-direction judgment calls stay Britton's, this section is
strictly "did something already get decided or built that the tracker doesn't yet
reflect" and "is there any new public information," not new decisions.

- **H3 (interaction hypothesis) — SUBMISSION_TRACKER.md was stale, now fixed.**
  Cross-checking `SUBMISSION_TRACKER.md`'s open-questions list against the actual
  project files found Open Question #6 still describing H3 as "still open... hasn't
  been through Britton's own review yet." That's wrong as of tonight: Britton
  reviewed it and gave a specific reversal instruction on **2026-09-10**
  (compensatory/cue-substitution direction — see
  `notes/2026-09-10-h3-reversal-literature-check.md`), and it was already rewritten
  into `Introduction_and_Theory_DRAFT_2026-08-12.md` and
  `Tariff_Manuscript_Working_Draft_2026-09-04.md`, then synced into this repo's
  mirror during the 09-11 local↔mirror reconciliation
  (`notes/2026-09-11-local-mirror-reconciliation.md` says so explicitly: "Repo had
  Britton's confirmed 2026-09-10 H3 reversal... Local was the strict superset here"
  — meaning the underlying decision was real and current, only the tracker doc's own
  open-questions list hadn't been updated to say so). Fixed `SUBMISSION_TRACKER.md`
  Open Question #6 and the Introduction/Theory status-table row to reflect this. This
  is reporting an already-made decision accurately, not making a new one — the H3
  direction itself was not touched, reconsidered, or second-guessed.
- **Study 2 Qualtrics build — SUBMISSION_TRACKER.md was stale here too, now fixed.**
  The tracker's critical-path step 3 and status table still said the Qualtrics
  instrument was "not yet built in Qualtrics," but `Study2_Qualtrics_IMPORT_2026-09-11.txt`
  (a full Advanced-Format import file: 11 blocks, 6 vignette blocks, 32 questions) and
  `Study2_Qualtrics_POST_IMPORT_CHECKLIST_2026-09-11.md` (step-by-step Survey Flow,
  randomizer, timer, and options instructions, ~20 minutes) were both already built
  and sitting in the project folder as of 2026-09-11 — just never reflected in the
  tracker. Updated the status table row and critical-path step 3 accordingly, and
  added a new Open Question #8 for the two small confirm/override items that build
  flagged (Opportunism item 2's reversed anchor direction; whether attention-check
  failure should flag-only or hard-terminate) — both still genuinely await Britton's
  call, built as-specified defaults for now. No live Qualtrics UI import was
  attempted tonight (same reasoning as 09-09/09-11: unsupervised multi-step Qualtrics
  UI automation is higher-risk than handing over an unambiguous, already-complete
  spec+checklist).
- **CITI Comprehensive-vs-Basic module question — not re-verified tonight, no new
  information.** This has already been independently confirmed twice (09-09, 09-10)
  by direct fetch of McNeese's own HSIRB policy page; a third identical fetch would
  add nothing. Status unchanged from the tracker's existing account: still a live,
  unresolved conflict between Britton's "I got the basic and I think that's all we
  need" (2026-09-08) and the policy page's own text naming the Comprehensive module.
  Not something an AI session can resolve — needs Britton to either confirm with the
  IRB office or complete the Comprehensive module as a precaution.
- **McNeese HSIRB turnaround time (Open Question #2) — attempted a fresh public-source
  search tonight, found nothing new, dead end confirmed again.** Tried McNeese's
  HSIRB policy page again (checked its full text tonight for "turnaround,"
  "business days," "weeks," "meeting," "expedited," etc. — no matches on any of
  those) and tried to reach McNeese's "IRB Application Guidelines" page
  (`mcneese.edu/hsirb/irb_application_guidelines/`), which search engines list but
  which returns a genuine 404 directly from McNeese's own server (confirmed via
  `curl -I`, not a WAF block — `cf-ray` present, ordinary Cloudflare-fronted 404).
  **This remains a real "needs a direct ask to the IRB office" item, not something
  findable from public pages** — same conclusion as every prior night that's checked
  this.
- **Grad-assistant (Jason) blind-coding worksheet — checked, still no file, no new
  information.** Searched the entire `TARIFF_PAPER` folder again for anything
  Jason-named or any Gwet's-AC1 computation — found nothing, same as the 09-09
  finding (`notes/2026-09-09-instrument-build-and-coder-check.md`). This is an
  external dependency on Jason's own time and isn't resolvable from files in this
  repo; still needs a direct check with Britton or Jason.
- **Purchase Intention item-count choice, banked-scales question — untouched, both
  are explicitly Britton's confirm/override calls per the tracker**, not decisions to
  make here.

## For Britton

- **Litigation dockets: quiet night, nothing new.** All four unchanged since
  yesterday. The two pending brief-deadline extension motions (Section 122's
  government request to Nov 12, V.O.S. Selections' appellee request to Oct 5) and
  the Section 301 amicus wave are all still exactly where they were — nothing ruled
  on. The Sep 18 reply deadline on the Section 301 docket is unaffected and now 5
  days out.
- **Two items in `SUBMISSION_TRACKER.md` were stale and are now fixed, no action
  needed from you:** it was still listing H3 as unreviewed (you resolved it
  2026-09-10) and the Qualtrics instrument as unbuilt (the import file + checklist
  were finished 2026-09-11). Both are now accurately reflected. The two small
  Qualtrics decisions that build flagged (Opportunism item 2 anchor direction,
  attention-check hard-terminate vs. flag-only) are new Open Question #8 — quick
  yes/no items, not urgent, don't block importing the survey.
- Everything else (CITI Comprehensive question, HSIRB turnaround, Jason's coding
  worksheet, Purchase Intention item count, banked scales) is exactly where it was —
  checked tonight, no new public information found on any of them, and none are
  things this session can resolve unilaterally.
