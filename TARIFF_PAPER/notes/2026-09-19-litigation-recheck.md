# 2026-09-19 — Litigation recheck: Section 301's Sep 18 reply deadline was met — filed on the deadline day itself, by the plaintiffs (correcting a "government reply" mislabel carried in the 09-15 through 09-18 notes); Section 122 got two non-substantive filings; V.O.S. Selections and Axle of Dearborn unchanged

## What this is (disclosure)

AI-assisted (Claude Code) autonomous overnight recheck of the same four
litigation dockets tracked nightly since early September, per the 09-18
note (`2026-09-18-litigation-recheck-section301-deadline-day.md`) and its
predecessors. This is a **direct primary-source docket pull**
(CourtListener), not a search-snippet or WebSearch summary — same four
URLs as every prior night:

1. Section 301 forced-labor master docket — `https://www.courtlistener.com/docket/74219533/in-re-section-301-forced-labor-cases/` [PRIMARY]
2. Section 122 appeal, *State of Oregon v. Trump* (CAFC 26-1804/-1805) — `https://www.courtlistener.com/docket/73318531/state-of-oregon-v-trump/` [PRIMARY]
3. V.O.S. Selections (CAFC 26-1895) — `https://www.courtlistener.com/docket/73433096/vos-selections-inc-v-trump/` [PRIMARY]
4. Axle of Dearborn (CIT 1:25-cv-00091) — `https://www.courtlistener.com/docket/70287201/axle-of-dearborn-inc-v-department-of-commerce/` [PRIMARY]

All four fetched via plain `curl` with a browser User-Agent. All four
returned HTTP 200 with `x-cache: Miss from cloudfront` and a `date:` header
of `Sat, 19 Sep 2026 05:07:3[1-7] GMT` — matching tonight's actual fetch
time within 6 seconds across all four, confirming fresh responses, not
cached or stale copies. Parsed with `beautifulsoup4` (freshly `pip
install`ed again this session — still not preinstalled in this container).
Read entry-by-entry by `id="entry-N"`, comparing full text of every entry
at/after the prior session's max against the 09-18 note's account, not
just an entry-count delta.

**Headline: the Section 301 reply that was due 2026-09-18 was in fact
filed that same day (09/18/2026) — the deadline was met, not missed.** But
correcting something the last several nights' notes got wrong: it is the
**plaintiffs'** reply, not "the government's reply." See §1 below for the
docket mechanics — this doesn't change the bottom line (deadline met on
time) but the party label in the 09-15/09-16/09-17/09-18 notes and
`SUBMISSION_TRACKER.md` was incorrect. Section 122 also picked up two new,
non-substantive entries (resolving an already-known amicus out-of-time
motion). V.O.S. Selections and Axle of Dearborn are both fully unchanged.

## 1. Section 301 forced-labor master docket — 51 → 52 entries; the Sep 18 reply deadline was MET, filed same-day by the plaintiffs (not the government)

`https://www.courtlistener.com/docket/74219533/in-re-section-301-forced-labor-cases/`

**New entry, #52**, filed and entered 09/18/2026:

> "Reply in Support of Motion for Judgment on the Agency Record (related
> document(s) 22). Filed by Pratik A. Shah of Akin, Gump, Strauss, Hauer &
> Feld, LLP on behalf of All Plaintiffs. (Attachments: # 1 Attachment A -
> Declaration of R. Woldenberg, # 2 Attachment B - Declaration of H.
> Stone)(Shah, Pratik) (Entered: 09/18/2026)"

This is exactly the reply flagged as due on 9/18/2026 by entry #22 — it
was filed on the deadline day itself, not late, and not slipped past
midnight into the 19th.

**Correcting the docket-mechanics error carried in the last several
nights' notes:** entries #16 and #22, reread directly, show this was never
going to be "the government's reply." Entry #16 (Aug 24, 2026) is the
**Motion for Judgment on the Agency Record**, filed by Pratik A. Shah on
behalf of **All Plaintiffs**. Entry #22 (Sep 4, 2026) is the
**government's response** to that motion, filed by DOJ's Douglas
Edelschick, with the docket text "Replies due by 9/18/2026." In standard
motion practice, the *movant* (here, the plaintiffs, via the same counsel
who filed entry #16) files the reply responding to the opponent's
response — not the other way around. Entry #52 confirms this exactly:
same filer (Pratik Shah, Akin Gump), same case caption ("All Plaintiffs"),
explicitly captioned as a reply to "related document(s) 22." **The 09-15,
09-16, 09-17, and 09-18 notes (and this project's tracker) all described
this as "the government's Section 301 reply" — that label was wrong from
the start. The deadline itself, and today's finding that it was met on
time, are unaffected by this correction; only the party who owed the
filing was mischaracterized.**

No new activity beyond entry #52 — entries #48-51 reread directly, text
matches the 09-18 account exactly (the Sep 14 amicus-grant order and the
routine notice-of-appearance/corporate-disclosure filings from the
Economists group's counsel).

## 2. Section 122 appeal (State of Oregon v. Trump, CAFC 26-1804/-1805) — 102 → 104 entries, both new entries non-substantive

`https://www.courtlistener.com/docket/73318531/state-of-oregon-v-trump/`

**Two new entries, #103 and #104**, both dated/entered 09/18/2026, closing
out the Economists' motion (entry #102, already known as of 09-17) to file
their amicus brief out of time:

- **Entry #103**: "ORDER filed granting Economists' motion [102] for leave
  to file a brief as amici curiae out of time. By: Per Curiam... [Entered:
  09/18/2026 12:03 PM]"
- **Entry #104**: "CORRECTED AMICUS BRIEF FILED by Olugbenga Ajilore, Alan
  J. Auerbach, et al. (Economists)... [Entered: 09/18/2026 12:08 PM]"

This is procedural housekeeping on a motion already flagged in the 09-17
note — it does not touch the government's own brief deadline, which
**remains 11/12/2026, untouched.**

## 3. V.O.S. Selections (CAFC 26-1895) — unchanged, still 26 entries

`https://www.courtlistener.com/docket/73433096/vos-selections-inc-v-trump/`

**Still 26 entries**, same max as 09-18. Reread entries #24-26 directly —
text matches exactly, including entry #26's text-only order granting the
extension, response brief due 10/05/2026. No new activity.

## 4. Axle of Dearborn (CIT 1:25-cv-00091) — unchanged, still 79 entries

`https://www.courtlistener.com/docket/70287201/axle-of-dearborn-inc-v-department-of-commerce/`

**Still 79 entries.** Reread entries #77-79 directly — text matches every
prior night's account exactly (Aug 17 reassignment, Aug 25 stay/
reliquidation order pair). No new activity.

Checked all four dockets' full page text for a "Date Terminated" field —
none found on any of the four, same as every prior night. All four remain
open/active.

## What changed vs. what didn't (since 09-18)

**Changed:**
- Section 301: 51 → 52 entries. New entry #52 is the reply due 9/18,
  filed on time, by the plaintiffs (see correction above).
- Section 122: 102 → 104 entries. Two new, non-substantive entries closing
  out an already-known amicus motion; government's 11/12/2026 brief
  deadline untouched.

**Did not change:**
- V.O.S. Selections: still 26 entries, extension grant (due 10/05/2026)
  still the latest entry.
- Axle of Dearborn: still 79 entries, no new activity.
- No docket shows "Date Terminated" — all four remain open.

## SUBMISSION_TRACKER.md and other project-file drift check (task priority 4)

**Updated `SUBMISSION_TRACKER.md`** with a new dated bullet under
"## Deadline" recording tonight's resolution of the Section 301 deadline
question: filed on time on 09/18/2026, by the plaintiffs (not the
government — correcting the mislabel in the 09-15/09-16/09-17/09-18
entries), plus the two new non-substantive Section 122 entries. Did not
rewrite or delete any prior dated entry, per this project's convention of
appending dated entries rather than overwriting history — left the
"government reply" phrasing in the older entries as-is (that's the
historical record of what was believed at the time) and added the
correction as new text rather than editing old bullets.

Checked file listing/mtimes for the whole `TARIFF_PAPER/` root: every
non-litigation file still carries the same 2026-09-13 05:05 mtime it has
carried every night since 09-13 — confirming **nothing new was built or
decided in this project outside the litigation-recheck thread since
09-13**. `git log` confirms the same: the last non-litigation commit
remains the Qualtrics-import addition from 2026-09-11.

## Other standing open items (task priority 5)

Per tonight's task scope, the standing open items (CITI Comprehensive-vs-
Basic module conflict, HSIRB turnaround time, Jason's blind-coding
worksheet, Purchase Intention item count, banked scales, the two
Qualtrics-build decisions) were not re-researched — these remain Britton's
calls or external dependencies, unchanged from every prior night's
account. No new public information surfaced on any of them during
tonight's docket work.

## Tooling note

Same approach as every prior session in this thread: plain `curl` with a
browser User-Agent, confirmed fresh via `x-cache: Miss from cloudfront` and
matching `date:` headers, parsed with `beautifulsoup4` (installed fresh
this session, as usual for this container). No WAF block, no 403/401 on
any of the four URLs tonight.

## For Britton

- **Section 301's reply, due 9/18/2026, was filed on time that same day.**
  This closes out the multi-night watch on that deadline — no missed
  filing, no extension needed.
- **One correction to flag: this was always the plaintiffs' reply, not
  "the government's reply."** The docket shows plaintiffs (via Akin Gump's
  Pratik Shah) moved for judgment on the agency record in August, the
  government responded September 4, and the plaintiffs' own reply to that
  response was due — and filed — September 18. The last several nights'
  notes (09-15 through 09-18) and the tracker called it "the government's
  reply," which was a mislabeling on this project's part, not something
  that changed on the docket. Doesn't affect anything substantively — just
  correcting the record.
- Section 122 picked up two small, non-substantive entries closing out an
  amicus brief's "out of time" filing motion (already flagged as pending
  back on 09-17) — the government's own brief deadline (11/12/2026) is
  untouched.
- V.O.S. Selections and Axle of Dearborn are completely unchanged since
  09-18 — no new filings, no rulings.
- Updated `SUBMISSION_TRACKER.md` with tonight's finding.
- Nothing else changed in the project since 09-13 — no new non-litigation
  files, confirmed via `git log` and mtimes.
- Everything on the actual critical path (CITI Comprehensive question,
  HSIRB turnaround, Jason's coding worksheet, Purchase Intention item
  count, banked scales, the two small Qualtrics decisions) is exactly
  where it was — still waiting on you or on Jason, not on anything this
  session could resolve.
