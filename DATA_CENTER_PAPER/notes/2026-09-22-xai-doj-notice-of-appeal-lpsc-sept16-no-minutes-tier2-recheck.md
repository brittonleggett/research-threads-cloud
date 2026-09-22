# 2026-09-22 — DOJ files Notice of Appeal in NAACP v. X.AI (new docket entry 123), LPSC Sept 16 still unminuted, Tier 2/Blue Owl rechecks

## What this is

Nightly follow-up to `2026-09-19-xai-docket-recheck-lpsc-september-session-agenda-and-blue-owl-financing-lead.md`.
This project hadn't been touched since 09-19 (three nights). Re-checked the xAI/NAACP docket directly (this
time it moved — see below, the most significant finding in several weeks of these rechecks), rechecked LPSC's
site for September 16 minutes/transcript and any October agenda, did the requested quick Georgia/Utah Tier 2
recheck, and followed up specifically on the Meta/Blue Owl financing thread per this run's instructions (LPSC/
advocacy-group activity only, since Feb 25, 2026 — not a corpus fold-in decision, which stays Britton's/whoever
next does Phase 3 coding). No design/theme/Phase-3 decisions were touched tonight.

## 1. NAACP v. X.AI Corp. (3:26-cv-00074, N.D. Miss.) — genuinely new: DOJ filed a Notice of Appeal (Sept 18, 2026)

**Correction to how to find this docket:** re-fetched with the URL used in most prior notes
(`courtlistener.com/docket/73188848/national-association-for-the-advancement-of-colored-people-v-xai-corp/`).
A first attempt tonight used a *different*, wrong docket ID guessed from memory (69864448) and pulled up an
unrelated criminal case (*United States v. Acevedo-Rodriguez*) — caught immediately by checking the page's own
"Citation" field before treating anything in it as data, and discarded. Flagging only so a future session
double-checks the docket ID (73188848) rather than re-typing it from memory.

**Fetch freshness, confirmed the documented way:** `curl` with a browser User-Agent, response headers
`x-cache: Miss from cloudfront`, `date: Tue, 22 Sep 2026 05:08:53 GMT` — a live, uncached pull, not a stale
mirror. **RECAP "Last Updated": Sept. 21, 2026, 3:52 p.m.** — again more current than 09-19's Sept. 18 reading.

**The docket now has a new entry 123** (highest entry was 122 as of 09-19; confirmed no entries between 122 and
123 were missed — 113-122 all match what prior notes already had). Entry 123, filed **September 18, 2026**,
docketed as: *"NOTICE OF APPEAL by Andrew M. Darlington on behalf of United States of America."* Downloaded the
actual filed PDF directly from CourtListener's RECAP storage (`storage.courtlistener.com/recap/gov.uscourts.msnd.52261/gov.uscourts.msnd.52261.123.0.pdf`,
confirmed a real 2-page PDF, uploaded to RECAP Sept. 21, 2026, 3:24 p.m.) and read it directly — not a search
summary. Full text, quoted:

> Pursuant to Rule 3(c) of the Federal Rules of Appellate Procedure, the United States, acting on behalf of Lee
> M. Zeldin as Administrator of the U.S. Environmental Protection Agency (together, the "United States"), hereby
> appeal to the United States Court of Appeals for the Fifth Circuit from this Court's August 24, 2026,
> constructive Order denying the United States' amended motion for intervention and dismissal. Dkt. 116
> (transcript of constructive oral Order); Dkt. 114 (Aug. 24 minute entry); Dkt. 117, 118 (motion requesting
> written Order by Sept. 10); Dkt. 85 (amended motion to intervene); *see In re Fort Worth Chamber of Com.*, 100
> F.4th 528, 532 (5th Cir. 2024) ("district court's failure to timely rule" constituted "effective denial" and
> appealable order).

Signed by Andrew M. Darlington, DOJ Environmental and Natural Resources Division, dated September 18, 2026.

**Reconstructing the sequence that led here, from the docket's own entries (not inference from press):**
- **Aug 24, 2026** — telephonic status conference before Judge Debra M. Brown (entry 114, minute entry). Per the
  Notice of Appeal, the judge apparently ruled from the bench denying DOJ's amended motion to intervene/dismiss
  at or via this conference, but no separate written order was entered on the docket as its own numbered item.
- **Sept 2, 2026** — DOJ filed a motion (entries 117-118) asking the court to enter a **written** order by
  **September 10** specifically so the ruling would be cleanly appealable.
- **Sept 3, 2026** — NAACP/plaintiffs opposed that motion (entries 120-121).
- **Sept 8, 2026** — DOJ's reply (entry 122, the entry every prior note through 09-19 flagged as "highest, still
  no ruling").
- **No written order was ever entered** by Sept 10 or after (nothing between 122 and 123 fills that gap).
- **Sept 18, 2026** — rather than keep waiting, DOJ filed this Notice of Appeal, treating the Aug 24 oral ruling
  plus the court's failure to issue a written order as together constituting an appealable "constructive"
  denial, citing Fifth Circuit precedent (*In re Fort Worth Chamber of Commerce*) for that theory.

**This changes the "still no ruling" framing that every note since ~09-08 has carried.** There *was* an oral
ruling at the Aug 24 conference (denying DOJ's intervention/dismissal motion) — it just was never memorialized
as a standalone written order, which is why the docket's own numbered-entry sequence kept looking like nothing
had happened. DOJ is now asking the Fifth Circuit to review that denial. **No entry after 123** was found
tonight — nothing yet from the appellate docket, and the district court hasn't shown a stay of its own
proceedings (no "Date Terminated" field on the district docket; case remains open there). This is genuinely new
information as of tonight's check — not found in any earlier note (checked via `grep -rli "notice of appeal\|entry 123\|Fifth Circuit"`
across this project's `notes/`, no hits before tonight) and not yet in any news coverage found in a fresh
WebSearch tonight (searches for "NAACP xAI... notice of appeal Fifth Circuit September 2026" surfaced only
older, already-known DOJ-intervention coverage from June).

**One incidental correction worth logging:** the case caption on this filing reads *"NAACP and NAACP
Mississippi State Conference v. X.AI and MZX TECH LLC"* — a co-defendant, MZX Tech LLC, appears alongside X.AI
in the caption. Prior notes have referred to the case as "NAACP v. X.AI Corp." only; MZX Tech LLC isn't new to
the docket (an Aug 24 attorney-appearance entry, 113, also lists "MZX Tech LLC, X.AI Corp." together), but
worth remembering both defendants are named going forward.

## 2. LPSC Docket U-37882 — still no September 16 minutes/transcript; a "Revised" agenda exists but is textually identical; October agenda not yet posted

- **Directly re-tested every plausible filename** for September 16, 2026 minutes and transcript
  (`/docs/minutes/` and `/docs/transcripts/`, ~9 variants combined) — **all 404.** By contrast, the August 12,
  2026 minutes URL used in the 09-17 note (`August_12_2026_Minutes.pdf`) still returns HTTP 200, confirming the
  test methodology is sound and it's specifically September's minutes that aren't up yet, not a broken link
  pattern. **Six days out from the meeting is well inside the ~3-5 week posting lag prior notes documented for
  this Commission, so this is expected, not a red flag** — reporting it plainly per the task instructions rather
  than guessing at an outcome.
- **Found one new file not in the 09-19 note: `Sept_16_2026_Agenda_Revised.pdf`**, linked from the LPSC's
  `/Agenda` page. Downloaded and read it directly. **Its text is identical, word-for-word, to the original
  `Sept_16_2026_Agenda.pdf` already quoted in the 09-19 note** — same Ex. 9 language on the U-37882 AEO
  settlement/immediate-review-motion item, same structure throughout. Whatever prompted LPSC to post a
  "Revised" version isn't visible in the extracted text (could be a formatting/metadata fix invisible to text
  extraction); **this is not a substantive update and doesn't confirm or change anything about the vote outcome.**
  One caution for future passes: both the original and revised agenda PDFs render with certain commissioner
  names in bold next to some (not all) agenda items when read directly — checked carefully and this same
  pattern is present in *both* the pre-meeting original and the "revised" file, meaning it's very likely a
  template/rendering artifact of the source PDF, not a real "this commissioner sponsored/moved this item"
  signal. Not treating it as evidence of anything and flagging so a future session doesn't over-read it either.
- **No October 22, 2026 agenda found** — tried three filename patterns, all 404. The LPSC's own site lists
  October 22, 2026 (Louisiana Supreme Court building, New Orleans) as the next B&E session date on its public
  calendar, alongside November 18 and December 16, but that's just the annual meeting-date list, not a posted
  agenda; agendas for this Commission are typically posted much closer to the meeting, consistent with why
  September's was only found on 09-19 (three days after the Sept 16 meeting). **Bottom line: nothing to report
  yet either way on whether U-37882 will resurface on an October agenda** — worth checking again once October
  gets closer.

## 3. Tier 2 quick recheck — Georgia and Utah, no change

- **Georgia (Bockrath v. Coweta County Superior Court, "Project Sail"):** fresh WebSearch specifically for a
  September 2026 ruling. Nothing found past the original May 2026 filing coverage; the case still appears
  pending. **No change from 09-19.**
- **Utah (Bar H Ranch / Stratos water-rights applications):** fresh WebSearch specifically for a refiling.
  Search results still only show the original March 25, 2026 application and its May 5-7/May 27, 2026
  withdrawals, plus Bar H Ranch's stated intent to refile "in a timely manner." **No refiling found tonight —
  no change from 09-19.** (Note: this and the Georgia check above are WebSearch-based rechecks, same method
  prior notes used for this specific claim — not a direct database/court-docket pull; flagging that limitation
  plainly rather than overstating rigor.)

## 4. Arizona moratorium fight — no new development since 09-17

Fresh WebSearch for anything after Sept 9, 2026 (Gov. Hobbs' rejection of AG Mayes' moratorium call, already
logged in the 09-17 note). Nothing dated after Sept 9 found; the same azfamily.com/kjzz.org coverage from
Sept 3 and Sept 9 is still the most recent. **No change** — noted briefly per this run's "light Tier 2 check"
instruction, not a deep dive.

## 5. Blue Owl/Meta financing thread — one real correction to the 09-19 note, no new LPSC/advocacy activity since Feb 25

The 09-19 note characterized its quotes as pulled "directly from the Feb. 25, 2026 motion (via UCS.org)."
**This is imprecise and worth fixing before it goes anywhere near the manuscript.** Downloaded and read the
actual underlying motion directly (`all4energy.org/wp-content/uploads/2026/01/2026-01-14-U-37425-AAE-UCS-Mtn-
for-Investigation.pdf`, a real, text-extractable 18-page filing) — it is **dated January 14, 2026**, not
February 25, and filed in **Docket No. U-37425** (Entergy's original generation/transmission certification
docket), titled *"Motion for Investigation of the New Financial Arrangement of Meta Platforms, LLC Associated
with the Hyperion Data Center Project in Richland Parish, and Motion to Institute Prudence Review of Entergy
Louisiana, LLC."* February 25, 2026 is the date the **Commission declined** that motion, not when it was filed.
Separately, checked UCS.org directly for the specific pull-quote the 09-19 note attributed to "the motion" —
*"Meta sold off 80% of the data center to a venture debt company — a new tactic by Big Tech to avoid bearing
these projects' great financial risks"* — and confirmed it is **not** in the motion's own text; it's from UCS's
**February 25, 2026 press release** (`ucs.org/about/news/louisiana-wont-investigate-risky-meta-data-center-
financing`), issued the same day as the Commission's declination, commenting on it. **So: the motion is Jan 14;
the declination and the UCS quote are both Feb 25 — two different documents, easy to conflate if cited loosely.**
Worth keeping straight for whoever folds this into the corpus.

**On the specific question this run was asked to check — anything new from LPSC or the advocacy groups on this
thread since Feb 25, 2026 — the answer is no.** No reconsideration motion, appeal, or further LPSC docket action
on the investigation request was found; no further Earthjustice/AAE/UCS statements on this specific financing
thread past the Feb 25 press release were found in tonight's searches. One adjacent, **not independently
verified** data point surfaced by a search-result summary (measuredai.substack.com, not fetched/confirmed
directly tonight): a claim that "Meta's audited maximum exposure to loss on the JV stands at $45.99 billion as
of March 31, 2026," and that Meta announced a further project expansion past $50 billion total investment in
July 2026. **Flagging as an unverified lead only** — not confirmed against a primary source (e.g., an actual
Meta SEC filing) tonight, and not folded into anything; a future pass could verify the $45.99B figure directly
against Meta's 10-Q if it's worth pursuing.

## For Britton — plain summary

- **The single biggest thing tonight: the DOJ has filed a Notice of Appeal to the Fifth Circuit in the NAACP v.
  X.AI case**, filed September 18, 2026 and only showing up in the docket as of September 21. Read the actual
  2-page filing directly. It appeals from an August 24, 2026 hearing where the judge apparently ruled from the
  bench denying DOJ's motion to intervene and dismiss the case — but never put that ruling in writing, so DOJ
  is now asking the Fifth Circuit to treat the combination of the oral ruling and the court's silence since as
  an appealable "constructive" denial. This is the first real docket movement in this case that these nightly
  checks have found in weeks of "still no ruling" — worth flagging to anyone tracking this case, and worth a
  follow-up once the Fifth Circuit docket itself starts showing entries (not checked tonight — a next step).
- **LPSC's September 16 session still has no posted minutes or transcript** — checked every filename variant
  that's worked before, all still 404, six days out. That's within the normal 3-5 week lag this Commission has
  shown before, not a red flag. A "Revised" version of the September 16 agenda has been posted, but its content
  is word-for-word identical to the original already-read agenda, so it doesn't tell us anything new about
  whether the Commission actually voted to approve the AEO settlement. No agenda for the October 22 session
  (the next one) has been posted yet either.
- **Georgia and Utah: no change**, confirmed again with fresh searches. **Arizona: no change** since the
  governor-vs-AG story broke earlier in September.
- **One citation-precision fix for the Blue Owl/Meta financing lead flagged on 09-19:** the underlying
  advocacy-group motion was filed January 14, 2026 (not February 25) — February 25 is when the Commission
  turned it down, and that's also the date of the UCS press release the sharpest pull-quote actually comes from.
  Worth using the right date for the right document if this goes into the manuscript. No new LPSC or advocacy-
  group action on this specific thread has happened since the February 25 declination, as far as tonight's
  searches could find.
- No design/theme/Phase-3 decisions were made or attempted tonight — this is verification and primary-source
  work only, consistent with the locked multi-state design. No corpus file was edited.
- Per this task's instructions, no git commit/push was made — the orchestrating session handles that.
