# 2026-09-04 — Litigation docket recheck: Section 122 states' response brief filed, Section 301 government response due today, Axle of Dearborn and V.O.S. Selections stable

Follow-up to `2026-09-03-fed-circuit-grant-bowman-withdrawal-1898-resolved-new-litigation-tracks.md`.
Checked CourtListener dockets directly (curl against courtlistener.com docket pages,
same technique as prior nightly passes) for the four items flagged for a pre-Sep-30
check, plus a general news scan. **No dramatic developments — mostly on-schedule
procedural progress — but two concrete new docket entries worth recording, and one
naming collision worth flagging clearly to Britton.**

## 1. V.O.S. Selections (26-1895, lead IEEPA refund-implementation appeal) — stable, no change

Re-fetched https://www.courtlistener.com/docket/73433096/vos-selections-inc-v-trump/
directly. **Still 24 docket entries total, same as the 09-03 note** (last entry is
the Sep 2 caption-revision entry already documented). No new filings, no response
brief, no oral argument scheduling. Nothing to update here.

## 2. Axle of Dearborn (de minimis, CIT 1:25-cv-00091) — stable, still not appealed

Re-fetched https://www.courtlistener.com/docket/70287201/axle-of-dearborn-inc-v-department-of-commerce/
directly. **Still 79 docket entries, same count as the 09-03 note.** No notice of
appeal has been filed. Per the 09-03 note's arithmetic (Slip Op. 26-94, Aug 13, 2026,
+60 days), the government's appeal window is now roughly **38 days remaining**
(~Oct 12, 2026 deadline) — this is the coordinator's arithmetic from the ruling date,
not a court-stated deadline, same caveat as before. No news of a filed appeal found
in a fresh search either.

## 3. Section 122 tariffs (State of Oregon v. Trump / Burlap and Barrel, CAFC 26-1804/-1805) — NEW: states' response brief filed Aug 31

The 09-03 note flagged that "appellee responses were due 'this week' as of Aug 26...
Docket entries themselves were not independently pulled today." Pulled them tonight
directly: https://www.courtlistener.com/docket/73318531/state-of-oregon-v-trump/
(80 entries as of today, up from whatever it was on 09-02/03).

Confirmed docket entries:
- **Entry #77 (Aug 31, 2026): RESPONSE BRIEF FILED** by the Oregon-led
  cross-appellant states (Oregon, Arizona, New York, Colorado, Connecticut, Delaware,
  Illinois, Kentucky, Maine, Maryland, Massachusetts, Michigan, Minnesota, Nevada,
  New Jersey, New Mexico, North Carolina, Pennsylvania, Rhode Island, Vermont,
  Virginia, Wisconsin) and appellees California and Washington. Flagged
  "PENDING COMPLIANCE REVIEW" as of filing.
- Entry #78 (Sep 1) / #80 (Sep 3): Basic Fun, Inc. and Burlap and Barrel, Inc. (the
  small-business appellees, represented by the Liberty Justice Center) filed a motion
  to extend their own brief deadline; the court's Sep 3 order found their submission
  **non-compliant** and set a corrected deadline of **09/11/2026**.
- Entry #79 (Sep 3): routine counsel-substitution motion for North Carolina, no
  substantive content.

**Net effect: the government-side (appellant) brief was already filed per the 09-03
note; the states' side (cross-appellant response) is now in too, on schedule. Only
the small-business appellees' corrected brief is still outstanding, now due Sep 11.**
No oral argument date found on this docket yet.

## 4. Section 301 forced-labor tariffs (In re Section 301 Forced Labor Cases, CIT) — government response due TODAY, not yet filed as of this check; a naming collision to flag

Pulled the master docket directly:
https://www.courtlistener.com/docket/74219533/in-re-section-301-forced-labor-cases/
(20 entries as of this check). Confirms the 09-03 note's summary and adds detail:

- Entry #16 (Aug 24, 2026): plaintiffs (Learning Resources et al., represented by
  Akin Gump) filed their motion for judgment on the agency record; docket text says
  **"Response to Dispositive Motion due by 9/4/2026"** — i.e., today. As of this
  check (still Sep 4), no government response has posted yet in the docket — expected
  later today or in the next day or two given normal filing-to-docket lag.
- Entry #17 (Aug 24): government filed its Answer to Complaint (master answer
  procedure) — not previously noted.
- Entries #18–20 (Sep 2–3): a consent protective order for confidential information
  was filed and granted — routine, no substantive signal either way.
- Reply brief (per the earlier TaxProf Blog secondary source) is still expected
  Sep 18, oral argument Sep 30, panel of Judges Choe-Groves, Reif, and Wang — all
  confirmed present on the docket page's party/judge metadata.

**New finding worth flagging clearly: there are now two different, unrelated cases
both captioned "State of Oregon v. Trump."** One is the Federal Circuit appeal of the
Section 122 CIT ruling (26-1804/-1805, discussed in §3 above — filed May 2026, an
appeal of a case decided in July 2026). The other is a **brand-new CIT complaint filed
Aug 3, 2026** by 25 Democratic state attorneys general (again led by Oregon) directly
challenging the Section 301 forced-labor tariffs under the APA — this is a *plaintiff*
case at the trial-court level, not an appeal, and it has been folded into the "In re
Section 301 Forced Labor Cases" consolidated proceeding alongside Learning Resources
and Burlap and Barrel/Collective Horology. Confirmed via CourtListener docket
73711779 ("the-state-of-oregon-v-donald-j-trump") and corroborated by a secondary
source (internationaltradeinsights.com, Aug 2026 post) describing the Aug 3 filing
and its APA claims (USTR "acted outside statutory authority," no individualized
negotiation, "pretextual investigation"). **If the manuscript or any note refers to
"State of Oregon v. Trump" for the Section 301 track, it needs a docket number or a
one-line disambiguator from the Section 122 case of the same name** — otherwise a
careful reader (or reviewer) could conflate two separate suits.

## Summary table

| Item | Status as of 09-04 |
|---|---|
| V.O.S. Selections (26-1895) | Stable, no new entries |
| Axle of Dearborn appeal | Stable, still not filed, ~38 days left |
| Section 122 (26-1804/-1805) | **Updated** — states' response brief filed Aug 31; small-business appellees' brief corrected deadline now Sep 11 |
| Section 301 forced-labor (In re Section 301 Forced Labor Cases) | Government's response to plaintiffs' dispositive motion due today (Sep 4); not yet docketed as of this check; oral argument Sep 30 confirmed on track |
| Section 301 — new state-AG suit | **New to project notes** — a second, separately-filed "State of Oregon v. Trump" (CIT, Aug 3, 2026) now consolidated into the Section 301 master docket — distinct from the Section 122 CAFC appeal of the same case name |

## Open items for Britton / next session

- Whether the manuscript's litigation framing distinguishes the two "State of Oregon
  v. Trump" cases if both are referenced — worth a quick check before this gets
  reused in a Discussion/Limitations section.
- Worth a follow-up check right around/after Sep 30 for the Section 301 oral argument
  outcome, and a check in the next few days for whether the government's Sep 4
  response to the dispositive motion has posted.
- Everything else here is informational, not blocking — consistent with the "no
  further action needed on the IRB thread this weekend" framing; this litigation
  tracking is corpus/background material, not on the critical path to submission.
