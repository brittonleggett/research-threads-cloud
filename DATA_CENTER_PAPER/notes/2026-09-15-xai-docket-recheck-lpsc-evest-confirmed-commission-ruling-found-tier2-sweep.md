# 2026-09-15 — xAI docket recheck (still no change), LPSC follow-ups closed out (Evest LLC confirmed, Commission's Aug 12 subpoena ruling found), Tier 2 national sweep

## What this is

Nightly follow-up to `2026-09-13-xai-ruling-recheck.md`, which left three things open:
(1) the NAACP v. X.AI Corp. docket, still sitting at entry 122 with a stale CourtListener
mirror; (2) independent confirmation of the "Evest LLC" entity name read (garbled) out of
the LPSC subpoena-referral PDF; (3) whether the full LPSC Commission has since ruled on
the subpoena question the ALJ referred up on July 31, 2026. All three are addressed below,
plus a Tier 2 national sweep (Georgia, Utah, Virginia, Arizona, Clinton County IN) since
real time remained after items 1-2.

## 1. NAACP v. X.AI Corp. (3:26-cv-00074, N.D. Miss.) — still no change

Re-fetched the docket directly (`curl` with a browser User-Agent, the documented
workaround — same tooling as the last three nights) rather than trusting a search
summary:

- **Highest docket entry: still 122** — read it again to confirm it's the identical
  filing (DOJ's Sept. 8, 2026 reply brief re the motion for a ruling on its
  intervention/dismissal motion), not a renumbered one. **Entry 123 does not exist**
  (checked directly with a string search on the fetched HTML).
- **RECAP "Last Updated" timestamp: Sept. 11, 2026, 2:57 p.m.** — byte-identical to the
  value recorded on 09-12 and 09-13. This is now the fourth consecutive night this
  mirror hasn't refreshed, so CourtListener's own copy is now running roughly four days
  stale relative to live PACER. Same caveat as the last two notes: this field reflects
  when a RECAP user last pulled the docket from PACER, not the live PACER state, and
  this tool has no PACER credentials to check further.
- **Fresh WebSearch cross-check tonight** for any September ruling, order, or news
  coverage of a decision on the DOJ intervention/dismissal motion turned up nothing
  dated after the already-known events (June 12 PI denial, Aug 24 evidentiary hearing).
  No outlet reports a ruling.

**Bottom line for Britton: no change, fourth night in a row.** The case is genuinely
quiet as far as any tool here can tell — that's a legitimate finding, not a gap in the
check. If the Dec-16-type "the case has been dormant for X weeks" framing shows up in
drafting, this is solid grounds for it, with the standing caveat about the stale RECAP
mirror noted honestly rather than glossed over.

## 2a. "Evest LLC" — CONFIRMED, independently, from two primary LPSC documents

The 09-13 note flagged this because the only read at the time came from a
badly-encoded `pdftotext` extraction of the subpoena-referral order. Tonight, pulled two
different LPSC documents directly from the LPSC's own portal and got clean text from
both:

- **Order No. U-37882** (the Commission's own procedural order, decided at the April 15,
  2026 Business & Executive Session, signed May 14, 2026) — cleanly extracted text
  reads: *"Entergy Louisiana LLC ('ELL' or the 'Company') filed its application seeking
  certification of generation and transmission resources needed to serve a substantial
  new load proposed for **Evest LLC**, a customer seeking to locate a large hyperscale
  data center in Richland Parish, adjacent to the facility currently being developed by
  Laidley, LLC."*
- **Ruling on Motion to Quash Subpoena** (Chief ALJ, dated August 4, 2026 — see 2b below)
  — cleanly extracted text again reads: *"...to serve Meta's wholly-owned subsidiary,
  **Evest LLC** ('Evest' or 'Customer'), and its large hyperscale data center that will
  be located in Richland Parish, Louisiana, adjacent to the facility previously approved
  in Commission Order No. U-37425 for Meta subsidiary, Laidley LLC."*
- Independently corroborated by an unaffiliated news source: The Lens (New Orleans),
  "Enforceable guarantees or pinky promises? A closer look at Meta's deal with Entergy
  Louisiana," refers to this second Richland Parish expansion as **"Project Evest"**
  throughout.

**This closes the open item — "Evest LLC" is a real, confirmed Meta subsidiary name, not
an OCR artifact, safe to use in the corpus now.** Two independent, clean, primary LPSC
filings plus a news source all agree. Worth noting for the corpus: Meta now has *two*
named shell entities in this docket family — **Laidley LLC** (the earlier-approved
Hyperion-adjacent phase, Order U-37425) and **Evest LLC** (this second/expansion phase,
U-37882) — both housed at the same Richland Parish site.

**Small correction to the 09-13 note:** that note's garbled `pdftotext` read named the
Chief ALJ "Melanie Boyvelt." The clean read from the August 4 ruling gives her actual
name as **Melanie Verzwyvelt** (matching an independent news source's spelling too) —
"Boyvelt" was indeed an OCR/font-encoding artifact, not a real alternate name. Flagging
so nothing downstream cites the wrong name.

## 2b. Full Commission's ruling on the referred subpoena question — FOUND (via news; primary order not yet located)

**Short answer: yes, the full Commission ruled on August 12, 2026, and it went against
the intervenors** — the Commission rejected the ALJ's recommendation, meaning Meta does
not have to turn over the requested job-creation, investment, and power-demand
documents.

What was pulled together tonight, and how confident each piece is:

- **August 4, 2026 — ALJ ruling, direct primary-source read (clean `pdftotext`, 23
  pages):** Chief ALJ Melanie Verzwyvelt denied Meta's Motion to Quash Subpoena (filed
  July 15, 2026), on the grounds that Meta's own affidavit "did not contain any
  extra-record evidence" to support its objection. The same order confirms the earlier
  procedural sequence: the ALJ's original Subpoena Ruling was not reconsidered on
  remand, and Meta's separate Motion for Immediate Review "was forwarded to the
  Commission for consideration" — i.e., this is the direct paper trail from the July 31
  referral (read on 09-13) to the Commission-level review.
- **August 12, 2026 — full Commission vote, found via two independent Louisiana news
  outlets, not yet independently confirmed against the primary order text:**
  - WRKF (Louisiana Public Radio): the Commission voted **3-1** to reject the ALJ's
    recommendation that would have compelled Meta to turn over the information.
    Commissioner **Davante Lewis** (District 3) was the lone dissent, quoted: *"We have
    found a way ... to find every excuse to not do something when it favors Entergy and
    Meta"* while finding exceptions to rules that benefit them. Earthjustice attorney
    Susan Stevens Miller is quoted: *"The PSC ultimately voted to let Meta off the
    hook."*
  - American Press independently confirms the docket number (U-37882) and the broader
    dispute status, and adds a **September 11, 2026** update: Entergy and the
    intervenor groups (Alliance for Affordable Energy, Union of Concerned Scientists)
    jointly asked the Commission to ease (not resolve) a *separate* "Attorneys' Eyes
    Only" confidentiality dispute — this is about intervenors' own experts getting
    broader access to Entergy's material, **not** a reopening of the Meta subpoena
    question. The Alliance is quoted directly stating the agreement "does not allow us
    to review Meta's documents related to our previous subpoena motion" — those
    documents were never produced and remain inaccessible. The underlying Application
    itself is set for Commission consideration at the **December 16, 2026** Business &
    Executive Session (this date is independently confirmed by the April 15, 2026
    primary order read above, which set that same date).
- **What tonight did NOT get:** the actual August 12, 2026 Commission order/transcript
  as a primary document. Searched the LPSC portal directly (document-details page,
  direct file-ID guesses based on nearby search hits) and could not locate it — the
  portal's document search isn't reachable in a simple, scriptable way from here. So the
  **3-1 vote count and the Lewis/Miller quotes rest on two independent news outlets, not
  yet a primary LPSC filing** — solid secondary sourcing (Louisiana Public Radio and a
  regional daily, both citing specifics like the exact date and a dissenting
  commissioner by name, not vague paraphrase), but if this goes into the manuscript as a
  quoted vote count, pull the actual LPSC order first. Flagging as the one open item
  from tonight's LPSC work.

**Why this matters for the paper:** this closes the loop on the corporate-secrecy/
discovery-fight data point flagged 09-13 — it's not just that intervenors *tried* to
get Meta's internal documents and were partly denied at the ALJ level; the full,
Commission-level appeal of that denial also failed, 3-1, with a state-appointed elected
commissioner going on record calling it favoritism toward the company. That is a
stronger, more citable version of the "corporate opacity survives regulatory review"
theme than what was in hand on 09-13.

## 3. Tier 2 national sweep — Georgia, Utah, Virginia, Arizona, Clinton County IN

Real time remained after items 1-2, so a targeted sweep for developments since the last
checks (mostly early-to-mid September 2026 window).

- **Georgia (Coweta County, "Project Sail," $17B Atlas Development campus):** no new
  September development found. The residents' Superior Court suit (filed ~May 2026,
  challenging the rezoning as inconsistent with the county's Rural Places Comprehensive
  Plan designation and a wetlands-review procedural gap) appears to still be pending; no
  ruling or hearing news surfaced tonight. **No change.**
- **Utah (Stratos Project, Box Elder County, near Great Salt Lake):** no new litigation
  event found, but two early-September opinion/feature pieces (Christian Science
  Monitor, Sept. 1) add a concrete corpus-worthy detail not previously logged: **more
  than 3,800 Utahns paid the $15 filing fee to formally object** to the project's water
  rights transfer application — a specific, citable scale-of-opposition figure. The
  HB60 water-rights law limiting how much weight broad-impact objections get (already
  in the corpus) is the same law these objections are being filed under. No ruling yet
  on the water-rights transfer itself as far as tonight's search found.
- **Virginia (Prince William County "Digital Gateway"):** found **conflicting dates**
  across sources for the same underlying ruling — tonight's search summarized "March
  2026 Court of Appeals" and "July 2026 developer withdrew its appeal," while a prior
  note in this project's own corpus (09-05) flagged the same ruling as dated **August 7,
  2025** from an earlier search. This is exactly the kind of date confusion this project
  has been burned by before (see item below on Clinton County) — **not resolving it
  tonight, flagging it as open**. Whoever next touches the VA case should pull the
  actual Virginia Court of Appeals opinion or docket directly rather than trusting
  either search summary.
- **Arizona (AG Kris Mayes' data-center moratorium call):** this lead was already in the
  corpus as of 09-08 (Mayes' Aug. 31 call for a legislative pause, tied to the Menlo
  Digital/Ahwatukee project and a ~450% Phoenix-area water-demand projection). Tonight
  found it's getting sustained, broader press pickup through mid-September
  (Arizona Mirror, Western Water, Grist) — not new information, but confirms it's a
  real, ongoing story rather than a one-day press release. **One genuinely new,
  corpus-worthy item:** a September 11, 2026 Cronkite News (ASU) piece features water
  researchers pushing back on the "data centers are causing the Colorado River cuts"
  framing directly — quoted experts say data centers aren't the primary driver of the
  shortage, while still acknowledging they "are definitely capable of making the
  problem ... much worse if they aren't sustainably managed." This is a legitimate
  negative/complicating case for the water-scarcity framing theme (transferability
  testing is exactly what Tier 2 is supposed to do per the design lock) — worth keeping
  in mind for Phase 3 so the AZ water-framing story doesn't get flattened into a
  one-sided narrative.
- **Clinton County, IN — checked carefully, genuinely no new development, and a search
  artifact caught before it became a false finding:** A WebSearch surfaced an article
  titled "Area Plan Commission Sends 'No Recommendation' on Data Center to Clinton
  County Commissioners," which read at first glance like a fresh September 2026 event
  (a new, smaller 152.92-acre Logix Realty petition, separate from the 714.55-acre
  "Data One" proposal the Commissioners denied in January 2026). **Checked the page's
  own `datePublished` metadata directly rather than trusting the search snippet's
  implied recency: the article is dated September 2, 2025 — a full year old,** an
  earlier, separate Logix Realty rezoning attempt that predates the whole "Data One"
  saga already in the corpus. Confirmed via a second, independent source (Indiana
  Economic Digest) that the January 2026 denial **bars the petitioner from refiling for
  12 months** — meaning no new Clinton County filing is realistically expected before
  around January 2027 anyway, which is consistent with finding nothing new tonight.
  **No change — flagging the near-miss here as a process note:** search results can
  surface stale articles that read as current; always check raw publish-date metadata
  before treating something as a "new" development, same lesson this project's already
  learned once with fabricated case numbers.

## For Britton — plain summary

- **xAI case: still nothing. Fourth night in a row it's quiet at entry 122**, and
  CourtListener's mirror of the docket is now about four days stale. That's just the
  honest state of it — no ruling has come down as far as any tool here can see.
- **The "Evest LLC" name from the 09-13 note is confirmed real** — pulled it cleanly
  from two different LPSC filings tonight, not just the garbled read from before. Safe
  to use now. Also: Meta has two named shell entities on this site — Laidley LLC (the
  earlier-approved phase) and Evest LLC (this second, larger phase).
- **Found the answer to the other 09-13 open question: yes, the full Commission ruled
  on the Meta subpoena fight, on August 12, 2026, and it went against the environmental
  intervenors, 3-1** — Meta doesn't have to hand over the job/investment/power-demand
  documents. One Commissioner (Davante Lewis) dissented and said on the record it looked
  like favoritism toward Entergy and Meta. I got this from two solid Louisiana news
  outlets, not yet from the Commission's own order text (couldn't locate that file on
  the LPSC portal tonight) — worth pulling the primary order before this goes into a
  manuscript with a quoted vote count.
- **National sweep:** nothing dramatic moved in Georgia or Clinton County. Arizona's AG
  moratorium story is still developing and picking up press, plus a useful pushback
  piece complicating the water-blame narrative. Utah has a striking new number (3,800+
  formal objections filed). Virginia has a genuine date conflict across sources on its
  key ruling that needs a primary-source check, not something I could safely resolve
  tonight.
- **One thing to know about tonight's process, not a finding about the case:** a search
  result made it look like there was a brand-new Clinton County development this month.
  It wasn't — it was a year-old article. Checked the page's own metadata before writing
  anything down, so nothing wrong went into the corpus, but flagging it because it's the
  kind of trap that could produce a bad citation if a future session trusts a search
  snippet's apparent recency without checking.
- No design/theme decisions touched — this is verification and primary-source work
  only, consistent with the design lock. No corpus files were edited; findings are
  recorded here for whoever next updates the Tier 1/Tier 2 corpus.
- Per this task's instructions, no git commit/push was made — the orchestrating session
  handles that.
