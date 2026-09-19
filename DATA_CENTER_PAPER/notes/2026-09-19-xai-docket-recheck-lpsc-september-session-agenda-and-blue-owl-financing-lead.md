# 2026-09-19 — xAI docket recheck (fresher "no ruling"), LPSC's September 16 B&E session agenda found (AEO settlement item), new Blue Owl Capital financing-risk lead surfaced

## What this is

Nightly follow-up to `2026-09-17-lpsc-aug12-primary-order-found-va-digital-gateway-date-conflict-resolved.md`,
which closed its two open items (LPSC's Aug 12 order, VA Digital Gateway dates) and left one explicit
thread open: the second, separate escalation on Docket U-37882 (Meta's/Entergy's Motion(s) for
Immediate Review of the ALJ's Aug 4, 2026 ruling) that LPSC counsel said was "not ripe" as of Aug 12
and was scheduled for the Commission's September Business & Executive (B&E) session. Tonight checked
that directly, rechecked the xAI/NAACP docket again, and (with time remaining) surfaced one genuinely
new corpus-worthy item — a Meta/Blue Owl Capital financing-risk story not previously logged in this
project's notes. No design/theme decisions were touched; this is verification and primary-source work
only, consistent with the locked design.

## 1. NAACP v. X.AI Corp. (3:26-cv-00074, N.D. Miss.) — still no new entry, RECAP mirror even fresher

Re-fetched the docket directly with `curl` (browser User-Agent) rather than trusting a search summary:

- **Highest docket entry: still 122** — read directly again (byte-identical text: DOJ's Sept. 8, 2026
  reply brief re the motion for a ruling on its intervention/dismissal motion). **No entry 123.**
- **Fetch confirmed fresh, not cached:** response header `x-cache: Miss from cloudfront` (same
  documented freshness check as prior nights).
- **RECAP "Last Updated" timestamp: Sept. 18, 2026, 10:42 a.m.** — this has moved forward again since
  09-17's reading of "Sept. 16, 2026, 4:59 p.m." That means a RECAP user pulled a fresh copy from
  PACER as recently as yesterday morning, and **that fresh pull still shows entry 122 as the highest
  entry.** This is now the strongest form of "no ruling yet" this project has recorded on this docket
  — the mirror is current to within about a day, not stale.
- No fresh WebSearch pass was needed tonight given the direct docket read already answers the
  question; a quick check for any September ruling/order news on the DOJ intervention/dismissal
  motion found nothing new.

**Bottom line for Britton: still no ruling in the xAI/NAACP case.** This is a real, current finding,
not a stale-mirror artifact.

## 2. LPSC Docket U-37882 — the September 16, 2026 B&E session agenda, found and read directly

The 09-17 note flagged that Meta's and Entergy's Motion(s) for Immediate Review of the ALJ's Aug 4
ruling had been referred to the Commissioners again on Aug 26, and were "not ripe," scheduled for the
September session, with no September date confirmed at the time.

**Found the session date and agenda tonight.** A WebFetch of the LPSC site confirmed the September B&E
session was held **September 16, 2026, 9:00 a.m., Galvez Building, 1st Floor Natchez Room, Baton
Rouge** — three days before tonight's check. The agenda PDF, guessed from the same filename pattern
documented on 09-17 (`https://lpsc.louisiana.gov/docs/agenda/Sept_16_2026_Agenda.pdf` — note: this
uses "Sept" where the August agenda used "Aug", so the naming convention isn't perfectly consistent
month to month; worth remembering for future date-guessing), returned a clean, directly-extractable
3-page PDF (`pdftotext -layout`, no OCR issues). **Ex. 9** of that agenda reads, verbatim:

> U-37882 - Entergy Louisiana, LLC, ex parte. In re: Application for certification of generation and
> transmission resources and for other relief.
>
> In re: Discussion and possible vote on Joint Motion of Entergy Louisiana, LLC, the Alliance for
> Affordable Energy, and Union of Concerned Scientists to vacate the August 6, 2026 Ruling, pursuant
> to Rule 57.
>
> In re: Discussion and possible vote on Motion for Immediate Review of Interlocutory Ruling.

**This confirms the item was real and was actually on the Commission's agenda that day** — not just a
projection from the Aug 12 transcript. Two things worth flagging precisely:

- **This is a different underlying ALJ ruling than the one covered on 09-15/09-17.** The Aug 12
  Commission vote (covered in the 09-15 and 09-17 notes) was about the **August 4, 2026** ALJ ruling
  that had *denied* Meta's Motion to Quash the subpoena — the Commission reversed that and vacated
  the subpoena outright. The item on tonight's September 16 agenda is about a **separate, August 6,
  2026** ALJ ruling. Per American Press (see below), that Aug 6 ruling was a *different* discovery
  dispute — Chief ALJ Melanie Verzwyvelt sided with the Alliance for Affordable Energy and Union of
  Concerned Scientists on an "Attorneys' Eyes Only" (AEO) confidentiality-access question, i.e., how
  much of Entergy's sensitive material intervenors' own experts and staff could see. Two days apart,
  two different rulings, two different subject matters (subpoena for Meta's underlying documents vs.
  AEO access to Entergy's own material) — worth keeping these straight in the manuscript; conflating
  "Aug 4" and "Aug 6" would be a real, avoidable error.
- **The item was already resolved by settlement before the vote, per direct news reporting
  (American Press, Sept. 11, 2026, "Entergy eases confidentiality restrictions in Meta power case"):**
  rather than let the Commission decide whether to uphold or overturn the Aug 6 ruling, **Entergy and
  the two consumer/environmental groups reached a settlement and jointly asked the Commission on
  September 4, 2026 to vacate the ruling.** Quoting the article directly: *"Rather than continue the
  fight, Entergy and the consumer groups reached a settlement and jointly asked the commission Sept.
  4 to vacate Verzwyvelt's ruling."* Under the stipulation, seven named representatives of the
  Alliance for Affordable Energy (including Executive Director Logan Burke) and the Union of
  Concerned Scientists get expanded access to material marked Attorneys' Eyes Only — they can review
  their own experts' full testimony, participate in discussions involving sensitive material, consult
  with attorneys about protected information, and inspect other documents at Entergy's New Orleans
  offices with 72 hours' notice. The Alliance was careful to draw the line on what this does *not*
  cover: *"This does not allow us to review Meta's documents related to our previous subpoena motion
  from last month"* — i.e., the settlement resolves the AEO-access dispute only, not the separate,
  already-decided (against the intervenors, Aug 12) subpoena fight over Meta's investment/job/
  power-demand figures.
- **Outcome of the September 16 vote itself: not yet confirmed from a primary document.** Unlike
  August 12, no LPSC minutes, agenda-with-vote-annotations, or transcript for September 16 have been
  posted yet as of tonight (checked several filename-pattern guesses for both `/docs/minutes/` and
  `/docs/transcripts/`, all 404). Given (a) this was a *joint* motion agreed by all the parties who'd
  actually litigated the underlying dispute, and (b) it's a discovery/confidentiality-access
  stipulation rather than a substantive ratemaking question, a Commission vote to approve it would be
  the unsurprising outcome — but that is an inference, not a confirmed fact, and should not be written
  into the manuscript as settled until the minutes/transcript are checked. **Flagging as the one open
  item to close out on a future pass:** once LPSC posts September 16 minutes/transcript (the August
  session's equivalent documents took roughly 3+ weeks to appear after the meeting date, based on this
  project's own history of finding the Aug 12 documents only on 09-17, five weeks out — so this may
  not be postable for some time yet).
- **Also on the same Ex. 9 agenda item, separately from the joint AEO motion:** a **"Motion for
  Immediate Review of Interlocutory Ruling"** with no ruling specified in the agenda language itself.
  Given the placement directly under the AEO joint-motion item and the procedural history in the 09-17
  note (Meta's/Entergy's own Motions for Immediate Review of the Aug 4 ruling were separately referred
  Aug 26), this could be a residual/protective motion kept on the docket in case the joint settlement
  motion doesn't fully resolve the underlying question — but the agenda text alone doesn't say which
  ruling this refers to, and nothing found tonight resolves that ambiguity. Not confident enough to
  characterize further; flagging as unresolved rather than guessing.

**Tooling note:** the LPSC portal's Kendo-grid JSON document-list API documented as working on 09-17
(`POST /portal/PSC/Docket_Documents` with `docketId`/`page`/`pageSize`) now returns a 500 error
("Value cannot be null. Parameter name: source") on every parameter combination tried tonight
(form-encoded, JSON body, with/without a session cookie from first loading the DocketDetails page,
with full Kendo pagination/sort parameters). Either the endpoint changed server-side or it needs a
session state this tool can't establish from a cookie alone. Not fixed tonight — flagging so a future
session doesn't assume it still works as documented, and doesn't re-burn time on it without a new
approach (e.g., checking whether the antiforgery/session requirement is discoverable another way).

## 3. New lead surfaced, not previously in this project's notes: Meta/Blue Owl Capital financing-risk story (Feb 2026)

With time remaining, a broader sweep for anything connecting to the corpus's existing
"corporate-opacity/regulatory-capture" theme surfaced a real, well-documented story that a check of
this project's notes (`grep`) confirms has never been logged here before: Meta's financing structure
for the Richland Parish buildout, and the LPSC's refusal to investigate it.

**The facts, cross-confirmed across multiple independent sources** (Union of Concerned Scientists —
ucs.org, Feb. 25, 2026; Alliance for Affordable Energy — all4energy.org; Earthjustice press release,
Feb. 25, 2026; Yahoo Finance/Reuters wire coverage):

- In October 2025, Meta closed a **$27 billion financing deal with Blue Owl Capital** for the Hyperion
  data-center campus — reported as the **largest private-credit transaction ever executed** at the
  time.
- The deal used a joint-venture holding company nicknamed **"Beignet."** Blue Owl contributed roughly
  $7 billion in cash to the JV; Meta received a one-time payout of about $3 billion and **retained
  only a 20% stake**, with Blue Owl holding the other 80%. Beignet then borrowed the $27 billion used
  to fund the data center build.
- **The structural risk intervenors flagged:** this arrangement is reported to let **Meta exit the
  project after as little as four years**, while the **three (or more) new gas plants built to power
  it have a ~30-year expected lifespan.** If the data center winds down or Meta exits well before the
  plants' useful life ends, intervenors argue the stranded-asset cost risk shifts to ratepayers, since
  the plants were approved as Entergy-owned, rate-based generation.
- Advocacy-group characterization, quoted directly from the Feb. 25, 2026 motion (via UCS.org):
  *"Meta sold off 80% of the data center to a venture debt company — a new tactic by Big Tech to avoid
  bearing these projects' great financial risks."* The Wall Street Journal is reported (via the same
  UCS piece) to have characterized the structure as **"Frankenstein financing."**
- **The LPSC's response:** on **February 25, 2026**, the Commission declined to open an investigation
  into the financing arrangement's ratepayer implications. None of the sources checked tonight name
  individual commissioners or give a vote tally for this specific declination — that remains
  unconfirmed, unlike the Aug 12 subpoena vote (3-1) or the April 15 procedural vote (4-1), both of
  which are recorded with named commissioners in primary LPSC orders. **Do not assume a vote count for
  this Feb. 25 item without further sourcing.**
- Advocacy quotes on the declination: Earthjustice's Susan Stevens Miller — *"When trillion-dollar
  tech companies like Meta make novel financing moves that allow them to walk away from a data center
  project earlier than reported — shifting even more of the long-term cost of fossil-fuel
  infrastructure onto ratepayers — regulators have a responsibility to take a hard look."* Alliance for
  Affordable Energy's Alaina DiLaura — *"This financing deal is not in the public interest ... the
  only ones benefiting from this risky financing scheme ... are Meta and Entergy Louisiana."* UCS's
  Paul Arbaje — the PSC "chose to prioritize a trillion dollar company over Louisianans already
  struggling with expensive, unreliable energy."

**Why this is worth adding to the corpus, and how it's distinct from what's already there:** the
project's existing Tier 1 material already documents (a) the subpoena fight over Meta's job/investment/
power-demand figures (denied by the Commission Aug 12) and (b) the AEO confidentiality dispute (item 2
above). This is a **third, distinct discovery/oversight thread** on the same underlying project — not
about what Meta discloses about its *operational* plans, but about the **financial structure of the
deal itself** and who bears the downside risk if Meta exits early. It's a clean, concrete instance of
the paper's "corporate opacity survives regulatory review" theme, with a specific, citable dollar
figure and mechanism (a 4-year exit option against a 30-year infrastructure commitment) rather than a
generic transparency complaint. **This is a February 2026 event, seven months old — it was simply never
logged in this project's `notes/` before now (confirmed via `grep -rli "Blue Owl\|Beignet\|MIDA" `
across the project directory), not a new development tonight.** Flagging it now so whoever next
touches the Tier 1 corpus/coding document can decide whether and how to fold it in — no corpus file
was edited tonight, per the design lock's guidance that Phase 3 coding decisions aren't this session's
call.

**One adjacent note, checked and ruled not new:** Utah's Executive Order 2026-03 (the "Data Center
Framework," signed May 29, 2026, directing state agencies to coordinate with — but not bind — the
Military Installation Development Authority on the Stratos Project) is already logged in this
project's `notes/2026-08-16-national-scan-beyond-louisiana.md` and in
`Study1_Corpus_and_Coding_DRAFT_2026-08-17_national-restructure.md`. A search tonight surfaced it
again as if new; checked against the project's own files before writing anything down, and it isn't.

## 4. Quick Tier 2 checks (Georgia, Utah) — no change

- **Georgia (Coweta County, "Project Sail"):** searched specifically for any September 2026 ruling on
  the residents' Superior Court suit (Bockrath v. Coweta County, filed ~May 2026). Found nothing dated
  after the original filing; the case appears to remain pending. **No change from 09-17.**
- **Utah (Bar H Ranch / Stratos):** searched specifically for any refiling of the withdrawn water-rights
  change applications (withdrawn May 5-7 and May 27, 2026). No refiling found as of tonight — most
  recent relevant coverage located is the May 31, 2026 piece on Executive Order 2026-03, which itself
  states no binding water applications were on file as of late May. **No change from 09-17's framing.**

## For Britton — plain summary

- **xAI/NAACP case: still no ruling**, and tonight's check is the freshest yet — the docket's own
  RECAP mirror was pulled from PACER as recently as yesterday morning and still shows nothing past
  entry 122.
- **The LPSC's September 16 session did take up the AEO confidentiality question**, and it did so as a
  **settlement**, not a contested vote: Entergy and the two consumer/environmental groups (Alliance for
  Affordable Energy, Union of Concerned Scientists) had already agreed by Sept. 4 to vacate the Aug. 6
  ALJ ruling and let those groups' representatives see more of Entergy's sensitive material — but this
  settlement is about a different ALJ ruling than the Aug. 12 subpoena vote (Aug. 6, not Aug. 4), and
  does **not** reopen or affect the Meta subpoena question that Meta already won on Aug. 12. I could not
  yet confirm from a primary LPSC document that the Commission actually voted to approve this
  settlement on Sept. 16 — the minutes/transcript for that date aren't posted yet. Worth a follow-up
  once they are.
- **A real find worth your attention for the corpus, even though it's not brand new:** Meta financed
  the Richland Parish buildout partly by selling 80% of a holding company ("Beignet") to Blue Owl
  Capital in a $27 billion deal, keeping only a 4-year exit option against gas plants built to run for
  30 years — and in February 2026 the LPSC declined to investigate the ratepayer risk this creates.
  This has been sitting in public reporting since February but was never logged in this project's
  notes before tonight. It's a clean, well-sourced addition to the "regulatory review doesn't catch
  corporate risk-shifting" theme, distinct from the subpoena and AEO-access threads already in the
  corpus.
- **One tooling regression to know about:** the LPSC portal's JSON document-list API that worked on
  09-17 is now erroring out (server-side 500) on every approach tried tonight — not fixed, flagged for
  whoever tries it next.
- No design/theme/Phase-3 decisions were made or attempted tonight — verification and primary-source
  work only, consistent with the locked multi-state design. No corpus file was edited; the Blue Owl
  lead and the AEO-settlement nuance are recorded here for whoever next updates the Tier 1 corpus/
  coding document.
- Per this task's instructions, no git commit/push was made — the orchestrating session handles that.
