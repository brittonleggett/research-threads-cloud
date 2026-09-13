# 2026-09-13 — NAACP v. xAI docket recheck (still pending, entry 122 unchanged) + LPSC U-37882 subpoena order finally read

## What this is
Nightly follow-up to the two most recent xAI-docket checks (`2026-09-10-tier1-louisiana-
primary-source-pull-and-xai-ruling-recheck.md` and `2026-09-12-xai-ruling-recheck-and-
clinton-county-date.md`), which both found the docket topped out at entry 122 (DOJ's
Sept. 8 reply brief) with no ruling. Also picked up the standing open item from
`2026-09-10-tier1-pdf-ocr-attempt-and-legislature-bill-count-check.md`: the LPSC
U-37882 subpoena-referral order PDF that two prior sessions downloaded but couldn't
get read (media-budget and tooling issues, not a real access block).

## 1. NAACP v. X.AI Corp. (3:26-cv-00074, N.D. Miss.) — still no ruling as of this snapshot

**Tooling note:** WebFetch was not tried directly this time — went straight to the
documented workaround (`curl` with a browser User-Agent header) since the last two
notes already established WebFetch 403s on this URL. That curl succeeded cleanly
(HTTP 200, ~917KB of real HTML, not a block/CAPTCHA page):

```
curl -L -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 ... Chrome/128.0.0.0 Safari/537.36" \
  "https://www.courtlistener.com/docket/73188848/national-association-for-the-advancement-of-colored-people-v-xai-corp/"
```

Read directly from the fetched page (parsed the actual HTML, not a search snippet):

- **Case:** National Association for the Advancement of Colored People v. X.AI Corp.,
  3:26-cv-00074 (N.D. Miss.).
- **Assigned to:** Debra Marie Brown — unchanged.
- **Date of Last Known Filing: Sept. 8, 2026** — unchanged from the 09-10 and 09-12 notes.
- **RECAP "Last Updated" metadata: Sept. 11, 2026, 2:57 p.m.** — this is byte-identical
  to the timestamp the 09-12 note recorded. That means no RECAP user has pulled a fresh
  copy of this docket from PACER since that Sept. 11 snapshot — i.e., **CourtListener's
  copy has not refreshed in the ~40 hours since the last check**, not that nothing has
  happened in the case. CourtListener's own tooltip on this field explicitly warns it
  reflects "when a RECAP user last downloaded the docket from PACER," not the live
  PACER state, and that "View on PACER" (which requires a PACER login this session
  doesn't have) is the authoritative version.
- **Highest docket entry number present: still 122**, same entry as both prior nights —
  read it directly again to confirm it's the identical filing, not a re-numbered one:
  "REPLY to Response to Motion re 117 MOTION For Entry of Written Order No Later Than
  September 10 on the United States Amended Motion to Intervene and Dismiss re 85
  Amended MOTION to Intervene MOTION to Dismiss filed by United States of America,"
  uploaded Sept. 8, 2026, 1:54 p.m. — same PDF, same filer (Darlington, Andrew), same
  everything as the 09-10 and 09-12 reads. **No entry 123 exists.**

**Cross-checked against fresh WebSearch (not docket-based) tonight:** searched for
any September ruling, order, or news coverage of a decision on the DOJ intervention/
dismissal motion. Found nothing dated after the already-known June 12, 2026 order
(denying NAACP's preliminary-injunction motion without prejudice) and the already-known
Aug. 24, 2026 evidentiary hearing (both already in the corpus from earlier notes). No
outlet — legal press, Memphis/Mississippi local news, or otherwise — reports a September
ruling on the intervention/dismissal motion.

**Conclusion, at the appropriate confidence level:** as of this snapshot (docket "Last
Updated" Sept. 11, 2026, 2:57 p.m., checked directly on Sept. 13, 2026), **no ruling on
DOJ's motion to intervene/dismiss has been entered** — the docket still tops out at
entry 122 (DOJ's Sept. 8 reply), and no independent news source reports otherwise. This
is a primary-source docket read, not search synthesis, but carries the same caveat as
the last two nights: CourtListener's RECAP mirror can lag the live PACER docket, and
since it hasn't refreshed at all since Sept. 11 this time, that lag window is a bit
wider than usual. This does not mean something landed in that window — just that this
tool can't rule it out with certainty. A direct PACER check (which this environment has
no credentials for) would be the only way to close that gap completely.

**Bottom line for Britton: still pending, no change from the last two nights' findings.**

## 2. LPSC Docket U-37882 subpoena-referral order — read successfully this time (prior tooling gap resolved)

Two prior sessions (2026-09-09 and 2026-09-10 notes) downloaded this PDF from the
LPSC's own portal but never got its text: the Read tool hit a "media removed: request
limit" error both times. Re-downloaded it fresh tonight from the same URL
(`https://lpscpubvalence.lpsc.louisiana.gov/portal/PSC/ViewFile?fileId=XUggTpCKCj4%3D`,
19.3MB, confirmed real PDF v1.7) and hit the **same** "media removed: request limit"
wall on the Read tool immediately — so this is evidently a harder budget limit than
last time's notes assumed, not something that clears by going first. Worked around it
with a different tool path instead of Read: installed `poppler-utils` and ran
`pdftotext -layout` directly on the file. That produced garbled-but-legible text (lots
of OCR-style ligature corruption — e.g. "³$SSOLFDWLRQ´" for what is clearly the word
"Application" — this PDF's embedded font/encoding is unusual, not a real OCR scan), but
the substantive content comes through clearly enough to read and quote reliably. Also
discovered via `pdfinfo` that the file is **103 pages**, not the "1 page" a prior
session's `file` command reported — that earlier page count was simply wrong.

**What the document actually is:** a July 31, 2026 order from Chief ALJ Melanie
Boyvelt (LPSC Administrative Hearings Division), docket U-37882 (Entergy Louisiana,
LLC, Ex Parte — the application to add generation/transmission for Meta's Richland
Parish data center). It refers an interlocutory subpoena ruling up to the full
Commission for review, and attaches the underlying filings. Reading it directly (not
a summary) surfaces several facts not previously in this project's notes:

- **ELL's application (filed ~March 26, 2026) seeks approval to add 5,278 MW of
  generation**, plus battery storage and transmission, to serve Meta's data-center
  buildout — a specific figure not previously pulled from a primary document (prior
  notes had only the "10 new gas plants" figure from news coverage). Note: the
  document names the customer entity as an LLC that the garbled text renders as
  "Evest LLC" — this could be a real, distinct shell-company name for this second/
  expansion phase (the corpus already has "Laidley LLC" as the shell for the earlier-
  approved Order No. U-37425 phase), or could itself be a font/encoding artifact.
  **Flagging, not asserting** — this specific entity name needs a second read (ideally
  from a cleaner text source or the LPSC's own docket index) before it goes in the
  corpus as a confirmed fact.
- **Discovery dispute:** On June 29, 2026, intervenor NGOs (Alliance for Affordable
  Energy and Union of Concerned Scientists) moved to subpoena Meta (a non-party)
  for documents. The ALJ's July 10, 2026 ruling granted requests for (1) investment/
  job-creation evidence and (2) load-demand evidence, but **denied** requests for
  (3) load-factor/variability detail, (4) any communications between Meta and Entergy
  about the "Sustainability Agreement" as a factor in Meta's siting decision, and
  (5) information on Meta's assets/guaranty obligations.
- **Meta's response:** Meta made a limited non-party appearance specifically to fight
  the subpoena — filing a Motion for Stay, a Motion for Immediate Review, and a Motion
  to Quash. The stay was granted; the underlying ruling was referred to the full
  Commission (which is what this document is).
- **Commission Staff's stated rationale for the denied requests** (read directly from
  the attached Subpoena Ruling, not just the referral cover order): on request 3,
  Staff argued ELL had already provided load-factor data and the NGOs' request wasn't
  narrowly enough tailored; on request 4, Staff argued the Sustainability Agreement
  itself (not internal deliberations about it) already discloses the commitment, and
  ELL had pointed to a "73-page report that is publicly available" as sufficient; on
  request 5, Staff argued Meta's financial information is already public via SEC
  filings and credit ratings, and that subpoenaing Meta directly would "harass and
  inconvenience" it without adding probative value.

**Why this matters for the paper:** this is a genuine primary-source data point for
the corporate-opacity/secrecy theme already in the Tier 1 corpus — a real regulatory
discovery fight where NGO intervenors tried and partly failed to get Meta's own
sustainability-commitment communications and financial detail into the record, with
the state's own Commission Staff arguing existing public disclosures (a "73-page
report," SEC filings, credit ratings) were sufficient. That's a concrete, quotable
instance of the "corporate secrecy vs. what's actually disclosed" dynamic, not just a
generic claim about it.

**What's still open on this document:** only skimmed enough to extract the facts
above — did not read all 103 pages (the attached exhibits include the full ALJ
Subpoena Ruling, Meta's Motion for Immediate Review, the NGOs' opposition, and
Commission Staff's memorandum, each likely 10-20+ pages). The "Evest LLC" entity name
needs independent confirmation before use. The ultimate outcome — how the full
Commission ruled on the referred subpoena question — is not in this document (it's
the referral itself, dated July 31, 2026); a follow-up docket check for the
Commission's actual disposition would be useful if this becomes a corpus artifact.
The extracted text is saved at
`/tmp/claude-0/.../scratchpad/lpsc_order.txt` (session-scratchpad only, not part of
this repo) for whoever picks this up next — full text is much longer than what's
excerpted above.

## For Britton — plain summary

- **xAI/NAACP case: no change, still pending.** Checked the actual docket again
  tonight (not a search summary) — still tops out at entry 122 (DOJ's Sept. 8 reply
  brief), no order or ruling has been entered on the DOJ intervention/dismissal
  motion. One wrinkle worth knowing: CourtListener's own copy of this docket hasn't
  refreshed since Sept. 11, so this check has a slightly wider blind-spot window than
  the last one — can't fully rule out something happening between Sept. 11 and now. A
  fresh news search found nothing suggesting a ruling has come down, though.
- **LPSC subpoena order (U-37882): finally read it, real content.** Two prior nights
  downloaded this PDF but couldn't extract its text; tonight a different tool
  (`pdftotext` instead of the Read tool, which hit the same wall again) got real,
  legible content out of it. It documents a discovery fight where environmental
  intervenors tried to subpoena Meta for internal communications and financial
  detail, and were partly turned down — the state's regulatory staff argued existing
  public disclosures were good enough. Useful, quotable material for the
  transparency/secrecy angle of the paper. One fact (a subsidiary LLC name) needs a
  second look before treating it as confirmed — flagged in the note above so it
  doesn't get used prematurely.
- No design/theme decisions touched — this is verification/primary-source work only,
  consistent with the paper's design-lock. No corpus files were edited; findings are
  recorded here for whoever next updates the corpus.
- Per this task's instructions, no git commit/push was made — the working tree just
  has this new file.
