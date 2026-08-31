# 2026-08-31 — V.O.S. Selections vs. Atmus Filtration "home case" question resolved via primary Federal Circuit docket + opening brief

Follow-up to the 2026-08-30 note's one flagged open loose end: which case is the actual "home
case" for the CBP liquidation/reliquidation order now on appeal at the Federal Circuit — *V.O.S.
Selections* (named in the Axle of Dearborn CIT opinion's footnote 12) or *Atmus Filtration*
(named in a cluster of law-firm secondary sources). **This is now resolved at primary-source
confidence.** Short answer: both names were partially right, for different reasons, and the
full picture is more precise than either source alone suggested. Neither the 2026-08-29 nor
2026-08-30 notes' summary was wrong — they just hadn't seen the actual docket/briefing yet.

## Tooling note (new working method for this project)

CourtListener's own docket HTML pages (`courtlistener.com/docket/...`) return a 403 to both
plain `curl` and WebFetch (Cloudflare/WAF-blocked, consistent with the 2026-08-30 note's
experience on `cit.uscourts.gov`). But **CourtListener's REST search API
(`courtlistener.com/api/rest/v4/search/?q=...&type=r`) works with plain, unauthenticated
`curl`** — the 2026-08-30 note's "CourtListener returned a CloudFront 403 on every query
attempted" was evidently either a different endpoint or a since-fixed/transient block; the
search API worked cleanly tonight on multiple queries. It returns full docket metadata
(parties, docket number, court, filing date, RECAP document list) as JSON. The single-docket
detail endpoint (`/api/rest/v4/dockets/{id}/`) does require auth (401), but the search endpoint
does not.

Even better: search results for cases with RECAP-archived filings include a `recap_documents`
array with **direct links to the actual PDF filings on CourtListener's public storage CDN**
(`storage.courtlistener.com/recap/gov.uscourts.<court>.<case>/...pdf`), which download cleanly
with plain `curl` — no WAF, no auth, no WebFetch workaround needed. These are real PACER
documents (federal court filings), uploaded to RECAP's public archive, and downloading a
government litigant's or agency's brief this way is not a paywall/copyright issue — it's a
public court record. `pdftotext -layout` (via `apt-get install poppler-utils`, not preinstalled
in this environment) extracts clean, accurately-paginated text from these. This is now a
confirmed pattern: **search the CourtListener API for a case name → find the docket_id and any
recap_documents entries → download the PDF from the storage CDN directly → pdftotext it.** Much
higher signal than the WebFetch-summarize-then-save-then-Read workaround used previously, when
it's available (RECAP coverage isn't universal — it depends on someone having PACER-purchased
and uploaded the document, so this won't always work).

## What was found

**Primary source: DOJ's Opening Brief for Appellants, filed 2026-08-10 in the U.S. Court of
Appeals for the Federal Circuit, Nos. 2026-1895, -1897, -1899 (consolidated).** Downloaded
directly from CourtListener's RECAP archive
(`storage.courtlistener.com/recap/gov.uscourts.cafc.24456/gov.uscourts.cafc.24456.19.0.pdf`,
717KB, 54 pages of substantive brief text, read in full via `pdftotext`). This is the actual
government appellate brief, not a secondary summary.

**The caption resolves the case-name question directly.** The consolidated appeal covers three
Federal Circuit docket numbers, corresponding to three underlying CIT plaintiffs, confirmed both
by the brief's own cover caption and independently cross-checked against CourtListener's docket
search (separate query per case name, each returning the matching CAFC docket number):

| Fed. Cir. No. | Case | CIT case no. |
|---|---|---|
| 26-1895 | **V.O.S. Selections, Inc. v. Trump** | 1:25-cv-00066 |
| 26-1897 | AGS Company Automotive Solutions v. CBP | 1:25-cv-00255 |
| 26-1899 | Grant & Bowman, Inc. v. CBP | (in the CIT list, see below) |
| 26-1898 *(dismissed, not in the "1895, -1897, -1899" caption)* | Euro-Notions Florida, Inc. v. CBP | 1:25-cv-00595 |

**Atmus Filtration, Inc. v. United States is not one of the three live appeals** — confirmed by
direct CourtListener search for "Atmus Filtration" restricted to the Federal Circuit court
(`court=cafc`), which returns zero CAFC dockets where Atmus is a party. Atmus only appears
*inside the text* of filings in other CAFC cases (i.e., cited as procedural history in the
opening brief above, and in a few unrelated CAFC filings that happen to mention it).

**The actual procedural history, straight from the brief (pp. 10-19 of the PDF), resolves why
both names appeared in different sources:**

1. **Atmus Filtration, Inc. v. United States** (CIT No. 26-1259, filed Feb. 27, 2026, assigned to
   Judge Richard K. Eaton) was the *first* case in this chain. Atmus sought a TRO to suspend
   liquidation of its own entries; the government didn't contest CIT authority to order
   reliquidation and the parties stipulated to that, so Atmus withdrew its TRO motion. Judge
   Eaton nonetheless proceeded, rejected the withdrawal, and — declaring himself "the only judge
   who [would] hear cases pertaining to the refund of IEEPA duties" — sua sponte entered a
   **universal injunction** (not limited to Atmus, not even requested by Atmus) ordering CBP to
   liquidate/reliquidate *any* importer's IEEPA-tariffed entries without regard to the duties.
   Orders and amendments in this case are dated March 4, March 6, March 16, March 20, March 27,
   and April 1, 2026 — this is exactly the case and date cluster the law-firm secondary sources
   (Greenberg Traurig, Forvis Mazars, etc.) were describing, and they were correct about it.
   **On April 6, 2026, Atmus voluntarily dismissed its own case** (CIT order dismissing it entered
   April 8). Atmus was never appealed — it no longer existed as a live case by the time any notice
   of appeal could be filed.
2. **Euro-Notions Florida, Inc. v. CBP** (CIT No. 25-595) was the next case Judge Eaton picked,
   the day after Atmus dismissed. He sua sponte lifted its stay and imposed the same universal
   injunction template, again without any motion from the plaintiff.
3. The CIT then extended the same sua sponte template to three more cases via a series of
   off-the-record conferences: **V.O.S. Selections, Inc. v. Trump** (the original SCOTUS case,
   CIT No. 25-66 — its plaintiffs had actually asked for a narrower, non-universal remedy, which
   the CIT denied without explanation before entering the same universal injunction instead),
   **AGS Company Automotive Solutions v. CBP**, and **Grant & Bowman, Inc. v. CBP**.
4. **All four injunctions (Euro-Notions, V.O.S. Selections, AGS, Grant & Bowman) were entered
   April 17, 2026** and separately noticed for appeal June 2, 2026 — this is the exact date the
   Axle of Dearborn slip opinion's footnote 12 cited for "the V.O.S. Selections order," now
   independently confirmed word-for-word by the government's own brief ("The CIT entered
   universal injunctions on April 17, 2026").
5. **All four appeals were consolidated at the Federal Circuit** as Nos. 26-1895 (V.O.S.
   Selections), -1897 (AGS), -1898 (Euro-Notions), -1899 (Grant & Bowman) — the "four appeals of
   identical Orders Directing Liquidation" the Axle opinion referenced. **Euro-Notions (26-1898)
   was then voluntarily dismissed as moot** on July 16, 2026 (its underlying CIT case was
   voluntarily dismissed, which automatically dissolved its injunction), leaving the three live,
   currently-pending appeals: **Nos. 2026-1895, -1897, -1899** — exactly the caption on the
   opening brief that answers this question.

**Bottom line for the manuscript/notes:** *V.O.S. Selections, Inc. v. Trump* is a correct and
precise name for the (lead-listed) case whose liquidation/reliquidation order is now on appeal
at the Federal Circuit (No. 26-1895, part of the 26-1895/-1897/-1899 consolidated group,
currently at the opening-brief stage as of Aug 10, 2026 — no Federal Circuit decision yet).
*Atmus Filtration* is also a correct name, but for a different, earlier role: it's the
originating case where Judge Eaton's universal-injunction template was first created (and later
copied into the other cases) — Atmus itself was voluntarily dismissed in April 2026 before any
appeal existed, so it is not part of what's now pending at the Federal Circuit. If the manuscript
ever needs to name "the case on appeal," V.O.S. Selections (or, for full precision, "V.O.S.
Selections, AGS Company Automotive Solutions, and Grant & Bowman, Fed. Cir. Nos. 26-1895/-1897/
-1899, consolidated") is the accurate citation. If it needs to describe where the injunction
*originated*, Atmus Filtration is the accurate citation. Using either name alone without this
distinction risks a citation-precision error; using both together, correctly scoped, is fully
supportable now.

**Bonus finding, upgraded from B-tier to A-tier:** the 2026-08-30 note flagged the "CAPE" refund-
processing system name as "WebSearch/law-firm-sourced only." This brief confirms it directly and
repeatedly, including citing a CBP CSMS bulletin exhibit titled "Consolidated Administration and
Processing of Entries (CAPE) for IEEPA Refunds" (dated April 20, 2026) and describing an April 20
CAPE launch and a June 29, 2026 CAPE functionality expansion. The "suspended... as to immediate
compliance" characterization is also confirmed directly (the CIT "suspended" its order "to the
extent that it directs immediate compliance" after CBP filed a declaration explaining its
systems couldn't comply immediately — Atmus Filtration, Inc. v. United States, 2026 WL 661636
(Ct. Int'l Trade Mar. 6, 2026)).

**One more relevant fact this brief surfaces, useful context for the refund-wave corpus
discussion (not a decision — just flagging, per standing instruction not to touch that
corpus-scope call):** the CIT has separately entered a different, narrower "importer-specific"
injunction (not on appeal, not contested by the government) in "hundreds of refund cases" as of
an August 5, 2026 status conference — see *In re Tariffs Collected in Reliance on Int'l
Emergency Econ. Powers Act (IEEPA)*, 2026 WL 2199714 (Ct. Int'l Trade July 20, 2026). This is
different from, and narrower than, the universal injunctions under appeal. Worth knowing if the
refund-wave section ever needs the current procedural landscape, but not a call for this note to
make.

## Confidence and what remains genuinely unconfirmed

**A-tier, primary-source confirmed tonight:**
- The three live Federal Circuit appeal numbers and their case names (26-1895 V.O.S. Selections,
  26-1897 AGS, 26-1899 Grant & Bowman), cross-checked two independent ways (the brief's own
  caption, and separate CourtListener docket-name searches for each).
- Euro-Notions (26-1898) was the fourth original appeal, voluntarily dismissed as moot in July
  2026 — explains the "four appeals" language in secondary sources cleanly.
- Atmus Filtration is not, and was never, part of any Federal Circuit appeal — confirmed by a
  direct court-scoped search returning zero results.
- The full procedural chain (Atmus → Euro-Notions → V.O.S. Selections/AGS/Grant & Bowman), all
  dates, and the April 17, 2026 injunction-entry date, are drawn directly from the government's
  own appellate brief, itself citing specific CIT docket entries by number for each assertion.

**Not independently verified tonight (brief is one side's characterization):**
- This is the *government's* opening brief, arguing the injunctions should be vacated — its
  characterization of the CIT's conduct (e.g., "without explanation," "sua sponte and without
  notice") is the appellant's framing, not a neutral court finding. The underlying CIT orders
  themselves weren't independently pulled and read tonight (time-boxed to resolving the
  case-identity question); if this procedural narrative ever needs to go into the manuscript in
  more depth than "which case is on appeal," it would be worth reading Judge Eaton's own orders
  directly rather than relying solely on the government's brief.
- No opposition/response brief from the plaintiffs-appellees was located or read — only the
  government's opening brief was in RECAP. The other side's account of the same events may frame
  things differently (this is normal in adversarial briefing, not a red flag).
- Not resolved and out of scope tonight: any Federal Circuit decision on the merits (none exists
  yet — opening brief only, filed Aug 10, 2026).

## Untouched per standing instructions

Did not touch the refund-wave corpus-scope decision or the Insteel freight/profit quote — both
remain Britton's calls, not approached tonight.

---

## For Britton

1. **The V.O.S. Selections / Atmus Filtration discrepancy flagged on 2026-08-30 is resolved.**
   Both names are accurate, for different roles: V.O.S. Selections (Fed. Cir. No. 26-1895, part
   of the consolidated 26-1895/-1897/-1899 appeal) is the case actually on appeal now; Atmus
   Filtration is the case that originated the injunction template in March 2026 but was
   voluntarily dismissed in April before any appeal existed. If you cite "the case on appeal,"
   use V.O.S. Selections (or name all three: V.O.S. Selections, AGS, Grant & Bowman). If you cite
   "where this started," Atmus Filtration is right.
2. No Federal Circuit ruling exists yet on this consolidated appeal — opening brief only, filed
   Aug 10, 2026. Not something the manuscript can characterize as decided.
3. Found (and verified against a manuscript-content check tonight) that no current manuscript
   draft file mentions "de minimis" at all — the 2026-08-30 note's flag about updating manuscript
   text for the resolved de minimis status turns out to be a non-issue: there's nothing in the
   drafts to update yet, since that section hasn't been written into the current draft files. Only
   the `notes/` files discussed de minimis, and the 2026-08-30 note already updated the working
   understanding there. Worth keeping in mind when the discussion/legal-background section
   actually gets drafted.
