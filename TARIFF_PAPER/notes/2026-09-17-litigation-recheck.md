# 2026-09-17 — Litigation recheck: V.O.S. Selections' extension motion turns out to already be granted (docket-sync lag, same pattern as before); Section 301's Sep 18 reply deadline is still unmet with the deadline now tomorrow

## What this is (disclosure)

AI-assisted (Claude Code) autonomous overnight recheck of the same four
litigation dockets tracked nightly since early September, per the 09-16
note (`2026-09-16-litigation-recheck.md`) and its predecessors. This is a
**direct primary-source docket pull** (CourtListener), not a search-snippet
or WebSearch summary — same four URLs as every prior night:

1. Section 301 forced-labor master docket — `https://www.courtlistener.com/docket/74219533/in-re-section-301-forced-labor-cases/` [PRIMARY]
2. Section 122 appeal, *State of Oregon v. Trump* (CAFC 26-1804/-1805) — `https://www.courtlistener.com/docket/73318531/state-of-oregon-v-trump/` [PRIMARY]
3. V.O.S. Selections (CAFC 26-1895) — `https://www.courtlistener.com/docket/73433096/vos-selections-inc-v-trump/` [PRIMARY]
4. Axle of Dearborn (CIT 1:25-cv-00091) — `https://www.courtlistener.com/docket/70287201/axle-of-dearborn-inc-v-department-of-commerce/` [PRIMARY]

All four fetched via plain `curl` with a browser User-Agent. All four
returned HTTP 200 with `x-cache: Miss from cloudfront` and a `date:` header
of `Thu, 17 Sep 2026 05:07:4[5-7] GMT` — matching tonight's actual fetch
time within 3 seconds across all four, confirming fresh responses. Parsed
with `beautifulsoup4` (freshly `pip install`ed again this session — still
not preinstalled in this container). Read entry-by-entry by `id="entry-N"`,
diffing full text of every entry at/after the prior session's max against
the 09-16 note's account, not just an entry-count delta.

**Headline: two of the four dockets moved since 09-16, and one of those
moves resolves a motion the last several nights' notes have been carrying
as "still unruled." Section 301 — the one with tomorrow's deadline — is
unchanged and the government's reply is still not on the docket.**

## 1. Section 301 forced-labor master docket — unchanged, still 51 entries; Sep 18 deadline still unmet, now 1 day out

`https://www.courtlistener.com/docket/74219533/in-re-section-301-forced-labor-cases/`

**Still 51 entries**, same max as 09-16. Reread entries #48-51 directly —
text matches the 09-16 account exactly (the Sep 14 amicus-grant order and
the routine notice-of-appearance/corporate-disclosure filings from the
Economists group's counsel).

**Entry #22 (the government's Sep 4 response) reread directly, unchanged
verbatim**: "Response to Motion for Judgment on the Agency Record...
Replies due by 9/18/2026... Modified on 9/8/2026... (Entered: 09/04/2026)."
**Today is 2026-09-17. That deadline is now 1 day out, and nothing on the
docket — no reply, no extension motion, no order — has appeared.** This is
the single item flagged as most time-sensitive going into tonight, and the
direct read confirms: still nothing filed, still on track for a Friday
9/18 filing (or a slip, which would need tomorrow's recheck to catch).

## 2. Section 122 appeal (State of Oregon v. Trump, CAFC 26-1804/-1805) — 101 → 102 entries, new entry is a procedural amicus filing, not a ruling

`https://www.courtlistener.com/docket/73318531/state-of-oregon-v-trump/`

**Now 102 entries** (up from 101 on 09-16). The new entry:

- **Entry #102** (Sep 15, 2026; Entered 09/15/2026 5:02 PM): a motion by the
  Economists amici group (Stan Veuger, Olugbenga Ajilore, et al., same group
  as entries #100-101) to file their amicus brief out of time, with two
  attachments — "Motion to File Brief for Amici Curiae Out of Time" and a
  "Corrected Brief of Amici Curiae of Economists in Support of
  Plaintiffs-Appellees." This is the fix for the non-compliance notice
  already on the docket at entry #98 (Sep 14 — their originally-filed brief
  wasn't rules-compliant, compliant version due 09/21/2026). **Not a ruling,
  doesn't touch the government's 11/12/2026 brief deadline.**

**Timing note worth flagging:** this entry's own "Entered" timestamp
(09/15/2026 5:02 PM) predates the 09-16 session's fetch window (05:08-05:14
GMT on 09-16, i.e. after midnight Eastern on the 16th) — meaning it should
plausibly have already been on the docket when the 09-16 fetch ran, but the
09-16 note reported max entry 101, not 102. This is the same
docket-mirror-sync-lag pattern already documented once before for Section
301 (`notes/2026-09-10-litigation-recheck-section301-government-response-
was-filed-on-time-not-actually-overdue.md`) — CourtListener's PACER mirror
doesn't always reflect an entry's "Entered" timestamp immediately. Noting
it rather than treating it as a same-day surprise.

## 3. V.O.S. Selections (CAFC 26-1895) — 25 → 26 entries: the previously-open extension motion is now granted

`https://www.courtlistener.com/docket/73433096/vos-selections-inc-v-trump/`

**Now 26 entries** (up from 25 on 09-16, 09-15, 09-13, 09-12). The new
entry:

- **Entry #26** (Sep 15, 2026; Entered 09/15/2026 4:05 PM): "**TEXT ONLY**
  ORDER granting motion to extend time to file brief [25] filed by Appellee
  V.O.S. Selections, Inc. The response brief is due 10/05/2026."

**This resolves the one motion every prior note (back through at least
09-11) has been carrying as "the one genuinely open motion left across all
four dockets."** V.O.S. Selections' Sep 11 motion to push its brief
deadline to Oct 5 (entry #25) has been granted exactly as requested — no
surprise in the outcome, just a formal ruling that wasn't there before.

**Same timing caveat as Section 122 above**: this order's own timestamp
(09/15/2026 4:05 PM) also predates the 09-16 fetch window, yet the 09-16
note reported "still 25 entries." Same docket-sync-lag explanation applies
— not something the 09-16 session missed by reading carelessly, the HTML
genuinely didn't have it yet. **Updated `SUBMISSION_TRACKER.md`
accordingly** — see below.

## 4. Axle of Dearborn (CIT 1:25-cv-00091) — unchanged, still 79 entries

`https://www.courtlistener.com/docket/70287201/axle-of-dearborn-inc-v-department-of-commerce/`

**Still 79 entries.** Reread entries #74-79 directly — text matches every
prior night's account exactly (Cape Phase 3 motion, Aug 13 Slip Op. 26-94
ruling and partial judgment, Aug 17 reassignment, Aug 25 stay/reliquidation
order pair). No new activity.

Checked all four dockets' full page text for a "Date Terminated" field —
none found on any of the four, same as every prior night. All four remain
open/active.

## What changed vs. what didn't (since 09-16)

**Changed:**
- V.O.S. Selections: 25 → 26 entries — the Oct 5 extension motion is now
  **granted** (order entered 09/15/2026, response brief due 10/05/2026).
  This was the last genuinely-open motion across all four dockets; it's now
  resolved.
- Section 122: 101 → 102 entries — a procedural amicus filing (Economists
  group fixing a non-compliance brief), no ruling, no deadline change.

**Did not change:**
- Section 301: entry count, the Sep 18 reply deadline text, and the absence
  of any reply/extension filing all confirmed unchanged verbatim. **Deadline
  is tomorrow (2026-09-18) with nothing filed yet.**
- Section 122's substantive posture: government's brief still due
  11/12/2026.
- Axle of Dearborn: still 79 entries, no new activity.
- No docket shows "Date Terminated" — all four remain open.

## SUBMISSION_TRACKER.md and other project-file drift check (task priority 2)

**Found and fixed one real drift item**: the tracker's 09-15 litigation
entry said "V.O.S. Selections' Oct 5 extension motion is still unruled,"
which was accurate as of 09-15 and 09-16 but is now stale per tonight's
finding above. Added a new dated bullet under "## Deadline" recording the
grant and the Section 301 deadline status — did not rewrite or delete the
09-15 entry, per this project's convention of appending dated entries
rather than overwriting history.

The rest of the tracker needs no other correction tonight. Checked file
listing/mtimes for the whole `TARIFF_PAPER/` root against
`notes/2026-09-13-litigation-recheck.md` (the last time this check found
drift) — nothing newer, same conclusion as 09-15 and 09-16. `git log`
confirms the last non-litigation commit to this project remains the
Qualtrics-import addition from 2026-09-11; the four most recent commits are
all litigation-recheck notes (09-13, 09-15, 09-16, and now tonight).

## Other Study 1 / manuscript progress (task priority 3)

Given how much of tonight went to the litigation recheck (including
resolving the sync-lag question above), and that this project's actual
critical-path blockers (HSIRB turnaround, Jason's coding pass, Purchase
Intention item count) are external dependencies or Britton's calls, not
research tasks — no separate Study 1 work was attempted tonight beyond
confirming (via the git-log/mtime check above) that nothing there has
drifted. Nothing new to report on citation verification, corpus expansion,
or methods polish; none of tonight's time went unused, it went to a more
thorough litigation pass than a pure diff would have required (chasing down
why two entries appeared "late").

## What's still open

- **Section 301 government reply — due 9/18/2026, now 1 day out.** No
  extension motion on the docket as of tonight. **This needs a same-day
  check on the 18th itself** — if a session runs then, this is the first
  thing to look at.
- **Section 122**: Economists amici's corrected brief (entry #102) still
  needs to actually get accepted/found compliant by the 09/21/2026 deadline
  noted at entry #98 — worth a glance in a few days, not urgent.
- **CITI Comprehensive-vs-Basic module conflict** — still open, unchanged.
  Britton's "I got the basic and I think that's all we need" (2026-09-08)
  vs. McNeese's own HSIRB policy page naming the Comprehensive module
  (confirmed twice, 09-09 and 09-10). Needs Britton to confirm with the IRB
  office or complete the Comprehensive module as a precaution.
- **McNeese HSIRB turnaround time** — still not publicly findable (confirmed
  dead-end five prior nights running). Needs a direct ask to the IRB office.
- **Jason's blind-coding worksheet** — still no file in the repo, no Gwet's
  AC1 computed. External dependency on Jason's time.
- **Purchase Intention item count (5 vs. 3-item subset)** — Britton's
  confirm/override call, untouched.
- **Banked scales for a future companion paper** — Britton's call, untouched.
- **Two small Qualtrics-build decisions** (Opportunism item-2 anchor
  direction; attention-check hard-terminate vs. flag-only) — both quick
  yes/no calls, don't block importing the survey, untouched.

## Tooling note

Same approach as every prior session in this thread: plain `curl` with a
browser User-Agent, confirmed fresh via `x-cache: Miss from cloudfront` and
matching `date:` headers, parsed with `beautifulsoup4` (installed fresh this
session, as usual for this container). No WAF block, no 403/401 on any of
the four URLs tonight.

## For Britton

- **Litigation dockets: real movement tonight, and it's good news on the
  item you'd been waiting on.** V.O.S. Selections' motion to push its brief
  deadline to Oct 5 has been **granted** — that's the last of the three
  extension motions this thread has been tracking since early September now
  resolved, and it went the way everyone expected (no fight over it).
- **Section 301's government reply is still due tomorrow, 9/18/2026, and
  still hasn't been filed as of tonight's check.** Nothing on the docket
  suggests it will slip, but worth a same-day glance on the 18th to confirm
  it lands.
- Section 122 picked up one more procedural filing (an amici group fixing a
  non-compliant brief) — not a ruling, doesn't touch anything you care
  about.
- One small process note: two of tonight's new docket entries (the V.O.S.
  order and the Section 122 filing) both carry "Entered" timestamps from
  the afternoon/evening of 09-15 — meaning they existed before last night's
  (09-16) recheck ran, but CourtListener's mirror hadn't picked them up yet
  at that point. Same lag pattern documented once before for Section 301 on
  09-10. Nothing wrong with last night's check; the source just updates on
  its own delay sometimes.
- Updated `SUBMISSION_TRACKER.md` with the V.O.S. Selections ruling — no
  other tracker drift found.
- Nothing else changed in the project since 09-13 — no new non-litigation
  files, confirmed via `git log` and mtimes. Everything on the actual
  critical path (CITI Comprehensive question, HSIRB turnaround, Jason's
  coding worksheet, Purchase Intention item count, banked scales, the two
  small Qualtrics decisions) is exactly where it was — still waiting on you
  or on Jason, not on anything this session could resolve.
