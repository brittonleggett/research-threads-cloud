# 2026-09-18 — Aguilar complaint systematic address dedup, damages-figure attribution check,
# and a stale-tracking-item fix (TCEQ $3,750 fine)

AI-run background-agent research pass (Claude, via Claude Code). Read-only web research, direct
document fetches, and file maintenance in this project's own working files only — no design/
theory-chain decision made, nothing submitted or contacted externally, no git operations
performed (per this repo's standing convention), no file touched outside `SPACEX_LOUISIANA_PAPER/`.
Executes the priority order given: (1) systematic address-dedup pass on the *Aguilar v. SpaceX*
complaint to pin down the "53 homes" figure, (2) damages-figure attribution check (complaint vs.
attorney statement vs. other), (3) TCEQ $3,750 fine verification, all with time remaining.
Confirmed current state first by reading `CLAUDE.md`, the two most recent notes files
(2026-09-14, 2026-09-16), and the corpus/coding draft file — the state matched the task brief's
summary.

## 1. Aguilar v. SpaceX complaint — systematic address-dedup pass (PRIORITY ITEM)

### Re-fetching and tooling
Re-fetched the same complaint PDF fetched 09-16
(`https://storage.courtlistener.com/recap/gov.uscourts.txsd.2082161/gov.uscourts.txsd.2082161.1.0_1.pdf`,
`curl` with a browser User-Agent) — HTTP 200, 1,220,737 bytes, identical to the file size the
09-14/09-16 notes recorded, confirming this is the same document. `pypdf` was not installed this
session; hit the same recurring `_cffi_backend`/pyo3-panic import error other project notes have
flagged. The documented fix worked again: `pip install --force-reinstall --no-cache-dir cffi`,
then `pip install pypdf`. Extracted full text (59 pages, 91,605 characters) cleanly.

### Locating the actual plaintiff-address section
The 09-16 note's rough regex search for "owned a home at" / "owned homes at" had found ~46-52
address mentions but flagged it as a quick, non-systematic count. Tonight, rather than repeating
that approach, I located the section structurally: **Section V, "Starship's Acoustic Energy Caused
Actual Structural Damages" (complaint ¶¶94-252, pp. 30-55)** is a clean, repeating structure — a
plaintiff/household name as a header, followed by exactly three numbered paragraphs: (a) "At all
times relevant, [Plaintiff(s)] owned a home/homes at [address]," (b) the launch dates that damaged
that home (all eleven, identical list every time), (c) a boilerplate "suffered economic and
non-economic damages... to be determined at trial" sentence. This is a much better section to
parse than the earlier "PARTIES" section (¶¶5-93), which only states each plaintiff's *county* of
residence ("citizen of Texas residing in Cameron County, Texas") with **no street address at all**
— I confirmed this by reading that section directly; a naive keyword search across the whole
document (as the 09-16 note's regex effectively did) would pick up noise from both sections and
undercount, which is part of why the earlier estimate landed low.

### Method
Cleaned and joined Section V's text (stripped repeating "Case 1:26-cv-00485 ... Page NN of 59"
page-break lines and bare page-number lines), then used the paragraph numbering itself (¶94, ¶97,
¶100, ... every third paragraph starting at 94) to programmatically split the section into
individual ownership statements. This is a purely mechanical/reproducible parse, not a keyword
search — every one of the 53 "owned a home/homes at" paragraphs was extracted and read in full
(the complete list is in this note's companion working file; available on request, not
reproduced in full here to keep this note a reasonable length, but every entry was individually
read, not just counted).

### Findings — primary-document tier, fully reproducible
- **Exactly 53 named-plaintiff/household paragraph-groups** in Section V (¶94 to ¶250, every
  third paragraph — confirmed both by the paragraph-number arithmetic, (250-94)/3+1 = 53, and by
  literally counting the 53 name-headers).
- **These 53 groups sum to exactly 80 named plaintiffs** — verified by counting each group's
  named individuals (e.g., "Fernando and Blanca Aguirre" = 2, "Ellie Kloak, Jorge L. Moreno, and
  Josefina B. Moreno" = 3, "Jazmin Aguilar" = 1) and summing programmatically: **80**, exactly
  matching the already-confirmed 80-named-plaintiff count from the caption/parties section. This
  is a strong internal-consistency check that the parse is correct and complete.
- **But 6 of those 53 groups plead ownership of two separate street addresses, not one:**
  - ¶136, Michael and Martha Cooney: 114 Oleander Drive, Laguna Vista, TX AND 221 E. Adam Street,
    Port Isabel, TX 78578
  - ¶160, Richard Gaviria and Linda Rodriguez: 110 East Coronado Drive #104, South Padre Island,
    TX 78597 AND 6403 Padre Boulevard #76, South Padre Island, TX 78597
  - ¶214, Dionicio and Margaret Ortiz: 391 Sand Dollar, Port Isabel, TX 78578 AND 505 E Adams
    Street, Port Isabel, TX 78578
  - ¶229, Jeffrey Robertson: 105 W. Houston Street, Port Isabel, TX 78578-2507 AND 1506 TX-100
    #306, Port Isabel, TX 78578
  - ¶241, Vanessa and Timothy Tillman: 1323 Harbor Island Drive #138, Port Isabel, TX 78578 AND
    1440 Harbor Island Drive, Port Isabel, TX 78578
  - ¶217, Thelma Pena: one street address, but **two distinct condo units** — "125 E Cora Lee
    Drive, Apts. 101 and 301, South Padre Island, Texas 78597" (same building, two separately
    numbered units, plausibly two separately owned/rented properties, not one).
- **No exact-duplicate addresses across any of the 53 groups** — checked programmatically
  (case/punctuation-normalized string comparison across all extracted addresses); every pleaded
  address is distinct from every other.
- **Net result: the complaint's own text supports 58-59 distinct residential properties, not 53**
  — 59 if Pena's two condo units are counted as separate properties (defensible: they're
  separately numbered units, separately described as damaged), 58 if that one building is counted
  once. Either way, **meaningfully more than 53**.

### What "53 homes" in press coverage most likely is
This resolves the open question, not just narrows it. Texas Tribune's own May 1, 2026 article
(fetched directly tonight, see below) states: *"The plaintiffs own 53 homes in Laguna Vista, Port
Isabel and South Padre Island, including several couples who shared homes."* That phrasing —
"including several couples who shared homes" — is explaining the 80-plaintiffs-to-53-homes
collapse (multiple people per household), which is exactly what my paragraph-group count is: **53
is very likely a count of Section V's household/plaintiff-groups (correctly explaining why 80
plaintiffs isn't 80 homes), but it does not account for the reverse case — 6 of those "homes" are
actually two homes each.** MyRGV's headline ("Nearly 60 Valley households...") is a looser,
rounded version of the same 53-ish figure. Neither MyRGV nor Texas Tribune's fetched text shows
any indication the reporter parsed out the 6 multi-property groups; the likely explanation is a
paragraph/household count exactly matching mine (53), without noticing the "owned homes at:
a./b." and "owned homes at X and Y" constructions plead two addresses.

**Bottom line for item (1): "53 homes" is a real, explicit, and — as best I can determine —
correctly-derived figure for the number of household/plaintiff-groups in the complaint (matching
Texas Tribune's own explanation of it). But it is not the number of distinct properties pleaded;
the complaint's own text supports 58-59 distinct addresses. If a manuscript needs one precise
number, "53 plaintiff households" and "58-59 distinct properties" are both primary-document-
defensible, but they answer different questions, and press coverage has been using "53 homes" to
mean the former while it reads to a casual audience as the latter.** This is a genuine, reportable
finding, not just "still unconfirmed" — I'm confident in it because the entire 53-group,
80-plaintiff, 58-59-address structure is internally consistent and mechanically reproducible from
the document's own numbered-paragraph structure, not a heuristic keyword count.

One additional pleading-level curiosity worth flagging (not a research finding, just an accuracy
note if anyone cites individual addresses from this table): the complaint itself contains at
least one apparent internal typo — ¶148 (Hector H. Garcia and Maria Antonia Garcia) gives a South
Padre Island address with ZIP "76561," which doesn't match any other South Padre Island entry
(all others are 78597-series); this looks like a drafting typo in the original pleading (76561 is
a real Texas ZIP, but for Belton, TX, nowhere near South Padre Island), not an extraction error on
my end — I did not correct it, just flagging it.

## 2. Damages-figure attribution — $10M and "$100K foundation repair"

Continuing from the 09-16 note's finding that neither figure appears in the complaint itself, I
checked what the press articles that report these figures actually say about their own sourcing
(the specific ask: does the coverage attribute these to the complaint, to an attorney statement,
or something else).

**Texas Tribune** (`texastribune.org/2026/05/01/spacex-south-texas-home-damage-lawsuit/`, fetched
directly, HTTP 200) — the "53 homes... including several couples who shared homes" line above is
from this article. It does **not** mention any dollar figure at all — no $10M, no $100K. Its own
line on damages is limited to: "the loud blasts can cause damage to walls, windows and roofs of
homes," no dollar figures pleaded.

**TheNextWeb** and **Futurism** (`thenextweb.com/news/spacex-starbase-class-action-homes-damaged-
launches`, `futurism.com/space/elon-musk-rocket-spacex-destroying-homes`, both fetched directly) —
both report the "$100,000 foundation repair" figure, and **both attribute it explicitly to a named
(to the reporter, not to us) plaintiff's own on-record interview with Reuters**, not to the
complaint and not to an attorney's public statement. TheNextWeb: *"One plaintiff showed Reuters her
home in Port Isabel, less than six miles from Starbase... She estimates $100,000 in foundation
repairs, more than the home is currently worth."* Futurism: *"Altogether, the plaintiff claims it
will take some $100,000 to repair the home's foundation, which would exceed its current value,"*
describing the same Port Isabel homeowner's account (cabinets that don't sit evenly, doors that
won't close, warped flooring after a waterline burst during a launch). **Neither article names an
attorney or cites an attorney statement anywhere regarding damages** — no attorney is quoted by
name in either piece. **This corrects the 09-16 note's guess** that the $100K figure was likely
"attorney-statement-sourced" — it's actually **plaintiff-interview-sourced, via a Reuters report**
that TheNextWeb and Futurism both cite as their source (I could not locate the original Reuters
article itself in tonight's searches to read it directly — this finding rests on TheNextWeb's and
Futurism's own explicit "showed Reuters"/citation language, which is a reasonable secondary-source
basis for the attribution claim, but flagging that the Reuters original wasn't independently
re-read).

**RGV Business Journal** (`rgvbusinessjournal.com/news/01/05/2026/more-than-70-residents...`,
fetched directly) reports the ~$10M figure as its own unattributed narration: *"The plaintiffs are
seeking more than $10 million in damages and a jury trial..."* — no in-article citation to a court
filing, an attorney quote, or another outlet. **The $10 million figure's ultimate origin remains
unresolved** — it is not in the complaint (confirmed 09-16, re-confirmed by nothing contradicting
that tonight), and tonight's check did not turn up an attorney quote or press release that states
it either. It may be a reporter's own estimate/extrapolation, or may trace to a source not checked
tonight (a press release from plaintiffs' counsel that didn't surface in search, or the original
Reuters piece, which I did not manage to locate directly). Do not upgrade this figure's
attribution status beyond "unattributed news narration, not complaint-sourced" without further
work.

**A secondary, unplanned finding**: press headcounts for this case are inconsistent across
outlets, not just imprecise about "53" specifically — MyRGV/Texas Tribune say "53 homes," RGV
Business Journal says "more than 70 homeowners" (unclear where that number comes from; possibly
double-counting some plaintiffs' individual names, or its own rough estimate), and
TheNextWeb/Futurism/IBTimes UK say "80 residents/plaintiffs" (correct, matching the primary
document exactly). Worth keeping this outlet-inconsistency in mind if any of these headcounts gets
cited in manuscript text — only "80 plaintiffs" and "53 household-groups" are actually verifiable
against the primary document; "more than 70" appears to be its own thing, not independently
confirmed or explained by anything found tonight.

## 3. TCEQ $3,750 fine — found to be ALREADY resolved, a stale-tracking-item correction

Went looking for the TCEQ docket number to verify the $3,750 state fine (item 3 on tonight's
priority list, distinct from the $148,378 federal EPA CAFO penalty already in the corpus). A
search led to TCEQ's own Docket No. 2024-1282-IWD-E — and reading the project's own prior notes
(`grep`-ing for "1282-IWD" and "3,750" across the notes folder) showed **this was already
fully primary-verified on 2026-09-04** (see
`notes/2026-09-04-coalition-organizers-found-and-boca-chica-primary-docs-pulled.md`, section 3c):
the Agreed Order text was fetched and read directly, confirming the $3,750 total penalty ($750
deferred, $3,000 paid), the July 25-30, 2024 violation-documentation dates, the same
admission-avoidance boilerplate as the EPA CAFO, and a bonus find — an Oct. 1, 2024 public comment
from Save RGV/Carrizo-Comecrudo Nation/SOTXEJN/Clean Water Action calling the $3,750 penalty
"absurdly low."

**The problem**: this was never given its own row in `Study1_Corpus_and_Coding_DRAFT_2026-08-27.md`
— the "What's still needed" list's item 4 kept describing it as "still sourced only to news
coverage" through the 09-16 pass, two weeks after it had actually been primary-verified. This is
the same class of stale-tracking-item bug the 09-16 note fixed for row 7's Tier field (documented
in the corpus table there, discovered because a note existed but the table row wasn't updated to
match).

**Fixed tonight**: re-verified the TCEQ PDF URL still resolves (HTTP 200, 13,331,483 bytes,
matching the 09-04 note's file size exactly — same document, still live), added a new **row 19**
to the corpus table with the full citation and penalty detail, and corrected "What's still
needed" item 4 to note it was resolved 09-04, not still open. This is corpus-table maintenance
of the same kind explicitly authorized for this project (not a design/theory-chain decision).

## What this does not do

Does not pick a Study 1 corpus option, theory frame, or lock any design element — unchanged,
Britton's call per `CLAUDE.md`. Did not contact, submit, or post anything externally. Did not run
any git commands. Did not touch any file outside `SPACEX_LOUISIANA_PAPER/`.

## Still open / next steps

- The ~$10 million total-damages figure's ultimate source is still unresolved — not the complaint,
  not clearly an attorney statement or press release in what was checked tonight. A future session
  with time to spare could try to locate the original Reuters piece directly (search tonight
  didn't surface a `reuters.com` URL for this story specifically, only outlets that cite Reuters
  secondhand) — that would likely resolve both the $10M and $100K figures' origins in one document.
- Standing broader open items, unchanged from prior notes: primary-source verification of facts in
  `notes/2026-08-27-orientation.md`, further expansion of the Boca Chica comparison corpus, and
  literature-gap scouting. Not touched tonight — time went to the priority-ordered items above,
  which took the full session given the care the address-dedup pass required to do properly
  (programmatic, reproducible parsing rather than another quick keyword pass).
- No new literature-scouting work was done tonight.
