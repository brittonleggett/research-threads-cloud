# 2026-09-10 — Litigation recheck: the Section 301 "overdue" government response was actually filed on time (Sep 4); it just didn't sync into the docket scrape until now. Section 122 docket jumped 81→90 entries with real appellate activity.

## What this is
Per the standing autonomy mandate, re-ran the same four-docket litigation check this
project has run nightly since 09-04, all via direct `curl` fetches of the actual
CourtListener docket pages (not WebSearch synthesis) — same technique as every prior
night. Last night (09-09) two of the four dockets were blocked by a new AWS WAF
JavaScript challenge; tonight all four came through clean (HTTP 200, real docket HTML),
consistent with 09-09's own guess that it was a transient rate-limit rather than a
permanent block.

## 1. Section 301 forced-labor master docket — the headline finding: the government's response was NOT actually late

`https://www.courtlistener.com/docket/74219533/in-re-section-301-forced-labor-cases/`

Five straight nights (09-05 through 09-09) found this docket stuck at 21 entries and
flagged the government's response (due 9/4 to plaintiffs' Aug 24 motion for judgment
on the agency record) as increasingly overdue — "4 days overdue" as of 09-08, "likely
5 days overdue but unconfirmed" as of 09-09 (WAF-blocked that night).

**Tonight the docket shows 22 entries.** Entry #22, read directly from the docket
page (not inferred from a count change):

> **Entry 22, Sep 4, 2026** — "Response to Motion for Judgment on the Agency Record
> Pursuant to Rule 56.1 (related document(s) 16). Replies due by 9/18/2026. Filed by
> Douglas Glenn Edelschick of U.S. Department of Justice on behalf of United States.
> (Edelschick, Douglas) **Modified on 9/8/2026** (Taronji, Steve). (Entered: 09/04/2026)"

Read literally: the government's response **was filed on time, on September 4, 2026**
— the docket's own "Entered" timestamp says 09/04/2026. The "Modified on 9/8/2026"
annotation (a routine RECAP/clerk correction, not a refiling) is the most likely
explanation for why five consecutive nightly scrapes of this same docket page, from
09-05 through 09-09, never showed it: the entry may not have synced into CourtListener's
RECAP mirror until on or after the Sep 8 modification, even though the underlying court
filing happened on the actual due date. **This is a case where CourtListener's docket
mirror itself lagged the real court record by several days — not a case of the
government being late, and not a case of a prior night's read being wrong at the time
it was made.** Every "not yet on the docket" note from 09-05 through 09-09 was an
accurate description of what the docket page actually showed on those dates; the
underlying filing just hadn't propagated into this mirror yet.

Confirmed the PDF itself exists and is fetchable directly from CourtListener's own
storage (`storage.courtlistener.com/recap/gov.uscourts.cit.21643/gov.uscourts.cit.21643.22.0_1.pdf`,
200 OK, 551KB, a real PDF file, downloaded to verify it isn't a broken/placeholder
link) — but this session's text-extraction tooling (`pdftotext`/`poppler-utils`, and a
`pypdf` install) both failed in this environment tonight (apt repo 404 for
poppler-utils; pypdf's `cryptography` dependency crashed on import), so **the response's
actual legal arguments haven't been read, only the docket entry's own metadata/caption**.
That's enough to confirm the filing happened and correct the "still overdue" status, but
not enough to characterize what the government actually argued — flagging as a future
task if the brief's substance matters for anything (it likely doesn't for this project,
since this is background litigation-tracking context, not something the manuscript cites
in detail).

**Replies are due Sep 18, 2026** — matches the Sep 18 date already in this project's
files as "the reply-brief deadline," now confirmed as specifically the plaintiffs'
reply-to-government's-response deadline on this docket, not a guess.

Entries 1-21 (everything checked in prior nights) reread as part of this fetch and
unchanged from the 09-08 note's account — no other correction needed there.

## 2. Section 122 (State of Oregon v. Trump / Burlap and Barrel, CAFC 26-1804/-1805) — real new activity, 81→90 entries

`https://www.courtlistener.com/docket/73318531/state-of-oregon-v-trump/`

Stable at 81 entries from 09-05 through 09-08; **now 90**. Read entries 82-90 directly:

- **#82-83 (Sep 4):** procedural — a notice of non-compliance against the Appellee/
  Cross-Appellant states' group and a motion for leave to file an appearance.
- **#84 (Sep 8):** the court (per curiam) **granted** the motion to extend time and
  correct Appellees Basic Fun/Burlap and Barrel's brief, and granted a counsel-
  withdrawal/appearance swap for North Carolina.
- **#85-86 (Sep 8):** North Carolina's new counsel entry, and the **corrected response
  brief** actually filed by Basic Fun, Inc. and Burlap and Barrel, Inc. (the small-
  business appellees whose "corrected deadline" the 09-08 note flagged as 3 days out —
  it landed on schedule).
- **#87-89 (Sep 8):** the **CATO Institute** (with Ilya Somin) entered an appearance,
  filed a certificate of interest, and **filed an amicus curiae brief** (marked
  "pending compliance review").
- **#90 (Sep 9):** a second **amicus curiae brief filed by "Economists"** (counsel
  Aaron Cooper), also pending compliance review.

Read for the paper: this is genuine appellate momentum, not routine housekeeping — two
amicus briefs (one from a named advocacy-adjacent think tank, one from an economist
group) landing within 24 hours of each other suggests the case is drawing outside
attention as briefing wraps up. Not something this project needs to act on beyond
noting it; no design/theory implication, just a litigation-tracking update.

## 3 & 4. V.O.S. Selections (CAFC 26-1895) and Axle of Dearborn (CIT 1:25-cv-00091) — both fully stable

Both re-fetched directly and reread entry-by-entry for the final 2 entries each. V.O.S.
Selections: still 24 entries, #24 (Sep 2) is the same caption-revision entry noted
09-04 through 09-08 — no change. Axle of Dearborn: still 79 entries, #78-79 (Aug 25,
the reliquidation stay order) match the 09-08 note exactly — no change.

## For Britton

- **The Section 301 "government response is overdue" thread that's been open since
  09-05 is resolved: it was filed on time (Sep 4), the docket mirror just hadn't
  caught up yet.** Nothing to chase here anymore. Replies are due Sep 18 — worth a
  glance around then if you want to see how the case develops, but not urgent.
- **Section 122 (Oregon v. Trump / Burlap and Barrel) picked up real activity**: a
  corrected small-business brief landed on schedule, and two amicus briefs (CATO
  Institute, an economists' group) were filed Sep 8-9. Background color only, not
  something the manuscript needs.
- V.O.S. Selections and Axle of Dearborn: no change, nothing to do.
- Everything else in this project (IRB submission status, CITI Comprehensive-module
  question, grad-assistant blind-coding worksheet, H3 direction, Purchase Intention
  item-count choice) is untouched tonight — all of it is either already flagged as
  your call or an external dependency this session can't check.
- One tooling note: this session couldn't extract text from a downloaded court PDF
  (`poppler-utils` failed to install — apt mirror returned 404 for that package
  tonight; a `pypdf` install also failed on a broken `cryptography`/Rust dependency in
  this environment). Didn't block tonight's work since the docket entry's own metadata
  was sufficient, but worth knowing if a future session needs to read PDF text and hits
  the same wall.
